#!/usr/bin/env python3
"""MS_SOC - Message Center coverage: which source knows which post (CLAUDE.md 5gf, 3 XI 2026).

Author: Piotr Wisniewski.
Owner, 3 XI 2026: "MC1488839 is on msmessagecenter.com, but neither merill nor DeltaPulse has it. Do we follow that
site? Do we cross-check the sources so that our list is always complete? Does the Message Center tab report how many
posts each source has, the differences, the technologies?"
Checked that day: mc.merill.net/messages-index.json (17 087 records, 4 829 MC) lacks MC1488839 and 165 other posts that
msmessagecenter.com lists; msmessagecenter.com publishes a sitemap (robots.txt allows everything) with every active
post (1 711) and its last change - so it is a full listing, not only the RSS feed of 100 posts we read since 5bo.
Sources (each with ok / unread and its window - a short window is not a gap):
  merill        https://mc.merill.net/messages-index.json - every post of his archive (MIT, github.com/merill/mc)
  msmc          https://msmessagecenter.com/sitemap.xml - every active post with its last change
  deltapulse    https://deltapulse.app/mcp - its public MCP server, `search` over the last 30 days (the site's terms
                forbid scraping; the MCP server is its documented programmatic access)
  tenant        site/data/mc-tenant.json - Message Center of our tenant through Graph (only subscribed services)
  ours          mc.entries of the newest brief state - what the portal shows
Writes site/data/mc-coverage.json: per post the sources that know it ("s"), counts per source, per technology per
source, and the differences inside the comparable window (posts changed in the last 30 days): which posts each source
lacks, and - the alarm - posts a source knows and OUR list does not (`gaps`, with title and link). The brief's
collector (collect_mc.py) adds the gaps it can read; the page shows them in Message Center > Sources & coverage.
"""
import datetime
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site", "data", "mc-coverage.json")
UA = "Mozilla/5.0 (compatible; MS-SOC-brief/1.0)"
MERILL = "https://mc.merill.net/messages-index.json"
SITEMAP = "https://msmessagecenter.com/sitemap.xml"
DPMCP = "https://deltapulse.app/mcp"
WINDOW = 30
NAMES = {"merill": "mc.merill.net", "msmc": "msmessagecenter.com", "deltapulse": "DeltaPulse", "tenant": "Our tenant (Graph)", "ours": "This portal"}
TECH = [(r"Entra|Azure AD|Azure Active Directory|Identity", "Entra"), (r"Intune|Endpoint Manager|Autopilot|Autopatch", "Intune"),
        (r"Exchange|Outlook", "Exchange & Outlook"), (r"Teams", "Teams"), (r"SharePoint|OneDrive", "SharePoint & OneDrive"),
        (r"Defender|Security", "Defender"), (r"Purview|Compliance|Information Protection|eDiscovery", "Purview"),
        (r"Copilot|AI", "Copilot"), (r"Power |Dynamics|Dataverse", "Power Platform & Dynamics"), (r"Windows", "Windows"),
        (r"Viva|Planner|Loop|Forms|Stream|Bookings|Whiteboard|Sway|Clipchamp|Engage|Yammer", "Other Microsoft 365 apps"),
        (r"Microsoft 365|Office|admin center|Apps", "Microsoft 365")]


def log(*a):
    print("mc_coverage:", *a, flush=True)


def load(p, d):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return d


def get(url, data=None, headers=None, timeout=90):
    h = {"User-Agent": UA}
    h.update(headers or {})
    req = urllib.request.Request(url, data=data, headers=h, method="POST" if data else "GET")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def techs(svcs, title=""):
    out = []
    for s in (svcs or []) + ([title] if not svcs else []):
        for rx, t in TECH:
            if re.search(rx, s or "", re.I):
                if t not in out:
                    out.append(t)
                break
    return out or ["Not stated"]


def read_merill():
    L = json.loads(get(MERILL))
    out = {}
    for m in L:
        i = m.get("Id") or m.get("id") or ""
        if re.match(r"MC\d+$", i):
            out[i] = {"title": m.get("Title") or "", "svc": m.get("Services") or [],
                      "changed": (m.get("LastModifiedDateTime") or m.get("StartDateTime") or "")[:10], "start": (m.get("StartDateTime") or "")[:10]}
    return out


def read_sitemap():
    s = get(SITEMAP).decode("utf-8", "replace")
    return {i: {"changed": d} for i, d in re.findall(r"<loc>https://msmessagecenter\.com/(MC\d+)[^<]*</loc>\s*<lastmod>([^<]*)</lastmod>", s)}


def read_dp():
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                       "params": {"name": "search", "arguments": {"source": "messages", "dateRange": "last_30_days", "limit": 2000}}}).encode()
    j = json.loads(get(DPMCP, body, {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}))
    if j.get("error"):
        raise RuntimeError(str(j["error"])[:150])
    o = json.loads(j["result"]["content"][0]["text"])
    while isinstance(o, dict) and isinstance(o.get("content"), list) and o["content"] and o["content"][0].get("type") == "text":
        o = json.loads(o["content"][0]["text"])
    out = {}
    for r in o.get("results") or o.get("items") or []:
        i = r.get("id") or ""
        if re.match(r"MC\d+$", i):
            out[i] = {"title": (r.get("title") or "").strip(), "svc": r.get("service") or [],
                      "changed": (r.get("lastUpdatedDate") or r.get("publishedDate") or "")[:10], "start": (r.get("publishedDate") or "")[:10]}
    return out


def newest_state():
    d = os.path.join(ROOT, "site", "data")
    for f in sorted((f for f in os.listdir(d) if re.match(r"\d{4}-\d{2}-\d{2}\.json$", f)), reverse=True):
        s = load(os.path.join(d, f), {})
        s = s.get("soc-brief-state") or s
        if (s.get("mc") or {}).get("entries"):
            return s, f[:10]
    return {}, ""


def run(day=None):
    day = day or datetime.date.today().isoformat()
    since = (datetime.date.fromisoformat(day) - datetime.timedelta(days=WINDOW)).isoformat()
    S, state = {}, {}
    for key, fn in (("merill", read_merill), ("msmc", read_sitemap), ("deltapulse", read_dp)):
        try:
            S[key] = fn()
            state[key] = {"state": "ok", "n": len(S[key])}
        except Exception as e:
            S[key] = {}
            state[key] = {"state": "unread", "n": 0, "note": str(e)[:160]}
            log(key, "not read:", e)
    t = load(os.path.join(ROOT, "site", "data", "mc-tenant.json"), {})
    S["tenant"] = {m["id"]: {"title": m.get("title") or "", "svc": m.get("services") or [], "changed": (m.get("modified") or m.get("start") or "")[:10],
                             "start": (m.get("start") or "")[:10]} for m in t.get("messages") or [] if m.get("id")}
    state["tenant"] = {"state": "ok" if S["tenant"] else "unread", "n": len(S["tenant"]), "read": t.get("read")}
    st, sday = newest_state()
    S["ours"] = {e["id"]: {"title": e.get("title") or "", "svc": e.get("tech") or [], "changed": (e.get("updated") or e.get("published") or "")[:10],
                           "start": (e.get("published") or "")[:10]} for e in (st.get("mc") or {}).get("entries") or [] if e.get("id")}
    state["ours"] = {"state": "ok" if S["ours"] else "unread", "n": len(S["ours"]), "brief": sday}
    window = {"merill": "every post of the archive", "msmc": "every active post", "deltapulse": "last 30 days", "tenant": "active posts of our services", "ours": "the brief's window"}
    allids = set()
    for v in S.values():
        allids |= set(v)

    def info(i):
        for k in ("ours", "tenant", "deltapulse", "merill", "msmc"):
            if i in S[k] and (S[k][i].get("title") or k == "msmc"):
                return S[k][i]
        return {}

    def changed(i):
        return max((S[k][i].get("changed") or "") for k in S if i in S[k])

    posts = {}
    for i in allids:
        posts[i] = {"s": "+".join(k for k in ("merill", "msmc", "deltapulse", "tenant", "ours") if i in S[k]), "c": changed(i)}
    recent = sorted(i for i in allids if posts[i]["c"] >= since)
    # per source: all, and inside the comparable window (posts changed in the last 30 days)
    counts = {k: {"all": len(S[k]), "window": sum(1 for i in recent if i in S[k]), "only": sum(1 for i in recent if posts[i]["s"] == k)} for k in S}
    missing = {k: [i for i in recent if i not in S[k]] for k in S if state[k]["state"] == "ok"}
    # posts other sources know, changed in the window, and our list does not carry - the alarm
    gaps = []
    for i in recent:
        if i in S["ours"]:
            continue
        x = info(i)
        gaps.append({"id": i, "title": x.get("title") or "", "changed": posts[i]["c"], "s": posts[i]["s"], "link": "https://msmessagecenter.com/" + i if i in S["msmc"] else "https://mc.merill.net/message/" + i})
    for g in gaps[:20]:   # msmessagecenter.com's sitemap has no titles: read the page title of a gap (robots.txt allows it)
        if g["title"] or "msmc" not in g["s"]:
            continue
        try:
            h = get("https://msmessagecenter.com/" + g["id"], timeout=30).decode("utf-8", "replace")
            m = re.search(r"<title>(.*?)</title>", h, re.S)
            g["title"] = re.sub(r"\s+", " ", re.sub(r"^\s*MC\d+:\s*", "", m.group(1))).replace(" | Microsoft 365 Message Center", "").strip()[:200] if m else ""
        except Exception:
            pass
    tech = {}
    for i in recent:
        x = info(i)
        for tt in techs(x.get("svc") or [], x.get("title") or ""):
            r = tech.setdefault(tt, {k: 0 for k in S})
            for k in S:
                if i in S[k]:
                    r[k] += 1
            r["all"] = r.get("all", 0) + 1
    lacks = {k: [{"id": i, "title": info(i).get("title") or "", "changed": posts[i]["c"], "s": posts[i]["s"]} for i in sorted(v, key=lambda i: posts[i]["c"], reverse=True)[:60]] for k, v in missing.items() if k != "ours"}
    out = {"generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "day": day, "spec": "5gf",
           "window": {"days": WINDOW, "since": since, "posts": len(recent)}, "names": NAMES, "reach": window, "sources": state,
           "counts": counts, "missingCount": {k: len(v) for k, v in missing.items()}, "gaps": gaps[:100], "lacks": lacks,
           "tech": dict(sorted(tech.items(), key=lambda kv: -kv[1]["all"])),
           "posts": {i: posts[i]["s"] for i in sorted(allids) if posts[i]["c"] >= (datetime.date.fromisoformat(day) - datetime.timedelta(days=400)).isoformat() or i in S["ours"]},
           "note": "A source with a shorter reach is not a gap: DeltaPulse reads 30 days, our tenant only the services it subscribes to. Compared inside the window: posts changed in the last %d days." % WINDOW}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    log("%d posts changed in %d days; %s; gaps in our list: %d" % (len(recent), WINDOW,
        ", ".join("%s %d (only %d)" % (k, counts[k]["window"], counts[k]["only"]) for k in counts), len(gaps)))
    return out


if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv) > 1 else None)
