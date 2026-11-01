---
layout: Conceptual
title: Records management for documents and emails in Microsoft 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/records-management
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2025-08-25T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-records-management
ms.collection:
- purview-compliance
- highpri
search.appverid:
- MOE150
- MET150
ms.custom:
- admindeeplinkCOMPLIANCE
- seo-marvel-apr2020
- seo-marvel-jun2020
- sfi-ga-nochange
description: Learn how Microsoft Purview Records Management supports high-value items for business, legal, or regulatory record-keeping requirements.
locale: en-us
document_id: 9f02c12f-33e0-2c57-6d1c-a6695d59e430
document_version_independent_id: 9f02c12f-33e0-2c57-6d1c-a6695d59e430
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/records-management.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: records-management
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/records-management.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 9d162429-eedc-dbd6-56a8-5f24d098be6e
---

# Records management for documents and emails in Microsoft 365 | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

A records management system, also known as records and information management, is a solution for organizations to manage regulatory, legal, and business-critical records. Records management for Microsoft Purview helps you achieve your organization's legal obligations, provides the ability to demonstrate compliance with regulations, and increases efficiency with regular disposition of items that are no longer required to be retained, no longer of value, or no longer required for business purposes.

Use the following capabilities to support your records management solution for Microsoft 365 data:

- **Label items as a record**. Create and configure retention labels to mark items as a record that can then be applied by users or automatically applied by identifying sensitive information, keywords, or content types.
- **Migrate and manage your retention requirements with file plan**. By using a [file plan](file-plan-manager), you can bring in an existing retention plan to Microsoft 365, or build a new one for enhanced management capabilities.
- **Configure retention and deletion settings with retention labels**. Configure [retention labels](retention#retention-labels) with the retention periods and actions based on various factors that include the date last modified or created.
- **Start different retention periods when an event occurs** with [event-based retention](event-driven-retention).
- **Review and validate disposition** with [disposition reviews](disposition#disposition-reviews) and proof of [records deletion](disposition#disposition-of-records).
- **Export information about all disposed items** with the [export option](disposition#filter-and-export-the-views).
- **Set specific permissions** for records manager functions in your organization to [have the right access](/en-us/microsoft-365/security/office-365-security/scc-permissions).

Using these capabilities, you can incorporate your organization's retention schedules and requirements into a records management solution that manages retention, records declaration, and disposition, to support the full lifecycle of your content.

In addition to the online documentation, you might find it useful to download a [deck with FAQs](https://aka.ms/MIPC/Blog-RecordsManagementWebinar) from a records management webinar. The recording of the actual webinar is no longer available.

## Records

When an item is declared a record by using a retention label:

- Restrictions are placed on the item in terms of what actions are allowed or blocked.
- Additional activities about the item are logged.
- You have proof of disposition when the item is deleted at the end of their retention period.

You use [retention labels](retention#retention-labels) to mark items as a **record**, or a **regulatory record**. The difference between these two are explained in the next section. You can either publish those labels so that users and administrators can manually apply them to items, or for labels that mark items as a record, you can auto-apply those labels.

By using retention labels to declare records, you can implement a single and consistent strategy for managing records across your Microsoft 365 environment.

### Compare restrictions for what actions are allowed or blocked

Use the following table to identify what restrictions are placed on items as a result of applying a standard retention label, and retention labels that mark items as a record or regulatory record.

A standard retention label has retention settings and actions but doesn't mark items as a record or a regulatory record.

Note

For completeness, the table includes columns for a locked and unlocked record, which is applicable to SharePoint and OneDrive, but not Exchange. The ability to lock and unlock a record uses [record versioning](record-versioning) that isn't supported for Exchange items. So for all Exchange items that are marked as a record, the behavior maps to the **Record - locked** column, and the **Record - unlocked column** is not relevant.

| Action | Retention label | Record - locked | Record - unlocked | Regulatory record |
| --- | --- | --- | --- | --- |
| Edit contents | Allowed | **Blocked** | Allowed | **Blocked** |
| Edit properties, including rename | Allowed | Allowed ^1^ | Allowed | **Blocked** |
| Delete | Allowed ^2^ | **Blocked** | **Blocked** | **Blocked** |
| Copy | Allowed | Allowed | Allowed | Allowed |
| Move within container ^3^ | Allowed | Allowed | Allowed | Allowed |
| Move across containers ^3^ | Allowed | Allowed if never unlocked | **Blocked** | **Blocked** |
| Open/Read | Allowed | Allowed | Allowed | Allowed |
| Change label | Allowed | Allowed - container admin only | **Blocked** | **Blocked** |
| Remove label ^4^ | Allowed | Allowed - container admin only | **Blocked** | **Blocked** |
| Override with [priority cleanup](priority-cleanup) | Allowed | **Blocked** | **Blocked** | **Blocked** |

Footnotes:

^1^ Editing properties for a locked record is allowed by default but can be blocked by a tenant setting in the [Microsoft Purview portal](purview-portal): [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Settings** &gt; **Solutions settings** &gt; **Records Management** &gt; **Retention Labels** &gt; **Allow editing of record properties**

^2^ Deleting labeled items in SharePoint and OneDrive can be blocked as a tenant setting in the [Microsoft Purview portal](purview-portal): [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Settings** &gt; **Solutions settings** &gt; **Records Management** &gt; **Retention Labels** &gt; **Deletion of items**.

When you apply a standard retention label to a list item that has a document attachment, that document doesn't inherit the retention settings and can be deleted from the list item. In comparison, if that retention label marked items as a record or regulatory record, the document attachment would inherit the retention settings and couldn't be deleted.

^3^ Containers include SharePoint sites, OneDrive accounts, and Exchange mailboxes.

^4^ Labels can be removed from items even if the labels are no longer published.

Important

The most important difference for a regulatory record is that after it is applied to content, nobody, not even a global administrator, can remove the label.

Retention labels configured for regulatory records also have the following admin restrictions:

- The retention period can't be made shorter after the label is saved, only extended.
- These labels aren't supported by auto-labeling policies, and must be applied by using [retention label policies](create-apply-retention-labels).

In addition, a regulatory label can't be applied to a document that's checked out in SharePoint.

Because of the restrictions and irreversible actions, make sure you really do need to use regulatory records before you select this option for your retention labels. To help prevent accidental configuration, this option is not available by default but must first be enabled by using PowerShell. Instructions are included in [Declare records by using retention labels](declare-records).

## Validating migrated records

If you're migrating files to SharePoint or OneDrive and your organization needs to manage these items as records, you might need to validate that the files haven't been altered and retain their immutability status. For example, you're using a migration solution and need to meet the chain of custody requirements. Typical file properties and methods often used for this type of validation, such as file size or file hash, might not be sufficient because SharePoint automatically updates the metadata for a file when it's uploaded.

Instead, to validate your migrated files, you can use the value of the `vti_writevalidationtoken` property, which is a base64-encoded XOR hash of the file before it is modified by SharePoint. Use the following steps:

1. Generate the XOR hash of the original file by using the QuickXorHash algorithm. For more information, see the [QuickXorHash Algorithm code snippet](/en-us/onedrive/developer/code-snippets/quickxorhash).
2. Base64-encode the XOR hash. For more information, see the [Base64Encode method documentation](/en-us/windows/win32/seccrypto/utilities-base64encode).
3. After the file is migrated, retrieve the value of the `vti_writevalidationtoken` property from the uploaded file.
4. Compare the value generated in step 2 with the value retrieved in step 3. These two values should match. If they do, you've validated that the file hasn't changed.

## Configuration guidance

See [Get started with records management](get-started-with-records-management). This article has information about subscriptions, permissions, and links to end-to-end configuration guidance for records management scenarios.