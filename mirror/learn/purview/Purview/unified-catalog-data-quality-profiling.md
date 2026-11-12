---
layout: Conceptual
title: Configure and Run Data Profiling in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-profiling
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to configure and run data profiling in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 724a29d2-7d08-8482-e345-1df838ba5586
document_version_independent_id: 724a29d2-7d08-8482-e345-1df838ba5586
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-profiling.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-profiling
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-profiling.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 7dcf1659-e6ce-07ac-b4f9-07f7e17fb24a
---

# Configure and Run Data Profiling in Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Data profiling is the process of examining the data available in different data sources and collecting statistics and information about this data. Data profiling helps you assess the quality level of the data according to a defined set of goals. If data is of poor quality, or managed in structures that can't be integrated to meet the needs of the organization, business processes and decision making suffer. Data profiling allows you to understand the trustworthiness and quality of your data, which is a prerequisite for making data-driven decisions that boost revenue and foster growth.

## Prerequisites

- To run and schedule data quality assessment scans, your users must be in the [data quality steward role](data-governance-roles-permissions#how-to-assign-governance-domain-roles).
- Currently, you can set the Microsoft Purview account to allow public access or managed virtual network access so data quality scans can run.

## Data quality life cycle

Data profiling is the **fifth** step in the [data quality life cycle for a data asset](unified-catalog-data-quality#data-quality-life-cycle). The previous steps are:

1. [Assign users(s) data quality steward permissions in Unified Catalog](data-governance-roles-permissions#how-to-assign-catalog-level-roles) to use all data quality features.
2. [Register](data-map-data-sources-register-manage#register-a-new-source) and [scan](data-map-scan-data-sources) a data source in your Purview Data Map.
3. [Add your data asset to a data product](unified-catalog-data-products-create-manage#add-and-remove-data-assets).
4. [Set up a data source connection to prepare your source for data quality assessment](unified-catalog-data-quality-supported-sources-connection).

## Supported multicloud data sources

Browse the [supported data source document](unified-catalog-data-quality-supported-sources-file-formats) to view the list of supported data sources, including file formats for data profiling and data quality scanning, with and without virtual network support.

Important

Data quality for Parquet file is designed to support:

1. A directory with Parquet Part File. For example: **./Sales/{Parquet Part Files}**. The Fully Qualified Name must follow `https://(storage account).dfs.core.windows.net/(container)/path/path2/{SparkPartitions}`. Make sure not to have {n} patterns in directory or subdirectory structure; it must be a direct FQN leading to {SparkPartitions}.
2. A directory with Partitioned Parquet Files, partitioned by columns within the dataset like sales data partitioned by year and month. For example: **./Sales/{Year=2018}/{Month=Dec}/{Parquet Part Files}.**

Both of these essential scenarios, which present a consistent Parquet dataset schema, are supported. **Limitation:** It isn't designed to or won't support N arbitrary hierarchies of directories with Parquet files. **We recommend presenting data in (1) or (2) constructed structure.**

## Supported authentication methods

Currently, Microsoft Purview can only run data quality scans by using [Managed Identity](data-map-data-scan-credentials#use-microsoft-purview-system-assigned-managed-identity-to-set-up-scans) as authentication option. Data quality services run on **Apache Spark 3.5** and **Delta Lake 3.2.1**. For more information about supported regions, see the [data quality overview](unified-catalog-data-quality).

Important

- If you update the schema on the data source, you need to import schema from data quality overview page by using **schema import feature** before running data profiling.
- Virtual network isn't supported for Google BigQuery.
- In the current version, you can profile 50 columns per batch. If your data asset has more than 50 columns, you can profile extra columns in more batches.
- Profiling is using random sample from the selected data asset, the sample size is 1 million records.
- If a column contains distinct value, don't profile that column. A column with distinct values can't create a normal distribution.

### Steps to configure data profiling job

1. Configure a [data source connection to the assets you're scanning for data quality](unified-catalog-data-quality-supported-sources-connection) if you haven't already done so.
2. From Microsoft Purview Unified Catalog, select **Health Management**, then select **Data quality**.
3. Select a **governance domain** from the list.
4. Select a **data product** to profile a **data asset** linked to that product.
5. Select a data asset to navigate into data quality **Overview** page for profiling.
6. Select **Profile** button to run profiling job for the selected data asset.
7. The AI recommendation engine suggests potentially important columns to run data profiling against. You can deselect recommended columns and/or select more columns to be profiled.
8. Once you've selected the relevant columns, select **Run Profile**.
9. While the job is running, [you can track its progress from the data quality monitoring page in the governance domain](unified-catalog-data-quality-job-monitor).
10. When the job is complete, select the **Profile** tab from left menu of the asset's data quality page to list browse the profiling result and statistical snapshot. There could be several profile result pages depending on how many columns your data assets have.
11. Browse the profiling results and statistical measures for each column.

## Understanding profiling results

- **Minimum**: Minimum length of the characters in the column.
- **Maximum**: Maximum length of the characters in the column.
- **Distribution**: Normal distribution of your data.
- **Unique values**: Values that don't repeat; they're unique.
- **Duplicate values**: Values that repeat more than once.
- **Empty/blank values**: The column is blank or empty.
- **Null**: Null values in the column.
- **Average**: Mid value or arithmetic average.
- **Standard deviation**: A statistical measure that quantifies the amount of variation or dispersion in a set of values.