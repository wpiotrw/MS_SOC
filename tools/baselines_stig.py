#!/usr/bin/env python3
"""MS_SOC - DISA STIGs for Microsoft products in Security baselines (CLAUDE.md 5ge, 2 XI 2026).

Author: Piotr Wisniewski.
Owner, 2 XI 2026: "did our portal and scripts catch the Intune STIG audit baseline (Learn) and Patch My PC's article?
Microsoft's article is based on cyber.mil/stigs/downloads, which has Intune, Entra, M365, EXO... - an addition to the
Tenable, Maester, CISA we already collect; do we show it in Today, Overview, the daily sentences, diff, week?"
DISA (Defense Information Systems Agency) publishes Security Technical Implementation Guides (STIGs) - configuration
standards of the US Department of Defense - with SCAP benchmarks (machine-readable checks) and policy packages. The
download page of cyber.mil is a Salesforce site; it loads the whole catalog with one public call
(apex getCyberDocumentCatalogByDocumentLibrary, documentLibrary "STIGs"): name, download link, type, upload date. We
keep the Microsoft products (Windows, Windows Server, Entra ID, Intune, Defender, Office/Microsoft 365 Apps, Exchange,
SQL, IIS, Edge, Active Directory, .NET, PAW) - names, versions, dates and links only; nothing is downloaded or run.
Checked 2 XI 2026: there is no STIG for Microsoft 365 as a service or for Exchange Online (Exchange 2016/2019 only,
both "Sunset"); the cloud STIGs are Entra ID, Intune (Desktop & Mobile), Defender for Endpoint, Office 365 ProPlus and
Azure SQL.
Intune's STIG audit baseline (Learn: intune/device-security/security-baselines/stig-audit-baseline, our copy in
mirror/learn/intune/...) names the DISA benchmark version it audits against - compared with the newest DISA release of
the same benchmark ("Intune audits V2R7, DISA is at V2R11").
Changes between runs become events of the Security baselines (src "DISA STIG"): stig-new, stig-updated (new version
or release date), stig-sunset, stig-removed, intune-stig (Intune's table changed). The first run records only.
Writes site/data/baselines-stig.json; memory in data/baselines-stig/state.json.
"""
import datetime
import hashlib
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site", "data", "baselines-stig.json")
MEM = os.path.join(ROOT, "data", "baselines-stig", "state.json")
API = "https://www.cyber.mil/webruntime/api/apex/execute?language=en-US&asGuest=true&htmlEncode=false"
BODY = {"namespace": "", "classname": "@udd/01pRw0000002mOj", "method": "getCyberDocumentCatalogByDocumentLibrary",
        "isContinuation": False, "params": {"documentLibrary": "STIGs"}, "cacheable": False}
PAGE = "https://www.cyber.mil/stigs/downloads"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36 (MS_SOC baselines)"
LEARN = "https://learn.microsoft.com/en-us/intune/device-security/security-baselines/stig-audit-baseline"
LEARN_MD = os.path.join(ROOT, "mirror", "learn", "intune", "intune", "device-security", "security-baselines", "stig-audit-baseline.md")

MS = re.compile(r"Microsoft|Windows|Active Directory|Intune|Entra|Azure|Office|Exchange|SharePoint|Defender|SQL Server|IIS|\.NET|DotNet|PAW|Skype|OneDrive|Outlook|Excel|\bWord\b|PowerPoint|\bVisio\b|OneNote|Publisher|Access 2016|Project 2016", re.I)
NOT_MS = re.compile(r"Apple|Apache|Firefox|Symantec|Splunk|EDB Postgres|SCC \d|Central Log Server|Chef|Ansible|PowerShell DSC|Lifecycle Support|CIO Memo", re.I)
TECH = [(r"Entra", "Entra ID"), (r"Intune", "Intune"), (r"Defender Firewall", "Windows"), (r"Defender", "Defender"), (r"Windows Server|Server DNS|2012 Server", "Windows Server"),
        (r"Windows 1[01]|Windows PAW|Windows Defender Firewall", "Windows"), (r"Active Directory", "Active Directory"),
        (r"Exchange", "Exchange (on-premises)"), (r"SharePoint", "SharePoint (on-premises)"),
        (r"Office 365|Office System|Excel|\bWord\b|PowerPoint|Outlook|OneNote|Publisher|\bVisio\b|Access 2016|Project 2016|OneDrive|Skype", "Microsoft 365 Apps"),
        (r"Azure", "Azure"), (r"SQL Server", "SQL Server"), (r"IIS", "IIS"), (r"Edge", "Edge"), (r"\.Net|DotNet", ".NET")]
CLOUD = {"Entra ID", "Intune", "Defender", "Azure"}


def log(*a):
    print("baselines_stig:", *a, flush=True)


def load(p, d):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return d


def save(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")


def fetch():
    req = urllib.request.Request(API, data=json.dumps(BODY).encode(), method="POST",
                                 headers={"User-Agent": UA, "Content-Type": "application/json", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return (json.loads(r.read()) or {}).get("returnValue") or []


def ver_of(name, link):
    m = re.search(r"Ver(?:sion)?\.?\s*(\d+)\s*,?\s*Rel(?:ease)?\.?\s*(\d+)", name, re.I)
    if m:
        return "V%sR%s" % (m.group(1), m.group(2))
    m = re.search(r"_V(\d+)R(\d+)", link or "")
    if m:
        return "V%sR%s" % (m.group(1), m.group(2))
    m = re.search(r"_Y(\d{2})M(\d{2})", link or "")
    if m:
        return "20%s-%s" % (m.group(1), m.group(2))
    m = re.search(r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})", name)
    return "%s %s" % (m.group(1), m.group(2)) if m else ""


def kind_of(name, dtype):
    t = name + " " + (dtype or "")
    if re.search(r"SCAP|Benchmark", name, re.I):
        return "SCAP benchmark"
    if re.search(r"Policy|GPO|Group Policy", t, re.I) and not re.search(r"\bSTIG\b", name):
        return "Policy package"
    if re.search(r"SRG", name):
        return "SRG"
    return "STIG"


def product_of(name):
    p = re.sub(r"^\s*Sunset\s*-?\s*", "", name.replace("​", ""), flags=re.I)
    p = re.sub(r"[-–,]?\s*Ver(?:sion)?\.?\s*\d+\s*,?\s*Rel(?:ease)?\.?\s*\d+.*$", "", p, flags=re.I)
    p = re.sub(r"\s*-\s*(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\s*$", "", p)
    return re.sub(r"\s+", " ", p).strip(" -–,")


def tech_of(name):
    for rx, t in TECH:
        if re.search(rx, name, re.I):
            return t
    return "Other Microsoft"


def intune_table():
    """the table "Available STIG baselines" of Intune's STIG audit baseline page (our Learn copy)"""
    try:
        with open(LEARN_MD, encoding="utf-8") as f:
            md = f.read()
    except Exception:
        return []
    rows = []
    for line in md.splitlines():
        m = re.match(r"^\|\s*([^|]*STIG[^|]*?)\s*\|\s*Version\s*(\d+),\s*Release\s*(\d+)\s*\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|", line)
        if m:
            d = ""
            try:
                d = datetime.datetime.strptime(m.group(5).strip(), "%B %d, %Y").date().isoformat()
            except Exception:
                d = m.group(5).strip()
            rows.append({"baseline": m.group(1).strip(), "ver": "V%sR%s" % (m.group(2), m.group(3)), "rules": int(m.group(4)), "date": d})
    return rows


def vnum(v):
    m = re.match(r"V(\d+)R(\d+)", v or "")
    return (int(m.group(1)), int(m.group(2))) if m else None


def fpr(x):
    return hashlib.sha1(json.dumps(x, sort_keys=True).encode()).hexdigest()[:12]


def run(day, seed=False):
    st = load(MEM, {})
    try:
        cat = fetch()
    except Exception as e:
        log("not read:", e)
        return {"ok": False, "error": str(e)[:200], "page": PAGE}, [], {}
    rows = []
    for x in cat:
        name = (x.get("FileName") or "").replace("​", "").strip()
        link = x.get("DownloadLink") or ""
        if not name or not MS.search(name) or NOT_MS.search(name):
            continue
        r = {"name": name, "product": product_of(name), "ver": ver_of(name, link), "kind": kind_of(name, x.get("DownloadType")),
             "tech": tech_of(name), "date": (x.get("UploadDate") or "")[:10], "sunset": bool(re.match(r"\s*Sunset", name, re.I)),
             "link": link, "file": link.rsplit("/", 1)[-1], "type": x.get("DownloadType") or ""}
        r["key"] = re.sub(r"[^a-z0-9]+", "-", (r["product"] + " " + r["kind"]).lower()).strip("-")
        r["cloud"] = r["tech"] in CLOUD
        rows.append(r)
    if not rows:
        return {"ok": False, "error": "no Microsoft STIG in the catalog", "page": PAGE}, [], {}
    by = {}
    for r in rows:   # one entry per product and kind - the newest upload wins
        o = by.get(r["key"])
        if not o or (r["date"], r["ver"]) > (o["date"], o["ver"]):
            by[r["key"]] = r
    rows = list(by.values())

    it = intune_table()
    for i in it:   # Intune's audit baseline against DISA's newest release of the same benchmark
        d = next((r for r in rows if r["kind"] == "SCAP benchmark" and not r["sunset"] and r["product"].lower().replace(" scap benchmark", "") in i["baseline"].lower()), None) \
            or next((r for r in rows if r["kind"] == "SCAP benchmark" and r["product"].lower() == i["baseline"].lower().replace(" scap benchmark", " stig scap benchmark")), None)
        if d:
            i["disa"] = {"ver": d["ver"], "date": d["date"], "link": d["link"]}
            a, b = vnum(i["ver"]), vnum(d["ver"])
            i["behind"] = (b[1] - a[1]) if a and b and a[0] == b[0] else (None if not (a and b) else 99)
            d["intune"] = {"ver": i["ver"], "date": i["date"], "rules": i["rules"], "behind": i.get("behind")}

    first = not st.get("snap")
    mute = seed or first
    old = st.get("snap") or {}
    snap, ev, first_seen = {}, [], st.get("first") or {}
    for r in rows:
        snap[r["key"]] = {"name": r["name"], "ver": r["ver"], "date": r["date"], "sunset": r["sunset"], "tech": r["tech"], "kind": r["kind"], "link": r["link"]}
        first_seen.setdefault(r["key"], day if not first else r["date"])
        r["first"] = first_seen[r["key"]]
        if mute:
            continue
        o = old.get(r["key"])
        base = {"day": day, "src": "DISA STIG", "id": r["key"], "title": r["product"] + (" (" + r["kind"] + ")" if r["kind"] != "STIG" else ""),
                "tech": r["tech"], "ver": r["ver"], "date": r["date"], "url": r["link"] or PAGE}
        if not o:
            ev.append(dict(base, type="stig-new"))
        elif r["sunset"] and not o.get("sunset"):
            ev.append(dict(base, type="stig-sunset", was=o.get("ver")))
        elif (o.get("ver"), o.get("date")) != (r["ver"], r["date"]):
            ev.append(dict(base, type="stig-updated", was=o.get("ver"), now=r["ver"], wasDate=o.get("date")))
    if not mute:
        for k, o in old.items():
            if k not in snap:
                ev.append({"day": day, "src": "DISA STIG", "type": "stig-removed", "id": k, "title": o.get("name") or k, "tech": o.get("tech") or "", "url": PAGE})
        if st.get("intune") is not None and fpr(st.get("intune")) != fpr([{k: v for k, v in i.items() if k in ("baseline", "ver", "rules", "date")} for i in it]):
            for i in it:
                ev.append({"day": day, "src": "DISA STIG", "type": "intune-stig", "id": "intune-" + re.sub(r"[^a-z0-9]+", "-", i["baseline"].lower()),
                           "title": "Intune STIG audit baseline: " + i["baseline"], "tech": "Intune", "ver": i["ver"], "rules": i["rules"],
                           "disaVer": (i.get("disa") or {}).get("ver"), "url": LEARN})

    seen = {(e["day"], e["type"], e.get("id")) for e in st.get("events") or []}
    keep = (st.get("events") or []) + [e for e in ev if (e["day"], e["type"], e.get("id")) not in seen]
    cut60 = (datetime.date.fromisoformat(day) - datetime.timedelta(days=60)).isoformat()
    st["events"] = [e for e in keep if e["day"] >= cut60]
    since14 = (datetime.date.fromisoformat(day) - datetime.timedelta(days=14)).isoformat()
    ev = [e for e in st["events"] if e["day"] >= since14]

    rows.sort(key=lambda r: r["product"].lower())
    rows.sort(key=lambda r: r["date"], reverse=True)
    rows.sort(key=lambda r: (r["sunset"], not r["cloud"], r["tech"]))
    techs = {}
    for r in rows:
        if not r["sunset"]:
            techs[r["tech"]] = techs.get(r["tech"], 0) + 1
    since30 = (datetime.date.fromisoformat(day) - datetime.timedelta(days=30)).isoformat()
    cur = [r for r in rows if not r["sunset"]]
    summ = {"ok": True, "entries": len(rows), "current": len(cur), "sunset": len(rows) - len(cur), "cloud": sum(1 for r in cur if r["cloud"]),
            "scap": sum(1 for r in cur if r["kind"] == "SCAP benchmark"), "updated30": sum(1 for r in rows if r["date"] >= since30),
            "newest": [{"key": r["key"], "name": r["name"], "date": r["date"], "tech": r["tech"]} for r in sorted(cur, key=lambda r: r["date"], reverse=True)[:5]],
            "intune": it, "page": PAGE, "learn": LEARN, "catalog": len(cat),
            "note": "No DISA STIG exists for Microsoft 365 as a service or for Exchange Online (checked 2 XI 2026); Exchange 2016/2019 are on-premises and sunset."}
    out = {"generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "day": day, "spec": "5ge",
           "source": summ, "stigs": rows,
           "licence": "DISA STIGs are US Government works published at cyber.mil; this file keeps names, versions, dates and download links only."}
    save(OUT, out)
    st.update({"snap": snap, "first": first_seen, "checked": day,
               "intune": [{k: v for k, v in i.items() if k in ("baseline", "ver", "rules", "date")} for i in it]})
    save(MEM, st)
    log("catalog %d documents, %d Microsoft entries (%d current, %d cloud), Intune audit table %s, %d events%s" % (
        len(cat), len(rows), len(cur), summ["cloud"], ", ".join("%s %s vs DISA %s" % (i["baseline"], i["ver"], (i.get("disa") or {}).get("ver")) for i in it) or "-",
        len(ev), " (first run: recorded only)" if mute else ""))
    return summ, ev, techs


if __name__ == "__main__":
    d = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
    s, e, t = run(d)
    print(json.dumps({"summary": s, "events": e[:10], "techs": t}, ensure_ascii=False, indent=1)[:3500])
