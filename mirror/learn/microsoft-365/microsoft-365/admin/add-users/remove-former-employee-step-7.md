---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Step 7 - Delete a former employee's user account - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/remove-former-employee-step-7?view=o365-worldwide
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
description: After you've saved and accessed all of a former employee's user data, you can delete the former employee's account in the Microsoft 365 admin center.
locale: en-us
document_id: 1313c6f6-7fb6-4487-5a6a-495eb4d77ac9
document_version_independent_id: f17ee402-dc00-c939-abfe-3afe2a3bee3a
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/add-users/remove-former-employee-step-7.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/add-users/remove-former-employee-step-7
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/add-users/remove-former-employee-step-7.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/37da4cc9-0cfc-42a9-ba5e-805706b01ef8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3661fb96-d414-4a4e-b7ad-9370637790dd
platformId: b0bff1d5-8282-cee5-f1b5-4796fb8cf760
---

# Step 7 - Delete a former employee's user account - Microsoft 365 admin | Microsoft Learn

After an employee has left your organization, and you've saved and accessed their user data, you can delete the former employee's account.

Important

Don't delete the account if you've set up email forwarding or converted it to a shared mailbox. Both need the account to anchor the forwarding or shared mailbox.

You must have appropriate permissions through a role, such as [User Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) to perform the tasks in this article.

1. In the [Microsoft 365 admin center](https://admin.cloud.microsoft/), go to **Users** &gt; **Active users**. (Or, go directly to the [Active users page](https://go.microsoft.com/fwlink/p/?linkid=834822).)
2. Select the name of the former employee's account that you want to delete.
3. Under the user's name, select **Delete user**. Choose the options you want for this user, and then select **Delete user**. If you've already given another user access to this user's email and OneDrive, you don't have to do it again here.

When you delete a user, the account becomes inactive for approximately 30 days. You have until then to restore the account before it's permanently deleted.

## Watch: Delete a former employee's user account

If you found this video helpful, check out the [complete training series for small businesses and those new to Microsoft 365](../../business-video/).

## Does your organization use Active Directory?

If your organization synchronizes user accounts to Microsoft 365 from a local Active Directory environment, you must delete and restore those user accounts in your local Active Directory service. You can't delete or restore the user in the Microsoft 365 admin center.

To learn how to delete and restore user account in Active Directory, see [Delete a User Account](/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753730%28v=ws.11%29).

If you're using Microsoft Entra ID, see the [Remove-MgUser](/en-us/powershell/module/microsoft.graph.users/remove-mguser) PowerShell cmdlet.

## What you need to know about terminating an employee's email session

Here's information about how to get an employee out of email (Exchange).

| What you can do | How you do it |
| --- | --- |
| Terminate a session (such as Outlook on the web, Outlook, Exchange active sync, etc.) and force to open a new session | Reset password |
| Terminate a session and block access to future sessions (for all protocols) | Disable the account. For example, in the Exchange admin center or using PowerShell: `Set-Mailbox user@contoso.com -AccountDisabled:$true` |
| Terminate the session for a particular protocol (such as ActiveSync) | Disable the protocol. For example, in the Exchange admin center or using PowerShell: `Set-CASMailbox user@contoso.com -ActiveSyncEnabled:$false` |

The preceding operations can be done in three places:

| If you terminate the session here | How long it takes |
| --- | --- |
| In the Exchange admin center or using PowerShell | Expected delay is within 30 min |
| In the Microsoft Entra admin center | Expected delay is 60 min |
| In an on-premises environment | Expected delay is 3 hours or more |

### How to get fastest response for account termination

**Fastest**: Use the Exchange admin center (use PowerShell) or Microsoft Entra admin center. In an on-premises environment, it can take several hours to sync the change through Microsoft Entra Connect.

**Fastest for a user with presence on-premises and in the Exchange Datacenter**: Terminate the session using Microsoft Entra admin center/Exchange admin center AND make the change in the on-premises environment as well. Otherwise, the change in Microsoft Entra admin center/Exchange admin center is overwritten by Microsoft Entra Connect.