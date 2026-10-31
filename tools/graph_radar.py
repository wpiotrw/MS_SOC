#!/usr/bin/env python3
"""graph_radar.py - what Microsoft adds to Microsoft Graph before (and after) it is documented (CLAUDE.md 5fs).

Owner, 30 X 2026: Jan Bakker wrote about allowPasswordChangeAfterSecureSignIn (PATCH .../authenticationMethodConfigurations/
Password, beta) on the day it appeared - "how did he find it? can our portal and scripts find such things, not only in
authentication methods but in every endpoint, and build the command for Graph Explorer or PowerShell?". Measured that
evening: the property was in neither the live beta $metadata nor microsoftgraph/msgraph-metadata (sync 28 X) - not even
its type passwordAuthenticationMethodConfiguration. It existed only in what the service RETURNS in a tenant.

Two readings, both read-only:
  1. $metadata of beta and v1.0 (public, every run): every entity, complex and enum type, property, navigation, action,
     function, entity set and singleton; compared with the previous run -> a change list (new / removed / type changed,
     "promoted to v1.0"). --backfill DIR: the same comparison between the weekly schema syncs of a clone of
     github.com/microsoftgraph/msgraph-metadata (schemas/{beta,v1.0}-Prod.csdl), so the history starts weeks back.
  2. our developer tenant (when the workflow gives a token - app "MS-SOC Dev tenant reader", federated credential): GET of
     tenant-wide configuration objects (policies, authentication methods, organization, sync features, Intune service
     settings). Only the NAMES of the properties the service returns are kept - never a value (the repository is
     public) - with the JSON kind (boolean, string, number, object, array) so a command can be written. A property the
     service returns that $metadata does not know is "undocumented"; that is how allowPasswordChangeAfterSecureSignIn
     shows up the day the rollout reaches the tenant. A 403 is recorded per endpoint, never fails the run.
Every change carries the path to call, the least-privileged permission from Microsoft's own permission file (the
portal's graphMap, newest site/data/<day>.json) and a GET / PATCH command for Graph Explorer and PowerShell, and the
Message Center posts whose words match the property's words.

Writes  site/data/graph-radar.json        (the portal: Graph API > Radar, Overview sentence, /diff, /week)
        data/graph-radar/meta-{beta,v1.0}.json.gz, tenant.json, history.json   (memory, not published)
Usage   python3 tools/graph_radar.py [--backfill DIR] [--day YYYY-MM-DD] [--no-tenant]
"""
import datetime, glob, gzip, json, os, re, subprocess, sys, urllib.error, urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site", "data")
MEM = os.path.join(ROOT, "data", "graph-radar")
OUT = os.path.join(SITE, "graph-radar.json")
META = {"beta": "https://graph.microsoft.com/beta/$metadata", "v1.0": "https://graph.microsoft.com/v1.0/$metadata"}
EDM = "{http://docs.oasis-open.org/odata/ns/edm}"
KEEP_DAYS = 60
UA = "Mozilla/5.0 (MS_SOC graph radar; +https://github.com/wpiotrw/MS_SOC)"

# tenant-wide configuration objects read with GET (beta). label, path, permission that opens it
PROBE = [
    ("Authentication methods policy", "/policies/authenticationMethodsPolicy", "Policy.Read.AuthenticationMethod"),
    ("Authentication method: Password", "/policies/authenticationMethodsPolicy/authenticationMethodConfigurations/Password", "Policy.Read.AuthenticationMethod"),
    ("Authorization policy", "/policies/authorizationPolicy", "Policy.Read.All"),
    ("Authentication flows policy", "/policies/authenticationFlowsPolicy", "Policy.Read.All"),
    ("Authentication strength policies", "/policies/authenticationStrengthPolicies", "Policy.Read.All"),
    ("Cross-tenant access policy", "/policies/crossTenantAccessPolicy", "Policy.Read.All"),
    ("Cross-tenant access: default", "/policies/crossTenantAccessPolicy/default", "Policy.Read.All"),
    ("Security defaults", "/policies/identitySecurityDefaultsEnforcementPolicy", "Policy.Read.All"),
    ("Device registration policy", "/policies/deviceRegistrationPolicy", "Policy.Read.All"),
    ("External identities policy", "/policies/externalIdentitiesPolicy", "Policy.Read.All"),
    ("Admin consent request policy", "/policies/adminConsentRequestPolicy", "Policy.Read.All"),
    ("Default app management policy", "/policies/defaultAppManagementPolicy", "Policy.Read.All"),
    ("Permission grant policies", "/policies/permissionGrantPolicies", "Policy.Read.PermissionGrant"),
    ("Token lifetime policies", "/policies/tokenLifetimePolicies", "Policy.Read.All"),
    ("Activity-based timeout policies", "/policies/activityBasedTimeoutPolicies", "Policy.Read.All"),
    # featureRolloutPolicies (staged rollout) is not read: Microsoft's permission file names Policy.Read.HybridAuthentication,
    # but Graph has no such application permission (30 X 2026, the grant script); the only application one is
    # Directory.ReadWrite.All - a write permission the radar does not take
    ("Conditional Access policies", "/identity/conditionalAccess/policies", "Policy.Read.All"),
    ("Conditional Access named locations", "/identity/conditionalAccess/namedLocations", "Policy.Read.All"),
    ("Conditional Access templates", "/identity/conditionalAccess/templates", "Policy.Read.All"),
    ("Organization", "/organization", "Organization.Read.All"),
    ("Directory sync features", "/directory/onPremisesSynchronization", "OnPremDirectorySynchronization.Read.All"),
    ("Intune: device management", "/deviceManagement", "DeviceManagementServiceConfig.Read.All"),
    ("Intune: enrollment configurations", "/deviceManagement/deviceEnrollmentConfigurations", "DeviceManagementServiceConfig.Read.All"),
    ("Intune: configuration policies (settings catalog)", "/deviceManagement/configurationPolicies", "DeviceManagementConfiguration.Read.All"),
]


def log(*a):
    print("graph_radar:", *a, flush=True)


def load(p, d):
    try:
        if p.endswith(".gz"):
            return json.load(gzip.open(p, "rt", encoding="utf-8"))
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return d


def save(p, obj, gz=False):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    txt = json.dumps(obj, ensure_ascii=False, separators=(",", ":"), sort_keys=gz)
    if gz:
        old = None
        try:
            old = gzip.open(p, "rt", encoding="utf-8").read()
        except Exception:
            pass
        if old != txt:
            with gzip.GzipFile(p, "wb", mtime=0) as f:
                f.write(txt.encode("utf-8"))
        return
    old = open(p, encoding="utf-8").read() if os.path.exists(p) else None
    def bare(t):
        try:
            o = json.loads(t); o.pop("generated", None); return json.dumps(o, sort_keys=True)
        except Exception:
            return t
    if old is None or bare(old) != bare(txt):
        open(p, "w", encoding="utf-8").write(txt)


def get(url, headers=None, timeout=120):
    h = {"User-Agent": UA}
    h.update(headers or {})
    with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=timeout) as r:
        return r.read()


# ------------------------------------------------------------------------------------------------- $metadata model
def short(t):
    t = t or ""
    m = re.match(r"^Collection\((.+)\)$", t)
    if m:
        return "Collection(" + short(m.group(1)) + ")"
    return t.replace("microsoft.graph.", "").replace("graph.", "")


def parse(xml):
    """$metadata -> {types: {name: {k, b, p, n, m}}, ops: {key: {k, bt, r, pa}}, roots: {name: [kind, type]}}"""
    root = ET.fromstring(xml)
    types, ops, roots = {}, {}, {}
    for sch in root.iter(EDM + "Schema"):
        ns = sch.get("Namespace") or ""
        pre = "" if ns == "microsoft.graph" else ns.replace("microsoft.graph.", "") + "."
        for el in sch:
            tag = el.tag.replace(EDM, "")
            name = pre + (el.get("Name") or "")
            if tag in ("EntityType", "ComplexType"):
                t = {"k": "E" if tag == "EntityType" else "C", "p": {}, "n": {}}
                if el.get("BaseType"):
                    t["b"] = short(el.get("BaseType"))
                if el.get("Abstract") == "true":
                    t["a"] = 1
                for c in el:
                    ct = c.tag.replace(EDM, "")
                    if ct == "Property":
                        t["p"][c.get("Name")] = short(c.get("Type"))
                    elif ct == "NavigationProperty":
                        t["n"][c.get("Name")] = short(c.get("Type")) + ("*" if c.get("ContainsTarget") == "true" else "")
                types[name] = t
            elif tag == "EnumType":
                types[name] = {"k": "N", "m": [c.get("Name") for c in el if c.tag == EDM + "Member"]}
            elif tag in ("Action", "Function"):
                params = [c for c in el if c.tag == EDM + "Parameter"]
                bound = el.get("IsBound") == "true"
                bt = short(params[0].get("Type")) if bound and params else ""
                rt = next((short(c.get("Type")) for c in el if c.tag == EDM + "ReturnType"), "")
                key = name + "(" + bt + ")"
                ops[key] = {"k": "A" if tag == "Action" else "F", "bt": bt, "r": rt,
                            "pa": [c.get("Name") for c in (params[1:] if bound else params)]}
            elif tag == "EntityContainer":
                for c in el:
                    ct = c.tag.replace(EDM, "")
                    if ct in ("EntitySet", "Singleton"):
                        roots[c.get("Name")] = ["S" if ct == "EntitySet" else "1", short(c.get("EntityType") or c.get("Type"))]
    return {"types": types, "ops": ops, "roots": roots}


def counts(m):
    t = m["types"]
    return {"entities": sum(1 for x in t.values() if x["k"] == "E"), "complex": sum(1 for x in t.values() if x["k"] == "C"),
            "enums": sum(1 for x in t.values() if x["k"] == "N"), "properties": sum(len(x.get("p", {})) for x in t.values()),
            "navigations": sum(len(x.get("n", {})) for x in t.values()), "actions": sum(1 for x in m["ops"].values() if x["k"] == "A"),
            "functions": sum(1 for x in m["ops"].values() if x["k"] == "F"), "roots": len(m["roots"])}


def all_props(m, tname, seen=None):
    """properties of a type including its base types"""
    seen = seen or set()
    t = m["types"].get(tname)
    if not t or tname in seen:
        return {}
    seen.add(tname)
    out = dict(all_props(m, t.get("b"), seen)) if t.get("b") else {}
    out.update(t.get("p", {}))
    out.update({k: v for k, v in t.get("n", {}).items()})
    return out


def diff(old, new, ver, day, via):
    """events between two models of one version"""
    ev = []
    ot, nt = old["types"], new["types"]
    def e(kind, typ, name, detail="", **kw):
        x = {"day": day, "ver": ver, "via": via, "kind": kind, "type": typ, "name": name}
        if detail:
            x["detail"] = detail
        x.update(kw)
        ev.append(x)
    for tn, t in nt.items():
        o = ot.get(tn)
        if o is None:
            e("type-new", tn, tn, {"E": "entity type", "C": "complex type", "N": "enum type"}[t["k"]],
              props=(sorted(t.get("p", {})) or t.get("m", []))[:40], base=t.get("b", ""))
            continue
        if t["k"] == "N":
            for mbr in t.get("m", []):
                if mbr not in o.get("m", []):
                    e("member-new", tn, mbr, "new value of " + tn)
            for mbr in o.get("m", []):
                if mbr not in t.get("m", []):
                    e("member-removed", tn, mbr)
            continue
        for p, ty in t.get("p", {}).items():
            if p not in o.get("p", {}):
                e("prop-new", tn, p, ty)
            elif o["p"][p] != ty:
                e("prop-type", tn, p, o["p"][p] + " -> " + ty)
        for p in o.get("p", {}):
            if p not in t.get("p", {}):
                e("prop-removed", tn, p, o["p"][p])
        for p, ty in t.get("n", {}).items():
            if p not in o.get("n", {}):
                e("nav-new", tn, p, ty)
        for p in o.get("n", {}):
            if p not in t.get("n", {}):
                e("nav-removed", tn, p)
    for tn in ot:
        if tn not in nt:
            e("type-removed", tn, tn)
    for k, op in new["ops"].items():
        if k not in old["ops"]:
            e("op-new", op["bt"] or "(unbound)", k.split("(")[0], ("action" if op["k"] == "A" else "function") + (" -> " + op["r"] if op["r"] else ""),
              params=op["pa"][:12])
    for k, op in old["ops"].items():
        if k not in new["ops"]:
            e("op-removed", op["bt"] or "(unbound)", k.split("(")[0])
    for r, v in new["roots"].items():
        if r not in old["roots"]:
            e("root-new", v[1], r, "entity set" if v[0] == "S" else "singleton")
    return ev


# ------------------------------------------------------------------------------------------------ paths and permissions
def path_index(m, depth=5, keep=8):
    """entity type -> up to `keep` shortest URL paths from an entity set or singleton (ids as {id}); best_path() picks
    the one Microsoft's permission file knows (an orphan entity set like /authenticationMethodConfigurations is shorter
    than /policies/authenticationMethodsPolicy/authenticationMethodConfigurations but is not where anyone calls it)"""
    types = m["types"]
    derived = {}
    for tn, t in types.items():
        if t.get("b"):
            derived.setdefault(t["b"], []).append(tn)
    best = {}
    queue = []
    for r, (kind, t) in sorted(m["roots"].items()):
        queue.append((t, "/" + r + ("/{id}" if kind == "S" else ""), 0))
    seen_pairs = set()
    while queue:
        t, p, d = queue.pop(0)
        lst = best.setdefault(t, [])
        if len(lst) >= keep or (t, p) in seen_pairs or p.count("/") > 12:
            continue
        seen_pairs.add((t, p))
        lst.append(p)
        for dt in derived.get(t, []):
            queue.append((dt, p, d))
        if d >= depth:
            continue
        for nav, nt in all_navs(m, t).items():
            coll = nt.startswith("Collection(")
            tt = re.sub(r"^Collection\((.+)\)$", r"\1", nt.rstrip("*"))
            queue.append((tt, p + "/" + nav + ("/{id}" if coll else ""), d + 1))
    return best


def best_path(cands, gp):
    for p in cands or []:
        if perms_for(gp, p, "GET"):
            return p
    return (cands or [None])[0]


def all_navs(m, tn, seen=None):
    seen = seen or set()
    t = m["types"].get(tn)
    if not t or tn in seen:
        return {}
    seen.add(tn)
    out = dict(all_navs(m, t.get("b"), seen)) if t.get("b") else {}
    out.update(t.get("n", {}))
    return out


def owner_entity(m, tname, cache={}):
    """for a complex type: the entity type that holds it (directly or one complex level down)"""
    if tname in cache:
        return cache[tname]
    for tn, t in m["types"].items():
        if t["k"] != "E":
            continue
        for p, ty in t.get("p", {}).items():
            if re.sub(r"^Collection\((.+)\)$", r"\1", ty) == tname:
                cache[tname] = (tn, p)
                return cache[tname]
    cache[tname] = None
    return None


def graph_perms():
    """Microsoft's own permission file as the portal reads it (graphMap of the newest state): path -> method -> perms"""
    days = sorted(f for f in os.listdir(SITE) if re.match(r"^\d{4}-\d{2}-\d{2}\.json(\.gz)?$", f))
    for f in reversed(days[-3:]):
        st = load(os.path.join(SITE, f), {}).get("soc-brief-state") or {}
        gm = st.get("graphMap") or {}
        if gm.get("p") and gm.get("perms"):
            P, M, idx = gm["p"], gm["m"], {}
            for name, v in gm["perms"].items():
                for part in (v.get("eps") or "").split(";"):
                    if ":" not in part:
                        continue
                    mi, ps = part.split(":", 1)
                    for rng in ps.split(","):
                        a, _, b = rng.partition("-")
                        if not a.isdigit():
                            continue
                        for x in range(int(a), int(b or a) + 1):
                            lv = min(((s.get("l") if isinstance(s.get("l"), int) else 9) for k, s in (v.get("s") or {}).items() if k in ("Application", "DelegatedWork")), default=9)
                            idx.setdefault(P[x], {}).setdefault(M[int(mi)], []).append((lv, name))
            return idx
    return {}


def perms_for(idx, path, method):
    if not idx or not path:
        return []
    pl = path.lower()
    cand = idx.get(pl)
    if cand is None:
        rx = re.compile("^" + re.escape(pl).replace(re.escape("{id}"), r"[^/]+") + "$")
        for k, v in idx.items():
            if rx.match(k):
                cand = v
                break
    if not cand or method not in cand:
        return []
    ranked = sorted(set(cand[method]))
    low = ranked[0][0]
    return [n for l, n in ranked if l == low][:3]


def sample(ty, m):
    """a value of the right type for a PATCH body - the reader replaces it"""
    ty = ty or ""
    if ty.startswith("Collection("):
        return []
    if ty == "Edm.Boolean":
        return True
    if ty in ("Edm.Int32", "Edm.Int64", "Edm.Int16", "Edm.Double", "Edm.Decimal"):
        return 0
    t = m["types"].get(ty) if m else None
    if t and t["k"] == "N" and t.get("m"):
        return t["m"][0]
    if t and t["k"] == "C":
        return {}
    return "<value>"


def command(path, tname, prop, ty, m, idx, ver="beta"):
    if not path:
        return None
    base = "https://graph.microsoft.com/" + ver
    c = {"get": base + path, "permGet": perms_for(idx, path, "GET"), "permPatch": perms_for(idx, path, "PATCH")}
    if prop:
        body = {"@odata.type": "#microsoft.graph." + tname, prop: sample(ty, m)}
        c["patch"] = base + path
        c["body"] = body
    return c


# ------------------------------------------------------------------------------------------------ MC posts
def mc_index():
    days = sorted(f for f in os.listdir(SITE) if re.match(r"^\d{4}-\d{2}-\d{2}\.json(\.gz)?$", f))
    out = {}
    for f in days[-2:]:
        st = load(os.path.join(SITE, f), {}).get("soc-brief-state") or {}
        for it in (st.get("items") or []):
            i = str(it.get("id") or "")
            if re.match(r"^MC\d+$", i):
                out[i] = " ".join(str(it.get(k) or "") for k in ("officialTitle", "title", "fingerprint"))
        for it in ((st.get("mc") or {}).get("items") if isinstance(st.get("mc"), dict) else []) or []:
            i = str(it.get("id") or "")
            if re.match(r"^MC\d+$", i):
                out.setdefault(i, " ".join(str(it.get(k) or "") for k in ("title", "summary")))
    return {k: " " + " ".join(re.findall(r"[a-z0-9]+", v.lower())) + " " for k, v in out.items()}


STOPW = {"is", "on", "of", "the", "for", "and", "to", "in", "a", "an", "by", "id", "at", "or", "with", "type", "settings", "setting", "configuration", "enabled", "state"}


def words(name):
    w = [x.lower() for x in re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?![a-z])|\d+", name)]
    return [x for x in w if x not in STOPW]


def mc_match(idx, name):
    """an MC post whose text holds the property's words as one phrase ("allow password change after secure sign in")"""
    w = [x.lower() for x in re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?![a-z])|\d+", (name or "").split(".")[-1])]
    if len([x for x in w if x not in STOPW]) < 3:
        return []
    ph = " " + " ".join(w) + " "
    return sorted(k for k, txt in idx.items() if ph in txt)[:3]


def learn_licensing():
    """Learn page edits a criterion marked "licensing" (collect_nt.py, 5fs) - shown with the radar in the Overview
    sentence; read from the newest published state (the routine writes nt.pages)"""
    days = sorted(f for f in os.listdir(SITE) if re.match(r"^\d{4}-\d{2}-\d{2}\.json(\.gz)?$", f))
    for f in reversed(days[-2:]):
        st = load(os.path.join(SITE, f), {}).get("soc-brief-state") or {}
        pages = (st.get("nt") or {}).get("pages") or []
        if pages:
            out = []
            for pg in pages:
                if "licensing" in (pg.get("promote") or []):
                    lines = [l for h in pg.get("hunks") or [] for l in h.get("add") or []][:3]
                    out.append({k: pg.get(k) for k in ("area", "name", "url", "date", "commit", "added", "removed")} | {"lines": lines})
            return out, f[:10]
    return [], ""


# ------------------------------------------------------------------------------------------------ tenant
GP = {}


def tenant_read(model, day):
    if not (os.environ.get("ACTIONS_ID_TOKEN_REQUEST_URL") and os.environ.get("AZURE_CLIENT_ID") and os.environ.get("AZURE_TENANT_ID")):
        return None, "no token in this run (the workflow signs in with the app of the developer tenant)"
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import fpa_tenant as T
    try:
        tok = T.token()[1]   # (tenant id, access token)
    except Exception as e:
        return None, "sign-in failed: %s" % e
    res = []
    for label, path, perm in PROBE:
        url = "https://graph.microsoft.com/beta" + path
        r = {"label": label, "path": path, "perm": perm}
        try:
            body = json.loads(get(url, {"Authorization": "Bearer " + tok, "ConsistencyLevel": "eventual"}, timeout=60))
            objs = body.get("value") if isinstance(body.get("value"), list) else [body]
            seen, vals = {}, {}
            root_t = resolve_path(model, path)
            for o in objs[:200]:
                walk(o, o.get("@odata.type") or "", root_t, "", seen, model, 0, vals)
            r["status"] = 200
            r["n"] = len(objs)
            r["props"] = seen
            r["vals"] = vals
        except urllib.error.HTTPError as e:
            r["status"] = e.code
            need = perms_for(GP, path, "GET") or [perm]
            r["note"] = "403: needs %s" % " or ".join(need) if e.code == 403 else "HTTP %d" % e.code
        except Exception as e:
            r["status"] = 0
            r["note"] = str(e)[:200]
        res.append(r)
    return res, ""


def kind(v):
    return "boolean" if isinstance(v, bool) else "number" if isinstance(v, (int, float)) else "string" if isinstance(v, str) \
        else "array" if isinstance(v, list) else "object" if isinstance(v, dict) else "null"


def resolve_path(model, path):
    """the declared type a GET of this path returns (the element type for a collection): /policies -> policyRoot,
    /authenticationMethodsPolicy -> authenticationMethodsPolicy, /authenticationMethodConfigurations/Password ->
    authenticationMethodConfiguration (a segment that is no navigation is a key)"""
    segs = [x for x in path.split("/") if x]
    if not segs or segs[0] not in model["roots"]:
        return ""
    t = model["roots"][segs[0]][1]
    for sg in segs[1:]:
        nv = all_navs(model, t)
        hit = next((k for k in nv if k.lower() == sg.lower()), None)
        if hit:
            t = re.sub(r"^Collection\((.+)\)$", r"\1", nv[hit].rstrip("*"))
            continue
        pr = all_props(model, t)
        hit = next((k for k in pr if k.lower() == sg.lower()), None)
        if hit:
            t = re.sub(r"^Collection\((.+)\)$", r"\1", pr[hit].rstrip("*"))
    return t


def path_is_collection(model, path):
    """5fy: does a GET of this path return a list (/identity/conditionalAccess/policies)? A PATCH then needs an item:
    path + /{id}. Owner, 31 X 2026: the Try it of conditions.times sent a PATCH to the list of policies"""
    segs = [x for x in path.split("/") if x]
    if not segs or segs[0] not in model["roots"]:
        return False
    coll = model["roots"][segs[0]][0] != "1"
    t = model["roots"][segs[0]][1]
    for sg in segs[1:]:
        if coll:            # a key into the list: /policies/{id}
            coll = False
            continue
        nv = all_navs(model, t)
        hit = next((k for k in nv if k.lower() == sg.lower()), None)
        ty = nv.get(hit) if hit else None
        if not ty:
            pr = all_props(model, t)
            hit = next((k for k in pr if k.lower() == sg.lower()), None)
            ty = pr.get(hit) if hit else None
        if not ty:
            return False
        ty = ty.rstrip("*")
        coll = ty.startswith("Collection(")
        t = re.sub(r"^Collection\((.+)\)$", r"\1", ty)
    return coll


def item_patch(u, model, gp):
    """5fy: a list that Microsoft's permission file lets you PATCH only per item (/identity/conditionalAccess/policies,
    /organization) gets /{id}; a list that takes the PATCH itself (beta /policies/authorizationPolicy) keeps its path"""
    if path_is_collection(model, u["path"]) and not perms_for(gp, u["path"], "PATCH"):
        p2 = u["path"] + "/{id}"
        if perms_for(gp, p2, "PATCH"):
            u["cmd"]["patch"] = u["cmd"]["get"] + "/{id}"
            u["cmd"]["permPatch"] = perms_for(gp, p2, "PATCH")
            u["itemPath"] = p2


SAFE_KEY = re.compile(r"name|mail|upn|principal|domain|url|uri|description|comment|note|address|phone|tenant|(^|[a-z])id$|ids$|Id$|Ids$|key|secret|thumbprint|subject|issuer", re.I)
ENUMISH = re.compile(r"^[a-z][a-zA-Z_]{1,39}$")
DATEISH = re.compile(r"^\d{4}-\d{2}-\d{2}(T[\d:.]+(Z|[+-]\d{2}:\d{2})?)?$")


def safe_val(k, v):
    """5fy: a value the radar may publish (the repository is public): true/false, an enum-like word ("autoEnable",
    "disabled", "all_users" is not one), a placeholder for everything else - never a name, an id, an address or text"""
    if isinstance(v, bool):
        return v
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return "<number>"
    if isinstance(v, str):
        if DATEISH.match(v):
            return "<date-time>" if "T" in v else "<date>"
        if not SAFE_KEY.search(k) and ENUMISH.match(v):
            return v
        return "<text>"
    return None


def walk(o, otype, declared, prefix, seen, model, depth=0, vals=None):
    """names of the properties the service returned. key: actual type | declared type | property path.
    The actual type is the object's own @odata.type; the declared type comes from $metadata (the root of the path, or
    the property that holds the object) and is used when Microsoft has not published the actual type yet.
    5fy: with vals, also the values seen per property path - only what safe_val lets through (true/false, enum words,
    placeholders), up to 8 per path; the deeper levels (depth 3-4) are walked for these paths too"""
    t = short((otype or "").lstrip("#")) or declared
    for k, v in o.items():
        if k.startswith("@") or "@odata" in k:
            continue
        if depth < 3:
            seen[t + "|" + declared + "|" + prefix + k] = kind(v)
        if vals is not None:
            sv = vals.setdefault(prefix + k, {"kind": kind(v), "v": []})
            if sv["kind"] == "null" and v is not None:
                sv["kind"] = kind(v)
            items = v if isinstance(v, list) else [v]
            for it in items[:20]:
                x = safe_val(k, it)
                if x is not None and x not in sv["v"] and len(sv["v"]) < 8:
                    sv["v"].append(x)
            if isinstance(v, list) and v and not isinstance(v[0], dict):
                sv["item"] = kind(v[0])
        if isinstance(v, dict) and depth < (4 if vals is not None else 2):
            d2 = nested_type(model, t, k) or nested_type(model, declared, k)
            walk(v, v.get("@odata.type") or "", d2, prefix + k + ".", seen, model, depth + 1, vals)
        elif isinstance(v, list) and v and isinstance(v[0], dict) and depth < (4 if vals is not None else 2):
            d2 = nested_type(model, t, k) or nested_type(model, declared, k)
            for it in v[:20]:
                walk(it, it.get("@odata.type") or "", d2, prefix + k + "[].", seen, model, depth + 1, vals)


def nested_type(model, t, k):
    ty = all_props(model, t).get(k, "") if t else ""
    return re.sub(r"^Collection\((.+)\)$", r"\1", ty.rstrip("*"))


def shape_of(vals, pp, n):
    """5fy (owner, 31 X 2026: "how does the community know what a parameter takes when Learn has nothing? If they can,
    so can you - show it for the other findings too"): what our tenant returns at this property and under it - every
    sub-property with its JSON kind and the safe values seen on the objects read (n of them)"""
    out = []
    for path, sv in sorted(vals.items()):
        if path == pp or path.startswith(pp + ".") or path.startswith(pp + "[]."):
            rel = path[len(pp):].lstrip(".") or ""
            e = {"p": rel, "k": sv["kind"]}
            if sv.get("v"):
                e["v"] = sv["v"]
            if sv.get("item"):
                e["i"] = sv["item"]
            out.append(e)
    return {"n": n, "rows": out[:40]} if out else None


def skeleton(shape):
    """5fy: a PATCH body in the shape our tenant returns - sub-properties with the first safe value seen, or a typed
    placeholder; None when the tenant returned nothing under the property (null, [] or a plain value)"""
    rows = [r for r in (shape or {}).get("rows") or [] if r["p"]]
    if not rows:
        return None
    def ph(r):
        v = (r.get("v") or [None])[0]
        if r["k"] == "array":
            return [v] if v is not None else []
        if v is not None and not (isinstance(v, str) and v.startswith("<")):
            return v
        return {"boolean": False, "number": 0, "string": "<text>", "object": {}}.get(r["k"], None)
    out = {}
    for r in rows:
        if "[]" in r["p"]:
            continue
        cur, segs = out, r["p"].split(".")
        for sg in segs[:-1]:
            cur = cur.setdefault(sg, {}) if isinstance(cur.get(sg, {}), dict) else {}
        if segs[-1] not in cur or not isinstance(cur[segs[-1]], dict):
            cur[segs[-1]] = ph(r) if r["k"] != "object" else cur.get(segs[-1], {})
    return out or None


def undocumented(res, model):
    out, done = [], set()
    for r in res or []:
        for key, kd in (r.get("props") or {}).items():
            parts = key.split("|")
            if len(parts) != 3:
                continue
            t, dt, pp = parts
            prop = pp.split(".")[-1].replace("[]", "")
            tdoc = t in model["types"]
            known = all_props(model, t) if tdoc else {}
            if not tdoc and dt:
                known = all_props(model, dt)
            if not t and not dt:
                continue                   # nothing to compare with: not a finding
            if prop in known:
                continue
            k2 = (t, prop)
            if k2 in done:                 # the same property on many objects (64 settings policies) is one finding
                continue
            done.add(k2)
            out.append({"type": t or dt, "prop": pp, "kind": kd, "path": r["path"], "label": r["label"], "typeDocumented": tdoc,
                        "declared": dt if dt != t else "", "shape": shape_of(r.get("vals") or {}, pp, r.get("n") or 0)})
    return out


# ------------------------------------------------------------------------------------------------ 5ft: readable findings
# Owner, 30 X 2026: "unreadable - no description of what it could be for, no split per technology; show the permission and
# its description better; if the internet ties a finding to an article (like Jan Bakker's), list it the way MC posts are;
# from what you find, write possible uses in bullets". Every finding gets: a technology, a plain-English title, whether
# Microsoft documents it anywhere (Learn reference pages from microsoft-graph-docs-contrib, v1.0 $metadata), the hand-
# written note of data/graph-radar/notes.json (what it is, uses, checked articles), the articles of the portal's own
# feeds whose title holds the property's words, and Microsoft's description of every permission named on its card.
CATS = [
    ("Conditional Access", r"conditionalAccess|namedLocation", "Who may sign in to what, from where and how - the policies that decide every sign-in."),
    ("Authentication methods", r"authenticationMethod|authenticationStrength|authenticationFlows|authenticationCombination|passwordless|fido2|temporaryAccessPass|mfa",
     "Which sign-in methods users may register and use (passkeys, Authenticator, SMS, voice, password, certificates)."),
    ("Cross-tenant access", r"crossTenant|multiTenantOrganization|externalIdentitiesPolicy|b2b", "What users of other Entra organizations may do in your tenant, and your users in theirs."),
    ("Default user permissions", r"authorizationPolicy|defaultUserRolePermissions", "What every user without an admin role may do: register apps, create groups, read other users, create agent blueprints."),
    ("Security defaults", r"identitySecurityDefaults", "The free baseline protection for tenants without Conditional Access."),
    ("App management & consent", r"appManagement|permissionGrant|adminConsent|tokenLifetime|tokenIssuance|claimsMapping|activityBasedTimeout|homeRealmDiscovery|oauth2|servicePrincipal|application",
     "Rules for app registrations and enterprise apps: credentials, consent, token lifetimes."),
    ("Agents & Copilot", r"agent|copilot|aiInteraction|^/ai|\bai[A-Z]", "AI agents and Copilot: agent identities, blueprints, interactions."),
    ("Global Secure Access", r"networkAccess", "Microsoft's security service edge: Internet Access, Private Access, compliant network."),
    ("Identity governance", r"identityGovernance|accessReview|entitlement|lifecycleWorkflow|customExtension|privilegedAccess|roleManagement|unifiedRole|termsOfUse",
     "Access reviews, access packages, lifecycle workflows, PIM and roles."),
    ("Planner, Places & productivity", r"planner|^/places|place[A-Z]|booking|todo|onenote|^/solutions", "Planner, Places (rooms, desks), Bookings, To Do, OneNote."),
    ("Identity protection", r"riskyUser|riskyServicePrincipal|riskDetection|identityProtection|riskyAgent|risk[A-Z]|^risk", "Risky users, risky sign-ins and risky agents."),
    ("Intune & devices", r"deviceManagement|deviceAppManagement|intune|autopilot|managedDevice|deviceRegistration|^/devices|device[A-Z]",
     "Intune device, app and enrollment settings, device registration."),
    ("Windows & Cloud PC", r"windows|cloudPc|virtualEndpoint", "Windows Update, Windows 365 Cloud PCs."),
    ("Security & Defender", r"^/security|^security\.|security[A-Z]|threat|alert|incident|attackSimulation|secureScore|ediscovery", "Defender XDR: alerts, incidents, hunting, Secure Score, attack simulation."),
    ("Purview & compliance", r"compliance|sensitivityLabel|dataLossPrevention|informationProtection|retention|records|purview",
     "Labels, DLP, retention, eDiscovery and audit."),
    ("Organization & sync", r"organization|onPremises|directorySync|domain|tenantRelationship|relatedTenant|^/directory", "The tenant itself: organization settings, domains, directory synchronization."),
    ("Teams & meetings", r"\bteams?\b|team[A-Z]|chat|onlineMeeting|call[A-Z]|communications|virtualEvent|meeting", "Teams, chats, meetings, calls."),
    ("Mail & calendar", r"mail|message|calendar|event[A-Z]|contact|outlook|inbox|exchange", "Exchange Online: mail, calendars, contacts."),
    ("Files & SharePoint", r"drive|site|sharepoint|fileStorage|onedrive|list[A-Z]|listItem", "SharePoint sites, OneDrive, files and lists."),
    ("Users & groups", r"^/users|^/groups|user[A-Z]|group[A-Z]|directoryObject|administrativeUnit|^user$|^group$", "Users, groups, administrative units."),
    ("Reports & audit", r"report|auditLog|signIn|usage", "Sign-in and audit logs, usage reports."),
]
CAT_INFO = {c[0]: c[2] for c in CATS}
CAT_INFO["Other"] = "Everything the other technologies do not cover."


def category(*texts):
    texts = [re.sub(r"^/me(?=/|$)", "", t) if t else t for t in texts]   # /me/... says nothing about the technology
    for name, rx, _ in CATS:
        for t in texts:
            if t and re.search(rx, t, re.I if not rx.startswith("^") else 0):
                return name
    return "Other"


def humanize(name):
    """allowPasswordChangeAfterSecureSignIn -> Allow password change after secure sign in"""
    w = re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?![a-z])|\d+", (name or "").split(".")[-1].replace("[]", ""))
    if not w:
        return name or ""
    out = [w[0][:1].upper() + w[0][1:].lower()] + [x if x.isupper() and len(x) > 1 else x.lower() for x in w[1:]]
    return " ".join(out)


DOCS_RAW = "https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-docs-contrib/main/api-reference/%s/resources/%s.md"
DOCS_URL = "https://learn.microsoft.com/graph/api/resources/%s?view=graph-rest-%s"


def docs_check(types, leaf, cache, day):
    """the Graph reference page of the type (beta and v1.0) names the property? -> the Learn URL. Microsoft writes these
    pages in microsoftgraph/microsoft-graph-docs-contrib; a property on the page but not in $metadata is documented
    before the service schema says so (isCompliantNetworkAccepted, 30 X)."""
    found = {}
    for ver in ("beta", "v1.0"):
        for t in [x for x in types if x]:
            k = "%s|%s" % (ver, t.lower())
            c = cache.get(k)
            if not c or c.get("day") != day:
                try:
                    txt = get(DOCS_RAW % (ver, t.lower()), timeout=30).decode("utf-8", "replace")
                    props = sorted(set(re.findall(r"^\|\s*([A-Za-z0-9_]+)\s*\|", txt, re.M)))
                    c = {"day": day, "ok": True, "props": props}
                except urllib.error.HTTPError as e:
                    c = {"day": day, "ok": False, "code": e.code, "props": []}
                except Exception as e:
                    c = (cache.get(k) or {}) if cache.get(k) else {"day": day, "ok": False, "props": [], "note": str(e)[:80]}
                cache[k] = c
            if leaf in (c.get("props") or []):
                found[ver] = DOCS_URL % (t.lower(), "beta" if ver == "beta" else "1.0")
                break
    return found


ART_STOP = STOPW | {"allow", "allowed", "is", "has", "include", "includes", "enable", "enabled", "configuration", "configurations", "settings",
                    "level", "levels", "details", "default", "value", "values", "list", "status", "new"}
TYPE_GENERIC = {"authentication", "method", "methods", "configuration", "policy", "access", "conditional", "settings", "default", "set",
                "condition", "conditions", "controls", "control", "session", "application", "applications", "management", "enforcement", "identity"}


def stem(w):
    w = w.lower()
    return w[:5] if len(w) > 5 else w


def text_stems(t):
    return {stem(x) for x in re.findall(r"[a-z0-9]+", (t or "").lower())}


def article_keys(typ, leaf):
    """the stems an article title must hold to be about this property; None when the name is too generic to match"""
    w = [x for x in words(leaf) if x not in ART_STOP and len(x) > 3]
    if len(w) < 2:
        return None
    ctx = [stem(x) for x in words(typ or "") if x not in TYPE_GENERIC and x not in ART_STOP and len(x) > 3 and stem(x) not in {stem(y) for y in w}]
    if len(w) == 2 and not ctx:
        return None                      # two common words alone ("agent actions") match too many titles
    return {"all": [stem(x) for x in w], "ctx": ctx if len(w) == 2 else []}


def article_pool(days=1):
    """titles the portal itself read: community articles, Microsoft blog posts, Learn What's new, Message Center posts"""
    files = sorted(f for f in os.listdir(SITE) if re.match(r"^\d{4}-\d{2}-\d{2}\.json(\.gz)?$", f))[-days:]
    pool, seen = [], set()
    for f in files:
        st = load(os.path.join(SITE, f), {}).get("soc-brief-state") or {}
        for it in ((st.get("community") or {}).get("items") or []):
            pool.append({"title": it.get("title"), "url": it.get("link"), "by": it.get("source"), "date": it.get("date"), "via": "Community Articles"})
        nt = st.get("nt") or {}
        for it in (nt.get("items") or []):
            pool.append({"title": it.get("title"), "url": it.get("link"), "by": it.get("source"), "date": str(it.get("date") or it.get("published") or "")[:10], "via": "Microsoft Blogs"})
        for it in (nt.get("recent") or []):
            pool.append({"title": it.get("title"), "text": it.get("text"), "url": it.get("url") or it.get("link"), "by": "Microsoft Learn - What's new (" + str(it.get("area") or "") + ")",
                         "date": "%s-%02d" % (it.get("year"), it.get("month") or 0) if it.get("year") else "", "via": "Microsoft Learn"})
        for it in ((st.get("mc") or {}).get("entries") or []):
            pool.append({"title": (it.get("id") or "") + " - " + (it.get("title") or ""), "text": it.get("feedSummary"), "url": it.get("link"), "by": "Microsoft Message Center",
                         "date": it.get("published"), "via": "Message Center"})
    out = []
    for p in pool:
        if p.get("url") and p.get("title") and p["url"] not in seen:
            seen.add(p["url"])
            p["st"] = text_stems(p["title"])    # titles only: summaries mention too much (30 X: 4 unrelated MC posts for optOutSettings)
            out.append(p)
    return out


def article_hits(keys, pool):
    if not keys:
        return []
    hits, ids = [], set()
    for p in pool:
        mid = re.match(r"^((?:MC|RM)\d+)", p.get("title") or "") or re.search(r"roadmap\?id=(\d+)", p.get("url") or "")
        if mid and mid.group(1).isdigit():
            mid = re.match(r"(.*)", "RM" + mid.group(1))      # the roadmap page and RM575285 are one item
        if mid and mid.group(1) in ids:
            continue                     # the same post through two feeds (admin center and merill.net)
        if all(k in p["st"] for k in keys["all"]) and (not keys["ctx"] or any(c in p["st"] for c in keys["ctx"])):
            hits.append({k: p.get(k) for k in ("title", "url", "by", "date", "via")} | {"rel": "words"})
            if mid:
                ids.add(mid.group(1))
    return hits[:6]


def perm_info(names):
    """Microsoft's own title and description of each permission (graph-sp.json, read from the service principal)"""
    sp = load(os.path.join(SITE, "graph-sp.json"), {}) or {}
    P = sp.get("perms") or {}
    out = {}
    for nm in sorted(set(names)):
        p = P.get(nm) or {}
        a, d = p.get("Application") or {}, p.get("Delegated") or {}
        if not (a or d):
            continue
        out[nm] = {"title": a.get("title") or d.get("title") or "", "app": a.get("text") or "", "del": d.get("text") or "",
                   "delConsent": d.get("consent") or "", "write": bool(re.search(r"ReadWrite|\.Manage|\.Create|\.Write|\.Send|\.Delete", nm))}
    return out


def merged_notes():
    """5fy: notes.json (written by a person) and site/data/graph-radar-notes.json (written by the morning routine after a web
    search for community articles, values and examples - routines/poranny-B-publish.md STEP -1c). Per property the
    note checked last wins; a person's note wins a tie; the articles of both are kept"""
    own = (load(os.path.join(MEM, "notes.json"), {}) or {}).get("notes") or {}
    com = (load(os.path.join(SITE, "graph-radar-notes.json"), {}) or {}).get("notes") or {}
    out = dict(own)
    for k, c in com.items():
        o = own.get(k)
        if not o:
            out[k] = c
            continue
        win, other = (c, o) if (c.get("checked") or "") > (o.get("checked") or "") else (o, c)
        m = dict(win)
        urls = {a.get("url") for a in m.get("articles") or []}
        m["articles"] = list(m.get("articles") or []) + [a for a in other.get("articles") or [] if a.get("url") not in urls]
        out[k] = m
    return out


def enrich_findings(und, beta, v1, day, mci_titles=None):
    """5ft: technology, documentation status, notes and articles for every undocumented property"""
    notes = merged_notes()
    dcache = load(os.path.join(MEM, "docs-cache.json"), {}) or {}
    amem = load(os.path.join(MEM, "articles.json"), None)
    pool = article_pool(30 if amem is None else 2)
    amem = amem or {}
    for u in und:
        leaf = u["prop"].split(".")[-1].replace("[]", "")
        key = u["type"] + "|" + leaf
        u["leaf"] = leaf
        u["cat"] = category(u.get("path"), u.get("label"), u["type"])
        if re.search(r"agent", leaf, re.I) and u["cat"] != "Agents & Copilot":
            u["also"] = ["Agents & Copilot"]
        u["human"] = humanize(leaf)
        doc = {}
        if v1 and (leaf in all_props(v1, u["type"]) or (u.get("declared") and leaf in all_props(v1, u["declared"]))):
            doc["v1meta"] = 1
        doc.update(docs_check([u["type"], u.get("declared")], leaf, dcache, day))
        u["doc"] = doc
        u["status"] = "v1" if doc.get("v1meta") else "learn" if (doc.get("beta") or doc.get("v1.0")) else "new"
        n = notes.get(key)
        if n:
            u["note"] = n
            if n.get("title"):
                u["human"] = n["title"]
        hits = article_hits(article_keys(u["type"], leaf), pool)
        known = {a.get("url") for a in (n or {}).get("articles") or []} | {"https://mc.merill.net/message/" + m for m in u.get("mc") or []}
        old = amem.get(key) or []
        def pid(x):   # one MC / roadmap item through several feeds is one source
            m = re.match(r"^((?:MC|RM)\d+)", x.get("title") or "") or re.search(r"roadmap\?id=(\d+)", x.get("url") or "")
            return ("RM" + m.group(1)) if m and m.group(1).isdigit() else (m.group(1) if m else "")
        have = {pid(x) for x in old} | set(u.get("mc") or [])
        old = [x for i, x in enumerate(old) if not pid(x) or pid(x) not in {pid(y) for y in old[:i]}]
        for h in hits:
            if h["url"] not in known and h["url"] not in {x["url"] for x in old} and not (pid(h) and pid(h) in have):
                have.add(pid(h))
                h["first"] = day
                old.append(h)
        amem[key] = old[-8:]
        u["auto"] = [a for a in amem[key] if a["url"] not in known]
    save(os.path.join(MEM, "docs-cache.json"), dcache)
    save(os.path.join(MEM, "articles.json"), amem)


# ------------------------------------------------------------------------------------------------ backfill
def backfill(repo, n=12):
    """events between the weekly schema syncs of a msgraph-metadata clone (blobless is fine)"""
    ev, last = [], {}
    for ver, f in (("beta", "schemas/beta-Prod.csdl"), ("v1.0", "schemas/v1.0-Prod.csdl")):
        log_ = subprocess.run(["git", "-C", repo, "log", "--format=%H %cs", "-%d" % (n + 1), "--", f], capture_output=True, text=True).stdout.split("\n")
        commits = [l.split() for l in log_ if l.strip()][::-1]
        prev = None
        for h, d in commits:
            xml = subprocess.run(["git", "-C", repo, "show", "%s:%s" % (h, f)], capture_output=True).stdout
            try:
                cur = parse(xml)
            except Exception as e:
                log("backfill: not parsed", ver, d, e)
                continue
            if prev is not None:
                ev += diff(prev, cur, ver, d, "msgraph-metadata")
            prev = cur
        last[ver] = prev
        log("backfill", ver, len(commits), "syncs")
    return ev, last


# ------------------------------------------------------------------------------------------------ main
def main(argv):
    day = datetime.date.today().isoformat()
    bf, no_tenant = None, False
    i = 0
    while i < len(argv):
        if argv[i] == "--day":
            day = argv[i + 1]; i += 2; continue
        if argv[i] == "--backfill":
            bf = argv[i + 1]; i += 2; continue
        if argv[i] == "--no-tenant":
            no_tenant = True
        i += 1
    hist = load(os.path.join(MEM, "history.json"), {"events": [], "daily": []})
    events = []
    models, read = {}, {}
    if bf:
        bev, last = backfill(bf)
        events += bev
        for v, mdl in last.items():
            if mdl and not os.path.exists(os.path.join(MEM, "meta-%s.json.gz" % v)):
                save(os.path.join(MEM, "meta-%s.json.gz" % v), mdl, gz=True)
    for ver, url in META.items():
        try:
            mdl = parse(get(url, timeout=180))
            read[ver] = {"ok": True, "at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), **counts(mdl)}
        except Exception as e:
            log("metadata not read", ver, e)
            mdl = load(os.path.join(MEM, "meta-%s.json.gz" % ver), None)
            read[ver] = {"ok": False, "note": str(e)[:200], **(counts(mdl) if mdl else {})}
            if not mdl:
                continue
        prev = load(os.path.join(MEM, "meta-%s.json.gz" % ver), None)
        if prev and read[ver].get("ok"):
            events += diff(prev, mdl, ver, day, "live $metadata")
        if read[ver].get("ok"):
            save(os.path.join(MEM, "meta-%s.json.gz" % ver), mdl, gz=True)
        models[ver] = mdl
    beta = models.get("beta")
    if not beta:
        log("no beta model - nothing written")
        return 1
    # promoted: new in v1.0 and already in beta
    for e in events:
        if e["ver"] == "v1.0" and e["kind"] in ("type-new", "prop-new", "op-new", "nav-new"):
            t = beta["types"].get(e["type"]) or {}
            if e["kind"] == "type-new" and e["type"] in beta["types"] or e["kind"] in ("prop-new", "nav-new") and e["name"] in all_props(beta, e["type"]):
                e["promoted"] = 1
    # tenant
    tstate = load(os.path.join(MEM, "tenant.json"), {"first": {}})
    GP.update(graph_perms())
    tres, tnote = (None, "skipped (--no-tenant)") if no_tenant else tenant_read(beta, day)
    und = undocumented(tres, beta) if tres else []
    if tres:
        first = tstate.setdefault("first", {})
        baseline = not first
        for u in und:
            k = u["type"] + "|" + u["prop"]
            if k not in first:
                first[k] = day
                if not baseline:
                    events.append({"day": day, "ver": "beta", "via": "our developer tenant", "kind": "tenant-undocumented", "type": u["type"],
                                   "name": u["prop"], "detail": "returned by the service, not in $metadata (" + u["kind"] + ")", "path": u["path"]})
        for r in tres:
            for key in (r.get("props") or {}):
                first.setdefault("seen|" + key, day)
        tstate["read"] = day
        tstate["endpoints"] = [{k: r.get(k) for k in ("label", "path", "perm", "status", "n", "note")} for r in tres]
        save(os.path.join(MEM, "tenant.json"), tstate)
    # enrich: path, permissions, command, MC
    pidx = path_index(beta)
    gp = graph_perms()
    mci = mc_index()
    KTY = {"boolean": "Edm.Boolean", "number": "Edm.Int32", "string": "Edm.String", "array": "Collection(x)", "object": "x"}
    for e in events:
        tn = e.get("type") or ""
        prop = e.get("name") if e.get("kind") in ("prop-new", "prop-type", "tenant-undocumented") else ""
        path = e.get("path")
        if not path:
            t = beta["types"].get(tn) or {}
            if t.get("k") == "C":
                own = owner_entity(beta, tn)
                if own:
                    path = best_path(pidx.get(own[0]), gp)
                    e["holder"] = own[0] + "." + own[1]
            else:
                path = best_path(pidx.get(tn), gp)
        if path:
            e["path"] = path
        simple = prop and "." not in prop and "[]" not in prop
        ty = all_props(beta, tn).get(prop, "") if simple else ""
        if e.get("kind") == "tenant-undocumented":
            ty = KTY.get((e.get("detail") or "").split("(")[-1].rstrip(")"), "")
        # a PATCH body only when the property sits directly on the entity at that path
        direct = simple and (beta["types"].get(tn) or {}).get("k") != "C"
        e["cmd"] = command(path, tn, prop if direct else "", ty, beta, gp, "v1.0" if e.get("ver") == "v1.0" else "beta") if path else None
        e["mc"] = mc_match(mci, prop or e.get("name") or "")
    for u in und:   # the undocumented list carries its own command
        prop = u["prop"].split(".")[-1].replace("[]", "")
        ty = {"boolean": "Edm.Boolean", "number": "Edm.Int32", "string": "Edm.String", "array": "Collection(x)", "object": "x"}.get(u["kind"], "")
        val = sample(ty, beta) if ty else "<value>"
        sk = skeleton(u.get("shape"))      # 5fy: the shape our tenant returns beats a placeholder
        if sk is not None and u["kind"] == "object":
            val = sk
        m1 = re.match(r"^(\w+)\[\]\.(\w+)$", u["prop"])
        root_t = resolve_path(beta, u["path"])
        if m1 and m1.group(1) in all_navs(beta, root_t):
            # an item of a navigation collection (authenticationMethodConfigurations[]): the item has its own URL
            p2 = u["path"] + "/" + m1.group(1) + "/{id}"
            u["cmd"] = command(p2, u["type"], "", "", beta, gp)
            u["cmd"]["patch"], u["cmd"]["body"] = u["cmd"]["get"], {"@odata.type": "#microsoft.graph." + u["type"], m1.group(2): val}
            u["cmd"]["permPatch"] = perms_for(gp, p2, "PATCH") or perms_for(gp, u["path"], "PATCH")
            u["itemPath"] = p2
        elif "[]" not in u["prop"] and "." in u["prop"]:
            # a property of a nested object: PATCH the root object with the nested shape
            body = {}
            cur = body
            segs = u["prop"].split(".")
            for sg in segs[:-1]:
                cur[sg] = {}
                cur = cur[sg]
            cur[segs[-1]] = val
            u["cmd"] = command(u["path"], root_t, "", "", beta, gp)
            if u["cmd"]:
                u["cmd"]["patch"], u["cmd"]["body"] = u["cmd"]["get"], dict({"@odata.type": "#microsoft.graph." + root_t}, **body)
                item_patch(u, beta, gp)
        elif "[]" not in u["prop"]:
            u["cmd"] = command(u["path"], u["type"] if u["typeDocumented"] else root_t, prop, ty, beta, gp)
            if u["cmd"] and u["cmd"].get("body") and sk is not None and u["kind"] == "object":
                u["cmd"]["body"][prop] = val
            if u["cmd"] and u["cmd"].get("patch"):
                item_patch(u, beta, gp)
        else:
            u["cmd"] = command(u["path"], root_t, "", "", beta, gp)   # deeper in a list: GET only
        u["mc"] = mc_match(mci, prop)
        u["first"] = (tstate.get("first") or {}).get(u["type"] + "|" + u["prop"], day)
    # 5ft: technology, documentation status, notes, articles (owner, 30 X 2026)
    if und:
        enrich_findings(und, beta, models.get("v1.0"), day)
    # 5ft-c (owner, 30 X 2026: "every finding should have its dates - found, updated"): per finding the day it was first
    # returned, the last day it was returned, the day its documentation status last changed, and a short log (status
    # moved, new sources); a finding the tenant stops returning is listed as gone with that day
    gone_out = []
    if und and tres:
        life = tstate.setdefault("life", {})
        cur = set()
        for u in und:
            k = u["type"] + "|" + u["prop"]
            cur.add(k)
            L = life.setdefault(k, {"first": u["first"], "status": u.get("status"), "statusDay": u["first"], "log": []})
            L.pop("gone", None)
            if L.get("status") != u.get("status"):
                L["log"].append({"day": day, "what": "documentation: %s -> %s" % (L.get("status"), u.get("status"))})
                L["status"], L["statusDay"] = u.get("status"), day
            na = len((u.get("note") or {}).get("articles") or []) + len(u.get("auto") or []) + len(u.get("mc") or [])
            if L.get("sources") is not None and na > L["sources"]:
                L["log"].append({"day": day, "what": "%d new source%s" % (na - L["sources"], "" if na - L["sources"] == 1 else "s")})
            L["sources"], L["last"] = na, day
            L["log"] = L["log"][-10:]
            u["last"], u["statusDay"], u["log"] = day, L["statusDay"], L["log"]
            u["updated"] = max([L["first"]] + [x["day"] for x in L["log"]])
        for k, L in life.items():
            if k not in cur:
                L.setdefault("gone", day)
                gone_out.append({"key": k, "first": L.get("first"), "last": L.get("last"), "gone": L["gone"]})
        save(os.path.join(MEM, "tenant.json"), tstate)
    order = {"new": 0, "learn": 1, "v1": 2}
    und.sort(key=lambda u: (u.get("first") or "") , reverse=True)
    und.sort(key=lambda u: (order.get(u.get("status"), 3), u.get("cat") or ""))   # stable: newest first inside a status and technology
    for e in events:
        e["cat"] = category(e.get("path"), e.get("holder"), e.get("type"))
    # history
    seen = {(x["day"], x["ver"], x["kind"], x["type"], x["name"]) for x in hist["events"]}
    for e in events:
        k = (e["day"], e["ver"], e["kind"], e["type"], e["name"])
        if k not in seen:
            hist["events"].append(e); seen.add(k)
    cut = (datetime.date.fromisoformat(day) - datetime.timedelta(days=KEEP_DAYS)).isoformat()
    hist["events"] = sorted([e for e in hist["events"] if e["day"] >= cut], key=lambda e: e["day"], reverse=True)
    hist["daily"] = [d for d in hist.get("daily", []) if d["day"] != day] + [{"day": day, "beta": read.get("beta", {}).get("properties"), "v1": read.get("v1.0", {}).get("properties"),
                                                                              "undoc": len(und)}]
    hist["daily"] = hist["daily"][-400:]
    save(os.path.join(MEM, "history.json"), hist)
    for e in hist["events"]:   # 5ft: events recorded before the technology existed
        if not e.get("cat"):
            e["cat"] = category(e.get("path"), e.get("holder"), e.get("type"))
    pn = []
    for x in und + hist["events"][:1500]:
        c = x.get("cmd") or {}
        pn += (c.get("permGet") or []) + (c.get("permPatch") or [])
    by = {}
    for e in hist["events"]:
        b = by.setdefault(e["day"], {"day": e["day"], "beta": 0, "v1.0": 0, "tenant": 0})
        b["tenant" if e["kind"].startswith("tenant") else e["ver"]] += 1
    out = {"generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "day": day, "spec": "5ft",
           "read": read, "tenant": {"read": bool(tres), "note": tnote, "endpoints": tstate.get("endpoints") if tres else [],
                                    "undocumented": und[:300], "day": tstate.get("read"), "gone": gone_out[-60:]},
           "events": hist["events"][:1500], "perDay": sorted(by.values(), key=lambda x: x["day"]), "daily": hist["daily"][-120:],
           "learnLicensing": learn_licensing()[0], "learnState": learn_licensing()[1],
           "perms": perm_info(pn), "cats": CAT_INFO,
           "sources": {"metadata": META, "syncs": "https://github.com/microsoftgraph/msgraph-metadata/commits/master/schemas"}}
    save(OUT, out)
    log("beta", read.get("beta"), "v1.0", read.get("v1.0"))
    log("events now", len(events), "kept", len(hist["events"]), "undocumented in tenant", len(und), tnote)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
