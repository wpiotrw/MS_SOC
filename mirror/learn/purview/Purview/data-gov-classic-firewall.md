---
layout: Conceptual
title: Configure Microsoft Purview firewall settings for classic governance portal | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-classic-firewall
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: zeinam
ms.date: 2025-02-24T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to configure firewall settings for your Microsoft Purview account for using the classic governance portal.
locale: en-us
document_id: 7f7c55e7-4821-7ee0-dcab-4fba1247f41a
document_version_independent_id: 7f7c55e7-4821-7ee0-dcab-4fba1247f41a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-classic-firewall.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-classic-firewall
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-classic-firewall.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 91b81c4c-e5a6-5c87-acfb-6e7835fc0b77
---

# Configure Microsoft Purview firewall settings for classic governance portal | Microsoft Learn

Important

This article covers private endpoints for the classic Microsoft Purview governance portal (https://web.purview.azure.com). If you're using the new Microsoft Purview portal (https://purview.microsoft.com/), follow the [documentation for private endpoints in the Microsoft Purview portal](data-governance-private-endpoints).

## Prerequisites

To configure Microsoft Purview account firewall settings, ensure you meet the following prerequisites:

1. An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
2. An existing Microsoft Purview account.
3. Must have IAM Contributor role on the Microsoft Purview account.
4. Must have IAM Reader role on the Azure subscription that hosts the Microsoft Purview account.

## Microsoft Purview firewall deployment scenarios

To configure Microsoft Purview firewall, follow these steps:

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Navigate to your Microsoft Purview account in the portal.
3. Under \**Settings*, choose **Networking**.
4. In the **Firewall** tab, under **Public network access**, change the firewall settings to the option that suits your scenario:

- **Enabled from all networks**

    ![Screenshot showing the purview account firewall page, selecting public network in the Azure portal.](media/catalog-private-link/purview-firewall-public.png)

    By choosing this option:

    - All public network access into your Microsoft Purview account is allowed.
    - If you're using a [managed Event Hubs for kafka notifications](data-map-kafa-notifications), public network access is set to *All networks* on your Microsoft Purview account's Event Hubs.
    - If you have an account created before December 15, 2023, public network access is set to *Enabled from all networks* on your Microsoft Purview account's managed storage account. If you have an account created after that date (or deployed using API version 2023-05-01-preview onwards), the public network access on your Microsoft Purview account's ingestion storage account *Enabled from all networks*.

    Note

    Even though the network access is enabled through public internet, to gain access to the classic governance portal, [users must be first authenticated and authorized](data-gov-classic-permissions).
- **Disabled for ingestion only (preview)**

    ![Screenshot showing the purview account firewall page, selecting ingestion only in the Azure portal.](media/catalog-private-link/purview-firewall-ingestion.png)

    By choosing this option:

    - Public network access to your Microsoft Purview account through API and the classic governance portal is allowed.
    - All public network traffic for ingestion is disabled. In this case, you must configure a private endpoint for ingestion before setting up any scans. For more information, see [Use private endpoints for your Microsoft Purview account](data-gov-classic-private-link).
    - If you're using a [managed Event Hubs for kafka notifications](data-map-kafa-notifications), public network access is set to *Disabled* on your Microsoft Purview account's Event Hubs.
    - If you have an account created before December 15, 2023, public network access is set to *Disabled* on your Microsoft Purview account's managed storage account. If you have an account created after that date (or deployed using API version 2023-05-01-preview onwards), the public network access on your Microsoft Purview account's ingestion storage account *Disabled*.
- **Disabled from all networks**

    ![Screenshot showing the purview account firewall page, selecting private network in the Azure portal.](media/catalog-private-link/purview-firewall-private.png)

    By choosing this option:

    - All public network access into your Microsoft Purview account is disabled.
    - All network access to your Microsoft Purview account through APIs or the classic governance portal including traffic to run scans is allowed only through private network using private endpoints. For more information, see [Connect to your Microsoft Purview and scan data sources privately and securely](data-gov-classic-private-link-end-to-end).
    - If you're using a [managed Event Hubs for kafka notifications](data-map-kafa-notifications), public network access is set to *Disabled* on your Microsoft Purview account's Event Hubs.
    - If you have an account created before December 15, 2023, public network access is set to *Disabled* on your Microsoft Purview account's managed storage account. If you have an account created after that date (or deployed using API version 2023-05-01-preview onwards), the public network access on your Microsoft Purview account's ingestion storage account is set to *Disabled*.

1. Select **Save**.

    ![Screenshot showing the purview account firewall page, selecting save in the Azure portal.](media/catalog-private-link/purview-firewall-save.png)