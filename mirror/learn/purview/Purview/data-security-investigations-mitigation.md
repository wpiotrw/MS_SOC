---
layout: Conceptual
title: Review mitigation recommendations in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-mitigation
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Discover how to review mitigation recommendations in Data Security Investigations. Learn to analyze risks, generate reports, and implement AI-driven solutions.
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
document_id: 565a898d-191e-d206-993c-cb2e850b057c
document_version_independent_id: 565a898d-191e-d206-993c-cb2e850b057c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-mitigation.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-mitigation
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-mitigation.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: d1ce4590-dcf0-1aff-007b-a7a7e4bc41b0
---

# Review mitigation recommendations in Data Security Investigations | Microsoft Learn

## Analyze data for mitigation information

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
8. Select *Mitigation: Identify threats and recommend mitigation steps in selected evidence* in the **Choose a focus area** field.
9. Select **Examine** to start the AI analysis.

Note

The time estimates for the process to complete are based on the amount and size of the selected data. To reduce processing time, filter and exclude data not applicable to the investigation.

## Mitigation recommendation report

After the AI processing completes for the selected data items, you can review the mitigation plan to identify details and recommended mitigation steps for each item.

The mitigation recommendation reports include the following information for each item:

- **Subject/Title**: The subject or title of the data item.
- **Risk score**: The risk score of the data item. Values range from 0.00 to 0.10.
- **Risk summary**: A summary of the risks associated with an item. Includes information about content types, users, senders/recipients, details about communications, and more.
- **Mitigation steps**: Guidance for recommended steps to help mitigate the risk associated with the item. Includes audit log reviews, location tracing, access reviews, monitoring suggestions, and more.
- **Thought process**: A summary of the reasoning as to why the risks associated with the item are important. Includes security, legal, financial justifications, and more.
- **Risk implications**: A summary of the implications if the identified risks aren't addressed.
- **Errors**: A summary of any processing errors encountered when the AI process runs.