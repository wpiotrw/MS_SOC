#!/usr/bin/env python3
"""fpa_tenant.py - read-only tenant snapshot for the First-party apps tab (CLAUDE.md Sec.5bl, README.md).

Runs in GitHub Actions (.github/workflows/fpa-tenant.yml). Signs in as the Entra app
"MS-SOC First-party apps reader" with a federated credential - the GitHub OIDC token is the
client assertion, so there is no secret anywhere. Needs, admin-consented, two read-only
application permissions: Application.Read.All (service principals and their app role
assignments) and DelegatedPermissionGrant.Read.All (delegated permission grants). Microsoft's
docs list Directory.Read.All as the least privileged for GET /oauth2PermissionGrants; the
narrower DelegatedPermissionGrant.Read.All exists as a Graph app role ("Read all delegated
permission grants") - if Graph refuses it (403), the snapshot keeps the app roles and records
`grantsNote` instead of failing. Writes site/data/fpa-tenant.json:

  {read, tenant, spTotal, spMicrosoft, clients:[{n, appId, owner, microsoft, grants:{API: scopes}, roles:[API: role]}]}

A client is any service principal NOT owned by this tenant that holds a delegated grant
(oauth2PermissionGrants) or an application permission (appRoleAssignments) here.
Env: AZURE_TENANT_ID, AZURE_CLIENT_ID, ACTIONS_ID_TOKEN_REQUEST_URL/_TOKEN (set by GitHub)."""
import json, os, sys, urllib.error, urllib.parse, urllib.request, datetime

MS = {"f8cdef31-a31e-4b4a-93e4-5f571e91255a", "72f988bf-86f1-41af-91ab-2d7cd011db47",
      "cdc5aeea-15c5-4db6-b079-fcadd2505dc2", "33e01921-4d64-4f8c-a055-5bdaffd5e33d",
      "975f013f-7f24-47e8-a7d3-abc4752bf346"}


def http(url, data=None, headers=None):
    req = urllib.request.Request(url, data=data, headers=headers or {})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def token():
    tid, cid = os.environ["AZURE_TENANT_ID"], os.environ["AZURE_CLIENT_ID"]
    oidc = http(os.environ["ACTIONS_ID_TOKEN_REQUEST_URL"] + "&audience=api://AzureADTokenExchange",
                headers={"Authorization": "bearer " + os.environ["ACTIONS_ID_TOKEN_REQUEST_TOKEN"]})["value"]
    body = urllib.parse.urlencode({
        "client_id": cid, "scope": "https://graph.microsoft.com/.default", "grant_type": "client_credentials",
        "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        "client_assertion": oidc}).encode()
    return tid, http("https://login.microsoftonline.com/%s/oauth2/v2.0/token" % tid, body,
                     {"Content-Type": "application/x-www-form-urlencoded"})["access_token"]


def pages(tok, url):
    out = []
    while url:
        d = http(url, headers={"Authorization": "Bearer " + tok})
        out += d.get("value") or []
        url = d.get("@odata.nextLink")
    return out


def main(out_path):
    tid, tok = token()
    G = "https://graph.microsoft.com/v1.0"
    sps = pages(tok, G + "/servicePrincipals?$top=999&$select=id,appId,displayName,appOwnerOrganizationId")
    by_id = {s["id"]: s for s in sps}
    grants, grants_note = [], None
    try:
        grants = pages(tok, G + "/oauth2PermissionGrants?$top=999")
    except urllib.error.HTTPError as ex:
        grants_note = "GET /oauth2PermissionGrants refused (%s) - DelegatedPermissionGrant.Read.All not enough or not consented" % ex.code
    clients = {}
    def client(spid):
        s = by_id.get(spid) or {}
        own = (s.get("appOwnerOrganizationId") or "").lower()
        if not s or own == tid.lower():
            return None
        return clients.setdefault(spid, {"n": s.get("displayName"), "appId": s.get("appId"), "owner": own,
                                         "microsoft": own in MS, "grants": {}, "roles": []})
    for g in grants:
        c = client(g.get("clientId"))
        if c is None:
            continue
        res = (by_id.get(g.get("resourceId")) or {}).get("displayName") or g.get("resourceId")
        scopes = " ".join(sorted(set((c["grants"].get(res, "") + " " + (g.get("scope") or "")).split())))
        c["grants"][res] = scopes
    role_names = {}
    for s in sps:
        own = (s.get("appOwnerOrganizationId") or "").lower()
        if own == tid.lower():
            continue
        for a in pages(tok, G + "/servicePrincipals/%s/appRoleAssignments?$top=999" % s["id"]):
            rid = a.get("resourceId")
            if rid not in role_names:
                r = http(G + "/servicePrincipals/%s?$select=displayName,appRoles" % rid, headers={"Authorization": "Bearer " + tok})
                role_names[rid] = (r.get("displayName"), {x["id"]: x.get("value") for x in r.get("appRoles") or []})
            c = client(s["id"])
            if c is not None:
                rn, roles = role_names[rid]
                c["roles"].append("%s: %s" % (rn, roles.get(a.get("appRoleId"), a.get("appRoleId"))))
    out = {"read": datetime.date.today().isoformat(), "tenant": tid, "spTotal": len(sps),
           "spMicrosoft": sum(1 for s in sps if (s.get("appOwnerOrganizationId") or "").lower() in MS),
           "grantsNote": grants_note,
           "clients": sorted([dict(c, roles=sorted(set(c["roles"]))) for c in clients.values()], key=lambda c: c["n"] or "")}
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    json.dump(out, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("OK %s: %d service principals, %d from Microsoft tenants, %d clients with grants or app roles"
          % (out_path, out["spTotal"], out["spMicrosoft"], len(out["clients"])))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "site/data/fpa-tenant.json")
