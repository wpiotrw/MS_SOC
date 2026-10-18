#!/usr/bin/env python3
"""public_trackers.py - two more "other tenants", read from public GitHub repositories (CLAUDE.md 5ej, 18 X 2026).

  python3 tools/public_trackers.py [site/data/graph-sp.json] [site/data]

Owner, 18 X 2026: "attach them, we will check". Research the same evening (claude/ms-soc-raw-sources-research-2026-10-18.md)
found two public, MIT-licensed repositories that read Microsoft Graph from THEIR OWN tenant on a schedule and commit the
raw result:
  rolelens  github.com/arusso-aboutcloud/Entra-Rolelens  data/roles_graph_raw.json  - every built-in Entra role definition
            (v1.0 roleManagement/directory/roleDefinitions), daily 01:00 UTC
  merill    github.com/merill/microsoft-info  _info/GraphAppRoles.json + GraphDelegateRoles.json - every Graph application
            permission and delegated scope of the Microsoft Graph service principal in Merill Fernando's tenant, 05:30 and
            17:30 UTC
Each is turned into the shape of site/data/graph-sp.json and compared with OUR tenant by tools/roles_elsewhere.py, exactly
like msadminroles.com and our developer tenant: site/data/roles-rolelens.json and site/data/roles-merill.json. The page
reads them with the other "elsewhere" files (identity ranking, "Last 3 days" in Graph API and Roles).
No credentials, no tenant data of ours; exit 0 always (a missing comparison is a gap, never a failed workflow).
"""
import json, os, sys, tempfile, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import roles_elsewhere  # noqa: E402

UA = {"User-Agent": "MS_SOC portal (github.com/wpiotrw/MS_SOC)"}
ROLELENS = "https://raw.githubusercontent.com/arusso-aboutcloud/Entra-Rolelens/master/data/roles_graph_raw.json"
MERILL_APP = "https://raw.githubusercontent.com/merill/microsoft-info/main/_info/GraphAppRoles.json"
MERILL_DEL = "https://raw.githubusercontent.com/merill/microsoft-info/main/_info/GraphDelegateRoles.json"


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return json.load(r)


def rolelens_state():
    raw = get(ROLELENS)
    roles = {}
    for r in raw if isinstance(raw, list) else raw.get("value", []):
        if not r.get("displayName") or r.get("isBuiltIn") is False:
            continue
        acts = sorted({a for rp in r.get("rolePermissions") or [] for a in rp.get("allowedResourceActions") or []})
        roles[r["displayName"]] = {"id": r.get("templateId") or r.get("id"), "actions": acts}
    return {"roles": roles, "perms": {}, "actions": {}, "rolesRead": None}


def merill_state():
    perms = {}
    for url, typ in ((MERILL_APP, "Application"), (MERILL_DEL, "Delegated")):
        for p in get(url):
            n = p.get("Value")
            if not n:
                continue
            text = p.get("Description") if typ == "Application" else (p.get("AdminConsentDescription") or p.get("UserConsentDescription") or "")
            perms.setdefault(n, {})[typ] = {"id": p.get("Id"), "text": text or "", "title": p.get("DisplayName") or p.get("AdminConsentDisplayName") or ""}
    return {"roles": {}, "perms": perms, "actions": {}, "rolesRead": None}


def one(name, build, label, ours, outdir):
    out = os.path.join(outdir, "roles-%s.json" % name)
    try:
        st = build()
    except Exception as e:
        print("public_trackers %s: skipped - %s" % (name, e)); return
    n = len(st["roles"]) or len(st["perms"])
    if n < 80:
        print("public_trackers %s: only %d records - looks broken, nothing written" % (name, n)); return
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(st, f); tmp = f.name
    try:
        roles_elsewhere.main(ours, out, there_state=tmp, label=label)
    finally:
        os.unlink(tmp)


def main(ours="site/data/graph-sp.json", outdir="site/data"):
    one("rolelens", rolelens_state, "Entra-Rolelens (another tenant, daily)", ours, outdir)
    one("merill", merill_state, "merill/microsoft-info (another tenant, twice a day)", ours, outdir)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(*sys.argv[1:3]))
    except Exception as e:
        print("public_trackers: skipped - %s" % e)
