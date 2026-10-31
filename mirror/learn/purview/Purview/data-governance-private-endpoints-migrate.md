---
layout: Conceptual
title: Migrate governance private endpoints to Microsoft Purview portal | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-private-endpoints-migrate
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
description: Learn how to migrate your existing private endpoints for governance solutions from the classic data governance portal to the Microsoft Purview portal.
locale: en-us
document_id: c2008e90-4b0b-c724-cf3f-d1a34623e02f
document_version_independent_id: c2008e90-4b0b-c724-cf3f-d1a34623e02f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-private-endpoints-migrate.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-private-endpoints-migrate
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-private-endpoints-migrate.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/20ed8455-bc18-4537-87a4-83784e7b2a39
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/9a7f703b-30bb-4d62-9eb4-97213f571849
platformId: 698c4877-5933-e46d-fc34-df99a4197bfe
---

# Migrate governance private endpoints to Microsoft Purview portal | Microsoft Learn

Important

This article covers migrating private endpoints for governance solutions from the [classic governance portal](https://web.purview.azure.com) to the [Microsoft Purview portal](https://purview.microsoft.com/). If you're building your private endpoint connections for the first time, follow the full [private endpoints article](data-governance-private-endpoints) instead.

Note

Currently, Azure Data Factory, Azure Machine Learning, and Azure Synapse connections aren't supported with the platform private endpoint, and might not work after switching.

Microsoft Purview now supports platform private endpoints for your [organization-level account](data-governance-purview-portal). You can follow these steps to migrate your existing Microsoft Purview account private endpoints to the new platform private endpoints.

## Prerequisites

If you're still using version 1 of the managed virtual network ([which you can check](data-governance-private-endpoints-managed-virtual-network#earlier-version-of-managed-virtual-network)), to migrate to the new private endpoints you need to [upgrade to the latest version of the virtual network.](data-governance-private-endpoints-managed-virtual-network-ir-migrate)

## Migrate your existing private endpoints

![Screenshot of the private endpoint migration experience in the Azure portal.](media/migrate-to-governance-private-endpoint/migration-experience.png)

1. In the [Azure portal](https://portal.azure.com), search for and open your Microsoft Purview account.
2. Select the **Networking** page.
3. If it's not already open, select the **Upgrade to platform PE** tab.
4. Set up your platform private endpoints
5. Create managed private endpoint connections to platform private endpoints
6. Switch your Microsoft Purview API endpoint

## Set up your platform private endpoints

For every [account private endpoint](data-gov-classic-private-link-end-to-end#enable-account-and-portal-private-endpoint) you'll need to set up a platform private endpoint. All the account private endpoints you have are listed under the step. For each existing endpoint:

1. In the [Azure portal](https://portal.azure.com), search for and open your Microsoft Purview account.
2. Select the **Networking** page.
3. If it's not already open, select the **Upgrade to platform PE** tab.
4. Select the **+ Create platform private endpoint** button.
5. In the **Create a private endpoint - Basics** tab, enter or select the following information:

    | Settings | Value |
    | --- | --- |
    | **Project details** |  |
    | Subscription | Select your Azure Subscription |
    | Resource group | Select your resource group. |
    | **Instance details** |  |
    | Name | Create a unique name. |
    | Network Interface Name | Filled automatically by the instance name. |
    | Region | Selected automatically based on your resource group. |
6. Once that information is complete, select **Next: Resource** and in the **Create a private endpoint - Resource** page, enter or select the following information:

    | Settings | Value |
    | --- | --- |
    | Connection method | Select connect to an Azure resource in my directory |
    | Subscription | Select your subscription |
    | Resource type | Select **Microsoft.Purview/accounts** |
    | Resource | Select your Microsoft Purview resource |
    | Target subresource | Platform |
7. Once that information is properly input, select **Next: Virtual Network** and enter or select the following information:

    | Settings | Value |
    | --- | --- |
    | **NETWORKING** |  |
    | Virtual network | Select your existing virtual network. |
    | Subnet | Select your existing subnet |
    | **PRIVATE IP configuration** | Select **Dynamically allocate IP address**. |
8. Select **Next: DNS** and enter the following information:

    | Settings | Value |
    | --- | --- |
    | Integrate with private DNS zone | Select **Yes** |
    | Subscription | Select your subscription where your DNS zone is configured. |
    | Resource group | Select the resource group where your DNS zone is configured. |
9. Select **Next: Tags** and on the tags page you can optionally add any tags your organization is using in Azure.
10. Select **Next: Review + create** which displays the **Review + create** page where Azure validates your configuration. When you see the **Validation passed** message, select **Create**.
11. If you configured firewall allowlist rules for your account endpoints (`{account-name}.purview.azure.com`), you need to update your firewall configuration for the new platform private endpoints: `{tenant id}-api.purview-service.microsoft.com`, `api.purview-service.microsoft.com`. The use of the endpoint `api.purview-service.microsoft.com` will require additional configuration and checks. This will depend on your network setup, and we recommend using `{tenant id}-api.purview-service.microsoft.com` for ease of setup.

Note

`api.purview-service.microsoft.com` won't be automatically configured in the DNS to point to `{tenant id}-api.purview-service.microsoft.com` when the private endpoint is created; it will continue to point to the public IP of the purview instance unless overridden by subsequent customer network or DNS configuration changes.

## Create managed private endpoint connections to platform private endpoints

1. In the [Microsoft Purview portal](https://purview.microsoft.com) open the Microsoft Purview Data Map.
2. Navigate to **Source management**, and select **Managed private endpoints**.
3. Select the pop-up link that says, 'Click here to provision platform managed PE for all your managed VNets'.
4. Microsoft Purview will create managed platform private endpoints for all your existing managed account endpoints.
5. Select each approval link to approve the endpoints, or approve them directly by:

    1. In the [Azure portal](https://portal.azure.com) search for your Microsoft Purview account and open it.
    2. Select **Networking**
    3. Select **Private endpoints**
    4. Approve the new list of private endpoints.

## Switch your Microsoft Purview API endpoint

Now that you've created the required private endpoints, connected your resources, and recreated your scans, you can update your API endpoint. On the networking page, select the **Switch endpoint** button to switch to the new Microsoft Purview API endpoint for scanning and tenant account access.

The new API endpoint you'll be using is either:

`https://api.purview-service.microsoft.com/`

`https://{your-tenant-id}-api.purview-service.microsoft.com/`

Note

The old endpoint will be operational in parallel for users with access to the classic portal. Scans that were already running will continue to use the existing endpoint until they finish. New scans will use the new platform endpoint.

## Remove account endpoints

Once all your currently running scans have completed, remove your existing account endpoints to switch completely to your new platform private endpoints.