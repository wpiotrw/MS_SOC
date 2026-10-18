---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Place a mailbox on litigation hold - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/misc/create-litigation-hold-mac?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn how to place a mailbox on litigation hold, retaining mailbox content during an investigation.
f1.keywords:
- NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2026-07-28T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-admin
ms.localizationpriority: medium
ms.custom:
- admindeeplinkCOMPLIANCE
- compliance
ms.collection:
- tier1
- purview-compliance
- ediscovery
locale: en-us
document_id: f932e13c-cc30-b427-3c9a-88553fc8c289
document_version_independent_id: f932e13c-cc30-b427-3c9a-88553fc8c289
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/misc/create-litigation-hold-mac.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/misc/create-litigation-hold-mac
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/misc/create-litigation-hold-mac.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
platformId: 69bd43d8-2fe2-a4fe-a815-1047e876b88d
---

# Place a mailbox on litigation hold - Microsoft 365 admin | Microsoft Learn

You can place a mailbox on litigation hold to retain mailbox content, including deleted items and the original versions of modified items. When you place a user mailbox on litigation hold, content in the user's archive mailbox (if enabled) is also retained.

When you create a hold, you can specify a hold duration (also called a *time-based hold*) so that deleted and modified items are retained for a specified period and then permanently deleted from the mailbox. Or, you can retain content indefinitely (called an *infinite hold*) or until the litigation hold is removed.

If you specify a hold duration period, it's calculated from the date a message is received or a mailbox item is created.

Here's what happens when you create a litigation hold.

- Items that are permanently deleted by the user are retained in the **Recoverable Items** folder in the user's mailbox during the hold.
- Items that are purged from the **Recoverable Items** folder by the user are retained during the hold.
- The storage quota for the **Recoverable Items** folder is increased from 30 GB to 100 GB, or to 110 GB when [auto-expanding archiving](/en-us/purview/autoexpanding-archiving) is enabled.
- Items in the user's primary and the archive mailboxes are retained

## Assign an Exchange Online Plan 2 license

To place an Exchange Online mailbox on litigation hold, that mailbox must be assigned an Exchange Online Plan 2 license. If a mailbox is assigned an Exchange Online Plan 1 license, you must assign that mailbox a separate Exchange Online Archiving license to place it on hold.

## Place a mailbox on litigation hold

1. Go to the [Microsoft 365 admin center](https://admin.microsoft.com) and sign in.
2. Select **Users** &gt; **Active users**, and then select the user for whom you want to place on litigation hold.
3. On the **Properties** flyout panel, select the **Mail** tab, and then under **More actions**, select **Manage litigation hold**.

    [![Screenshot showing th eManage Litigation Hold option.](media/create-litigation-hold-mac/user-manage-litigation-hold.png)](media/create-litigation-hold-mac/user-manage-litigation-hold.png#lightbox)
4. On the **Manage litigation hold** flyout page, select the **Turn on litigation hold** checkbox, and then add the following optional information:

    - **Hold duration (days)**: Use this box to create a time-based hold and specify how long mailbox items are held when the mailbox is placed on Litigation hold. The duration is calculated from the date a mailbox item is received or created. When the hold duration expires for a specific item, that item is no longer preserved. If you leave this box blank, items are preserved indefinitely or until the hold is removed. Use days to specify the duration.
    - **Note visible to the user**: Use this box to inform the user their mailbox is on litigation hold. The note appears on the Account Information page in the user's mailbox if they're using Outlook 2010 or later. To access this page, users can select **File** in Outlook.
    - **Web page with more information for the user**: Use this box to direct the user to a website for more information about litigation hold. This URL appears on the Account Information page in the user's mailbox if they're using Outlook 2010 or later. To access this page, users can select **File** in Outlook.
5. Select **Save changes** on the **Litigation hold** flyout page to create the hold.

    The system displays a banner saying it might take up to 240 minutes for the change to take effect.

    Note

    After a litigation hold is enabled, the "created by" field reflects the original user who enabled the hold, even when the hold is later modified.

### Create a litigation hold using PowerShell

You can also create a litigation hold by running the following command in [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell):

```powershell
Set-Mailbox <username> -LitigationHoldEnabled $true
```

The previous command preserves items indefinitely because the hold duration isn't specified. To create a time-based hold, using the following command:

```powershell
Set-Mailbox <username> -LitigationHoldEnabled $true -LitigationHoldDuration <number of days>
```

You can also run the following command to verify if the mailbox is placed on litigation hold:

```powershell
Get-Mailbox <username> | FL LitigationHoldEnabled
```

A value of *True* indicates that the mailbox is on litigation hold.

For more information, see [Set-Mailbox](/en-us/powershell/module/exchangepowershell/set-mailbox).

## How does litigation hold work?

In the normal deleted item workflow, a mailbox item is moved to the **Deletions** subfolder in the **Recoverable Items** folder when a user permanently deletes it (Shift + Delete) or deletes it from the **Deleted Items** folder. A deletion policy (which is a retention tag configured with a Delete retention action) also moves items to the **Deletions** subfolder when the retention period expires.

When a user purges an item in the **Recoverable Items** folder, or when the deleted item retention period expires for an item, it moves to the **Purges** subfolder in the **Recoverable Items** folder, and is marked for permanent deletion. It's purged from Exchange the next time the mailbox is processed by the Managed Folder Assistant (MFA).

When a mailbox is placed on litigation hold, items in the **Purges** subfolder are preserved for the hold duration specified by the litigation hold. The hold duration is calculated from the original date an item was received or created, and defines how long items in the **Purges** subfolder are held.

When the hold duration expires for an item in the **Purges** subfolder, the item is marked for permanent deletion and is purged from Exchange the next time the mailbox is processed by the MFA. If an indefinite hold is placed on a mailbox, items aren't purged from the **Purges** subfolder.

The following illustration shows the subfolders in the **Recoverable Items** folders and the hold workflow process.

[![Diagram depicting how litigation hold works.](media/create-litigation-hold-mac/how-litigation-hold-works.png)](media/create-litigation-hold-mac/how-litigation-hold-works.png#lightbox)

Note

- If a hold associated with an eDiscovery case is placed on a mailbox, purged items are moved from the **Deletions** subfolder to the **Discovery Holds** subfolder, and are preserved until the mailbox is released from the eDiscovery hold.
- If you don't see the **Manage litigation hold** option in the Microsoft 365 admin center, it might be because the mailbox isn't assigned an Exchange Online Plan 2 license.