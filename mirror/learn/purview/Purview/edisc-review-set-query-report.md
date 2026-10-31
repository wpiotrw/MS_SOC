---
layout: Conceptual
title: Use the Query Report to create keyword reports for KeyQL queries | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-review-set-query-report
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use the Query Report to generate keyword reports for KeyQL queries in eDiscovery.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-19T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 13ac003b-c9e4-d502-3f46-e01d824b1a6a
document_version_independent_id: 13ac003b-c9e4-d502-3f46-e01d824b1a6a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-review-set-query-report.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-review-set-query-report
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-review-set-query-report.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: ea727f33-fc5b-0bb9-9fa3-43ab056e32c9
---

# Use the Query Report to create keyword reports for KeyQL queries | Microsoft Learn

When you filter in a review set, it can be difficult to compare filtered results when using multiple saved queries. The Query Report helps you generate and download a consolidated report on multiple queries for a review set. With the consolidated query report, you can quickly see the total count and volume of filtered items on a particular keyword search or multiple compound KeyQL queries.

Select an individual query report item to review specific filtered items. You can select individual items and view the source, plain text, and metadata information for an item.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Create a query report

To create a query report in a review set, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, then select **Cases**.
3. Select a case, then select the **Review sets** tab.
4. Select a review set, then select the **All items** tab.
5. Select **Actions** &gt; **Query Report**.
6. On the **Query Report** page, enter your search queries and separate each with a line break (pressing enter on your keyboard). A report is generated for each search query line.

    For example, if you want to filter by:

    - a keyword *confidential* in items for one query,
    - a filter for two keywords *confidential* and *Project Infinity* in items for another query,
    - and filter using a complex KeyQL statement *(((FileClass="Email") AND (InclusiveType="InclusiveMinus" OR InclusiveType="Inclusive")) OR ((FileClass="Attachment") AND (UniqueInEmailSet="true")) OR ((FileClass="Document") AND (MarkAsRepresentative="Unique")) OR (FileClass="Conversations"))* for a third query,

    You would use the following values on separate lines in the **Query Report (preview)** search query field:

    `confidential``confidential AND Project Infinity``(((FileClass="Email") AND (InclusiveType="InclusiveMinus" OR InclusiveType="Inclusive")) OR ((FileClass="Attachment") AND (UniqueInEmailSet="true")) OR ((FileClass="Document") AND (MarkAsRepresentative="Unique")) OR (FileClass="Conversations"))`
7. Select **Generate report**.

The results of the queries are summarized with the following information displayed for each query:

- **KeyQL**: The Keyword Query Language (KeyQL) statement used for the filter query.
- **Locations with hits**: The number of locations with filter query hits.
- **Count**: The number of items in the filter result.
- **Percentage**: The percentage of hits in the total count of items.
- **Size**: The file size of the items with hits.

## Use the Query Report

To view the individual items that the filter queries return, double-select the filter query line in the report. Select an individual item to view item details. The item information is read-only, so you can't annotate, modify, or export these items.

To download the report summary information for the filter queries, select **Download report** to create a .csv file containing the report summary information. When you exit the Query Report, the filter queries aren't saved.