---
layout: Conceptual
title: Data Quality Scan for a Data Asset in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-scan-asset
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
description: Learn how to run data quality scans on data assets not associated to a data product in Microsoft Purview Unified Catalog.
locale: en-us
document_id: b9fb1444-8cee-5fd0-68fe-465d58783d24
document_version_independent_id: b9fb1444-8cee-5fd0-68fe-465d58783d24
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-scan-asset.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-scan-asset
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-scan-asset.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/20ed8455-bc18-4537-87a4-83784e7b2a39
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/9a7f703b-30bb-4d62-9eb4-97213f571849
platformId: 7cc81270-97bc-eeff-3555-5b988811475b
---

# Data Quality Scan for a Data Asset in Unified Catalog | Microsoft Learn

A standalone data asset is a data asset that isn't associated with a data product in Microsoft Purview Unified Catalog. When you manage data quality for standalone data assets, you can measure, monitor, and improve the quality of these assets independently, without requiring a data product association.

## Benefits of running data quality on a data asset

- **Helps you assess and improve the quality of your data before linking it to a data product**. Microsoft Purview Data Quality users can profile and evaluate the quality of their data before associating it with a data product. Users can standardize, clean, and resolve issues upfront.
- **Helps you decide which assets should be part of a data product**. By understanding the quality of standalone assets, organizations can make informed decisions about which assets are suitable for curation and governance within a data product.
- **Supports broader use cases beyond analytics.** Many organizations associate data products only with analytics use cases. Standalone data assets might serve other purposes such as:

    - Data monetization
    - AI grounding data
    - Operational workloads
- **Provides unified data quality tooling across all data**. Organizations can use a single Microsoft Purview Data Quality solution to assess both standalone data assets and data product–associated assets, including issue remediation.
- **Helps optimize data storage and reduce costs**. If standalone assets are low quality, incomplete, or unusable, organizations can archive them to lower-cost storage or apply data minimalism principles, which reduces unnecessary data retention and improving return on investment.
- **Accelerates data governance maturity**. Organizations can begin measuring and improving data quality immediately, without waiting for data product definitions or use cases. This significantly speeds up governance adoption.

Data quality scans review your data assets based on their applied [data quality rules](unified-catalog-data-quality-rules) and produce a score. Your data stewards can use that score to assess the data health and address any issues that might be lowering the quality of your data. Here's an example of how data asset scores appear in a governance domain:

[![stamdalon data asset quality scan.](media/concept-data-quality-rules/data-asset-quality.png)](media/concept-data-quality-rules/data-asset-quality.png#lightbox)

## Prerequisites

- To run and schedule data quality assessment scans, you need the [data quality steward role](data-governance-roles-permissions#how-to-assign-governance-domain-roles).
- Currently, you can set the Microsoft Purview account to allow public access or managed virtual network access so that data quality scans can run.
- Configure the data source connection if it isn't created yet for the data asset’s source system.
- Configure the data quality error records storage if you want to store data quality failed records for review and correction.

## Data quality life cycle for data assets

Data quality scanning is the **seventh** step in the [data quality life cycle for a data asset](unified-catalog-data-quality#data-quality-life-cycle). The previous steps are:

1. [Register](data-map-data-sources-register-manage#register-a-new-source) and [scan](data-map-scan-data-sources) a data source in Microsoft Purview Data Map.
2. [Assign users data quality steward permissions in Unified Catalog](data-governance-roles-permissions#how-to-assign-catalog-level-roles) so they can use all data quality features.
3. [Set up a data source connection to prepare your source for data quality assessment](unified-catalog-data-quality-supported-sources-connection).
4. Add your data asset from Data Map to a governance domain.
5. [Configure a storage to store data quality error records](unified-catalog-data-quality-error-records) if you want to store data quality error record for review and remediation.
6. [Configure and run data profiling for an asset in your data source.](unified-catalog-data-quality-profiling). When profiling is complete, browse the results for each column in the data asset to understand your data's current structure and state to identify what rules need to be created to measure and monitor data quality of your data continuously.
7. [Set up data quality rules](unified-catalog-data-quality-rules) based on the profiling results, and apply them to your data asset.
8. Review data quality error records and correct those failed records to improve data quality of your data.

## Supported multicloud data sources

To see the list of supported data sources, including file formats for data profiling and data quality scanning with and without virtual network support, see the [supported data sources](unified-catalog-data-quality-supported-sources-file-formats).

Important

Data quality for Parquet file supports:

1. A directory with Parquet Part File. For example: **./Sales/{Parquet Part Files}**. The fully qualified name (FQN) must follow `https://(storage account).dfs.core.windows.net/(container)/path/path2/{SparkPartitions}`. Make sure there are no {n} patterns in directory or subdirectory structure. It must be a direct FQN leading to {SparkPartitions}.
2. A directory with Partitioned Parquet Files, partitioned by columns within the dataset like sales data partitioned by year and month. For example: **./Sales/{Year=2018}/{Month=Dec}/{Parquet Part Files}.**

Both of these essential scenarios, which present a consistent parquet dataset schema, are supported. **Limitation:** The feature doesn't support N arbitrary hierarchies of directories with Parquet files. **Present data in (1) or (2) constructed structure.**

## Supported authentication methods

Currently, Microsoft Purview can only run data quality scans by using [Managed Identity](data-map-data-scan-credentials#use-microsoft-purview-system-assigned-managed-identity-to-set-up-scans) as authentication option. Data quality services run on **Apache Spark 3.5** and **Delta Lake 3.2.1**. For more information about supported regions, see [data quality overview](unified-catalog-data-quality).

Important

- If you update the schema on the data source, import the schema from the Data Quality overview page by using **schema import feature** before running a data quality scan.
- Virtual network isn't supported for Google BigQuery.

## Run a data quality scan for standalone data asset

1. In Unified Catalog, select **Health Management**, and then select **Data quality**.
2. Select a governance domain from the list.
3. Configure a [data source connection to the assets you're scanning for data quality](unified-catalog-data-quality-supported-sources-connection) if you haven't already done so.
4. Select a **Data asset** and select **Add data assets** to add data assets from Data Map for a data quality assessment. Select the data assets you want from the Data Map assets list to add them to the governance domain to begin measuring their data quality.
5. Select the name of a data asset, which takes you to the data quality **Overview** page.
6. Profile the selected data asset if you want to know the distribution, min, max, uniqueness, completeness, standard deviation, and other statistical measures of your data assets.
7. To set up the scan, browse the existing [data quality rules](unified-catalog-data-quality-rules) and add new rules by selecting **Rules**. Browse the schema of the data asset by selecting **Schema**. Toggle on or off the rules you added. If you toggle off a rule, that rule isn't included in the data quality scan.
8. Run the quality scan by selecting **Run quality scan** on the overview page.
9. While the scan is running, [you can track its progress from the data quality monitoring page in the governance domain](unified-catalog-data-quality-job-monitor).
10. If you configured [data quality error records](unified-catalog-data-quality-error-records) in the governance domain level or data asset level, check the error records in the configured storage.

### Add a data asset with a quality score to another governance domain

After a data asset has a data quality score, you can add it to another governance domain by cloning it. You can clone and associate the same data asset with any governance domain as needed.

- Select a data asset with data quality score.
- Select **Add to another domain**, and then select the domain from the drop-down list.
- Select the domain to add the selected data asset.

### Associate asset with a quality score to a data product

You can associate a data asset with its latest data quality score to a data product in a different governance domain.

- Select a data asset with data quality score.
- Select **Add to data product**, and then select the **Governance domain** and **Data product** from the drop-down list.
- Select the domain and data product to add the selected data asset.

When the same data asset is associated with multiple data products, the meaning and expectations of data quality for that asset can differ depending on the business context.

For example, a customer profile data asset might be associated with a Marketing data product for campaign use cases and a Finance data product for billing scenarios. In this case, billing address quality is critical for Finance but less important for Marketing, while customer contact email quality is critical for Marketing but less relevant for Finance.

Because data quality expectations vary by data product, you need to run data quality scans locally on the cloned or associated asset within each target data product to ensure that data quality is evaluated based on the specific use case.

Note

- When you clone or associate a data asset with an existing data quality score from the Data Quality &gt; Data Asset page to another domain or data product, you must run the data quality scan locally in the target domain or data product where the asset is cloned or associated.
- For example, if you clone a data asset named Budget with an existing data quality score from the Marketing domain to the Sales domain, you will need to run a data quality scan for the Budget asset within the Sales domain to view the updated data quality score in that domain.
- A similar process must be followed for any asset cloned or associated with a data product.

Important

- Threshold and alert metadata don't publish to Azure Data Lake Storage Gen2 or Fabric Lakehouse for self-serve analytics.
- Standalone data assets and associated metadata, for example data quality score and data quality rules, don't publish to Azure Data Lake Storage Gen2 or Fabric Lakehouse for self-serve analytics. If a standalone data asset is associated with a data product, then the associated metadata is available for self-serve analytics with the data product association.

## Roles and permissions

- You can't associate a standalone data asset with a data quality score to a data product that is in a published state. The data product must be in draft state.
- If you're not the data product owner, you can't add a standalone data asset to a data product.
- If you don't have permissions for a business domain, you can't clone a standalone data asset into that domain.
- A data product owner must have a local or global Domain Reader role or a Data Quality Reader role to browse the standalone data asset data quality page and to associate a data asset (with data quality scores and rules) to a data product.
- A data steward must have a local or global Domain Owner role to browse the standalone data asset data quality page.

Note

If you delete a data asset from the Data Map, it appears in read-only mode and you identify it by its GUID instead of the asset name. When you hover over the asset GUID, a tooltip message is displayed. You can't run data quality scans on deleted assets, so you can remove the asset from the list.

## Schedule data quality scans

Although you can run data quality scans on an ad-hoc basis by selecting **Run quality scan**, in production scenarios, the source data is likely to be constantly updated. You should regularly monitor data quality to detect any issues. Automating the scanning process helps you manage regular updates of quality scans.

1. In Unified Catalog, select **Health Management**, and then select **Data quality**.
2. Select a **governance domain** from the list.
3. Select **Manage**, then select **Scheduled scans**.
4. Fill out the form on the **Create scheduled scan** page. Add a **name** and **description** for the source you're setting up the schedule.
5. Select **Continue**.
6. On the **Scope** tab, select data assets you want to set up schedule to run data quality as per configured schedule.
7. Select **Continue**.
8. Set a schedule based on your preferences and select **Continue**.
9. On the **Review** tab, select **Save** (or **Save and run** to test immediately) to complete scheduling the data quality assessment scan.

You can monitor scheduled scans on the [data quality job monitoring page](unified-catalog-data-quality-job-monitor) under the **Scans** tab.

Note

- You can't add more than 30 assets across all data products in a single schedule. Create multiple schedules for 30 assets per batch. You can configure to run multiple schedules in the same time window.
- Auto‑scheduling to run a weekly scan is enabled at the asset level by default. If you want to disable auto‑scheduling for a data asset, go to **Health management** &gt; **Data quality** &gt; **Run quality scan**, and then select the option to disable the scheduled scan.
- When you manually run a data quality scan, a notification appears on the Data Quality page prompting you to configure alerts. Ignore this notification if you don't want to configure alerts.

## Delete previous data quality scans and history

To remove a data asset from the data asset list on the data quality page, first delete the data quality score if the data asset has one. Then, remove the data asset from the data quality data asset list.

When you delete data quality history data, you remove the profile history, the data quality scan history, and data quality rules. Data quality actions aren't deleted.

To delete previous data quality scans for a data asset, follow these steps:

1. In Unified Catalog, select **Health Management**, and then select **Data quality**.
2. Select a **governance domain** from the list.
3. Select the **data asset** from the list to go to the Data quality overview page.
4. Select the ellipsis (...) at the upper right of the Data quality overview page.
5. Select **Delete data quality data** to delete the history of data quality runs.

Note

- Use **Delete data quality data** for test runs, errored data quality runs, or if you're removing a data asset from the data quality data asset list.
- The system stores up to 50 snapshots of data quality profiling and data quality assessment history. To delete a specific snapshot, select the desired history run and select the delete icon.

## Import schema

If the data type in a schema is undefined, incorrectly defined, or changed in the source, your data quality job might fail. If it fails, reimport the schema by using the schema import capability. You can import schemas for data sources on both public networks and behind private endpoints. For a list of supported data sources, see [Data sources and file formats supported for data quality](unified-catalog-data-quality-supported-sources-file-formats). To import a schema from your data sources, follow these steps:

- Select **Data quality** from **Health Management**.
- Select a governance domain, and then select a data asset from the list to go to the Data Quality overview page.
- Select **Schema**, and then select the **Schema management** toggle.
- Select **Import schema** to import the schema.