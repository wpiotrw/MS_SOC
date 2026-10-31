---
layout: Conceptual
title: New case format in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-new-case-format
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use the new case format in eDiscovery (Premium) so you can add more items to review sets and take advantage of other increased limits and new functionality.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
ms.reviewer: ninachen
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
manager: laurawi
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
document_id: 5ecdd280-ebea-2658-3972-cc1ae2975fd6
document_version_independent_id: 5ecdd280-ebea-2658-3972-cc1ae2975fd6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-new-case-format.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-new-case-format
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-new-case-format.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e4f48d48-dfb7-4973-a019-e504674667cb
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/495840e0-c52f-49d2-a584-185aefeb98c7
platformId: 77a336f8-f4a8-69e5-b8e8-057829802983
---

# New case format in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

More organizations are using the eDiscovery (Premium) solution in Microsoft Purview for critical eDiscovery processes. This includes responding to regulatory requests, investigations, and litigation. As usage of eDiscovery (Premium) increases, a common customer requirement is to expand the total amount of content that can be managed in a single eDiscovery (Premium) case. To help accommodate significant increases in case size, both for total data volume and the total number of items, you can choose the new case format when you create an eDiscovery (Premium) case.

## Benefits of the new case format

The new case format allows you to manage cases that contain over 40 million items. This capability helps you effectively manage large volumes of case data through the entire eDiscovery workflow.

Here's a list of other benefits of large cases in eDiscovery (Premium) workflow.

- **Collection**: In the new case format, you can collect up to 1 TB of data for a single collection.

    For each case, the collection settings will default to collect cloud Attachments and contextual Teams and Viva Engage content. These settings help to collect the full picture of digital communications within an investigation. For Teams and Viva Engage contextual conversations, the new case format will convert time-based snapshots of 1:1, 1: N and Channel conversations into HTML transcripts to help provide context of conversations and reduce the total number of items produced by chat-based content.
- **Review**: Each review set will support up to 1 TB of pre-expansion content. Additional metadata will be available for filters and queries including Team name, channel name and conversation name for Teams content. Each transcript will include time-based content for before and after the responsive item. For Channel conversations, the root post and all replies will be collected for responsive content. For more information, see [eDiscovery (Premium) workflow for content in Microsoft Teams](ediscovery-teams-workflow)
- **Export**: You can export large sets of content in a single export job. The new case format lets you can export 5 million documents or 500 GB, whichever is smaller in an export job.

Additionally, the new case format includes an updated user interface that displays the total size of each review set in the case. Review set sizes are displayed in a column on the **Review sets** tab.

![New review set statistics in eDiscovery (Premium) user interface.](media/largecaseui.png)

## Create a case in the new format

To create an eDiscovery (Premium) case using the new case format, complete the following steps:

1. Go to https://compliance.microsoft.com and sign in.
2. In the left navigation pane of the Microsoft Purview portal, select **eDiscovery &gt; Premium**.
3. On the **eDiscovery (Premium)** page, select the **Cases** tab, and then select **Create a case**.

    The **New eDiscovery case** flyout page is displayed. The **Case format** section on the **Name and description** page provides the option to create a case using the *New (recommended)* or *Classic* format.

    ![New case format option on the New eDiscovery case page.](media/ediscovery-new-case-format-option.png)
4. After naming the case, select the **New (recommended)** option, and then select **Next** to continue in the new case workflow to finish creating your case.

After you've created your case, the case format information is displayed on the **Case format** card on the case **Overview** tab and in the **Case format** section on the case settings page for each case.

## Frequently asked questions

**If I attempt to collect over 1 TB in a single collection, will it work?**

The performance will be negatively impacted and may cause instability in some instances.

**If cloud attachments are included by default in the large case format; how can I remove that content from my review experience?**

Use review set filters to filter by message kind or to exclude cloud attachments by using the HasAttachment filter. For more information, see [Query and filter content in a review set](ediscovery-review-set-search).

**When exporting chat conversation transcripts, will the load file contain all of the expanded metadata and a single item for each transcript?**

All metadata for a conversation is embedded in the HTML transcript file. Many of the common fields are available in the load file. For more information about exported metadata, see [Document metadata fields in eDiscovery (Premium)](ediscovery-document-metadata-fields).