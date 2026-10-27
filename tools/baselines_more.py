#!/usr/bin/env python3
"""baselines_more.py - the three sources the Baselines tab gained on 27 X 2026 (CLAUDE.md 5fq), next to Maester and
Tenable (tools/baselines.py calls this module at the end of every run; it can also run alone for a test).

Owner, 27 X 2026: "we track Tenable and Maester but not CISA SCuBA - add it, sort it nicely in the tab where Tenable and
Maester are, list the differences, and for every source say clearly what to check in the tenant (M365, M365 security)
to be compliant; check again whether Tenable really has no update; show it so nobody gets lost and sees what to look
at in our M365 / Entra / Purview / EXO; links to the PDFs and to single controls; changes in Today, Overview, the
sentences, /diff and /week under one name" - answers: layout "technology first", name "Security baselines", and also
"Intune security baselines" and "Zero Trust Assessment".

Reads (all public, no key; the portal never runs a test against a tenant):
  CISA SCuBA   git clone (sparse) of github.com/cisagov/ScubaGear: PowerShell/ScubaGear/baselines/*.md - every policy
               (MS.<PRODUCT>.<n>.<m>v<k>) with its statement, SHALL/SHOULD, the BOD 25-01 badge, automated or manual
               check, rationale, last modified, NIST SP 800-53 and MITRE ATT&CK mapping, the section's resources,
               licence and the policy's implementation steps; removedpolicies.md; tags (git ls-remote) for versions.
  Intune       our own copy of the Learn reference pages of the Intune security baselines (mirror/learn/intune/.../
               security-baselines/ref-*.md, workflow learn-mirror.yml): every baseline, its versions (zone pivots) and
               the settings with their baseline default; the newest version is compared with the one before.
  ZTA          git clone (sparse) of github.com/microsoft/zerotrustassessment: src/powershell/tests/Test-Assessment.
               <id>.ps1 ([ZtTest(...)] attribute: Title, Pillar, Category, RiskLevel, UserImpact, ImplementationCost,
               licence, service) and the .md next to it (what it checks, remediation); the module version from
               src/powershell/ZeroTrustAssessment.psd1.
Writes:
  site/data/baselines-controls.json  CISA policies per technology with their Maester tests and Tenable items, the
                                     differences between the three, removed policies, the Intune baselines (settings of
                                     the newest version + what changed against the one before) and the ZTA tests -
                                     read when the "By technology" view opens (not by Overview: phones)
  returns to baselines.py: a small summary (versions, counts, lag of Tenable) for baselines.json and the events
  (new / removed / changed policy, test, setting; a new baseline version) that go to Today, Overview, /diff, /week.
History of this module: site/data/baselines-more-history.json (fingerprints, versions, first-seen days)."""
import datetime, glob, hashlib, json, os, re, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "site", "data")
OUT_C = os.path.join(DATA, "baselines-controls.json")
OUT_I = os.path.join(DATA, "baselines-intune.json")
OUT_Z = os.path.join(DATA, "baselines-zta.json")
HIST_X = os.path.join(DATA, "baselines-more-history.json")
MIRROR_IB = os.path.join(ROOT, "mirror", "learn", "intune", "intune", "device-security", "security-baselines")

SCUBA_REPO = "https://github.com/cisagov/ScubaGear"
SCUBA_BLOB = SCUBA_REPO + "/blob/main/PowerShell/ScubaGear/baselines/"
ZTA_REPO = "https://github.com/microsoft/zerotrustassessment"
ZTA_BLOB = ZTA_REPO + "/blob/main/src/powershell/tests/"
BOD = "https://www.cisa.gov/news-events/directives/bod-25-01-implementing-secure-practices-cloud-services"

# ScubaGear baseline file -> (portal technology, where in the tenant, ScubaGear product name)
CISA_FILES = {
    "aad": ("Entra ID", "Microsoft Entra admin center (entra.microsoft.com)", "aad"),
    "securitysuite": ("Defender", "Microsoft Defender portal (security.microsoft.com) and Microsoft Purview portal (purview.microsoft.com)", "securitysuite"),
    "defender": ("Defender", "Microsoft Defender portal (security.microsoft.com)", "defender"),
    "exo": ("Exchange Online", "Exchange admin center (admin.exchange.microsoft.com) and DNS of the domains", "exo"),
    "sharepoint": ("SharePoint Online", "SharePoint admin center (<tenant>-admin.sharepoint.com)", "sharepoint"),
    "teams": ("Teams", "Teams admin center (admin.teams.microsoft.com)", "teams"),
    "powerplatform": ("Power Platform", "Power Platform admin center (admin.powerplatform.microsoft.com)", "powerplatform"),
    "powerbi": ("Power BI", "Fabric / Power BI admin portal (app.powerbi.com > Settings > Admin portal)", "powerbi"),
}
CISA_PREFIX = {"AAD": "aad", "SECURITYSUITE": "securitysuite", "DEFENDER": "defender", "EXO": "exo", "SHAREPOINT": "sharepoint",
               "TEAMS": "teams", "POWERPLATFORM": "powerplatform", "POWERBI": "powerbi"}
ZTA_PILLAR = {"Identity": "Entra ID", "Devices": "Intune", "Data": "Purview", "AI": "AI and agents", "Network": "Global Secure Access",
              "SecOps": "Defender", "Infrastructure": "Azure"}
# Intune baseline reference pages (mirror file -> name, portal technology)
IB_PAGES = [
    ("ref-windows-mdm-settings", "Security Baseline for Windows", "Intune"),
    ("ref-defender-settings", "Microsoft Defender for Endpoint baseline", "Defender"),
    ("ref-v2-office-settings", "Microsoft 365 Apps for Enterprise baseline", "Microsoft 365 Apps"),
    ("ref-v2-edge-settings", "Microsoft Edge baseline", "Edge"),
    ("ref-windows-365-settings", "Windows 365 Security Baseline", "Intune"),
    ("ref-windows-365-agents-settings", "Windows 365 for Agents security baseline", "AI and agents"),
    ("ref-openclaw-settings", "Local AI Agent Baseline - OpenClaw (preview)", "AI and agents"),
]


def log(*a):
    print("baselines_more:", *a, flush=True)


def load(p, dflt):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return dflt


def dump(p, obj):
    txt = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    old = open(p, encoding="utf-8").read() if os.path.exists(p) else None
    def bare(t):
        try:
            o = json.loads(t); o.pop("generated", None); return json.dumps(o, sort_keys=True)
        except Exception:
            return t
    if old is None or bare(old) != bare(txt):
        open(p, "w", encoding="utf-8").write(txt)
        return True
    return False


def fp(*parts):
    return hashlib.sha1("␟".join(str(x) for x in parts).encode("utf-8")).hexdigest()[:12]


def clip(s, n):
    s = (s or "").strip()
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0] + " …"


def ver_key(v):
    return [int(x) if x.isdigit() else 0 for x in re.split(r"[.\-]", str(v or "0"))]


def sparse_clone(url, paths, dest=None):
    d = dest or tempfile.mkdtemp(prefix="bm-")
    if not os.path.isdir(os.path.join(d, ".git")):
        subprocess.run(["git", "clone", "-q", "--depth", "1", "--filter=blob:none", "--no-checkout", url, d], check=True, timeout=300)
        subprocess.run(["git", "-C", d, "sparse-checkout", "init", "--no-cone"], check=True, capture_output=True)
        subprocess.run(["git", "-C", d, "sparse-checkout", "set"] + paths, check=True, capture_output=True)
        subprocess.run(["git", "-C", d, "checkout", "-q"], check=True, timeout=300)
    h = subprocess.run(["git", "-C", d, "log", "-1", "--format=%h %cI"], capture_output=True, text=True).stdout.split()
    return d, (h[0] if h else ""), (h[1][:10] if len(h) > 1 else "")


def tags(url):
    r = subprocess.run(["git", "ls-remote", "--tags", "--refs", url], capture_output=True, text=True, timeout=120)
    return [l.split("refs/tags/", 1)[1] for l in r.stdout.splitlines() if "refs/tags/" in l]


def plain(md):
    """Markdown/HTML of an implementation block -> readable text lines (links keep their text, <pre> keeps its paths)"""
    t = md.replace("\r", "")
    t = re.sub(r"<br\s*/?>", "\n", t)
    t = re.sub(r"</?(pre|b|i|code|strong|em|ul|li|p|sub|sup|span)[^>]*>", "", t)
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    t = t.replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&").replace("&nbsp;", " ").replace("**", "").replace("`", "")
    out = []
    for l in t.split("\n"):
        l = l.rstrip()
        if not l.strip():
            if out and out[-1] != "":
                out.append("")
            continue
        out.append(re.sub(r"^\s{2,}", "   ", l))
    return "\n".join(out).strip()


def links(md, n=8):
    seen, out = set(), []
    for t, u in re.findall(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", md or ""):
        if "img.shields.io" in u or u in seen:
            continue
        seen.add(u)
        out.append({"t": clip(re.sub(r"[*`]", "", t), 100), "u": u})
    return out[:n]


# ------------------------------------------------------------------------------------------------------- CISA SCuBA
def gh_anchor(h):
    return re.sub(r"[^a-z0-9 \-_]", "", h.strip().lower()).replace(" ", "-")


def cisa_parse(base):
    pols, removed, products = [], [], {}
    for path in sorted(glob.glob(os.path.join(base, "*.md"))):
        key = os.path.basename(path)[:-3]
        txt = open(path, encoding="utf-8", errors="replace").read()
        if key == "removedpolicies":
            for grp, body in re.findall(r"<summary>\s*(.+?)\s*</summary>(.*?)</details>", txt, re.S):
                for pid, rest in re.findall(r"^#### (MS\.[A-Z]+\.\d+\.\d+v\d+)\s*\n(.*?)(?=^#### |\Z)", body, re.S | re.M):
                    st = rest.strip().split("\n- _")[0].strip()
                    rd = re.search(r"_Removal date:_\s*(.+)", rest)
                    rr = re.search(r"_Removal rationale:_\s*(.+)", rest)
                    removed.append({"id": pid, "base": re.sub(r"v\d+$", "", pid), "group": grp.strip(), "t": clip(plain(st), 300),
                                    "date": rd.group(1).strip() if rd else "", "why": clip(plain(rr.group(1)) if rr else "", 400),
                                    "url": SCUBA_BLOB + "removedpolicies.md#" + gh_anchor(pid)})
            continue
        if key not in CISA_FILES:
            log("cisa: unknown baseline file", key)
            continue
        tech, where, prod = CISA_FILES[key]
        h1 = re.search(r"^# (.+)$", txt, re.M)
        products[key] = {"file": key, "tech": tech, "title": h1.group(1).strip() if h1 else key, "where": where, "product": prod,
                         "url": SCUBA_BLOB + key + ".md"}
        # sections "## n. Title"
        secs = re.split(r"^## (\d+)\. (.+)$", txt, flags=re.M)
        for i in range(1, len(secs) - 2, 3):
            sno, stitle, sbody = secs[i], secs[i + 1].strip(), secs[i + 2]
            pol_part = sbody.split("\n### ", 1)
            intro = re.split(r"^### Policies", sbody, flags=re.M)[0].strip()
            res = re.search(r"^### Resources\s*\n(.*?)(?=^### |\Z)", sbody, re.S | re.M)
            lic = re.search(r"^### License Requirements\s*\n(.*?)(?=^### |\Z)", sbody, re.S | re.M)
            impl = re.search(r"^### Implementation\s*\n(.*)", sbody, re.S | re.M)
            impl_txt = impl.group(1) if impl else ""
            steps = {}
            for pid, body in re.findall(r"^#### (MS\.[A-Z]+\.\d+\.\d+v\d+) Instructions\s*\n(.*?)(?=^#### |\Z)", impl_txt, re.S | re.M):
                steps[pid] = body
            impl_common = re.split(r"^#### ", impl_txt, flags=re.M)[0] if impl_txt else ""
            polblock = re.search(r"^### Policies\s*\n(.*?)(?=^### (?!Policies)|\Z)", sbody, re.S | re.M)
            for pid, body in re.findall(r"^#### (MS\.[A-Z]+\.\d+\.\d+v\d+)\s*\n(.*?)(?=^#### |\Z)", polblock.group(1) if polblock else "", re.S | re.M):
                lines = body.strip().split("\n")
                stmt = []
                for l in lines:
                    if not l.strip() or l.startswith("[![") or l.startswith("<!--") or l.startswith("- _"):
                        if stmt:
                            break
                        continue
                    stmt.append(l.strip())
                crit = re.search(r"Criticality:\s*(SHALL|SHOULD)", body)
                rat = re.search(r"_Rationale:_\s*(.+?)(?=\n- _|\n\n|\Z)", body, re.S)
                lm = re.search(r"_Last modified:_\s*(.+)", body)
                nist = re.search(r"_NIST SP 800-53[^:]*:_\s*(.+)", body)
                note = re.search(r"_Note:_\s*(.+?)(?=\n- _|\n\n|\Z)", body, re.S)
                st = steps.get(pid, "")
                pol = {
                    "id": pid, "base": re.sub(r"v\d+$", "", pid), "file": key, "tech": tech,
                    "sec": sno + ". " + stitle, "secIntro": clip(plain(intro), 500) if intro else "",
                    "t": plain(" ".join(stmt)), "crit": crit.group(1) if crit else ("SHALL" if " SHALL" in " ".join(stmt) else "SHOULD"),
                    "bod": "BOD_25--01" in body, "auto": "Automated_Check" in body, "manual": "Manual-" in body or "badge/Manual" in body,
                    "cfg": "Configurable" in body or "Requires_Configuration" in body,
                    "why": plain(rat.group(1)) if rat else "", "mod": lm.group(1).strip() if lm else "",
                    "nist": [x.strip() for x in re.split(r"[,;]", nist.group(1)) if x.strip()][:10] if nist else [],
                    "mitre": sorted(set(re.findall(r"\b(T\d{4}(?:\.\d{3})?)\b", body)))[:12],
                    "note": clip(plain(note.group(1)), 500) if note else "",
                    "how": clip(plain(st) or plain(impl_common), 2500),
                    "lic": clip(plain(lic.group(1)), 300) if lic else "",
                    "res": links(res.group(1)) if res else [],
                    "links": links(st, 6),
                    "url": SCUBA_BLOB + key + ".md#" + gh_anchor(pid), "where": where,
                }
                # the security suite's DLP and audit sections are set in Purview, not in Defender (owner: "Purview, EXO...")
                if key == "securitysuite" and sno in ("3", "5"):
                    pol["tech"], pol["where"] = "Purview", "Microsoft Purview portal (purview.microsoft.com)"
                pol["h"] = fp(pol["t"], pol["crit"], pol["bod"], pol["how"])
                pols.append(pol)
    return pols, removed, products


def cisa(hist):
    base_dir = os.environ.get("SCUBA_DIR")
    try:
        d, commit, date = sparse_clone(SCUBA_REPO + ".git", ["PowerShell/ScubaGear/baselines/"], base_dir)
    except Exception as e:
        log("cisa: clone failed", e)
        return None
    pols, removed, products = cisa_parse(os.path.join(d, "PowerShell", "ScubaGear", "baselines"))
    try:
        tg = sorted({t.lstrip("v") for t in tags(SCUBA_REPO + ".git") if re.match(r"^v?\d+\.\d+\.\d+$", t)}, key=ver_key)
    except Exception:
        tg = (hist.get("cisa") or {}).get("tags") or []
    log("cisa:", len(pols), "policies,", sum(1 for p in pols if p["bod"]), "BOD 25-01,", len(removed), "removed, commit", commit, date)
    return {"policies": pols, "removed": removed, "products": products, "commit": commit, "date": date, "tags": tg}


# -------------------------------------------------------------------------------------------- Intune security baselines
def ib_parse(path, slug, name, tech):
    txt = open(path, encoding="utf-8", errors="replace").read()
    can = re.search(r"^canonicalUrl:\s*(\S+)", txt, re.M)
    url = can.group(1) if can else "https://learn.microsoft.com/intune/device-security/security-baselines/" + slug
    msd = re.search(r"^ms\.date:\s*(\S+)", txt, re.M)
    body = txt.split("\n---", 2)[-1] if txt.startswith("---") else txt
    # zones: ::: zone pivot="a,b" ... ::: zone-end ; outside a zone = every version
    versions, order, cur, cat, sub = {}, [], None, "", ""
    vtitle = {}
    nozone = "::: zone pivot" not in body
    if nozone:
        cur, order = ["current"], ["current"]
    for line in body.split("\n"):
        z = re.match(r'^::: zone pivot="([^"]+)"', line)
        if z:
            cur = [p.strip() for p in z.group(1).split(",")]
            for p in cur:
                if p not in order:
                    order.append(p)
            continue
        if line.startswith("::: zone-end"):
            cur = None
            continue
        h2 = re.match(r"^## (.+)$", line)
        if h2 and nozone and not h2.group(1).lower().startswith(("about", "next", "related", "learn")):
            vtitle.setdefault("current", h2.group(1).strip())
        if h2 and cur and len(cur) == 1 and not nozone:
            vtitle.setdefault(cur[0], h2.group(1).strip())
            cat = sub = ""
            continue
        h3 = re.match(r"^### (.+)$", line)
        if h3:
            cat, sub = plain(h3.group(1)), ""
            continue
        h4 = re.match(r"^#### (.+)$", line)
        if h4:
            sub = plain(h4.group(1))
            continue
        s = re.match(r"^(\s*)- \*\*(.+?)\*\*\s*Baseline default:\s*\*(.*?)\*(.*)$", line)
        if s and cur:
            child = len(s.group(1)) >= 2
            nm, dv = plain(s.group(2)), plain(s.group(3))
            lk = re.search(r"\[Learn more\]\(([^)]+)\)", s.group(4))
            u = lk.group(1) if lk else ""
            if u.startswith("/"):
                u = "https://learn.microsoft.com" + re.sub(r"^/en-us", "", u)
            u = re.sub(r"[?&]WT\.mc_id=[^#&]*", "", u).replace("?#", "#")
            for p in cur:
                versions.setdefault(p, []).append({"c": cat + (" > " + sub if sub else ""), "n": nm, "d": dv, "u": u, "ch": child})
    if not order:
        return None
    vs = [{"pivot": p, "title": vtitle.get(p, p), "n": len(versions.get(p, [])), "url": url + ("" if p == "current" else "?pivots=" + p)} for p in order]
    newest = vs[0]["pivot"] if vs else None
    prev = next((v["pivot"] for v in vs[1:] if v["n"] > 0), None)
    diff = None
    if newest and prev:
        a = {(x["c"], x["n"]): x["d"] for x in versions.get(prev, [])}
        b = {(x["c"], x["n"]): x["d"] for x in versions.get(newest, [])}
        an, bn = {k[1]: v for k, v in a.items()}, {k[1]: v for k, v in b.items()}
        diff = {"from": prev, "to": newest,
                "added": [{"n": k[1], "c": k[0], "d": v} for k, v in b.items() if k[1] not in an][:80],
                "removed": [{"n": k[1], "c": k[0], "d": v} for k, v in a.items() if k[1] not in bn][:80],
                "changed": [{"n": k[1], "c": k[0], "was": an[k[1]], "now": v} for k, v in b.items() if k[1] in an and an[k[1]] != v][:80]}
    return {"slug": slug, "name": name, "tech": tech, "url": url, "updated": (msd.group(1)[:10] if msd else ""), "versions": vs,
            "newest": newest, "settings": versions.get(newest, []), "diff": diff}


def intune():
    out = []
    for slug, name, tech in IB_PAGES:
        p = os.path.join(MIRROR_IB, slug + ".md")
        if not os.path.exists(p):
            out.append({"slug": slug, "name": name, "tech": tech, "missing": True,
                        "url": "https://learn.microsoft.com/intune/device-security/security-baselines/" + slug})
            continue
        try:
            b = ib_parse(p, slug, name, tech)
            if b:
                out.append(b)
        except Exception as e:
            log("intune: not parsed", slug, e)
    log("intune:", sum(1 for b in out if not b.get("missing")), "baselines read,", sum(1 for b in out if b.get("missing")), "not yet in the mirror")
    return out


# ------------------------------------------------------------------------------------------ Zero Trust Assessment
ZT_ATTR = re.compile(r"\[ZtTest\((.*?)\)\]", re.S)
ZT_KV = re.compile(r"(\w+)\s*=\s*(\([^)]*\)|'(?:[^']|'')*'|\$\w+|\d+)", re.S)


def zta(hist):
    try:
        d, commit, date = sparse_clone(ZTA_REPO + ".git", ["src/powershell/tests/", "src/powershell/ZeroTrustAssessment.psd1"], os.environ.get("ZTA_DIR"))
    except Exception as e:
        log("zta: clone failed", e)
        return None
    ver = ""
    try:
        m = re.search(r"ModuleVersion\s*=\s*'([^']+)'", open(os.path.join(d, "src", "powershell", "ZeroTrustAssessment.psd1"), encoding="utf-8-sig").read())
        ver = m.group(1) if m else ""
    except Exception:
        pass
    tests = []
    for ps in sorted(glob.glob(os.path.join(d, "src", "powershell", "tests", "Test-Assessment.*.ps1"))):
        m = ZT_ATTR.search(open(ps, encoding="utf-8-sig", errors="replace").read())
        if not m:
            continue
        a = {}
        for k, v in ZT_KV.findall(m.group(1)):
            if v.startswith("("):
                a[k] = [x.replace("''", "'") for x in re.findall(r"'((?:[^']|'')*)'", v)]
            elif v.startswith("'"):
                a[k] = v[1:-1].replace("''", "'")
            else:
                a[k] = v
        tid = str(a.get("TestId") or re.search(r"\.(\d+)\.ps1$", ps).group(1))
        pil = a.get("Pillar") or ""
        pil = pil if isinstance(pil, list) else [pil]
        pil = [p for p in pil if p]
        md = ps[:-4] + ".md"
        summ, fix, lk = "", "", []
        if os.path.exists(md):
            t = open(md, encoding="utf-8-sig", errors="replace").read()
            t = re.sub(r"<!---?\s*Results\s*-?-->.*", "", t, flags=re.S).replace("%TestResult%", "")
            parts = re.split(r"\*\*Remediation actions?:?\*\*:?", t, maxsplit=1, flags=re.I)
            summ = clip(plain(parts[0]), 600)
            fix = clip(plain(parts[1]), 900) if len(parts) > 1 else ""
            lk = [{"t": l["t"], "u": re.sub(r"[?&]wt\.mc_id=[^#&)]*", "", l["u"])} for l in links(t, 6)]
        title = (a.get("Title") or "").replace("’’", "’")
        tests.append({"id": "ZTA." + tid, "n": tid, "title": title, "pillar": pil, "tech": ZTA_PILLAR.get(pil[0], pil[0] if pil else "Other") if pil else "Other",
                      "cat": a.get("Category") or "", "risk": a.get("RiskLevel") or "", "impact": a.get("UserImpact") or "",
                      "cost": a.get("ImplementationCost") or "", "lic": a.get("CompatibleLicense") or [], "svc": a.get("Service") or [],
                      "sfi": a.get("SfiPillar") or "", "sum": summ, "fix": fix, "links": lk,
                      "url": ZTA_BLOB + os.path.basename(md)})
    for t in tests:
        t["h"] = fp(t["title"], t["risk"], t["sum"], t["fix"])
    log("zta:", len(tests), "tests, module", ver, "commit", commit, date)
    return {"tests": tests, "ver": ver, "commit": commit, "date": date}


# --------------------------------------------------------------------------------------------- compare and events
def words(t):
    return set(w for w in re.findall(r"[a-z0-9]+", (t or "").lower()) if len(w) > 2 and w not in ("shall", "should", "the", "and", "for", "all", "not", "are", "with", "that"))


def jacc(a, b):
    a, b = words(a), words(b)
    return len(a & b) / float(len(a | b)) if a and b else 0.0


def run(day, seed=False, maester_tests=None, tenable_items=None, tenable_audits=None):
    """returns (summary for baselines.json, events); writes baselines-controls.json and its own history"""
    hist = load(HIST_X, {})
    first = not hist.get("state")
    ev = []
    C = cisa(hist)
    I = intune()
    Z = zta(hist)
    if C is None:
        C = (hist.get("last") or {}).get("cisa")
    if Z is None:
        Z = (hist.get("last") or {}).get("zta")
    st = hist.get("state") or {}
    mute = seed or first

    # ---- CISA: Maester and Tenable counterparts, differences
    mt = {}
    for t in (maester_tests or []):
        if t.get("suite") == "CISA":
            mt.setdefault(t["id"][len("CISA."):], []).append({"id": t["id"], "title": t.get("title"), "sev": t.get("sev")})
    ti, tall = {}, []
    tv = ""
    for aid, d in (tenable_items or {}).items():
        if "SCuBA" not in aid:
            continue
        mv = re.search(r"_v(\d+\.\d+\.\d+)$", aid)
        tv = max(tv, mv.group(1), key=ver_key) if mv else tv
        for i in d.get("items") or []:
            if str(i.get("n") or "").startswith("MS."):
                b = re.sub(r"v\d+$", "", i["n"])
                rec = {"a": aid, "f": d.get("file") or aid + ".audit", "k": i["k"], "n": i["n"], "t": i.get("t"), "sol": clip(i.get("sol") or "", 900)}
                ti.setdefault(b, []).append(rec)
                tall.append(rec)
    pols = (C or {}).get("policies") or []
    bases = {p["base"] for p in pols}
    removed_b = {r["base"]: r for r in (C or {}).get("removed") or []}
    used_t = set()
    for p in pols:
        p["maester"] = mt.get(p["base"], [])
        p["tenable"] = ti.get(p["base"], [])
        p["tmatch"] = "id" if p["tenable"] else ""
        if not p["tenable"]:
            # ScubaGear 2.0 moved MS.DEFENDER.* to MS.SECURITYSUITE.*: Tenable 1.5.0 still uses the old ids - match the text
            best = max(((jacc(p["t"], x["t"]), x) for x in tall if re.sub(r"v\d+$", "", x["n"]) not in bases), key=lambda z: z[0], default=(0, None))
            if best[1] and best[0] >= 0.55:
                p["tenable"] = [best[1]]
                p["tmatch"] = "text"
        if not p["maester"]:
            # the same move for Maester's CISA tests that still carry the ScubaGear 1.x ids
            best = max(((max(jacc(p["t"], l[0].get("title")), jacc(p["t"], (removed_b.get(b) or {}).get("t"))), l) for b, l in mt.items() if b not in bases),
                       key=lambda z: z[0], default=(0, None))
            if best[1] and best[0] >= 0.42:
                p["maester"] = best[1]; p["mmatch"] = "text"
        for x in p["tenable"]:
            used_t.add(x["n"])
    tech_order = ["Entra ID", "Exchange Online", "Defender", "Purview", "SharePoint Online", "Teams", "Power Platform", "Power BI", "Intune",
                  "Microsoft 365 Apps", "Edge", "Global Secure Access", "AI and agents", "Azure"]
    gaps = {
        "noTool": [p["id"] for p in pols if not p["maester"] and not p["tenable"]],
        "onlyMaester": [p["id"] for p in pols if p["maester"] and not p["tenable"]],
        "onlyTenable": [p["id"] for p in pols if p["tenable"] and not p["maester"]],
        "both": [p["id"] for p in pols if p["tenable"] and p["maester"]],
        "tenableOld": sorted({x["n"] for x in tall if x["n"] not in used_t}),
        "maesterOld": sorted({l[0]["id"] for b, l in mt.items() if b not in bases and not any(p.get("mmatch") and p["maester"] is l for p in pols)}),
        "renamed": [{"id": p["id"], "was": p["tenable"][0]["n"]} for p in pols if p.get("tmatch") == "text"],
    }
    for x in gaps["tenableOld"]:
        pass
    gaps["tenableOldWhy"] = {x: (removed_b.get(re.sub(r"v\d+$", "", x)) or {}).get("why", "") for x in gaps["tenableOld"]}
    up = (C or {}).get("tags") or []
    lag = None
    if tv and up:
        newer = [t for t in up if ver_key(t) > ver_key(tv)]
        lag = {"tenable": tv, "cisa": up[-1], "behind": len(newer), "versions": newer}

    # ---- events
    sp = st.get("cisa") or {}
    if pols and not mute:
        cur = {p["id"]: p for p in pols}
        for p in pols:
            o = sp.get(p["id"])
            if o is None:
                ev.append({"day": day, "src": "CISA", "type": "policy-new", "id": p["id"], "title": p["t"], "tech": p["tech"], "crit": p["crit"], "bod": p["bod"], "url": p["url"]})
            elif o.get("h") != p["h"]:
                what = [k for k, v in (("text", o.get("t") != p["t"]), ("criticality", o.get("crit") != p["crit"]), ("BOD 25-01", o.get("bod") != p["bod"])) if v] or ["implementation steps"]
                e = {"day": day, "src": "CISA", "type": "policy-changed", "id": p["id"], "title": p["t"], "tech": p["tech"], "what": what, "url": p["url"]}
                if "criticality" in what:
                    e["was"], e["now"] = o.get("crit"), p["crit"]
                if "text" in what:
                    e["wasTitle"] = o.get("t")
                ev.append(e)
        for k, o in sp.items():
            if k not in cur:
                r = next((x for x in (C or {}).get("removed") or [] if x["id"] == k), None)
                ev.append({"day": day, "src": "CISA", "type": "policy-removed", "id": k, "title": o.get("t"), "tech": o.get("tech"), "why": (r or {}).get("why", ""), "url": (r or {}).get("url", "")})
    zp = st.get("zta") or {}
    zt = (Z or {}).get("tests") or []
    if zt and not mute:
        cur = {t["id"] for t in zt}
        for t in zt:
            o = zp.get(t["id"])
            if o is None:
                ev.append({"day": day, "src": "Zero Trust Assessment", "type": "test-new", "id": t["id"], "title": t["title"], "tech": t["tech"], "sev": t["risk"], "url": t["url"]})
            elif o.get("h") != t["h"]:
                what = [k for k, v in (("title", o.get("title") != t["title"]), ("risk", o.get("risk") != t["risk"])) if v] or ["text"]
                e = {"day": day, "src": "Zero Trust Assessment", "type": "test-changed", "id": t["id"], "title": t["title"], "tech": t["tech"], "what": what, "url": t["url"]}
                if "risk" in what:
                    e["was"], e["now"] = o.get("risk"), t["risk"]
                ev.append(e)
        for k, o in zp.items():
            if k not in cur:
                ev.append({"day": day, "src": "Zero Trust Assessment", "type": "test-removed", "id": k, "title": o.get("title"), "tech": o.get("tech")})
    ip = st.get("intune") or {}
    for b in I:
        if b.get("missing"):
            continue
        o = ip.get(b["slug"]) or {}
        if o and not mute:
            if o.get("newest") and o.get("newest") != b["newest"]:
                vt = next((v["title"] for v in b["versions"] if v["pivot"] == b["newest"]), b["newest"])
                ev.append({"day": day, "src": "Intune security baselines", "type": "baseline-version", "id": b["slug"], "title": vt, "tech": b["tech"],
                           "was": o.get("newest"), "now": b["newest"], "url": b["url"] + "?pivots=" + b["newest"]})
            elif o.get("h") and o.get("h") != fp(json.dumps(b["settings"], sort_keys=True)):
                ev.append({"day": day, "src": "Intune security baselines", "type": "baseline-settings", "id": b["slug"], "title": b["name"] + " " + b["newest"], "tech": b["tech"],
                           "url": b["url"] + "?pivots=" + b["newest"], "nWas": o.get("n"), "nNow": len(b["settings"])})
    if C and not mute and (st.get("cisaTags") or []) and up and up[-1] not in (st.get("cisaTags") or []):
        pass  # the ScubaGear release itself is an event of baselines.py ("scubagear" version)

    # ---- history
    st2 = dict(st)
    if pols:
        st2["cisa"] = {p["id"]: {"h": p["h"], "t": p["t"], "crit": p["crit"], "bod": p["bod"], "tech": p["tech"]} for p in pols}
        st2["cisaTags"] = up
    if zt:
        st2["zta"] = {t["id"]: {"h": t["h"], "title": t["title"], "risk": t["risk"], "tech": t["tech"]} for t in zt}
    st2["intune"] = dict(ip, **{b["slug"]: {"newest": b["newest"], "n": len(b["settings"]), "h": fp(json.dumps(b["settings"], sort_keys=True))} for b in I if not b.get("missing")})
    hist["state"] = st2
    fs = hist.setdefault("firstSeen", {})
    for p in pols:
        fs.setdefault(p["id"], day)
    for t in zt:
        fs.setdefault(t["id"], day)
    seen = {(e["day"], e["type"], e.get("id")) for e in hist.get("events") or []}
    hist["events"] = (hist.get("events") or []) + [e for e in ev if (e["day"], e["type"], e.get("id")) not in seen]
    cut = (datetime.date.fromisoformat(day) - datetime.timedelta(days=60)).isoformat()
    hist["events"] = [e for e in hist["events"] if e["day"] >= cut]
    hist["day"] = day
    if C:
        hist.setdefault("last", {})["cisa"] = {k: C[k] for k in ("commit", "date", "tags")}
    if Z:
        hist.setdefault("last", {})["zta"] = {k: Z[k] for k in ("ver", "commit", "date")}

    # ---- outputs
    for p in pols:
        p["first"] = fs.get(p["id"], day)
    for t in zt:
        t["first"] = fs.get(t["id"], day)
    techs = {}
    for p in pols:
        x = techs.setdefault(p["tech"], {"tech": p["tech"], "cisa": 0, "shall": 0, "should": 0, "bod": 0, "noTool": 0})
        x["cisa"] += 1
        x["shall" if p["crit"] == "SHALL" else "should"] += 1
        x["bod"] += 1 if p["bod"] else 0
        x["noTool"] += 1 if not p["maester"] and not p["tenable"] else 0
    for t in zt:
        techs.setdefault(t["tech"], {"tech": t["tech"], "cisa": 0, "shall": 0, "should": 0, "bod": 0, "noTool": 0}).setdefault("zta", 0)
        techs[t["tech"]]["zta"] = techs[t["tech"]].get("zta", 0) + 1
    for b in I:
        x = techs.setdefault(b["tech"], {"tech": b["tech"], "cisa": 0, "shall": 0, "should": 0, "bod": 0, "noTool": 0})
        x["intune"] = x.get("intune", 0) + len(b.get("settings") or [])
    ctl = {"generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "day": day, "spec": "5fq",
           "cisa": {"policies": pols, "removed": (C or {}).get("removed") or [], "products": (C or {}).get("products") or {},
                    "commit": (C or {}).get("commit"), "date": (C or {}).get("date"), "ver": up[-1] if up else "", "tags": up[-8:],
                    "repo": SCUBA_REPO, "bod": BOD, "gaps": gaps, "lag": lag},
           "intune": [{k: v for k, v in b.items() if k not in ("settings", "diff")} for b in I],
           "zta": {k: v for k, v in (Z or {}).items() if k != "tests"}, "techOrder": tech_order}
    wrote = dump(OUT_C, ctl)
    wrote = dump(OUT_I, {"generated": ctl["generated"], "day": day, "baselines": I}) | wrote
    wrote = dump(OUT_Z, {"generated": ctl["generated"], "day": day, "ver": (Z or {}).get("ver"), "commit": (Z or {}).get("commit"),
                         "date": (Z or {}).get("date"), "repo": ZTA_REPO, "tests": [{k: v for k, v in t.items() if k != "h"} for t in zt]}) | wrote
    dump(HIST_X, hist)
    since14 = (datetime.date.fromisoformat(day) - datetime.timedelta(days=14)).isoformat()
    summary = {
        "cisa": {"ok": bool(C and pols), "ver": up[-1] if up else "", "commit": (C or {}).get("commit"), "date": (C or {}).get("date"),
                 "policies": len(pols), "bod": sum(1 for p in pols if p["bod"]), "shall": sum(1 for p in pols if p["crit"] == "SHALL"),
                 "removed": len((C or {}).get("removed") or []), "repo": SCUBA_REPO, "lag": lag,
                 "gaps": {k: len(v) for k, v in gaps.items() if isinstance(v, list)}},
        "intune": {"ok": any(not b.get("missing") for b in I), "baselines": [{"slug": b["slug"], "name": b["name"], "tech": b["tech"], "newest": b.get("newest"),
                    "title": next((v["title"] for v in b.get("versions") or [] if v["pivot"] == b.get("newest")), ""), "n": len(b.get("settings") or []),
                    "updated": b.get("updated", ""), "url": b["url"], "missing": bool(b.get("missing"))} for b in I]},
        "zta": {"ok": bool(zt), "ver": (Z or {}).get("ver"), "commit": (Z or {}).get("commit"), "date": (Z or {}).get("date"), "tests": len(zt), "repo": ZTA_REPO,
                "pillars": {k: sum(1 for t in zt if t["tech"] == k) for k in sorted({t["tech"] for t in zt})}},
        "techs": sorted(techs.values(), key=lambda x: (tech_order.index(x["tech"]) if x["tech"] in tech_order else 99, x["tech"])),
    }
    log("controls", "written" if wrote else "unchanged", "- events today", sum(1 for e in ev if e["day"] == day))
    return summary, [e for e in hist["events"] if e["day"] >= since14]


if __name__ == "__main__":
    d = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
    mt = (load(os.path.join(DATA, "baselines-tests.json"), {}) or {}).get("tests")
    ti = (load(os.path.join(DATA, "baselines-tenable.json"), {}) or {}).get("audits")
    s, e = run(d, maester_tests=mt, tenable_items=ti)
    print(json.dumps(s, indent=1)[:3000])
    print(len(e), "events")
