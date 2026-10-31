---
layout: Conceptual
title: Review risk examinations in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-risks
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Discover how to review risk examinations in Data Security Investigations. Analyze data, understand risk scores, and take action to secure your organization.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-11T00:00:00.0000000Z
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
document_id: d8a919bb-37af-af7c-a0d9-e1ecd342b423
document_version_independent_id: d8a919bb-37af-af7c-a0d9-e1ecd342b423
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-risks.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-risks
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-risks.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 4da127bf-ae52-31b6-a88a-084f2db2b08a
---

# Review risk examinations in Data Security Investigations | Microsoft Learn

By examining impacted data for security risks, you can find network risks or data that presents continued security risks in your organization. Risk examinations provide reasoning for risk scores and recommended mitigation steps for each item so you can take the appropriate mitigation steps. Data Security Investigations summarizes scores and explanations for the [risk focus areas](data-security-investigations-ai#examination).

## Analyze data for risk information

Complete the following steps to identify risks in data items included in the investigation scope:

Important

[Add to scope](data-security-investigations-scope#automatic-vectorization) must complete before you can configure examinations.

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in with the credentials for a user account assigned [Data Security Investigations permissions](data-security-investigations-permissions).
2. Select **Investigations** in the left navigation.
3. Select an investigation, then select **Analysis** on the navigation bar.
4. Use vector search or categorization tools to identify data for credentials examination.
5. Select one or more items, then select **Examine** on the command bar.
6. In the **Examine** dialog, enter a name for your examination process in the **Name** field.
7. Enter a description for the examination process in the **Description** field.
8. Select *Risk: Analyze and score all active risks in selected evidence* in the **Choose a focus area** field.
9. Select **Examine** to start the AI analysis.

Note

The time estimates for the process to complete are based on the amount and size of the selected data. To reduce processing time, filter and exclude data not applicable to the investigation.

Risk examination scores range between 0 (low risk) to 4 (critical risk) and include the following information for each item:

- **Subject/Title**: The subject or title of the data item.
- **Privileged content**: Indication if the data item is privileged content. Values are *Yes* or *No*.
- **Overall security risk score**: The risk score of the data item. Values from 0 to 4, higher values indicate higher risk items.
- **Overall security risk explanation**: A summary of the reasoning as to why the risks associated with the item are important.
- **Errors**: A summary of any processing errors encountered when the AI process runs.

The following risk examination areas, with scores and explanations, are available for each item:

- **Asset identifiers score**: Score reflecting the presence and severity of information related to identities or internal assets within emails and files.
- **Credentials and secrets exposure score**: Score reflecting the discussion of credential exposure within emails and files.
- **Customer intel risk score**: Score capturing the risk associated with confidential information related to business deals, trade secrets, corporate strategy, and cybersecurity vulnerabilities.
- **Government intel risk score**: Score capturing the risk associated with confidential government information related to security of infrastructure and products, domestic and foreign security, and domestic and foreign affairs.
- **Infrastructure risk score**: Score assessing the risk related to infrastructure exploits, critical gaps related to infrastructure, and potential infrastructure related discussions.
- **Network and access risk score**: Score reflecting the risk associated with network security and access control, including exposed ports and anonymous connections.
- **Personal sensitive content score**: Score reflecting the level of personal or sensitive information within emails and files, such as medical details, financial information, or confidential topics.
- **Policy compliance and data protection risk score**: Score capturing the risk associated with policy deviations, compliance, and data protection practices.
- **Privileged information risk score**: Score capturing the risk associated with exposure of privileged and confidential information and/or attorney communication for business matters.
- **Threat actor or breach discussion score**: Score reflecting the discussion of threat actors or sensitive topics within emails and files, including past breaches, ongoing investigations, or internally reported risks.
- **Trade secret risk score**: Score capturing the risk associated with policy deviations, compliance, and data protection practices.
- **Urgent security incident score**: Score reflecting the discussion of any urgent, immediately actionable security incidents that threat actors might find valuable.
- **Vulnerability and security hygiene information score**: Score reflecting the discussion of vulnerabilities within emails and files, such as zero-day exploits, security hygiene practices, internet-exposed endpoints, and over-provisioned accounts.