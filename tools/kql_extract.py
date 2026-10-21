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
        hs = re.findall(r"(?is)<(?:h[1-5]|strong|b)\b[^>]*>(.*?)</(?:h[1-5]|strong|b)>", seg)
        hs = [re.sub(r"\s+", " ", text(x)).strip() for x in hs]
        hs = [x for x in hs if 6 <= len(x) <= 160]
        com = [l.strip()[2:].strip() for l in code.splitlines() if l.strip().startswith("//") and len(l.strip()) > 8]
        title = hs[-1] if hs else (com[0] if com else "")
        out.append({"key": k, "title": title[:160], "query": code, "tables": tables(code), "product": product(tables(code))})
        last = m.end()
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
