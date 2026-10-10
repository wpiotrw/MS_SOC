#!/usr/bin/env python3
"""graph_sp.py - Microsoft's Graph permissions and Entra role definitions read from OUR tenant every
three hours, with a history of what changed (CLAUDE.md 5cy, README.md 5.2).

Owner, 10 X 2026, after Daniel Bradley's post on the new CopilotCostManagement permissions (first seen
9 X): "it is crucial to monitor not only campaigns but roles, Graph API, first-party apps and all of
those changes". Until now the brief learned of a new grantable permission from Merill's daily dump of
the Graph service principal (one export a day, in the evening) - the five Copilot permissions reached
the brief the next morning. This script reads the same object in our tenant, in the same workflow and
with the same read-only sign-in as fpa_tenant.py:

  GET /servicePrincipals(appId='00000003-0000-0000-c000-000000000000')
      ?$select=appRoles,oauth2PermissionScopes,resourceSpecificApplicationPermissions
      -> Application.Read.All (Microsoft: "To read information about all Microsoft Graph permissions
         programmatically ... at least the Application.Read.All permission", permissions reference)
  GET /roleManagement/directory/roleDefinitions?$filter=isBuiltIn eq true
      -> RoleManagement.Read.Directory (read-only). Without it Graph answers 403; the script records
         `rolesNote` and goes on - the permissions part never depends on the roles part.

Writes
  site/data/graph-sp.json          the current state: every permission name with its application role,
                                   delegated scope and RSC permission (id, enabled, consent type, Microsoft's
                                   own admin-consent text), and every built-in role (template id, actions,
                                   privileged flag) when the roles read was allowed
  site/data/graph-sp-history.json  what changed between two reads, newest first, 90 days:
                                   {seen (UTC, minutes), day, surface: permission|role, name, change, type,
                                    before, after, text}
                                   change: added | removed | type-added | type-removed | consent | enabled |
                                           text | actions-added | actions-removed | privileged
A read that looks broken (fewer than 500 application roles, or a role list under 80) is not written:
the previous state stays and the history gets no false "removed". The first read is a baseline and
writes no events. Microsoft deploys in rings, so "added" means "grantable in this tenant from now",
not "new worldwide" (CLAUDE.md, "Service principal w tenancie to replika").

Prints counts only. Everything written is Microsoft's public metadata of its own API; nothing about the
tenant's users, apps or grants (the tenant id is not written at all)."""
import datetime, json, os, sys, urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fpa_tenant as T

GRAPH_APP = "00000003-0000-0000-c000-000000000000"
KEEP_DAYS = 90


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def load(path, default):
    try:
        return json.load(open(path, encoding="utf-8"))
    except Exception:
        return default


def perm_state(sp):
    """{name: {"Application": {...}, "Delegated": {...}, "RSC": {...}}}"""
    out = {}
    for r in sp.get("appRoles") or []:
        n = r.get("value")
        if n:
            out.setdefault(n, {})["Application"] = {"id": r.get("id"), "enabled": bool(r.get("isEnabled", True)),
                                                   "text": (r.get("description") or "").strip(),
                                                   "title": (r.get("displayName") or "").strip()}
    for s in sp.get("oauth2PermissionScopes") or []:
        n = s.get("value")
        if n:
            out.setdefault(n, {})["Delegated"] = {"id": s.get("id"), "enabled": bool(s.get("isEnabled", True)),
                                                 "consent": s.get("type") or "",   # Admin | User
                                                 "text": (s.get("adminConsentDescription") or "").strip(),
                                                 "title": (s.get("adminConsentDisplayName") or "").strip()}
    for s in sp.get("resourceSpecificApplicationPermissions") or []:
        n = s.get("value")
        if n:
            out.setdefault(n, {})["RSC"] = {"id": s.get("id"), "enabled": bool(s.get("isEnabled", True)),
                                           "text": (s.get("description") or "").strip(),
                                           "title": (s.get("displayName") or "").strip()}
    return out


def role_state(defs):
    out = {}
    for d in defs:
        n = d.get("displayName")
        if not n:
            continue
        acts = sorted({a for rp in d.get("rolePermissions") or [] for a in rp.get("allowedResourceActions") or []})
        out[n] = {"id": d.get("templateId") or d.get("id"), "privileged": d.get("isPrivileged"),
                  "enabled": d.get("isEnabled", True), "text": (d.get("description") or "").strip(), "actions": acts}
    return out


def diff_perms(old, new, seen):
    ev, day = [], seen[:10]
    def e(name, change, typ="", before=None, after=None, text=""):
        ev.append({"seen": seen, "day": day, "surface": "permission", "name": name, "change": change, "type": typ,
                   "before": before, "after": after, "text": text[:400]})
    for n in sorted(set(old) | set(new)):
        a, b = old.get(n), new.get(n)
        if a is None:
            types = sorted(b)
            first = b.get("Application") or b.get("Delegated") or b.get("RSC") or {}
            e(n, "added", "+".join(types), None, ", ".join(types)
              + (" (consent: %s)" % b["Delegated"]["consent"] if "Delegated" in b and b["Delegated"].get("consent") else ""),
              first.get("text", ""))
            continue
        if b is None:
            e(n, "removed", "+".join(sorted(a)), ", ".join(sorted(a)), None)
            continue
        for t in sorted(set(a) | set(b)):
            x, y = a.get(t), b.get(t)
            if x is None:
                e(n, "type-added", t, None, t + (" (consent: %s)" % y.get("consent") if y.get("consent") else ""), y.get("text", ""))
            elif y is None:
                e(n, "type-removed", t, t, None)
            else:
                if (x.get("consent") or "") != (y.get("consent") or ""):
                    e(n, "consent", t, x.get("consent"), y.get("consent"))
                if x.get("enabled") != y.get("enabled"):
                    e(n, "enabled", t, x.get("enabled"), y.get("enabled"))
                if x.get("text") != y.get("text") and x.get("text") and y.get("text"):
                    e(n, "text", t, x.get("text")[:400], y.get("text")[:400])
    return ev


def diff_roles(old, new, seen):
    ev, day = [], seen[:10]
    def e(name, change, before=None, after=None, text=""):
        ev.append({"seen": seen, "day": day, "surface": "role", "name": name, "change": change, "type": "",
                   "before": before, "after": after, "text": text[:400]})
    for n in sorted(set(old) | set(new)):
        a, b = old.get(n), new.get(n)
        if a is None:
            e(n, "added", None, "%d actions" % len(b["actions"]) + (", privileged" if b.get("privileged") else ""), b.get("text", ""))
            continue
        if b is None:
            e(n, "removed", "%d actions" % len(a["actions"]), None)
            continue
        plus, minus = sorted(set(b["actions"]) - set(a["actions"])), sorted(set(a["actions"]) - set(b["actions"]))
        if plus:
            e(n, "actions-added", None, ", ".join(plus[:40]) + (" (+%d more)" % (len(plus) - 40) if len(plus) > 40 else ""))
        if minus:
            e(n, "actions-removed", ", ".join(minus[:40]) + (" (+%d more)" % (len(minus) - 40) if len(minus) > 40 else ""), None)
        # None = not read (v1.0 before 10 X 2026): the first read with the flag is not a change
        if a.get("privileged") is not None and b.get("privileged") is not None and a.get("privileged") != b.get("privileged"):
            e(n, "privileged", a.get("privileged"), b.get("privileged"))
    return ev


def main(state_path="site/data/graph-sp.json", hist_path="site/data/graph-sp-history.json"):
    tid, tok = T.token()
    G = "https://graph.microsoft.com/v1.0"
    seen = now()
    prev = load(state_path, {})
    hist = load(hist_path, {"events": []})
    sp = T.http(G + "/servicePrincipals(appId='%s')?$select=appRoles,oauth2PermissionScopes,resourceSpecificApplicationPermissions" % GRAPH_APP,
                headers={"Authorization": "Bearer " + tok})
    perms = perm_state(sp)
    n_app = sum(1 for v in perms.values() if "Application" in v)
    n_del = sum(1 for v in perms.values() if "Delegated" in v)
    n_rsc = sum(1 for v in perms.values() if "RSC" in v)
    if n_app < 500:
        print("graph_sp: only %d application roles read - looks broken, nothing written" % n_app)
        return 1
    roles, roles_note = None, None
    try:
        # beta: v1.0 does not return isPrivileged (measured 10 X 2026 - all 145 roles came back without it)
        defs = T.pages(tok, "https://graph.microsoft.com/beta/roleManagement/directory/roleDefinitions?$filter=isBuiltIn%20eq%20true")
        roles = role_state(defs)
        if len(roles) < 80:
            roles_note = "only %d built-in roles read - looks broken, the previous role list is kept" % len(roles)
            roles = None
    except urllib.error.HTTPError as ex:
        roles_note = ("GET /roleManagement/directory/roleDefinitions refused (%s) - the app needs RoleManagement.Read.Directory "
                      "(read-only, admin consent; README 5.2)" % ex.code)
    events = []
    if prev.get("perms"):
        events += diff_perms(prev["perms"], perms, seen)
    if roles is not None and prev.get("roles"):
        events += diff_roles(prev["roles"], roles, seen)
    state = {"read": seen, "source": "Microsoft Graph service principal of this tenant (v1.0), via .github/workflows/fpa-tenant.yml",
             "counts": {"names": len(perms), "application": n_app, "delegated": n_del, "rsc": n_rsc,
                        "roles": len(roles) if roles is not None else (len(prev.get("roles") or {}) or None)},
             "rolesRead": seen if roles is not None else prev.get("rolesRead"), "rolesNote": roles_note,
             "perms": perms, "roles": roles if roles is not None else prev.get("roles")}
    cut = (datetime.date.fromisoformat(seen[:10]) - datetime.timedelta(days=KEEP_DAYS)).isoformat()
    old_ev = [x for x in hist.get("events") or [] if (x.get("day") or "") >= cut]
    hist = {"updated": seen, "baseline": hist.get("baseline") or (seen if not prev.get("perms") else prev.get("read")),
            "lastRead": seen, "rolesNote": roles_note, "keepDays": KEEP_DAYS,
            "counts": state["counts"], "events": events + old_ev}
    os.makedirs(os.path.dirname(state_path) or ".", exist_ok=True)
    # written only when something changed, so the repository does not take a 0.5 MB commit every three hours;
    # the history file carries the day of the last read (once a day) so the page can say when we last looked
    same = prev.get("perms") == state["perms"] and prev.get("roles") == state["roles"] and prev.get("rolesNote") == roles_note
    if not same:
        json.dump(state, open(state_path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    if events or not os.path.exists(hist_path) or str(load(hist_path, {}).get("lastRead") or "")[:10] != seen[:10] \
            or load(hist_path, {}).get("rolesNote") != roles_note:
        json.dump(hist, open(hist_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if os.environ.get("GITHUB_OUTPUT"):
        open(os.environ["GITHUB_OUTPUT"], "a").write("events=%d\n" % len(events))
    by = {}
    for x in events:
        by[x["surface"] + " " + x["change"]] = by.get(x["surface"] + " " + x["change"], 0) + 1
    print("graph_sp: %d names (%d application, %d delegated, %d RSC), roles %s; %s; %d new events %s"
          % (len(perms), n_app, n_del, n_rsc, len(roles) if roles is not None else "not read",
             "baseline" if not prev.get("perms") else "compared with " + str(prev.get("read")), len(events), by))
    if roles_note:
        print("graph_sp: " + roles_note)
    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:3]))
