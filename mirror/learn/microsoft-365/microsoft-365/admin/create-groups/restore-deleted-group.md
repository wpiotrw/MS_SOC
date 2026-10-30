---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Restore a deleted Microsoft 365 group - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/restore-deleted-group?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
ms.reviewer: rahulnayak
ms.date: 2026-07-28T00:00:00.0000000Z
f1.keywords: CSH
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
- AdminSurgePortfolio
- AdminTemplateSet
- m365-groups
- user-accounts
search.appverid:
- BCS160
- MET150
- MOE150
ms.assetid: b7c66b59-657a-4e1a-8aa0-8163b1f4eb54
description: A deleted group is retained for 30 days and you can still restore the group. After 30 days, the group and its content are permanently deleted.
customer-intent: As an administrator, I want to restore a Microsoft 365 group that was previously deleted.
locale: en-us
document_id: 7d49db57-a705-20aa-e98d-5b3d6bbbf9fd
document_version_independent_id: 5a056f2c-03c9-7a34-3196-8bfb1039f6a5
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/create-groups/restore-deleted-group.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/create-groups/restore-deleted-group
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/create-groups/restore-deleted-group.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
platformId: 653bd7a2-feaf-a015-9dec-310519152bd0
---

# Restore a deleted Microsoft 365 group - Microsoft 365 admin | Microsoft Learn

If you delete a group, by default, it's retained for 30 days. This 30-day period is considered a "soft-delete" because you can still restore the group. After 30 days, the group and its associated contents are permanently deleted and can't be restored.

When a group is restored, the following content is restored:

- Microsoft Entra Microsoft 365 Groups object, properties, and members
- Group's e-mail addresses
- Exchange Online shared Inbox and calendar
- SharePoint Online team site and files
- OneNote notebook
- Planner
- Teams
- Viva Engage group and group content (If the Microsoft 365 group was created from Viva Engage)
- Power BI [Classic workspace](/en-us/power-bi/collaborate-share/service-create-workspaces)

Note

This article describes how to restore Microsoft 365 groups only.

## Restore a group

You can restore a group in Outlook, the Microsoft 365 admin center, or PowerShell.

### Restore a group in Outlook

If you're the owner of a Microsoft 365 group, you can restore the group yourself in Outlook on the web by following these steps:

1. In Outlook, on the [deleted groups page](https://outlook.office.com/people/group/deleted), select the **Manage groups** option under the **Groups** node, and then choose **Deleted**.
2. Select the **Restore** tab next to the group you want to restore.

If the deleted group doesn't appear here, contact an administrator.

### Restore a group in the Microsoft 365 admin center

If you're a groups administrator, you can restore a deleted group in the Microsoft 365 admin center:

1. Go to the [Microsoft 365 admin center](https://admin.cloud.microsoft/) and sign in.
2. Expand **Groups**, and then select **Deleted groups**.
3. Select the group that you want to restore, and then select **Restore group**.

### Restore a group by using PowerShell

To use PowerShell to restore a deleted group, see [Restore a deleted Microsoft 365 group or cloud security group in Microsoft Entra ID](/en-us/entra/identity/users/groups-restore-deleted#view-the-deleted-microsoft-365-groups-that-are-available-to-restore-by-using-powershell).

Note

1. In some cases, it can take as long as 24 hours for the group and all of its data to be restored.
2. After restoring a Microsoft 365 Group, wait at least one hour before sending email messages to the group. Messages sent immediately after restoration may fail with an NDR error message that says `550 5.1.10_ RESOLVER.ADR.RecipientNotFound`.

## Do you have questions about Microsoft 365 Groups?

Visit the [Microsoft Tech Community](https://techcommunity.microsoft.com/t5/microsoft-365-groups/bd-p/Microsoft365Groups) to post questions and participate in conversations about Microsoft 365 groups.