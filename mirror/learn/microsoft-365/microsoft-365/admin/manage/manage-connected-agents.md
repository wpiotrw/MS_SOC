---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Manage connected agents in the Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-connected-agents?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: View, add, remove, and make connected agents available to users in the Microsoft 365 admin center.
ai-usage: ai-assisted
f1.keywords:
- NOCSH
ms.author: mkaur
author: mduelae
manager: tapanm
ms.date: 2026-09-17T00:00:00.0000000Z
ms.update-cycle: 180-days
audience: Admin
ms.topic: concept-article
ms.service: microsoft-365-copilot
ms.subservice: agent-management
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
ms.custom:
- AdminSurgePortfolio
- AdminTemplateSet
search.appverid:
- BCS160
- MET150
- MOE150
locale: en-us
document_id: f3f52818-911e-c04b-2fa9-9b6ac088e9f4
document_version_independent_id: f3f52818-911e-c04b-2fa9-9b6ac088e9f4
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/manage-connected-agents.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/manage-connected-agents
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/manage-connected-agents.md
platformId: 4ab3aaf6-de6b-32a3-d519-c6aebb64f34c
---

# Manage connected agents in the Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn

On an agent's **Connected Agents** tab, you can view agents that provide information and answers when users interact with the primary agent. You can also add connected agents to Researcher and Sales. For other agents, you can view the connections configured by the agent developer, but you can't add or remove them.

## What are connected agents

Connected agents are other Copilot-enabled agents that a primary agent can invoke during a conversation. When a user's request falls within a connected agent's domain, the primary agent can delegate the request to that agent.

Important

If a connected agent is external to your organization, the primary agent can include information from its context in the prompt it sends to the connected agent. The primary agent determines what information is needed for the connected agent to respond accurately. Review the connected agent and your organization's data policies before making it available to users.

For connected agents to work, both the primary agent and the connected agent must be acquired for the user. You can install each agent for users from the Microsoft 365 admin center.

## Key details

- **Agents you can connect** - You can add connected agents to Researcher and Sales. For other primary agents, you can only view the connections configured by the agent developer.
- **Types of agents** - Primary agents can connect to declarative agents and agents that are available over the Agent2Agent (A2A) protocol.
- **Limit** - An agent can connect to up to 10 other agents.
- **Developer-configured agents** - You can't remove connected agents configured by the agent developer.
- **User access** - Both the primary agent and each connected agent must be acquired for the user.

## Connect agents to Researcher or Sales

1. In the [Microsoft 365 admin center](https://admin.microsoft.com/), go to **Agents** &gt; **All agents**.
2. Select **Researcher** or **Sales**, and then select the **Connected Agents** tab.

    [![Screenshot showing how to connect an agent with Researcher in the Microsoft 365 admin center.](../../media/agents/connect-agent.png)](../../media/agents/connect-agent.png#lightbox)
3. Select **+ Connect agents**.
4. In the **Select agent to connect** pane:

    - Use the search bar to find agents.
    - Check the box next to the agents you want to connect.
5. Select **Save** to confirm.

## Make connected agents available to users

Both the primary agent and its connected agents must be acquired for a user before the primary agent can invoke them. To review and install a connected agent:

1. On the **Connected Agents** tab, select an agent from the list. The agent's details page opens.
2. Install the agent for the users who need access.

Install the primary agent and each connected agent for the users who need them.

## Manage connected agents

- **Remove an agent** - From the **Connected Agents** list, select an agent that an admin added, and then select **Remove**. You can't remove an agent configured by the agent developer.
- **Reset to default** - Use this option to remove all admin-added connections and restore the connections configured by the agent developer.