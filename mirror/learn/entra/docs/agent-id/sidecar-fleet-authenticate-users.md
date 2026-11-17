---
layout: Conceptual
title: Authenticate users and route requests to agents in a fleet with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/sidecar-fleet-authenticate-users
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Validate user access tokens with the Auth SDK sidecar, route each request to an agent in a shared runtime, and enforce per-agent access.
ms.topic: how-to
ms.date: 2026-11-05T00:00:00.0000000Z
ms.reviewer: dastrock
ai-usage: ai-assisted
locale: en-us
document_id: 97e95ce3-571b-e26f-693d-4ab6a9f9f0ed
document_version_independent_id: 97e95ce3-571b-e26f-693d-4ab6a9f9f0ed
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/sidecar-fleet-authenticate-users.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/sidecar-fleet-authenticate-users
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/sidecar-fleet-authenticate-users.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: d37c572f-2296-6d4a-bf11-0a4f68533bc8
---

# Authenticate users and route requests to agents in a fleet with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn

Users call a fleet agent with an access token for the blueprint's `access_agent` scope. Every agent in the fleet shares that audience, so token validation proves who the user is but not which agent they're allowed to use. The runtime routes each request to an agent and enforces per-agent access itself.

## Prerequisites

- Complete [Call APIs as an agent in a fleet with the Auth SDK sidecar](sidecar-fleet-call-apis-as-agent).
- The `access_agent` scope [exposed on the blueprint](set-up-blueprint-agent-fleet#expose-the-inbound-scope).
- An upstream client that signs in users and requests the scope `api://<agent-identity-blueprint-client-id>/access_agent`.

## Configure token validation

Token validation is the same as for a single agent. Configure the sidecar with the blueprint client ID and the `access_agent` scope, and validate each inbound token with `GET /Validate`. For details, see [Authenticate users with the Auth SDK sidecar](sidecar-authenticate-users). Keep the fleet's per-request identity overrides from the preceding articles and the shared network namespace for local sidecar requests; don't replace them with the single-instance defaults.

To limit which users can call the fleet at all, [require an app role assignment](sidecar-control-user-access-agents) on the blueprint principal. Those app roles apply to every agent in the fleet.

## Enforce per-agent access

Decide who can use each agent, and store that decision in the runtime. For example, record the users and groups that an agent's owner shares it with. Identify the user by the validated `tid` and `oid` claims. Don't use the user principal name or email as a stable key.

## Route requests to agents

Put the runtime's agent ID in the route. Validate the token, confirm the agent exists, and check the access policy before running the agent. The following examples assume an `access_policy` object that implements the runtime's per-agent access check.

# [Python](#tab/python)
```python
import requests

SIDECAR_URL = "http://localhost:5000"

class AgentNotFound(Exception):
    """Return 404 Not Found to the caller."""

def authorize_agent_request(inbound_auth_header: str, agent_id: str) -> dict:
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
    object_id = claims.get("oid")
    tenant_id = claims.get("tid")
    if (
        result.get("protocol", "").lower() != "bearer"
        or not object_id
        or not tenant_id
    ):
        raise PermissionError("The token isn't a validated user bearer token.")

    scopes = claims.get("scp", "").split()
    if "access_agent" not in scopes:
        raise PermissionError("The token doesn't contain the access_agent scope.")

    if directory.find(agent_id) is None or not access_policy.can_use_agent(
        tenant_id, object_id, agent_id
    ):
        raise AgentNotFound(agent_id)

    return claims

# For a request to POST /agents/{agent_id}/messages:
claims = authorize_agent_request(request.headers.get("Authorization"), agent_id)
```

# [JavaScript](#tab/javascript)
```javascript
const SIDECAR_URL = "http://localhost:5000";

class AgentNotFoundError extends Error {}

async function authorizeAgentRequest(inboundAuthHeader, agentId) {
    const response = await fetch(`${SIDECAR_URL}/Validate`, {
        headers: { Authorization: inboundAuthHeader },
    });
    if (response.status === 401 || response.status === 403) {
        throw new Error("The sidecar rejected the caller's access token.");
    }
    if (!response.ok) {
        throw new Error(`Sidecar validation failed with status ${response.status}.`);
    }

    const { protocol, claims = {} } = await response.json();
    const objectId = claims.oid;
    const tenantId = claims.tid;
    if (protocol?.toLowerCase() !== "bearer" || !objectId || !tenantId) {
        throw new Error("The token isn't a validated user bearer token.");
    }

    const scopes = (claims.scp ?? "").split(" ");
    if (!scopes.includes("access_agent")) {
        throw new Error("The token doesn't contain the access_agent scope.");
    }

    if (!(await directory.find(agentId))
        || !(await accessPolicy.canUseAgent(tenantId, objectId, agentId))) {
        throw new AgentNotFoundError(agentId);
    }

    return claims;
}

// For a request to POST /agents/:agentId/messages:
const claims = await authorizeAgentRequest(req.headers.authorization, req.params.agentId);
```

---

Return `401 Unauthorized` when the token is missing or invalid. Return `404 Not Found` both for an unknown agent and for an agent the user can't use, so callers can't discover other agents in the fleet. After these checks pass, use the same agent ID for every token request made while handling the request.