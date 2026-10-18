---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Step 1 - Prevent user sign-in and block access to Microsoft 365 - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/remove-former-employee-step-1?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: Learn how to block a user from signing in and restrict their access to Microsoft 365 services with step-by-step instructions for admins.
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
- admindeeplinkEXCHANGE
- has-azure-ad-ps-ref, azure-ad-ref-level-one-done
- user-accounts
locale: en-us
document_id: 4ecd4f58-0a50-05f2-426d-6bc8ca8f5940
document_version_independent_id: b3344450-204e-3bb4-54ad-5fa4f85a2695
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/add-users/remove-former-employee-step-1.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/add-users/remove-former-employee-step-1
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/add-users/remove-former-employee-step-1.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: c4bdd4d3-cf60-b1a0-0752-89c141108b6d
---

# Step 1 - Prevent user sign-in and block access to Microsoft 365 - Microsoft 365 admin | Microsoft Learn

When an employee leaves your organization, the first step to preventing unauthorized access is to reset their password. You can also force the user account to be signed out from your Microsoft 365 services. If you think the account might be compromised, make sure to block signing in so that no one can use those credentials.

## Prerequisites

To complete this action for standard users, you must have an appropriate role assigned, such as User Administrator or Helpdesk Administrator role.

To sign out other administrators, you need to be a Global Administrator.

Important

Use roles with the fewest permissions. Lower permissioned accounts help improve security for your organization. Global Administrator is a highly privileged role. Limit its use to emergency scenarios when you can't use an existing role. For more information, see [About admin roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

## Reset password and sign out of all sessions

1. In the [Microsoft 365 admin center](https://admin.cloud.microsoft/), go to **Users** &gt; **Active users**. (Or, go directly to the [Active users page](https://admin.cloud.microsoft/?#/users).)
2. Select the user's name, then select **Reset password**.
3. Choose whether to automatically create a new password and whether to require the user to change their password when they first sign in.
4. Select **Reset password**. You can print the new password if you want. Then select **Close**.
5. Select the user's name again, and on the **Account** tab, select **Sign out of all sessions**.

Within an hour, or after the user leaves the current Microsoft 365 page they're on, they're prompted to sign in again. An access token is good for an hour, so the timeline depends on how much time is left on that token, and whether they leave the current webpage.

Important

If the user is using their mailbox in Outlook on the web, they might not be signed out immediately. As soon as they select a different tile, such as OneDrive, or refresh their browser, the service signs them out.

To use PowerShell to sign out a user immediately, see the [Revoke-MgUserSignInSession](/en-us/powershell/module/microsoft.graph.users.actions/revoke-mgusersigninsession) cmdlet.

For more information about how long it takes to get someone out of email, see [What you need to know about ending an user's email session](remove-former-employee-step-7#what-you-need-to-know-about-terminating-an-employees-email-session).

## Block a user's access to Microsoft 365 services

Important

Blocking an account can take up to 24 hours to take effect. To immediately prevent a user's sign-in access, follow the previous steps to reset their password.

1. In the [Microsoft 365 admin center](https://admin.cloud.microsoft/), go to **Users** &gt; **Active users**. (Or, go directly to the [Active users page](https://admin.cloud.microsoft/?#/users).)
2. Select the name of the user that you want to block, and select **Block sign-in**.
3. On the **Block sign-in** page, select **Block this user from signing in**, and then **Save changes**.

## Block a user's access to email in Exchange Online

If you have email as part of your Microsoft 365 subscription, you can use the Exchange admin center to block a user from accessing their email. See [Manage user mailboxes in Exchange Online](/en-us/exchange/recipients-in-exchange-online/manage-user-mailboxes/manage-user-mailboxes).

1. In the [Exchange admin center](https://admin.exchange.microsoft.com/), go to **Recipients** &gt; **Mailboxes**. (Or, go directly to the [Mailboxes page](https://admin.cloud.microsoft/exchange#/mailboxes).)
2. Select a user's mailbox.
3. Under **Email apps & mobile devices**, select **Manage email apps settings**.
4. On the **Manage email apps settings** page, turn **Off** the slider for all the options:

    - **Outlook desktop (MAPI)**
    - **Exchange web services**
    - **Mobile (Exchange ActiveSync)**
    - **IMAP**
    - **POP3**
    - **Outlook on the web**
5. Select **Save**.