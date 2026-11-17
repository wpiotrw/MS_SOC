---
layout: Conceptual
title: Call APIs as an agent's user account in a fleet with ASP.NET Core - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/aspnet-core-fleet-call-apis-as-agent-user
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Select the agent identity and agent's user account for each token request in a shared ASP.NET Core runtime that hosts many agents.
ms.topic: how-to
ms.date: 2026-11-05T00:00:00.0000000Z
ms.reviewer: dastrock
ai-usage: ai-assisted
locale: en-us
document_id: 6abe9b2c-dfee-6a04-9cfb-4f284fc89656
document_version_independent_id: 6abe9b2c-dfee-6a04-9cfb-4f284fc89656
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/aspnet-core-fleet-call-apis-as-agent-user.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/aspnet-core-fleet-call-apis-as-agent-user
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/aspnet-core-fleet-call-apis-as-agent-user.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d452572f-6212-498f-9050-ca4a9e50a425
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/a12e40b7-59a2-4437-96e2-166ce622b864
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 9930ea01-504c-298a-2ad1-5949bbcb70d8
---

# Call APIs as an agent's user account in a fleet with ASP.NET Core - Microsoft Entra Agent ID | Microsoft Learn

Some agents in a fleet need a user object for Microsoft 365 workloads, such as a mailbox or Teams membership. For those agents, look up both the agent identity and its agent's user account in the agent directory, and pass them to `WithAgentUserIdentity`.

To decide whether an agent needs an agent's user account, see [Use an agent's user account with Microsoft 365](agent-user-oauth-flow#determine-whether-the-agent-needs-a-user-object).

## Prerequisites

- Complete [Call APIs as an agent in a fleet with ASP.NET Core](aspnet-core-fleet-call-apis-as-agent).
- An agent's user account [provisioned for the agent](aspnet-core-fleet-provision-agent-identities#provision-an-agent).
- Delegated permissions for the target API, such as `Mail.ReadWrite`, [granted to the agent identity](grant-agent-access-microsoft-365) or [inherited from the blueprint](set-up-blueprint-agent-fleet#optionally-configure-inheritable-permissions).
- The Microsoft 365 licenses and resource access that the agent's user account needs. For details, see [Provision access](agent-user-oauth-flow#provision-access).

## Get a token for an agent's user account

Add a method to `FleetTokenService`:

```csharp
using System.Security.Claims;

public async Task<string> CreateAuthorizationHeaderForAgentUserAsync(
    string agentId, string scope)
{
    AgentRegistration registration = await GetRegistrationAsync(agentId);

    if (registration.AgentUserId is null)
    {
        throw new InvalidOperationException(
            $"Agent '{agentId}' doesn't have an agent's user account.");
    }

    var options = new AuthorizationHeaderProviderOptions()
        .WithAgentUserIdentity(
            registration.AgentIdentityId,
            Guid.Parse(registration.AgentUserId));

    return await authorizationHeaderProvider
        .CreateAuthorizationHeaderForUserAsync([scope], options, new ClaimsPrincipal());
}
```

Pass `new ClaimsPrincipal()` because no person is signed in. The user comes from the agent directory, not from the request context.

Call the method from the agent's work, and send the header to Microsoft Graph:

```csharp
using System.Net.Http.Headers;

string authorizationHeader = await fleetTokenService
    .CreateAuthorizationHeaderForAgentUserAsync(agentId, "https://graph.microsoft.com/.default");

HttpClient client = httpClientFactory.CreateClient();
client.DefaultRequestHeaders.Authorization =
    AuthenticationHeaderValue.Parse(authorizationHeader);

using HttpResponseMessage response =
    await client.GetAsync("https://graph.microsoft.com/v1.0/me/messages");
response.EnsureSuccessStatusCode();
```

The token represents the agent's user account, so `/me` returns that account's data. Each agent can reach only the mailbox, files, and teams that its own account was given.

For this example, verify that Microsoft Graph returns a successful messages response for the selected agent's mailbox. An empty messages collection isn't an authentication failure. If the call fails, check delegated permission grants separately from the account's license, mailbox provisioning, and resource access; acquiring a token doesn't provision a mailbox.