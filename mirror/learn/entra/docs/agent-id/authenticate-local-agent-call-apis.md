---
layout: Conceptual
title: Call APIs as a user from a local agent (preview) - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/authenticate-local-agent-call-apis
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Use a local agent to call a protected API for the signed-in user.
ms.topic: how-to
ms.date: 2026-11-05T00:00:00.0000000Z
ms.reviewer: dastrock
ai-usage: ai-assisted
locale: en-us
document_id: 9e32494f-35f0-2a96-eced-d74af76a4730
document_version_independent_id: 9e32494f-35f0-2a96-eced-d74af76a4730
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/authenticate-local-agent-call-apis.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/authenticate-local-agent-call-apis
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/authenticate-local-agent-call-apis.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: f781896d-598e-5833-ec34-7becd01cb1cb
---

# Call APIs as a user from a local agent (preview) - Microsoft Entra Agent ID | Microsoft Learn

After the local agent [signs in a user](authenticate-local-agent), request the delegated scopes required by the protected API. MSAL acquires an access token for the signed-in user and caches it for later calls. The API authorizes the request based on the user, the client Agent ID, and the scopes in the token.

## Prerequisites

Important

Local agent authentication is in preview. This preview is provided without a service-level agreement and isn't recommended for production workloads. Some features might be unsupported or have constrained capabilities. For more information, see [Universal License Terms for Online Services](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/all).

- Complete [Sign in users from a local agent](authenticate-local-agent). The MSAL.NET snippets here continue in the same application and reuse its public-client application variable, `app`.
- Obtain the target API's delegated scope and endpoint from its owner. Replace `<resource-client-id>`, `<delegated-scope>`, and `<resource-url>` with values for that API.
- Arrange consent with a tenant administrator if the requested permission or tenant policy requires it.

## Request the API scope

Request only the delegated scopes needed for the operation:

```csharp
var scopes = new[] { "api://<resource-client-id>/<delegated-scope>" };
```

For Microsoft Graph, use Microsoft Graph scopes such as `User.Read` or `Files.Read`.

The resource owner controls which delegated permissions are available. A user or administrator must consent before the agent can use them.

## Acquire a token

Try the MSAL cache before prompting the user again:

```csharp
AuthenticationResult result;
var account = (await app.GetAccountsAsync()).FirstOrDefault();

try
{
    result = await app.AcquireTokenSilent(scopes, account).ExecuteAsync();
}
catch (MsalUiRequiredException)
{
    result = await app.AcquireTokenInteractive(scopes).ExecuteAsync();
}
```

Don't inspect or modify the access token in the agent. Treat it as an opaque credential for the target API.

## Call the API

Send the token in the HTTP `Authorization` header:

The snippet assumes your application supplies an `HttpClient` named `httpClient`. Keep the token acquisition and API call in the same operation so the call uses the resulting `result.AccessToken`.

```csharp
using System.Net.Http.Headers;

using var request = new HttpRequestMessage(HttpMethod.Get, "<resource-url>");
request.Headers.Authorization =
    new AuthenticationHeaderValue("Bearer", result.AccessToken);

using var response = await httpClient.SendAsync(request);
response.EnsureSuccessStatusCode();
```

Request a token for each resource. A token issued for one API, such as Microsoft Graph, can't be used with another API.

Local public clients support delegated access only. They can't use client credentials to obtain app-only tokens.

Verify that the API returns its expected response for the signed-in user; successful sign-in alone doesn't prove API access. For `401 Unauthorized`, check that the token was requested for this API and that the API's validation settings match its registration. For `403 Forbidden`, check delegated consent and the user's access to the requested resource. If consent requires administrator approval, hand off the client ID, target resource, and requested scopes instead of repeatedly prompting the user.