#!/usr/bin/env python3
"""MS_SOC - CIPP standards in Security baselines (CLAUDE.md 5fw, 31 X 2026).

Author: Piotr Wisniewski.
Owner, 31 X 2026: "would github.com/CyberDrain/CIPP help next to Tenable, Maester and SCuBA? - yes, add it in the scope
you said, and keep watching that JSON all the time; whatever they change goes into our daily sentences and into Today".
CIPP (CyberDrain Improved Partner Portal, AGPL-3.0) is a multi-tenant portal for Microsoft partners that ENFORCES its
"standards" (report, alert or remediate) rather than only testing them. Its public repository keeps every standard in one
file, frontend/src/data/standards.json (the same list its standards page shows). We read that file - nothing is run in a
tenant, no secret is used (GITHUB_TOKEN only raises the GitHub API rate limit for the commit date).
Kept from each standard (the agreed scope - no long descriptions are copied): the id, the label, CIPP's category, the
impact, the date CIPP added it, the framework tags (CIS Microsoft 365, NIST CSF, Essential 8, EIDSCA, CISA), who
recommends it and CIPP's note of the PowerShell / Graph equivalent. Matched to our sources:
  CIS id   -> Maester test CIS.M365.<n> and Tenable's CIS Microsoft 365 Foundations items with number <n>
  EIDSCA   -> Maester test EIDSCA.<x>
  CISA tag -> kept only when ScubaGear knows the id today (27 of CIPP's tags were checked 31 X: 20 are not ScubaGear ids)
Changes between runs become events of the Security baselines (src "CIPP"): standard-new, standard-changed,
standard-removed, cipp-version. The first run records the list without events.
Writes site/data/baselines-cipp.json; memory in data/baselines-cipp/state.json.
"""
import datetime
import hashlib
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site", "data", "baselines-cipp.json")
MEM = os.path.join(ROOT, "data", "baselines-cipp", "state.json")
CTL = os.path.join(ROOT, "site", "data", "baselines-controls.json")
REPO = "CyberDrain/CIPP"
PATH = "frontend/src/data/standards.json"
RAW = "https://raw.githubusercontent.com/%s/main/" % REPO
UA = "Mozilla/5.0 (MS_SOC baselines; +https://github.com/wpiotrw/MS_SOC)"
PAGE = "https://standards.cipp.app/"
JSON_URL = "https://github.com/%s/blob/main/%s" % (REPO, PATH)

CAT_TECH = {"Entra (AAD) Standards": "Entra ID", "Exchange Standards": "Exchange Online", "SharePoint Standards": "SharePoint Online",
            "Defender Standards": "Defender", "Teams Standards": "Teams", "Intune Standards": "Intune", "Device Management Standards": "Intune",
            "Copilot (M365) Standards": "AI and agents", "Global Standards": "Microsoft 365"}
TEMPLATE_TECH = [(r"ConditionalAccess|PIMRole|GroupTemplate", "Entra ID"), (r"Dlp|Retention|SensitivityLabel|SensitiveInfo", "Purview"),
                 (r"SafeLinks", "Defender"), (r"Transport|ExchangeConnector", "Exchange Online"), (r"Intune|AssignmentFilter|ReusableSettings", "Intune")]
# PowerShell modules Microsoft retired - CIPP's note still names them for some standards
RETIRED = re.compile(r"\b(?:\w+-Msol\w+|\w+-AzureAD\w*)\b")


def log(*a):
    print("baselines_cipp:", *a, flush=True)


def load(p, d):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return d


def save(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    txt = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    old = open(p, encoding="utf-8").read() if os.path.exists(p) else None
    def bare(t):
        try:
            o = json.loads(t)
            o.pop("generated", None)
            return json.dumps(o, sort_keys=True)
        except ValueError:
            return t
    if old is None or bare(old) != bare(txt):
        with open(p, "w", encoding="utf-8") as f:
            f.write(txt)
        return True
    return False


def get(url, headers=None, timeout=60):
    h = {"User-Agent": UA}
    h.update(headers or {})
    with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def commit_info():
    h = {"Accept": "application/vnd.github+json"}
    tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if tok:
        h["Authorization"] = "Bearer " + tok
    try:
        c = json.loads(get("https://api.github.com/repos/%s/commits?path=%s&per_page=1" % (REPO, PATH), headers=h))[0]
        return c["sha"][:7], (c["commit"]["committer"]["date"] or "")[:10], c.get("html_url") or ""
    except Exception as e:
        log("commit date not read:", e)
        return "", "", ""


def fetch():
    """the standards and CIPP's version: from GitHub, or from a local checkout (CIPP_DIR) for a test run"""
    loc = os.environ.get("CIPP_DIR")
    if loc:
        std = load(os.path.join(loc, PATH), None)
        ver = (load(os.path.join(loc, "frontend/public/version.json"), {}) or {}).get("version", "")
        return std, ver, ("local", "", "")
    std = json.loads(get(RAW + PATH))
    try:
        ver = json.loads(get(RAW + "frontend/public/version.json")).get("version", "")
    except Exception:
        ver = ""
    return std, ver, commit_info()


def tech_of(s):
    if s.get("cat") == "Templates":
        for rx, t in TEMPLATE_TECH:
            if re.search(rx, s.get("name") or ""):
                return t
        return "Microsoft 365"
    return CAT_TECH.get(s.get("cat"), "Microsoft 365")


def tags(s):
    out = {"cis": [], "nist": [], "e8": [], "eidsca": [], "cisaTag": [], "other": []}
    for t in s.get("tag") or []:
        t = str(t)
        m = re.match(r"CIS M365 [\d.]+ \(([\d.]+)\)", t)
        if m:
            out["cis"].append(m.group(1)); continue
        m = re.match(r"NIST CSF [\d.]+ \((.+)\)", t)
        if m:
            out["nist"].append(m.group(1)); continue
        m = re.match(r"Essential 8 \((.+)\)", t)
        if m:
            out["e8"].append(m.group(1)); continue
        if t.startswith("EIDSCA."):
            out["eidsca"].append(t); continue
        m = re.match(r"CISA \((.+)\)", t)
        if m:
            out["cisaTag"].append(m.group(1)); continue
        out["other"].append(t)
    return out


def fpr(x):
    return hashlib.sha1(json.dumps(x, sort_keys=True).encode("utf-8")).hexdigest()[:12]


def run(day, seed=False, maester_tests=None, tenable_items=None):
    """returns (summary for baselines.json, events, per-technology counts); writes baselines-cipp.json and its memory"""
    st = load(MEM, {})
    try:
        std, ver, (commit, committed, curl) = fetch()
    except Exception as e:
        log("not read:", e)
        return {"ok": False, "ver": st.get("ver", ""), "error": str(e)[:200]}, [], {}
    if not isinstance(std, list) or not std:
        log("standards.json empty or not a list")
        return {"ok": False, "ver": st.get("ver", "")}, [], {}

    # counterparts in our sources
    mt = {t["id"]: t for t in (maester_tests or []) if t.get("id")}
    tcis = {}
    for aid, a in (tenable_items or {}).items():
        if not aid.startswith("CIS_Microsoft_365_Foundations"):
            continue
        for i in a.get("items") or []:
            n = str(i.get("n") or "")
            if re.match(r"^\d+(\.\d+)+$", n):
                tcis.setdefault(n, []).append({"a": aid, "f": a.get("file") or aid + ".audit", "k": i.get("k"), "n": n})
    cisa_ids = {p.get("id") for p in ((load(CTL, {}) or {}).get("cisa") or {}).get("policies") or []}

    first = not st.get("fp")
    mute = seed or first
    old_fp, old_snap, first_seen = st.get("fp") or {}, st.get("snap") or {}, st.get("first") or {}
    rows, fps, snap, ev = [], {}, {}, []
    for s in std:
        nm = str(s.get("name") or "")
        if not nm:
            continue
        sid = nm.replace("standards.", "", 1)
        tg = tags(s)
        ps = str(s.get("powershellEquivalent") or "").strip()
        tech = tech_of(s)
        r = {"id": sid, "label": s.get("label") or sid, "cat": s.get("cat") or "", "tech": tech,
             "impact": (s.get("impact") or "").replace(" Impact", ""), "added": s.get("addedDate") or "",
             "cis": tg["cis"], "nist": tg["nist"], "e8": tg["e8"], "eidsca": tg["eidsca"],
             "cisa": [c for c in tg["cisaTag"] if c in cisa_ids], "cisaOld": [c for c in tg["cisaTag"] if c not in cisa_ids],
             "rec": s.get("recommendedBy") or [], "ps": ps if ps.lower() not in ("none", "") else "",
             "retired": bool(RETIRED.search(ps)), "deprecated": bool(s.get("deprecated")), "beta": bool(s.get("beta")),
             "multi": bool(s.get("multiple") or s.get("multi"))}
        r["maester"] = [x for x in ["CIS.M365." + c for c in tg["cis"]] + tg["eidsca"] if x in mt]
        r["tenable"] = [t for c in tg["cis"] for t in tcis.get(c, [])][:6]
        cur = {"label": r["label"], "impact": r["impact"], "tags": sorted(s.get("tag") or []), "deprecated": r["deprecated"], "ps": ps,
               "help": fpr(s.get("helpText") or ""), "docs": fpr(s.get("docsDescription") or ""), "cat": r["cat"]}
        fps[sid] = fpr(cur)
        snap[sid] = {"label": r["label"], "impact": r["impact"], "tech": tech, "tags": cur["tags"], "deprecated": r["deprecated"], "ps": ps,
                     "help": cur["help"], "docs": cur["docs"], "cat": r["cat"]}
        first_seen.setdefault(sid, day if not first else (r["added"] or day))
        r["first"] = first_seen[sid]
        rows.append(r)
        if mute:
            continue
        if sid not in old_fp:
            ev.append({"day": day, "src": "CIPP", "type": "standard-new", "id": sid, "title": r["label"], "tech": tech,
                       "impact": r["impact"], "cis": r["cis"], "added": r["added"], "url": PAGE})
        elif old_fp[sid] != fps[sid]:
            o = old_snap.get(sid) or {}
            what = [k for k, lab in (("label", "name"), ("impact", "impact"), ("tags", "frameworks"), ("deprecated", "deprecated"),
                                     ("ps", "PowerShell equivalent"), ("help", "description"), ("docs", "documentation"), ("cat", "category"))
                    if o.get(k) != snap[sid][k]]
            e = {"day": day, "src": "CIPP", "type": "standard-changed", "id": sid, "title": r["label"], "tech": tech,
                 "what": [dict(label="name", impact="impact", tags="frameworks", deprecated="deprecated", ps="PowerShell equivalent",
                               help="description", docs="documentation", cat="category")[k] for k in what], "url": PAGE}
            if "impact" in what:
                e["was"], e["now"] = o.get("impact"), r["impact"]
            if "label" in what:
                e["wasTitle"] = o.get("label")
            if "tags" in what:
                e["tagsAdded"] = [t for t in snap[sid]["tags"] if t not in (o.get("tags") or [])]
                e["tagsRemoved"] = [t for t in (o.get("tags") or []) if t not in snap[sid]["tags"]]
            if "deprecated" in what:
                e["deprecated"] = r["deprecated"]
            ev.append(e)
    if not mute:
        for sid, o in old_snap.items():
            if sid not in fps:
                ev.append({"day": day, "src": "CIPP", "type": "standard-removed", "id": sid, "title": o.get("label") or sid, "tech": o.get("tech") or "", "url": JSON_URL})
        if st.get("ver") and ver and ver != st.get("ver"):
            ev.append({"day": day, "src": "CIPP", "type": "cipp-version", "id": "cipp", "title": "CIPP " + ver, "was": st.get("ver"), "now": ver,
                       "url": "https://github.com/%s/releases" % REPO})

    # the events of 60 days stay in the memory: every run (twice a day) returns those of the last 14 days, not only its own
    seen = {(e["day"], e["type"], e.get("id")) for e in st.get("events") or []}
    keep = (st.get("events") or []) + [e for e in ev if (e["day"], e["type"], e.get("id")) not in seen]
    cut60 = (datetime.date.fromisoformat(day) - datetime.timedelta(days=60)).isoformat()
    st["events"] = [e for e in keep if e["day"] >= cut60]
    since14 = (datetime.date.fromisoformat(day) - datetime.timedelta(days=14)).isoformat()
    ev = [e for e in st["events"] if e["day"] >= since14]

    # per technology, newest first (the date CIPP added it), then by name - stable sorts, last key first
    rows.sort(key=lambda r: r["label"].lower())
    rows.sort(key=lambda r: r["added"], reverse=True)
    rows.sort(key=lambda r: r["tech"])
    imp = {}
    techs = {}
    for r in rows:
        imp[r["impact"]] = imp.get(r["impact"], 0) + 1
        techs[r["tech"]] = techs.get(r["tech"], 0) + 1
    since30 = (datetime.date.fromisoformat(day) - datetime.timedelta(days=30)).isoformat()
    newest = sorted(rows, key=lambda r: r["added"], reverse=True)[:5]
    summ = {"ok": True, "ver": ver, "commit": commit, "date": committed, "commitUrl": curl, "standards": len(rows),
            "cis": sum(1 for r in rows if r["cis"]), "maester": sum(1 for r in rows if r["maester"]), "tenable": sum(1 for r in rows if r["tenable"]),
            "cisaOk": sum(1 for r in rows if r["cisa"]), "cisaOld": sum(1 for r in rows if r["cisaOld"]),
            "impact": imp, "added30": sum(1 for r in rows if r["added"] >= since30), "retired": sum(1 for r in rows if r["retired"]),
            "newest": [{"id": r["id"], "label": r["label"], "added": r["added"], "tech": r["tech"]} for r in newest],
            "page": PAGE, "json": JSON_URL}
    out = {"generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "day": day, "spec": "5fw",
           "source": summ, "standards": rows,
           "licence": "CIPP is AGPL-3.0 (github.com/CyberDrain/CIPP); this file keeps ids, names, tags, impact and dates only, with links back to CIPP."}
    save(OUT, out)
    st.update({"ver": ver, "commit": commit, "fp": fps, "snap": snap, "first": first_seen, "checked": day})
    save(MEM, st)
    log("CIPP %s, standards.json %s (%s): %d standards, %d with a CIS id, %d matched to Maester, %d events%s" % (
        ver or "?", commit or "?", committed or "?", len(rows), summ["cis"], summ["maester"], len(ev), " (first run: recorded only)" if mute else ""))
    return summ, ev, techs


if __name__ == "__main__":
    d = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
    tests = (load(os.path.join(ROOT, "site", "data", "baselines-tests.json"), {}) or {}).get("tests")
    items = (load(os.path.join(ROOT, "site", "data", "baselines-tenable.json"), {}) or {}).get("audits")
    s, e, t = run(d, maester_tests=tests, tenable_items=items)
    print(json.dumps({"summary": s, "events": e[:10], "techs": t}, ensure_ascii=False, indent=1)[:3000])
