---
layout: Conceptual
title: Plugins overview for Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-overview
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about plugins in Microsoft Security Copilot, how the plugins extend agents with external tools and services, and how to use Microsoft, partner-built, or create custom plugins.
ms.date: 2026-06-01T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: how-to
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: copilot-learning-hub
ms.reviewer: shivanpatel
search.audiencetype: Admin
locale: en-us
document_id: 95d80808-3230-d484-c5b0-80fa9113af5a
document_version_independent_id: 95d80808-3230-d484-c5b0-80fa9113af5a
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-overview.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-overview.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: 00a45b76-ebca-bb83-60ad-5a5ca063feec
---

# Plugins overview for Microsoft Security Copilot | Microsoft Learn

A plugin is a collection of related tools that users can enable in Security Copilot when relevant to creating new prompting, promptbook, or agentic capabilities. A tool (also referred to as a skill) is a resource accessed outside of the agent instructions and LLM that a Security Copilot agent can invoke to help complete its outcome.

For agents, plugins extend what an agent can do by giving it access to resources outside of an agent and LLM. An example is a plugin that uses an API to connect to an external service such as reputation lookup, where underlying tool definitions for the plugin could return a reputation score, related malware, threat intelligence, etc.

Security Copilot comes with many default plugins and supports several non-Microsoft plugins. You can also extend Security Copilot's capabilities by adding or creating your own plugin. The Security Copilot platform enables developers and users to write plugins that can be invoked to perform specialized tasks.

Note

Products that integrate with Security Copilot as plugins need to be purchased separately.

For more information on how to develop plugins that use the OpenAI schema, see [Plugins for Microsoft Copilot documentation](custom-plugins).

## Preinstalled plugins

Get familiar with the plugins Security Copilot can use to source information or take action when it's responding to your prompts. Depending on which services your organization uses, any of the plugins in the following lists might be available to you.

To find out which plugins Security Copilot can use when you interact with it, select the plugin button. Check for plugins that are toggled on in the list that opens. Security Copilot automatically uses the available plugins without any extra setup from you.

### Microsoft plugins

Security Copilot uses the on-behalf-of authentication flow to provide access to other Microsoft services that your organization already has access to. For more information, see [Understand authentication](authentication).

For the full list of built-in plugins, see Microsoft plugins.

### Non-Microsoft plugins

For more information on non-Microsoft plugins, see [Other plugins](plugin-other).

### Websites

- Public web

## Custom plugins

You can create new plugins to extend what Copilot can do by following the steps in [Create new plugins](custom-plugins).

To add and manage your custom plugins to Security Copilot, follow the steps in [Manage custom plugins](manage-plugins#manage-custom-plugins).