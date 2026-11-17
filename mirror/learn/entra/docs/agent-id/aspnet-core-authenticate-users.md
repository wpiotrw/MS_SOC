---
layout: Conceptual
title: Authenticate users to an ASP.NET Core agent API - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/aspnet-core-authenticate-users
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Configure an ASP.NET Core agent API to validate access tokens obtained by an upstream client for signed-in users.
ms.topic: how-to
ms.date: 2026-11-06T00:00:00.0000000Z
ai-usage: ai-assisted
ms.reviewer: dastrock, jomondi
locale: en-us
document_id: 3d696d24-4179-c78f-0527-c3004bd00907
document_version_independent_id: 3d696d24-4179-c78f-0527-c3004bd00907
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/aspnet-core-authenticate-users.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/aspnet-core-authenticate-users
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/aspnet-core-authenticate-users.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d452572f-6212-498f-9050-ca4a9e50a425
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/a12e40b7-59a2-4437-96e2-166ce622b864
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 5e95080a-c97c-23b7-6ba7-2f7158632ce5
---

# Authenticate users to an ASP.NET Core agent API - Microsoft Entra Agent ID | Microsoft Learn

An upstream client signs in the user and sends an access token to your agent API. This article configures the ASP.NET Core agent API to validate that token and shows a local test client that signs in a user and calls `/whoami`.

Authentication establishes the caller's identity. [Control user access to agents](control-user-access-agents) separately determines whether that identity can invoke the agent.

## Prerequisites

- Completion of [Create an identity for your agent](create-single-instance-agent), including the tenant enablement and administrator handoff. Record the shared client ID and the agent identity's object ID.
- The [.NET 10 SDK](/en-us/dotnet/core/install/). The examples use Microsoft.Identity.Web 4.17.0.
- An upstream client application that can sign in users and request an access token for the agent API, or permission to register the local test client.
- For the preview consent step, the [management client](create-single-instance-agent#set-up-the-management-client) with administrator consent for the additional delegated Graph permission `DelegatedPermissionGrant.ReadWrite.All`. Use an administrator authorized to consent to these delegated permissions. Choose the least privileged supported role from [Grant tenant-wide admin consent](../identity/enterprise-apps/grant-admin-consent), and confirm any additional preview consent requirements with your Microsoft representative.
- A trusted local HTTPS development certificate for local testing. Run `dotnet dev-certs https --trust` and approve the trust prompt on your development machine. Don't disable certificate verification.

## Register a local test client

Skip this section if you already have a client that signs in users and calls your agent. This test client is a separate, ordinary app registration, not another agent identity.

1. [Register a single-tenant application](../identity-platform/quickstart-register-app) named **Agent API test client** in the agent's tenant.
2. Under **Authentication**, add the **Mobile and desktop applications** platform with redirect URI `http://localhost`. No client secret is needed.
3. Record its **Application (client) ID**. Under **Enterprise applications**, find the corresponding application and record its **Object ID**. Token requests use the client ID; consent grants use the enterprise application's object ID.

The client uses a browser and PKCE. The loopback redirect receives the authorization response locally; API calls still use HTTPS.

## Configure the delegated permission

The upstream client needs a delegated permission to call the agent API for the signed-in user.

1. On the blueprint, [expose an identifier URI and delegated scope](create-blueprint#configure-identifier-uri-and-scope). Use `access_agent` as the scope value for this walkthrough. Preserve existing scopes and set `api.requestedAccessTokenVersion` to `2`.
2. Declare that scope in the upstream client's `requiredResourceAccess`. Use the shared agent client ID as `resourceAppId` and the exposed scope's GUID with `"type": "Scope"`.
3. Grant the upstream client access for the test user as described in the next section. During preview, browser consent doesn't support an agent identity as the resource.

For more information, see [Configure a client application to access a web API](../identity-platform/quickstart-configure-app-access-web-apis) and [Permissions and consent in the Microsoft identity platform](../identity-platform/permissions-consent-overview).

Configure the upstream client by following the authentication flow for that client type. For example, see the [OAuth 2.0 authorization code flow](../identity-platform/v2-oauth2-auth-code-flow). Request the fully qualified agent API scope:

```text
api://<agent-client-id>/access_agent
```

Use an authentication library in the upstream client. Don't send ID tokens or authorization codes to the agent API.

## Grant the upstream client access

Use the management client for these Microsoft Graph requests, not the agent's runtime credential. This grant authorizes the upstream client to call the agent; it doesn't grant the agent access to downstream APIs.

Before running the requests, open the **management app's** registration in the Microsoft Entra admin center. Under **API permissions**, select **Add a permission** &gt; **Microsoft Graph** &gt; **Delegated permissions**, add `DelegatedPermissionGrant.ReadWrite.All`, and have an authorized administrator grant consent. Keep the two management permissions from provisioning. Don't add these permissions to the agent or the test client.

Reconnect with all three consented scopes:

```powershell
Disconnect-MgGraph
Connect-MgGraph -ClientId "<management-app-client-id>" `
    -TenantId "<tenant-id>" `
    -Scopes "AgentIdentityBlueprint.ReadWrite.All", "AgentIdentity.ReadWrite.All", "DelegatedPermissionGrant.ReadWrite.All" `
    -ContextScope Process
```

Use `Invoke-MgGraphRequest` as shown in [Set up the management client](create-single-instance-agent#set-up-the-management-client).

1. Check for an existing applicable grant:

    ```http
    GET https://graph.microsoft.com/v1.0/oauth2PermissionGrants?$filter=clientId eq '<upstream-client-service-principal-object-id>' and resourceId eq '<agent-identity-object-id>'
    ```

    Follow pagination. An applicable tenant-wide grant or a grant for the test user might already include `access_agent`.
2. If no applicable grant exists, grant access for the one user who will sign in:

    ```http
    POST https://graph.microsoft.com/v1.0/oauth2PermissionGrants
    Content-Type: application/json
    
    {
      "clientId": "<upstream-client-service-principal-object-id>",
      "resourceId": "<agent-identity-object-id>",
      "consentType": "Principal",
      "principalId": "<user-object-id>",
      "scope": "access_agent"
    }
    ```

    `clientId` and `resourceId` are service principal **object IDs**, not OAuth client IDs. If a grant already exists for that user but lacks the scope, [update the OAuth2 permission grant scope](/en-us/graph/api/oauth2permissiongrant-update) with the union of existing and required scopes. Don't create a duplicate or remove unrelated scopes.
3. Record the grant's `id` for cleanup. Sign in as that user when you run the test client. Don't force a new consent prompt against the agent resource.

## Configure token validation

Create the agent API project if you don't already have one:

```dotnetcli
dotnet new webapi --framework net10.0 --name AgentApi
cd AgentApi
```

Install `Microsoft.Identity.Web` from the project directory:

```dotnetcli
dotnet add package Microsoft.Identity.Web --version 4.17.0
```

Configure the agent API in `appsettings.json`:

```json
{
  "AzureAd": {
    "Instance": "https://login.microsoftonline.com/",
    "TenantId": "<tenant-id>",
    "ClientId": "<agent-client-id>"
  }
}
```

Replace the project's `Program.cs` with the following code. It requires the `access_agent` scope before returning the caller's validated identity:

```csharp
using System.Security.Claims;
using Microsoft.Identity.Web;
using Microsoft.Identity.Web.Resource;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddMicrosoftIdentityWebApiAuthentication(
    builder.Configuration);
builder.Services.AddAuthorization();

var app = builder.Build();

app.UseAuthentication();
app.UseAuthorization();

app.MapGet("/whoami", (HttpContext context) =>
{
    context.VerifyUserHasAnyAcceptedScope("access_agent");

    ClaimsPrincipal user = context.User;
    string? objectId = user.GetObjectId();
    string? tenantId = user.GetTenantId();

    return Results.Ok(new { objectId, tenantId });
})
.RequireAuthorization();

app.Run();
```

`AddMicrosoftIdentityWebApiAuthentication` validates the token signature, issuer, audience, and lifetime. Authorization policies can then evaluate scopes, app roles, and other claims.

`VerifyUserHasAnyAcceptedScope` rejects a valid token that doesn't contain the `access_agent` delegated permission.

Use `GetObjectId()` and `GetTenantId()` to read the stable identity. These helpers handle both the original JWT claim names and the claim names mapped by the authentication middleware.

## Understand the request path

1. The upstream client signs in the user.
2. The client obtains an access token for `access_agent`.
3. The client sends `Authorization: Bearer <token>` to the agent API.
4. The ASP.NET Core authentication middleware validates the token.
5. The agent API applies its authorization policy.

## Run the test client

Start the agent API:

```dotnetcli
dotnet run --urls https://localhost:5001
```

In another terminal, create a console project outside the agent API directory:

```dotnetcli
dotnet new console --framework net10.0 --name AgentTestClient
cd AgentTestClient
dotnet add package Microsoft.Identity.Client
```

Replace the console project's `Program.cs` with this code. Substitute the tenant ID, test client's client ID, and agent's shared client ID:

```csharp
using System.Net.Http.Headers;
using Microsoft.Identity.Client;

var client = PublicClientApplicationBuilder.Create("<upstream-client-id>")
    .WithAuthority("https://login.microsoftonline.com/<tenant-id>")
    .WithRedirectUri("http://localhost")
    .Build();

var result = await client
    .AcquireTokenInteractive(["api://<agent-client-id>/access_agent"])
    .ExecuteAsync();

using var http = new HttpClient();
http.DefaultRequestHeaders.Authorization =
    new AuthenticationHeaderValue("Bearer", result.AccessToken);
using var response = await http.GetAsync("https://localhost:5001/whoami");
Console.WriteLine($"HTTP {(int)response.StatusCode}");
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());
```

Run `dotnet run` and sign in as the user named in the consent grant. Expect `HTTP 200` and that user's object ID and tenant ID. A request to `/whoami` without a token must return `401`. Don't log the token or use an ID token in its place.

If your API exposes another delegated scope and your test client has consent for it, also request a token for that scope alone and call `/whoami`. Confirm that the token has the agent API's audience but lacks `access_agent`, and that the request is rejected. This optional scope-negative test requires a second scope; the minimal local setup defines only `access_agent`. A token for a different audience tests audience validation, not scope authorization.

If sign-in fails, check the test client's redirect URI and the per-user grant before changing the agent's configuration. If HTTPS fails, fix the development certificate's trust rather than bypassing validation.

## Clean up the local test

Stop both projects when you're done. Keep the test client and agent registration if you continue to the next task. When you no longer need a test grant, delete it with `DELETE https://graph.microsoft.com/v1.0/oauth2PermissionGrants/<grant-id>` through the management client, before deleting its client app registration. Don't delete shared clients or grants used by other users.