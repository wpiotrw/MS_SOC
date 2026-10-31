---
layout: Conceptual
title: Use private endpoints in the classic Microsoft Purview governance portal | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-classic-private-link
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
ms.subservice: purview-data-governance-classic
ms.collection: 
search.appverid:
- MET150
- MOE150
description: This article describes a high level overview of how you can use private endpoints to secure access to the classic Microsoft Purview governance portal.
locale: en-us
document_id: 29279f3f-dcb9-09ec-842d-16ba5c3452a7
document_version_independent_id: 29279f3f-dcb9-09ec-842d-16ba5c3452a7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-classic-private-link.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-classic-private-link
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-classic-private-link.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: d8eeebf4-6587-1647-acfa-02b20606c023
---

# Use private endpoints in the classic Microsoft Purview governance portal | Microsoft Learn

Important

This article covers private endpoints for the classic Microsoft Purview governance portal (https://web.purview.azure.com). If you're using the new Microsoft Purview portal (https://purview.microsoft.com/), follow the [documentation for private endpoints in the Microsoft Purview portal](data-governance-private-endpoints).

## Conceptual Overview

You can use [Azure private endpoints](/en-us/azure/private-link/private-endpoint-overview) for your Microsoft Purview accounts to allow users on a virtual network (VNet) to securely access the catalog over a Private Link. A private endpoint uses an IP address from the VNet address space for your Microsoft Purview account. Network traffic between the clients on the VNet and the Microsoft Purview account traverses over the VNet and a private link on the Microsoft backbone network.

If you're still using the [classic portal experience](use-microsoft-purview-governance-portal), you can deploy Microsoft Purview *account* private endpoint, to allow only client calls to Microsoft Purview that originate from within the private network. To connect to the classic governance portal using a private network connectivity, you can deploy *portal* private endpoint.

For both the new and classic experience, you can deploy *ingestion* private endpoints if you need to scan Azure IaaS and PaaS data sources inside Azure virtual networks and on-premises data sources through a private connection. This method ensures network isolation for your metadata flowing from the data sources to Microsoft Purview Data Map.

![Screenshot that shows Microsoft Purview with Private Endpoints.](media/catalog-private-link/purview-private-link-overview.png)

## Prerequisites

Before deploying private endpoints for Microsoft Purview account, ensure you meet the following prerequisites:

1. An Azure account with an active subscription. [Create an account for free.](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn)
2. An existing Azure Virtual network. Deploy a new [Azure virtual network](/en-us/azure/virtual-network/quick-create-portal) if you don't have one.

## Microsoft Purview private endpoint deployment scenarios

Use the following recommended checklist to perform deployment of Microsoft Purview account with private endpoints:

| Scenario | Objectives |
| --- | --- |
| **Scenario 1** - [Connect to your Microsoft Purview and scan data sources privately and securely](data-gov-classic-private-link-end-to-end) | You need to restrict access to your Microsoft Purview account only via a private endpoint, including access to the classic governance portal, Atlas APIs and scan data sources in on-premises and Azure (but inside a virtual network) using self-hosted integration runtime ensuring end to end network isolation. (Deploy *account*, \_portal, and *ingestion* private endpoints.) |
| **Scenario 2** - [Connect privately and securely to your Microsoft Purview account](data-gov-classic-private-link-account-portal) | You need to enable access to your Microsoft Purview account, including access to *the Microsoft Purview governance portal* and Atlas API through private endpoints. (Deploy *account* and *portal* private endpoints). |
| **Scenario 3** - [Scan data source securely using Managed Virtual Network](data-governance-private-endpoints-managed-virtual-network) | You need to scan Azure data sources securely, without having to manage a virtual network or a self-hosted integration runtime VM. (Deploy managed private endpoints for Microsoft Purview Azure data sources). |
| **Scenario 4** - [Using the new Microsoft Purview portal](data-governance-private-endpoints) | If you're using the [new portal experience](purview-portal), [you can set up ingestion and platform private endpoints.](data-governance-private-endpoints) |

## Frequently Asked Questions

For FAQs related to private endpoint deployments in Microsoft Purview, see [FAQ about Microsoft Purview private endpoints](data-gov-classic-private-link-faq).

## Troubleshooting guide

For troubleshooting private endpoint configuration for Microsoft Purview accounts, see [Troubleshooting private endpoint configuration for Microsoft Purview accounts](data-gov-classic-private-link-troubleshoot).

## Known limitations

To view list of current limitations related to Microsoft Purview private endpoints, see [Microsoft Purview private endpoints known limitations](data-gov-classic-private-link-troubleshoot#known-limitations).