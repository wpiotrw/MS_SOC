---
layout: Conceptual
title: Add search results to a review set in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-search-add-to-review-set
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about adding search results to a review set, including sampling options, for a case in eDiscovery in the Microsoft Purview portal.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-29T00:00:00.0000000Z
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
f1.keywords:
- NOCSH
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 5b571c0e-0900-b029-5c2e-092958659960
document_version_independent_id: 5b571c0e-0900-b029-5c2e-092958659960
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-search-add-to-review-set.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-search-add-to-review-set
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-search-add-to-review-set.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: f775f183-61c2-489f-020e-f76e1f283ebb
---

# Add search results to a review set in eDiscovery | Microsoft Learn

When you're satisfied with the results of a search and ready to review and analyze the results, add them to a review set in the case. You can add all search results or configure sampling to add a statistically representative subset based on confidence or percentage. Copying the original data to the review set also facilitates the review and analysis process by providing you with advanced analytics tools such as themes detection, near-duplicate detection, and email thread identification.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Create or add results to a review set

Tip

Want an interactive configuration guide experience? Check out the [Create and manage review sets](https://mslearn.cloudguides.com/guides/Create%20and%20manage%20review%20sets%20with%20Microsoft%20Purview%20eDiscovery) guide.

When you add the results of a search to a review set (the review sets in a case are listed on the **Review sets** tab), the following things occur:

- The search runs again. This step means the actual search results you copy to the review set might be different from the estimated results that the search returned.
- All items in the search results are copied from the original data source in the live services to a secure Azure Storage location in the Microsoft cloud.
- All items (including the content and metadata) are reindexed so that all data in the review set is fully searchable during the review of the case data. Reindexing the data results in thorough and fast searches when you search the data in the review set during the case investigation.
- A file encrypted with a [Microsoft encryption technology](encryption) and attached to an email message that's returned in the search results is decrypted when the email message and attached file are added to the review set. You can review and query the decrypted file in the review set. You must be assigned the *RMS Decrypt* role to add decrypted email attachments to a review set. For more information, see [Decryption in Microsoft Purview eDiscovery tools](edisc-decryption).

When you add content to a review set, the items and their metadata are copied to a Microsoft-managed Azure Storage location dedicated to the case.

| Question | Answer |
| --- | --- |
| Is review set content stored in Microsoft-managed Azure Storage? | Yes. The storage is Microsoft-owned and Microsoft-managed. Customers don't see, manage, or pay for these storage resources directly. |
| Is storage provisioned per review set? | No. Storage is provisioned **per case**. Multiple review sets within the same case share the underlying case storage, with logical separation so each review set's content remains independently queryable, taggable, and exportable. |
| How are different tenants and cases isolated? | Each case is isolated from other cases and other tenants at the storage boundary. Tenant separation is enforced by the service. |
| What region hosts the storage? | The storage is provisioned in the region that matches the case's geo, consistent with Microsoft 365 data residency commitments. |
| Does Customer Key apply to review set content? | Yes. If your tenant is configured with [Customer Key](/en-us/purview/customer-key-overview), review set content at rest is encrypted with the customer-managed key. |
| Can customers access the storage directly? | No. There's no customer-accessible SAS token, account key, or storage URL for review set content. Access to review set content is only through the Microsoft Purview portal and approved export workflows. |

If the search you're adding to review set is tenant wide or contains large number of data sources, running a **Generate statistics** process before adding to review set can significantly improve performance. When search statistics are available, eDiscovery uses the search statistics to optimize subsequent Add to review set process by limiting processing to only the locations that contain search hits, instead of reprocessing all locations in scope. This location optimization helps reduce process duration and improves reliability for large tenants. If the **Generate statistics** process is outdated or the search query or data sources have changed, eDiscovery processes all locations again to ensure accuracy. To confirm if your Add to review set process has location optimization applied, refer to [settings.csv](/en-us/purview/edisc-process-report) of the Add to review set process report. Additionally, completing the **Generate statistics** process is required to enable sampling options when adding search results to a review set.

Note

Even if the **Generate statistics** process has errored locations, those locations are still included in subsequent Add to review set process. If the **Generate statistics** process is retried, the subsequent Add to review set process doesn't have location optimization applied.

To add data to a review set, complete the following steps:

1. Select a search on the **Searches** tab, and then select **Add to review set**.
2. On the **Add items to review set** flyout, select **Add to a new review set** or **Add to an existing review set**.

    For a new review set, enter a name for the review set. To add data to an existing review set, select a review set from the drop-down choices.

    Adding data to a review set is a long-running process that includes gathering items from the original data sources in Microsoft 365 (for example, from mailboxes and sites), copying them to the Azure Storage location (this copying process is also called *ingestion*), and then reindexing the items. You can track the progress on the **Process manager** page. After the review set processing completes, select the **Review sets** tab in the case, then select the review set to start the process of filtering, reviewing, tagging, and exporting data in the review set.
3. In the **Select items to add to review set** section, choose one of the following options:

    - *Indexed items that match your search query*: This option exports only the indexed items that matched the query.
    - *Indexed items that match your search query and partially indexed items that might not match query*: This option exports only the indexed items that matched the query and the partially indexed or unindexed items that might not completely match the query.
    - *Partially indexed items that might not match query*: This option exports only the partially indexed or unindexed items that might not completely match the query.

    Scope the partially indexed items further by selecting *Exclude partially indexed items in locations without search hits*. With this option selected, only partially indexed items from location where there's already an indexed hit are returned. Additionally, user also has the option to *perform advanced indexing on partially indexed items*. For more information about advanced indexing, see [Learn more about advanced indexing in eDiscovery](edisc-ref-advanced-indexing).
4. In the **Configure sampling** section, choose one of the following options to control how many items are added to the review set. Sampling options are only available after you complete the **Generate statistics** process on the search. If statistics haven't been generated, are outdated, or the query or data sources changed since statistics were last run, sampling options are disabled and only the **Add all search results** option is available.

    - **Add all search results to review set** (default): Commits every item that matches the search query to the review set.
    - **Add samples to review set based on confidence**: Commits a statistically derived sample based on a **Confidence level** and **Confidence interval**. The confidence level (default: 95%) is the probability that your sample reflects the characteristics of the entire search result population. The confidence interval (default: 5%) is the range within which the true value is expected to fall. Higher confidence and tighter intervals produce larger samples.
    - **Add samples to review set based on percentage**: Commits a specified percentage of the total estimated items. Enter a value between 1 and 99 in the **Sample size** field (default: 50%). For example, if the search estimates 2,000 items and you select 50%, approximately 1,000 items are added to the review set.

    The actual number of items added to a review set may differ slightly from the calculated sample size. During the add-to-review-set process, items undergo expansion and extraction, which can result in minor variances between the expected and actual item counts.
5. In the **What to include for files from ODSP sites?** section, complete the following options:

    - **Select document versions**: Specify how many versions of SharePoint documents to collect. Choose from *Latest version only*, *Recent 10 versions*, *Recent 100 versions*, or *All versions*.
    - **Select folder items**: Choose one of following options to collect items inside subfolders of a matched folder:
        - **Only include items that matches query**
        - **Include all items in folder even if they don't match query**
    - **Select items in lists and attachments (list expansion)**: Choose of the following to collect files attached to SharePoint lists and their child items.
        - **Include all items in SharePoint if any item matches the query**
        - If applicable, select the **Include attachments of lists** checkbox.
    - **Convert supported file formats to HTML**: Select this option to convert supported cloud-native file formats, such as `.loop` and `.page` files (used by Copilot Notebook and Page content), to HTML when adding items to the review set. Converted content is indexed and available for keyword search in the review set, making it easier to review and analyze. This option isn't selected by default.
6. In the **What to include for messages and related items from Mailboxes?** section, select the following options as applicable:

    - **Organize conversation into HTML transcript**: Contextual chat messages are threaded into HTML transcript of ease of review/handling.
    - **Include Teams and Viva Engage conversations**: Collect up to 12 hours of related conversations when a message matches a search.
    - **Access links (cloud attachments) in messages**: Collect items from links to SharePoint or OneDrive. Choose from *Latest version only*, *Recent 10 versions*, *Recent 100 versions*, or *All versions*.

        When you search for emails or other mailbox content that might include [cloud attachments](edisc-cloud-attachments), the cloud attachment link to a storage location in SharePoint or OneDrive is considered as an attachment of the message file rather than separate documents.

        Treating cloud attachment links as message attachments is similar to how a search returns emails with embedded local attachments. These attachments are retrieved as if they're part of the emails. Any compliance boundaries for SharePoint or OneDrive aren't reflected in the collection of cloud attachments included in responsive messages.

        Important

        Items that are encrypted aren't supported for embedded entity extractions for example attachments. To collect cloud attachments from Shared Channels in Teams,the Shared Channel SharePoint site must be included in the search scope.
7. In **Tenant-wide source configuration** options, configure the organization-wide source **All people and groups** to include one or more user or content types:

    - **All people and groups** should include unlicensed and on-premises users
    - **All people and groups** should include guest users
    - **All people and groups** should include shared Teams channels
    - **All people and groups** should include departed users
8. Review your selections for the review set, and then select **Add to review set**. To cancel, select **Cancel**.

## Optical character recognition

When you add search results to a review set, eDiscovery's optical character recognition (OCR) functionality automatically extracts text from images. It includes the image text with the data that it adds to a review set. You can view the extracted text in the Text viewer of the selected image file in the review set. This extracted text is then searchable within the review set. This feature lets you conduct further review and analysis on text in images. OCR supports loose files, email attachments, and embedded images. For a list of image file formats that support OCR, see [Supported file types in eDiscovery](edisc-ref-supported-file-types#image).

Important

Microsoft Purview eDiscovery OCR extracts text from images only when content is added to a review set, it doesn't make images searchable during the search phase. To find image-based content, first search broadly then use OCR text in the review set. OCR in eDiscovery is separate from the tenant-level Microsoft Purview OCR setting (used by DLP, Insider Risk Management, and Retention). Enabling tenant-level OCR doesn't [enable eDiscovery OCR](edisc-settings-search-analytics#optical-character-recognition-ocr). For more information about tenant-level OCR, see [Learn about OCR in Microsoft Purview](ocr-learn-about).

You need to enable OCR functionality for each case that you create in eDiscovery. For more information, see [Configure search and analytics settings](edisc-settings-search-analytics#optical-character-recognition-ocr).

## Conversation threading

Instant messaging is a convenient way to ask questions, share ideas, or quickly communicate across large audiences. As instant messaging platforms, like Microsoft Teams and Viva Engage groups, become core to enterprise collaboration, organizations must evaluate how their eDiscovery workflow addresses these new forms of communication and collaboration.

The conversation reconstruction feature in eDiscovery helps you identify contextual content and produce distinct conversation views. This capability allows you to efficiently and rapidly review complete instant message conversations (also called *threaded conversations*) that platforms like Microsoft Teams generate.

By using conversation reconstruction, you can reconstruct, [review](edisc-review-set-teams-data), and export threaded conversations. Use eDiscovery conversation reconstruction to:

- Preserve unique message-level metadata across all messages within a conversation.
- Collect contextual messages around your search results.
- Review, annotate, and redact threaded conversations.
- Export individual messages or threaded conversations.

### Conversation threading terminology

Here are a few definitions to help you get started using conversation reconstruction.

- **Messages:** Represent the smallest unit of a conversation. Messages might vary in size, structure, and metadata.
- **Conversation:** Represents a grouping of one or more messages. Across different applications, conversations might be represented in different ways. In some applications, an explicit action results from replying to an existing message. Conversations form explicitly as a result of this user action. For example, here's a screenshot of a channel conversation in Microsoft Teams.

    ![Screenshot of a Microsoft Teams channel conversation thread showing replies.](media/threadedchat.png)

    In other apps (such as group chat messages in Teams), there's no formal reply chain and instead messages appear as a "flat river of messages" within a single thread. In these types of apps, conversations are inferred from a group of messages that occur within a certain time. This "soft-grouping" of messages (as opposed to a reply chain) represent the "back and forth" conversation about a specific subject of interest.

### Add conversations to a review set

After you review and finalize the search query, add the search results to a review set. Use the threaded conversations option to collect contextual messages from conversations that contain items that match the criteria of the search. When you select the thread conversations option, the following things can happen:

![Screenshot of conversation retrieval showing how eDiscovery collects contextual messages from a conversation thread.](media/messagesandconversations.png)

1. Using a keyword and date range query, the search returns a hit on *Message 3*. This message is part of a larger conversation, illustrated by *CRC1*.
2. When you add the data into a review set and enable the conversation retrieval options, eDiscovery goes back and collects other items in *CRC1*.
3. After you add the items to the review set, you can review all the individual messages from *CRC1*.