---
layout: Conceptual
title: Use Process reports in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-process-report-use
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to review and manage processes with Process reports in eDiscovery.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-04-01T00:00:00.0000000Z
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
document_id: c8d213e6-b1a9-f521-15ef-8005a0132d4c
document_version_independent_id: c8d213e6-b1a9-f521-15ef-8005a0132d4c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-process-report-use.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-process-report-use
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-process-report-use.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 4d6328fe-d43f-ef37-41f6-80e779607c6e
---

# Use Process reports in eDiscovery | Microsoft Learn

## Process report for the organization

eDiscovery includes [Process reports](edisc-process-report) that list all processes in your organization that count towards case process concurrency and daily limits in eDiscovery. *eDiscovery administrators* and *eDiscovery Managers* can access this report on the **Dashboards** &gt; **Process report**. Use this report to see the process activities across all activities and eDiscovery components. *eDiscovery Managers* can only view processes for the cases to which they're assigned.

Important

You can't delete or remove processes listed on the **Process manager** page. Long-running processes automatically time out after seven days.

## Process report for items

eDiscovery also includes a **Process manager** that lists all processes scoped to the current eDiscovery item and page. For example, if you're on the **Search** page, selecting **Process manager** lists all processes relevant to the current search. If you're in a case, selecting **Process manager** lists all processes relevant to the current case. Each process in the Process manager list contains a detailed report .zip file that contains detailed information about the process after the process completes. You can download the process report .zip file for more information about when the process ran, the applied settings, the query used, and if the process had any item-level or location-level errors.

Important

You can't delete or remove processes listed on the **Process manager** page. Long-running processes automatically time out after seven days.

For more information about Process reports in eDiscovery, watch the following video:

## Process types and descriptions

User actions trigger these processes when managing searches, review sets, and holds.

| Process type | Area | Description |
| --- | --- | --- |
| Add items to another review set | Review set | A user adds documents from one review set to a different review set in the same case. For more information, see [Add data to a review set from another review set](edisc-review-set-add-to-other-review-set). |
| Add to review | Review set | A user adds search results to a review set or adds items into the review set from another review set. The process copies the items to an Azure Storage location and then reindexes those items in the Azure Storage location. This new index is used when querying and analyzing items in the data set. |
| Applying or updating hold | Hold | A user places data sources on hold or updates a hold. |
| Export | Search  Review set | A user exports documents from a search or a review set. When the export process completes, they can download the exported data to a local computer. |
| Generate sample | Search | After a user creates and runs a new search estimate (or reruns an existing search estimate), the search tool prepares a sample subset of items (that match the search query) that you can preview. Previewing search results helps you determine the effectiveness of the search. |
| Generate statistics | Search | After a user creates and runs or reruns a search estimate, the search tool searches the index for items that match the search query and prepares an estimate that includes the number and total size of all items by the search, the number of data sources searched, and other relevant pattern to the search hits like keywords, sensitive information types, and more. |
| Import external data | Review set | A user uploads external data to a review set. The data is also indexed during this process. For more information, [see Import external data into a review set](edisc-review-set-external-data). |
| Redact | Review set | After a user annotates a document in a review set and redacts a portion of it, they can choose to convert the redacted document to a PDF file. This ensures that the redacted portion won't be visible if the document is exported for presentation. For more information, [see View documents in a review set](edisc-review-set-view). |
| Run analytics | Search | A user analyzes data in a review set by running eDiscovery analytics tools such as near duplicate detection, email threading analysis, and themes analysis. |
| Tag | Review set | This process triggers when a user selects **Start tagging process** in the **Tagging panel** when reviewing documents in a review set. A user can start this process after tagging documents in a review set and then bulk-selecting them in the view document panel. |

## Process status

The following table describes the different status states for processes:

Note

You can cancel only **Generate statistics** and **generate sample** processes.

| Status | Description |
| --- | --- |
| Abandoned | The process was automatically stopped. This stoppage might be due to excessive processing time or other reasons. |
| Canceled | The user canceled the process. |
| Complete | The process completed successfully. |
| Failed | The process encountered an error and didn't complete. This error might be caused by a wrongly formatted query. |
| In progress | The process is in progress. You can monitor the progress of the process in the **Process manager** for the area. |

## Download report

All processes support the ability to download a packaged report. The packaged report name is `Reports-*caseName-EntityName-ProcessName-timestamp*.zip`, with `EntityName` being the user-given name to the search or hold. Depending on the process, the report contains different `.csv` files.

- **Summary**: Tracks the time the process started, when it ended, the number of total items or locations, and the user who submitted the process request. It also contains the search query used and if a [compliance boundary](edisc-compliance-boundaries) is applied. For *Add to review set* and *Export* from search processes, the summary report contains the summary of factors affecting the total item count added to review set or exported. The report name is `Summary_*the date/time of the report*.csv`.
- **Settings**: Contains the enumerated settings parameter for the process and values. The report name is `Settings_*the date/time of the report*`.
- **Statistics**: Contains all statistics details for the process, including all categories (if the setting was selected during process submission) such as sensitive information types, data type, and communication participants. The report name is `Statistics_*the date/time of the report*`.
- **Locations**: Tracks all data sources and associated locations scoped for the process. Includes the user/group entity name, location (mailbox/site URL), and count returned for that location. Also includes the status of the location (success/error and error detail). The report name is `Locations_*the date/time of the report*`.
- **Items**: Track all items processed, including information such as item ID, location of the item, subject/title of the item, item class/type, and success/error status. The report name is `Items_*the date/time of the report*`.

The following table shows the process types and available reports:

| Process type | Summary | Settings | Statistics | Location | Items |
| --- | --- | --- | --- | --- | --- |
| Add to review | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |  | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |
| Apply hold/rerun policy | ![Supported.](media/check-mark.png) |  |  | ![Supported.](media/check-mark.png) |  |
| Export (review set) | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |  | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |
| Export (search) | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |  | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |
| Generate sample | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |  | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |
| Generate statistics | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |  |
| Redact | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |  |  | ![Supported.](media/check-mark.png) |
| Tag | ![Supported.](media/check-mark.png) | ![Supported.](media/check-mark.png) |  |  |  |

Note

When running an [export process](edisc-search-export) using the *report only* option, all string fields in the report are limited to the first 255 characters. This means some items with long compound path may be truncated. If full details are needed, use the *Export items with items report* option.

### Summary CSV report

All reporting packages contain a `Summary-*the date/time of the report*.csv` file. This file contains the following information:

#### Overview

This section of the report includes the following details:

- **Job ID**: A unique identifier assigned to each eDiscovery process for support reference purposes.
- **Case name**: The name assigned to the eDiscovery case.
- **Search name**: The name given to a specific search within an eDiscovery case when the process runs. This detail only applies to processes like *Generate statistics*, *Generated sample*, *Add to review set*, and *Export* from a search.
- **Review set name**: The name of the review set where search results are added when the process runs. This detail only applies to the *Add to review set* and *Export from a review set* processes.
- **Export name**: The name given to the export. This detail only applies to the *Add to review set* and *Export from a review set* processes.
- **IsRetry**: Indicates if the current process is triggered by the *Retry failed locations* operation. If the value is *Yes*, it contains the aggregated hit count and the location reports detail the failed locations. This detail only applies to the *Generate statistics* process.
- **Query**: The query conditions for the applicable process types.
- **StartTime**: The date and time when the report generation started.
- **EndTime**: The date and time when the report generation completed.
- **SubmittedBySmtp**: The SMTP address for the user creating the report.
- **Security filter applied**: Indicates if security filters were applied during the process run. *Yes* indicates that filters were used to limit results based on specified criteria set by an admin in PowerShell.
- **Location restriction**: The filters applied to limit the search to specific locations. To review which mailboxes are filtered, use the provided query with the [Get-Mailbox](/en-us/powershell/module/exchange/get-mailbox) or [Get-Recipient](/en-us/powershell/module/exchange/get-recipient) cmdlets and the *-Filter* attribute. For example, if the filter attribute is *Department -eq 'marketing'*, retrieve the relevant mailboxes with *Get-Recipient -Filter "Department -eq 'marketing'*. The output lists all mailboxes allowed to be searched.
- **Content restriction**: The query used to filter content during the search. Content matching this query is included in the search results. The provided query is available to perform KeyQL searches.

#### Search results

Summary of number of items that matched your search query, including partially indexed items or items where advanced indexing was performed (depending on what setting you selected). This section of the report includes the following details:

- **Indexed items**: Number of items matching the query that were natively indexed by Exchange and SharePoint.
- **Partially indexed items**: Number of partially indexed items that might not match the query. Included if you chose to include partially indexed items.
- **Advanced Indexed Items**: Number of items matching the query if you chose to perform advanced indexing on partially indexed items.

#### Consumption summary

This section of the report includes the following details:

- **Microsoft 365 content data**: Total size of data for all Microsoft 365 data.
- **Microsoft 365 metadata**: Total size of metadata for all Microsoft 365 data and Microsoft 365 Copilot data.
- **Non-Microsoft 365 AI content data**: Total size of data for all non-Microsoft 365 AI data. Includes data from Microsoft Fabric Copilot, Microsoft Security Copilot, and other AI data from enterprise and cloud applications.
- **Non-Microsoft 365 AI metadata**: Total size of metadata for all non-Microsoft 365 AI data.

Note

For more information about the consumption summary and billing implications, see [Understanding the consumption summary](edisc-process-report#understanding-the-consumption-summary).

#### Error

This section of the report includes the following details:

- **Retrieval exceptions**: Number of items that weren't exported or added to review set due to exceptions such as empty files, access time-outs, and similar issues.

#### Warning

- **Items with processing errors**: Number of items that experienced processing errors but were still exported or added to the review set. These errors might be caused by unsupported file types, decryption problems, and similar issues.

#### Totals

This section of the report includes the following details:

- **Total items collected**: Total number of items exported or added to the review set. This number factors in items from estimated results, the settings that might increase or decrease the number of items retrieved, and items that weren't collected due to errors.

#### Information

Note

The **Information** section of this report shows how the item count can increase or decrease based on the settings you choose. The calculation process uses these settings and updates the search estimate count, so the counts don't add up exactly in most cases. This information gives you a sense of the changes and the reasons behind them.

This section of the report includes the following details:

- **Duplicates in review set (skipped)**: Items that are skipped because they already exist in the review set.
- **Cloud attachments**: Number of [cloud attachments](edisc-cloud-attachments) in email messages and Teams conversations that come from links shared through SharePoint or OneDrive. Maps to the setting *Access links(cloud attachments) in messages*.
- **Cloud attachments versions**: Number of cloud attachment versions that are collected depending on whether you choose to include more than just the latest version in your query.
- **Cloud attachments at time of sharing**: Number of cloud attachment versions that represent the original version shared from SharePoint or OneDrive. This count applies only to cloud attachments that have a retention label applied, which retains a copy of the file at the time of sharing.
- **Contextual conversation**: Number of contextual chat messages that are collected along with the message that matches your query. This count shows the number of additional messages collected before and after the message with hit. This count corresponds to the setting "Include Teams and Viva Engage conversations".
- **Teams conversations consolidated into transcripts**: Teams chat conversations that are converted to HTML transcript files. This conversion results in many Teams chat messages being consolidated into a single HTML transcript. This count corresponds to the setting "Organize conversations into HTML transcripts".
- **SharePoint file versions**: Number of SharePoint file versions that are collected depending on whether you choose to include more than just the latest version.
- **SharePoint list items collected as .csv files**: Matches from the same SharePoint list are exported or added to review set as a single SharePoint list csv item. This count corresponds to the setting "Collect files attached to SharePoint lists and their child items."
- **List attachments**: Number of list attachments collected. This count corresponds to the setting *Include list attachments* when collecting files attached to SharePoint lists.
- **Items in SharePoint folders**: Number of items expanded from SharePoint folders that match your query. This count corresponds to the setting *Collect all items (even if they don't match search query)*.
- **Items extracted from parent items**: Number of embedded or attached items that the process extracts from parent items. For example, this count might include attachments or embedded images from an email that matches your query.

### Settings CSV report

The settings report helps you validate and interpret the configuration of your submitted processes. The downloadable report package includes this report. It captures the specific options you select during the submission of a process, such as **Generate statistics**, **Add to review set**, and **Export**.

These settings directly influence the scope and format of the results. Some examples of these settings include:

- **Include document versions**: Determines the number of versions of a document to include.
- **Organize conversations into HTML transcripts**: Affects how Teams conversations are threaded and presented.
- **Access links in message**: Controls whether cloud attachments from message links are included.
- **Various export formats and options**: Influences how exported content is organized and packaged.
- **Decryption settings**: Indicates whether the specific process has associated Exchange or SharePoint decryption capability enabled.
- **Location optimization**: Indicates if location optimization is applied for the search *Export* or *Add to review set* process. If optimization is applied, the relevant *Generate statistics* process ID used.
- **Sampling mode**: Indicates the sampling method used for the *Add to review set* process. Values include *All items*, *Percentage*, or *Confidence*.
- **Sample percentage**: The percentage value configured when using percentage-based sampling. Present only for the *Percentage* sampling mode.
- **Confidence level**: The confidence level configured when using confidence-based sampling. Present only for the *Confidence* sampling mode.
- **Confidence interval**: The confidence interval configured when using confidence-based sampling. Present only for the *Confidence* sampling mode.

For more information about how these settings affect search result counts, see [Understanding the impact of search settings on results](edisc-process-report#understanding-the-impact-of-search-settings-on-results). For guidance on using the Settings CSV for traceability and compliance, see [Understanding export settings and traceability](edisc-process-report#understanding-export-settings-and-traceability).

### Statistics CSV report

This report provides detailed information for all the patterns derived from search hits when you complete the *Generate statistics* process. The report contains information on the top communication participants, the top item type, the top sensitive information type, and more.

The report includes the following details:

- **DataSourceName**: A list of data source names associated with the process. This information indicates the name of the people or groups.
- **DateSourceType:** Type of data source. For example, *Group* or *TeamsGroup*.
- **Location**: The location information. For example, the URL of the site or SMTP address of the mailbox.
- **LocationType**: Type of location. For example, a mailbox or site.
- **LocationSubType**: The subtype of the location type. If the location type is *Mailbox*, the subtype might have *PrimaryMailbox*, *SystemMailbox*, and other subtypes. If the location type is *Site*, it might have *OneDriveSite* and other subtypes.
- **OriginalStateName**: Native version of StatName.
- **StatName**: Name of the StatType. For example, for StatType *Keywords*, possible values are the keywords you entered in your query.
- **StatType:** The type of statistics information. For example, *Keywords*, *Communication participants*, and more.
- **Value**: The value or count associated with the statistics in the current data source.

### Items CSV report

This report provides a detailed inventory of all items processed during an eDiscovery process, such as using the **Add to review set** or **Export** actions. The system automatically generates this report and includes it with the output to support auditing, traceability, and downstream analysis. This report is useful for users who need to validate the scope and accuracy of collected or exported content.

Each row in the file corresponds to a single item and includes the following metadata and more:

- **Date source**: Identifies the originating location of the item (mailbox, SharePoint site, Teams chat).
- **Compound path**: The full path to the item in its source container.
- **Subject/Title**: The subject line (for emails) or title (for documents) of the item.
- **Date**: The timestamp associated with the item, such as sent or last modified date.
- **Added by**: Shows how the item was included in the job:

    - *IndexedQuery*: The item is indexed and matches the search query.
    - *UnindexedQuery*: The item is included based on its partially indexed content and user specified setting.
- **Status**: Shows whether the item was successfully retrieved and processed. If the item failed, the **ErrorWarning** field includes the failure reason. For common item-level errors, see [Why certain items weren't exported](edisc-process-report#why-certain-items-werent-exported).
- **Other metadata**: Might include the file extension, content type, workload, and other relevant attributes depending on the source and process type.

### Locations CSV report

This report provides an overview of the locations targeted during an eDiscovery process, such as **Search**, **Add to review set**, or **Export**. This report helps you understand the scope of the process and assess the distribution and relevance of search results across different locations.

This report can help with:

- **Heat mapping**: Identifying which locations yielded the most relevant content and which yielded none, helping you visualize the "hot spots" of data relevance.
- **Query refinement**: Understanding which sources you might need to exclude or more precisely target.
- **Audit and validation**: Verifying that the intended locations were included and assessing the effectiveness of the search scope.

By analyzing the `location.csv` report, you can make informed decisions about refining your search strategy and optimizing the scope of future eDiscovery workflows.

Note

If multiple mailboxes share the same SMTP address, the location report might show several rows. This situation occurs because a single SMTP address might include different mailbox subtypes, such as primary, system, or archive. The row count in the CSV report might exceed the count shown on the location card in the **Statistics** view. The **Statistics** view aggregates all mailboxes under the same SMTP address without distinguishing subtypes. For a more detailed breakdown of hits by sublocation, use the CSV report instead of the **Statistics** view. SharePoint and OneDrive locations can also have archive sites and are counted as separate locations in the report.

Each row in the report represents a unique content location and includes the following key details:

- **Count**: The number of items in the location that matched the search criteria. This doesn't apply to the *Applying or updating hold* process.
- **Location ID**: Site ID for SharePoint or mailbox ID for mailboxes.
- **Location Subtype**: Specifies the type of location, such as *PrimaryMailbox*, *SystemMailbox*, *ArchiveMailbox*, or *OneDriveSite*.
- **Location**: The full URL or SMTP address of the location. For organization-wide searches, locations are empty for sites without hits. If needed, use the *LocationID* to identify the site URL.
- **Size**: The total size of responsive items from the location in bytes. This doesn't apply to *Applying or updating hold* process.
- **Status**: Indicates whether the location was successfully processed. If a location failed to be searched or exported, the **ErrorWarning** field includes the failure reason. For common location errors and remediation steps, see [Understanding location-level errors](edisc-process-report#understanding-location-level-errors).