#!/usr/bin/env python3
"""MS_SOC - cross-check of dates between Message Center posts on the same change (CLAUDE.md 5gf, 3 XI 2026).

Author: Piotr Wisniewski.
Owner, 3 XI 2026, about MC1529463 ("Final reminder to replace MemberOf rule operator configurations by November 3,
2026"): "MC1488839 extends it to 31 March 2027 - so why do we still say MemberOf ends in November? We do not
cross-check. Say that something was until X but now is until Y - and check every piece of information that way."
The campaign layer (tools/campaigns.py, site/data/campaigns.json) already groups the posts of one change and reads
their dates, but each sentence, card and row of the portal quoted ONE post. This file gives every Message Center
post the dates the OTHER posts of the same change give:
  says    - the dates this post carries (milestones whose sources include it)
  others  - future dates given only by other posts of the same change (with the post, its date, the sentence)
  moved   - dates Microsoft itself revised in this post ("previously ..."): was -> now
  newer   - posts on the same change published after this one
  why     - the campaign's own explanation of how the dates fit together (campaigns.json `changes`)
  verdict - "moved" (a later post or Microsoft moved the date), "differs" (other posts give another date, e.g. for
            some licences or roles), "newer" (a later post exists, same date)
Read by the page (Overview sentences, Today, Deadlines, Message Center card), by /diff and by the routine before it
writes a sentence with a date (routines/poranny-B-publish.md).
Writes site/data/mc-datecheck.json. No network.
"""
import datetime
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMP = os.path.join(ROOT, "site", "data", "campaigns.json")
OUT = os.path.join(ROOT, "site", "data", "mc-datecheck.json")


def load(p, d):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return d


def newest_state():
    d = os.path.join(ROOT, "site", "data")
    days = sorted(f for f in os.listdir(d) if re.match(r"\d{4}-\d{2}-\d{2}\.json$", f))
    for f in reversed(days):
        s = load(os.path.join(d, f), {})
        s = s.get("soc-brief-state") or s
        if (s.get("mc") or {}).get("entries"):
            return s
    return {}


def run(day=None):
    day = day or datetime.date.today().isoformat()
    C = load(CAMP, {})
    st = newest_state()
    ent = {e["id"]: e for e in (st.get("mc") or {}).get("entries") or [] if e.get("id")}
    by = {}
    for c in C.get("campaigns") or []:
        ms = c.get("milestones") or []
        posts = {}
        for m in ms:
            if m.get("post") and m.get("src") and m.get("date"):
                posts.setdefault(m["src"], m["date"])
        dated = [m for m in ms if not m.get("post") and m.get("date") and m.get("key") != "posted"]
        mcs = [x for x in c.get("members") or [] if re.match(r"MC\d+$", x)]
        if len(mcs) < 2 and not any(m.get("msWas") for m in dated):
            continue
        for mc in mcs:
            def srcs(m):
                return m.get("srcs") or [m.get("src")]
            own = [m for m in dated if mc in srcs(m)]
            ownd = sorted({m["date"] for m in own})
            last_own = max(ownd) if ownd else ""
            oth, seen = [], set()
            for m in sorted(dated, key=lambda m: m["date"]):
                if mc in srcs(m) or m.get("past") or m["date"] < day:
                    continue
                k = (m["date"], m.get("src"))
                if k in seen:
                    continue
                seen.add(k)
                if m["date"] in ownd:
                    continue
                oth.append({"date": m["date"], "src": m.get("src"), "text": (m.get("text") or "")[:260],
                            "post": posts.get(m.get("src")), "later": bool(last_own and m["date"] > last_own),
                            "link": m.get("link")})
            oth = oth[:5]
            moved = [{"was": m["msWas"], "now": m["date"], "text": (m.get("text") or "")[:260]} for m in own if m.get("msWas") and not m.get("past")][:3]
            mine = posts.get(mc) or (ent.get(mc) or {}).get("published") or ""
            newer = sorted([{"id": s, "date": d, "title": (ent.get(s) or {}).get("title") or ""} for s, d in posts.items()
                            if s != mc and re.match(r"MC\d+$", s) and mine and d > mine], key=lambda x: x["date"])[-3:]
            why = [x.get("change") for x in c.get("changes") or [] if x.get("change") and x.get("src") != mc and
                   any(t in x["change"].lower() for t in ("while", "extended", "until", "instead", "moved", "previously", "only for", "for everyone else", "except"))][:2]
            if not (oth or moved or newer):
                continue
            verdict = "moved" if moved or any(o["later"] and o.get("post") and mine and o["post"] > mine for o in oth) else "differs" if oth else "newer"
            r = by.setdefault(mc, {"says": [], "others": [], "moved": [], "newer": [], "why": [], "campaigns": []})
            r["campaigns"].append({"id": c.get("id"), "name": c.get("name")})
            r["says"] = sorted(set(r["says"]) | set(d for d in ownd if d >= day))[:4] or ownd[-1:]
            for k, v in (("others", oth), ("moved", moved), ("newer", newer), ("why", why)):
                for x in v:
                    if x not in r[k]:
                        r[k].append(x)
            order = {"moved": 0, "differs": 1, "newer": 2}
            if order[verdict] < order.get(r.get("verdict"), 9):
                r["verdict"] = verdict
    out = {"generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "day": day, "spec": "5gf",
           "source": "site/data/campaigns.json (" + str(C.get("day") or "") + ")", "count": len(by), "byMc": by}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("mc_datecheck: %d posts with another date or a later post on the same change (%s)" % (
        len(by), ", ".join("%s %d" % (v, sum(1 for x in by.values() if x.get("verdict") == v)) for v in ("moved", "differs", "newer"))))
    return out


if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv) > 1 else None)
