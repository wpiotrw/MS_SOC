#!/usr/bin/env python3
"""fpa_compare.py - how far our own tenant could carry the First-party apps list (CLAUDE.md 5cw, decision aid).

Owner, 9 X 2026: "first check what is in our tenant and how it differs from Merill's list - how much we would
have to fill in - and then decide which solution is better". Runs in .github/workflows/fpa-compare.yml with the
same read-only sign-in as fpa_tenant.py. Prints COUNTS ONLY - the log of a public repository is public, so no
application id or name from the tenant is printed or written anywhere.
"""
import json, os, sys, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fpa_tenant as T

MERILL = "https://raw.githubusercontent.com/merill/microsoft-info/main/_info/MicrosoftApps.json"


def main():
    tid, tok = T.token()
    sps = T.pages(tok, "https://graph.microsoft.com/v1.0/servicePrincipals?$top=999&$select=appId,displayName,appOwnerOrganizationId,servicePrincipalType")
    ms = {s["appId"].lower(): s for s in sps if (s.get("appOwnerOrganizationId") or "").lower() in T.MS and s.get("appId")}
    m = json.loads(urllib.request.urlopen(urllib.request.Request(MERILL, headers={"User-Agent": "MS_SOC"}), timeout=60).read())
    mer = {}
    for x in m:
        a = str(x.get("AppId") or "").lower()
        if a:
            mer.setdefault(a, set()).add(str(x.get("Source") or "?"))
    # Microsoft's own list, the one Merill takes 82 % of his file from: entra-docs .docutune known-guids.json
    kg = json.loads(urllib.request.urlopen(urllib.request.Request(
        "https://raw.githubusercontent.com/MicrosoftDocs/entra-docs/main/.docutune/dictionaries/known-guids.json",
        headers={"User-Agent": "MS_SOC"}), timeout=60).read())
    kgi = set()
    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                for x in (k, v):
                    if isinstance(x, str) and len(x) == 36 and x.count("-") == 4:
                        kgi.add(x.lower())
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(kg)
    own = set(ms) | kgi
    merill_only = set(mer) - own
    mo_src = {}
    for a in merill_only:
        for s_ in mer[a]:
            mo_src[s_] = mo_src.get(s_, 0) + 1
    both = set(ms) & set(mer)
    only_t = set(ms) - set(mer)
    only_m = set(mer) - set(ms)
    by_src = {}
    for a in mer:
        for s in mer[a]:
            by_src[s] = by_src.get(s, 0) + 1
    by_src_t = {}
    for a in both:
        for s in mer[a]:
            by_src_t[s] = by_src_t.get(s, 0) + 1
    out = {"tenantServicePrincipals": len(sps), "tenantMicrosoftOwned": len(ms),
           "merillDistinctAppIds": len(mer), "merillBySource": by_src,
           "inBoth": len(both), "inBothByMerillSource": by_src_t,
           "tenantMicrosoftNotInMerill": len(only_t),
           "tenantMicrosoftNotInMerillWithName": sum(1 for a in only_t if (ms[a].get("displayName") or "").strip()),
           "merillNotInTenant": len(only_m),
           "shareOfMerillCoveredByTenant": round(100.0 * len(both) / max(1, len(mer)), 1),
           "knownGuidsMicrosoft": len(kgi), "ownBaselineTenantPlusKnownGuids": len(own),
           "merillOnlyNotInOwnBaseline": len(merill_only), "merillOnlyBySource": mo_src,
           "ownBaselineNotInMerill": len(own - set(mer)),
           "shareOfMerillCoveredByOwnBaseline": round(100.0 * len(set(mer) & own) / max(1, len(mer)), 1)}
    print(json.dumps(out, indent=1))
    print("::notice title=fpa-compare::" + json.dumps(out))   # readable through the check-run annotations API


if __name__ == "__main__":
    main()
