#!/usr/bin/env python3
"""stamp.py - when a workflow last changed what the portal shows (CLAUDE.md 5cz, README.md 13).

  python3 tools/stamp.py <key> [note]

Owner, 10 X 2026: "mark exactly, in a bigger frame top right, when the portal was updated; a tab that refreshes
more often through GitHub Actions says its exact date and time". Each workflow that commits data or page code
calls this just before its commit, so the stamp travels in the same commit (and the same deployment) as the data
it describes. One small file per workflow - site/data/fresh/<key>.json - so two workflows never edit the same file
(no rebase conflicts):

  {"key", "at" (UTC, minutes), "workflow", "run" (GitHub run id), "sha" (commit the run started from, 7 chars),
   "note", "spec" (code only: the newest stage of CLAUDE.md, e.g. "5da")}

Keys in use: code (code-refresh.yml), tenant (fpa-tenant.yml), campaigns (campaigns.yml), publish (publish.yml),
learn (learn-mirror.yml). The page reads them (data/fresh/*.json) for the header frame, the chips on the tabs and
the About tab. Nothing secret: workflow names, run numbers and commit ids are public in a public repository."""
import datetime, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def newest_stage(path):
    """the highest **§5..** stage written in CLAUDE.md (5da > 5cz > 5cy ...; a longer suffix is newer)"""
    try:
        txt = open(path, encoding="utf-8").read()
    except OSError:
        return None
    best = None
    for m in re.finditer(r"\*\*§(5[a-z]{2,3})\b", txt):
        k = m.group(1)
        if best is None or (len(k), k) > (len(best), best):
            best = k
    return best


def main(key, note=""):
    if not re.match(r"^[a-z][a-z0-9-]{0,30}$", key):
        raise SystemExit("stamp.py: bad key %r" % key)
    out = {"key": key, "at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
           "workflow": os.environ.get("GITHUB_WORKFLOW") or "", "run": os.environ.get("GITHUB_RUN_ID") or "",
           "sha": (os.environ.get("GITHUB_SHA") or "")[:7], "note": note}
    if key == "code":
        out["spec"] = newest_stage(os.path.join(ROOT, "CLAUDE.md"))
    d = os.path.join(ROOT, "site", "data", "fresh")
    os.makedirs(d, exist_ok=True)
    json.dump(out, open(os.path.join(d, key + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("stamp: %s %s %s" % (key, out["at"], out.get("spec") or ""))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "", " ".join(sys.argv[2:]))
