#!/usr/bin/env python3
"""threat_todo.py - the morning routine's helper for Threat Research notes (CLAUDE.md 5el-b, 19 X 2026).

  python3 tools/threat_todo.py todo  [--days 3] [--backlog 30] [--max 5]  -> stories that need a note (JSON on stdout)
  python3 tools/threat_todo.py check                        -> validates site/data/threat-notes.json, exit 1 on error

Two notes files, read by tools/threats.py in this order (the first one wins on a repeated id):
  threat_notes.json              - written by a person; the routine never edits it
  site/data/threat-notes.json    - written by the morning routine (inside site/, the only folder a routine may touch)

`todo` lists, best first:
  new     - a story NOT yet analysed, first seen or updated in the last --days days (a first run's baseline of
            older stories is never a to-do: the owner asked for what is happening now);
  update  - a story analysed by the routine whose newest article is newer than the note's `updated` date.
  enrich  - (5ez) a routine note written before `apps`, `phase` and `kqlPublished` existed: `missing` names what to add,
            `appsFoundInArticles` the application IDs the articles name (verify them against the source before copying).
  backlog - when fewer than --max are new or updated, a story not yet analysed from the last --backlog days, highest
            score first, so the stories that were already on the tab on its first day get their notes a few a day.
A story analysed by a person that gained articles is listed under `ownerNotes` for information only.

`check` refuses (exit 1) a routine note that the page could not render honestly: no source link, a remediation step
`from: source` with no named source, a `phase` outside contain|investigate|eradicate|harden|detect, an `apps` entry
without `name`/`src` or with an appId that is not a lowercase GUID, a `kqlPublished` entry without title/query/src/link
(5ez), a `match` word so common that it would pull unrelated articles into the story,
an id already used by a person's note. Warnings (exit 0) for a `match` that hits no article yet.
"""
import datetime as dt, json, re, sys

THREATS = "site/data/threats.json"
OWNER = "threat_notes.json"
ROUTINE = "site/data/threat-notes.json"
AREAS = {"Apps & OAuth", "Identity attacks", "Roles & privilege", "Hybrid & federation", "M365 workloads", "Vulnerabilities"}
STATUS = {"active", "contained", "resolved"}
# a match word must name THIS event; these name a whole field and would glue unrelated articles together
GENERIC = {"microsoft", "entra", "azure", "office", "m365", "microsoft 365", "phishing", "phish", "attack", "attacks",
           "oauth", "token", "tokens", "tenant", "tenants", "identity", "malware", "ransomware", "credential",
           "credentials", "vulnerability", "exploit", "campaign", "breach", "mfa", "teams", "exchange", "outlook",
           "sharepoint", "onedrive", "copilot", "graph", "consent", "service principal", "aitm", "device code",
           "password spray", "supply chain", "threat", "security", "cloud", "windows", "admin", "global admin"}
URL = re.compile(r"^https?://[^\s]+$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# 5ez (22 X 2026): the morning routine's scheduled-task prompt is edited by hand by the owner, so the rules for the
# fields added that day travel in the `todo` output itself - the routine reads it before writing any note
RULES = [
    "5ff - when a researcher's post on X names domains / IPs of THIS incident (Steven Lim x.com/0x534c and others - found with WebSearch: incident name + 'x.com' or the handle), add its URL to `posts` (a list of https://x.com/<handle>/status/<id>). You cannot open x.com - IOC watch reads the post's text and images (OCR) by code and lists the indicators with the post as the reason. Never copy domains from a search snippet into `iocs`.",
    "5ez - every note where a service principal, enterprise application, app registration, managed identity or OAuth app is involved MUST carry `apps`: one entry per application with `name`, `appId` (the application (client) ID as a lowercase GUID copied character for character from the source - never typed from memory, omitted when the source prints none), `kind`, `did` (what it did), `roles`, `permissions`, `action` (what the sources say, e.g. 'Disable - do not delete'), `src`, `link`. A tenant ID or object ID goes in `appsNote`. `appsFoundInArticles` is a hint found by code: verify each ID in the source.",
    "5ez - every remediation step MUST carry `phase`: contain | investigate | eradicate | harden | detect. Steps `from: ours` are shown in their own 'Our proposal' box - write them as concrete actions.",
    "5ez - before writing your own KQL, search for queries already published for THIS incident by the vendor (Microsoft Threat Intelligence / Security / Sentinel / Defender XDR blogs, the affected vendor's advisory) and the community (detect.fyi, kqlquery.com, devsecopsdadattack.com, Steven Lim x.com/0x534c and github.com/SlimKQL, KQL Search MCP): WebSearch with the incident name / CVE / app ID plus 'KQL'. Record each in `kqlPublished` (`title`, `query` as published, `by`, `src`, `link`, `date`, `vendor: true` for Microsoft or the affected vendor). x.com cannot be fetched - record the post link and only what the search result shows. Never rewrite a published query as theirs, never invent one. Nothing found: `kqlSearched: \"YYYY-MM-DD\"`. Queries already in the story's articles are shown automatically - do not copy them.",
    "5ez - action `enrich`: an older note of yours; add only the fields named in `missing`, keep the rest, set `updated` to today.",
]
GUID = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
PHASES = {"contain", "investigate", "eradicate", "harden", "detect"}


def load(p, default):
    try:
        return json.load(open(p, encoding="utf-8"))
    except FileNotFoundError:
        return default


def art_index(T):
    return {a["id"]: a for a in T.get("articles") or []}


def todo(days, maxn, backlog=30):
    T = load(THREATS, {})
    owner = {n["id"] for n in load(OWNER, {"stories": []}).get("stories", [])}
    mine = {n["id"]: n for n in load(ROUTINE, {"stories": []}).get("stories", [])}
    A = art_index(T)
    now = dt.datetime.now(dt.timezone.utc)
    cut = (now - dt.timedelta(days=days)).strftime("%Y-%m-%d")
    bcut = (now - dt.timedelta(days=backlog)).strftime("%Y-%m-%d")
    out, info = [], []
    for s in T.get("stories") or []:
        last = (s.get("lastUpdate") or "")[:10]
        seen = (s.get("firstSeen") or "")[:10]
        arts = [A[i] for i in s.get("articles") or [] if i in A]
        row = {"id": s["id"], "title": s["title"], "firstReported": s.get("firstReported"), "firstSeen": seen,
               "lastUpdate": last, "score": s.get("score"), "areas": s.get("areas"), "cves": s.get("cves"),
               "words": s.get("words"), "sources": s.get("sources"),
               "microsoft": (s.get("microsoft") or {}).get("status"),
               "microsoftItems": [{"title": m.get("title"), "link": m.get("link"), "date": m.get("date")}
                                  for m in (s.get("microsoft") or {}).get("items") or []],
               "articles": [{"source": a.get("source"), "title": a.get("title"), "link": a.get("link"),
                             "published": (a.get("published") or a.get("firstSeen") or "")[:10]} for a in arts]}
        if s.get("curated"):
            upd = ((s.get("notes") or {}).get("updated") or "")[:10]
            if last and upd and last > upd:
                if s["id"] in mine:
                    row["action"], row["noteUpdated"] = "update", upd
                    out.append(row)
                elif s["id"] in owner:
                    info.append({"id": s["id"], "lastUpdate": last, "noteUpdated": upd,
                                 "say": "a person's note; new articles since it was written - not edited by the routine"})
            elif s["id"] in mine:
                # 5ez: a note written before the fields existed - add the applications involved, the phases and the KQL
                # the vendor / community published (an `enrich` pass reads the same articles once more)
                n = mine[s["id"]]
                miss = []
                if not n.get("apps") and (s.get("apps") or re.search(r"service principal|app registration|multi-tenant app|enterprise app|oauth app",
                                                                      json.dumps(n).lower())):
                    miss.append("apps")
                if any(not r.get("phase") for r in n.get("remediation") or []):
                    miss.append("phase")
                if not n.get("kqlPublished") and not n.get("kqlSearched"):
                    miss.append("kqlPublished")
                if miss:
                    row["action"], row["missing"], row["noteUpdated"] = "enrich", miss, upd
                    row["appsFoundInArticles"] = [{k: a.get(k) for k in ("appId", "name", "src", "link")} for a in s.get("apps") or [] if a.get("origin") == "source"]
                    out.append(row)
            continue
        if max(last, seen) >= cut:
            row["action"] = "new"
        elif max(last, seen) >= bcut:
            row["action"] = "backlog"
        else:
            continue
        out.append(row)
    rank = {"update": 0, "new": 1, "enrich": 2, "backlog": 3}
    out.sort(key=lambda r: (rank[r["action"]], -(r["score"] or 0)))
    print(json.dumps({"date": dt.date.today().isoformat(), "days": days, "max": maxn, "rules": RULES, "todo": out[:maxn],
                      "notListed": max(0, len(out) - maxn), "ownerNotes": info}, ensure_ascii=False, indent=1))
    return 0


def check():
    errs, warns = [], []
    T = load(THREATS, {})
    texts = [(a.get("title", "") + " " + a.get("summary", "")).lower() for a in T.get("articles") or []]
    owner = {n["id"] for n in load(OWNER, {"stories": []}).get("stories", [])}
    try:
        D = json.load(open(ROUTINE, encoding="utf-8"))
    except FileNotFoundError:
        print("check: %s does not exist yet - nothing to check" % ROUTINE)
        return 0
    except Exception as e:
        print("check: ERROR %s is not valid JSON: %s" % (ROUTINE, e))
        return 1
    if not isinstance(D.get("stories"), list):
        errs.append("top level needs a `stories` list")
    ids = set()
    for n in D.get("stories") or []:
        i = n.get("id") or "?"
        def E(m):
            errs.append("%s: %s" % (i, m))
        if not re.match(r"^[a-z0-9][a-z0-9-]{4,80}$", i):
            E("id must be a lowercase slug (a-z, 0-9, -)")
        if i in ids:
            E("id used twice in this file")
        if i in owner:
            E("id already used by a person's note in threat_notes.json - choose another id")
        ids.add(i)
        for k in ("title", "summary", "updated", "status", "by"):
            if not n.get(k):
                E("missing `%s`" % k)
        if n.get("updated") and not DATE.match(n["updated"]):
            E("`updated` must be YYYY-MM-DD")
        if n.get("status") and n["status"] not in STATUS:
            E("`status` must be one of %s" % sorted(STATUS))
        if len(n.get("summary") or "") < 80:
            E("`summary` shorter than 80 characters")
        bad = [a for a in n.get("areas") or [] if a not in AREAS]
        if not n.get("areas") or bad:
            E("`areas` must be a non-empty subset of %s%s" % (sorted(AREAS), (" (bad: %s)" % bad) if bad else ""))
        m = n.get("match") or []
        if not m:
            E("`match` is empty - the note would attach to no article")
        for w in m:
            wl = w.lower().strip()
            if len(wl) < 4:
                E("match word %r shorter than 4 characters" % w)
            if wl in GENERIC:
                E("match word %r names a whole field, not this event" % w)
            hits = sum(1 for t in texts if wl in t)
            if hits > 15:
                E("match word %r hits %d articles - too broad" % (w, hits))
        if m and texts and not any(any(w.lower() in t for t in texts) for w in m):
            warns.append("%s: no article in threats.json carries any match word yet" % i)
        tl = n.get("timeline") or []
        if not tl:
            E("`timeline` needs at least one entry")
        for t in tl:
            if not DATE.match(t.get("date") or "") or not t.get("text"):
                E("timeline entry needs `date` YYYY-MM-DD and `text`")
        rem = n.get("remediation") or []
        if not rem:
            E("`remediation` needs at least one step")
        for r in rem:
            if r.get("from") not in ("source", "ours"):
                E("remediation `from` must be `source` or `ours`")
            if r.get("from") == "source" and not r.get("src"):
                E("remediation step from a source must name it in `src`")
            if not r.get("text"):
                E("remediation step without `text`")
        links = n.get("links") or []
        if not links:
            E("`links` needs at least one source link")
        for l in links + [x for x in n.get("microsoft") or []]:
            u = l.get("url") or l.get("link") or ""
            if not URL.match(u):
                E("link %r is not an http(s) URL" % u)
        for q in n.get("kql") or []:
            if not q.get("title") or not q.get("query"):
                E("kql entry needs `title` and `query`")
        for p in n.get("portal") or []:
            if p.get("kind") not in ("permission", "role") or not p.get("label"):
                E("portal entry needs `label` and `kind` permission|role")
        # 5ez: applications involved, phases, KQL the vendor or the community published
        for r in rem:
            if r.get("phase") and r["phase"] not in PHASES:
                E("remediation `phase` must be one of %s" % sorted(PHASES))

        fresh = (n.get("updated") or "") >= "2026-10-23"    # 5ez: notes written from 23 X on must carry the new fields
        if fresh and any(not r.get("phase") for r in rem):
            E("remediation step without `phase` (required from 23 Oct 2026 - see `rules` in the todo output)")
        elif any(not r.get("phase") for r in rem):
            warns.append("%s: %d remediation step(s) without `phase` (the page guesses it from the first verb)" % (i, sum(1 for r in rem if not r.get("phase"))))
        for a in n.get("apps") or []:
            if not a.get("name") or not a.get("src"):
                E("apps entry needs `name` and `src` (the source that names it)")
            if a.get("appId") and not GUID.match(a["appId"]):
                E("apps `appId` %r is not a GUID" % a["appId"])
            if a.get("appId") and a["appId"] != a["appId"].lower():
                E("apps `appId` %r must be lowercase" % a["appId"])
            for k in ("roles", "permissions"):
                if a.get(k) is not None and not isinstance(a[k], list):
                    E("apps `%s` must be a list" % k)
        blob = json.dumps(n).lower()
        if fresh and re.search(r"service principal|app registration|multi-tenant app|enterprise app|oauth app|client credential", blob) and not n.get("apps"):
            E("the note involves service principals / app registrations but has no `apps` list (required from 23 Oct 2026)")
        elif re.search(r"service principal|app registration|multi-tenant app|enterprise app|oauth app|client credential", blob) and not n.get("apps"):
            warns.append("%s: the note talks about service principals / app registrations but has no `apps` list" % i)
        for q in n.get("kqlPublished") or []:
            for k in ("title", "query", "src", "link"):
                if not q.get(k):
                    E("kqlPublished entry needs `%s`" % k)
            if q.get("link") and not URL.match(q["link"]):
                E("kqlPublished link %r is not an http(s) URL" % q["link"])
        if fresh and not n.get("kqlPublished") and not n.get("kqlSearched"):
            E("no `kqlPublished` and no `kqlSearched` date - search for the vendor's and the community's queries first (required from 23 Oct 2026)")
    for w in warns:
        print("check: WARN " + w)
    for e in errs:
        print("check: ERROR " + e)
    print("check: %d notes, %d errors, %d warnings" % (len(D.get("stories") or []), len(errs), len(warns)))
    return 1 if errs else 0


if __name__ == "__main__":
    a = sys.argv[1:]
    cmd = a[0] if a else "todo"
    opt = lambda k, d: int(a[a.index(k) + 1]) if k in a else d
    if cmd == "todo":
        sys.exit(todo(opt("--days", 3), opt("--max", 5), opt("--backlog", 30)))
    if cmd == "check":
        sys.exit(check())
    print(__doc__)
    sys.exit(2)
