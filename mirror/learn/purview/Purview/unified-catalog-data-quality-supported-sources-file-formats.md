---
layout: Conceptual
title: Data Quality Supported Sources and File Types in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-supported-sources-file-formats
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-04-09T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Get a list of supported data sources and file formats for data quality in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 3105c065-252a-0081-a781-4cf22db43821
document_version_independent_id: 3105c065-252a-0081-a781-4cf22db43821
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-supported-sources-file-formats.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-supported-sources-file-formats
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-supported-sources-file-formats.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bad69977-db6a-44f3-b752-d2bee7de49ca
- https://authoring-docs-microsoft.poolparty.biz/devrel/cbe4ca68-43ac-4375-aba5-5945a6394c20
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31d7aff-61be-45e2-a324-a578cf0c3360
- https://authoring-docs-microsoft.poolparty.biz/devrel/ced846cc-6a3c-4c8f-9dfb-3de0e90e2742
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: b6ad53ed-b89e-8d49-4d45-ff3d7cba737e
---

# Data Quality Supported Sources and File Types in Unified Catalog | Microsoft Learn

## Supported sources

| **Data source** | **Data profiling** | **Data quality scan** | **Virtual network support** | **Note** |
| --- | --- | --- | --- | --- |
| Azure Data Lake Storage Gen2 | Yes | Yes | Yes |  |
| Azure Databricks Unity Catalog | Yes | Yes | Yes |  |
| Azure Synapse serverless | Yes | Yes | Yes |  |
| Azure Synapse Data Warehouse | Yes | Yes | Yes |  |
| Azure SQL Database | Yes | Yes | Yes |  |
| Azure SQL Managed Instance | Yes | Yes | Yes |  |
| Azure Dedicated SQL Pool (formarly SQL DW) | Yes | Yes | No |  |
| Google BigQuery | Yes | Yes | No |  |
| Snowflake | Yes | Yes | Yes |  |
| Fabric | Yes | Yes | Yes | Lakehouse, Shortcut to other filesystem, and mirroring with other database |
| Amazon S3 | Yes | Yes | No | Supported via Fabric shortcut |
| Dataverse | Yes | Yes | No | Supported via Fabric shortcut |
| Google Cloud Storage | Yes | Yes | No | Supported via Fabric shortcut |
| Oracle | No | Yes | NA | On-premises infrastructure |
| SQL Server | No | Yes | NA | On-premises infrastructure |

## Supported file formats

| **File format** | **Data profiling** | **Data quality scan** | **vNet support** |
| --- | --- | --- | --- |
| Delta | Yes | Yes | NA |
| Parquet | Yes | Yes | NA |
| Iceberg Avro | Yes | Yes | NA |
| Iceberg Orc | Yes | Yes | NA |

## Supported resource set pattern

| **Pattern Name** | **Details** |
| --- | --- |
| SparkPartitions | All patterns ending with {SparkPartitions} are supported provided that they do not contain any other mixed non-column patterns in their folder path. |
| Column partitions | All column partition patterns for parquet, delta and iceberg datasets are supported. |

- **Example 1 (supported)**: Standard resource-set folder path: ` https://myblob.blob.core.windows.net/sample-data/name-of-folder-output/{SparkPartitions}`
- **Example 2 (supported)**: Column partitioned resource-set folder path: `https://myblob.blob.core.windows.net/my-partitioned-data/Year={Year}/Month={Month}/Day={Day}/{SparkPartitions}`
- **Example 3 (not supported)**: Mixed resource-set path: `https://myblob.blob.core.windows.net/sample-data/data{N}.parquet`

For more information on Microsoft Data Map resource sets, see [Understanding resource set](data-map-resource-sets).