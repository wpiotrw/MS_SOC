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


def roles_from_state(path):
    """5ef: the second tenant read by tools/graph_sp.py (graph-sp-dev.json) in the same shape as the msadminroles roles"""
    st = json.load(open(path, encoding="utf-8"))
    return {n: {"templateId": v.get("id"), "actions": sorted(v.get("actions") or []), "version": None, "since": None}
            for n, v in (st.get("roles") or {}).items()}, st


def main(ours_path="site/data/graph-sp.json", out_path="site/data/roles-elsewhere.json", there_state=None, label=None):
    now = datetime.datetime.now(datetime.timezone.utc)
    day = now.date().isoformat()
    prev = {}
    try:
        prev = json.load(open(out_path, encoding="utf-8"))
    except Exception:
        pass
    there_st = None
    try:
        if there_state:
            there, there_st = roles_from_state(there_state)
        else:
            there = roles_from(fetch())
    except Exception as e:
        print("roles_elsewhere: skipped - %s" % e)
        return 0
    # 5ej: a source that lists only Graph permissions (merill/microsoft-info) has no roles to compare
    if len(there) < 80 and not (there_st and len(there_st.get("perms") or {}) >= 80):
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
    # 5ef: with a second tenant of ours, also its Graph permissions and its catalog of directory actions that ours lacks
    extra = {}
    if there_st:
        ours_p, ours_a = set(ours_state.get("perms") or {}), set(ours_state.get("actions") or {})
        tp, ta = there_st.get("perms") or {}, there_st.get("actions") or {}
        pfirst = {k: v for k, v in (prev.get("permsFirst") or {}).items() if k in tp and k not in ours_p}
        afirst = {k: v for k, v in (prev.get("actionsFirst") or {}).items() if k in ta and k not in ours_a}
        newp = [k for k in sorted(set(tp) - ours_p) if k not in pfirst]
        newa = [k for k in sorted(set(ta) - ours_a) if k not in afirst] if ours_a else []
        for k in newp: pfirst[k] = day
        for k in newa: afirst[k] = day
        if newp and prev:
            events.append({"day": day, "name": "Graph permissions", "change": "perms-there-only", "actions": newp})
        if newa and prev:
            events.append({"day": day, "name": "Directory actions", "change": "actions-there-only", "actions": newa})
        extra = {"permsThereOnly": sorted(pfirst), "permsFirst": pfirst, "actionsThereOnly": sorted(afirst), "actionsFirst": afirst,
                 "permsText": {k: ((tp[k].get("Application") or tp[k].get("Delegated") or {}).get("text") or "")[:300] for k in pfirst},
                 "actionsText": {k: (ta[k].get("text") or "")[:300] for k in afirst}}
    cut = (now.date() - datetime.timedelta(days=KEEP)).isoformat()
    ev = events + [x for x in prev.get("events") or [] if (x.get("day") or "") >= cut]
    body = {"source": SRC if not there_state else ("our second tenant (tools/graph_sp.py)" if not label or "developer" in label else label),
            "sourceLabel": label or ("our developer tenant" if there_state else "msadminroles.com"),
            "sourceNote": "Daniel Bradley's msadminroles.com - built-in role definitions as his tenant reads them" if not there_state
            else ("built-in role definitions of our second (developer) tenant, read every 3 hours with the same app permissions"
                  if not label or "developer" in label else "public repository: " + label),
            "thereRead": (there_st or {}).get("rolesRead"),
            "ourRead": ours_state.get("rolesRead"), "keepDays": KEEP,
            "counts": {"rolesThere": len(there), "rolesDiffering": len(roles),
                       "thereOnly": sum(len(v["there"]) for v in roles.values()), "oursOnly": sum(len(v["ours"]) for v in roles.values())},
            "roles": roles, "events": ev}
    body.update(extra)
    # the times of the reads are not a change: without this the file (and a deploy) would follow every 3-hour run
    strip = lambda d: {k: v for k, v in d.items() if k not in ("read", "ourRead", "thereRead")}
    if strip(prev) == strip(body):
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
        a = sys.argv[1:]
        ts = a[a.index("--there-state") + 1] if "--there-state" in a else None
        lb = a[a.index("--label") + 1] if "--label" in a else None
        pos = [x for i, x in enumerate(a) if not x.startswith("--") and (i == 0 or a[i - 1] not in ("--there-state", "--label"))]
        sys.exit(main(*(pos[:2] or []), there_state=ts, label=lb))
    except Exception as e:
        print("roles_elsewhere: skipped - %s" % e)
