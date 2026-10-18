---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Guests in the Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-guest-users?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn how to manage guest access in the Microsoft 365 admin center. Add guests to attend meetings, view documents, and chat in Teams they're invited to.
f1.keywords:
- NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2025-09-17T00:00:00.0000000Z
audience: Admin
ms.topic: overview
ms.service: microsoft-365-admin
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- must-keep
ms.custom:
- AdminSurgePortfolio
- AdminTemplateSet
- admindeeplinkMAC
locale: en-us
document_id: 1015a9d3-f0bb-dad5-7210-e3dd9b62881c
document_version_independent_id: 5c517c9b-cd05-2794-2f5d-c89c4d72b4a4
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/add-users/about-guest-users.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/add-users/about-guest-users
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/add-users/about-guest-users.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 9a553fd9-9e12-3bdf-7dc4-9c3b6528c2fc
---

# Guests in the Microsoft 365 admin center - Microsoft 365 admin | Microsoft Learn

By default, guest access for Microsoft 365 Groups is turned on for your organization. Admins can control whether to allow guest access to groups for their whole organization or for individual groups.

Any guests you add to your Microsoft Teams, SharePoint, or Microsoft Entra External ID are also added to the **`Guest users`** list in the [Microsoft 365 admin center](https://admin.microsoft.com/). Guests can attend meetings, view documents, and chat in Teams they're invited to. Once a user shows up in the **`Guest users`** list, you can remove their access there.

To view guests, in the [Microsoft 365 admin center](https://admin.microsoft.com/), in the left nav, expand **Users**, and then choose **`Guest users`**.

## Before you begin

To add a guest, you need to have a role that allows you to create users in your tenant directory. For example, at least a [Guest Inviter role](/en-us/entra/identity/role-based-access-control/permissions-reference#guest-inviter) or a [User Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator).

Important

Use roles with the fewest permissions. Lower permissioned accounts help improve security for your organization. Global Administrator is a highly privileged role. Limit its use to emergency scenarios when you can't use an existing role. For more information, see [About admin roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

## Add guests to Teams

The following video shows how to create a team with guests in Microsoft Teams. It's one minute and 26 seconds long.

## Join a team as a guest

The following video shows how to join a team as a guest in Microsoft Teams. It's one minute and 38 seconds long.

## Understanding guest accounts in Microsoft 365

To easily share files and documents with the right people while preventing oversharing, you need to plan your approach. The following resources provide more background to help you create a secure guest sharing environment in Microsoft 365.

- [Plan external collaboration](/en-us/previous-versions/microsoft-365/solutions/plan-external-collaboration)
- [Create a secure guest sharing environment](/en-us/previous-versions/microsoft-365/solutions/create-secure-guest-sharing-environment)
- [Set up secure file and document sharing and collaboration with Teams in Microsoft 365](/en-us/previous-versions/microsoft-365/solutions/setup-secure-collaboration-with-teams)
- [Guest access in Microsoft Teams](/en-us/microsoftteams/guest-access)

In addition to Microsoft Teams and SharePoint, Microsoft 365 also supports guest access in other applications. The following Microsoft 365 products support guest access.

- **Power Apps (Canvas apps)**: [Share a canvas app with guests](/en-us/power-apps/maker/canvas-apps/share-app-guests).
- **Lists**: [External or guest sharing in OneDrive, SharePoint, and Lists](https://support.microsoft.com/office/external-or-guest-sharing-in-onedrive-sharepoint-and-lists-7aa070b8-d094-4921-9dd9-86392f2a79e7).
- **OneDrive**: [External or guest sharing in OneDrive, SharePoint, and Lists](https://support.microsoft.com/office/external-or-guest-sharing-in-onedrive-sharepoint-and-lists-7aa070b8-d094-4921-9dd9-86392f2a79e7).
- **Planner**: Applies to Web and mobile platforms. [Guest access in Microsoft Planner](https://support.microsoft.com/office/guest-access-in-microsoft-planner-cc5d7f96-dced-4da4-ab62-08c72d9759c6).
- **Microsoft 365 Groups**: [Manage guest access in Microsoft 365 Groups](../create-groups/manage-guest-access-in-groups).
- **Viva Engage**: [Work with external groups in Viva Engage networks not aligned to native mode](/en-us/viva/engage/work-with-external-users/create-and-manage-external-groups).

For apps in Microsoft 365 like Word and Excel, the location of the output file controls guest access. For example, Microsoft SharePoint, Teams, and OneDrive.

## Next steps: Add guests in Microsoft Entra External ID

To add guests in Microsoft Entra External ID, see [add a guest](/en-us/entra/external-id/b2b-quickstart-add-guest-users-portal).

After you add a user, you can also assign them to a group or give them access to an app in your organization. When you add a user in the Microsoft Entra admin center, the user also appears on the **Guest users** page in the [Microsoft 365 admin center](https://admin.microsoft.com/).

To invite multiple guests to collaborate with your organization, see [add guests in bulk](/en-us/entra/external-id/tutorial-bulk-invite).