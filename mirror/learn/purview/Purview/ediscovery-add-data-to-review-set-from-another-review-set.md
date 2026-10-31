---
layout: Conceptual
title: Add data from one review set to another | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-add-data-to-review-set-from-another-review-set
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to select documents from one review set and work with them individually in another set in a Microsoft Purview eDiscovery (Premium) case.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
ms.custom:
- seo-marvel-mar2020
- seo-marvel-apr2020
locale: en-us
document_id: db52d8b3-333b-1c5d-e512-68c5e6654044
document_version_independent_id: db52d8b3-333b-1c5d-e512-68c5e6654044
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-add-data-to-review-set-from-another-review-set.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-add-data-to-review-set-from-another-review-set
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-add-data-to-review-set-from-another-review-set.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: fc10d363-a343-4b86-9952-9b849fc8471d
---

# Add data from one review set to another | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

In some cases, it may be necessary to select documents from one review set and work with them individually in another review set. This is especially useful if you've culled content in a review set and want to run analytics on the subset of data.

Follow the workflow in this article to add content from one review set to another.

## Create a review set

Before you start, you'll need to create a review set to add the data to. A new review set can be added on the **Review sets** tab of the case. For more information, see [Create a review set](ediscovery-managing-review-sets#create-a-review-set).

## Step 1: Identify content to add to another review set

You can add content from one review set to another one by selecting specific documents in the source review set or by selecting all items returned by review set query. If you're adding selected items, select the items, select **Action**, and then select **Add to another review set**.

![Add to another review set in the Action menu.](media/64f2a4d4-eba3-4ab3-a3ba-d519feea3142.png)

## Step 2: Specify options for adding to another review set

In the **Add to another review set options** flyout page, choose the review set you want to add the items to. Choose whether to add **All search results** or **Selected items**. **Additional information** provides options to include all metadata from the items and whether to include the tags (by selecting the **Labels** check box) from the source review set when the documents are added to the new review set.

![Options for adding data to another review set.](media/6440ee44-68fd-44d7-b43a-3a477345525c.png)

After you select **Ok**, a new job (named **Adding data to another review set**) is created to add the content to another review set. You can go to the **Jobs** tab and monitor the progress of this job. For more information, see [Manage jobs](ediscovery-managing-jobs).