---
layout: Conceptual
title: Managed virtual networks and private endpoints in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-private-endpoints-managed-virtual-network
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2025-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Understand how to use managed virtual networks and managed private endpoints in Microsoft Purview
ms.custom: sfi-image-nochange
locale: en-us
document_id: 07d16c65-812f-8b83-8340-d58674563060
document_version_independent_id: 07d16c65-812f-8b83-8340-d58674563060
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-private-endpoints-managed-virtual-network.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-private-endpoints-managed-virtual-network
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-private-endpoints-managed-virtual-network.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/20ed8455-bc18-4537-87a4-83784e7b2a39
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9a7f703b-30bb-4d62-9eb4-97213f571849
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: fd0ea58d-8ded-215b-525f-f77977db8880
---

# Managed virtual networks and private endpoints in Microsoft Purview | Microsoft Learn

This article describes managed virtual networks and managed private endpoints in Microsoft Purview.

Note

- Microsoft Purview added new version of Managed Virtual Network support mid November 2023. New managed private endpoints no longer support the old managed virtual network. Create new a managed virtual network, and all your newly created resources will be using the latest version. Learn about the difference here.
- Microsoft Purview accounts that were deployed before December 15, 2023 include a managed storage account. Microsoft Purview accounts that are deployed after (or deployed using API version 2023-05-01-preview onwards) don't have manage storage accounts deployed to the Azure subscription. Instead, these accounts include an ingestion storage account that's deployed to Microsoft's internal Azure subscriptions.

## Managed Virtual Network

A Managed Virtual Network (virtual network) is a virtual network that is deployed and managed by Microsoft Purview to empower scanning data sources inside a private network, without having to deploy and manage any self-hosted integration runtime virtual machines by the customer in Azure.

![Microsoft Purview Managed Virtual Network architecture](media/catalog-managed-vnet/purview-managed-vnet-architecture.png)

You can deploy Azure Managed Virtual Network Integration Runtimes (IR) within Microsoft Purview Managed Virtual Networks in any available Microsoft Purview region. From there, the managed virtual network IR can use private endpoints to securely connect to and scan the supported data sources.

Creating a Managed virtual network IR within Managed Virtual Network ensures that data integration process is isolated and secure.

Benefits of using Managed Virtual Network:

- With a Managed Virtual Network, you can offload the burden of managing the Virtual Network to Microsoft Purview. You don't need to create and manage VNets or subnets for Azure Integration Runtime to use for scanning Azure data sources.
- It doesn't require deep Azure networking knowledge to do data integrations securely. Using a Managed Virtual Network is much simplified for data engineers.
- Managed Virtual Network along with Managed private endpoints protects against data exfiltration.

A managed virtual network is created for your Microsoft Purview account when you create a Managed Virtual Network Integration Runtime for the first time in your Microsoft Purview account. You can't view or manage the virtual networks outside of Microsoft Purview.

## Managed private endpoints

Managed private endpoints are private endpoints created in the Microsoft Purview Managed Virtual Network establishing a private link to Microsoft Purview and Azure resources. Microsoft Purview manages these private endpoints on your behalf.

![Microsoft Purview Managed private endpoint](media/catalog-managed-vnet/purview-managed-pe-list-2.png)

Microsoft Purview supports private links. Private link enables you to access Azure services like Azure Storage, Azure SQL Database, Azure Cosmos DB, Azure Synapse Analytics.

When you use a private link, traffic between your data sources and Managed Virtual Network traverses entirely over the Microsoft backbone network. Private Link protects against data exfiltration risks. You establish a private link to a resource by creating a private endpoint.

Private endpoint uses a private IP address in the Managed Virtual Network to effectively bring the service into it. Private endpoints are mapped to a specific resource in Azure and not the entire service. Customers can limit connectivity to a specific resource approved by their organization. Learn more about [private links and private endpoints](/en-us/azure/private-link).

Warning

If an Azure PaaS data store (Blob, Azure Data Lake Storage Gen2, Azure Synapse Analytics) has a private endpoint already created against it, and even if it allows access from all networks, Microsoft Purview would only be able to access it using a managed private endpoint. If a private endpoint does not already exist, you must create one in such scenarios.

A private endpoint connection is created in a "Pending" state when you create a managed private endpoint in Microsoft Purview. An approval workflow is initiated. The private link resource owner is responsible to approve or reject the connection.

![approval for managed private endpoint](media/catalog-managed-vnet/purview-managed-data-source-approval.png)

If the owner approves the connection, the private link is established. Otherwise, the private link won't be established. In either case, the Managed private endpoint is updated with the status of the connection.

![Approve Managed private endpoint](media/catalog-managed-vnet/purview-managed-data-source-pe-azure.png)

Only a Managed private endpoint in an approved state can send traffic to a given private link resource.

## Supported regions and data sources

**Supported regions:** Managed Virtual Network is available in all the Microsoft Purview supported regions. Up to five managed virtual networks can be deployed across different regions in a single Microsoft Purview instance.

**Supported data sources for scan:** You can use the Managed Virtual Network Integration Runtime to scan many types of data source. Refer to [the supported data sources](data-map-integration-runtime-choose#supported-data-sources).

**Supported systems with managed private endpoint:** The following services have native private endpoint support. They can be connected through private link from Microsoft Purview's Managed Virtual Network:

- Azure Blob Storage
- Azure Cosmos DB
- Azure Data Lake Storage Gen 2
- Azure Database for MySQL
- Azure Database for PostgreSQL
- Azure Databricks
- Azure Dedicated SQL pool (formerly SQL DW)
- Azure Files
- Azure Key Vault
- Azure SQL Database
- Azure SQL Managed Instance
- Azure Synapse Analytics
- Snowflake

## Pricing details

When using Managed Virtual Network feature, you're charged by two parts:

- **Charge per scan run** (pay as you go): based on scan duration \* used vCore hours \* unit price per vCore hour. This is the common charge for scan running on any integration runtime types.
- **Charge on Managed VNet IR uptime** (always on): based on **Managed VNet IR life time \* 1/8 vCore hour** \* unit price per vCore hour. Managed virtual network IR life time means from the IR instance being successfully created until its deleted. The charge applies no matter you have scan run or not.

You can find details for "Automated Scanning, Ingestion & Classification" pricing from [Microsoft Purview pricing page](https://azure.microsoft.com/pricing/details/purview/).

As an example, for a given month, you scan various data sources and the execution consumes X vCore hours of "Scanning Ingestion and Classification - Standard vCore" in total, and the managed virtual network runtime is provisioned to run for the whole month. The charge is: X vCore hours \* $0.63 per vCore hour for scan runs + 1/8 \* $0.63 per vCore hour \* 730 hours for Managed virtual network IR uptime.

## Deployment steps

### Prerequisites

Before deploying a Managed virtual network and Managed Virtual Network Integration Runtime for a Microsoft Purview account, ensure you meet the following prerequisites:

1. From Microsoft Purview roles, you need Data Source Administrator permission on any collection in your Microsoft Purview account.
2. From Azure RBAC roles, you must be contributor on the Microsoft Purview account and data source to approve private links.

### Create Managed Virtual Network Integration Runtime

1. Open the Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Selecting the [**the Microsoft Purview governance portal**](https://web.purview.azure.com/) button.
2. Navigate to the **Data Map -&gt; Integration runtimes**.
3. From **Integration runtimes** page, select **+ New** icon, to create a new runtime. Select **Azure** and then select **Continue**.

    ![Screenshot that shows how to create new Azure runtime](media/catalog-managed-vnet/purview-managed-ir-create.png)
4. Provide a **name** for your Managed Virtual Network Integration Runtime, select a region, and give your managed virtual network a name.

    ![Screenshot that shows to create a Managed VNet Integration Runtime with details](media/catalog-managed-vnet/purview-managed-ir-create-details.png)
5. Select **Create**.
6. Deploying the Managed Virtual Network Integration Runtime triggers multiple workflows in the Microsoft Purview governance portal for creating managed private endpoints for Microsoft Purview and its managed Storage Account. Select each workflow to approve the private endpoint for the corresponding Azure resource.

    ![Screenshot that shows deployment of a Managed VNet Integration Runtime](media/catalog-managed-vnet/purview-managed-ir-pe-creation.png)
7. In Azure portal, from your Microsoft Purview account resource window, approve the managed private endpoint. From managed storage account page approve the managed private endpoints for blob and queue services:

    ![Screenshot that shows how to approve a managed private endpoint for Microsoft Purview](media/catalog-managed-vnet/purview-managed-pe-account.png)

    ![Screenshot that shows how to approve ingestion private endpoints for managed storage account](media/catalog-managed-vnet/purview-managed-pe-ingestion.png)
8. From Management, select Managed private endpoint to validate if all managed private endpoints are successfully deployed and approved.

    ![Screenshot that shows managed private endpoints in Microsoft Purview](media/catalog-managed-vnet/purview-managed-pe-list-account-and-ingestion.png)
9. Go to the Integration runtimes page, you'll see the IR status shown up as “Initializing” upon creation. Wait until it turns into “**Running**” state to use in scan. It usually takes several minutes.

    ![Screenshot that shows managed VNet IR status in Microsoft Purview](media/catalog-managed-vnet/purview-managed-vnet-ir-status.png)

Tip

You can create multiple managed virtual networks in different regions in your Microsoft Purview account to securely access resources across regions.

### Create managed private endpoints for data sources

You can use managed private endpoints to connect your data sources to ensure data security during transmission.

Tip

If your data source allows public access and you want to connect via public network, you can skip this step. Scan runs can be executed as long as the integration runtime can connect to your data source.

To deploy and approve a managed private endpoint for a data source, follow these steps selecting data source of your choice from the list:

1. Navigate to **Management**, and select **Managed private endpoints**.
2. Select **+ New**.
3. From the list of supported data sources, select the type that corresponds to the data source you're planning to scan using Managed Virtual Network Integration Runtime.

    ![Screenshot that shows how to create a managed private endpoint for data sources](media/catalog-managed-vnet/purview-managed-data-source.png)
4. Provide a name for the managed private endpoint, select the Azure subscription, data source, and Managed Virtual Network from the drop-down lists. Select **Create**.

    ![Screenshot that shows how to select data source for setting managed private endpoint](media/catalog-managed-vnet/purview-managed-data-source-pe.png)
5. From the list of managed private endpoints, select the newly created managed private endpoint for your data source and then select on **Manage approvals in the Azure portal**, to approve the private endpoint in Azure portal.

    ![Screenshot that shows the approval for managed private endpoint for data sources](media/catalog-managed-vnet/purview-managed-data-source-approval.png)
6. By selecting the link, you're redirected to Azure portal. Under the private endpoints connection, select the newly created private endpoint and select **Approve**.

    ![Screenshot that shows how to approve a  private endpoint for data sources in Azure portal](media/catalog-managed-vnet/purview-managed-data-source-pe-azure.png)

    ![Screenshot that shows approved private endpoint for data sources in Azure portal](media/catalog-managed-vnet/purview-managed-data-source-pe-azure-approved.png)
7. Inside the Microsoft Purview governance portal, the managed private endpoint must be shown as approved as well.

    ![Screenshot that shows managed private endpoints including data sources' in Purview governance portal](media/catalog-managed-vnet/purview-managed-pe-list-2.png)

### Set up scan to use managed virtual network IR

1. Go to **Data map** -&gt; **Sources**, register the source that you want to scan if not already done.
2. Go to your source -&gt; **+ New scan**.
3. Under the **Connect via integration runtime**, select the managed virtual network IR you created. Configure the other scan settings as usual, and trigger a run.

    ![Screenshot that shows how to set up scan using managed VNet IR](media/catalog-managed-vnet/purview-managed-vnet-ir-scan.png)

## Earlier version of Managed Virtual Network

To check the version of managed virtual network IR that you're using, go to **Data Map** -&gt; **Integration runtimes**, and see the **Version** column.

![Screenshot that shows how to check managed VNet IR version](media/catalog-managed-vnet/purview-managed-vnet-ir-versions.png)

The concept and architecture of Managed Virtual Network and managed private endpoint apply for both versions. The following table lists the differences in some aspects of the two versions. The version 2 provides better scan performance as well.

| Area | Version 1 | Version 2 (current) |
| --- | --- | --- |
| Supported regions | Available only in Australia East, Canada Central, East US, East US 2, North Europe, and West Europe. | Available in all Microsoft Purview supported regions. |
| Multi-vnet & multi-region | Only one virtual network supported at a time. | Up to five virtual networks supported across multiple regions. |
| Supported data source types for scan | Support scanning the following Azure data sources only.- Azure Blob Storage- Azure Cosmos DB- Azure Data Lake Storage Gen 2- Azure Database for MySQL- Azure Database for PostgreSQL- Azure Dedicated SQL pool (formerly SQL DW)- Azure Files- Azure SQL Database- Azure SQL Managed Instance- Azure Synapse Analytics | Expanded to support scanning more data sources. See full list [here](data-map-integration-runtime-choose#supported-data-sources). |
| Interactive authoring from Microsoft Purview portal (test connection, browse source during scan setup) | Need to turn on in Managed virtual network IR settings. | Always available |
| Name of the managed virtual network | default (autogenerated) | Configurable |
| Pricing | Charge on scan and ingestion jobs. | Charge on scan and ingestion jobs, and the running period of the managed virtual network IR. Learn more from Pricing details. |

## Update to latest version

Microsoft Purview added new version of Managed Virtual Network support mid-November 2023. All the newly created resources will be using the new offering. If you're using the earlier version (which you can check), you can update to the latest version of the managed virtual network.

There are several advantages of using the new version of Managed Virtual Network:

- Generally available in all Microsoft Purview supported regions.
- Expanded data source support, including Databricks, Snowflake, Fabric, and all the sources that are supported by the default Azure integration runtime.
- Better scan performance.
- Interactive operations from Purview portal are always available (test connection, browse source during scan setup, etc.)

To upgrade, you can follow the instructions on this page: [Upgrade to the new managed virtual network integration runtime.](data-governance-private-endpoints-managed-virtual-network-ir-migrate)