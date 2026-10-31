---
layout: Conceptual
title: Create and manage an eDiscovery (Premium) case | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-create-and-manage-cases
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article describes how to create and manage Microsoft Purview eDiscovery (Premium) cases. The first step is to create a case and start using eDiscovery (Premium) features and functionality.
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
- m365solution-aed
- m365solution-scenario
- highpri
- ediscovery
ms.custom:
- admindeeplinkCOMPLIANCE
- sfi-image-nochange
search.appverid:
- MOE150
- MET150
locale: en-us
document_id: c7a581f0-66c3-52aa-5769-d7e988be92f2
document_version_independent_id: c7a581f0-66c3-52aa-5769-d7e988be92f2
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-create-and-manage-cases.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-create-and-manage-cases
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-create-and-manage-cases.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 5d086462-3982-bf59-6afd-ef67be21a514
---

# Create and manage an eDiscovery (Premium) case | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

After setting up Microsoft Purview eDiscovery (Premium) and [assigning permissions to eDiscovery managers](ediscovery-premium-get-started#step-2-assign-ediscovery-permissions) in your organization that will manage cases, the next step is to create and manage a case.

This article also provides a high-level overview of using cases to manage the eDiscovery (Premium) workflow for a legal case or other types of investigations.

## Create a case

Complete the following steps to create a case and configure case settings. The user who creates the case is automatically added as a member. Members of the case can access the case in the Microsoft Purview portal and perform eDiscovery (Premium) tasks.

1. Go to the [Microsoft Purview portal](https://go.microsoft.com/fwlink/p/?linkid=2077149) and sign in using the credentials for user account that has been assigned eDiscovery permissions. Members of the *Organization Management* role group can also create eDiscovery (Premium) cases.
2. In the left navigation pane of the Microsoft Purview portal, select **Show all**, and then select **eDiscovery** &gt; **Premium**, and then select the [**Cases**](https://go.microsoft.com/fwlink/p/?linkid=2173764)tab.
3. Select **Create a case**.
4. On the **Name and description** page, complete the following fields:

    - **Name**: give the case a name (required). The case name must be unique in your organization
    - **Description**: Add an optional description to help others understand this case.
    - **Number**: Enter an optional docket number or other numeric identifier.
    - **Case format**: The **New (recommended)** option is automatically selected.

    Note

    The legacy **Classic** format is no longer available when creating new cases. This format is now retired for all new cases.
5. Select **Next**.
6. On the **Members and settings** page, complete the following fields as applicable:

    - **Team members**: Select users and groups that should be assigned to the case. Make sure that users and groups assigned here have been [assigned the appropriate eDiscovery permissions](ediscovery-assign-permissions).
    - **Search and analytics**: Select the options to configure the case. You can skip this section and configure these settings after the case is created if needed.
    - **Text to ignore**: Add text or regex expressions to define text to ignore in the case. You can apply this to *Near-duplicates*, *Email threads*, or *Themes* modules.
    - **Optical character recognition (OCR)**: Configure the option and settings for finding text contained in images during advanced indexing.
7. Select **Next**.
8. On the **Summary** page, review the settings for the case and edit the settings if needed. Select **Submit** to create the new case and start your investigation.

## Mark a case as a favorite

You can mark an eDiscovery (Premium) case as a favorite for quicker access to cases you want to prioritize. Cases marked as favorites can be accessed quickly via the eDiscovery (Premium) **Overview** page or can be sorted to be shown at the top of the **Cases** tab for ease of access. You can mark a case as a favorite in the case list on the **Cases** tab or on the top right of the case **Overview** tab for each case. The **Recent favorite cases** card on the **Overview** tab displays all the cases marked as favorites in your organization.

![eDiscovery (Premium) favorite case list.](media/ediscovery-case-favorite.png)

## Manage the workflow

To get you started using eDiscovery (Premium), here's a basic workflow that aligns with [common eDiscovery practices](ediscovery-overview). In each of these steps, we'll also highlight some extended eDiscovery (Premium) functionality that you can explore. ediscovery-overview

![eDiscovery (Premium) workflow.](media/aedworkflow.png)

1. **[Add custodians](ediscovery-add-custodians-to-case) and [non-custodial data sources](ediscovery-non-custodial-data-sources) to the case**. The first step after creating a case is to add custodians. A *custodian* is a person having administrative control of a document or electronic file that may be relevant to the case. Additionally, you can add data sources that aren't associated with a specific user but may be relevant to the case. These are *non-custodial data sources*.

    Here are some things that happen (or that you can do) when you add custodians to a case:

    - Data in the custodian's Exchange mailbox, OneDrive account, and any Microsoft Teams or Viva Engage groups that the custodian is a member of can be "marked" as custodial data in the case.
    - Custodian (and non-custodial) data is reindexed (by a process called *Advanced indexing*). This helps optimize searching for it in the next step.
    - You can place a hold on custodian and non-custodial data. This hold preserves data that may be relevant to the case during the investigation. To learn more about managing holds, see [Manage holds in eDiscovery (Premium)](ediscovery-managing-holds).
    - You can associate other data sources with a custodian (for example, you can associate a SharePoint site or Microsoft 365 Group with a custodian) so this data can be reindexed, placed on hold, and searched, just like the data in the custodian's mailbox or OneDrive account.
    - You can use the [communications workflow](ediscovery-managing-custodian-communications) in eDiscovery (Premium) to send a legal hold notification to custodians.
2. **[Collect relevant content from data sources](ediscovery-create-draft-collection)**. After you add custodians and non-custodial data sources to a case, use the built-in collections tool to search these data sources for content that may be relevant to the case. You use keywords, properties, and conditions to [build search queries](ediscovery-building-search-queries) that return search results with the data that's most likely relevant to the case. You can also:

    - View [collection statistics](ediscovery-collection-statistics-reports) that may help you refine a collection to narrow the results.
    - Preview a sample of the collection to quickly verify whether the relevant data is being found.
    - Revise a query and rerun the collection.
3. **[Commit collection to a review set](ediscovery-commit-draft-collection)**. Once you've configured and verified that a search returns the desired data, the next step is to add the search results to a review set. When you add data to a review set, items are copied from their original location to a secure Azure Storage location. The data is reindexed again to optimize it for thorough and fast searches when reviewing and analyzing items in the review set. Additionally, you can also [add non-Office 365 data into a review set](ediscovery-load-non-office-365-data-into-a-review-set).

    There's also a special kind of review set that you can add data to, called a *conversation review set*. These types of reviews sets provide conversation reconstruction capabilities to reconstruct, review, and export threaded conversations like those in Microsoft Teams. For more information, see [Review conversations in eDiscovery (Premium)](ediscovery-conversation-review-sets).
4. **Review and analyze data in a review set**. Now that data is in a review set, you can use a wide-variety of tools and capabilities to view and analyze the case data with the goal of reducing the data set to what is most relevant to the case you're investigating. Here's a list of some tools and capabilities that you can use during this process.

    - [Group and view documents](ediscovery-view-documents-in-review-set). This includes selecting the group options for review sets in your cases, viewing the metadata for each document in a review set, and viewing the document in its native version or text version.
    - [Create queries and filters](ediscovery-review-set-search). You create search queries using various search criteria (including the ability to search all [file metadata properties](ediscovery-document-metadata-fields) to further refine and cull the case data to what is most relevant to the case. You can also use review set filters to quickly apply other conditions to the results of a search query to further refine those results.
    - [Create and use tags](ediscovery-tagging-documents). You can apply tags to documents in a review set to identify which are responsive (or non-responsive to the case) and then use those tags when creating search queries to include or exclude the tagged documents. You can also tagging to determine which documents to export.
    - [Annotate and redact documents](ediscovery-view-documents-in-review-set#annotate-view). You can use the annotation tool in a review to annotate documents and redact content in documents as work product. We generate a PDF version of an annotated or redacted document during review to reduce the risk of exporting the unredacted native version of the document.
    - [Analyze case data](ediscovery-analyzing-data-in-review-set). The analytics functionality in eDiscovery (Premium) is powerful. After you run analytics on the data in review set, we perform analysis such as near duplicate detection, email threading, and themes that can help reduce the volume of documents that you have to review. We also generate an Analytics reports that summarize the result of running analytics. As previously explained, running analytics also runs [the attorney-client privilege detection model](ediscovery-attorney-privilege-detection#use-the-attorney-client-privilege-detection-model).
5. **Export and download case data**. A final step after collecting, reviewing, and analyzing case data is to export it out of eDiscovery (Premium) for external review or for review by people outside of the investigation team. Exporting data is a two-step process. The first step is to [export](ediscovery-export-documents-from-review-set) data out of the review set and copy it to a different Azure Storage location (one provided by Microsoft or one managed by your organization). Then you use Azure Storage Explorer to [download](ediscovery-download-export-jobs) the data to a local computer. In addition to the exported data files, the contains of the export package also contains an export report, a summary report, and an error report.

## eDiscovery (Premium) architecture

Here's an architecture diagram that shows the eDiscovery (Premium) end-to-end workflow in a single-geo environment and in a multi-geo environment, and the end-to-end data flow that's aligned with the [Electronic Discovery Reference Model](ediscovery-overview#ediscovery-premium-alignment-with-the-electronic-discovery-reference-model).

[![Model poster: eDiscovery (Premium) Architecture in Microsoft 365.](media/solutions-architecture-center/ediscovery-poster-thumb.png)](media/solutions-architecture-center/m365-advanced-ediscovery-architecture.png)

[View as an image](media/solutions-architecture-center/m365-advanced-ediscovery-architecture.png)

[Download as a PDF file](https://download.microsoft.com/download/d/1/c/d1ce536d-9bcf-4d31-b75b-fcf0dc560665/m365-advanced-ediscovery-architecture.pdf)

[Download as a Visio file](https://download.microsoft.com/download/d/1/c/d1ce536d-9bcf-4d31-b75b-fcf0dc560665/m365-advanced-ediscovery-architecture.vsdx)