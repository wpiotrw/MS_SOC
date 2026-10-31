---
layout: Conceptual
title: Preview the results of an eDiscovery search | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-preview-search-results
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Preview a sample of the results returned by a Content search in the Microsoft Purview portal.
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
- MED150
- MET150
ms.custom:
- seo-marvel-apr2020
- sfi-image-nochange
locale: en-us
document_id: 1d5991ea-a59f-bc77-5614-5b97a47e370b
document_version_independent_id: 1d5991ea-a59f-bc77-5614-5b97a47e370b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-preview-search-results.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-preview-search-results
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-preview-search-results.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: a3077993-9125-217a-2f18-4aae981eb645
---

# Preview the results of an eDiscovery search | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

After you run a Content search, you can preview a sample of the results returned by the search. Previewing items returned by the search query can help you determine if the search is returning the results you hope for or if you need to change the search query and rerun the search.

Note

There may be scenarios when the preview sample doesn’t contain all available results of searches, and sampling is best effort. In some cases (such as in environments operated by 21Vianet in China), the review sample might not function reliably. For the most accurate and complete search results, use [export](ediscovery-export-search-results) to obtain the full set of search results.

To preview a sample of results returned by a search:

1. In the [Microsoft Purview portal](https://compliance.microsoft.com), go to the **Content search**.
2. Select search to display the flyout page.
3. On the bottom of the flyout page, select **Review sample**.

    ![Select Review sample on the flyout page to preview results.](media/previewsearchresults1.png)

    A page is displayed containing a sample of the search results.
4. Select an item to view its contents in the reading pane.

    ![Preview items in the reading pane.](media/previewsearchresults2.png)

    In the previous screenshot, the keywords from the search query are highlighted when you preview items.

## How the search result samples are selected

A maximum of 1,000 randomly selected items are available to preview. In addition to being randomly selected, items available for preview must also meet the following criteria:

- A maximum of 100 items from a single content location (a mailbox or a site) can be previewed. This maximum means that it's possible that less than 1,000 items might be available for preview. For example, if you search four mailboxes and the search returns 1,500 estimated items, only 400 are available for preview because only 100 items from each mailbox can be previewed.
- For mailbox items, only email messages are available to preview. Preview for items like tasks, calendar items, and contacts aren't available.
- For site items, only documents are available to preview. Preview for items like folders, lists, or list attachments aren't available.

## File types supported when previewing search results

You can preview supported file types in the preview pane. If a file type isn't supported, you have to download a copy of the file to your local computer (by selecting **Download original item**). For .aspx Web pages, the URL for the page is included though you may not have permissions to access the page. Unindexed items aren't available for previewing.

The following file types are supported and can be previewed in the search results pane.

- .txt, .html, .mhtml
- .eml
- .doc, .docx, .docm
- .pptm, .pptx
- .pdf

Also, the following file container types are supported. You can view the list of files in the container in the preview pane.

- .zip
- .gzip