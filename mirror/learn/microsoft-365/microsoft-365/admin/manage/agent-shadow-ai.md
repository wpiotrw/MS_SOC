---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Understand Shadow AI in Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-shadow-ai?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Understand Shadow AI in Microsoft 365 admin center.
f1.keywords:
- NOCSH
ms.author: mkaur
author: mduelae
manager: tapanm
ms.date: 2026-08-25T00:00:00.0000000Z
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
document_id: 0e880142-4961-265f-7bc9-311992abccd8
document_version_independent_id: 0e880142-4961-265f-7bc9-311992abccd8
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/agent-shadow-ai.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/agent-shadow-ai
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/agent-shadow-ai.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/8b9ae643-2e85-42b8-beb2-eef4bae8c4bc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e047e27d-b5f3-43a8-b4b0-4f6dca95e7c9
platformId: 1ccb3c89-23f2-f066-45a4-c40badf9edb4
---

# Understand Shadow AI in Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn

Important

This feature is part of [Frontier preview program](https://www.microsoft.com/microsoft-365-copilot/frontier-program). Frontier connects you directly with Microsoft's latest AI innovations. Frontier previews are subject to the existing preview terms of your customer agreements. As these features are still in development, their availability and capabilities might change over time.

The Shadow AI page in the Microsoft 365 admin center helps IT administrators discover, monitor, and govern unmanaged AI agents used within their organization.

This preview capability provides a dedicated view for detecting and governing unapproved AI agents such as OpenClaw, and enables administrators to take governance actions to maintain security and compliance.

Note

Shadow AI is currently in public preview. Features, supported agents, and behaviors might change before general availability.

## Prerequisites

To use Shadow AI detection and governance, you need:

- Opt in to the [Frontier preview experience](https://www.microsoft.com/microsoft-365-copilot/frontier-program) in the Microsoft 365 admin center.
- Enable Microsoft Defender for Endpoint on devices for shadow agent detection. For more information, see [Local AI agent discovery with Microsoft Defender for Endpoint (Preview)](/en-us/defender-endpoint/local-agent-discovery-overview).
- Microsoft 365 E5 license to view Shadow AI Agents
- [Microsoft Intune](/en-us/intune/fundamentals/what-is-intune) enrollment for managed Windows devices.
- Enable Global Secure Access (GSA) for your tenant and enrolled devices to view additional metadata on how detected agents are being used. For more information on GSA, see [Tutorial: Enable Internet Access traffic forwarding](/en-us/entra/global-secure-access/tutorial-internet-access-enable-traffic-forwarding).
- At least one of the following roles:

    - [Security Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#security-administrator).
    - [AI Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#ai-administrator).
    - [Global Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader).
    - [Security Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#security-reader).
    - [Security Operator](/en-us/entra/identity/role-based-access-control/permissions-reference#security-operator).
    - [Reports Reader](/en-us/entra/identity/role-based-access-control/permissions-reference#reports-reader).
    - [User Experience Success Manager](/en-us/entra/identity/role-based-access-control/permissions-reference#user-experience-success-manager).
    - [Intune Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#intune-administrator).

## What is Shadow AI?

Shadow AI refers to consumer-facing AI applications and standalone agents deployed across your organization without IT visibility or approval. These agents can operate autonomously on user devices, creating blind spots in your security and compliance posture. While these agents can boost productivity, unmanaged usage introduces significant risks, such as the following:

- Data leakage.
- Compliance violations.
- Security vulnerabilities.
- Lack of auditability and governance.

The Shadow AI experience helps administrators identify and manage these risks without disrupting legitimate business workflows.

## Available features

During public preview, the Shadow AI experience allows admins the following capabilities:

| Agent | Detection | Blocking |
| --- | --- | --- |
| OpenClaw | Available | Available |
| ChatGPT Desktop | Available | Not available |
| Ollama Desktop | Available | Not available |
| Poe Desktop | Available | Not available |
| Claw/ZeroClaw | Available | Not available |
| OpenCode | Available | Not available |
| Claude Desktop | Available | Not available |

Note

Shadow AI blocking currently apply only to managed Windows devices enrolled with Microsoft Intune.

## Access the Shadow AI (Frontier) agent

The **Shadow AI (Frontier)** page in the Microsoft 365 admin center is a dedicated experience separate from the **All agents** page. It focuses exclusively on unmanaged AI agents that require detection and governance.

To access the **Shadow AI (Frontier)** page in the Microsoft 365 admin center, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. Select **Agents** &gt; **Shadow AI**. The **Shadow AI (Frontier)** page displays a list of known Shadow AI agents that can be detected in your environment.

### View Shadow AI agent details

1. To view Shadow AI agent details, such as OpenClaw details, select the Shadow AI agent from the list of agents in the **Shadow AI (Frontier)** page. The details pane opens for the selected Shadow AI agent.
2. Confirm **Details** is selected. The **Details** pane provides the following agent information:

    - **Details** tile:

        - **First accessed**: Date the agent was first accessed.
        - **Most recent activity**: Date the agent was last used.
        - **Last scanned**: Date the agent was last detected.
    - **Detections** tile:

        - **Devices**: Count of devices that this agent is detected running on.
        - **Users**: Unique count of users that are detected using this agent.
    - **Security policies** tile: Displays if a blocking Intune policy has been applied to prevent this agent from running.
    - **Total traffic** tile:

        - **Unique endpoints**: Number of unique fully qualified domain names (FQDN) the agent accessed.
        - **Requests**: Number of network requests made by the agent.
        - **Data sent**: Network traffic sent by the agent.
        - **Data received**: Network traffic received by the agent.

Note

The following fields and tiles will only be populated with data if Global Secure Access (GSA) has been enabled:

- **Total traffic** tile.
- **Users** field.
- **Most recent activity** field.
- **Last scanned** field.

### View detected devices for a Shadow AI agent

You can view detected devices in the Shadow AI agent details pane by following these steps:

1. In the Shadow AI agent details pane, select the **Detected devices** tab.

     A list of detected devices is displayed.
2. In **Detected devices**, you can search for a specific device name. You can also see the following device data:

    - **Device name**: Name of the device.
    - **Model**: Type of device (Desktop, Virtual Machine, Server, Laptop, etc.)
    - **Operating system**: Operating system installed on the device.
    - **Last Seen**: The last time Microsoft Defender detected the agent on the device.

### Blocking a Shadow AI agent

After detection is enabled and the Shadow AI agent is identified in your environment, you can block it to prevent execution on managed devices. When a Shadow AI agent is blocked, such as OpenClaw, it blocks common ways of running it by creating a new Microsoft Intune policy that automatically propagates to all managed Windows devices enrolled in Intune.

To view the policy details, search for the policy name **A365 - Block OpenClaw** in the article [Assign policies in Microsoft Intune](/en-us/intune/device-configuration/assign-device-profile). Depending on how Intune is configured in your organization, this Intune policy update could take anywhere from 15 minutes up to 8 hours to apply. Full policy details, including when Intune policy applies, can be found in Intune. Lastly, policies can also be edited in Intune to add additional controls.

To block a Shadow AI agent, follow these steps:

1. In the Shadow AI agent details pane, select **Security policies**.
2. Under **Security policies**, select **Block** &gt; **Apply Policies**.