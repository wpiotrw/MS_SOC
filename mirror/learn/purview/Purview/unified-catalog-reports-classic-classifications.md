---
layout: Conceptual
title: Classic Classifications Report in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-reports-classic-classifications
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2024-04-07T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to view and use Microsoft Purview classification reporting on your data.
locale: en-us
document_id: 4f8b4cb2-b6c9-cde3-795f-097d96fde8b3
document_version_independent_id: 4f8b4cb2-b6c9-cde3-795f-097d96fde8b3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-reports-classic-classifications.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-reports-classic-classifications
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-reports-classic-classifications.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: c1d79b2b-e242-9758-0aaa-b53ffb9afd66
---

# Classic Classifications Report in Unified Catalog | Microsoft Learn

This article describes how to access, view, and filter the classic classifications report for your data.

In this article, you learn how to:

- Launch your Microsoft Purview account from Microsoft Azure.
- View classification insights on your data.
- Drill down for more classification details on your data.

## Prerequisites

Before getting started with Data Estate Insights, make sure you complete the following steps:

- Set up a storage resource and populate the account with data.
- Set up and complete a scan on the data in each data source. For more information, see [Manage data sources in Microsoft Purview](data-map-data-sources-register-manage) and [Create a scan rule set](data-map-scan-rule-set).
- Permissions depending on your current experience:
    - [If using the classic Microsoft Purview Catalog](use-microsoft-purview-governance-portal), you need the [data curator role or insight reader role](data-gov-classic-permissions#roles).
    - [If using the new Microsoft Purview Unified Catalog](unified-catalog), you need [data health reader](data-governance-roles-permissions#unified-catalog-permissions) permissions.

## Use Data Estate Insights for classifications

In Microsoft Purview, classifications are similar to subject tags, and are used to mark and identify data of a specific type that's found within your data estate during scanning.

Microsoft Purview uses the same sensitive information types as Microsoft 365, allowing you to stretch your existing security policies and protection across your entire data estate.

Note

After you scan your source types, wait a couple of hours for the classic classifications report to reflect the new assets.

## View classification insights

1. Open the Microsoft Purview portal.
2. If you're using the [classic Microsoft Purview portal](use-microsoft-purview-governance-portal), select **Data estate insights**. If you're using the [new Microsoft Purview portal](purview-portal) open **Unified Catalog**, select **Health management**, then select **Reports**.
3. Select the **Classic classifications** report. The **Classification insights** page displays the following areas:

    | Area | Description |
    | --- | --- |
    | **Overview of sources with classifications** | Displays tiles that provide: - The number of subscriptions found in your data - The number of unique classifications found in your data - The number of classified sources found - The number of classified files found - The number of classified tables found |
    | **Top sources with classified data (last 30 days)** | Shows the trend, over the past 30 days, of the number of sources found with classified data. |
    | **Top classification categories by sources** | Shows the number of sources found by classification category, such as **Financial** or **Government**. |
    | **Top classifications for files** | Shows the top classifications applied to files in your data, such as credit card numbers or national/regional identification numbers. |
    | **Top classifications for tables** | Shows the top classifications applied to tables in your data, such as personal identifying information. |
    | **Classification activity**(files and tables) | Displays separate graphs for files and tables, each showing the number of files or tables classified over the selected timeframe. **Default**: 30 daysSelect the **Time** filter above the graphs to select a different time frame to display. |
    |  |  |

## Classification insights drilldown

In any of the following **Classification insights** graphs, select the **View details** link to drill down for more details:

- **Top classification categories by sources**
- **Top classifications for files**
- **Top classifications for tables**
- **Classification activity &gt; Classification data**

To learn more, use the following options:

| Option | Description |
| --- | --- |
| **Filter your data** | Use the filters above the grid to filter the data shown, including the classification name, subscription name, or source type. If you're not sure of the exact classification name, enter part or all of the name in the **Filter by keyword** box. |
| **Sort the grid** | Select a column header to sort the grid by that column. |
| **Edit columns** | To display more or fewer columns in your grid, select **Edit Columns**, then select the columns you want to view or change the order. |
| **Drill down further** | To drill down to a specific classification, select a name in the **Classification** column to view the **Classification by source** report. This report displays data for the selected classification, including the source name, source type, subscription ID, and the numbers of classified files and tables. |
| **Browse assets** | To browse through the assets found with a specific classification or source, select a classification or source, depending on the report you're viewing, then select **Browse assets** above the filters. The search results display all of the classified assets found for the selected filter. For more information, see [Search the Microsoft Purview Unified Catalog](unified-catalog-data-assets-search). |
|  |  |