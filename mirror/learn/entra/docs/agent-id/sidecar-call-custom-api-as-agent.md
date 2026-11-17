---
layout: Conceptual
title: Call a custom API as an agent with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/sidecar-call-custom-api-as-agent
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Use an app-only Agent ID token from the Auth SDK sidecar to call a custom protected API.
ms.topic: how-to
ms.date: 2026-11-06T00:00:00.0000000Z
ai-usage: ai-assisted
ms.reviewer: dastrock
locale: en-us
document_id: 7a4f6fcc-0ad9-b05c-5577-80e1853d6167
document_version_independent_id: 7a4f6fcc-0ad9-b05c-5577-80e1853d6167
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/sidecar-call-custom-api-as-agent.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/sidecar-call-custom-api-as-agent
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/sidecar-call-custom-api-as-agent.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
platformId: c16b059a-0282-7ce7-dadf-9b56d05645f2
---

# Call a custom API as an agent with the Auth SDK sidecar - Microsoft Entra Agent ID | Microsoft Learn

Use app-only access when a cloud agent performs scheduled, event-driven, or other autonomous work without a signed-in user. This article calls a custom API, but the same sidecar flow applies to Azure services and Microsoft Graph.

In this article, you configure application permissions and use the sidecar to acquire an app-only authorization header or call the API.

## Prerequisites

- Completion of [Configure the Auth SDK sidecar](microsoft-entra-sdk-for-agent-identities), including the agent's registration, client ID, and credential.
- An application permission exposed by the custom API.

## Configure access

1. Expose an application permission on the custom API.
2. [Grant that permission to the Agent ID and verify administrator consent](call-api-custom#grant-application-permissions). Use the shared client ID for consent and the agent identity's object ID when verifying the app role assignment.
3. Configure the API in the sidecar with its base URL and `api://<api-client-id>/.default` scope.
4. Configure the API to validate the Agent ID token and required app role.

## Configure the sidecar

The agent calls the sidecar through loopback in their shared network namespace. The sidecar uses the configured client ID and credential to acquire an authorization header for the API.

Add an app-only profile for the custom API. Keep identity overrides disabled as described in the sidecar setup:

```json
{
  "DownstreamApis": {
    "custom-api": {
      "BaseUrl": "https://api.contoso.com/",
      "Scopes": [
        "api://<custom-api-client-id>/.default"
      ],
      "RequestAppToken": true
    }
  }
}
```

For the blueprint identity, credential, and container configuration, see [Configure the Auth SDK sidecar](microsoft-entra-sdk-for-agent-identities).

## Get a token and call the API

```http
GET /AuthorizationHeaderUnauthenticated/custom-api
```

Send the returned `authorizationHeader` to the custom API. Don't pass an `AgentIdentity` override or send the blueprint credential to the API.

The API must verify the token's signature, issuer, audience, expiry, Agent ID claims, and required `roles` value.

Alternatively, use `POST /DownstreamApiUnauthenticated/custom-api` to have the sidecar call the configured API. No identity override is needed.

Confirm that the API operation succeeds with the required role and rejects a request without that role. A successful token response alone doesn't establish API authorization. Don't log the authorization header.