---
layout: Conceptual
title: Call APIs as an agent's user account in a fleet with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/sidecar-fleet-call-apis-as-agent-user
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Select the agent identity and agent's user account for each token request to the Auth SDK sidecar in a shared runtime that hosts many agents.
ms.topic: how-to
ms.date: 2026-11-04T00:00:00.0000000Z
ms.reviewer: dastrock
ai-usage: ai-assisted
locale: en-us
document_id: e73b1cef-adad-ae91-7b61-e1104f287111
document_version_independent_id: e73b1cef-adad-ae91-7b61-e1104f287111
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/sidecar-fleet-call-apis-as-agent-user.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/sidecar-fleet-call-apis-as-agent-user
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/sidecar-fleet-call-apis-as-agent-user.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: ecb4124b-e743-a7b0-2c6d-ef5b812eb9df
---

# Call APIs as an agent's user account in a fleet with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn

Some agents in a fleet need a user object for Microsoft 365 workloads, such as a mailbox or Teams membership. For those agents, look up both the agent identity and its agent's user account in the agent directory, and pass them in the `AgentIdentity` and `AgentUserId` parameters.

To decide whether an agent needs an agent's user account, see [Use an agent's user account with Microsoft 365](agent-user-oauth-flow#determine-whether-the-agent-needs-a-user-object).

## Prerequisites

- Complete [Call APIs as an agent in a fleet with the Auth SDK sidecar](sidecar-fleet-call-apis-as-agent).
- An agent's user account [provisioned for the agent](sidecar-fleet-provision-agent-identities#provision-an-agent).
- Delegated permissions for the target API, such as `Mail.ReadWrite`, [granted to the agent identity](grant-agent-access-microsoft-365) or [inherited from the blueprint](set-up-blueprint-agent-fleet#optionally-configure-inheritable-permissions).
- The Microsoft 365 licenses and resource access that the agent's user account needs. For details, see [Configure the account](sidecar-call-microsoft-365-as-agent-user#configure-the-account).

## Configure the sidecar

Add a delegated Microsoft Graph profile to the runtime sidecar:

```json
{
  "DownstreamApis": {
    "MsGraph": {
      "BaseUrl": "https://graph.microsoft.com/v1.0/",
      "Scopes": [
        "Mail.ReadWrite"
      ]
    }
  }
}
```

Replace `Mail.ReadWrite` with the delegated permissions the agents need. The `GetAuthorizationHeaderUnauthenticated` override from the previous article also covers the `AgentUserId` parameter.

## Get a token for an agent's user account

# [Python](#tab/python)
```python
def authorization_header_for_agent_user(agent_id: str, api_name: str) -> str:
    registration = directory.find(agent_id)
    if registration is None or not registration["agent_user_id"]:
        raise LookupError(f"Agent '{agent_id}' doesn't have an agent's user account.")

    response = requests.get(
        f"{SIDECAR_URL}/AuthorizationHeaderUnauthenticated/{api_name}",
        params={
            "AgentIdentity": registration["agent_identity_id"],
            "AgentUserId": registration["agent_user_id"],
        },
        timeout=5,
    )
    response.raise_for_status()
    return response.json()["authorizationHeader"]

graph_response = requests.get(
    "https://graph.microsoft.com/v1.0/me/messages",
    headers={"Authorization": authorization_header_for_agent_user(agent_id, "MsGraph")},
    timeout=10,
)
graph_response.raise_for_status()
```

# [JavaScript](#tab/javascript)
```javascript
async function authorizationHeaderForAgentUser(agentId, apiName) {
    const registration = await directory.find(agentId);
    if (!registration?.agentUserId) {
        throw new Error(`Agent '${agentId}' doesn't have an agent's user account.`);
    }

    const params = new URLSearchParams({
        AgentIdentity: registration.agentIdentityId,
        AgentUserId: registration.agentUserId,
    });
    const response = await fetch(
        `${SIDECAR_URL}/AuthorizationHeaderUnauthenticated/${apiName}?${params}`
    );
    if (!response.ok) {
        throw new Error(`Sidecar request failed with status ${response.status}.`);
    }
    const { authorizationHeader } = await response.json();
    return authorizationHeader;
}

const graphResponse = await fetch("https://graph.microsoft.com/v1.0/me/messages", {
    headers: { Authorization: await authorizationHeaderForAgentUser(agentId, "MsGraph") },
});
```

---

The token represents the agent's user account, so `/me` returns that account's data. Each agent can reach only the mailbox, files, and teams that its own account was given.