---
layout: Conceptual
title: Authenticate users and route requests to agents in a fleet with ASP.NET Core - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/aspnet-core-fleet-authenticate-users
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Validate user access tokens once for a shared ASP.NET Core runtime, route each request to an agent, and enforce per-agent access.
ms.topic: how-to
ms.date: 2026-11-05T00:00:00.0000000Z
ms.reviewer: dastrock
ai-usage: ai-assisted
locale: en-us
document_id: 04810a4c-b6f1-f449-2280-e32c006d62f4
document_version_independent_id: 04810a4c-b6f1-f449-2280-e32c006d62f4
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/aspnet-core-fleet-authenticate-users.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/aspnet-core-fleet-authenticate-users
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/aspnet-core-fleet-authenticate-users.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d452572f-6212-498f-9050-ca4a9e50a425
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/a12e40b7-59a2-4437-96e2-166ce622b864
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: b8a6b713-9177-e26a-94a5-439503428b3b
---

# Authenticate users and route requests to agents in a fleet with ASP.NET Core - Microsoft Entra Agent ID | Microsoft Learn

Users call a fleet agent with an access token for the blueprint's `access_agent` scope. Every agent in the fleet shares that audience, so token validation proves who the user is but not which agent they're allowed to use. The runtime routes each request to an agent and enforces per-agent access itself.

## Prerequisites

- Complete [Call APIs as an agent in a fleet with ASP.NET Core](aspnet-core-fleet-call-apis-as-agent).
- The `access_agent` scope [exposed on the blueprint](set-up-blueprint-agent-fleet#expose-the-inbound-scope).
- An upstream client that signs in users and requests the scope `api://<agent-identity-blueprint-client-id>/access_agent`.

## Configure token validation

Token validation is the same as for a single agent. Use the blueprint client ID as the expected audience. For upstream client setup and validation details, see [Authenticate users to an ASP.NET Core agent API](aspnet-core-authenticate-users).

To limit which users can call the fleet at all, [require an app role assignment](control-user-access-agents) on the blueprint principal. Those app roles apply to every agent in the fleet.

## Enforce per-agent access

Decide who can use each agent, and store that decision in the runtime. For example, record the users and groups that an agent's owner shares it with. Define an access policy that the runtime checks on every request:

```csharp
using System.Security.Claims;

public interface IAgentAccessPolicy
{
    Task<bool> CanUseAgentAsync(ClaimsPrincipal user, string agentId);
}
```

Identify the user by the `tid` and `oid` claims. Don't use the user principal name or email as a stable key.

Implement `IAgentAccessPolicy` against your sharing records and register it in dependency injection before mapping the endpoint. The interface alone doesn't enforce access.

## Route requests to agents

Put the runtime's agent ID in the route. Validate the token, confirm the agent exists, and check the access policy before running the agent:

```csharp
using Microsoft.Identity.Web.Resource;

app.MapPost("/agents/{agentId}/messages", async (
    string agentId,
    HttpContext context,
    IAgentDirectory directory,
    IAgentAccessPolicy accessPolicy) =>
{
    context.VerifyUserHasAnyAcceptedScope("access_agent");

    if (await directory.FindAsync(agentId) is null
        || !await accessPolicy.CanUseAgentAsync(context.User, agentId))
    {
        return Results.NotFound();
    }

    // Run the agent for this request.
    return Results.Accepted();
})
.RequireAuthorization();
```

The endpoint returns `404 Not Found` both for an unknown agent and for an agent the user can't use, so callers can't discover other agents in the fleet. After these checks pass, use `agentId` for every token request made while handling the request.

Before adding agent work, test with a user who can access one agent but not another. The allowed request reaches the placeholder `202 Accepted` response; requests for the other agent and an unknown agent return `404 Not Found`. Confirm that neither rejected request runs agent work or requests a downstream token. The placeholder response verifies routing and access checks, not agent execution.