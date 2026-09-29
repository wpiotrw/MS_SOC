#!/usr/bin/env node

// Mirrors a Microsoft Learn docset into a git working tree, one file per page.
//
// Learn serves every page as Markdown when it is asked for `text/markdown`, and
// the page's front matter records the file it was built from (`source_path`).
// That is enough to rebuild the shape of a documentation repository from the
// public site alone, so a git repository can go on recording how the docs change
// after the repository they were written in stops being public.
//
// A run is incremental. Every page is revalidated with the ETag the previous run
// saw, so an unchanged page costs a 304 and no body, and a run that finds
// nothing new leaves the working tree untouched — there is nothing to commit.
//
// Usage, from the root of the mirror repository:
//   node learn-mirror.js [--config=learn-mirror.config.json] [--full]
//                        [--limit=N] [--message-file=path] [--allow-mass-delete]
//                        [--seed-urls=file] [--max-minutes=N]
//
// A page, once found, stays in the mirror until Learn answers 404 for it or
// redirects it to another page. The sitemaps are how pages are found, not how
// they are lost: Learn leaves some live pages out of them, and a page that
// drops out of a sitemap is usually still there.
//
// Learn rations requests per client, and far more tightly for cloud addresses
// (a GitHub runner) than for a home connection: a runner can be held to a few
// hundred requests every few minutes, and a sitemap's lastmod is the author's
// ms.date rather than when the page last changed, so there is no cheaper signal
// to check first. So a run paces itself, halving its rate on a 429, and with
// --max-minutes stops starting requests once its time is up. Pages it did not
// reach keep what they had; the next run starts where this one stopped, after
// re-checking the pages that match `priority`.

const fs = require('fs');
const path = require('path');

const DEFAULTS = {
  sitemapIndex: 'https://learn.microsoft.com/_sitemaps/sitemapindex.xml',
  // Learn's sitemaps leave out some live pages. A docset's toc.json lists most
  // of those, and extraUrls names the rest.
  tocs: [],
  extraUrls: [],
  // Repositories a page's `original_content_git_url` may name, as owner/repo.
  // Learn paths are shared between repositories (a docset can publish under
  // azure/, which another repository also fills), so a page's source_path alone
  // does not say it belongs to this mirror. Empty accepts any repository.
  sourceRepos: [],
  exclude: [],
  stateFile: '.learn-mirror/state.json',
  // Pages no sitemap or TOC lists, one URL per line, read on every run when the
  // file exists. Seed it from the original repository's tree while that is
  // still public.
  seedUrlsFile: '.learn-mirror/seed-urls.txt',
  concurrency: 6,
  // Requests per second at most. A 429 halves the working rate; it recovers
  // one step at a time as requests succeed.
  maxRequestsPerSecond: 8,
  // Pages checked first on every run, whatever the rotation reached — the
  // what's-new pages a reader expects to be current.
  priority: null,
  timeoutMs: 30000,
  retries: 6,
  // Keys Learn rewrites on every publish whether or not the page changed. They
  // are kept in the state file instead, so a republish is not a diff.
  stripFrontMatter: ['updated_at', 'git_commit_id', 'gitcommit', 'word_count'],
  userAgent: 'learn-mirror/1.0 (+https://github.com/merill/learn-mirror)',
  // A run that would delete more than this share of the mirror is refused: a
  // sitemap that comes back truncated must not empty the repository.
  maxDeleteRatio: 0.1
};

function loadMirrorConfig(file) {
  const raw = JSON.parse(fs.readFileSync(file, 'utf8'));
  const config = { ...DEFAULTS, ...raw };
  for (const key of ['sitemaps', 'include', 'trackedPaths']) {
    if (typeof config[key] !== 'string') throw new Error(`${file}: '${key}' must be a regular expression string`);
  }
  return {
    ...config,
    sitemaps: new RegExp(config.sitemaps),
    include: new RegExp(config.include),
    exclude: [].concat(config.exclude).map(pattern => new RegExp(pattern)),
    trackedPaths: new RegExp(config.trackedPaths),
    priority: config.priority ? new RegExp(config.priority) : null
  };
}

function decodeXml(value) {
  return value
    .replace(/&lt;/g, '<').replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"').replace(/&apos;/g, "'")
    .replace(/&amp;/g, '&');
}

// Every <loc> in a sitemap or sitemap index. Learn's sitemaps also carry
// hreflang alternates, which are <xhtml:link> elements and not matched here.
function parseSitemapLocs(xml) {
  return [...xml.matchAll(/<loc>\s*([^<]+?)\s*<\/loc>/g)].map(match => decodeXml(match[1]));
}

// Every page a toc.json links to, resolved against the TOC's own URL. Links out
// of Learn are dropped here; links into other docsets fall to `include`.
function parseTocHrefs(toc, tocUrl) {
  const base = new URL(tocUrl);
  const hrefs = [];
  const walk = items => {
    for (const item of items || []) {
      if (typeof item.href === 'string' && item.href) {
        const url = new URL(item.href, base);
        if (url.host === base.host && !url.pathname.endsWith('.json')) {
          url.hash = '';
          url.search = '';
          hrefs.push(url.href);
        }
      }
      walk(item.children);
    }
  };
  walk(toc.items);
  return hrefs;
}

function selectPageUrls(urls, config) {
  const selected = urls.filter(url => config.include.test(url) && !config.exclude.some(re => re.test(url)));
  return [...new Set(selected)].sort();
}

function splitFrontMatter(text) {
  const match = /^---\r?\n([\s\S]*?)\r?\n---\r?\n?/.exec(text);
  if (!match) return { frontMatter: '', body: text };
  return { frontMatter: match[1], body: text.slice(match[0].length) };
}

// A top-level scalar from Learn's front matter. Learn writes it flat — one key
// per line, lists indented beneath — so a full YAML parser is not needed.
function frontMatterValue(frontMatter, key) {
  const escaped = key.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const match = new RegExp(`^${escaped}:[ \\t]*(.*)$`, 'm').exec(frontMatter);
  if (!match) return null;
  const value = match[1].trim().replace(/^(['"])(.*)\1$/, '$2');
  return value === '' ? null : value;
}

// Removes top-level keys, and any indented or list lines beneath them.
function stripFrontMatterKeys(text, keys) {
  const { frontMatter, body } = splitFrontMatter(text);
  if (!frontMatter) return text;
  const drop = new Set(keys);
  const kept = [];
  let skipping = false;
  for (const line of frontMatter.split(/\r?\n/)) {
    const key = /^([^\s:#-][^:]*):/.exec(line);
    if (key) skipping = drop.has(key[1]);
    else if (!/^(\s|-)/.test(line)) skipping = false;
    if (!skipping) kept.push(line);
  }
  return `---\n${kept.join('\n')}\n---\n${body}`;
}

// Where a page lives in the mirror. Learn's landing pages are built from YAML,
// but what Learn serves for them is Markdown, and the monitor reads `.md` files.
function mirrorPathFor(sourcePath) {
  const normalized = path.posix.normalize(sourcePath.replace(/\\/g, '/'));
  if (normalized.startsWith('/') || normalized.startsWith('..') || normalized.includes('/../')) {
    throw new Error(`refusing source_path outside the mirror: ${sourcePath}`);
  }
  return normalized.replace(/\.(md|ya?ml)$/i, '') + '.md';
}

function readState(file) {
  try {
    const state = JSON.parse(fs.readFileSync(file, 'utf8'));
    return { cursor: state.cursor || null, pages: state.pages || {} };
  } catch (error) {
    if (error.code === 'ENOENT') return { cursor: null, pages: {} };
    throw error;
  }
}

// One page per line, sorted, so the state file's own history reads as a log of
// which pages changed and when.
function serializeState(state) {
  const urls = Object.keys(state.pages).sort();
  const lines = urls.map((url, index) =>
    `    ${JSON.stringify(url)}: ${JSON.stringify(sortKeys(state.pages[url]))}${index < urls.length - 1 ? ',' : ''}`
  );
  const cursor = state.cursor ? `  "cursor": ${JSON.stringify(state.cursor)},\n` : '';
  return `{\n  "version": 1,\n${cursor}  "pages": {\n${lines.join('\n')}\n  }\n}\n`;
}

function sortKeys(object) {
  return Object.fromEntries(Object.entries(object).filter(([, v]) => v !== undefined && v !== null).sort(([a], [b]) => a.localeCompare(b)));
}

const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

// Learn throttles per client, not per request, so pacing is shared by every
// worker: requests leave one slot apart, a 429 halves the rate and pauses
// everyone, and each run of successes earns one step back.
const pace = { rate: DEFAULTS.maxRequestsPerSecond, max: DEFAULTS.maxRequestsPerSecond, next: 0, streak: 0, pausedUntil: 0, throttled: 0 };

function setPace(maxRequestsPerSecond) {
  Object.assign(pace, { rate: maxRequestsPerSecond, max: maxRequestsPerSecond, next: 0, streak: 0, pausedUntil: 0, throttled: 0 });
}

async function takeSlot() {
  for (;;) {
    const now = Date.now();
    const at = Math.max(now, pace.next, pace.pausedUntil);
    if (at > now) {
      await sleep(at - now);
      continue;
    }
    pace.next = now + 1000 / pace.rate;
    return;
  }
}

function paceSucceeded() {
  if (++pace.streak >= 50 && pace.rate < pace.max) {
    pace.rate = Math.min(pace.max, pace.rate + 1);
    pace.streak = 0;
  }
}

function paceThrottled(retryAfter, attempt) {
  pace.streak = 0;
  const pause = retryAfter > 0 ? Math.min(retryAfter, 120) * 1000 : Math.min(60000, 5000 * 2 ** attempt);
  if (Date.now() + pause <= pace.pausedUntil) return;
  pace.pausedUntil = Date.now() + pause;
  pace.rate = Math.max(0.5, pace.rate / 2);
  pace.throttled++;
  console.log(`  ⏸️  Learn is throttling (HTTP 429${retryAfter > 0 ? `, Retry-After ${retryAfter}s` : ''}); pausing ${Math.round(pause / 1000)}s, then ${pace.rate} request(s)/s`);
}

async function fetchWithRetry(url, headers, config) {
  let lastError;
  for (let attempt = 0; attempt <= config.retries; attempt++) {
    if (attempt > 0) await sleep(Math.min(30000, 1000 * 2 ** attempt) + Math.random() * 500);
    await takeSlot();
    try {
      const response = await fetch(url, { headers, redirect: 'follow', signal: AbortSignal.timeout(config.timeoutMs) });
      if (response.status === 429 || response.status >= 500) {
        lastError = new Error(`HTTP ${response.status}`);
        if (response.status === 429) paceThrottled(Number(response.headers.get('retry-after')), attempt);
        await response.body?.cancel();
        continue;
      }
      paceSucceeded();
      return response;
    } catch (error) {
      lastError = error;
    }
  }
  throw lastError;
}

async function fetchText(url, config) {
  const response = await fetchWithRetry(url, { 'User-Agent': config.userAgent }, config);
  if (!response.ok) throw new Error(`${url}: HTTP ${response.status}`);
  return response.text();
}

async function discoverPages(config) {
  const sitemapUrls = parseSitemapLocs(await fetchText(config.sitemapIndex, config)).filter(url => config.sitemaps.test(url));
  if (sitemapUrls.length === 0) throw new Error(`no sitemap in ${config.sitemapIndex} matches ${config.sitemaps}`);
  const pages = [];
  for (const sitemap of sitemapUrls) {
    const locs = parseSitemapLocs(await fetchText(sitemap, config));
    if (locs.length === 0) throw new Error(`${sitemap} listed no pages`);
    pages.push(...locs);
  }
  for (const toc of config.tocs) {
    const hrefs = parseTocHrefs(JSON.parse(await fetchText(toc, config)), toc);
    if (hrefs.length === 0) throw new Error(`${toc} listed no pages`);
    pages.push(...hrefs);
  }
  pages.push(...config.extraUrls);
  return { sitemapUrls, pageUrls: selectPageUrls(pages, config) };
}

// Revalidates one page. Never throws: a failure is a result, and the page keeps
// what the previous run recorded for it.
async function fetchPage(url, previous, root, config, full) {
  const headers = { Accept: 'text/markdown', 'User-Agent': config.userAgent };
  // An ETag is only worth sending when the file it vouches for is still there.
  const haveFile = previous?.path
    ? fs.existsSync(path.join(root, previous.path))
    : Boolean(previous?.untracked || previous?.aliasOf);
  if (!full && previous?.etag && haveFile) headers['If-None-Match'] = previous.etag;

  let response;
  try {
    response = await fetchWithRetry(url, headers, config);
  } catch (error) {
    return { url, kind: 'error', error: error.message };
  }
  if (response.status === 304) return { url, kind: 'unchanged' };
  if (response.status === 404 || response.status === 410) {
    await response.body?.cancel();
    return { url, kind: 'gone' };
  }
  const type = response.headers.get('content-type') || '';
  if (!response.ok || !type.startsWith('text/markdown')) {
    await response.body?.cancel();
    return { url, kind: 'error', error: `HTTP ${response.status} ${type}` };
  }

  const text = await response.text();
  const { frontMatter } = splitFrontMatter(text);
  const sourcePath = frontMatterValue(frontMatter, 'source_path');
  const entry = {
    etag: response.headers.get('etag') || undefined,
    sourcePath: sourcePath || undefined,
    updatedAt: frontMatterValue(frontMatter, 'updated_at') || undefined,
    gitCommitId: frontMatterValue(frontMatter, 'git_commit_id') || undefined,
    redirectedTo: response.url !== url ? response.url : undefined
  };
  if (!sourcePath) return { url, kind: 'error', error: 'no source_path in front matter' };
  const sourceRepo = /^https:\/\/github\.com\/([^/]+\/[^/]+)\//.exec(frontMatterValue(frontMatter, 'original_content_git_url') || '')?.[1];
  const fromSourceRepo = config.sourceRepos.length === 0 ||
    config.sourceRepos.some(repo => repo.toLowerCase() === sourceRepo?.toLowerCase());
  if (!fromSourceRepo || !config.trackedPaths.test(sourcePath)) {
    return { url, kind: 'fetched', entry: { ...entry, sourceRepo, untracked: true } };
  }

  let mirrorPath;
  try {
    mirrorPath = mirrorPathFor(sourcePath);
  } catch (error) {
    return { url, kind: 'error', error: error.message };
  }
  const content = stripFrontMatterKeys(text, config.stripFrontMatter);
  return { url, kind: 'fetched', entry: { ...entry, path: mirrorPath }, content };
}

// Runs the worker over items in order until they run out or the deadline
// passes. Items never started come back as undefined.
async function pool(items, concurrency, worker, deadline = Infinity) {
  const results = new Array(items.length);
  let next = 0;
  let done = 0;
  const runners = Array.from({ length: Math.min(concurrency, items.length) }, async () => {
    while (next < items.length && Date.now() < deadline) {
      const index = next++;
      results[index] = await worker(items[index]);
      if (++done % 100 === 0) console.log(`  … ${done}/${items.length}`);
    }
  });
  await Promise.all(runners);
  return results;
}

// The order a run checks pages in: the priority pages, then every other page
// starting after the one the last run stopped at, wrapping round.
function runOrder(urls, cursor, priority) {
  const first = priority ? urls.filter(url => priority.test(url)) : [];
  const rest = priority ? urls.filter(url => !priority.test(url)) : urls.slice();
  const start = cursor ? rest.findIndex(url => url > cursor) : 0;
  const rotated = start > 0 ? [...rest.slice(start), ...rest.slice(0, start)] : rest;
  return { order: [...first, ...rotated], priorityCount: first.length };
}

// Folds one run's fetch results into the previous state and decides what the
// working tree should hold. Pure: the caller does the writing.
function reconcile(previousPages, pageUrls, results) {
  const pages = {};
  const errors = [];
  const byUrl = new Map(results.map(result => [result.url, result]));

  for (const url of pageUrls) {
    const result = byUrl.get(url);
    const previous = previousPages[url];
    if (!result) {
      if (previous) pages[url] = previous;
    } else if (result.kind === 'unchanged') {
      pages[url] = previous;
    } else if (result.kind === 'fetched') {
      pages[url] = result.entry;
    } else if (result.kind === 'error') {
      errors.push(result);
      if (previous) pages[url] = previous;
    }
    // 'gone' drops the page, as does falling out of the sitemap.
  }

  // Two URLs can resolve to the same source file (a redirect Learn still lists,
  // say). The first in sorted order owns the file; the others are recorded as
  // aliases so they are neither written twice nor deleted from under the owner.
  const owners = new Map();
  for (const url of Object.keys(pages).sort()) {
    const entry = pages[url];
    if (!entry.path) continue;
    if (owners.has(entry.path)) pages[url] = { ...entry, path: undefined, aliasOf: owners.get(entry.path) };
    else owners.set(entry.path, url);
  }

  const writes = [];
  for (const result of results) {
    if (result.kind === 'fetched' && result.content !== undefined && owners.get(result.entry.path) === result.url) {
      writes.push({ path: result.entry.path, content: result.content, entry: result.entry });
    }
  }

  const keptPaths = new Set(owners.keys());
  const deletes = [...new Set(Object.values(previousPages).map(entry => entry.path).filter(Boolean))]
    .filter(file => !keptPaths.has(file))
    .sort();
  return { pages, writes, deletes, errors };
}

function shortSha(sha) {
  return sha ? sha.slice(0, 7) : null;
}

function commitMessage(changes) {
  const { added, modified, deleted } = changes;
  const parts = [];
  if (modified.length) parts.push(`${modified.length} changed`);
  if (added.length) parts.push(`${added.length} added`);
  if (deleted.length) parts.push(`${deleted.length} removed`);
  const published = [...added, ...modified].map(c => c.entry.updatedAt).filter(Boolean).sort();
  const lines = [`Mirror Learn: ${parts.join(', ') || 'metadata only'}`, ''];
  if (published.length) lines.push(`Latest publish on Learn: ${published[published.length - 1]}`, '');
  const describe = (status, change) => {
    const meta = [change.entry?.updatedAt && `published ${change.entry.updatedAt}`, shortSha(change.entry?.gitCommitId) && `upstream ${shortSha(change.entry.gitCommitId)}`]
      .filter(Boolean).join(', ');
    return `${status} ${change.path}${meta ? ` (${meta})` : ''}`;
  };
  for (const change of modified) lines.push(describe('M', change));
  for (const change of added) lines.push(describe('A', change));
  for (const change of deleted) lines.push(describe('D', change));
  return lines.join('\n') + '\n';
}

function parseArgs(argv) {
  const args = { config: 'learn-mirror.config.json', full: false, limit: 0, messageFile: null, allowMassDelete: false, seedUrls: null, maxMinutes: 0 };
  for (const arg of argv) {
    const [flag, value] = arg.split(/=(.*)/s);
    if (flag === '--config') args.config = value;
    else if (flag === '--full') args.full = true;
    else if (flag === '--limit') args.limit = Number(value);
    else if (flag === '--message-file') args.messageFile = value;
    else if (flag === '--allow-mass-delete') args.allowMassDelete = true;
    else if (flag === '--seed-urls') args.seedUrls = value;
    else if (flag === '--max-minutes') args.maxMinutes = Number(value);
    else throw new Error(`unknown option ${arg}`);
  }
  return args;
}

function writeGitHubOutputs(values, summary) {
  if (process.env.GITHUB_OUTPUT) {
    fs.appendFileSync(process.env.GITHUB_OUTPUT, Object.entries(values).map(([k, v]) => `${k}=${v}\n`).join(''));
  }
  if (process.env.GITHUB_STEP_SUMMARY) fs.appendFileSync(process.env.GITHUB_STEP_SUMMARY, summary);
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const root = process.cwd();
  const config = loadMirrorConfig(path.resolve(root, args.config));
  setPace(config.maxRequestsPerSecond);
  const stateFile = path.join(root, config.stateFile);
  const previous = readState(stateFile);
  const started = Date.now();

  const { sitemapUrls, pageUrls: discovered } = await discoverPages(config);
  // Seed files add pages the sitemaps and TOCs do not list.
  const seedFiles = [path.resolve(root, config.seedUrlsFile), args.seedUrls && path.resolve(root, args.seedUrls)]
    .filter(file => file && fs.existsSync(file));
  const seeded = selectPageUrls(
    seedFiles.flatMap(file => fs.readFileSync(file, 'utf8').split(/\r?\n/)).map(line => line.trim()).filter(Boolean),
    config
  );
  const known = Object.keys(previous.pages).filter(url => config.include.test(url) && !config.exclude.some(re => re.test(url)));
  const allUrls = [...new Set([...discovered, ...seeded, ...known])].sort();
  const { order, priorityCount } = runOrder(allUrls, previous.cursor, config.priority);
  const pageUrls = args.limit > 0 ? order.slice(0, args.limit) : order;
  console.log(`🗺️  ${sitemapUrls.length} sitemap(s): ${discovered.length} page(s) listed, ${allUrls.length - discovered.length} more already known${seeded.length ? ' or seeded' : ''}; ${priorityCount} priority${args.limit ? `; limited to ${pageUrls.length}` : ''}${args.maxMinutes ? `; ${args.maxMinutes} minute budget` : ''}`);

  const deadline = args.maxMinutes > 0 ? started + args.maxMinutes * 60000 : Infinity;
  const settled = await pool(pageUrls, config.concurrency, url =>
    fetchPage(url, previous.pages[url], root, config, args.full), deadline
  );
  const results = settled.filter(Boolean);
  const unreached = pageUrls.length - results.length;
  // Pages this run did not reach are carried over as they were, and the next
  // run starts after the last page of the rotation this one checked.
  const plan = reconcile(previous.pages, allUrls, results);
  const checkedRotation = pageUrls.slice(priorityCount).filter((url, index) => settled[priorityCount + index]);
  plan.cursor = checkedRotation.length ? checkedRotation[checkedRotation.length - 1] : previous.cursor;

  const counts = results.reduce((acc, r) => ({ ...acc, [r.kind]: (acc[r.kind] || 0) + 1 }), {});
  console.log(`📥 ${JSON.stringify(counts)} in ${((Date.now() - started) / 1000).toFixed(1)}s${pace.throttled ? `, throttled ${pace.throttled} time(s)` : ''}${unreached ? `; ${unreached} left for the next run` : ''}`);

  if (plan.errors.length > Math.max(10, results.length / 2)) {
    for (const error of plan.errors.slice(0, 10)) console.error(`  ✗ ${error.url}: ${error.error}`);
    throw new Error(`${plan.errors.length} of ${results.length} pages failed; refusing to write a mirror from a mostly failed run`);
  }
  const mirrored = new Set(Object.values(previous.pages).map(e => e.path).filter(Boolean)).size;
  if (!args.allowMassDelete && plan.deletes.length > Math.max(25, mirrored * config.maxDeleteRatio)) {
    throw new Error(`run would delete ${plan.deletes.length} of ${mirrored} mirrored files; rerun with --allow-mass-delete if that is intended`);
  }

  const changes = { added: [], modified: [], deleted: [] };
  for (const write of plan.writes) {
    const file = path.join(root, write.path);
    let existing = null;
    try { existing = fs.readFileSync(file, 'utf8'); } catch (error) { if (error.code !== 'ENOENT') throw error; }
    if (existing === write.content) continue;
    fs.mkdirSync(path.dirname(file), { recursive: true });
    fs.writeFileSync(file, write.content);
    (existing === null ? changes.added : changes.modified).push(write);
  }
  for (const relative of plan.deletes) {
    const file = path.join(root, relative);
    if (!fs.existsSync(file)) continue;
    fs.rmSync(file);
    changes.deleted.push({ path: relative });
  }
  fs.mkdirSync(path.dirname(stateFile), { recursive: true });
  fs.writeFileSync(stateFile, serializeState({ cursor: plan.cursor, pages: plan.pages }));

  for (const error of plan.errors) console.warn(`  ⚠️  ${error.url}: ${error.error}`);
  const message = commitMessage(changes);
  if (args.messageFile) fs.writeFileSync(path.resolve(root, args.messageFile), message);
  const contentChanged = changes.added.length + changes.modified.length + changes.deleted.length > 0;
  console.log(contentChanged ? message : '✅ No content changes');

  writeGitHubOutputs(
    {
      content_changed: contentChanged,
      added: changes.added.length,
      modified: changes.modified.length,
      deleted: changes.deleted.length,
      errors: plan.errors.length,
      unreached
    },
    `### Learn mirror\n\n| Pages | Unchanged (304) | Fetched | Gone | Errors | Not reached | Added | Changed | Removed | Throttled | Seconds |\n|---|---|---|---|---|---|---|---|---|---|---|\n` +
      `| ${pageUrls.length} | ${counts.unchanged || 0} | ${counts.fetched || 0} | ${counts.gone || 0} | ${plan.errors.length} | ${unreached} | ${changes.added.length} | ${changes.modified.length} | ${changes.deleted.length} | ${pace.throttled} | ${((Date.now() - started) / 1000).toFixed(0)} |\n\n` +
      (plan.errors.length ? `<details><summary>Errors</summary>\n\n${plan.errors.map(e => `- ${e.url}: ${e.error}`).join('\n')}\n</details>\n\n` : '') +
      (contentChanged ? '```\n' + message + '```\n' : '')
  );
}

module.exports = {
  loadMirrorConfig,
  parseSitemapLocs,
  parseTocHrefs,
  selectPageUrls,
  splitFrontMatter,
  frontMatterValue,
  stripFrontMatterKeys,
  mirrorPathFor,
  runOrder,
  serializeState,
  reconcile,
  commitMessage
};

if (require.main === module) {
  main().catch(error => {
    console.error(`❌ ${error.message}`);
    process.exit(1);
  });
}
