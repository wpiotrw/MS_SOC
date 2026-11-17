---
layout: Conceptual
title: Call Azure services as an agent with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/sidecar-call-azure-api-as-agent
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Use an app-only Agent ID token from the Auth SDK sidecar to call an Azure service.
ms.topic: how-to
ms.date: 2026-11-06T00:00:00.0000000Z
ai-usage: ai-assisted
ms.reviewer: dastrock
locale: en-us
document_id: 3dfb70e6-a093-76fa-ec9f-5f5e7460a99d
document_version_independent_id: 3dfb70e6-a093-76fa-ec9f-5f5e7460a99d
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/sidecar-call-azure-api-as-agent.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/sidecar-call-azure-api-as-agent
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/sidecar-call-azure-api-as-agent.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/4e834929-0ce1-4c1d-9c81-fcb14721edfb
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/75670257-a3f0-4627-9981-8046f99219e6
platformId: 5bb92e80-61b4-e502-e18e-4f7ffc5778df
---

# Call Azure services as an agent with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn

Use this pattern when an autonomous agent needs access to an Azure service that accepts Microsoft Entra application tokens.

## Prerequisites

- Completion of [Configure the Auth SDK sidecar](microsoft-entra-sdk-for-agent-identities), including the agent's registration and client ID.
- A resource group and subscription where an administrator can assign the Agent ID an Azure role.

## Configure access

1. Assign the Azure built-in **Reader** role to the Agent ID at the target resource group scope.
2. Configure the Azure service in the sidecar with its resource scope. For Azure Resource Manager, use `https://management.azure.com/.default`.
3. Record the sidecar API configuration name.

For this example, Azure Resource Manager uses Azure RBAC: the Agent ID's **Reader** assignment authorizes the read. The `/.default` scope requests an app-only token for Azure Resource Manager; it isn't an Azure role or an additional OAuth permission grant.

## Configure the sidecar

The following profile requests app-only tokens for Azure Resource Manager with the configured client ID:

```json
{
  "DownstreamApis": {
    "azure-management": {
      "BaseUrl": "https://management.azure.com/",
      "Scopes": [
        "https://management.azure.com/.default"
      ],
      "RequestAppToken": true
    }
  }
}
```

For another Azure service, replace the base URL and scope with the values documented by that service. For the blueprint identity, credential, and container configuration, see [Configure the Auth SDK sidecar](microsoft-entra-sdk-for-agent-identities).

## Read a resource group

This example uses Node.js 18 or later and the built-in Fetch API. Run it in the agent container, which shares the sidecar's loopback network namespace. Set `subscriptionId` and `resourceGroupName` to the target resource group.

The sidecar request uses the configured app-only profile:

```http
GET /AuthorizationHeaderUnauthenticated/azure-management
```

```javascript
async function getResourceGroupAsAgent(subscriptionId, resourceGroupName) {
  const tokenResponse = await fetch("http://localhost:5000/AuthorizationHeaderUnauthenticated/azure-management");
  if (!tokenResponse.ok) {
    throw new Error(`Sidecar token request failed (HTTP ${tokenResponse.status}); check the profile and blueprint credential.`);
  }
  const { authorizationHeader } = await tokenResponse.json();

  const url = `https://management.azure.com/subscriptions/${encodeURIComponent(subscriptionId)}/resourceGroups/${encodeURIComponent(resourceGroupName)}?api-version=2021-04-01`;
  const response = await fetch(url, { headers: { Authorization: authorizationHeader } });
  if (!response.ok) {
    throw new Error(`Azure Resource Manager returned HTTP ${response.status}; verify the Agent ID's Reader role at this resource group.`);
  }
  return response.json();
}
```

Call `getResourceGroupAsAgent(subscriptionId, resourceGroupName)` from the agent. A successful request returns `200 OK` with the resource group's name, ID, and location. A `403` from Azure Resource Manager means the Agent ID lacks access at that scope; assign **Reader** to the Agent ID on this resource group and retry after the role assignment takes effect. If the sidecar returns `401`, check the credential and `azure-management` profile. Don't pass an identity override. Request a separate token for each different API audience.

The [Resource Groups - Get API](/en-us/rest/api/resources/resource-groups/get?view=rest-resources-2021-04-01&amp;preserve-view=true) documents this request and its `200 OK` response. The Azure built-in [Reader role](/en-us/azure/role-based-access-control/built-in-roles/general#reader) grants read-only access at the scope where you assign it.