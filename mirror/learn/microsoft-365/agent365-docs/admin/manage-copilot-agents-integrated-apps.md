---
layout: Conceptual
title: Manage agents in the Microsoft 365 admin center | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-agent-365/admin/manage-copilot-agents-integrated-apps
breadcrumb_path: ../breadcrumb/agent365/toc.json
uhfHeaderId: MSDocsHeader-Agent365
feedback_system: Standard
permissioned-type: public
ms.service: agent-365
hideScope: false
ms.custom:
- AdminSurgePortfolio
- AdminTemplateSet
- integrated-apps
ms.subservice: admin
description: Manage agents in the Microsoft 365 admin center. Learn how to enable, assign, block, or remove agents to optimize your organization's agentic experience.
f1.keywords:
- NOCSH
ms.author: erikre
author: Erikre
manager: dansimp
ms.date: 2026-07-09T00:00:00.0000000Z
ms.update-cycle: 180-days
audience: Admin
ms.topic: concept-article
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- m365copilot
- magic-ai-copilot
- operations-pod
search.appverid:
- BCS160
- MET150
- MOE150
locale: en-us
document_id: 55fb022e-5308-64c5-0b9a-cb19a4681be7
document_version_independent_id: 55fb022e-5308-64c5-0b9a-cb19a4681be7
original_content_git_url: https://github.com/MicrosoftDocs/agent365-docs-pr/blob/live/agent365-docs/admin/manage-copilot-agents-integrated-apps.md
site_name: Docs
depot_name: Learn.agent365
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage-copilot-agents-integrated-apps
moniker_range_name: 
monikers: []
item_type: Content
source_path: agent365-docs/admin/manage-copilot-agents-integrated-apps.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 84c90f65-5a3d-6b4f-8f54-fb2655752513
---

# Manage agents in the Microsoft 365 admin center | Microsoft Learn

Important

- This article is intended for IT administrators.
- The capability is enabled by default in all Microsoft Copilot licensed tenants.

Microsoft Copilot combines the power of large language models with your data and apps in Microsoft 365. It captures natural language commands to produce content and analyze data. It enables access to and use of other apps, such as Jira, [Dynamics 365](/en-us/microsoft-365-copilot/extensibility/overview-business-applications), or Bing Web Search.

You can manage agents for Copilot by using the [Microsoft 365 admin center](https://admin.microsoft.com/). You can enable, disable, assign, block, or remove agents for your organization, and manage Copilot capabilities.

Note

Researcher and Analyst are first-party Microsoft experiences built on the same foundation as Microsoft Copilot, operating entirely within the Microsoft 365 commercial data processing boundary. These tools inherit all existing security, privacy, and compliance commitments that apply across the suite of Microsoft 365 products. These tools are available in Microsoft Copilot Chat under **Tools** and can be invoked by the user anytime. While Researcher and Analyst coexist with agents and abide by all the agent-related governance capabilities, Researcher and Analyst are part of the core Copilot chat experience and will not fall under any agent-related settings. For related information, see [Agent settings in Microsoft 365 admin center](agent-settings).

Microsoft Agent 365 is the control plane for AI agents, empowering your organization to confidently deploy, govern, and manage all your agents at scale, regardless of where these agents are built or acquired. For more information, see [Overview of Microsoft Agent 365](../overview) and [Microsoft Agent 365 documentation](../).

## Overview

Agents enhance the functionality of Copilot by adding search capabilities, custom actions, connectors, and APIs. Agents are custom versions of Microsoft Copilot that combine instructions, knowledge, and skills to perform specific tasks or scenarios. For more information about using agents with Copilot, see [Get started with agents in the Microsoft Copilot app](https://support.microsoft.com/topic/169469d7-328d-4d37-9090-bfc2058a39bd).

The members of your organization can find and add agents from the [Agent Store](/en-us/microsoft-365/copilot/copilot-agent-store) within the Microsoft Copilot app. However, before users can access these agents, each agent must undergo a streamlined process of submission and approval. Agents are managed in the [Agent Registry](agent-registry-overview) of Microsoft 365 admin center. As part of agent management, you can review [agent requests](agent-requests) and determine whether to publish the agent to the store or reject the agent submission. For more information, see [Agent management in Microsoft 365 admin center](agent-365-overview). Members of your organization can only access the agents that you have allowed.

## Agent types you can manage

You can manage several types of agents in Microsoft Copilot, each serving different purposes:

- **Published by your organization**: Built with predefined instructions and actions. These agents follow structured logic and are best for predictable, rule-based tasks. Before you make these agents available to members of your organization, these agents go through an admin approval to ensure compliance and readiness. For more information, see [Manage agent requests in Microsoft 365 admin center](agent-requests).

    Note

    Publishing agents to the organization is supported in Microsoft 365 Government Community Cloud High (GCCH) and Government Community Cloud Moderate (GCCM) environments.
- **Shared by creator**: Shared agents are custom versions of Microsoft Copilot that combine instructions, knowledge, and skills to perform specific tasks or scenarios. Creators can create and share these agents through multiple channels, such as Microsoft Copilot Studio, Microsoft Copilot Agent Builder, and more. Shared agents enhance the functionality of Copilot by adding search capabilities, custom actions, connectors, and APIs. For more information, see [Share agents with other users](/en-us/microsoft-copilot-studio/admin-share-bots).

    As an admin, you can view shared agents on the **Agents** page in the Microsoft 365 admin center. You can see a list of all shared agents in the **Agent Registry**, including details such as the agent's name, creator, creation date, host products, and availability status. You can search for specific agents and manage their lifecycle, including blocking agents that are deemed unsafe or noncompliant.

    For your users, shared agents are available through Copilot on different surfaces. Users can interact with these agents to perform specific tasks or get assistance based on the agent's capabilities.
- **Microsoft agents**: Developed by Microsoft and integrated with Microsoft 365 services.
- **External partner agents**: Created by external developers or vendors. You can control their availability and permissions.
- **Frontier agents**: Experimental or advanced agents that use new capabilities or integrations. These agents might be in early stages of development or testing and could require more oversight or limited rollout.

    - **App Builder agent**: A type of Frontier agent developed by Microsoft that can be managed as part of Microsoft Copilot. You can also manage App Builder using [Power Platform admin center](https://admin.powerplatform.microsoft.com).
    - **Workflows agent**: A type of Frontier agent developed by Microsoft that can be managed as part of Microsoft Copilot. Flows created in Copilot are saved to the default environment unless [environment routing](/en-us/power-platform/admin/default-environment-routing?tabs=new#turn-on-environment-routing-in-the-admin-center) is enabled for Copilot Studio. You can also manage flows using the [Power Platform admin center](https://admin.powerplatform.microsoft.com).

Note

The same Copilot Studio agent (declarative or custom engine) can appear more than once in the admin center with different publisher states, such as **Shared by creator** and **Published by your organization**. Depending on the publishing lifecycle and the actions that creators and admins take, these duplicate-looking entries can represent separate lifecycle and publisher records for the same underlying agent. They're expected and by design, not an error.

For lifecycle details and available admin actions, see [How one agent can appear as multiple entries](agent-registry-overview#how-one-agent-can-appear-as-multiple-entries).

## Get started

To get started managing agents within Microsoft 365 admin center, see [Agent management in Microsoft 365 admin center](agent-365-overview). You will learn about agent management roles and permissions, as well as agent inventory, lifecycle, tools, and settings.

Important

Use roles with the fewest permissions. Accounts with lower permissions help improve security for your organization. Global Administrator is a highly privileged role. Limit its use to emergency scenarios when you can't use an existing role. For more information, see [About admin roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

[![Screenshot showing the Agents &amp; connectors page in the Microsoft 365 admin center.](media/agents/get-started.png)](media/agents/get-started.png#lightbox)