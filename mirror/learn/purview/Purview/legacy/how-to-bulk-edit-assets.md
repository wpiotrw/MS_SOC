---
layout: Conceptual
title: How to bulk edit assets | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-bulk-edit-assets
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn bulk edit assets in Microsoft Purview to add classifications, glossary terms, and modify contacts on multiple assets at once.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: nayenama
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: how-to
ms.date: 2025-02-26T00:00:00.0000000Z
locale: en-us
document_id: 57b8f8eb-e71a-a226-113f-9202550e324e
document_version_independent_id: 57b8f8eb-e71a-a226-113f-9202550e324e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-bulk-edit-assets.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-bulk-edit-assets
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-bulk-edit-assets.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 91073aab-f95b-00a0-8d1a-e9969d30da07
---

# How to bulk edit assets | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

This article describes how you can update assets in bulk to add glossary terms, classifications, owners, and experts on multiple assets at once.

Note

Bulk editing as described here is for data assets. Other assets like classifications and glossary terms can't be added to the bulk edit list.

## Select assets to bulk edit

1. Use Microsoft Purview search or browse to discover assets you wish to edit.
2. In the search results, each data asset has a checkbox you can select to add the asset to the selection list.

    ![Screenshot of the bulk edit checkbox.](../media/how-to-bulk-edit-assets/asset-checkbox.png)
3. You can also add an asset to the bulk edit list from the asset detail page. Select **Select for bulk edit** to add the asset to the bulk edit list.

    ![Screenshot of the asset page with the bulk edit box highlighted.](../media/how-to-bulk-edit-assets/asset-list.png)
4. Select the checkbox to add it to the bulk edit list. You can see the selected assets by selecting the **View selected** button.

    ![Screenshot of the asset list with the View Selected button highlighted.](../media/how-to-bulk-edit-assets/selected-list.png)

## Bulk edit assets

1. When all assets have been chosen, select **View selected** to pull up the selected assets.

    ![Screenshot of the view.](../media/how-to-bulk-edit-assets/view-list.png)
2. Review the list and select **Deselect** if you want to remove any assets from the list.

    ![Screenshot with the Deselect button highlighted.](../media/how-to-bulk-edit-assets/remove-list.png)
3. Select **Bulk edit** to add, remove, or replace an annotation for all the selected assets. You can edit the glossary terms, classifications, owners, or experts of an asset.

    ![Screenshot with the bulk edit button highlighted.](../media/how-to-bulk-edit-assets/bulk-edit.png)
4. For each attribute selected, you can choose which edit operation to apply

    1. **Add** will append a new annotation to the selected data assets.
    2. **Replace with** will replace all of the annotations for the selected data assets with the annotation selected.
    3. **Remove** will remove all annotations for selected data assets.

    You can edit multiple assets at once by selecting **Select a new attribute**.

    ![Screenshot of the add.](../media/how-to-bulk-edit-assets/add-list.png)
5. When you have made all your updates, select **Apply**.
6. Once complete, close the bulk edit blade by selecting **Close** or **Remove all and close**. Close won't remove the selected assets whereas remove all and close will remove all the selected assets. ![Screenshot of the close.](../media/how-to-bulk-edit-assets/close-list.png)

Important

In the UI you can currently only select up to 25 assets. The **View Selected** box will be visible only if there is at least one asset selected.