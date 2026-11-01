---
layout: Conceptual
title: Restore an inactive mailbox | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/restore-an-inactive-mailbox
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
ms.subservice: purview-mailboxes
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
ms.assetid: 97e06a7a-ef9a-4ce8-baea-18b9e20449a3
description: Learn how to restore (or merge) the contents of an inactive mailbox to an existing mailbox.
ms.custom: seo-marvel-apr2020
locale: en-us
document_id: 8822e03c-c290-a37b-70d8-d2553f371cca
document_version_independent_id: 8822e03c-c290-a37b-70d8-d2553f371cca
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/restore-an-inactive-mailbox.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: restore-an-inactive-mailbox
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/restore-an-inactive-mailbox.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: f5256556-5480-1961-c1b8-1958f5888943
---

# Restore an inactive mailbox | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

An inactive mailbox (which is a type of soft-deleted mailbox) is used to retain a former employee's email after they leave your organization. If another employee takes on the job responsibilities of the former employee or if that employee returns to your organization, there are two ways that you can make the contents of the inactive mailbox available to a user:

- **Restore an inactive mailbox** If another employee takes on the job responsibilities of the former employee, or if another user needs access to the contents of the inactive mailbox, you can restore (or merge) the contents of the inactive mailbox to an existing mailbox. You can also restore the archive from an inactive mailbox. After it's restored, the inactive mailbox is preserved and is retained as an inactive mailbox. This article describes the procedures for restoring an inactive mailbox.
- **Recover an inactive mailbox** If the former employee returns to your organization, or if a new employee is hired to take on the job responsibilities of the former employee, you can recover the contents of the inactive mailbox. This method converts the inactive mailbox to a new mailbox that contains the contents of the inactive mailbox. After it's recovered, the inactive mailbox no longer exists. For the step-by-step procedures, see [Recover an inactive mailbox in Office 365](recover-an-inactive-mailbox).

See the More information section in this article for more details about the differences between restoring and recovering an inactive mailbox. Both operations are designed for email data and don't support restoring or recovering application data that can be stored in mailbox hidden folders.

Note

You can't recover or restore an inactive mailbox that's configured with an auto-expanding archive. If, for compliance reasons, you need to recover data from an inactive mailbox with an auto-expanding archive, use content search to export the data from the mailbox. This action is supported for eDiscovery purposes only, and can't be used as a backup solution. For instructions to use content search for the recovery of data for eDiscovery, see following articles:

- [Content search](ediscovery-content-search)
- [Export content search results](ediscovery-export-search-results)

## Requirements to restore an inactive mailbox

- You must use Exchange Online PowerShell to restore an inactive mailbox. You can't use the Exchange admin center (EAC), or the Microsoft Purview portal for this procedure. For step-by-step instructions to use Exchange Online PowerShell, see [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
- Run the following command in Exchange Online PowerShell to get identity information for the inactive mailboxes in your organization.

    ```powershell
    Get-Mailbox -InactiveMailboxOnly | Format-List Name,DistinguishedName,ExchangeGuid,PrimarySmtpAddress
    ```

    Use the information returned by this command to identify and restore a specific inactive mailbox.
- For more information about inactive mailboxes, see [Inactive mailboxes in Office 365](inactive-mailboxes-in-office-365).

## Restore inactive mailboxes

Use the **New-MailboxRestoreRequest** cmdlet with the *SourceMailbox* and *TargetMailbox* parameters to restore the contents of an inactive mailbox to an existing mailbox. For more information about using this cmdlet, see [New-MailboxRestoreRequest](/en-us/powershell/module/exchange/new-mailboxrestorerequest).

Before you can restore an inactive mailbox, you have to add the LegacyExchangeDN of the inactive mailbox to the target mailbox, as an X500 proxy address of the target mailbox. This has to be done because the **New-MailboxRestoreRequest** cmdlet checks to make sure the value of the **LegacyExchangeDN** property on the source and target mailboxes is the same. After you restore the inactive mailbox, you can optionally remove the LegacyExchangeDN of the inactive mailbox from source mailbox. Be sure to wait until the mailbox restore request is complete before removing the LegacyExchangeDN.

Follow these steps to restore an inactive mailbox to an existing mailbox:

1. Create a variable that contains the properties of the inactive mailbox.

    ```powershell
    $inactiveMailbox = Get-Mailbox -InactiveMailboxOnly -Identity <identity of inactive mailbox>
    ```

    Important

    In the previous command, use the value of the **DistinguishedName** or **ExchangeGUID** property to identify the inactive mailbox. These properties are unique for each mailbox in your organization, whereas it's possible that an active and an inactive mailbox might have the same primary SMTP address.
2. Display the LegacyExchangeDN of the inactive mailbox so that you can add it as a proxy address to the target mailbox in the next step.

    ```powershell
    $inactiveMailbox.LegacyExchangeDN
    ```
3. Add the LegacyExchangeDN of the inactive mailbox as an X500 proxy address to the target mailbox.

    ```powershell
    Set-Mailbox <identity of target mailbox> -EmailAddresses @{Add="X500:<LegacyExchangeDN of inactive mailbox>"}
    ```
4. Restore the contents of the inactive mailbox to an existing mailbox. The contents of the inactive mailbox (source mailbox) will be merged into the corresponding folders in the existing mailbox (target mailbox).

    ```powershell
    New-MailboxRestoreRequest -SourceMailbox $inactiveMailbox.DistinguishedName -TargetMailbox <identity of target mailbox> 
    ```

    Alternatively, you can specify a top-level folder in the target mailbox in which to restore the contents from the inactive mailbox. If the specified target folder or target folder structure doesn't already exist in the target mailbox, it is created during the restore process.

    This example copies mailbox items and subfolders from an inactive mailbox to a folder named "Inactive Mailbox" in the top-level folder structure of the target mailbox.

    ```powershell
    New-MailboxRestoreRequest -SourceMailbox $InactiveMailbox.DistinguishedName -TargetMailbox <identity of target mailbox> -TargetRootFolder "Inactive Mailbox"
    ```
5. After the restore request is complete, you can optionally remove the LegacyExchangeDN of the inactive mailbox from the target mailbox. Leaving the LegacyExchangeDN from the inactive mailbox won't affect the target mailbox.

    ```powershell
    Set-Mailbox <identity of target mailbox> -EmailAddresses @{Remove="X500:<LegacyExchangeDN of inactive mailbox>"}
    ```

## Restore the archive from an inactive mailbox

If an inactive mailbox has an archive mailbox, you can also restore it to the archive mailbox of an existing mailbox. To restore the archive from an inactive mailbox, you have to add the *SourceIsArchive* and *TargetIsArchive* switches to the command used to restore an inactive mailbox.

1. Create a variable that contains the properties of the inactive mailbox.

    ```powershell
    $inactiveMailbox = Get-Mailbox -InactiveMailboxOnly -Identity <identity of inactive mailbox>
    ```

    Note

    In the previous command, use the value of the **DistinguishedName** or **ExchangeGUID** property to identify the inactive mailbox. These properties are unique for each mailbox in your organization, whereas it's possible that an active and an inactive mailbox might have the same primary SMTP address.
2. Display the LegacyExchangeDN of the inactive mailbox so that you can add it as a proxy address to the target mailbox in the next step.

    ```powershell
    $inactiveMailbox.LegacyExchangeDN
    ```
3. Add the LegacyExchangeDN of the inactive mailbox as an X500 proxy address to the target mailbox.

    ```powershell
    Set-Mailbox <identity of target mailbox> -EmailAddresses @{Add="X500:<LegacyExchangeDN of inactive mailbox>"}
    ```
4. Restore the contents of the archive from the inactive mailbox (source archive) to the archive of an existing mailbox (target archive). In this example, the contents from the source archive are copied to a folder named "Inactive Mailbox Archive" in the archive of the target mailbox.

    ```powershell
    New-MailboxRestoreRequest -SourceMailbox $InactiveMailbox.DistinguishedName -SourceIsArchive -TargetMailbox <identity of target mailbox> -TargetIsArchive -TargetRootFolder "Inactive Mailbox Archive"
    ```
5. After the restore request is complete, you can optionally remove the LegacyExchangeDN of the inactive mailbox from the target mailbox. Leaving the LegacyExchangeDN from the inactive mailbox won't affect the target mailbox.

    ```powershell
    Set-Mailbox <identity of target mailbox> -EmailAddresses @{Remove="X500:<LegacyExchangeDN of inactive mailbox>"}
    ```

## More information

- **What's the main difference between recovering and restoring an inactive mailbox?** When you recover an inactive mailbox, the mailbox is converted to a new mailbox. The contents and folder structure of the inactive mailbox are retained, and the mailbox is linked to a new user account. After it's recovered, the inactive mailbox no longer exists, and any changes made to the content in the new mailbox will affect the content that was originally on hold in the inactive mailbox. Conversely, when you restore an inactive mailbox, the contents are merely copied to another mailbox. The inactive mailbox is preserved and remains an inactive mailbox. Any changes made to the content in the target mailbox won't affect the original content held in the inactive mailbox. The inactive mailbox can still be searched by using the [Content Search tool](ediscovery-content-search), its contents can be restored to another mailbox, or it can be recovered or deleted at a later date.
- **How do you find inactive mailboxes?** To get a list of the inactive mailboxes in your organization and display information that is useful for restoring an inactive mailbox, you can run this command.

    ```powershell
    Get-Mailbox -InactiveMailboxOnly | Format-List Name,PrimarySMTPAddress,DistinguishedName,ExchangeGUID,LegacyExchangeDN,ArchiveStatus
    ```
- **Use a Microsoft 365 retention policy or Litigation Hold or to retain inactive mailbox content.** If you want to retain the state of an inactive mailbox after it's restored, you can apply a [Microsoft 365 retention policy](retention) to the target mailbox or place the target mailbox on [Litigation Hold](/en-us/exchange/policy-and-compliance/holds/litigation-holds) before you restore the inactive mailbox. This will prevent the permanent deletion of any items from the inactive mailbox after they're restored to the target mailbox.
- **Enable retention hold on the target mailbox before you restore an inactive mailbox.** Because mailbox items from an inactive mailbox could be old, you might consider enabling retention hold on the target mailbox before you restore an inactive mailbox. When you put a mailbox on retention hold, the retention policy that's assigned to it won't be processed until the retention hold is removed or until the retention hold period expires. This gives the owner of the target mailbox time to manage old messages from the inactive mailbox. Otherwise, the retention policy might delete old items (or move items to the archive mailbox, if it's enabled) that have expired based on the retention settings configured for the target mailbox. For more information, see [Place a mailbox on retention hold in Exchange Online](/en-us/exchange/security-and-compliance/messaging-records-management/mailbox-retention-hold).
- **You can use other parameters with the New-MailboxRestoreRequest cmdlet to implement different restore scenarios for inactive mailboxes.** For example, you can run this command to restore the archive from the inactive mailbox into the primary mailbox of the target mailbox.

    ```powershell
    New-MailboxRestoreRequest -SourceMailbox <inactive mailbox> -SourceIsArchive -TargetMailbox <target mailbox> -TargetRootFolder "Inactive Mailbox Archive"
    ```

    You can also restore the inactive primary mailbox into the archive of the target mailbox by running this command.

    ```powershell
    New-MailboxRestoreRequest -SourceMailbox <inactive mailbox> -TargetMailbox <target mailbox> -TargetIsArchive -TargetRootFolder "Inactive Mailbox"
    ```
- **What does the TargetRootFolder parameter do?** As previously explained, you can use the **TargetRootFolder** parameter to specify a folder in the top of the folder structure (also called the root) in the target mailbox in which to restore the contents of the inactive mailbox. If you don't use this parameter, mailbox items from the inactive mailbox are merged into the corresponding default folders of the target mailbox, and custom folders are re-created in the root of the target mailbox. The following illustrations highlight these differences between not using and using the **TargetRootFolder** parameter.

    Note

    To restore the contents of a primary mailbox to an archive mailbox, use the **TargetRootFolder** parameter to specify the archive mailbox folders to migrate the content to. This content will be visible after it's restored. If you don't use this parameter, the restored content is not visible because it's mapped to locations in the archive mailbox that aren't visible to users.

    **Folder hierarchy in the target mailbox when the TargetRootFolder parameter isn't used**

    ![Screenshot when TargetRootFolder parameter isn't used.](media/76a759af-f483-4d1c-8cc7-243435b5562e.png)

    **Folder hierarchy in the target mailbox when the TargetRootFolder parameter is used**

    ![Screenshot when TargetRootFolder parameter is used.](media/300da592-7323-48db-b8a4-07012259d113.png)