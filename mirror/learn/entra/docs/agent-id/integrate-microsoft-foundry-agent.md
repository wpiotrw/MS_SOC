---
layout: Conceptual
title: Use Microsoft Entra Agent ID with Microsoft Foundry - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/integrate-microsoft-foundry-agent
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Use the built-in Agent ID for a new Microsoft Foundry agent.
ms.topic: how-to
ms.date: 2026-10-28T00:00:00.0000000Z
ms.reviewer: dastrock
locale: en-us
document_id: eb88542a-9538-e5eb-9509-3ee6d154924a
document_version_independent_id: eb88542a-9538-e5eb-9509-3ee6d154924a
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/integrate-microsoft-foundry-agent.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/integrate-microsoft-foundry-agent
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/integrate-microsoft-foundry-agent.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/64b65f6c-101f-411a-9b83-9f577fab52d0
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/1a667fd1-8145-4b11-af0f-9f5de205a6e5
platformId: 5764ec47-03bd-5d70-ab99-15c370e24f26
---

# Use Microsoft Entra Agent ID with Microsoft Foundry - Microsoft Entra Agent ID | Microsoft Learn

Microsoft Foundry has built-in support for Microsoft Entra Agent ID. Foundry creates and manages the agent identity blueprint, Agent ID, and platform credential. You don't add a client secret or implement the Agent ID token exchange.

Use the current Foundry agent object model to opt in to this integration. Agents that use the legacy model continue to use a shared project identity or an Agent Application identity.

## Prerequisites

- A [Microsoft Foundry project](/en-us/azure/foundry/how-to/create-projects).
- Permission to create agents in the project.
- Permission to grant the Agent ID access to each downstream resource.

## Create an agent with Agent ID

Create a new agent by using the current Foundry agent model. A new agent receives:

- A unique agent identity blueprint.
- A unique Agent ID for its default instance.
- A stable agent endpoint.
- A platform-managed federated credential that Foundry uses for token exchange.

Follow [Configure and share your Microsoft Foundry agent](/en-us/azure/foundry/agents/how-to/configure-agent) to create and configure the agent.

If the project contains a legacy agent, create a new agent from the same definition. Foundry doesn't add a unique Agent ID to a legacy agent in place. For the opt-in and migration steps, see [Migrate from Agent Applications to the new Microsoft Foundry agent model](/en-us/azure/foundry/agents/how-to/migrate-agent-applications#migration-paths).

## Verify the agent identity

Retrieve or inspect the agent and confirm that `instance_identity` isn't null. A non-null value identifies an agent created with the current model.

Foundry manages the blueprint credential and runtime token exchange. Don't create another credential for the Foundry-managed blueprint.

For details about the objects that Foundry creates, see [Agent identity concepts in Microsoft Foundry](/en-us/azure/foundry/agents/concepts/agent-identity#how-foundry-provisions-identities).

## Grant access to a resource

New Agent IDs start without resource permissions. Grant access to the Agent ID used by the tool call:

- For an Azure resource, assign the least-privileged Azure role at the narrowest practical scope.
- For a custom API, assign the required application permission or app role.
- For delegated access, configure a supported user-delegation connection and obtain consent.

Use the Agent ID's object ID, not its client ID, when an Azure role assignment requires a principal ID.

For supported tools and authorization models, see [Permissions and access boundaries in Microsoft Foundry](/en-us/azure/foundry/agents/concepts/agent-identity#permissions-and-access-boundaries).