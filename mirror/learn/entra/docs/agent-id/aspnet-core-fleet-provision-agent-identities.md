---
layout: Conceptual
title: Provision agent identities for a fleet with ASP.NET Core - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/aspnet-core-fleet-provision-agent-identities
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Create an agent identity and an optional agent's user account when an agent is deployed to a shared ASP.NET Core runtime, and delete them when it's retired.
ms.topic: how-to
ms.date: 2026-11-05T00:00:00.0000000Z
ms.reviewer: dastrock
ai-usage: ai-assisted
locale: en-us
document_id: a5b2f2f5-ec96-e492-38a2-6364ad792403
document_version_independent_id: a5b2f2f5-ec96-e492-38a2-6364ad792403
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/aspnet-core-fleet-provision-agent-identities.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/aspnet-core-fleet-provision-agent-identities
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/aspnet-core-fleet-provision-agent-identities.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/d452572f-6212-498f-9050-ca4a9e50a425
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/a12e40b7-59a2-4437-96e2-166ce622b864
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 94520905-4d98-1721-bf3f-2b33a7e2e6d2
---

# Provision agent identities for a fleet with ASP.NET Core - Microsoft Entra Agent ID | Microsoft Learn

When an agent is deployed to the fleet, the provisioning service authenticates as the agent identity blueprint and calls Microsoft Graph. It creates an agent identity and, if the agent needs one, an agent's user account. It records both in the agent directory so the runtime can select them on later token requests. When the agent is retired, the service deletes both identities.

## Prerequisites

- Complete [Set up an agent identity blueprint for a fleet](set-up-blueprint-agent-fleet).
- The .NET 8 SDK or later.
- A user or group to assign as each agent's sponsor.
- A verified domain in the tenant for agent's user account user principal names, if agents need them.
- A persistent store for the agent directory, such as a database table.

The snippets extend your ASP.NET Core provisioning service; they aren't a standalone application or a complete `Program.cs`. Implement `IAgentDirectory` with the persistent store and register that implementation before invoking `AgentProvisioner`. Keep the service's existing host startup code.

## Install the packages

```dotnetcli
dotnet add package Microsoft.Identity.Web
dotnet add package Microsoft.Identity.Web.DownstreamApi
```

## Configure the blueprint and Microsoft Graph

Add the blueprint credential and two Microsoft Graph profiles to *appsettings.json*. `RequestAppToken` requests a token for the blueprint itself, not for an agent identity.

```json
{
  "AzureAd": {
    "Instance": "https://login.microsoftonline.com/",
    "TenantId": "<tenant-id>",
    "ClientId": "<agent-identity-blueprint-client-id>",
    "ClientCredentials": [
      {
        "SourceType": "SignedAssertionFromManagedIdentity",
        "ManagedIdentityClientId": "<managed-identity-client-id>"
      }
    ]
  },
  "DownstreamApis": {
    "agent-identities": {
      "BaseUrl": "https://graph.microsoft.com/",
      "RelativePath": "beta/serviceprincipals/Microsoft.Graph.AgentIdentity",
      "Scopes": [ "https://graph.microsoft.com/.default" ],
      "RequestAppToken": true
    },
    "agent-users": {
      "BaseUrl": "https://graph.microsoft.com/",
      "RelativePath": "v1.0/users/microsoft.graph.agentUser",
      "Scopes": [ "https://graph.microsoft.com/.default" ],
      "RequestAppToken": true
    }
  }
}
```

Warning

Client secrets shouldn't be used as client credentials in production environments for agent identity blueprints due to security risks. Instead, use more secure authentication methods such as [federated identity credentials (FIC) with managed identities](/en-us/entra/workload-id/workload-identity-federation-config-app-trust-managed-identity) or client certificates. These methods provide enhanced security by eliminating the need to store sensitive secrets directly within your application configuration.

Register the downstream APIs:

```csharp
using Microsoft.Identity.Web;

var builder = WebApplication.CreateBuilder(args);

builder.Services
    .AddMicrosoftIdentityWebApiAuthentication(builder.Configuration)
    .EnableTokenAcquisitionToCallDownstreamApi()
    .AddInMemoryTokenCaches();

builder.Services.AddDownstreamApis(
    builder.Configuration.GetSection("DownstreamApis"));
builder.Services.AddScoped<AgentProvisioner>();
// Register your IAgentDirectory implementation.
```

## Define the agent directory

The agent directory maps the runtime's agent ID to the agent's identities. Later articles in this path use it to select the identity for each token request.

```csharp
public record AgentRegistration(
    string AgentId,
    string AgentIdentityId,
    string? AgentUserId);

public interface IAgentDirectory
{
    Task<AgentRegistration?> FindAsync(string agentId);
    Task SaveAsync(AgentRegistration registration);
    Task DeleteAsync(string agentId);
}
```

| Field | Value | Used by |
| --- | --- | --- |
| `AgentId` | The runtime's own identifier for the agent. | Lookups |
| `AgentIdentityId` | The agent identity's ID. For an agent identity, the object ID (`id`) and client ID (`appId`) are the same value. | Token requests, creating the agent's user account, and deleting the agent identity |
| `AgentUserId` | The agent's user account object ID, or `null`. | `WithAgentUserIdentity` and deletion |

## Provision an agent

Call the provisioning service from the code that deploys agents, not from an endpoint that agents or users can reach.

```csharp
using System.Text.Json.Serialization;
using Microsoft.Identity.Abstractions;

public class AgentProvisioner(
    IDownstreamApi graph,
    IAgentDirectory directory,
    IConfiguration configuration)
{
    public async Task<AgentRegistration> ProvisionAsync(
        string agentId,
        string displayName,
        string sponsorUserId,
        string? agentUserPrincipalName = null)
    {
        AgentRegistration registration = await directory.FindAsync(agentId)
            ?? await CreateAgentIdentityAsync(agentId, displayName, sponsorUserId);

        if (agentUserPrincipalName is not null && registration.AgentUserId is null)
        {
            registration = await CreateAgentUserAsync(
                registration, displayName, agentUserPrincipalName);
        }

        return registration;
    }

    private async Task<AgentRegistration> CreateAgentIdentityAsync(
        string agentId, string displayName, string sponsorUserId)
    {
        AgentIdentityResponse? identity = await graph
            .PostForAppAsync<AgentIdentityRequest, AgentIdentityResponse>(
                "agent-identities",
                new AgentIdentityRequest(
                    displayName,
                    configuration["AzureAd:ClientId"]!,
                    [$"https://graph.microsoft.com/v1.0/users/{sponsorUserId}"]));

        var registration = new AgentRegistration(
            agentId, identity!.Id, AgentUserId: null);
        await directory.SaveAsync(registration);
        return registration;
    }

    private async Task<AgentRegistration> CreateAgentUserAsync(
        AgentRegistration registration, string displayName, string userPrincipalName)
    {
        AgentUserResponse? agentUser = await graph
            .PostForAppAsync<AgentUserRequest, AgentUserResponse>(
                "agent-users",
                new AgentUserRequest(
                    AccountEnabled: true,
                    displayName,
                    MailNickname: userPrincipalName.Split('@')[0],
                    userPrincipalName,
                    IdentityParentId: registration.AgentIdentityId));

        registration = registration with { AgentUserId = agentUser!.Id };
        await directory.SaveAsync(registration);
        return registration;
    }
}

public record AgentIdentityRequest(
    [property: JsonPropertyName("displayName")] string DisplayName,
    [property: JsonPropertyName("agentIdentityBlueprintId")] string AgentIdentityBlueprintId,
    [property: JsonPropertyName("sponsors@odata.bind")] string[] Sponsors)
{
    [JsonPropertyName("@odata.type")]
    public string ODataType => "#Microsoft.Graph.AgentIdentity";
}

public record AgentIdentityResponse(
    [property: JsonPropertyName("id")] string Id);

public record AgentUserRequest(
    [property: JsonPropertyName("accountEnabled")] bool AccountEnabled,
    [property: JsonPropertyName("displayName")] string DisplayName,
    [property: JsonPropertyName("mailNickname")] string MailNickname,
    [property: JsonPropertyName("userPrincipalName")] string UserPrincipalName,
    [property: JsonPropertyName("identityParentId")] string IdentityParentId);

public record AgentUserResponse(
    [property: JsonPropertyName("id")] string Id);
```

The service saves the agent directory entry after each Microsoft Graph call and reuses saved identities on retries. This isn't an atomic transaction with Microsoft Graph. Serialize provisioning for each agent ID, and reconcile a successful Graph call whose response or directory write failed before retrying, to avoid duplicate identities.

Pass `agentUserPrincipalName` only for agents that need an agent's user account. Use a verified domain and a unique alias for each agent. Creating the account doesn't assign licenses, a mailbox, or team membership. For those steps, see [Use an agent's user account with Microsoft 365](agent-user-oauth-flow#provision-access).

A new agent identity can take a short time to become available for permission assignments, agent-user creation, and token requests. If Microsoft Graph or the token service reports that the newly created identity or the agent user's parent can't be found, retry with bounded backoff and reuse the saved registration. A new agent user can also take time to be recognized as the principal in a consent grant. Use the same bounded retry approach if Microsoft Graph explicitly reports that the new principal can't be found.

After granting permissions, allow time for those grants to appear in a newly acquired token; retrying with the same cached token doesn't pick up new grants. Don't treat an authorization failure as successful provisioning.

Before continuing, read the saved registration through `IAgentDirectory.FindAsync` using the runtime's agent ID. Confirm it contains the returned agent identity ID and, when requested, the agent user ID. This verifies the directory handoff; it doesn't yet prove downstream API access.

## Grant the agent access

After the agent identity exists, grant it the access that this agent needs. Grant application permissions, delegated permissions, Azure role assignments, and access to other resources directly to the agent identity. Each agent's access then stays separate and visible on its own identity.

- [Grant application permissions](grant-application-permissions-agent-identity)
- [Grant delegated permissions](grant-agent-access-microsoft-365)

Permissions that are [inherited from the blueprint](set-up-blueprint-agent-fleet#optionally-configure-inheritable-permissions) apply to the new agent identity without another grant.

## Retire an agent

Stop routing new requests and scheduling work for the agent, and let its in-flight operations finish before deleting its identities. Retire only that agent's resources; don't delete the shared blueprint or runtime credential while other agents still use them.

Delete the agent's user account before the agent identity, and then remove the agent directory entry:

```csharp
public async Task RetireAsync(string agentId)
{
    AgentRegistration? registration = await directory.FindAsync(agentId);
    if (registration is null)
    {
        return;
    }

    if (registration.AgentUserId is not null)
    {
        await graph.DeleteForAppAsync<string>(
            "agent-users",
            null!,
            options => options.RelativePath += $"/{registration.AgentUserId}");
    }

    await graph.DeleteForAppAsync<string>(
        "agent-identities",
        null!,
        options => options.RelativePath =
            $"beta/serviceprincipals/{registration.AgentIdentityId}");

    await directory.DeleteAsync(agentId);
}
```

Add `RetireAsync` to the `AgentProvisioner` class. Deleted agent identities can be restored for a limited time. For details, see [Delete and restore agent identity objects](howto-delete-agent-identity).

Use the single-type `DeleteForAppAsync<TInput>` overload because Microsoft Graph returns `204 No Content`; the two-type overload tries to deserialize a response body. In production, make retirement retry-safe by treating `404 Not Found` as already deleted and reconciling the directory after partial failures.

## Use Agent 365 provisioning instead

If agents are created through Agent 365, Agent 365 creates the agent identity. Instead of calling Microsoft Graph, listen for Agent 365 agent provisioning events, read the agent identity ID from each event, and save an `AgentRegistration` in the agent directory. For event details, see the [Agent 365 developer documentation](/en-us/microsoft-agent-365/developer/).