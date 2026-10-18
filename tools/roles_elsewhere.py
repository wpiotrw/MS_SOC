#!/usr/bin/env python3
"""roles_elsewhere.py - Entra built-in roles as ANOTHER tenant sees them, compared with ours (CLAUDE.md 5ed).

  python3 tools/roles_elsewhere.py [site/data/graph-sp.json] [site/data/roles-elsewhere.json]

Why (owner, 18 X 2026): Daniel Bradley wrote on 18 X about Conditional Access policy plans - three new directory
actions (microsoft.directory/conditionalAccessPolicyPlans/create, /delete, /basic/update) that his tracker
msadminroles.com shows on the Conditional Access Administrator role ("Recently changed: 16 Oct 2026"). The portal
had nothing: our tenant (tools/graph_sp.py, every 3 h) is a test tenant in a later deployment ring and still lists
the role without them; Microsoft's permissions reference on Learn does not mention them either. A role change reaches
tenants in rings, so one tenant is never the only source (the owner's rule for Message Center, same here).

What it does: reads the public page https://msadminroles.com/ (Daniel Bradley's independent reference; the page embeds
every built-in role definition as JSON - displayName, templateId, rolePermissions.allowedResourceActions), compares each
role's actions with OUR tenant's role in site/data/graph-sp.json, and writes site/data/roles-elsewhere.json:
  {read, source, ourRead, counts, roles: {name: {templateId, there: [actions only there], ours: [actions only in ours],
   firstNoticed: {action: day}}}, events: [{day, name, change: there-only|ours-only|caught-up, actions}], keepDays}
"there-only" = seen in the other tenant, not yet in ours (usually: rolling out, ours will follow; or preview).
"caught-up" = an action that was there-only and is now in our tenant too. Events are kept 90 days.
No credentials, no tenant data; exit 0 always (a missing comparison is a gap, never a failed workflow).
"""
import datetime, json, os, re, sys, urllib.request

SRC = "https://msadminroles.com/"
KEEP = 90


def fetch():
    req = urllib.request.Request(SRC, headers={"User-Agent": "Mozilla/5.0 (MS_SOC portal; github.com/wpiotrw/MS_SOC)"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read().decode("utf-8", "replace")


def roles_from(html):
    parts = re.findall(r'self\.__next_f\.push\(\[1,"((?:[^"\\]|\\.)*)"\]\)', html)
    txt = "".join(json.loads('"' + p + '"') for p in parts)
    out, dec = {}, json.JSONDecoder()
    for m in re.finditer(r'\{"id":"[0-9a-f-]{36}","(?:deletedDateTime|assignmentMode)"', txt):
        try:
            obj, _ = dec.raw_decode(txt, m.start())
        except Exception:
            continue
        n = obj.get("displayName")
        if not n or not obj.get("isBuiltIn", True):
            continue
        acts = sorted({a for rp in obj.get("rolePermissions") or [] for a in rp.get("allowedResourceActions") or []})
        if n not in out or len(acts) > len(out[n]["actions"]):
            out[n] = {"templateId": obj.get("templateId") or obj.get("id"), "actions": acts,
                      "version": obj.get("version"), "since": obj.get("dateCreated")}   # the tracker's version of the role and its day
    return out


def main(ours_path="site/data/graph-sp.json", out_path="site/data/roles-elsewhere.json"):
    now = datetime.datetime.now(datetime.timezone.utc)
    day = now.date().isoformat()
    prev = {}
    try:
        prev = json.load(open(out_path, encoding="utf-8"))
    except Exception:
        pass
    try:
        there = roles_from(fetch())
    except Exception as e:
        print("roles_elsewhere: skipped - %s" % e)
        return 0
    if len(there) < 80:
        print("roles_elsewhere: only %d roles parsed from %s - looks broken, nothing written" % (len(there), SRC))
        return 0
    ours_state = json.load(open(ours_path, encoding="utf-8"))
    ours = ours_state.get("roles") or {}
    by_tid = {v.get("id"): k for k, v in ours.items()}
    roles, events = {}, []
    prev_roles = prev.get("roles") or {}
    for n, t in sorted(there.items()):
        on = n if n in ours else by_tid.get(t["templateId"])
        if not on:
            continue
        a_there, a_ours = set(t["actions"]), set(ours[on].get("actions") or [])
        only_there, only_ours = sorted(a_there - a_ours), sorted(a_ours - a_there)
        p = prev_roles.get(on) or {}
        first = {a: d for a, d in (p.get("firstNoticed") or {}).items() if a in only_there}
        new = [a for a in only_there if a not in first]
        for a in new:
            first[a] = day
        caught = [a for a in (p.get("there") or []) if a not in only_there and a in a_ours]
        if new:
            events.append({"day": day, "name": on, "change": "there-only", "actions": new, "thereSince": t.get("since")})
        if caught:
            events.append({"day": day, "name": on, "change": "caught-up", "actions": caught})
        newo = [a for a in only_ours if a not in (p.get("ours") or [])]
        if newo and prev_roles:
            events.append({"day": day, "name": on, "change": "ours-only", "actions": newo})
        if only_there or only_ours:
            roles[on] = {"templateId": t["templateId"], "there": only_there, "ours": only_ours, "firstNoticed": first,
                         "thereVersion": t.get("version"), "thereSince": t.get("since")}
    cut = (now.date() - datetime.timedelta(days=KEEP)).isoformat()
    ev = events + [x for x in prev.get("events") or [] if (x.get("day") or "") >= cut]
    body = {"source": SRC, "sourceNote": "Daniel Bradley's msadminroles.com - built-in role definitions as his tenant reads them",
            "ourRead": ours_state.get("rolesRead"), "keepDays": KEEP,
            "counts": {"rolesThere": len(there), "rolesDiffering": len(roles),
                       "thereOnly": sum(len(v["there"]) for v in roles.values()), "oursOnly": sum(len(v["ours"]) for v in roles.values())},
            "roles": roles, "events": ev}
    old = {k: v for k, v in prev.items() if k != "read"}
    if old == body:
        print("roles_elsewhere: no change (%d roles there, %d differ)" % (len(there), len(roles)))
        return 0
    body = dict(read=now.strftime("%Y-%m-%dT%H:%MZ"), **body)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    json.dump(body, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("roles_elsewhere: changed - %d roles there, %d differ from ours, %d actions only there, %d only ours, %d new events"
          % (len(there), len(roles), body["counts"]["thereOnly"], body["counts"]["oursOnly"], len(events)))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(*sys.argv[1:3]))
    except Exception as e:
        print("roles_elsewhere: skipped - %s" % e)
