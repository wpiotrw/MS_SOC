---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Create, edit, or delete a security group in the Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/email/create-edit-or-delete-a-security-group?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2026-05-18T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: m365-core
ms.subservice: identity
ms.localizationpriority: medium
description: Learn to create, edit, or delete a security group.
locale: en-us
document_id: 63d0ee25-905c-80a3-16b0-b582d7815c2b
document_version_independent_id: 5198168e-5a5b-8ddd-d1ee-643d039d7b1e
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/email/create-edit-or-delete-a-security-group.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/email/create-edit-or-delete-a-security-group
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/email/create-edit-or-delete-a-security-group.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: c2f8fbce-9fd7-ca4f-ed3c-89489cac2a52
---

# Create, edit, or delete a security group in the Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn

On the Microsoft 365 **Active teams and groups** page, you can create groups of user accounts that you can use to assign the same permissions to in SharePoint Online and CRM Online. For example, an administrator can create a security group to grant a certain group of people access to a SharePoint site.

## Before you begin

User management administrators have permissions to create, edit, or delete security groups; for more information about administrator roles, see [Assigning admin roles](../add-users/assign-admin-roles).

There are also Groups in Exchange Online and SharePoint Online that you can use to send email or assign permissions to a group of users, and Groups in Exchange Online and SharePoint Online that grant users rights and access to sites and site collections.

## Manage security groups in the admin center

### Add a security group

1. In the Microsoft 365 admin center, go to **Teams & groups** &gt; [Active teams and groups](https://go.microsoft.com/fwlink/p/?linkid=2052855) page.
2. Go to the **Security groups** page, and select **Add a security group**.
3. On the **Set up the basics** page, add your group name and a description and choose **Next**.
4. On the **Edit settings** page, select whether you want to allow Microsoft Entra roles to be assigned to the group and select **Next**.
5. Review your selections and choose **Create group** and **Close**.

### Add owners or members to a security group

1. Select the security group name on the [Active teams and groups](https://go.microsoft.com/fwlink/p/?linkid=2052855) page.
2. On the **General** tab, select **Add owners** to add group owners.
3. On the **Members** tab, select **View all and manage members** and choose the person from the list or use the **Search** box. Select **Add** and close.

### Remove members from a security group

1. Select the security group name on the [Active teams and groups](https://go.microsoft.com/fwlink/p/?linkid=2052855) page, and on the **Members** tab, select **View all and manage members**.
2. To remove members, select the user, choose the ellipsis and choose **Remove members**.

### Edit a security group

1. Select the security group name on the [Active teams and groups](https://go.microsoft.com/fwlink/p/?linkid=2052855) page, and on the **Members** tab, select **View all and manage members**.
2. Select the group's name and make your changes.

### Delete a security group

1. In the Microsoft 365 admin center, go to **Teams & groups** &gt; [Active teams and groups](https://go.microsoft.com/fwlink/p/?linkid=2052855) page.
2. Select the security group and on the **General** tab, select **Delete group** and then confirm by selecting **Delete group**. Then **Close** once the group is deleted.

## Groups in Exchange Online and SharePoint Online

If you want to create groups of users so you can send email to them all at the same time, you can do that in the Exchange admin center by going to **Admin** &gt; **Exchange** &gt; **Recipients** &gt; [**Groups**](https://go.microsoft.com/fwlink/?linkid=2183233). Next, select **Add a group**. Then, choose the type of group you want to create. For more information, see [Compare types of groups in Microsoft 365](/en-us/microsoft-365/admin/create-groups/compare-groups).

After you create distribution groups and mail-enabled security groups in the [Exchange admin center](https://go.microsoft.com/fwlink/p/?linkid=2059104), their names and user lists appear on the **Security groups** page. You can delete these groups in both locations, but you can edit them only in the Exchange admin center. Dynamic distribution groups don't show up on the **Security groups** page.

SharePoint groups are created automatically when you make a site collection. The default groups use the default permission levels in SharePoint-sometimes called SharePoint roles-to grant users rights and access. For more information, see [Default SharePoint groups in SharePoint Online](/en-us/sharepoint/default-sharepoint-groups).

## Frequently asked questions about groups

### How is a security group different from security groups I create in SharePoint?

Security groups can be used with SharePoint, Exchange, Windows, and more. A security group you create in SharePoint is only recognized by that SharePoint site collection.

### Do I have to use security groups for my organization to be secure?

No. This is just one more way you can manage security for your organization. You can always grant user permissions and access to sites individually. But with security groups, you can easily manage larger groups of users.

### Can I send email to a security group?

Yes. But if you want to use groups for email and collaboration, we recommend that you [create a Microsoft 365 group](../create-groups/create-groups) instead.