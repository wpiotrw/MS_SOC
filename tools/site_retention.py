#!/usr/bin/env python3
"""site_retention.py - keep site/ (deployed to Azure Static Web Apps) inside its size limit.

  python3 tools/site_retention.py <site dir> [--days 30] [--today YYYY-MM-DD] [--dry-run]

Why (30 IX 2026, CLAUDE.md §0h): site/ had 107 MB and grew ~3 MB a day. The packing and the 30-day
retention of §0h were a step of the morning mirror routine, and the retention never deleted anything:
`find -mtime +30` reads the file's modification time, which on a fresh clone is the clone time, so no
file is ever "older than 30 days" (27-30 VIII were still there on 30 IX). The owner decided the same
day: the app is on the Standard plan, and site/history/ may keep 30 days too - older versions stay in
the git history (`git log --all -- site/history/`), nothing is lost from the repository.

What it does, from the DATE IN THE FILE NAME, never from the file's time on disk:
  1. packs every site/history/*.html and every site/data/<date>.json except the two newest states
     (the registers changelog*.json and the undated files fpa-tenant.json, mc-tenant.json and
     history.json are read by the page and stay as they are), checking every .gz by decompressing it;
  2. deletes site/history/<date>-* and site/data/<date>.json[.gz] older than --days, but never one of
     the two newest data states, whatever their date.
Prints one line per action and a summary; exit 0 also when nothing changed. Run by
.github/workflows/code-refresh.yml before its commit; the routines do not delete anything themselves.
"""
import datetime as dt, gzip, os, re, sys

DATED = re.compile(r"^(\d{4}-\d{2}-\d{2})")

def pack(path, dry):
    if dry:
        print("pack    %s" % path); return
    raw = open(path, "rb").read()
    with gzip.open(path + ".gz", "wb", compresslevel=9) as g:
        g.write(raw)
    if gzip.open(path + ".gz", "rb").read() != raw:
        os.remove(path + ".gz")
        sys.exit("gzip check failed for %s - nothing removed" % path)
    os.remove(path)
    print("pack    %s (%d -> %d B)" % (path, len(raw), os.path.getsize(path + ".gz")))

def main():
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        sys.exit(__doc__)
    site = args[0]
    days = int(args[args.index("--days") + 1]) if "--days" in args else 30
    today = (dt.date.fromisoformat(args[args.index("--today") + 1]) if "--today" in args
             else dt.datetime.now(dt.timezone.utc).date())
    dry = "--dry-run" in args
    cutoff = today - dt.timedelta(days=days)
    hist, data = os.path.join(site, "history"), os.path.join(site, "data")
    before = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(site) for f in fs)
    packed = deleted = 0

    states = sorted(f for f in os.listdir(data) if re.match(r"^\d{4}-\d{2}-\d{2}\.json(\.gz)?$", f))
    newest_days = sorted({f[:10] for f in states})[-2:]

    # 1. pack
    for f in sorted(os.listdir(hist)):
        if f.endswith(".html"):
            pack(os.path.join(hist, f), dry); packed += 1
    for f in states:
        if f.endswith(".json") and f[:10] not in newest_days:
            pack(os.path.join(data, f), dry); packed += 1

    # 2. retention by the date in the name
    def old(name):
        m = DATED.match(name)
        if not m:
            return False
        try:
            return dt.date.fromisoformat(m.group(1)) < cutoff
        except ValueError:
            return False
    for d, keep in ((hist, set()), (data, set(newest_days))):
        for f in sorted(os.listdir(d)):
            if not old(f) or f[:10] in keep:
                continue
            if d == data and not re.match(r"^\d{4}-\d{2}-\d{2}\.json(\.gz)?$", f):
                continue
            p = os.path.join(d, f)
            print("delete  %s" % p)
            if not dry:
                os.remove(p)
            deleted += 1

    after = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(site) for f in fs)
    print("retention: packed %d, deleted %d (older than %s), site/ %.1f MB -> %.1f MB%s"
          % (packed, deleted, cutoff.isoformat(), before / 1e6, after / 1e6, " [dry run]" if dry else ""))

if __name__ == "__main__":
    main()
