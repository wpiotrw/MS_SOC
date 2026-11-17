---
layout: Conceptual
title: Use Microsoft Entra Agent ID with Copilot Studio - Microsoft Entra Agent ID | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/agent-id/integrate-copilot-studio-agent
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
author: Dickson-Mwendia
ms.author: dmwendia
ms.service: entra-id
ms.subservice: agent-id
manager: pmwongera
description: Find and manage the Agent ID that Copilot Studio creates for a new agent.
ms.topic: how-to
ms.date: 2026-10-28T00:00:00.0000000Z
ms.reviewer: dastrock
locale: en-us
document_id: d8d9d5fd-5db7-3e53-2992-6d18e5c59bea
document_version_independent_id: d8d9d5fd-5db7-3e53-2992-6d18e5c59bea
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/agent-id/integrate-copilot-studio-agent.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agent-id/integrate-copilot-studio-agent
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agent-id/integrate-copilot-studio-agent.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c389ea6b-b6a0-46df-93a1-1e21f25e19e7
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/19ada1b6-705b-4ed7-aad0-bffd1bd03dfa
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 25817344-6abc-a3e9-df4d-c815b56aab48
---

# Use Microsoft Entra Agent ID with Copilot Studio - Microsoft Entra Agent ID | Microsoft Learn

Microsoft Copilot Studio automatically creates a Microsoft Entra Agent ID for each new agent. Copilot Studio manages the blueprint, Agent ID, and platform credentials. You don't register the identity or implement token acquisition.

Automatic Agent ID creation is built in for new agents and can't be turned off. Agents created before the integration rollout can continue to use legacy app registrations until they migrate.

## Create the agent

Create an agent by following [Create and delete agents in Copilot Studio](/en-us/microsoft-copilot-studio/authoring-first-bot). Copilot Studio creates the Agent ID as part of the agent lifecycle.

When the first Agent ID is created, Copilot Studio adds the **Microsoft Copilot Studio agent identity blueprint** to the tenant. Copilot Studio manages this shared blueprint and its credentials.

Don't create a separate blueprint or Agent ID for the Copilot Studio agent.

## Find the Agent ID

1. Open the agent in Copilot Studio.
2. Go to **Settings** &gt; **Advanced**.
3. Expand **Metadata**.
4. Copy the GUID under **Entra Agent ID**.
5. Use the GUID to find the Agent ID in the [Microsoft Entra admin center](https://entra.microsoft.com).

For the current lifecycle, metadata, and deletion behavior, see [Manage Entra Agent IDs in Copilot Studio](/en-us/microsoft-copilot-studio/admin-use-entra-agent-identities).

## Review connector permissions

When you publish the agent, Copilot Studio attaches API permissions for its Power Platform connectors to the Agent ID. Review those permissions in Microsoft Entra ID and keep the agent's connectors and data policies aligned with the intended scenario.

Copilot Studio manages the connector runtime and platform credential. Don't add credentials to the Agent ID.

## Handle an existing agent

An older agent might still use an app-registration identity. You can wait for the platform migration or use the self-service migration process.

For current migration options, see [Migrate Copilot Studio agents to Microsoft Entra Agent ID](/en-us/microsoft-copilot-studio/govern-migrate-api-entra-agent-identity). For planning guidance in this documentation, see [Recreate Copilot Studio agents with Microsoft Entra Agent ID](migrate-copilot-studio-agents-to-agent-id).