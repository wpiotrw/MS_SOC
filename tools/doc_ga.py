#!/usr/bin/env python3
"""doc_ga.py - "the preview label came off": features Microsoft moved to general availability in its documentation,
announced or not (CLAUDE.md 5eo, 21 X 2026).

  python3 tools/doc_ga.py [REPO]            # REPO = the MS_SOC checkout (default .)

Owner, 21 X 2026: "I do not see that device sync in Entra Cloud Sync is now GA
(learn.microsoft.com/entra/identity/hybrid/cloud-sync/device-sync) - check when Microsoft took the preview flag off,
maybe it is on GitHub; if it is, why did we not catch it? Do we not track the Cloud Sync docs?"
Measured: MicrosoftDocs/entra-docs commit 8a1bca2fb8 of 29 IX 2026, "Remove preview labels from cloud sync device sync",
changed the title "Configure device sync with Microsoft Entra Cloud Sync (preview)" to "... Cloud Sync" and dropped the
preview note. Entra's What's new never mentioned it. The portal missed it twice over: the page was not in our Learn copy
(the copy held only pages the brief cites), and nothing compared titles for a dropped "(preview)".

Two detectors, one list:
  1. OUR LEARN COPY (mirror/learn/**.md, frontmatter `title` + `canonicalUrl`): titles are remembered in
     cache/doc-titles.json; a page whose remembered title carried "(preview)" and whose title now does not is an event
     dated the day we saw it. Works after Microsoft retires its public doc repositories (December 2026). First run =
     baseline, no events.
  2. MICROSOFT'S DOC REPOSITORIES while they are public (REPOS below; Entra first): a shallow clone of the last DAYS days,
     every commit whose diff removes "(preview)" from a page title (frontmatter or H1) is an event dated by the commit,
     with its link. Once a day (cache/doc-titles.json remembers when it last ran).
For each event: was it announced? - the Entra What's new page in our copy is searched for the page's path or its title.
Writes site/data/doc-ga.json (events, newest first, 180 days). Exit 0 always - a failed source is named in `sources`.
"""
import datetime as dt, json, os, re, subprocess, sys, tempfile

DAYS = 60            # how far back the repository scan looks
KEEP = 180           # how long an event stays listed
PREV = re.compile(r"\(\s*preview\s*\)|\[\s*preview\s*\]|\s[-–—:]\s*preview\b", re.I)
REPOS = [  # name, clone URL, path prefix in the repo, Learn URL prefix for that path, What's new page in our copy
    ("Microsoft Entra documentation", "https://github.com/MicrosoftDocs/entra-docs", "docs/",
     "https://learn.microsoft.com/en-us/entra/", "mirror/learn/entra/docs/fundamentals/whats-new.md"),
]


def same_page(before, after):
    """only "X (preview)" -> "X" is a GA by label; a new title in the same commit is a rewrite, not a GA
    (measured 21 X: a revert retitled "Microsoft Entra provisioning setup (Preview)" to a different page title)"""
    n = lambda x: re.sub(r"[^a-z0-9]+", "", PREV.sub("", clean(x)).lower())
    return n(before) == n(after)


def now():
    return dt.datetime.now(dt.timezone.utc)


def frontmatter(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            head = f.read(4000)
    except OSError:
        return None, None
    if not head.startswith("---"):
        return None, None
    end = head.find("\n---", 3)
    fm = head[3:end] if end > 0 else head
    t = re.search(r"^title:\s*(.+)$", fm, re.M)
    u = re.search(r"^canonicalUrl:\s*(\S+)", fm, re.M)
    return (t.group(1).strip().strip("'\"") if t else None), (u.group(1).strip() if u else None)


def clean(t):
    return re.sub(r"\s*[-|]\s*(Microsoft Entra( ID)?|Microsoft Learn|Microsoft Intune|Microsoft Defender.*?)(\s*\|.*)?$", "", t or "").strip()


def announced(whatsnew_text, url, title):
    if not whatsnew_text:
        return None
    path = url.split("learn.microsoft.com/en-us/", 1)[-1].rstrip("/")
    tail = "/".join(path.split("/")[-2:])
    base = PREV.sub("", clean(title)).strip().lower()
    t = whatsnew_text.lower()
    return bool((tail and tail.lower() in t) or (len(base) > 12 and base in t))


def scan_mirror(repo, titles, today):
    """detector 1: remembered title had (preview), current title does not"""
    events, seen = [], 0
    root = os.path.join(repo, "mirror", "learn")
    for d, _, files in os.walk(root):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            t, u = frontmatter(os.path.join(d, fn))
            if not t or not u:
                continue
            seen += 1
            old = titles.get(u)
            if old and PREV.search(old.get("t", "")) and not PREV.search(t) and same_page(old["t"], t):
                events.append({"url": u, "title": clean(t), "before": clean(old["t"]), "date": today, "how": "mirror",
                               "evidence": "title in our Learn copy lost its preview label between " + old.get("d", "?") + " and " + today})
            if not old or old.get("t") != t:
                titles[u] = {"t": t, "d": today}
    return events, seen


def scan_repo(name, url, prefix, base, since):
    """detector 2: commits in Microsoft's doc repository that drop (preview) from a title"""
    tmp = tempfile.mkdtemp(prefix="docga-")
    dest = os.path.join(tmp, "r")
    r = subprocess.run(["git", "clone", "-q", "--shallow-since=" + since, "--filter=blob:limit=200k", "--no-checkout", url, dest],
                       capture_output=True, text=True, timeout=600)
    if r.returncode != 0:
        raise RuntimeError("clone failed: " + (r.stderr or "")[-200:])
    # -G keeps only the files whose diff adds or removes a line with "preview" (the whole log -p of 60 days ran the
    # runner out of memory, measured 21 X 2026); the output is read as a stream, never held whole
    proc = subprocess.Popen(["git", "-C", dest, "log", "--since=" + since, "-G", "[Pp][Rr][Ee][Vv][Ii][Ee][Ww]", "-p", "--unified=0",
                             "--no-color", "--format=@@C %H %cI %s", "--", "*.md"], stdout=subprocess.PIPE, text=True, errors="replace")
    events, commits = [], 0
    cur, fname, minus = None, None, {}
    for line in proc.stdout:
        line = line.rstrip("\n")
        if line.startswith("@@C "):
            commits += 1
            p = line.split(" ", 3)
            cur = {"sha": p[1], "date": p[2][:10], "msg": p[3] if len(p) > 3 else ""}
            fname, minus = None, {}
            continue
        if line.startswith("+++ b/"):
            fname, minus = line[6:], {}
            continue
        if not cur or not fname or not fname.startswith(prefix):
            continue
        m = re.match(r"^([-+])(?:title:\s*|#\s+)(.+)$", line)
        if not m:
            continue
        sign, text = m.group(1), m.group(2).strip().strip("'\"")
        kind = "title" if re.match(r"^[-+]title:", line) else "h1"
        if sign == "-":
            minus[kind] = text
        elif kind in minus and PREV.search(minus[kind]) and not PREV.search(text) and same_page(minus[kind], text):
            path = fname[len(prefix):-3]
            if path.endswith("/index"):
                path = path[:-6]
            events.append({"url": base + path, "title": text, "before": minus[kind], "date": cur["date"], "how": "repo",
                           "repo": name, "commit": url + "/commit/" + cur["sha"], "commitMsg": cur["msg"][:140],
                           "evidence": "Microsoft's commit of " + cur["date"] + " removed the preview label from the page " + ("title" if kind == "title" else "heading")})
            minus.pop(kind, None)
    proc.wait(timeout=600)
    subprocess.run(["rm", "-rf", tmp])
    return events, commits


def main(repo="."):
    t0 = now(); today = t0.strftime("%Y-%m-%d")
    out_p = os.path.join(repo, "site", "data", "doc-ga.json")
    cache_p = os.path.join(repo, "cache", "doc-titles.json")
    try:
        prev = json.load(open(out_p, encoding="utf-8"))
    except Exception:
        prev = {}
    try:
        cache = json.load(open(cache_p, encoding="utf-8"))
    except Exception:
        cache = {}
    titles = cache.get("titles") or {}
    baseline = not titles
    events, sources = [], []
    try:
        ev, n = scan_mirror(repo, titles, today)
        if baseline:
            ev = []
        events += ev
        sources.append({"name": "Our Learn copy (mirror/learn)", "state": "ok", "pages": n, "events": len(ev),
                        "note": "baseline - titles remembered, no event on the first run" if baseline else ""})
    except Exception as e:
        sources.append({"name": "Our Learn copy (mirror/learn)", "state": "failed", "error": str(e)[:200]})
    last = cache.get("repoScan") or ""
    if last[:10] != today:
        since = (t0 - dt.timedelta(days=DAYS)).strftime("%Y-%m-%d")
        for name, url, prefix, base, wn in REPOS:
            try:
                ev, n = scan_repo(name, url, prefix, base, since)
                events += ev
                sources.append({"name": name, "url": url, "state": "ok", "commits": n, "events": len(ev), "since": since})
            except Exception as e:
                sources.append({"name": name, "url": url, "state": "failed", "error": str(e)[:200]})
        cache["repoScan"] = t0.strftime("%Y-%m-%dT%H:%M:%SZ")
    else:
        sources += [s for s in (prev.get("sources") or []) if s.get("url")]
    # merge with what was already listed; one event per page, the earliest date wins, both detectors noted
    by = {}
    for e in (prev.get("events") or []) + events:
        k = e["url"].rstrip("/").lower()
        o = by.get(k)
        if not o:
            by[k] = dict(e, how=[e["how"]] if isinstance(e["how"], str) else e["how"]); continue
        hw = o["how"] + ([e["how"]] if isinstance(e["how"], str) else e["how"])
        o["how"] = sorted(set(hw))
        if e.get("commit") and not o.get("commit"):
            o.update({k2: e[k2] for k2 in ("commit", "commitMsg", "repo") if e.get(k2)})
        if e["date"] < o["date"]:
            o["date"], o["evidence"] = e["date"], e["evidence"]
    wn_text = ""
    for _, _, _, _, wn in REPOS:
        try:
            wn_text += open(os.path.join(repo, wn), encoding="utf-8", errors="replace").read()
        except OSError:
            pass
    cut = (t0 - dt.timedelta(days=KEEP)).strftime("%Y-%m-%d")
    evs = [e for e in by.values() if e["date"] >= cut]
    for e in evs:
        e["announced"] = announced(wn_text, e["url"], e["title"])
    evs.sort(key=lambda e: (e["date"], e["url"]), reverse=True)
    body = {"source": "tools/doc_ga.py (CLAUDE.md 5eo)", "sources": sources, "events": evs,
            "window": {"repoDays": DAYS, "keepDays": KEEP}}
    strip = lambda d: {k: v for k, v in d.items() if k != "generated"}
    os.makedirs(os.path.dirname(cache_p), exist_ok=True)
    cache["titles"] = titles
    json.dump(cache, open(cache_p, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    if prev and strip(prev) == body:
        print("doc_ga: no change (%d events)" % len(evs))
        return 0
    body = dict(generated=t0.strftime("%Y-%m-%dT%H:%M:%SZ"), **body)
    json.dump(body, open(out_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("doc_ga: changed - %d events (%s)" % (len(evs), "; ".join("%s %s" % (s["name"], s["state"]) for s in sources)))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(*(sys.argv[1:2])))
    except Exception as e:
        print("doc_ga: skipped - %s" % e)
        sys.exit(0)
