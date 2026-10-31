---
layout: Conceptual
title: Classic Sensitivity Labels Report in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-reports-classic-sensitivity-labels
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2024-04-29T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to view and use sensitivity label reporting on your data.
locale: en-us
document_id: bd5cbff2-f950-32e7-5b36-5536ebdefc1b
document_version_independent_id: bd5cbff2-f950-32e7-5b36-5536ebdefc1b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-reports-classic-sensitivity-labels.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-reports-classic-sensitivity-labels
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-reports-classic-sensitivity-labels.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/5c1f3bfc-fced-4ad1-b4e6-b7200832734d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/5017978e-5a12-4c31-bdfd-1880eb1a780b
platformId: ec438a4a-f1d8-495c-2a92-0970404b7232
---

# Classic Sensitivity Labels Report in Unified Catalog | Microsoft Learn

This article describes how to access, view, and filter security insights provided by sensitivity labels applied to your data.

Supported data sources include: Azure Blob Storage, Azure Data Lake Storage (ADLS) GEN 1, Azure Data Lake Storage (ADLS) GEN 2, SQL Server, Azure SQL Database, Azure SQL Managed Instance, Amazon S3 buckets, Amazon RDS databases (public preview), Power BI.

In this article, you learn how to:

- Launch your Microsoft Purview account from Microsoft Azure.
- View sensitivity labeling insights on your data.
- Drill down for more sensitivity labeling details on your data.

## Prerequisites

Before getting started with Data Estate Insights, make sure that you complete the following steps:

- Set up your Azure resources and populate the relevant accounts with test data.
- [Extended sensitivity labels to assets in Microsoft Purview Data Map](data-map-sensitivity-labels-apply), and create or select the labels you want to apply to your data.
- Set up and complete a scan on the test data in each data source. For more information, see [Manage data sources in Microsoft Purview](data-map-data-sources-register-manage) and [Create a scan rule set](data-map-scan-rule-set).
- Permissions depending on your current experience:
    - [If using the classic Microsoft Purview Catalog](use-microsoft-purview-governance-portal), you need the [data curator role or insight reader role](data-gov-classic-permissions#roles).
    - [If using the new Microsoft Purview Unified Catalog](unified-catalog), you need [data health reader](data-governance-roles-permissions#unified-catalog-permissions) permissions.

For more information, see [Manage data sources in Microsoft Purview](data-map-data-sources-register-manage) and [Automatically label your data in Microsoft Purview](data-map-sensitivity-labels).

## Use Data Estate Insights for sensitivity labels

Classifications are similar to subject tags. Use them to mark and identify data of a specific type that you find within your data estate during scanning.

Sensitivity labels enable you to state how sensitive certain data is in your organization. For example, a specific project name might be highly confidential within your organization, while that same term isn't confidential to other organizations.

Classifications match directly, such as a social security number, which has a classification of **Social Security Number**.

In contrast, sensitivity labels are applied when one or more classifications and conditions are found together. In this context, [conditions](apply-sensitivity-label-automatically) refer to all the parameters that you can define for unstructured data, such as **proximity to another classification**, and **% confidence**.

Data Estate Insights uses the same classifications, also known as [sensitive information types](sit-sensitive-information-type-entity-definitions), as those used with Microsoft 365 apps and services. This enables you to extend your existing sensitivity labels to assets in Data Map.

Note

After you scan your source types, wait a couple of hours for the **Classic sensitivity labels** report to reflect the new assets.

## View sensitivity labeling insights

1. Open the Microsoft Purview portal.
2. If you're using the [classic Microsoft Purview portal](use-microsoft-purview-governance-portal), select **Data estate insights**. If you're using the [new Microsoft Purview portal](purview-portal) open **Unified Catalog**, select **Health Management**, then select **Reports**.
3. Select the **Classic sensitivity labels** report.

    Note

    If this report is empty, you might not have extended your sensitivity labels to Data Map. For more information, see [Learn about sensitivity labels in Data Map](data-map-sensitivity-labels).

    ![Sensitivity labeling insights](media/insights/sensitivity-labeling-insights-small.png)

    The main **Sensitivity labeling insights** page displays the following areas:

    | Area | Description |
    | --- | --- |
    | **Overview of sources with sensitivity labels** | Displays tiles that provide: - The number of subscriptions found in your data. - The number of unique sensitivity labels applied on your data - The number of sources with sensitivity labels applied - The number of files and tables found with sensitivity labels applied |
    | **Top sources with labeled data (last 30 days)** | Shows the trend, over the past 30 days, of the number of sources with sensitivity labels applied. |
    | **Top labels applied across sources** | Shows the top labels applied across all of your Microsoft Purview data resources. |
    | **Top labels applied on files** | Shows the top sensitivity labels applied to files in your data. |
    | **Top labels applied on tables** | Shows the top sensitivity labels applied to database tables in your data. |
    | **Labeling activity** | Displays separate graphs for files and tables, each showing the number of files or tables labeled over the selected time frame. **Default**: 30 daysSelect the **Time** filter above the graphs to select a different time frame to display. |
    |  |  |

## Sensitivity labeling insights drilldown

In any of the following **Sensitivity labeling insights** graphs, select the **View more** link to drill down for more details:

- **Top labels applied across sources**
- **Top labels applied on files**
- **Top labels applied on tables**
- **Labeling activity &gt; Labeled data**

For example:

![Sensitivity label drilldown](media/insights/sensitivity-label-drilldown-small.png)

To learn more, use the following options:

| Option | Description |
| --- | --- |
| **Filter your data** | Use the filters above the grid to filter the data shown, including the label name, subscription name, or source type. If you're not sure of the exact label name, enter part or all of the name in the **Filter by keyword** box. |
| **Sort the grid** | Select a column header to sort the grid by that column. |
| **Edit columns** | To display more or fewer columns in your grid, select **Edit Columns**, then select the columns you want to view or change the order. Select a column header to sort the grid by that column. |
| **Drill down further** | To drill down to a specific label, select a name in the **Sensitivity label** column to view the **Label by source** report. This report displays data for the selected label, including the source name, source type, subscription ID, and the numbers of classified files and tables. |
| **Browse assets** | To browse through the assets found with a specific label or source, select one or more labels or sources, depending on the report you're viewing, then select **Browse assets** above the filters. The search results display all of the labeled assets found for the selected filter. For more information, see [Search the Microsoft Purview Unified Catalog](unified-catalog-data-assets-search). |
|  |  |

## Sensitivity label integration with Microsoft Purview Information Protection

Close integration with [Microsoft Purview Information Protection](information-protection) means that you have direct ways to extend visibility into your data estate, and classify and label your data. For more information about sensitivity labels, see: [Learn about sensitivity labels](sensitivity-labels).

To extend sensitivity labels to your assets in Data Map, you must turn on this capability in the Microsoft Purview portal.

For more information, see [Apply sensitivity labels to your data in Data Map](data-map-sensitivity-labels-apply).