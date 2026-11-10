#!/usr/bin/env python3
"""MS_SOC - Message Center posts that MUST be described in the brief and are not (CLAUDE.md 5gi, 10 XI 2026).

Author: Piotr Wisniewski.
Owner, 10 XI 2026: "did our mechanisms catch MC1546438 (Claude models in Copilot come into the EU Data Boundary and
are enabled by default)? merill? DeltaPulse? I saw nothing in the sentences we write - do we skip Copilot?"
Checked: the collector had it at the 06:47 UTC publication (mc.merill.net, msmessagecenter.com, our tenant; not
DeltaPulse), it was one of the 8 posts new that day, and the routine described 5 of the 8 - not this one, although it
is major, carries an act-by date (09/12/2026) and Admin impact. Copilot is not excluded: 10+ Copilot items were in the
brief. The choice of what becomes an item was left to the routine's judgement, and nothing checked it.
This file is the check. A post MUST be described when it is new in the window (first tracked in the last DAYS days)
and at least one of: Microsoft marks it major; it carries an act-by date; it is a retirement; it is a plan for change
with Admin impact. It is covered when its MC number appears in the items of any brief of the window. Otherwise it is
listed - unless data/mc-skip.json records it with a reason (a skip is a decision, written down, not a silence).
Writes site/data/mc-uncovered.json (read by the page: Today and Message Center show the uncovered posts in an amber
frame) and prints the list (read by the routine before it writes the items: every one becomes an item or a skip).
  python3 tools/mc_must_cover.py [day] [days]     exit 0 always
"""
import datetime
import glob
import json
import os
import re
import sys
import gzip

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site", "data", "mc-uncovered.json")
SKIP = os.path.join(ROOT, "data", "mc-skip.json")


def load(p, d):
    try:
        op = gzip.open if p.endswith(".gz") else open
        with op(p, "rt", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return d


def states(day, days):
    since = (datetime.date.fromisoformat(day) - datetime.timedelta(days=days)).isoformat()
    out = []
    for p in glob.glob(os.path.join(ROOT, "site", "data", "20??-??-??.json*")):
        d = os.path.basename(p)[:10]
        if since <= d <= day:
            s = load(p, {})
            out.append((d, s.get("soc-brief-state") or s))
    return sorted(out, key=lambda x: x[0])


def reasons(e):
    r = []
    if e.get("isMajor"):
        r.append("major")
    if e.get("action"):
        r.append("act by " + e["action"])
    tags = " ".join(e.get("tags") or [])
    if re.search(r"Retirement", tags) or re.search(r"\bretir", e.get("title") or "", re.I):
        r.append("retirement")
    if "Admin impact" in tags and (e.get("category") or "").lower().startswith("planforchange"):
        r.append("plan for change, admin impact")
    return r


def run(day=None, days=7):
    day = day or datetime.date.today().isoformat()
    S = states(day, days)
    if not S:
        print("mc_must_cover: no brief state in the window"); return {}
    since = (datetime.date.fromisoformat(day) - datetime.timedelta(days=days)).isoformat()
    covered = set()
    for _, s in S:
        covered |= set(re.findall(r"MC\d{6,8}", json.dumps(s.get("items") or [])))
    newest = S[-1][1]
    # a post whose change (campaign) already has another post described counts as covered through it - said so
    via = {}
    for c in (load(os.path.join(ROOT, "site", "data", "campaigns.json"), {}).get("campaigns") or []):
        mem = [m for m in c.get("members") or [] if re.match(r"MC\d+$", m)]
        hit = [m for m in mem if m in covered]
        if hit:
            for m in mem:
                if m not in covered:
                    via[m] = {"by": hit[0], "campaign": c.get("name")}
    skips = {x.get("id"): x for x in (load(SKIP, {}).get("skip") or []) if x.get("id")}
    unc, skipped, n, viaL = [], [], 0, []
    for e in (newest.get("mc") or {}).get("entries") or []:
        if (e.get("firstTracked") or "") < since or not re.match(r"MC\d+$", e.get("id") or ""):
            continue
        r = reasons(e)
        if not r:
            continue
        n += 1
        if e["id"] in covered:
            continue
        if e["id"] in via:
            viaL.append({"id": e["id"], "by": via[e["id"]]["by"], "campaign": via[e["id"]]["campaign"], "title": e.get("title") or ""})
            continue
        row = {"id": e["id"], "title": e.get("title") or "", "why": r, "action": e.get("action"), "tech": e.get("tech") or [],
               "first": e.get("firstTracked"), "summary": (e.get("feedSummary") or "")[:400],
               "link": e.get("feedLink") or e.get("link") or "https://mc.merill.net/message/" + e["id"]}
        if e["id"] in skips:
            row["skip"] = skips[e["id"]].get("why") or ""
            skipped.append(row)
        else:
            unc.append(row)
    unc.sort(key=lambda x: (x["action"] or "9999", x["first"]))
    out = {"generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "day": day, "spec": "5gi",
           "window": {"days": days, "since": since, "briefs": [d for d, _ in S]}, "mustCover": n, "uncovered": unc, "skipped": skipped, "viaCampaign": viaL,
           "rule": "new in the window and major, or with an act-by date, or a retirement, or a plan for change with Admin impact"}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("mc_must_cover: %d posts of %d days must be described; %d are not (%d skipped with a reason, %d covered through another post of the same change)" % (n, days, len(unc), len(skipped), len(viaL)))
    for x in unc:
        print("  %s  %-34s %s" % (x["id"], ", ".join(x["why"])[:34], x["title"][:90]))
    return out


if __name__ == "__main__":
    a = sys.argv[1:]
    run(a[0] if a else None, int(a[1]) if len(a) > 1 else 7)
