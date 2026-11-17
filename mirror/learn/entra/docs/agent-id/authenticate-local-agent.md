---
layout: Conceptual
title: Sign in users from a local agent - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/authenticate-local-agent
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Configure a local agent as an OAuth public client and sign in users with authorization code flow and PKCE.
ms.topic: how-to
ms.date: 2026-11-05T00:00:00.0000000Z
ms.reviewer: dastrock
ai-usage: ai-assisted
locale: en-us
document_id: 2f2595d0-33e0-0325-45a2-6ee5e2c464f4
document_version_independent_id: 2f2595d0-33e0-0325-45a2-6ee5e2c464f4
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/authenticate-local-agent.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/authenticate-local-agent
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/authenticate-local-agent.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
platformId: 9f3f53a7-0257-4d98-016a-e2d5e9eea3e5
---

# Sign in users from a local agent - Microsoft Entra Agent ID | Microsoft Learn

A local agent runs on an endpoint device and can't securely store a client secret or certificate. Configure it as an OAuth public client and use authorization code flow with Proof Key for Code Exchange (PKCE).

The user signs in through a browser. The agent receives an authorization code at its registered redirect URI and redeems the code without a client credential.

Important

Local agent authentication is in preview. This preview is provided without a service-level agreement and isn't recommended for production workloads. Some features might be unsupported or have constrained capabilities. For more information, see [Universal License Terms for Online Services](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/all).

## Prerequisites

You need a Microsoft Entra tenant where you can register an Agent ID, or a tenant that supports Client ID Metadata Documents (CIMD).

## Choose a client ID

| Option | Client ID | Use when |
| --- | --- | --- |
| Register an Agent ID in Microsoft Entra | Client ID assigned by Microsoft Entra | Recommended when you know the agent connects to Microsoft Entra. |
| Use a CIMD | Public HTTPS URL of the client's metadata document | Use when the same distributed client connects to independently operated authorization servers and preregistration isn't practical. |

Prefer a registered Agent ID when possible. For more information about CIMD, see [Client ID Metadata Documents in Microsoft Entra ID](client-id-metadata-documents#when-to-use-cimd).

## Register the Agent ID

1. [Create a single-instance blueprint and provision its Agent ID](create-single-instance-agent). Choose the instance mode when you create the blueprint; you can't change it afterward.
2. Add the redirect URI recommended by your authentication library under the blueprint's `publicClient` platform.
3. Record the Agent ID's client ID and tenant ID.

Every installation uses the same client ID. Don't create a separate Agent ID for each device, and don't add a client secret, certificate, or federated identity credential for this flow.

For redirect URI options, see [Desktop app that calls web APIs: Code configuration](/en-us/entra/identity-platform/scenario-desktop-app-configuration).

## Sign in with MSAL.NET

Install MSAL.NET:

```dotnetcli
dotnet add package Microsoft.Identity.Client
```

Create a public-client application:

```csharp
using Microsoft.Identity.Client;

var app = PublicClientApplicationBuilder
    .Create("<agent-client-id>")
    .WithAuthority("https://login.microsoftonline.com/<tenant-id>")
    .WithDefaultRedirectUri()
    .Build();
```

Sign in the user without requesting delegated permissions for an API:

```csharp
var result = await app
    .AcquireTokenInteractive(Array.Empty<string>())
    .ExecuteAsync();

Console.WriteLine($"Signed in as {result.Account.Username}");
```

`AcquireTokenInteractive` doesn't have a parameterless overload. Pass an empty scope collection when the agent only needs to sign in the user. MSAL adds the reserved OpenID Connect scopes required for sign-in, but it doesn't request a delegated scope for an API.

MSAL opens the system browser, uses PKCE, validates the response, and caches the account. Use a tenant-specific authority for a registered Agent ID. Don't use the account name or ID token to authorize access to an API. Request the API's delegated scopes in the next step.

## Use a CIMD client for delegated API access (preview)

Use the CIMD URL as the client ID in an OAuth library that supports URL-valued client IDs. The library must use authorization code flow with PKCE and must not send a client credential when it redeems the code.

CIMD doesn't support ID tokens for user sign-in. This branch uses browser authentication to obtain delegated API access, not the sign-in-only MSAL.NET result shown earlier. Request the resource's delegated scopes by following the CIMD configuration procedure.

For metadata and redirect URI requirements, see [Configure a client with a Client ID Metadata Document](configure-client-id-metadata-document).