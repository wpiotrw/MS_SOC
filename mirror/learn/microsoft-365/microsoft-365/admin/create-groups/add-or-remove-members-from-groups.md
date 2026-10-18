---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Add or remove members from Microsoft 365 groups - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/add-or-remove-members-from-groups?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
ms.reviewer: batre
ms.date: 2025-05-21T00:00:00.0000000Z
f1.keywords: NOCSH
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
- AdminTemplateSet
- m365-groups
- user-accounts
search.appverid:
- MET150
ms.assetid: e186d224-a324-4afa-8300-0e4fc0c3000a
description: Learn how to add a member to a group, remove member from group, and manage group owner status in the Microsoft 365 admin center.
locale: en-us
document_id: 40174ff9-7dc6-a706-c546-77e2391ab8d7
document_version_independent_id: a01b7077-976f-dded-ed25-18e8585b28b0
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/create-groups/add-or-remove-members-from-groups.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/create-groups/add-or-remove-members-from-groups
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/create-groups/add-or-remove-members-from-groups.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: e0216f4e-aabd-3472-6e82-f2d180f88d5b
---

# Add or remove members from Microsoft 365 groups - Microsoft 365 admin | Microsoft Learn

In Microsoft 365, group members typically create their own groups, add themselves to groups they want to join, or are invited by group owners. If group ownership changes, or if you determine that a member should be added or removed, as the admin you can also make that change. Only an Exchange administrator, Groups administrator, or user administrator can make these changes. [What is a Microsoft 365 group?](https://support.microsoft.com/office/b565caa1-5c40-40ef-9915-60fdb2d97fa2)

Tip

If you're not an admin, you can [add or remove members using Outlook](https://support.microsoft.com/office/3b650f4a-5c9b-4f94-a1bb-0cca4b1091de).

Note

Nesting of groups isn't supported with regard to Microsoft 365 Group, that is, you can't add an existing Distribution List (DL) or Microsoft 365 Group as member of another Microsoft 365 Group.

## Add a member to a group in the admin center

1. In the admin center, go to the [Active groups](https://go.microsoft.com/fwlink/p/?linkid=2052855) page.
2. Click a group name.
3. In the details pane, on the **Membership** tab, select **Members**, and then select **Add members**.
4. Search for or select the name of the member you want to add.
5. Select **Save**.

## Add a group to a member in the admin center

1. In the admin center, go to the [Active users](https://go.microsoft.com/fwlink/p/?linkid=834822) page.
2. Click a user.
3. In the details pane, on the **Account** tab, select **Manage groups**.
4. Select **Assign memberships** and search for or select the name of the group you want to add.
5. Select **Save**.

## Remove a member from a group in the admin center

Note

When you remove a member from a private group, it takes 5 minutes for the person to be blocked from the group.

1. In the admin center, go to the [Active groups](https://go.microsoft.com/fwlink/p/?linkid=2052855) page.
2. Click a group name.
3. In the details pane, on the **Membership** tab, select **Members**.
4. Next to the member you want to remove, select the X.
5. Select **Save** to remove the member.

## Manage group owner status

By default, the person who created the group is the group owner. Often a group will have multiple owners for backup support or other reasons. Members can be promoted to owner status and owners can be demoted to member status.

### Promote a member to owner status in the admin center

1. In the admin center, go to the [Active groups](https://go.microsoft.com/fwlink/p/?linkid=2052855) page.
2. Click a group name.
3. In the details pane, on the **Membership** tab, select **Owners**.
4. Select **Add owners**.
5. Select the check box next to the name of the member you want to add.
6. Select **Save**, and then **Close**.

### Remove owner status in the admin center

1. In the admin center, go to the [Active groups](https://go.microsoft.com/fwlink/p/?linkid=2052855) page.
2. Click a group name.
3. In the details pane, on the **Membership** tab, select **Owners**.
4. Select the X next to the owner's name.
5. Select **Save**.