---
layout: Conceptual
title: Call APIs as a user in a fleet with ASP.NET Core - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/aspnet-core-fleet-call-apis-as-user
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Use the On-Behalf-Of flow with the routed agent's identity to call APIs for a signed-in user from a shared ASP.NET Core runtime.
ms.topic: how-to
ms.date: 2026-11-05T00:00:00.0000000Z
ms.reviewer: dastrock
ai-usage: ai-assisted
locale: en-us
document_id: eb385835-b81a-a33f-3ac0-e5bd40b98b00
document_version_independent_id: eb385835-b81a-a33f-3ac0-e5bd40b98b00
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/aspnet-core-fleet-call-apis-as-user.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/aspnet-core-fleet-call-apis-as-user
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/aspnet-core-fleet-call-apis-as-user.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d452572f-6212-498f-9050-ca4a9e50a425
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/a12e40b7-59a2-4437-96e2-166ce622b864
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 5b32d740-0950-76c9-ad62-b82a4caf68b9
---

# Call APIs as a user in a fleet with ASP.NET Core - Microsoft Entra Agent ID | Microsoft Learn

After the runtime routes a user's request to an agent, the agent can call APIs for that user with the On-Behalf-Of (OBO) flow. Pass the routed agent's identity to `WithAgentIdentity`. The downstream token represents both the signed-in user and that agent.

## Prerequisites

- Complete [Authenticate users and route requests to agents in a fleet with ASP.NET Core](aspnet-core-fleet-authenticate-users).
- Delegated permissions for the target API, [granted to the agent identity](grant-agent-access-microsoft-365) or [inherited from the blueprint](set-up-blueprint-agent-fleet#optionally-configure-inheritable-permissions).

## Get a token for the signed-in user

Add a method to `FleetTokenService`:

```csharp
using System.Security.Claims;

public async Task<string> CreateAuthorizationHeaderForUserAsync(
    string agentId, string scope, ClaimsPrincipal user)
{
    AgentRegistration registration = await GetRegistrationAsync(agentId);

    var options = new AuthorizationHeaderProviderOptions()
        .WithAgentIdentity(registration.AgentIdentityId);

    return await authorizationHeaderProvider
        .CreateAuthorizationHeaderForUserAsync([scope], options, user);
}
```

The `user` argument is the authenticated `HttpContext.User`. *Microsoft.Identity.Web* uses the user's incoming access token as the OBO assertion.

## Call the API

Call the method after the routing and access checks from the previous article pass:

Replace the previous article's placeholder mapping for `POST /agents/{agentId}/messages` with this mapping; don't register both routes. Replace the sample API URL and delegated scope with values from the same downstream API registration.

```csharp
using System.Net.Http.Headers;
using Microsoft.Identity.Web.Resource;

app.MapPost("/agents/{agentId}/messages", async (
    string agentId,
    HttpContext context,
    IAgentDirectory directory,
    IAgentAccessPolicy accessPolicy,
    FleetTokenService fleetTokenService,
    IHttpClientFactory httpClientFactory) =>
{
    context.VerifyUserHasAnyAcceptedScope("access_agent");

    if (await directory.FindAsync(agentId) is null
        || !await accessPolicy.CanUseAgentAsync(context.User, agentId))
    {
        return Results.NotFound();
    }

    string authorizationHeader = await fleetTokenService
        .CreateAuthorizationHeaderForUserAsync(
            agentId, "api://<custom-api-client-id>/<delegated-scope>", context.User);

    HttpClient client = httpClientFactory.CreateClient();
    client.DefaultRequestHeaders.Authorization =
        AuthenticationHeaderValue.Parse(authorizationHeader);

    using HttpResponseMessage response =
        await client.GetAsync("https://api.contoso.com/user-data");
    response.EnsureSuccessStatusCode();

    return Results.Content(
        await response.Content.ReadAsStringAsync(),
        response.Content.Headers.ContentType?.ToString());
})
.RequireAuthorization();
```

Always use the agent ID that passed the access check. If the runtime used a different agent's identity, the downstream API would see the wrong agent acting for the user.

Verify the allowed request returns the downstream API's expected user data. Repeat the denied-agent and unknown-agent checks from the previous article: both must still return `404 Not Found` without calling the API. If only the allowed request fails downstream, check the selected agent's delegated grant and the API's user authorization rather than weakening the routing policy.

## Call specific resources

Use the resource scopes and permission setup from the linked articles, while keeping the fleet's blueprint configuration and `AddAgentIdentities` registration. The single-instance examples omit identity overrides. For each fleet request, call `CreateAuthorizationHeaderForUserAsync` with the routed agent ID and authenticated user.

| Resource | Example scope | Guidance |
| --- | --- | --- |
| Custom API | `api://<custom-api-client-id>/<delegated-scope>` | [Call a custom API as a user](aspnet-core-call-custom-api-as-user) |
| Azure services | `https://storage.azure.com/user_impersonation` | [Call Azure services as a user](aspnet-core-call-azure-api-as-user) |
| Microsoft Graph | `https://graph.microsoft.com/User.Read` | [Call Microsoft Graph as a user](aspnet-core-call-graph-as-user) |

For Azure REST APIs, use the same helper with the service's delegated scope and endpoint. For example, Azure Resource Manager uses `https://management.azure.com/user_impersonation`. The signed-in user's Azure role assignments determine resource access.

If you use `GraphServiceClient` instead of an HTTP authorization header, install and register it as described in the linked Graph article, but select the fleet agent on each call after the routing and access checks:

```csharp
using Microsoft.Graph;
using Microsoft.Identity.Web;

var me = await graphClient.Me.GetAsync(request =>
    request.Options.WithAuthenticationOptions(options =>
    {
        options.Scopes = ["https://graph.microsoft.com/User.Read"];
        options.User = context.User;
        options.WithAgentIdentity(registration.AgentIdentityId);
    }));
```

Here, `registration` is the directory entry for the agent ID that passed the access check, and `context` is the current `HttpContext`. Don't set `RequestAppToken` for OBO.