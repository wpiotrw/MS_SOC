---
layout: Conceptual
title: Declare records by using retention labels | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/declare-records
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2024-03-26T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-records-management
ms.collection:
- purview-compliance
- SPO_Content
search.appverid:
- MOE150
- MET150
description: To declare documents and emails as records, use Microsoft 365 retention labels that mark items as a record or a regulatory record.
ms.custom: sfi-image-nochange
locale: en-us
document_id: f58fb37f-723b-6b95-a910-0f12331d7d3c
document_version_independent_id: f58fb37f-723b-6b95-a910-0f12331d7d3c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/declare-records.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: declare-records
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/declare-records.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e2560d35-6f40-44b4-a8f1-a6691f82061d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/2e5e1bdc-5c79-4dc1-9c05-485e6e6ae0ce
platformId: 639c1b41-093b-b5a9-4815-24e8da146383
---

# Declare records by using retention labels | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

To declare documents and emails as [records](records-management#records), you use [retention labels](retention#retention-labels) that mark the content as a **record** or a **regulatory record**.

If you're not sure whether to use a record or a regulatory record, see [Compare restrictions for what actions are allowed or blocked](records-management#compare-restrictions-for-what-actions-are-allowed-or-blocked). If you need to use regulatory records, you must first run a PowerShell command, as described in the next section.

You can then either publish those labels in a retention label policy so that users and administrators can apply them to content, or for labels that mark items as records (but not regulatory records), auto-apply those labels to content that you want to declare a record.

## How to display the option to mark content as a regulatory record

Note

The following procedure is an auditable action, logging **Enabled regulatory record option for retention labels** in the [Retention policy and retention label activities](audit-log-activities#retention-policy-and-retention-label-activities) section of the audit log.

By default, the retention label option to mark content as a regulatory record isn't displayed in the retention label wizard. To display this option, you must first run a PowerShell command:

1. [Connect to the Office 365 Security & Compliance PowerShell](/en-us/powershell/exchange/office-365-scc/connect-to-scc-powershell/connect-to-scc-powershell).
2. Run the following cmdlet:

    ```powershell
    Set-RegulatoryComplianceUI -Enabled $true
    ```

    There is no prompt to confirm and the setting takes effect immediately.

If you change your mind about seeing this option in the retention label wizard, you can hide it again by running the same cmdlet with the **false** value: `Set-RegulatoryComplianceUI -Enabled $false`

## Configuring retention labels to declare records

When you create a retention label from the **Records Management** solution in the Microsoft Purview portal, you have the option to mark items as a record. If you ran the PowerShell command from the previous section, you can alternatively mark items as a regulatory record.

For example:

![Configure a retention label to mark content as a record or regulatory.](media/declare-records.png)

Using this retention label, you can now apply it to SharePoint or OneDrive documents and Exchange emails, as needed.

For full instructions:

- [Publish retention labels and apply them in apps](create-apply-retention-labels)
- [Apply a retention label to content automatically](apply-retention-labels-automatically) (not supported for regulatory records)

## Tenant setting for editing record properties

If you'll use retention labels to declare items as records (rather than regulatory records) in SharePoint and OneDrive, consider whether you need to change the default tenant setting that allows users to edit the properties for a [locked record](record-versioning) when files are larger than 0 bytes.

To change this default, turn off the setting **Allow users to edit record properties**: [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Settings** &gt; **Solutions settings** &gt; **Records Management** &gt; **Retention Labels** &gt; **Allow users to edit record properties**

## Applying the configured retention label to content

When retention labels that mark items as a record or regulatory record are made available for users to apply them in apps:

- For Exchange, any user with write-access to the mailbox can apply these labels.
- For SharePoint and OneDrive, any user in the default Members group (the Contribute permission level) can apply these labels.

Example of a document marked as record by using a retention label:

![Details pane for document tagged as a record.](media/recordversioning7.png)

## Searching the audit log for labeled items that were declared records

The actions of labeling to declare items as records are logged in the audit log.

For SharePoint items:

- From **File and page activities**, select **Changed retention label for a file**. This audit event is for retention labels that mark items as records, regulatory records, or that are standard retention labels.

For Exchange items:

- From **Exchange mailbox activities**, select **Labeled message as a record**. This audit event is for retention labels that mark items as records or regulatory records.

For more information about these events, see [Audit log activities](audit-log-activities).