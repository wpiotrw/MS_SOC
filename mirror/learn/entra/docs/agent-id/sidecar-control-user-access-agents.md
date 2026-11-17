---
layout: Conceptual
title: Control user access to agents with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/sidecar-control-user-access-agents
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Use app roles to control which users, groups, and applications can access an agent that uses the Auth SDK sidecar.
ms.topic: how-to
ms.date: 2026-11-06T00:00:00.0000000Z
ai-usage: ai-assisted
ms.reviewer: dastrock
locale: en-us
document_id: e128283f-c483-2243-a91c-9b891f1975cf
document_version_independent_id: e128283f-c483-2243-a91c-9b891f1975cf
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/sidecar-control-user-access-agents.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/sidecar-control-user-access-agents
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/sidecar-control-user-access-agents.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: efd0aa5b-012a-633b-50da-7838da3ff24c
---

# Control user access to agents with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn

App roles define who can access an agent and what they can do. Define and assign an inbound access role, then enforce it by checking the `roles` claim returned by the sidecar. The user-access helpers in this article require the `Agent.User` role and a delegated user scope.

For the single-instance cloud journey, use the **agent identity's object ID** as `<agent-api-service-principal-object-id>` in the requests in this article; a single-instance blueprint has no blueprint principal. For the advanced fleet journey, use the fleet's **blueprint principal** instead; its assignments apply across the fleet.

## Prerequisites

- A blueprint and the service principal that represents the agent API.
- The [management permissions and administrator roles for app role configuration and assignment](control-user-access-agents#prerequisites).
- An agent that validates inbound tokens with the sidecar, as described in [Authenticate users with the Auth SDK sidecar](sidecar-authenticate-users).

## Define app roles

Use the same [role definition procedure as the ASP.NET Core agent](control-user-access-agents#define-app-roles):

- **Single-instance:** Declare `Agent.User` on the blueprint, then publish the same GUID and value directly on the Agent ID service principal, with `allowedMemberTypes` set to `["User"]`. Don't rely on a blueprint-only declaration.
- **Fleet:** Define the role on the blueprint application and use its blueprint principal for assignments.

[Verify the role on the resource principal](control-user-access-agents#verify-the-role-on-the-resource-principal) before continuing. Save its GUID for `<app-role-id>` below. Role values must stay stable because the agent checks them in the claims returned by the sidecar.

## Require an app role assignment

Set `appRoleAssignmentRequired` on the agent API service principal. When the property is `true`, Microsoft Entra ID issues an access token for the agent API only to assigned users and applications.

```http
PATCH https://graph.microsoft.com/v1.0/servicePrincipals/<agent-api-service-principal-object-id>
Content-Type: application/json
Authorization: Bearer <access-token>

{
  "appRoleAssignmentRequired": true
}
```

For more information, see the [Microsoft Graph update API reference](/en-us/graph/api/serviceprincipal-update).

## Assign an app role

Assign the app role to a user on the agent API service principal:

```http
POST https://graph.microsoft.com/v1.0/users/<user-object-id>/appRoleAssignments
Content-Type: application/json
Authorization: Bearer <access-token>

{
  "principalId": "<user-object-id>",
  "resourceId": "<agent-api-service-principal-object-id>",
  "appRoleId": "<app-role-id>"
}
```

For a group, create the assignment through the group's app role assignments. Use the agent API service principal's object ID as `resourceId`. These helpers authorize signed-in users; they don't authorize application-only callers.

## Enforce app roles with the sidecar

After the sidecar validates the inbound token, its response includes the token's claims. Check the `roles` claim before processing the request.

The following user-access helpers require the `Bearer` protocol, nonempty `oid` and `tid` claims, `access_agent` in the space-separated `scp` claim, and the required value in the `roles` array. Use `Agent.User` as the required role for this example. These helpers don't authorize app-only callers or an agent's dedicated user account.

# [Python](#tab/python)
Call the sidecar's `/Validate` endpoint and verify the required role before processing each request:

```python
import requests

SIDECAR_URL = "http://localhost:5000"

def validate_and_check_role(inbound_auth_header: str, required_role: str) -> dict:
    """Validate an inbound token and verify the caller has the required app role."""
    response = requests.get(
        f"{SIDECAR_URL}/Validate",
        headers={"Authorization": inbound_auth_header},
        timeout=5,
    )

    if response.status_code in (401, 403):
        raise PermissionError("The sidecar rejected the caller's access token.")

    response.raise_for_status()
    result = response.json()
    claims = result.get("claims", {})
    if (
        result.get("protocol", "").lower() != "bearer"
        or not claims.get("oid")
        or not claims.get("tid")
        or "access_agent" not in claims.get("scp", "").split()
    ):
        raise PermissionError("The caller isn't an authorized user of the agent API.")

    roles = claims.get("roles", [])

    if required_role not in roles:
        raise PermissionError(
            f"The caller doesn't have the required '{required_role}' role."
        )

    return claims
```

Call the helper before processing each request:

```python
claims = validate_and_check_role(
    inbound_auth_header=request.headers.get("Authorization"),
    required_role="Agent.User",
)
# Use claims["oid"] and claims["tid"] as the stable caller identity.
```

# [JavaScript](#tab/javascript)
Call the sidecar's `/Validate` endpoint and verify the required role before processing each request:

```javascript
const SIDECAR_URL = "http://localhost:5000";

async function validateAndCheckRole(inboundAuthHeader, requiredRole) {
    const response = await fetch(`${SIDECAR_URL}/Validate`, {
        headers: { Authorization: inboundAuthHeader },
    });

    if (response.status === 401 || response.status === 403) {
        throw new Error("The sidecar rejected the caller's access token.");
    }

    if (!response.ok) {
        throw new Error(`Sidecar validation failed with status ${response.status}.`);
    }

    const result = await response.json();
    const claims = result.claims ?? {};
    if (
        result.protocol?.toLowerCase() !== "bearer" ||
        !claims.oid ||
        !claims.tid ||
        !(claims.scp ?? "").split(" ").includes("access_agent")
    ) {
        throw new Error("The caller isn't an authorized user of the agent API.");
    }

    const roles = claims.roles ?? [];

    if (!roles.includes(requiredRole)) {
        throw new Error(`The caller doesn't have the required '${requiredRole}' role.`);
    }

    return claims;
}
```

Call the helper before processing each request:

```javascript
const claims = await validateAndCheckRole(
    req.headers.authorization,
    "Agent.User"
);
// Use claims.oid and claims.tid as the stable caller identity.
```

---

Return `403 Forbidden` when the role check fails. Return `401 Unauthorized` only when the token itself is missing or invalid. Request a new access token after changing an assignment. When troubleshooting, verify the assignment on the agent API service principal and check the `roles` claim in the response from `/Validate`.