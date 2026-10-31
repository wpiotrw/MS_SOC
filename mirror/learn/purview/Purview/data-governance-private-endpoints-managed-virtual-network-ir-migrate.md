---
layout: Conceptual
title: Migrate to virtual network integration runtime in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-private-endpoints-managed-virtual-network-ir-migrate
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
description: Understand the steps needed to migrate to the new Kubernetes based managed virtual network integration runtime for a Microsoft Purview account.
locale: en-us
document_id: 12f9e704-eea2-1743-cf88-428889643035
document_version_independent_id: 12f9e704-eea2-1743-cf88-428889643035
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-private-endpoints-managed-virtual-network-ir-migrate.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-private-endpoints-managed-virtual-network-ir-migrate
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-private-endpoints-managed-virtual-network-ir-migrate.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/20ed8455-bc18-4537-87a4-83784e7b2a39
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9a7f703b-30bb-4d62-9eb4-97213f571849
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: e1aaf513-e4bd-296b-343b-c187f6dbb950
---

# Migrate to virtual network integration runtime in Microsoft Purview | Microsoft Learn

Microsoft Purview added new version of Managed Virtual Network support mid-November 2023. All the newly created resources will be using the new offering. If you're using the earlier version ([which you can check](data-governance-private-endpoints-managed-virtual-network#earlier-version-of-managed-virtual-network)), you can update to the latest version of the managed virtual network.

There are several advantages of using the new version of Managed Virtual Network:

- Generally available in all Microsoft Purview supported regions.
- Expanded data source support, including Databricks, Snowflake, Fabric, and all the sources that are supported by the default Azure integration runtime.
- Better scan performance.
- Interactive operations from Purview portal are always available (test connection, browse source during scan setup, etc.)

Important

There is a pricing change to use a managed virtual network with Microsoft Purview. For more information about the capabilities of managed virtual networks and for pricing details, see the [managed virtual network article.](data-governance-private-endpoints-managed-virtual-network#pricing-details)

To upgrade, you need to create a new Managed Virtual Network IR and switch your scans to this new IR. Here's an overview of what you'll need to do to migrate. All specific steps are listed after:

1. Ensure you meet prerequisites
2. Create a new Managed Virtual Network IR
3. Create managed private endpoints for data sources
4. Link your existing scans to the new managed virtual network IR
5. Delete the old managed virtual network V1

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

### Link your existing scans to the new managed virtual network IR

1. Inside Microsoft Purview, navigate to **Data Map**-&gt;**Collections**.

    ![Screenshot of the data map menu with collections selected.](media/migrate-to-new-managed-vnet/select-collections.png)
2. Select to your collections with scans and select the **Scans** button.

    ![Screenshot of the collections page for an example collection with the scans button highlighted.](media/migrate-to-new-managed-vnet/select-scans.png)
3. Select your scan name to see details.

    ![Screenshot of scans in a collection with one of them highlighted.](media/migrate-to-new-managed-vnet/select-scan.png)
4. Select **Edit scan** and choose your new Managed Virtual Network IR from the drop-down.

    ![Screenshot of the scan page with edit scan selected and the integration runtime highlighted](media/migrate-to-new-managed-vnet/edit-scan.png)
5. Save your changes and edit any other scans.

### Delete the old managed virtual network V1

You can look for your old Managed Virtual Network IRs under **Integration Runtimes** and delete them.

![Screenshot of the integration runtime page, showing a managed virtual network highlighted with the delete button.](media/migrate-to-new-managed-vnet/delete-old-vnet.png)