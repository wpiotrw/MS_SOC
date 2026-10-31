---
layout: Conceptual
title: Use Microsoft Purview to manage data security & compliance for Channel Agent in Teams | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ai-teams-channel-agent
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
description: Use Microsoft Purview to help you protect and manage data security and compliance protections for Channel Agent in Microsoft Teams.
locale: en-us
document_id: c22de021-fd50-0f52-99bc-55d0e4e6ca67
document_version_independent_id: c22de021-fd50-0f52-99bc-55d0e4e6ca67
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ai-teams-channel-agent.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ai-teams-channel-agent
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ai-teams-channel-agent.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 5a4aa98d-4658-e65e-ecef-effea97442f9
---

# Use Microsoft Purview to manage data security & compliance for Channel Agent in Teams | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use the following sections to identify the [Microsoft Purview capabilities that are supported for AI interactions](ai-microsoft-purview) with agents in Teams channels, and some get started recommendations for you to manage these AI interactions for security and compliance.

For additional information, see [Get started with Channel Agent in Microsoft Teams](https://support.microsoft.com/office/get-started-with-channel-agent-for-teams-channels-b85945cf-deef-4f1e-9db1-66e1a23b6a65).

## Capabilities supported

Use the following table to see at a glance the Microsoft Purview capabilities that are supported with Channel Agent in Teams.

| Capability or solution in Microsoft Purview | Supported for AI interactions |
| --- | --- |
| DSPM and DSPM for AI (classic) | **✓** |
| Auditing | **✓** |
| Data classification | **✓** |
| Sensitivity labels | **✓** |
| Encryption without sensitivity labels | **✕** |
| Data loss prevention | **✓** |
| Insider Risk Management | **✕** |
| Communication compliance | **✓** |
| eDiscovery | **✓** |
| Data Lifecycle Management | **✓** |
| Compliance Manager | **✓** |

### DSPM and DSPM for AI (classic)

Use [Data Security Posture Management](data-security-posture-management-learn-about) or [Data Security Posture Management for AI (classic)](dspm-for-ai) as your front door to discover, secure, and apply compliance controls for AI usage across your enterprise. Both DSPM versions use existing controls from Microsoft Purview information protection and compliance management with easy-to-use graphical tools and reports to quickly gain insights into AI use within your organization. With personalized recommendations, and one-click policies help you protect your data and comply with regulatory requirements.

###### AI app-specific information:

- [One-click policies](dspm-for-ai-considerations#one-click-policies-from-data-security-posture-management-for-ai) available:

    - **DSPM for AI - Detect risky AI usage** from the recommendation or remediation action **Detect risky interactions in AI apps**.
    - **DSPM for AI - Unethical behavior in AI apps** from the recommendation or remediation action **Detect unethical behavior in AI**.
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

- Channel Agent in Teams responses display the sensitivity label for items listed in the response and citations. Using the sensitivity labels' [priority number](sensitivity-labels#label-priority-order-matters) that's defined in the [Microsoft Purview portal](purview-portal), the latest response from Channel Agent displays the highest priority sensitivity label from the data used for that channel chat.

    Although compliance admins define a sensitivity label's priority, a higher priority number usually denotes higher sensitivity of the content, with more restrictive permissions. As a result, the Channel Agent responses display the most restrictive sensitivity label to educate the user about the sensitivity of the data.
- When Channel Agent creates newly created content that supports sensitivity labels, that action supports sensitivity label inheritance. See the following section for more information.
- Currently, Channel Agent could summarize for an authorized user the content of encrypted items that one or more users in the channel don't have permissions to open. The requesting user is warned of this risk and administrators always have the ability to [turn off Channel Agent in Teams](/en-us/microsoftteams/manage-apps). For additional information about this and other deployment considerations, see [Information protection considerations for Channel Agent in Teams](ai-m365-copilot-considerations#information-protection-considerations-for-channel-agent-in-teams).

#### Sensitivity label inheritance

If you use Channel Agent in Teams to create new content based on an item that has a sensitivity label applied, the sensitivity label from the source item is automatically inherited, with the label's protection settings.

For example, you ask an agent to create a Loop component based on a file that's uploaded to the channel. The file has the sensitivity label **Confidential\Project Bluebird** applied and that label is configured to apply encryption that restricts access to people involved with the project. The new Loop component is automatically labeled **Confidential\Project Bluebird** and can't be opened by people who aren't involved with the project.

AI-generated items that currently support sensitivity label inheritance for Channel Agent in Teams: Loop components and pages, and files in OneDrive and SharePoint.

If multiple labeled sources are used to create new content, the sensitivity label with the [highest priority](sensitivity-labels#label-priority-order-matters) is used for label inheritance.

As with all automatic labeling scenarios, a user can always override and replace an inherited label (or remove, if you're not using [mandatory labeling](sensitivity-labels-office-apps#require-users-to-apply-a-label-to-their-email-and-documents)).

### Data loss prevention and AI interactions

[Microsoft Purview Data Loss Prevention](dlp-learn-about-dlp) (DLP) helps you identify sensitive items across Microsoft 365 services and endpoints, monitor them, and helps protect against leakage of those items. It uses deep content inspection and contextual analysis to identify sensitive items and it enforces policies to protect sensitive data such as financial records, health information, or intellectual property.

Windows computers that are [onboarded to Microsoft Purview](device-onboarding-overview) can be configured for Endpoint data loss prevention (DLP) policies that warn or block users from sharing sensitive information with third-party generative AI sites that are accessed via a browser. For example, a user is prevented from pasting credit card numbers into ChatGPT, or they see a warning that they can override. For more information about the supported DLP actions and which platforms support them, see the first two rows in the table from [Endpoint activities you can monitor and take action on](endpoint-dlp-learn-about#endpoint-activities-you-can-monitor-and-take-action-on).

###### AI app-specific information:

- The following DLP capability only is supported for Channel Agent in Teams:
    - When an agent interacts with a user in a Teams conversation, a [DLP policy can scan the messages for sensitive data](dlp-microsoft-teams).

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

- Configuration for retention and deletion:
    - For Channel Agent in Teams interactions, use a retention policy with the **Teams chats** option.

#### Compliance Manager and AI interactions

[Microsoft Purview Compliance Manager](compliance-manager) is a solution that helps you automatically assess and manage compliance across your multicloud environment. Compliance Manager can help you throughout your compliance journey, from taking inventory of your data protection risks to managing the complexities of implementing controls, staying current with regulations and certifications, and reporting to auditors.

To help you keep compliant with AI regulations, Compliance Manager provides regulatory templates to help you assess, implement, and strengthen your compliance requirements for all generative AI apps. For example, monitoring AI interactions and preventing data loss in AI applications. For more information, see [Assessments for AI regulations](compliance-manager-assessments#assessments-for-ai-regulations).

## Getting started recommended steps

Use the following steps to get started with managing data security & compliance for AI interactions with Channel Agent in Teams.

Note

These steps focus on managing a specific AI app or agent. For broader coverage that uses security objectives with guided workflows, use the current version of [Data Security Posture Management](data-security-posture-management-learn-about).

Because Data Security Posture Management for AI is your front door for securing and managing AI interactions, the following instructions use that solution:

- [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **DSPM for AI (classic)** with an account that has [appropriate permissions](ai-microsoft-purview-permissions). For example, an account that's a member of the **Microsoft Entra Compliance Administrator** group role.

    [![Selecting the Microsoft Purview Data Security Posture Management for AI solution from the Microsoft Purview portal.](media/dspm-solution.png)](media/example-dspm.png#lightbox)

### Discover interactions from Channel Agent in Teams

1. From **DSPM for AI (classic)** &gt; **Overview**, in the **Get Started** section, look to see if auditing is on for your tenant. If not, select **Activate Microsoft Purview Audit**.
2. In the **Recommendations** section, select **View all recommendations** to take you to the **Recommendations** page. If the following recommendation has a status of **Not Started**, select it to create a [one-click policy](dspm-for-ai-considerations#one-click-policies-from-data-security-posture-management-for-ai):

    - **Detect risky interactions in AI apps**: This recommendation creates a policy to help calculate user risk by detecting risky prompts and responses in Microsoft 365 Copilot, agents, and other generative AI apps.
3. Wait at least a day for data, and then navigate to the **Reports** page. Select the AI app category of **Copilot experiences & agents** and view information such as:

    - Total interactions over time (Microsoft Copilot and agents)
    - Sensitive interactions per AI app
    - Insider Risk severity
    - Insider risk severity per AI app
4. Select **View details** for each of the report graphs to view detailed activities in the activity explorer.

    Select the available filters to see the results from **Copilot experiences & agents** based on the different **Activity type**, **AI app category**, **App**, and **Scope** for administrative units, and more. Then drill down to each activity to view details that include displaying the prompts and response when you're a member of the Microsoft Purview Content Explorer Content Viewer role group. For more information about this requirement, see [Permissions for Data Security Posture Management for AI](ai-microsoft-purview-permissions).

### Apply compliance controls to interactions with Channel Agent in Teams

1. If you need to ensure that interactions with Channel Agent in Teams are retained for compliance reasons:

    In the Microsoft Purview portal, navigate to **Data Lifecycle Management** &gt; **Policies** &gt; **Retention Policies** and [create a retention policy](create-retention-policies) with the following policy location: - **Teams chats** for interactions with a channel agent
2. If you need to preserve, collect, analyze, review, or export interactions for Channel Agent in Teams:

    In the Microsoft Purview portal, navigate to **eDiscovery** &gt; **Cases** &gt; **Create case**. In the case, [create a search](edisc-search-query) and use the *ItemClass* property and the `IPM.SkypeTeams.Message` value to search for these interactions in your organization.

## Other documentation to help you secure and manage generative AI apps

Securing and managing AI interactions with Channel Agent in Teams has much in common with securing and managing AI interactions with Microsoft 365 Copilot. For more detailed information, see [Considerations for Microsoft Purview to manage Microsoft 365 Copilot and Channel Agent in Teams for security and compliance](ai-m365-copilot-considerations).