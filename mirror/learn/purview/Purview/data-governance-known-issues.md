---
layout: Conceptual
title: Known Issues in Microsoft Purview Data Governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-known-issues
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: jife
ms.date: 2026-04-15T00:00:00.0000000Z
audience: Admin
ms.topic: error-reference
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: This article covers known issues in Microsoft Purview Data Governance solutions, and their current status and resolution estimates.
locale: en-us
document_id: c8748e75-edc1-98dd-2ae3-0b420bc431a6
document_version_independent_id: c8748e75-edc1-98dd-2ae3-0b420bc431a6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-known-issues.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-known-issues
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-known-issues.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/cbe4ca68-43ac-4375-aba5-5945a6394c20
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/ced846cc-6a3c-4c8f-9dfb-3de0e90e2742
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 871c309e-3d4e-1187-fa68-2903c708019c
---

# Known Issues in Microsoft Purview Data Governance | Microsoft Learn

This article provides information about known issues when using Microsoft Purview data governance solutions.

## Browser issues

To learn about browser issues that might affect use of data governance solutions, see these resources:

- [Microsoft Edge known issues](/en-us/deployedge/microsoft-edge-known-issues)
- [Google Chrome Local Network Access](https://developer.chrome.com/blog/local-network-access)

If you need further assistance, contact Microsoft support.

## Unified Catalog management issues

| Issue ID | Description | Publish Date | Status | Fixed Date |
| --- | --- | --- | --- | --- |
| 1 | Data assets from top-level hierarchies aren’t selectable.While adding data assets to data products, assets that are part of a semantic model, or Power BI dataset, hierarchy are automatically expanded without getting user input on which ones to include. | 9/6/2024 | Active |  |
| 2 | Missing duplication checks.All business concepts except governance domains are missing duplication checks during creation. | 9/6/2024 | Active |  |
| 3 | Incomplete workflow then Privacy reviewer is selected.Privacy reviewer selection skips the last step of showing data assets table for recording asset level access provisioning status and instructions to data consumer. | 9/6/2024 | Active |  |
| 4 | Inconsistent asset details page experience.In the asset discovery experience under **Discovery &gt; Data assets**, the asset details page for assets within the default/merged account render in the new Microsoft Purview portal but assets within accounts that were merged to the default account render in the classic governance portal. | 10/25/2024 | Active |  |
| 5 | Usage monitoring (preview) for governed assets in Unified Catalog settings has a gap for some customers in the East US region. Values for April 12, 13, and 14, 2026, won't contain the number of governed assets on those days and will appear blank. | 4/14/2026 | Active |  |

## Discovery issues

| Issue ID | Title | Publish Date | Status | Fixed Date |
| --- | --- | --- | --- | --- |
| 1 | Data lineage on a data asset in a data product isn't clickable to expand. To view the full lineage of the asset, it must be expanded at the asset in view details first then refreshed and the data product level. | 5/9/2025 | Active |  |
| 2 | Enterprise glossary filters don’t interact.Filters in the enterprise glossary don't automatically update based on other filter selections. | 9/6/2024 | Fixed | 9/26/2024 |
| 3 | Data asset metadata don’t autorefresh.Data assets within data products don’t automatically reflect owner, description, or lineage updates made in the Data Map. They need to be manually refreshed in the **Catalog management &gt; Data products** section by selecting **Refresh** in the asset details page. | 9/6/2024 | Active |  |
| 4 | Linked objectives and key results (OKRs) don't show in data product search.Published OKRs that are linked to data products don't display in the data product details page within the **Discovery &gt; Data products** search experience today. | 9/6/2024 | Active |  |

## Health management issues

| Issue ID | Title | Publish Date | Status | Fixed Date |
| --- | --- | --- | --- | --- |
| 1 | Virtual network isn't supported for Google BigQuery | 9/1/2024 | Active | 7/2/2025: Virtual network is supported for Azure SQL, Synapse, Fabric, Azure Databricks, and Snowflake |
| 2 | No SQL query is generated for custom data quality rules failures. SQL queries are only generated for failures of out-of-the-box rules. | 4/11/2024 | Active |  |
| 3 | Data quality profiling uses a random sample of 1 million records. Users can include a maximum of 50 columns in a single batch, but they can run multiple batches if they need to profile files or tables with more than 50 columns. | 4/11/2024 | Active | There's no limit for rule based data quality scan; customers can run a data quality scan for billions of records and hundreds of columns. |
| 4 | A table lookup rule can be created for the tables within the same governance domain. You need to use four characters when you search for a data asset to reference to look up. | 4/11/2024 | Active |  |
| 5 | The freshness data quality rule isn't supported for Azure SQL, Google BigQuery, Databricks Unity Catalog, Snowflake, and Synapse. | 9/1/2024 | Active |  |
| 6 | Azure SQL doesn't support RLIKE keywords, so any query containing RLIKE keywords won't run in Azure SQL. Custom regex rule won't work for Azure SQL. | 4/11/2024 | Active |  |
| 7 | Fabric OneLake tables and semantic model data quality scanning isn't supported. Only Fabric Lakehouse tables data quality scanning is supported (private preview). | 9/1/2024 | Active |  |
| 8 | Scheduled jobs have a maximum limit of 30 data assets. Customers need to set up multiple schedules if they have more than 30 data assets in a governance domain. | 9/1/2024 | Active |  |
| 9 | Data quality threshold alerts can be set up for a maximum of 30 data assets in one batch. If customers have more than 30 data assets in the same governance domain, they need to create multiple alerts, for example: Alert 1 for first 30 data assets and Alert 2 for next 30 data asset, and so on. | 9/1/2024 | Active |  |
| 10 | Reports show all records (metadata), no filter available for role-based access control (RBAC). This means a data steward from one org (part of collection 1) can view analytics and reports from another org (collection 2). [Recommending to use Purview metadata from OneLake to create own reports and insights.](/en-us/purview/purview-dg-self-service-analytics-and-insight) | 9/1/2024 | Active |  |
| 11 | Not support N arbitrary Hierarchies of Directories with Parquet Files. We advise users to present data in (1) A directory with Parquet Part File. For example: `./Sales/{Parquet Part Files}` or  (2) A directory with Partitioned Parquet Files, partitioned by columns within the dataset like sales data partitioned by year and month. For example: `./Sales/{Year=2018}/{Month=Dec}/{Parquet Part Files}`. | 9/1/2024 | Active |  |