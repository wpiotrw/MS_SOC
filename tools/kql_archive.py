#!/usr/bin/env python3
"""kql_archive.py - keep every KQL query the brief has published in site/kql/ (CLAUDE.md 5l, 5cv-c).

The Hunting & actions tab carries the newest queries only; the archive in the repository keeps all of them:
one file per query, site/kql/<date>-<slug>.kql, and site/kql/index.json (file, title, date, product, tables,
purpose, source, reused). The routine was meant to write it and stopped after 31 Aug 2026 (owner, 9 X 2026:
"is it refreshed daily? does it keep the queries found before in a folder on GitHub? - that was the process").
This script does it from the published page itself, so it no longer depends on a prompt:

    python3 tools/kql_archive.py                 # the current page, site/index.html
    python3 tools/kql_archive.py --backfill      # also every morning page kept in site/history/

A query identical to one already archived (same code once comments and spacing are removed) gets no new file:
its index entry gains the date in "reused". Nothing is ever deleted.
"""
import glob
import gzip
import hashlib
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")
KQL = os.path.join(SITE, "kql")
INDEX = os.path.join(KQL, "index.json")
MONTHS = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
TABLE = re.compile(r"\b(?:AuditLogs|SigninLogs|AADNonInteractiveUserSignInLogs|AADServicePrincipalSignInLogs|AADManagedIdentitySignInLogs|"
                   r"OfficeActivity|SecurityEvent|SecurityAlert|SecurityIncident|Usage|Heartbeat|Syslog|CommonSecurityLog|"
                   r"MicrosoftGraphActivityLogs|IntuneAuditLogs|IntuneDevices|AzureActivity|"
                   r"(?:Device|Identity|Email|Url|Cloud|Alert|EntraId|Behavior|Exposure|Campaign|AIAgents?|Agents?|Message|"
                   r"GraphApiAudit|DisruptionAndResponse|FileMaliciousContent|OAuthApp)[A-Za-z]*"
                   r"(?:Events|Info|Logs|Vulnerabilities|Evidence|Activity|PostDeliveryEvents|Entities|Inventory|Assessments?|"
                   r"Nodes|Edges|UrlInfo|Configuration\w*|KB|Software\w*))\b")
PRODUCT = [(r"^(?:Device|DeviceTvm)", "Defender for Endpoint"), (r"^Identity", "Defender for Identity"), (r"^(?:Email|Url)", "Defender for Office 365"),
           (r"^(?:CloudAppEvents|OAuthApp)", "Defender for Cloud Apps"), (r"^(?:AuditLogs|SigninLogs|AAD|EntraId|MicrosoftGraph|GraphApiAudit)", "Entra"),
           (r"^(?:OfficeActivity)", "Microsoft 365"), (r"^Intune", "Intune"), (r"^(?:Usage|Heartbeat|Security|Syslog|CommonSecurityLog|AzureActivity)", "Sentinel"),
           (r"^(?:Alert|Behavior|Exposure|Campaign|AIAgents|Agents|Message|DisruptionAndResponse|FileMaliciousContent)", "Defender XDR")]


def hunting_section(page):
    m = re.search(r'id="tab-hunting".*?(?=id="tab-products"|<div class="tabpanel"[^>]*id="tab-(?!hunting))', page, re.S)
    if m:
        return m.group(0)
    m = re.search(r'<section[^>]*id="(?:kql|hunting)[^"]*".*?</section>', page, re.S)
    return m.group(0) if m else ""


def text(fragment):
    return html.unescape(html.unescape(re.sub(r"<[^>]+>", "", fragment)))


def page_date(page, fallback):
    m = re.search(r'id="soc-brief-state"[^>]*>\s*\{.{0,400}?"briefDate"\s*:\s*"(\d{4}-\d\d-\d\d)"', page, re.S) or \
        re.search(r'"briefDate"\s*:\s*"(\d{4}-\d\d-\d\d)"', page)
    return m.group(1) if m else fallback


def date_in(line, fallback):
    m = re.search(r"\b(\d{1,2})\s+([A-Za-z]{3})[a-z]*\.?\s+(\d{4})\b", line)
    if m and m.group(2).lower() in MONTHS:
        return "%s-%02d-%02d" % (m.group(3), MONTHS[m.group(2).lower()], int(m.group(1)))
    return fallback


def slug(t):
    w = re.findall(r"[a-z0-9]+", t.lower())
    return "-".join(w[:8])[:60].strip("-") or "query"


def body_key(q):
    code = "\n".join(l for l in q.splitlines() if not l.strip().startswith("//"))
    return hashlib.sha1(re.sub(r"\s+", " ", code).strip().encode()).hexdigest()


def queries(page, day):
    sec = hunting_section(page)
    out = []
    prev_end = 0
    for m in re.finditer(r"<pre[^>]*>(.*?)</pre>", sec, re.S):
        q = text(m.group(1)).strip("\n")
        code = [l for l in q.splitlines() if l.strip() and not l.strip().startswith("//")]
        if len(code) < 2 or not re.search(r"^\s*(?:let\b|union\b|[A-Z][A-Za-z]+\s*$|[A-Z][A-Za-z]+\s*\|)", "\n".join(code), re.M):
            prev_end = m.end()
            continue   # not KQL (a PowerShell or Graph snippet in the same tab)
        com = [l.strip()[2:].strip() for l in q.splitlines() if l.strip().startswith("//")]
        first = com[0] if com else ""
        title = re.sub(r"^Microsoft SOC Brief\s*[-—–]?\s*(?:\d{1,2}\s+\w+\s+\d{4})?\s*[-—–]?\s*", "", first).strip(" -—–")
        seg = sec[prev_end:m.start()]
        h4 = re.findall(r"<h4[^>]*>(.*?)</h4>", seg, re.S)
        if h4:   # the entry's own heading on the page is the title a reader searches for
            title = text(h4[-1]).strip()
            ps = [text(x).strip() for x in re.findall(r"<p>(.*?)</p>", seg[seg.rfind("<h4"):], re.S)]
            ps = [x for x in ps if len(x) > 40]
            lead = ps[0] if ps else ""
        else:
            lead = ""
        if not title:   # the heading of the entry the query belongs to (not its "Why now." / "Schema." labels)
            before = sec[prev_end:m.start()]
            h = [text(x).strip() for x in re.findall(r"<(?:h[2-5]|summary|b|strong|dt)[^>]*>(.*?)</(?:h[2-5]|summary|b|strong|dt)>", before, re.S)]
            h = [x for x in h if len(x) > 12 and not re.match(r"(?i)^(?:why now|schema|source|query|how to read|what it finds)\b", x)]
            title = h[0] if h else (com[0] if com else "Hunting query")
        title = re.sub(r"\s+", " ", title)[:160]
        tables = sorted(set(TABLE.findall("\n".join(code))))
        product = next((p for rx, p in PRODUCT for t in tables if re.search(rx, t)), "Microsoft 365")
        # the schema page of THIS entry: links between the previous query and the next one, the one naming a table first
        nxt = re.search(r"<pre[^>]*>", sec[m.end():])
        win = sec[prev_end:m.end() + (nxt.start() if nxt else 2500)]
        cand = [html.unescape(u) for u in re.findall(r'href="(https://learn\.microsoft\.com[^"]+)"', win)]
        links = [u for u in cand if any(t.lower() in u.lower() for t in tables)] or cand
        why = re.search(r"Why now\.?\s*(.+?)(?:Schema\.|$)", re.sub(r"\s+", " ", text(sec[prev_end:m.start()])))
        purpose = lead or (why.group(1).strip() if why else "") or \
            next((c for c in com[1:] if len(c) > 25 and not re.search(r"(?i)verified against|schema page", c)), "")
        out.append({"title": title, "date": date_in(first, day), "product": product, "tables": tables,
                    "purpose": purpose[:300], "source": links[0] if links else None, "query": q, "key": body_key(q)})
        prev_end = m.end()
    return out


def main(argv):
    os.makedirs(KQL, exist_ok=True)
    try:
        index = json.load(open(INDEX, encoding="utf-8"))
    except (OSError, ValueError):
        index = []
    keys = {}
    for e in index:
        try:
            keys[body_key(open(os.path.join(KQL, e["file"]), encoding="utf-8").read())] = e
        except OSError:
            pass
    pages = []
    if "--backfill" in argv:
        for f in sorted(glob.glob(os.path.join(SITE, "history", "*-poranny.html.gz"))):
            pages.append((gzip.open(f, "rt", encoding="utf-8").read(), os.path.basename(f)[:10]))
    cur = os.path.join(SITE, "index.html")
    if os.path.exists(cur):
        s = open(cur, encoding="utf-8").read()
        pages.append((s, page_date(s, "")))
    added = reused = 0
    names = {e["file"] for e in index}
    for page, day in pages:
        for q in queries(page, day):
            e = keys.get(q["key"])
            if e:
                if day and day != e.get("date") and day not in (e.get("reused") or []):
                    e.setdefault("reused", []).append(day)
                    reused += 1
                continue
            name = "%s-%s.kql" % (q["date"] or day or "undated", slug(q["title"]))
            n = 2
            while name in names:
                name = "%s-%s-%d.kql" % (q["date"] or day, slug(q["title"]), n)
                n += 1
            head = ["// title: " + q["title"], "// date: " + (q["date"] or day), "// product: " + q["product"],
                    "// tables: " + ", ".join(q["tables"]), "// purpose: " + (q["purpose"] or q["title"]),
                    "// source: " + (q["source"] or "see the brief of that day"), "// archived by tools/kql_archive.py (CLAUDE.md 5l)", ""]
            with open(os.path.join(KQL, name), "w", encoding="utf-8") as f:
                f.write("\n".join(head) + q["query"].rstrip() + "\n")
            e = {"file": name, "title": q["title"], "date": q["date"] or day, "product": q["product"], "tables": q["tables"],
                 "purpose": q["purpose"] or q["title"], "source": q["source"]}
            index.append(e)
            keys[q["key"]] = e
            names.add(name)
            added += 1
    index.sort(key=lambda e: (e.get("date") or "", e["file"]), reverse=True)
    with open(INDEX, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("OK kql archive: %d queries, %d new, %d reused today" % (len(index), added, reused))


if __name__ == "__main__":
    main(sys.argv[1:])
