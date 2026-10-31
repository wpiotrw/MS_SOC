---
layout: Conceptual
title: Process reports in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-process-report
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to interpret process reports in Microsoft Purview eDiscovery to understand search results, export outcomes, hold status, and item-level details.
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
document_id: 62736332-2b4f-70ea-2da9-f208d2c9742a
document_version_independent_id: 62736332-2b4f-70ea-2da9-f208d2c9742a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-process-report.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-process-report
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-process-report.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: bbe1babd-4579-175c-b3ff-8a40d485cc06
---

# Process reports in eDiscovery | Microsoft Learn

Every process in Microsoft Purview eDiscovery generates a downloadable process report that contains detailed information about what happened during the process. This article provides scenario-based guidance for interpreting report data in depth. Use it to understand unexpected item counts, identify location errors, see how settings affected results, and know what to look for in reports when investigating specific outcomes.

For more information about the structure and contents of each report, see [Use process reports in eDiscovery](edisc-process-report-use).

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Best practices for using process reports

- **Download reports for every process**: Even when a process completes successfully, download the report package to keep a record of what was collected, from where, and with what settings. This information is valuable for transparency and audit purposes.
- **Check the Summary.csv first**: Start with the Summary CSV to get an overview of the process outcome, including item counts, errors, and the factors that affected the count.
- **Use the Items.csv for item-level investigation**: When you need to understand why a specific item was or wasn't included, look at the Items.csv for detailed per-item status and error information.
- **Use the Locations.csv for scope validation**: Verify that all intended locations were included and successfully processed. Identify any locations with errors that need attention.
- **Compare Settings.csv across processes**: When comparing the results of two processes, compare their Settings CSV reports to confirm the same configuration was used.
- **Use the Statistics.csv for search analysis**: After a *Generate statistics* process, use this report to understand the distribution of search hits across keywords, data types, sensitive information types, and communication participants.

## Understanding search result counts

Search result counts can vary between runs and differ from export or collection counts. For a detailed explanation of the behavioral reasons behind these differences, see [Understanding statistics and search results](edisc-search-results#understanding-statistics-and-search-results) and [Differences between statistics and export results](edisc-search-results#differences-between-statistics-and-export-results). The sections below explain how to use the process reports to investigate these differences.

### Investigating missing items in search results

If expected content doesn't appear in search results, use the process reports from your *Generate statistics* or *Generate sample* process to identify the cause.

What to look at in the process report:

- **Settings.csv — Partially indexed items setting**: Check whether the process was configured to include partially indexed items. By default, search results exclude content that isn't fully indexed, such as image-only files, unsupported file types, or items with processing errors. If the setting shows that the process didn't include partially indexed items, rerun the search with this option enabled to determine if the missing items are unindexed.
- **Settings.csv — Security filter applied**: If this value is *Yes*, a [compliance boundary](edisc-compliance-boundaries) (search permissions filter) limits which locations the search can access. The search silently excludes items in locations outside the filter scope. The **Location restriction** field shows the filter criteria. If you suspect the filter is excluding expected content, ask an eDiscovery administrator or another user without search permission filter applied to run the same search for comparison.
- **Locations.csv — Status column**: Check for locations with errors. If a location shows a failure status, the **ErrorWarning** field explains why. For more information about common reasons that can affect location access, see [Export considerations](edisc-search-export#export-considerations).
- **Locations.csv — Count column**: If a location you expected to have results shows a count of zero, the search query didn't match any content in that location. Verify the query is correct and that the content exists at the source. Items you recently added to a mailbox or site might not yet be indexed. Rerun the search after a short wait to resolve this condition.
- **Locations.csv — Missing locations**: If an expected location doesn't appear in the report at all, it wasn't included in the search scope. Verify the data sources configured for the search and add any missing mailboxes or sites.

Tip

When investigating missing items, start with the **Locations.csv** to confirm all expected locations were searched successfully, then check the **Settings.csv** to verify the right options were enabled. If both look correct and items are still missing, the content might be deleted or not yet indexed at the time of the search.

### Search result differences with tenant-wide searches

When you use a tenant-wide search scope such as **All people and groups**, the results can vary depending on additional source configuration settings that control which user and content types are included. These settings expand or narrow the scope of the search and directly affect item counts.

What to look at in the process report:

- **Settings.csv — Tenant-wide process settings**: When a search uses **All people and groups**, the [Settings CSV](edisc-process-report-use#settings-csv-report) captures which additional source types were enabled at the time of the search export or **Add to Review** set. Check these settings to understand why certain content was included or excluded:

    - **Include departed users**: When enabled, the search includes mailboxes and OneDrive sites of users who left the organization (soft-deleted or inactive accounts). If this setting wasn't enabled and you expected to find content from former users, it explains why those items are missing from results.
    - **Include shared Teams channels**: When enabled, the search includes content from shared Teams channels. Shared channel data is stored in separate SharePoint sites, so it's only included when this setting is active. If you're missing shared channel content, verify this setting was enabled.
    - **Include unlicensed and on-premises users**: When enabled, the search includes mailboxes for users who don't have a license or are synced from on-premises environments.
    - **Include guest users**: When enabled, the search includes content associated with guest user accounts in your tenant.

Note

You configure tenant-wide source settings at the process level. Including these settings increases the scope of the process and can affect performance.

### Interpreting count differences between search and export

When you export search results or add them to a review set, the final item count often differs from the original search estimate. For the full list of reasons, see [Differences between statistics and export results](edisc-search-results#differences-between-statistics-and-export-results). The [Summary CSV report](edisc-process-report-use#summary-csv-report) shows the specific factors that affected the count for your process.

What to look at in the process report:

- **Information section of Summary.csv**: This section lists every factor that increased or decreased the item count compared to the original estimate, such as cloud attachments, contextual conversations, consolidated transcripts, SharePoint file versions, and duplicates skipped in a review set. For a complete list of these factors and what each one means, see [Information section](edisc-process-report-use#information).
- **Search results section of Summary.csv**: Shows the breakdown of indexed items, partially indexed items, and advanced indexed items. If the count is lower than expected, check whether you included partially indexed items in the process settings. For more information, see [Assess partially indexed items in your organization](edisc-ref-partially-indexed-items#assess-partially-indexed-items-in-your-organization).
- **Error section of Summary.csv**: Shows retrieval exceptions — items that couldn't be exported or added to the review set. For the specific exception types tracked in this section, see [Error](edisc-process-report-use#error).
- **Sampling configured**: If you configured sampling (confidence-based or percentage-based) when adding search results to a review set, the item count in the review set is intentionally lower than the total search estimate. This reduction reflects the configured sample size, not a processing discrepancy. Check the [Settings CSV report](edisc-process-report-use#settings-csv-report) to confirm the sampling mode and parameters used.

### Understanding the impact of search settings on results

The [Settings CSV report](edisc-process-report-use#settings-csv-report) captures the exact configuration used when you submitted a process. Compare this report against your intended configuration to identify discrepancies.

Key settings that affect result scope include:

- **Include document versions**: Determines how many versions of each document are collected. Selecting *All versions* can significantly increase the item count and data volume.
- **Organize conversations into HTML transcripts**: When enabled, individual Teams chat messages consolidate into transcript files, which changes the item count.
- **Include contextual Teams and Viva Engage conversations**: When enabled, the search includes messages outside your search date range to provide conversation context. For 1:1 and group chats, this setting adds messages 12 hours before and after each responsive item. For Teams channel posts and Viva Engage posts, the search includes entire conversation threads regardless of date range. If you see items outside your expected date range, check whether this setting is enabled.
- **Access links in messages**: Controls whether the search retrieves cloud attachments from links in emails and Teams conversations.

## Understanding export reports

### Why certain items weren't exported

When an export finishes, the [Items CSV report](edisc-process-report-use#items-csv-report) and the **Error** section of the [Summary CSV report](edisc-process-report-use#summary-csv-report) explain what happened to each item.

What to look at in the export report:

- **Items.csv — Status column**: Each row represents an item. Items with a status other than success include an **ErrorWarning** field with the failure reason. Common reasons include:

    - **Item deleted or moved**: The search found the item, but someone removed or relocated it at the source between the time of the search and the export. These items count in the search estimate but can't be retrieved at export time.
    - **Access timeout**: The system couldn't retrieve the item within the allowed time, often due to a large file size or transient service issue.
    - **Permission or access issue**: The export process couldn't access the item, possibly because the source location is locked or the user account lacks access.
- **Items.csv — AddedBy column**: Shows how each item was included in the results. For definitions of each value, see [Items CSV report](edisc-process-report-use#items-csv-report).
- **Summary.csv — Retrieval exceptions**: Shows the total count of items that couldn't be exported. This count matches the number of error entries in the Items.csv file.

### Understanding file timestamps in exports

When you extract files from an export package, file timestamps might show the current date instead of the original modified date. This behavior occurs because the Windows built-in ZIP extractor resets file dates during extraction. The original timestamps are preserved in the **Items.csv** report and inside the file formats themselves.

To preserve timestamps during extraction, use a tool like 7-Zip, WinZip, or WinRAR. For emails in PST format, opening the PST in Outlook shows the original sent and received dates.

### Understanding export settings and traceability

The [Settings CSV report](edisc-process-report-use#settings-csv-report) serves as the authoritative record of the configuration used for an export. This report is essential for traceability and transparency, especially when responding to compliance inquiries.

Use this report to:

- Confirm which items were included (indexed, partially indexed, or both).
- Verify the export format (PST or .msg) and package size settings.
- Check whether decryption was enabled for Exchange or SharePoint content.
- Validate that the correct document version settings were applied.

## Understanding location reports

### Identifying which locations have results

The [Locations CSV report](edisc-process-report-use#locations-csv-report) provides a breakdown of every content location targeted during a search, export, or add to review set process. Each row represents a location and includes the item count and size.

What to look at in the location report:

- **Count column**: Shows the number of responsive items found in each location. Locations with a count of zero have no search hits for the query used.
- **Size column**: Shows the total size of responsive items from the location, in bytes.
- **Location Subtype column**: Distinguishes between different mailbox and site subtypes. A single user's SMTP address might appear in multiple rows if they have different mailbox subtypes. For the full list of subtype values, see [Locations CSV report](edisc-process-report-use#locations-csv-report).
- **Status column**: Shows whether the location was successfully processed. If a location failed, the **ErrorWarning** field includes the reason.

### Understanding location-level errors

Location-level errors in the Locations CSV report indicate that the process couldn't access a specific mailbox or site. Common errors include:

| Error | What it means | What to do |
| --- | --- | --- |
| **Permission or access issue** | The process can't access the mailbox or site. The user might be unlicensed, the site might be locked, or the searching account lacks permissions. | Verify the user's license status and that the site isn't [locked](/en-us/sharepoint/manage-lock-status?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json). Confirm that the eDiscovery admin or manager role has the required permissions, and then rerun the process. |
| **Timeout** | The location took too long to process. This error can happen with very large mailboxes or sites. | Rerun the process. If the timeout persists, narrow the search query or split the search to target fewer locations per run. |
| **Location not found** | The mailbox or site doesn't exist. The user might be deleted or the site URL might be incorrect. | Verify the user account or site URL in the Microsoft 365 admin center. If the user was deleted, use an [inactive mailbox](edisc-data-sources#inactive-mailboxes) or add the OneDrive URL directly as a SharePoint location. |

If a location has errors, it doesn't mean the entire process failed. Other locations might be processed successfully. Review the Locations CSV to identify which specific locations need attention.

## Understanding hold reports

### Interpreting hold distribution status

When you create or update a hold, the process report for the *Applying or updating hold* process includes a [Locations CSV report](edisc-process-report-use#locations-csv-report) that shows the status of each location in the hold.

What to look at in the hold report:

- **Status column**: Shows whether the hold was successfully applied to each location.
- **ErrorWarning column**: If a location failed, this field contains the specific error. Common hold distribution errors include:

    | Error | What it means | What to do |
    | --- | --- | --- |
    | **PolicySyncTimeout / PolicyNotifyError** | Transient errors. The hold took too long to apply. | Rerun the hold distribution. These errors usually resolve on retry. |
    | **FailedToOpenContainer** | The mailbox or site can't be accessed. The user might not have a mailbox, or the site doesn't exist. | Verify the user account status in the Microsoft 365 admin center and confirm the mailbox or site is active. |
    | **SiteInReadonlyOrNotAccessible / SiteOutOfQuota** | The SharePoint site or OneDrive is in a read-only state or has no storage quota left. | Contact your SharePoint admin to unlock the site or increase the storage quota, then rerun the hold. |
    | **RecipientTypeNotAllowed** | The hold was attempted on an ineligible object, such as a distribution group. Only user mailboxes, group mailboxes, and SharePoint or OneDrive sites can be held. | Remove the ineligible object and add the individual user mailboxes or sites instead. |

## Understanding the consumption summary

The **Consumption summary**[section](edisc-process-report-use#consumption-summary) of the [Summary CSV report](edisc-process-report-use#summary-csv-report) breaks down the data volume by content type. This information helps you understand storage and billing implications for processes that add data to a review set or export data.

Note

If you don't have an active pay-as-you-go subscription, data isn't exported or added to a review set. For more information, see [Enable Microsoft Purview pay-as-you-go features](purview-payg-subscription-based-enablement).