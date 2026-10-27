#!/usr/bin/env python3
"""baselines.py - the Baselines tab: what Maester and Tenable test in Microsoft 365, Entra, M365 Apps and AI,
which baseline each test comes from, and what changed (CLAUDE.md 5dv, README 14).

Owner, 15 X 2026: "add Tenable and Maester: from Tenable everything about M365, Entra, M365 Apps, Entra apps and AI,
from Maester all of M365, Entra and AI; from both CIS, CISA SCuBA, NIS2; one tab with views inside; analyses, trends,
test names and solutions laid out like roles and Graph API; versions and dates in rounded frames; trend lines and
charts; compare Maester with Tenable". The portal is statistics only: we NEVER run a test against a tenant; we read
the public catalogues and show the steps to check and to fix.

Reads (all public, no key):
  Maester   git clone of github.com/maester365/maester - every tests/**/Test.<ID>.ps1 carries a [MaesterTest(...)]
            attribute (Id, Title, Product, Feature, Area, Severity, UserImpact, ImplementationCost, Mitre, Control,
            Service, License) and a Test.<ID>.md next to it (what it checks, "Remediation action", related links);
            tests/<suite>/suite.json gives the benchmark versions; GitHub releases API gives the versions.
  Tenable   www.tenable.com/audits/{updated,newest}?page=N - the audit file listings (Next.js page data: name,
            plugin, type, revision, date); www.tenable.com/audits/<id> - one audit file with every item
            (description, solution, references, categories). In scope: baselines_sources.json "tenable.include".
  Upstream  GitHub releases API of cisagov/ScubaGear (which SCuBA version Tenable's audit files follow).

Writes:
  site/data/baselines.json          the tab's summary: counts, Tenable audit files and families, frameworks,
                                    comparison, trends, events of the last 14 days, versions (Overview, /diff/ and
                                    /week/ read only this one - about 60 kB)
  site/data/baselines-tests.json    the Maester catalogue: every test with what it checks and how to fix it
  site/data/baselines-tenable.json  the Tenable items of the newest audit file of every family (read when the
                                    Tenable view or a panel needs them - kept out of the first file for phones)
  site/data/baselines-history.json  the collector's memory: month-end counts since 2024 (seeded from Maester's git
                                    history), daily snapshots, first-seen day per test and audit, fingerprints,
                                    events of 60 days

Usage: python3 tools/baselines.py [--seed MONTHLY.json] [--maester DIR] [--offline-tenable] [--day YYYY-MM-DD]
  --seed     first run: month-end ID sets from Maester's git history (tools/baselines.py --backfill writes them);
             records everything without events, so /diff/ does not get 600 "new test" rows on day one
  --backfill DIR OUT   write the month-end ID sets of the Maester clone DIR (full history, blobless) to OUT
Exit code 0 when at least one source was read; a source that fails keeps its last data from the history."""
import datetime, hashlib, json, os, re, subprocess, sys, tempfile, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "site", "data")
OUT = os.path.join(DATA, "baselines.json")
OUT_T = os.path.join(DATA, "baselines-tenable.json")
OUT_M = os.path.join(DATA, "baselines-tests.json")
HIST = os.path.join(DATA, "baselines-history.json")
CFG = os.path.join(ROOT, "baselines_sources.json")
UA = "Mozilla/5.0 (MS_SOC baselines; +https://github.com/wpiotrw/MS_SOC)"

PRODUCT = {"entra": "Entra ID", "defender": "Defender", "exchange": "Exchange Online", "intune": "Intune", "teams": "Teams",
           "sharepoint": "SharePoint Online", "purview": "Purview", "microsoft-365": "Microsoft 365",
           "copilot-studio": "Copilot Studio", "azure": "Azure", "power-platform": "Power Platform"}
SUITES = [("MT", "Maester"), ("CIS", "CIS"), ("CISA", "CISA SCuBA"), ("EIDSCA", "EIDSCA"), ("ORCA", "ORCA")]
SEV_ORDER = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3, "Info": 4}


def log(*a):
    print("baselines:", *a, flush=True)


def warsaw_today():
    try:
        from zoneinfo import ZoneInfo
        return datetime.datetime.now(ZoneInfo("Europe/Warsaw")).date().isoformat()
    except Exception:
        return datetime.datetime.utcnow().date().isoformat()


def now_utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def get(url, tries=3, timeout=60, headers=None):
    h = {"User-Agent": UA}
    h.update(headers or {})
    last = None
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=timeout) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:  # network errors are expected sometimes; the caller keeps the old data
            last = e
            time.sleep(2 + 3 * i)
    raise RuntimeError("GET %s failed: %s" % (url, last))


def gh_api(path):
    h = {"Accept": "application/vnd.github+json"}
    tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if tok:
        h["Authorization"] = "Bearer " + tok
    try:
        return json.loads(get("https://api.github.com/" + path, headers=h, tries=2))
    except Exception:
        # a workstation with the gh CLI (or the session's gh) - same public data
        r = subprocess.run(["gh", "api", path], capture_output=True, text=True, timeout=120)
        if r.returncode:
            raise
        return json.loads(r.stdout)


def load(p, dflt):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return dflt


def dump(p, obj, pretty=False):
    txt = json.dumps(obj, ensure_ascii=False, indent=1 if pretty else None, separators=None if pretty else (",", ":"), sort_keys=False)
    old = open(p, encoding="utf-8").read() if os.path.exists(p) else None
    def bare(t):          # the run time alone is not a change: no commit, no deployment, when only "generated" moved
        try:
            o = json.loads(t)
            o.pop("generated", None)
            return json.dumps(o, sort_keys=True)
        except Exception:
            return t
    if old is None or bare(old) != bare(txt):
        open(p, "w", encoding="utf-8").write(txt)
        return True
    return False


def fp(*parts):
    return hashlib.sha1("␟".join(str(x) for x in parts).encode("utf-8")).hexdigest()[:12]


def mdy(s):
    """Tenable date m/d/yyyy -> yyyy-mm-dd"""
    m = re.match(r"^(\d{1,2})/(\d{1,2})/(\d{4})$", s or "")
    return "%s-%02d-%02d" % (m.group(3), int(m.group(1)), int(m.group(2))) if m else ""


def clip(s, n):
    s = (s or "").strip()
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + " …"


def label(slug):
    if isinstance(slug, list):
        slug = slug[0] if slug else ""
    s = (slug or "").replace("-", " ").strip()
    fix = {"ai": "AI and agents", "mfa": "MFA", "dlp": "DLP", "pim": "PIM", "spf": "SPF", "dkim": "DKIM", "dmarc": "DMARC"}
    if s.lower() in fix:
        return fix[s.lower()]
    return s[:1].upper() + s[1:]


# ---------------------------------------------------------------------------------------------- Maester
ID_BROAD = (r"MT\.[0-9]{4}|CIS(\.M365\.| )[0-9]+(\.[0-9]+)+|CIS M365 v[0-9.]+|(CISA\.)?MS\.(AAD|EXO|DEFENDER|SHAREPOINT|TEAMS|"
            r"POWERPLATFORM|POWERBI)\.[0-9]+\.[0-9]+|EIDSCA\.[A-Z]{2}[0-9]{2}|ORCA\.[0-9]{3}(\.[0-9]+)?")


def norm_id(x):
    if x.startswith("MT."):
        return "MT", x
    if x.startswith("CIS M365 v"):
        return "CISV", x[10:].rstrip(".")
    m = re.match(r"CIS(?:\.M365\.| )(\d+(?:\.\d+)+)", x)
    if m:
        return "CIS", "CIS.M365." + m.group(1)
    if x.startswith("EIDSCA"):
        return "EIDSCA", x
    if x.startswith("ORCA"):
        return "ORCA", x
    return "CISA", "CISA." + re.sub(r"^CISA\.", "", x)


def backfill(repo, out):
    """month-end ID sets from Maester's git history (one-time seed; the daily run adds today's set itself)"""
    def run(*a):
        return subprocess.run(["git", "-C", repo] + list(a), capture_output=True, text=True).stdout
    res, d = [], datetime.date(2024, 2, 1)
    end = datetime.date.today() + datetime.timedelta(days=1)
    while d <= end:
        c = run("rev-list", "-1", "--before=" + min(d, end).isoformat(), "HEAD").strip()
        if c:
            ids = {"MT": set(), "CIS": set(), "CISA": set(), "EIDSCA": set(), "ORCA": set(), "CISV": set()}
            for x in run("grep", "-h", "-o", "-E", ID_BROAD, c, "--", "tests").split("\n"):
                if x.strip():
                    k, v = norm_id(x.strip())
                    ids[k].add(v)
            res.append({"date": min(d - datetime.timedelta(days=1), datetime.date.today()).isoformat(), "commit": c[:10],
                        "cisVersions": sorted(ids.pop("CISV")), "ids": {k: sorted(v) for k, v in ids.items()}})
            log("backfill", res[-1]["date"], {k: len(v) for k, v in res[-1]["ids"].items()})
        d = (d.replace(day=28) + datetime.timedelta(days=4)).replace(day=1)
    json.dump(res, open(out, "w"))


ATTR_RE = re.compile(r"\[MaesterTest\((.*?)\)\]\s*\[", re.S)
KV_RE = re.compile(r"(\w+)\s*=\s*(\((?:'(?:[^']|'')*'|\s|,)*\)|'(?:[^']|'')*'|\$\w+|-?\d+)")


def parse_attr(txt):
    m = ATTR_RE.search(txt)
    if not m:
        return None
    out = {}
    for k, v in KV_RE.findall(m.group(1)):
        if v.startswith("("):
            out[k] = [x.replace("''", "'") for x in re.findall(r"'((?:[^']|'')*)'", v)]
        elif v.startswith("'"):
            out[k] = v[1:-1].replace("''", "'")
        else:
            out[k] = v
    return out


def parse_md(txt):
    txt = (txt or "").replace("﻿", "")
    txt = re.sub(r"<!---?\s*Results\s*-?-->.*", "", txt, flags=re.S).replace("%TestResult%", "").strip()
    parts = re.split(r"^#{2,4}\s*(.+?)\s*:?\s*$", txt, flags=re.M)
    head, sec = parts[0].strip(), {}
    for i in range(1, len(parts) - 1, 2):
        sec[parts[i].strip().rstrip(":").lower()] = parts[i + 1].strip()
    fix = ""
    for k in sec:
        if k.startswith("remediation"):
            fix = sec[k]
            break
    links = []
    for k in sec:
        if "link" in k or "learn more" in k or "reference" in k:
            for t, u in re.findall(r"(?:\[([^\]]+)\]\()?(https?://[^\s)<>\]]+)", sec[k]):
                links.append({"t": clip(t or "", 90), "u": u.rstrip(".,")})
    for t, u in re.findall(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", head + "\n" + fix):
        links.append({"t": clip(t, 90), "u": u})
    seen, uniq = set(), []
    for l in links:
        if l["u"] not in seen:
            seen.add(l["u"])
            uniq.append(l)
    return {"summary": head, "fix": fix, "links": uniq[:8]}


def maester_clone(path):
    if path:
        return path
    d = tempfile.mkdtemp(prefix="maester-")
    subprocess.run(["git", "clone", "-q", "--depth", "1", "https://github.com/maester365/maester.git", d], check=True)
    return d


def maester_read(repo, cfg):
    excl = set(cfg.get("excludeProducts") or [])
    head = subprocess.run(["git", "-C", repo, "log", "-1", "--format=%H %cI"], capture_output=True, text=True).stdout.split()
    tests, skipped = [], {}
    for base, _dirs, files in os.walk(os.path.join(repo, "tests")):
        for f in files:
            m = re.match(r"^Test\.(.+)\.ps1$", f)
            if not m:
                continue
            p = os.path.join(base, f)
            src = open(p, encoding="utf-8-sig", errors="replace").read()
            a = parse_attr(src)
            if not a or not a.get("Id"):
                continue
            for k in ("Product", "RelatedProduct", "Feature", "Area", "Severity", "Title", "UserImpact", "ImplementationCost"):
                if isinstance(a.get(k), list):
                    a[k] = a[k][0] if a[k] else ""
            prod = a.get("Product") or ""
            if prod in excl:
                skipped[prod] = skipped.get(prod, 0) + 1
                continue
            tid = a["Id"]
            suite = next((s for s, _n in SUITES if tid.startswith(s + ".")), None)
            if not suite:
                skipped["other:" + tid.split(".")[0]] = skipped.get("other:" + tid.split(".")[0], 0) + 1
                continue
            mdp = p[:-4] + ".md"
            md = parse_md(open(mdp, encoding="utf-8-sig", errors="replace").read() if os.path.exists(mdp) else "")
            fn = re.search(r"function\s+(Test-[\w-]+)", src)
            reads = sorted(set(re.findall(r"-RelativeUri\s+['\"]([^'\"$]+)['\"]", src)))[:6]
            rel = os.path.relpath(p, repo).replace(os.sep, "/")
            mitre = a.get("Mitre") or []
            mitre = [mitre] if isinstance(mitre, str) else mitre
            ctl = a.get("Control") or []
            ctl = [ctl] if isinstance(ctl, str) else ctl
            area = a.get("Area") or ""
            t = {"id": tid, "suite": suite, "title": (a.get("Title") or "").strip(), "sev": a.get("Severity") or "",
                 "prod": PRODUCT.get(prod, label(prod)), "rel": PRODUCT.get(a.get("RelatedProduct") or "", label(a.get("RelatedProduct") or "")),
                 "feat": label(a.get("Feature") or ""), "area": label(area), "ai": area == "ai" or prod == "copilot-studio",
                 "impact": a.get("UserImpact") or "", "cost": a.get("ImplementationCost") or "",
                 "mitre": [x for x in mitre if x and x != "None"], "ctl": ctl, "svc": a.get("Service") or "",
                 "lic": a.get("License") or "", "fn": fn.group(1) if fn else "", "src": rel, "reads": reads,
                 "sum": clip(md["summary"], 900), "fix": clip(md["fix"], 2600), "links": md["links"]}
            if isinstance(t["svc"], list):
                t["svc"] = ", ".join(t["svc"])
            if isinstance(t["lic"], list):
                t["lic"] = ", ".join(t["lic"])
            tests.append(t)
    tests.sort(key=lambda x: (x["suite"], ver_key(x["id"])))
    suites = {}
    for sj in ("cis", "cisa", "eidsca", "orca", "maester"):
        d = load(os.path.join(repo, "tests", sj, "suite.json"), {})
        if d:
            suites[sj] = {"name": d.get("Name"), "upstream": (d.get("Upstream") or {}).get("Name"), "url": (d.get("Upstream") or {}).get("Url"),
                          "versions": {f.get("Key"): f.get("Version") for f in (d.get("Frameworks") or [])}}
    return {"commit": head[0][:10] if head else "", "committed": head[1] if len(head) > 1 else "", "tests": tests,
            "skipped": skipped, "suites": suites}


def ls_remote_tags(url):
    r = subprocess.run(["git", "ls-remote", "--tags", "--refs", url], capture_output=True, text=True, timeout=120)
    return [l.split("refs/tags/", 1)[1] for l in r.stdout.splitlines() if "refs/tags/" in l]


def maester_releases(cfg, hist_repo=None):
    try:
        rel = gh_api(cfg["releasesApi"])
    except Exception as e:
        log("releases: API not read (%s); tags from git" % e)
        try:
            tags = [t for t in ls_remote_tags(cfg["repo"]) if re.match(r"^v?\d+\.\d+", t)]
        except Exception:
            return None
        out = []
        for t in tags:
            d = ""
            if hist_repo:
                d = subprocess.run(["git", "-C", hist_repo, "log", "-1", "--format=%cs", t], capture_output=True, text=True).stdout.strip()
            out.append({"tag": t, "date": d, "pre": "preview" in t, "url": "https://github.com/maester365/maester/releases/tag/" + t})
        out.sort(key=lambda r: (r["date"], ver_key(r["tag"])), reverse=True)
        return out[:30]
    out = []
    for r in rel:
        if r.get("draft"):
            continue
        out.append({"tag": r.get("tag_name"), "date": (r.get("published_at") or "")[:10], "pre": bool(r.get("prerelease")),
                    "url": r.get("html_url")})
    return out


# ---------------------------------------------------------------------------------------------- Tenable
NEXT_RE = re.compile(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', re.S)


def next_data(html):
    m = NEXT_RE.search(html)
    if not m:
        raise RuntimeError("no page data")
    return json.loads(m.group(1))["props"]["pageProps"]


FILEREV = re.compile(r"^v\d+\.\d+(?:\.\d+)?$")


def split_name(name):
    """'CIS Microsoft 365 Foundations v7.0.0 L1 E3' -> family, version, profile.
    The version is the first v-token (v7.0.0, v2r5, v151) - or a bare number right before Tenable's own file revision
    ('MSCT M365 Apps for enterprise 2512 v1.0.0', 'MSCT Office 365 ProPlus 1908 v1.0.0'); '365' and 'Windows 11' stay
    in the family name."""
    tok = name.split()
    for i in range(1, len(tok)):
        t, nxt = tok[i], tok[i + 1] if i + 1 < len(tok) else ""
        bare = (re.match(r"^\d{4}$", t) or (re.match(r"^\d{2,3}$", t) and tok[i - 1].lower() == "version")) and FILEREV.match(nxt)
        if re.match(r"^v\d+(?:\.\d+)*(?:r\d+)?$", t, re.I) or bare:
            fam, ver, rest = " ".join(tok[:i]), t, tok[i + 1:]
            if rest and FILEREV.match(rest[0]) and (bare or re.match(r"^v\d+$", t)):
                rest = rest[1:]                               # Tenable's file revision after an MSCT version
            fam = re.sub(r"^(?:MSCT )?Microsoft 365 Apps for Enterprise$|^MSCT M365 Apps for enterprise$", "MSCT M365 Apps for enterprise", fam, flags=re.I)
            fam = re.sub(r"^MSCT (?:Microsoft )?[Ee]dge(?: Version)?$", "MSCT Edge", fam)
            fam = re.sub(r"^MSCT Office 365 ProPlus$", "MSCT M365 Apps for enterprise", fam)   # the same Microsoft baseline before its rename
            ver = ver[1:] if re.match(r"^v\d+\.\d", ver) else ver
            if fam == "MSCT Edge" and re.match(r"^\d+$", ver):
                ver = "v" + ver
            return fam, ver, " ".join(rest).strip(" -")
    return name, "", ""


def ver_key(v):
    return [(0, int(x), "") if x.isdigit() else (1, 0, x) for x in re.findall(r"\d+|[a-z]+", (v or "").lower())]


def tenable_list(cfg):
    audits = {}
    for tpl in cfg["listings"]:
        first = next_data(get(tpl.format(n=1)))
        pages = (int(first.get("total") or 0) + 49) // 50
        for n in range(1, pages + 1):
            pp = first if n == 1 else next_data(get(tpl.format(n=n)))
            for a in pp.get("audits") or []:
                s = a.get("_source") or {}
                audits[a["_id"]] = {"id": a["_id"], "name": s.get("display_name") or a["_id"], "plugin": (s.get("plugin") or {}).get("type") or "",
                                    "type": s.get("type") or "", "rev": s.get("revision") or "", "date": mdy(s.get("date")),
                                    "replacedBy": s.get("replaced_by") or ""}
            time.sleep(0.6)
    return audits


def tenable_scope(audits, cfg):
    inc = [(re.compile(r["re"], re.I), r["tech"]) for r in cfg["include"]]
    out = []
    for a in audits.values():
        tech = next((t for rx, t in inc if rx.search(a["name"])), None)
        if not tech:
            continue
        fam, ver, prof = split_name(a["name"])
        a = dict(a, tech=tech, family=fam, ver=ver, profile=prof)
        out.append(a)
    # newest version of each family is "current"; older files are its history (frames on the page)
    best = {}
    for a in out:
        k = a["family"]
        if k not in best or ver_key(a["ver"]) > ver_key(best[k]):
            best[k] = a["ver"]
    for a in out:
        a["current"] = a["ver"] == best[a["family"]]
    out.sort(key=lambda a: (a["tech"], a["family"], ver_key(a["ver"]), a["profile"]))
    return out


def item_number(desc, typ):
    m = re.match(r"^\s*(MS\.[A-Z]+\.\d+\.\d+v\d+)\s*[-–:]\s*(.*)$", desc or "", re.S)
    if m:
        return m.group(1), m.group(2).strip()
    m = re.match(r"^\s*(\d+(?:\.\d+)+)\s+(.*)$", desc or "", re.S)
    if m:
        return m.group(1), m.group(2).strip()
    m = re.match(r"^\s*([A-Z]{2,}-[\w.-]+)\s*[-–:]\s*(.*)$", desc or "", re.S)
    if m:
        return m.group(1), m.group(2).strip()
    return "", (desc or "").strip()


def tenable_items(aid, tpl):
    a = next_data(get(tpl.format(id=aid), timeout=90))["audit"]
    out = []
    for it in a.get("items") or []:
        s = it.get("_source") or {}
        n, t = item_number(s.get("description") or "", a.get("type"))
        out.append({"k": (it.get("_id") or "").split(":")[-1], "n": n, "t": clip(t, 240),
                    "cat": (s.get("references_categories") or [])[:3],
                    "nist": [r.split("|", 1)[1] for r in (s.get("references") or []) if r.startswith("800-53|")][:6],
                    "sol": clip(s.get("solutions"), 1000), "info": clip(s.get("infos"), 300),
                    "see": (s.get("see_also") or [])[:2]})
    if len(out) == 1 and re.search(r"\.audit from ", out[0]["t"] or ""):
        out = []                                              # Tenable's page lists the file itself, not its items yet
        return {"count": 0, "pending": True, "file": a.get("filename") or "", "date": mdy(a.get("date")), "rev": a.get("revision") or "", "items": []}
    return {"count": a.get("item_counts") or len(out), "file": a.get("filename") or "", "date": mdy(a.get("date")),
            "rev": a.get("revision") or "", "items": out}


# ---------------------------------------------------------------------------------------------- build
def scuba_num(n):
    return re.sub(r"v\d+$", "", n or "")


def build(day, seed, args, cfg, hist):
    ev = []
    prev = hist.get("state") or {}
    first_seen = hist.setdefault("firstSeen", {})
    src_ok = {}

    # ---- Maester
    M = None
    try:
        repo = maester_clone(args.get("maester"))
        M = maester_read(repo, cfg["maester"])
        src_ok["maester"] = True
        log("maester", len(M["tests"]), "tests in scope; skipped", M["skipped"])
    except Exception as e:
        log("maester: not read:", e)
    prevOut = load(OUT, {})
    prevTests = load(OUT_M, {}).get("tests")
    if M is None and prevTests:
        M = {"commit": prevOut["sources"]["maester"].get("commit"), "committed": prevOut["sources"]["maester"].get("committed"),
             "tests": prevTests, "skipped": {}, "suites": {}}
    rel = maester_releases(cfg["maester"], args.get("history")) or hist.get("releases") or []
    hist["releases"] = rel
    try:
        sg = gh_api(cfg["upstream"]["scubagear"])
        scuba_up = {"tag": (sg.get("tag_name") or "").lstrip("v"), "date": (sg.get("published_at") or "")[:10], "url": sg.get("html_url")}
        hist["scubagear"] = scuba_up
    except Exception as e:
        log("scubagear: API not read (%s); tags from git" % e)
        try:
            tags = sorted([t.lstrip("v") for t in ls_remote_tags("https://github.com/cisagov/ScubaGear.git") if re.match(r"^v?\d+\.\d+\.\d+$", t)], key=ver_key)
            scuba_up = {"tag": tags[-1], "date": "", "url": "https://github.com/cisagov/ScubaGear/releases/tag/v" + tags[-1]} if tags else hist.get("scubagear")
        except Exception:
            scuba_up = hist.get("scubagear")
        if scuba_up and hist.get("scubagear", {}).get("tag") == scuba_up.get("tag") and hist["scubagear"].get("date"):
            scuba_up = hist["scubagear"]
        hist["scubagear"] = scuba_up

    # ---- Tenable
    T, items = None, load(OUT_T, {}).get("audits", {})
    try:
        allA = tenable_list(cfg["tenable"])
        T = tenable_scope(allA, cfg["tenable"])
        src_ok["tenable"] = True
        fw = {k: [a["name"] for a in allA.values() if re.search(rx, a["name"], re.I)] for k, rx in cfg["tenable"]["frameworkWords"].items()}
        hist["frameworkWords"] = {"day": day, "found": fw, "listed": len(allA)}
        log("tenable", len(allA), "audit files listed,", len(T), "in scope")
    except Exception as e:
        log("tenable listing: not read:", e)
        T = (prevOut.get("tenable") or {}).get("audits") or []
    # items for the newest file of each family (fetched again when the file's date or revision changed)
    pa = (prev.get("audits") or {})
    newitems = {}
    for a in T:
        if not a["current"]:
            continue
        old = items.get(a["id"])
        if old and old.get("date") == a["date"] and old.get("rev") == a["rev"] and not args.get("refetch"):
            newitems[a["id"]] = old
            continue
        try:
            newitems[a["id"]] = tenable_items(a["id"], cfg["tenable"]["audit"])
            time.sleep(0.8)
        except Exception as e:
            log("items not read for", a["id"], e)
            if old:
                newitems[a["id"]] = old
    items = newitems
    for a in T:
        a["items"] = (items.get(a["id"]) or {}).get("count") if a["current"] else None
        if a["current"] and (items.get(a["id"]) or {}).get("pending"):
            a["pending"] = True

    # ---- events (never on --seed)
    tests = M["tests"] if M else []
    tid = {t["id"]: t for t in tests}
    ph = prev.get("tests") or {}
    for t in tests:
        h = fp(t["title"], t["sev"], t["fix"], t["sum"])
        if t["id"] not in first_seen:
            first_seen[t["id"]] = day
        if ph and t["id"] not in ph and not seed:
            ev.append({"day": day, "src": "Maester", "type": "test-new", "id": t["id"], "title": t["title"], "tech": t["prod"], "sev": t["sev"]})
        elif ph and t["id"] in ph and ph[t["id"]]["h"] != h and not seed:
            what = [k for k, v in (("title", ph[t["id"]].get("title") != t["title"]), ("severity", ph[t["id"]].get("sev") != t["sev"])) if v] or ["text"]
            e = {"day": day, "src": "Maester", "type": "test-changed", "id": t["id"], "title": t["title"], "tech": t["prod"], "what": what}
            if "severity" in what:
                e["was"], e["now"] = ph[t["id"]].get("sev"), t["sev"]
            if "title" in what:
                e["wasTitle"] = ph[t["id"]].get("title")
            ev.append(e)
    if M and ph and not seed:
        for k, v in ph.items():
            if k not in tid:
                ev.append({"day": day, "src": "Maester", "type": "test-removed", "id": k, "title": v.get("title"), "tech": v.get("prod")})
    prel = set(prev.get("releases") or [])
    for r in rel:
        if prel and r["tag"] not in prel and not seed:
            ev.append({"day": day, "src": "Maester", "type": "release", "id": r["tag"], "title": "Maester " + r["tag"] + (" (preview)" if r["pre"] else ""), "date": r["date"], "url": r["url"]})
    pv = prev.get("versions") or {}
    curv = {"cis-m365": ((M or {}).get("suites", {}).get("cis", {}).get("versions") or {}).get("cis-m365"),
            "cisa-scuba": ((M or {}).get("suites", {}).get("cisa", {}).get("versions") or {}).get("cisa-scuba"),
            "scubagear": (scuba_up or {}).get("tag")}
    for k, v in curv.items():
        if pv.get(k) and v and pv[k] != v and not seed:
            ev.append({"day": day, "src": "Maester" if k != "scubagear" else "CISA", "type": "version", "id": k, "title": {"cis-m365": "Maester follows CIS Microsoft 365 Foundations", "cisa-scuba": "Maester follows CISA SCuBA", "scubagear": "ScubaGear release"}[k], "was": pv[k], "now": v})
    for a in T:
        if a["id"] not in first_seen:
            first_seen[a["id"]] = day
        o = pa.get(a["id"])
        if pa and not o and not seed:
            ev.append({"day": day, "src": "Tenable", "type": "audit-new", "id": a["id"], "title": a["name"], "tech": a["tech"], "date": a["date"]})
        elif o and (o.get("date") != a["date"] or o.get("rev") != a["rev"] or (a["items"] is not None and o.get("items") not in (None, a["items"]))) and not seed:
            e = {"day": day, "src": "Tenable", "type": "audit-updated", "id": a["id"], "title": a["name"], "tech": a["tech"], "date": a["date"]}
            if o.get("rev") != a["rev"]:
                e["was"], e["now"] = o.get("rev"), a["rev"]
            if a["items"] is not None and o.get("items") not in (None, a["items"]):
                e["itemsWas"], e["itemsNow"] = o.get("items"), a["items"]
            ev.append(e)
    if src_ok.get("tenable") and pa and not seed:
        cur = {a["id"] for a in T}
        for k, o in pa.items():
            if k not in cur:
                ev.append({"day": day, "src": "Tenable", "type": "audit-gone", "id": k, "title": o.get("name"), "tech": o.get("tech")})
    # item level: new / removed items inside the newest file of a family, compared by number
    pit = prev.get("items") or {}
    for aid, d in items.items():
        a = next((x for x in T if x["id"] == aid), None)
        nums = sorted({i["n"] or i["k"] for i in d["items"]})
        was = pit.get(aid)
        if was is not None and not seed:
            add = [n for n in nums if n not in set(was)]
            gone = [n for n in was if n not in set(nums)]
            if add or gone:
                ev.append({"day": day, "src": "Tenable", "type": "items", "id": aid, "title": a["name"] if a else aid, "tech": a["tech"] if a else "", "added": add[:30], "removed": gone[:30]})
        pit[aid] = nums

    # ---- mapping Maester <-> Tenable (CIS by benchmark number, SCuBA by policy id)
    tmap = {}
    cis_items, scuba_items = {}, {}
    for aid, d in items.items():
        a = next((x for x in T if x["id"] == aid), None)
        if not a:
            continue
        for i in d["items"]:
            if a["family"] == "CIS Microsoft 365 Foundations" and re.match(r"^\d+(\.\d+)+$", i["n"]):
                cis_items.setdefault(i["n"], []).append({"a": aid, "p": a["profile"], "k": i["k"]})
            if a["family"].startswith("CISA SCuBA") and i["n"].startswith("MS."):
                scuba_items.setdefault(scuba_num(i["n"]), []).append({"a": aid, "p": a["profile"] or a["tech"], "k": i["k"]})
    for t in tests:
        if t["suite"] == "CIS":
            n = t["id"][len("CIS.M365."):]
            if n in cis_items:
                tmap[t["id"]] = cis_items[n]
        if t["suite"] == "CISA":
            n = t["id"][len("CISA."):]
            if n in scuba_items:
                tmap[t["id"]] = scuba_items[n]
    for t in tests:
        if t["id"] in tmap:
            t["tenable"] = tmap[t["id"]][:6]
        t["first"] = first_seen.get(t["id"], day)
    m_cis = {t["id"][len("CIS.M365."):] for t in tests if t["suite"] == "CIS"}
    m_sc = {t["id"][len("CISA."):] for t in tests if t["suite"] == "CISA"}

    # ---- trends
    snaps = hist.setdefault("daily", [])
    mcount = {s: sum(1 for t in tests if t["suite"] == s) for s, _n in SUITES}
    tcount = {"audits": sum(1 for a in T if a["current"]), "files": len(T), "items": sum(d["count"] for d in items.values()),
              "cisItems": len(cis_items), "scubaItems": len(scuba_items)}
    if M and src_ok.get("tenable"):
        snaps[:] = [s for s in snaps if s["day"] != day] + [{"day": day, "maester": dict(mcount, total=len(tests)), "tenable": tcount}]
    snaps[:] = snaps[-400:]
    monthly = hist.setdefault("monthly", [])
    if seed and isinstance(seed, list):
        monthly[:] = [{"date": r["date"], "commit": r.get("commit"), "cis": r.get("cisVersions"), **{k: len(v) for k, v in r["ids"].items()}} for r in seed]
        # first-seen month per test from the seed (better than "today" for a test that existed in 2024)
        for r in seed:
            for k, v in r["ids"].items():
                for i in v:
                    if i in tid and (first_seen.get(i) in (None, day) or first_seen[i] > r["date"]):
                        first_seen[i] = r["date"]
        for t in tests:
            t["first"] = first_seen.get(t["id"], day)
    if M:
        mkey = day[:7]
        row = {"date": day, "commit": M["commit"], "cis": [curv["cis-m365"]] if curv["cis-m365"] else [], **mcount}
        monthly[:] = [r for r in monthly if r["date"][:7] != mkey] + [row]
        monthly.sort(key=lambda r: r["date"])
    added = {}
    for t in tests:
        k = (t["first"] or day)[:7]
        added.setdefault(k, {s: 0 for s, _n in SUITES})[t["suite"]] += 1
    t_month = {}
    for a in T:
        k = (a["date"] or "")[:7]
        if k:
            t_month.setdefault(k, {"files": 0, "current": 0})
            t_month[k]["files"] += 1
            t_month[k]["current"] += 1 if a["current"] else 0
    bulk = sorted({a["date"] for a in T if sum(1 for b in T if b["date"] == a["date"]) >= 25})

    # ---- frameworks and comparison
    cis_T = [a for a in T if a["family"] == "CIS Microsoft 365 Foundations"]
    sc_T = [a for a in T if a["family"].startswith("CISA SCuBA")]
    def tver(lst):
        vs = sorted({a["ver"] for a in lst if a["current"]}, key=ver_key)
        return vs[-1] if vs else ""
    def tdate(lst):
        ds = sorted({a["date"] for a in lst if a["current"] and a["date"]})
        return ds[-1] if ds else ""
    fwk = [
        {"key": "cis-m365", "name": "CIS Microsoft 365 Foundations", "kind": "Industry benchmark",
         "maester": {"n": mcount["CIS"], "ver": curv["cis-m365"] or "", "ids": "CIS.M365.*"},
         "tenable": {"n": len(cis_items), "ver": tver(cis_T), "date": tdate(cis_T), "files": [a["id"] for a in cis_T if a["current"]]},
         "both": len(m_cis & set(cis_items)), "onlyM": len(m_cis - set(cis_items)), "onlyT": len(set(cis_items) - m_cis),
         "note": "Maester and Tenable follow the same CIS version" if curv["cis-m365"] and curv["cis-m365"] == tver(cis_T) else "Maester and Tenable follow different CIS versions"},
        {"key": "cisa-scuba", "name": "CISA SCuBA (Microsoft 365)", "kind": "Government baseline (US)",
         "maester": {"n": mcount["CISA"], "ver": curv["cisa-scuba"] or "", "ids": "CISA.MS.*"},
         "tenable": {"n": len(scuba_items), "ver": tver(sc_T), "date": tdate(sc_T), "files": [a["id"] for a in sc_T if a["current"]]},
         "upstream": scuba_up or {}, "both": len(m_sc & set(scuba_items)), "onlyM": len(m_sc - set(scuba_items)), "onlyT": len(set(scuba_items) - m_sc)},
        {"key": "nis2", "name": "NIS2 (EU 2022/2555)", "kind": "EU regulation",
         "maester": {"n": 0, "ver": "", "ids": ""}, "tenable": {"n": len((hist.get("frameworkWords") or {}).get("found", {}).get("nis2") or []), "ver": "", "date": ""},
         "checked": (hist.get("frameworkWords") or {}).get("day") or day, "listed": (hist.get("frameworkWords") or {}).get("listed"),
         "names": ((hist.get("frameworkWords") or {}).get("found") or {}).get("nis2") or [],
         "note": "Neither catalogue has a NIS2 suite or audit file for Microsoft 365 (checked on every run). The tests carry NIST SP 800-53 controls instead."},
        {"key": "maester-mt", "name": "Maester's own tests", "kind": "Tool (community)", "maester": {"n": mcount["MT"], "ver": "", "ids": "MT.*"}, "tenable": {"n": 0}},
        {"key": "eidsca", "name": "EIDSCA (Entra ID Security Config Analyzer)", "kind": "Tool (community)", "maester": {"n": mcount["EIDSCA"], "ver": "", "ids": "EIDSCA.*"}, "tenable": {"n": 0}},
        {"key": "orca", "name": "ORCA (Office 365 Recommended Configuration Analyzer)", "kind": "Tool (community)", "maester": {"n": mcount["ORCA"], "ver": "", "ids": "ORCA.*"}, "tenable": {"n": 0}},
    ]
    fams = {}
    for a in T:
        f = fams.setdefault(a["family"], {"family": a["family"], "tech": a["tech"], "type": a["type"], "versions": {}})
        v = f["versions"].setdefault(a["ver"] or "-", {"ver": a["ver"], "date": a["date"], "files": 0, "current": a["current"]})
        v["files"] += 1
        v["date"] = max(v["date"] or "", a["date"] or "")
    for f in fams.values():
        f["versions"] = sorted(f["versions"].values(), key=lambda v: ver_key(v["ver"]))
        f["newest"] = f["versions"][-1]["ver"]
        f["newestDate"] = f["versions"][-1]["date"]
        cur = [a for a in T if a["family"] == f["family"] and a["current"]]
        f["items"] = sum(a["items"] or 0 for a in cur)
        f["profiles"] = [{"id": a["id"], "p": a["profile"], "items": a["items"], "date": a["date"], "rev": a["rev"]} for a in cur]
    for fname, fam in fams.items():
        if fname not in ("CIS Microsoft 365 Foundations",) and not fname.startswith("CISA SCuBA"):
            fwk.append({"key": "t:" + fname, "name": fname, "kind": {"CIS": "Industry benchmark", "MSCT": "Microsoft baseline", "DISA STIG": "Government baseline (US)", "TNS": "Tenable best practice"}.get(fam["type"], fam["type"]),
                        "maester": {"n": 0}, "tenable": {"n": fam["items"], "ver": fam["newest"], "date": fam["newestDate"], "files": [p["id"] for p in fam["profiles"]]}, "tech": fam["tech"]})

    # ---- history bookkeeping
    # a second run on the same day keeps the day's earlier events and adds only what is new since then
    seen = {(e["day"], e["type"], e.get("id")) for e in (hist.get("events") or [])}
    hist["events"] = (hist.get("events") or []) + [e for e in ev if (e["day"], e["type"], e.get("id")) not in seen]
    cut = (datetime.date.fromisoformat(day) - datetime.timedelta(days=60)).isoformat()
    hist["events"] = [e for e in hist["events"] if e["day"] >= cut]
    hist["state"] = {"tests": {t["id"]: {"h": fp(t["title"], t["sev"], t["fix"], t["sum"]), "title": t["title"], "sev": t["sev"], "prod": t["prod"]} for t in tests} if M else prev.get("tests"),
                     "audits": {a["id"]: {"date": a["date"], "rev": a["rev"], "items": a["items"], "name": a["name"], "tech": a["tech"]} for a in T},
                     "items": pit, "releases": [r["tag"] for r in rel], "versions": {k: v for k, v in curv.items() if v} or pv}
    hist["day"] = day

    techs = {}
    for t in tests:
        x = techs.setdefault(t["prod"], {"tech": t["prod"], "maester": 0, "high": 0, "tenable": 0})
        x["maester"] += 1
        x["high"] += 1 if t["sev"] in ("High", "Critical") else 0
    for a in T:
        if a["current"]:
            techs.setdefault(a["tech"], {"tech": a["tech"], "maester": 0, "high": 0, "tenable": 0})["tenable"] += a["items"] or 0
    since14 = (datetime.date.fromisoformat(day) - datetime.timedelta(days=14)).isoformat()
    sev = {}
    for t in tests:
        sev[t["sev"] or "-"] = sev.get(t["sev"] or "-", 0) + 1
    out = {
        "generated": now_utc(), "day": day, "spec": "5dv",
        "sources": {"maester": {"ok": bool(src_ok.get("maester")), "commit": (M or {}).get("commit"), "committed": (M or {}).get("committed"),
                                "repo": "https://github.com/maester365/maester", "docs": "https://maester.dev/docs/tests/"},
                    "tenable": {"ok": bool(src_ok.get("tenable")), "listed": (hist.get("frameworkWords") or {}).get("listed"),
                                "url": "https://www.tenable.com/audits"}},
        "counts": {"tests": len(tests), "high": sum(1 for t in tests if t["sev"] in ("High", "Critical")), "ai": sum(1 for t in tests if t["ai"]),
                   "suites": mcount, "sev": sev, "tenableFiles": len(T), "tenableCurrent": tcount["audits"], "tenableItems": tcount["items"],
                   "mapped": len(tmap), "events14": sum(1 for e in hist["events"] if e["day"] >= since14)},
        "releases": rel[:20], "versions": curv, "frameworks": fwk, "techs": sorted(techs.values(), key=lambda x: -(x["maester"] + x["tenable"])),
        "tenable": {"audits": T, "families": sorted(fams.values(), key=lambda f: (f["tech"], f["family"])), "bulkDates": bulk},
        "trends": {"monthly": monthly, "added": [dict(m=k, **v) for k, v in sorted(added.items())], "tenableMonths": [dict(m=k, **v) for k, v in sorted(t_month.items())],
                   "daily": snaps[-120:]},
        "events": [e for e in hist["events"] if e["day"] >= since14],
    }
    return out, {"day": day, "generated": out["generated"], "audits": items}, {"day": day, "generated": out["generated"], "tests": tests}


def more(out, day, seed, mtests, items):
    """CLAUDE.md 5fq (27 X 2026): CISA ScubaGear (the source the SCuBA files of Maester and Tenable follow), the Intune
    security baselines (Learn) and Microsoft's Zero Trust Assessment - tools/baselines_more.py; a failure there never
    stops the Maester and Tenable part"""
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import baselines_more
        summ, ev = baselines_more.run(day, seed=bool(seed), maester_tests=mtests.get("tests"), tenable_items=items.get("audits"))
    except Exception as e:
        log("more sources: not read:", e)
        return
    out["spec"] = "5dv+5fq"
    out["sources"]["cisa"] = summ["cisa"]
    out["sources"]["intune"] = summ["intune"]
    out["sources"]["zta"] = summ["zta"]
    out["more"] = {"techs": summ["techs"], "history": summ.get("history") or {}}
    since14 = (datetime.date.fromisoformat(day) - datetime.timedelta(days=14)).isoformat()
    out["events"] = sorted(out["events"] + [e for e in ev if e["day"] >= since14], key=lambda e: e["day"], reverse=True)
    out["counts"]["events14"] = len(out["events"])
    c = summ["cisa"]
    for f in out["frameworks"]:
        if f["key"] == "cisa-scuba" and c.get("ok"):
            f["cisa"] = {"n": c["policies"], "bod": c["bod"], "shall": c["shall"], "ver": c["ver"], "date": c["date"], "commit": c["commit"], "lag": c.get("lag")}
            if c.get("lag") and c["lag"]["behind"]:
                f["note"] = "Tenable's SCuBA files follow v%s; CISA ScubaGear is at v%s (%d release%s newer). Maester follows ScubaGear main but still uses the 1.x ids for %d of its tests." % (
                    c["lag"]["tenable"], c["lag"]["cisa"], c["lag"]["behind"], "" if c["lag"]["behind"] == 1 else "s", c["gaps"].get("maesterOld", 0))
    z = summ["zta"]
    if z.get("ok"):
        out["frameworks"].insert(3, {"key": "zta", "name": "Zero Trust Assessment (Microsoft)", "kind": "Microsoft assessment tool", "maester": {"n": 0}, "tenable": {"n": 0},
                                     "zta": {"n": z["tests"], "ver": z["ver"], "date": z["date"]}, "note": "Microsoft's own PowerShell assessment: Identity, Devices, Data, Network, AI, SecOps"})
    ib = [b for b in summ["intune"]["baselines"] if not b["missing"]]
    if ib:
        out["frameworks"].insert(4, {"key": "intune-sb", "name": "Intune security baselines (Microsoft)", "kind": "Microsoft baseline", "maester": {"n": 0}, "tenable": {"n": 0},
                                     "intune": {"n": sum(b["n"] for b in ib), "baselines": len(ib), "newest": [b["title"] for b in ib]},
                                     "note": "Settings and defaults of the newest version of every Intune security baseline (Learn)"})


def main(argv):
    args, i = {}, 0
    while i < len(argv):
        a = argv[i]
        if a == "--backfill":
            backfill(argv[i + 1], argv[i + 2])
            return 0
        if a in ("--seed", "--maester", "--day", "--history"):
            args[a[2:]] = argv[i + 1]
            i += 2
            continue
        if a == "--refetch":
            args["refetch"] = True
        i += 1
    cfg = load(CFG, None)
    if not cfg:
        raise SystemExit("baselines.py: baselines_sources.json not readable")
    day = args.get("day") or warsaw_today()
    hist = load(HIST, {})
    seed = load(args["seed"], None) if args.get("seed") else None
    if args.get("seed") and seed is None:
        raise SystemExit("baselines.py: seed file not readable")
    out, items, mtests = build(day, seed if seed is not None else False, args, cfg, hist)
    if not out["sources"]["maester"]["ok"] and not out["sources"]["tenable"]["ok"]:
        log("no source read; nothing written")
        return 1
    more(out, day, seed, mtests, items)
    c1 = dump(OUT, out)
    c2 = dump(OUT_T, items) | dump(OUT_M, mtests)
    c3 = dump(HIST, hist)
    log("written" if (c1 or c2 or c3) else "unchanged", "tests", out["counts"]["tests"], "tenable files", out["counts"]["tenableFiles"],
        "events today", sum(1 for e in out["events"] if e["day"] == day))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
