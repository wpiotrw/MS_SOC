---
layout: Conceptual
title: Learn about the Data Security Investigations workflow | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-workflow
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Discover how the Data Security Investigations workflow helps you identify, investigate, and mitigate data security incidents efficiently using AI tools.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-security-investigations
ms.collection:
- purview-compliance
- data-security-investigations
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: fab02f49-4400-fe9b-240f-f6631f6cac3f
document_version_independent_id: fab02f49-4400-fe9b-240f-f6631f6cac3f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-workflow.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-workflow
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-workflow.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1577a46d-8446-40bd-bfae-0578362f4d94
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/cdf3f22d-5420-4d59-a2bf-66d6b3d9c828
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: a27c1ef0-9490-893e-dc50-8b4471bce11e
---

# Learn about the Data Security Investigations workflow | Microsoft Learn

The Data Security Investigations workflow helps you quickly identify, investigate, and take action on data associated with security and data breach incidents. This workflow isn't a linear process. It includes significant iteration requirements for several of the steps to fine tune searches, evidence gathering, classification, and investigation by using AI and activities.

Identifying and taking action on data and access uses the following workflow:

![Data Security Investigations workflow diagram.](media/dsi-workflow.png)

## Step 1: Identify and escalate incidents

### Identify a data security incident

Data breaches and other data security incidents require quick action to identify and contain potential risks to your organization. You need to quickly identify these incidents and streamline an integrated response. Investigating a data security incident can be daunting. It might include inefficient workflows across multiple tools, manual work, and extra complexity as the investigation grows in size. You might face labor-intensive reviews of impacted data and increased costs.

Data Security Investigations helps you investigate and mitigate data security incidents and accelerates the time to resolution. After you identify a data security incident, create a new investigation to enable your data security team to identify incident-related data, conduct deep content analysis, and mitigate risk within one unified solution.

### Escalate a data security incident from Microsoft Defender XDR

If you're already using [Microsoft Defender XDR](/en-us/defender-xdr/microsoft-365-defender?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json) in your organization, the [integration](data-security-investigations-investigation#create-an-investigation-from-defender-xdr) with Data Security Investigations allows you to quickly and seamlessly create a new investigation. The investigation automatically includes all incident-related data items from the Defender XDR incident node.

### Escalate a data security incident from Insider Risk Management

If you're already using [Insider Risk Management](insider-risk-management) in your organization, the [integration](data-security-investigations-investigation#create-an-investigation-from-insider-risk-management) with Data Security Investigations allows you to quickly create a new investigation for identified risky user activities.

### Escalate from an insight in Data Security Posture Management

If you're already using [Data Security Posture Management](data-security-posture-management-learn-about) in your organization, the [integration](data-security-investigations-investigation#create-an-investigation-from-data-security-posture-management) with Data Security Investigations allows you to quickly create a new investigation from potential data exfiltration findings and insights.

## Step 2: Create an investigation and find impacted data

Creating an investigation in Data Security Investigations is quick and easy. Depending on your scenario, you can create investigations from:

- **Microsoft Defender XDR incidents**: Create an investigation from a [Defender XDR incident](data-security-investigations-investigation#create-an-investigation-from-defender-xdr).
- **Microsoft Purview Insider Risk Management cases**: Create an investigation from [Insider Risk Management](data-security-investigations-investigation#create-an-investigation-from-insider-risk-management).
- **Data Security Posture Management insights**: Create an investigation from [Data Security Posture Management](data-security-investigations-investigation#create-an-investigation-from-data-security-posture-management) exfiltration findings, or enable proactive AI insights that auto-create an investigation.
- **Manually by using full draft mode**: Create an investigation by using the [full draft mode option](data-security-investigations-investigation-full-draft-mode) to configure specific data sources and search conditions.

## Step 3: Search, evaluate results, and review

After creating an investigation, you can review and update data sources. Use search tools to identify items related to the data security incident. This review includes items from the following Microsoft 365 services:

| Data source | Content type searched | Risky content examples |
| --- | --- | --- |
| Endpoint Data Loss Prevention (DLP) | Files captured by endpoint DLP evidence collection | Files copied to USB, printed, uploaded to cloud, or accessed by unauthorized apps on onboarded devices. |
| Exchange Online | Emails and attachments in user mailboxes | Credentials or secrets sent in email, sensitive files shared externally. |
| Microsoft Copilot | AI prompts and responses | Sensitive data in Copilot or AI prompts. |
| Microsoft Teams | Chat messages (1:1 and group chats) and channel posts | Secrets included in chats, confidential information in Teams conversations. |
| OneDrive | User files | User files with secure access keys, export of databases, and more. |
| SharePoint | Documents and files in sites | Documents containing passwords, customer data, or confidential plans. |

You can create and run different [searches](data-security-investigations-search) that are associated with an investigation. Use conditions such as keywords, file types, incidents, and more in the [query builder](data-security-investigations-search#query-builder) to create custom search queries. These queries return results with the data most likely relevant to the data security incident. You can also use [audit search](data-security-investigations-search#audit-search) to identify content based on user activities recorded in the unified audit log, such as files accessed, downloads, and sensitivity label changes. Additionally, you can use [endpoint DLP evidence collection](data-security-investigations-search#endpoint-dlp-evidence-collection-preview) to query data captured by endpoint DLP policies on onboarded devices.

## Step 4: Add data to the investigation scope

After you review and refine your search query, add all relevant data items to the [investigation scope](data-security-investigations-scope). In this step, you filter and review specific data items. You also identify any items you don't want to review by using AI tools in Data Security Investigations.

## Step 5(a): Investigate items

After adding data items to the [investigation scope](data-security-investigations-scope), start refining and narrowing the data to the most relevant items for your investigation. Narrowing the items to the smallest amount of applicable data helps increase the speed and reduce costs associated with AI processing.

In this step, perform the following actions:

- Select specific items to add directly to your [mitigation plan](data-security-investigations-mitigation-actions) if applicable.
- Identify or exclude specific items from [AI processing](data-security-investigations-ai-analysis).

After data items are added to the investigation scope, the system [automatically prepares all items](data-security-investigations-scope#automatic-vectorization). This automatic vectorization enables semantic searches and categorization of data.

## Step 5(b): Investigate with AI

After Add to scope completes for the data items in the investigation, start using AI-related tools to help narrow the focus of your investigation to only the most impactful and critical items.

Use the following tools and actions in your review to identify and take action on specific data items:

- Use [vector search](data-security-investigations-ai#vector-search) for natural language queries to identify items for review.
- Use [Search with AI (preview)](data-security-investigations-ai#search-with-ai-preview) with natural language queries and keywords to summarize search results for review.
- Define and configure [AI-driven categories](data-security-investigations-ai#categorization) for the content.
- Use built-in and custom [examination areas](data-security-investigations-ai#examination) for selected items.
- Select items to add to the [mitigation plan](data-security-investigations-mitigation-actions).

Important

Storage and AI capacity cost considerations are associated with the usage of each of the AI tools in Data Security Investigations. For more information, see [Billing models in Data Security Investigations](data-security-investigations-billing) and [Use AI analysis in Data Security Investigations](data-security-investigations-ai-analysis).

## Step 6: Take actions to mitigate

After you identify the most relevant and impactful items associated with the data security incident, take specific actions to help mitigate risks.

- **Review mitigation recommendations**: When you select items for examination and choose *Mitigation* as the focus area, the solution creates [mitigation recommendations](data-security-investigations-mitigation). Automated AI processing identifies related threats and recommends mitigation steps.
- **Review credentials examinations**: When you select items for examination and choose *Credentials* as the focus area, the solution identifies [credentials and other access asset examinations](data-security-investigations-credentials). AI analysis processing automatically identifies and generates credential details, type, and specific recommendations.
- **Review risk examinations**: When you select items for examination and choose *Risks* as the focus area, the solution automatically creates a security [risk score and examination](data-security-investigations-risks). The risk score helps you prioritize mitigation actions for the most impactful and risky data items.
- **Review personal data examinations**: When you select items for examination and choose *Personal Data* as the focus area, the solution identifies and extracts [personal data](data-security-investigations-personal-data) from selected items. AI analysis processing automatically identifies PII types, extracts values, and provides surrounding context.
- **Use the mitigation plan**: After reviewing examinations and recommendations, add specific data items from the investigation scope to the [mitigation plan](data-security-investigations-mitigation-actions). This plan helps you manage and track the mitigation status for each data item.
- **Purge items if needed**: Create a search query and save it as a purge query to help you identify and [remove items](data-security-investigations-mitigation-actions#purge) in your organization. You can soft purge items to move them to the recoverable items folder or hard purge items to permanently delete them.

## Best practices

- **Iterate and use AI analysis wisely**: Investigations rarely finish in one step. Use the AI suggestions in [categorization](data-security-investigations-ai-analysis#use-categorization) and [vector search](data-security-investigations-ai-analysis#use-vector-search) to uncover hidden issues. Always validate any critical findings by using human judgment. The investigator’s judgment is key in critical decision-making.
- **Keep the investigation scope focused**: It’s easy to get overwhelmed as you discover more data. Use [categorization](data-security-investigations-ai-analysis#use-categorization) to exclude irrelevant information and concentrate primarily on any risky items.
- **Engage the right teams in your organization early**: Data security incidents often span multiple areas. These areas might include security, IT, and compliance in your organization. Share with partner teams as soon as you identify areas needing action.
- **Use integrated Microsoft services**: Data Security Investigations is part of the broader Microsoft Purview and Defender ecosystem. If your investigation suggests an insider risk, open an [Insider Risk Management](insider-risk-management) case. If it started from a [Microsoft Defender XDR](/en-us/defender-xdr/microsoft-365-defender?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json) alert, update that incident with your findings. The goal is an end-to-end view of the incident in your organization.

## Email and portal notifications

Data Security Investigations sends notifications to inform investigators about setup status and keep them updated on investigation progress. Notifications are delivered through both the Microsoft Purview Notification Center (bell icon in the Microsoft Purview portal) and email. Email notifications include the investigation name as the header and a button that links directly to the relevant page in the Microsoft Purview portal.

The following table describes the notifications associated with setup and onboarding:

| Notification | Trigger | Recipients | Description |
| --- | --- | --- | --- |
| Setup complete | Initial setup is completed | All users with Data Security Investigations roles | Notifies all assigned users that Data Security Investigations is configured and ready for use. |
| Integration investigation ready | Initial setup is completed and user previously created investigations from [Microsoft Defender XDR](/en-us/defender-xdr/microsoft-365-defender?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json), [Insider Risk Management](insider-risk-management), or [Data Security Posture Management](data-security-posture-management-learn-about) | Users who created investigations before setup completed | Directs users back to their pre-existing investigation to begin AI analysis. |
| Setup reminder | User created an investigation but initial setup isn't completed after 7 days | User who created the investigation | Reminds the user or their admin to complete setup so the investigation can proceed. |
| Permissions provisioning complete | 1 hour after permissions assignment when final onboarding step isn't completed | User completing onboarding | Reminds the user to complete the final onboarding step after permissions are provisioned. |

Note

Notification preference settings aren't currently available. All users with Data Security Investigations roles receive notifications for the scenarios listed in this section.

## Ready to get started?

- [Get started with Data Security Investigations](data-security-investigations-get-started)