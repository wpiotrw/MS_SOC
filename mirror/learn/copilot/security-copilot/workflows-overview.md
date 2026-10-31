---
layout: Conceptual
title: Microsoft Security Copilot in your workflows | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/workflows-overview
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about agents, plugins, connectors, and promptbooks in Microsoft Security Copilot and how they work together in your security workflows.
ms.date: 2026-05-01T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: overview
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: partner-contribution
ms.reviewer: 
search.audiencetype: Admin
search.appverid: MET150
f1.keywords: NOCSH
audience: ITPro
locale: en-us
document_id: f49270cb-163e-6ad0-2481-fa74aab825cc
document_version_independent_id: f49270cb-163e-6ad0-2481-fa74aab825cc
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/workflows-overview.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: workflows-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/workflows-overview.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: 26143eba-4117-f724-cfef-205c4fcfcabe
---

# Microsoft Security Copilot in your workflows | Microsoft Learn

This article provides an overview of the key personas and how you can discover, set up and use agents, and the related components in the workflow in Microsoft Security Copilot. Advanced users and developers can also build and publish custom agents tailored to their organization’s needs.

## Start with agents

In newer onboarding experiences, agents are the primary way to begin working in Security Copilot.

Agents help you:

- Automate investigation workflows
- Perform repeatable tasks
- Guide analysis using structured steps

You can still use prompts and promptbooks alongside agents as needed.

## Personas

Security Copilot agents span across three key personas:

- **Administrators** - Discover and determine which agents to install, configure plugins, and review usage and success metrics of the agents.
- **End users** (analysts or data security team; or IT admins) - Interact with agents or prompts by using workflow outputs and providing feedback.

    For more information on use cases across personas, see [Use cases](use-case-role-overview).
- **Developers** - Build and publish agents for internal use or broader organizational deployment. For more information on the developer documentation, see [Build custom agents](/en-us/copilot/security/developer/custom-agent-overview).

## Work with agents, plugins, and connectors

Microsoft Security Copilot uses these capabilities to automate and extend security operations. Understanding how these components work together helps you choose the right approach for each scenario.

| Scenario | Recommended approach | Guidance |
| --- | --- | --- |
| Getting started / investigation | Use **agents** or start a chat session with **prompts** | - Agents: Begin with prebuilt or recommended agents - Prompts: Start a session from **All history** → **New session** |
| Ad-hoc analysis | Use **prompts** and **promptbooks** | [Prompting in Security Copilot](prompting-security-copilot) |
| Repeatable workflow & integration | Use **agents**, **plugins**, and **connectors** | [Plugins](plugin-overview) and [Connectors](connectors-overview) |
| Automation | Use **agents** | - Review key [agent terminology](agents-overview#agent-terminology)- Explore [Discover agents](discover-agents)- Review [Use cases](use-case-role-overview) |
| Advanced workflows | Build **custom agents**, **promptbooks**, and **custom plugins** | - Agents: [Build custom agents](/en-us/copilot/security/developer/custom-agent-overview)- Promptbooks: [Build your own promptbooks](build-promptbooks)- Plugins: [Build custom plugins](custom-plugins) |

## Combine agents and prompts

You can use agents together with prompts as part of your workflow:

- Start with an agent for structured workflows
- Use prompts to explore results or investigate further
- Return to agents for repeatable execution

This flexibility allows you to adapt Security Copilot to your workflow and operational needs.

### Agents

An agent is an AI-driven security assistant or workflow that can autonomously execute and orchestrate tasks on behalf of security teams. Each agent has a defined goal such as triaging phishing alerts, generating a threat intelligence briefing, or remediating vulnerabilities.

You can discover Microsoft-built agents, deploy partner agents, or build your own custom agents.

Agents can be:

- **[Interactive](/en-us/copilot/security/developer/interactive-agents-overview)** – respond to user input in real time
- **Automated** – triggered by events or schedules

### Plugins

When an agent needs information or needs to take action, it uses a plugin. A plugin connects Security Copilot to a security product or service and provides access to data and actions.

For example:

- Retrieve alerts from Microsoft Sentinel
- Query threat intelligence data

A Security Owner can enable or disable plugins, and developers can build custom plugins.

For more information, see [Plugins overview](plugin-overview).

### Connectors

Connectors integrate Security Copilot with external systems and workflows.

Connectors can:

- Trigger agents
- Run prompts
- Start automation workflows

For more information, see [Connectors overview](connectors-overview).

## Custom agents

If you are a developer, you can build and publish Security Copilot custom agents tailored to your organization's needs.

Security Copilot supports building, testing, and publishing agents for internal or organizational use.

For more information, see the [Agent development overview](/en-us/copilot/security/developer/custom-agent-overview) developer content documentation.

## Promptbooks

A promptbook is a reusable, multi-step workflow made up of natural language prompts. It guides Security Copilot through structured investigations such as analyzing incidents or generating reports.

Promptbooks can:

- Include multiple prompts
- Reference plugins or skills
- Be reused across workflows

Analysts can run promptbooks manually or as part of agent-driven workflows.

For more information, see [Promptbooks](using-promptbooks).