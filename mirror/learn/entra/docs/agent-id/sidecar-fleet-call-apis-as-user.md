---
layout: Conceptual
title: Call APIs as a user in a fleet with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/sidecar-fleet-call-apis-as-user
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Use the On-Behalf-Of flow with the routed agent's identity to call APIs for a signed-in user through the Auth SDK sidecar in a shared runtime.
ms.topic: how-to
ms.date: 2026-11-05T00:00:00.0000000Z
ms.reviewer: dastrock
ai-usage: ai-assisted
locale: en-us
document_id: e6f1bd20-2371-3133-a850-ffb837251235
document_version_independent_id: e6f1bd20-2371-3133-a850-ffb837251235
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/sidecar-fleet-call-apis-as-user.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/sidecar-fleet-call-apis-as-user
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/sidecar-fleet-call-apis-as-user.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: a62dd188-1224-22e5-6d91-3d20fc0631a7
---

# Call APIs as a user in a fleet with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn

After the runtime routes a user's request to an agent, the agent can call APIs for that user with the On-Behalf-Of (OBO) flow. Forward the user's token to the sidecar, and pass the routed agent's identity in the `AgentIdentity` parameter. The downstream token represents both the signed-in user and that agent.

## Prerequisites

- Complete [Authenticate users and route requests to agents in a fleet with the Auth SDK sidecar](sidecar-fleet-authenticate-users).
- Delegated permissions for the target API, [granted to the agent identity](grant-agent-access-microsoft-365) or [inherited from the blueprint](set-up-blueprint-agent-fleet#optionally-configure-inheritable-permissions).

## Configure the sidecar

Add a delegated profile for each API to the runtime sidecar:

```json
{
  "Sidecar": {
    "AllowOverrides": {
      "GetAuthorizationHeader": true
    }
  },
  "DownstreamApis": {
    "custom-api-user": {
      "BaseUrl": "https://api.contoso.com/",
      "Scopes": [
        "api://<custom-api-client-id>/<delegated-scope>"
      ]
    }
  }
}
```

Explicitly enable `GetAuthorizationHeader` as shown, even if you previously disabled overrides by following the single-instance setup. Otherwise the sidecar ignores `AgentIdentity`. Only trusted runtime code should select and send identity overrides.

## Get a token for the signed-in user

After routing the request and confirming the user can access the agent, call the sidecar:

# [Python](#tab/python)
```python
def authorization_header_for_user(
    inbound_auth_header: str, agent_id: str, api_name: str
) -> str:
    registration = directory.find(agent_id)

    response = requests.get(
        f"{SIDECAR_URL}/AuthorizationHeader/{api_name}",
        params={"AgentIdentity": registration["agent_identity_id"]},
        headers={"Authorization": inbound_auth_header},
        timeout=5,
    )
    if response.status_code in (401, 403):
        raise PermissionError("The sidecar rejected the user token or OBO request.")
    response.raise_for_status()
    return response.json()["authorizationHeader"]

inbound_auth_header = request.headers.get("Authorization")
authorize_agent_request(inbound_auth_header, agent_id)

api_response = requests.get(
    "https://api.contoso.com/user-data",
    headers={
        "Authorization": authorization_header_for_user(
            inbound_auth_header, agent_id, "custom-api-user"
        )
    },
    timeout=10,
)
api_response.raise_for_status()
```

# [JavaScript](#tab/javascript)
```javascript
async function authorizationHeaderForUser(inboundAuthHeader, agentId, apiName) {
    const registration = await directory.find(agentId);

    const params = new URLSearchParams({
        AgentIdentity: registration.agentIdentityId,
    });
    const response = await fetch(
        `${SIDECAR_URL}/AuthorizationHeader/${apiName}?${params}`,
        { headers: { Authorization: inboundAuthHeader } }
    );
    if (response.status === 401 || response.status === 403) {
        throw new Error("The sidecar rejected the user token or OBO request.");
    }
    if (!response.ok) {
        throw new Error(`Sidecar request failed with status ${response.status}.`);
    }
    const { authorizationHeader } = await response.json();
    return authorizationHeader;
}

const inboundAuthHeader = req.headers.authorization;
await authorizeAgentRequest(inboundAuthHeader, req.params.agentId);

const apiResponse = await fetch("https://api.contoso.com/user-data", {
    headers: {
        Authorization: await authorizationHeaderForUser(
            inboundAuthHeader, req.params.agentId, "custom-api-user"
        ),
    },
});
```

---

Always use the agent ID that passed the access check. If the runtime used a different agent's identity, the downstream API would see the wrong agent acting for the user. Don't send the inbound token directly to the downstream API, and don't log either authorization header.

## Call specific resources

Use the scopes and endpoints from the linked resource articles, while keeping the fleet's blueprint client ID and override settings. The single-instance requests omit `AgentIdentity`. For each fleet resource request, call `authorization_header_for_user` or `authorizationHeaderForUser` to supply the routed agent identity and inbound user token.

| Resource | Guidance |
| --- | --- |
| Custom API | [Call a custom API as a user](sidecar-call-custom-api-as-user) |
| Azure services | [Call Azure services as a user](sidecar-call-azure-api-as-user) |
| Microsoft Graph | [Call Microsoft Graph as a user](sidecar-call-graph-as-user) |