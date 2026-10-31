#!/usr/bin/env python3
"""radar_todo.py - the morning routine's helper for community notes on Graph radar findings (CLAUDE.md 5fy, 31 X 2026).

The owner, 31 X 2026: "you found the new Conditional Access parameter time - but no full example of use; the community
describes it (dpatyk.com, Medium). Look for examples in the community when the radar finds a new API or parameter - also
what values it takes. If the community can work it out without Learn, so can you - show it for the other findings too."

  python3 tools/radar_todo.py todo [--max 3] [--recheck 14]  -> findings that need a community search (JSON on stdout)
  python3 tools/radar_todo.py check                          -> validates site/data/graph-radar-notes.json, exit 1 on error

Two notes files, merged by tools/graph_radar.py (merged_notes): the note checked last wins, a person's note wins a tie,
the articles of both are kept.
  data/graph-radar/notes.json        - written by a person; the routine never edits it
  site/data/graph-radar-notes.json   - written by the morning routine (inside site/, the only folder a routine may touch)

`todo` lists, best first:
  new      - a finding with no note in either file (first seen most recently first);
  recheck  - a note whose basis is still "name" (nothing published) and that was checked more than --recheck days ago;
  values   - a note with articles but no values and no examples, checked more than --recheck days ago.
Each entry carries what the radar knows: type, property, path, the label of the endpoint, the shape our tenant
returned (sub-properties, kinds, safe values) and the current note's title - the search starts from the exact name.

`check` refuses (exit 1) a routine note the page could not render honestly: no title / what / checked, a basis outside
microsoft|article|name, basis article or microsoft with no article, an article without an https url or with a rel
outside names-it|feature|doc, an example without method / a graph.microsoft.com uri / tested / src, a value without
name / accepted, a key that is not type|property, or a GUID anywhere outside a URL (the repository is public: a
tenant id, an object id or an app id never goes into a note; examples use <placeholders>).
"""
import datetime as dt, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RADAR = os.path.join(ROOT, "site", "data", "graph-radar.json")
OWNER = os.path.join(ROOT, "data", "graph-radar", "notes.json")
ROUTINE = os.path.join(ROOT, "site", "data", "graph-radar-notes.json")
GUID = re.compile(r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b")
# well-known ids that are the same in every tenant may stay (role template ids, the Graph app, zero placeholders)
KNOWN = {"00000003-0000-0000-c000-000000000000", "00000000-0000-0000-0000-000000000000",
         "a0b1b346-4d3e-4e8b-98f8-753987be4970", "10dae51f-b6af-4016-8d66-8c2a99b929b3", "2af84b1e-32c8-42b7-82bc-daa82404023b"}
BASIS = {"microsoft", "article", "name"}
REL = {"names-it", "feature", "doc"}
METHODS = {"GET", "POST", "PATCH", "PUT", "DELETE"}


def load(p, d):
    try:
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return d


def days_since(d, today):
    try:
        return (today - dt.date.fromisoformat(str(d)[:10])).days
    except Exception:
        return 9999


def todo(mx=3, recheck=14):
    today = dt.date.today()
    R = load(RADAR, {})
    und = ((R.get("tenant") or {}).get("undocumented")) or []
    own = (load(OWNER, {}) or {}).get("notes") or {}
    rt = (load(ROUTINE, {}) or {}).get("notes") or {}
    out = []
    for u in und:
        leaf = u.get("leaf") or str(u.get("prop", "")).split(".")[-1].replace("[]", "")
        key = u["type"] + "|" + leaf
        n = rt.get(key) if (rt.get(key) or {}).get("checked", "") > (own.get(key) or {}).get("checked", "") else own.get(key) or rt.get(key)
        why = None
        if not n:
            why = "new"
        elif n.get("basis") == "name" and days_since(n.get("checked"), today) > recheck:
            why = "recheck"
        elif not n.get("values") and not n.get("examples") and n.get("articles") and days_since(n.get("checked"), today) > recheck:
            why = "values"
        if not why:
            continue
        out.append({"why": why, "key": key, "type": u["type"], "property": u.get("prop"), "path": u.get("path"),
                    "endpoint": u.get("label"), "status": u.get("status"), "first": u.get("first"),
                    "shape": u.get("shape"), "noteTitle": (n or {}).get("title"), "noteChecked": (n or {}).get("checked"),
                    "inOwnerNotes": key in own})
    order = {"new": 0, "recheck": 1, "values": 2}
    out.sort(key=lambda x: (order[x["why"]], "" if x["why"] != "new" else "~" + str(x.get("first") or "")), reverse=False)
    news = sorted([x for x in out if x["why"] == "new"], key=lambda x: str(x.get("first") or ""), reverse=True)
    rest = [x for x in out if x["why"] != "new"]
    picked = (news + rest)[:mx]
    print(json.dumps({"day": today.isoformat(), "todo": picked, "left": max(0, len(out) - len(picked)),
                      "file": "site/data/graph-radar-notes.json"}, indent=1, ensure_ascii=False))
    return 0


def guids_outside_urls(o, path=""):
    bad = []
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ("url", "u"):
                continue
            bad += guids_outside_urls(v, path + "." + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            bad += guids_outside_urls(v, path + "[%d]" % i)
    elif isinstance(o, str):
        for g in GUID.findall(o):
            if g.lower() not in KNOWN:
                bad.append(path + ": " + g)
    return bad


def check():
    if not os.path.exists(ROUTINE):
        print("OK - no routine notes yet (%s)" % ROUTINE)
        return 0
    d = load(ROUTINE, None)
    if not isinstance(d, dict) or not isinstance(d.get("notes"), dict):
        print("BRAK - %s is not {\"notes\": {...}}" % ROUTINE)
        return 1
    err = []
    for key, n in d["notes"].items():
        if not re.match(r"^[A-Za-z0-9]+\|[A-Za-z0-9]+$", key):
            err.append("%s: key must be type|property" % key)
        for f in ("title", "what", "checked", "basis"):
            if not n.get(f):
                err.append("%s: no %s" % (key, f))
        if n.get("basis") and n["basis"] not in BASIS:
            err.append("%s: basis %r" % (key, n["basis"]))
        if not isinstance(n.get("uses", []), list):
            err.append("%s: uses must be a list" % key)
        arts = n.get("articles") or []
        if n.get("basis") in ("article", "microsoft") and not arts:
            err.append("%s: basis %s with no article" % (key, n.get("basis")))
        for a in arts:
            if not str(a.get("url", "")).startswith("https://"):
                err.append("%s: article without an https url: %s" % (key, a.get("title")))
            if a.get("rel") not in REL:
                err.append("%s: article rel %r" % (key, a.get("rel")))
            if not a.get("title"):
                err.append("%s: article without a title" % key)
        for v in n.get("values") or []:
            if not v.get("name") or not v.get("accepted"):
                err.append("%s: a value without name/accepted" % key)
        for x in n.get("examples") or []:
            if x.get("method") not in METHODS:
                err.append("%s: example method %r" % (key, x.get("method")))
            if not str(x.get("uri", "")).startswith("https://graph.microsoft.com/"):
                err.append("%s: example uri must start with https://graph.microsoft.com/" % key)
            if not x.get("tested") or not x.get("src") or not x.get("title"):
                err.append("%s: example needs title, tested and src" % key)
            if x.get("method") in ("POST", "PATCH", "PUT") and not isinstance(x.get("body"), dict):
                err.append("%s: a %s example needs a JSON object body" % (key, x.get("method")))
        err += ["%s: a GUID outside a URL (%s) - use a <placeholder>" % (key, b) for b in guids_outside_urls(n)]
    if err:
        print("BRAK - %d problem(s):" % len(err))
        print("\n".join("  " + e for e in err))
        return 1
    print("OK - %d routine note(s)" % len(d["notes"]))
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] not in ("todo", "check"):
        print(__doc__)
        sys.exit(2)
    if a[0] == "check":
        sys.exit(check())
    mx = int(a[a.index("--max") + 1]) if "--max" in a else 3
    rc = int(a[a.index("--recheck") + 1]) if "--recheck" in a else 14
    sys.exit(todo(mx, rc))
