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
    ("Enforcement", r"\benforce|mandatory (?:upgrade|migration|update|requirement|change)|\brequired\b(?! for)|will require|must (?:use|be|have|migrate|move|register|upgrade|configure)|block(?:ed|ing|s)? by default|"
                    r"hardening|no longer allow"),
    ("Rollout", r"(?:on|enabled|turned on|switch(?:ed)? on|available) by default|by default|default (?:setting|configuration|value)|automatically (?:enabled|turned on)|"
                r"opt[- ]out|generally available|\bGA\b"),
]
SEC = re.compile(r"auth|sign-?in|mfa|passkey|fido|password|conditional access|admin|permission|consent|security|encrypt|token|"
                 r"policy|policies|audit|retention|label|dlp|external|guest|sharing|phish|defender|identity|certificate|\btls\b|"
                 r"protocol|legacy|basic|\bews\b|smtp|pop|imap|oauth|app registration|service principal|role|privilege|access|"
                 r"device|compliance|baseline|firewall|bitlocker|credential|kerberos|ntlm|ldap|smb|\bacl\b|branding|report", re.I)
NOISE = re.compile(r"planned maintenance|\bKB\d{6,}|patch tuesday|monthly (?:security )?update|optional non-security|"
                   r"hotpatch calendar|release notes for|what's new in (?:copilot|teams) for|weekly roundup|non-security preview update|"
                   r"documentation set|enters the roadmap", re.I)
OUT_OF_SCOPE = re.compile(r"dynamics|finance and operations|viva|power platform|power apps|power automate|power bi|dataverse|"
                          r"planner|project for the web|microsoft forms|bookings|clipchamp|stream|sway|loop\b|minecraft|"
                          r"supply chain|business central|customer service|sales|marketing|powerpoint|\bexcel\b|\bword\b|onenote|"
                          r"whiteboard|zendesk|brand kit|learning coach|surveys agent|similarity checker|glint|engage|"
                          r"slide|canvas|python in excel|ai builder", re.I)
GENERIC_CAMEL = set("powershell sharepoint onedrive github linkedin youtube devops microsoft windows teams outlook azure office "
                    "fasttrack techcommunity javascript typescript macos ios ipados iphone ipad visio onenote copilot intune "
                    "entra defender purview exchange graph bitlocker autopilot".split())
GENERIC_ACR = set("api apis ga ai pc ca it ui id os sdk url mfa dlp xdr mde mdi mdo mda mdca rbac kb esu ltsc ltsb gcc dod "
                  "us eu uk faq iot vm vms aks pim sso saml mcp new ms m365 o365 spo odb otp pwa ios macos cli".split())
TITLE_PREFIX = re.compile(r"^(?:\d+[- ]day reminder|\d+ (?:weeks?|days?|months?) until(?= )|final reminder(?: to)?|reminder|follow[- ]up(?: on)?|update(?:d)?(?=\s*[:-])|"
                          r"plan for change|action required|heads up)[:\s-]+", re.I)
EXPAND = [(re.compile(r"exchange web services", re.I), " EWS "), (re.compile(r"self[- ]service password reset", re.I), " SSPR "),
          (re.compile(r"distributed key manager", re.I), " DKM "), (re.compile(r"one[- ]time passcode", re.I), " OTP ")]
TECHMAP = [
    # word boundaries everywhere: "centralized" is not Entra, "paragraph" is not Graph (9 X 2026)
    (r"\bdefender\b|\bsentinel\b|\bxdr\b|security copilot|threat intel|\bmde\b|\bmdi\b|\bmdo\b|\bmda\b|cloud apps", "Defender"),
    (r"\bentra\b|azure ad|authenticator|conditional access|passkey|\bmfa\b|\bsspr\b", "Entra"),
    (r"\bintune\b|endpoint manager|autopilot", "Intune"),
    (r"\bpurview\b|\bcompliance\b|\bdlp\b|sensitivity label|information protection|insider risk|ediscovery|\bretention\b", "Purview"),
    (r"\bexchange\b|\boutlook\b|\bews\b", "Exchange"),
    (r"\bteams\b", "Teams"),
    (r"\bsharepoint\b|\bonedrive\b", "SharePoint"),
    (r"windows 365|cloud pc", "Windows 365"),
    (r"\bwindows\b|\bad fs\b|active directory|\bdkm\b", "Windows"),
    (r"\bcopilot\b", "Copilot"),
    (r"microsoft 365 apps|m365 apps|\boffice\b|ltsc", "Microsoft 365 apps"),
    (r"\bgraph\b", "Graph"),
    (r"\bazure\b", "Azure"),
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


def shrink(t):
    """The long name replaced by its abbreviation: "self-service password reset" is SSPR, so "reset" alone is not
    a word the SSPR campaign shares with an unrelated password-reset post."""
    for rx, ab in EXPAND:
        t = rx.sub(ab, t or "")
    return t or ""


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
    # a flattened post runs on into its next section: "... mid-November 2026 [Impact on Your Organization] Who is
    # affected ..." - the milestone ends where the next "[Section]" begins, when the date is before it
    sec = re.search(r"\s\[[A-Z][^\]]{2,50}\]\s", text)
    if sec and any(d == iso for d, *_ in find_dates(text[:sec.start()])):
        text = text[:sec.start()].rstrip(" ,;")
    if ": " in text:
        tail = text.rsplit(": ", 1)[1]
        if any(d == iso for d, *_ in find_dates(tail)) and len(tail.split()) >= 4:
            text = tail[:1].upper() + tail[1:]
    return text


BOILER = re.compile(r"^(?:thank you for your patience|we apologi[sz]e|we have updated (?:the|this)|this message is associated|"
                    r"we will communicate|learn more|for more information)", re.I)
STAMP = re.compile(r"^\s*(?:\[)?updated (" + MON_RE + r" \d{1,2},? \d{4})\]?:?", re.I)


def milestones_from(text, src, link, base):
    """Dated sentences of one source -> milestones. `Updated <date>:` stamps are not milestones;
    they are returned separately (Microsoft says it changed the timeline that day)."""
    ms, stamps = [], []
    # list items flattened without a full stop ("... late March 2026 GCC High, DoD clouds: Rollout ...") are split
    # again at the cloud / ring labels, so a date for a sovereign cloud is not read as a worldwide date
    text = re.sub(r"(?<=[\w)])\s+(?=(?:Public cloud\s+)?(?:Worldwide|GCC High|GCC|DoD|USNat|USSec|Targeted Release|Standard Release|"
                  r"General Availability|Public Preview)\b[^:.]{0,40}:\s)", ". ", text or "")
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
        if re.search(r"\b(?:GCC|GCCH|DoD|USNat|USSec|Gallatin|21Vianet|air-?gapped|government clouds?)\b", sen) and not re.search(r"worldwide|\bWW\b|commercial", sen, re.I):
            continue   # a date for a sovereign cloud only
        for pos, (iso, label, prec, span) in enumerate(find_dates(whole)):
            body = whole
            # Microsoft's own "(previously early October)" after a date is a date move it states itself
            pv = re.match(r"\s*\(previously ([^)]{3,40})\)", whole[span[1]:])
            was_ms = None
            if pv:
                pd = find_dates(pv.group(1) + (" " + iso[:4] if not re.search(r"\d{4}", pv.group(1)) else ""))
                was_ms = pd[0][1] if pd else pv.group(1)
            if len(find_dates(whole)) > 1:
                own = [c for c in clauses if any(d == iso for d, *_ in find_dates(c)) and len(c.split()) >= 3]
                if own:
                    body = own[0][:1].upper() + own[0][1:]
            if prec in ("month", "quarter") and iso < base[:8] + "01":
                continue
            if re.search(r"\b(?:published|posted|blog|announced on|last updated|this message)\b", body, re.I) and prec == "day" and iso <= base:
                continue
            body = tidy(body, iso)
            ms.append({"date": iso, "label": label, "prec": prec, "text": body[:240], "who": who, "pos": pos, "whole": whole[:240], "msWas": was_ms,
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
    S_ = globals().get("SET") or SETTINGS
    level = "critical" if score >= S_["criticalScore"] else "high" if score >= S_["highScore"] else "normal"
    return {"level": level, "score": score, "why": why}


SETTINGS = {  # defaults; campaigns.json "settings" overrides any of them (CLAUDE.md 5cu-e)
    "closedDays": 30,          # a campaign whose last date passed stays under "Final milestone passed" this long
    "archiveShowDays": 365,    # the Archive group on the page lists campaigns that ended within this many days
    "noDateDays": 90,          # a campaign without any date stays while its newest post is younger than this
    "baselineDays": 60,        # a released security baseline stays under "Released" this long
    "signalLookbackDays": 240, # a post older than this starts no campaign unless it carries a future date
    "freshPostDays": 120,      # ... and a post without a future date must have moved within this many days
    "newCampaignDays": 14,     # "new campaign" event only when the newest post is younger than this
    "newMilestoneDays": 3,     # "new milestone" event only when its post moved within this many days
    "eventsKeepDays": 60,      # events kept in the history file
    "videoDays": 200,          # videos older than this are not matched
    "criticalScore": 9,        # priority: score at or above = critical
    "highScore": 5,            # priority: score at or above = high
}


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
    SET = dict(SETTINGS)
    for k, v in (corr.get("settings") or {}).items():
        if k in SET and isinstance(v, (int, float)) and v >= 0:
            SET[k] = v
    globals()["SET"] = SET

    def ago(n):
        return (today - datetime.timedelta(days=int(n))).isoformat()
    ytsrc = (jload(os.path.join(ROOT, "youtube_sources.json"), {}) or {}).get("channels", [])
    hist = jload(HIST, {"campaigns": {}, "events": [], "archive": {}})
    _tdoc = jload(os.path.join(DATA, "mc-tenant.json"), {}) or {}
    tenant = {m["id"]: m for m in _tdoc.get("messages", [])}
    tchanges = _tdoc.get("changes") or []

    # ---- records: everything that can seed a campaign ----
    recs = {}
    for e in (st.get("mc") or {}).get("entries", []):
        if not re.match(r"^[\w-]+$", e.get("id") or ""):
            continue  # "MC1456735 · MC1471963" is a joined row of two posts that are listed on their own too
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
    # an MC-list row under a story name ("entra-sms-voice-full-retirement") whose link is a Message Center post is that post
    alias = {}
    for r in recs.values():
        mm_ = re.search(r"/message/(MC\d{5,8})\b", r.get("link") or "")
        if mm_ and r["src"] == "MC" and not re.match(r"^MC\d", r["id"]):
            alias[r["id"]] = mm_.group(1)
    for r in recs.values():  # a post without a service tag takes the technology of the brief items it names (MC1448379 MemberOf)
        if not r["tech"] and r["src"] != "item":
            tt = [recs["item:" + x]["tech"] for x in r.get("itemIds") or [] if recs.get("item:" + x, {}).get("tech")]
            if tt:
                r["tech"] = Counter(tt).most_common(1)[0][0]

    # ---- which records are signals ----
    horizon_old = ago(SET["signalLookbackDays"])
    fresh = ago(SET["freshPostDays"])
    seeds = {}
    for r in recs.values():
        k = kind_of(r["title"])
        if not k and r["src"] == "item" and r.get("deadline"):
            # our own item title counts only when the item carries a date: "Managed Home Screen can now require
            # authentication" is a feature, not a campaign (9 X 2026)
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
            if not k or OUT_OF_SCOPE.search(r["title"] + " " + (r.get("ourTitle") or "")) or NOISE.search(r["title"]):
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
        if not sid.startswith("item:") and "item:" + sid in seeds:
            uf.union(sid, "item:" + sid)   # an MC-list entry and a main-list item with the same id are one story
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
            # an acronym that names ONE thing (EWS, DKM, SSPR) groups across technologies: "Teams devices ... ahead of
            # the retirement of EWS" belongs to the EWS campaign (9 X 2026: EWS had split into five campaigns)
            sh = {x for x in anc[a] & anc[b] if adf[x] <= 30}
            if not sh:
                continue
            ra, rb = uf.find(a), uf.find(b)
            if ra == rb or size[ra] + size[rb] > 40:   # one named thing (EWS) may run to many posts
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

    # ---- campaigns the owner DEFINES (campaigns.json "define"): one Message Center post can announce two campaigns
    # (MC1426371: passkeys by default AND the SMS/voice retirement - owner, 9 X 2026: "they have separate dates,
    # separate posts"). A defined campaign takes its listed posts and items out of the automatic grouping; a post
    # listed by two definitions is shared, and its dates, rows and actions are split by the definition's keywords.
    defs = corr.get("define") or []
    claimed = defaultdict(list)
    for dfn in defs:
        for mid in dfn.get("members") or []:
            for rid in (mid, "item:" + mid):
                if rid in recs:
                    claimed[rid].append(dfn["id"])
    shared = {rid for rid, lst in claimed.items() if len(lst) > 1}
    KW = {dfn["id"]: re.compile("|".join(re.escape(k) for k in dfn.get("keywords") or ["."]), re.I) for dfn in defs}

    for root in list(clusters):
        clusters[root] = [r for r in clusters[root] if r["id"] not in claimed]
        if not clusters[root]:
            del clusters[root]

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
    vid_from = ago(SET["videoDays"])
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
    for dfn in defs:
        mem = [recs[rid] for rid in claimed if dfn["id"] in claimed[rid]]
        if not mem:
            continue
        for m in mem:
            if not m.get("kind"):
                m["kind"] = dfn.get("type") or "Change"
        mem.sort(key=lambda r: (r.get("published") or "9999", r["id"]))
        used_ids.add(dfn["id"])
        camps.append({"id": dfn["id"], "members": mem, "defined": dfn,
                      "kw": re.compile("|".join(re.escape(k) for k in dfn.get("keywords") or ["."]), re.I)})

    # ---- EVERY campaign gathers all its posts by the same rules (owner, 9 X 2026: "all detected and future
    # campaigns follow exactly the same rules" as the hand-defined passkeys campaign; CLAUDE.md 5cu-g).
    # 1) a post or item linked by number joins: its own MC number, the brief items it names, the MC numbers its
    #    text names (at most 4 - a round-up page is not a campaign post); 2) a post naming the campaign's anchor
    #    (EWS, DKM, MemberOf, EWSAllowedAppIDs) joins when the campaign retires that thing or the post shares a rare
    #    word with it; 3) a post that joins two campaigns is shared and its sentences are split by keywords the
    #    collector derives per campaign (anchors and rare title words) - the owner's keywords for a defined one.
    def base_of(rid):
        if rid in alias:
            return alias[rid]
        mm_ = re.match(r"^(?:item:)?(MC\d{5,8})", rid) or re.match(r"^(?:item:)?RM(\d{5,7})$", rid)
        return mm_.group(1) if mm_ else rid.replace("item:", "")

    def keys_of(r):
        ks = {base_of(x) for x in (r.get("refs") or []) + (r.get("itemIds") or [])}
        named = set(re.findall(r"\b(MC\d{5,8})\b", " ".join(t or "" for t in r["texts"])))
        if len(named) <= 4:
            ks |= named
        ks.discard(base_of(r["id"]))
        return ks if len(ks) <= 4 else set()

    def anc_of(r):
        t = expand((r.get("title") or "") + " " + (r.get("ourTitle") or ""))
        camel = {w.lower() for w in re.findall(r"\b[A-Z][a-z]+(?:[A-Z][a-z0-9]*)+\b|\b[A-Z]{2,}[a-z]+[A-Z]\w*\b", t)}
        return anchors(t) | (camel - GENERIC_CAMEL)
    tdf = Counter(t for r in recs.values() for t in toks(expand(r["title"])))
    in_camp = {m["id"] for c in camps for m in c["members"]}

    def alive(r):
        if NOISE.search(r["title"]) or (r["src"] != "item" and OUT_OF_SCOPE.search(r["techRaw"] + " " + r["title"])):
            return False
        if max(r.get("published") or "", r.get("updated") or "") >= horizon_old:
            return True
        return (r.get("deadline") or "") >= day or any(d >= day for t in r["texts"] for d, *_ in find_dates(t))
    prof = {}
    for c in camps:
        mem = c["members"]
        an = Counter(a for m in mem for a in anc_of(m))
        prof[c["id"]] = {"keys": {base_of(m["id"]) for m in mem} | {k for m in mem for k in keys_of(m)},
                         "core": {a for a, n in an.items() if n * 2 >= len(mem) or n >= 2},
                         "anc": set(an),
                         "sig": {t for m in mem for t in toks(shrink(m["title"] + " " + (m.get("ourTitle") or ""))) if tdf[t] <= 8} - set(an),
                         # the thing the campaign retires: an anchor named by its retirement / end-of-support posts
                         "retired": {a for m in mem if m.get("kind") in ("Retirement", "Support end") for a in anc_of(m)}}
    aown = Counter(a for p in prof.values() for a in p["core"])
    joins = defaultdict(list)
    cands = [r for rid, r in recs.items() if rid not in in_camp and rid not in claimed and alive(r)]
    for strong in (True, False):
        for c in camps:
            p = prof[c["id"]]
            for r in cands:
                if c["id"] in joins[r["id"]]:
                    continue
                if strong:
                    ok = base_of(r["id"]) in p["keys"] or bool(keys_of(r) & p["keys"])
                else:
                    sh = {a for a in anc_of(r) & p["core"] if aown[a] <= 1}
                    ok = bool(sh) and (bool(sh & p["retired"])
                                       or bool(toks(shrink(r["title"] + " " + (r.get("ourTitle") or ""))) & p["sig"]))
                if ok:
                    joins[r["id"]].append(c["id"])
    cby = {c["id"]: c for c in camps}
    for rid, cids in joins.items():
        for cid in cids:
            cby[cid]["members"].append(recs[rid])
    for c in camps:
        c["members"].sort(key=lambda r: (r.get("published") or "9999", r["id"]))
    owners = defaultdict(list)
    for c in camps:
        for m in c["members"]:
            if c["id"] not in owners[m["id"]]:
                owners[m["id"]].append(c["id"])
    for rid, lst in claimed.items():  # the owner's order decides the primary campaign of a post listed twice
        owners[rid] = list(dict.fromkeys(lst + owners[rid]))

    def hit(c, text):
        if c.get("kw"):
            return bool(c["kw"].search(text or ""))
        p = prof[c["id"]]
        return bool(anc_of({"title": text or ""}) & p["anc"]) or bool(toks(shrink(text or "")) & p["sig"])

    def belongs(c, rid, text):
        """A shared post's sentence goes to the campaign whose keywords it names; a sentence that names none
        goes to the post's primary campaign."""
        own_ = owners.get(rid) or []
        if len(own_) < 2:
            return True
        if hit(c, text):
            return True
        if any(hit(cby[o], text) for o in own_ if o != c["id"] and o in cby):
            return False
        return own_[0] == c["id"]

    # ---- corrections keyed by any member id ----
    ccorr = corr.get("campaigns") or {}

    def corr_for(c):
        out = {}
        for key in [m["id"] for m in c["members"]] + [m["id"].replace("item:", "") for m in c["members"]] + [c["id"]]:
            if key in ccorr and not c.get("defined"):
                out.update(ccorr[key])
        if c.get("defined"):
            out.update({k: v for k, v in c["defined"].items() if k not in ("id", "members")})
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
                a = [x for x in a if belongs(c, m["id"], x["text"])]
                ms += a
                stamps += [dict(s, src=m["id"]) for s in b]
            if m.get("deadline") and belongs(c, m["id"], (m.get("deadlineNote") or "") + " " + (m.get("ourTitle") or "")):
                ms.append({"date": m["deadline"], "label": label_of(m["deadline"]), "prec": "day",
                           "text": tidy(m.get("deadlineNote") or m.get("ourTitle") or "Deadline", m["deadline"]), "who": None, "src": m["id"].replace("item:", ""), "link": m["link"], "key": "deadline"})
            if m.get("actionBy"):
                ms.append({"date": m["actionBy"], "label": label_of(m["actionBy"]), "prec": "day", "text": "Act by this date (Message Center)",
                           "who": None, "src": m["id"], "link": m["link"], "key": "actionBy"})
            if m["src"] in ("MC", "Roadmap") and m.get("published") and base_of(m["id"]) == m["id"]:  # one "posted" per post, not per step row
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
                ss = [re.sub(r"^\[[^\]]{0,40}\]\s*", "", x) for x in sentences(" ".join(t for t in m["texts"][:2] if t))
                      if not STAMP.match(x) and not BOILER.search(re.sub(r"^\[[^\]]{0,40}\]\s*", "", x))]
                before = next((x for x in ss if re.search(r"\b(?:currently|today,|previously|until now|at present|right now)\b", x, re.I)), "")
                says = next((x for x in ss if x != before and re.search(r"\b(?:will|now|starting|after|no longer|instead|retir|deprecat|enforce)", x, re.I)), "") or \
                    (ss[0] if ss and ss[0] != before else "")
                row["before"], row["says"] = before[:320], says[:420]
            rows = [r for r in byid.values() if r["says"] or r["why"] or r["before"]]
            rows = [r for r in rows if all(belongs(c, rid, " ".join([r["change"], r["says"], r["why"]])) for rid in (r["src"], "item:" + r["src"]))]
            rows = rows[:10]
        # every row says when: the post's own dates and the next date it gives (owner, 9 X: "why has the table no dates?")
        recd = {m["id"].replace("item:", ""): m for m in mem}
        for r in rows:
            m0 = recd.get(r["src"]) or {}
            r["published"] = m0.get("published")
            r["updated"] = m0.get("updated") if m0.get("updated") != m0.get("published") else None
            fx = [x for x in ms if r["src"] in (x.get("srcs") or [x["src"]]) and not x.get("post") and x["date"] >= day]
            r["next"] = {"date": fx[0]["date"], "label": fx[0]["label"], "prec": fx[0].get("prec")} if fx else None
        # ---- what to do ----
        todo = cc.get("todo") or []
        if not todo:
            for m in item_members:
                if m.get("action"):
                    todo.append({"text": m["action"], "src": m["id"].replace("item:", ""), "ours": True})
            for m in mc_members:
                if m.get("prepare"):
                    todo.append({"text": m["prepare"][:450], "src": m["id"]})
            todo = [t for t in todo if all(belongs(c, rid, t["text"]) for rid in (t.get("src") or "", "item:" + (t.get("src") or "")))]
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
    events = [e for e in hist.get("events", []) if e.get("day", "") >= ago(SET["eventsKeepDays"]) and e.get("day") != day]
    newhist = {}
    out = []
    archive = hist.get("archive", {})
    cut30 = ago(SET["closedDays"])
    cut60 = ago(SET["baselineDays"])
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
            status = "No date" if last_act >= ago(SET["noDateDays"]) else "Archive"
        if status == "Archive" and c.get("pin") and c["id"].startswith("c-comp-"):
            status = "Active"
        c["status"] = status
        h = prev.get(c["id"]) or archive.get(c["id"]) or {}
        first = h.get("firstSeen") or day
        # a milestone is NEWS only when its post is new to the campaign or Microsoft touched it in the last 3 days;
        # a date that appears because the collector reads more of an old post is recorded quietly (9 X 2026: the
        # tenant snapshot started carrying "When this will happen" and 38 old dates came out as "new milestone")
        old_members = set(h.get("members") or [])
        touched = {}
        for m in c["members"]:
            if isinstance(m, dict):
                # the post's own dates only: an old post a campaign gathers today (a new rule, a new keyword) is not news
                touched[m["id"].replace("item:", "")] = max(m.get("updated") or "", m.get("published") or "")
        recent3 = ago(SET["newMilestoneDays"])

        def fresh_src(x):
            return any(touched.get(s0, "") >= recent3 for s0 in (x.get("srcs") or [x["src"]]))
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
            elif not o and not seed and h and not x.get("post") and not x["past"] and fresh_src(x):
                events.append({"day": day, "cid": c["id"], "type": "milestone", "name": c["name"], "src": x["src"],
                               "now": x["label"], "text": x["text"][:200]})
        # remember moves seen on earlier days so the card keeps them
        moves = [m for m in (h.get("moves") or [])]
        for x in ms:
            if x.get("moved"):
                moves.append({"src": x["src"], "key": x["key"], "was": x["moved"]["was"], "now": x["moved"]["now"], "seen": day, "text": x["text"][:160]})
        for x in ms:
            if x.get("msWas") and not x.get("moved"):
                x["moved"] = {"was": x["msWas"], "now": x["label"], "seen": None, "by": "Microsoft"}
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
                    news = (str(mt.get("date") or day))[:10] >= ago(SET["newCampaignDays"])  # an old article matched today is not news
                    if news and (not seed and h and grp != "microsoft" or (not seed and h and grp == "microsoft" and mt.get("source") != "Message Center")):
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
        newest = max([v for v in touched.values() if v] + [""])
        if not seed and not h and status in ("Active", "No date", "Released") and newest >= ago(SET["newCampaignDays"]):
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
        for x in ms:
            if x.get("moved") and x["moved"].get("by") == "Microsoft":
                m0 = next((m for m in c["members"] if isinstance(m, dict) and m["id"].replace("item:", "") == x["src"]), {})
                log.append({"date": m0.get("updated") or m0.get("published") or day, "id": x["src"], "what": "Microsoft moved the date",
                            "before": x["moved"]["was"], "after": x["moved"]["now"]})
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
        c["revisions"] = sum(1 for e in merged if e["what"] in ("Microsoft's update note", "Microsoft moved the date", "Microsoft revised the post",
                                                               "Microsoft edited the post text", "Date moved", "Deadline", "Act-by date"))
        c["lastMsUpdate"] = max([e["date"] for e in merged if e["what"].startswith("Microsoft")] +
                                [m.get("updated") or "" for m in c["members"] if isinstance(m, dict) and m.get("src") in ("MC", "Roadmap")] + [""]) or None
        # every Message Center post of the campaign, once, under its own number: "MC1325414-enforcement" is a step
        # of MC1325414, and a brief item named after a post the indexes no longer carry still links to the post
        _pp = {}
        for m in sorted(c["members"], key=lambda m: (m["src"] == "item", m["id"] != base_of(m["id"]))):
            b0 = base_of(m["id"])
            if b0 in _pp or not re.match(r"^[\w-]+$", b0):
                continue
            if m["src"] in ("MC", "Roadmap"):
                _pp[b0] = {"id": b0, "title": m["title"], "link": m.get("link"), "published": m.get("published"),
                           "updated": m.get("updated"), "kind": m["src"]}
            elif re.match(r"^MC\d{5,8}$", b0):
                _pp[b0] = {"id": b0, "title": m["title"], "link": "https://mc.merill.net/message/" + b0, "published": m.get("published"),
                           "updated": None, "kind": "MC", "via": "brief item"}
        c["posts"] = sorted(_pp.values(), key=lambda p: (p.get("published") or "9999", p["id"]))
        rec = {"firstSeen": first, "lastSeen": day, "name": c["name"], "status": status, "members": [m["id"] for m in c["members"]], "log": c["log"],
               "milestones": newms, "moves": moves[-20:], "materials": allmat}
        if c.get("component"):
            rec["versions"] = c["component"]["versions"]
            rec["mandatory"] = c["component"]["mandatory"]
        rec.update({"final": c["final"]["date"] if c.get("final") else None, "type": c["type"], "tech": c["tech"],
                    "posts": [p["id"] for p in c.get("posts") or []][:6]})
        if status == "Archive":
            archive[c["id"]] = dict(rec, archivedOn=(archive.get(c["id"]) or {}).get("archivedOn") or day)
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
        c.pop("kw", None)
        if c.pop("defined", None):
            c["definedBy"] = "owner"
    # related: campaigns sharing a technology and rare title words
    # (or one word only two or three campaign names share: "PowerShell" links the -Credential retirement and the
    # ExchangeOnlineManagement 3.10.1 requirement - two Microsoft campaigns about one tool)
    def tech_words(n):  # PowerShell, MemberOf, EWS, FIDO2: words written as names of things
        return {w.lower() for w in re.findall(r"\b[A-Z][a-z]+(?:[A-Z][a-z0-9]*)+\b|\b[A-Z][A-Z0-9]{2,}\b", n or "")} - GENERIC_ACR
    ndf = Counter(t for c in out for t in tech_words(c["name"]))
    for c in out:
        tc, tw = toks(c["name"]), tech_words(c["name"])
        rel = []
        for o in out:
            if o is c or o["tech"] != c["tech"]:
                continue
            sh = tc & toks(o["name"]) - {"authentication", "method"}
            if len(sh) >= 2 or any(ndf[t] <= 3 for t in tw & tech_words(o["name"])):
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
           "notes": notes, "events": [e for e in events if e["day"] >= ago(14)],
           "settings": SET,
           "archive": sorted([{"id": k, "name": v.get("name"), "tech": v.get("tech"), "type": v.get("type"), "final": v.get("final"),
                               "firstSeen": v.get("firstSeen"), "lastSeen": v.get("lastSeen"), "posts": v.get("posts") or []}
                              for k, v in archive.items() if (v.get("final") or v.get("lastSeen") or "") >= ago(SET["archiveShowDays"])],
                             key=lambda a: a.get("final") or a.get("lastSeen") or "", reverse=True),
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
