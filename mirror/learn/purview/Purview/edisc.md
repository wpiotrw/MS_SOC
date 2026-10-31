---
layout: Conceptual
title: Learn about eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about eDiscovery features and capabilities in the Microsoft Purview portal.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-29T00:00:00.0000000Z
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
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: 408ce8e8-e042-e173-0798-b66072572279
document_version_independent_id: 408ce8e8-e042-e173-0798-b66072572279
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: b45f43f8-d570-49e2-8178-f514407d017f
---

# Learn about eDiscovery | Microsoft Learn

Electronic discovery, or eDiscovery, is the process of identifying and delivering electronically stored information (ESI) that you can use as evidence in investigations and legal cases. Use Microsoft Purview eDiscovery to identify, review, and manage content in Microsoft 365 services to support your investigations. Supported Microsoft 365 services include:

- Exchange Online
- Microsoft Teams
- Microsoft 365 Groups
- OneDrive
- SharePoint
- Viva Engage

You can search mailboxes and sites in the same eDiscovery search, and then export the search results. Use eDiscovery cases to identify, hold, and export content found in mailboxes and sites. If your organization has an Office 365 E5 or Microsoft 365 E5 subscription (or related E5 add-on subscriptions), you can further manage cases and analyze content by using premium eDiscovery features.

## eDiscovery in the Microsoft Purview portal

Depending on the licensing and subscriptions for your organization, you have access to specific eDiscovery or premium eDiscovery features in the Microsoft Purview portal. All Content Search features are now included within the search experience in eDiscovery, or you can use the Content Search case in eDiscovery to manage all new and existing content searches.

To get the latest information on planned eDiscovery features and capabilities and estimated release dates, see the [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap?searchterms=ediscovery).

## Notable changes in eDiscovery

If you're familiar with previous versions of eDiscovery, you might notice several differences when using eDiscovery in the Microsoft Purview portal:

- **Advanced indexing**: In previous versions of eDiscovery, when you added a custodian or noncustodial data source to a case, you needed to reindex any content that's partially indexed or has indexing errors. Reindexing determines if the contents are relevant to defined search conditions. This reindexing process is called *advanced indexing*. As you add more partially and unindexed items to data sources (user's mailbox, OneDrive account, and so on), you need to separately update the index for specific custodian or noncustodial data sources.

    In eDiscovery, [advanced indexing](edisc-ref-advanced-indexing) runs automatically during each search that's scoped for statistics results and when you add results to a review set or export search results, depending on the indexing options you choose for the process. You no longer need to separately reindex data sources before the search process. This just in time indexing process helps avoid issues with stale indices that might result in indexing and search running sequentially and separately in the classic experience. Running (or rerunning) a search automatically updates all indexes.
- **Collections**: In previous versions of eDiscovery, *collections* provided managers with estimates of the content that might be relevant to cases. These estimates allowed managers to make quick, informed decisions about the size and scope of content relevant to cases. Once added to a review set, the collection is immutable.

    In eDiscovery, *Statistics* in searches replace *collections*. Statistics results in searches now allow managers to review important insights about the items included in the results and the relevance to the case. Searches aren't immutable in eDiscovery, even after the results are added to a review set. You can update searches at any time. Adding only a sample of the collection into review set and deleting a search is removed in eDiscovery.
- **Content Search**: Content search in the retired compliance portal was a separate solution from eDiscovery used for basic searches for content. Results from content search were estimated numbers of locations and search results that you could preview or export to a local computer.

    In the Microsoft Purview portal, all Content Search functionality is now included in a system generated eDiscovery case by default for all members of the *eDiscovery manager* and *Administrator* role groups. If you need to limit access to content searches, use *Case settings* to remove or add members to the case to manage access to these searches. You can also select **Content Search** in eDiscovery to create a Content Search case in your organization that contains all new and existing content searches.

    For more information about the changes to Content Search in eDiscovery, check out the following video:
- **Custodians**: In previous versions of eDiscovery, *custodians* (users) were the primary component of the eDiscovery workflow. Custodians were potential persons of interest in an investigation that you added to cases.

    In eDiscovery, cases are the primary component of the eDiscovery workflow. You still add people, groups, and data sources to cases, but the case is the central organizing unit.
- **Export updates**: The new [export flow](edisc-search-export) in eDiscovery supports a unified export structure across premium and nonpremium feature exports, faster export performance, detailed reporting, and flexible export options.
- **Jobs**: In previous versions of eDiscovery, tasks, activities, and reports associated with workflow components were called *jobs*. These events and reports are now referred to as *processes* in eDiscovery.

## Features and capabilities

The following table compares key eDiscovery capabilities and features:

| Capability | eDiscovery feature support | Premium eDiscovery feature support |
| --- | --- | --- |
| Search for content | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |
| Keyword queries and search conditions | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |
| Search statistics and samples | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |
| Export search results | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |
| Role-based permissions | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |
| Case management | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |
| Place content locations on hold | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |
| Search and delete data | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |
| Advanced indexing |  | ![Supported.](media/check-mark.png) |
| Review sets |  | ![Supported.](media/check-mark.png) |
| Import external data to review sets |  | ![Supported.](media/check-mark.png) |
| Support for cloud attachments and SharePoint versions |  | ![Supported.](media/check-mark.png) |
| Optical character recognition |  | ![Supported.](media/check-mark.png) |
| Conversation threading |  | ![Supported.](media/check-mark.png) |
| Decryption |  | ![Supported.](media/check-mark.png) |
| Review set filtering |  | ![Supported.](media/check-mark.png) |
| Review set KQL queries (preview) |  | ![Supported.](media/check-mark.png) |
| Query Report (preview) |  | ![Supported.](media/check-mark.png) |
| Tagging |  | ![Supported.](media/check-mark.png) |
| Analytics |  | ![Supported.](media/check-mark.png) |
| Computed document metadata |  | ![Supported.](media/check-mark.png) |
| Guest user access (preview) |  | ![Supported.](media/check-mark.png) |
| Security Copilot |  | ![Supported.](media/check-mark.png) |
| Transparency of long-running processes |  | ![Supported.](media/check-mark.png) |
| Full reporting for all processes |  | ![Supported.](media/check-mark.png) |
| Enhanced data source mapping |  | ![Supported.](media/check-mark.png) |
| Graph API delegated authentication | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |
| Graph API app-only authentication |  | ![Supported.](media/check-mark.png) |

Here's a description of each eDiscovery capability.

- **Search for content**: [Search for content](edisc-search-query) that's stored in Exchange mailboxes, OneDrive accounts, SharePoint sites, Microsoft Teams, Microsoft 365 Groups, and Viva Engage Teams. Searches include content generated by other Microsoft 365 apps that store data in mailboxes and sites.
- **Keyword queries and search conditions**: Create Keyword Query Language (KeyQL) [search queries](edisc-keyword-query-language) to search for content keywords that match query criteria. You can also include [conditions](edisc-condition-builder) to narrow the scope of your search.
- **Search statistics and samples**: After you run a search, you can view [statistics](edisc-search-results#statistics-dashboard) of the estimated search results, such as the number and total size of items matching your search criteria, the content locations that contain the most items, and the number of items returned by the search query. You can also view a representative [sample](edisc-search-results#sample-dashboard) of the items included in the search results.
- **Export search results**: [Export search results](edisc-search-export) to a local computer in your organization. When you export search results, items are copied from their original content location and packaged. Then you can download those items in the export package to a local computer.
- **Role-based permissions**: Use role-based access control (RBAC) [permissions](edisc-permissions) to control what eDiscovery-related tasks that different users can perform. You can use a built-in eDiscovery-related role group or create custom role groups that assign specific eDiscovery permissions.
- **Case management**: An eDiscovery [case](edisc-cases-manage) contains all searches, holds, and review sets related to a specific investigation. You can also assign members to a case to control who can access the case and view the contents of the case.
- **Place content locations on hold**: Preserve content relevant to your investigation by placing a [hold](edisc-hold-create) on the content locations in a case. Holds let you secure electronically stored information from inadvertent (or intentional) deletion during your investigation.
- **Search and delete data**: Use eDiscovery to [search for and delete email messages](edisc-search-mailbox-data), [Microsoft Teams chat messages](edisc-search-teams-data), and [Copilot and AI application data](edisc-search-copilot-data) across your organization. This capability helps you find and remove content that's potentially harmful or high-risk.
- **Advanced indexing**: When a search, review set, or export process runs, the associated content locations where items are partially indexed are reindexed in a process called *[Advanced indexing](edisc-ref-advanced-indexing)*. Advanced indexing ensures any content deemed as partially indexed is reprocessed to make it fully searchable when you collect data for an investigation.
- **Review sets**: Add relevant data to a [review set](edisc-review-set-manage). A review set is a secure, Microsoft-provided Azure Storage location in the Microsoft cloud. When you add data to a review set, the collected items are copied from their original content location to the review set. Review sets provide a static, known set of content that you can search, filter, tag, analyze, and predict relevancy using predictive coding models. You can also track and report on what content gets added to the review set.
- **Import external data to review sets**: Not all documents that you need to analyze in eDiscovery are in Microsoft 365. By using the [external data import feature](edisc-review-set-external-data), you can upload documents that aren't in Microsoft 365 to a review set.
- **Support for cloud attachments and SharePoint versions**: When you add content to a review set, you can include [cloud attachments](edisc-cloud-attachments) or linked files. The target file of a cloud attachment or linked file is added to the review set. You also can add all versions of a SharePoint document to a review set.
- **Optical character recognition (OCR)**: When content is added to a review set, [OCR functionality](edisc-search-add-to-review-set#optical-character-recognition) extracts text from images, and includes the image text with the content that's added to a review set. This feature lets you search for image text when you query the content in the review set.
- **Conversation threading**: When chat messages from Teams and Viva Engage conversations are added to a review set, you can collect the entire [conversation thread](edisc-search-add-to-review-set#conversation-threading). The entire chat conversation that contains items that match the search criteria is added to the review set. This feature lets you review chat items in the context of the back-and-forth conversation.
- **Decryption**: eDiscovery supports [decryption](edisc-decryption) of content protected with Microsoft encryption technologies. Email messages and attachments encrypted with Microsoft Purview Message Encryption, and documents protected with sensitivity labels or Azure Rights Management, are automatically decrypted when added to search results or review sets.
- **Review set filtering**: After content is added to a review set, you can apply [filters](edisc-review-set-search) to display only the set of items that match your filtering criteria. Then you can save the filter sets as a query, which lets you quickly reapply the saved filters. Review set filtering and saved queries help you quickly select content items that are most relevant to your investigation.
- **Review set KQL queries (preview)**: Use the [Advanced review set explorer (preview)](edisc-review-set-explorer) to run Kusto Query Language (KQL) queries directly against review set data. Build complex queries with filtering, aggregation, pattern matching, regex, and data visualization to analyze and identify key information in the review set.
- **Query Report (preview)**: Generate and download a consolidated [Query Report](edisc-review-set-query-report) on multiple queries for a review set. This report lets you quickly see the total count and volume of filtered items on a particular keyword search or multiple compound KeyQL queries.
- **Tagging**: [Tags](edisc-review-set-tagging) also help you omit nonrelevant content and identify the most relevant content. When experts, attorneys, or other users review content in a review set, their opinions related to the content can be captured by using tags. For example, if the intent is to exclude unnecessary content, a user can tag documents with a tag such as "nonresponsive". After content is reviewed and tagged, a review set query can be created to exclude any content tagged as "nonresponsive". This process eliminates the nonresponsive content from subsequent steps in the eDiscovery workflow.
- **Analytics**: eDiscovery allows you to [analyze](edisc-review-set-analytics) review set documents to help you organize the documents in a coherent manner and reduce the volume of documents to be reviewed. *Near duplicate detection* groups textually similar documents together to help you make your review process more efficient. *Email threading* identifies specific email messages that give a complete context of the conversation in an email thread. *Themes* functionality attempts to analyze themes in review set documents and assign a theme to documents so that you can review documents with related theme. These analytics capabilities help make your review process more efficient so that reviewers can review a fraction of collected documents.
- **Computed document metadata**: Many of the eDiscovery premium features, such as conversation threading and analytics, add metadata properties to review set documents. This [metadata](edisc-review-set-view#use-metadata-view) contains information related to the function performed by a specific feature. When reviewing documents, you can filter on metadata properties to display documents that match your filter criteria. This metadata can be imported into third-party review applications after review set documents are exported.
- **Guest user access (preview)**: Invite [guest users](edisc-settings-guest-users) to access eDiscovery cases for collaboration with external reviewers. Guest users are assigned the *Reviewer* role group permission and can view and work with case content shared with them.
- **Security Copilot**: Use [Microsoft Security Copilot](edisc-review-set-view#summarize-an-item-by-using-microsoft-security-copilot) features to draft KeyQL search queries by using natural language and to generate contextual summaries of items in a review set.
- **Transparency of long-running processes**: Processes in eDiscovery typically involve long-running activities that user actions trigger, such as adding custodians to a case, adding content to a review set, running analytics, and creating search queries. You can [track the status](edisc-process-managers) of these processes and get support information if you need to escalate issues to Microsoft Support.
- **Full reporting for all processes**: Use the [Process report](edisc-process-report) to view and manage processes in cases, searches, review sets, and holds.
- **Enhanced data source mapping**: [Data sources](edisc-data-sources) streamline the process of identifying and managing data. You can search locations based on users, search one site for groups, and map other locations with groups. You can also explore frequent collaborators as part of data sources.
- **Graph API delegated authentication**: [Graph API calls](edisc-ref-api-guide#microsoft-purview-apis) are made on behalf of a signed-in user. The [application acquires a token](/en-us/graph/auth-v2-user?tabs=http) that combines the user's identity with the app's permissions (scopes), so Graph enforces both the user's privileges and the app's consented permissions.
- **Graph API app-only authentication**: [Graph API calls](edisc-ref-api-guide#microsoft-purview-apis) are made by the application itself, without a user context. The [app authenticates using its own credentials](/en-us/graph/auth-v2-service?tabs=http) (client secret or certificate) and acquires a token tied solely to its consented application permissions.

## Integration with other solutions

### Insider risk management

In [Microsoft Purview Insider Risk Management](insider-risk-management), you can quickly escalate cases to new cases in eDiscovery when you need additional legal review for potentially risky user activity. The tight integration between these solutions helps your risk and legal teams work more efficiently and provides a complete end-to-end view of user activities under review.

For more information, see [get started with Insider Risk Management](insider-risk-management-configure) and [escalate an Insider Risk Management case](insider-risk-management-cases#escalate-for-investigation) to an eDiscovery (Premium) case.

### Microsoft Security Copilot

In eDiscovery, you can use [Microsoft Security Copilot](copilot-in-purview-overview) features to draft KeyQL search queries by using natural language. Copilot translates natural language to KeyQL without requiring you to learn how to construct a KeyQL query, know operators, or know supported search metadata fields.

Copilot can also provide a contextual summary of most items in a review set. The summary is in the context of text included in a selected item. This summary saves time for reviewers by quickly identifying information helpful when tagging or exporting items. Security Copilot summarizes the entire item, including any documents, meetings transcripts, or attachments. Most of the common document file types are supported.

For more information about using Security Copilot with review sets, see [Summarize an item by using Security Copilot](edisc-review-set-view#summarize-an-item-by-using-microsoft-security-copilot).

## Ready to get started?

- [Learn about the eDiscovery workflow](edisc-workflow)
- [Get started with eDiscovery](edisc-get-started)