---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Restore a user - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/restore-user?view=o365-worldwide
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
ms.date: 2026-01-06T00:00:00.0000000Z
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
ms.custom:
- MSStore_Link
- AdminSurgePortfolio
- AdminTemplateSet
- user-accounts
description: Within 30 days of deleting a user account, you can restore the account and all data, and the user can sign in with the same account.
customer-intent: As an admin, I want to restore a user account that was deleted.
locale: en-us
document_id: c346b60d-9c8e-2b49-fa69-a6525978f5fc
document_version_independent_id: 519bb4de-6226-907f-e666-6439b017e384
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/add-users/restore-user.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/add-users/restore-user
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/add-users/restore-user.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 64a2476a-73ae-8fb2-2b42-3104446f76fa
---

# Restore a user - Microsoft 365 admin | Microsoft Learn

When you restore a user account within 30 days of deleting it, the account and all associated data are restored. The user can sign in with their same work or school account. Their mailbox is fully restored.

To find out how much time remains to restore a specific user account, [contact support](../../business-video/get-help-support).

Tip

- Make sure enough Microsoft 365 licenses are available to assign to the account.
- If your business uses Active Directory on-premises, see [How to restore deleted user accounts in Microsoft 365, Azure, and Intune](/en-us/microsoft-365/troubleshoot/active-directory/restore-deleted-user-accounts).

## Restore one or more user accounts

You must be a [User Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) to do these steps.

1. In the [Microsoft 365 admin center](https://admin.cloud.microsoft/), go to **Users** &gt; **Deleted users**. (Or, go directly to the [Deleted users page](https://go.microsoft.com/fwlink/p/?linkid=2071581).)
2. On the **Deleted users** page, select the name of the user you want to restore, and then select **Restore user**. To restore multiple deleted accounts, select multiple users.

    If you don't see the user account you're looking for on the **Deleted users** page, it might be that too much time has elapsed since the user account was deleted. In this case, [Get support for Microsoft 365 for business](../get-help-support).
3. Follow the prompts to set their password, and then select **Restore**.
4. If the user is successfully restored, select **Print** to print the user name and password information, and then securely send it to the user.

    If you encounter a user name conflict or proxy address conflict, see Restore a user that has a user name conflict or Restore a user that has a proxy address conflict in this article.
5. After you restore the user, add a license if you want them to use Microsoft 365.

Make sure to notify the user that their password changed and follow up with them.

## Restore a user that has a user name conflict

A user name conflict occurs when you delete a user account, create a new account with the same user name (for the same or a different user), and then try to restore the deleted account.

To resolve the conflict, replace the active user account with the one you're restoring, or assign a different user name to the account you're restoring. Follow these steps:

1. In the [Microsoft 365 admin center](https://admin.cloud.microsoft/), go to **Users** &gt; **Deleted users**. (Or, go directly to the [Deleted users page](https://go.microsoft.com/fwlink/p/?linkid=2071581).)
2. On the **Deleted users** page, select the names of the users you want to restore, and then select **Restore user**.

    Note

    If two or more user accounts fail to be restored, an error message tells you that the restore operation failed for some users. View the log to see which users weren't restored, and then restore the failed accounts one at a time.
3. Follow the prompts to set the password and select **Restore**.
4. If a message appears saying there's a problem restoring the account, take one of the following steps:

    - Cancel the restore and rename the current active user. Then try the restore again.
    - Type a new primary email address for the user and select **Restore**.
5. Review the results, and then select **Close**.

## Restore a user that has a proxy address conflict

A proxy address conflict occurs when you delete a user account that contains a proxy address, assign the same proxy address to another account, and then try to restore the deleted account. Follow these steps to fix this issue.

You must have the [User Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#user-administrator) role assigned to perform this procedure.

1. In the [Microsoft 365 admin center](https://admin.cloud.microsoft/), go to **Users** &gt; **Deleted users**. (Or, go directly to the [Deleted users page](https://go.microsoft.com/fwlink/p/?linkid=2071581).)
2. On the **Deleted users** page, select the user you want to restore, and then select **Restore user**.
3. On the **Restore** page, follow the prompts to set the password and select **Restore**. Any conflicting proxy addresses are automatically removed from the user you're restoring.
4. Review the results, and then select **Close**.