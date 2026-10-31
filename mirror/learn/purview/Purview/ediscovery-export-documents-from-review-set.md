---
layout: Conceptual
title: Export documents from a review set in eDiscovery (Premium) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-export-documents-from-review-set
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to select and export content from an eDiscovery (Premium) review set for presentations or external reviews.
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
ms.custom: seo-marvel-mar2020
locale: en-us
document_id: 14c5a0ff-4e05-9a20-b9fa-61ef728164ed
document_version_independent_id: 14c5a0ff-4e05-9a20-b9fa-61ef728164ed
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-export-documents-from-review-set.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-export-documents-from-review-set
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-export-documents-from-review-set.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/a9a12e3a-5d9d-4197-ad96-b826bc774b60
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6dfd60ec-b0d6-48ef-9c74-057162ea03fb
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 904d127d-ed8f-58ef-7e61-f894c11b5541
---

# Export documents from a review set in eDiscovery (Premium) | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Export allows users to customize the content that is included in the download package when you export document from a review set in eDiscovery (Premium).

To export documents from a review set:

Important

Exporting documents to your Azure Storage locations in eDiscovery was permanently **retired on August 31, 2025**, this functionality isn't available in the new [eDiscovery experience](edisc).

1. In the Microsoft Purview portal, open the eDiscovery (Premium) case, select the **Review sets** tab, and then select the review set that you want to export.
2. In the review set, select the items to export.
3. Select **Action** &gt; **Export**.

    The Export tool displays the flyout page with the settings to configure the export. Some options are selected by default, but you can change these. See the following section for descriptions of the export options that you can configure.

    ![Configuration options for exporting items from a review set.](media/ediscovery-review-set-export-options.png)
4. After you configure the export options, select **Export** to start the export process. Depending on the option that you selected in **Output options** section, you can access the export files by direct download or in your organization's Azure Storage account.

Note

Export jobs are retained for the life of the case. However, you must download the content from an export job within 30 days after the export job is complete.

## Export options

Use the following options to configure the export. Not all options are allowed for some output options, most notably, the export of text files and redacted PDFs aren't allowed when exporting to the PST format.

- **Export name**: Name of the export job. This is used to name the ZIP files that will be downloaded.
- **Description**: Free-text field for you to add a description.
- **Export these documents**

    - *Selected documents only*: This option exports only the documents that are currently selected. This option is only available when items are selected in a review set.
    - *All filtered documents*: This option exports the documents in an active filter. This option is only available when a filter is applied to the review set.
    - *All documents in the review set*: This option exports all documents in the review set.
- **Expand selection**: Use the following options to export additional items that are related to filtered/selected items in the review set:

    - *None*: This option doesn't export the family items or conversation items. It only exports the items that are selected or to all items in the review set list.
    - *Include associated family items*: This option includes associated family items. Family items are items that share the same [*FamilyId* metadata property](ediscovery-document-metadata-fields) value. For example, a document that's attached to an email message shares the same *FamilyId* as the email message. If this option is selected, the email message and the document are exported in this example, even though the document might not be included in the list of review set items.
    - *Include associated conversation items*: This option includes associated items that are in the same Teams or Viva Engage conversation. Conversation items are items that share the same [*ConversationId* metadata property](ediscovery-document-metadata-fields) value. All messages, posts, and corresponding transcript file of a conversation share the same *ConversationId*.

    If any option other than *None* is selected, all items that share the same association ID are exported, even though some of those items might not be in the results of the current review set query. For more information about conversation items, see [eDiscovery (Premium) workflow for content in Microsoft Teams](ediscovery-teams-workflow#grouping).
- **Output options**: Exported content is either available for download directly through a web browser or can be sent to an Azure Storage account. The first two options enable direct download.

    - *Reports only*: Only the summary and load file are created.
    - *Loose files and PSTs (email is added to PSTs when possible)*: Files are exported in a format that resembles the original directory structure seen by users in their native applications. For more information, see the Loose files and PST export structure section.
    - *Condensed directory structure*: Files are exported and included in the download.
    - *Condensed directory structure exported to your Azure Storage account*: Files are exported to your organization's Azure Storage account. For this option, you have to provide the URL for the container in your Azure Storage account to export the files to. You also have to provide the shared access signature (SAS) token for your Azure Storage account. For more information, see [Export documents in a review set to an Azure Storage account](ediscovery-download-export-jobs).

        Note

        Condensed output options include all extracted items. The item count for condensed output is always more than the *Loose files and PSTs* option because email and attachments are counted differently. For example, for an email with two attachments, the condensed output results in 3 items (1 item for the email and 1 item for each attachment) while the *Loose files and PSTs* option would result in 1 item for the email and all attachments.
- **Include**

    - *Tags*: When selected, tagging information is included in the load file.
    - *Text files*: This option includes the extracted text versions of native files in the export.
    - *Replace redacted natives with converted PDFs*: If redacted PDF files are generated during review, these files are available for export. You can choose to export only the native files that were redacted (by not selecting this option) or you can select this option to export the PDF files that contain the actual redactions.

The following sections describe the folder structure for loose files and condensed directory structure options. Exports are partitioned into ZIP files with a maximum size of uncompressed content of 75 GB. If the export size is less than 75 GB, the export consists of a summary file and a single ZIP file. For exports larger than 75 GB of uncompressed data, multiple ZIP files are created. Once downloaded, the ZIP files can be uncompressed into a single location to recreate the full export.

### Loose files and PST export structure

If you select this export option, the exported content is organized in the following structure:

- **Summary.csv**: Includes a summary of the content exported from the review set. This file is structured with the following columns:

    - *Total*: The number of the items found in the review set.
    - *Actual*: he number of items fetched in the package for the export.
    - *Errors*: The number of errors and warnings. More information can be found in the errors and warnings file. The warning and error file contains important information about the items that weren't exported. Check this file to make sure you understand which files have issues.
    - *Skipped Processing*: The number of items skipped for processing.

    Note

    Skipped processing also contains the number of extracted child items for PST format. For example, a review set has two items, one corresponding to an email and one corresponding to an attachment. When the file is converted to the PST, it is mappped to one item only (the mail item). This results in skipping the child attachment.

    - *Export Containers*: This contains the list of .zip and .pst files created for the export.
- Root folder: This folder in named [Export Name] x of z.zip and is repeated for each .zip file partition. The root folder contains the following:

    - *Export\_load\_file\_x of z.csv*: The metadata file.
    - *Warnings and errors x of z.csv*: This file includes information about errors encountered when trying to export from the review set.
- **Exchange**: This folder contains all content from Exchange stored in PST files. Redacted PDF files can't be included with this option. If an attachment is selected in the review set, the parent email message is exported with the attachment attached.

    The Exchange folder may also contain a subfolder named mailboxname\_loosefiles.zip, which contains the following items:

    - Information Rights Management (IRM) protected messages that have been decoded.
    - Error-remediated messages.
    - Modern attachments or links referenced in messages.
    - Encrypted items (which aren't included in the PST files in the Exchange folder).
- **SharePoint**: This folder contains all native content from SharePoint in a native file format. Redacted PDF files can't be included with this option.

Note

The *Group* option selected in the review set determines which items are included in the content exported from the review set. If *None* is selected, the exported content only includes the selected or filtered items. If *Group by family* is selected, the exported content includes all items in the family.

### Condensed directory structure

- **Summary.csv**: Includes a summary of the content exported from the review set. This file is structured with the following columns:

    - *Total*: The number of the items found in the review set.
    - *Actual*: he number of items fetched in the package for the export.
    - *Errors*: The number of errors and warnings. More information can be found in the errors and warnings file.
    - *Skipped Processing*: The number of items skipped for processing.

    Note

    Skipped processing also contains the number of extracted child items for PST format. For example, a review set has two items, one corresponding to an email and one corresponding to an attachment. When the file is converted to the PST, it is mappped to one item only (the mail item). This results in skipping the child attachment.

    - *Export Containers*: This contains the list of .zip and .pst files created for the export.
- **Root folder**: This folder in named [Export Name] x of z.zip and will be repeated for each ZIP file partition.

    - *Export\_load\_file\_x of z.csv*: The metadata file and also includes the location of each file that is stored in the ZIP file
    - *Warnings and errors x of z.csv*: This file includes information about errors encountered when trying to export from the review set.
    - *NativeFiles*: This folder contains all the native files that were exported. Natives files are replaced with redacted PDFs if you selected the *Replace redacted natives with converted PDFs* option.
    - *Error\_files*: This folder contains files that had either extraction or other processing error. The files are placed into separate folders, either ExtractionError or ProcessingError. These files are listed in the load file.
    - *Extracted\_text\_files*: This folder contains all of the extracted text files that were generated at processing.

### Condensed directory structure exported to your Azure Storage Account

This option uses the same general structure as the *Condensed directory structure*, the contents are zipped and the data is saved to your Azure Storage account. This option is used when working with a third-party eDiscovery provider. For details about how to use this option, see [Export documents in a review set to an Azure Storage account](ediscovery-download-export-jobs).