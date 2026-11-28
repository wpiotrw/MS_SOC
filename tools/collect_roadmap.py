#!/usr/bin/env python3
"""MS_SOC - Microsoft 365 Roadmap, the products and functions the portal tracks (CLAUDE.md 5hw, 28 XI 2026).

Author: Piotr Wisniewski.
Owner, 28 XI 2026: "we follow MC from many sources, but not the Roadmap (RM575283, RM573698, RM576199) - why? ... only the
products and functions we track, not everything - we don't need the rest".

Source: Microsoft's own Roadmap API, https://www.microsoft.com/releasecommunications/api/v1/m365 - every item (2 420 on
28 XI 2026) with status (In development / Rolling out / Launched / Cancelled), the planned month ("December CY2026"), the
preview month, products, release phase, platforms, cloud instances, created and modified. Microsoft keeps no history, so
this script keeps a snapshot (data/roadmap/snapshot.json) and writes what changed between two reads as events.

Scope (SCOPE below): an item is kept when one of its products is a tracked technology (Entra, Intune, Purview, Defender,
Exchange, SharePoint, OneDrive, Microsoft 365 admin center, Graph, Agent 365), or when it belongs to a broad end-user
product (Copilot, Copilot Studio, Teams, Outlook, Microsoft 365, Edge) AND its
title or description names a function the portal tracks (admin, policy, security, compliance, identity, sharing, data
protection, agents' governance, retirements). Owner, 28 XI: "only what we really track and need" - Power Platform, Dynamics 365,
Viva, Word, Excel, PowerPoint, Planner ... are out; Windows (11, Server, 365) is in, Edge only for security, M365, Entra, Intune.

Writes site/data/roadmap.json: {generated, source, total, inScope, baseline, scope, items[], events[]}.
The first run is the baseline: it records every item and reports no "new" ones.
"""
import datetime
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site", "data", "roadmap.json")
MEM = os.path.join(ROOT, "data", "roadmap")
SNAP = os.path.join(MEM, "snapshot.json")
MCT = os.path.join(ROOT, "site", "data", "mc-tenant.json")
API = "https://www.microsoft.com/releasecommunications/api/v1/m365"
# CLAUDE.md 5hw-b (28 XI 2026, owner: "is Merill the only one collecting RM? any extra sources for a cross check, for a
# Merill outage?"): Merill is not used at all - the primary is Microsoft's API above. Two more readers:
#   RSS  - Microsoft's Roadmap RSS (same data, another endpoint): the FALLBACK when the API fails, and a cross check
#          (ids missing on one side, status that differs);
#   DPMCP - DeltaPulse's public MCP server (independent tracker, items changed in the last 30 days): a cross check of
#          status and of items Microsoft's API does not return.
RSS = "https://www.microsoft.com/releasecommunications/api/v2/m365/rss"
DPMCP = "https://deltapulse.app/mcp"
STATUSES = {"In development", "Rolling out", "Launched", "Cancelled"}
PHASES = {"General Availability", "Preview", "Targeted Release", "Targeted Release (Entire Organization)", "Targeted Release (Select People)", "Current Channel", "Monthly Enterprise Channel", "Semi-Annual Enterprise Channel", "Semi-Annual Enterprise Channel (Preview)", "Beta Channel", "Current Channel (Preview)"}
CLOUDS = {"GCC", "GCC High", "DoD", "Worldwide (Standard Multi-Tenant)", "China", "Education", "Government Community Cloud (GCC)"}
PLATFORMS = {"Web", "Desktop", "Mac", "iOS", "Android", "Teams and Surface Devices", "Windows", "Linux", "Developer", "Mobile"}
UA = "MS_SOC-portal (github.com/wpiotrw/MS_SOC; Roadmap reader)"
KEEP_DAYS = 120          # events kept on the page
DONE_DAYS = 60           # a Launched or Cancelled item stays on the page this long after Microsoft last touched it

# Roadmap product tag -> the portal's technology (the same names as the brief's TECH list, SCRIPT 17)
CORE = {
    "Microsoft Entra": "Entra ID", "Microsoft Intune": "Intune", "Microsoft Purview": "Purview",
    "Microsoft Information Protection": "Purview", "Microsoft Defender for Office 365": "Defender",
    "Microsoft 365 Defender": "Defender", "Microsoft Defender": "Defender", "Microsoft Defender for Endpoint": "Defender",
    "Microsoft Defender for Identity": "Defender", "Microsoft Defender for Cloud Apps": "Defender",
    "Microsoft Sentinel": "Sentinel", "Exchange": "Exchange & Outlook", "Exchange Online": "Exchange & Outlook",
    "SharePoint": "SharePoint & OneDrive", "OneDrive": "SharePoint & OneDrive",
    "Microsoft 365 admin center": "Microsoft 365", "Microsoft 365 Admin Center": "Microsoft 365",
    "Microsoft Graph": "Graph API", "Microsoft Agent 365": "Copilot",
    # owner, 28 XI 09:18: "Windows - Windows 11, Windows Server, Windows 365 - stays, for RM and MC"
    "Windows": "Windows", "Windows 365": "Windows", "Windows 11": "Windows", "Windows Server": "Windows",
}
BROAD = {
    "Microsoft Copilot (Microsoft 365)": "Copilot", "Microsoft Copilot Studio": "Copilot", "Microsoft Teams": "Teams",
    "Outlook": "Exchange & Outlook", "Microsoft 365": "Microsoft 365",
    # owner, 28 XI 09:18: "Edge - only what is about security and M365, Entra, Intune"
    "Microsoft Edge": "Edge",
}
# the functions the portal tracks, read from the title and description of a broad product's item
FUNC = re.compile(
    r"\badmin|polic(?:y|ies)|security|secure|compliance|govern|retention|\bdlp\b|sensitivity|label|conditional access|audit|"
    r"ediscovery|external (?:access|user)|guest|sharing|tenant|permission|consent|oversharing|data protection|encrypt|"
    r"authenticat|sign-in|identity|agent (?:management|registry|inventory|governance)|licens|deprecat|retire|block|restrict|"
    r"phish|spam|malware|threat|insider|lockbox|residency|records management|information barrier|access review|"
    r"(?:entra|intune|purview|defender)\b", re.I)
# Edge: only security and what touches Microsoft 365, Entra and Intune (owner, 28 XI 09:18)
EDGE_FUNC = re.compile(r"security|secure|smartscreen|phish|malware|password|passkey|certificate|polic(?:y|ies)|admin|"
                       r"managed (?:device|browser)|intune|entra|purview|\bdlp\b|data (?:loss|protection)|microsoft 365|\bm365\b|"
                       r"enterprise|work profile|conditional access|identity|sign-in|compliance|deprecat|retire|block", re.I)
EDGE_STRONG = re.compile(r"security|smartscreen|phish|malware|intune|entra|purview|\bdlp\b|data loss|conditional access|"
                         r"microsoft 365|\bm365\b|compliance", re.I)


def log(*a):
    print("collect_roadmap:", *a, flush=True)


def load(p, d):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return d


def save(p, obj, indent=None):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    tmp = p + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=indent, separators=(",", ":") if indent is None else None)
        f.write("\n")
    os.replace(tmp, p)


def plain(h):
    t = re.sub(r"<[^>]+>", " ", h or "")
    t = t.replace("&nbsp;", " ").replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&#39;", "'")
    return re.sub(r"\s+", " ", t).strip()


def tags(i, k):
    return [x.get("tagName") for x in ((i.get("tagsContainer") or {}).get(k) or []) if x.get("tagName")]


def scope(i):
    """The portal's technologies an item belongs to, [] when it is out of scope."""
    prods = tags(i, "products")
    tech = sorted({CORE[p] for p in prods if p in CORE})
    if tech:
        return tech, "product"
    broad = sorted({BROAD[p] for p in prods if p in BROAD})
    txt = i.get("title", "") + " " + plain(i.get("description"))
    if broad == ["Edge"]:   # the title names the function, or the description names a security / M365 / Entra / Intune control
        ok = EDGE_FUNC.search(i.get("title", "")) or EDGE_STRONG.search(plain(i.get("description")))
        return (broad, "function") if ok else ([], "")
    if broad and FUNC.search(txt):
        return broad, "function"
    return [], ""


def shape(i, tech, why, mc):
    rid = str(i.get("id"))
    return {
        "id": rid, "title": (i.get("title") or "").strip(), "text": plain(i.get("description"))[:700],
        "status": i.get("status") or "", "when": (i.get("publicDisclosureAvailabilityDate") or "").strip(),
        "preview": (i.get("publicPreviewDate") or "").strip(), "phase": tags(i, "releasePhase"),
        "products": tags(i, "products"), "tech": tech, "why": why, "platforms": tags(i, "platforms"),
        "clouds": tags(i, "cloudInstances"), "created": (i.get("created") or "")[:10], "modified": (i.get("modified") or "")[:10],
        "more": i.get("moreInfoLink") or "", "mc": mc.get(rid, []),
        "url": "https://www.microsoft.com/microsoft-365/roadmap?id=" + rid, "merill": "https://mc.merill.net/message/RM" + rid,
    }


WATCH = (("status", "status"), ("when", "date"), ("preview", "preview"), ("phase", "phase"), ("title", "title"))
# month order for "slipped" / "earlier": "December CY2026", "Q1 CY2027"
MON = {m: n for n, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august", "september",
                                    "october", "november", "december"], 1)}


def month_key(s):
    m = re.search(r"(?i)([a-z]+)\s+(?:cy)?(\d{4})", s or "")
    if m and m.group(1).lower() in MON:
        return int(m.group(2)) * 100 + MON[m.group(1).lower()]
    q = re.search(r"(?i)q([1-4])\s+(?:cy)?(\d{4})", s or "")
    if q:
        return int(q.group(2)) * 100 + int(q.group(1)) * 3
    return None


def read_api():
    req = urllib.request.Request(API, headers={"User-Agent": UA, "Accept": "application/json"})
    raw = json.loads(urllib.request.urlopen(req, timeout=90).read().decode("utf-8"))
    if not isinstance(raw, list) or len(raw) < 500:
        raise RuntimeError("unexpected answer (%s items)" % (len(raw) if isinstance(raw, list) else type(raw).__name__))
    return raw


def read_rss():
    """Microsoft's RSS turned into the API's shape: the categories carry status, phase, clouds, platforms and products;
    the description ends with "GA date: <month>" and "Preview date: <month>"."""
    import xml.etree.ElementTree as ET
    req = urllib.request.Request(RSS, headers={"User-Agent": UA})
    root = ET.fromstring(urllib.request.urlopen(req, timeout=90).read())
    out = []
    for it in root.iter("item"):
        g = (it.findtext("guid") or "").strip()
        if not g.isdigit():
            continue
        cats = [c.text.strip() for c in it.findall("category") if c.text]
        desc = it.findtext("description") or ""
        ga = re.search(r"GA date:\s*([^<\n]+)", desc); pv = re.search(r"Preview date:\s*([^<\n]+)", desc)
        body = re.split(r"<br>\s*GA date:|<br>\s*Preview date:", desc)[0]
        upd = (it.findtext("{http://www.w3.org/2005/Atom}updated") or "")
        tc = lambda S: [{"tagName": c} for c in cats if c in S]
        out.append({"id": int(g), "title": (it.findtext("title") or "").strip(), "description": body,
                    "status": next((c for c in cats if c in STATUSES), ""), "publicDisclosureAvailabilityDate": ga.group(1).strip() if ga else "",
                    "publicPreviewDate": pv.group(1).strip() if pv else "", "created": "", "modified": upd[:19], "moreInfoLink": None,
                    "tagsContainer": {"releasePhase": tc(PHASES), "cloudInstances": tc(CLOUDS), "platforms": tc(PLATFORMS),
                                      "products": [{"tagName": c} for c in cats if c not in STATUSES | PHASES | CLOUDS | PLATFORMS]}})
    if len(out) < 500:
        raise RuntimeError("RSS: %d items" % len(out))
    return out


def read_dp():
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                       "params": {"name": "search", "arguments": {"source": "roadmap", "dateRange": "last_30_days", "limit": 2000}}}).encode()
    req = urllib.request.Request(DPMCP, body, {"User-Agent": UA, "Content-Type": "application/json", "Accept": "application/json, text/event-stream"})
    j = json.load(urllib.request.urlopen(req, timeout=90))
    if j.get("error"):
        raise RuntimeError("deltapulse: %s" % str(j["error"])[:150])
    o = json.loads(j["result"]["content"][0]["text"])
    while isinstance(o, dict) and isinstance(o.get("content"), list) and o["content"] and o["content"][0].get("type") == "text":
        o = json.loads(o["content"][0]["text"])
    return {str(r.get("id")): r for r in (o.get("results") or []) if str(r.get("id", "")).isdigit()}


def main():
    force_baseline = "--baseline" in sys.argv
    day = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    SRC = {}
    raw = rss = dp = None
    try:
        raw = read_api(); SRC["api"] = {"state": "ok", "items": len(raw), "url": API, "role": "primary"}
    except Exception as e:
        SRC["api"] = {"state": "unread", "items": 0, "url": API, "role": "primary", "error": str(e)[:160]}
    try:
        rss = read_rss(); SRC["rss"] = {"state": "ok", "items": len(rss), "url": RSS, "role": "fallback and cross check"}
    except Exception as e:
        SRC["rss"] = {"state": "unread", "items": 0, "url": RSS, "role": "fallback and cross check", "error": str(e)[:160]}
    try:
        dp = read_dp(); SRC["deltapulse"] = {"state": "ok", "items": len(dp), "url": DPMCP, "role": "cross check (changed in 30 days)"}
    except Exception as e:
        SRC["deltapulse"] = {"state": "unread", "items": 0, "url": DPMCP, "role": "cross check (changed in 30 days)", "error": str(e)[:160]}
    if raw is None:
        if rss is None:
            log("neither Microsoft's API nor its RSS answered - nothing written"); return 1
        raw = rss; SRC["rss"]["used"] = True
        log("API unread - the RSS is used (%d items)" % len(raw))
    log("Microsoft's Roadmap: %d items" % len(raw))

    mc = {}
    for m in load(MCT, {}).get("messages", []):
        for r in m.get("rm") or []:
            mc.setdefault(str(r), []).append(m.get("id"))

    prev_out = load(OUT, {})
    snap = load(SNAP, {})
    base = force_baseline or not snap
    cur, items, byid0 = {}, [], {}
    for i in raw:
        tech, why = scope(i)
        if not tech:
            continue
        it = shape(i, tech, why, mc)
        cur[it["id"]] = {k: it[k] for k in ("title", "status", "when", "preview", "phase", "modified")}
        byid0[it["id"]] = it
        items.append(it)

    # ---- cross checks (5hw-b): what the other readers say about the items in scope ----
    xc = {}
    if rss is not None and SRC["api"]["state"] == "ok":
        rs = {str(i["id"]): i for i in rss}
        only_api = [r for r in cur if r not in rs]; diff = [r for r in cur if r in rs and rs[r]["status"] and rs[r]["status"] != cur[r]["status"]]
        rss_in = [r for r, i in rs.items() if r not in {str(x["id"]) for x in raw} and scope(i)[0]]
        xc["rss"] = {"missingInRss": len(only_api), "missingInApi": len(rss_in), "statusDiffers": len(diff),
                     "examples": (only_api[:5] + rss_in[:5] + diff[:5])}
    if dp is not None:
        dpin = {r: v for r, v in dp.items() if r in cur or scope({"title": v.get("title", ""), "description": "", "tagsContainer": {"products": [{"tagName": p.strip()} for p in str(v.get("product") or "").split(",")]}})[0]}
        miss = [r for r in dpin if r not in cur]
        sd = [r for r, v in dpin.items() if r in cur and v.get("status") and v.get("status") != cur[r]["status"]]
        api_ids = {str(x["id"]) for x in raw}
        gone = [r for r in miss if r not in api_ids]     # DeltaPulse still lists it, Microsoft's own list no longer does
        xc["deltapulse"] = {"inScope": len(dpin), "missingInOurs": len(miss), "goneFromMicrosoft": len(gone), "statusDiffers": len(sd),
                            "examples": [{"id": r, "theirs": dpin[r].get("status"), "ours": cur[r]["status"]} for r in sd[:5]] + [{"id": r, "missing": True, "goneFromMicrosoft": r in gone, "title": dpin[r].get("title")} for r in miss[:5]]}
    for k, v in xc.items():
        SRC[k]["check"] = v
    log("cross check: %s" % json.dumps(xc)[:300])

    events = [e for e in prev_out.get("events", []) if e.get("day", "") >= (datetime.date.fromisoformat(day) - datetime.timedelta(days=KEEP_DAYS)).isoformat()]
    if not base:
        events = [e for e in events if e.get("day") != day]   # a second read the same day replaces that day's events
        old_snap = load(os.path.join(MEM, "snapshot.prev.json"), {}) if prev_out.get("read", "")[:10] == day else snap
        byid = {it["id"]: it for it in items}
        for rid, c in cur.items():
            p = old_snap.get(rid)
            it = byid[rid]
            if p is None:
                events.append({"day": day, "id": rid, "kind": "new", "after": c["status"], "title": it["title"], "tech": it["tech"]})
                continue
            for k, kind in WATCH:
                if (p.get(k) or "") != (c.get(k) or ""):
                    e = {"day": day, "id": rid, "kind": kind, "before": p.get(k), "after": c.get(k), "title": it["title"], "tech": it["tech"]}
                    if kind == "date":
                        a, b = month_key(p.get(k)), month_key(c.get(k))
                        if a and b:
                            e["move"] = "later" if b > a else "earlier" if b < a else ""
                    events.append(e)
        for rid, p in old_snap.items():
            if rid not in cur:
                events.append({"day": day, "id": rid, "kind": "removed", "before": p.get("status"), "title": p.get("title"),
                               "tech": (prev_out.get("_tech", {}) or {}).get(rid, [])})
    if prev_out.get("read", "")[:10] != day:
        save(os.path.join(MEM, "snapshot.prev.json"), snap)

    last = {}
    for e in events:
        last[e["id"]] = e
    for it in items:
        if it["id"] in last:
            it["changed"] = last[it["id"]]["day"]
            it["last"] = {k: last[it["id"]].get(k) for k in ("kind", "before", "after", "move") if last[it["id"]].get(k) is not None}
    # "only what we really need": open items always; a Launched / Cancelled one only while it is news (it changed in our
    # events, or Microsoft touched it in the last DONE_DAYS). The snapshot keeps them all, so leaving the page is no event.
    cut = (datetime.date.fromisoformat(day) - datetime.timedelta(days=DONE_DAYS)).isoformat()
    items = [it for it in items if it["status"] not in ("Launched", "Cancelled") or it.get("changed") or it["modified"] >= cut]
    items.sort(key=lambda x: (x.get("changed", ""), x["modified"]), reverse=True)
    out = {
        "read": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"), "source": API,
        "sources": SRC, "total": len(raw), "inScope": len(cur), "shown": len(items), "doneDays": DONE_DAYS, "baseline": prev_out.get("baseline") if not base else day,
        "scope": {"products": sorted(CORE), "broad": sorted(BROAD), "functions": FUNC.pattern},
        "items": items, "events": sorted(events, key=lambda e: (e["day"], e["id"]), reverse=True),
        "_tech": {rid: (byid0.get(rid) or {}).get("tech", []) for rid in cur},
    }
    save(OUT, out)
    save(SNAP, cur)
    kinds = {}
    for e in events:
        if e["day"] == day:
            kinds[e["kind"]] = kinds.get(e["kind"], 0) + 1
    log("in scope %d of %d, on the page %d; %s; events today %s" % (len(cur), len(raw), len(items), "baseline" if base else "compared", kinds or "none"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
