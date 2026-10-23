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
VT_PIVOT = 6                       # passive-DNS pivots per run (each one VirusTotal request)
GN_MAX, GN_DAYS = 6, 7             # 50 a week with a key
AB_MAX = 120                       # abuse.ch lookups per run (fair use)
MS_MAX = 150                       # Microsoft Threat Intelligence reputation lookups per run
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


PAGES = "cache/ioc-pages.json"
PAGE_DAYS, PAGE_MAX = 7, 25           # re-read an article after a week; at most 25 page reads a run
EXAMPLE = re.compile(r"(?i)contoso|company-?name|example|yourdomain|tenant-?name|fabrikam")
_page_reads = [0]


def page_iocs(link, pages, today):
    if not link:
        return []
    c = pages.get(link)
    if c and c.get("read", "") >= (dt.date.fromisoformat(today) - dt.timedelta(days=PAGE_DAYS)).isoformat():
        return [tuple(z) for z in c.get("iocs") or []]
    if _page_reads[0] >= PAGE_MAX:
        return [tuple(z) for z in (c or {}).get("iocs") or []]
    _page_reads[0] += 1
    st, body = http(link, timeout=30)
    if st != 200:
        return [tuple(z) for z in (c or {}).get("iocs") or []]
    h = (body or b"").decode("utf-8", "replace")
    h = re.sub(r"(?is)<(script|style|noscript)\b.*?</\1>", " ", h)
    found, seen = [], set()
    def txt(x):
        return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", x)).replace("&nbsp;", " ").replace("&#8211;", "-").replace("&amp;", "&").strip()
    # table rows: the indicator and what the other cells say about it ("Passkey support lure", "C2 server")
    for tbl in re.findall(r"(?is)<table\b.*?</table>", h):
      last = ""                          # a description cell spanning several rows (rowspan) belongs to all of them
      for row in re.findall(r"(?is)<tr\b.*?</tr>", tbl):
        cells = [txt(c) for c in re.findall(r"(?is)<t[dh]\b.*?</t[dh]>", row)]
        line = " | ".join(cells)
        if "[.]" not in line and "hxxp" not in line.lower():
            continue
        for kind, v in extract(line):
            if EXAMPLE.search(v):
                continue
            rest = [c for c in cells if refang(c).lower().strip() != v and v not in refang(c).lower()]
            desc = " · ".join(z for z in rest if z and z.lower() not in ("domain", "domains", "ip", "ip address", "ipv4", "url"))[:160]
            if desc and not re.search(r"(?i)^(ip|domain|url)s?$", desc):
                last = desc
            desc = desc or last
            # the same indicator in two tables (a themed list of examples, then the IOC table): keep the fuller description
            old_ = next((f for f in found if f[0] == kind and f[1] == v), None)
            if old_:
                if len(desc) > len(old_[2]) - len("IOC table: "):
                    old_[2] = "IOC table: " + desc
                continue
            seen.add((kind, v))
            found.append([kind, v, "IOC table: " + (desc or "listed without a description")])
    # defanged mentions in the text: the sentence around it
    plain = txt(re.sub(r"(?is)<tr\b.*?</tr>", " ", h))
    for sent in re.split(r"(?<=[.!?])\s+(?=[A-Z])", plain):
        if "[.]" not in sent and "hxxp" not in sent.lower():
            continue
        for kind, v in extract(sent):
            if (kind, v) in seen or EXAMPLE.search(v) or EXAMPLE.search(sent[:0]):
                continue
            seen.add((kind, v))
            found.append([kind, v, "In the text: " + sent[:180]])
    pages[link] = {"read": today, "iocs": found[:200]}
    return [tuple(z) for z in found[:200]]


def ioc_repos(repos, words, add):
    """Shallow-clone each community IOC repository and read the files whose name carries an incident's word."""
    import subprocess, csv, io, tempfile
    r = {"state": "ok", "files": 0, "iocs": 0, "note": ""}
    if not repos:
        return {"state": "skipped", "note": "no Kind ioc-repo in ti_sources.json"}
    for rp in repos:
        d = tempfile.mkdtemp(prefix="iocrepo-")
        url = rp.get("Repo") or ""
        p = subprocess.run(["git", "clone", "-q", "--depth", "1", url, d], capture_output=True, text=True, timeout=180)
        if p.returncode != 0:
            r["note"] += "%s: clone failed; " % url; continue
        base = os.path.join(d, rp.get("Path") or "")
        for fn in sorted(os.listdir(base)) if os.path.isdir(base) else []:
            key = re.sub(r"[^a-z0-9]", "", fn.lower())
            hit = [w for w in words if not w.startswith("story:") and len(w) >= 6 and (w in key or (len(w) >= 8 and w.rstrip("s") in key))]
            if not hit:
                continue
            try:
                raw = open(os.path.join(base, fn), encoding="utf-8-sig", errors="replace").read()
            except Exception:
                continue
            r["files"] += 1
            n = 0
            rows_ = list(csv.reader(io.StringIO(raw)))
            head = [h.strip() for h in rows_[0]] if rows_ and not IP_RX.fullmatch(refang((rows_[0] or [""])[0].strip().lower())) and "." not in (rows_[0] or [""])[0] else None
            for row_ in rows_[(1 if head else 0):REPO_MAX + 1]:
                if not row_:
                    continue
                line = ",".join(row_)
                cols = " · ".join("%s: %s" % (head[i] if head and i < len(head) else "col%d" % i, v.strip()) for i, v in enumerate(row_[1:], 1) if v.strip())[:150]
                cell = row_[0].strip().strip('"').lower()
                cell = refang(cell)
                kind = None
                if IP_RX.fullmatch(cell):
                    try:
                        kind = "ip" if ipaddress.ip_address(cell).is_global else None
                    except ValueError:
                        kind = None
                elif re.fullmatch(r"[a-z0-9-]+(\.[a-z0-9-]+)+", cell) and not BENIGN.search(regdom(cell)):
                    kind = "domain"
                if not kind:
                    continue
                for w in hit:
                    for sid in words[w]:
                        add(kind, cell, None if sid == "_watch" else sid, "ioc-list",
                            {"list": {"repo": rp.get("SourceName"), "file": fn, "url": (rp.get("Site") or "").rstrip("/") + "/blob/main/" + (rp.get("Path") or "") + "/" + fn}},
                            why=(rp.get("Author") or rp.get("SourceName") or "IOC list", "list “%s”%s" % (fn, (" — " + cols) if cols else " — campaign domain list")))
                n += 1
                if n >= REPO_MAX:
                    break
            r["iocs"] += n
    return r


REPO_MAX = 60                         # indicators per community file (VirusTotal can check 60 a run)

COMMON_CAPS = {"AITM", "ADFS", "OAUTH", "AZURE", "ENTRA", "CISA", "CVE", "MFA", "SSPR", "DPAPI", "PHISHING", "MICROSOFT",
               "WINDOWS", "DEFENDER", "SENTINEL", "INTUNE", "GITHUB", "DEVOPS", "KUBERNETES", "HUNTRESS", "RANSOMWARE",
               "CLOUDFLARE", "CYBERARK", "BLIZZARD", "TYPHOON", "TEMPEST", "SLEET", "TOKENS", "ACCESS", "ACTIVE", "DATABASE"}


def title_words(title):
    """Coined names in a title: CamelCase (NeedyMantis), letters with digits (PHP2Shell), a capitalised word of 5+
    letters written in capitals (ARTEX). Never Storm-NNNN or a CVE, never a common product or security word."""
    out = []
    for t in re.findall(r"[A-Za-z][A-Za-z0-9]+", title):
        u = t.upper()
        if len(t) < 5 or u in COMMON_CAPS or re.match(r"(?i)^(storm|cve)\d*$", t):
            continue
        camel = re.search(r"[a-z][A-Z]", t) is not None
        mixed = re.search(r"[A-Za-z]\d|\d[A-Za-z]", t) is not None
        caps = t.isupper() and t.isalpha()
        if camel or mixed or caps:
            w = t.lower()
            if len(w) >= 6 or mixed:
                out.append(w)
    return list(dict.fromkeys(out))


def ms_reputation(order, due, stamp):
    """Microsoft's own verdict on a host (Graph threatIntelligence/hosts/{id}/reputation: classification unknown /
    neutral / suspicious / malicious, score 0-100). Needs the tenant app (GitHub OIDC, the same federated credential as
    fpa-tenant.yml) with the application permission ThreatIntelligence.Read.All - available with a Defender XDR or Sentinel
    licence. Without them the source is skipped with the reason."""
    req = ("AZURE_TENANT_ID", "AZURE_CLIENT_ID", "ACTIONS_ID_TOKEN_REQUEST_URL", "ACTIONS_ID_TOKEN_REQUEST_TOKEN")
    if not all(os.environ.get(k) for k in req):
        return {"state": "skipped", "note": "no tenant sign-in in this run (OIDC variables missing)"}
    try:
        st, b = http(os.environ["ACTIONS_ID_TOKEN_REQUEST_URL"] + "&audience=api://AzureADTokenExchange",
                     headers={"Authorization": "bearer " + os.environ["ACTIONS_ID_TOKEN_REQUEST_TOKEN"]})
        oidc = json.loads(b)["value"]
        st, b = http("https://login.microsoftonline.com/%s/oauth2/v2.0/token" % os.environ["AZURE_TENANT_ID"], "POST",
                     {"Content-Type": "application/x-www-form-urlencoded"},
                     urllib.parse.urlencode({"client_id": os.environ["AZURE_CLIENT_ID"], "scope": "https://graph.microsoft.com/.default",
                                             "grant_type": "client_credentials",
                                             "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
                                             "client_assertion": oidc}).encode())
        tok = json.loads(b)["access_token"]
    except Exception as e:
        return {"state": "failed", "note": "sign-in: %s" % str(e)[:120]}
    r = {"state": "ok", "checked": 0, "note": ""}
    for x in order:
        if r["checked"] >= MS_MAX or not due(x, "ms", RECHECK_DAYS):
            continue
        st, b = http("https://graph.microsoft.com/v1.0/security/threatIntelligence/hosts/" + urllib.parse.quote(refang(x["v"])) + "/reputation",
                     headers={"Authorization": "Bearer " + tok})
        r["checked"] += 1
        if st == 403:
            return {"state": "skipped", "checked": r["checked"], "note": "HTTP 403 - the app needs ThreatIntelligence.Read.All (admin consent) and a Defender XDR or Sentinel licence"}
        if st == 200:
            j = json.loads(b or b"{}")
            x["ms"] = {"checked": stamp, "cls": j.get("classification") or "", "score": j.get("score"),
                       "rules": [z.get("name") or z.get("description") or "" for z in (j.get("rules") or [])][:4]}
        elif st == 404:
            x["ms"] = {"checked": stamp, "cls": "unknown"}
        else:
            r["note"] += "%s HTTP %s; " % (x["v"], st)
        time.sleep(0.4)
    return r


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
    def add(kind, value, story, origin, extra=None, why=None):
        k = kind + ":" + value
        o = old.get(k) or {}
        x = I.get(k) or {"key": k, "type": kind, "v": defang(value, kind), "stories": [], "origins": [],
                         "first": o.get("first") or today}
        for f in ("vt", "gn", "uh", "tf", "ct", "ms", "flaggedOn", "pv", "pivoted", "verdict", "why"):
            if f in o and f not in x:
                x[f] = o[f]
        if story and story not in x["stories"]:
            x["stories"].append(story)
        if origin not in x["origins"]:
            x["origins"].append(origin)
        if extra:
            x.update(extra)
        if why:      # 5fe: WHY this indicator is listed - its role in the attack, in the source's words
            w0 = {"src": why[0], "t": re.sub(r"\s+", " ", why[1]).strip()[:220]}
            W = [z for z in (x.get("why") or []) if z.get("t") != w0["t"]] + [w0]
            rank = lambda z: 0 if z["src"] == "Our analysis" else 1 if z["t"].startswith("IOC table") else 2 if "list “" in z["t"] else 3 if z["src"] == "ThreatFox" else 4
            x["why"] = sorted(W, key=rank)[:5]      # the most telling reasons survive, not the latest
        I[k] = x
    words = {}
    arts = {a.get("id"): a for a in T.get("articles") or []}
    pages = load(PAGES, {})          # 5fe: article link -> {"read": day, "iocs": [[kind, value, why]]}
    for st in T.get("stories") or []:
        n = st.get("notes") or {}
        for line in n.get("iocs") or []:
            for kind, v in extract(line):
                add(kind, v, st["id"], "analysis", why=("Our analysis", line))
        # every story, curated or not: defanged indicators the source articles print in their text
        for aid in st.get("articles") or []:
            a = arts.get(aid) or {}
            for kind, v in extract(a.get("summary") or ""):
                add(kind, v, st["id"], "article", why=(a.get("source") or "Article", "named in the article summary"))
            # 5fe: the whole article - IOC tables (indicator + the role the author gives it) and defanged mentions
            for kind, v, why in page_iocs(a.get("link"), pages, today):
                add(kind, v, st["id"], "article", {"art": a.get("link")}, why=(a.get("source") or "Article", why))
        # every story: the coined names in its title (PHP2Shell, NeedyMantis, EvilTokens, ARTEX) - what a campaign's
        # domains copy; scales to any new incident that enters the filters, no list to keep
        for w in title_words(st.get("title") or ""):
            words.setdefault(w, set()).add(st["id"])
        # the event's own words (curated match words; never a field word - threat_todo.py check refuses those)
        for w in ((st.get("words") or []) if st.get("curated") else []):   # threats.py: the note's match words, lowercased
            if " " in w.strip():
                continue          # a phrase ("Front Door") is not a brand a look-alike domain would copy
            w2 = re.sub(r"[^a-z0-9-]", "", w.lower())
            if len(w2) >= 6 and not re.match(r"^(storm|cve)-?\d", w2):
                words.setdefault(w2, set()).add(st["id"])
    ct = src("crt.sh")
    labels = {}
    for w in ct.get("WatchKeywords") or []:          # "copilot" or {"word": "copilot", "label": "Copilot look-alikes"}
        lab = w.get("label") if isinstance(w, dict) else None
        w = w.get("word") if isinstance(w, dict) else w
        w2 = re.sub(r"[^a-z0-9-]", "", str(w or "").lower())
        if len(w2) >= 6:
            words.setdefault(w2, set()).add("_watch")
            labels[w2] = lab or w2
    # a watched brand (copilot, passkey, onedrive...) belongs to every story that names it
    for st in T.get("stories") or []:
        blob = ((st.get("title") or "") + " " + " ".join(st.get("words") or [])).lower()
        for w2 in labels:
            if w2 in blob:
                words[w2].add(st["id"])

    # ---- 1b. community IOC lists (ti_sources.json Kind "ioc-repo": Steven Lim's SlimKQL IOC folder...) ----
    # a file whose name carries an incident's word (greynoise_php2shell_attacker_ips.csv -> PHP2Shell,
    # EvilTokens26Apr.csv -> EvilTokens) gives that incident its indicators, with the file as the reason
    rep["IOC lists"] = ioc_repos([s_ for s_ in srcs.values() if s_.get("Kind") == "ioc-repo"], words, add)

    # ---- 2. Certificate Transparency look-alikes ----
    cut = (t0 - dt.timedelta(days=CT_DAYS)).strftime("%Y-%m-%d")
    r = {"state": "ok", "queries": 0, "candidates": 0, "note": ""}
    ctvol = {}
    for w, sids in sorted(words.items()):
        for attempt in (1, 2):    # crt.sh answers 502 under load; one retry
            # identity= matches the word inside a name (q= matches whole tokens only: %copilot% found 0, identity= 862)
            st, body = http("https://crt.sh/?identity=%25" + urllib.parse.quote(w) + "%25&output=json&exclude=expired", timeout=120)
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
        seen, vol = 0, set()
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
                vol.add((rd, (row.get("not_before") or "")[:10]))
                if seen >= CT_PER_WORD:
                    continue      # keep counting the volume; only the newest CT_PER_WORD go on to the reputation checks
                for sid in sids:
                    add("domain", host, None if sid == "_watch" else sid, "crtsh",
                        {"ct": {"word": w, "notBefore": (row.get("not_before") or "")[:10], "issuer": (row.get("issuer_name") or "")[:80]}})
                seen += 1
        r["candidates"] += seen
        # volume per certificate day: distinct registrable domains (a.example.com and b.example.com count once)
        vd = {}
        for rd_, d_ in vol:
            vd.setdefault(d_, set()).add(rd_)
        ctvol[w] = {d_: len(v) for d_, v in vd.items()}
        time.sleep(2)
    rep["crt.sh"] = r

    # ---- 3. ThreatFox tags (needs the abuse.ch key) ----
    if keys["ab"]:
        r = {"state": "ok", "tags": 0, "iocs": 0, "note": ""}
        for w, sids in sorted(words.items()):       # every watched word (5fe: was the first 10 alphabetically)
            if w.startswith("story:"):
                continue
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
                    add(kind, v.lower(), None if sid == "_watch" else sid, "threatfox-tag", {"tfTag": w},
                        why=("ThreatFox", "%s · %s · tagged “%s” · confidence %s%% · reported %s" % (
                            {"botnet_cc": "botnet command-and-control server", "payload_delivery": "serves malware payloads",
                             "cc_skimming": "card-skimming server", "payload": "malware file"}.get(d.get("threat_type"), d.get("threat_type") or "indicator"),
                            d.get("malware_printable") or "unknown malware", w, d.get("confidence_level"), (d.get("first_seen") or "")[:10])))
                r["iocs"] += 1
            time.sleep(1)
        rep["ThreatFox tags"] = r
    else:
        rep["ThreatFox tags"] = {"state": "skipped", "note": "no ABUSECH_AUTH_KEY"}

    def due(x, f, days):
        c = (x.get(f) or {}).get("checked") or ""
        return not c or c[:10] <= (t0 - dt.timedelta(days=days)).strftime("%Y-%m-%d")
    order = sorted(I.values(), key=lambda x: ((x.get("vt") or {}).get("checked") or "", "analysis" not in x["origins"], x["key"]))

    # ---- 3a. carried indicators join BEFORE the checks (pivot and certificate finds of earlier runs stay "not checked
    # yet" forever otherwise - seen 23 X: 5 pivot domains never reached VirusTotal) ----
    for k, o in old.items():
        if k not in I and (o.get("first") or "") >= (t0 - dt.timedelta(days=KEEP_DAYS)).strftime("%Y-%m-%d"):
            I[k] = dict(o)

    # ---- 3b. VirusTotal pivot: other domains that resolved to an incident's bad IP (passive DNS) ----
    # crt.sh substring search returns a different, truncated slice each time (862 rows, then 125; it missed
    # copilot-cloud-microsoft[.]com), so new campaign domains are found by pivoting from what is known bad.
    pv_used = 0
    if keys["vt"]:
        for x in sorted(I.values(), key=lambda x: (x.get("pivoted") or "", x["key"])):
            if pv_used >= VT_PIVOT:
                break
            if x["type"] != "ip" or not ({"analysis", "article"} & set(x["origins"])) or x.get("verdict", (old.get(x["key"]) or {}).get("verdict")) != "malicious":
                continue
            if (x.get("pivoted") or "") > (t0 - dt.timedelta(days=RECHECK_DAYS)).strftime("%Y-%m-%dT"):
                continue
            st, body = http("https://www.virustotal.com/api/v3/ip_addresses/%s/resolutions?limit=40" % refang(x["v"]), headers={"x-apikey": keys["vt"]})
            pv_used += 1
            x["pivoted"] = stamp
            if st == 200:
                for d in json.loads(body).get("data") or []:
                    a = d.get("attributes") or {}
                    host = (a.get("host_name") or "").lower()
                    when = dt.datetime.fromtimestamp(a["date"], dt.timezone.utc).strftime("%Y-%m-%d") if a.get("date") else today
                    if host and not BENIGN.search(regdom(host)) and when >= (t0 - dt.timedelta(days=KEEP_DAYS)).strftime("%Y-%m-%d"):
                        for sid in x["stories"]:
                            add("domain", host, sid, "vt-pivot", {"pv": {"from": x["v"], "date": when}})
            elif st == 429:
                break
            time.sleep(VT_GAP)

    # ---- 4. VirusTotal ----
    # the pivot added domains after the queue was built - rebuild it so they are checked in this run
    order = sorted(I.values(), key=lambda x: ((x.get("vt") or {}).get("checked") or "", not ({"analysis", "article"} & set(x["origins"])), x["key"]))
    if keys["vt"]:
        r = {"state": "ok", "checked": 0, "notFound": 0, "note": "", "pivots": pv_used}
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
                           # which engines call it malicious / suspicious, and what they call it ("Fortinet: phishing")
                           "engines": sorted([{"e": e, "r": (v.get("result") or v.get("category") or "")[:40], "c": v.get("category")}
                                              for e, v in (a.get("last_analysis_results") or {}).items()
                                              if v.get("category") in ("malicious", "suspicious")], key=lambda z: (z["c"] != "malicious", z["e"]))[:12],
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

    # ---- 6b. Microsoft Threat Intelligence host reputation (the owner's tenant, Graph, ThreatIntelligence.Read.All) ----
    rep["Microsoft TI"] = ms_reputation(order, due, stamp)

    # ---- 7. verdicts, carried indicators, history ----
    for k, o in old.items():          # an indicator no longer in an analysis stays until KEEP_DAYS after it was first seen
        if k not in I and (o.get("first") or "") >= (t0 - dt.timedelta(days=KEEP_DAYS)).strftime("%Y-%m-%d"):
            I[k] = o
    for x in I.values():
        vt, uh, tf, gn, ms = x.get("vt") or {}, x.get("uh") or {}, x.get("tf") or {}, x.get("gn") or {}, x.get("ms") or {}
        if (vt.get("m") or 0) >= 2 or uh.get("online") or tf.get("count") or ms.get("cls") == "malicious":
            verdict = "malicious"
        elif (vt.get("m") or 0) == 1 or (vt.get("s") or 0) >= 1 or uh.get("count") or gn.get("cls") == "malicious" or ms.get("cls") == "suspicious":
            verdict = "suspicious"
        elif vt and not vt.get("notFound"):
            verdict = "no detections"
        else:
            verdict = "not checked yet" if not vt else "unknown to VirusTotal"
        x["verdict"] = verdict
        if verdict in ("malicious", "suspicious") and not x.get("flaggedOn"):
            x["flaggedOn"] = today          # the day a service first called it bad (the trend "already flagged" counts these)
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
    # per watched word (a campaign: copilot, passkey, an incident's brand): new look-alike domains per certificate day,
    # how many a service already calls bad, which engines say so
    camp = {}
    stitle = {st["id"]: st.get("title") or st["id"] for st in T.get("stories") or []}
    for x in inds:
        w = (x.get("ct") or {}).get("word")
        if not w and x.get("pv") and x["stories"]:
            w = "story:" + x["stories"][0]          # pivot discoveries: one series per incident
            labels.setdefault(w, "Same IP as " + stitle.get(x["stories"][0], x["stories"][0])[:70])
            words.setdefault(w, set()).update(x["stories"])
        if not w:
            continue
        c = camp.setdefault(w, {"label": labels.get(w) or w, "stories": sorted(words.get(w, [])), "days": {}, "weeks": {},
                                "total": 0, "flagged": 0, "malicious": 0, "engines": {}})
        d0 = (x.get("ct") or {}).get("notBefore") or (x.get("pv") or {}).get("date") or x["first"]
        wk = dt.date.fromisoformat(d0).strftime("%G-W%V")
        c["days"][d0] = c["days"].get(d0, 0) + 1
        c["weeks"][wk] = c["weeks"].get(wk, 0) + 1
        c["total"] += 1
        c["flagged"] += x["verdict"] in ("malicious", "suspicious")
        c["malicious"] += x["verdict"] == "malicious"
        for e in (x.get("vt") or {}).get("engines") or []:
            c["engines"][e["e"]] = c["engines"].get(e["e"], 0) + 1
    for w, vd in ctvol.items():      # a word with no candidate kept still shows its volume
        c = camp.setdefault(w, {"label": labels.get(w) or w, "stories": sorted(words.get(w, [])), "days": {}, "weeks": {},
                                "total": 0, "flagged": 0, "malicious": 0, "engines": {}})
        c["volume"] = dict(sorted(vd.items()))          # distinct look-alike domains per certificate day, last CT_DAYS
        wk = {}
        for d_, k_ in vd.items():
            z = dt.date.fromisoformat(d_).strftime("%G-W%V"); wk[z] = wk.get(z, 0) + k_
        c["volumeWeeks"] = dict(sorted(wk.items()))
    for w, c in camp.items():
        c["engines"] = sorted(c["engines"].items(), key=lambda z: -z[1])[:10]
        c["vtChecked"] = sum(1 for x in inds if (x.get("ct") or {}).get("word") == w and x.get("vt"))
    H.setdefault("words", {})[today] = {w: {"total": c["total"], "flagged": c["flagged"]} for w, c in camp.items()}
    keep = sorted(H["days"])[-HIST_DAYS:]
    H["days"] = {d: H["days"][d] for d in keep}
    H["source"] = "tools/ioc_watch.py (CLAUDE.md 5fb)"
    titles = {st["id"]: st["title"] for st in T.get("stories") or []}
    json.dump(pages, open(PAGES, "w"), indent=0, sort_keys=True)
    body = {"source": "tools/ioc_watch.py (CLAUDE.md 5fb)", "sources": rep, "words": {w: sorted(s) for w, s in sorted(words.items())},
            "titles": titles, "campaigns": camp, "counts": {v: sum(1 for x in inds if x["verdict"] == v) for v in
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
