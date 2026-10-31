---
layout: Conceptual
title: Work with processing errors in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-processing-data-for-case
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Overview about processing various forms of data in eDiscovery (Premium).
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: overview
ms.service: purview
ms.subservice: purview-ediscovery
search.appverid:
- MOE150
- MET150
ms.custom:
- seo-marvel-apr2020
ms.collection:
- purview-compliance
- ediscovery
locale: en-us
document_id: 9cfdd7ee-9d9c-51fa-1774-c13751dd039a
document_version_independent_id: 9cfdd7ee-9d9c-51fa-1774-c13751dd039a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-processing-data-for-case.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-processing-data-for-case
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-processing-data-for-case.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/97159432-14a9-4307-a469-d2f2c75f0e33
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/50565c62-5f6b-4687-be38-323113c72c2e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 4b2ff18a-ab15-65be-d2af-6a0742dace89
---

# Work with processing errors in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

*Processing* is the process of file identification, expansion of embedded documents and attachments, text extraction, and Optical Character Recognition (OCR) of image files and the subsequent indexing of that content.

When you add custodians and non-custodian data sources to a case on the **Sources** tab, all partially indexed items from Microsoft 365 are processed to make them fully searchable. Likewise, when content is added to a review set from both Microsoft 365 and non-Microsoft 365 data sources, this content is also processed.

The **Processing** tab in eDiscovery (Premium) provides insight into the status of Advanced indexing for different processing scenarios.

For more information, see the following articles:

- [Advanced indexing of custodian data](ediscovery-indexing-custodian-data)
- [Error remediation when processing data](ediscovery-error-remediation-when-processing-data)
- [Single item error remediation](ediscovery-single-item-error-remediation)