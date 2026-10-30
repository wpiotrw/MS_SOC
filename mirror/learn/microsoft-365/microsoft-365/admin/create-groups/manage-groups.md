---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Manage a group in the admin center - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/manage-groups?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
ms.reviewer: batre
ms.date: 2025-05-23T00:00:00.0000000Z
f1.keywords: NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
audience: Admin
ms.topic: how-to
ms.service: m365-core
ms.subservice: identity
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- trust-pod
ms.custom:
- admindeeplinkMAC
- has-azure-ad-ps-ref, azure-ad-ref-level-one-done
- m365-groups
- user-accounts
search.appverid:
- BCS160
- MET150
- MOE150
ms.assetid: 74a1ef8b-3844-4d08-9980-9f8f7a36000f
description: Learn to manage Microsoft 365 Groups, including adding remove group members, editing the email address, group name, or description, and customizing how the group works.
locale: en-us
document_id: 18c17598-3ade-528a-922d-1904f194b931
document_version_independent_id: a9561e0d-3247-58bd-654b-41898affc6ea
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/create-groups/manage-groups.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/create-groups/manage-groups
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/create-groups/manage-groups.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 8d0fddff-9318-2292-b0ca-c2cd3be5addc
---

# Manage a group in the admin center - Microsoft 365 admin | Microsoft Learn

After you have [created a Microsoft 365 group](create-groups) and added group members, you can configure your group. You can edit the group name or description, manage owners or members, and specify whether external senders can email the group and whether to send copies of group conversations to members.

Go to the Microsoft 365 admin center at [https://admin.cloud.microsoft](https://go.microsoft.com/fwlink/p/?linkid=2024339).

## Edit the group name or description

1. In the admin center, expand **Teams & groups**, and then click [**Active teams & groups**](https://go.microsoft.com/fwlink/p/?linkid=2052855).
2. Select the group that you want to edit, and then click **Edit name and description**.
3. Update the name and description, and then select **Save**.

## Change the email address or email domain of the group

You can change the email address of a Microsoft 365 group or Microsoft Teams by using the Microsoft 365 admin center. Just select the group and select @edit email address.

You can also use the following EXO PowerShell command to change the primary SMTP address of a Microsoft 365 group/Teams:

```powershell
Set-UnifiedGroup <Group Name> -PrimarySmtpAddress <new SMTP Address>
```

Example:

```powershell
Set-UnifiedGroup Marketing -PrimarySmtpAddress marketing@contoso.com
```

## Manage group owners and members

1. In the admin center, expand **Teams & groups**, and then click [**Active teams & groups**](https://go.microsoft.com/fwlink/p/?linkid=2052855).
2. Click the name of the group you want to manage to open the settings pane.
3. On the **Membership** tab, choose if you want to manage **Owners** or **Members**.
4. Choose **Add** to add someone or click **X** to remove someone.
5. Click **Close**.

## Send copies of conversations to group members' inboxes

When you use the admin center to create a group, by default users do not get copies of group emails sent to their inboxes though users get copies of group meeting invitations sent to their inboxes. They'll need to go to the group to see conversations. You can change this setting in the admin center.

When you turn this setting on, group members will get a copy of group emails and meeting invitations sent to their Outlook Inbox. They can read and delete this copy of the email and not affect anyone else. In the Group inbox, a copy of the email still exists.

Group members can opt out of receiving these emails by choosing to stop following the group in Outlook.

1. In the admin center, expand **Teams & groups**, and then click [**Active teams & groups**](https://go.microsoft.com/fwlink/p/?linkid=2052855).
2. Click the name of the group you want to manage to open the settings pane.
3. On the **Settings** tab, select **Send copies of group conversations and events to group members** if you want members to receive copies of group messages and calendar items in their own inbox.
4. Select **Save**.

## Let people outside the organization email the group

This option is great if you want to have a company email address such as info@contoso.com.

1. In the admin center, expand **Teams & groups**, and then click [**Active teams & groups**](https://go.microsoft.com/fwlink/p/?linkid=2052855).
2. Click the name of the group you want to manage to open the settings pane.
3. In the admin center groups list, select the name of the group you want to change, and then on the **Settings** tab, select **Let people outside the organization to email this group**.
4. Select **Save**.

Note

It may take up to 30 minutes before users outside the organization can email the group.

## Permanently delete a Microsoft 365 group

Sometimes you may want to permanently purge a group without waiting for the 30 day soft-deletion period to expire. To do that, start PowerShell and run this command to get the object ID of the group:

First, install Microsoft Graph PowerShell.

Then run the following command:

```powershell
Connect-MgGraph -Scopes "Group.ReadWrite.All"
```

Then use this command to list deleted groups:

```powershell
Get-MgDirectoryDeletedGroup
```

Note down the ID of group you are looking to permenantly delete and then run the following command:

```powershell
Remove-MgDirectoryDeletedItem -DirectoryObjectId <ID of the group to be permenantly deleted>
```

To confirm that the group has been successfully purged, run the *Get-MgDirectoryDeletedItem* cmdlet again to confirm that the group no longer appears on the list of soft-deleted groups. In some cases it may take as long as 24 hours for the group and all of its data to be permanently deleted.