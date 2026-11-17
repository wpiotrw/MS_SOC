---
layout: Conceptual
title: Call Microsoft Graph as a user with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/sidecar-call-graph-as-user
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Use the Auth SDK sidecar and On-Behalf-Of flow to call Microsoft Graph with delegated permissions.
ms.topic: how-to
ms.date: 2026-11-06T00:00:00.0000000Z
ai-usage: ai-assisted
ms.reviewer: dastrock
locale: en-us
document_id: d6a43b33-98d5-1a3f-c409-d5937bacbb04
document_version_independent_id: d6a43b33-98d5-1a3f-c409-d5937bacbb04
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/sidecar-call-graph-as-user.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/sidecar-call-graph-as-user
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/sidecar-call-graph-as-user.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 63cb8b1d-f51f-61ac-ef90-920309e2dbea
---

# Call Microsoft Graph as a user with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn

Use delegated Microsoft Graph permissions when an operation should run with the signed-in user's access.

## Prerequisites

- Completion of [Authenticate users with the Auth SDK sidecar](sidecar-authenticate-users), including consent for the upstream client to call the agent.
- Consent for the Microsoft Graph delegated permissions required by the operation.

## Configure access

1. Declare the Microsoft Graph delegated permission `User.Read` on the blueprint.
2. [Obtain user or administrator consent](grant-agent-access-microsoft-365) for `User.Read` on the agent identity.
3. Configure a sidecar API, such as `graph`, with the Microsoft Graph base URL and delegated scopes.

Request only the scopes required by the operation.

## Configure the sidecar

Add a delegated profile for Microsoft Graph:

```json
{
  "DownstreamApis": {
    "graph": {
      "BaseUrl": "https://graph.microsoft.com/v1.0/",
      "Scopes": [
        "User.Read"
      ]
    }
  }
}
```

Replace `User.Read` with the delegated Microsoft Graph permissions required by the operation. Use the shared client ID and keep identity overrides disabled as described in [Configure the Auth SDK sidecar](microsoft-entra-sdk-for-agent-identities).

## Read the signed-in user's profile

This example uses Node.js 18 or later and the built-in Fetch API. Pass the access token issued to the signed-in user for your agent API to the function. `User.Read` is the least-privileged delegated permission for this request.

The sidecar request uses the configured delegated profile and the inbound user token:

```http
GET /AuthorizationHeader/graph
Authorization: Bearer <agent-api-access-token>
```

```javascript
async function getMyGraphProfile(agentApiAccessToken) {
  const tokenResponse = await fetch("http://localhost:5000/AuthorizationHeader/graph", {
    headers: { Authorization: `Bearer ${agentApiAccessToken}` }
  });
  if (!tokenResponse.ok) {
    throw new Error(`Sidecar token request failed (HTTP ${tokenResponse.status}); check the inbound user token and User.Read consent.`);
  }
  const { authorizationHeader } = await tokenResponse.json();

  const response = await fetch("https://graph.microsoft.com/v1.0/me?$select=id,displayName", {
    headers: { Authorization: authorizationHeader }
  });
  if (!response.ok) {
    throw new Error(`Microsoft Graph returned HTTP ${response.status}; verify User.Read consent and the signed-in user's access.`);
  }
  return response.json();
}
```

Call `getMyGraphProfile(agentApiAccessToken)` while handling that user's request. A successful request returns `200 OK` with that user's ID and display name. If Graph returns `403`, verify that `User.Read` is consented and the access token represents the expected signed-in user; then retry. If the sidecar returns `401`, check that the inbound token is an access token for the agent API and that delegated consent is in place. After changing consent, retry with a newly issued agent API access token. Don't replace this flow with an app-only token or `/AuthorizationHeaderUnauthenticated`; Microsoft Graph doesn't support application permissions for `/me`. See the [Get a user API](/en-us/graph/api/user-get) for the delegated permission requirement.