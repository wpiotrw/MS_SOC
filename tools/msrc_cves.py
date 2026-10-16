#!/usr/bin/env python3
"""msrc_cves.py - the MSRC Security Update Guide details of every CVE the portal lists.

  python3 tools/msrc_cves.py site [--max 120] [--budget 240]

Why (CLAUDE.md 5eb, 16 X 2026, owner: "in Microsoft Blogs, Vulnerabilities & threats, you give the CVE number and
title, but when expanded there are no details such as Weakness or Released / Last updated"). The MSRC RSS feed the
blog collector reads carries only a title and a generic summary. The public, unauthenticated MSRC API
(api.msrc.microsoft.com/sug/v2.0) has the rest: CWE, release and last-revision dates, severity, impact, CVSS,
exploited / publicly disclosed, exploitability. It sends no CORS header, so a browser cannot read it - this script
does, from GitHub Actions, and writes site/data/msrc-cves.json, which the page loads when a CVE row is opened.

What it reads: the CVE numbers in the newest site/data/<date>.json (blog posts nt.items, items, community, MC
titles - any string field named title). What it writes: {"generated", "cves": {CVE: {...}}}. Entries already in the
file are kept; a CVE is re-read when it is new, or when its last check is older than 12 hours and it was released in
the last 45 days (MSRC revises recent CVEs). Exit 0 always - a missing detail is a gap, never a failed page.
No credentials, no tenant data.
"""
import datetime as dt, glob, gzip, html, json, os, re, sys, time, urllib.parse, urllib.request

API = "https://api.msrc.microsoft.com/sug/v2.0/en-US/vulnerability?$filter="
CVE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b")


def newest_state(site):
    files = sorted(glob.glob(os.path.join(site, "data", "20??-??-??.json")))
    if files:
        return json.load(open(files[-1], encoding="utf-8"))
    files = sorted(glob.glob(os.path.join(site, "data", "20??-??-??.json.gz")))
    return json.load(gzip.open(files[-1], "rt", encoding="utf-8")) if files else {}


def cves_in(obj, out):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, str) and k in ("title", "officialTitle", "link", "url", "id"):
                out.update(CVE.findall(v))
            else:
                cves_in(v, out)
    elif isinstance(obj, list):
        for v in obj:
            cves_in(v, out)


def strip(h):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h or ""))).strip()


def fetch(cve):
    url = API + urllib.parse.quote("cveNumber eq '%s'" % cve, safe="")
    req = urllib.request.Request(url, headers={"User-Agent": "MS_SOC portal (github.com/wpiotrw/MS_SOC)", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=25) as r:
        v = (json.load(r).get("value") or [])
    if not v:
        return None
    # one CVE can have several rows (one per release); the newest revision speaks for it
    v.sort(key=lambda x: x.get("latestRevisionDate") or "", reverse=True)
    x = v[0]
    cwe = x.get("cweList") or []
    cweUrl = [s.split("cweUrl: ", 1)[1] for s in (x.get("cweDetailsListForSearch") or []) if s.startswith("cweUrl: ")]
    return {
        "title": x.get("cveTitle") or "", "released": (x.get("releaseDate") or "")[:10],
        "updated": (x.get("latestRevisionDate") or "")[:10], "release": x.get("releaseNumber") or "",
        "weakness": cwe, "weaknessUrl": cweUrl, "severity": x.get("severity") or "", "impact": x.get("impact") or "",
        "cvss": x.get("baseScore") or "", "temporal": x.get("temporalScore") or "", "vector": x.get("vectorString") or "",
        "exploited": x.get("exploited") or "", "disclosed": x.get("publiclyDisclosed") or "",
        "exploitability": x.get("latestSoftwareRelease") or "", "product": x.get("tag") or "",
        "cna": x.get("issuingCna") or "", "description": strip(x.get("description"))[:600],
        "url": "https://msrc.microsoft.com/update-guide/vulnerability/" + cve, "cveOrg": x.get("mitreUrl") or "",
    }


def main():
    site = sys.argv[1] if len(sys.argv) > 1 else "site"
    mx = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 120
    budget = float(sys.argv[sys.argv.index("--budget") + 1]) if "--budget" in sys.argv else 240.0
    path = os.path.join(site, "data", "msrc-cves.json")
    old = {}
    try:
        old = json.load(open(path, encoding="utf-8")).get("cves") or {}
    except Exception:
        pass
    found = set()
    cves_in(newest_state(site), found)
    now = dt.datetime.now(dt.timezone.utc)
    cut45 = (now - dt.timedelta(days=45)).date().isoformat()

    def due(c):
        e = old.get(c)
        if not e:
            return True
        chk = e.get("checked") or ""
        recent = (e.get("released") or "9999") >= cut45
        try:
            age_h = (now - dt.datetime.fromisoformat(chk)).total_seconds() / 3600
        except Exception:
            age_h = 999
        return recent and age_h >= 12

    todo = sorted((c for c in found if due(c)), reverse=True)[:mx]
    t0, ok, miss, err = time.time(), 0, 0, 0
    cves = dict(old)
    for c in todo:
        if time.time() - t0 > budget:
            break
        try:
            d = fetch(c)
            if d:
                d["checked"] = now.isoformat(timespec="seconds")
                cves[c] = d; ok += 1
            else:
                miss += 1
        except Exception as e:
            err += 1
            print("  %s: %s" % (c, str(e)[:120]))
        time.sleep(0.3)
    # keep what the portal can still show: listed today, or released in the last 120 days
    cut120 = (now - dt.timedelta(days=120)).date().isoformat()
    cves = {k: v for k, v in cves.items() if k in found or (v.get("released") or "") >= cut120}
    body = {"source": "https://api.msrc.microsoft.com/sug/v2.0 (public MSRC Security Update Guide API)", "cves": dict(sorted(cves.items()))}
    prev = None
    try:
        prev = json.load(open(path, encoding="utf-8"))
    except Exception:
        pass
    if prev and {k: v for k, v in prev.items() if k != "generated"} == body:
        print("msrc: no change (%d CVEs listed, %d read, %d unknown to MSRC, %d errors)" % (len(found), ok, miss, err))
        return
    body = dict(generated=now.isoformat(timespec="seconds"), **body)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(body, f, ensure_ascii=False, separators=(",", ":"))
    print("msrc: changed (%d CVEs in file, %d listed today, %d read, %d unknown to MSRC, %d errors)" % (len(cves), len(found), ok, miss, err))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # never fail the workflow over a detail
        print("msrc: skipped - %s" % e)
