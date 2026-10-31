---
layout: Conceptual
title: Export search results in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-search-export
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about exporting search results for a case in eDiscovery in the Microsoft Purview portal.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-23T00:00:00.0000000Z
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
ms.custom: msecd-doc-authoring-1015
locale: en-us
document_id: 8b3f107e-bdc7-8600-a589-fc29ee9fca65
document_version_independent_id: 8b3f107e-bdc7-8600-a589-fc29ee9fca65
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-search-export.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-search-export
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-search-export.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 9f470cfc-88da-9a68-595e-a945ecc770c2
---

# Export search results in eDiscovery | Microsoft Learn

After you run a search associated with a Microsoft Purview eDiscovery (preview) case, you can export the search results. When you export search results, you download mailbox items in PST files or as individual messages. When you export content from SharePoint and OneDrive sites, you export copies of native Office documents and other documents. When you export items, you prepare the items for download depending on the export options that you define. You can monitor the export's progress and download the results from the **Process manager** page. Larger exports might take longer to complete.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

For more information about new eDiscovery export enhancements and the retirement of the Microsoft Office 365 eDiscovery Export Tool, check out the following video: 

## Export considerations

This section describes important considerations when exporting content from eDiscovery. These considerations include requirements, limitations, and behaviors that might affect how content is accessed, exported, or logged.

- Search export packages expire 14 days after you create the export. After 14 days, the export and all data contained in the export package are automatically deleted and can't be recovered. To retain the exported data, download the export packages before the 14-day expiry. This expiry applies only to search exports, not to [review set exports](edisc-review-set-export).
- To export content in eDiscovery, assign the eDiscovery user a Microsoft 365 Enterprise E3 or E5 license. When exporting SharePoint content, the account must also have a Microsoft SharePoint E3 license; otherwise, SharePoint items might not export as expected.
- You can't export files that are [restricted by DLP action](dlp-policy-reference) in eDiscovery. These files can appear in search statistics results but are excluded from the export.
- You can't export content stored in SharePoint sites that are in a **Locked** state with **NoAccess**. When a site is locked, eDiscovery can't retrieve items from that site, and the content is skipped during export.
- You can't export individual files if they're restricted by SharePoint access controls. To export restricted files, the collecting user must have direct access to the content (for example, be a site admin, site owner, or the owner or last modifier of the document). Files that don't meet these access requirements might appear in search results but are excluded from export.
- When you add SharePoint items to a review set or export them from eDiscovery, a **FileAccessed** audit event might be recorded in the Microsoft 365 audit log. This event reflects that the eDiscovery service accessed the content to perform the requested operation.
- For large exports - especially tenant-wide search exports that target a large number of locations - running a **Generate statistics** process before exporting can significantly improve performance. When search statistics are available, eDiscovery uses those results to optimize the subsequent export process by limiting processing to only the locations that contain search hits, instead of reprocessing all locations in scope. This location optimization helps reduce process duration and improves reliability for large tenants. If the statistics process is outdated or the search query or data sources changed, eDiscovery processes all locations again to ensure accuracy. To confirm if your export has location optimization applied, refer to [settings.csv](edisc-process-report) of the export process report.

Note

Even if the **Generate statistics** process has errored locations, those locations are still included in the subsequent export process. If you retry the **Generate statistics** process, the subsequent export process doesn't have location optimization applied.

## Enable CMK (Customer Managed Key) for direct exports (preview)

Organizations that configure Customer Key through the Microsoft 365 Data-at-Rest Encryption Platform (MDEP) with a Data Encryption Policy (DEP) in policy assigned status can extend CMK protections to eDiscovery direct export packages. When enabled, exported investigation data is encrypted at rest using tenant-specific encryption scopes backed by customer-managed keys.

The following prerequisites are required to enable CMK for direct exports:

- The CMK direct export feature is enabled for your organization. To enable this feature, contact Microsoft Support or your Customer Success Account Manager (CSAM) and request CMK for eDiscovery direct exports for your tenant.
- Your organization configured Azure Key Vault following the standard Customer Key setup process. For more information, see [Set up Customer Key](customer-key-set-up).
- A Data Encryption Policy (DEP) is in *PolicyAssigned* state via the Microsoft 365 Data-at-Rest Encryption Platform (MDEP) onboarding cmdlets.

Note

This encryption applies to direct exports only. Data at rest in an eDiscovery review set isn't included at this time. Your tenant must remain CMK enabled at the time of the export.

## Export search results

Tip

Want an interactive configuration guide experience? Check out the [Export data](https://mslearn.cloudguides.com/guides/Export%20data%20with%20Microsoft%20Purview%20eDiscovery) guide.

To export search results, complete the following steps:

Tip

Your download speeds might be slower if you don't configure *Enable export download via pre-authorized link* in [eDiscovery export settings](edisc-settings-export).

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, and then select **Cases**.
3. Select a case, select the **Searches** tab, and then select a search query to export.
4. In the search query, select **Export**.
5. On the **Export** pane, configure export options.
6. Enter a name for the export in **Export name**. This field is required.
7. In **Export description**, enter an optional description for the export.
8. In **Tenant-wide source configuration** options, configure the organization-wide source "All people and groups" to include one or more user or content types:

    - **"All people and groups" should include unlicensed and on-premises users**
    - **"All people and groups" should include guest users**
    - **"All people and groups" should include shared Teams channels**
    - **"All people and groups" should include departed users**
9. In the **Select items to include in your export**, select one of the following options:

    - *Indexed items that match your search query*: This option exports only the indexed items that matched the query.
    - *Indexed items that match your search query and partially indexed items that might not match query*: This option exports only the indexed items that matched the query and the partially indexed or unindexed items that might not completely match the query.
    - *Partially indexed items that might not match query*: This option exports only the partially indexed or unindexed items that might not completely match the query.

        For these options including partially indexed items, you can scope the partially indexed items further by selecting *Exclude partially indexed items in locations without search hits*. When you select this option, the export returns partially indexed items only from mailboxes and sites where the indexed search query already returned at least one match.

        Important

        This option scopes by **location** (a mailbox or a SharePoint or OneDrive site), not by Kusto Query Language (KQL) conditions. Partially indexed items aren't evaluated against your search query. If a location is responsive (has any indexed hit), every partially indexed item in that location is included, regardless of any path, URL, or property restriction in your query. If your scope is a single location, this option has no effect. For details and examples, see [Locations and the "in locations without search hits" option](edisc-ref-partially-indexed-items#locations-and-the-in-locations-without-search-hits-option).

        Note

        Partially indexed item settings made on the original search are for statistics and preview only. The authoritative include/exclude decision is made at export time using the options on this dialog. See [Search-time and export-time settings are independent](edisc-ref-partially-indexed-items#search-time-and-export-time-settings-are-independent).

        To apply your KQL conditions to partially indexed items, also select *Perform advanced indexing on partially indexed items*. Advanced indexing re-indexes the items so your query restrictions evaluate against them. [Learn more about advanced indexing in eDiscovery](edisc-ref-advanced-indexing).
10. In the **OneDrive and SharePoint items** section, select from the following document options:

    - **Select document versions**: Specify how many versions of SharePoint documents to export. Values are *Latest version only*, *Recent 10 versions*, *Recent 100 versions*, *All versions*.
    - **Select folder items**: Export items inside subfolders of a matched folder. Choose *Only include items that match search query* or *All items in folder (even if they don't match search query)*.
    - **Select items in lists and attachments (list expansion)**: Export files attached to SharePoint lists and their child items. Choose *All items in SharePoint list if any item matches search query*. If applicable, select *Include list attachments*.
11. In the **Messages and related items from mailboxes and Exchange Online** section, select one or more of the following options:

    - **Organize conversation into HTML transcript**: Contextual chat messages are threaded into HTML transcripts for ease of review and handling.
    - **Include Teams and Viva Engage conversations**: Include messages posted within a 12-hour window before and after each responsive item.
    - **Access links (cloud attachments) in messages**: Collect items from links to SharePoint or OneDrive.

        Important

        Including [cloud attachments](edisc-cloud-attachments) increases the size and quantity of your exported results. Items that are encrypted don't have embedded entities extracted including attachments. To collect cloud attachments from Shared Channels in Teams, the Shared Channel SharePoint site must be included in the search to include cloud attachments.

        To improve export performance, reduce the size of the export by using date ranges or other types of filters to decrease the total size of the search results. If an export runs for more than seven days without completing, it automatically cancels. To prevent cancellation, divide exports into smaller batches.

        When you search for emails or other mailbox content that might include cloud attachments, the cloud attachment link to a storage location in SharePoint or OneDrive is considered as attachments of the message file rather than separate documents.

        This behavior is similar to how a search returns emails with embedded local attachments. These attachments are retrieved as if they're part of the emails. Any compliance boundaries for SharePoint or OneDrive aren't reflected in the collection of cloud attachments included in responsive messages.

        Select a version for access links. Values are *Latest version only*, *Recent 10 versions*, *Recent 100 versions*, *All versions*.

        Important

        If you have versions as shared feature enabled, this option retrieves the version of the document when it was shared.
12. In the **Export type** section, choose one of the following options:

    - *Export items report only*: Only the summary and item report are created. The various options for organizing data, folder and path structure, condensing paths, and other structures are hidden.

    Note

    When you use the *Exporting items report only* option, all string fields in the CSV report are limited to the first 255 characters. This limitation might truncate some items with long compound paths. If you need the full details, use the *Export items with items report* option.

    - *Export items with items report*: This option exports items with the item report. Other export format options are available with this option in the **Export format** section.
13. In the **Export format** section, choose one of the following options:

    - *Create PSTs for messages*: This option creates .pst files for messages.
    - *Create .msg files for messages*: This option creates .msg files for messages.
14. In the **Package size settings** section, configure the maximum export package size the export process creates.

    1. If you select *Create PSTs for messages* in the previous step, set the maximum PST package size to 1 GB, 2 GB, 5 GB (default), or 10 GB.
    2. Set the maximum .zip package size to 2 GB, 10 GB (default), 20 GB, or 40 GB. The maximum .zip package size needs to be the same or greater than the maximum PST package size to contain the PST files in .zip packages when downloaded.
15. Select one or more of the following output package options. For details about each option, see Export package options.

    - *Organize data from different locations into separate folders or PSTs*: This option organizes data into separate folders for each data location. When exporting mailbox content, even if you select this export option, items from the primary mailbox and any associated archive mailboxes (including multiple archives) merge into a single PST file.
    - *Include folder and path of the source*: This option includes the original folder and folder path structure for items.
    - *Condense paths to fit within 256 characters*: This option condenses the folder path for each item to 256 characters or less.
    - *Give each item a friendly name*: This option creates a friendly name for each item.
16. Select **Export**.
17. When the export process starts, a confirmation dialog appears. Select **OK** to continue.

For more information about export file types and item.csv report fields, see [Document metadata fields in eDiscovery](edisc-ref-document-metadata-fields).

## Export package options

The export package options control how the system packages content in downloadable export packages. Depending on your needs and the post-export process an eDiscovery user needs to perform, adjust these options.

### Organize data from different locations into separate folders or PSTs

This setting controls whether the system groups exported content by its original source. This grouping includes specific mailboxes or specific OneDrive or SharePoint sites, or it combines these items into a single container.

Note

Exchange mailboxes store data from many applications, not only email. Some of the data from these applications might be converted to HTML and exported into separate `Items.zip` files. For example, the system might convert data from Microsoft Forms, Sway, and other apps. The list of applications in this category is evolving. These applications generally store data in the `/ApplicationDataRoot/` folder within a mailbox.

#### For Exchange Mailbox items

- **Selected**: The system exports each mailbox’s content into a separate PST file named after the mailbox (for example, *john.doe@contoso.com.pst*).
- **Not selected**: The system merges all mailbox content across the selected data sources into a single PST file (for example, *exchange.pst*), subject to the maximum PST size limit. If the combined data exceeds this limit, the system creates extra PST files.

#### For OneDrive and SharePoint items

- **Selected**: The system exports content into separate folders per site. Each folder is named after the site and the system places all files from that site in each folder to preserve site-level organization.
- **Not selected**: The system exports all content into a single folder regardless of the originating site. Use the [items.csv](edisc-process-report) to understand the original source location and other relevant metadata for the item.

### Include folder and path of the source

This setting determines whether the export preserves the original folder structure from the source. The source is the folder where items reside in an Exchange mailbox or OneDrive and SharePoint site.

#### For Exchange Mailbox items

- **Selected**: The exported PST retains the full folder hierarchy from the mailbox. For example, if a message is located in *Inbox &gt; Legal &gt; Q2*, this exact path is preserved inside the PST. This structure helps reviewers understand the original context and organization of the content.
- **Not selected**: All messages go to the root of the PST file, with no folder structure retained. While the messages are still exported, the original location within the mailbox is lost in the content itself. To find the original path of the item, review the [items.csv in process report](edisc-process-report).

In both cases, the export process creates one PST file per mailbox if you select the **Organize data from different locations into separate folders or PSTs** option. The **Include folder and path of the source** option only affects the internal folder structure within each PST.

#### For OneDrive and SharePoint items

- **Selected**: Files are exported with the full folder path preserved. For example, if a file is stored in *Department &gt; Legal &gt; Contracts &gt; Proposal.docx*, the entire path is recreated in the export package for this file. This structure mirrors the original site structure in which the file resides.
- **Not selected**: All files from a site go directly into a single folder for that site, without any subfolders. For example, if a file is stored in *Department &gt; Legal &gt; Contracts &gt; Proposal.docx*, the path is *SharePoint &gt; Items &gt; Proposal.docx*. This structure flattens the folder hierarchy and might mix files from different folders. To find the original folder structure of the item, review the [items.csv in process report](edisc-process-report).

### Condense paths to fit within 259 characters

This setting helps prevent unzipping errors caused by long file paths during export. This problem can happen when you export content from OneDrive and SharePoint sites where deeply nested items are inside many layers of folders.

OneDrive and SharePoint sites might have deeply nested folder structures and long file names. When you export content and select the option to preserve folder and path structure, the resulting file paths can exceed the Windows file system limit of 259 characters. This limit leads to the following error message when unzipping the export package:

`The file name(s) would be too long for the destination folder. You can shorten the file name and try again.`

To help avoid this issue, use this option as needed:

- **Selected**: The export process automatically truncates folder paths - by shortening folder names or collapsing intermediate folders - so that the total path length for each file stays within the 259-character limit. This setting helps ensure that you can unzip and access the export package without errors.
- **Not selected**: The export process preserves the full original folder path. While this setting maintains the most accurate representation of the source structure, it increases the risk of hitting the path length limit - especially for deeply nested OneDrive and SharePoint items.

Note

Different unzip utilities handle long file names and folder paths differently. The built-in extraction tool in Windows File Explorer might fail if the file name or path exceeds its character limit. Other non-Microsoft tools support longer paths and can extract these files successfully.

### Give each item a friendly name

This setting controls whether the export item uses its original friendly name or the unique GUID generated by eDiscovery.

#### For Exchange Mailbox items

Note

This setting doesn't apply when exporting Exchange items to PST format. Regardless of whether you select this option, email messages in PST exports always retain the original subject lines for the message title within the PST file.

When exporting as a .msg file:

- **Selected**: Exported .msg file uses the subject of the email.
- **Not selected**: Exported .msg file uses a system-generated GUID.

#### For OneDrive and SharePoint items

- **Selected**: Files are exported using the original file names. For example, a file named *Q2\_Budget\_Plan.docx* in SharePoint is exported with the exact same name in the export package.

    - If multiple files have the same name and the folder structure isn't preserved (the Include folder and path of the source option isn't selected), this situation might lead to file name collisions in the export folder. If this happens, the suffix is appended to the collided file names to differentiate the files.
    - When exporting versions, friendly names include version suffixes to distinguish between versions of the file. For example, *Project Plan.docx*, *Project Plan\_v1.docx*, and *Project Plan\_v2.docx*.
- **Not selected**: Files are exported using system-generated identifiers. This approach ensures uniqueness and avoids naming conflicts. For example, *Project Plan.docx* might be named b7f3a9c2-4e1e-4c9a-9f3e-2a1d8e7f9c1a.docx in the export package. Use the [items.csv in process report](edisc-process-report) to correlate the original title and other relevant metadata for the file.

## View the export process status

To view the progress of the export in the [Process manager](edisc-process-managers), select **Process manager** and the **Export** process. You can track the process status and download export packages.

The **Overview** tab shows a progress bar that displays the current status, number of locations, and number of items for the export. An estimated completion time and current elapsed time are displayed in hours, minutes, and seconds. The **Overview** tab also contains the following export information:

- **Name**: The name of the export.
- **Completed**: The UTC date and time the export process completed.
- **Duration**: The duration of the export process.
- **Status**: The current status of the export process.
- **Process type**: The *Export* process type value.
- **Created**: The UTC date and time the export was created.
- **Created by**: The user who created the export.

The **Settings** tab displays a summary of the export options you selected for the export process.

## View completed exports from a search

To view a list and details about completed exports from a search, select the **Exports** tab in a case. Search exports expire 14 days after creation. You can't download expired exports. On the **Exports** tab, you see the following details for each export process:

- **Export name**: The name of the export.
- **Status**: The current status of the export process.
- **Review set name**: The name of the review set from which the export was created (when you create the export from a review set).
- **Search name**: The name of the search from which the export was created (when you create the export from a search).
- **Created**: The UTC date and time the export was created.
- **Completed**: The UTC date and time the export was completed.
- **Duration**: The duration of the export process.
- **Created by**: The user that created the export process.

To delete an export that you created from a search, complete the following steps:

Important

Deleting an export removes the export and all data contained in the export package. This action doesn't delete data in the original location.

1. In a case, select the **Exports** tab.
2. Select a completed export from a previous search. You can't delete in progress exports.
3. Select the ellipsis by the export name, and then select **Delete**.
4. On the **Delete export** dialog, select **Yes**.

## Export packages

Important

Export package download links are for individual use only. Don't share them.

**Standard (signed-in) download links:** Each user must sign in. If someone else opens the link, they're prompted to sign in and must have access to the case and export. **Pre-authorized download links** (when **Enable export download via pre-authorized link** is turned on): These links act like bearer tokens. Anyone who has the link can download the export until the link expires. They're designed for reliable, resumable downloads by the user who generates them, not for sharing with others. Treat them like passwords and set the shortest practical expiration time. For more information, see Configure export settings in eDiscovery. To give other people access to case data, add internal users to the case with the appropriate role, or invite external users as guests ([guest accounts](edisc-settings-guest-users)) to review content in the case. Guests can't download exports. If external parties need the exported files, an authorized user should download them and share them through your organization's own access-controlled channels.

After the export process finishes, you can download export packages. You can download search export packages for 14 days from the export creation time. After 14 days, the export packages are automatically deleted. The **Export packages** section on the **Overview** tab lists the export packages and shows the package name and size. To download a package, select the package and select **Download packages**.

Tip

You can configure the [Microsoft Purview eDiscovery API](edisc-ref-api-guide) to enable the programmatic download of export packages and the reports from an export process in an eDiscovery case.

## Best practices for downloading export packages

To ensure a smooth download experience, consider the following best practices:

- **Use a supported, up-to-date browser**: Use the latest version of Microsoft Edge for the best export download experience. Older browser versions can have issues with the download mechanism.
- **Allow pop-ups from Microsoft Purview**: The download process triggers a pop-up window. Make sure your browser is configured to allow pop-ups from the Microsoft Purview site. For example, see instructions on [how to configure pop-ups on Microsoft Edge](https://support.microsoft.com/microsoft-edge/block-pop-ups-in-microsoft-edge-1d8ba4f8-f385-9a0b-e944-aa47339b6bb5).
- **Check your browser's automatic download settings**: If the **Automatic Downloads** setting is configured to *Ask* or *Block*, it might prevent multiple files from downloading at the same time. For export package downloads, configure this setting to *Allow* or adjust permissions for the Microsoft Purview portal site. For the Microsoft Edge browser, go to **Settings** &gt; **Privacy, search, and services** &gt; **Site permissions** &gt; **All permissions** &gt; **Automatic downloads** and confirm that the site is **Allowed to automatically download multiple files**.
- **Set your preferred download location**: By default, export packages save to your browser’s default download folder. If you want to choose where files are saved, update your browser settings to prompt for a download location each time. See instructions for [changing the downloads folder location in Microsoft Edge](https://support.microsoft.com/microsoft-edge/change-the-downloads-folder-location-in-microsoft-edge-4049e93b-0ef6-e44f-aca0-7d5f37a39294).
- **Check your organization's network configuration**: Ensure that your organization allows downloads from Microsoft Purview by verifying that all required endpoints and IP addresses are allowlisted. This verification includes enabling access to the Microsoft Purview export service and associated Azure storage endpoints. If your organization uses network security tools such as Zscaler, Microsoft Defender for Endpoint (MDE), or other proxy or firewall solutions, make sure these tools are configured to allow traffic to the export endpoints. In some cases, you might need to isolate specific endpoints from third-party security scanning to prevent download interference. For optimal performance and to avoid download interruptions, consider using a local drive (not a network share), and test your connection throughput to Azure endpoints. For detailed allowlist guidance, see [Microsoft 365 URLs and IP address ranges](/en-us/microsoft-365/enterprise/urls-and-ip-address-ranges?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json).
- **Test on a different network if downloads are slow**: If downloads are slow or stalling, try downloading on a different network (for example, a home network or mobile hotspot). If performance improves, the corporate network is likely the bottleneck due to firewall scanning, VPN overhead, or proxy throttling.
- **Enable parallel downloading in your browser settings**: Use parallel downloading to improve download speeds for large eDiscovery export packages. For example, use `edge://flags` in Microsoft Edge. This feature can significantly reduce wait times by allowing simultaneous file chunk downloads. This setting is also available for other chromium-based browsers.
- **Use a download manager**: A download manager can improve the reliability and speed of large file downloads. A download manager allows you to resume interrupted downloads and manage network fluctuations, which is especially helpful when downloading large export packages.
- **Split very large exports**: For exports of tens of gigabytes or more, consider breaking the export into smaller parts by splitting searches by date range or data source. Smaller export packages download faster and are less likely to stall due to network interruptions.
- **Allow first-party and third-party cookies** for the download sites. These sites include the following depending on the global location of the tenant:

    - **APC**: apc.proxyservice.ediscovery.svc.cloud.microsoft
    - **NAM**: nam.proxyservice.ediscovery.svc.cloud.microsoft
    - **EUR**: eur.proxyservice.ediscovery.svc.cloud.microsoft
    - **GCC**: gccm.proxyservice.ediscovery.gcc.svc.cloud.microsoft
    - **GCCH**: gcch.proxyservice.ediscovery.svc.usgovcloud.microsoft
    - **DOD**: dod.proxyservice.ediscovery.svc.usgovcloud.microsoft
- **Unzipping export files**: Data is compressed into a .zip file for improved performance and reliability. Avoid using the built-in Windows .zip utility. Use 7-Zip, WinZip, or similar tools for the best experience.
- **Verify timestamps after extraction**: Microsoft Purview eDiscovery doesn't modify or rewrite timestamps. The export preserves the authoritative date and time metadata from source Microsoft 365 workloads such as Exchange, SharePoint, OneDrive, and Microsoft Teams. When exporting content, these original timestamps are preserved in the export metadata and within the native file formats. However, local ZIP extraction tools may modify certain file properties. Use the [Items.csv report](edisc-process-report-use#items-csv-report) or internal file metadata to confirm original timestamp values.
- Disable **Tracking prevention for this site**: If enabled, it blocks downloads and should be turned off.