---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Step 6 - Remove and delete a Microsoft 365 for business license from a former employee - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/remove-former-employee-step-6?view=o365-worldwide
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
ms.date: 2026-01-05T00:00:00.0000000Z
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
description: You can remove a former employee's Microsoft 365 license, and then delete it from your subscription or assign the license to another user.
locale: en-us
document_id: ec150243-21c5-7e85-bb76-632cf4d4c242
document_version_independent_id: 9d2b32f2-9a77-d44c-f631-4e4400f300c7
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/add-users/remove-former-employee-step-6.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/add-users/remove-former-employee-step-6
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/add-users/remove-former-employee-step-6.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
platformId: 8d3c2641-8475-6e88-212d-b144a744cd02
---

# Step 6 - Remove and delete a Microsoft 365 for business license from a former employee - Microsoft 365 admin | Microsoft Learn

If an employee leaves your organization, and you don't want to continue to pay for their Microsoft 365 license, you can unassign that license and then delete it from your subscription. You can reassign a license to another user if you don't want to delete it. This article describes how to remove a license from a user and delete it.

Before you remove a license, you *must* remove all holds for the user. For more information about holds, see [Remove an In-Place Hold in Exchange Online](/en-us/exchange/security-and-compliance/create-or-remove-in-place-holds).

If the mailbox needs to be accessed by authorized people who have been granted eDiscovery permissions for compliance or legal reasons, it must be assigned an Exchange Online Plan 2 license (or an Exchange Online Plan 1 license with an Exchange Online Archiving add-on license) so that a hold can be applied to the mailbox before it's deleted. After the user account is deleted, any Exchange Online license associated with the user account will be available to assign to a new user.

When you remove a license, that user's data is held for 30 days. You can [access](get-access-to-and-back-up-a-former-user-s-data) the data, or [restore](restore-user) the account if need be.

After 30 days, the user's content (except for documents stored in SharePoint) is permanently deleted from Microsoft 365 and can't be recovered.

Note

You must have appropriate permissions through a role, such as [License Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#license-administrator) or [User Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) to perform the tasks in this article.

## Remove licenses

1. In the [Microsoft 365 admin center](https://admin.cloud.microsoft/), go to **Users** &gt; **Active users**. (Or go directly to the [Active users page](https://go.microsoft.com/fwlink/p/?linkid=834822).)
2. Select the name of the former employee, and then select the **Licenses and Apps** tab.
3. Clear the check boxes for the licenses you want to remove, and then select **Save changes**.

## Reduce the number of licenses

To reduce the number of licenses you're paying for until you hire another person, do the following steps:

1. In the [Microsoft 365 admin center](https://admin.cloud.microsoft/), go to **Billing** &gt; **Your products**. (Or, go directly to the [Your products page](https://go.microsoft.com/fwlink/p/?linkid=842054).)
2. Select the subscription from which you want to remove licenses.
3. On the subscription page, select **Remove licenses**.
4. In the **Remove licenses** pane, specify when the following information:

    - When the change could take effect
    - What the new total license quantity should be
5. Select **Save**.

## How the deleted employee account affects their PSTN number

When you remove a user's license from your Microsoft 365 subscription, and your organization is using [Public Switched Telephone Network (PSTN) connectivity](/en-us/microsoftteams/pstn-connectivity), the PSTN calling number associated with the former employee is released. You can then assign it to another user. See [Manage phone numbers for users](/en-us/microsoftteams/assign-change-or-remove-a-phone-number-for-a-user?tabs=assign-by-number-list).

If the user belongs to a queue group, they're no longer a viable target of the call queue agents. We recommend removing that user from any groups that are associated with the call queue.

## Set up call forwarding to people in your organization

If you need to set up call forwarding for the terminated employee's phone number, the call forwarding setting under calling policies can be set up forwarding. Incoming calls can be forwarded to other users or can ring another person at the same time. For more information, see [Calling policies in Microsoft Teams](/en-us/microsoftteams/teams-calling-policy).