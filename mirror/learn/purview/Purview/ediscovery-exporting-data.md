---
layout: Conceptual
title: Export case data in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-exporting-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to export or download content from a review set for presentations or external reviews in an eDiscovery (Premium) case.
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
document_id: 0a60de05-331a-16ed-b617-64cc6d78e3ed
document_version_independent_id: 0a60de05-331a-16ed-b617-64cc6d78e3ed
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-exporting-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-exporting-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-exporting-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: a1b84be9-1e84-7367-733a-bfdc24d1b98b
---

# Export case data in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

There are three ways to export data from a review set:

**Download:** Download (by using a browser) a small set of native files. This is the quickest way to export a small set of data. This method preserves the native file names. For more information, see [Download documents from a review set](ediscovery-download-documents-from-review-set).

**Export:** Customize what data is exported. This includes exporting file metadata, native files, text files, and redacted documents that have been saved to a PDF file. Once the exported data is prepared, you can download the data from the **Export** tab to a local computer. For more information, see [Export documents from a review set](ediscovery-export-documents-from-review-set)

**Add to another review set:** Copy data from one review set to a different review set. For more information, see [Add data from one review set to another review set](ediscovery-add-data-to-review-set-from-another-review-set).

Note

In Microsoft 365, data is hashed and those hashes are provided in the output file for verification purposes. This is supplemented by audit logs and reporting functionality, such as collection statistics, load set reports, and export reports (including the export load file).