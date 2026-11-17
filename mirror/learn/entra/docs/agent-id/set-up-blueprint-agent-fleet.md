---
layout: Conceptual
title: Set up an agent identity blueprint for a fleet - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/set-up-blueprint-agent-fleet
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Configure an agent identity blueprint, credential, permissions, and inbound scope for a fleet of agents on a shared runtime.
ms.topic: how-to
ms.date: 2026-11-05T00:00:00.0000000Z
ms.reviewer: dastrock
ai-usage: ai-assisted
locale: en-us
document_id: 39f53aba-0a87-9bf6-b318-9ec8340e2abd
document_version_independent_id: 39f53aba-0a87-9bf6-b318-9ec8340e2abd
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/set-up-blueprint-agent-fleet.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/set-up-blueprint-agent-fleet
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/set-up-blueprint-agent-fleet.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 1f4fbf84-37d2-b2e8-6876-0dfca94bf3ca
---

# Set up an agent identity blueprint for a fleet - Microsoft Entra Agent ID | Microsoft Learn

A fleet runtime uses one [agent identity blueprint](agent-blueprint) to create agent identities and to acquire tokens for them. Configure the blueprint once, before the first agent is deployed. For the overall design, see [Plan an agent fleet on a shared runtime](plan-agent-fleet).

## Prerequisites

- The Agent ID Developer role, to create the blueprint.
- An administrator who can grant tenant-wide admin consent for Microsoft Graph application permissions.
- An Azure compute resource for the runtime with a user-assigned managed identity.

## Create the blueprint and its principal

1. [Create an agent identity blueprint](create-blueprint#create-an-agent-identity-blueprint). Record its client ID.
2. [Create the agent identity blueprint principal](create-blueprint#create-an-agent-blueprint-principal) in the tenant. The principal creates agent identities and receives admin consent.

Record the tenant ID, blueprint client ID and object ID, blueprint principal object ID, and runtime managed identity client ID for the developer who configures provisioning. Use [Record the identifiers for your scenario](key-concepts#record-the-identifiers-for-your-scenario) to distinguish these values.

## Add the blueprint credential

[Add the runtime's managed identity as a federated identity credential](create-blueprint#configure-credentials-for-the-agent-identity-blueprint) on the blueprint. The runtime and the provisioning service use this credential to authenticate as the blueprint.

Don't use client secrets in production. Every agent in the fleet depends on this credential.

## Grant provisioning permissions

The blueprint principal needs the following Microsoft Graph application permissions to provision identities. Neither permission is granted by default.

| Permission | Required for |
| --- | --- |
| `AgentIdentity.CreateAsManager` | Creating and deleting agent identities |
| `AgentIdUser.ReadWrite.IdentityParentedBy` | Creating and deleting agent's user accounts |

Skip `AgentIdUser.ReadWrite.IdentityParentedBy` if no agent in the fleet needs an agent's user account. Skip both if [Agent 365 provisions your agents](plan-agent-fleet#choose-how-agents-are-provisioned).

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com).
2. Browse to **Entra ID** &gt; **App registrations** and open the blueprint app registration.
3. Select **API permissions** &gt; **Add a permission** &gt; **Microsoft Graph** &gt; **Application permissions**.
4. Select `AgentIdentity.CreateAsManager` and, if needed, `AgentIdUser.ReadWrite.IdentityParentedBy`.
5. Select **Add permissions**, and then select **Grant admin consent**.

Before handing setup back to the runtime developer, confirm that admin consent is granted for each selected Microsoft Graph application permission on this blueprint. A permission listed without consent doesn't make the provisioning service ready. Keep these provisioning permissions separate from the downstream permissions granted to agents.

For more information about these permissions, see [Agent identity blueprint principals](agent-id-creation-channels#agent-identity-blueprint-principals).

## Plan how agents get access

Grant access to each agent identity individually. This approach is recommended because each agent's access stays separate and visible on its agent identity. After the provisioning service creates an agent identity, grant it the application permissions, delegated permissions, Azure role assignments, or other access that the agent needs:

- [Grant application permissions](grant-application-permissions-agent-identity)
- [Grant delegated permissions](grant-agent-access-microsoft-365)

### Optionally configure inheritable permissions

If every agent in the fleet needs the same permissions, you can grant them once on the blueprint principal and let each agent identity inherit them. This approach is a convenience: new agent identities receive the permissions without a separate grant.

1. Add the shared permissions to the blueprint's required resource access.
2. [Configure inheritable permissions](configure-inheritable-permissions-blueprints) for each resource app, such as Microsoft Graph or your custom API.
3. Have an administrator grant admin consent for those permissions on the blueprint principal.

Inherited permissions don't appear on agent identities in the admin center or through Microsoft Graph. They appear only in the tokens that agent identities receive. For the rules that determine which permissions are inherited, see [Inheritable permissions](concept-inheritable-permissions#declaration-grant-and-inheritance).

## Expose the inbound scope

If users or client applications call agents in the fleet, [configure an identifier URI and the `access_agent` scope](create-blueprint#configure-identifier-uri-and-scope) on the blueprint. Every agent in the fleet shares this audience.

To limit who can call the fleet, [define app roles and require assignment](control-user-access-agents) on the blueprint principal. App roles apply to every agent in the fleet. Enforce per-agent access in the runtime.