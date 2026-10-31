---
layout: Conceptual
title: Use Microsoft Purview to manage data security & compliance for Anthropic Claude (Enterprise) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ai-claude-enterprise
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: arpitha-dhanapathi
ms.service: purview
ms.update-cycle: 180-days
ms.date: 2026-08-04T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.collection:
- msec-ai-copilot
description: Use Microsoft Purview to help you protect and manage data security and compliance protections for Anthropic Claude (Enterprise).
locale: en-us
document_id: 9edd8c72-dbec-5b24-a12f-9f997533fc4d
document_version_independent_id: 9edd8c72-dbec-5b24-a12f-9f997533fc4d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ai-claude-enterprise.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ai-claude-enterprise
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ai-claude-enterprise.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 6bca5ba4-eee8-dd2b-0b74-c5e03890a677
---

# Use Microsoft Purview to manage data security & compliance for Anthropic Claude (Enterprise) | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use the following sections to identify the [Microsoft Purview data security and compliance protections for generative AI apps](ai-microsoft-purview) with Anthropic Claude, and recommendations to get started to help you manage these AI interactions for security and compliance.

For setup information and prerequisites, see [Set up a connector to manage Anthropic Claude data](manage-anthropic-data). You must set up and configure the connector before Microsoft Purview can manage the AI interactions for Anthropic Claude.

Important

Managing these AI interactions with Microsoft Purview requires you to enable pay-as-you-go billing in your organization, which is subject to the Microsoft Purview billing model. For more information, see [Consent to use pay-as-you-go capabilities](purview-payg-consent-based-enablement) and [Learn about Microsoft Purview billing models](purview-billing-models).

Note

The Anthropic Claude connector is currently in preview.

## Capabilities supported

The following table lists the Microsoft Purview capabilities supported for Anthropic Claude.

| Capability or solution in Microsoft Purview | Supported for AI interactions |
| --- | --- |
| DSPM and DSPM for AI (classic) | **✓** |
| Auditing | **✓** |
| Data classification | **✓** |
| Sensitivity labels | **✕** |
| Encryption without sensitivity labels | **✕** |
| Data loss prevention | **✕** |
| Insider Risk Management | **✓** |
| Communication compliance | **✓** |
| eDiscovery | **✓** |
| Data Lifecycle Management | **✓** |
| Compliance Manager | **✓** |

### DSPM and DSPM for AI (classic)

Use [Data Security Posture Management](data-security-posture-management-learn-about) or [Data Security Posture Management for AI (classic)](dspm-for-ai) as your front door to discover, secure, and apply compliance controls for AI usage across your enterprise. Both DSPM versions use existing controls from Microsoft Purview information protection and compliance management with easy-to-use graphical tools and reports to quickly gain insights into AI use within your organization. With personalized recommendations, and one-click policies help you protect your data and comply with regulatory requirements.

###### AI app-specific information:

- Currently, there are no recommendations or one-click policies applicable to Anthropic Claude, but you can view and monitor the AI interactions by using the **Reports** page, **activity explorer** (**AI activities** tab), and the **Apps and agents** dashboard.
- Because agents for Anthropic Claude aren't currently supported, they aren't displayed in **AI observability**.

### Auditing and AI interactions

[Microsoft Purview Audit solutions](audit-solutions-overview) provide comprehensive tools for searching and managing audit records of activities performed across various Microsoft services by users and admins, and help organizations to effectively respond to security events, forensic investigations, internal investigations, and compliance obligations.

Like other activities, prompts and responses are [captured in the unified audit log](audit-log-activities). Events include how and when users interact with the AI app, and can include in which Microsoft 365 service the activity took place, and references to the files stored in Microsoft 365 that were accessed during the interaction. If these files have a sensitivity label applied, that's also captured.

These events flow into [activity explorer](ai-microsoft-purview-considerations#activity-explorer-events) in the **AI activities** tab in the current version of DSPM and in DSPM for AI, where the data from prompts and responses can be displayed. You can also use the **Audit** solution from the [Microsoft Purview portal](purview-portal) to search and find these auditing events.

For more information, see [Audit logs for Copilot and AI activities](audit-copilot).

## Recommended steps to get started

Use the following steps to get started with managing data security & compliance for AI interactions that use Anthropic Claude.

Note

These steps focus on managing a specific AI app or agent. For broader coverage that uses security objectives with guided workflows, use the current version of [Data Security Posture Management](data-security-posture-management-learn-about).

Because Data Security Posture Management for AI is your front door for securing and managing AI interactions, most of the following instructions use that solution:

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **DSPM for AI (classic)** with an account that has appropriate permissions. For example, an account that's a member of the **Microsoft Entra Compliance Administrator** group role. For more information, see [Permissions for Data Security Posture Management for AI - (classic)](ai-microsoft-purview-permissions).
2. If you haven't already set up and configured the connector to manage AI interactions for Anthropic Claude, see [Set up a connector to manage Anthropic Claude data](manage-anthropic-data).
3. After setting up the Anthropic Claude connector, wait at least a day for data to populate. Go to the **Reports** page to view information such as:

    - Total interactions over time.
    - Interaction trends by AI app.
4. Select **View details** for each of the report graphs to view detailed activities in activity explorer.

    From the filters, select the **AI app category** of **Enterprise AI apps** with the **App** filter of **Anthropic Claude**, and then use the other filters if you need to further refine the displayed data.

Regularly review the reports in DSPM for AI to determine whether you need to make changes, and use activity explorer for deeper analysis of how users are interacting with Anthropic Claude.