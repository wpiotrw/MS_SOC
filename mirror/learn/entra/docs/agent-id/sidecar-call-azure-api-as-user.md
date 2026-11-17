---
layout: Conceptual
title: Call Azure services as a user with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/sidecar-call-azure-api-as-user
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Use the Auth SDK sidecar and On-Behalf-Of flow to call an Azure service for the signed-in user.
ms.topic: how-to
ms.date: 2026-11-06T00:00:00.0000000Z
ai-usage: ai-assisted
ms.reviewer: dastrock
locale: en-us
document_id: fbd42246-7229-e28d-1f77-fc40930161be
document_version_independent_id: fbd42246-7229-e28d-1f77-fc40930161be
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/sidecar-call-azure-api-as-user.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/sidecar-call-azure-api-as-user
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/sidecar-call-azure-api-as-user.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/4e834929-0ce1-4c1d-9c81-fcb14721edfb
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/75670257-a3f0-4627-9981-8046f99219e6
platformId: ffc5cfe7-96a9-d2d2-ef26-5dbf35ae149d
---

# Call Azure services as a user with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn

Use this pattern when an Azure service supports delegated access and should evaluate the signed-in user's permissions.

## Prerequisites

- Completion of [Authenticate users with the Auth SDK sidecar](sidecar-authenticate-users), including consent for the upstream client to call the agent.
- A target Azure resource group, and an administrator who can assign the signed-in user an Azure role on it.

## Configure access

1. Assign the signed-in user the Azure built-in **Reader** role at the target resource group scope.
2. Declare the Azure Resource Manager delegated permission `user_impersonation` on the blueprint and [grant consent to the agent identity](grant-agent-access-microsoft-365).
3. Configure the Azure Resource Manager audience and `user_impersonation` scope in the sidecar.

This example uses both authorization systems: `user_impersonation` lets the agent request an Azure Resource Manager token on behalf of the user, and the user's **Reader** role allows the read at the resource group scope. Some Azure services accept only application tokens; use [app-only access](sidecar-call-azure-api-as-agent) for those services.

## Configure the sidecar

The following profile requests delegated tokens for Azure Resource Manager:

```json
{
  "DownstreamApis": {
    "azure-management": {
      "BaseUrl": "https://management.azure.com/",
      "Scopes": [
        "https://management.azure.com/user_impersonation"
      ]
    }
  }
}
```

For another Azure service, replace the base URL and scope with the values documented by that service. Use the shared client ID and keep identity overrides disabled as described in [Configure the Auth SDK sidecar](microsoft-entra-sdk-for-agent-identities).

## Read a resource group as the signed-in user

This example uses Node.js 18 or later and the built-in Fetch API. Pass the access token issued to the signed-in user for your agent API to the function. Don't pass an ID token or an app-only token.

The sidecar request uses the configured delegated profile and the inbound user token:

```http
GET /AuthorizationHeader/azure-management
Authorization: Bearer <agent-api-access-token>
```

```javascript
async function getResourceGroupAsUser(agentApiAccessToken, subscriptionId, resourceGroupName) {
  const tokenResponse = await fetch("http://localhost:5000/AuthorizationHeader/azure-management", {
    headers: { Authorization: `Bearer ${agentApiAccessToken}` }
  });
  if (!tokenResponse.ok) {
    throw new Error(`Sidecar token request failed (HTTP ${tokenResponse.status}); check the inbound user token and delegated consent.`);
  }
  const { authorizationHeader } = await tokenResponse.json();

  const url = `https://management.azure.com/subscriptions/${encodeURIComponent(subscriptionId)}/resourceGroups/${encodeURIComponent(resourceGroupName)}?api-version=2021-04-01`;
  const response = await fetch(url, { headers: { Authorization: authorizationHeader } });
  if (!response.ok) {
    throw new Error(`Azure Resource Manager returned HTTP ${response.status}; verify the signed-in user's Reader role at this resource group.`);
  }
  return response.json();
}
```

Call `getResourceGroupAsUser(agentApiAccessToken, subscriptionId, resourceGroupName)` while handling that user's request. A successful request returns `200 OK` with the resource group's name, ID, and location. A `403` from Azure Resource Manager means the signed-in user lacks access at that scope; assign **Reader** to that user on this resource group and retry after the role assignment takes effect. If the sidecar returns `401`, verify that the inbound token is for the agent API and that `user_impersonation` consent is in place. After changing consent, retry with a newly issued agent API access token. Don't switch to the unauthenticated endpoint: it would call as the Agent ID, not as the user.

The [Resource Groups - Get API](/en-us/rest/api/resources/resource-groups/get?view=rest-resources-2021-04-01&amp;preserve-view=true) documents this request and its `200 OK` response. The Azure built-in [Reader role](/en-us/azure/role-based-access-control/built-in-roles/general#reader) grants read-only access at the scope where you assign it.