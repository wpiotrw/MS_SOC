---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Configure email forwarding - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/email/configure-email-forwarding?view=o365-worldwide
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
ms.date: 2026-02-03T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier3
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- must-keep
- operations-pod
ms.custom:
- MSStore_Link
- AdminSurgePortfolio
- okr_smb
- AdminTemplateSet
- business_assist
description: Email forwarding lets you forward email messages sent to a Microsoft 365 user mailbox to another mailbox inside or outside of your organization.
locale: en-us
document_id: 5885a586-76b8-83ae-161b-6c9c8793b42d
document_version_independent_id: 681fe343-6272-a75a-ed00-dc7ef4355e67
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/email/configure-email-forwarding.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/email/configure-email-forwarding
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/email/configure-email-forwarding.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 297379d1-52cf-603e-bb1b-aa5d1ea0a5d3
---

# Configure email forwarding - Microsoft 365 admin | Microsoft Learn

As the admin of an organization, you might have company requirements to set up email forwarding for a user's mailbox. Email forwarding lets you forward email messages sent to a user's mailbox to another user's mailbox inside or outside of your organization.

Important

You can use outbound spam filter policies to control automatic forwarding to external recipients. For more information, see [Control automatic external email forwarding in Microsoft 365](/en-us/microsoft-365/security/office-365-security/outbound-spam-policies-external-email-forwarding#how-the-outbound-spam-filter-policy-settings-work-with-other-automatic-email-forwarding-controls).

Email forwarding to external recipient domains outside the organization doesn't prevent messages identified as spam, phishing, or high-confidence phishing from being forwarded. The recipient needs their own email security filter to identify and block these messages.

## Before you begin

Before you set up email forwarding, note the following:

- Allow automatically forwarded messages to be sent to people on the remote domain. See [Manage remote domains](/en-us/exchange/mail-flow-best-practices/remote-domains/manage-remote-domains) for details.
- Once you set up email forwarding, only **new** emails sent to the **from** mailbox will be forwarded.
- Email forwarding requires that the *from* account has a license unless it's a shared mailbox. If you're setting up email forwarding because the user has left your organization, another option is to [convert their mailbox to a shared mailbox](convert-user-mailbox-to-shared-mailbox). This way several people can access it. However, a shared mailbox can't exceed 50 GB.
- You must be an Exchange administrator in Microsoft 365 to do these steps. For more information, see the article [About admin roles](../add-users/about-admin-roles).

## Configure email forwarding

::: moniker range="o365-worldwide"

1. In the admin center, go to the **Users** &gt; **[Active users](https://go.microsoft.com/fwlink/p/?linkid=834822)** page.
2. Select the name of the user whose email you want to forward and select the **Mail** tab.
3. Select **Manage email forwarding**.
4. On the email forwarding page, select **Forward all emails sent to this mailbox**. Enter the forwarding address, and choose whether you want to keep a copy of forwarded emails. If you don't see this option, make sure a license is assigned to the user account. Select **Save changes**.
5. Don't delete the account of the user who's email you're forwarding or remove their license! If you do, email forwarding will stop.

**To forward to multiple email addresses**, you can ask this user to set up a rule in Outlook to forward to the addresses. For more info, check out [Turn on automatic forwarding in Outlook](https://support.microsoft.com/office/turn-on-automatic-forwarding-in-outlook-7f2670a1-7fff-4475-8a3c-5822d63b0c8e). For Outlook on the web, see [Use rules to automatically forward messages](https://support.microsoft.com/office/45aa9664-4911-4f96-9663-ece42816d746).

::: moniker-end

::: moniker range="o365-21vianet"

1. In the admin center, go to the **Users** &gt; **[Active users](https://go.microsoft.com/fwlink/p/?linkid=850628)** page.
2. Select the name of the user whose email you want to forward to open the properties page.
3. Expand **Mail settings**, and then in the **Email forwarding** section, select **Edit**.
4. On the email forwarding page, set the toggle to **On**, enter the forwarding address, and choose whether you want to keep a copy of forwarded emails. If you don't see this option, make sure a license is assigned to the user account. Select **Save**.

    **To forward to multiple email addresses**, you can ask the user to set up a rule in Outlook to forward to the addresses. To learn more, see [Use rules to automatically forward messages](https://support.microsoft.com/office/45aa9664-4911-4f96-9663-ece42816d746).

    Or, in the admin center, [create a distribution group](../setup/create-distribution-lists), [add the addresses to it](add-user-or-contact-to-distribution-list), and then set up forwarding to point to the DL using the instructions in this article.
5. Don't delete the account of the user who's email you're forwarding or remove their license! If you do, email forwarding will stop.

::: moniker-end