---
layout: Conceptual
title: Call an Azure service as a user with ASP.NET Core - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/aspnet-core-call-azure-api-as-user
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Use an agent identity and the on-behalf-of flow to call an Azure service for the signed-in user.
ms.topic: how-to
ms.date: 2026-11-05T00:00:00.0000000Z
ai-usage: ai-assisted
ms.reviewer: dastrock, jomondi
locale: en-us
document_id: d3a16f8e-8ed8-06eb-2af9-5e3d94dbadb5
document_version_independent_id: d3a16f8e-8ed8-06eb-2af9-5e3d94dbadb5
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/aspnet-core-call-azure-api-as-user.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/aspnet-core-call-azure-api-as-user
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/aspnet-core-call-azure-api-as-user.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d452572f-6212-498f-9050-ca4a9e50a425
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/a12e40b7-59a2-4437-96e2-166ce622b864
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 473020da-f103-6a67-74e4-1668a39b2c88
---

# Call an Azure service as a user with ASP.NET Core - Microsoft Entra Agent ID | Microsoft Learn

Use the OAuth On-Behalf-Of (OBO) flow when an upstream client calls an agent API for a signed-in user and the agent calls an Azure service for that user.

The agent API validates the access token from the upstream client. Microsoft.Identity.Web then uses ordinary confidential-client OBO to acquire an Azure access token for the signed-in user. The user's Azure role assignments determine which resources the downstream call can access.

## Prerequisites

- Complete [Authenticate users to an ASP.NET Core agent API](aspnet-core-authenticate-users).
- A credential on the agent identity blueprint. For local testing, use the [registered certificate and local credential configuration](call-api-custom#configure-a-local-development-credential). Use a managed identity federated credential in production.
- [User or administrator consent](grant-agent-access-microsoft-365) for the agent identity to use the Azure service's delegated scope.
- An Azure RBAC role assigned to the signed-in user at the required scope.

## Install the packages

```dotnetcli
dotnet add package Microsoft.Identity.Web
```

## Configure the blueprint credential

Use the same `AzureAd` section that validates incoming tokens, and add the blueprint credential:

The managed identity example requires an Azure host with that identity assigned and federation configured. On a workstation, use the local certificate configuration from the prerequisites instead; signing in to Azure CLI doesn't make the managed identity configuration work locally.

```json
{
  "AzureAd": {
    "Instance": "https://login.microsoftonline.com/",
    "TenantId": "<tenant-id>",
    "ClientId": "<agent-client-id>",
    "ClientCredentials": [
      {
        "SourceType": "SignedAssertionFromManagedIdentity",
        "ManagedIdentityClientId": "<managed-identity-client-id>"
      }
    ]
  }
}
```

Warning

Client secrets shouldn't be used as client credentials in production environments for agent identity blueprints due to security risks. Instead, use more secure authentication methods such as [federated identity credentials (FIC) with managed identities](/en-us/entra/workload-id/workload-identity-federation-config-app-trust-managed-identity) or client certificates. These methods provide enhanced security by eliminating the need to store sensitive secrets directly within your application configuration.

## Configure token validation and OBO

Replace the agent API's `Program.cs` from the authentication walkthrough with the following block, followed by the endpoint in **Call Azure Resource Manager**. Don't append a second application builder or `app.Run()`. This sample uses an in-memory token cache.

```csharp
using System.Net.Http.Headers;
using Microsoft.Identity.Abstractions;
using Microsoft.Identity.Web;
using Microsoft.Identity.Web.Resource;

var builder = WebApplication.CreateBuilder(args);

builder.Services
    .AddMicrosoftIdentityWebApiAuthentication(builder.Configuration)
    .EnableTokenAcquisitionToCallDownstreamApi()
    .AddInMemoryTokenCaches();

builder.Services.AddHttpClient();
builder.Services.AddAuthorization();

var app = builder.Build();

app.UseAuthentication();
app.UseAuthorization();
```

## Call Azure Resource Manager

Use `CreateAuthorizationHeaderForUserAsync` with the authenticated `HttpContext.User`. The provider uses the agent's configured client ID and blueprint credential.

The following endpoint enforces the agent API's `access_agent` scope, requests a delegated Azure Resource Manager token, and lists the subscriptions visible to the user:

```csharp
app.MapGet("/azure-subscriptions", async (
    HttpContext context,
    IAuthorizationHeaderProvider authorizationHeaderProvider,
    IHttpClientFactory httpClientFactory) =>
{
    context.VerifyUserHasAnyAcceptedScope("access_agent");

    string authorizationHeader = await authorizationHeaderProvider
        .CreateAuthorizationHeaderForUserAsync(
            ["https://management.azure.com/user_impersonation"],
            claimsPrincipal: context.User);

    HttpClient client = httpClientFactory.CreateClient();
    client.DefaultRequestHeaders.Authorization =
        AuthenticationHeaderValue.Parse(authorizationHeader);

    using HttpResponseMessage response = await client.GetAsync(
        "https://management.azure.com/subscriptions?api-version=2022-12-01");
    response.EnsureSuccessStatusCode();

    return Results.Content(
        await response.Content.ReadAsStringAsync(),
        "application/json");
})
.RequireAuthorization();

app.Run();
```

The returned authorization header includes the `Bearer` scheme. Send it only to the intended Azure service, and don't return or log it.

For another Azure service, use the delegated scope, endpoint, and Azure RBAC role documented by that service.

## Verify the Azure call

1. Start the agent API with `dotnet run --urls https://localhost:5001` in the environment where its configured credential is available.
2. In the [local test client](aspnet-core-authenticate-users#run-the-test-client), change the request URL to `https://localhost:5001/azure-subscriptions`. Keep the requested scope as `api://<agent-client-id>/access_agent`, not the Azure Resource Manager scope.
3. Run the client and sign in as the user covered by both consent grants. Expect `HTTP 200` and a JSON subscription list. An empty list can be valid when the user has no visible subscriptions; compare it with the user's expected Azure access.
4. Call the agent endpoint without a token and confirm `401 Unauthorized`.

If token acquisition reports missing consent, check the agent identity's delegated Azure permission. If the Azure call is denied or expected subscriptions are absent, check the signed-in user's Azure RBAC assignments separately. The sample's `EnsureSuccessStatusCode` throws for a downstream failure; it doesn't forward that status to the client. Record correlation IDs and request times, not tokens.

Stop the API and test client when you're done. Follow the steps to [clean up the local agent authentication test](aspnet-core-authenticate-users#clean-up-the-local-test), and remove only test-specific grants or Azure role assignments you created.