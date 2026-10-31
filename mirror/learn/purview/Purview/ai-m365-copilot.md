---
layout: Conceptual
title: Use Microsoft Purview to manage data security & compliance for Microsoft 365 Copilot & Microsoft 365 Copilot Chat | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ai-m365-copilot
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: yibingchen
ms.service: purview
ms.update-cycle: 180-days
ms.date: 2026-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.collection:
- highpri
- m365copilot
- msec-ai-copilot
description: Use Microsoft Purview to help you protect and manage data security and compliance protections for Microsoft 365 Copilot & Microsoft 365 Copilot Chat.
locale: en-us
document_id: 2f0cd5f8-4da1-cdd4-449a-2a1eeaba9a15
document_version_independent_id: 2f0cd5f8-4da1-cdd4-449a-2a1eeaba9a15
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ai-m365-copilot.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ai-m365-copilot
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ai-m365-copilot.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0fc65d4-7c73-4029-a261-7f99ff744363
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b2daec57-5914-4967-8ed3-1d444897ba59
platformId: 0ec75a2a-5854-9a63-a4a8-fabff15d15c7
---

# Use Microsoft Purview to manage data security & compliance for Microsoft 365 Copilot & Microsoft 365 Copilot Chat | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use the following sections to identify the [Microsoft Purview capabilities that are supported for AI interactions](ai-microsoft-purview) with Microsoft 365 Copilot & Microsoft 365 Copilot Chat, and some get started recommendations for you to manage these AI interactions for security and compliance.

## Capabilities supported

Use the following table to see at a glance the Microsoft Purview capabilities that are supported with Microsoft 365 Copilot & Microsoft 365 Copilot Chat.

| Capability or solution in Microsoft Purview | Supported for AI interactions |
| --- | --- |
| DSPM and DSPM for AI (classic) | **✓** |
| Auditing | **✓** |
| Data classification | **✓** |
| Sensitivity labels | **✓** |
| Encryption without sensitivity labels | **✓** |
| Data loss prevention | **✓** |
| Insider Risk Management | **✓** |
| Communication compliance | **✓** |
| eDiscovery | **✓** |
| Data Lifecycle Management | **✓** |
| Compliance Manager | **✓** |

### DSPM and DSPM for AI (classic)

Use [Data Security Posture Management](data-security-posture-management-learn-about) or [Data Security Posture Management for AI (classic)](dspm-for-ai) as your front door to discover, secure, and apply compliance controls for AI usage across your enterprise. Both DSPM versions use existing controls from Microsoft Purview information protection and compliance management with easy-to-use graphical tools and reports to quickly gain insights into AI use within your organization. With personalized recommendations, and one-click policies help you protect your data and comply with regulatory requirements.

###### AI app-specific information:

- [Data risk assessments](dspm-for-ai#data-assessments) help you identify and fix issues that could results in oversharing of data. From the recommendations:

    - **Protect your data from potential oversharing risks** for the default weekly data risk assessment.
    - **Protect sensitive data references in Copilot and agent responses** for a custom data risk assessment.
- Recommendation: **Get guided assistance to AI regulations**, which uses [control-mapping regulatory templates from Compliance Manager](compliance-manager-regulations).
- Additional guidance from **Overview** &gt; **Microsoft 365 Copilot** view.
- [One-click policies](dspm-for-ai-considerations#one-click-policies-from-data-security-posture-management-for-ai) available:

    - **Sensitivity labels and policies** from the recommendation or remediation action **Protect your data with sensitivity labels**.
    - **DSPM for AI - Detect risky AI usage** from the recommendation or remediation action **Detect risky interactions in AI apps**.
    - **DSPM for AI - Unethical behavior in AI apps** from the recommendation or remediation action **Detect unethical behavior in AI**.
    - **DSPM for AI - Protect sensitive data from Copilot processing** from the recommendation or remediation action **Protect items with sensitivity labels from Microsoft 365 Copilot and agent processing**
    - **DSPM for AI - Detect sensitive info shared with AI via network** from the recommendation or remediation action **Extend insights into sensitive data in AI app interactions**.

### Auditing and AI interactions

[Microsoft Purview Audit solutions](audit-solutions-overview) provide comprehensive tools for searching and managing audit records of activities performed across various Microsoft services by users and admins, and help organizations to effectively respond to security events, forensic investigations, internal investigations, and compliance obligations.

Like other activities, prompts and responses are [captured in the unified audit log](audit-log-activities). Events include how and when users interact with the AI app, and can include in which Microsoft 365 service the activity took place, and references to the files stored in Microsoft 365 that were accessed during the interaction. If these files have a sensitivity label applied, that's also captured.

These events flow into [activity explorer](ai-microsoft-purview-considerations#activity-explorer-events) in the **AI activities** tab in the current version of DSPM and in DSPM for AI, where the data from prompts and responses can be displayed. You can also use the **Audit** solution from the [Microsoft Purview portal](purview-portal) to search and find these auditing events.

For more information, see [Audit logs for Copilot and AI activities](audit-copilot).

### Data classification and AI interactions

Microsoft Purview data classification provides a comprehensive framework for identifying and tagging sensitive data across various Microsoft services, including Office 365, Dynamics 365, and Azure. Classifying data is often the first step to ensure compliance with data protection regulations and safeguard against unauthorized access, alteration, or destruction. You can use built-in system classifications or create your own.

Sensitive information types and trainable classifiers can be used to find sensitive data in user prompts and responses when they use AI apps. The resulting information then surfaces in [Microsoft Purview Reports overview](purview-reports) and [activity explorer](ai-microsoft-purview-considerations#activity-explorer-events) in DSPM for AI and the **AI activities** tab in activity explorer from the preview version of DSPM.

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

- [Microsoft 365 Copilot Chat](https://support.microsoft.com/topic/use-microsoft-365-chat-preview-at-microsoft365-com-or-in-the-microsoft-365-office-app-4a2538f9-962f-4c7c-a368-f6006bc13d6f) displays the sensitivity label for items listed in the response and citations. Using the sensitivity labels' [priority number](sensitivity-labels#label-priority-order-matters) that's defined in the [Microsoft Purview portal](purview-portal), the latest response in Microsoft 365 Copilot Chat and [threaded summaries](https://support.microsoft.com/office/cccccca2-9dc8-49a9-ab76-b1a8ee21486c#bkmk_thread_summaries) in Copilot in Teams chat and channels display the highest priority sensitivity label from the data used for that Copilot chat.

    Although compliance admins define a sensitivity label's priority, a higher priority number usually denotes higher sensitivity of the content, with more restrictive permissions. As a result, Copilot responses display the most restrictive sensitivity label to educate the user about the sensitivity of the data.
- Copilot in Word, Copilot in PowerPoint, and Copilot in Outlook support sensitivity label inheritance for newly created content. See the following section for more information.

#### Sensitivity label inheritance

If you use Copilot in Word, Copilot in PowerPoint, and Copilot in Outlook to create new content based on an item that has a sensitivity label applied, the sensitivity label from the source file is automatically inherited, with the label's protection settings.

For example, a user selects **Draft with Copilot** in Word and then **Reference a file**. Or a user selects **Create presentation from file** in PowerPoint, or **Edit in Pages** from Microsoft 365 Copilot Chat. The source content has the sensitivity label **Confidential\Anyone (unrestricted)** applied and that label is configured to apply a footer that displays "Confidential". The new content is automatically labeled **Confidential\Anyone (unrestricted)** with the same footer.

To see an example of this in action, watch the following demo from the Ignite 2023 session, "Getting your enterprise ready for Microsoft 365 Copilot". The demo shows how the default sensitivity label of **General** is replaced with a **Confidential** label when a user drafts with Copilot and references a labeled file. The information bar under the ribbon informs the user that content created by Copilot resulted in the new label being automatically applied: 

If multiple files are used to create new content, the sensitivity label with the [highest priority](sensitivity-labels#label-priority-order-matters) is used for label inheritance.

As with all automatic labeling scenarios, the user can always override and replace an inherited label (or remove, if you're not using [mandatory labeling](sensitivity-labels-office-apps#require-users-to-apply-a-label-to-their-email-and-documents)).

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

###### AI app-specific information:

- Use the **Microsoft 365 Copilot and Copilot Chat** policy location to restrict the processing of prompts that contain sensitive information types, or processing files and emails that have specific sensitivity labels applied. For more information, see [Learn about using Microsoft Purview Data Loss Prevention to protect interactions with Microsoft 365 Copilot and Copilot Chat](dlp-microsoft365-copilot-location-learn-about).
- Microsoft 365 Copilot Chat (web version only) supports the following Endpoint DLP capabilities:

    - Block paste of sensitive content
    - Block files based on a specified sensitivity label

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

### Data Lifecycle Management and AI interactions

[Microsoft Purview Data Lifecycle Management](data-lifecycle-management) provides tools and capabilities to manage the lifecycle of organizational data by retaining necessary content and deleting unnecessary content. These tools ensure compliance with business, legal, and regulatory requirements.

Use [retention policies](retention) to automatically retain or delete user prompts and responses for AI apps. For detailed information about this retention works, see [Learn about retention for Copilot & AI apps](retention-policies-copilot).

As with all retention policies and holds, if more than one policy for the same location applies to a user, the [principles of retention](retention#the-principles-of-retention-or-what-takes-precedence) resolve any conflicts. For example, the data is retained for the longest duration of all the applied retention policies or eDiscovery holds.

###### AI app-specific information:

- For retention policies, select the option for **Microsoft Copilot Experiences**.
- Retention labels can automatically retain files referenced in Microsoft 365 Copilot when you select the option for cloud attachments with an auto-apply retention label policy: **Apply label to cloud attachments and links shared in Exchange, Teams, Viva Engage, and Copilot**. As with all retained cloud attachments, the file version at the time it's referenced is retained.

    ![Updated cloud attachments option for auto-apply retention label to include interactions for Copilot.](media/cloud-attachments-copilot.png)

    For detailed information about how this retention works, see [How retention works with cloud attachments](retention-policies-sharepoint#how-retention-works-with-cloud-attachments).

#### Compliance Manager and AI interactions

[Microsoft Purview Compliance Manager](compliance-manager) is a solution that helps you automatically assess and manage compliance across your multicloud environment. Compliance Manager can help you throughout your compliance journey, from taking inventory of your data protection risks to managing the complexities of implementing controls, staying current with regulations and certifications, and reporting to auditors.

To help you keep compliant with AI regulations, Compliance Manager provides regulatory templates to help you assess, implement, and strengthen your compliance requirements for all generative AI apps. For example, monitoring AI interactions and preventing data loss in AI applications. For more information, see [Assessments for AI regulations](compliance-manager-assessments#assessments-for-ai-regulations).

## Getting started recommended steps

Use the following steps to get started with managing data security & compliance for AI interactions from Microsoft 365 Copilot & Microsoft 365 Copilot Chat.

Note

These steps focus on managing a specific AI app or agent. For broader coverage that uses security objectives with guided workflows, use the current version of [Data Security Posture Management](data-security-posture-management-learn-about).

Because Data Security Posture Management for AI is your front door for securing and managing AI interactions, most of the following instructions use that solution:

- [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **DSPM for AI (classic)** with an account that has [appropriate permissions](ai-microsoft-purview-permissions). For example, an account that's a member of the **Microsoft Entra Compliance Administrator** group role.

    [![Selecting the Microsoft Purview Data Security Posture Management for AI solution from the Microsoft Purview portal.](media/dspm-solution.png)](media/example-dspm.png#lightbox)

### Confirm that auditing is turned on

From **DSPM for AI (classic)** &gt; **Overview** &gt; **All AI apps** view &gt; **Get Started** section, look to see if auditing is on for your tenant. If not, select **Activate Microsoft Purview Audit**.

### Use the Microsoft 365 Copilot view to discover, protect, and apply compliance controls

Change the view from **All AI apps** to **Microsoft 365 Copilot** and work your way through the sections:

- **Assess and prevent oversharing of sensitive data**
- **Secure your data in Microsoft 365 Copilot**
- **Discover Microsoft 365 Copilot activity**

These sections include recommendations that are specific to Microsoft 365 Copilot. Wait at least a day for data to display for the reports on this page.

Tip

**Secure your data in Microsoft 365 Copilot** includes the following recommendations with manual configuration instructions for their respective Microsoft Purview solutions: **Create sensitivity labels for your organization** and **Protect items with sensitivity labels from Copilot processing**

If you prefer, you can use DSPM for AI one-click policies for these recommendations, as described in the next section.

### Use one-click policies to increase coverage

Select **Recommendations** from the navigation and use [one-click policies](dspm-for-ai-considerations#one-click-policies-from-data-security-posture-management-for-ai) to automatically create policies that help you discover, protect, and apply compliance controls. Specific to Microsoft 365 Copilot:

- **Protect your data with sensitivity labels**
- **Detect risky interactions in AI apps**
- **Detect unethical behavior in AI**
- **Protect items with sensitivity labels from Microsoft 365 Copilot and agent processing**

### View data from your policies

1. Wait at least a day for data, and then navigate to the **Reports** page to view the results of your policies. Select **Copilot experiences & agents** and view information such as:

    - Total interactions over time (Microsoft Copilot and agents)
    - Sensitive interactions per AI app
    - Top unethical AI interactions
    - Top sensitivity labels references in Microsoft 365 Copilot and agents
    - Insider Risk severity
    - Insider risk severity per AI app
    - Potential risky AI usage
2. Select **View details** for each of the report graphs to view detailed activities in the activity explorer.

    From the filters, select the **AI app category** of **Copilot experiences & agents**, and then use the other filters if you need to further refine the displayed data. Then drill down to each activity to view details that include displaying the prompts and response when you're a member of the Microsoft Purview Content Explorer Content Viewer role group. For more information about this requirement, see [Permissions for Data Security Posture Management for AI](ai-microsoft-purview-permissions).

### Apply additional compliance controls to Microsoft 365 Copilot interactions

1. If you need to retain the exact version of files referenced in Microsoft 365 Copilot interactions:

    In the Microsoft Purview portal, navigate to **Data Lifecycle Management** &gt; **Retention labels** &gt; and either locate or create a retention label with the required retention period. Then, navigate to **Label policies** to auto-apply that label, and select the option **Apply label to cloud attachments and links shared in Exchange, Teams, Viva Engage, and Copilot**. For more information, see [Automatically apply a retention label to retain or delete content](apply-retention-labels-automatically#how-to-create-an-auto-apply-retention-label-policy).
2. If you need to preserve, collect, analyze, review, or export Microsoft 365 Copilot interactions:

    In the Microsoft Purview portal, navigate to **eDiscovery** &gt; **Cases** &gt; **Create case**. In the case, [create a search](edisc-search-query) and use the *ItemClass* property and the `IPM.SkypeTeams.Message.Copilot.*` value to search for these interactions in your organization.

Routinely review the reports and data risk assessments in DSPM for AI to determine if you need to make changes, and use activity explorer and [events](dspm-for-ai-considerations#activity-explorer-events) for deeper analysis of how users are interacting with Microsoft 365 Copilot & Microsoft 365 Copilot Chat.

## Other documentation to help you secure and manage generative AI apps

For more detailed information, see [Considerations to manage Microsoft 365 Copilot for security and compliance](ai-m365-copilot-considerations).

Microsoft 365 Copilot documentation:

- [Microsoft 365 Copilot documentation](/en-us/microsoft-365-copilot)
- [Microsoft 365 Copilot admin guide for E5 + SAM licenses](/en-us/copilot/microsoft-365/microsoft-365-copilot-e5-guide)
- [Apply principles of Zero Trust to Microsoft 365 Copilot](/en-us/security/zero-trust/zero-trust-microsoft-365-copilot)