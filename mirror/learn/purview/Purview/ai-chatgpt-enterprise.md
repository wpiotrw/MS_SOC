---
layout: Conceptual
title: Use Microsoft Purview to manage data security & compliance for ChatGPT Enterprise | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ai-chatgpt-enterprise
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: sseth
ms.service: purview
ms.update-cycle: 180-days
ms.date: 2026-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.collection:
- highpri
- m365copilot
- msec-ai-copilot
description: Use Microsoft Purview to help you protect and manage data security and compliance protections for ChatGPT Enterprise.
locale: en-us
document_id: c7caf131-dd88-02c1-9a70-f11d42a83299
document_version_independent_id: c7caf131-dd88-02c1-9a70-f11d42a83299
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ai-chatgpt-enterprise.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ai-chatgpt-enterprise
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ai-chatgpt-enterprise.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: d417c231-29af-3302-d5b6-a040e31b75da
---

# Use Microsoft Purview to manage data security & compliance for ChatGPT Enterprise | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use the following sections to identify the [Microsoft Purview capabilities that are supported for AI interactions](ai-microsoft-purview) with ChatGPT Enterprise, and some get started recommendations for you to manage these AI interactions for security and compliance.

For setup information and prerequisites, see [Connect to and manage ChatGPT Enterprise AI interactions in Microsoft Purview](archive-chatgpt-interactions). You must run the connector scan before Microsoft Purview can manage the AI interactions for ChatGPT Enterprise.

Managing these AI interactions with Microsoft Purview requires you to enable [pay-as-you-go billing](purview-billing-models) in your organization.

## Capabilities supported

Use the following table to see at a glance the Microsoft Purview capabilities that are supported for ChatGPT Enterprise.

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

Note

These features only apply to the enterprise version of ChatGPT. For more information on the available Purview features for the consumer version, see [Learn about Microsoft Purview Network Data Security](dlp-network-data-security-learn) and [Learn about Data Loss Prevention for Cloud Apps in Edge for Business](dlp-browser-dlp-learn).

### DSPM and DSPM for AI (classic)

Use [Data Security Posture Management](data-security-posture-management-learn-about) or [Data Security Posture Management for AI (classic)](dspm-for-ai) as your front door to discover, secure, and apply compliance controls for AI usage across your enterprise. Both DSPM versions use existing controls from Microsoft Purview information protection and compliance management with easy-to-use graphical tools and reports to quickly gain insights into AI use within your organization. With personalized recommendations, and one-click policies help you protect your data and comply with regulatory requirements.

###### AI app-specific information:

- Recommendation **Get guided assistance to AI regulations**, which uses [control-mapping regulatory templates from Compliance Manager](compliance-manager-regulations).
- [One-click policies](dspm-for-ai-considerations#one-click-policies-from-data-security-posture-management-for-ai) available:

    - **DSPM for AI - Capture interactions for enterprise AI apps** from the recommendation or remediation action **Secure interactions from enterprise apps**.
    - **DSPM for AI - Detect sensitive info shared with AI via network** from the recommendation or remediation action **Extend insights into sensitive data in AI app interactions**.

### Auditing and AI interactions

[Microsoft Purview Audit solutions](audit-solutions-overview) provide comprehensive tools for searching and managing audit records of activities performed across various Microsoft services by users and admins, and help organizations to effectively respond to security events, forensic investigations, internal investigations, and compliance obligations.

Like other activities, prompts and responses are [captured in the unified audit log](audit-log-activities). Events include how and when users interact with the AI app, and can include in which Microsoft 365 service the activity took place, and references to the files stored in Microsoft 365 that were accessed during the interaction. If these files have a sensitivity label applied, that's also captured.

These events flow into [activity explorer](ai-microsoft-purview-considerations#activity-explorer-events) in the **AI activities** tab in the current version of DSPM and in DSPM for AI, where the data from prompts and responses can be displayed. You can also use the **Audit** solution from the [Microsoft Purview portal](purview-portal) to search and find these auditing events.

For more information, see [Audit logs for Copilot and AI activities](audit-copilot).

### Data classification and AI interactions

Microsoft Purview data classification provides a comprehensive framework for identifying and tagging sensitive data across various Microsoft services, including Office 365, Dynamics 365, and Azure. Classifying data is often the first step to ensure compliance with data protection regulations and safeguard against unauthorized access, alteration, or destruction. You can use built-in system classifications or create your own.

Sensitive information types and trainable classifiers can be used to find sensitive data in user prompts and responses when they use AI apps. The resulting information then surfaces in [Microsoft Purview Reports overview](purview-reports) and [activity explorer](ai-microsoft-purview-considerations#activity-explorer-events) in DSPM for AI and the **AI activities** tab in activity explorer from the preview version of DSPM.

### Insider Risk Management and AI interactions

[Microsoft Purview Insider Risk Management](insider-risk-management) helps you detect, investigate, and mitigate internal risks such as IP theft, data leakage, and security violations. It leverages machine learning models and various signals from Microsoft 365 and third-party indicators to identify potential malicious or inadvertent insider activities. The solution includes privacy controls like pseudonymization and role-based access, ensuring user-level privacy while enabling risk analysts to take appropriate actions.

Use the [Risky AI usage policy template](insider-risk-management-policy-templates#risky-ai-usage) to detect risky usage that includes prompt injection attacks and accessing protected materials. Insights from these signals are integrated into Microsoft Defender XDR to provide a comprehensive view of AI-related risks.

###### AI app-specific information:

- For prompts and responses, requires a [collection policy](collection-policies-solution-overview) such as **DSPM for AI - Capture interactions for enterprise AI apps** from the DSPM for AI recommendation **Secure interactions from enterprise apps**.

### Communication compliance and AI interactions

[Microsoft Purview Communication Compliance](communication-compliance) provides tools to help you detect and manage regulatory compliance and business conduct violations across various communication channels, which include user prompts and responses for AI apps. It's designed with privacy by default, pseudonymizing usernames and incorporating role-based access controls. The solution helps identify and remediate inappropriate communications, such as sharing sensitive information, harassment, threats, and adult content.

To learn more about using communication compliance policies for AI apps, see [Configure a communication compliance policy to detect for generative AI interactions](communication-compliance-copilot).

###### AI app-specific information:

- For prompts and responses, requires a [collection policy](collection-policies-solution-overview) such as **DSPM for AI - Capture interactions for enterprise AI apps** from the DSPM for AI recommendation **Secure interactions from enterprise apps**.

### eDiscovery and AI interactions

[Microsoft Purview eDiscovery](edisc) lets you identify and deliver electronic information that can be used as evidence in legal cases. The eDiscovery tools in Microsoft Purview support searching for content in Exchange Online, OneDrive for Business, SharePoint Online, Microsoft Teams, Microsoft 365 Groups, and Viva Engage teams. You can then prevent the information from deletion and export the information.

Because user prompts and responses for AI apps are stored in a user's mailbox, you can create a case and use [search](edisc-search-query) when a user's mailbox is selected as the source for a search query. For example, select and retrieve this data from the source mailbox by selecting from the query builder **Add condition** &gt; **Type** &gt; **Contains any of** &gt; **Edit** &gt; *Copilot activity*. This query condition includes all Copilot and other AI application activity.

After the search is refined, you can export the results or add to a [review set](edisc-review-set-manage). You can review and export information directly from the review set.

For more information about identifying and deleting user AI interaction data, see [Search for and delete Copilot data in eDiscovery](edisc-search-copilot-data).

###### AI app-specific information:

- For prompts and responses, requires a [collection policy](collection-policies-solution-overview) such as **DSPM for AI - Capture interactions for enterprise AI apps** from the DSPM for AI recommendation **Secure interactions from enterprise apps**.

### Data Lifecycle Management and AI interactions

[Microsoft Purview Data Lifecycle Management](data-lifecycle-management) provides tools and capabilities to manage the lifecycle of organizational data by retaining necessary content and deleting unnecessary content. These tools ensure compliance with business, legal, and regulatory requirements.

Use [retention policies](retention) to automatically retain or delete user prompts and responses for AI apps. For detailed information about this retention works, see [Learn about retention for Copilot & AI apps](retention-policies-copilot).

As with all retention policies and holds, if more than one policy for the same location applies to a user, the [principles of retention](retention#the-principles-of-retention-or-what-takes-precedence) resolve any conflicts. For example, the data is retained for the longest duration of all the applied retention policies or eDiscovery holds.

###### AI app-specific information:

- For retention policies, select the option for **Enterprise AI apps**.
- For prompts and responses, requires a [collection policy](collection-policies-solution-overview) such as **DSPM for AI - Capture interactions for enterprise AI apps** from the DSPM for AI recommendation **Secure interactions from enterprise apps**.

#### Compliance Manager and AI interactions

[Microsoft Purview Compliance Manager](compliance-manager) is a solution that helps you automatically assess and manage compliance across your multicloud environment. Compliance Manager can help you throughout your compliance journey, from taking inventory of your data protection risks to managing the complexities of implementing controls, staying current with regulations and certifications, and reporting to auditors.

To help you keep compliant with AI regulations, Compliance Manager provides regulatory templates to help you assess, implement, and strengthen your compliance requirements for all generative AI apps. For example, monitoring AI interactions and preventing data loss in AI applications. For more information, see [Assessments for AI regulations](compliance-manager-assessments#assessments-for-ai-regulations).

## Getting started recommended steps

Use the following steps to get started with managing data security & compliance for AI interactions that use ChatGPT Enterprise.

Note

These steps focus on managing a specific AI app or agent. For broader coverage that uses security objectives with guided workflows, use the current version of [Data Security Posture Management](data-security-posture-management-learn-about).

Because Data Security Posture Management for AI is your front door for securing and managing AI interactions, most of the following instructions use that solution:

- [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **DSPM for AI (classic)** with an account that has [appropriate permissions](ai-microsoft-purview-permissions). For example, an account that's a member of the **Microsoft Entra Compliance Administrator** group role.

    [![Selecting the Microsoft Purview Data Security Posture Management for AI solution from the Microsoft Purview portal.](media/dspm-solution.png)](media/example-dspm.png#lightbox)

1. From **DSPM for AI (classic)** &gt; **Recommendations** page, locate and select **Discover and govern interactions with ChatGPT Enterprise AI**, which has set up instructions to capture prompts and responses for AI apps that use one or more Azure AI subscriptions.
2. Also from the recommendations list, select **Secure interactions from enterprise apps**, which creates a [one-click policy](dspm-for-ai-considerations#one-click-policies-from-data-security-posture-management-for-ai) to capture prompts and responses from enterprise AI apps.
3. Wait at least a day for data, and then navigate to the **Reports** page to view the results of your policy. Select the AI app category of **Enterprise AI apps** and view information such as:

    - Total interactions over time (enterprise AI apps)
    - Sensitive interactions per AI app
    - Insider Risk severity
    - Insider risk severity per AI app
4. Select **View details** for each of the report graphs to view detailed activities in the activity explorer.

    From the filters, select the **AI app category** of **Enterprise AI apps** with the **App** filter of **ChatGPT Enterprise**, and then use the other filters if you need to further refine the displayed data. Drill down to each activity to view details that include displaying the prompts and response when you're a member of the Microsoft Purview Content Explorer Content Viewer role group. For more information about this requirement, see [Permissions for Data Security Posture Management for AI](ai-microsoft-purview-permissions).
5. If you need to ensure that interactions from ChatGPT Enterprise are retained for compliance reasons:

    In the Microsoft Purview portal, navigate to **Data Lifecycle Management** &gt; **Policies** &gt; **Retention Policies** and create a retention policy to retain interactions with ChatGPT Enterprise by selecting the location **Enterprise AI apps** and specify the required retention period. For more information, see [Create and configure retention policies](create-retention-policies).
6. If you need to preserve, collect, analyze, review, or export ChatGPT Enterprise interactions:

    In the Microsoft Purview portal, navigate to **eDiscovery** &gt; **Cases** &gt; **Create case**. In the case, [create a search](edisc-search-query) and use the *ItemClass* property and the `IPM.SkypeTeams.Message.ConnectedAIApp.Connector.<ChatGPTEnterprise>` value for local machine activities or the `IPM.SkypeTeams.Message.CloudAIApp.SaaS.<AppID>` value for browser-based activities to search for these interactions in your organization.

Routinely review the reports in DSPM for AI to determine if you need to make changes, and use activity explorer and [events](dspm-for-ai-considerations#activity-explorer-events) for deeper analysis of how users are interacting with ChatGPT Enterprise.