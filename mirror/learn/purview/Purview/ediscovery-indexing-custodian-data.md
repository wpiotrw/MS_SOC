---
layout: Conceptual
title: Advanced indexing of custodian and noncustodial data sources | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-indexing-custodian-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: When a custodian or noncustodial data source is added to an eDiscovery (Premium) case, any content that was deemed as partially indexed is reprocessed to make it fully searchable.
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
locale: en-us
document_id: ac87f0fd-36fd-60f4-4399-c80ca1cd2728
document_version_independent_id: ac87f0fd-36fd-60f4-4399-c80ca1cd2728
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-indexing-custodian-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-indexing-custodian-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-indexing-custodian-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 6ffa0c5c-d19d-c67f-ae92-79888738e7df
---

# Advanced indexing of custodian and noncustodial data sources | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

When a custodian or noncustodial data source is added to an eDiscovery (Premium) case, any content that was deemed as partially indexed or had indexing errors is reindexed. The reindexing process is called *Advanced indexing*. There are many reasons that content is partially indexed or has indexing errors. This includes image files or the presence of images in a file, unsupported file types, or file sized indexing limits.

For SharePoint files, Advanced indexing only runs on items marked as partially indexed or items with indexing errors. In Exchange, email messages with image attachments aren't marked as partially indexed or with indexing errors. This means that those files won't be reindexed by the Advanced indexing process.

To learn more about processing support and partially indexed items, see:

- [Supported file types in eDiscovery (Premium)](ediscovery-supported-file-types)
- [Partially indexed items in eDiscovery](ediscovery-partially-indexed-items-in-content-search)
- [File formats indexed by Exchange Search](/en-us/exchange/file-formats-indexed-by-exchange-search-exchange-2013-help)
- [Default crawled file name extensions and parsed file types in SharePoint Server](/en-us/SharePoint/technical-reference/default-crawled-file-name-extensions-and-parsed-file-types)

## Viewing Advanced indexing results

After the Advanced indexing process is completed, you can get an understanding of the effectiveness of reprocessing. In the Advanced indexing results view on the **Processing** tab for a case, the graph lists the number of items added to the *hybrid index*. The hybrid index is where eDiscovery (Premium) stores the reprocessed content.

This view also includes the number of items that require remediation and another graph of errors by file type. For more information, see:

- [Error remediation when processing data](ediscovery-error-remediation-when-processing-data)
- [Single item error remediation](ediscovery-single-item-error-remediation)

## Updating the Advanced index

When a custodian or noncustodial data source is added to an eDiscovery (Premium) case, all partially indexed items are reprocessed. However, as time passes, more partially indexed items may be added to a user's mailbox or OneDrive account. If necessary, you can update the index for specific custodian or noncustodial data source. For more information, see [Manage custodians in an eDiscovery (Premium) case](ediscovery-manage-new-custodians#reindex-custodian-data). You can also update the index for all custodians and noncustodial data sources in a case by selecting the **Update index** on the **Processing** tab.

Note

Updating custodian and noncustodial indexes is a long running process. It's recommended that you don't update indexes more than once a day in a case.