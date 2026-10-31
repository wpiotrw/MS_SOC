---
layout: Conceptual
title: Use Microsoft Purview to manage data security & compliance for other AI apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ai-other-apps
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: kyracatwork
ms.service: purview
ms.update-cycle: 180-days
ms.date: 2026-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.collection:
- highpri
- m365copilot
- msec-ai-copilot
description: Use Microsoft Purview to help you protect and manage data security and compliance protections for third-party AI apps.
locale: en-us
document_id: d7b2cdc7-a871-fdb3-b397-68b0eb4db9fd
document_version_independent_id: d7b2cdc7-a871-fdb3-b397-68b0eb4db9fd
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ai-other-apps.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ai-other-apps
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ai-other-apps.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
platformId: 44ff947e-9656-0964-f5ee-881f45e72d65
---

# Use Microsoft Purview to manage data security & compliance for other AI apps | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use the following sections to identify the [Microsoft Purview capabilities that are supported for AI interactions](ai-microsoft-purview) that use a browser to third-party AI sites, and some get started recommendations for you to manage these AI interactions for security and compliance.

Managing these AI interactions with Microsoft Purview requires you to enable [pay-as-you-go billing](purview-billing-models) in your organization.

## Capabilities supported

Use the following table to see at a glance the Microsoft Purview capabilities that are supported for third-party AI sites, such as ChatGPT, Google Gemini, and DeepSeek.

Unless noted for specific solutions, the list of supported AI sites is the same as those supported for DSPM for AI: [List of AI sites supported by Microsoft Purview Data Security Posture Management for AI](ai-microsoft-purview-supported-sites).

| Capability or solution in Microsoft Purview | Supported for AI interactions |
| --- | --- |
| DSPM and DSPM for AI (classic) | **✓** |
| Auditing | **✓** |
| Data classification | **✓** |
| Sensitivity labels | **✕** |
| Encryption without sensitivity labels | **✕** |
| Data loss prevention | **✓** |
| Insider Risk Management | **✓** |
| Communication compliance | **✓** |
| eDiscovery | **✓** |
| Data Lifecycle Management | **✓** |
| Compliance Manager | **✓** |

Most of the supported capabilities and solutions require the [Microsoft Purview browser extension](insider-risk-management-browser-support#configure-browser-signal-detection-for-microsoft-edge) and [devices onboarded to Microsoft Purview](device-onboarding-overview). The exceptions are, with their own prerequisites:

- [Network data security](dlp-network-data-security-learn) to detect sensitive information types at the network layer, using a Secure Access Service Edge or Security Service Edge integration.
- [Browser data security](dlp-browser-dlp-learn) to detect sensitive information types at the Edge browser layer, using a direct integration from Purview into the Edge browser.

### DSPM and DSPM for AI (classic)

Use [Data Security Posture Management](data-security-posture-management-learn-about) or [Data Security Posture Management for AI (classic)](dspm-for-ai) as your front door to discover, secure, and apply compliance controls for AI usage across your enterprise. Both DSPM versions use existing controls from Microsoft Purview information protection and compliance management with easy-to-use graphical tools and reports to quickly gain insights into AI use within your organization. With personalized recommendations, and one-click policies help you protect your data and comply with regulatory requirements.

###### AI app-specific information:

- The **Getting started** section from the **Overview** page contains the required steps and information to install the Microsoft Purview browser extension and devices onboarding process.
- Recommendation **Get guided assistance to AI regulations**, which uses [control-mapping regulatory templates from Compliance Manager](compliance-manager-regulations).
- [One-click policies](ai-microsoft-purview-considerations#one-click-policies-from-data-security-posture-management-for-ai) available:

    - **DSPM for AI: Detect sensitive info added to AI sites** from the recommendation or remediation action **Extend your insights for data discovery**
    - **DSPM for AI - Detect when users visit AI sites** from the recommendation or remediation action **Extend your insights for data discovery**
    - **DSPM for AI - Detect sensitive info shared in AI prompts in Edge** from the recommendation or remediation action **Extend your insights for data discovery**
    - **DSPM for AI - Detect sensitive info shared with AI via network** from the recommendation or remediation action **Extend insights into sensitive data in AI app interactions**.

### Auditing and AI interactions

[Microsoft Purview Audit solutions](audit-solutions-overview) provide comprehensive tools for searching and managing audit records of activities performed across various Microsoft services by users and admins, and help organizations to effectively respond to security events, forensic investigations, internal investigations, and compliance obligations.

Like other activities, prompts and responses are [captured in the unified audit log](audit-log-activities). Events include how and when users interact with the AI app, and can include in which Microsoft 365 service the activity took place, and references to the files stored in Microsoft 365 that were accessed during the interaction. If these files have a sensitivity label applied, that's also captured.

These events flow into [activity explorer](ai-microsoft-purview-considerations#activity-explorer-events) in the **AI activities** tab in the current version of DSPM and in DSPM for AI, where the data from prompts and responses can be displayed. You can also use the **Audit** solution from the [Microsoft Purview portal](purview-portal) to search and find these auditing events.

For more information, see [Audit logs for Copilot and AI activities](audit-copilot).

###### AI app-specific information:

- Use [network data security](dlp-network-data-security-learn) to audit prompts and responses at the network layer, using a Secure Access Service Edge or Security Service Edge integration.

### Data classification and AI interactions

Microsoft Purview data classification provides a comprehensive framework for identifying and tagging sensitive data across various Microsoft services, including Office 365, Dynamics 365, and Azure. Classifying data is often the first step to ensure compliance with data protection regulations and safeguard against unauthorized access, alteration, or destruction. You can use built-in system classifications or create your own.

Sensitive information types and trainable classifiers can be used to find sensitive data in user prompts and responses when they use AI apps. The resulting information then surfaces in [Microsoft Purview Reports overview](purview-reports) and [activity explorer](ai-microsoft-purview-considerations#activity-explorer-events) in DSPM for AI and the **AI activities** tab in activity explorer from the preview version of DSPM.

###### AI app-specific information:

- Use [network data security](dlp-network-data-security-learn) to detect sensitive info types at the network layer, using a Secure Access Service Edge or Security Service Edge integration.
- Use [browser data security](dlp-browser-dlp-learn) to detect sensitive info types at the Edge browser layer, using a direct integration from Purview into the Edge browser.

### Data loss prevention and AI interactions

[Microsoft Purview Data Loss Prevention](dlp-learn-about-dlp) (DLP) helps you identify sensitive items across Microsoft 365 services and endpoints, monitor them, and helps protect against leakage of those items. It uses deep content inspection and contextual analysis to identify sensitive items and it enforces policies to protect sensitive data such as financial records, health information, or intellectual property.

Windows computers that are [onboarded to Microsoft Purview](device-onboarding-overview) can be configured for Endpoint data loss prevention (DLP) policies that warn or block users from sharing sensitive information with third-party generative AI sites that are accessed via a browser. For example, a user is prevented from pasting credit card numbers into ChatGPT, or they see a warning that they can override. For more information about the supported DLP actions and which platforms support them, see the first two rows in the table from [Endpoint activities you can monitor and take action on](endpoint-dlp-learn-about#endpoint-activities-you-can-monitor-and-take-action-on).

###### AI app-specific information:

- Endpoint DLP supports an option to block the upload of files based on a specified sensitivity label.

### Insider Risk Management and AI interactions

[Microsoft Purview Insider Risk Management](insider-risk-management) helps you detect, investigate, and mitigate internal risks such as IP theft, data leakage, and security violations. It leverages machine learning models and various signals from Microsoft 365 and third-party indicators to identify potential malicious or inadvertent insider activities. The solution includes privacy controls like pseudonymization and role-based access, ensuring user-level privacy while enabling risk analysts to take appropriate actions.

Use the [Risky AI usage policy template](insider-risk-management-policy-templates#risky-ai-usage) to detect risky usage that includes prompt injection attacks and accessing protected materials. Insights from these signals are integrated into Microsoft Defender XDR to provide a comprehensive view of AI-related risks.

###### AI app-specific information:

- For prompts and responses, requires a collection policy that includes the setting to capture content. For more information, see [Collection Policies solution overview](collection-policies-solution-overview).

### Communication compliance and AI interactions

[Microsoft Purview Communication Compliance](communication-compliance) provides tools to help you detect and manage regulatory compliance and business conduct violations across various communication channels, which include user prompts and responses for AI apps. It's designed with privacy by default, pseudonymizing usernames and incorporating role-based access controls. The solution helps identify and remediate inappropriate communications, such as sharing sensitive information, harassment, threats, and adult content.

To learn more about using communication compliance policies for AI apps, see [Configure a communication compliance policy to detect for generative AI interactions](communication-compliance-copilot).

###### AI app-specific information:

- Support restricted to the Edge browser, for ChatGPT, Microsoft Chat (consumer version), Google Gemini, and DeepSeek.
- For prompts and responses, requires a collection policy that includes the setting to capture content. For more information, see [Collection Policies solution overview](collection-policies-solution-overview).
- Use [network data security](dlp-network-data-security-learn) to analyze prompts and responses at the network layer, using a Secure Access Service Edge or Security Service Edge integration.

### eDiscovery and AI interactions

[Microsoft Purview eDiscovery](edisc) lets you identify and deliver electronic information that can be used as evidence in legal cases. The eDiscovery tools in Microsoft Purview support searching for content in Exchange Online, OneDrive for Business, SharePoint Online, Microsoft Teams, Microsoft 365 Groups, and Viva Engage teams. You can then prevent the information from deletion and export the information.

Because user prompts and responses for AI apps are stored in a user's mailbox, you can create a case and use [search](edisc-search-query) when a user's mailbox is selected as the source for a search query. For example, select and retrieve this data from the source mailbox by selecting from the query builder **Add condition** &gt; **Type** &gt; **Contains any of** &gt; **Edit** &gt; *Copilot activity*. This query condition includes all Copilot and other AI application activity.

After the search is refined, you can export the results or add to a [review set](edisc-review-set-manage). You can review and export information directly from the review set.

For more information about identifying and deleting user AI interaction data, see [Search for and delete Copilot data in eDiscovery](edisc-search-copilot-data).

###### AI app-specific information:

- Support restricted to the Edge browser, for ChatGPT, Microsoft Chat (consumer version), Google Gemini, and DeepSeek.
- For prompts and responses, requires a collection policy that includes the setting to capture content. For more information, see [Collection Policies solution overview](collection-policies-solution-overview).
- Use [network data security](dlp-network-data-security-learn) to analyze prompts and responses at the network layer.

### Data Lifecycle Management and AI interactions

[Microsoft Purview Data Lifecycle Management](data-lifecycle-management) provides tools and capabilities to manage the lifecycle of organizational data by retaining necessary content and deleting unnecessary content. These tools ensure compliance with business, legal, and regulatory requirements.

Use [retention policies](retention) to automatically retain or delete user prompts and responses for AI apps. For detailed information about this retention works, see [Learn about retention for Copilot & AI apps](retention-policies-copilot).

As with all retention policies and holds, if more than one policy for the same location applies to a user, the [principles of retention](retention#the-principles-of-retention-or-what-takes-precedence) resolve any conflicts. For example, the data is retained for the longest duration of all the applied retention policies or eDiscovery holds.

###### AI app-specific information:

- Support restricted to the Edge browser, for ChatGPT, Microsoft Chat (consumer version), Google Gemini, and DeepSeek.
- For retention policies, select the option for **Other AI apps**.
- For prompts and responses, requires a collection policy that includes the setting to capture content. For more information, see [Collection Policies solution overview](collection-policies-solution-overview).
- Use [network data security](dlp-network-data-security-learn) to retain prompts and responses at the network layer.
- Use [browser data security](dlp-browser-dlp-learn) to retain prompts and responses at the Edge browser layer.

#### Compliance Manager and AI interactions

[Microsoft Purview Compliance Manager](compliance-manager) is a solution that helps you automatically assess and manage compliance across your multicloud environment. Compliance Manager can help you throughout your compliance journey, from taking inventory of your data protection risks to managing the complexities of implementing controls, staying current with regulations and certifications, and reporting to auditors.

To help you keep compliant with AI regulations, Compliance Manager provides regulatory templates to help you assess, implement, and strengthen your compliance requirements for all generative AI apps. For example, monitoring AI interactions and preventing data loss in AI applications. For more information, see [Assessments for AI regulations](compliance-manager-assessments#assessments-for-ai-regulations).

## Getting started recommended steps

Use the following steps to get started with managing data security & compliance for AI interactions that use a browser to third-party AI sites.

Note

These steps focus on managing a specific AI app or agent. For broader coverage that uses security objectives with guided workflows, use the current version of [Data Security Posture Management](data-security-posture-management-learn-about).

Because Data Security Posture Management for AI is your front door for securing and managing AI interactions, the following instructions use that solution:

- [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **DSPM for AI (classic)** with an account that has [appropriate permissions](ai-microsoft-purview-permissions). For example, an account that's a member of the **Microsoft Entra Compliance Administrator** group role.

    [![Selecting the Microsoft Purview Data Security Posture Management for AI solution from the Microsoft Purview portal.](media/dspm-solution.png)](media/example-dspm.png#lightbox)

### Discover potential security risks in interactions with other AI apps

1. From **DSPM for AI (classic)** &gt; **Overview**, in the **Get Started** section, locate and take action on the following required steps:

    - **Install Microsoft Purview browser extension**
    - **Onboard devices to Microsoft Purview**
    - **Extend your insights for data discovery**

    If you need more information about the browser extension, or other onboarding requirements, see [Prerequisites for Data Security Posture Management for AI](ai-microsoft-purview-considerations#prerequisites-for-data-security-posture-management-for-ai).

    For more information about the one-click policies that are automatically created with the option to extend your insights for data discovery, see [Default policies for data discovery using Data Security Posture Management for AI](dspm-for-ai-considerations#one-click-policies-from-data-security-posture-management-for-ai) and the policies that have the source of **Extend your insights for data discovery**.
2. Wait at least a day for data, and then navigate to the **Reports** page to view the results of your policy. Select **Other AI apps** and view information such as:

    - Total interactions over time (other AI apps)
    - Total visits (other AI apps)
    - Sensitive interactions per AI app
    - Insider Risk severity
    - Insider risk severity per AI apps
3. Select **View details** for each of the report graphs to view detailed activities in the activity explorer.

    Select the available filters to see the results from **Copilot experiences & agents** based on the different **Activity type**, **AI app category**, **App**, and **Scope** for administrative units, and more. Then drill down to each activity to view details that include displaying the prompts and response when you're a member of the Microsoft Purview Content Explorer Content Viewer role group. For more information about this requirement, see [Permissions for Data Security Posture Management for AI](ai-microsoft-purview-permissions).

### Protect sensitive data in interactions with other AI apps

1. From **DSPM for AI (classic)** &gt; **Recommendations** page, under **Not Started**, select **Fortify your data security** to create the following [one-click policies](dspm-for-ai-considerations#one-click-policies-from-data-security-posture-management-for-ai):

    - **Block elevated risk users from pasting or uploading sensitive info on AI sites**: This recommendation creates a policy that uses Adaptive Protection to give a block-with-override to elevated risky users attempting to paste or upload sensitive information to other AI apps in Edge, Chrome, and Firefox. This policy covers all users and groups in your org in test mode.
    - **Block elevated risk users from submitting prompts to AI apps in Microsoft Edge**: This recommendation guides you through the process of creating a Purview Data Loss Prevention (DLP) policy to [block elevated, moderate, and minor risk users attempting to put information in AI apps while using Microsoft Edge](dlp-learn-about-dlp).
    - **Block sensitive info sharing to AI apps in Edge**: This recommendation guides you through the process of creating a Purview Data Loss Prevention (DLP) policy to [detect inline for a selection of common sensitive information types and blocks prompts from being sent in AI apps while using Microsoft Edge](dlp-learn-about-dlp).

### Apply compliance controls to interactions with other AI apps

If you need to ensure that interactions with supported other AI apps are retained for compliance reasons:

- In the Microsoft Purview portal, navigate to **Data Lifecycle Management** &gt; **Policies** &gt; **Retention Policies** and create a retention policy to retain interactions with other AI apps by selecting the location **Other AI apps** and specify the required retention period. For more information, see [Create and configure retention policies](create-retention-policies).

    Note

    Retention is supported only for the Edge browser, and for ChatGPT, Microsoft Chat (consumer version), Google Gemini, and DeepSeek.
- In the Microsoft Purview portal, navigate to **eDiscovery** &gt; **Cases** &gt; **Create case**. In the case, [create a search](edisc-search-query) and use the *ItemClass* property and the `IPM.SkypeTeams.Message.ConnectedAIApp.Connector.<AppName>` value for local machine activities or the `IPM.SkypeTeams.Message.CloudAIApp.SaaS.<AppID>` value for browser-based activities to search for these interactions in your organization.

Routinely review the reports in DSPM for AI to determine if you need to make changes, and use activity explorer and [events](dspm-for-ai-considerations#activity-explorer-events) for deeper analysis of how users are interacting with other AI apps when they use a browser to third-party AI sites.