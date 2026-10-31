---
layout: Conceptual
title: Download documents from a review set | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-download-documents-from-review-set
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to select and download content from a review set in eDiscovery (Premium) for presentations or external reviews.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
ms.custom: seo-marvel-mar2020
locale: en-us
document_id: 3ff477eb-7ae8-f1c7-a3e0-6c96bf410f41
document_version_independent_id: 3ff477eb-7ae8-f1c7-a3e0-6c96bf410f41
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-download-documents-from-review-set.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-download-documents-from-review-set
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-download-documents-from-review-set.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/60932d05-feee-4685-a73b-595e25dd9318
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/c43bb58b-1190-419b-8d18-e6052371b599
platformId: cbc32d4d-8145-49f8-143c-b8eaa77e2739
---

# Download documents from a review set | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Download offers a simple way to download content from a review set in native format. The download tool in eDiscovery (Premium) uses the browser's data transfer features. A browser prompt appears when a download is ready.

Files downloaded using this method are zipped in a container file, and this file contains item-level files. It means that if you select to download an attachment, you receive the email message with the attachment included. Similarly, if you export an Excel spreadsheet that is embedded in a Word document, the Word document and the embedded Excel spreadsheet are included in the download.

When you download items, the *Last Modified Data* property is preserved and can be viewed as a file property.

Important

Downloading an item from a review set does not preserve the item metadata. Item metadata is only preserved when exporting items from a review set.

To download a review set item from a review set in an eDiscovery (Premium) case, start by selecting the item you want to download and select **Download original** from the item menu.

Important

To download original items from a review set, you must be assigned the *Export* role or be assigned to a role group that includes the *Export* role. For more information about eDiscovery permissions, see [Assign eDiscovery permissions in the Microsoft Purview portal](ediscovery-assign-permissions#rbac-roles-related-to-ediscovery).

To download multiple items from a review set at the same time, select the items you want to download then export the selected documents from the review set.