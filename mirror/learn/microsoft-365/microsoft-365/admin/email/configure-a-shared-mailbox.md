---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Configure shared mailbox settings - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/email/configure-a-shared-mailbox?view=o365-worldwide
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
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- operations-pod
ms.custom:
- MSStore_Link
- AdminSurgePortfolio
- AdminTemplateSet
- user-accounts
description: Create a shared mailbox and configure some settings for its users, such as email forwarding and automatic replies.
locale: en-us
document_id: 198eb002-1d99-5a13-05d4-34d1cbb8d9d9
document_version_independent_id: 6218b3c9-f0a2-ed0e-ef0a-c99c3c280030
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/email/configure-a-shared-mailbox.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/email/configure-a-shared-mailbox
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/email/configure-a-shared-mailbox.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 718f5de4-7138-86f7-27f2-1952e8e7346d
---

# Configure shared mailbox settings - Microsoft 365 admin | Microsoft Learn

After you have [created a shared mailbox](create-a-shared-mailbox), you'll want to configure some settings for the mailbox users, such as email forwarding and automatic replies. Later, you might want to change other settings, such as the mailbox name, members, or member permissions.

## Change the name of a shared mailbox

1. In the admin center, go to **Teams & groups** &gt; [Shared mailboxes](https://go.microsoft.com/fwlink/p/?linkid=2066847).
2. Select the shared mailbox you want to edit, and then select **Edit** under **Basic information**.
3. Enter a new name for the shared mailbox.
4. Select **Save**.

## Change the email address of a shared mailbox

1. In the admin center, go to **Teams & groups** &gt; [Shared mailboxes](https://go.microsoft.com/fwlink/p/?linkid=2066847).
2. Select the shared mailbox you want to edit, and then select **Edit** under **Email addresses**.
3. Enter a new email address for the shared mailbox. If you want to change the primary email address, your mailbox must have more than one email alias.

## Forward emails that are sent to a shared mailbox

Important

Email forwarding to recipients outside the organization doesn't prevent messages identified as spam, phishing, or malware from being forwarded. The recipient needs their own email security filter to identify and block these messages.

You do not need to assign a license to the shared mailbox in order to forward email that's sent to it. You can forward the messages to any valid email address or distribution list.

1. In the admin center, go to **Teams & groups** &gt; [Shared mailboxes](https://go.microsoft.com/fwlink/p/?linkid=2066847).
2. Select the shared mailbox you want to edit, then select **Edit** under **Email forwarding**.
3. Select the checkbox to **Forward all emails sent to this mailbox**. Enter one email address to forward the messages to. It can be any valid email address. To forward to multiple addresses, you need to [create a distribution group](/en-us/office365/admin/setup/create-distribution-lists) for the addresses, and then enter the name of the group in this box.
4. Select **Save**.

## Send automatic replies from a shared mailbox

1. In the admin center, go to **Teams & groups** &gt; [Shared mailboxes](https://go.microsoft.com/fwlink/p/?linkid=2066847).
2. Select the shared mailbox you want to edit, then select **Edit** under **Automatic replies**.
3. Select the checkbox to **Send automatic replies to senders inside this organization**.
4. Enter the replies you want to send to people inside or outside your organization. You can't add images, only text.
5. Select **Save**.

## Allow everyone to see the Sent email (the replies)

By default, messages sent from the shared mailbox aren't saved to the Sent Items folder of the shared mailbox. Instead, they are saved to the Sent Items folder of the person who sent the message.

If you want to allow everyone to see the Sent email, in the admin center, edit the shared mailbox settings. Select **Edit** under **Sent items**. Select the options you want for sent items.

## Choose the apps that a shared mailbox can use to access Microsoft email

1. In the admin center, go to **Teams & groups** &gt; [Shared mailboxes](https://go.microsoft.com/fwlink/p/?linkid=2066847).
2. Select the shared mailbox you want to edit, then select **Edit** under **Email apps**.
3. Select the checkboxes for all of the apps you want members to be able to use to access the shared mailbox.
4. Select **Save**.

## Put a shared mailbox on litigation hold

To learn more about litigation hold, see [Create a Litigation Hold](../../compliance/ediscovery-create-a-litigation-hold).

1. Go to the [Exchange admin center](https://go.microsoft.com/fwlink/p/?linkid=2059104).
2. Select **Recipients** &gt; **Mailboxes** and select the shared mailbox you want to manage.
3. On the **Others** tab, select **Edit** under **Litigation hold**.
4. Enter a duration, a note about the hold for the user if you want, and a URL with more information.
5. Select **Save**.

## Add or remove members

1. In the Microsoft 365 admin center, go to **Teams & groups** &gt; [Shared mailboxes](https://go.microsoft.com/fwlink/p/?linkid=2066847).
2. Select the shared mailbox you want to edit, then select **Edit** under **Members**.
3. Do one of the following:

    - To add members, select **Add members**, search for or select a member to add, and then select **Save**.
    - To remove members, use the Search box to search for the member if necessary, deselect the member and choose **Remove member**.

## Add or remove permissions of members

1. In the Microsoft 365 admin center, go to **Teams & groups** &gt; [Shared mailboxes](https://go.microsoft.com/fwlink/p/?linkid=2066847).
2. Select the shared mailbox you want to edit, then under Manage mailbox permissions, select one of the permissions.
3. Do one of the following:

    - To give that permission to an additional member, select **Add permissions**, search for or select a member to add, and then select **Add**.
    - To remove the permission from a member, select the user, and then select **Remove permissions**.

## Show or hide a shared mailbox in the global address list

If you choose not to show the shared mailbox in the global address list, the mailbox won't appear in your organization's address list, but it will still receive email sent to it.

1. In the Microsoft 365 admin center, go to **Teams & groups** &gt; [Shared mailboxes](https://go.microsoft.com/fwlink/p/?linkid=2066847).
2. Select the shared mailbox you want to edit, then select **Edit** under **Show in global address list**.
3. Select the option you want next to Show in my organization's global address list. Select **Save**.

Note

Hiding a shared mailbox from address list will make it impossible for new shared mailbox members to add the hidden mailbox to their Outlook profile until the shared mailbox is again shown in the address list.