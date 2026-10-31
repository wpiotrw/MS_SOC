---
layout: Conceptual
title: Cloud attachments in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-cloud-attachments
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use eDiscovery to collect cloud attachments for review sets and to export from searches in a case.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
ms.date: 2026-02-27T00:00:00.0000000Z
manager: laurawi
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
ai-usage: ai-assisted
locale: en-us
document_id: c165e363-f93e-1240-28da-4620fa90dfea
document_version_independent_id: c165e363-f93e-1240-28da-4620fa90dfea
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-cloud-attachments.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-cloud-attachments
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-cloud-attachments.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
platformId: 963a519a-2fbe-1759-79bd-0b550b639e4c
---

# Cloud attachments in eDiscovery | Microsoft Learn

This article explains how eDiscovery handles cloud (modern or linked) attachments versus traditional (classic) attachments. Cloud attachments are links to files stored in SharePoint or OneDrive rather than embedded copies. Because a cloud attachment points to a live file stored in Microsoft 365 services that you can modify after sharing, eDiscovery offers options to collect the live file, the version that you shared, or multiple versions to preserve context. You can collect cloud attachments as part of the export or add to review set workflow.

## Collect cloud attachments

eDiscovery supports the following options for the collection of modern attachments:

- Live version of the linked document at the moment of collection.
- Version at the time of sharing.
- Other version options (collect all versions or specific shared versions).

Regardless of the location of the modern attachment, the process attributes the *Custodian* property to the owner of the message. For example, if User A shares a linked attachment with User B that resides in User C's OneDrive and you collect the message from User B's mailbox, the linked attachment belongs to User B (custodian) and not User C.

To enable the collection of cloud attachments, select the **Access links (cloud attachments) in messages** option so linked content is included in [Add to review set](edisc-search-add-to-review-set) and [export](edisc-search-export) workflows.

Important

Including attachments increases the size and quantity of export results.

After the workflow process completes, you can group the modern attachment and parent message or email together by using **Group by conversations and related items** filter and the **Is modern attachment** column value.

## Considerations and unsupported scenarios

Before collecting cloud attachments, review the following considerations and scenarios:

- Plain text emails aren't supported. Only HTML emails are processed.
- Encrypted emails and messages don't support modern attachment extraction.
- Non-clickable links aren't supported. Links that aren't clickable aren't processed. Most links in emails are rewritten to clickable safelinks by the Exchange backends for opt-in tenants.
- Malformed URLs aren't supported. URLs that don't parse correctly aren't stamped.
- Maximum message body length. If the body length is greater than 100,000 characters, any content (modern attachment link) beyond this limit isn't considered.
- Maximum URL length. URLs longer than 2,048 characters are skipped.
- Maximum total property size. If the total property size exceeds 1 MB, it's dropped.
- Maximum number of links per message. Only the first 50 links in a message are processed. Other links beyond 50 are ignored.
- If a message is forwarded and the modern attachment link is expired or stale, the extraction doesn't work. Similarly, if the modern attachment file is renamed or moved, the link isn't extracted.
- Cloud attachment links in forwarded or replied emails aren't extracted from the quoted portion of the original message. Only the original email retains the cloud attachment association. If you need to collect a cloud attachment that was shared in the original email, search for and collect the original message rather than a forward or reply.
- Teams shared channel messages and posts don't support modern attachment link extraction. Users need to include the shared channel site and include the file manually as part of their collection.
- Cloud attachments are treated as part of the parent's message, not separate entities.
    - If an email or Teams message matches the condition of a search, its linked cloud attachments are retrieved - even if the file doesn't meet the condition of the search.
    - If an email or Teams message matches the condition of a search, its linked cloud attachments are retrieved - even if the file resides outside the compliance boundary.
- Advanced indexing isn't applied to cloud attachment files referenced within emails or messages. This limitation means the content of the cloud attachment file itself isn't processed by advanced indexing or OCR.
- Cloud attachment collection doesn't collect folder links or OneNote notebooks. It processes links to individual files only. It doesn't resolve or collect links to folders, document libraries, or OneNote notebooks stored as folders in SharePoint. If a user shares a link to a OneNote notebook in an email or Teams message, cloud attachment collection doesn't collect notebook content. To collect OneNote content, add the SharePoint site that contains the notebook as a search location. The system indexes individual OneNote section files (.one), and makes them searchable.

## Collecting the version shared in cloud attachments

By default, the eDiscovery workflow for collecting cloud attachments only includes adding the most current version of a cloud attachment to a review set or for export. This workflow means the version you collect and add to a review set or export might be different from the version that was originally shared in the cloud attachment. So, content that was present in the cloud attachment at the time it was shared might be removed and doesn't exist in the current version that's added to the review set or exported.

Use [retention labels](retention) to preserve the version of a document at the time when it was shared as a cloud attachment. To do this, create a retention label, choose the option to apply the label to cloud attachments, and then automatically apply the label to documents stored in SharePoint and OneDrive. After you set up this configuration, a copy of a document is created at the time when the file is shared. Also, if the document is modified and shared again as a cloud attachment, the modified version is also preserved. If the file is modified and shared again, a new copy of the file as a new version is preserved.

Preserving the shared versions of cloud attachments helps you scope the preservation and collection of potentially relevant content to the specific version of the document that you shared rather than the current live version. After you implement this retention solution, both the current live version of a cloud attachment and the version that you shared in the cloud attachment are collected and added to a review set or exported.

For instructions on setting up a retention label and automatically applying it to cloud attachments, see [Auto-apply labels to cloud attachments](apply-retention-labels-automatically#auto-apply-labels-to-cloud-attachments).

Additionally, the current live version and the version that you shared have the same **GroupID** property value, which is the same as the **GroupID** for the parent object (such as an email message or a Teams chat conversation). This property value lets you group cloud attachments with the item in which you shared them.

After you implement the retention label and auto-apply the label to SharePoint documents, select the option to collect cloud attachments when adding items to a review set. When you collect the cloud attachments, both the current live version and the version that was originally shared are added to the review set or exported.

## View in eDiscovery reports

eDiscovery includes a [Process manager](edisc-process-report) that lists all processes scoped for each area. Each process in the Process manager list contains a detailed report .zip file that contains detailed information about the process after the process completes.

### Summary CSV report

All reporting packages include a `Summary-*the date/time of the report*.csv` file. This file includes information related to cloud attachments. This report includes information about the following items:

- Cloud attachments
- Cloud attachments versions
- Cloud attachment versions at time of sharing

For more information about these areas, see [Summary CSV: Information](edisc-process-report-use#information).

### Items CSV report

Reporting packages also include an [Items CSV report](edisc-process-report-use#items-csv-report). In the `items.csv` file, you can:

- Filter on all modern attachments by using the property **Is modern attachment** = `True`.
- Correlate modern attachment with its parent email or message through group ID and the property **Has attachment** = `True`.