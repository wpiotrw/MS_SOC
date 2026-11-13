#!/usr/bin/env python3
"""MS_SOC - Microsoft 365 Service health with incident numbers (CLAUDE.md 5gr-e, 13 XI 2026). Author: Piotr Wisniewski.

The public status feed (status.cloud.microsoft) names no incident number. Service health of a tenant does
(MO1550821, EX1550543...), with service, feature, classification, start and the full history of updates. This script
signs in to our developer tenant as the app "MS-SOC Dev tenant reader" with the federated credential of GitHub Actions
(no secret; permission ServiceHealth.Read.All, application) and reads GET /admin/serviceAnnouncement/issues.

The repository and the page are public, so it keeps ONLY issues with origin "microsoft" (issues Microsoft publishes to
every tenant). Issues of origin customer / thirdParty, details (keyValuePair) and anything tenant-specific are dropped.
Kept: unresolved issues, and issues changed in the last 3 days. Posts: the newest 12, text only.

Writes one JSON file (path in argv[1]). A failed sign-in or read writes {"ok": false, "error": ...} so the page can
say the source is unavailable instead of showing nothing.
"""
import datetime
import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

KEEP_DAYS = 3
POSTS = 12
G = "https://graph.microsoft.com/v1.0/admin/serviceAnnouncement/issues"


def text(h):
    """HTML of a post -> plain lines (one line per paragraph / list item / <br>)"""
    s = re.sub(r"<\s*(br|/p|/div|/li|li|p|div)[^>]*>", "\n", h or "", flags=re.I)
    s = html.unescape(re.sub(r"<[^>]+>", " ", s))
    out = []
    for ln in s.split("\n"):
        ln = re.sub(r"[ \t ]+", " ", ln).strip()
        if ln:
            out.append(ln[:2000])
    return out[:80]


def slim(i):
    posts = sorted(i.get("posts") or [], key=lambda p: p.get("createdDateTime") or "", reverse=True)[:POSTS]
    return {
        "id": i.get("id"),
        "title": i.get("title"),
        "service": i.get("service"),
        "feature": i.get("feature"),
        "featureGroup": i.get("featureGroup"),
        "classification": i.get("classification"),
        "status": i.get("status"),
        "isResolved": bool(i.get("isResolved")),
        "start": i.get("startDateTime"),
        "end": i.get("endDateTime"),
        "modified": i.get("lastModifiedDateTime"),
        "impact": (i.get("impactDescription") or "")[:2000],
        "posts": [{"at": p.get("createdDateTime"), "type": p.get("postType"),
                   "lines": text(((p.get("description") or {}).get("content")) or "")} for p in posts],
        "postCount": len(i.get("posts") or []),
    }


def keep(i, since):
    if (i.get("origin") or "").lower() != "microsoft":
        return False
    if not i.get("isResolved"):
        return True
    return (i.get("lastModifiedDateTime") or "") >= since


def main(out):
    now = datetime.datetime.now(datetime.timezone.utc)
    since = (now - datetime.timedelta(days=KEEP_DAYS)).strftime("%Y-%m-%dT%H:%M:%SZ")
    res = {"generated": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "source": "Microsoft 365 Service health (Microsoft Graph)",
           "keepDays": KEEP_DAYS}
    try:
        import fpa_tenant as T
        tok = T.token()[1]
        raw = []
        url = G + "?$top=100&$filter=" + urllib.parse.quote("lastModifiedDateTime ge " + since + " or isResolved eq false")
        try:
            raw = T.pages(tok, url)
        except urllib.error.HTTPError as e:
            if e.code != 400:
                raise
            raw = T.pages(tok, G + "?$top=100")       # the filter is not accepted: read everything, filter here
        kept = [slim(i) for i in raw if keep(i, since)]
        kept.sort(key=lambda x: x["modified"] or "", reverse=True)
        kept.sort(key=lambda x: (x["isResolved"], x["classification"] != "incident"))
        res.update(ok=True, read=len(raw), issues=kept)
    except urllib.error.HTTPError as e:
        res.update(ok=False, error="HTTP %d%s" % (e.code, " - the app needs ServiceHealth.Read.All" if e.code == 403 else ""))
    except Exception as e:  # noqa: BLE001 - the page must learn the source failed
        res.update(ok=False, error=str(e)[:200])
    with open(out, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, separators=(",", ":"))
    print("ms_health: ok=%s issues=%s %s" % (res.get("ok"), len(res.get("issues") or []), res.get("error", "")))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "ms-health.json")
