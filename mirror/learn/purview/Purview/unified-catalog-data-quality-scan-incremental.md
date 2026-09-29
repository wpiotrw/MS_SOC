---
layout: Conceptual
title: Incremental Data Quality Scan in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-scan-incremental
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
ai-usage: ai-assisted
description: Use time-based filter to scan data quality incrementally in Microsoft Purview Unified Catalog.
locale: en-us
document_id: c7bca066-645a-e079-701b-ef25a7e5d795
document_version_independent_id: c7bca066-645a-e079-701b-ef25a7e5d795
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-scan-incremental.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-scan-incremental
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-scan-incremental.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/20ed8455-bc18-4537-87a4-83784e7b2a39
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/9a7f703b-30bb-4d62-9eb4-97213f571849
platformId: 3591e637-d51c-9322-4c7b-286f1ef65aa3
---

# Incremental Data Quality Scan in Unified Catalog | Microsoft Learn

Microsoft Purview Data Quality supports incremental data quality scans by using time-based filtering. By using incremental scans, you can choose between full scans, incremental scans, or both when you run data quality rules on data assets.

While certain rules, such as duplicate detection, require a full scan of the entire dataset, you can efficiently evaluate many data quality checks on newly created or updated data. By using incremental scans, you can run these rules on a defined schedule, such as daily or weekly, which improves performance and reduces scan costs.

By using incremental data quality scans, you can:

- Create rules that run on full scans, incremental scans, or both.
- Flexibly assign existing rules to incremental or full scan execution.
- Configure schedules for data assets to run incremental scans at defined intervals.

Data quality scores are calculated across all rules and data assets, regardless of whether the scan is incremental or full. Microsoft Purview Data Quality computes a cumulative data quality score to help you understand overall data quality trends over time.

## Benefits of running incremental scans

Data offices and data practitioners don't always need to assess data quality across the entire historical dataset, such as five to 10 years of data, on a frequent basis. You can evaluate historical data periodically, such as monthly or quarterly, while newly created or updated data often requires more frequent monitoring.

By using incremental scans, you can enable continuous data quality monitoring on recent data so that you can identify and address problems quickly, before they affect downstream systems and analytics.

## Configure and run a data quality scan

Data quality scans review your data assets based on their applied [data quality rules](unified-catalog-data-quality-rules) and produce a score. Your data stewards can use that score to assess the data health and address any problems that might lower the quality of your data.

## Prerequisites

- To run and schedule data quality assessment scans, users need the [data quality steward role](data-governance-roles-permissions#how-to-assign-governance-domain-roles).
- Currently, you can set the Microsoft Purview account to allow public access or managed virtual network access so that data quality scans can run.

## Data quality life cycle

Data quality scanning is the **seventh** step in the [data quality life cycle for a data asset](unified-catalog-data-quality#data-quality-life-cycle). The previous steps are:

1. [Register](data-map-data-sources-register-manage#register-a-new-source) and [scan](data-map-scan-data-sources) a data source in Microsoft Purview Data Map.
2. [Assign users data quality steward permissions in Unified Catalog](data-governance-roles-permissions#how-to-assign-catalog-level-roles) so they can use all data quality features.
3. [Add your data asset to a data product](unified-catalog-data-products-create-manage#add-and-remove-data-assets). This step is needed only if you want to run data quality for data assets associated to a data product to calculate data product data quality score.
4. If you want to measure data quality for a standalone data asset, add a data asset from the Data Map to a domain to run data quality scan for the asset without association to a data product.
5. [Set up a data source connection to prepare your source for data quality assessment](unified-catalog-data-quality-supported-sources-connection).
6. Configure a container or storage to store data quality error records for review and correct the failed records.
7. [Configure and run data profiling for an asset in your data source.](unified-catalog-data-quality-profiling). When profiling is complete, browse the results for each column in the data asset to understand your data's current structure and state.
8. [Set up data quality rules](unified-catalog-data-quality-rules) based on the profiling results, and apply them to your data asset.
9. Run data quality scan to understand and improve the quality of your data.

## Supported multicloud data sources

Browse the [supported data source document](unified-catalog-data-quality-supported-sources-file-formats) to view the list of supported data sources, including file formats for data profiling and data quality scanning, with and without virtual network support.

Important

Data quality for Parquet file is designed to support:

1. A directory with Parquet Part File. For example: **./Sales/{Parquet Part Files}**. The Fully Qualified Name must follow `https://(storage account).dfs.core.windows.net/(container)/path/path2/{SparkPartitions}`. Make sure there are no {n} patterns in directory/sub-directory structure. It must be a direct FQN leading to {SparkPartitions}.
2. A directory with Partitioned Parquet Files, partitioned by columns within the dataset like sales data partitioned by year and month. For example: **./Sales/{Year=2018}/{Month=Dec}/{Parquet Part Files}.**

Both of these essential scenarios, which present a consistent parquet dataset schema, are supported. **Limitation:** It isn't designed to or won't support N arbitrary hierarchies of directories with Parquet files. **We recommend presenting data in (1) or (2) constructed structure.**

Microsoft Purview Data Quality doesn't currently support specifying data quality rules on maps, lists, and structs in Parquet data structures.

## Supported authentication methods

Currently, Microsoft Purview can only run data quality scans by using [Managed Identity](data-map-data-scan-credentials#use-microsoft-purview-system-assigned-managed-identity-to-set-up-scans) as authentication option. Data quality services run on **Apache Spark 3.5** and **Delta Lake 3.2.1**. For more information about supported regions, see [data quality overview](unified-catalog-data-quality).

Important

- If you update the schema on the data source, you need to import schema from data quality overview page by using **schema import feature** before running a data quality scan.
- Virtual network isn't supported for Google BigQuery.

## Configure and run incremental data quality scan

1. In Unified Catalog, select **Health Management**, then select **Data quality**.
2. Select a **governance domain** from the list.
3. Configure a [data source connection to the assets you're scanning for data quality](unified-catalog-data-quality-supported-sources-connection) if you haven't already done so.
4. Select a **data product** to assess the data quality of the **data assets** associated with that product. If you want to scan a data asset without data product association, select **Add assets** to add a data asset to the asset list from Data Map.
5. Select the name of a data asset, which takes you to the data quality **Overview** page.
6. Browse the existing data quality rules and add new rules by selecting **Rules**. Create custom rules using SQL expression or ADF expression language if out of the box rules aren't enough for your use case. Toggle on or off the rules you added if you want to turn off or on any rule.
7. Select the scan recurrence option:
    - Incremental
    - Full
    - Both
8. Select **Run quality scan** from the upper-right corner on the overview page.
9. Enable the Run incremental scan toggle and provide the following details:
    - Choose the time window for updated data: last day, last week, last two weeks, or last month
    - Select the datetime column to use for incremental scanning
    - Use the **Add Rule** tab to select rules from the predefined rule list
10. Select **Run Quality Scan** to execute the incremental scan.
11. Schedule incremental scan. To set up a schedule to run data quality scan, enable scheduled execution by selecting **Enable recurring scan** and setting the desired schedule. If you configure a recurring schedule, the **Run Quality Scan** button is read-only on the Scan Run Configuration page.
12. While the scan is running, [you can track its progress](unified-catalog-data-quality-job-monitor) from the data quality monitoring page in the governance domain.

[![Incremental data quality scan with rules.](media/concept-data-quality-rules/incremental-scan.png)](media/concept-data-quality-rules/incremental-scan.png#lightbox)

Note

- Both **datetime** and **date** columns are supported, but we recommend using a **datetime** column. If the data asset doesn't contain a timestamp column, incremental data quality scans can't be configured for daily scans. A date column prevents the system from calculating the last 24 hours accurately, which is required to slice one day's data for data quality scans. The datetime data type is also more commonly used for created, updated, and other timestamp columns.
- Filter days: 90 days for three months, 180 days for six months, and 365 days for one year.
- Auto‑scheduling to run a weekly scan is enabled at the asset level by default. If you want to disable auto‑scheduling for a data asset, go to **Health management** &gt; **Data quality** &gt; **Run quality scan**, and then select the option to disable the scheduled scan.
- When you manually run a data quality scan, a notification appears on the Data Quality page prompting you to configure alerts. Ignore this notification if you don't want to configure alerts.
- Cumulative score is calculated as the average of the incremental scan score and the full (regular) scan score.
- Incremental data quality scan isn't supported for on-premises data sources.

Important

Scan type, incremental data quality score, and cumulative data quality score don't publish to Azure Data Lake Storage Gen2 or Fabric Lakehouse for self-serve analytics.

## Delete previous data quality scans and history

When you remove a data asset from a data product, if that data asset has a data quality score, delete the data quality score first, and then remove the data asset from the data product.

When you delete data quality history data, you remove the profile history, the data quality scan history, and data quality rules. Data quality actions aren't deleted.

To delete previous data quality scans of a data asset, follow these steps:

1. In Unified Catalog, select **Health Management**, then select **Data quality**.
2. Select a **governance domain** from the list.
3. Select the **data product** from the list. Select the **data asset** from the list to go to the Data quality overview page. If you're using the standalone data asset data quality feature, select the data asset from the data asset list.
4. Select the ellipsis (...) at the upper right of the Data quality overview page.
5. Select **Delete data quality data** to delete the history of data quality runs.

Note

- Use **Delete data quality data** for test runs, errored data quality runs, or if you're removing a data asset from a data product.
- The system stores up to 50 snapshots of data quality profiling and data quality assessment history. To delete a specific snapshot, select the desired history run and select the delete icon.

## Import schema

If the data type in a schema is undefined, incorrectly defined, or changed in the source, your data quality job might fail. If it fails, reimport the schema by using the schema import capability. You can import schemas for data sources on both public networks and behind private endpoints. For a list of supported data sources, see [Data sources and file formats supported for data quality](unified-catalog-data-quality-supported-sources-file-formats). To import a schema from your data sources, follow these steps:

- Select **Data quality** from **Health Management**.
- Select a business domain, and then select a data product. Select a data asset from that data product. You arrive at the data quality overview page.
- Select **Schema**, then select the **Schema management** toggle.
- Select **Import schema** to import the schema.