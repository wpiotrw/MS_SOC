---
layout: Conceptual
title: Add items from a review set to another review set in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-review-set-add-to-other-review-set
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to select items from one review set and work with them individually in another review set in eDiscovery.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-19T00:00:00.0000000Z
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
f1.keywords:
- NOCSH
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 010b763f-779d-14e8-a7d5-d7fb5f52b032
document_version_independent_id: 010b763f-779d-14e8-a7d5-d7fb5f52b032
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-review-set-add-to-other-review-set.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-review-set-add-to-other-review-set
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-review-set-add-to-other-review-set.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 9594978b-fb89-e174-a3e1-b0c329fd19b4
---

# Add items from a review set to another review set in eDiscovery | Microsoft Learn

In some cases, you might need to select documents from one review set and work with them individually in another review set. This approach is especially useful if you culled content in a review set and want to run analytics on the subset of data.

Follow the workflow in this article to add content from one review set to another.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Create a review set

Before you start, you need to create a review set to add the data to. You can add a new review set on the **Review sets** tab of the case. For more information, see [Create a review set](edisc-review-set-manage).

## Step 1: Identify content to add to another review set

You can add content from one review set to another review set by selecting specific documents in the source review set or by selecting all items returned by a [review set query](edisc-review-set-search), which filters items based on search criteria you define. If you're adding selected items, select the items, select **Action**, and then select **Add to another review set**.

## Step 2: Specify options for adding to another review set

In the **Add to another review set** flyout, complete the following steps:

1. Select the review set you want to add the items to.
2. Choose from the following content options:

    - **Selected documents only**
    - **All filtered documents**
    - **All documents in the review set**
3. In the **Additional information** section, select options to include all metadata (by selecting the **Metadata** check box) from the items and whether to include the tags (by selecting the **Tags** check box) from the source review set when the documents are added to the new review set.
4. After you select **OK**, a new process named **Adding data to another review set** is created to add the content to another review set. You can go to the **Process manager** in the new review set to monitor the progress of this process.