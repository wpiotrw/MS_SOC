---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft 365 Group mailbox size management - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/group-mailbox-size-management?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn about the group mailbox size management in Microsoft 365.
ms.author: dansimp
author: Dansimp
manager: dansimp
audience: ITPro
ms.topic: article
ms.service: m365-core
ms.subservice: identity
ms.localizationpriority: medium
search.appverid: 
ms.custom:
- m365-groups
- user-accounts
ms.collection:
- trust-pod
ms.reviewer: batre
ms.date: 2025-05-21T00:00:00.0000000Z
locale: en-us
document_id: 79d897cc-0be6-a995-fc23-e0259c0c47ba
document_version_independent_id: 79d897cc-0be6-a995-fc23-e0259c0c47ba
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/create-groups/group-mailbox-size-management.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/create-groups/group-mailbox-size-management
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/create-groups/group-mailbox-size-management.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 77f6f1b5-3ae0-1aac-1d7d-151e458ab3d7
---

# Microsoft 365 Group mailbox size management - Microsoft 365 admin | Microsoft Learn

Each Microsoft 365 group comes equipped with a dedicated mailbox that stores the emails received on the group. The group mailbox is also used by applications like SharePoint Online, Viva Engage, Teams etc. The group mailbox is equipped with initial storage quota of 50 GB. If the group mailbox quota is reached, people sending emails to the group receive a non-delivery report. Hence, it's a good practice to remove the older content from group mailboxes, to ensure the group mailbox doesn't reach its quota.

The following ways help you understand how the quota calculation works, best practices or proactive approach taken to ensure the group mailbox doesn't reach its quota. And the course of action to be performed if the group mailbox as reached or exceeded its quota.

## Proactive approach to keep group mailbox size in check

You can create retention policies to ensure older email from groups are removed automatically upon reaching the specified time limit. For more information, on steps to create retention policy for Microsoft 365 Group, see [Create and configure retention policies](/en-us/microsoft-365/compliance/create-retention-policies). The retention policies take longer work cycle to clean up the data, hence must be applied during the creation of a group mailbox. The retention policies can't be used as tool to immediately flush or remove the data from a group mailbox.

## To monitor the group mailbox size:

Use the following command to check the current quota assigned for the group mailbox:

```PowerShell
Get-Mailbox -GroupMailbox <groupname> |ft ProhibitSendReceiveQuota,ProhibitSendQuota,IssueWarningQuota 
```

And use the following command to check the current size of the group mailbox:

```PowerShell
Get-MailboxStatistics <groupname> | ft TotalDeletedItemSize,TotalItemSize 
```

## Steps to follow when the group mailbox has reached its limit:

As mentioned earlier, the group mailbox is used for various applications to store data. Once the group mailbox as reached its quota, it's important to identify the folders occupying more data and take the appropriate action.

Group owners can follow [these steps](https://support.microsoft.com/office/mailbox-storage-limits-in-outlook-21d25b99-525e-4fb3-a7c0-28367e3e76ce) to clean up the group mailbox and empty the space.

Or, you can use PowerShell:

1. Start with the following command to confirm that the group mailbox quota has exceeded:

    ```PowerShell
    Get-MailboxStatistics <groupname> |ft TotalItemSize,TotalDeletedItemSize 
    ```

    The group mailbox is distributed in various `TargetQuota`, namely System, Recoverable and User. The folders matching `TargetQuota` "User" is the only one considered in the calculation of the group quota.
2. Use the following command to verify the folder size that's occupying User data:

    ```PowerShell
    Get-MailboxFolderStatistics <groupname> | where { $_.TargetQuota -like 'User' } | ft Name,FolderPath,FolderType,FolderSize 
    
    Get-MailboxFolderStatistics <groupname> -FolderScope NonIPMRoot | where { $_.TargetQuota -like 'User' } | ft Name,FolderType,*size* 
    ```
3. Check the folders quota or size.
4. If the folder consuming the space is `SharePointWebPartsConnectorMessages`, as mentioned in [Use the Connector web part](https://support.microsoft.com/en-us/office/use-the-connector-web-part-db0756aa-f78f-4b74-8b19-be5dca0420e1?ns=spostandard&amp;version=16&amp;syslcid=1033&amp;uilcid=1033&amp;appver=spo160&amp;helpid=wssenduser_useconnectorwebpart_fl862286&amp;ui=en-us&amp;rs=en-us&amp;ad=us) then do the following:

    1. Disable the connector if not used.
    2. Wait for the messages to be cleared by default in 90 days.
5. If there's no special folder occupying the group mailbox size, [apply the group mailbox retention policy,](/en-us/microsoft-365/compliance/create-retention-policies) and wait for retention policy to clean up the emails from group mailbox.