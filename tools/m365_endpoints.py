#!/usr/bin/env python3
"""MS_SOC - Microsoft 365 URLs and IP address ranges (CLAUDE.md 5fu, 30 X 2026).

Author: Piotr Wisniewski.
Owner, 30 X 2026: "tracking the changes of the Microsoft 365 address and IP range list - yes, a separate tab under Graph
API Radar". Microsoft's own web service (https://learn.microsoft.com/microsoft-365/enterprise/microsoft-365-ip-web-service):
  version/Worldwide              - the latest version (YYYYMMDDNN); Microsoft asks for at most one call an hour
  version/Worldwide?AllVersions  - every version since 2018
  changes/worldwide/0000000000   - every change record since July 2018 (id, endpointSetId, disposition, impact, add /
                                   remove ips and urls, effectiveDate of an addition, previous / current attributes)
  endpoints/worldwide            - the current endpoint sets (service area, urls, ips, ports, category Optimize / Allow /
                                   Default, required, expressRoute, notes)
The changes and the list are read only when the version moved (Microsoft: "only call the endpoints web method when the
version web method indicates that a new version is available"). Writes site/data/m365-endpoints.json and keeps its memory
in data/m365-endpoints/ (the client request id - a random GUID that identifies this caller, not a secret - and every
endpoint set ever seen, so a set Microsoft removed keeps its name and URLs).
"""
import datetime
import json
import os
import sys
import urllib.request
import uuid

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site", "data", "m365-endpoints.json")
MEM = os.path.join(ROOT, "data", "m365-endpoints")
WS = "https://endpoints.office.com"
KEEP_FROM = "2024010100"       # change records shown on the page (the memory keeps all)

# Microsoft's words for each impact (the web service article), shortened; what the admin does
IMPACT = {
    "AddedIp": ("IP range added", "act", "Add it to firewall rules before the effective date - Microsoft starts using it then; missing it can cause an outage."),
    "AddedUrl": ("URL added", "act", "Add it to the proxy bypass / allow list before the effective date - missing it can cause an outage."),
    "AddedIpAndUrl": ("IP range and URL added", "act", "Add both: the IP to firewall rules, the URL to the proxy list, before the effective date."),
    "AddedSubstituteUrl": ("URL published instead of a wildcard", "act", "A name hidden behind a removed wildcard is now listed; effective immediately - allow it if you allowed the wildcard."),
    "RemovedIpOrUrl": ("IP range or URL removed", "tidy", "Remove it from your network devices when convenient - there is no deadline."),
    "ChangedIsExpressRoute": ("ExpressRoute support changed", "check", "Only if you use ExpressRoute for Microsoft 365: check your routing."),
    "MovedIpOrUrl": ("Moved between endpoint sets", "none", "Generally no action."),
    "RemovedDuplicateIpOrUrl": ("Duplicate removed", "none", "Generally no action - it is still published elsewhere."),
    "OtherNonPriorityChanges": ("Other change (notes, ports)", "none", "Less critical: a note or another attribute changed."),
}
AREA = {"Common": "Microsoft 365 Common and Office Online", "Exchange": "Exchange Online", "SharePoint": "SharePoint Online and OneDrive",
        "Skype": "Microsoft Teams (and Skype for Business Online)"}


def log(*a):
    print("m365_endpoints:", *a, flush=True)


def load(p, d):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return d


def save(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, separators=(",", ":"))


def get(path, cid):
    sep = "&" if "?" in path else "?"
    req = urllib.request.Request(WS + path + sep + "clientrequestid=" + cid, headers={"User-Agent": "MS_SOC m365 endpoints (+https://github.com/wpiotrw/MS_SOC)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def vday(v):
    v = str(v or "")
    return "%s-%s-%s" % (v[:4], v[4:6], v[6:8]) if len(v) >= 8 else ""


def eday(d):
    d = str(d or "")
    return "%s-%s-%s" % (d[:4], d[4:6], d[6:8]) if len(d) == 8 and d.isdigit() else ""


def main(argv):
    force = "--force" in argv
    os.makedirs(MEM, exist_ok=True)
    st = load(os.path.join(MEM, "state.json"), {})
    cid = st.get("clientRequestId") or str(uuid.uuid4())
    st["clientRequestId"] = cid
    today = datetime.date.today().isoformat()
    try:
        ver = get("/version/Worldwide?AllVersions=true", cid)
    except Exception as e:
        log("version not read:", e)
        return 0
    latest = ver.get("latest")
    old = load(OUT, {})
    if latest == st.get("version") and not force and old.get("version") == latest:
        log("version", latest, "unchanged - nothing to do")
        st["checked"] = today
        save(os.path.join(MEM, "state.json"), st)
        return 0
    changes = get("/changes/worldwide/0000000000", cid)
    sets = get("/endpoints/worldwide", cid)
    known = load(os.path.join(MEM, "sets.json"), {})
    for s in sets:
        known[str(s["id"])] = {k: s.get(k) for k in ("id", "serviceArea", "serviceAreaDisplayName", "urls", "ips", "tcpPorts", "udpPorts", "category",
                                                     "expressRoute", "required", "notes")} | {"seen": today}
    # first day a version was seen by us (Microsoft publishes it with its own date in the number)
    firstSeen = st.setdefault("firstSeen", {})
    if latest not in firstSeen:
        firstSeen[latest] = today if st.get("version") else vday(latest)
    cur = {str(s["id"]) for s in sets}
    out_ch = []
    for c in changes:
        if str(c.get("version") or "") < KEEP_FROM:
            continue
        sid = str(c.get("endpointSetId"))
        ks = known.get(sid) or {}
        prev, curv = c.get("previous") or {}, c.get("current") or {}
        area = curv.get("serviceArea") or prev.get("serviceArea") or ks.get("serviceArea") or ""
        imps = [x.strip() for x in str(c.get("impact") or "").split(",") if x.strip()]
        add, rem = c.get("add") or {}, c.get("remove") or {}
        out_ch.append({
            "id": c.get("id"), "version": c.get("version"), "day": vday(c.get("version")), "set": c.get("endpointSetId"),
            "disposition": c.get("disposition"), "impact": imps, "desc": c.get("changeDescription") or "",
            "area": area, "areaName": AREA.get(area, area),
            "category": curv.get("category") or prev.get("category") or ks.get("category") or "",
            "required": (curv.get("required") or prev.get("required") or ks.get("required")),
            "addIps": add.get("ips") or [], "addUrls": add.get("urls") or [], "effective": eday(add.get("effectiveDate")),
            "remIps": rem.get("ips") or [], "remUrls": rem.get("urls") or [],
            "prev": prev, "cur": curv,
            "setUrls": (ks.get("urls") or [])[:8], "setInList": sid in cur,
            "notes": ks.get("notes") or curv.get("notes") or prev.get("notes") or "",
        })
    out_ch.sort(key=lambda x: (x["version"], x["id"] or 0), reverse=True)
    vers = []
    for v in (ver.get("versions") or [])[:40]:
        cs = [c for c in out_ch if c["version"] == v]
        vers.append({"version": v, "day": vday(v), "n": len(cs), "act": sum(1 for c in cs if any(IMPACT.get(i, ("", ""))[1] == "act" for i in c["impact"])),
                     "seen": firstSeen.get(v, "")})
    totals = {"sets": len(sets), "urls": sum(len(s.get("urls") or []) for s in sets), "ips": sum(len(s.get("ips") or []) for s in sets),
              "byCategory": {}, "byArea": {}}
    for s in sets:
        totals["byCategory"][s.get("category")] = totals["byCategory"].get(s.get("category"), 0) + 1
        totals["byArea"][s.get("serviceArea")] = totals["byArea"].get(s.get("serviceArea"), 0) + 1
    out = {"generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "day": today, "spec": "5fu",
           "instance": "Worldwide", "version": latest, "versionDay": vday(latest), "previous": st.get("version") or "",
           "versions": vers, "changes": out_ch, "impact": {k: list(v) for k, v in IMPACT.items()}, "areas": AREA, "totals": totals,
           "sets": [{k: s.get(k) for k in ("id", "serviceArea", "serviceAreaDisplayName", "urls", "ips", "tcpPorts", "udpPorts", "category", "expressRoute",
                                           "required", "notes")} for s in sets],
           "source": "https://learn.microsoft.com/microsoft-365/enterprise/microsoft-365-ip-web-service",
           "list": "https://learn.microsoft.com/microsoft-365/enterprise/urls-and-ip-address-ranges"}
    save(OUT, out)
    st["version"], st["checked"] = latest, today
    save(os.path.join(MEM, "state.json"), st)
    save(os.path.join(MEM, "sets.json"), known)
    log("version", latest, "(was %s)" % (out["previous"] or "none"), "-", len(out_ch), "change records kept,", len(sets), "endpoint sets")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
