#!/usr/bin/env python3
"""api_surfaces.py - every Microsoft API an app registration can be granted permissions on, counted from OUR tenant
(CLAUDE.md 5dr, README.md 5.2). Runs in .github/workflows/fpa-tenant.yml every three hours, read-only.

Owner, 14 X 2026: "where is the section that shows all permissions per API - Microsoft Graph has xyz application
and abc delegated permissions - and are we sure we show every resource?". Until now the table "APIs an app
registration can be granted permissions on" carried 16 rows whose numbers the morning run copied from Microsoft's
documentation by hand: measured that day, 11 of the 16 rows had a total but 0 delegated and 0 application
permissions (Azure DevOps 86 / 0 / 0, Power Platform API 51 / 0 / 0) - counts that cannot both be true.

The tenant knows the real answer. Every Microsoft API is a service principal in it, and the service principal
carries what an app can request: appRoles (application permissions) and oauth2PermissionScopes (delegated):

  GET /servicePrincipals?$top=999&$select=appId,displayName,appOwnerOrganizationId,appRoles,
      oauth2PermissionScopes,resourceSpecificApplicationPermissions
      -> Application.Read.All (already granted to the reader app for fpa_tenant.py; nothing new to consent)

Kept: service principals owned by Microsoft (the same tenant ids as fpa_tenant.py) that expose at least one
permission. Per API: application, delegated, both (one name offered as both), RSC, total distinct names, delegated
that need admin consent, and the names themselves (so the page can list them). Changes between two reads go to
`changes` (90 days): an API that appeared or disappeared, a permission name added or removed.

A read with fewer than 50 Microsoft APIs is treated as broken and not written. Writes only when something changed.
Everything written is Microsoft's public metadata of its own APIs - no tenant id, user, app or grant of ours."""
import datetime, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fpa_tenant as T

KEEP_DAYS = 90
MIN_APIS = 50
SELECT = "appId,displayName,appOwnerOrganizationId,appRoles,oauth2PermissionScopes,resourceSpecificApplicationPermissions"


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def load(path, default):
    try:
        return json.load(open(path, encoding="utf-8"))
    except Exception:
        return default


def surface(sp):
    """counts and names of one service principal; None when it exposes nothing"""
    app = sorted({r.get("value") for r in sp.get("appRoles") or []
                  if r.get("value") and r.get("isEnabled", True) and "Application" in (r.get("allowedMemberTypes") or [])})
    scopes = [s for s in sp.get("oauth2PermissionScopes") or [] if s.get("value") and s.get("isEnabled", True)]
    dele = sorted({s["value"] for s in scopes})
    admin = sorted({s["value"] for s in scopes if (s.get("type") or "").lower() == "admin"})
    rsc = sorted({r.get("value") for r in sp.get("resourceSpecificApplicationPermissions") or [] if r.get("value") and r.get("isEnabled", True)})
    if not (app or dele or rsc):
        return None
    names = set(app) | set(dele) | set(rsc)
    return {"name": (sp.get("displayName") or "").strip(), "appId": sp.get("appId"),
            "application": len(app), "delegated": len(dele), "both": len(set(app) & set(dele)), "rsc": len(rsc),
            "total": len(names), "adminDelegated": len(admin),
            "names": {"application": app, "delegated": dele, "rsc": rsc, "admin": admin}}


def diff(prev, cur, seen):
    out, day = [], seen[:10]
    p = {a["appId"]: a for a in prev}
    c = {a["appId"]: a for a in cur}
    for k in sorted(set(c) - set(p)):
        out.append({"seen": seen, "day": day, "api": c[k]["name"], "appId": k, "change": "api-added", "total": c[k]["total"]})
    for k in sorted(set(p) - set(c)):
        out.append({"seen": seen, "day": day, "api": p[k]["name"], "appId": k, "change": "api-removed", "total": p[k]["total"]})
    for k in sorted(set(p) & set(c)):
        for t in ("application", "delegated", "rsc"):
            a, b = set(p[k]["names"].get(t) or []), set(c[k]["names"].get(t) or [])
            for n in sorted(b - a):
                out.append({"seen": seen, "day": day, "api": c[k]["name"], "appId": k, "change": "added", "type": t, "permission": n})
            for n in sorted(a - b):
                out.append({"seen": seen, "day": day, "api": c[k]["name"], "appId": k, "change": "removed", "type": t, "permission": n})
    return out


def main(path="site/data/api-surfaces.json"):
    tid, tok = T.token()
    G = "https://graph.microsoft.com/v1.0"
    seen = now()
    prev = load(path, {})
    sps = T.pages(tok, G + "/servicePrincipals?$top=999&$select=" + SELECT)
    apis = []
    for sp in sps:
        if (sp.get("appOwnerOrganizationId") or "").lower() not in T.MS:
            continue
        s = surface(sp)
        if s:
            apis.append(s)
    apis.sort(key=lambda a: (-a["total"], a["name"].lower()))
    if len(apis) < MIN_APIS:
        print("api_surfaces: only %d Microsoft APIs read - looks broken, nothing written" % len(apis))
        return 1
    events = diff(prev.get("apis") or [], apis, seen) if prev.get("apis") else []
    cut = (datetime.date.fromisoformat(seen[:10]) - datetime.timedelta(days=KEEP_DAYS)).isoformat()
    changes = events + [x for x in prev.get("changes") or [] if (x.get("day") or "") >= cut]
    state = {"read": seen, "source": "Service principals owned by Microsoft in this tenant (v1.0), via .github/workflows/fpa-tenant.yml",
             "baseline": prev.get("baseline") or seen, "spRead": len(sps), "count": len(apis),
             "totals": {k: sum(a[k] for a in apis) for k in ("application", "delegated", "rsc", "total")},
             "apis": apis, "changes": changes}
    same = prev.get("apis") == apis and prev.get("changes") == changes
    if not same:
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        json.dump(state, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    if os.environ.get("GITHUB_OUTPUT"):
        open(os.environ["GITHUB_OUTPUT"], "a").write("events=%d\n" % len(events))
    print("api_surfaces: %d service principals read, %d Microsoft APIs expose permissions (%d application, %d delegated, %d RSC names); %s; %d changes%s"
          % (len(sps), len(apis), state["totals"]["application"], state["totals"]["delegated"], state["totals"]["rsc"],
             "baseline" if not prev.get("apis") else "compared with " + str(prev.get("read")), len(events), "" if not same else " (file unchanged)"))
    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:2]))
