---
layout: Conceptual
title: Considerations for deploying Microsoft Purview Data Security Posture Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-posture-management-considerations
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: helenachen-microsoft
ms.service: purview
ms.subservice: purview-data-security-posture-management
ms.date: 2026-05-01T00:00:00.0000000Z
ms.update-cycle: 180-days
audience: Admin
ms.topic: reference
ms.collection:
- highpri
- tier1
- m365copilot
- msec-ai-copilot
description: Learn about deployment details for Microsoft Purview Data Security Posture Management that includes prerequisites, permissions, using the Data Security Posture Agent, and more.
locale: en-us
document_id: c106a815-03eb-3e8e-6d03-40715946d55c
document_version_independent_id: c106a815-03eb-3e8e-6d03-40715946d55c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-posture-management-considerations.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-posture-management-considerations
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-posture-management-considerations.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0fc65d4-7c73-4029-a261-7f99ff744363
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b2daec57-5914-4967-8ed3-1d444897ba59
platformId: defbffb7-d540-939e-070d-ca16110abb39
---

# Considerations for deploying Microsoft Purview Data Security Posture Management | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Note

This documentation is for the **current** version of Data Security Posture Management that expands coverage to more data sources, introduces guided workflows for proactive risk management, and streamlines data security operations so you can more confidently adopt AI across your digital estate.

Most new features will be added to this version only but you can still access the previous versions and their documentation:

- [DSPM for AI (classic)](dspm-for-ai)
- [DSPM (classic)](data-security-posture-management)

For the most part, [Microsoft Purview Data Security Posture Management](data-security-posture-management-learn-about) is easy to use and self-explanatory, guiding you through setup and configuration tasks to help secure and govern your data. Use this section to complement that information and provide additional details that you might need.

## Prerequisites for Data Security Posture Management

Use this section to identify prerequisites that aren't included in [setup tasks](data-security-posture-management-setup).

- You have a supporting license for this Microsoft Purview solution, and your region is supported. For more information, see the [Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description).
- You have the [right permissions](ai-microsoft-purview-permissions).
- For Microsoft 365 Copilot and agents, users are [assigned a license for Microsoft 365 Copilot](/en-us/microsoft-365-copilot/microsoft-365-copilot-enable-users#assign-licenses).

    - For Copilot in Fabric and Security Copilot:
        - The [enterprise version of Microsoft Purview data governance](data-governance-free-version-upgrade-to-enterprise), to support the required APIs.
        - A collection policy, such as the one created from the setup task **Secure interactions in Microsoft Copilot experiences**.
- For monitoring interactions and applying DLP policies to other AI apps in Edge:

    - An Edge configuration policy is required to activate the Microsoft Purview integration in Edge. For configuration information, see [Activate your DLP policy in Microsoft Edge](/en-us/deployedge/microsoft-edge-dlp-purview-configuration).
- For Fabric data risk assessments, shared with DSPM for AI (classic): [Configuration in both Entra and the Fabric admin portal](dspm-for-ai-considerations#prerequisites-for-fabric-data-risk-assessments).
- For Microsoft 365 custom data risk assessments and item-level scanning, shared with DSPM for AI (classic): [Configuration in the Entra admin portal](dspm-for-ai-considerations#prerequisites-for-microsoft-365-item-level-scanning-for-data-risk-assessments).
- For [Entra-registered AI apps](ai-entra-registered), they are [integrated with the Microsoft Purview SDK](/en-us/purview/developer) to support all the Microsoft Purview capabilities.
- For Security Copilot promptbooks and agents that support data discovery and remediation for sensitive data, [Enable Security Copilot for Purview Audit and DSPM Solutions](/en-us/copilot/security/audit-log#enable-security-copilot-for-purview-audit-and-dspm-solutions).

## Support for administrative units in Data Security Posture Management

When your tenant is configured for [administrative units](purview-admin-units), restricted administrators who view policies, reports, activity explorer or asset explorer see data for users in their assigned administrative units only.

Because the [one-click policies](dspm-for-ai-considerations#one-click-policies-from-data-security-posture-management-for-ai) apply to all users, restricted administrators can't create these policies. You must be an unrestricted administrator to create one-click policies.

## Activity explorer events in Data Security Posture Management

Use the following information to help you understand the events you might see in the activity explorer from Data Security Posture Management and the **AI activities** tab. References to a generative AI site can include Microsoft 365 Copilot, Microsoft 365 Copilot Chat, agents, other Microsoft copilots, and third-party AI sites.

| Event | Description |
| --- | --- |
| AI interaction | User interacted with a generative AI site. Details include the prompts and responses, except for unmanaged AI apps in Edge where text prompts only are included. For Microsoft 365 Copilot and Microsoft 365 Copilot Chat, this event requires auditing to be turned on. For Copilot in Fabric and Security Copilot, and for non-Copilot AI apps, prompts and responses require a collection policy with content capture selected to capture these interactions. |
| AI website visit | User browsed to a generative AI site. |
| DLP rule match | A data loss prevention rule was matched when a user interacted with a generative AI site. Includes DLP for Microsoft 365 Copilot. |
| Sensitive info types | Sensitive information types were found while a user interacted with a generative AI site. For Microsoft 365 Copilot and Microsoft 365 Copilot Chat, this event requires auditing to be turned on but doesn't require any active policies. |

Known issues:

- The **AI interaction** event doesn't always display text for the prompt and response. Sometimes, the prompt and response spans consecutive entries. Other scenarios can include:

    - Microsoft Facilitator AI-generated notes, no prompt or response is displayed
    - When a user doesn't have a mailbox hosted in Exchange Online, no prompt or response is displayed
- The **Sensitive info types detected** event doesn't display the user risk level.
- For Microsoft Facilitator AI-generated notes, **AI interaction** events can't be linked to **Sensitive info types detected** events.
- For collection policies, no prompt or response is displayed if the option to [capture content](collection-policies-solution-overview#content-capture-for-ai-interactions) isn't selected in the policy. For example, the one-click policy **DSPM for AI - Detect sensitive info shared with AI via network** doesn't select this option when the policy is automatically created, but you can manually edit the policy and select this option after the policy is created.

## Data updates paused for inactive tenants

To optimize resources,Microsoft pauses the background processing that refreshes Microsoft 365 data in Data Security Posture Management when a tenant hasn't accessed the solution for more than 60 days. While paused, you won't see any information for Microsoft 365 data in places such as in asset explorer, the data snapshot, and the data scanned posture metric.

Processing automatically resumes when you or another admin for your tenant returns to Data Security Posture Management. Data begins displaying again, although you can expect an initial delay. You might see an in-product message to indicate that updates were paused due to inactivity. This message disappears after processing resumes and no action is required from you to restart the updates.

## Using the Data Security Posture Agent

The Data Security Posture Agent is currently in preview.

This agent acts as a quick, intent-based search mechanism for sensitive data. It’s designed for pre-investigation checks rather than formal cases that still require other Microsoft Purview solutions, such as eDiscovery, audit, and Data Security Investigations. It uses natural‑language search and doesn't rely on keywords, sensitive information types, or classifiers to search across files in SharePoint and OneDrive, messages in Teams, emails in Exchange, and interactions with Copilot.

The Data Security Posture Agent is exclusive to the current version of Data Security Posture Management and isn't available in Data Security Posture Management (classic). Before you can use it, you must first activate and configure it. For more information, see [Get started with the Microsoft Purview Posture Agent in Data Security Posture Management](copilot-in-purview-posture-agent-get-started).

Run searches from **DSPM** &gt; **Discover** &gt; **Asset explorer** &gt; **Agent** tab. As with all Security Copilot agents, you can use this agent with preconfigured prompts and custom prompts. Before you run a custom prompt, you must first select **Add data sources**. In the flyout pane, enter at least 3 characters to search for users, groups, or sites. If you specify a user or group, the agent automatically selects the related mailbox, OneDrive account, or Sharepoint site. Keep in mind the following:

- For more efficient and faster processing, use a restricted search rather than tenant-wide searches.
- If you don't specify a time period for your prompt, search results are returned for the last 7 days.
- Search supports content up to 1 GB of data, but not metadata. For example, the agent can search all files containing financial information but not all files containing financial information and shared externally by a specific user in the last 7 days.

When a prompt is processed, you see a count of items matched against each item with any applied sensitivity labels and its risk level. The risk level is based on how closely related the match of the content is from the prompt provided to the agent.

The **View Insights** option provides a report that includes a summary, risk assessment, findings, labeled or unlabeled items, and the top unlabeled items. You can download this report as a Word document to share with others for further analysis.

For auditing events as a result of running this agent, see [Data Security Posture Agent activities](audit-log-activities#data-security-posture-agent-activities) from the auditing documentation.

## Tips for custom Security Copilot prompts in Data Security Posture Management

For an enhanced experience with Security Copilot in Data Security Posture Management, use the following tips for higher accuracy for your Copilot responses:

- Always include the user's UPN for questions involving a specific user.
- Always specify the complete name for the sensitive info type or label for questions that involve a specific type of sensitive info type or label.
- Clearly list the sorting criteria for questions for top users, activities, and alerts.
- Always specify the date period for questions for data in a specific date period. If you don't specify a date period, only data from the last 10 days from current date is included. The maximum lookback is 30 days from the current date.
- Put all items (classifiers or labels) in single quotes in your prompt.
- Use "/" as a separator for any path (for example, a file path) in a user prompt.
- Scope the prompt to a single intent for higher accuracy of responses. Break complex prompts into single intent questions and enter the prompts one by one.
- Make questions self-contained. Avoid referring to previous questions or responses.
- Avoid using generic terms.
- Support prompts for data security across Information Protection, DLP, Insider Risk Management, or from public documentation.

For more information about creating Security Copilot prompts, see [Create effective prompts](/en-us/copilot/security/prompting-tips).