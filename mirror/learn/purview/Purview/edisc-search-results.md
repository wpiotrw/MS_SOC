---
layout: Conceptual
title: Evaluate and refine search results in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-search-results
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about evaluating and refining search results for a case in eDiscovery in the Microsoft Purview portal.
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
document_id: 83f405cf-64bb-f694-6120-b9133cf388c0
document_version_independent_id: 83f405cf-64bb-f694-6120-b9133cf388c0
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-search-results.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-search-results
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-search-results.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 9203e1f7-a5cb-78af-e1eb-768262a3d2d3
---

# Evaluate and refine search results in eDiscovery | Microsoft Learn

Evaluating and refining your search results is an important step in your eDiscovery investigation. The search query you configure and the results that return help you determine if you discover items and information applicable to your investigation or if you need to modify your search to try to discover additional pertinent items. This initial search of items and initial review of information helps you determine what actions are required after you finalize your search parameters.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Evaluate search results

After you create and run a search, view the search statistics to help you verify whether relevant content is found and the content locations with the most hits. You can also review a sample of the search results to further help you determine if the content is within scope of your investigation.

### Statistics dashboard

If you select **Statistics** as the initial result type for your search, the search automatically redirects you to this dashboard when the search results complete. If you're already familiar with previous versions of eDiscovery, the information on the **Statistics** tab is similar to collection estimates. The search results for the **Statistics** dashboard are included in the following sections:

- **Summary**: This section shows the number of search hits, locations, data sources, and the total file size of partially indexed items.

    - **Search hits**: Displays the total search hit count and volume from all items matching the query criteria from locations searched.
    - **Locations**: Displays the fraction of locations with hits out of all locations searched. The numerator shows the locations with hits and denominator shows the number of locations searched. Locations with errors are shown in red. To view full details on all the locations and associated hits and errors, select **Download report** to download the full .csv report. Note that the displayed location count in this card might be different from the number of rows in [locations CSV report](edisc-process-report). If multiple mailboxes share the same SMTP address, the location report might show several rows. This situation occurs because a single SMTP address might include different mailbox subtypes, such as primary, system, or archive. The row count in the CSV location report might exceed the count shown on the location card in the **Statistics** view. The **Statistics** view aggregates all mailboxes under the same SMTP address without distinguishing subtypes. For a more detailed breakdown of hits by sublocation, use the CSV report instead of the **Statistics** view. SharePoint and OneDrive locations can also have archive sites and are counted as separate locations in the report.
    - **Retry failed locations**: This action is available when there are failed locations. *Retry failed locations* operation triggers a new search process targeting those locations with error and then aggregate the retried hit count with the original search process' hit count. After the retry process completes, the statistics view shows the new aggregated hit count.
    - **Data sources**: Displays the fraction of data sources with hits out of all data sources searched. The numerator shows the data sources with hits and denominator shows the number of data sources included in the search. This data source is consistent with the data source in the search design flow and should match the number of people or groups included in the search. A tenant-wide data source of *All people and all groups* counts as a single data source.
    - **Partially indexed items** or "Advanced indexed items hits": Displays the count and volume of partially and unindexed items returned as part of the search. This card displays partially indexed items information if you choose to include partially or unindexed items as part of the search configuration. If you choose to include partially and unindexed items and enable advanced indexing options, this card displays additional hits you get from advanced indexed items. The advanced indexed hit count is from a statistic sample on the partially indexed items, actual hits might be more and should be confirmed using the add to a review set and export search results actions. For more information, see [Assess partially indexed items in your organization](edisc-ref-partially-indexed-items#assess-partially-indexed-items-in-your-organization).
- **Search hit trends**: This section shows the following search result cards. The charts are interactive, hover to display section names, percentages, and item numbers. Select **View top 100** for more information about items included in each trend and to download the results to a .csv file:

    - **Top data sources**: Displays the top five data sources that make up the most search hits matching your query. The name of these data sources (names of users, groups, or organization-wide locations) are listed with the hit count. These data sources should match what you selected in the data sources workflow when building the search query.
    - **Top sensitive information types (SITs)**: Displays the top five sensitive information types (SITs) in SharePoint files that are most often included in the search hits matching your query. Adding each SIT’s count doesn't necessarily equate to the total count hits because a single item or document might contain more than one SIT type. For example, a document contains both a password and social security number (SSN). In this example, it's counted twice. Select **View top 100** to get a deeper understanding of the locations of these SIT counts to verify if they overlap or not.
    - **Top keywords**: Query keywords, which resulted in the most search hits matching your query.

        Note

        To generate a keyword report in the statistics view, you must populate at least two or more keyword grids. If you enter only a single keyword, the total hit count shown reflects the results for that one keyword, and a keyword report isn't generated.
    - **Top items types**: Most frequent item types within search hits matching your query. This count is determined by *itemClass* for Exchange content and *ContentType* for SharePoint content.
    - **Indexing status**: Breakdown of unindexed (including partially indexed) and fully indexed data items.
    - **Top communication participants**: Senders or recipients for emails, Microsoft Teams chats, and calendar invites in Exchange locations.
    - **Top location type**: Hit count by location type (mailbox versus site).

Select **Regenerate view** to rerun the query and to review the most current results. Select **Download report** to combine all **Statistics** results into a single .csv file. When viewing the top 100 results for any trend area, select **Download report** for a .csv file of the top 100 results of the selected hit trend.

Note

Search statistics expire after 14 days. Re-run search statistics for any searches older than 14 days to view current statistics.

Running the **Generate statistics** process is also required to enable [sampling options](edisc-search-add-to-review-set#create-or-add-results-to-a-review-set) when adding search results to a review set.

### Understanding statistics and search results

Tip

For more information about how to use process report CSVs (Summary.csv, Locations.csv, Settings.csv) to investigate count differences, see [Process reports in eDiscovery](edisc-process-report).

Depending on when you run a search in eDiscovery, the statistics for the search can show different results. For example, if you run two searches with the exact same conditions but at different times, you likely see different statistics results. These differences might occur for the following reasons:

- **Your organization is active**: Because you have active users in a production environment, data in your organization is constantly moved, added, deleted, and retired. The same search conditions run against the same locations likely return different search results because the data in those locations changed between the time you ran the searches.
- **Transient errors**: When you run a search (or export or add to a review set), transient processing errors might occur, especially for large sets of data. These errors often happen because of processing timeouts and can be mitigated by breaking up searches into smaller date ranges and exporting the data in parallel. Always try to break up searches into smaller sizes with more specific search conditions and more targeted with selected locations. This approach helps the process run more efficiently with less chance of errors.
- **Location access**: Some scenarios cause locations included in a search to be invalid, not accessible, or time out during processing. When you compare the results between two searches with the same conditions, make sure the locations you searched successfully match. For example, a search against 1,000 locations might have one failed location in the first run and no failed locations in the second run. This example means the first run searched only 999 locations successfully and the second run searched 1,000 locations. The difference of one location is the reason why search results between two runs are different. Use the *locations.csv*[report](edisc-process-report) for search, export, and add to review set processes to view a comprehensive report on what locations were successful and what locations failed. Rerun searches for any failed locations.
- **User running the search**: Depending on the user starting the search process, the user might or might not have the compliance boundary or compliance search filter applied. This filter either filters locations based on mailbox properties or filters content based on content path (SharePoint sites). The results for the user might be limited if a compliance boundary or search permission filter is applied. For example, one user doesn't have a compliance boundary applied but a second user has a compliance boundary applied that restricts this user to user mailboxes and OneDrive sites to a specific region. A search by the first user returns all mailbox and OneDrive matches for the search conditions for all regions and a search for the second user returns only matches for mailboxes and OneDrive sites only for the allowed region.
- **Search results counts might vary across searches because of legal holds**: If you run the same search query at different times, the number of items in the search or export might differ. This difference can happen when items are edited or deleted between searches. For example, items under legal hold retain previous versions and might appear in later exports, while items not on hold might change or be removed if they no longer meet the hold criteria.
- **Search statistics are estimates**: Don't use these estimates to compare to OneDrive and SharePoint site storage. Estimates use index‑based approximations, so the estimated eDiscovery content size can differ. Site storage often includes data not reflected in eDiscovery estimates, such as file versions and items in the Recycle Bin. For a view of site content, use the [export process](edisc-search-export) rather than the statistics dashboard size estimation.

### Sample dashboard

If you select **Sample** as the initial result type for your search, you're automatically redirected to this dashboard when the search results complete. The search results for the **Sample** dashboard columns contain the following information for each item:

- **Subject/Title**: The subject or title of the items included in the sample.
- **Date**: The date the item was created or sent.
- **Sender/Author**: The sender or author of the item.

Samples let you inspect a representative subset of individual items and details for each item returned for the search. The number of samples per location and the number of sample locations defined in the search determine the number of sample items and location representation in the sample items.

Select a sample item to view the [Source](edisc-review-set-view#use-source-view) information for the item. If available for the item, this view displays a rich view of a selected item so that you can evaluate the relevancy of the item as it relates to the defined search data source and conditions.

Note

Sample items you generate are valid for 24 hours. If you generated the view more than 24 hours ago, regenerate the view to retrieve the latest samples matching your search query.

Select **Regenerate view** to rerun the query and review the most current results. Select **Download reports** to combine all **Sample** results into a single .csv file. Select **View settings** to view the settings applied to the sample view generation.

## Refine search results

Based on the estimates and statistics that the search returns, you can edit and refine the search. Change the data sources that the search includes and change the search query to expand or narrow the search. You can update and run the search again until you're confident that the search results contain the content that's most relevant to your case.

After you're satisfied with the search results, you can take the following actions:

- [Add search results to a review set](edisc-search-add-to-review-set)
- [Export the search results](edisc-search-export)
- [Create a hold](edisc-hold-create)

## Before you open a support ticket about unexpected search results

If your search returns **zero results, fewer results than expected, or items you weren't expecting**, work through this checklist before opening a ticket. Most `RFC` (request for clarification) tickets filed against eDiscovery search are resolved by one of the items in the following list.

| # | Check | Where to verify |
| --- | --- | --- |
| 1 | **Hold vs. search confusion**: A hold preserves content but doesn't surface it in search results until you run a search across the held locations. | [Create holds in eDiscovery](edisc-hold-create) |
| 2 | **Indexing lag**: Newly ingested or recently modified items can take time to appear in the index. Re-run the search after the lag window. | [Limits in eDiscovery — Indexing limits](edisc-ref-limits#indexing-limits) |
| 3 | **Partially indexed items**: Encrypted, oversized, or unsupported-format items aren't returned by content queries. You must export them separately as partially indexed items. | [Partially indexed items in eDiscovery](edisc-ref-partially-indexed-items) |
| 4 | **Location scope**: Confirm you add every relevant mailbox, site, group, and Teams location as a data source to the search. Add inactive mailboxes and group members explicitly. | [Data sources in eDiscovery](edisc-data-sources) |
| 5 | **RBAC and permission filters**: Search permission filters and case-level RBAC silently scope results to what the searcher is entitled to see - even when running the search as an admin. | [Search permission filtering](edisc-search-permission-filtering) and [Assign permissions in eDiscovery](edisc-permissions) |
| 6 | **Region or sovereign cloud**: Confirm the data source is in the same Microsoft 365 cloud and region as the case. You can't search cross-boundary data from the wrong cloud. | [Compliance boundaries in eDiscovery](edisc-compliance-boundaries) |
| 7 | **Recipient expansion behavior**: Departed users whose Microsoft Entra ID object was deleted aren't expanded. You must add their historical SMTP addresses, aliases, and display names manually. | [Recipient expansion](edisc-search-mailboxes#recipient-expansion) |
| 8 | **Recent service changes**: Check the Microsoft 365 Message Center for service changes (for example, security-filter or Teams-private-channel changes) that affect search scope or results. | Microsoft 365 admin center → Message center |

If you complete all eight checks and the result is still unexpected, capture the exact KeyQL of the search, the case ID, the data sources selected, and the run timestamp before opening a ticket. Support's first request is always for these four items.

## Differences between statistics and export results

Tip

For guidance on interpreting the Summary.csv and Locations.csv reports that explain count differences for a specific process, see [Interpret count differences between search and export](edisc-process-report#interpreting-count-differences-between-search-and-export).

When you run an eDiscovery search, the statistics return an estimate of the number of items (and their total size) that match the search criteria. However, the size and number of actual exported search results that you download differ from the estimated size and number of search results.

Several potential reasons explain these differences:

- **The way results are estimated**: The estimate provides an estimate (and not an actual count) of the items that meet the search query criteria. To compile the estimate of Exchange items, eDiscovery requests from the Exchange database a list of the message IDs that meet the search criteria. But when you export the search results, the search reruns and the actual messages are retrieved from the Exchange database. Differences might result because of how the estimated number of items and the actual number of items are determined.
- **The way size of results is estimated**: During the estimate, size is approximated. The system gathers large numbers of items and sums the sizes up using approximations. You should consider the size estimate as an order of magnitude, not a specific measure of size. For example, a size estimate of 10 MB indicates the data is expected to be between 1 MB and 100 MB. The larger the number, the more variance there is in the estimate.

    - For Exchange-based content, file size is the size of the text in the message and attachment bytes. When exported, the format is converted to .msg and added to .pst or .zip files. Both these operations can significantly impact size.
    - For SharePoint-based content, the file size is approximate bytes of the file. In many cases for SharePoint-based data, file size can't be estimated during search.
- **Changes that happen between the time when estimating and exporting search results**: When you export search results, the search restarts to collect the most recent items in the search index that meet the search criteria. It's possible additional items were created, sent, or received that meet the search criteria in the time between when the estimated search results were collected and when the search results were exported. It's also possible that items that were in the search index when the search results were estimated are no longer there because they're purged from the content location before the search results are exported. To mitigate this problem, specify a date range for an eDiscovery search or place a hold on content locations so that items are preserved and can't be purged.

    Other issues that can result in differences between estimated and exported search results include:

    - An increase in items when using a date query. This issue is typically caused by the following two things:

        - **Hold versioning in SharePoint**: If a document is deleted from a site that's on hold and document versioning is enabled, all versions of the deleted document are preserved.
        - **Calendar items**: Accept and reject messages and recurring meetings automatically continue creating new items in the background with old dates.
    - With holds, there can be cases where the same item is preserved in a user's primary mailbox and in their archive mailbox. This situation can happen when a user manually moves an item to their archive.
    - Although rare, even in the case when a hold is applied, maintenance of built-in calendar items (which aren't editable by the user, but are included in many search results) might be removed from time to time. This periodic removal of calendar items results in fewer items that are exported.
- **Unindexed items**: Items that are unindexed for search can cause differences between estimated and actual search results. You can include unindexed items when you export the search results. If you include unindexed items when exporting search results, there might be more items that are exported. This difference causes a difference between the estimated and exported search results.

    When using search, you can include unindexed items when you export search results. The number of unindexed items returned by the search is listed on the [statistics](edisc-search-results#statistics-dashboard) page. When you export search results, you can choose to include or not include unindexed items. How you [configure these options](edisc-search-export#export-search-results) might result in differences between estimated and the actual results exported.
- **Document versions in SharePoint and OneDrive**: When searching SharePoint sites and OneDrive accounts, multiple versions of a document aren't included in the count of estimated search results. But you have the option to include document versions when you export the search results. If you include document versions when exporting search results, the actual number (and total size) of the exported items increases.
- **SharePoint folders**: If folders in SharePoint match a search query, for example, searching by date, the search estimate includes a count of those folders with the last modified date range (but not the items in those folders). When you export the search results, you have the option to choose export items inside subfolders of a matched folder or only include items that match search query. This option can affect the number of exported items. If a folder is empty, then the number of actual search results exported is reduced by one item, because the actual folder isn't exported.
- **SharePoint lists**: If the name of a SharePoint list matches a search query, the search estimate includes a count of all the items in the list. When you export the search results, the list (and the list items) is exported as a single CSV file. You can choose export setting that include list attachments, the attachments are exported as separate documents, which might increase the number of items exported.
- **Raw file formats versus exported file formats**: For Exchange items, the estimated size of the search results is calculated by using the raw Exchange message sizes. However, email messages are exported in a PST file or as individual messages. Both of these export options use a different file format than raw Exchange messages, which results in the total exported file size being different than the estimated file size.