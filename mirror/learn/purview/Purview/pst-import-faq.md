---
layout: FAQ
title: Importing PST files FAQ | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/pst-import-faq
summary: >
  <p><strong>This article is for administrators. Do you want to import PST files to your own mailbox? See <a href="https://go.microsoft.com/fwlink/p/?LinkID=785075">Import email, contacts, and calendar from an Outlook .pst file</a></strong></p>

  <p>This article answers frequently asked questions about importing PST files to Microsoft 365 mailboxes. For requirements, limits, and planning guidance, see <a href="pst-import-overview">Learn about importing PST files</a>.</p>

  <p>For step-by-step instructions, see <a href="pst-import-network-upload">Use network upload to import PST files</a> or <a href="pst-import-drive-shipping">Use drive shipping to import PST files</a>. To learn about filtering imported data, see <a href="pst-import-filter-data">Filter data when importing PST files</a>.</p>
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.date: 2026-04-06T00:00:00.0000000Z
description: Frequently asked questions for administrators about importing PST files to Microsoft 365 mailboxes.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
audience: Admin
ms.topic: faq
ms.service: purview
ms.subservice: purview-exchange-legacy
ms.collection:
- purview-compliance
- import
search.appverid:
- MOE150
- MED150
- MET150
ms.assetid: 2fe71b05-f5a2-4182-ade7-4dc5cabdfd51
ms.custom: seo-marvel-apr2020
locale: en-us
document_id: a9a1ed8f-4c70-8dd7-4ce6-bff647e8cf74
document_version_independent_id: a9a1ed8f-4c70-8dd7-4ce6-bff647e8cf74
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/pst-import-faq.yml
site_name: Docs
depot_name: MSDN.Purview
page_type: faq
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: pst-import-faq
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/pst-import-faq.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 8c06f2cb-66bb-4816-9e29-f910d76fd521
---

# Importing PST files FAQ | Microsoft Learn

**This article is for administrators. Do you want to import PST files to your own mailbox? See [Import email, contacts, and calendar from an Outlook .pst file](https://go.microsoft.com/fwlink/p/?LinkID=785075)**

This article answers frequently asked questions about importing PST files to Microsoft 365 mailboxes. For requirements, limits, and planning guidance, see [Learn about importing PST files](pst-import-overview).

For step-by-step instructions, see [Use network upload to import PST files](pst-import-network-upload) or [Use drive shipping to import PST files](pst-import-drive-shipping). To learn about filtering imported data, see [Filter data when importing PST files](pst-import-filter-data).

## General

### How does the PST import process handle duplicate email items?

The PST import process uses a SourceEntryId-based matching system to detect duplicate items. During import, each PST item's EntryId is stamped as a SourceEntryId property on the imported item in the target mailbox. The import process then checks for this property to determine whether an item was previously imported.

It's important to understand how this matching works in different scenarios:

- **Reimporting the same PST file to the same target folder**. Items imported during a previous import job already have a SourceEntryId stamp. The import process matches on this property and skips the item, preventing duplicates.
- **First-time import of a PST file**. Items that already exist natively in the target mailbox (items that weren't previously imported from a PST file) don't have a SourceEntryId property. Because no match is found, the import process copies the PST item to the mailbox, which can result in duplicate items.
- **Importing a different PST file that contains overlapping content**. SourceEntryId values differ between PST files. Even if a different PST file contains the same email content, the import process doesn't find a matching SourceEntryId and copies the item, which can result in duplicates.
- **Reimporting the same PST file to a different target folder**. If you specify a different target folder (using the TargetRootFolder property in the PST import mapping file) than the one specified in a previous import job, all items in the PST file are reimported because the import process checks for matches only within the specified target folder.

The import process doesn't use content-based matching criteria such as message subject, date, body, or size to detect duplicates. The conflict resolution behavior (keeping the existing target item when a match is found) is built in to the import service and isn't configurable through the Microsoft Purview portal or the CSV mapping file.

### Are message properties, such as when the message was sent or received, the list of recipients and other properties, preserved when PST files are imported to a Microsoft 365 mailbox?

Yes. The original message metadata isn't changed during the import process.

### Are there any screen resolution requirements when I create an import job?

If the screen resolution on your local computer is set to 1366 x 768, you may have issues creating an import job. If so, we recommend that you change the screen resolution to a different setting and then create a new import job. We're working to fix this issue.

## Network upload

### After I upload my PST files to the Azure Storage area, how long are they kept in Azure before they're deleted?

When you use the network upload method to import PST files, you upload them to an Azure blob container named `ingestiondata`. If there are no import jobs in progress on the **Import PST files** page in the Microsoft Purview portal, then all PST files in the `ingestiondata` container in Azure are deleted 30 days after the most recent import job was created in the Microsoft Purview portal. That also means you have to create a new import job in the Microsoft Purview portal (described in Step 5 in the network upload instructions) within 30 days of uploading PST files to Azure.

This also means that after PST files are deleted from the Azure Storage area, they're no longer displayed in the list of files for a completed import job in the Microsoft Purview portal. Although an import job might still be listed on the **Import PST files** page in the Microsoft Purview portal, the list of PST files might be empty when you view the details of older import jobs.

## Drive shipping

### After I ship my hard drive, how long does it take to get to the Microsoft data center?

That depends on a few things, such as your proximity to the Microsoft data center and what kind of shipping option you used to ship your hard drive (such as, next-day delivery, two-day delivery, or ground-delivery). With most shippers, you can use the tracking number to track the status of your delivery.

### After Microsoft uploads my PST files to Azure, how long are they kept in Azure before they're deleted?

All PST files in the Azure Storage location for your organization (in blob container named `ingestiondata`), are deleted 30 days after the most recent import job was created on the **Import PST files** page in the Microsoft Purview portal.

This also means that after PST files are deleted from the Azure Storage area, they're no longer displayed in the list of files for a completed import job in the Microsoft Purview portal. Although an import job might still be listed on the **Import PST files** page in the Microsoft Purview portal, the list of PST files might be empty when you view the details of older import jobs.

### Can Microsoft wipe my hard drive before they ship it back to me?

No, Microsoft can't wipe hard drives before shipping them back to customers. Hard drives are returned to you in the same state they were in when they were received by Microsoft.

### Can Microsoft shred my hard drive instead of shipping it back to me?

No, Microsoft can't destroy your hard drive. Hard drives are returned to you in the same state they were in when they were received by Microsoft.

### What courier services are supported for return shipping?

If you're a customer in the United States or Europe, Microsoft uses FedEx to return your hard drive. For all other regions, Microsoft uses DHL.

### What are the return shipping costs?

Return shipping costs vary, depending on your proximity to the Microsoft data center that you shipped your hard drive to. Microsoft bills your FedEx or DHL account to return your hard drive. The cost of return shipping is your responsibility.

### Can I use a custom courier shipping service, such as FedEx Custom Shipping, to ship my hard drive to Microsoft?

Yes.

### If I have to ship my hard drive to another country/region, is there anything I need to do?

The hard drive that you ship to Microsoft might have to cross international borders. If so, you're responsible for ensuring that the hard drive and the data it contains are imported and/or exported in accordance with the applicable laws. Before shipping a hard drive, check with your advisors to verify that your drive and data can legally be shipped to the specified Microsoft data center. This helps to ensure that it reaches Microsoft in a timely manner.