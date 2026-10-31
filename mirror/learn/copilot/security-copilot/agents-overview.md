---
layout: Conceptual
title: Microsoft Security Copilot agents overview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/agents-overview
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about agents, plugins, and connectors in Microsoft Security Copilot.
ms.date: 2026-03-18T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: overview
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
- essentials-get-started
locale: en-us
document_id: 89054e61-b876-588a-9cfc-9b45a05f1558
document_version_independent_id: 89054e61-b876-588a-9cfc-9b45a05f1558
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/agents-overview.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: agents-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/agents-overview.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 3d8a1824-5a38-c57d-7e87-0f9718b7b7cc
---

# Microsoft Security Copilot agents overview | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

Microsoft Security Copilot agents automate repetitive tasks and reduce manual workloads. They enhance security and IT operations across cloud, data security and privacy, identity, and network security. These agents handle high-volume, time-consuming tasks by pairing data and code with an AI language model. They respond to user requests and system events, helping teams work more efficiently and focus on higher-impact tasks.

Agents fit naturally into existing workflows. You don't need special training or other licensing to use them. Agents utilize SCUs to operate just like other features in the product. They integrate seamlessly with Microsoft Security solutions and the broader supported partner ecosystem. Agents learn based on feedback and keep you in control on the actions it takes. They handle resource-intensive tasks like threat intelligence briefings, and Conditional Access optimization. With Microsoft Security Copilot agents, you can scale up your teams, people, and processes.

Microsoft Security Copilot agents offer significant benefits for security teams and IT operations by automating routine tasks and freeing up valuable time for teams to concentrate on strategic initiatives and complex problem-solving. This leads to improved operational efficiency, enhanced security and giving teams the ability to respond more swiftly to emerging threats. With Security Copilot agents, organizations can achieve greater scalability and resilience in their security and IT processes.

## Agent terminology

This article defines key agent terminology used during agent setup.

### Trigger

A trigger is an event or condition that tells an agentic system to initiate an action or series of actions. You can set the agent to run automatically at specific intervals or choose to run it manually when needed.

### Permissions

In the context of agents, permissions are the level of authorization an AI agent is given by an administrator during configuration that enables it to access specific information or carry out its tasks.

These permissions might include the ability to read data from other solutions; for example, Microsoft Defender External Attack Surface Management or Microsoft Threat Intelligence. By giving the agent permissions to access data from these solutions, the agent can generate insights or provide recommendations based on the information it's able to gather.

### Identity

An agent needs an identity to authenticate and securely access resources when it runs. During the agent setup process, you can choose from two types of identity:

- **Create an agent identity**

    Note

    Currently, this option is only available for Microsoft-built agents.

    This option creates a dedicated identity for the agent using the Microsoft Entra Agent ID capability. Microsoft Entra Agent IDs are identities created specifically for AI agents. The user setting up the agent grants the agent ID permissions needed for the agent to run successfully. Using Agent IDs keeps access scoped, secure, and easier to manage. For more information, see [What are agent identities?](https://aka.ms/WhatAreAgentIdentities).
- **Connect with an existing user account**

    This option lets the agent use your credentials to run. It inherits your access and permissions while it's active.

### Plugins

Plugins extend Security Copilot's capabilities. A plugin is a component that extends what an agent can do by giving it access to capabilities in Microsoft and non-Microsoft services and public websites through APIs. Having access to plugins adds more context to the output of an agent.

## Get started

To get started with Microsoft Security Copilot and harness agentic AI to transform security and IT operations, follow these steps in the journey to discover and use agents.

1. **Discover agents**: Browse Microsoft and partner-built agents
    - [Standalone](discover-agents) or [embedded](discover-agents#agents-in-the-microsoft-security-ecosystem) experience in the Microsoft security products
    - [Security Store](security-store-integration)
2. **Configure and manage agents**: [Setup agents](agents-manage)
3. **Create your own agents** tailored for your use case: [Build custom agents](/en-us/copilot/security/developer/custom-agent-overview)
4. **Extend agents with plugins**: [Plugins](plugin-overview)
5. **Connect external systems**: [Connectors](connectors-overview)