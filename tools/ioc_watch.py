#!/usr/bin/env python3
"""ioc_watch.py - the infrastructure of our incidents: domains and IPs, checked every day (CLAUDE.md 5fb, 23 X 2026).

    python3 tools/ioc_watch.py            # in .github/workflows/ioc-watch.yml; keys come from the environment

Owner, 23 X 2026: "use VirusTotal to follow the domains of a campaign or an incident we describe (PHP2Shell, ConnectWise):
many phishing and malware domains appear - show them, say whether they are real or not, statistics and trend lines;
store the sources in a JSON and use them in our workflow". The sources and their limits are ti_sources.json (5fa); this
script reads ONLY that file for what to use:

  indicators  1. the IOCs of our analyses (notes.iocs of every incident in site/data/threats.json; IPs, and domains /
                 URLs written defanged - evil[.]com, hxxps://)
              2. look-alike candidates from Certificate Transparency (crt.sh): certificates of the last 30 days whose
                 registered domain contains a word of the incident (notes.match: ConnectWise, SkyKick ...) or a word of
                 the watch list (ti_sources.json crt.sh entry, WatchKeywords) - and is not the vendor's own domain
              3. ThreatFox IOCs carrying such a word as a tag (last 30 days)
  checks      VirusTotal (domain / IP report: engine verdicts, categories, creation date), GreyNoise (IP: internet scanner
              or not), URLhaus (host: malware URLs, online / offline), ThreatFox (is the indicator known, which malware)
  budgets     from ti_sources.json Limits: VirusTotal <= VT_MAX per run at 4 a minute, a domain re-checked after
              RECHECK_DAYS; GreyNoise <= GN_MAX per run (50 a week), an IP re-checked after 7 days
  output      site/data/ioc-watch.json (indicators, DEFANGED - the page never prints a live domain) and
              site/data/ioc-watch-history.json (per day, per incident: total, malicious, suspicious, new) -> the trend

A missing key = that source is skipped, with the reason in `sources`; a failed call = the source is `failed` with its
error; the job never fails. VirusTotal adds every queried indicator to its dataset - only public IOCs and look-alike
domains are queried, never anything from a tenant.
"""
import datetime as dt, ipaddress, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "ti_sources.json")
THREATS = os.path.join(ROOT, "site", "data", "threats.json")
OUT = os.path.join(ROOT, "site", "data", "ioc-watch.json")
HIST = os.path.join(ROOT, "site", "data", "ioc-watch-history.json")
UA = "MS_SOC-ioc-watch/1.0 (+https://github.com/wpiotrw/MS_SOC)"
VT_MAX, VT_GAP = 60, 16            # public API: 4 a minute, 500 a day; two runs a day stay far below
GN_MAX, GN_DAYS = 6, 7             # 50 a week with a key
AB_MAX = 120                       # abuse.ch lookups per run (fair use)
RECHECK_DAYS = 3
CT_DAYS, CT_PER_WORD = 30, 40
KEEP_DAYS, HIST_DAYS = 120, 120
SECOND_LEVEL = {"co", "com", "org", "net", "gov", "ac", "edu", "or", "ne", "go"}
BENIGN = re.compile(r"(?i)(^|\.)(microsoft|microsoftonline|office|office365|windows|azure|live|outlook|sharepoint|"
                    r"github|google|apple|amazonaws|cloudflare|virustotal|abuse\.ch|crt\.sh)\.(com|net|org|sh|ch)$")


def now():
    return dt.datetime.now(dt.timezone.utc)


def http(url, method="GET", headers=None, data=None, timeout=45):
    h = {"User-Agent": UA, "Accept": "application/json"}
    h.update(headers or {})
    req = urllib.request.Request(url, method=method, headers=h, data=data)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read() if hasattr(e, "read") else b""


def refang(s):
    return (s.replace("[.]", ".").replace("(.)", ".").replace("{.}", ".").replace("[:]", ":")
            .replace("hxxps", "https").replace("hxxp", "http"))


def defang(v, kind):
    if kind == "ip":
        a = v.rsplit(".", 1)
        return a[0] + "[.]" + a[1] if len(a) == 2 else v
    if kind == "url":
        return v.replace("http", "hxxp", 1).replace(".", "[.]")
    return v.replace(".", "[.]")


def regdom(host):
    p = host.lower().strip(".").split(".")
    if len(p) >= 3 and p[-2] in SECOND_LEVEL and len(p[-1]) == 2:
        return ".".join(p[-3:])
    return ".".join(p[-2:])


IP_RX = re.compile(r"(?<![\d.])(\d{1,3})(?:\[\.\]|\.)(\d{1,3})(?:\[\.\]|\.)(\d{1,3})(?:\[\.\]|\.)(\d{1,3})(?![\d])")
DEF_DOM = re.compile(r"(?i)\b((?:[a-z0-9-]+(?:\[\.\]|\.))*[a-z0-9-]+\[\.\][a-z][a-z0-9-]{1,23})\b")
URL_RX = re.compile(r"(?i)\bhxxps?://[^\s\"'<>)]+")


def extract(text):
    """IPs (public only) and domains / URLs written defanged - a plain domain in prose is not an indicator"""
    out = []
    for m in IP_RX.finditer(text):
        ip = ".".join(m.groups())
        try:
            if ipaddress.ip_address(ip).is_global:
                out.append(("ip", ip))
        except ValueError:
            pass
    for m in URL_RX.finditer(text):
        u = refang(m.group(0)).rstrip(".,;")
        host = urllib.parse.urlparse(u).hostname or ""
        if host and not IP_RX.fullmatch(host):
            out.append(("domain", host.lower()))
    for m in DEF_DOM.finditer(text):
        d = refang(m.group(1)).lower().strip(".")
        if not IP_RX.fullmatch(d) and not BENIGN.search(d):
            out.append(("domain", d))
    return out


def load(p, default):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return default


def main():
    t0 = now()
    today = t0.strftime("%Y-%m-%d")
    stamp = t0.strftime("%Y-%m-%dT%H:%M:%SZ")
    srcs = {s.get("SourceName", ""): s for s in load(SRC, [])}
    def src(prefix):
        return next((s for n, s in srcs.items() if n.startswith(prefix)), {})
    T = load(THREATS, {})
    prev = load(OUT, {})
    old = {i["key"]: i for i in prev.get("indicators") or []}
    rep = {}
    keys = {"vt": os.environ.get("VT_API_KEY", "").strip(), "ab": os.environ.get("ABUSECH_AUTH_KEY", "").strip(),
            "gn": os.environ.get("GREYNOISE_API_KEY", "").strip()}

    # ---- 1. indicators of our analyses ----
    I = {}
    def add(kind, value, story, origin, extra=None):
        k = kind + ":" + value
        o = old.get(k) or {}
        x = I.get(k) or {"key": k, "type": kind, "v": defang(value, kind), "stories": [], "origins": [],
                         "first": o.get("first") or today}
        for f in ("vt", "gn", "uh", "tf", "ct"):
            if f in o and f not in x:
                x[f] = o[f]
        if story and story not in x["stories"]:
            x["stories"].append(story)
        if origin not in x["origins"]:
            x["origins"].append(origin)
        if extra:
            x.update(extra)
        I[k] = x
    words = {}
    for st in T.get("stories") or []:
        n = st.get("notes") or {}
        txt = "\n".join(n.get("iocs") or [])
        for kind, v in extract(txt):
            add(kind, v, st["id"], "analysis")
        # the event's own words (curated match words; never a field word - threat_todo.py check refuses those)
        for w in ((st.get("words") or []) if st.get("curated") else []):   # threats.py: the note's match words, lowercased
            if " " in w.strip():
                continue          # a phrase ("Front Door") is not a brand a look-alike domain would copy
            w2 = re.sub(r"[^a-z0-9-]", "", w.lower())
            if len(w2) >= 6 and not re.match(r"^(storm|cve)-?\d", w2):
                words.setdefault(w2, set()).add(st["id"])
    ct = src("crt.sh")
    for w in ct.get("WatchKeywords") or []:
        w2 = re.sub(r"[^a-z0-9-]", "", str(w).lower())
        if len(w2) >= 6:
            words.setdefault(w2, set()).add("_watch")

    # ---- 2. Certificate Transparency look-alikes ----
    cut = (t0 - dt.timedelta(days=CT_DAYS)).strftime("%Y-%m-%d")
    r = {"state": "ok", "queries": 0, "candidates": 0, "note": ""}
    for w, sids in sorted(words.items()):
        for attempt in (1, 2):    # crt.sh answers 502 under load; one retry
            st, body = http("https://crt.sh/?q=%25" + urllib.parse.quote(w) + "%25&output=json&exclude=expired", timeout=60)
            if st == 200:
                break
            time.sleep(8)
        r["queries"] += 1
        if st != 200:
            r["note"] += "%s: HTTP %s; " % (w, st)
            continue
        try:
            rows = json.loads(body or b"[]")
        except Exception:
            r["note"] += "%s: not JSON; " % w
            continue
        seen = 0
        for row in sorted(rows, key=lambda x: x.get("not_before") or "", reverse=True):
            if (row.get("not_before") or "")[:10] < cut:
                continue
            for name in (row.get("name_value") or "").split("\n"):
                host = name.strip().lower().lstrip("*.")
                if not host or " " in host or "@" in host or not re.match(r"^[a-z0-9.-]+\.[a-z]{2,}$", host):
                    continue
                rd = regdom(host)
                if w.replace("-", "") not in rd.replace("-", "") or rd.split(".")[0] == w.replace("-", "") or BENIGN.search(rd):
                    continue      # the vendor's own domain (connectwise.com) and its subdomains are not look-alikes
                if seen >= CT_PER_WORD:
                    break
                for sid in sids:
                    add("domain", host, None if sid == "_watch" else sid, "crtsh",
                        {"ct": {"word": w, "notBefore": (row.get("not_before") or "")[:10], "issuer": (row.get("issuer_name") or "")[:80]}})
                seen += 1
        r["candidates"] += seen
        time.sleep(2)
    rep["crt.sh"] = r

    # ---- 3. ThreatFox tags (needs the abuse.ch key) ----
    if keys["ab"]:
        r = {"state": "ok", "tags": 0, "iocs": 0, "note": ""}
        for w, sids in sorted(words.items())[:10]:
            st, body = http("https://threatfox-api.abuse.ch/api/v1/", "POST", {"Auth-Key": keys["ab"], "Content-Type": "application/json"},
                            json.dumps({"query": "taginfo", "tag": w, "limit": 50}).encode())
            r["tags"] += 1
            try:
                j = json.loads(body or b"{}")
            except Exception:
                j = {}
            if st != 200:
                r["note"] += "%s: HTTP %s; " % (w, st); continue
            for d in (j.get("data") or []) if isinstance(j.get("data"), list) else []:
                if (d.get("first_seen") or "")[:10] < cut:
                    continue
                v, kind = str(d.get("ioc") or ""), None
                if d.get("ioc_type") == "domain": kind = "domain"
                elif d.get("ioc_type") == "ip:port": kind, v = "ip", v.split(":")[0]
                elif d.get("ioc_type") == "url": kind, v = "domain", (urllib.parse.urlparse(v).hostname or "")
                if not kind or not v:
                    continue
                for sid in sids:
                    add(kind, v.lower(), None if sid == "_watch" else sid, "threatfox-tag", {"tfTag": w})
                r["iocs"] += 1
            time.sleep(1)
        rep["ThreatFox tags"] = r
    else:
        rep["ThreatFox tags"] = {"state": "skipped", "note": "no ABUSECH_AUTH_KEY"}

    def due(x, f, days):
        c = (x.get(f) or {}).get("checked") or ""
        return not c or c[:10] <= (t0 - dt.timedelta(days=days)).strftime("%Y-%m-%d")
    order = sorted(I.values(), key=lambda x: ((x.get("vt") or {}).get("checked") or "", "analysis" not in x["origins"], x["key"]))

    # ---- 4. VirusTotal ----
    if keys["vt"]:
        r = {"state": "ok", "checked": 0, "notFound": 0, "note": ""}
        for x in order:
            if r["checked"] >= VT_MAX:
                break
            if not due(x, "vt", RECHECK_DAYS):
                continue
            v = refang(x["v"])
            path = ("ip_addresses/" if x["type"] == "ip" else "domains/") + urllib.parse.quote(v)
            st, body = http("https://www.virustotal.com/api/v3/" + path, headers={"x-apikey": keys["vt"]})
            r["checked"] += 1
            if st == 429:
                r["state"], r["note"] = "limited", "HTTP 429 - daily or per-minute quota reached"; break
            if st == 404:
                x["vt"] = {"checked": stamp, "notFound": True}; r["notFound"] += 1
            elif st == 200:
                a = (json.loads(body).get("data") or {}).get("attributes") or {}
                s = a.get("last_analysis_stats") or {}
                x["vt"] = {"checked": stamp, "m": s.get("malicious", 0), "s": s.get("suspicious", 0), "h": s.get("harmless", 0),
                           "u": s.get("undetected", 0), "rep": a.get("reputation"),
                           "created": dt.datetime.fromtimestamp(a["creation_date"], dt.timezone.utc).strftime("%Y-%m-%d") if a.get("creation_date") else None,
                           "last": dt.datetime.fromtimestamp(a["last_analysis_date"], dt.timezone.utc).strftime("%Y-%m-%d") if a.get("last_analysis_date") else None,
                           "cats": sorted(set((a.get("categories") or {}).values()))[:4],
                           "owner": a.get("as_owner") or a.get("registrar") or "", "country": a.get("country") or ""}
            else:
                r["note"] += "%s HTTP %s; " % (x["v"], st)
            time.sleep(VT_GAP)
        rep["VirusTotal"] = r
    else:
        rep["VirusTotal"] = {"state": "skipped", "note": "no VT_API_KEY"}

    # ---- 5. GreyNoise (IPs) ----
    r = {"state": "ok", "checked": 0, "note": "with key" if keys["gn"] else "without key (10 a day)"}
    lim = GN_MAX if keys["gn"] else 3
    for x in order:
        if x["type"] != "ip" or r["checked"] >= lim or not due(x, "gn", GN_DAYS):
            continue
        st, body = http("https://api.greynoise.io/v3/community/" + refang(x["v"]), headers={"key": keys["gn"]} if keys["gn"] else {})
        r["checked"] += 1
        if st == 429:
            r["state"], r["note"] = "limited", "HTTP 429 - weekly quota reached"; break
        try:
            j = json.loads(body or b"{}")
        except Exception:
            j = {}
        if st in (200, 404):
            x["gn"] = {"checked": stamp, "noise": bool(j.get("noise")), "riot": bool(j.get("riot")),
                       "cls": j.get("classification") or ("unknown" if st == 404 else ""), "name": j.get("name") or "",
                       "last": j.get("last_seen") or ""}
        else:
            r["note"] += "%s HTTP %s; " % (x["v"], st)
        time.sleep(2)
    rep["GreyNoise"] = r

    # ---- 6. URLhaus and ThreatFox for every indicator ----
    if keys["ab"]:
        ru = {"state": "ok", "checked": 0, "listed": 0, "note": ""}
        rt = {"state": "ok", "checked": 0, "listed": 0, "note": ""}
        for x in order:
            if ru["checked"] >= AB_MAX:
                break
            v = refang(x["v"])
            if due(x, "uh", RECHECK_DAYS):
                st, body = http("https://urlhaus-api.abuse.ch/v1/host/", "POST", {"Auth-Key": keys["ab"]},
                                urllib.parse.urlencode({"host": v}).encode())
                ru["checked"] += 1
                try:
                    j = json.loads(body or b"{}")
                except Exception:
                    j = {}
                if st == 200:
                    urls = j.get("urls") or []
                    x["uh"] = {"checked": stamp, "status": j.get("query_status") or "", "count": len(urls),
                               "online": sum(1 for u in urls if u.get("url_status") == "online"),
                               "threats": sorted({u.get("threat") or "" for u in urls} - {""})[:3],
                               "first": min([u.get("date_added") or "" for u in urls] or [""])[:10]}
                    ru["listed"] += 1 if urls else 0
                else:
                    ru["note"] += "%s HTTP %s; " % (x["v"], st)
            if due(x, "tf", RECHECK_DAYS):
                st, body = http("https://threatfox-api.abuse.ch/api/v1/", "POST", {"Auth-Key": keys["ab"], "Content-Type": "application/json"},
                                json.dumps({"query": "search_ioc", "search_term": v, "exact_match": True}).encode())
                rt["checked"] += 1
                try:
                    j = json.loads(body or b"{}")
                except Exception:
                    j = {}
                if st == 200:
                    d = j.get("data") if isinstance(j.get("data"), list) else []
                    x["tf"] = {"checked": stamp, "count": len(d),
                               "malware": sorted({e.get("malware_printable") or "" for e in d} - {""})[:3],
                               "threat": sorted({e.get("threat_type") or "" for e in d} - {""})[:2],
                               "first": min([e.get("first_seen") or "" for e in d] or [""])[:10]}
                    rt["listed"] += 1 if d else 0
                else:
                    rt["note"] += "%s HTTP %s; " % (x["v"], st)
            time.sleep(0.5)
        rep["URLhaus"], rep["ThreatFox"] = ru, rt
    else:
        rep["URLhaus"] = rep["ThreatFox"] = {"state": "skipped", "note": "no ABUSECH_AUTH_KEY"}

    # ---- 7. verdicts, carried indicators, history ----
    for k, o in old.items():          # an indicator no longer in an analysis stays until KEEP_DAYS after it was first seen
        if k not in I and (o.get("first") or "") >= (t0 - dt.timedelta(days=KEEP_DAYS)).strftime("%Y-%m-%d"):
            I[k] = o
    for x in I.values():
        vt, uh, tf, gn = x.get("vt") or {}, x.get("uh") or {}, x.get("tf") or {}, x.get("gn") or {}
        if (vt.get("m") or 0) >= 2 or uh.get("online") or tf.get("count"):
            verdict = "malicious"
        elif (vt.get("m") or 0) == 1 or (vt.get("s") or 0) >= 1 or uh.get("count") or gn.get("cls") == "malicious":
            verdict = "suspicious"
        elif vt and not vt.get("notFound"):
            verdict = "no detections"
        else:
            verdict = "not checked yet" if not vt else "unknown to VirusTotal"
        x["verdict"] = verdict
    inds = sorted(I.values(), key=lambda x: ({"malicious": 0, "suspicious": 1}.get(x["verdict"], 2), x["first"], x["key"]))
    H = load(HIST, {"days": {}})
    row = {}
    for x in inds:
        for sid in x["stories"] or ["_watch"]:
            c = row.setdefault(sid, {"total": 0, "malicious": 0, "suspicious": 0, "new": 0})
            c["total"] += 1
            c["malicious"] += x["verdict"] == "malicious"
            c["suspicious"] += x["verdict"] == "suspicious"
            c["new"] += x["first"] == today
    H["days"][today] = row
    keep = sorted(H["days"])[-HIST_DAYS:]
    H["days"] = {d: H["days"][d] for d in keep}
    H["source"] = "tools/ioc_watch.py (CLAUDE.md 5fb)"
    titles = {st["id"]: st["title"] for st in T.get("stories") or []}
    body = {"source": "tools/ioc_watch.py (CLAUDE.md 5fb)", "sources": rep, "words": {w: sorted(s) for w, s in sorted(words.items())},
            "titles": titles, "counts": {v: sum(1 for x in inds if x["verdict"] == v) for v in
                                         ("malicious", "suspicious", "no detections", "unknown to VirusTotal", "not checked yet")},
            "indicators": inds}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(dict(generated=stamp, **body), open(OUT, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    json.dump(H, open(HIST, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print("ioc_watch: %d indicators (%s) | %s | %.0f s" % (len(inds), ", ".join("%s %d" % (k, v) for k, v in body["counts"].items() if v),
          "; ".join("%s %s%s" % (k, v.get("state"), (" (" + v["note"].strip("; ")[:120] + ")") if v.get("note") else "") for k, v in rep.items()),
          (now() - t0).total_seconds()))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print("ioc_watch: skipped - %s" % e)
        sys.exit(0)
