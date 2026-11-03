#!/usr/bin/env python3
"""MS_SOC - which Message Center posts need "Use it - PowerShell", and is site/data/mc-howto.json well formed
(CLAUDE.md 5gf, 3 XI 2026). Author: Piotr Wisniewski.

Owner, 3 XI 2026: "for some MC you show PowerShell that reads the post - fine, keep it - but I meant PowerShell to USE
the feature the post describes: here, how to create such a group, or list the groups with that parameter. Think it
through, because not every MC can have a PowerShell."
  todo   posts of the last DAYS days (newest brief state) without a note, for services an admin manages with a script
         (Entra, Intune, Exchange, Teams, SharePoint, Defender, Purview, Power Platform, Windows), with Admin impact,
         a retirement, a deadline or major change first; the routine (routines/poranny-B-publish.md STEP -1d) writes
         notes for the first ones or marks them scriptable:false with the reason (a client or UI change).
  check  every note: ids are MC numbers, title, checked date, sources https with "says"; scriptable:true needs blocks
         with t / kind read|write / scopes / code / src; a write block needs a warning and -WhatIf; scriptable:false
         needs `why`. The PowerShell itself is checked by tools/mc_howto_validate.ps1 (parser, cmdlets, parameters).
  python3 tools/mc_howto_todo.py todo [days] | check
"""
import json, os, re, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOW = os.path.join(ROOT, "site", "data", "mc-howto.json")
SCRIPTABLE = re.compile(r"Entra|Azure AD|Intune|Exchange|Outlook|Teams|SharePoint|OneDrive|Defender|Purview|Power Platform|Power Apps|Power Automate|Windows|Microsoft 365 admin|Copilot", re.I)


def load(p, d):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return d


def state():
    d = os.path.join(ROOT, "site", "data")
    for f in sorted((f for f in os.listdir(d) if re.match(r"\d{4}-\d{2}-\d{2}\.json$", f)), reverse=True):
        s = load(os.path.join(d, f), {})
        s = s.get("soc-brief-state") or s
        if (s.get("mc") or {}).get("entries"):
            return s
    return {}


def check():
    H = load(HOW, None)
    if H is None:
        print("FAIL mc-howto.json not readable"); return 1
    bad = 0
    for n in H.get("notes") or []:
        k = n.get("key") or "?"
        def f(msg):
            nonlocal bad
            bad += 1; print("FAIL", k, msg)
        if not n.get("ids") or any(not re.match(r"MC\d+$", i) for i in n["ids"]): f("ids must be MC numbers")
        if not n.get("title"): f("no title")
        if not re.match(r"\d{4}-\d{2}-\d{2}$", n.get("checked") or ""): f("no checked date")
        for s in n.get("sources") or []:
            if not str(s.get("u", "")).startswith("https://") or not s.get("says"): f("source without https or says: %s" % s.get("t"))
        if n.get("scriptable"):
            if not n.get("blocks"): f("scriptable without blocks")
            for b in n.get("blocks") or []:
                for x in ("t", "kind", "scopes", "code", "src"):
                    if not b.get(x): f("block %r without %s" % (b.get("t"), x))
                if b.get("kind") not in ("read", "write"): f("block %r kind must be read or write" % b.get("t"))
                if b.get("kind") == "write" and ("-WhatIf" not in (b.get("code") or "") or not b.get("warn")): f("write block %r needs -WhatIf and warn" % b.get("t"))
                if re.search(r"(?i)client_secret|password\s*=|-ClientSecret", b.get("code") or ""): f("block %r carries a secret" % b.get("t"))
                if re.search(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", b.get("code") or "", re.I): f("block %r carries a GUID - use a <placeholder>" % b.get("t"))
        elif not n.get("why"):
            f("scriptable:false needs why")
    print("mc_howto check: %d notes, %d problem(s)" % (len(H.get("notes") or []), bad))
    return 1 if bad else 0


def todo(days=14):
    H = load(HOW, {})
    have = {i for n in H.get("notes") or [] for i in n.get("ids") or []}
    s = state()
    since = (datetime.date.today() - datetime.timedelta(days=days)).isoformat()
    rows = []
    for e in (s.get("mc") or {}).get("entries") or []:
        if e.get("id") in have or (e.get("updated") or e.get("published") or "") < since:
            continue
        svc = " ".join(e.get("tech") or []) + " " + (e.get("title") or "")
        if not SCRIPTABLE.search(svc):
            continue
        tags = " ".join(e.get("tags") or [])
        w = (3 if "Admin impact" in tags else 0) + (3 if re.search(r"Retirement|retire|deprecat", tags + e.get("title", ""), re.I) else 0) + \
            (2 if e.get("action") else 0) + (2 if e.get("isMajor") else 0) + (1 if e.get("category") == "Plan for Change" else 0)
        rows.append((w, e.get("updated") or e.get("published") or "", e["id"], e.get("title") or "", ", ".join(e.get("tech") or [])))
    rows.sort(reverse=True)
    for r in rows[:40]:
        print("%2d  %s  %-10s %s  [%s]" % r)
    print("mc_howto todo: %d posts of %d days without a note (first 40 shown, most important first)" % (len(rows), days))


if __name__ == "__main__":
    a = sys.argv[1:] or ["check"]
    if a[0] == "todo":
        todo(int(a[1]) if len(a) > 1 else 14)
    else:
        sys.exit(check())
