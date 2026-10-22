#!/usr/bin/env python3
"""threats.py - the Threat Research tab: recent incidents, attack campaigns and vulnerabilities that touch Entra ID and
Microsoft 365 (CLAUDE.md 5el, 19 X 2026).

  python3 tools/threats.py [threat_sources.json] [site/data/threats.json] [--notes threat_notes.json]

Owner, 19 X 2026: "collect, summarise and analyse the most important recent security incidents, attacks and
vulnerabilities related to what our portal measures (Entra first) - the ConnectWise cloud backup multi-tenant app,
for example; show which are new, when they were detected, remediation steps (found or written by us); check whether
Microsoft already describes it; reports, trend lines, rounded frames like the other tabs."

What it does - code only, no model (the 19 X lesson: the morning run ran out of context; this data is NOT in the brief
state, it is its own file):
  1. reads every feed of threat_sources.json (RSS/Atom; CISA KEV as JSON, Microsoft entries only);
  2. keeps an article when it is about Entra / Microsoft 365 AND about an attack, a compromise or a vulnerability
     (a Microsoft Threat Intelligence post is always kept), and tags its areas (apps & OAuth, identity attacks,
     roles & privilege, hybrid & federation, M365 workloads, vulnerabilities);
  3. groups articles about one event into a STORY: a curated story of threat_notes.json by its match words, else two
     articles sharing a CVE, a Storm-#### name, or two rare names within 14 days;
  4. asks whether Microsoft has described the story: a Microsoft feed item (Threat Intelligence, Security Blog,
     Incident Response, MSRC) or a Message Center post (mc.merill.net index) carrying the story's words;
  5. keeps every article's first-seen time between runs (the file itself is the memory), 120 days;
  6. writes trend counts per day (articles per area, stories started) for the last 30 days.
Exit 0 always: a feed that fails is named in `sources[].error`, never a failed workflow.
"""
import datetime as dt, email.utils, hashlib, html, json, os, re, sys, urllib.request
import xml.etree.ElementTree as ET
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kql_extract   # CLAUDE.md 5eu: Kusto queries in the articles

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
      " MS_SOC-portal (github.com/wpiotrw/MS_SOC)")
KEEP_DAYS, TREND_DAYS, STORY_GAP = 120, 30, 14
MCIDX = "https://mc.merill.net/messages-index.json"

STRONG = ["entra", "azure ad", "azure active directory", "aad ", "oauth", "consent", "service principal", "multi-tenant",
          "multitenant", "app registration", "enterprise app", "graph api", "microsoft graph", "conditional access",
          "mfa", "multi-factor", "device code", "token", "aitm", "adversary-in-the-middle", "passkey", "fido",
          "privileged identity", "global admin", "federat", "adfs", "entra connect", "cross-tenant", "b2b",
          "workload identit", "managed identit", "tenant", "client secret", "app credential", "refresh token",
          "primary refresh", "prt", "password spray", "identity"]
M365 = ["microsoft 365", "m365", "office 365", "o365", "exchange online", "exchange server", "outlook", "sharepoint",
        "onedrive", "microsoft teams", "copilot", "intune", "defender", "purview", "entra id"]
GENERAL = ["microsoft", "azure", "windows"]
# the article must be about MICROSOFT's identity or cloud - "token" or "phishing" alone matched a Google AitM campaign
MSCTX = ["entra", "azure ad", "azure active directory", "aad", "microsoft graph", "graph api", "conditional access",
         "entra connect", "adfs", "ad fs", "service principal", "app registration", "microsoft 365", "m365", "office 365",
         "o365", "exchange", "sharepoint", "onedrive", "microsoft teams", "outlook", "copilot", "intune", "defender",
         "purview", "microsoft", "azure"]
# vendor marketing in security blogs ("The 8 best enterprise browsers", "Ranking the best anti-phishing tools")
MARKETING = re.compile(r"\b(best|ranking|top \d+|webinar|buyer|how to choose|vs\.? |comparison|announc|launch|introduc|expanding|now available|partner|award|podcast|recap)\b", re.I)
ATTACK = ["attack", "breach", "compromis", "exploit", "vulnerab", "cve-", "phish", "campaign", "threat actor",
          "storm-", "malware", "ransomware", "abuse", "hijack", "takeover", "steal", "stole", "theft", "supply chain",
          "supply-chain", "backdoor", "zero-day", "0-day", "unauthorized", "hacker", "intrusion", "persistence",
          "privilege escalation", "lateral", "exfiltrat", "spray", "bypass", "flaw", "patch", "incident"]
AREAS = [
    ("Apps & OAuth", ["oauth", "consent", "service principal", "multi-tenant", "multitenant", "app registration",
                      "enterprise app", "client secret", "app credential", "graph api", "microsoft graph", "api secret",
                      "third-party app", "vendor credential", "permission"]),
    ("Identity attacks", ["phish", "aitm", "adversary-in-the-middle", "device code", "token", "mfa", "multi-factor",
                          "password spray", "credential", "session", "passkey", "fido", "sign-in", "login"]),
    ("Roles & privilege", ["global admin", "role", "privilege", "pim", "exchange administrator", "directory.readwrite"]),
    ("Hybrid & federation", ["adfs", "federat", "entra connect", "hybrid", "active directory", "kerberos", "on-prem"]),
    ("M365 workloads", ["exchange", "outlook", "sharepoint", "onedrive", "teams", "copilot", "mailbox", "inbox"]),
    ("Vulnerabilities", ["cve-", "vulnerab", "zero-day", "0-day", "exploit", "patch", "flaw"]),
    ("Hunting (KQL)", []),     # CLAUDE.md 5eu: set when the article carries Kusto queries
]
M365SCOPE = ["entra", "azure ad", "azure active directory", "microsoft 365", "m365", "office 365", "o365", "exchange", "sharepoint",
             "onedrive", "teams", "outlook", "copilot", "intune", "purview", "oauth", "conditional access", "service principal",
             "microsoft graph", "graph api", "app registration", "enterprise app", "multi-tenant", "multitenant", "cross-tenant",
             "adfs", "ad fs", "entra connect", "passkey", "mfa", "device code", "aitm", "token theft", "consent phishing"]
# CLAUDE.md 5ex (owner 22 X: "most of these are not incidents like PHP2Shell or ConnectWise - collect incidents about
# M365 / Entra, or incidents elsewhere that relate to the M365 cloud through the KQL they give for analysis and
# detection"): a STORY needs an event - a CVE, a named actor, or words of an attack that happened - and is not a
# product post, a how-to, a hunting technique or a playbook; an "other" story also needs Kusto queries
EVENT = re.compile(r"cve-\d{4}[-\u2013\u2014]\d+|\bstorm-\d+|\b\w+ (?:blizzard|typhoon|tempest|sleet|sandstorm|hail|dust|flood|cyclone|frost)\b|"
                   r"campaign|breach|compromis|exploit|hijack|\babus(?:e|es|ed|ing)\b|\bst(?:eal|ole|olen)\b|ransomware|malware|"
                   r"phishing kit|phishing-as-a-service|backdoor|zero-day|0-day|supply[- ]chain|intrusion|threat actor|in the wild|"
                   r"exposed|leak|victims|attacked|attackers used|nation-state", re.I)
EDU = re.compile(r"(?i)^(?:introducing|integrated|smarter|stop |protecting|the next frontier|building|how to|a guide|guide to|"
                 r"threat hunting|hunting|detecting (?!cve)|before it|unlock|what's new|announcing)|\bplaybook\b|\bschema\b|"
                 r"walkthrough|\blab\b|best practices|recommendations|what to watch|\(\+ ?kql|practical kql|kql queries")


def incident_like(title, text):
    if EDU.search(title) and not re.search(r"(?i)cve-\d{4}[-\u2013\u2014]\d+|\bstorm-\d+", title):
        return False
    return bool(EVENT.search(title + " " + text))


KQL_PAGES = 25      # article pages read per run to look for Kusto queries the feed text does not carry
DIGEST_PAGES = 12   # 5ez: digest posts (DevSecOpsDad) read per run - their own budget, the article budget runs out first
APP_PAGES = 15      # 5ez: article pages read per run to look for the application IDs an M365 incident names
KQL_KEEP = 365      # days a found query stays in site/data/kql-found.json
STOP = set("""about above after again against also among another attack attacks attacker attackers azure being
between breach breaches campaign cloud companies company could credential credentials critical customers data
defender during entra exchange exploit exploited flaw from global hacker hackers have hijack identity inside into
microsoft million more most multiple network news october office outlook over password patch report researchers
security sharepoint some still teams their there these they threat through tokens update updates used users using
vendor vulnerabilities vulnerability warns which while windows with within year years your what when where how why
new now week weeks month months first last over under since until after before onedrive copilot tenant tenants
access accounts account apps application applications service services enterprise organizations organization
admin admins administrator software supply chain backup actor actors group groups state sponsored malicious
""".split())


def now_utc():
    return dt.datetime.now(dt.timezone.utc)


def get(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/rss+xml, application/xml, application/json, text/xml, */*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def strip(h):
    h = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h or "", flags=re.S | re.I)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h))).strip()


def pdate(s):
    s = (s or "").strip()
    if not s:
        return None
    try:
        d = email.utils.parsedate_to_datetime(s)
    except Exception:
        try:
            d = dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
        except Exception:
            m = re.match(r"(\d{4}-\d{2}-\d{2})", s)
            return m.group(1) + "T00:00:00Z" if m else None
    if d.tzinfo is None:
        d = d.replace(tzinfo=dt.timezone.utc)
    return d.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_feed(raw):
    root = ET.fromstring(raw)
    out = []
    def t(e, *names):
        for n in names:
            x = e.find(n)
            if x is not None and (x.text or "").strip():
                return x.text.strip()
        return ""
    ns = {"a": "http://www.w3.org/2005/Atom", "c": "http://purl.org/rss/1.0/modules/content/",
          "dc": "http://purl.org/dc/elements/1.1/"}
    items = root.findall(".//item")
    if items:
        for it in items:
            link = t(it, "link") or t(it, "guid")
            body = t(it, "description") or ""
            c = it.find("c:encoded", ns)
            if c is not None and c.text and len(c.text) > len(body):
                body = c.text
            cr = it.find("dc:creator", ns)
            out.append({"title": strip(t(it, "title")), "link": link.strip(), "published": pdate(t(it, "pubDate") or t(it, "dc:date")),
                        "summary": strip(body)[:1500], "html": body, "author": (cr.text or "").strip() if cr is not None and cr.text else ""})
    else:
        for it in root.findall("a:entry", ns):
            lk = ""
            for l in it.findall("a:link", ns):
                if l.get("rel") in (None, "alternate"):
                    lk = l.get("href") or lk
            body = ""
            for n in ("a:content", "a:summary"):
                x = it.find(n, ns)
                if x is not None and x.text and len(x.text) > len(body):
                    body = x.text
            pub = it.find("a:published", ns)
            upd = it.find("a:updated", ns)
            au = it.find("a:author/a:name", ns)
            out.append({"title": strip((it.find("a:title", ns).text if it.find("a:title", ns) is not None else "") or ""),
                        "link": lk, "published": pdate((pub.text if pub is not None else "") or (upd.text if upd is not None else "")),
                        "summary": strip(body)[:1500], "html": body, "author": (au.text or "").strip() if au is not None and au.text else ""})
    return [x for x in out if x["title"] and x["link"]]


def has(text, words):
    return [w for w in words if w in text]


def relevance(title, summary, src):
    t = (" " + title + " " + summary[:900] + " ").lower()
    tt = (" " + title + " ").lower()
    strong, m365, gen, att = has(t, STRONG), has(t, M365), has(t, GENERAL), has(t, ATTACK)
    score = 3 * len(set(strong)) + 2 * len(set(m365)) + (1 if gen else 0)
    ms_t, ms_any = set(has(tt, MSCTX)), set(has(t, MSCTX))
    ms_ok = bool(ms_t) or len(ms_any) >= 2
    keep = bool(src.get("AllRelevant") and ms_any) or \
           (ms_ok and att and score >= 4 and not MARKETING.search(title))
    if src.get("Name") == "Microsoft Threat Intelligence":
        keep = True
    areas = [a for a, ws in AREAS if has(t, ws)]
    return keep, score, areas


def entities(title, summary):
    text = title + " " + summary[:600]
    # 5ez: en / em dash too ("CVE-2026–109618" on detect.fyi), written back with a hyphen
    cves = sorted(set(re.sub(r"[\u2013\u2014]", "-", c) for c in re.findall(r"CVE-\d{4}[-\u2013\u2014]\d{4,7}", text, re.I)))
    storms = sorted(set(x.lower() for x in re.findall(r"Storm-\d{3,4}", text, re.I)))
    names = set()
    for w in re.findall(r"\b[A-Z][A-Za-z0-9]{3,}\b", title + " " + summary[:300]):
        lw = w.lower()
        if lw in STOP or lw.isdigit():
            continue
        names.add(lw)
    return [c.upper() for c in cves], storms, sorted(names)


def aid(link):
    return hashlib.sha1(link.encode()).hexdigest()[:12]


def mc_titles():
    try:
        ix = json.loads(get(MCIDX, 120))
        cut = (now_utc() - dt.timedelta(days=60)).strftime("%Y-%m-%d")
        return [{"title": r.get("Title") or "", "link": "https://mc.merill.net/message/" + r["Id"], "id": r["Id"],
                 "date": (r.get("LastModifiedDateTime") or r.get("StartDateTime") or "")[:10], "summary": r.get("Summary") or ""}
                for r in ix if str(r.get("Id", "")).startswith("MC") and (r.get("LastModifiedDateTime") or "")[:10] >= cut]
    except Exception:
        return []


def main(src_path="threat_sources.json", out_path="site/data/threats.json", notes_path="threat_notes.json"):
    now = now_utc()
    stamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    srcs = json.load(open(src_path, encoding="utf-8-sig"))
    for s in srcs:
        s["Name"] = s.get("SourceName")
    prev = {}
    try:
        prev = json.load(open(out_path, encoding="utf-8"))
    except Exception:
        pass
    # notes_path may list several files, comma separated (CLAUDE.md 5el-b): the hand-curated
    # threat_notes.json first, then site/data/threat-notes.json written by the morning routine.
    # On a repeated id the EARLIER file wins, so a person's edit is never overwritten by the routine.
    notes = {}
    for np_ in [x.strip() for x in str(notes_path).split(",") if x.strip()]:
        try:
            for n in json.load(open(np_, encoding="utf-8")).get("stories", []):
                if n.get("id") and n["id"] not in notes:
                    notes[n["id"]] = n
        except Exception as e:
            print("threats: notes file %s not read (%s)" % (np_, e))
    seen_before = {a["link"]: a for a in prev.get("articles") or []}
    cut = (now - dt.timedelta(days=KEEP_DAYS)).strftime("%Y-%m-%d")
    arts, msitems, kev, srep = [], [], [], []
    kq, budget, feed_links = [], [KQL_PAGES], set()
    app_budget, digest_seen, digest_budget = [APP_PAGES], [], [DIGEST_PAGES]
    dprev = {d["link"]: d for d in prev.get("digests") or []}
    for s in srcs:
        rep = {"name": s["Name"], "site": s.get("Site") or s["SourceURL"], "feed": s["SourceURL"], "tier": s.get("Tier", ""),
               "kind": s.get("Kind", "rss"), "state": "ok", "read": 0, "kept": 0, "newest": None, "error": ""}
        try:
            raw = get(s["SourceURL"])
            if s.get("Kind") == "kev":
                j = json.loads(raw)
                ms = [v for v in j.get("vulnerabilities") or [] if (v.get("vendorProject") or "").lower() == "microsoft"]
                rep["read"] = len(ms)
                for v in ms:
                    if (v.get("dateAdded") or "") >= (now - dt.timedelta(days=180)).strftime("%Y-%m-%d"):
                        kev.append({"cve": v.get("cveID"), "product": v.get("product"), "name": v.get("vulnerabilityName"),
                                    "added": v.get("dateAdded"), "due": v.get("dueDate"), "action": v.get("requiredAction"),
                                    "ransomware": v.get("knownRansomwareCampaignUse"), "notes": (v.get("notes") or "")[:300],
                                    "link": "https://msrc.microsoft.com/update-guide/vulnerability/" + (v.get("cveID") or "")})
                kev.sort(key=lambda x: (x["added"] or "", x["cve"] or ""), reverse=True)
                rep["kept"] = len(kev); rep["newest"] = kev[0]["added"] if kev else None
                srep.append(rep); continue
            items = parse_feed(raw)
            rep["read"] = len(items)
            rep["newest"] = max([i["published"] or "" for i in items] or [""]) or None
            for i in items:
                feed_links.add(i["link"])
                if (i["published"] or "9999")[:10] < cut:
                    continue
                if s.get("Microsoft"):
                    msitems.append({"title": i["title"], "link": i["link"], "date": (i["published"] or "")[:10],
                                    "summary": i["summary"][:600], "source": s["Name"]})
                if s.get("CheckOnly"):
                    continue      # MSRC: 5 000 CVE titles are a Microsoft reference to search, not incidents
                keep, score, areas = relevance(i["title"], i["summary"], s)
                # CLAUDE.md 5eu (owner 21 X: "an incident anywhere in the world described with KQL that helps the
                # analysis - collect it, as a full incident, with the query's full text and the link"): Kusto in the
                # feed text, else in the article page (new articles first, a budget per run); an article with Kusto
                # queries is kept whatever product it is about
                old = seen_before.get(i["link"]) or {}
                found = kql_extract.blocks(i.get("html") or "")
                checked = old.get("kqlChecked") or (dprev.get(i["link"]) or {}).get("kqlChecked") or ""
                page = [None]
                def read_page():
                    if page[0] is None:
                        try:
                            page[0] = get(i["link"], 25).decode("utf-8", "replace")
                        except Exception:
                            page[0] = ""
                    return page[0]
                if not found and not checked and not s.get("Digest") and (keep or s.get("Kind") == "kql") and budget[0] > 0:
                    budget[0] -= 1
                    found = kql_extract.blocks(read_page())
                    checked = stamp
                elif not checked:
                    checked = stamp if found else ""
                # 5ez: the application IDs an article names (ConnectWise: seven app IDs in BleepingComputer and Huntress),
                # read once per article - from the feed text, else from the page of an M365 incident article
                apps = old.get("apps")
                appsChecked = old.get("appsChecked") or ""
                if apps is None or not appsChecked:
                    apps = kql_extract.app_ids(i.get("html") or "")
                    t0 = (" " + i["title"] + " " + i["summary"][:900] + " ").lower()
                    if not apps and keep and has(t0, M365SCOPE) and incident_like(i["title"], i["summary"]) and (page[0] is not None or app_budget[0] > 0):
                        if page[0] is None:
                            app_budget[0] -= 1
                        apps = kql_extract.app_ids(read_page())
                        appsChecked = stamp
                    elif apps:
                        appsChecked = stamp
                if s.get("Digest"):
                    # 5ez (owner 22 X: "devsecopsdadattack.com - a site we should track for incidents, following our
                    # agreements"): a DIGEST post covers several incidents in one page; it is never an incident itself -
                    # each of its queries is attached to the incident its section names (below, after the stories)
                    if not found and not checked and digest_budget[0] > 0:
                        digest_budget[0] -= 1
                        found = kql_extract.blocks(read_page()); checked = stamp
                    for qi, q in enumerate(found):
                        kq.append(dict(q, pos=qi, article=aid(i["link"]), link=i["link"], articleTitle=i["title"], source=s["Name"],
                                       author=i.get("author") or s.get("Author") or "", published=(i["published"] or "")[:10], digest=True))
                    digest_seen.append({"link": i["link"], "kqlChecked": checked, "n": len(found)})
                    rep["kept"] += 1 if found else 0
                    continue
                prevk = 0 if found else int(old.get("kql") or 0)   # found on an earlier run (the page is read once)
                # 5ew: KQL makes an INCIDENT only when the article reports an attack, a compromise or a vulnerability -
                # a product post or a lab walkthrough with queries ("Building a CCF connector") goes to the KQL library only
                tl = (" " + i["title"] + " " + i["summary"][:900] + " ").lower()
                if (found or prevk) and has(tl, ATTACK) and not MARKETING.search(i["title"]):
                    keep = True
                    if "Hunting (KQL)" not in areas:
                        areas = areas + ["Hunting (KQL)"]
                if found:   # every query goes to the KQL library; the article is an incident only when kept
                    for qi, q in enumerate(found):
                        kq.append(dict(q, pos=qi, article=aid(i["link"]), link=i["link"], articleTitle=i["title"], source=s["Name"],
                                       author=i.get("author") or "", published=(i["published"] or "")[:10], vendor=bool(s.get("Microsoft"))))
                if not keep:
                    continue
                cves, storms, names = entities(i["title"], i["summary"])
                # the first run is a BASELINE: an article that existed before the portal read it is dated by its
                # publication, not by today (otherwise 22 stories were "new" on 19 X)
                arts.append({"id": aid(i["link"]), "title": i["title"], "link": i["link"], "source": s["Name"],
                             "tier": s.get("Tier", ""), "microsoft": bool(s.get("Microsoft")),
                             "published": i["published"], "firstSeen": old.get("firstSeen") or (stamp if prev else (i["published"] or stamp)),
                             "score": score, "areas": areas or ["Other"], "cves": cves, "storms": storms, "names": names,
                             "summary": i["summary"][:420], "kql": len(found) or prevk, "kqlChecked": checked,
                             "apps": apps or [], "appsChecked": appsChecked})
                rep["kept"] += 1
        except Exception as e:
            rep["state"], rep["error"] = "failed", str(e)[:160]
        srep.append(rep)
    # an article read before and missing from today's feed stays (a feed shows its newest 10-50 posts)
    have = {a["link"] for a in arts}
    for a in prev.get("articles") or []:
        # 5ew: only an article that LEFT its feed is carried; one still in the feed was judged again today
        if a["link"] not in have and a["link"] not in feed_links and (a.get("published") or a.get("firstSeen") or "")[:10] >= cut:
            if "names" not in a:   # the saved file drops `names`; a carried article needs them for the story grouping
                a["cves"], a["storms"], a["names"] = entities(a.get("title") or "", a.get("summary") or "")
            arts.append(a)
    arts.sort(key=lambda a: a.get("published") or a["firstSeen"], reverse=True)

    # ---- stories ----
    df = {}
    for a in arts:
        for n in set(a["names"]):
            df[n] = df.get(n, 0) + 1
    def day(a):
        return (a.get("published") or a["firstSeen"])[:10]
    def match_note(a):
        t = (a["title"] + " " + a["summary"]).lower()
        for nid, n in notes.items():
            if any(w.lower() in t for w in n.get("match") or []):
                return nid
        return None
    story_of = {}
    for a in arts:
        nid = match_note(a)
        if nid:
            story_of[a["id"]] = nid
    loose = [a for a in arts if a["id"] not in story_of]
    parent = {a["id"]: a["id"] for a in loose}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for i, a in enumerate(loose):
        for b in loose[i + 1:]:
            if abs((dt.date.fromisoformat(day(a)) - dt.date.fromisoformat(day(b))).days) > STORY_GAP:
                continue
            shared_hard = set(a["cves"]) & set(b["cves"]) or set(a["storms"]) & set(b["storms"])
            rare = {n for n in set(a["names"]) & set(b["names"]) if df.get(n, 0) <= 6}
            if shared_hard or len(rare) >= 2:
                parent[find(a["id"])] = find(b["id"])
    groups = {}
    for a in arts:
        k = story_of.get(a["id"]) or ("auto-" + find(a["id"]))
        groups.setdefault(k, []).append(a)
    mcs = mc_titles()
    prev_st = {s["id"]: s for s in prev.get("stories") or []}
    stories = []
    for k, L in groups.items():
        L.sort(key=lambda a: a.get("published") or a["firstSeen"])
        note = notes.get(k) or {}
        if not note and len(L) == 1 and L[0]["score"] < 6 and not L[0]["microsoft"] and not L[0].get("kql"):
            continue    # a single weak article is listed in Articles, it is not a story
        txt = " ".join(a["title"] + " " + a.get("summary", "")[:600] for a in L)
        scope = "m365" if note or any(has((" " + a["title"] + " " + a.get("summary", "")[:900] + " ").lower(), M365SCOPE) for a in L) else "other"
        nkql = sum(a.get("kql") or 0 for a in L)
        if not note and (not incident_like(L[-1]["title"] if len(L) == 1 else max(L, key=lambda a: a["score"])["title"], txt)
                         or (scope == "other" and not nkql)):
            continue    # 5ex: not an incident (or, outside M365, no query to run) - its articles stay in Articles
        names = {}
        for a in L:
            for n in a["names"]:
                if df.get(n, 0) <= 6:
                    names[n] = names.get(n, 0) + 1
        words = [w.lower() for w in note.get("match") or []] or \
                [n for n, c in sorted(names.items(), key=lambda x: (-x[1], x[0]))[:3] if c >= 1]
        cves = sorted({c for a in L for c in a["cves"]})
        lead = next((a for a in L if not a["microsoft"]), L[0])
        sid = k if note else "auto-" + re.sub(r"[^a-z0-9]+", "-", (lead["title"].lower()))[:40].strip("-") + "-" + day(L[0])
        # Microsoft described it? (a Microsoft article in the story, a Microsoft feed item or an MC post with its words)
        ms = [{"what": a["source"], "title": a["title"], "link": a["link"], "date": day(a)} for a in L if a["microsoft"]]
        # one curated word or one CVE is enough; automatic words need two (one rare word matched unrelated posts)
        keys = [w for w in words if len(w) >= 4]
        need = 1 if note else 2
        def hit(t):
            return any(c.lower() in t for c in cves) or sum(1 for w in keys if w in t) >= need
        for m in msitems:
            t = (m["title"] + " " + m["summary"]).lower()
            if hit(t) and m["link"] not in {x["link"] for x in ms}:
                ms.append({"what": m["source"], "title": m["title"], "link": m["link"], "date": m["date"]})
        for m in mcs:
            t = (m["title"] + " " + m["summary"]).lower()
            if hit(t):
                ms.append({"what": "Message Center " + m["id"], "title": m["title"], "link": m["link"], "date": m["date"]})
        for x in note.get("microsoft") or []:
            if x.get("link") not in {y["link"] for y in ms}:
                ms.append(x)
        areas = []
        for a in L:
            for ar in a["areas"]:
                if ar not in areas:
                    areas.append(ar)
        # 5ez: the applications / service principals the incident involves - the analysis's list first (name, app ID,
        # what it did, the action), then every app ID an article names that the analysis does not list
        apps = {}
        for x in note.get("apps") or []:
            k = (x.get("appId") or x.get("name") or "").lower()
            if k:
                apps[k] = dict(x, origin="analysis")
        for a in L:
            ntext = json.dumps(note, ensure_ascii=False) if note else ""
            for x in a.get("apps") or []:
                k = x["appId"]
                if k not in apps and k in (note.get("appsNote") or "").lower():
                    continue      # the analysis files it as something else (the vendor's owner tenant)
                if not x.get("name"):    # the analysis names it in an indicator: "506e08f9-... (Cloud Backup)"
                    mm = re.search(re.escape(k) + r"\s*\(([^)]{3,80})\)", ntext, re.I)
                    if mm:
                        x = dict(x, name=mm.group(1))
                if k in apps:
                    apps[k].setdefault("alsoIn", [])
                    if a["source"] not in apps[k]["alsoIn"] and a["source"] != apps[k].get("src"):
                        apps[k]["alsoIn"].append(a["source"])
                    continue
                apps[k] = {"appId": k, "name": x.get("name") or "", "kind": x.get("kind") or "app", "context": x.get("context") or "",
                           "origin": "source", "src": a["source"], "link": a["link"]}
        ps = prev_st.get(sid) or {}
        stories.append({
            "id": sid, "curated": bool(note), "title": note.get("title") or lead["title"],
            "firstReported": min(day(a) for a in L), "firstSeen": min(a["firstSeen"] for a in L),
            "lastUpdate": max((a.get("published") or a["firstSeen"]) for a in L),
            "articles": [a["id"] for a in L], "sources": sorted({a["source"] for a in L}),
            "areas": note.get("areas") or areas, "cves": cves, "words": words,
            "microsoft": {"status": "described" if ms else "not-yet", "items": ms[:8],
                          "checked": "Microsoft Threat Intelligence, Microsoft Security Blog, Microsoft Incident Response, MSRC Security Update Guide, Message Center (mc.merill.net, 60 days)"},
            "score": max(a["score"] for a in L) + 2 * len({a["source"] for a in L}) + (6 if note else 0),
            "articlesBefore": len(ps.get("articles") or []) if ps else 0,
            # CLAUDE.md 5ey (owner 22 X: "ConnectWise has KQL when expanded - why is it not shown? Does KQL mean the incident
            # is on the list because it has KQL and is not M365? Then distinguish it and store both"): kql = all queries,
            # kqlSources = published by the sources, kqlAnalysis = written in our analysis; why = the reasons the incident
            # is listed - m365 (about Entra / a Microsoft 365 workload), kql (queries to run), analysis (we analysed it)
            "kql": nkql + len(note.get("kql") or []),
            "kqlSources": nkql,
            "kqlAnalysis": len(note.get("kql") or []),
            "why": [w for w, on in (("m365", scope == "m365"), ("kql", bool(nkql or note.get("kql"))), ("analysis", bool(note))) if on],
            # CLAUDE.md 5ew (owner 22 X: "Microsoft 365 / Entra / Teams first, then the others - they are another kind and
            # have KQL"): m365 = the story is about Entra or a Microsoft 365 workload; other = anything else (a PHP flaw,
            # a GitHub enumeration) kept for its hunting queries
            "scope": scope,
            "apps": sorted(apps.values(), key=lambda x: (x.get("origin") != "analysis", not x.get("appId"), x.get("kind") == "tenant")),
            "appsNote": note.get("appsNote") or "",
            # the curated text travels with the story, so the page reads one file
            "notes": {k: v for k, v in note.items() if k not in ("id", "match", "title", "areas", "microsoft")} if note else None,
        })
    stories.sort(key=lambda s: (s["lastUpdate"], s["score"]), reverse=True)

    # ---- CLAUDE.md 5eu: every Kusto query found in an article, with its story, kept KQL_KEEP days ----
    story_by_art = {a: st["id"] for st in stories for a in st["articles"]}
    kpath = os.path.join(os.path.dirname(out_path) or ".", "kql-found.json")
    try:
        kprev = json.load(open(kpath, encoding="utf-8")).get("queries") or []
    except Exception:
        kprev = []
    kby = {q["key"]: q for q in kprev}
    for q in kq:
        o = kby.get(q["key"])
        q = dict(q, story=(q.get("story") if q.get("digest") else story_by_art.get(q["article"])) or (o or {}).get("story") or "", firstSeen=(o or {}).get("firstSeen") or stamp,
                 cves=sorted(set(re.findall(r"CVE-\d{4}-\d{4,7}", q["articleTitle"] + " " + q["query"], re.I))))
        kby[q["key"]] = q
    # ---- 5ez: incidents that are one event seen twice (ConnectWise and Storm-0940/ARTEX), community and digest KQL ----
    def stext(st):
        n = notes.get(st["id"]) or {}
        A = {a["id"]: a for a in arts}
        return (" ".join([st["title"], n.get("summary") or ""] + [(A[x]["title"] + " " + A[x].get("summary", "")) for x in st["articles"] if x in A])).lower()
    COMMON_CAPS = {"KQL", "HTTP", "HTTPS", "AZURE", "ENTRA", "OAUTH", "MSRC", "CISA", "NTLM", "SAML", "LDAP", "TEAMS", "WEBDAV", "API", "APIS",
                   "AITM", "SSPR", "OTP", "MFA", "FIDO", "PHISH", "SAAS", "IAAS", "EDR", "XDR", "SIEM", "SOAR", "RMM", "VPN", "DLL", "UEFI"}
    def wb(w, t):      # a whole word: "artex" must not hit "cleartext"
        return re.search(r"(?<![a-z0-9])" + re.escape(w) + r"(?![a-z0-9])", t) is not None
    def skeys(st):
        n = notes.get(st["id"]) or {}
        hard = {c.lower() for c in st["cves"]} | {x["appId"] for x in st.get("apps") or [] if x.get("appId") and x.get("kind") != "tenant"}
        words = {w.lower() for w in (n.get("match") or []) if len(w) >= 4} | {w for w in re.findall(r"storm-\d{3,5}", st["title"].lower())}
        # a name the title coins (PHP2Shell, NeedyMantis, ARTEX) - never an ordinary word the grouping happened to pick
        for w in re.findall(r"\b(?:\w*\d\w*[A-Za-z]\w*|[A-Z][a-z]+[A-Z]\w+|[A-Z]{4,})\b", st["title"]):
            if w.upper() not in COMMON_CAPS and not re.match(r"(?i)^(cve|\d)", w) and len(w) >= 4:
                words.add(w.lower())
        return hard, words
    ST = {st["id"]: (stext(st), ) + skeys(st) for st in stories}
    for st in stories:
        t, hard, words = ST[st["id"]]
        rel = []
        for o in stories:
            if o["id"] == st["id"]:
                continue
            ot, oh, ow = ST[o["id"]]
            why = sorted(hard & oh) or [w for w in words if wb(w, ot)] or [w for w in ow if wb(w, t)]
            if why:
                rel.append({"id": o["id"], "title": o["title"], "why": why[:3]})
        st["related"] = rel[:5]
    # digest queries (one post, several incidents): attached to the incident their section names - re-matched every run
    def best_story(title_, ctx_):
        # the section's own heading decides; its body counts only for an app ID or a CVE (hard keys)
        norm = lambda x: re.sub(r"[\u2013\u2014]", "-", x or "").lower()
        tt, tc, best = norm(title_), norm(ctx_), (0, "")
        for st in stories:
            _, hard, words = ST[st["id"]]
            sc = 3 * sum(1 for h in hard if h in tt or h in tc) + 3 * sum(1 for w in words if wb(w, tt))
            if sc > best[0]:
                best = (sc, st["id"])
        return best[1] if best[0] >= 3 else ""
    for q in kq:
        if q.get("digest"):
            q["story"] = best_story(q.get("title", ""), q.get("context", ""))
    for q in kby.values():
        if q.get("digest"):
            q["story"] = best_story(q.get("title", ""), q.get("context", ""))
    # community repositories (cache/kql-repos.json, tools/kql_repos.py): a query naming the incident's app ID, CVE or name
    try:
        repo_q = json.load(open(os.path.join(os.path.dirname(os.path.abspath(src_path)), "cache", "kql-repos.json"), encoding="utf-8")).get("queries") or []
    except Exception:
        repo_q = []
    for st in stories:
        _, hard, words = ST[st["id"]]
        hit = []
        for q in repo_q:
            # an app ID or a CVE anywhere in the query; a name only in its title or description (a list of RMM tools
            # that happens to include ConnectWise is not a query about this incident)
            tq = (q.get("title", "") + " " + q.get("description", "") + " " + q.get("query", "")).lower()
            th = (q.get("title", "") + " " + q.get("description", "")).lower()
            w = [k for k in hard if k in tq] + [k for k in words if len(k) >= 5 and wb(k, th)]
            if w:
                hit.append({"key": q["key"], "title": q["title"], "query": q["query"], "repo": q.get("repo"), "author": q.get("author"),
                            "license": q.get("license"), "link": q.get("link"), "tables": q.get("tables") or [], "why": w[:3]})
        st["kqlCommunity"] = hit[:8]
    kcut = (now - dt.timedelta(days=KQL_KEEP)).strftime("%Y-%m-%d")
    kall = sorted([q for q in kby.values() if (q.get("firstSeen") or "")[:10] >= kcut],
                  key=lambda q: (q.get("published") or q.get("firstSeen") or "", q["key"]), reverse=True)
    # 5ez: the counts every tile and row shows - analysis / sources (articles, digests, the analysis's kqlPublished) /
    # community repositories; a related incident's queries are shown under it, counted on their own incident
    for st in stories:
        n = notes.get(st["id"]) or {}
        arts_ = set(st["articles"])
        src_keys = {q["key"] for q in kall if q.get("story") == st["id"] or q.get("article") in arts_}
        st["kqlAnalysis"] = len(n.get("kql") or [])
        st["kqlSources"] = len(src_keys) + len(n.get("kqlPublished") or [])
        st["kqlVendor"] = len({q["key"] for q in kall if q["key"] in src_keys and q.get("vendor")}) + \
            sum(1 for x in n.get("kqlPublished") or [] if x.get("vendor"))
        st["kqlCommunityN"] = len(st.get("kqlCommunity") or [])
        st["kql"] = st["kqlAnalysis"] + st["kqlSources"] + st["kqlCommunityN"]
        st["why"] = [w for w, on in (("m365", st["scope"] == "m365"), ("kql", st["kql"] > 0), ("analysis", bool(n))) if on]
    kbody = {"source": "tools/threats.py (CLAUDE.md 5eu)", "keepDays": KQL_KEEP, "queries": kall}
    try:
        old_k = json.load(open(kpath, encoding="utf-8"))
    except Exception:
        old_k = {}
    if {k: v for k, v in old_k.items() if k != "generated"} != kbody:
        json.dump(dict(generated=stamp, **kbody), open(kpath, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print("threats: %d Kusto queries in articles (%d found this run, %d pages read)" % (len(kall), len(kq), KQL_PAGES - budget[0]))

    # ---- trend ----
    days = [(now.date() - dt.timedelta(days=i)).isoformat() for i in range(TREND_DAYS - 1, -1, -1)]
    trend = {"days": days, "areas": {a: [0] * TREND_DAYS for a, _ in AREAS}, "articles": [0] * TREND_DAYS, "stories": [0] * TREND_DAYS}
    pos = {d: i for i, d in enumerate(days)}
    for a in arts:
        i = pos.get(day(a))
        if i is None:
            continue
        trend["articles"][i] += 1
        for ar in a["areas"]:
            if ar in trend["areas"]:
                trend["areas"][ar][i] += 1
    for s in stories:
        i = pos.get(s["firstReported"])
        if i is not None:
            trend["stories"][i] += 1
    for a in arts:
        a.pop("names", None)
    body = {"source": "tools/threats.py (CLAUDE.md 5el)", "sources": srep, "stories": stories, "articles": arts,
            "kev": kev[:60], "trend": trend, "notesFile": notes_path, "keepDays": KEEP_DAYS,
            # the day the portal started tracking (kept between runs): stories reported before it are "new to the portal"
            # on that day, not new events (CLAUDE.md 5en)
            "started": prev.get("started") or "2026-10-19",
            # 5ez: digest posts read (they are not articles) - the page is read once
            "digests": digest_seen + [d for l_, d in dprev.items() if l_ not in {x["link"] for x in digest_seen}][:60]}
    strip_t = lambda d: {k: v for k, v in d.items() if k != "generated"}
    if prev and strip_t(prev) == body:
        print("threats: no change (%d stories, %d articles)" % (len(stories), len(arts)))
        return 0
    body = dict(generated=stamp, **body)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    json.dump(body, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print("threats: changed - %d sources (%d failed), %d articles, %d stories (%d curated, %d described by Microsoft), %d KEV"
          % (len(srep), sum(1 for r in srep if r["state"] != "ok"), len(arts), len(stories),
             sum(1 for s in stories if s["curated"]), sum(1 for s in stories if s["microsoft"]["status"] == "described"), len(kev)))
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    notes = a[a.index("--notes") + 1] if "--notes" in a else "threat_notes.json"
    pos = [x for i, x in enumerate(a) if not x.startswith("--") and (i == 0 or a[i - 1] != "--notes")]
    try:
        sys.exit(main(*(pos[:2]), notes_path=notes))
    except Exception as e:
        print("threats: skipped - %s" % e)
