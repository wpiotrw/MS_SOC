#!/usr/bin/env python3
"""fpa_sources.py - our own copy of every First-party apps source, and Microsoft's docs list of app names
(CLAUDE.md 5cw-b). Runs in .github/workflows/fpa-tenant.yml every three hours.

Owner, 9 X 2026: "our portal was meant to stand on its own, Merill as a backup - what if external sources go
down?" and, after the comparison, "do B". This script:
  1. keeps the last good copy of each external source in cache/fpa/<key>.json (merill, roadtools, gpc and
     Microsoft's entra-docs known-guids.json - all under a licence that allows a copy; entrascopes.com has none
     and is not copied) with cache/fpa/index.json
     (fetched, sha256, bytes, ok). collect_fpa.py reads the copy when a source does not answer, and says from
     which day it is - so an outage freezes nothing and loses nothing;
  2. writes site/data/fpa-docs.json - the applications Microsoft names in entra-docs
     .docutune/dictionaries/known-guids.json. That file is a dictionary of every GUID in Learn content:
     Graph permission ids, licence SKUs, Azure and Entra roles, FIDO2 key AAGUIDs and Purview sensitive
     information types sit beside the app ids. Merill takes all of it as apps (3 659 of his 4 444 rows on
     9 X 2026); here only the entries that are apps are kept, by the classifier below, and the page shows
     them as "named only in Microsoft docs" where no other source carries the app.
Never prints an identifier from the tenant; reads no tenant data at all."""
import datetime, hashlib, json, os, re, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "cache", "fpa")
RAW = "https://raw.githubusercontent.com/"
SRC = {
    "merill": "merill/microsoft-info/main/_info/MicrosoftApps.json",
    "roadtools": "dirkjanm/ROADtools/master/roadtx/roadtools/roadtx/firstpartyscopes.json",
    "gpc": "zh54321/GraphPreConsentExplorer/main/lists/GraphPreConsent.json",
    # entrascopes.com (resources.json, bypasses.json) carries no licence file: it is read with credit and never
    # copied into this public repository, so it has no cached copy - it names APIs and bypasses, not apps
    "kg": "MicrosoftDocs/entra-docs/main/.docutune/dictionaries/known-guids.json",
}
FIDO = re.compile(r"(?i)security key|yubikey|yubico|fido|digipass|\btoken\b|biometric|\bbio\b|passkey|feitian|thales|ensurity|"
                  r"swissbit|excelsecu|hypersecu|onespan|nitrokey|solokey|token2|idem key|titan|cryptnox|vinkey|authentrend|"
                  r"kensington|hid crescendo|atos|smartdisplayer|ledger|trustkey|vivokey|pone|winmagic|wiSECURE", re.I)
ROLE = re.compile(r"(?i)\b(contributor|reader|administrator|operator|owner|user access|data access|role|approver|"
                  r"manager|writer|viewer|developer|auditor|analyst)\b")
SKU = re.compile(r"(?i)\b(plan [0-9a-z]|plan$|e[1-5]\b|a[1-5]\b|f[1-3]\b|g[1-5]\b|premium|standard|basic|add-?on|units?|licen[cs]e|"
                 r"trial|edu\b|faculty|student|for government|gcc\b|sku|subscription|capacity|per user|calling|minutes|"
                 r"conferencing|tier \d|\(\d+ unit|without |with |p[12]\b)")


def classify(name):
    n = str(name or "")
    if re.search(r" - (Delegated|Application)$", n):
        return "graph permission"
    if n.startswith("Purview/"):
        return "purview type"
    if FIDO.search(n):
        return "fido2 key"
    if re.search(r"(?i)template|designated empty|sample|example|placeholder|dummy|default tenant|re-register|cluster$|"
                 r"remove users|purchaser|\bkey\b|fingerprint", n):
        return "other id" if not re.search(r"(?i)\bkey\b|fingerprint", n) else "fido2 key"
    if re.match(r"^[A-Za-z-]+(\.[A-Za-z-]+)+$", n):
        return "graph permission"   # resource-specific consent permissions carry no ' - Delegated' suffix
    if re.search(r"_\d+$|vtrial|\bstorage\b|extra file|advanced compliance|sandbox", n, re.I):
        return "licence"
    if n.isupper() or SKU.search(n):
        return "licence"
    if ROLE.search(n):
        return "role"
    return "app"


def get(path):
    req = urllib.request.Request(RAW + path, headers={"User-Agent": "MS_SOC fpa_sources"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read()


def parse(key, raw):
    txt = raw.decode("utf-8-sig")
    if key == "kg":
        txt = "\n".join(l for l in txt.splitlines() if not l.lstrip().startswith("//"))
    return json.loads(txt)


def main():
    os.makedirs(CACHE, exist_ok=True)
    ip = os.path.join(CACHE, "index.json")
    try:
        index = json.load(open(ip, encoding="utf-8"))
    except Exception:
        index = {}
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    data = {}
    for k, path in SRC.items():
        rec = index.get(k) or {}
        try:
            raw = get(path)
            obj = parse(k, raw)
            if not obj:
                raise ValueError("empty")
            sha = hashlib.sha256(raw).hexdigest()
            if sha != rec.get("sha256"):
                open(os.path.join(CACHE, k + ".json"), "wb").write(raw)
                rec.update(sha256=sha, bytes=len(raw), changed=now)
            rec.update(url=RAW + path, fetched=now, ok=True, note="")
            data[k] = obj
        except Exception as e:
            rec.update(url=RAW + path, ok=False, note="not answered at %s: %s" % (now, str(e)[:120]))
            try:
                data[k] = parse(k, open(os.path.join(CACHE, k + ".json"), "rb").read())
            except Exception:
                data[k] = None
        index[k] = rec
    index = {k: v for k, v in index.items() if k in SRC}
    json.dump(index, open(ip, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # Microsoft's docs list, split into what it is
    kg = data.get("kg") or {}
    cls, apps = {}, []
    for name, gid in (kg.items() if isinstance(kg, dict) else []):
        g = str(gid or "").lower()
        if not re.match(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", g) or len(set(g.replace("-", ""))) < 3:
            c = "other id"
        else:
            c = classify(name)
        cls[c] = cls.get(c, 0) + 1
        if c == "app":
            apps.append([g, re.sub(r"(?i)\s*\b(app(lication)? id|client id)\b\s*$", "", str(name)).strip()])
    mer = data.get("merill") or []
    mids = {}
    for x in mer if isinstance(mer, list) else []:
        a = str(x.get("AppId") or "").lower()
        if a:
            mids.setdefault(a, set()).add(str(x.get("Source") or "?"))
    kgc = {str(v).lower(): classify(k) for k, v in (kg.items() if isinstance(kg, dict) else [])}
    mer_cls = {}
    for a, ss in mids.items():
        c = "app" if ss - {"EntraDocs"} else kgc.get(a, "app")
        mer_cls[c] = mer_cls.get(c, 0) + 1
    out = {"built": now[:10], "source": RAW + SRC["kg"], "fetched": (index.get("kg") or {}).get("fetched"),
           "knownGuids": sum(cls.values()), "byClass": cls, "apps": sorted(apps, key=lambda x: x[1].lower()),
           "merill": {"rows": len(mids), "byClass": mer_cls},
           "rule": "Only entries that are applications: Graph permission ids (' - Delegated' / ' - Application'), licence SKUs, "
                   "Azure and Entra roles, FIDO2 key AAGUIDs, Purview sensitive information types and template/sample ids are left out "
                   "(tools/fpa_sources.py classify())."}
    json.dump(out, open(os.path.join(ROOT, "site", "data", "fpa-docs.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print("fpa_sources: %s; known-guids %d -> %s; Merill %d rows -> %s"
          % (", ".join("%s %s" % (k, "ok" if v.get("ok") else "CACHED") for k, v in index.items()),
             out["knownGuids"], cls, len(mids), mer_cls))


if __name__ == "__main__":
    main()
