---
layout: Conceptual
title: Call Microsoft Graph as a user with ASP.NET Core - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/aspnet-core-call-graph-as-user
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Configure GraphServiceClient to call Microsoft Graph on behalf of a signed-in user through an agent identity.
ms.topic: how-to
ms.date: 2026-11-05T00:00:00.0000000Z
ai-usage: ai-assisted
ms.reviewer: dastrock, jomondi
locale: en-us
document_id: e3ad26c7-9096-d7fa-5ad2-cc7375635c3a
document_version_independent_id: e3ad26c7-9096-d7fa-5ad2-cc7375635c3a
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/aspnet-core-call-graph-as-user.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/aspnet-core-call-graph-as-user
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/aspnet-core-call-graph-as-user.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/d452572f-6212-498f-9050-ca4a9e50a425
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/a12e40b7-59a2-4437-96e2-166ce622b864
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 2effa437-cc73-c16d-0cab-bd1194f9280e
---

# Call Microsoft Graph as a user with ASP.NET Core - Microsoft Entra Agent ID | Microsoft Learn

Use Microsoft Graph to read the signed-in user's profile through your agent API.

In this article, the client calls the agent with an agent API token. Microsoft.Identity.Web exchanges it for a delegated Graph token without starting another interactive sign-in.

## Prerequisites

- Complete [Authenticate users to an ASP.NET Core agent API](aspnet-core-authenticate-users), including the local test client.
- Reuse the [blueprint credential and OBO services](aspnet-core-call-custom-api-as-user#configure-the-blueprint-credential). You don't need that walkthrough's custom downstream API registration, consent grant, or local API project for this Graph example.
- Declare the Microsoft Graph delegated permission `User.Read` on the blueprint and [grant delegated Microsoft Graph permissions to the agent identity](grant-agent-access-microsoft-365) for the test user. Client-to-agent consent doesn't grant the agent access to Graph.

## Add Microsoft Graph

Install the integration package:

```dotnetcli
dotnet add package Microsoft.Identity.Web.GraphServiceClient
```

Register `GraphServiceClient` with the services configured in the parent article. For this example, call `builder.Services.AddMicrosoftGraph` with `options.BaseUrl` set to `https://graph.microsoft.com/v1.0` and `options.Scopes` set to `["User.Read"]`. This configures downstream Graph access, not the incoming agent API's permission.

Place this registration before `builder.Build()` in the agent API's `Program.cs`.

```csharp
builder.Services.AddMicrosoftGraph(options =>
{
    options.BaseUrl = "https://graph.microsoft.com/v1.0";
    options.Scopes = ["User.Read"];
});
```

## Call Microsoft Graph

`GraphServiceClient` uses the authenticated user assertion from the request and the configured shared client ID. Don't set `RequestAppToken` or an Agent ID override; this call uses ordinary delegated access.

Require authentication and verify the incoming `access_agent` scope before calling `graphClient.Me.GetAsync()`. The incoming token is for the agent API; Microsoft.Identity.Web acquires a different token for Microsoft Graph.

Merge the following `using` directives with those at the top of `Program.cs`, and place the endpoint before its single `app.Run()`. You can omit the custom API endpoint from the parent walkthrough.

```csharp
using Microsoft.Graph;
using Microsoft.Identity.Web;
using Microsoft.Identity.Web.Resource;

app.MapGet("/graph-me", async (
    HttpContext context,
    GraphServiceClient graphClient) =>
{
    context.VerifyUserHasAnyAcceptedScope("access_agent");

    var user = await graphClient.Me.GetAsync();

    return Results.Ok(new
    {
        user?.Id,
        user?.DisplayName,
        user?.UserPrincipalName
    });
})
.RequireAuthorization();
```

The example requires `User.Read`. Add only the delegated permissions required by your Graph calls.

## Verify the Graph call

Start the agent API with `dotnet run --urls https://localhost:5001`. In the [local test client](aspnet-core-authenticate-users#run-the-test-client), change only the request URL to `https://localhost:5001/graph-me`; keep the agent API scope. Sign in as the user covered by both grants. Expect `HTTP 200` and that user's profile, with `id` matching the object ID returned by `/whoami`.

A call without a token must return `401`. If token acquisition reports missing consent, check the agent-to-Graph grant separately from the client's access to the agent. OBO can't display an interactive consent prompt. Stop the projects when finished and follow the steps to [clean up the local agent authentication test](aspnet-core-authenticate-users#clean-up-the-local-test) for test-only resources.