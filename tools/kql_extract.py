#!/usr/bin/env python3
"""kql_extract.py - find Kusto (KQL) queries in an article or a file (CLAUDE.md 5eu, 21 X 2026).

Owner, 21 X 2026: "we follow incidents in Threat Research, mostly Microsoft 365 - but if somewhere in the world an
incident is described with KQL that helps the analysis (the newest PHP2Shell on detect.fyi), we should collect it too;
store the full text and the link". Used by tools/threats.py (articles), tools/kql_repos.py (community repositories)
and tools/kql_archive.py (one archive in site/kql/).

Kusto, not Kibana: Elastic also calls its query language "KQL". A block counts as Kusto only when it has pipe
operators (| where, | summarize, | project ...) AND names a Microsoft Defender XDR / Sentinel / Entra / Log Analytics
table, or starts with let / union / a table name followed by a pipe.

    python3 tools/kql_extract.py FILE.html      # prints what it finds (a test)
"""
import hashlib, html, re, sys

TABLE = re.compile(r"\b(?:AuditLogs|SigninLogs|AADNonInteractiveUserSignInLogs|AADServicePrincipalSignInLogs|AADManagedIdentitySignInLogs|"
                   r"AADProvisioningLogs|AADRiskyUsers|AADUserRiskEvents|AADRiskyServicePrincipals|AADServicePrincipalRiskEvents|"
                   r"OfficeActivity|SecurityEvent|SecurityAlert|SecurityIncident|Usage|Heartbeat|Syslog|CommonSecurityLog|Event|"
                   r"MicrosoftGraphActivityLogs|IntuneAuditLogs|IntuneDevices|IntuneOperationalLogs|AzureActivity|AzureDiagnostics|"
                   r"W3CIISLog|AppServiceHTTPLogs|ThreatIntelligenceIndicator|ThreatIntelIndicators|BehaviorAnalytics|IdentityInfo|"
                   r"StorageBlobLogs|KeyVaultEvents|CloudKeyVaultEvents|ContainerLog|KubeEvents|LAQueryLogs|Watchlist|"
                   r"(?:Device|Identity|Email|Url|Cloud|Alert|EntraId|Behavior|Exposure|Campaign|AIAgents?|Agents?|Message|"
                   r"GraphApiAudit|DisruptionAndResponse|FileMaliciousContent|OAuthApp)[A-Za-z]*"
                   r"(?:Events|Info|Logs|Vulnerabilities|Evidence|Activity|PostDeliveryEvents|Entities|Inventory|Assessments?|"
                   r"Nodes|Edges|UrlInfo|Configuration\w*|KB|Software\w*))\b")
OPS = re.compile(r"\|\s*(?:where|summarize|project(?:-\w+)?|extend|join|take|limit|top|count|distinct|parse|mv-expand|make-series|"
                 r"order|sort|render|lookup|invoke|evaluate|union|as|search|getschema|serialize|scan)\b")
START = re.compile(r"^\s*(?:let\s+\w+\s*=|union\b|search\b|[A-Z][A-Za-z_]+\s*(?:\(|$|\|))", re.M)
PRODUCT = [(r"^(?:Device|DeviceTvm)", "Defender for Endpoint"), (r"^Identity", "Defender for Identity"), (r"^(?:Email|Url)", "Defender for Office 365"),
           (r"^(?:CloudAppEvents|OAuthApp)", "Defender for Cloud Apps"), (r"^(?:AuditLogs|SigninLogs|AAD|EntraId|MicrosoftGraph|GraphApiAudit)", "Entra"),
           (r"^(?:OfficeActivity)", "Microsoft 365"), (r"^Intune", "Intune"),
           (r"^(?:Usage|Heartbeat|Security|Syslog|CommonSecurityLog|AzureActivity|AzureDiagnostics|W3CIISLog|Event$|ThreatIntel|BehaviorAnalytics|Watchlist)", "Sentinel"),
           (r"^(?:Alert|Behavior|Exposure|Campaign|AIAgents|Agents|Message|DisruptionAndResponse|FileMaliciousContent)", "Defender XDR")]


def text(fragment):
    f = re.sub(r"(?i)<br\s*/?>", "\n", fragment)
    f = re.sub(r"(?i)</(?:p|div|li|tr)>", "\n", f)
    return html.unescape(html.unescape(re.sub(r"<[^>]+>", "", f)))


def tables(code):
    return sorted(set(TABLE.findall(code)))


def product(tbls):
    return next((p for rx, p in PRODUCT for t in tbls if re.search(rx, t)), "Sentinel" if tbls else "")


def is_kusto(code):
    lines = [l for l in code.splitlines() if l.strip() and not l.strip().startswith("//")]
    if len(lines) < 2:
        return False
    body = "\n".join(lines)
    if not OPS.search(body):
        return False
    if re.search(r"(?i)\b(?:index\s*=|sourcetype\s*=|stats\s+count\s+by|SELECT\s+\w+\s+FROM|event\.code\s*:|process\.name\s*:)", body):
        return False      # Splunk SPL, SQL, Elastic
    return bool(tables(body)) or bool(START.search(body))


def key(code):
    c = "\n".join(l for l in code.splitlines() if not l.strip().startswith("//"))
    return hashlib.sha1(re.sub(r"\s+", " ", c).strip().encode()).hexdigest()[:16]


def blocks(page_html):
    """Kusto blocks of an HTML article: <pre>, <code> on several lines, Tech Community's <li-code>; each with the
    heading above it (h2-h4, or a bold line) as its title"""
    h = page_html or ""
    out, seen = [], set()
    rx = re.compile(r"(?is)<(pre|li-code|code)\b[^>]*>(.*?)</\1>")
    last = 0
    for m in rx.finditer(h):
        raw = m.group(2)
        if m.group(1).lower() == "code" and "\n" not in raw and "<br" not in raw.lower():
            continue
        code = text(raw).strip("\n")
        code = "\n".join(l.rstrip() for l in code.splitlines()).strip()
        if not is_kusto(code):
            last = m.end(); continue
        k = key(code)
        if k in seen:
            last = m.end(); continue
        seen.add(k)
        seg = h[max(last, m.start() - 6000):m.start()]   # only what stands between the previous block and this one
        # a real heading first (h1-h5); a bold line only when there is none ("Required telemetry:" is not a title)
        hs = []
        for pat in (r"(?is)<h[1-5]\b[^>]*>(.*?)</h[1-5]>", r"(?is)<(?:strong|b)\b[^>]*>(.*?)</(?:strong|b)>"):
            hs = [re.sub(r"\s+", " ", text(x)).strip() for x in re.findall(pat, seg)]
            hs = [x for x in hs if 6 <= len(x) <= 160 and not x.endswith(":")]
            if hs:
                break
        com = [l.strip()[2:].strip() for l in code.splitlines() if l.strip().startswith("//") and len(l.strip()) > 8]
        title = hs[-1] if hs else (com[0] if com else "")
        # 5ez: a section heading that only names the part ("KQL", "Query", "Deployment Gates") is not a title - take
        # the h2 above it ("Detection 4: ConnectWise Agent Spawning ..."), and the text under that h2 is the context
        h2s = [x for x in re.finditer(r"(?is)<h[12]\b[^>]*>(.*?)</h[12]>", h[:m.start()]) if len(text(x.group(1)).strip()) >= 6]
        sec = h2s[-1] if h2s else None
        if sec and (not title or len(title) < 20 or re.match(r"(?i)^(kql|query|queries|hunting quer|detection logic|deployment gates?|code|sentinel|defender)", title)):
            title = re.sub(r"\s+", " ", text(sec.group(1))).strip()
        if sec:
            seg = h[sec.start():m.start()]
        # 5ez: the text between the previous block and this one - a digest post (one page, several incidents) is
        # matched to an incident by it
        ctx = re.sub(r"\s+", " ", text(seg)).strip()[:1500]
        out.append({"key": k, "title": title[:160], "query": code, "tables": tables(code), "product": product(tables(code)), "context": ctx})
        last = m.end()
    return out


GUID = re.compile(r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b")
APPWORD = re.compile(r"(?i)app(?:lication)?\s*(?:\(client\)\s*)?id|client\s*id|\bappid\b|service principal|enterprise app|"
                     r"app registration|multi-?tenant|oauth app|application")


def app_ids(page_html):
    """5ez (owner 22 X: "many sites describe the ConnectWise incident and show the application IDs involved - why do you
    not even mention them?"): every GUID in an article that stands beside application words, with the text of its
    table row / list item / paragraph as the name. A GUID beside the word tenant is a tenant ID (an indicator), not an
    application. Returned as found in the source - the page labels them so; the analysis confirms them."""
    h = re.sub(r"(?is)<(script|style|nav|footer|header)\b.*?</\1>", " ", page_html or "")
    out, seen = [], set()
    for m in re.finditer(r"(?is)<(tr|li|p|h[2-5]|td|pre|code)\b[^>]*>(.*?)</\1>", h):
        raw = m.group(2)
        cells = [re.sub(r"\s+", " ", text(c)).strip() for c in re.findall(r"(?is)<t[dh]\b[^>]*>(.*?)</t[dh]>", raw)] if m.group(1).lower() == "tr" else []
        line = " | ".join(c for c in cells if c) if cells else re.sub(r"\s+", " ", text(raw)).strip()
        for g in GUID.findall(line):
            gl = g.lower()
            if gl in seen:
                continue
            ctx = h[max(0, m.start() - 1500):m.end()]
            if not APPWORD.search(text(ctx)):
                continue
            seen.add(gl)
            if cells:
                nm = [c for c in cells if not GUID.search(c) and 3 <= len(c) <= 90]
            else:   # a sentence: the capitalised name right before the GUID ("... ConnectWise Cloud Backup (506e08f9-...)")
                pre = line[:line.lower().find(gl)].replace("\u200b", "")
                mm = re.search(r"([A-Z][\w.&/]*(?:\s*[-\u2013]?\s*[A-Z0-9][\w.&/]*){0,7})[\s:(\[\u2013\u2014-]*$", pre)
                nm = [mm.group(1)] if mm and len(mm.group(1)) >= 4 else []
            kind = "tenant" if re.search(r"(?i)tenant\s*id|owner tenant|tenant", line) and not re.search(r"(?i)app(?:lication)?\b", line) else "app"
            out.append({"appId": gl, "name": (nm[0].strip() if nm else ""), "kind": kind, "context": line[:240]})
    return out


def from_text(s):
    """Kusto blocks in plain text or Markdown (```kql fences, or a whole .kql file)"""
    out = []
    fences = re.findall(r"(?s)```[ \t]*(?:kql|kusto|KQL|Kusto|sql)?[ \t]*\n(.*?)```", s)
    for code in (fences or [s]):
        code = code.strip()
        if is_kusto(code):
            out.append({"key": key(code), "query": code, "tables": tables(code), "product": product(tables(code))})
    return out


if __name__ == "__main__":
    for f in sys.argv[1:]:
        raw = open(f, encoding="utf-8", errors="replace").read()
        found = blocks(raw) if "<" in raw[:2000] else from_text(raw)
        print("%s: %d Kusto block(s)" % (f, len(found)))
        for b in found:
            print(" -", b.get("title") or "(no title)", "|", ", ".join(b["tables"]), "|", b["query"].splitlines()[0][:80])
