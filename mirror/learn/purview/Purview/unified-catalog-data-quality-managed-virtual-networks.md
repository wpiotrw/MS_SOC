---
layout: Conceptual
title: Set Up Managed Virtual Networks for Data Quality Scans of Data Sources in Virtual Networks | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-managed-virtual-networks
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
description: Set up managed virtual networks and private endpoints in Microsoft Purview to profile and scan data sources that are secured inside virtual networks.
locale: en-us
document_id: a792b57c-ca2c-afbf-e867-617698ea91ab
document_version_independent_id: a792b57c-ca2c-afbf-e867-617698ea91ab
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-managed-virtual-networks.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-managed-virtual-networks
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-managed-virtual-networks.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/20ed8455-bc18-4537-87a4-83784e7b2a39
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9a7f703b-30bb-4d62-9eb4-97213f571849
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: d6099fba-64f9-7845-9e6b-19907452730b
---

# Set Up Managed Virtual Networks for Data Quality Scans of Data Sources in Virtual Networks | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

This article outlines the steps to create protected data source connections for [data profiling](unified-catalog-data-quality-profiling) and [data quality scans](unified-catalog-data-quality-scan) in Microsoft Purview.

Virtual networks and private endpoints enhance the security and isolation of Azure resources. Virtual network protected endpoints let you access Azure services while keeping traffic on the Azure backbone network. Private endpoints go further by assigning a private IP address in your virtual network, so all traffic stays within the network and doesn't use the public internet. Virtual network protected endpoints and private endpoints are essential when security and network isolation are critical, because they minimize exposure to threats from the public internet.

## Review user permission requirements

You need the following permissions to set up managed virtual networks for data quality:

- Compute provision – [Governance Domain Owner](data-gov-classic-permissions)
- Managed private endpoint creation - [Governance Domain Owner](data-gov-classic-permissions)
- Private endpoint approval – [Owner of the Azure storage source](/en-us/azure/role-based-access-control/built-in-roles#general)

Caution

Compute and managed private endpoint connections are shared across all governance domains in the same Purview account. These connections are shared per region and data source.

## Manage virtual network provisioning

Data Governance Administrators can provision a virtual network compute location in supported Azure regions. To provision a compute location, go to **Settings** &gt; **Unified Catalog** &gt; **Virtual network** in the Unified Catalog Admin page. Select a region from the **Region** dropdown. Regions that are already set up are greyed out.

![provisioning page for data governance adminstrator to provision vnet.](media/data-quality-virtual-network-support/provisioning.png)

Deleting a configured region removes all associated data quality connections linked to that region's virtual network across business domains. To delete a region, select **X** on the region's row. You can't delete a region while it's being provisioned. Provisioning has three stages: Provisioning, Completed, and Available.

## Configure a data quality managed virtual network

Configure a data quality managed virtual network by creating a connection to a protected data source.

1. In the Microsoft Purview Unified Catalog, select **Health Management**, and then select **Data quality**.
2. Select a governance domain from the list.
3. From the **Manage** dropdown list, select **Connections** to open the connections page.
4. Select the **New** tab to create a new connection for the data products and data assets in your governance domain.
5. In the connection page, add a display name and description, and select the data source type.
6. Add other data source details like **Subscription** and **Storage Account** name or **Server Name** and **database name**, depending on the source.
7. Select the **Enable managed V-Net** checkbox.
8. Select the region where the data source is housed.
9. Purview Data Quality checks if a compute infrastructure already exists for the account in that region. If not, you're prompted to create a new **virtual network dedicated compute**.

    ![Screenshot of the create connection overview page with the enable managed virtual network selected.](media/data-quality-virtual-network-support/vnet-connection-setup-c.png)

    Tip

    Provisioning compute can take up to 10 minutes. After requesting compute provisioning, you can save the connection creation request in draft mode and edit it later.
10. After the compute is provisioned, data quality checks if a **private endpoint** connection to the asset already exists. If not, you're prompted to create a private endpoint connection.

    ![Screenshot of the create connection page with the private endpoint prompt.](media/data-quality-virtual-network-support/vnet-connection-setup-e.png)
11. After the private endpoint is created, or if a private endpoint already exists but wasn't approved, you're prompted to approve the private endpoint connection request.

    ![Screenshot of the create connection page with the approve private endpoint prompt.](media/data-quality-virtual-network-support/vnet-connection-setup-f.png)
12. To approve this request, go to the Networking tab in Storage Account or SQL Server. Select the **Private access** tab, select a pending connection, and select **Approve**.

    ![Screenshot of the networking page of a SQL server private access tab with a request selected.](media/data-quality-virtual-network-support/vnet-connection-setup-g.png)
13. Select **Yes** to approve the connection.

    ![Screenshot of the networking page of a SQL server private access tab with the approval prompt.](media/data-quality-virtual-network-support/vnet-connection-setup-h.png)
14. The request now shows as **Approved**.

    ![Screenshot of the networking page of a SQL server private access tab showing the request is approved.](media/data-quality-virtual-network-support/vnet-connection-setup-i.png)

    Tip

    After you request the private endpoint connection, you can save the connection as a draft and resume after the request is approved.
15. After the private endpoint connection is created and approved, submit the connection.

    ![Screenshot of the create connections page where the Submit button is now available.](media/data-quality-virtual-network-support/vnet-connection-setup-j.png)

Caution

Test connection isn't currently supported for virtual network protected assets.
16. After the connection is completed, you can run data quality jobs as usual against the virtual network protected assets.

Note

Virtual Network currently supports only these data sources:

- **Azure Data Lake storage**
- **Azure SQL**
- **Synapse serverless and Synapse Data Warehouse**
- **Azure Databricks**
- **Snowflake**
- **Microsoft Fabric OneLake (in tenant level)**
- **Azure SQL Managed Instance (SQL MI)**

### Set up data source-specific connections

To set up virtual network connections for specific data sources, see the following resources:

- [Data quality for Azure Databricks UC](unified-catalog-data-quality-azure-databricks-unity-catalog)
- [Data quality for Azure Synapse serverless and data warehouse](unified-catalog-data-quality-azure-synapse)
- [Data quality for Snowflake data](unified-catalog-data-quality-azure-synapse)
- [Data quality for Fabric Lakehouse](unified-catalog-data-quality-fabric-lakehouse)

For Azure SQL and Data Lake storage, follow the steps in Configure a data quality managed virtual network.

## Import a schema for data quality

If the data type in a schema is undefined, incorrectly defined, or changed in the source, your data quality job might fail. If the job fails, re-import the schema by using the schema import capability. You can import schemas for data sources on both public networks and those behind private endpoints. For supported data sources, see Configure a data quality managed virtual network. To import a schema from your data sources, follow these steps:

- In Unified Catalog, under **Health Management**, select **Data quality**.
- Select a business domain, then select a data product, then select a data asset from that data product. You arrive at the data quality overview page.
- Select **Schema**, then select the **Schema management** toggle.
- Select **Import schema** to import the schema.