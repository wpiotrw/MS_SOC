---
layout: Conceptual
title: Data Quality for Fabric Lakehouse in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-fabric-lakehouse
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
description: Learn how to register Fabric Lakehouse data, configure Data Map scans, and run data quality assessments in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 705983ee-44c0-0dc6-f61d-b771732a823c
document_version_independent_id: 705983ee-44c0-0dc6-f61d-b771732a823c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-fabric-lakehouse.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-fabric-lakehouse
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-fabric-lakehouse.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e7cd09c2-9e9a-4f0d-b160-c15783f45b1f
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1d337399-0ca4-4b4c-acef-8df37820e018
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 821382f2-4a6f-da99-89e1-387be1aa2e1d
---

# Data Quality for Fabric Lakehouse in Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

This article explains how to register, scan, and run data quality assessments on Fabric Lakehouse data using Microsoft Purview. Before you begin, review the prerequisites.

## Overview of Fabric OneLake

Fabric OneLake is a single, unified, logical data lake for your whole organization. A data lake processes large volumes of data from various sources. Like Microsoft OneDrive, OneLake comes automatically with every Microsoft Fabric tenant and is designed to be the single place for all your analytics data. OneLake brings customers:

- One data lake for the entire organization
- One copy of data for use with multiple analytical engines

OneLake aims to give you the most value possible out of a single copy of data without data movement or duplication. You no longer need to copy data just to use it with another engine or to break down silos so you can analyze the data with data from other sources. You can use Microsoft Purview to catalog fabric data estate and measure data quality to govern and drive improvement action.

You can use shortcut for referencing to data that is stored in other file locations. These file locations can be within the same workspace or across different workspaces, within OneLake or external to OneLake in Azure Data Lake Storage (ADLS), Amazon Web Services (AWS) S3, or Dataverse with more target locations coming soon. Data source location doesn't matter that much, OneLake shortcuts make files and folders appear as if they are stored locally. When teams work independently in separate workspaces, shortcuts enable you to combine data across different business groups and domains into a virtual data product to fit a user’s specific needs.

You can use mirroring to bring data from various sources together into Fabric. Mirroring in Fabric is a low-cost and low-latency solution to bring data from various systems together into a single analytics platform. You can continuously replicate your existing data estate directly into Fabric's OneLake, including data from Azure SQL Database, Azure Cosmos DB, and Snowflake. With the most up-to-date data in a queriable format in OneLake, you can now use all the different services in Fabric. For example, running analytics with Spark, executing notebooks, data engineering, visualizing through Power BI Reports, and more. The Delta tables created from mirrored data can then be used throughout Fabric, allowing users to accelerate their journey into Fabric.

## Register Fabric OneLake as a data source

To configure Data Map scan, you need to first register data source that you want to scan. To scan a Fabric workspace, there are no changes to the existing experience to register a Fabric tenant as a data source. To register a new data source, follow these steps:

- In the Microsoft Purview portal, go to **Data Map**.
- Select **Register**.
- On **Register** sources, select **Fabric**.

For setup instructions, see [same-tenant Fabric scan setup](register-scan-fabric-tenant) and [cross-tenant Fabric scan setup](register-scan-fabric-tenant-cross-tenant).

## Set up a Data Map scan for Fabric Lakehouse

To scan Lakehouse subartifacts, you don't need to change your existing experience in Data Map to set up a scan. A viewer role is sufficient to scan metadata and item-level lineage.

**Currently, only service principal is supported as an authentication method**. Managed identity (MSI) support is still in the backlog.

For setup instructions, see [same-tenant Fabric scan setup](register-scan-fabric-tenant) and [cross-tenant Fabric scan setup](register-scan-fabric-tenant-cross-tenant).

### Set up connection for Fabric Lakehouse scan

After you register Fabric Lakehouse as a source, you can select Fabric from the list of your registered data sources in Data Map and select **New scan**. Add a **Data source ID**, then follow these steps:

1. Create a security group and a service principal.
2. Add both this service principal and the Purview Managed Identity to this security group, then specify that security group in the Fabric tenant Admin API settings.
3. Associate the security group with Fabric tenant.

    1. Sign in to the Fabric admin portal.
    2. Select the Tenant settings page. **You need to be a Fabric Admin to see the tenant settings page.**
    3. Select Admin API settings &gt; Allow service principals to use read-only admin APIs.
    4. Select Specific security groups.
    5. Select Admin API settings &gt; Enhance admin APIs responses with detailed metadata and Enhance admin APIs responses with DAX and mashup expressions &gt; Enable the toggle to allow Data Map to automatically discover the detailed metadata of Fabric datasets as part of its scans. **After you update the Admin API settings on your Fabric tenant, wait about 15 minutes before registering a scan and test connection.**
4. Provide Admin API settings read-only API permission to the security group that contains the service principal and Purview Managed Identity.
5. Add **SPN** into **Credential** field.
6. Add Azure resource name.

    [![fabric datamap scan page 1](media/dq-fabric/fabric-datamap-scan-connection-p1.png)](media/dq-fabric/fabric-datamap-scan-connection-p1.png#lightbox)
7. Add **Tenant ID**.
8. Add **Service Principal ID**.
9. Add **Key Vault connection**.
10. Add **Secret name**.

[![fabric datamap scan page 2](media/dq-fabric/fabric-datamap-scan-connection-p2.png)](media/dq-fabric/fabric-datamap-scan-connection-p2.png#lightbox)

After you finish the Data Map scan, locate a Lakehouse instance in Unified Catalog.

1. In the Microsoft Purview portal, open **Unified Catalog**.
2. Select **Discovery**, then **Data assets**.
3. On the **Data assets** page, select **Microsoft Fabric**.
4. Select **Fabric workspaces**, then select a workspace from the list.
5. On the workspace's page, find the Lakehouse instance under **Item name**.

To browse Lakehouse tables:

1. On a workspace page, select the item name **Tables**.
2. Select a Lakehouse table asset listed under **Item name**.
3. View the asset's details page to find metadata such as schema, lineage, and properties.

## Review Fabric Lakehouse data quality scan prerequisites

Before you run a data quality scan on Fabric Lakehouse data, complete the following prerequisites:

1. Shortcut, mirror, or load your data to Fabric Lakehouse in delta format.

[![Screenshot that shows fabric delta table.](media/dq-fabric/fabric-delta-table.png)](media/dq-fabric/fabric-delta-table.png#lightbox)

Important

If you add new tables, files, or new sets of data to Fabric Lakehouse through mirroring or shortcut, run a Data Map scope scan to catalog those new sets of data before adding those data assets to a data product for data quality assessment.

1. Grant Contributor right to your workspace for Purview MSI

[![Screenshot that shows how to grant contributor access.](media/dq-fabric/fabric_contributo_access.png)](media/dq-fabric/fabric_contributo_access.png#lightbox)

1. Add scanned data asset from Lakehouse to the data products of the governance domain. On a data product's page in Unified Catalog, locate the data assets and select **Add data assets**. You can only perform data profiling and data quality scanning for the data assets associated with the data products under the governance domain.

For data profiling and data quality scanning, you need to create a separate data source connection. Data Map uses a service principal scan connection, while Unified Catalog data quality uses a Fabric connection with Microsoft Purview MSI. To set up the data quality connection:

1. In Unified Catalog, select **Health management**, then select **Data quality**.
2. Select a governance domain, and from the **Manage** dropdown list, select **Connections**.
3. Select **New** to open connection configuration page.
4. Add connection display name and a description.
5. Add Source type **Fabric**.
6. Add **Tenant ID**.
7. Add **Workspace ID**.
8. Add **Lakehouse ID**.
9. Add **Credential** - **Microsoft Purview MSI**.

    [![screenshot that shows where to find workspace and lakehouse ID.](media/dq-fabric/fabric-id.png)](media/dq-fabric/fabric-id.png#lightbox)
10. Test connection to make sure that the configured connection is successful.

    [![Screenshot that shows how to set up fabric connection.](media/dq-fabric/dq-fabric-connection.png)](media/dq-fabric/dq-fabric-connection.png#lightbox)

If your Fabric tenant is configured to run on Virtual Network or in Private Link, check the Virtual Network checkbox in the connection screen. Then select the Azure region where your Fabric and Microsoft Purview are running; for example, UAE North, West Europe, or Canada Central.

In addition to Azure region, you need to add the **Private Link Resource ID**. The following example shows the format:

`/subscriptions/07d669d6-83f2-4f15-8b5b-4a4b31a7050e/resourceGroups/pdgbugbashfabricvnet/providers/Microsoft.PowerBI/privateLinkServicesForPowerBI/fabricvnetpl.`

To set up compute for virtual networks, refer to [Set up data quality for managed virtual networks](unified-catalog-data-quality-managed-virtual-networks). And get details on how to [set up and use private link for your Fabric tenant](/en-us/fabric/security/security-private-links-use). You need to set up the private link for the Fabric tenant before configuring data quality virtual network connection and compute allocation.

Important

- For a data quality scan, Microsoft Purview MSI must have contributor access to Fabric workspace to connect Fabric workspace. To grant contributor access, open your Fabric workspace, select three dots (...), select **Workspace access**, then **Add people or group**, then add Purview MSI as **Contributor**.
- Fabric tables must be in Delta format or Iceberg format.

## Profiling and data quality scanning for data in Fabric Lakehouse

After completed connection setup successfully, you can profile, create and apply rules, and run a data quality (DQ) scan of your data in Fabric Lakehouse. Follow these steps:

1. Associate a Lakehouse table to a data product for curation, discovery, and subscription. Learn how to [create and manage data products](unified-catalog-data-products-create-manage).
2. Profile Fabric Lakehouse table. Learn how to [configure and run data profiling for a data asset](unified-catalog-data-quality-profiling).
3. Configure and run data quality scan to measure data quality of a Fabric Lakehouse table. Learn how to [configure and run a data quality scan](unified-catalog-data-quality-scan).

Important

- Make sure that your data are in Delta format or Iceberg format.
- Make sure the Data Map scan ran successfully. If it didn't, then rerun the scan.

## Limitations

**Data Quality for Parquet file is designed to support:**

- A directory with Parquet Part File. For example: *./Sales/{Parquet Part Files}*. The Fully Qualified Name must follow `https://(storage account).dfs.core.windows.net/(container)/path/path2/{SparkPartitions}`. Make sure there are no {n} patterns in directory/sub-directory structure; it must rather be a direct FQN leading to {SparkPartitions}.
- A directory with Partitioned Parquet Files, partitioned by columns within the dataset like sales data partitioned by year and month. For example: *./Sales/{Year=2018}/{Month=Dec}/{Parquet Part Files}*.

Both supported Parquet directory patterns present a consistent Parquet dataset schema. Limitation: It isn't designed to or won't support N arbitrary Hierarchies of Directories with Parquet Files. We advise the customer to present data in (1) or (2) constructed structure. So recommending customer to follow the supported parquet standard or migrate their data to **ACID** compliant delta format.

## Tips for initial setup

Use the following tips when setting up data quality scanning for Fabric Lakehouse data for the first time.

**For Data Map:**

- Ensure the service principal (SPN) has workspace permissions.
- Ensure scan connection uses the service principal.
- Running a full scan is suggested if you're setting up a Lakehouse scan for the first time.
- Check that the ingested assets have been updated or refreshed.

**For Unified Catalog:**

- The data quality connection needs to use MSI credentials.
- Ideally, create a new data product for first-time testing of Lakehouse data quality scans.
- Add the ingested data assets, and check that the data assets are updated.
- Try running a profile first. If successful, try running a data quality rule. If not successful, try refreshing the asset schema (**Schema** &gt; **Schema management** &gt; **Import schema**).
- Some users also had to create a new Lakehouse and sample data to verify everything works from scratch. In some cases, working with assets that were previously ingested in the Data Map, the experience isn't consistent.

## Resources

Use the following resources for related tasks and concepts.

**Data quality tasks:**

- [Configure and run data profiling of your data](unified-catalog-data-quality-profiling)
- [Configure and run data quality scan](unified-catalog-data-quality-scan)
- [Set up data quality connection](unified-catalog-data-quality-supported-sources-connection)
- [FAQ and self-help](unified-catalog-data-quality-troubleshooting)

**Fabric data ingestion:**

- [Learn about Mirroring in Fabric](/en-us/fabric/database/mirrored-database/overview)
- [OneLake shortcuts](/en-us/fabric/onelake/onelake-shortcuts)

**Related data quality scenarios:**

- [Data Quality for Fabric mirrored data sources](unified-catalog-data-quality-fabric-mirrored-databases)
- [Data Quality for Fabric shortcut databases](unified-catalog-data-quality-fabric-shortcut-databases)