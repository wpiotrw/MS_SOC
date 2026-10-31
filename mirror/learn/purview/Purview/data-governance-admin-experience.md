---
layout: Conceptual
title: Managing Unified Catalog with the Data Governance Admin Experience | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-admin-experience
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2026-03-29T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to use the Data Governance Administrator experience to manage settings in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 680b8a94-594c-415b-7089-e8633513c87b
document_version_independent_id: 680b8a94-594c-415b-7089-e8633513c87b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-admin-experience.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-admin-experience
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-admin-experience.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: 18aa6329-aa85-ac3a-5ac1-ec1770739da0
---

# Managing Unified Catalog with the Data Governance Admin Experience | Microsoft Learn

In the data governance admin experience, you can manage the data governance settings that apply to Microsoft Purview Unified Catalog in one place. Users who hold the [Data Governance Administrator role](data-governance-roles-permissions#unified-catalog-permissions) can set Unified Catalog roles and permissions, configure self-service analytics (preview), and manage other settings described in this article.

## Prerequisites

To use the data governance admin experience, you need to be in the [tenant-level data governance admin role](data-governance-roles-permissions#unified-catalog-permissions).

## Where to find Unified Catalog solution settings

To use the Data Governance Administrator experience in the [Microsoft Purview portal](https://purview.microsoft.com):

1. In the Microsoft Purview portal, select **Settings**.
2. Under **Solution settings**, select **Unified Catalog**.
3. Select a setting name from the navigation. Each setting is explained in more detail in the following sections.

## Roles and permissions

The roles and permissions item moved from the Unified Catalog solution to the solution settings, but the steps for applying those permissions are still the same. For more information about setting up roles and permissions for your users, see the [data governance permissions documentation](data-governance-roles-permissions).

## Solution integrations for self-serve analytics and insights

The **Solution integrations (preview)** page is where you set up self-service analytics and insights. These insights are data, tools, and platforms that enable business users to access, analyze, and generate insights from data independently by bringing their own tools and compute. For details, see [Self-serve analytics and insights](unified-catalog-self-serve-analytics).

## Usage settings (preview)

Data Governance Administrators can understand and adjust the usage settings available for Unified Catalog in this experience. The Data Health Management SKU can be changed for data quality jobs, and [data quality monitoring](how-to-data-quality-job-monitoring) can be used to monitor and understand the effect on processing. In the rare event of capacity not being available for a higher SKU, a basic SKU is defaulted to. Learn more about [data governance billing](data-governance-billing).

## Usage monitoring (preview)

Note

Usage monitoring is rolling out across regions. If you don't see it yet in your tenant, it will appear in the coming weeks.

The **Usage monitoring** experience is the Data Governance Administrator’s view of [governed assets](data-governance-billing#what-are-governed-assets-and-how-are-you-billed) and [data governance processing unit (DGPU)](data-governance-billing#data-health-management-usage) consumption across different governance domains. This view lets the admin take the overall bill and use the consumption breakdown by governance domains to create a chargeback model in their organization across governed assets and DGPU meters.

The data reported in the charts reflects daily totals. The counts are by each governance domain and aren't aggregated to the parent.

Consumption data is split across governance domains as follows:

- **Governed asset**: Asset used in more than one governance domain split evenly across each domain that uses the asset. This count can show decimals in asset count.
- **Data quality**: Each data quality job maps to a governance domain, not split.
- **Data health management**: Split evenly across all governance domains.

You can use any other advanced split logic through [self-serve analytics](unified-catalog-self-serve-analytics), when all DGPU data is available in self-serve analytics.

Other points to know:

- Cumulative governed assets are the cumulative governed assets for the time period you choose that is used to calculate your bill, not a unique count. For more information, see [how governed assets are billed](data-governance-billing#what-are-governed-assets-and-how-are-you-billed).
- The **Usage monitoring** settings don't show the actual bill; you can find your bill in the Microsoft Azure portal.
- If you rename a governance domain, the previous name shows on the chart for the date on which it changed. The new name shows on the date after the name change.
- When you delete a governance domain, only the GUID shows, not the domain name and owner name.

Tip

Find detailed information about [data governance billing](data-governance-billing) and a [billing FAQ](data-governance-billing-faq).

## Data observability (preview)

[Data observability (preview)](unified-catalog-observability) provides a single view of your data estate to help you understand lineage and data health, and identify improvements in metadata, ownership, data quality, or data architecture. In this area of Unified Catalog settings, admins handle initial setup steps to generate data visualizations. For more information, see [Set up data observability](unified-catalog-observability-setup).

## Virtual network

Data Governance Administrators can provision a virtual network compute location in supported Microsoft Azure regions. Get details at [Manage virtual network provisioning](unified-catalog-data-quality-managed-virtual-networks#manage-virtual-network-provisioning)