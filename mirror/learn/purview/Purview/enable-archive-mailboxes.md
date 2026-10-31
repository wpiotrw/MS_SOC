---
layout: Conceptual
title: Enable archive mailboxes for Microsoft 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/enable-archive-mailboxes
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.reviewer: mekaus
ms.date: 2026-04-06T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-mailboxes
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
ms.assetid: 268a109e-7843-405b-bb3d-b9393b2342ce
ms.custom:
- seo-marvel-apr2020
- admindeeplinkCOMPLIANCE
- admindeeplinkEXCHANGE
- sfi-ga-blocked
- sfi-image-nochange
description: Learn how to enable or disable archive mailboxes to support your organization's message retention, eDiscovery, and hold requirements.
locale: en-us
document_id: 5d7a568f-8ef9-c737-8637-7f3cb4e7beca
document_version_independent_id: 5d7a568f-8ef9-c737-8637-7f3cb4e7beca
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/enable-archive-mailboxes.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enable-archive-mailboxes
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/enable-archive-mailboxes.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: b6c4b17b-201f-c551-921e-01e8935c8a11
---

# Enable archive mailboxes for Microsoft 365 | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Email archiving in Microsoft 365 (also called *In-Place Archiving*) provides users with more mailbox storage space. For more information, see [Learn about archive mailboxes](archive-mailboxes).

Use the information in this article to enable or disable an archive mailbox by using the Exchange admin portal or by using PowerShell. Also learn how to run an automated diagnostic check on a user's archive mailbox to identify any problems and suggested resolutions.

Configuration to enable or disable archive mailboxes has moved to the [new Exchange admin center (EAC)](/en-us/exchange/exchange-admin-center).

## Get the necessary permissions

You must be assigned the Mail Recipients role in Exchange Online to enable or disable archive mailboxes. By default, this role is assigned to the Recipient Management and Organization Management role groups on the **Permissions** page in the [Exchange admin center](https://go.microsoft.com/fwlink/p/?linkid=2059104).

## How to enable an archive mailbox

Note

When you enable the archive mailbox, items in the user's mailbox that are older than the archiving policy assigned to the mailbox will be moved to the new archive mailbox.

The default archive policy that is part of the retention policy assigned to Exchange Online mailboxes moves items to the archive mailbox two years after the date the item was delivered to the mailbox or created by the user. For more information, see [Learn about archive mailboxes](archive-mailboxes).

1. Sign in to the [Exchange admin center](https://go.microsoft.com/fwlink/p/?linkid=2059104) (EAC) and navigate to **Recipients** &gt; **Mailboxes**.
2. In the list of mailboxes, select the user to enable their mailbox for archive.
3. In the flyout pane, select **Others**, and under **Mailbox archive**, select **Manage mailbox archive**:

    ![Manage mailbox archive for a selected user.](media/manage-mailbox-archive-option.png)
4. On the **Manage mailbox archive** pane, turn on **Mailbox archive**, and then **Save**.

It might take a few moments to create the archive mailbox. When it's created, **Active** is displayed in the **Archive status** column for the selected user, although you might need to refresh the page to see the change of status.

## How to auto-enable archive mailboxes

You can use the [Set-OrganizationConfig](/en-us/powershell/module/exchange/set-organizationconfig#-autoenablearchivemailbox) PowerShell command to automatically provision an archive mailbox when a primary Exchange Online mailbox reaches 90% of its storage quota. An archive mailbox is created automatically only if all of the following conditions are met:

- The mailbox is a User Mailbox or Shared Mailbox in Exchange Online.
- Archiving is included in the Microsoft 365 assigned license.
- The mailbox is not synchronized from an on‑premises environment (the IsDirSynced property is set to False).

```powershell
Set-OrganizationConfig -AutoEnableArchiveMailbox $true
```

## How to disable an archive mailbox

Similarly to how you enable an archive mailbox, you can use the same configuration in the Exchange admin center to disable a user's archive mailbox. This time, turn **Mailbox archive** off in the Exchange admin center.

After you disable an archive mailbox, you can reconnect it to the user's primary mailbox within 30 days of disabling it. In this case, the original contents of the archive mailbox are restored. After 30 days, the contents of the original archive mailbox are permanently deleted and can't be recovered. So if you re-enable the archive more than 30 days after disabling it, a new archive mailbox is created.

The default archive policy assigned to users' mailboxes moves items to the archive mailbox two years after the date the item is delivered. If you disable a user's archive mailbox, no action will be taken on mailbox items and they'll remain in the user's primary mailbox.

## Use Exchange Online PowerShell to enable or disable archive mailboxes

You can also use Exchange Online PowerShell to enable archive mailboxes. The primary reason to use PowerShell is that you can quickly enable the archive mailbox for all users in your organization.

The first step is to connect to Exchange Online PowerShell. For instructions, see [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).

After you're connected to Exchange Online, you can run the commands in the following sections to enable or disable archive mailboxes.

### Enable archive mailboxes

Run the following command to enable the archive mailbox for a single user.

```powershell
Enable-Mailbox -Identity <username> -Archive
```

Run the following command to enable the archive mailbox for all users in your organization whose archive mailbox is currently not enabled and who do not already have a disabled archive:

```powershell
Get-Mailbox -Filter {ArchiveGuid -Eq "00000000-0000-0000-0000-000000000000" -AND DisabledArchiveGuid -Eq "00000000-0000-0000-0000-000000000000" -AND RecipientTypeDetails -Eq "UserMailbox"} | Enable-Mailbox -Archive
```

Note

If archive for a mailbox was disabled more than 30 days ago, the command fails with the following error:

"Write-ErrorMessage : |Microsoft.Exchange.Data.Directory.MissingDisconnectReceiptsException|AD modification is not allowed - disconnect of shard with ExchangeGuid *GUID* is not authorized".

To resolve this error, run the Set-Mailbox cmdlet for the mailbox with -RemoveDisabledArchive. Then run the command again to enable the archive mailbox.

When enabling archiving for a specific user whose mailbox is on hold or assigned to a retention policy, the following configuration changes are implemented:

- The storage quota for the user's primary mailbox's Recoverable Items folder is expanded by 5 GB, raising it from 100 GB to 105 GB. This adjustment provides additional space to accommodate deleted items during the archiving process, even if auto-expanding archive isn't enabled. The Recoverable Items warning quota is also augmented by 5 GB, increasing it from 90 GB to 95 GB.

### Disable archive mailboxes

Run the following command to disable the archive mailbox for a single user.

```powershell
Disable-Mailbox -Identity <username> -Archive
```

Run the following command to disable the archive mailbox for all users in your organization (whose archive mailbox is currently enabled).

```powershell
Get-Mailbox -Filter {ArchiveGuid -Ne "00000000-0000-0000-0000-000000000000" -AND RecipientTypeDetails -Eq "UserMailbox"} | Disable-Mailbox -Archive
```

## Run diagnostics on archive mailboxes

Important

You must be a Microsoft 365 global admin to use the archive mailbox diagnostic check.

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about [Microsoft Purview roles and permissions](purview-permissions).

You can run an automated diagnostic check on a user's archive mailbox to identify any problems and suggested resolutions.

To run the diagnostic check, click the button below.

![Run diagnostics on an archive mailbox.](media/archivemailboxdiagnostics.png)

A flyout page opens in the Microsoft 365 admin center. Enter the email address of the mailbox you want to check and click **Run Tests**.

Note

this feature isn't available in Microsoft 365 Government clouds, Microsoft 365 operated by 21Vianet, or Microsoft 365 Germany.

## Instructions for end users

Explain to users how their archive mailbox works, and how they can interact with it in Outlook on Windows, macOS, and the web. The most effective documentation will be customized for your organization. But for basic instructions, see [Manage email storage with online archive mailboxes](https://support.microsoft.com/office/manage-email-storage-with-online-archive-mailboxes-1cae7d17-7813-4fe8-8ca2-9a5494e9a721).