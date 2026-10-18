---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Step 2 - Save the contents of a former employee's mailbox - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/remove-former-employee-step-2?view=o365-worldwide
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
ms.date: 2026-03-06T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-admin
ms.localizationpriority: medium
ms.collection:
- Tier1
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- SPO_Content
ms.custom:
- MSStore_Link
- TRN_M365B
- OKR_SMB_Videos
- AdminSurgePortfolio
- m365solution-removeemployee
- user-accounts
description: Once you've blocked a user from being able to log into your organization, learn two ways you can save the contents of the former employee's mailbox.
locale: en-us
document_id: 9b2ba944-52a9-1dc9-eebe-e16111a8ccc4
document_version_independent_id: 22f2b1ec-a287-b315-ae6c-caeabc86beba
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/add-users/remove-former-employee-step-2.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/add-users/remove-former-employee-step-2
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/add-users/remove-former-employee-step-2.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
platformId: 6c25f310-5947-a27a-a911-a25717520a67
---

# Step 2 - Save the contents of a former employee's mailbox - Microsoft 365 admin | Microsoft Learn

If a former employee is subject to a litigation hold or in-place hold, you can export their Outlook content to a `.pst` file.

You must have appropriate permissions through a role, such as [Microsoft 365 Backup Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#microsoft-365-backup-administrator) or [User Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) to perform the tasks in this article.

## Place hold or export user's data to a .pst file

If a former employee is blocked from signing into your organization's Microsoft 365 subscription, and it's important that you don't lose their data, you can save the contents of the former employee's mailbox. There are two ways you can save the contents of the former employee's mailbox.

- **Place a litigation hold or an in-place hold on the mailbox** before the deleting the user account. This is much more complicated than the other option, but is worth doing if your Enterprise plan includes archiving and legal hold, litigation is a possibility, and you have a technically strong IT department.

    After you convert the mailbox to an inactive mailbox, administrators, compliance officers, or records managers can use In-Place eDiscovery tools in Exchange Online to access and search the contents.

    Inactive mailboxes can't receive email and aren't displayed in your organization's shared address book or other lists.

    To learn how to place a hold on a mailbox, see [Manage inactive mailboxes in Exchange Online](../../compliance/create-and-manage-inactive-mailboxes).

**OR**

- **Add the former employee's email address to your version of Outlook** (desktop app), and then export the data to a `.pst` file. You can import the data to another email account as needed.

    See the following articles:

    - [Step 4 - Give another employee access to OneDrive and Outlook data](remove-former-employee-step-4)
    - [Export emails, contacts, and calendar items to Outlook using a .pst file](https://support.microsoft.com/office/export-emails-contacts-and-calendar-items-to-outlook-using-a-pst-file-14252b52-3075-4e9b-be4e-ff9ef1068f91)