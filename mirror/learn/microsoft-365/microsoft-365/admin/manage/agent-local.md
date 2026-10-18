---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Understand Local Agents in Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-local?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Understand Local Agents in Microsoft 365 admin center.
f1.keywords:
- NOCSH
ms.author: mkaur
author: mduelae
manager: tapanm
ms.date: 2026-09-04T00:00:00.0000000Z
ms.update-cycle: 180-days
audience: Admin
ms.topic: concept-article
ms.service: microsoft-365-copilot
ms.subservice: agent-management
ms.localizationpriority: medium
ms.collection:
- Tier2
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
document_id: a48f9fa4-fcaf-6a1d-b0ba-598bafbbbe2a
document_version_independent_id: a48f9fa4-fcaf-6a1d-b0ba-598bafbbbe2a
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/agent-local.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/agent-local
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/agent-local.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f97c0bd5-0580-4767-b5c8-219bede529e2
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c61bdaa9-b56c-4fa3-873a-58cafacba4f6
platformId: 8f99cad9-54dd-da67-ee05-78598b51af9f
---

# Understand Local Agents in Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn

Important

This feature is part of [Frontier preview program](https://www.microsoft.com/microsoft-365-copilot/frontier-program). Frontier connects you directly with Microsoft's latest AI innovations. Frontier previews are subject to the existing preview terms of your customer agreements. As these features are still in development, their availability and capabilities might change over time.

The Local agents page in the Microsoft 365 admin center helps IT administrators discover, monitor, and govern unmanaged AI agents used within their organization.

This preview capability provides a dedicated view for viewing how these local agents, which include local agentic developer tools are currently used within their organization.

Note

Local Agents is currently in public preview. Features, supported agents, and behaviors might change before general availability.

## Prerequisites

To use Local Agents detection and governance, you need:

- A Microsoft 365 E3 license to view Local Agents.
- At least one of the following roles:

    - [Security Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator).
    - [AI Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#ai-administrator).
    - [Global Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader).
    - [Security Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader).
    - [Security Operator](/en-us/entra/identity/role-based-access-control/permissions-reference#security-operator).
    - [Reports Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#reports-reader).
    - [User Experience Success Manager](/en-us/entra/identity/role-based-access-control/permissions-reference#user-experience-success-manager).
    - [Intune Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#intune-administrator).
- [Microsoft Intune](/en-us/intune/fundamentals/what-is-intune) enrollment for managed Windows devices.
- Opt in to the [Frontier preview experience](https://www.microsoft.com/microsoft-365-copilot/frontier-program) in the Microsoft 365 admin center.
- To view more metadata about how detected agents are being used, enable Global Secure Access (GSA) for your tenant and enrolled devices by using a Microsoft Entra Internet Access (IA) license, Microsoft Entra Suite license, or Microsoft 365 E7 license. For more information, see [Tutorial: Enable Internet Access traffic forwarding](/en-us/entra/global-secure-access/tutorial-internet-access-enable-traffic-forwarding).

## What are Local Agents?

Local Agents are developer-controlled tools and extensions—such as IDE plugins, CLIs, and code editors—intentionally integrated into development workflows with explicit configuration. These agents include extensions for VS Code and similar developer-focused applications built to enhance productivity during the software development lifecycle.

**How Local Agents differs from Shadow AI**: Local Agents are intentionally chosen developer tools managed within known environments, while Shadow AI consists of unmanaged, autonomous applications deployed without organizational awareness.

## Available features

During public preview, the Local Agents experience allows admins to detect the following local agents:

| Name | Detection | Blocking |
| --- | --- | --- |
| Antigravity CLI | Available | Not Available |
| Antigravity Desktop | Available | Not Available |
| Antigravity IDE | Available | Not Available |
| Claude Code | Available | Not Available |
| Codex CLI | Available | Not Available |
| Codex Desktop | Available | Not Available |
| Cursor | Available | Not Available |
| Devin Desktop | Available | Not Available |
| GitHub Copilot App | Available | Not Available |
| GitHub Copilot CLI | Available | Not Available |
| Junie CLI | Available | Not Available |
| Kiro CLI | Available | Not Available |
| Kiro IDE | Available | Not Available |
| Microsoft Scout | Available | Not Available |
| Warp | Available | Not Available |
| Windsurf | Available | Not Available |
| Gemini CLI | Available | Available |
| VSCode Claude Code Extension | Available | Available |
| VSCode Cline Extension | Available | Available |
| VSCode Codex Extension | Available | Available |
| VSCode Gemini Code Assist Extension | Available | Available |
| VSCode GitHub Copilot Extension | Available | Available |
| VSCode Roo Code Extension | Available | Available |

Note

Shadow AI detection and blocking currently apply only to managed Windows devices enrolled with Microsoft Intune.

## Access the Local Agent (Frontier) page

The Local Agents (Frontier) page in the Microsoft 365 admin center is a dedicated experience separate from the **All agents** page. It focuses exclusively on unmanaged AI agents that require detection and governance.

To access the Local Agents (Frontier) page in the Microsoft 365 admin center, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. Select **All Agents** &gt; **Local Agents (Frontier)**. The Local Agents (Frontier) page displays a list of known local agents that you can detect in your environment.

## View the details of a local agent

Use the following step to view the details for a local agent:

1. Select the agent from the **Local Agents** list in the **Local Agents (Frontier)** page. The **Details** pane opens for the selected local agent.
2. Select the **Details** tab. The **Details** pane provides the following agent information:

    - **Details** tile:

        - **First accessed**: Date the agent was first accessed.
        - **Most recent activity**: Date the agent was last used.
        - **Last scanned**: Date the agent was last detected.
    - **Detections** tile:

        - **Devices**: Count of devices that this agent is detected running on.
        - **Users**: Unique count of users that are detected using this agent.
    - **Total traffic** tile:

        - **Unique endpoints**: Number of unique fully qualified domain names (FQDN) the agent accessed.
        - **Requests**: Number of network requests made by the agent.
        - **Data sent**: Network traffic sent by the agent.
        - **Data received**: Network traffic received by the agent.

Note

The following fields are populated only if Global Secure Access (GSA) is enabled:

- Users
- Most recent activity
- Last scanned
- Unique endpoints
- Requests
- Data sent
- Data received

## View detected devices for a Local Agent

You can view detected devices for an agent in the Local Agent details pane. Follow these steps:

1. Select the agent from the **Local Agents** list in the **Local Agents (Frontier)** page. The **Details** pane opens for the selected local agent.
2. Select the **Detected devices** tab. You see a list of detected devices.
3. View devices listed in the device table, or search for a specific device name.

The **Detected devices** table provides the following device data:

| Device information | Description |
| --- | --- |
| Device name | Name of the device |
| Model | Type of device, such as Desktop, Virtual Machine, Server, or Laptop. |
| Operating system | Operating system installed on the device. |
| Last Seen | The last time Microsoft Defender detected the agent on the device. |

### Block a Local agent

After you enable detection and identify the Local AI agent in your environment, you can block it to prevent execution on managed devices. When you block a Local AI agent, it blocks common ways of running it by creating a new Microsoft Intune policy that automatically propagates to all managed Windows devices enrolled in Intune.

To view the policy details, search for the policy name **A365 - Block OpenClaw** in the article [Assign policies in Microsoft Intune](/en-us/intune/device-configuration/assign-device-profile). Depending on how Intune is configured in your organization, this Intune policy update could take anywhere from 15 minutes up to 8 hours to apply. Full policy details, including when Intune policy applies, can be found in Intune. You can also edit policies in Intune to add more controls.

To block a Local AI agent, follow these steps:

1. In the Local AI agent details pane, select **Security policies**.
2. Under **Security policies**, select **Block agent** &gt; **Apply Policies**.

### Block and unblock VS Code extension agents

Block agents that run as Visual Studio Code extensions by using a VS Code extension policy. Deploy the policy to managed devices and enforce it by using Visual Studio Code.

You can view blocked VS Code extension agents in Visual Studio Code under the allowed extension list. For more information, see [Manage extensions in enterprise environments](https://code.visualstudio.com/docs/enterprise/extensions).

### Blocking and unblocking Node.js–based agents

Node.js–based agents share a single run type, so blocking one blocks them all. When you block any of the following agents, you block all of them:

- OpenClaw
- QClaw
- Claw/Nanobot
- Gemini CLI

Blocking a Node.js–based agent blocks all agents and processes of that run type on managed devices. Ensure no legitimate business processes depend on these agents before applying the policy. [Learn more about this Intune Policy](/en-us/intune/device-security/security-baselines/ref-openclaw-settings). Removing a block on any Node.js–based agent removes the Node.js block for all other Node.js–based agents, not just the one you selected.

## Additional information

- [Shadow AI in Microsoft 365 admin center](/en-us/microsoft-365/admin/manage/agent-shadow-ai)