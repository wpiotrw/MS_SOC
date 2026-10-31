---
layout: Conceptual
title: Microsoft Purview data security and compliance protections for Microsoft 365 Copilot and other generative AI apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ai-microsoft-purview
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: libarson
ms.service: purview
ms.date: 2026-05-27T00:00:00.0000000Z
ms.update-cycle: 180-days
audience: Admin
ms.topic: concept-article
ms.collection:
- highpri
- m365copilot
- msec-ai-copilot
description: Use Microsoft Purview to help you protect and manage data security and compliance protections for generative AI apps such as Microsoft 365 Copilot, Security Copilot, Microsoft Facilitator, ChatGPT Enterprise, and more.
locale: en-us
document_id: e5cc535a-91ec-4c5c-1e26-0c2497e55144
document_version_independent_id: e5cc535a-91ec-4c5c-1e26-0c2497e55144
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ai-microsoft-purview.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ai-microsoft-purview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ai-microsoft-purview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 670307b2-8f08-abcb-5264-eb436628274d
---

# Microsoft Purview data security and compliance protections for Microsoft 365 Copilot and other generative AI apps | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use Microsoft Purview to mitigate and manage the risks associated with AI usage, and implement corresponding protection and governance controls.

The following sections on this page provide an overview of Data Security Posture Management for AI and the Microsoft Purview capabilities that provide additional data security and compliance controls to accelerate your organization's adoption of Copilots and agents, and other generative AI apps.

In some Microsoft Purview solutions, you might see the supported AI apps grouped by the following category names:

- **Copilot experiences and agents** or **Microsoft Copilot experiences** for supported Copilots and agents that include:

    - Microsoft 365 Copilot
    - Security Copilot
    - Copilot in Fabric
    - Copilot Studio
- **Enterprise AI apps** for non-Copilot AI apps and agents connected to your organization through Entra registration, data connectors, Microsoft Foundry, and other methods, and include:

    - Microsoft Foundry
    - Entra-registered AI apps
    - Anthropic Claude (Enterprise)
    - ChatGPT Enterprise
- **Other AI apps** that are detected through browser activity and categorized as "Generative AI" in the Defender for Cloud Apps catalog. This category can include AI apps and agents from the other two categories but also uniquely includes AI apps and agents from third-party LLMs, such as:

    - ChatGPT
    - Google Gemini
    - Microsoft Copilot (consumer version)
    - DeepSeek

For a breakdown of Microsoft Purview security and compliance supported capabilities for AI interactions by app, see the additional pages identified in the following table. Where these AI apps support agents, they inherit the same security and compliance capabilities as their parent AI app. However, for a quick summary, see [Use Microsoft Purview to manage data security & compliance for AI agents](ai-agents).

| Copilot experiences and agents | Enterprise AI apps | Other AI apps |
| --- | --- | --- |
| [Microsoft 365 Copilot & Microsoft 365 Copilot Chat](ai-m365-copilot) | [Entra-registered AI apps](ai-entra-registered) | [Other AI apps](ai-other-apps) |
| [Microsoft 365 Copilot Cowork](ai-copilot-cowork) | [Microsoft Foundry](ai-azure-foundry) |  |
| [Microsoft Security Copilot](ai-security-copilot) | [ChatGPT Enterprise](ai-chatgpt-enterprise) |  |
| [Copilot in Fabric](ai-copilot-fabric) | [Anthropic Claude (Enterprise)](ai-claude-enterprise) |  |
| [Microsoft Copilot Studio](ai-copilot-studio) |  |  |
| [Microsoft Facilitator](ai-teams-facilitator) |  |  |
| [Channel Agent in Teams](ai-teams-channel-agent) |  |  |

For a list of supported Microsoft Purview security and compliance supported capabilities for Microsoft Agent 365, see [Use Microsoft Purview to manage data security & compliance for Microsoft Agent 365](ai-agent-365).

If you're new to Microsoft Purview, you might also find an overview of the product helpful: [Learn about Microsoft Purview](purview).

## DSPM and DSPM for AI (classic)

Use [Data Security Posture Management](data-security-posture-management-learn-about) or [Data Security Posture Management for AI (classic)](dspm-for-ai) as your front door to discover, secure, and apply compliance controls for AI usage across your enterprise. Both DSPM versions use existing controls from Microsoft Purview information protection and compliance management with easy-to-use graphical tools and reports to quickly gain insights into AI use within your organization. With personalized recommendations, and one-click policies help you protect your data and comply with regulatory requirements.

## Microsoft Purview strengthens information protection for AI apps

Because of the power and speed AI can proactively surface content, generative AI amplifies the problem and risk of oversharing or leaking data. Learn how information protection capabilities from Microsoft Purview can help to strengthen your existing data security solutions.

### Sensitivity labels and AI interactions

AI apps that Microsoft Purview support use [existing controls to ensure that data stored in your tenant is never returned](/en-us/microsoft-365-copilot/microsoft-365-copilot-privacy#how-does-microsoft-365-copilot-protect-sensitive-organizational-data) to the user or used by a large language model (LLM) if the user doesn't have access to that data. When the data has [sensitivity labels](sensitivity-labels) from your organization applied to the content, there's an extra layer of protection:

- When a file is open in Word, Excel, PowerPoint, or similarly an email or calendar event is open in Outlook, the sensitivity of the data is displayed to users in the app with the label name and content markings (such as header or footer text) that have been configured for the label. [Loop components and pages also support the same sensitivity labels](sensitivity-labels-loop).
- When the sensitivity label applies encryption, users must have the [EXTRACT usage right](ai-m365-copilot-considerations#copilot-honors-existing-protection-with-the-extract-usage-right), as well as VIEW, for the AI apps to return the data.
- This protection extends to data stored outside your Microsoft 365 tenant when it's open in an Office app (data in use). For example, local storage, network shares, and cloud storage.

Tip

If you haven't already, we recommend you enable sensitivity labels for SharePoint and OneDrive and also familiarize yourself with the file types and label configurations that these services can process. When sensitivity labels aren't enabled for these services, the encrypted files that Copilot and agents can access are limited to data in use from Office apps on Windows.

For instructions, see [Enable sensitivity labels for Office files in SharePoint and OneDrive](sensitivity-labels-sharepoint-onedrive-files).

If you're not already using sensitivity labels, see [Get started with sensitivity labels](get-started-with-sensitivity-labels).

### Encryption without sensitivity labels and AI interactions

Even if a sensitivity label isn't applied to content, services and products might use the encryption capabilities from the Azure Rights Management service. As a result, AI apps can still check for the VIEW and EXTRACT usage rights before returning data and links to a user, but there's no automatic inheritance of protection for new items.

Tip

You'll get the best user experience when you always use sensitivity labels to protect your data, and encryption is applied by a label.

Examples of products and services that can use the encryption capabilities from the Azure Rights Management service without sensitivity labels:

- Microsoft Purview Message Encryption
- Microsoft Information Rights Management (IRM)
- Microsoft Rights Management connector
- Microsoft Rights Management SDK

For other encryption methods that don't use the Azure Rights Management service:

- S/MIME protected emails won't be returned by Copilot, and Copilot isn't available in Outlook when an S/MIME protected email is open.
- Password-protected documents can't be accessed by AI apps unless they're already opened by the user in the same app (data in use). Passwords aren't inherited by a destination item.

As with other Microsoft 365 services, such as eDiscovery and search, items encrypted with [Microsoft Purview Customer Key](customer-key-overview) or [your own root key (BYOK)](/en-us/azure/information-protection/byok-price-restrictions) are supported and eligible to be returned by Copilot.

### Data loss prevention and AI interactions

[Microsoft Purview Data Loss Prevention](dlp-learn-about-dlp) (DLP) helps you identify sensitive items across Microsoft 365 services and endpoints, monitor them, and helps protect against leakage of those items. It uses deep content inspection and contextual analysis to identify sensitive items and it enforces policies to protect sensitive data such as financial records, health information, or intellectual property.

Windows computers that are [onboarded to Microsoft Purview](device-onboarding-overview) can be configured for Endpoint data loss prevention (DLP) policies that warn or block users from sharing sensitive information with third-party generative AI sites that are accessed via a browser. For example, a user is prevented from pasting credit card numbers into ChatGPT, or they see a warning that they can override. For more information about the supported DLP actions and which platforms support them, see the first two rows in the table from [Endpoint activities you can monitor and take action on](endpoint-dlp-learn-about#endpoint-activities-you-can-monitor-and-take-action-on).

### Insider Risk Management and AI interactions

[Microsoft Purview Insider Risk Management](insider-risk-management) helps you detect, investigate, and mitigate internal risks such as IP theft, data leakage, and security violations. It leverages machine learning models and various signals from Microsoft 365 and third-party indicators to identify potential malicious or inadvertent insider activities. The solution includes privacy controls like pseudonymization and role-based access, ensuring user-level privacy while enabling risk analysts to take appropriate actions.

Use the [Risky AI usage policy template](insider-risk-management-policy-templates#risky-ai-usage) to detect risky usage that includes prompt injection attacks and accessing protected materials. Insights from these signals are integrated into Microsoft Defender XDR to provide a comprehensive view of AI-related risks.

### Data classification and AI interactions

Microsoft Purview data classification provides a comprehensive framework for identifying and tagging sensitive data across various Microsoft services, including Office 365, Dynamics 365, and Azure. Classifying data is often the first step to ensure compliance with data protection regulations and safeguard against unauthorized access, alteration, or destruction. You can use built-in system classifications or create your own.

Sensitive information types and trainable classifiers can be used to find sensitive data in user prompts and responses when they use AI apps. The resulting information then surfaces in [Microsoft Purview Reports overview](purview-reports) and [activity explorer](ai-microsoft-purview-considerations#activity-explorer-events) in DSPM for AI and the **AI activities** tab in activity explorer from the preview version of DSPM.

## Microsoft Purview supports compliance management for AI apps

Interactions using supported AI apps can be monitored for each user in your tenant. As such, together with data classification, you can use Microsoft Purview's auditing, communication compliance, eDiscovery with content search, and automatic retention and deletion capabilities from Data Lifecycle Management to manage this AI usage.

### Auditing and AI interactions

[Microsoft Purview Audit solutions](audit-solutions-overview) provide comprehensive tools for searching and managing audit records of activities performed across various Microsoft services by users and admins, and help organizations to effectively respond to security events, forensic investigations, internal investigations, and compliance obligations.

Like other activities, prompts and responses are [captured in the unified audit log](audit-log-activities). Events include how and when users interact with the AI app, and can include in which Microsoft 365 service the activity took place, and references to the files stored in Microsoft 365 that were accessed during the interaction. If these files have a sensitivity label applied, that's also captured.

These events flow into [activity explorer](ai-microsoft-purview-considerations#activity-explorer-events) in the **AI activities** tab in the current version of DSPM and in DSPM for AI, where the data from prompts and responses can be displayed. You can also use the **Audit** solution from the [Microsoft Purview portal](purview-portal) to search and find these auditing events.

For more information, see [Audit logs for Copilot and AI activities](audit-copilot).

### Communication compliance and AI interactions

[Microsoft Purview Communication Compliance](communication-compliance) provides tools to help you detect and manage regulatory compliance and business conduct violations across various communication channels, which include user prompts and responses for AI apps. It's designed with privacy by default, pseudonymizing usernames and incorporating role-based access controls. The solution helps identify and remediate inappropriate communications, such as sharing sensitive information, harassment, threats, and adult content.

To learn more about using communication compliance policies for AI apps, see [Configure a communication compliance policy to detect for generative AI interactions](communication-compliance-copilot).

### eDiscovery with content search and AI interactions

[Microsoft Purview eDiscovery](edisc) lets you identify and deliver electronic information that can be used as evidence in legal cases. The eDiscovery tools in Microsoft Purview support searching for content in Exchange Online, OneDrive for Business, SharePoint Online, Microsoft Teams, Microsoft 365 Groups, and Viva Engage teams. You can then prevent the information from deletion and export the information.

Because user prompts and responses for AI apps are stored in a user's mailbox, you can create a case and use [search](edisc-search-query) when a user's mailbox is selected as the source for a search query. For example, select and retrieve this data from the source mailbox by selecting from the query builder **Add condition** &gt; **Type** &gt; **Contains any of** &gt; **Edit** &gt; *Copilot activity*. This query condition includes all Copilot and other AI application activity.

After the search is refined, you can export the results or add to a [review set](edisc-review-set-manage). You can review and export information directly from the review set.

For more information about identifying and deleting user AI interaction data, see [Search for and delete Copilot data in eDiscovery](edisc-search-copilot-data).

### Data Lifecycle Management and AI interactions

[Microsoft Purview Data Lifecycle Management](data-lifecycle-management) provides tools and capabilities to manage the lifecycle of organizational data by retaining necessary content and deleting unnecessary content. These tools ensure compliance with business, legal, and regulatory requirements.

Use [retention policies](retention) to automatically retain or delete user prompts and responses for AI apps. For detailed information about this retention works, see [Learn about retention for Copilot & AI apps](retention-policies-copilot).

As with all retention policies and holds, if more than one policy for the same location applies to a user, the [principles of retention](retention#the-principles-of-retention-or-what-takes-precedence) resolve any conflicts. For example, the data is retained for the longest duration of all the applied retention policies or eDiscovery holds.

### Compliance Manager and AI interactions

[Microsoft Purview Compliance Manager](compliance-manager) is a solution that helps you automatically assess and manage compliance across your multicloud environment. Compliance Manager can help you throughout your compliance journey, from taking inventory of your data protection risks to managing the complexities of implementing controls, staying current with regulations and certifications, and reporting to auditors.

To help you keep compliant with AI regulations, Compliance Manager provides regulatory templates to help you assess, implement, and strengthen your compliance requirements for all generative AI apps. For example, monitoring AI interactions and preventing data loss in AI applications. For more information, see [Assessments for AI regulations](compliance-manager-assessments#assessments-for-ai-regulations).

## Other documentation to help you secure and manage generative AI apps

Blog post announcement: [Accelerate AI adoption with next-gen security and governance capabilities](https://techcommunity.microsoft.com/blog/microsoftsecurityandcompliance/accelerate-ai-adoption-with-next-gen-security-and-governance-capabilities/4296064)

Microsoft 365 Copilot:

- [Microsoft 365 Copilot documentation](/en-us/microsoft-365-copilot)
- [Apply principles of Zero Trust to Microsoft 365 Copilot](/en-us/security/zero-trust/zero-trust-microsoft-365-copilot)

Related resources:

- [Secure Generative AI with Microsoft Entra](/en-us/entra/architecture/secure-generative-ai)
- [Govern AI apps and data for regulatory compliance](/en-us/security/security-for-ai/govern)
- Blog posts (April 2025):
    - [How to deploy Microsoft Purview DSPM for AI to secure your AI apps](https://techcommunity.microsoft.com/blog/microsoft-security-blog/how-to-deploy-microsoft-purview-dspm-for-ai-to-secure-your-ai-apps/4397714)
    - [How to use DSPM for AI Data Risk Assessment to Address Internal Oversharing](https://techcommunity.microsoft.com/blog/microsoft-security-blog/how-to-use-dspm-for-ai-data-risk-assessment-to-address-internal-oversharing/4399785)