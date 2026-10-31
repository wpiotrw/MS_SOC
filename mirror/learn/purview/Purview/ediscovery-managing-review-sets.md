---
layout: Conceptual
title: Manage review sets in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-managing-review-sets
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to manage review sets so you can analyze, query, view, tag, and export data in an eDiscovery (Premium) case.
ms.custom: seo-marvel-mar2020
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
locale: en-us
document_id: a31b8548-51c9-a684-ab49-a8f1acba31e8
document_version_independent_id: a31b8548-51c9-a684-ab49-a8f1acba31e8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-managing-review-sets.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-managing-review-sets
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-managing-review-sets.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: a60e7118-c45a-cfcc-e092-0cebda0b6be7
---

# Manage review sets in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Review sets are a static set of documents where you can analyze, query, view, tag, and export data in a case. For more information about performing these tasks, see:

- [Analyze data in a review set](ediscovery-analyzing-data-in-review-set)
- [Query the data in a review set](ediscovery-review-set-search)
- [View documents in a review set](ediscovery-view-documents-in-review-set)
- [Tag documents in a review set](ediscovery-tagging-documents)
- [Export case data](ediscovery-exporting-data)

## Create a review set

Review sets can be created on the **Review sets** tab by selecting **+ Add review set**.

![Add review set.](media/f45c51d9-585d-47d1-b7fb-0288715e0b6a.png)

On the **Add review set** flyout page, type a name for the review set and then select **Save**. The new review set is displayed in the list on the **Review sets** tab.

![New review set listed on Review set tab.](media/aednewreviewset.png)

There are three different ways to add data to a review set in an eDiscovery (Premium) case.

![Three ways to add to a review sets.](media/1f1f4efd-c03b-4255-bc3d-df358e56549c.png)

1. [Add search results to a review set](ediscovery-add-data-to-review-set)
2. [Load non-Microsoft 365 data into a review set](ediscovery-load-non-office-365-data-into-a-review-set)
3. [Add data to a review set from another review set](ediscovery-add-data-to-review-set-from-another-review-set)

Note

You can't delete items from a review set and you can't delete review sets from a case. To delete a review set (and delete the data in it), you have to delete the eDiscovery (Premium) case the review set is located in. For more information, see [Close or delete an eDiscovery (Premium) case](ediscovery-close-or-delete-case).