---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Manage guest access in Microsoft 365 groups - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/manage-guest-access-in-groups?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
ms.reviewer: rahulnayak
ms.date: 2026-04-22T00:00:00.0000000Z
f1.keywords: NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-admin
ms.localizationpriority: medium
ms.collection:
- M365-subscription-management
- Adm_O365
- Adm_TOC
ms.custom:
- AdminSurgePortfolio
- AdminTemplateSet
- admindeeplinkMAC
- no-azure-ad-ps-ref
- m365-groups
- user-accounts
search.appverid:
- MET150
- MOE150
description: Learn how to add guests to a Microsoft 365 group, view guests, and use PowerShell to control guest access.
locale: en-us
document_id: 9f5592e2-3fee-9034-5b33-2d1687d60ba2
document_version_independent_id: 5b8dee58-e383-9a26-570a-47f5c81121cb
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/create-groups/manage-guest-access-in-groups.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/create-groups/manage-guest-access-in-groups
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/create-groups/manage-guest-access-in-groups.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e4f48d48-dfb7-4973-a019-e504674667cb
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/495840e0-c52f-49d2-a584-185aefeb98c7
platformId: 51f3091b-a54c-28cf-f72c-0908602eff39
---

# Manage guest access in Microsoft 365 groups - Microsoft 365 admin | Microsoft Learn

By default, guest access for Microsoft 365 groups is turned on for your organization. Administrators can control whether to allow guest access to groups for the whole organization or for individual groups.

When it's turned on, group members can invite guests to a Microsoft 365 group through Outlook on the web. The group owner receives the invitations for approval.

Once approved, the guest is added to the directory and the group.

Note

Viva Engage Enterprise networks that are in Native Mode or within the [EU Geo](/en-us/viva/engage/manage-security-and-compliance/manage-data-compliance) don't support network guests. Microsoft 365 Connected Viva Engage groups don't currently support guest access, but you can create nonconnected, external groups in your Viva Engage network. See [Create and manage external groups in Viva Engage](/en-us/viva/engage/work-with-external-users/create-and-manage-external-groups) for instructions.

Guest access in groups is often used as part of a broader scenario that includes SharePoint or Teams. These services have their own guest sharing settings. For complete instructions for setting up guest sharing across groups, SharePoint, and Teams, see:

- [Collaborate with guests in a site](/en-us/previous-versions/microsoft-365/solutions/collaborate-in-site)
- [Collaborate with guests in a team](/en-us/previous-versions/microsoft-365/solutions/collaborate-as-team)

## Manage groups guest access

To enable or disable guest access in groups, use the [Groups](https://go.microsoft.com/fwlink/p/?linkid=2052855) settings.

1. In the [Microsoft 365 admin center](https://admin.microsoft.com), go to **Show all** &gt; **Settings** &gt; **Org settings**. On the [Services](https://go.microsoft.com/fwlink/p/?linkid=2053743) tab, select **Microsoft 365 Groups**.
2. On **Microsoft 365 Groups**, choose whether you want to let people outside your organization access group resources or let group owners add people outside your organization to groups.

## Add guests to a Microsoft 365 group in the admin center

If the guest already exists in your directory, you can add them to your groups from the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2052855). You must [manage groups with dynamic membership in Microsoft Entra ID](/en-us/azure/active-directory/enterprise-users/groups-create-rule).

1. In the admin center, go to **Teams & groups** &gt; [Active teams & groups](https://go.microsoft.com/fwlink/p/?linkid=2052855).
2. Select the group you want to add the guest to and select **Membership** &gt; **Members**.
3. Select **Add members** and choose the name of the guest you want to add.
4. Select **Save**.

To add a guest to the directory directly, you can [Add Microsoft Entra B2B collaboration users in the Azure portal](/en-us/azure/active-directory/b2b/add-users-administrator).

To edit any of a guest's information, you can [Add or update a user's profile information using Microsoft Entra ID](/en-us/azure/active-directory/fundamentals/active-directory-users-profile-azure-portal).

## Remove a guest

When you're done collaborating with a guest, remove them so they no longer have access to your organization.

1. In the [Microsoft 365 admin center](https://admin.microsoft.com), expand **Users** and select [Guest users](https://go.microsoft.com/fwlink/p/?linkid=2074830).
2. On the **Guest users** page, choose the user you want to remove and then choose **Delete a user**.

To remove users in the Microsoft Entra admin center, see [remove a guest and resources](/en-us/azure/active-directory/b2b/b2b-quickstart-add-guest-users-portal#clean-up-resources).