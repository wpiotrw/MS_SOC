#!/usr/bin/env python3
"""feed_refresh.py - rebuild the RSS feeds from the newest published state, after every run (CLAUDE.md 5dz).

  python3 tools/feed_refresh.py CLAUDE.md site [<work dir, default .refresh>]

Why (16 X 2026): the feeds were written only by the morning mirror, so whatever the evening pass added reached a
feed reader the next morning. code-refresh.yml runs after every published run (workflow_run after "Campaign
tracking", which itself follows "Publish routine output" - the morning brief and the evening pass) and after the
campaign / baseline / tenant workflows, and calls this script there.

What it does, and nothing more:
  1. takes mirror_artifact.py as cut out of CLAUDE.md by code_refresh.py (the same work dir; bootstraps it if absent);
  2. reads the newest site/data/YYYY-MM-DD.json and calls write_feed() - site/feed.xml and site/feed-<key>.xml;
  3. puts the byline, JSON-LD and RSS <link>s into site/index.html and the routines' pages (diff/full.html, week/print.html; 5eq)
     when a page does not carry them yet (sign_page() is idempotent; a page that has them is not rewritten).
Prints "feeds: changed" when any file changed, "feeds: no change" otherwise. write_feed() only rewrites a file whose
content differs, and its lastBuildDate is the newest item's date, so a run with no new data changes nothing."""
import glob, hashlib, importlib.util, json, os, re, sys


def digest(paths):
    h = hashlib.sha256()
    for p in sorted(paths):
        try:
            h.update(p.encode() + open(p, "rb").read())
        except OSError:
            pass
    return h.hexdigest()


def main():
    doc, site = sys.argv[1], sys.argv[2]
    work = sys.argv[3] if len(sys.argv) > 3 else ".refresh"
    ma = os.path.join(work, "mirror_artifact.py")
    if not os.path.exists(ma):
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from code_refresh import bootstrap
        bootstrap(doc, work)
    spec = importlib.util.spec_from_file_location("mirror_artifact", ma)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    days = sorted(f for f in glob.glob(os.path.join(site, "data", "*.json"))
                  if re.match(r"\d{4}-\d\d-\d\d\.json$", os.path.basename(f)))
    if not days:
        sys.exit("feed_refresh: no site/data/YYYY-MM-DD.json")
    state = json.load(open(days[-1], encoding="utf-8"))
    date = (state.get("soc-brief-state") or {}).get("briefDate") or os.path.basename(days[-1])[:10]
    # 5eq: /diff/ and /week/ are the "What changed" app (tools/changes_page.py); the routines' pages moved to
    # diff/full.html and week/print.html carry the byline now. A page with the app's marker is never signed.
    pages = [os.path.join(site, p) for p in ("index.html", "diff/full.html", "week/print.html", "diff/index.html", "week/index.html")]
    pages = [p for p in pages if not (os.path.exists(p) and "data-changes-app" in open(p, encoding="utf-8", errors="replace").read(4000))]
    watch = glob.glob(os.path.join(site, "feed*.xml")) + pages
    before = digest(watch)
    n = m.write_feed(state, site, date)
    for p in pages:
        if not os.path.exists(p):
            continue
        h = open(p, encoding="utf-8").read()
        g = m.sign_page(h, date, "/")
        if g != h:
            open(p, "w", encoding="utf-8").write(g)
            print("signed: %s" % os.path.relpath(p, site))
    after = digest(glob.glob(os.path.join(site, "feed*.xml")) + pages)
    print("feeds: %s (%d items in feed.xml, state %s)" % ("changed" if after != before else "no change", n, date))


if __name__ == "__main__":
    main()
