#!/usr/bin/env python3
"""campaigns.py - campaign tracking: retirements, enforcements, support ends, rollouts by default and
security baselines, followed across every source of the brief (CLAUDE.md 5cu).

A campaign is one change Microsoft runs over weeks or months (SMS and voice MFA retirement, EWS
retirement, Entra Connect version support ...). The brief sees its pieces scattered: several
Message Center posts, a blog post, a Learn "what's new" entry, community articles, a video. This
collector finds them with OUR OWN code, groups them into one campaign, reads the dates next to the
signal words, keeps the history (date moved, new milestone, new material, closed) and writes:

  site/data/campaigns.json          today's campaigns (the page and /diff/ read it)
  site/data/campaigns-history.json  first seen, milestones with every date change, materials with
                                    the day they were found, events of the last 60 days, archive

Inputs (all already in the repository, plus three public reads):
  site/data/<newest brief>.json     state: items, Message Center entries, Microsoft blogs, Learn
                                    "what's new", community articles, component versions
  site/data/mc-tenant.json          the tenant's Message Center (summary, "When this will happen",
                                    "What you need to do to prepare", dated sentences)
  campaigns.json                    the owner's corrections only (rename, merge, hide, keywords,
                                    before/after rows); detection works without it
  youtube_sources.json              watched YouTube channels (public channel feed, no key)
  Microsoft Learn version table     Entra Connect Sync "Retiring ... 2.x versions" (public markdown)

Usage: python3 tools/campaigns.py [--seed] [--day YYYY-MM-DD] [--offline] [--state FILE] [--out-dir DIR]
  --seed     first run: record everything without events (no flood of "new campaign" in /diff/)
  --offline  skip the three network reads (YouTube, Learn table); keeps materials from history
Exit code 0 always when the state was read; the workflow must not fail on a missing feed."""
import calendar, datetime, gzip, html, json, math, os, re, sys, urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "site", "data")
OUT = os.path.join(DATA, "campaigns.json")
HIST = os.path.join(DATA, "campaigns-history.json")
UA = {"User-Agent": "Mozilla/5.0 (MS_SOC campaign tracking; +https://github.com/wpiotrw/MS_SOC)"}

MONTHS = {m.lower(): i for i, m in enumerate(calendar.month_name) if m}
MONTHS.update({m.lower(): i for i, m in enumerate(calendar.month_abbr) if m})
MONTHS["sept"] = 9
MON_RE = "(?:" + "|".join(calendar.month_name[1:]) + "|Sept|" + "|".join(calendar.month_abbr[1:]) + r")(?![a-z])\.?"
PART = {"early": 5, "beginning of": 3, "the beginning of": 3, "mid": 15, "middle of": 15, "late": 25,
        "end of": 0, "the end of": 0}
DATE_PATTERNS = [
    ("part", re.compile(r"\b(early|mid|late|(?:the )?end of|(?:the )?beginning of|middle of)[- ](" + MON_RE + r"),? (\d{4})", re.I)),
    ("day", re.compile(r"\b(" + MON_RE + r") (\d{1,2})(?:st|nd|rd|th)?,? (\d{4})", re.I)),
    ("day2", re.compile(r"\b(\d{1,2}) (" + MON_RE + r"),? (\d{4})", re.I)),
    ("iso", re.compile(r"\b(20\d\d)-(\d\d)-(\d\d)\b")),
    ("quarter", re.compile(r"\bQ([1-4]) (?:CY ?)?(20\d\d)\b", re.I)),
    ("month", re.compile(r"\b(" + MON_RE + r"),? (\d{4})", re.I)),
]

# ---- signals ---------------------------------------------------------------------------------
TYPES = [
    ("Baseline", r"security baseline"),
    ("Support end", r"end of (?:support|servicing|extended support)|no longer (?:be )?supported|minimum (?:supported )?(?:version|os)|"
                    r"older versions?|unsupported versions?|support (?:for|of) [\w .,-]{0,40} (?:ends|will end|ending)|leaves? support|"
                    r"out of support|version support"),
    ("Retirement", r"\bretir|deprecat|sunset|discontinu|no longer (?:be )?available|will be removed|removal of|phas(?:e|ing) out|"
                   r"shut ?down|turn(?:ing)? off|end of life"),
    ("Enforcement", r"\benforce|mandatory|\brequired?\b(?! for)|will require|must (?:use|be|have|migrate|move|register|upgrade|configure)|block(?:ed|ing|s)? by default|"
                    r"hardening|no longer allow"),
    ("Rollout", r"(?:on|enabled|turned on|switch(?:ed)? on|available) by default|by default|default (?:setting|configuration|value)|automatically (?:enabled|turned on)|"
                r"opt[- ]out|generally available|\bGA\b"),
]
SEC = re.compile(r"auth|sign-?in|mfa|passkey|fido|password|conditional access|admin|permission|consent|security|encrypt|token|"
                 r"policy|policies|audit|retention|label|dlp|external|guest|sharing|phish|defender|identity|certificate|\btls\b|"
                 r"protocol|legacy|basic|\bews\b|smtp|pop|imap|oauth|app registration|service principal|role|privilege|access|"
                 r"device|compliance|baseline|firewall|bitlocker|credential|kerberos|ntlm|ldap|smb|\bacl\b|branding|report", re.I)
NOISE = re.compile(r"planned maintenance|\bKB\d{6,}|patch tuesday|monthly (?:security )?update|optional non-security|"
                   r"hotpatch calendar|release notes for|what's new in (?:copilot|teams) for|weekly roundup", re.I)
OUT_OF_SCOPE = re.compile(r"dynamics|finance and operations|viva|power platform|power apps|power automate|power bi|dataverse|"
                          r"planner|project for the web|microsoft forms|bookings|clipchamp|stream|sway|loop\b|minecraft|"
                          r"supply chain|business central|customer service|sales|marketing|powerpoint|\bexcel\b|\bword\b|onenote|"
                          r"whiteboard|zendesk|brand kit|learning coach|surveys agent|similarity checker|glint|engage|"
                          r"slide|canvas|python in excel", re.I)
GENERIC_ACR = set("api apis ga ai pc ca it ui id os sdk url mfa dlp xdr mde mdi mdo mda mdca rbac kb esu ltsc ltsb gcc dod "
                  "us eu uk faq iot vm vms aks pim sso saml mcp new ms m365 o365 spo odb otp pwa ios macos cli".split())
TITLE_PREFIX = re.compile(r"^(?:\d+[- ]day reminder|\d+ (?:weeks?|days?|months?) until(?= )|final reminder(?: to)?|reminder|follow[- ]up(?: on)?|update(?:d)?|"
                          r"plan for change|action required|heads up)[:\s-]+", re.I)
EXPAND = [(re.compile(r"exchange web services", re.I), " EWS "), (re.compile(r"self[- ]service password reset", re.I), " SSPR "),
          (re.compile(r"distributed key manager", re.I), " DKM "), (re.compile(r"one[- ]time passcode", re.I), " OTP ")]
TECHMAP = [
    (r"entra|azure ad|authenticator|conditional access|passkey|\bmfa\b|identity", "Entra"),
    (r"intune|endpoint manager|autopilot", "Intune"),
    (r"defender|sentinel|\bxdr\b|security copilot|threat intel|\bmde\b|\bmdi\b|\bmdo\b|\bmda\b|cloud apps", "Defender"),
    (r"purview|compliance|\bdlp\b|sensitivity|information protection|insider risk|ediscovery|retention", "Purview"),
    (r"exchange|outlook|\bews\b", "Exchange"),
    (r"teams", "Teams"),
    (r"sharepoint|onedrive", "SharePoint"),
    (r"windows 365|cloud pc", "Windows 365"),
    (r"windows|ad fs|active directory|\bdkm\b", "Windows"),
    (r"copilot", "Copilot"),
    (r"microsoft 365 apps|m365 apps|\boffice\b|ltsc", "Microsoft 365 apps"),
    (r"graph", "Graph"),
    (r"azure", "Azure"),
    (r"microsoft 365|m365|admin center", "Microsoft 365"),
]
STOP = set("""the a an and or of to for in on with by from as is are be will at new now its it this that your into via more than
after before over about up out off not no can may all any our we you they their there what when how who which while also using use
used under between within without across per each other only just get set make makes made available microsoft entra intune defender
purview teams exchange online windows outlook sharepoint onedrive office 365 m365 copilot azure update updates updated change changes
changing feature features support supported supporting experience experiences user users admin admins administrator administrators
tenant tenants retirement retire retiring retired retires deprecation deprecated deprecate deprecating rollout rolling roll generally
availability preview public private ga coming soon starting start starts begin begins beginning end ending ends plan planned
announcement announcing introducing introduce introduces upcoming follow followup follow-up reminder action required important
default enabled enable enables disable disabled improved improvement improvements capability capabilities option options setting
settings part ii iii series day days week month year blog post video microsoft's apps app early mid late""".split()) | \
    {m.lower() for m in calendar.month_name if m} | {m.lower() for m in calendar.month_abbr if m}


def tech_of(*texts):
    t = " ".join(x for x in texts if x)
    for pat, name in TECHMAP:
        if re.search(pat, t, re.I):
            return name
    return None


def kind_of(text):
    for k, p in TYPES:
        if re.search(p, text or "", re.I):
            return k
    return None


def stem(w):
    w = w.lower().strip("-.'")
    if len(w) > 4 and w.endswith("ies"):
        return w[:-3] + "y"
    if len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
        return w[:-1]
    return w


def toks(text):
    out = set()
    for w in re.findall(r"[A-Za-z0-9][A-Za-z0-9\-\.']{1,}", text or ""):
        s = stem(w)
        if len(s) < 3 and not (w.isupper() and len(w) >= 2):
            continue
        if s in STOP or re.match(r"^mc\d+$", s):
            continue
        if re.match(r"^\d", s) and not re.match(r"^(?:20\d\d|\d\dh\d|\d+\.\d+(?:\.\d+)*)$", s):
            continue
        out.add(s)
    return out


def expand(t):
    for rx, ab in EXPAND:
        if rx.search(t or "") and ab.strip() not in (t or ""):
            t = (t or "") + ab
    return t or ""


def anchors(title):
    """Acronyms that name one thing (EWS, DKM, SSPR) - one shared anchor is enough to group."""
    return {w.lower() for w in re.findall(r"\b[A-Z][A-Z0-9]{2,6}\b", expand(title)) if w.lower() not in GENERIC_ACR}


def clean_title(t):
    t = re.sub(r"^\s*\((?:updated|retirement|deferred|reminder)\)\s*", "", t or "", flags=re.I)
    t = re.sub(r"^\s*\((?:updated|retirement|deferred|reminder)\)\s*", "", t, flags=re.I)
    t = TITLE_PREFIX.sub("", re.sub(r"\s+", " ", t).strip(" ."))
    return t[:1].upper() + t[1:]


def short_name(t):
    t = clean_title(t)
    m = re.match(r"^(Microsoft [\w ]{2,30}|[\w ]{2,25}):\s+(.{12,})$", t)
    return clean_title(m.group(2)) if m else t


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\[])", text or "") if s.strip()]


# ---- dates -----------------------------------------------------------------------------------
def last_day(y, m):
    return calendar.monthrange(y, m)[1]


def find_dates(text):
    """[(iso, label, precision, span)] for every date phrase in the text, non-overlapping."""
    found, taken = [], []
    for kind, rx in DATE_PATTERNS:
        for m in rx.finditer(text or ""):
            a, b = m.span()
            if any(a < y and b > x for x, y in taken):
                continue
            try:
                if kind == "part":
                    p, mon, y = m.group(1).lower(), MONTHS[m.group(2).lower().rstrip(".")], int(m.group(3))
                    d = PART.get(p, 15) or last_day(y, mon)
                    word = {"beginning of": "early", "the beginning of": "early", "middle of": "mid",
                            "end of": "end of", "the end of": "end of"}.get(p, p)
                    iso, label, prec = "%04d-%02d-%02d" % (y, mon, d), "%s %s %d" % (word, calendar.month_abbr[mon], y), "part"
                elif kind == "day":
                    mon, d, y = MONTHS[m.group(1).lower().rstrip(".")], int(m.group(2)), int(m.group(3))
                    iso, label, prec = "%04d-%02d-%02d" % (y, mon, d), "%d %s %d" % (d, calendar.month_abbr[mon], y), "day"
                elif kind == "day2":
                    d, mon, y = int(m.group(1)), MONTHS[m.group(2).lower().rstrip(".")], int(m.group(3))
                    iso, label, prec = "%04d-%02d-%02d" % (y, mon, d), "%d %s %d" % (d, calendar.month_abbr[mon], y), "day"
                elif kind == "iso":
                    y, mon, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
                    iso, label, prec = "%04d-%02d-%02d" % (y, mon, d), "%d %s %d" % (d, calendar.month_abbr[mon], y), "day"
                elif kind == "quarter":
                    q, y = int(m.group(1)), int(m.group(2))
                    mon = q * 3 - 1
                    iso, label, prec = "%04d-%02d-15" % (y, mon), "Q%d %d" % (q, y), "quarter"
                else:
                    mon, y = MONTHS[m.group(1).lower().rstrip(".")], int(m.group(2))
                    iso, label, prec = "%04d-%02d-15" % (y, mon), "%s %d" % (calendar.month_abbr[mon], y), "month"
                datetime.date.fromisoformat(iso)
            except (ValueError, KeyError):
                continue
            if not 2020 <= int(iso[:4]) <= 2032:
                continue
            taken.append((a, b))
            found.append((iso, label, prec, (a, b)))
    return found


def label_of(iso):
    d = datetime.date.fromisoformat(iso)
    return "%d %s %d" % (d.day, calendar.month_abbr[d.month], d.year)


def tidy(text, iso):
    """'Microsoft's post X of 1 October states the date this post left as "early October": Y becomes required
    on 10 October' -> 'Y becomes required on 10 October' (the part after the last colon that carries the date)."""
    text = text or ""
    if ": " in text:
        tail = text.rsplit(": ", 1)[1]
        if any(d == iso for d, *_ in find_dates(tail)) and len(tail.split()) >= 4:
            text = tail[:1].upper() + tail[1:]
    return text


STAMP = re.compile(r"^\s*(?:\[)?updated (" + MON_RE + r" \d{1,2},? \d{4})\]?:?", re.I)


def milestones_from(text, src, link, base):
    """Dated sentences of one source -> milestones. `Updated <date>:` stamps are not milestones;
    they are returned separately (Microsoft says it changed the timeline that day)."""
    ms, stamps = [], []
    for sen in sentences(text):
        sen = re.sub(r"^\[[^\]]{0,60}\]:?\s*", "", sen)
        st = STAMP.match(sen)
        if st:
            ds = find_dates(st.group(1))
            if ds:
                stamps.append({"date": ds[0][0], "text": sen[st.end():].strip(" :")[:200]})
            sen = sen[st.end():].strip(" :")
            if not find_dates(sen):
                continue
        who = None
        m = re.match(r"^([A-Z][\w ,()/&-]{2,48}):\s+(.+)$", sen)
        whole = sen
        if m and not find_dates(m.group(1)):
            who, whole = m.group(1).strip(), m.group(2)
        clauses = [c.strip(" ,;") for c in re.split(r"(?<!\d),\s+(?!\d{4})|;\s+|\s+—\s+", whole) if c.strip(" ,;")]
        for pos, (iso, label, prec, _) in enumerate(find_dates(whole)):
            body = whole
            if len(find_dates(whole)) > 1:
                own = [c for c in clauses if any(d == iso for d, *_ in find_dates(c)) and len(c.split()) >= 3]
                if own:
                    body = own[0][:1].upper() + own[0][1:]
            if prec in ("month", "quarter") and iso < base[:8] + "01":
                continue
            if re.search(r"\b(?:published|posted|blog|announced on|last updated|this message)\b", body, re.I) and prec == "day" and iso <= base:
                continue
            body = tidy(body, iso)
            ms.append({"date": iso, "label": label, "prec": prec, "text": body[:240], "who": who, "pos": pos, "whole": whole[:240],
                       "src": src, "link": link})
    return ms, stamps


# ---- reading ---------------------------------------------------------------------------------
def newest_state():
    names = sorted(n for n in os.listdir(DATA) if re.match(r"^\d{4}-\d\d-\d\d\.json$", n))
    if not names:
        sys.exit("no state file in site/data")
    with open(os.path.join(DATA, names[-1]), encoding="utf-8") as f:
        d = json.load(f)
    return d.get("soc-brief-state") or d, names[-1][:10]


def jload(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def http(url, timeout=25):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def youtube(sources, notes):
    vids = []
    ns = {"a": "http://www.w3.org/2005/Atom", "m": "http://search.yahoo.com/mrss/"}
    for ch in sources:
        url = "https://www.youtube.com/feeds/videos.xml?channel_id=" + ch["channelId"]
        try:
            root = ET.fromstring(http(url))
        except Exception as e:  # noqa: BLE001 - one channel must not stop the others
            notes.append("YouTube %s: %s" % (ch["name"], str(e)[:80]))
            continue
        for e in root.findall("a:entry", ns):
            t = e.findtext("a:title", "", ns)
            ln = e.find("a:link", ns)
            desc = e.findtext("m:group/m:description", "", ns) or ""
            vids.append({"title": t, "link": ln.get("href") if ln is not None else "", "date": (e.findtext("a:published", "", ns) or "")[:10],
                         "source": ch["name"], "desc": desc[:400]})
    return vids


def support_table(md):
    """Rows of a Learn 'End of support date | Release date' table (Entra Connect Sync)."""
    rows = []
    for line in md.splitlines():
        m = re.match(r"^\|\s*\[?([\d.]+)\]?(?:\([^)]*\))?\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*$", line)
        if not m:
            continue
        eos_txt, rel_txt = m.group(2).strip(), m.group(3).strip()
        eos = find_dates(eos_txt)
        rel = find_dates(rel_txt)
        note = re.search(r"\(([^)]*)\)", eos_txt)
        rows.append({"version": m.group(1), "eos": eos[0][0] if eos else None, "eosNote": note.group(1) if note else None,
                     "released": rel[0][0] if rel else None})
    return rows


# ---- union-find ------------------------------------------------------------------------------
class UF:
    def __init__(self):
        self.p = {}

    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[max(ra, rb)] = min(ra, rb)


LOG_FIELDS = {"Deadline": "Deadline", "Action required by": "Act-by date", "Revised at source": "Microsoft revised the post",
              "Status": "Status", "Published": "Published"}
IDENTITY = re.compile(r"auth|sign-?in|mfa|passkey|fido|password|sspr|conditional access|token|credential|kerberos|ntlm|"
                      r"\bad fs\b|\bdkm\b|certificate|privilege|admin role|global admin|consent|\bews\b|legacy|tls|"
                      r"entra connect|federat|encrypt|security baseline|exploit|cve|b2b|guest|external user", re.I)
USER_FACING = re.compile(r"sign-?in|mfa|sms|voice|passkey|password|outlook|teams|calendar|users? (?:can|will|lose)|"
                         r"end of support|stop working|lose|blocked|no longer", re.I)


def priority(c):
    """Which campaigns matter most now (owner, 9 X 2026): a near date, an enforcement or end of support,
    security weight (identity, sign-in, privileged paths, the main list's own weight and Tier 0 flag) and
    user impact. Score -> critical (>= 9) / high (>= 5) / normal; the reasons are shown on the page."""
    score, why = 0, []
    nx = c.get("next")
    if nx:
        d, exact = nx.get("days", 999), nx.get("prec", "day") == "day"
        if exact and d <= 7:
            score += 4; why.append("date within 7 days")
        elif d <= 30:
            score += 2; why.append("date within 30 days")
    if c["type"] in ("Enforcement", "Support end", "Retirement") and nx:
        score += 1; why.append({"Enforcement": "enforcement — breaks what is not ready",
                                "Support end": "end of support — no fixes after the date",
                                "Retirement": "retirement — the feature stops"}[c["type"]])
    text = c["name"] + " " + " ".join(m.get("title") or "" for m in c["members"] if isinstance(m, dict))
    if IDENTITY.search(text):
        score += 2; why.append("security: identity, sign-in or a privileged path")
    mems = [m for m in c["members"] if isinstance(m, dict)]
    if any(m.get("tier0") for m in mems):
        score += 2; why.append("touches Tier 0")
    if any(m.get("src") == "item" and (m.get("socWeight") or 9) <= 1 for m in mems):
        score += 1; why.append("in the brief's main list, weight 1")
    if any("User impact" in (m.get("tags") or []) for m in mems) or USER_FACING.search(text):
        score += 1; why.append("users notice it")
    if any(m.get("major") and m.get("src") != "item" for m in mems):
        score += 1; why.append("Microsoft marks it a major change")
    if c.get("component"):
        score += 1; why.append("component you run on your servers")
    if c["status"] in ("Recently closed",):
        score, why = min(score, 2), why
    level = "critical" if score >= 9 else "high" if score >= 5 else "normal"
    return {"level": level, "score": score, "why": why}


def main(argv):
    global OUT, HIST
    if "--out-dir" in argv:  # tests: write campaigns.json and the history elsewhere
        od = argv[argv.index("--out-dir") + 1]
        OUT, HIST = os.path.join(od, "campaigns.json"), os.path.join(od, "campaigns-history.json")
    seed = "--seed" in argv
    offline = "--offline" in argv
    if "--state" in argv:
        sp = argv[argv.index("--state") + 1]
        with open(sp, encoding="utf-8") as f:
            d0 = json.load(f)
        st, state_day = d0.get("soc-brief-state") or d0, os.path.basename(sp)[:10]
    else:
        st, state_day = newest_state()
    day = argv[argv.index("--day") + 1] if "--day" in argv else datetime.datetime.now(datetime.timezone.utc).date().isoformat()
    today = datetime.date.fromisoformat(day)
    notes = []
    corr = jload(os.path.join(ROOT, "campaigns.json"), {})
    ytsrc = (jload(os.path.join(ROOT, "youtube_sources.json"), {}) or {}).get("channels", [])
    hist = jload(HIST, {"campaigns": {}, "events": [], "archive": {}})
    _tdoc = jload(os.path.join(DATA, "mc-tenant.json"), {}) or {}
    tenant = {m["id"]: m for m in _tdoc.get("messages", [])}
    tchanges = _tdoc.get("changes") or []

    # ---- records: everything that can seed a campaign ----
    recs = {}
    for e in (st.get("mc") or {}).get("entries", []):
        tm = tenant.get(e["id"], {})
        title = clean_title(e.get("title") or tm.get("title"))
        texts = [e.get("dpSummary") or "", tm.get("summary") or "", tm.get("when") or "", " ".join(tm.get("dates") or [])]
        techs = " ".join((e.get("tech") or []) + (tm.get("services") or []))
        recs[e["id"]] = {"id": e["id"], "src": "MC" if e.get("type") != "RM" else "Roadmap", "title": title,
                         "tech": tech_of(techs, title), "techRaw": techs, "published": e.get("published") or tm.get("start") or e.get("firstTracked"),
                         "updated": e.get("updated") or tm.get("modified"), "link": e.get("link"), "texts": texts,
                         "summary": e.get("dpSummary") or tm.get("summary") or "", "prepare": tm.get("prepare"),
                         "actionBy": tm.get("actionBy"), "major": bool(e.get("isMajor") or tm.get("major")),
                         "tags": e.get("tags") or tm.get("tags") or [], "itemIds": e.get("itemIds") or [], "storyKey": e.get("storyKey")}
    for mid, tm in tenant.items():  # tenant messages the public indexes have not carried
        if mid in recs:
            continue
        title = clean_title(tm.get("title"))
        recs[mid] = {"id": mid, "src": "MC", "title": title, "tech": tech_of(" ".join(tm.get("services") or []), title),
                     "techRaw": " ".join(tm.get("services") or []), "published": tm.get("start"), "updated": tm.get("modified"),
                     "link": "https://admin.microsoft.com/#/MessageCenter/:/messages/" + mid,
                     "texts": [tm.get("summary") or "", tm.get("when") or "", " ".join(tm.get("dates") or [])],
                     "summary": tm.get("summary") or "", "prepare": tm.get("prepare"), "actionBy": tm.get("actionBy"),
                     "major": bool(tm.get("major")), "tags": tm.get("tags") or [], "itemIds": [], "storyKey": mid}
    items = {i["id"]: i for i in st.get("items", []) if i.get("product") not in ("This report",)}
    for i in items.values():
        refs = re.findall(r"\b(MC\d{5,8})\b", " ".join(str(i.get(k) or "") for k in ("id", "reference", "storyKey")))
        recs["item:" + i["id"]] = {"id": "item:" + i["id"], "src": "item", "title": clean_title(i.get("officialTitle") or i.get("title")),
                                   "ourTitle": i.get("title"), "tech": tech_of(i.get("product"), i.get("area"), i.get("title")) or i.get("product"),
                                   "techRaw": i.get("product") or "", "published": i.get("published") or i.get("firstSeen"),
                                   "updated": i.get("lastChanged"), "link": i.get("url"),
                                   "texts": [i.get("deadlineNote") or ""],
                                   "summary": i.get("fingerprint") or "", "why": i.get("why"), "action": i.get("action"),
                                   "deadline": i.get("deadline"), "deadlineNote": i.get("deadlineNote"), "refs": refs,
                                   "major": True, "tags": [], "itemIds": [i["id"]], "storyKey": i.get("storyKey"),
                                   "socWeight": i.get("socWeight"), "tier0": bool(i.get("tier0Touch"))}

    # ---- which records are signals ----
    horizon_old = (today - datetime.timedelta(days=240)).isoformat()
    fresh = (today - datetime.timedelta(days=120)).isoformat()
    seeds = {}
    for r in recs.values():
        k = kind_of(r["title"])
        if not k and r["src"] == "item":
            k = kind_of(" ".join(str(x or "") for x in (r.get("ourTitle"), r.get("deadlineNote"))))
        if "Retirement" in r["tags"] and k in (None, "Rollout"):
            k = "Retirement"
        if not k and r["src"] != "item" and re.search(r"\b(?:will (?:be )?retir|is retiring|are retiring|will be deprecated|reach(?:es)? end of support|"
                                                      r"will no longer be supported)", " ".join(r["texts"][:2]), re.I):
            k = "Retirement"
        if k == "Baseline" and not re.search(r"security baseline", r["title"], re.I):
            k = None
        future = [d for t in r["texts"] for d, *_ in find_dates(t) if d >= day]
        if r.get("deadline") and r["deadline"] >= day:
            future.append(r["deadline"])
        if r.get("actionBy") and r["actionBy"] >= day:
            future.append(r["actionBy"])
        r["kind"] = k
        if r["src"] == "item":
            if not k or OUT_OF_SCOPE.search(r["title"] + " " + (r.get("ourTitle") or "")):
                continue
            if k == "Rollout" and not SEC.search(r["title"] + " " + (r.get("ourTitle") or "")):
                continue
            seeds[r["id"]] = r
            continue
        if not k or NOISE.search(r["title"]):
            continue
        if not r["tech"] or OUT_OF_SCOPE.search(r["techRaw"] + " " + r["title"]) and not r["itemIds"]:
            continue
        recent = max(r.get("published") or "", r.get("updated") or "")
        if not future and recent < fresh:
            continue
        if (r.get("published") or "9999") < horizon_old and not future:
            continue
        if k == "Rollout" and not (SEC.search(r["title"]) or r["itemIds"]):
            continue
        if r["tech"] in ("Copilot", "Microsoft 365 apps", "Microsoft 365", "Teams", "SharePoint") and k != "Support end" and not SEC.search(r["title"]):
            continue
        seeds[r["id"]] = r

    # ---- grouping ----
    uf = UF()
    for sid in seeds:
        uf.find(sid)
    for sid, r in seeds.items():
        for iid in r.get("itemIds") or []:
            if "item:" + iid in seeds and sid != "item:" + iid:
                uf.union(sid, "item:" + iid)
        for ref in r.get("refs") or []:
            if ref in seeds:
                uf.union(sid, ref)
        for t in r["texts"]:
            for ref in re.findall(r"\b(MC\d{5,8})\b", t or ""):
                if ref in seeds and ref != sid:
                    uf.union(sid, ref)
    by_story = defaultdict(list)
    for sid, r in seeds.items():
        if r.get("storyKey"):
            by_story[r["storyKey"]].append(sid)
    story_n = Counter(r.get("storyKey") for r in recs.values() if r.get("storyKey"))
    for key, ids in by_story.items():
        if story_n[key] > 2:
            continue  # a "what's new" page several items point at is not one campaign
        for x in ids[1:]:
            uf.union(ids[0], x)
    # text similarity on titles, rare words only, same technology, size cap
    ttok = {sid: toks(r["title"]) for sid, r in seeds.items()}
    df = Counter(t for ts in ttok.values() for t in ts)
    rare = {sid: {t for t in ts if df[t] <= 8} for sid, ts in ttok.items()}
    ids = sorted(seeds, key=lambda s: seeds[s].get("published") or "")
    size = Counter(uf.find(s) for s in seeds)
    anc = {sid: anchors(r["title"] + " " + (r.get("ourTitle") or "")) for sid, r in seeds.items()}
    adf = Counter(a for v in anc.values() for a in v)
    for a_i, a in enumerate(ids):
        for b in ids[a_i + 1:]:
            sh = {x for x in anc[a] & anc[b] if adf[x] <= 12}
            if not sh or seeds[a]["tech"] != seeds[b]["tech"]:
                continue
            ra, rb = uf.find(a), uf.find(b)
            if ra == rb or size[ra] + size[rb] > 14:
                continue
            uf.union(a, b)
            size[uf.find(a)] = size[ra] + size[rb]
    for a_i, a in enumerate(ids):
        for b in ids[a_i + 1:]:
            if seeds[a]["tech"] != seeds[b]["tech"]:
                continue
            shared = rare[a] & rare[b]
            if len(shared) < 2:
                continue
            jac = len(ttok[a] & ttok[b]) / max(1, len(ttok[a] | ttok[b]))
            if jac < 0.34:
                continue
            ra, rb = uf.find(a), uf.find(b)
            if ra == rb or size[ra] + size[rb] > 12:
                continue
            uf.union(a, b)
            nr = uf.find(a)
            size[nr] = size[ra] + size[rb]
    # owner's merges
    merges = (corr.get("merge") or [])
    for grp in merges:
        present = [g for g in grp if g in seeds]
        for x in present[1:]:
            uf.union(present[0], x)
    # main-list items without a signal word of their own join the campaign they belong to
    # (same MC number, same story, or two rare title words and the same technology)
    for rid, r in recs.items():
        if r["src"] != "item" or rid in seeds:
            continue
        target = None
        for ref in r.get("refs") or []:
            if ref in seeds:
                target = ref
                break
        if not target:
            for sid, sr in seeds.items():
                if rid[5:] in (sr.get("itemIds") or []) or (r.get("storyKey") and r["storyKey"] == sr.get("storyKey") and story_n[r["storyKey"]] <= 2):
                    target = sid
                    break
        if not target:
            rt = toks(expand(r["title"] + " " + (r.get("ourTitle") or "")))
            best, bscore = None, 0
            for sid, sr in seeds.items():
                if sr["tech"] != r["tech"]:
                    continue
                if sid not in ttok:
                    continue  # an item attached a moment ago is not a target itself
                an = anchors(r["title"] + " " + (r.get("ourTitle") or "")) & anc[sid]
                sh = {t for t in rt & ttok[sid] if df.get(t, 0) <= 6}
                if not an or len(sh) < 2:
                    continue
                jac = len(rt & ttok[sid]) / max(1, min(len(rt), len(ttok[sid])))
                if jac >= 0.5 and len(sh) > bscore:
                    best, bscore = sid, len(sh)
            target = best
        if target:
            r["kind"] = seeds[target]["kind"]
            seeds[rid] = r
            uf.union(target, rid)
    clusters = defaultdict(list)
    for sid in seeds:
        clusters[uf.find(sid)].append(seeds[sid])

    # ---- previous ids: a campaign keeps its id when its members move ----
    prev = hist.get("campaigns", {})
    member_of = {}
    for cid, c in prev.items():
        for m in c.get("members", []):
            member_of[m] = cid

    # ---- corpus for material matching ----
    nt = st.get("nt") or {}
    community = (st.get("community") or {}).get("items", [])
    blogs = nt.get("items", [])
    learn = nt.get("changes", []) or []
    videos = []
    if not offline and ytsrc:
        videos = youtube(ytsrc, notes)
    vid_from = (today - datetime.timedelta(days=200)).isoformat()
    videos = [v for v in videos if v["date"] >= vid_from]
    corpus = [toks(x.get("title")) for x in blogs + community + videos] + [toks(x.get("title")) for x in learn] + list(ttok.values())
    cdf = Counter(t for ts in corpus for t in ts)
    N = max(1, len(corpus))

    def idf(t):
        return math.log(N / (1 + cdf[t]))

    camps = []
    used_ids = set()
    for root, members in clusters.items():
        members.sort(key=lambda r: (r.get("published") or "9999", r["id"]))
        mids = [m["id"] for m in members]
        votes = Counter(member_of[m] for m in mids if m in member_of)
        cid = None
        for cand, _ in votes.most_common():
            if cand not in used_ids:
                cid = cand
                break
        if not cid:
            first = next((m for m in mids if not m.startswith("item:")), mids[0])
            cid = "c-" + re.sub(r"[^a-z0-9]+", "-", first.lower()).strip("-")[:60]
            n = 2
            base_id = cid
            while cid in used_ids:
                cid = "%s-%d" % (base_id, n)
                n += 1
        used_ids.add(cid)
        camps.append({"id": cid, "members": members})

    # ---- corrections keyed by any member id ----
    ccorr = corr.get("campaigns") or {}

    def corr_for(c):
        out = {}
        for key in [c["id"]] + [m["id"] for m in c["members"]] + [m["id"].replace("item:", "") for m in c["members"]]:
            if key in ccorr:
                out.update(ccorr[key])
        return out

    results = []
    for c in camps:
        mem = c["members"]
        cc = corr_for(c)
        if cc.get("hide"):
            continue
        mc_members = [m for m in mem if m["src"] in ("MC", "Roadmap")]
        item_members = [m for m in mem if m["src"] == "item"]
        kinds = Counter(m["kind"] for m in mem)
        order = ["Support end", "Retirement", "Enforcement", "Baseline", "Rollout", "Change"]
        ctype = cc.get("type") or sorted(kinds, key=lambda k: (order.index(k) if k in order else 9, -kinds[k]))[0]
        if ctype == "Change":
            ctype = "Required change"
        tech = cc.get("tech") or Counter(m["tech"] for m in mem if m["tech"]).most_common(1)[0][0] if any(m["tech"] for m in mem) else "Microsoft 365"
        tech = cc.get("tech") or tech
        named = mc_members[0] if mc_members else mem[0]
        if item_members and not mc_members:
            t = clean_title(item_members[0].get("ourTitle") or item_members[0]["title"])
            nm = t if len(t) <= 110 else t[:110].rsplit(" ", 1)[0] + "…"
        else:
            # the announcement names the campaign; a follow-up post names a step of it
            cand = [m for m in mc_members if not re.search(r"^(?:[\w ]{2,30}: )?(?:follow[- ]up|(?:final |\d+[- ]day )?reminder|update|\d+ weeks? until)", m["title"], re.I)] or mc_members
            nm = short_name(cand[0]["title"])
        name = cc.get("name") or nm
        # summary: Microsoft's own words first, then ours
        summ = cc.get("summary")
        if not summ:
            for m in mc_members:
                ss = [re.sub(r"^\[[^\]]{0,40}\]\s*", "", s) for s in sentences(m["summary"]) if not STAMP.match(s) and len(s) > 30]
                if ss:
                    summ = ss[0]
                    break
        if not summ and item_members:
            summ = item_members[0].get("ourTitle")
        # ---- milestones ----
        ms, stamps = [], []
        for m in mem:
            for t in m["texts"]:
                a, b = milestones_from(t, m["id"].replace("item:", ""), m["link"], day)
                ms += a
                stamps += [dict(s, src=m["id"]) for s in b]
            if m.get("deadline"):
                ms.append({"date": m["deadline"], "label": label_of(m["deadline"]), "prec": "day",
                           "text": tidy(m.get("deadlineNote") or m.get("ourTitle") or "Deadline", m["deadline"]), "who": None, "src": m["id"].replace("item:", ""), "link": m["link"], "key": "deadline"})
            if m.get("actionBy"):
                ms.append({"date": m["actionBy"], "label": label_of(m["actionBy"]), "prec": "day", "text": "Act by this date (Message Center)",
                           "who": None, "src": m["id"], "link": m["link"], "key": "actionBy"})
            if m["src"] in ("MC", "Roadmap") and m.get("published"):
                ms.append({"date": m["published"], "label": label_of(m["published"]), "prec": "day", "post": True,
                           "text": "Posted: " + m["title"], "who": None, "src": m["id"], "link": m["link"], "key": "posted"})
        # one row per date (posts apart): Microsoft's own sentence first, our note when there is none
        seen = {}
        item_src = {m["id"].replace("item:", "") for m in item_members}
        for x in ms:
            k = (x["date"], bool(x.get("post")), x["src"] if x.get("post") else "")
            o = seen.get(k)
            if not o:
                x["srcs"] = [x["src"]]
                seen[k] = x
                continue
            if x["src"] not in o["srcs"]:
                o["srcs"].append(x["src"])
            better = (o["src"] in item_src and x["src"] not in item_src) or \
                     ((o["src"] in item_src) == (x["src"] in item_src) and len(x["text"]) > len(o["text"]) and len(o["text"]) < 60)
            if better:
                srcs = o["srcs"]
                x["srcs"] = srcs
                seen[k] = x
        ms = sorted(seen.values(), key=lambda x: (x["date"], x.get("post") is not True))
        for x in ms:
            x["past"] = x["date"] < day
            # the key names the sentence and the place of the date in it: one sentence with two dates
            # ("from early October to late April") is two milestones, and a move is a change at one place
            x.setdefault("key", re.sub(r"[^a-z]+", " ", re.sub(r"\b\d+\b|" + MON_RE, "", x.get("whole") or x["text"], flags=re.I).lower()).strip()[:60] + "#%d" % x.get("pos", 0))
            x.pop("whole", None)
        fut = [x for x in ms if not x["past"] and not x.get("post")]
        nxt = fut[0] if fut else None
        dated = [x for x in ms if not x.get("post")]
        final = max(dated, key=lambda x: x["date"]) if dated else None
        # ---- what changes ----
        rows = cc.get("changes") or []
        if not rows:
            byid = {}
            for m in mem:
                sid = m["id"].replace("item:", "")
                row = byid.setdefault(sid, {"change": "", "before": "", "says": "", "why": "", "src": sid,
                                            "link": m.get("link"), "srcKind": "MC" if re.match(r"^MC\d", sid) else "Roadmap" if m["src"] == "Roadmap" or re.match(r"^\d+$", sid) else "item"})
                if m["src"] == "item":
                    row["change"] = m.get("ourTitle") or row["change"] or m["title"]
                    row["why"] = " ".join(sentences(m.get("why") or "")[:2])[:420]
                    continue
                row["change"] = row["change"] or m["title"]
                ss = [re.sub(r"^\[[^\]]{0,40}\]\s*", "", x) for x in sentences(" ".join(t for t in m["texts"][:2] if t)) if not STAMP.match(x)]
                before = next((x for x in ss if re.search(r"\b(?:currently|today,|previously|until now|at present|right now)\b", x, re.I)), "")
                says = next((x for x in ss if x != before and re.search(r"\b(?:will|now|starting|after|no longer|instead|retir|deprecat|enforce)", x, re.I)), "") or \
                    (ss[0] if ss and ss[0] != before else "")
                row["before"], row["says"] = before[:320], says[:420]
            rows = [r for r in byid.values() if r["says"] or r["why"] or r["before"]][:8]
        # ---- what to do ----
        todo = cc.get("todo") or []
        if not todo:
            for m in item_members:
                if m.get("action"):
                    todo.append({"text": m["action"], "src": m["id"].replace("item:", ""), "ours": True})
            for m in mc_members:
                if m.get("prepare"):
                    todo.append({"text": m["prepare"][:450], "src": m["id"]})
            todo = todo[:4]
        # ---- materials ----
        key_t = Counter()
        for m in mem:
            for t in toks(expand(m["title"])):
                key_t[t] += 1
        for kw in cc.get("keywords") or []:
            for t in toks(kw):
                key_t[t] += len(mem)
        sig = {t for t in key_t if cdf[t] <= 15}
        anc_c = set()
        for m in mem:
            anc_c |= anchors(m["title"])
        anc_c = {x for x in anc_c if cdf.get(x, 0) <= 12}
        phrases = [p.lower() for p in cc.get("keywords") or []]
        mc_ids = {m["id"] for m in mc_members}

        def match(title, desc=""):
            low = (title or "").lower()
            if any(p in low for p in phrases):
                return True
            if set(re.findall(r"\bMC\d{5,8}\b", (title or "") + " " + (desc or ""))) & mc_ids:
                return True
            mt = tech_of(title)
            if mt and mt != tech and not (tech == "Defender" and mt == "Entra"):
                return False
            if anc_c & anchors(title or ""):
                return True
            sh = toks(expand(title)) & sig
            return len(sh) >= 2 and sum(idf(t) for t in sh) >= 9
        mats = {"microsoft": [], "community": [], "video": []}
        for m in mc_members:
            mats["microsoft"].append({"title": m["title"], "link": m["link"], "source": "Message Center" if m["src"] == "MC" else "Roadmap",
                                      "id": m["id"], "date": m.get("published"), "updated": m.get("updated")})
        for m in item_members:
            if m["link"]:
                mats["microsoft"].append({"title": m["title"], "link": m["link"], "source": "Main list source", "id": m["id"].replace("item:", ""),
                                          "date": m.get("published")})
        for b in blogs:
            if match(b.get("title"), b.get("summary")):
                mats["microsoft"].append({"title": b["title"], "link": b["link"], "source": b.get("source"), "date": b.get("date")})
        for l in learn:
            if match(l.get("title"), ""):
                mats["microsoft"].append({"title": l["title"], "link": l.get("url"), "source": "Microsoft Learn · What's new · " + (l.get("area") or ""),
                                          "date": l.get("msDate") or "%04d-%02d-01" % (l.get("year") or 2000, l.get("month") or 1)})
        for a in community:
            if match(a.get("title")):
                mats["community"].append({"title": a["title"], "link": a["link"], "source": a.get("source"), "date": a.get("date")})
        for v in videos:
            if match(v["title"], v.get("desc")):
                mats["video"].append({"title": v["title"], "link": v["link"], "source": v["source"], "date": v["date"]})
        c.update({"name": name, "type": ctype, "tech": tech, "summary": summ, "milestones": ms, "next": nxt, "final": final,
                  "stamps": sorted(stamps, key=lambda s: s["date"]), "changes": rows, "todo": todo, "materials": mats,
                  "items": [m["id"].replace("item:", "") for m in item_members], "pin": bool(cc.get("pin"))})
        results.append(c)

    # ---- component support campaigns (version tables) ----
    comp_cfg = corr.get("components") or {}
    for comp in st.get("components") or []:
        cfg = comp_cfg.get(comp["id"]) or {}
        if not (comp.get("deadline") or cfg.get("supportTable")):
            continue
        rows, mand = [], None
        prevc = prev.get("c-comp-" + comp["id"], {})
        if cfg.get("supportTable") and not offline:
            try:
                md = http(cfg["supportTable"])
                rows = support_table(md)
                mm = re.search(r"\*\*Mandatory upgrade required:\*\*\s*([^\n]+)", md)
                if mm:
                    mand = re.sub(r"\s+", " ", mm.group(1)).strip()
            except Exception as e:  # noqa: BLE001
                notes.append("%s support table: %s" % (comp["name"], str(e)[:80]))
        if not rows:
            rows = prevc.get("versions") or []
            mand = mand or prevc.get("mandatory")
        cur = (comp.get("lastChange") or {}).get("to")
        ms = []
        for r in rows:
            r["status"] = ("current" if r["version"] == cur or not r.get("eos") else
                           "retired" if r["eos"] < day else "ends soon" if r["eos"] <= (today + datetime.timedelta(days=60)).isoformat() else "supported")
            if r.get("eos") and r["eos"] >= (today - datetime.timedelta(days=60)).isoformat():
                ms.append({"date": r["eos"], "label": label_of(r["eos"]), "prec": "day", "src": "Learn", "link": (comp.get("sources") or [{}])[0].get("url"),
                           "text": "%s %s support" % (r["version"], "left" if r["eos"] < day else "leaves"), "who": None, "key": "eos " + r["version"]})
            if r.get("released") and r["released"] >= (today - datetime.timedelta(days=60)).isoformat():
                ms.append({"date": r["released"], "label": label_of(r["released"]), "prec": "day", "src": "Learn", "link": (comp.get("sources") or [{}])[0].get("url"),
                           "text": "%s released" % r["version"], "who": None, "key": "rel " + r["version"]})
        if mand:
            for iso, label, prec, _ in find_dates(mand):
                ms.append({"date": iso, "label": label, "prec": prec, "src": "Learn", "link": (comp.get("sources") or [{}])[0].get("url"),
                           "text": mand[:240], "who": None, "key": "mandatory"})
        if comp.get("deadline") and not any(x["date"] == comp["deadline"] for x in ms):
            ms.append({"date": comp["deadline"], "label": label_of(comp["deadline"]), "prec": "day", "src": "Component versions",
                       "link": None, "text": comp.get("deadlineNote") or "Deadline", "who": None, "key": "deadline"})
        ms.sort(key=lambda x: x["date"])
        for x in ms:
            x["past"] = x["date"] < day
        fut = [x for x in ms if not x["past"]]
        results.append({"id": "c-comp-" + comp["id"], "members": [], "name": cfg.get("name") or comp["name"] + " — version support",
                        "type": "Support end", "tech": cfg.get("tech") or tech_of(comp["name"], comp.get("scope")) or "Microsoft 365",
                        "summary": cfg.get("summary") or comp.get("deadlineNote"), "milestones": ms, "next": fut[0] if fut else None,
                        "final": ms[-1] if ms else None, "stamps": [], "changes": [], "todo": [{"text": t} for t in cfg.get("todo") or []],
                        "materials": {"microsoft": [{"title": s.get("label"), "link": s.get("url"), "source": "Microsoft Learn"} for s in comp.get("sources") or []],
                                      "community": [], "video": []},
                        "items": [], "pin": True, "component": {"id": comp["id"], "name": comp["name"], "current": cur,
                                                                 "released": (comp.get("lastChange") or {}).get("released"),
                                                                 "checkedOn": comp.get("checkedOn"), "versions": rows, "mandatory": mand}})

    # ---- a component campaign absorbs the main-list items and posts about the same component ----
    for comp_c in [c for c in results if c.get("component")]:
        rx = (comp_cfg.get(comp_c["component"]["id"]) or {}).get("absorb")
        if not rx:
            continue
        for c in [c for c in results if not c.get("component") and re.search(rx, c["name"], re.I)
                  and c["type"] in ("Support end", "Retirement", "Enforcement", "Required change")]:
            have = {x["date"] for x in comp_c["milestones"]}
            comp_c["milestones"] += [x for x in c["milestones"] if x["date"] not in have and not x.get("post")]
            comp_c["milestones"].sort(key=lambda x: x["date"])
            for g in comp_c["materials"]:
                comp_c["materials"][g] += c["materials"].get(g, [])
            comp_c["todo"] = [t for t in c["todo"] if t.get("ours")] + comp_c["todo"]
            comp_c["items"] += c["items"]
            comp_c["members"] += c["members"]
            comp_c["changes"] += c["changes"]
            results.remove(c)
        fut = [x for x in comp_c["milestones"] if not x["past"]]
        comp_c["next"] = fut[0] if fut else None

    # ---- status, history, events ----
    events = [e for e in hist.get("events", []) if e.get("day", "") >= (today - datetime.timedelta(days=60)).isoformat() and e.get("day") != day]
    newhist = {}
    out = []
    archive = hist.get("archive", {})
    cut30 = (today - datetime.timedelta(days=30)).isoformat()
    cut60 = (today - datetime.timedelta(days=60)).isoformat()
    for c in results:
        ms = c["milestones"]
        dated_ms = [x for x in ms if not x.get("post")]
        last_act = max([m.get("updated") or m.get("published") or "" for m in c["members"]] + [""])
        if c["next"]:
            status = "Active"
        elif c["type"] == "Baseline":
            status = "Released" if (c["final"] and c["final"]["date"] >= cut60) or last_act >= cut60 else "Archive"
        elif dated_ms:
            status = "Recently closed" if c["final"]["date"] >= cut30 else "Archive"
        else:
            status = "No date" if last_act >= (today - datetime.timedelta(days=90)).isoformat() else "Archive"
        if status == "Archive" and c.get("pin") and c["id"].startswith("c-comp-"):
            status = "Active"
        c["status"] = status
        h = prev.get(c["id"]) or archive.get(c["id"]) or {}
        first = h.get("firstSeen") or day
        # milestone memory: key -> date
        oldms = h.get("milestones") or {}
        newms = {}
        for x in ms:
            k = x["src"] + "|" + x["key"]
            newms[k] = {"date": x["date"], "label": x["label"], "text": x["text"][:160]}
            o = oldms.get(k)
            if o and o["date"] != x["date"] and not x.get("post"):
                x["moved"] = {"was": o["label"], "now": x["label"], "seen": day}
                if not seed:
                    events.append({"day": day, "cid": c["id"], "type": "moved", "name": c["name"], "src": x["src"],
                                   "was": o["label"], "now": x["label"], "text": x["text"][:200]})
            elif not o and not seed and h and not x.get("post") and not x["past"]:
                events.append({"day": day, "cid": c["id"], "type": "milestone", "name": c["name"], "src": x["src"],
                               "now": x["label"], "text": x["text"][:200]})
        # remember moves seen on earlier days so the card keeps them
        moves = [m for m in (h.get("moves") or [])]
        for x in ms:
            if x.get("moved"):
                moves.append({"src": x["src"], "key": x["key"], "was": x["moved"]["was"], "now": x["moved"]["now"], "seen": day, "text": x["text"][:160]})
        for x in ms:
            for mv in moves:
                if mv["src"] == x["src"] and mv["key"] == x["key"] and mv["now"] == x["label"]:
                    x["moved"] = {"was": mv["was"], "now": mv["now"], "seen": mv["seen"]}
        # materials accumulate, with the day they were found
        oldmat = h.get("materials") or {}
        allmat = dict(oldmat)
        for grp, lst in c["materials"].items():
            for mt in lst:
                if not mt.get("link"):
                    continue
                if mt["link"] not in allmat:
                    allmat[mt["link"]] = dict(mt, group=grp, found=day)
                    if not seed and h and grp != "microsoft" or (not seed and h and grp == "microsoft" and mt.get("source") != "Message Center"):
                        events.append({"day": day, "cid": c["id"], "type": "material", "name": c["name"], "group": grp,
                                       "title": mt["title"], "source": mt.get("source"), "link": mt["link"]})
        mats = {"microsoft": [], "community": [], "video": []}
        seen_t = set()
        order = sorted(allmat.values(), key=lambda m: (m.get("source") != "Message Center", m.get("source") == "Main list source"))
        for mt in order:
            tk = re.sub(r"[^a-z0-9]+", " ", clean_title(mt.get("title") or "").lower()).strip()
            tk = re.sub(r"^(?:microsoft [a-z ]{2,25}? )", "", tk)
            if tk and tk in seen_t:
                continue
            seen_t.add(tk)
            mats.setdefault(mt.get("group", "microsoft"), []).append(mt)
        for g in mats:
            mats[g].sort(key=lambda m: m.get("date") or "", reverse=True)
        c["materials"] = mats
        if not seed and not h and status in ("Active", "No date", "Released"):
            events.append({"day": day, "cid": c["id"], "type": "new", "name": c["name"], "ctype": c["type"], "tech": c["tech"],
                           "next": c["next"]["label"] if c["next"] else None, "text": (c["summary"] or "")[:200]})
        if not seed and h.get("status") in ("Active", "No date") and status in ("Recently closed",):
            events.append({"day": day, "cid": c["id"], "type": "closed", "name": c["name"], "final": c["final"]["label"] if c["final"] else None})
        if not seed and h.get("status") in ("Recently closed", "Archive") and status == "Active":
            events.append({"day": day, "cid": c["id"], "type": "reopened", "name": c["name"], "next": c["next"]["label"]})
        # change log, Message Center post by post (owner, 9 X: "a table like Jan Bakker's - MC numbers, what it was
        # before and what changed"): the register's field changes (ledger14), the tenant's Message Center changes,
        # Microsoft's "Updated <date>" notes and our own date moves; kept in the history beyond the 14-day window
        mids = {m["id"].replace("item:", "") for m in c["members"]}
        titles = {m["id"].replace("item:", ""): m.get("ourTitle") or m["title"] for m in c["members"]}
        links = {m["id"].replace("item:", ""): m.get("link") for m in c["members"]}
        log = []
        for e in ((st.get("ledger14") or {}).get("entries") or []):
            if e.get("id") not in mids:
                continue
            if e.get("kind") == "added":
                log.append({"date": e.get("seen"), "id": e["id"], "what": "Entered the brief (" + str(e.get("tab") or "") + ")", "before": "", "after": e.get("title") or titles.get(e["id"], "")})
            elif e.get("field") and (e["field"] in LOG_FIELDS or re.search(r"date|deadline|phase|rollout", e["field"], re.I)) and \
                    (e["field"] == "Status" or all(not v or re.match(r"^\d{4}-\d\d-\d\d", str(v)) for v in (e.get("before"), e.get("after")))):
                if not e.get("after") and e["field"] != "Status":
                    continue
                log.append({"date": e.get("seen"), "id": e["id"], "what": LOG_FIELDS.get(e["field"], e["field"]),
                            "before": str(e.get("before") or ""), "after": str(e.get("after") or "")})
        FN = {"end": "Message Center end date", "actionBy": "Act-by date", "start": "Start date", "title": "Title", "severity": "Severity", "major": "Major change"}
        for ch in tchanges:
            if ch.get("id") not in mids or ch.get("type") != "changed":
                continue
            for f, ba in (ch.get("fields") or {}).items():
                if f == "tags":
                    continue
                if f == "bodyHash":
                    log.append({"date": ch.get("date"), "id": ch["id"], "what": "Microsoft edited the post text", "before": "", "after": "see the post"})
                else:
                    log.append({"date": ch.get("date"), "id": ch["id"], "what": FN.get(f, f), "before": str(ba[0] or ""), "after": str(ba[1] or "")})
        for stp in c.get("stamps") or []:
            sid = str(stp.get("src", "")).replace("item:", "")
            log.append({"date": stp["date"], "id": sid, "what": "Microsoft's update note", "before": "", "after": stp.get("text") or "updated"})
        for mv in moves:
            log.append({"date": mv.get("seen"), "id": mv.get("src"), "what": "Date moved", "before": mv.get("was"), "after": mv.get("now")})
        seen_l, merged = set(), []
        # the same change seen by the morning and the afternoon run, or in two tabs, is one row: the earliest day wins
        for e in sorted(log + (h.get("log") or []), key=lambda e: e.get("date") or "9"):
            k = (e.get("id"), e.get("what"), e.get("before"), e.get("after"))
            if str(e.get("what", "")).startswith("Entered the brief"):
                k = (e.get("id"), "entered")
            if k in seen_l or not e.get("date"):
                continue
            seen_l.add(k)
            e.setdefault("title", titles.get(e.get("id"), ""))
            e.setdefault("link", links.get(e.get("id")))
            merged.append(e)
        merged.sort(key=lambda e: (e["date"], e.get("id") or ""), reverse=True)
        c["log"] = merged[:120]
        c["posts"] = [{"id": m["id"], "title": m["title"], "link": m.get("link"), "published": m.get("published"), "updated": m.get("updated"),
                       "kind": m["src"]} for m in c["members"] if m["src"] in ("MC", "Roadmap")]
        rec = {"firstSeen": first, "lastSeen": day, "name": c["name"], "status": status, "members": [m["id"] for m in c["members"]], "log": c["log"],
               "milestones": newms, "moves": moves[-20:], "materials": allmat}
        if c.get("component"):
            rec["versions"] = c["component"]["versions"]
            rec["mandatory"] = c["component"]["mandatory"]
        if status == "Archive":
            archive[c["id"]] = rec
            continue
        archive.pop(c["id"], None)
        newhist[c["id"]] = rec
        c["firstSeen"] = first
        out.append(c)
    # campaigns that vanished from the sources keep their history in the archive
    for cid, h in prev.items():
        if cid not in newhist and cid not in archive:
            archive[cid] = dict(h, status="Archive", lastSeen=h.get("lastSeen"))

    # week column: events of the last 7 days per campaign
    wk = (today - datetime.timedelta(days=6)).isoformat()
    for c in out:
        evs = [e for e in events if e["cid"] == c["id"] and e["day"] >= wk]
        c["week"] = evs
        c["counts"] = {"mc": sum(1 for m in c["materials"]["microsoft"] if m.get("source") in ("Message Center", "Roadmap")),
                       "microsoft": sum(1 for m in c["materials"]["microsoft"] if m.get("source") not in ("Message Center", "Roadmap")),
                       "community": len(c["materials"]["community"]), "video": len(c["materials"]["video"])}
        if c["next"]:
            c["next"]["days"] = (datetime.date.fromisoformat(c["next"]["date"]) - today).days
        c["prio"] = priority(c)
        c["members"] = [m["id"] for m in c["members"]]
    # related: campaigns sharing a technology and rare title words
    for c in out:
        tc = toks(c["name"])
        rel = []
        for o in out:
            if o is c or o["tech"] != c["tech"]:
                continue
            if len(tc & toks(o["name"]) - {"authentication", "method"}) >= 2:
                rel.append({"id": o["id"], "name": o["name"]})
        c["related"] = rel[:3]
    rank = {"Active": 0, "Released": 1, "No date": 2, "Recently closed": 3}
    out.sort(key=lambda c: (rank.get(c["status"], 9), c["next"]["date"] if c["next"] else "9999", c["name"]))
    stats = Counter(c["status"] for c in out)
    doc = {"day": day, "stateDay": state_day, "generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "counts": {"active": stats["Active"], "noDate": stats["No date"], "released": stats["Released"], "closed30": stats["Recently closed"],
                      "in7": sum(1 for c in out if c["next"] and c["next"]["days"] <= 7 and c["next"].get("prec", "day") == "day"),
                      "in30": sum(1 for c in out if c["next"] and c["next"]["days"] <= 30),
                      "critical": sum(1 for c in out if c["prio"]["level"] == "critical"),
                      "high": sum(1 for c in out if c["prio"]["level"] == "high"),
                      "moved7": sum(1 for e in events if e["type"] == "moved" and e["day"] >= wk),
                      "archive": len(archive), "videos": len(videos), "channels": len(ytsrc)},
           "notes": notes, "events": [e for e in events if e["day"] >= (today - datetime.timedelta(days=14)).isoformat()],
           "campaigns": out}
    old = jload(OUT, {})
    same = {k: v for k, v in old.items() if k != "generated"} == json.loads(json.dumps({k: v for k, v in doc.items() if k != "generated"}))
    if not same:  # a run that changed nothing leaves the file alone, so the workflow commits nothing
        with open(OUT, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, separators=(",", ":"))
    with open(HIST, "w", encoding="utf-8") as f:
        json.dump({"updated": day, "campaigns": newhist, "events": events, "archive": archive}, f, ensure_ascii=False, indent=0, separators=(",", ":"))
    print("OK campaigns %s: %d shown (active %d, no date %d, released %d, closed30 %d), archive %d, events today %d, videos %d%s"
          % (day, len(out), stats["Active"], stats["No date"], stats["Released"], stats["Recently closed"], len(archive),
             sum(1 for e in events if e["day"] == day), len(videos), ("; notes: " + "; ".join(notes)) if notes else ""))


if __name__ == "__main__":
    main(sys.argv[1:])
