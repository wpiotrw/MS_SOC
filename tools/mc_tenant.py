#!/usr/bin/env python3
"""mc_tenant.py - Message Center read from OUR tenant through Microsoft Graph (README.md 5.4).

Runs in GitHub Actions right after fpa_tenant.py (same workflow, same Entra app, same federated
credential - no secret). Needs the application permission ServiceMessage.Read.All,
admin-consented. Without it Graph answers 403: the file then records `note` and keeps the
previous messages, and the workflow does not fail (the tenant snapshot must not be lost because
of this one).

  GET /admin/serviceAnnouncement/messages   (all service update messages for the tenant)

Microsoft publishes Message Center per tenant: a tenant sees messages for the services it is
subscribed to. This is ONE source; the brief keeps comparing it with mc.merill.net, DeltaPulse
and msmessagecenter.com (CLAUDE.md 5an) - a message those know and this file does not is a
coverage gap of the tenant, not a message that does not exist.

Writes site/data/mc-tenant.json:
  {read, source, count, note, messages:[{id,title,services,category,severity,major,actionBy,
    start,end,modified,tags,summary,bodyHash}],
   changes:[{date,id,type:new|changed|removed,title,fields:{field:[before,after]}}]}   (last 30 days)

`summary` is the first ~400 characters of the message text; the full text stays in Microsoft's
admin center (link per message). `bodyHash` lets a body edit be reported as a change without
publishing the body.
Env: AZURE_TENANT_ID, AZURE_CLIENT_ID, ACTIONS_ID_TOKEN_REQUEST_URL/_TOKEN (set by GitHub)."""
import datetime, hashlib, html, json, os, re, sys, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fpa_tenant  # token() and pages(): the OIDC exchange lives in one place

FIELDS = ["title", "services", "category", "severity", "major", "actionBy", "start", "end", "tags", "bodyHash"]
KEEP_DAYS = 30


def text(body):
    t = re.sub(r"<[^>]+>", " ", body or "")
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def shape(m):
    body = ((m.get("body") or {}).get("content")) or ""
    plain = text(body)
    return {"id": m.get("id"), "title": m.get("title"),
            "services": sorted(m.get("services") or []), "category": m.get("category"),
            "severity": m.get("severity"), "major": bool(m.get("isMajorChange")),
            "actionBy": (m.get("actionRequiredByDateTime") or "")[:10] or None,
            "start": (m.get("startDateTime") or "")[:10] or None,
            "end": (m.get("endDateTime") or "")[:10] or None,
            "modified": (m.get("lastModifiedDateTime") or "")[:10] or None,
            "tags": sorted(m.get("tags") or []),
            "summary": plain[:400] + ("…" if len(plain) > 400 else ""),
            "bodyHash": hashlib.sha256(plain.encode("utf-8")).hexdigest()[:16]}


def diff(prev, cur, day):
    out = []
    pm = {m["id"]: m for m in prev}
    cm = {m["id"]: m for m in cur}
    for i, m in cm.items():
        if i not in pm:
            out.append({"date": day, "id": i, "type": "new", "title": m["title"], "fields": {}})
            continue
        f = {k: [pm[i].get(k), m.get(k)] for k in FIELDS if pm[i].get(k) != m.get(k)}
        if f:
            out.append({"date": day, "id": i, "type": "changed", "title": m["title"], "fields": f})
    for i, m in pm.items():
        if i not in cm:
            out.append({"date": day, "id": i, "type": "removed", "title": m["title"], "fields": {}})
    return out


def main(out_path):
    day = datetime.date.today().isoformat()
    old = {}
    if os.path.exists(out_path):
        try:
            old = json.load(open(out_path, encoding="utf-8"))
        except Exception:
            old = {}
    prev = old.get("messages") or []
    note = None
    try:
        tid, tok = fpa_tenant.token()
        raw = fpa_tenant.pages(tok, "https://graph.microsoft.com/v1.0/admin/serviceAnnouncement/messages?$top=1000")
        cur = sorted((shape(m) for m in raw), key=lambda m: m["id"] or "")
    except urllib.error.HTTPError as ex:
        cur = prev
        note = ("GET /admin/serviceAnnouncement/messages refused (%s) - ServiceMessage.Read.All not granted "
                "or not consented; previous messages kept" % ex.code)
    changes = diff(prev, cur, day) if (prev and not note) else []
    if not prev and not note:
        note = "baseline: first read, %d messages recorded; changes are reported from the next run" % len(cur)
    cutoff = (datetime.date.today() - datetime.timedelta(days=KEEP_DAYS)).isoformat()
    log = [c for c in (old.get("changes") or []) if c.get("date", "") >= cutoff] + changes
    out = {"read": day, "source": "Microsoft Graph /admin/serviceAnnouncement/messages (tenant of the owner)",
           "count": len(cur), "note": note, "messages": cur, "changes": log}
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    json.dump(out, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("OK %s: %d messages, %d changes today (%s), log %d%s"
          % (out_path, len(cur), len(changes),
             ", ".join("%s %d" % (t, sum(1 for c in changes if c["type"] == t)) for t in ("new", "changed", "removed")),
             len(log), (" - " + note) if note else ""))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "site/data/mc-tenant.json")
