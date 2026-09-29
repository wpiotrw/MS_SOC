---
layout: Conceptual
title: Use Microsoft Purview to manage data security & compliance for Microsoft 365 Copilot Cowork | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ai-copilot-cowork
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: minz
ms.service: purview
ms.update-cycle: 180-days
ms.date: 2026-06-22T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.collection:
- highpri
- m365copilot
- msec-ai-copilot
ai-usage: ai-assisted
description: Use Microsoft Purview to help you protect and manage data security and compliance protections for Microsoft 365 Copilot Cowork.
locale: en-us
document_id: 1a82d17a-3ae6-c2a2-7d10-e71381c06bdb
document_version_independent_id: 1a82d17a-3ae6-c2a2-7d10-e71381c06bdb
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ai-copilot-cowork.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ai-copilot-cowork
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ai-copilot-cowork.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0fc65d4-7c73-4029-a261-7f99ff744363
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b2daec57-5914-4967-8ed3-1d444897ba59
platformId: 47485d0a-f395-608d-8075-304992746cf1
---

# Use Microsoft Purview to manage data security & compliance for Microsoft 365 Copilot Cowork | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use the following sections to identify the Microsoft Purview capabilities that are supported for [Microsoft 365 Copilot Cowork](/en-us/microsoft-365/copilot/cowork).

Note

Although Copilot Cowork is part of Microsoft 365 Copilot, Cowork introduces long‑running, multi‑step work across apps. Because this model can result in different behaviors and feature support, its capabilities are documented separately to provide accurate guidance for administrators to better understand security and compliance scenarios.

## Capabilities supported

Use the following table to see at a glance the Microsoft Purview capabilities that are supported with Copilot Cowork.

| Capability or solution in Microsoft Purview | Supported for AI interactions |
| --- | --- |
| DSPM and DSPM for AI (classic) | **✓** |
| Auditing | **✓** |
| Data classification | **✕** |
| Sensitivity labels | **✓** |
| Encryption without sensitivity labels | **✓** |
| Data loss prevention | **✕** |
| Insider Risk Management | **✓** |
| Communication compliance | **✓** |
| eDiscovery | **✓** |
| Data Lifecycle Management | **✓** |
| Compliance Manager | **✕** |

### DSPM and DSPM for AI (classic)

Use [Data Security Posture Management](data-security-posture-management-learn-about) or [Data Security Posture Management for AI (classic)](dspm-for-ai) as your front door to discover, secure, and apply compliance controls for AI usage across your enterprise. Both DSPM versions use existing controls from Microsoft Purview information protection and compliance management with easy-to-use graphical tools and reports to quickly gain insights into AI use within your organization. With personalized recommendations, and one-click policies help you protect your data and comply with regulatory requirements.

###### AI app-specific information:

- [Data risk assessments](dspm-for-ai#data-assessments) help you identify and fix issues that could results in oversharing of data. From the recommendations:

    - **Protect your data from potential oversharing risks** for the default weekly data risk assessment.
    - **Protect sensitive data references in Copilot and agent responses** for a custom data risk assessment.
- [One-click policies](dspm-for-ai-considerations#one-click-policies-from-data-security-posture-management-for-ai) available:

    - **Sensitivity labels and policies** from the recommendation or remediation action **Protect your data with sensitivity labels**.
    - **DSPM for AI - Detect risky AI usage** from the recommendation or remediation action **Detect risky interactions in AI apps**.
    - **DSPM for AI - Unethical behavior in AI apps** from the recommendation or remediation action **Detect unethical behavior in AI**.
- Although interactions from Cowork display in activity explorer (**AI activities** tab), they don't display in the **Apps and agents** dashboard or the **AI observability** page.

### Auditing and AI interactions

[Microsoft Purview Audit solutions](audit-solutions-overview) provide comprehensive tools for searching and managing audit records of activities performed across various Microsoft services by users and admins, and help organizations to effectively respond to security events, forensic investigations, internal investigations, and compliance obligations.

Like other activities, prompts and responses are [captured in the unified audit log](audit-log-activities). Events include how and when users interact with the AI app, and can include in which Microsoft 365 service the activity took place, and references to the files stored in Microsoft 365 that were accessed during the interaction. If these files have a sensitivity label applied, that's also captured.

These events flow into [activity explorer](ai-microsoft-purview-considerations#activity-explorer-events) in the **AI activities** tab in the current version of DSPM and in DSPM for AI, where the data from prompts and responses can be displayed. You can also use the **Audit** solution from the [Microsoft Purview portal](purview-portal) to search and find these auditing events.

For more information, see [Audit logs for Copilot and AI activities](audit-copilot).

###### AI app-specific information:

Typical auditing events:

- A user starts a new Cowork conversation
- A user adds, removes, or shares a skill or plugin
- A user runs a scheduled prompt
- A user starts a browser task
- A user uploads a file to Cowork
- Cowork creates an artifact in OneDrive on behalf of a user

### Sensitivity labels and AI interactions

AI apps that Microsoft Purview support use [existing controls to ensure that data stored in your tenant is never returned](/en-us/microsoft-365-copilot/microsoft-365-copilot-privacy#how-does-microsoft-365-copilot-protect-sensitive-organizational-data) to the user or used by a large language model (LLM) if the user doesn't have access to that data. When the data has [sensitivity labels](sensitivity-labels) from your organization applied to the content, there's an extra layer of protection:

- When a file is open in Word, Excel, PowerPoint, or similarly an email or calendar event is open in Outlook, the sensitivity of the data is displayed to users in the app with the label name and content markings (such as header or footer text) that have been configured for the label. [Loop components and pages also support the same sensitivity labels](sensitivity-labels-loop).
- When the sensitivity label applies encryption, users must have the [EXTRACT usage right](ai-m365-copilot-considerations#copilot-honors-existing-protection-with-the-extract-usage-right), as well as VIEW, for the AI apps to return the data.
- This protection extends to data stored outside your Microsoft 365 tenant when it's open in an Office app (data in use). For example, local storage, network shares, and cloud storage.

Tip

If you haven't already, we recommend you enable sensitivity labels for SharePoint and OneDrive and also familiarize yourself with the file types and label configurations that these services can process. When sensitivity labels aren't enabled for these services, the encrypted files that Copilot and agents can access are limited to data in use from Office apps on Windows.

For instructions, see [Enable sensitivity labels for Office files in SharePoint and OneDrive](sensitivity-labels-sharepoint-onedrive-files).

If you're not already using sensitivity labels, see [Get started with sensitivity labels](get-started-with-sensitivity-labels).

###### AI app-specific information:

- Microsoft 365 Copilot Cowork displays the sensitivity label for items listed in the response and citations. Using the sensitivity labels' [priority number](sensitivity-labels#label-priority-order-matters) that's defined in the [Microsoft Purview portal](purview-portal), the latest response displays the highest priority sensitivity label from the data used for that Copilot chat.

    Although compliance admins define a sensitivity label's priority, a higher priority number usually denotes higher sensitivity of the content, with more restrictive permissions. As a result, Copilot responses display the most restrictive sensitivity label to educate the user about the sensitivity of the data.
- Sensitivity label inheritance is supported for newly created content. See the following section for more information.

#### Sensitivity label inheritance

If you use Cowork to create new content in Word, PowerPoint, and Outlook based on an item that has a sensitivity label applied, the sensitivity label from the source file is automatically inherited, with the label's protection setting.

For example, Cowork creates a new Word document based on labeled data. The source content has the sensitivity label **Confidential\Anyone (unrestricted)** applied and that label is configured to apply a footer that displays "Confidential". The new content is automatically labeled **Confidential\Anyone (unrestricted)** with the same footer.

If multiple sources are used to create new content, the sensitivity label with the [highest priority](sensitivity-labels#label-priority-order-matters) is used for label inheritance.

As with all automatic labeling scenarios, a user can always override and replace an inherited label (or remove, if you're not using [mandatory labeling](sensitivity-labels-office-apps#require-users-to-apply-a-label-to-their-email-and-documents)).

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

### Insider Risk Management and AI interactions

[Microsoft Purview Insider Risk Management](insider-risk-management) helps you detect, investigate, and mitigate internal risks such as IP theft, data leakage, and security violations. It leverages machine learning models and various signals from Microsoft 365 and third-party indicators to identify potential malicious or inadvertent insider activities. The solution includes privacy controls like pseudonymization and role-based access, ensuring user-level privacy while enabling risk analysts to take appropriate actions.

Use the [Risky AI usage policy template](insider-risk-management-policy-templates#risky-ai-usage) to detect risky usage that includes prompt injection attacks and accessing protected materials. Insights from these signals are integrated into Microsoft Defender XDR to provide a comprehensive view of AI-related risks.

### Communication compliance and AI interactions

[Microsoft Purview Communication Compliance](communication-compliance) provides tools to help you detect and manage regulatory compliance and business conduct violations across various communication channels, which include user prompts and responses for AI apps. It's designed with privacy by default, pseudonymizing usernames and incorporating role-based access controls. The solution helps identify and remediate inappropriate communications, such as sharing sensitive information, harassment, threats, and adult content.

To learn more about using communication compliance policies for AI apps, see [Configure a communication compliance policy to detect for generative AI interactions](communication-compliance-copilot).

### eDiscovery and AI interactions

[Microsoft Purview eDiscovery](edisc) lets you identify and deliver electronic information that can be used as evidence in legal cases. The eDiscovery tools in Microsoft Purview support searching for content in Exchange Online, OneDrive for Business, SharePoint Online, Microsoft Teams, Microsoft 365 Groups, and Viva Engage teams. You can then prevent the information from deletion and export the information.

Because user prompts and responses for AI apps are stored in a user's mailbox, you can create a case and use [search](edisc-search-query) when a user's mailbox is selected as the source for a search query. For example, select and retrieve this data from the source mailbox by selecting from the query builder **Add condition** &gt; **Type** &gt; **Contains any of** &gt; **Edit** &gt; *Copilot activity*. This query condition includes all Copilot and other AI application activity.

After the search is refined, you can export the results or add to a [review set](edisc-review-set-manage). You can review and export information directly from the review set.

For more information about identifying and deleting user AI interaction data, see [Search for and delete Copilot data in eDiscovery](edisc-search-copilot-data).

###### AI app-specific information:

In scope for eDiscovery:

- Conversation transcripts — The full text of a user's Cowork conversations, including prompts and responses.
- Files Cowork created — Documents, decks, PDFs, and images saved to the user's OneDrive.
- Scheduled prompts — The prompt text and the conversations created by each scheduled run.
- Uploaded files — Files a user uploaded to Cowork that are retained in the user's OneDrive or in the conversation.

### Data Lifecycle Management and AI interactions

[Microsoft Purview Data Lifecycle Management](data-lifecycle-management) provides tools and capabilities to manage the lifecycle of organizational data by retaining necessary content and deleting unnecessary content. These tools ensure compliance with business, legal, and regulatory requirements.

Use [retention policies](retention) to automatically retain or delete user prompts and responses for AI apps. For detailed information about this retention works, see [Learn about retention for Copilot & AI apps](retention-policies-copilot).

As with all retention policies and holds, if more than one policy for the same location applies to a user, the [principles of retention](retention#the-principles-of-retention-or-what-takes-precedence) resolve any conflicts. For example, the data is retained for the longest duration of all the applied retention policies or eDiscovery holds.

###### AI app-specific information:

- For retention policies, select the option for **Microsoft Copilot Experiences**.
- Retention labels can automatically retain files referenced in Microsoft 365 Copilot Cowork when you select the option for cloud attachments with an auto-apply retention label policy: **Apply label to cloud attachments and links shared in Exchange, Teams, Viva Engage, and Copilot**. As with all retained cloud attachments, the file version at the time it's referenced is retained.

    ![Updated cloud attachments option for auto-apply retention label to include interactions for Copilot.](media/cloud-attachments-copilot.png)

    For detailed information about how this retention works, see [How retention works with cloud attachments](retention-policies-sharepoint#how-retention-works-with-cloud-attachments).

## Other documentation to help you secure and manage generative AI apps

- [Microsoft Purview data security and compliance protections for generative AI apps](ai-microsoft-purview)
- [Microsoft 365 Copilot Cowork Overview](/en-us/microsoft-365/copilot/cowork)