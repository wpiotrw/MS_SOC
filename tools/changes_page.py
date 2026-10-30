#!/usr/bin/env python3
"""changes_page.py - the "What changed" page (/diff/) and its 7-day view (/week/), CLAUDE.md 5eq (21 X 2026).

  python3 tools/changes_page.py [SITE]          # SITE = site (default)

Owner, 21 X 2026: "the diff and week pages show the data far worse and less approachably than the main page; it is very
hard to catch any change - in Graph API, components, roles; rethink both pages tab by tab, section by section" -
decisions: one page with a period switch (since the previous brief | last 7 days), technology as a filter, build it all.

What it does (code only, run by the "Code refresh" workflow after every published run):
  1. site/data/changes-7d.json - the last 7 days of the change register (site/data/changelog.json, written by
     make_diff.py in both routines) cut to what a reader acts on: bookkeeping is dropped (version counters, "changed"
     dates, link checks, rows leaving a rolling list, the watch list itself), the fields of one item are merged into ONE
     record (a Graph permission's endpoints, privilege level and consent in one row), plus the dated events of the
     portal's own data files that the register does not carry: first-party apps (state `fpa.chg`), campaigns
     (campaigns.json), baselines (baselines.json), Threat Research (threats.json), preview-to-GA (doc-ga.json),
     Graph API Radar (graph-radar.json, 5ft), M365 endpoints (m365-endpoints.json, 5fu).
  2. site/diff/index.html and site/week/index.html - the page itself, from tools/changes_app.html (same file; /week/
     opens on "Last 7 days" and offers printing). A page a routine wrote there before (make_diff.py's full comparison,
     write_week()'s summary) is moved aside first: site/diff/full.html, site/week/print.html - both stay linked.
Exit 0 always; prints one line.
"""
import datetime as dt, glob, gzip, json, os, re, shutil, sys

MARK = "data-changes-app"
DAYS = 7
DROP_FIELDS = {"version", "changed", "kind", "Link status", "Link", "Source link", "Newest article", "Note",
               "left the list", "watched", "page", "baseline"}
DROP_KIND_FIELD = {("removed", "what's new"), ("removed", "dated"), ("removed", "left the list")}
PRODUCT = {"Graph API": "Microsoft Graph", "Roles": "Entra"}
TAB_ALIAS = {"Graph endpoints": "Graph API", "Source text": "Microsoft Learn"}


def load(p, default=None):
    try:
        if p.endswith(".gz"):
            return json.load(gzip.open(p, "rt", encoding="utf-8"))
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return default


def newest_state(site):
    days = sorted(f for f in os.listdir(os.path.join(site, "data")) if re.match(r"^\d{4}-\d{2}-\d{2}\.json(\.gz)?$", f))
    for f in reversed(days):
        d = load(os.path.join(site, "data", f))
        if d:
            return f[:10], (d.get("soc-brief-state") or d.get("state") or {})
    return "", {}


def clip(s, n):
    s = "" if s is None else str(s)
    return s if len(s) <= n else s[: n - 1] + "…"


def merge_register(entries, lo):
    """one record per (day, tab, kind, id); bookkeeping fields dropped; a change left with no field is dropped"""
    out, idx, dropped = [], {}, 0
    for e in entries:
        if e.get("seen", "") < lo:
            continue
        f = e.get("field")
        if f in DROP_FIELDS or (e.get("kind"), f) in DROP_KIND_FIELD:
            dropped += 1
            continue
        tab = TAB_ALIAS.get(e.get("tab"), e.get("tab"))
        k = (e["seen"], tab, e.get("kind"), e.get("id"))
        r = idx.get(k)
        if not r:
            r = {"d": e["seen"], "tab": tab, "k": e.get("kind"), "id": clip(e.get("id"), 200),
                 "t": clip(e.get("title") or "", 220), "u": e.get("url") or "", "p": e.get("product") or PRODUCT.get(tab, ""),
                 "w": e.get("weight"), "t0": bool(e.get("tier0")), "ms": e.get("msDate") or "", "f": []}
            if e.get("tab") == "Source text":
                r["src"] = "page text"
            idx[k] = r
            out.append(r)
        if f and f not in ("dated", "published", "what's new", "grantable here"):
            r["f"].append([clip(f, 80), clip(e.get("before"), 300), clip(e.get("after"), 300), clip(e.get("detail") or "", 400)])
        elif f:
            r.setdefault("x", clip(f + (": " + str(e.get("after")) if e.get("after") else ""), 120))
    out = [r for r in out if r["k"] != "changed" or r["f"]]
    return out, dropped


def extras(site, state, lo, hi):
    X = []
    # first-party apps: state fpa.chg {d, t: added|renamed|redirects|scopes|foci, id, n, a/b or add/rem, na/nr, src}
    FPA = {"added": "new app", "renamed": "name", "redirects": "redirect URIs", "scopes": "delegated scopes", "foci": "family of client IDs (FOCI)"}
    for c in ((state.get("fpa") or {}).get("chg") or []):
        d = str(c.get("d") or "")[:10]
        if not (lo <= d <= hi):
            continue
        t = c.get("t") or "change"
        lst = lambda L: ", ".join(str(x[1] if isinstance(x, list) and len(x) > 1 else x) for x in (L or [])[:4])
        if t == "added":
            f = [["first seen", "", "in " + (c.get("src") or "tenant"), ""]]
        elif t in ("redirects", "scopes"):
            na, nr = c.get("na") or len(c.get("add") or []), c.get("nr") or len(c.get("rem") or [])
            f = [[FPA[t], "", ("+%d" % na if na else "") + (" −%d" % nr if nr else ""),
                  clip(("+ " + lst(c.get("add")) if c.get("add") else "") + (" − " + lst(c.get("rem")) if c.get("rem") else ""), 400)]]
        else:
            f = [[FPA.get(t, t), clip(c.get("b"), 160), clip(c.get("a"), 160), ""]]
        X.append({"d": d, "tab": "First-party apps", "k": "added" if t == "added" else "changed", "id": c.get("id") or "",
                  "t": clip(c.get("n") or c.get("id"), 160), "u": "", "p": "Entra", "w": None, "t0": t in ("scopes", "foci"), "f": f})
    camp = load(os.path.join(site, "data", "campaigns.json"), {}) or {}
    names = {c.get("id"): c for c in camp.get("campaigns") or []}
    for e in camp.get("events") or []:
        d = str(e.get("day") or "")[:10]
        if lo <= d <= hi:
            cc = names.get(e.get("cid")) or {}
            X.append({"d": d, "tab": "Campaigns", "k": "added" if e.get("type") in ("new", "created") else "changed",
                      "id": e.get("cid") or "", "t": clip(e.get("name") or cc.get("name"), 200), "u": "", "p": cc.get("tech") or "",
                      "w": None, "t0": False, "f": [[e.get("type") or "event", "", clip(e.get("now") or "", 80), clip(e.get("text") or "", 300)]]})
    base = load(os.path.join(site, "data", "baselines.json"), {}) or {}
    for e in base.get("events") or []:
        d = str(e.get("day") or "")[:10]
        if lo <= d <= hi:
            ty = e.get("type") or ""
            X.append({"d": d, "tab": "Security baselines", "k": "added" if ty.endswith(("added", "-new", "-version")) or ty in ("release", "new") else "removed" if ty.endswith(("removed", "-gone")) else "changed",   # 5fq: test-new / policy-new are additions
                      "id": e.get("id") or "", "t": clip(e.get("title"), 200), "u": e.get("url") or "", "p": e.get("tech") or e.get("src") or "",
                      "w": None, "t0": False, "f": [[ty, "", ", ".join(e.get("what") or []), e.get("src") or ""]]})
    # 5ft (30 X 2026, owner: "Graph radar in /week too"): settings our tenant returned before $metadata knew them (one record
    # each), and the $metadata changes grouped per day, version and type (a weekly schema sync holds hundreds of properties)
    rad = load(os.path.join(site, "data", "graph-radar.json"), {}) or {}
    ST5 = {"new": "undocumented", "learn": "on Learn, not in $metadata", "v1": "in v1.0, missing from beta $metadata"}
    for u in ((rad.get("tenant") or {}).get("undocumented") or []):
        d = str(u.get("first") or "")[:10]
        if lo <= d <= hi:
            nm = (u.get("type") or "") + "." + (u.get("leaf") or str(u.get("prop") or "").split(".")[-1])
            X.append({"d": d, "tab": "Graph API Radar", "k": "added", "id": nm, "t": clip(u.get("human") or nm, 200), "u": "", "p": u.get("cat") or "Microsoft Graph",
                      "w": None, "t0": False,
                      "f": [["our tenant returns it · " + ST5.get(u.get("status") or "new", ""), "", nm, clip((u.get("note") or {}).get("what") or "", 300)]]})
    KL = {"type-new": "new type", "prop-new": "new property", "nav-new": "new navigation", "op-new": "new action / function", "member-new": "new enum value",
          "root-new": "new entity set", "prop-type": "property type changed", "type-removed": "type removed", "prop-removed": "property removed",
          "nav-removed": "navigation removed", "op-removed": "action / function removed", "member-removed": "enum value removed"}
    grp = {}
    for e in rad.get("events") or []:
        d = str(e.get("day") or "")[:10]
        if e.get("kind") == "tenant-undocumented" or not (lo <= d <= hi):
            continue
        g = grp.setdefault((d, e.get("ver") or "", e.get("type") or ""), {"kinds": {}, "cat": e.get("cat") or "", "prom": False})
        g["kinds"].setdefault(e.get("kind"), []).append(e.get("name") or "")
        g["prom"] = g["prom"] or bool(e.get("promoted"))
    for (d, ver, ty), g in grp.items():
        ks = set(g["kinds"])
        k = "added" if all(x.endswith("-new") for x in ks) else "removed" if all(x.endswith("-removed") for x in ks) else "changed"
        X.append({"d": d, "tab": "Graph API Radar", "k": k, "id": ty, "t": clip(ty + " (Graph " + ver + (", promoted to v1.0" if g["prom"] else "") + ")", 200), "u": "",
                  "p": g["cat"] or "Microsoft Graph", "w": None, "t0": False,
                  "f": [[KL.get(kd, kd), "", "%d" % len(v), clip(", ".join(v[:10]) + (" …" if len(v) > 10 else ""), 300)] for kd, v in sorted(g["kinds"].items())]})
    # 5fu (30 X 2026): Microsoft 365 URLs and IP address ranges - one record per change record of a version in the window
    mep = load(os.path.join(site, "data", "m365-endpoints.json"), {}) or {}
    MK = {k: v for k, v in (mep.get("impact") or {}).items()}
    for c in mep.get("changes") or []:
        d = str(c.get("day") or "")[:10]
        if not (lo <= d <= hi):
            continue
        kinds = [(MK.get(i) or [i, "none"])[1] for i in c.get("impact") or []]
        k = "added" if "act" in kinds else "removed" if "tidy" in kinds else "changed"
        labs = ", ".join((MK.get(i) or [i])[0] for i in c.get("impact") or []) or (c.get("disposition") or "change")
        f = []
        for lab, key in (("added URLs", "addUrls"), ("added IP ranges", "addIps"), ("removed URLs", "remUrls"), ("removed IP ranges", "remIps")):
            if c.get(key):
                f.append([lab, "", "%d" % len(c[key]), clip(", ".join(c[key][:12]) + (" …" if len(c[key]) > 12 else ""), 400)])
        if c.get("effective"):
            f.append(["effective date", "", c["effective"], "allow it before this day"])
        X.append({"d": d, "tab": "M365 endpoints", "k": k, "id": "set %s · version %s" % (c.get("set"), c.get("version")),
                  "t": clip("%s · endpoint set %s · %s" % (c.get("areaName") or c.get("area") or "Microsoft 365", c.get("set"), labs), 220),
                  "u": mep.get("list") or "", "p": "Microsoft 365 network", "w": None, "t0": False, "f": f or [[labs, "", "", ""]]})
    thr = load(os.path.join(site, "data", "threats.json"), {}) or {}
    arts = {a["id"]: a for a in thr.get("articles") or []}
    for s in thr.get("stories") or []:
        fs = str(s.get("firstSeen") or "")[:10]
        news = [arts[i] for i in s.get("articles") or [] if i in arts and lo <= str(arts[i].get("firstSeen") or "")[:10] <= hi]
        if lo <= fs <= hi or news:
            X.append({"d": max([fs] + [str(a.get("firstSeen"))[:10] for a in news]) if news else fs, "tab": "Threat Research",
                      "k": "added" if lo <= fs <= hi else "changed", "id": s.get("id"), "t": clip(s.get("title"), 220), "u": "", "p": ", ".join(s.get("areas") or [])[:80],
                      "w": None, "t0": True if s.get("curated") else False,
                      "f": [["new article" if not (lo <= fs <= hi) else "reported", "", (s.get("microsoft") or {}).get("status", ""),
                             clip("; ".join(a.get("source", "") + ": " + a.get("title", "") for a in news[:3]), 400)]]})
    ga = load(os.path.join(site, "data", "doc-ga.json"), {}) or {}
    for e in ga.get("events") or []:
        if lo <= e.get("date", "") <= hi:
            X.append({"d": e["date"], "tab": "Microsoft Learn", "k": "changed", "id": e["url"], "t": clip("Preview → GA: " + e.get("title", ""), 220),
                      "u": e["url"], "p": "Documentation", "w": 2, "t0": False,
                      "f": [["preview label", e.get("before", ""), e.get("title", ""), ("announced in What's new" if e.get("announced") else "not announced in What's new")]]})
    return X


# 5eq: "technology" is a filter over every tab (owner, 21 X: decision B). The register's `product` is a technology on some
# tabs and a SOURCE on others (Community Articles: "MC - Merill", "Hacker News"), so one family is derived per record:
# the product when it names one, else the first family named in the title / id.
TECH = [("Entra", r"\bentra\b|azure ad\b|azure active directory|conditional access|\bmfa\b|passkey|authenticator|cloud sync|entra id|\bpim\b|first-party app"),
        ("Microsoft Graph", r"\bgraph\b"),
        ("Defender", r"defender|\bmde\b|\bmdi\b|\bmdo\b|\bxdr\b"),
        ("Sentinel", r"sentinel"), ("Purview", r"purview|\bdlp\b|sensitivity label|insider risk|ediscovery"),
        ("Intune", r"intune|endpoint manager|autopilot"), ("Exchange", r"exchange|outlook|\bews\b"),
        ("Teams", r"\bteams\b"), ("SharePoint & OneDrive", r"sharepoint|onedrive"), ("Copilot", r"copilot|security copilot"),
        ("Windows", r"windows|\bad fs\b|\badfs\b|active directory|kerberos|bitlocker|\bwsus\b"), ("Azure", r"azure|\barc\b|foundry"),
        ("Threat intelligence", r"threat intel|storm-\d+|threat actor")]


def tech_of(r):
    for v in (r.get("p") or "", (r.get("t") or "") + " " + (r.get("id") or "")):
        for name, rx in TECH:
            if re.search(rx, v, re.I):
                return name
    return ""


def carry(full):
    """what other pages read from /diff/ keeps working: the main page fetches /diff/ for `<div id="diff-meta">` (the
    afternoon pass's items, §5cj) and for the text "what changed YYYY-MM-DD" (the age of the changes page, §5bz) -
    both are copied from the routine's page into the app"""
    try:
        h = open(full, encoding="utf-8", errors="replace").read()
    except OSError:
        return ""
    out = []
    m = re.search(r'<div id="diff-meta"[^>]*>\s*</div>', h) or re.search(r'<div id="diff-meta"[^>]*>', h)
    if m:
        out.append(m.group(0) if m.group(0).endswith("</div>") else m.group(0) + "</div>")
    w = re.search(r"what changed (\d{4}-\d{2}-\d{2})", h)
    if w:
        out.append("<!-- what changed %s -->" % w.group(1))
    return "\n".join(out)


def fix_archive(site, full):
    """the evening routine moves the page it finds at site/diff/index.html to site/history/...-diff.html before writing
    its own - since 5eq that page is this app; the comparison it meant to keep is full.html, so it is put back there"""
    if not os.path.exists(full):
        return
    hs = sorted(glob.glob(os.path.join(site, "history", "*-diff.html")))
    if not hs:
        return
    h = hs[-1]
    if MARK in open(h, encoding="utf-8", errors="replace").read(4000):
        shutil.copyfile(full, h)


def main(site="site"):
    app_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "changes_app.html")
    app = open(app_src, encoding="utf-8").read()
    cl = load(os.path.join(site, "data", "changelog.json"), {}) or {}
    ents = cl.get("entries") or []
    runs = [r for r in (cl.get("runs") or []) if isinstance(r, dict)]
    hi = max([e.get("seen", "") for e in ents] + [""])
    if not hi:
        print("changes_page: no register - nothing written"); return 0
    lo = (dt.date.fromisoformat(hi) - dt.timedelta(days=DAYS - 1)).isoformat()
    sday, state = newest_state(site)
    recs, dropped = merge_register(ents, lo)
    recs += extras(site, state, lo, hi)
    for r in recs:
        r["tc"] = tech_of(r) or ("Entra" if r["tab"] in ("Roles", "First-party apps") else "")
    recs.sort(key=lambda r: (r["d"], r["tab"]), reverse=True)
    prev_day = sorted({r.get("date") for r in runs if r.get("date") and r.get("date") < hi})
    cw = state.get("comparedWith") or {}
    body = {"source": "tools/changes_page.py (CLAUDE.md 5eq)", "day": hi, "from": lo, "days": DAYS,
            "previousBrief": (cw if isinstance(cw, str) else cw.get("date")) or (prev_day[-1] if prev_day else ""),
            "runs": [r for r in runs if r.get("date", "") >= lo], "dropped": dropped, "records": recs}
    out = os.path.join(site, "data", "changes-7d.json")
    old = load(out, {}) or {}
    if {k: v for k, v in old.items() if k != "generated"} != body:
        body = dict(generated=dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), **body)
        json.dump(body, open(out, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    wrote = []
    for sub, aside, rng in (("diff", "full.html", "brief"), ("week", "print.html", "week")):
        d = os.path.join(site, sub)
        os.makedirs(d, exist_ok=True)
        p, a = os.path.join(d, "index.html"), os.path.join(d, aside)
        if os.path.exists(p) and MARK not in open(p, encoding="utf-8", errors="replace").read(4000):
            if sub == "diff":
                fix_archive(site, a)
            shutil.move(p, a)                          # a routine's page: kept, linked from the app
            wrote.append(sub + "/" + aside)
        page = app.replace("@@RANGE@@", rng).replace("@@HOME@@", "../").replace("<!--@@META@@-->", carry(a))
        if not os.path.exists(p) or open(p, encoding="utf-8").read() != page:
            open(p, "w", encoding="utf-8").write(page)
            wrote.append(sub + "/index.html")
    print("changes_page: %d records (%s..%s, %d bookkeeping rows dropped)%s" % (
        len(recs), lo, hi, dropped, (" - wrote " + ", ".join(wrote)) if wrote else " - pages unchanged"))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(*(sys.argv[1:2])))
    except Exception as e:
        print("changes_page: skipped - %s" % e)
        sys.exit(0)
