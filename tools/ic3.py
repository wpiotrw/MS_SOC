#!/usr/bin/env python3
"""ic3.py - FBI IC3 advisories for Threat Research and the infrastructure watch (CLAUDE.md 5gz, 17 XI 2026).
Author: Piotr Wisniewski.

Owner, 17 XI 2026: "would https://www.ic3.gov help in our Threat Research tab and our sources?" - and, after the proposal,
"do it as you proposed": the FBI's technical alerts (CSA, FLASH, joint advisories with CISA) as a government-advisory
source of Threat Research, joined to the incident they describe; their IOC files (CSV, STIX JSON) as indicators of the
infrastructure watch; and the public service announcements (PSA) only when they are technical.

    ic3.items(html, kind, base, get, known)   the advisories listed on https://www.ic3.gov/CSA or /PSA
    ic3.iocs(url, get)                        (kind, value, description) from one IOC file (CSV or STIX 2.1 JSON)

There is no RSS for CSA and the PSA feed carries five titles, so both list pages are read (they answer a browser-like
User-Agent). A CSA is a PDF: its "Summary" section is read once (pypdf, else pdftotext) and kept in the article, so a
PDF is never fetched twice. The IOC files listed right after a PDF belong to it (the page lists a PDF, then its CSV /
JSON / STIX). Nothing here ever fails the run: a page or a file that cannot be read gives an empty answer.
"""
import datetime as dt
import html as H
import io
import json
import re
import shutil
import subprocess
import tempfile

BASE = "https://www.ic3.gov"
LINK = re.compile(r'<a[^>]+href="(/(?:CSA|PSA)/(\d{4})/([^"#?]+))"[^>]*>(.*?)</a>', re.S | re.I)
IOC_EXT = (".csv", ".json")
LANG = re.compile(r"(?i)\bversi[oó]n\b|español|français|deutsch")          # STIX XML duplicates the STIX JSON
# a PSA is for the SOC only when it is technical: an attack, a vulnerability, a malware family, an account takeover
TECH = re.compile(r"(?i)phish|consent|oauth|malware|ransom|vulnerab|exploit|\bcve\b|zero-day|backdoor|botnet|intrusion|"
                  r"cyber (?:threat )?actors|credential|account takeover|supply chain|router|edge device|infostealer|"
                  r"remote (?:access|monitoring)|\brat\b|ddos|wiper|it workers")
NOT_SOC = re.compile(r"(?i)election|voter|swatting|white powder|sexual|sextortion|romance|elder|investment|lottery|"
                     r"law enforcement and government officials|kidnap|counterfeit|charity|refrigeration|water and wastewater|programmable logic|\bplcs?\b|industrial control|operational technology")


def _date(name, year):
    """261113.pdf / PSA261023-2 -> 2026-11-13; AA26-281A -> the 281st day of 2026"""
    m = re.search(r"(\d{2})(\d{2})(\d{2})", name)
    if m:
        try:
            return dt.date(2000 + int(m.group(1)), int(m.group(2)), int(m.group(3))).isoformat()
        except ValueError:
            pass
    m = re.search(r"AA(\d{2})-(\d{3})", name)
    if m:
        return (dt.date(2000 + int(m.group(1)), 1, 1) + dt.timedelta(days=int(m.group(2)) - 1)).isoformat()
    return year + "-01-01"


def _text(x):
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", x))).strip()


def pdf_text(data):
    """the text of a PDF: pypdf when installed, else poppler's pdftotext; '' when neither works"""
    try:
        import pypdf
        r = pypdf.PdfReader(io.BytesIO(data))
        return "\n".join((p.extract_text() or "") for p in r.pages[:4])
    except Exception:
        pass
    if shutil.which("pdftotext"):
        try:
            with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
                f.write(data); f.flush()
                return subprocess.run(["pdftotext", "-l", "4", f.name, "-"], capture_output=True, timeout=60).stdout.decode("utf-8", "replace")
        except Exception:
            pass
    return ""


def summary_of(text):
    """the advisory's own Summary paragraph, without the TLP marks and the footnote numbers"""
    t = re.sub(r"TLP:\w+", " ", text)
    m = re.search(r"(?s)\bSummary\b\s*(.+?)(?:\n\s*(?:Technical Details|Background|Threat Overview|Recommendations|Mitigations|"
                  r"Indicators|Tactics|Reporting)\b|$)", t)
    body = m.group(1) if m else t
    body = re.sub(r"(?<=[a-z.,)])(\d{1,2}(?:,\d{1,2})*)(?=\s)", "", body)    # footnote numbers: "globally.1,2,3"
    body = re.sub(r"\s+", " ", body).strip()
    return body[:1500]


def flash_no(text):
    m = re.search(r"\b(FLASH-\d{8}-\d{3}|AA\d{2}-\d{3}[A-Z]?|PIN-\d{8}-\d{3})\b", text)
    return m.group(1) if m else ""


def items(page, kind, get, known):
    """the advisories of one list page. kind 'csa' or 'psa'. known: link -> the article saved by the previous run
    (its summary is reused, so a PDF is read once). get(url) returns bytes."""
    out, last, reads = [], None, [0]
    for href, year, name, label in LINK.findall(page):
        url = BASE + href
        title = _text(label)
        low = name.lower()
        if kind == "csa" and low.endswith(IOC_EXT + (".xml",)):
            if last is not None and low.endswith(IOC_EXT):
                last["iocFiles"].append({"url": url, "label": title or name})
            continue
        if kind == "psa" and not name.upper().startswith("PSA"):
            continue
        if not title or any(o["link"] == url for o in out) or len(re.findall(r"[A-Za-z]", title)) < 8 or LANG.search(title):
            continue                               # a translation of the advisory above it ("日本語版", "Version en español")
        it = {"title": title, "link": url, "published": _date(name, year), "html": "", "author": "FBI IC3",
              "gov": kind.upper(), "iocFiles": [], "flash": "", "summary": ""}
        old = known.get(url) or {}
        if old.get("summary"):
            it["summary"], it["flash"] = old["summary"], old.get("flash") or ""
        elif reads[0] < 8 and (kind == "csa" or (TECH.search(title) and not NOT_SOC.search(title))):
            reads[0] += 1                          # a new advisory: read its text once
            try:
                raw = get(url)
                txt = pdf_text(raw) if low.endswith(".pdf") else _text(re.sub(r"(?is)<(script|style|nav|header|footer)\b.*?</\1>", " ", raw.decode("utf-8", "replace")))
                if kind == "psa":                  # the PSA page: the text after its title
                    txt = re.sub(r"(?i)^.*?\bSkip to main(?: content)?\b", "", txt)
                    i = txt.find(title[:40]); txt = txt[i + len(title):] if i >= 0 else txt
                    it["summary"] = re.sub(r"\s+", " ", txt).strip()[:1500]
                else:
                    it["summary"], it["flash"] = summary_of(txt), flash_no(txt)
            except Exception:
                pass
        out.append(it)
        last = it
    return out


def soc_relevant(title, summary):
    """a PSA reaches Threat Research only when technical; a CSA unless it is plainly outside a SOC's remit"""
    return bool(TECH.search(title + " " + summary[:400])) and not NOT_SOC.search(title)


STIX = re.compile(r"\[(domain-name|ipv4-addr|url):value\s*=\s*'([^']+)'\]")


def iocs(url, get):
    """(kind, value, description) from an IC3 IOC file: CSV 'IOC,Description' or a STIX 2.1 bundle"""
    try:
        raw = get(url).decode("utf-8", "replace")
    except Exception:
        return []
    out = []
    if url.lower().endswith(".csv"):
        for line in raw.splitlines()[1:]:
            parts = [p.strip().strip('"') for p in line.split(",", 1)]
            if not parts or not parts[0]:
                continue
            v, d = parts[0], (parts[1] if len(parts) > 1 else "")
            kind = "ip" if re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", v) else "url" if re.match(r"(?i)https?://", v) else \
                   "domain" if re.fullmatch(r"(?i)[a-z0-9-]+(?:\.[a-z0-9-]+)+", v) else ""
            if kind:
                out.append((kind, v, d))
    else:
        try:
            for o in json.loads(raw).get("objects") or []:
                if o.get("type") != "indicator":
                    continue
                for k, v in STIX.findall(o.get("pattern") or ""):
                    out.append(({"domain-name": "domain", "ipv4-addr": "ip"}.get(k, "url"), v, o.get("name") or o.get("description") or ""))
        except Exception:
            pass
    return out
