/* MS_SOC Microsoft service status (CLAUDE.md 5gr, 13 XI 2026). Author: Piotr Wisniewski.
   Reads the PUBLIC status feeds of Microsoft 365 and Azure (status.cloud.microsoft) and answers a small JSON for the
   badges under the logo. The feeds send no CORS header, so the page cannot read them itself; this function can, on the
   same origin. Anonymous (staticwebapp.config.json gives /api/ms-status to everyone; every other /api/* stays owner-only).
   No keys, no tenant data. The answer is kept 120 s in memory, so Microsoft is asked at most once in two minutes
   however many people open the page. A feed that cannot be read says so ("error"), it is never reported as "OK". */

const FEEDS = [
  { key: "m365", name: "Microsoft 365", feed: "https://status.cloud.microsoft/api/feed/mac",
    page: "https://status.cloud.microsoft/", admin: "https://admin.microsoft.com/#/servicehealth" },
  { key: "azure", name: "Azure", feed: "https://rssfeed.azure.status.microsoft/en-us/status/feed/",
    page: "https://azure.status.microsoft/en-us/status", admin: "https://portal.azure.com/#blade/Microsoft_Azure_Health/AzureHealthBrowseBlade" }
];
const TTL = 120000, T_OUT = 10000;
let CACHE = null;

const ENT = { amp: "&", lt: "<", gt: ">", quot: '"', apos: "'", nbsp: " " };
function unent(s) {
  return String(s || "").replace(/&(#x[0-9a-f]+|#\d+|[a-z]+);/gi, (m, e) => {
    if (e[0] === "#") { const n = e[1] === "x" || e[1] === "X" ? parseInt(e.slice(2), 16) : parseInt(e.slice(1), 10); return isFinite(n) ? String.fromCodePoint(n) : m; }
    return ENT[e.toLowerCase()] !== undefined ? ENT[e.toLowerCase()] : m;
  });
}
function cdata(s) { return String(s || "").replace(/^\s*<!\[CDATA\[([\s\S]*?)\]\]>\s*$/, "$1"); }
function tag(block, name) { const m = new RegExp("<" + name + "(?:\\s[^>]*)?>([\\s\\S]*?)</" + name + ">", "i").exec(block); return m ? cdata(m[1]).trim() : ""; }
function lines(desc) {
  const html = unent(desc);                                   // the description is escaped HTML
  return html.split(/<\s*(?:br|\/?div|\/?p|\/?li)[^>]*>/i)
    .map((x) => unent(x.replace(/<[^>]+>/g, " ")).replace(/\s+/g, " ").trim())
    .filter(Boolean).slice(0, 30).map((x) => x.slice(0, 600));
}
function level(status, title) {
  const s = (status + " " + title).toLowerCase();
  if (/restored|resolved|falsepositive|false positive|postincident|post-incident|mitigated/.test(s)) return "resolved";
  if (/interruption|outage|unavailable|down\b/.test(s)) return "bad";
  return "warn";                                             // ServiceDegradation, Investigating, advisories, an Azure item without status
}
function parse(xml) {
  const items = [];
  const re = /<item[\s>][\s\S]*?<\/item>/gi; let m;
  while ((m = re.exec(xml))) {
    const b = m[0], status = tag(b, "status"), title = unent(tag(b, "title"));
    const pub = tag(b, "pubDate"); const d = pub ? new Date(pub.replace(/ Z$/, " GMT")) : null;
    items.push({ title, status: status || null, level: level(status, title), published: d && !isNaN(d) ? d.toISOString() : null,
      link: unent(tag(b, "link")) || null, lines: lines(tag(b, "description")) });
  }
  const lb = tag(xml, "lastBuildDate"), d = lb ? new Date(lb.replace(/ Z$/, " GMT")) : null;
  return { items, built: d && !isNaN(d) ? d.toISOString() : null };
}
async function read(f) {
  const ctl = new AbortController(); const t = setTimeout(() => ctl.abort(), T_OUT);
  const out = { key: f.key, name: f.name, feed: f.feed, page: f.page, admin: f.admin };
  try {
    const r = await fetch(f.feed, { signal: ctl.signal, headers: { "User-Agent": "MS_SOC status badge (+https://guardzilla.azureme.pl/)", Accept: "application/rss+xml, text/xml" } });
    const txt = await r.text();
    if (r.status !== 200 || !/<rss[\s>]/i.test(txt)) { out.state = "error"; out.error = "HTTP " + r.status; return out; }
    const p = parse(txt);
    const open = p.items.filter((i) => i.level !== "resolved");
    out.items = p.items; out.built = p.built;
    out.state = open.some((i) => i.level === "bad") ? "bad" : (open.length ? "warn" : "ok");
    out.open = open.length;
  } catch (e) {
    out.state = "error"; out.error = e.name === "AbortError" ? "timeout after " + T_OUT / 1000 + " s" : String(e.message || e).slice(0, 120);
  } finally { clearTimeout(t); }
  return out;
}

module.exports = async function (context, req) {
  const now = Date.now(), force = req && req.query && req.query.refresh === "1";
  // ?refresh=1 skips the cache, but no more often than every 20 s (the Refresh button cannot hammer Microsoft)
  if (!CACHE || now - CACHE.t > TTL || (force && now - CACHE.t > 20000)) {
    const services = await Promise.all(FEEDS.map(read));
    CACHE = { t: now, data: { checked: new Date(now).toISOString(), ttlSeconds: TTL / 1000, services } };
  }
  context.res = { status: 200, headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "public, max-age=60" },
    body: JSON.stringify(CACHE.data) };
};
module.exports._test = { parse, lines, level };
