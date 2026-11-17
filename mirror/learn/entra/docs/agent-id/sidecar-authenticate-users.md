---
layout: Conceptual
title: Authenticate users with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/sidecar-authenticate-users
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Validate an access token sent by an upstream client and read the signed-in user's claims with the Auth SDK sidecar.
ms.topic: how-to
ms.date: 2026-11-06T00:00:00.0000000Z
ai-usage: ai-assisted
ms.reviewer: dastrock
locale: en-us
document_id: 4b23042d-214c-588c-481c-9599d2f41073
document_version_independent_id: 4b23042d-214c-588c-481c-9599d2f41073
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/sidecar-authenticate-users.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/sidecar-authenticate-users
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/sidecar-authenticate-users.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 5185b4c5-0e3a-59ba-4a8e-f3a767c7ccd7
---

# Authenticate users with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn

An upstream client signs in the user and sends an access token to the agent. The agent passes that token to the sidecar for validation before it uses the user's claims or performs an On-Behalf-Of (OBO) exchange.

The sidecar doesn't provide the user interface for sign-in. Use MSAL in the upstream web, desktop, or mobile client.

## Prerequisites

- Completion of [Configure the Auth SDK sidecar](microsoft-entra-sdk-for-agent-identities), including the agent's registration and credential.
- An upstream client that signs in a user and requests a token for the agent's exposed scope.
- Completion of [Configure the delegated permission](aspnet-core-authenticate-users#configure-the-delegated-permission) and [Grant the upstream client access](aspnet-core-authenticate-users#grant-the-upstream-client-access). These registration and Microsoft Graph consent steps also apply to the sidecar; don't use the ASP.NET Core code from that article.

## Configure the audience

Register a scope exposed by the agent's API. The upstream client requests that scope so the resulting access token is intended for the agent.

Don't send a token issued for Microsoft Graph or another resource to the agent API.

Configure the sidecar to validate the agent API's audience and delegated scope:

Set `AzureAd:ClientId` to the client ID recorded during setup, not a directory object ID. Set `AzureAd:Scopes` to `access_agent`. The upstream client requests `api://<agent-client-id>/access_agent`.

```json
{
  "AzureAd": {
    "Instance": "https://login.microsoftonline.com/",
    "TenantId": "<tenant-id>",
    "ClientId": "<agent-client-id>",
    "Scopes": "access_agent"
  }
}
```

Use the same `AzureAd` section to configure the blueprint credential. For the complete container and credential setup, see [Configure the Auth SDK sidecar](microsoft-entra-sdk-for-agent-identities).

## Validate the token

Forward the complete inbound authorization header to the sidecar:

```http
GET /Validate
Authorization: ******
```

The response includes the validated protocol, token, and claims. Use the claims to identify the user and enforce the agent's authorization policy.

Don't trust claims decoded by the client or agent before validation.

## Invoke the sidecar

Validate the inbound authorization header with the sidecar before using its returned claims. Require `protocol` to be `Bearer`, nonempty `oid` and `tid` claims, and `access_agent` in the space-separated `scp` claim. Identify the caller by the combination of `tid` and `oid`. Reject the request if any check fails, and apply the agent's authorization policy before processing it.

# [Python](#tab/python)
```python
import requests

SIDECAR_URL = "http://localhost:5000"

def validate_caller(inbound_auth_header: str) -> dict:
    """Validate an inbound access token with the sidecar and return the token claims."""
    response = requests.get(
        f"{SIDECAR_URL}/Validate",
        headers={"Authorization": inbound_auth_header},
        timeout=5,
    )

    if response.status_code in (401, 403):
        raise PermissionError("The sidecar rejected the caller's access token.")

    response.raise_for_status()
    result = response.json()

    if result.get("protocol", "").lower() != "bearer":
        raise PermissionError("The validated token used an unexpected protocol.")

    claims = result.get("claims", {})
    object_id = claims.get("oid")
    tenant_id = claims.get("tid")

    if not object_id or not tenant_id:
        raise PermissionError("The validated token doesn't identify a user and tenant.")

    if "access_agent" not in claims.get("scp", "").split():
        raise PermissionError("The caller doesn't have the required delegated scope.")

    return claims

# Call before processing each request:
claims = validate_caller(request.headers.get("Authorization"))
# Use claims["oid"] and claims["tid"] as the stable caller identity.
# Apply the agent's authorization policy before processing the request.
```

# [JavaScript](#tab/javascript)
```javascript
const SIDECAR_URL = "http://localhost:5000";

async function validateCaller(inboundAuthHeader) {
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

    if (result.protocol?.toLowerCase() !== "bearer") {
        throw new Error("The validated token used an unexpected protocol.");
    }

    const claims = result.claims ?? {};
    const { oid: objectId, tid: tenantId } = claims;

    if (!objectId || !tenantId) {
        throw new Error("The validated token doesn't identify a user and tenant.");
    }

    if (!(claims.scp ?? "").split(" ").includes("access_agent")) {
        throw new Error("The caller doesn't have the required delegated scope.");
    }

    return claims;
}

// Call before processing each request:
const claims = await validateCaller(req.headers.authorization);
// Use claims.oid and claims.tid as the stable caller identity.
// Apply the agent's authorization policy before processing the request.
```

---

Keep `SIDECAR_URL` on loopback in the shared network namespace. Replace the authorization-header placeholder with the complete `Authorization` header received by the agent. If you use a scope other than `access_agent`, update both the sidecar configuration and the helper's scope check.

The response also contains the validated token, but the example doesn't deserialize it. Don't return or log the token. If the sidecar rejects the token, reject the agent request instead of decoding the token locally or continuing without an authenticated user.

Return `401 Unauthorized` for a missing or invalid token and `403 Forbidden` when an authenticated caller lacks the required scope or access. Don't continue to the downstream API after either rejection.

The example also rejects credentials that the sidecar validated with another protocol, such as an app-only proof-of-possession token. Use the validated tenant ID and object ID as the stable user key. Apply the agent's authorization policy before processing the request.