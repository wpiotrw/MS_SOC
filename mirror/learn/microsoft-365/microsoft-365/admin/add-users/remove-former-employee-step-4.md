---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Step 4 - Forward a former employee's email to another employee or convert to a shared mailbox - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/remove-former-employee-step-4?view=o365-worldwide
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
ms.date: 2025-10-28T00:00:00.0000000Z
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
description: Forward a former employee's email to another employee or convert it to a shared mailbox where several people are able to access it instead of one person.
locale: en-us
document_id: bff0c10d-5f00-da0d-3780-70596925a3db
document_version_independent_id: bff0c10d-5f00-da0d-3780-70596925a3db
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/add-users/remove-former-employee-step-4.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/add-users/remove-former-employee-step-4
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/add-users/remove-former-employee-step-4.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 2ae134c5-bf97-8aed-6585-efa75dcaf72f
---

# Step 4 - Forward a former employee's email to another employee or convert to a shared mailbox - Microsoft 365 admin | Microsoft Learn

If an employee leaves your organization, and you don't want to lose existing email or calendar information, you can either assign the former employee's email address to another employee, or convert the former employee's mailbox to a shared mailbox.

Note

You must have appropriate permissions through a role, such as [Microsoft 365 Backup Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#microsoft-365-backup-administrator) or [User Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) to perform the tasks in this article.

## Convert former employee's mailbox to a shared mailbox

When you convert a user's mailbox to a shared mailbox, all of the existing email and calendar are retained in a shared mailbox that several people can acess. You can convert a shared mailbox back to an individual user's private mailbox later if needed.

- Creating a shared mailbox can be a less expensive way to go because you don't have to pay for a license **as long as the mailbox is smaller than 50 GB**. If it is over 50 GB, you need to assign a license to it.
- If you convert the mailbox to a shared mailbox, all the old email is available, too. This configuration can take up a lot of space.
- If you set up email forwarding, only *new* emails sent to the former employee's email address are sent to the current employee.

Follow these steps to [convert the user's mailbox to a shared mailbox](../email/convert-user-mailbox-to-shared-mailbox).

## Forward a former employee's email to another employee

Important

If you're setting up email forwarding or a shared mailbox, don't delete the former employee's account. The account needs to be there to anchor the email forwarding or shared mailbox.

1. In the [Microsoft 365 admin center](https://admin.cloud.microsoft/), go to **Users** &gt; **Active users**. (Or, go directly to the [Active users page](https://go.microsoft.com/fwlink/p/?linkid=834822).)
2. Select the name of the former employee, and then select the **Mail** tab.
3. Under **Email Forwarding**, select **Manage email forwarding**.
4. Select **Forward all emails sent to this mailbox**. In the **Forwarding email address** box, type the email address of the current employee who's going to get the email. Choose whether to keep a copy of the forwarded email in the former employee's mailbox.
5. Select **Save changes**. Remember not to delete the former employee's account.

Important

In scenarios where the mailbox is inactive due to compliance reasons, mail forwarding or converting the mailbox to a shared mailbox doesn't work.

### Cancel Outlook meetings

Make sure to cancel all meetings that the former user had on their calendar. This lets people remove the meetings created by the former user.

If the person had meetings that booked equipment or rooms, they won't be available to be booked until those meetings are canceled. Read [Delete an appointment or a meeting](https://support.microsoft.com/office/delete-an-appointment-or-a-meeting-2703bfdb-9a07-4396-be3b-a9f79438455b) for the steps.