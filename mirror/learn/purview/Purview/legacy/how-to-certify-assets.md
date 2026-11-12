---
layout: Conceptual
title: Asset certification in the Microsoft Purview Data Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-certify-assets
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: How to certify assets in the Microsoft Purview Data Catalog
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: nayenama
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: how-to
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
locale: en-us
document_id: 8d4fc14f-1333-381d-1aba-abed23a23bbd
document_version_independent_id: 8d4fc14f-1333-381d-1aba-abed23a23bbd
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-certify-assets.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-certify-assets
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-certify-assets.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/3f837592-9b7c-422c-82fa-3523042264d7
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/f37b967c-efb8-47e1-9b0d-0ab7670e3db4
platformId: f1187c3c-d77e-0c0e-c9bf-ae9feeefb8f0
---

# Asset certification in the Microsoft Purview Data Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

As a Microsoft Purview Data Catalog grows in size, it becomes important for data consumers to understand what assets they can trust. Data consumers must know if an asset meet their organization's quality standards and can be regarded as reliable. Microsoft Purview allows data stewards to manually endorse assets to indicate that they're ready to use across an organization or business unit. This article describes how data stewards can certify assets and data consumers can view certification labels.

## How to certify an asset

To certify an asset, you must be a **data curator** for the collection containing the asset. For steps to assign this role, [see our permissions documentation](../data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).

1. Navigate to the [asset details]classic-catalog-asset-details.md) of the desired asset. Select **Edit**.

    ![Edit an asset from the asset details page](../media/how-to-certify-assets/edit-asset.png)
2. Toggle the **Certified** field to **Yes**.

    ![Toggle an asset to be certified](../media/how-to-certify-assets/toggle-certification-on.png)
3. Save your changes. The asset has a "Certified" label next to the asset name.

    ![An asset with a certified label](../media/how-to-certify-assets/view-certified-asset.png)

Note

PowerBI assets can only be [certified in a PowerBI workspace](/en-us/power-bi/collaborate-share/service-endorse-content). PowerBI endorsement labels are displayed in Microsoft Purview's search and browse experiences.

### Certify assets in bulk

You can use the Microsoft Purview [bulk edit experience](../how-to-bulk-edit-assets) to certify multiple assets at once.

1. After searching or browsing the data catalog, select checkbox next to the assets you wish to certify.

    ![Select assets to bulk certify](../media/how-to-certify-assets/bulk-edit-select.png)
2. Select **View selected**.
3. Select **Bulk edit**

    ![Open the bulk edit experience](../media/how-to-certify-assets/bulk-edit-open.png)
4. Choose attribute **Certified**, operation **Replace with**, and new value **Yes**.

    ![Apply certification labels to all selected assets](../media/how-to-certify-assets/bulk-edit-certify.png)
5. Select **Apply**

All assets selected have the "Certified" label.

## Viewing certification labels in Search

When search or browsing the data catalog, you see a certification label on any asset that is certified. Certified assets boosted in search results to help data consumers discover them easily.

![Search results with certified assets](../media/how-to-certify-assets/search-certified-assets.png)