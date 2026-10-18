---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Create a group in the admin center - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/create-groups?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
ms.reviewer: batre
ms.date: 2025-05-21T00:00:00.0000000Z
f1.keywords: CSH
ms.author: dansimp
author: Dansimp
manager: dansimp
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-admin
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- trust-pod
ms.custom:
- AdminSurgePortfolio
- okr_smb
- AdminTemplateSet
- admindeeplinkMAC
- m365-groups
- user-accounts
search.appverid:
- BCS160
- MET150
- MOE150
ms.assetid: 74a1ef8b-3844-4d08-9980-9f8f7a36000f
description: Learn to create and delete Microsoft 365 groups, add and remove group members, and customize how the group works.
locale: en-us
document_id: 8cdc937f-ed29-e584-d38f-9dd114847eaa
document_version_independent_id: b0a76263-1274-edc9-0205-673f69d24951
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/create-groups/create-groups.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/create-groups/create-groups
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/create-groups/create-groups.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e4f48d48-dfb7-4973-a019-e504674667cb
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/495840e0-c52f-49d2-a584-185aefeb98c7
platformId: a49422ff-ec8f-53c0-afb6-e2893b751c2d
---

# Create a group in the admin center - Microsoft 365 admin | Microsoft Learn

While users can create a Microsoft 365 group from Outlook or other apps, as an admin, you may need to create or delete groups, add or remove members, and customize how they work. The [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2052855) is the place to do this.

Tip

Microsoft 365 connected Viva Engage groups must be created in Viva Engage, but can be managed in the Microsoft 365 admin center like other Microsoft 365 groups. To learn more, see [Viva Engage and Microsoft 365 groups](/en-us/viva/engage/manage-viva-engage-groups/viva-engage-and-office-365-groups).

## Create a Microsoft 365 group

1. In the admin center, expand **Teams & groups**, and then select **[Active teams & groups](https://go.microsoft.com/fwlink/p/?linkid=2052855)**.
2. Select **Add Microsoft 365 group**.
3. On the **Basics** page, type a name for the group, and, optionally, a description. Select **Next**.
4. On the **Owners** page, choose the name of one or more people who will be designated to manage the group. Anyone who is a group owner will be able to delete email from the Group inbox. Other members won't be able to delete email from the Group inbox. Select **Next**.
5. On the **Members** page, choose the name of one or more people who will be designated as members of the group. Select **Next**.
6. On the **Settings** page, type a unique email address for the group, choose a privacy option and whether you want to add Microsoft Teams, and then select **Next**.

    Note

    The email domain of the group can be changed after the group has been created.
7. After reviewing your settings and making any changes, select **Create group**.
8. Select **Close**.

## Add members to the group

Once the group has been created, you can add members and configure additional settings.

Users can [add themselves or request approval](https://support.microsoft.com/office/2e59e19c-b872-44c8-ae84-0acc4b79c45d), or you can add them now.

1. In the admin center, refresh the page so your new group appears, and then select the name of the group that you want to add members to.
2. On the **Membership** tab, select **Members**.
3. Select **Add members**.
4. Select the users you want to add, and then select **Save**.
5. Select **Close** three times.

    The group will appear in Outlook with members assigned to it.

## Who can delete email from the Group inbox?

The Group owner can delete any emails from the Group Inbox, regardless of whether they were the initial author.

A member can delete an email conversation from the Group inbox if they initiated it, and only using Outlook on the web (right-click the email, then choose **Delete**). They can't do it from the Outlook app (Outlook 2016).

When an email is deleted from the group mailbox, it is not deleted from any of the group members' personal mailboxes.