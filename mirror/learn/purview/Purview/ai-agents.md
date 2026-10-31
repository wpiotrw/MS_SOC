---
layout: Conceptual
title: Use Microsoft Purview to manage data security & compliance for AI agents | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ai-agents
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: minz
ms.service: purview
ms.date: 2026-05-27T00:00:00.0000000Z
ms.update-cycle: 180-days
audience: Admin
ms.topic: concept-article
ms.collection:
- highpri
- m365copilot
- msec-ai-copilot
description: Use Microsoft Purview to help you protect and manage data security and compliance protections for AI agents.
locale: en-us
document_id: e722fae6-d5db-991c-cd4a-ab2bcaccbc3b
document_version_independent_id: e722fae6-d5db-991c-cd4a-ab2bcaccbc3b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ai-agents.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ai-agents
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ai-agents.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 58aa4a5d-b9dc-1b56-9762-aa664008c819
---

# Use Microsoft Purview to manage data security & compliance for AI agents | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use the following table to see at a glance the [Microsoft Purview capabilities that are supported for AI interactions](ai-microsoft-purview) for AI agents from Microsoft AI apps and supported enterprise AI apps.

Managing these AI interactions with Microsoft Purview might require you to enable [pay-as-you-go billing](purview-billing-models) in your organization.

## Capabilities supported

AI agents typically have the same security and compliance protections for AI interactions as their parent AI app. Select the name of each app to learn the support details at the solution or capabilities level.

All the listed agents are supported by [Data Security Posture Management](data-security-posture-management-learn-about) and [Data Security Posture Management for AI (classic)](dspm-for-ai), and have their own dedicated **Apps and agents** page. Only Data Security Posture Management has an additional **AI observability** page that includes more information and support for [Agent 365](ai-agent-365). Use the dashboard from those pages to view how the agents and their apps are being used across your organization.

| AI app and agents | [Information protection for AI interactions](ai-microsoft-purview#microsoft-purview-strengthens-information-protection-for-ai-apps) | [Compliance management for AI interactions](ai-microsoft-purview#microsoft-purview-supports-compliance-management-for-ai-apps) |
| --- | --- | --- |
| [Microsoft 365 Copilot](ai-m365-copilot) agents | **✓** | **✓** |
| [Microsoft Security Copilot](ai-security-copilot) agents | **✓**^1^ | **✓** |
| [Copilot in Fabric](ai-copilot-fabric) agents | **✓**^1^ | **✓** |
| [Microsoft Copilot Studio](ai-copilot-studio) agents | **✓**^2^ | **✓** |
| [Microsoft Facilitator](ai-teams-facilitator) agents | **✓**^1^ | **✓** |
| [Channel Agent in Teams](ai-teams-channel-agent) agents | **✓**^3^ | **✓** |
| [Entra-registered](ai-entra-registered) agents | **✓** | **✓** |
| [Microsoft Foundry](ai-azure-foundry) agents | **✓**^2^ | **✓** |
| [ChatGPT Enterprise](ai-chatgpt-enterprise) agents | **✕**^4^ | **✕** |
| [Anthropic Claude (Enterprise)](ai-claude-enterprise) agents | **✕** | **✕** |

**Footnotes**

The following capabilities are supported:

^1^ Data classification

^2^ Data classification, sensitivity labels, data loss prevention, Insider Risk Management

^3^ Data classification, sensitivity labels, data loss prevention

^4^ Data classification, Insider Risk Management