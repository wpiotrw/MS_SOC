---
layout: Conceptual
title: Call Microsoft Graph as an agent with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/sidecar-call-graph-as-agent
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Use an app-only Agent ID token from the Auth SDK sidecar to call Microsoft Graph.
ms.topic: how-to
ms.date: 2026-11-06T00:00:00.0000000Z
ai-usage: ai-assisted
ms.reviewer: dastrock
locale: en-us
document_id: 06cea926-9db7-b41c-0f1f-935fa0ff9872
document_version_independent_id: 06cea926-9db7-b41c-0f1f-935fa0ff9872
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/sidecar-call-graph-as-agent.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/sidecar-call-graph-as-agent
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/sidecar-call-graph-as-agent.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: d1f7399c-1c61-e7c1-73cc-9cc7385d9010
---

# Call Microsoft Graph as an agent with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn

Use application permissions when an autonomous agent calls Microsoft Graph without a signed-in user.

## Prerequisites

- Completion of [Configure the Auth SDK sidecar](microsoft-entra-sdk-for-agent-identities), including the agent's registration and client ID.
- Administrator consent for the Microsoft Graph application permission `Organization.Read.All` on the Agent ID.

## Configure access

1. [Grant the Microsoft Graph application permission `Organization.Read.All`](grant-application-permissions-agent-identity) to the Agent ID and have an administrator consent to it.
2. Configure a sidecar API, such as `graph-app`, with the Microsoft Graph base URL and `https://graph.microsoft.com/.default` scope.

Application permissions can provide broad tenant access. Grant only the permissions required by the scenario.

## Configure the sidecar

Add an app-only profile for Microsoft Graph with the configured client ID:

```json
{
  "DownstreamApis": {
    "graph-app": {
      "BaseUrl": "https://graph.microsoft.com/v1.0/",
      "Scopes": [
        "https://graph.microsoft.com/.default"
      ],
      "RequestAppToken": true
    }
  }
}
```

For the blueprint identity, credential, and container configuration, see [Configure the Auth SDK sidecar](microsoft-entra-sdk-for-agent-identities).

## Read the organization with Microsoft Graph

This example uses Node.js 18 or later and the built-in Fetch API. Run it from the agent; don't pass a user token or identity override.

The sidecar request uses the configured app-only profile:

```http
GET /AuthorizationHeaderUnauthenticated/graph-app
```

```javascript
async function getOrganizationAsAgent() {
  const tokenResponse = await fetch("http://localhost:5000/AuthorizationHeaderUnauthenticated/graph-app");
  if (!tokenResponse.ok) {
    throw new Error(`Sidecar token request failed (HTTP ${tokenResponse.status}); check the profile, credential, and admin consent.`);
  }
  const { authorizationHeader } = await tokenResponse.json();

  const response = await fetch("https://graph.microsoft.com/v1.0/organization?$select=id,displayName", {
    headers: { Authorization: authorizationHeader }
  });
  if (!response.ok) {
    throw new Error(`Microsoft Graph returned HTTP ${response.status}; verify Organization.Read.All is consented for the Agent ID.`);
  }
  return response.json();
}
```

Call `getOrganizationAsAgent()` from the agent. A successful request returns `200 OK` and one organization object containing its ID and display name. If Graph returns `403`, verify that `Organization.Read.All` is granted to the Agent ID and admin consent is current; then retry. If the sidecar returns `401`, check token acquisition and the `graph-app` profile. Don't log the authorization header. See the [List organizations API](/en-us/graph/api/organization-list) for its application permission requirements.