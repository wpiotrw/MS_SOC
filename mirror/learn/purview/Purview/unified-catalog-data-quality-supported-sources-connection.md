---
layout: Conceptual
title: Connect to Data Sources for Data Quality in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-supported-sources-connection
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
description: Learn how to set up data source connection for data quality in Microsoft Purview Unified Catalog.
locale: en-us
document_id: aa029780-87c7-24ab-ffb1-8bfe1921cdd6
document_version_independent_id: aa029780-87c7-24ab-ffb1-8bfe1921cdd6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-supported-sources-connection.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-supported-sources-connection
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-supported-sources-connection.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/20ed8455-bc18-4537-87a4-83784e7b2a39
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/9a7f703b-30bb-4d62-9eb4-97213f571849
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 05e9c719-0f1e-10b4-75b9-314f7f7a809b
---

# Connect to Data Sources for Data Quality in Unified Catalog | Microsoft Learn

Data source connections set up the authentication needed to profile your data for a statistical snapshot, or scan your data for data quality anomalies and scoring.

Setting up data source connections is the **fourth** step in the data quality life cycle for a data asset. Previous steps are:

1. [Assign users data quality steward permissions in Unified Catalog](data-governance-roles-permissions#how-to-assign-catalog-level-roles) to use all data quality features.
2. [Register](data-map-data-sources-register-manage#register-a-new-source) and [scan](data-map-scan-data-sources) a data source in your Microsoft Purview Data Map.
3. [Add data assets to a data product](unified-catalog-data-products-create-manage#add-and-remove-data-assets).

## Prerequisites

1. To create connections to data assets, your users must be in the [data quality steward role](data-governance-roles-permissions#how-to-assign-governance-domain-roles).
2. You need at least read access to the data source for which you're setting up the connection.

## Supported multicloud data sources

Browse the [supported data source document](unified-catalog-data-quality-supported-sources-file-formats) to view the list of supported data sources, including file formats for data profiling and data quality scanning, with and without virtual network support.

Currently, data quality scans can only run by using [managed identity](data-map-data-scan-credentials#use-microsoft-purview-system-assigned-managed-identity-to-set-up-scans) as an authentication option for Microsoft native data sources, such as Microsoft Fabric, Azure Data Lake Storage Gen2, Azure SQL, Synapse, and Azure SQL Managed Instance. **For Azure Databricks, Snowflake, and Google BigQuery, a managed identity can't be used as an authentication option**.

Data quality services run on **Apache Spark 3.5** and **Delta Lake 3.2.1**.

Important

To access these sources, either you need to set your Azure Storage sources to have an open firewall, to [Allow Trusted Azure Services](/en-us/azure/storage/common/storage-network-security?tabs=azure-portal#grant-access-to-trusted-azure-services), or to use private endpoints follow the guideline documented in the [data quality managed virtual network configuration guide.](unified-catalog-data-quality-managed-virtual-networks)

Microsoft Purview only needs read-level permissions to discover metadata, run profiling, and execute Data Quality scans.

## Set up data source connection

Follow these steps to create a new connection for the data products and data assets in a governance domain.

1. In Unified Catalog, select **Health management**, and then select **Data quality**.
2. Select a governance domain from the list.
3. From the **Manage** dropdown list, select **Connections**.
4. On **Connections**, select **New**.
5. On **Create connection**, enter a **Display name** and an optional **Description**.
6. Select a **Source type**.
7. Select one of the data sources: Azure subscription, Data Map, or enter a data source manually. Depending on which data source you choose, enter the required access details. The connection is then tested.
8. If the test connection is successful, select **Submit** to complete the connection setup.

Tip

- You can also create a connection to your resources by using private endpoints and a Microsoft Purview Data Quality managed virtual network. Learn more about [setting up managed virtual networks for data quality](unified-catalog-data-quality-managed-virtual-networks).
- Connection setup steps vary for native connectors. Check the connection setup steps from native connectors articles to set up connection for [Azure Databricks](unified-catalog-data-quality-azure-databricks-unity-catalog), [Snowflake](unified-catalog-data-quality-snowflake), [Google BigQuery](unified-catalog-data-quality-google-big-query), and [Azure Synapse](unified-catalog-data-quality-azure-synapse) connectors.
- To set up Azure Dedicated SQL Pool (formerly SQL DW) connection, select source type as **Azure SQL Database** and add `sqldatawarehouse.database.windows.net` as **endpoint** name.
- The virtual network region is auto populated from the selected source region. Find details on [managing virtual network provisioning](unified-catalog-data-quality-managed-virtual-networks#manage-virtual-network-provisioning).
- For Azure SQL Managed Instance, you need to provide the port number for connection. Public endpoint port number is 3342 and private endpoint port number is 1433.

## Grant Microsoft Purview permissions on the source

After you create the connection, grant Microsoft Purview managed identity permissions on your data sources to scan them:

- To scan Azure Data Lake Storage Gen2, assign the storage blob data reader role to Microsoft Purview Managed Identity. Follow the [steps to assign managed identity permissions](register-scan-adls-gen2#authentication-for-a-scan).
- To scan an Azure SQL database, assign the db\_datareader role to the Microsoft Purview Managed Identity. Follow the [steps to assign managed identity permissions](register-scan-azure-sql-database).