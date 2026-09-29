---
layout: Conceptual
title: Use Microsoft Purview to manage data security & compliance for Microsoft Agent 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ai-agent-365
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: tiffanyyu
ms.service: purview
ms.update-cycle: 180-days
ms.date: 2026-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.collection:
- highpri
- tier1
- m365copilot
- msec-ai-copilot
description: Use Microsoft Purview to help you protect and manage data security and compliance protections for Microsoft Agent 365.
locale: en-us
document_id: e44c031d-d9ae-2e91-0b51-c6d7bafde606
document_version_independent_id: e44c031d-d9ae-2e91-0b51-c6d7bafde606
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ai-agent-365.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ai-agent-365
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ai-agent-365.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 12e45464-1fdd-2fdf-a7af-4f36d57db9b8
---

# Use Microsoft Purview to manage data security & compliance for Microsoft Agent 365 | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

## Capabilities supported

Use the following table to see at a glance the Microsoft Purview capabilities that are supported for [Microsoft Agent 365](/en-us/microsoft-agent-365/overview).

| Capability or solution in Microsoft Purview | Supported for AI interactions |
| --- | --- |
| DSPM and DSPM for AI (classic) | **✓** |
| Auditing | **✓** |
| Data classification | **✓** |
| Sensitivity labels | **✓** |
| Encryption without sensitivity labels | **✕** |
| Data loss prevention | **✓** |
| Insider Risk Management | **✓** |
| Communication compliance | **✓** |
| eDiscovery | **✓** |
| Data lifecycle management | **✓** |
| Compliance manager | **✓** |

When you create an agent instance for Agent 365, it's automatically enabled for audit, detection of sensitive data with data classification, and included with the [Assessments for AI regulations](compliance-manager-assessments#assessments-for-ai-regulations) from Compliance Manager. For other capabilities, include the agent instance in policies as you would a user.

### DSPM and DSPM for AI (classic)

Use [Data Security Posture Management](data-security-posture-management-learn-about) or [Data Security Posture Management for AI (classic)](dspm-for-ai) as your front door to discover, secure, and apply compliance controls for AI usage across your enterprise. Both DSPM versions use existing controls from Microsoft Purview information protection and compliance management with easy-to-use graphical tools and reports to quickly gain insights into AI use within your organization. With personalized recommendations, and one-click policies help you protect your data and comply with regulatory requirements.

###### AI app-specific information:

- Supported for Data Security Posture Management only, use the **AI observability** page to gain visibility into active agent instances to better understand potential risks and how to remediate them. For more information, see the Getting started recommended steps.

### Auditing and AI interactions

[Microsoft Purview Audit solutions](audit-solutions-overview) provide comprehensive tools for searching and managing audit records of activities performed across various Microsoft services by users and admins, and help organizations to effectively respond to security events, forensic investigations, internal investigations, and compliance obligations.

Like other activities, prompts and responses are [captured in the unified audit log](audit-log-activities). Events include how and when users interact with the AI app, and can include in which Microsoft 365 service the activity took place, and references to the files stored in Microsoft 365 that were accessed during the interaction. If these files have a sensitivity label applied, that's also captured.

These events flow into [activity explorer](ai-microsoft-purview-considerations#activity-explorer-events) in the **AI activities** tab in the current version of DSPM and in DSPM for AI, where the data from prompts and responses can be displayed. You can also use the **Audit** solution from the [Microsoft Purview portal](purview-portal) to search and find these auditing events.

For more information, see [Audit logs for Copilot and AI activities](audit-copilot).

###### AI app-specific information:

- Audit an agent instance as you would a user.
- Supported interactions: All agent-to-human, human-to-agent, agent-to-tools, and agent-to-agent interactions.
- In addition to displaying in activity explorer in DSPM, [search the audit log](audit-search) for [Agent 365 activities](audit-log-activities#agent-365-activities).

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

- For agent instances to access files, the files must be explicitly [shared](https://support.microsoft.com/en-us/office/share-your-documents-651e1cb9-9a51-46dc-8d32-bdb7d928eedd) with them.
- If an applied sensitivity label is [configured for encryption](encryption-sensitivity-labels), that encryption must explicitly grant the agent instance VIEW and EXTRACT usage rights. For example, a sensitivity label that's configured for **Add all users and groups in your organization** or **Add any authenticated users** wouldn't be sufficient.
- Newly created content from Agent 365 doesn't inherit sensitivity labels from the source items. As a result, that content isn't automatically labeled or encrypted.

### Data loss prevention and AI interactions

[Microsoft Purview Data Loss Prevention](dlp-learn-about-dlp) (DLP) helps you identify sensitive items across Microsoft 365 services and endpoints, monitor them, and helps protect against leakage of those items. It uses deep content inspection and contextual analysis to identify sensitive items and it enforces policies to protect sensitive data such as financial records, health information, or intellectual property.

Windows computers that are [onboarded to Microsoft Purview](device-onboarding-overview) can be configured for Endpoint data loss prevention (DLP) policies that warn or block users from sharing sensitive information with third-party generative AI sites that are accessed via a browser. For example, a user is prevented from pasting credit card numbers into ChatGPT, or they see a warning that they can override. For more information about the supported DLP actions and which platforms support them, see the first two rows in the table from [Endpoint activities you can monitor and take action on](endpoint-dlp-learn-about#endpoint-activities-you-can-monitor-and-take-action-on).

###### AI app-specific information:

- Supported by explicitly specifying agent instances in the DLP policy as you would a user, or by specifying a security group that includes agent instances.
- Supported interactions: Block or audit agent-to-human and human-to-agent for Microsoft Teams, OneDrive or SharePoint, and emails.
- Because an agent instance is unaware of the block action, the agent owner must actively monitor a DLP policy that uses this configuration and understand the impact to subsequent workflows.

### Insider Risk Management and AI interactions

[Microsoft Purview Insider Risk Management](insider-risk-management) helps you detect, investigate, and mitigate internal risks such as IP theft, data leakage, and security violations. It leverages machine learning models and various signals from Microsoft 365 and third-party indicators to identify potential malicious or inadvertent insider activities. The solution includes privacy controls like pseudonymization and role-based access, ensuring user-level privacy while enabling risk analysts to take appropriate actions.

Use the [Risky AI usage policy template](insider-risk-management-policy-templates#risky-ai-usage) to detect risky usage that includes prompt injection attacks and accessing protected materials. Insights from these signals are integrated into Microsoft Defender XDR to provide a comprehensive view of AI-related risks.

###### AI app-specific information:

- Supported by explicitly specifying agent instances in the Insider Risk Management policy as you would a user.
- Supports built-in trigger events, such as data exfiltration.

### Communication compliance and AI interactions

[Microsoft Purview Communication Compliance](communication-compliance) provides tools to help you detect and manage regulatory compliance and business conduct violations across various communication channels, which include user prompts and responses for AI apps. It's designed with privacy by default, pseudonymizing usernames and incorporating role-based access controls. The solution helps identify and remediate inappropriate communications, such as sharing sensitive information, harassment, threats, and adult content.

To learn more about using communication compliance policies for AI apps, see [Configure a communication compliance policy to detect for generative AI interactions](communication-compliance-copilot).

###### AI app-specific information:

- Supports detection of unethical communication for Microsoft Teams and emails, for agent-to-human and human-to-agent interactions.

### eDiscovery and AI interactions

[Microsoft Purview eDiscovery](edisc) lets you identify and deliver electronic information that can be used as evidence in legal cases. The eDiscovery tools in Microsoft Purview support searching for content in Exchange Online, OneDrive for Business, SharePoint Online, Microsoft Teams, Microsoft 365 Groups, and Viva Engage teams. You can then prevent the information from deletion and export the information.

Because user prompts and responses for AI apps are stored in a user's mailbox, you can create a case and use [search](edisc-search-query) when a user's mailbox is selected as the source for a search query. For example, select and retrieve this data from the source mailbox by selecting from the query builder **Add condition** &gt; **Type** &gt; **Contains any of** &gt; **Edit** &gt; *Copilot activity*. This query condition includes all Copilot and other AI application activity.

After the search is refined, you can export the results or add to a [review set](edisc-review-set-manage). You can review and export information directly from the review set.

For more information about identifying and deleting user AI interaction data, see [Search for and delete Copilot data in eDiscovery](edisc-search-copilot-data).

###### AI app-specific information:

- Identify an agent instance as you would a user.
- Supports agent-to-human and human-to-agent interactions.

### Data Lifecycle Management and AI interactions

[Microsoft Purview Data Lifecycle Management](data-lifecycle-management) provides tools and capabilities to manage the lifecycle of organizational data by retaining necessary content and deleting unnecessary content. These tools ensure compliance with business, legal, and regulatory requirements.

Use [retention policies](retention) to automatically retain or delete user prompts and responses for AI apps. For detailed information about this retention works, see [Learn about retention for Copilot & AI apps](retention-policies-copilot).

As with all retention policies and holds, if more than one policy for the same location applies to a user, the [principles of retention](retention#the-principles-of-retention-or-what-takes-precedence) resolve any conflicts. For example, the data is retained for the longest duration of all the applied retention policies or eDiscovery holds.

###### AI app-specific information:

- Supports locations that include Microsoft Teams, OneDrive and SharePoint, and emails.
- Supports agent-to-human and human-to-agent interactions.

#### Compliance Manager and AI interactions

[Microsoft Purview Compliance Manager](compliance-manager) is a solution that helps you automatically assess and manage compliance across your multicloud environment. Compliance Manager can help you throughout your compliance journey, from taking inventory of your data protection risks to managing the complexities of implementing controls, staying current with regulations and certifications, and reporting to auditors.

To help you keep compliant with AI regulations, Compliance Manager provides regulatory templates to help you assess, implement, and strengthen your compliance requirements for all generative AI apps. For example, monitoring AI interactions and preventing data loss in AI applications. For more information, see [Assessments for AI regulations](compliance-manager-assessments#assessments-for-ai-regulations).

## Getting started recommended steps

To get started with managing data security & compliance for Agent 365. use the [Microsoft Purview portal](purview-portal). You need an account that has appropriate permissions for security and compliance management, such as an account that's a member of the Entra **Compliance Administrator** role, or the **Microsoft Purview Compliance Administrator** role group.

Then navigate to [Data Security Posture Management](data-security-posture-management-learn-about): **DSPM** &gt; **AI observability**.

Note

Don't confuse this current version with the older version, that's named **Data Security Posture Management (classic)**. The classic version doesn't support Agent 365.

From the **AI observability** page:

- Review the overview of all agents in your organization with activities in the last 30 days, prioritized with the highest risk level determined by Insider Risk Management.
- Analyze top risky activities: oversharing, exfiltration, and unethical behavior.
- Select a specific agent to see details:
    - Agent details that include Entra-enabled status, created date, owner, agent user ID, and which agent it's an instance of.
    - Agent activities that include the risk level determined by Insider Risk Management and any risky activities from agent interactions.
    - Recommendations for remediation that use Microsoft Purview solutions, based on the identified risks.