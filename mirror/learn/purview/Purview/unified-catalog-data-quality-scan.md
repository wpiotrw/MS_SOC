---
layout: Conceptual
title: Configure and Run a Data Quality Scan in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-scan
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-05-15T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to apply data quality scans on assets associated with a data product in Microsoft Purview Unified Catalog.
locale: en-us
document_id: d4906b3f-9ead-80f3-1245-1d843e98ada4
document_version_independent_id: d4906b3f-9ead-80f3-1245-1d843e98ada4
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-scan.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-scan
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-scan.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/20ed8455-bc18-4537-87a4-83784e7b2a39
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/9a7f703b-30bb-4d62-9eb4-97213f571849
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: dbb3f84d-f6ff-d541-da13-3d510c5347f2
---

# Configure and Run a Data Quality Scan in Unified Catalog | Microsoft Learn

Data quality scans review your data assets based on their applied [data quality rules](unified-catalog-data-quality-rules) and produce a score. Your data stewards can use that score to assess the data health and address any issues that might be lowering the quality of your data.

Note

There are two other types of data quality scans you can run:

- Data quality scan for a [standalone data asset (preview)](unified-catalog-data-quality-scan-asset).
- [Incremental data quality scan (preview)](unified-catalog-data-quality-scan-incremental) using a time-based filter.

## Prerequisites

- To run and schedule data quality assessment scans, users need the [data quality steward role](data-governance-roles-permissions#how-to-assign-governance-domain-roles).
- Currently, you can set the Microsoft Purview account to allow public access or managed virtual network access so that data quality scans can run.

## Data quality life cycle

Data quality scanning is the **seventh** step in the [data quality life cycle for a data asset](unified-catalog-data-quality#data-quality-life-cycle). The previous steps are:

1. [Assign users data quality steward permissions in Microsoft Purview Unified Catalog](data-governance-roles-permissions#how-to-assign-catalog-level-roles) so they can use all data quality features.
2. [Register](data-map-data-sources-register-manage#register-a-new-source) and [scan](data-map-scan-data-sources) a data source in Microsoft Purview Data Map.
3. [Add your data asset to a data product](unified-catalog-data-products-create-manage#add-and-remove-data-assets).
4. [Set up a data source connection to prepare your source for data quality assessment](unified-catalog-data-quality-supported-sources-connection).
5. [Configure and run data profiling for an asset in your data source](unified-catalog-data-quality-profiling). When profiling is complete, browse the results for each column in the data asset to understand your data's current structure and state.
6. [Set up data quality rules](unified-catalog-data-quality-rules) based on the profiling results, and apply them to your data asset.

## Supported multicloud data sources

Browse the [supported data source document](unified-catalog-data-quality-supported-sources-file-formats) to view the list of supported data sources, including file formats for data profiling and data quality scanning, with and without virtual network support.

Important

Data quality for Parquet file is designed to support:

1. A directory with Parquet Part File. For example: **./Sales/{Parquet Part Files}**. The Fully Qualified Name must follow `https://(storage account).dfs.core.windows.net/(container)/path/path2/{SparkPartitions}`. Make sure there are no {n} patterns in directory/sub-directory structure. It must be a direct FQN leading to {SparkPartitions}.
2. A directory with Partitioned Parquet Files, partitioned by Columns within the dataset like sales data partitioned by year and month. For example: **./Sales/{Year=2018}/{Month=Dec}/{Parquet Part Files}.**

Both of these essential scenarios, which present a consistent parquet dataset schema, are supported. **Limitation:** It isn't designed to or won't support N arbitrary Hierarchies of Directories with Parquet Files. **We recommend presenting data in (1) or (2) constructed structure.**

## Supported authentication methods

Currently, Microsoft Purview can only run data quality scans by using [Managed Identity](data-map-data-scan-credentials#use-microsoft-purview-system-assigned-managed-identity-to-set-up-scans) as authentication option. Data quality services run on **Apache Spark 3.5** and **Delta Lake 3.2.1**. For more information about supported regions, see [data quality overview](unified-catalog-data-quality).

Important

- If you update the schema on the data source, you need to import schema from data quality overview page by using **schema import feature** before running a data quality scan.
- Virtual network isn't supported for Google BigQuery.

## Run a data quality scan

1. Configure a [data source connection to the assets you're scanning for data quality](unified-catalog-data-quality-supported-sources-connection) if you haven't already done so.
2. In Unified Catalog, select **Health Management**, then select **Data quality**.
3. Select a **governance domain** from the list.
4. Select a **data product** to assess the data quality of the **data assets** linked to that product.
5. Select the name of a data asset, which takes you to the data quality **Overview** page.
6. Browse the existing data quality rules and add new rules by selecting **Rules**. Browse the schema of the data asset by selecting **Schema**. Toggle on or off the rules you added.
7. Run the quality scan by selecting **Run quality scan** on the overview page.
8. While the scan is running, [you can track its progress from the data quality monitoring page in the governance domain](unified-catalog-data-quality-job-monitor).

## Schedule data quality scans

Although you can run data quality scans on an ad-hoc basis by selecting **Run quality scan**, in production scenarios the source data is likely to be constantly updated. You should regularly monitor data quality to detect any issues. Automating the scanning process helps you manage regular updates of quality scans.

1. In Unified Catalog, select **Health Management**, then select **Data quality**.
2. Select a **governance domain** from the list.
3. Select **Manage**, then select **Scheduled scans**.
4. Fill out the form on the **Create scheduled scan** page. Add a **name** and **description** for the source you're setting up the schedule.
5. Select **Continue**.
6. On the **Scope** tab, select individual data product and assets or all data products and data assets of the entire governance domain.
7. Select **Continue**.
8. Set a schedule based on your preferences and select **Continue**.
9. On the **Review** tab, select **Save** (or **Save and run** to test immediately) to complete scheduling the data quality assessment scan.

You can monitor scheduled scans on the [data quality job monitoring page](unified-catalog-data-quality-job-monitor) under the **Scans** tab.

Note

- You can't add more than 30 assets across all data products in a single schedule. Create multiple schedules for 30 assets per batch. You can configure to run multiple schedules in the same time window.
- Auto‑scheduling to run a weekly scan is enabled at the asset level by default. If you want to disable auto‑scheduling for a data asset, go to **Health management** &gt; **Data quality** &gt; **Run quality scan**, and then select the option to disable the scheduled scan.
- When you manually run a data quality scan, a notification appears on the Data Quality page prompting you to configure alerts. Ignore this notification if you don't want to configure alerts.

## Delete previous data quality scans and history

When you remove a data asset from a data product, if that data asset has a data quality score, you need to delete the data quality score first, then remove the data asset from the data product.

When you delete data quality history data, it removes the profile history, the data quality scan history, and data quality rules, but data quality actions aren't deleted.

Follow the steps below to delete previous data quality scans of a data asset:

1. In Unified Catalog, select **Health Management**, then select **Data quality**.
2. Select a **governance domain** from the list.
3. Select the **data product** from the list.
4. Select the **data asset** from the list to navigate the Data quality overview page.
5. Select the ellipsis (...) at the top right of the Data quality overview page.
6. Select **Delete data quality data** to delete the history of data quality runs.

Note

- Use **Delete data quality data** for test runs, errored data quality runs, or if you're removing a data asset from a data product.
- The system stores up to 50 snapshots of data quality profiling and data quality assessment history. If you want to delete a specific snapshot, select the desired history run and select the delete icon.

## Import schema

If the data type in a schema is undefined, incorrectly defined, or changed in the source, your data quality job might fail. If it fails, reimport the schema by using the schema import capability. Schema import is supported for data sources on both public networks and behind private endpoints. The supported data sources are listed at [Data sources and file formats supported for data quality](unified-catalog-data-quality-supported-sources-file-formats). To import a schema from your data sources, follow these steps:

- Select **Data quality** from **Health Management**.
- Select a business domain, then select a data product, then select a data asset from that data product. You arrive at the data quality overview page.
- Select **Schema**, then select the **Schema management** toggle.
- Select **Import schema** to import the schema.