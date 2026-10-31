---
layout: Conceptual
title: Advanced indexing in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-ref-advanced-indexing
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about Advanced indexing in eDiscovery.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2025-06-25T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- SPO160
- MOE150
- MET150
ai-usage: ai-assisted
locale: en-us
document_id: f5a4988b-88d1-8142-e993-fe35991cfd01
document_version_independent_id: f5a4988b-88d1-8142-e993-fe35991cfd01
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-ref-advanced-indexing.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-ref-advanced-indexing
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-ref-advanced-indexing.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 205c5043-ea83-79fb-6287-3e1a2f996806
---

# Advanced indexing in eDiscovery | Microsoft Learn

When you add a data source to an eDiscovery case, the system reindexes any content it deems as [partially indexed](edisc-ref-partially-indexed-items) or that has indexing errors. This reindexing process is called *advanced indexing*. Many reasons can cause content to be partially indexed or have indexing errors. These errors might include image files, the presence of images in a file, unsupported file types, or file size indexing limits.

Advanced indexing is available in eDiscovery with premium feature support. The system applies advanced indexing when it runs processes like generating statistics, adding items to review set, and direct export. You don't need to wait for advanced indexing to complete before conducting a search or adding items to a review set like previous versions of eDiscovery. Also, you don't need to manually trigger any update on advanced indexing to ensure newly added content to the target locations need to be reindexed.

Tip

Want to try premium eDiscovery features? See the [subscription requirements](https://aka.ms/M365EnterprisePlans) for Microsoft 365 Enterprise E5 licensing.

For SharePoint files, advanced indexing only runs on items marked as partially indexed or items with indexing errors. In Exchange, email messages with image attachments aren't marked as partially indexed or with indexing errors. This means that those files aren't reindexed by the advanced indexing process.

Note

Optical Character Recognition (OCR) automatically runs during advanced indexing. For more information about how OCR works and to configure OCR related settings, see [Learn about search and analytics settings in eDiscovery cases](edisc-settings-search-analytics#optical-character-recognition-ocr).

## View advanced indexing results

On the [statistics dashboard](edisc-search-results#statistics-dashboard), you can review advanced indexing hits and choose where to apply advanced indexing. You can view estimated hits on how many additional items from partially indexed items that match the search query after they're reindexed with advanced indexing. To ensure full advanced indexing runs on all partially indexed items in scope without sampling, use add to a review set and export with advanced indexing.

You can also review advanced indexed items in [search results](edisc-process-report-use#search-results) in the process report. This report provides details on natively indexed items, partially indexed items, and items identified by advanced indexing.

For more granular insights, you can use the CSV reports. This might include which specific items were exported or which locations were searched. These reports indicate whether an [item](edisc-process-report-use#items-csv-report) was included due to a match with the indexed query or as a result of advanced indexing. The [location report](edisc-process-report-use#locations-csv-report) provides hit counts and data volume per location, broken down by matches to the standard index versus the advanced index.

## Scope advanced indexing

You can scope advanced indexing to partially indexed items in locations where there are already indexed hits, partially indexed items in locations where there aren't any indexed hits, or both.

- **Partially indexed items from locations with indexed hits**: This option is more targeted and limits the scope to only those locations (mailboxes, sites) where some content was successfully indexed and matched the search criteria.

    Choose this option when:

    - You want to reduce noise and focus only on locations already known to be relevant.
    - You're conducting a narrow investigation and want to avoid reviewing irrelevant content.
    - You're optimizing for review efficiency and cost control (for example, in large-scale eDiscovery cases).
    - You want to prioritize the locations and the partially indexed items in locations with high relevancy to the matter first, then later come back to do a more comprehensive analysis that include all locations (including those without indexed hits).
- **Partially indexed items from all locations searched**: This option is more comprehensive and includes partially indexed items from every location searched, regardless of whether any indexed content matched.

    Choose this option when:

    - You need maximum completeness for legal defensibility or regulatory compliance.
    - You're investigating potential data concealment or malicious behavior where relevant content might exist only in unindexed formats (for example, image-based attachments or encrypted files).
    - You're dealing with high-risk scenarios where missing even one critical item could have legal or business consequences.