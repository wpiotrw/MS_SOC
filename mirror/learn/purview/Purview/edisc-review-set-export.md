---
layout: Conceptual
title: Export items from a review set in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-review-set-export
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about exporting items from a review set with eDiscovery in the Microsoft Purview portal.
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
document_id: 7e41c517-1956-7709-b385-6879bb3c96a7
document_version_independent_id: 7e41c517-1956-7709-b385-6879bb3c96a7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-review-set-export.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-review-set-export
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-review-set-export.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/a3955c7b-f5ee-420d-aff5-d7119738f38b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31948f4-2f38-404b-ac93-c3c8c5b3ae33
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: efd49022-c8cd-8fa4-5939-54559b7cf838
---

# Export items from a review set in eDiscovery | Microsoft Learn

The export feature lets you customize the content that's included in the download package when you export items from a review set in eDiscovery. Export processes are retained for the life of the case. However, you must download the content from an export process within 30 days after the export process completes.

Tip

Do you prefer an interactive configuration guide experience? Check out the [Export data](https://mslearn.cloudguides.com/guides/Export%20data%20with%20Microsoft%20Purview%20eDiscovery) guide.

To export documents from a review set, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery permissions.
2. Select the **eDiscovery** solution card, then select **Cases** in the left navigation.
3. Select a case, then select the **Review sets** tab.
4. Select the review set that you want to export and select the **All items** tab.
5. In the review set, select the items to export.
6. Select **Action** &gt; **Export** on the command bar.
7. The **Export** flyout page appears with the settings to configure the export. Some options are selected by default, but you can change these options. See the export options section for descriptions of the options that you can configure.
8. After you configure the export options, select **Export** to start the export process. Go to the **Process manager** to track the progress and to download exported content.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Choose export options for a review set

Use the following options to configure the export. Some output options don't allow all options. For example, when exporting to the PST format, you can't export text files or redacted PDFs.

- **Export name**: Name of the export job. This value names the downloaded ZIP files.
- **Description for the export**: Free-text field for you to add a description.
- **Select items to include in your export**

    - **Selected documents only**: This option exports only the documents that you currently selected. This option is only available when you select items in a review set.
    - **All filtered documents**: This option exports the documents in an active filter. This option is only available when you apply a filter to the review set.
    - **All documents in the review set**: This option exports all documents in the review set.
- **Expand selected documents to include**: Use the following options to export additional items that are related to filtered or selected items in the review set:

    - **Associated family items**: This option includes associated family items. Family items are items that share the same [*FamilyId* metadata property](edisc-ref-document-metadata-fields) value. For example, a document that's attached to an email message shares the same *FamilyId* as the email message. If you select this option, the email message and the document are exported in this example, even though the document might not be included in the list of review set items.
    - **Associated conversation items**: This option includes associated items that are in the same Teams or Viva Engage conversation. Conversation items are items that share the same [*ConversationId* metadata property](edisc-ref-document-metadata-fields) value. All messages, posts, and corresponding transcript file of a conversation share the same *ConversationId*.

        If you select **Associated family items** or **Associated conversation items**, all items that share the same association ID are exported, even though some of those items might not be in the results of the current review set query.
- **Export type**: Exported content is either available for download directly through a web browser or can be sent to an Azure Storage account. The **Export item report only** and **Export items with item report** options enable direct download.

    - **Export item report only**: Only the summary and item report are created. When you select “Export item report only,” the various options for organizing data, folder and path structure, condensing paths, and other options are hidden to avoid any confusion.

        - *Export tags*: Includes tags you created and applied during review in the Item report.
    - **Export items with item report**: Items are exported with the item report.

        - *Export redaction*: When selected, items in the export package that have committed redactions are delivered as the redacted PDF (`{itemId}_burn.pdf`) instead of the original native file. Specifically:

            - **Individual documents and email attachments** with committed redactions: the native file is **replaced** by the redacted PDF in the export package. The original native isn't included alongside.
            - **Conversations** (for example, Microsoft Teams or Viva Engage threads): both the native conversation file and the redacted PDF are included.
            - **Extracted text** files for redacted items contain the OCR'd text from the redacted PDF, not the original text.
            - **Family expansion** applies to redaction the same way it applies to the rest of the export: a redacted child attachment of a responsive parent is included as the redacted PDF.

            If you need both the original native file and the redacted PDF for the same item, run two exports — one with *Export redaction* selected and one without — and combine the packages.

            If you don't select this option, the export contains original native files only, even for items that have committed redactions.
        - *Export text files*: This option exports the extracted text of the document in a separate file.
        - *Export tags*: This option includes tags you created and applied during review in the Item report.
        - *Convert supported file formats to HTML*: This option converts supported cloud-native file formats, such as `.loop` and `.page` files (used by Copilot Notebook and Page content), to HTML during export. This option is useful when your organization's post-export workflows support HTML but lack tooling for native cloud file formats. This option isn't selected by default.
- **Export format**: Exported content options for Exchange items.

    - **Create PSTs for messages where possible**: This option creates .pst files for messages.
    - **Create .msg files for messages**: This option creates .msg files for messages.

        The following settings control whether the output package contains splits based on location of the item and whether to include folder structure and naming convention.
    - In the **Package size settings** section, configure the maximum export package size the export process creates.

        - If you chose *Create PSTs for messages*, you can configure the Maximum PST package size to 1 GB, 2 GB, 5 GB (default), or 10 GB.
        - You can configure the maximum .zip package size to 2 GB, 10 GB (default), 20 GB, or 40 GB. The maximum .zip package size needs to be the same or greater than the maximum PST package size to contain the PST files in .zip packages when downloaded.
        - Select one or more of the following options:

            - **Organize data from different locations into separate folders or PSTs**: This option organizes data into separate folders for each data location. When exporting mailbox content, items from the primary mailbox and any associated archive mailboxes (including multiple archives) are merged into a single PST file, even if this export option is selected.
            - **Include folder and path structure of the source**: This option includes the original folder and folder path structure for items.
            - **Condense paths to fit within 259 characters**: This option condenses the folder path for each item to 259 characters or less.
            - **Give each item a friendly name**: This option creates a friendly name for each item.

            The option for a condensed directory structure was previously available in the legacy eDiscovery experience. For a similar experience, deselect the following options in the **Export format** section:

            - *Organize data from different locations into separate folders or PSTs*
            - *Include folder and path structure of the source*
            - *Give each item a friendly name*

For more information about export file types and `item.csv` report fields, see [Document metadata fields in eDiscovery](edisc-ref-document-metadata-fields).

## Monitor your export process and view export settings

After you submit your export process, you can monitor the progress in the [Process manager](edisc-process-managers). You can also view the settings you chose for the export and download information for this export process in a consolidated report. If you're working with Microsoft support, you can copy process job information to share with your support representative.

To improve export performance, reduce the size of the exported package using date ranges or other types of filters to decrease the total size of the search results. If an export runs for more than seven days without completing, it's automatically canceled. To prevent cancellation, divide exports into smaller batches.

## View completed exports from a review set

To view a list and details about completed exports from a review set, select the **Exports** tab in a case. On the **Exports** tab, you see the following details for each export process:

- **Export name**: The name of the export.
- **Status**: The current status of the export process.
- **Review set name**: The name of the review set from which the export was created (when the export is created from a review set).
- **Search name**: The name of the search from which the export was created (when the export is created from a search).
- **Created**: The UTC date and time the export was created.
- **Completed**: The UTC date and time the export was completed.
- **Duration**: The duration of the export process.
- **Created by**: The user that created the export process.

Tip

You can configure the [Microsoft Purview eDiscovery API](edisc-ref-api-guide) to enable the programmatic download of export packages and the reports from an export process in an eDiscovery case.