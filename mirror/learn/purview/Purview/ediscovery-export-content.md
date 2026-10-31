---
layout: Conceptual
title: Export and download content from an eDiscovery (Standard) case | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-export-content
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Describes how to export and download content from an eDiscovery (Standard) case in Microsoft 365.
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
- admindeeplinkCOMPLIANCE
- sfi-image-nochange
locale: en-us
document_id: c6905b16-3186-f730-11f0-8447a6e6c0c7
document_version_independent_id: c6905b16-3186-f730-11f0-8447a6e6c0c7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-export-content.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-export-content
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-export-content.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: c9d3baeb-dec1-a373-82da-a72cc623a42e
---

# Export and download content from an eDiscovery (Standard) case | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

After a search associated with a Microsoft Purview eDiscovery (Standard) case is successfully run, you can export the search results. When you export search results, mailbox items are downloaded in PST files or as individual messages. When you export content from SharePoint and OneDrive sites, copies of native Office documents and other documents are exported. A Results.csv file that contains information about every item that's exported and a manifest file (in XML format) that contains information about every search result is also exported.

## Export search results

1. Go to the [Microsoft Purview portal](https://go.microsoft.com/fwlink/p/?linkid=2077149) and sign in using the credentials for user account that has been assigned the appropriate eDiscovery permissions.
2. In the left navigation pane of the Microsoft Purview portal, select **Show all**, and then select **eDiscovery** &gt; [**eDiscovery (Standard)**](https://go.microsoft.com/fwlink/p/?linkid=2174007).
3. On the **eDiscovery (Standard)** page, select the name of the case that you want to create the hold in.
4. On the **Home** page for the case, select the **Searches** tab.
5. On the **Actions** menu at the bottom of the flyout page, select **Export results**.

    ![Export results option in Actions menu.](media/actionmenuexportresults.png)

    The workflow to export the results of a search associated with an eDiscovery (Standard) case is that same as exporting the search results for a search on the **Content search** page. For step-by-step instructions, see [Export content search results](ediscovery-export-search-results).

    Note

    When you export search results, you have the option to enable deduplication so that only one copy of an email message is exported even though multiple instances of the same message might have been found in the mailboxes that were searched.

    After you start the export, the search results are prepared for downloading, which means they're transferred to a Microsoft-provided Azure Storage location in the Microsoft cloud.
6. Select the **Exports** tab in the case to display the list of export jobs.

    ![Export jobs on the Export tab in eDiscovery (Standard) case.](media/coreediscoveryexport.png)

    You may have to select **Refresh** to update the list of export jobs so that it shows the export job you created. Export jobs have the same name as the corresponding search with **\_Export** appended to the search name.
7. Select the export job you created to display status information on the flyout page. This information includes the percentage of items that have been transferred to the Azure Storage location.
8. After all items have been transferred, select **Download results** to download the search results to your local computer. For more information downloading search results, see Step 2 in [Export content search results](ediscovery-export-search-results#step-2-download-the-search-results)

Note

The exported search results must be downloaded within 14 days after you created the export job.

### More information about exporting searches from a case

- If you restart the export, any changes to the queries of the searches that make up the export job won't affect the search results that are retrieved. When you restart an export, the same combined search query job that was run when the export job was created will be run again.
- Also, if you restart an export, the search results that are copied to the Azure Storage location overwrites the previous results. The previous results that were copied won't be available to be downloaded.