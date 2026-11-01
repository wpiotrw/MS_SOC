---
layout: Conceptual
title: Data quality for on-premises data sources in Unified Catalog (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-on-premises-data-sources
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-04-26T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Measure and monitor data quality for on-premises data sources in Microsoft Purview Unified Catalog (preview).
locale: en-us
document_id: 1010cc19-a0aa-0523-1fb7-b84b94cccc57
document_version_independent_id: 1010cc19-a0aa-0523-1fb7-b84b94cccc57
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-on-premises-data-sources.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-on-premises-data-sources
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-on-premises-data-sources.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/cbe4ca68-43ac-4375-aba5-5945a6394c20
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/ced846cc-6a3c-4c8f-9dfb-3de0e90e2742
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: 371f0019-6ff1-75b2-5d0a-540670cc5f0e
---

# Data quality for on-premises data sources in Unified Catalog (preview) | Microsoft Learn

On-premises data source data quality refers to the ability to assess, monitor, score, and improve the quality of data that resides inside enterprise-owned infrastructure such as on-premises SQL Server and on-premises Oracle. These datasets are stored within a customer’s private network environment rather than in cloud platforms.

## Prerequisites

On-premises databases are scanned in on-premises infrastructure to ensure that data doesn't move beyond the customer premises. You need to set up a Kubernetes cluster to host the runtime that scans these databases. Before you use Microsoft Purview Data Quality for on-premises data sources:

1. Create a Kubernetes cluster.
2. Download the data integration runtime.
3. Register it with Microsoft Purview.

For prerequisites, installation, and set up, see:

- [Set up DIRCTL tool for self-hosted integration runtime (preview)](unified-catalog-data-integration-runtime-command-line-tool)
- [Kubernetes supported self-hosted data integration runtime for on-premises data sources (preview)](unified-catalog-data-integration-runtime-kubernetes)

Before you run a data quality scan, you must scan the assets through a Data Map scan. The Data Map scan requires you to install and configure a self-hosted integration runtime.

## Set up a connection to your on-premises databases

Create connections for on-premises data sources the same way you create connections for other data source types. In Unified Catalog, select **Health management**, then select **Data quality**. Select the governance domain where you created your data product with the on-premises data asset. Select **Manage** and select **Connection** to set up a connection for your on-premises databases. Supported on-premises data sources are:

- Oracle
- SQL Server

Create connections by associating them with a data integration runtime instance. In SQL Server, a single database can contain tables belonging to multiple schemas. So, you can use a single connection to scan all schemas in a single database. Therefore, a connection accepts only database information but not schema. For an Oracle database, you can create the connection at the schema level or the database level. If you want to restrict the connection to the schema level, add the schema name in the connection configuration page.

Note

- One Oracle database should have only one database level connection, but it can have many schema level connections for schema 1, schema 2, and schema 3.
- Each schema level connection is used as a separate connection because they're separate schemas.
- If an Oracle database has both schema level and database level connections, the system uses only the schema level connection.
- If an Oracle database has two database level connections, the system uses only the first connection.

## Data quality scan

After you complete the connection setup, follow the data quality scanning documentation to measure and monitor data quality of Oracle and SQL Server on-premises data sources.

- [Data quality overview](unified-catalog-data-quality)
- [Supported data sources](unified-catalog-data-quality-supported-sources-file-formats)
- [Set up data source connection](unified-catalog-data-quality-supported-sources-connection)
- [Data product quality scan](unified-catalog-data-quality-scan)
- [Data asset quality scan](unified-catalog-data-quality-scan-asset)
- [Incremental data quality scan](unified-catalog-data-quality-scan-incremental)

## Limitations

- Profiling on-premises data sources isn't supported.
- Table lookup rules aren't supported if you don't publish the tables as data assets, or if the databases of the reference tables aren't running or hosting on the same server.
- Freshness rule isn't supported for SQL Server database.
- Custom expressions that are supported for cloud sources aren't supported for SQL Server database, but Custom SQL is supported.
- Regex rules aren't supported, but LIKE is supported.

## Resolve common errors

- **Error**: *Value cannot be null. (Parameter 'Password property is missing')*. This error occurs when the key vault secret isn't found. The actual error message in the Kubernetes log is: "A secret with `(name/id)` KVSecretsOfficers-purview was not found in this key vault."