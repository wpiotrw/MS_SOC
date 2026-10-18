---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Create a shared mailbox - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/email/create-a-shared-mailbox?view=o365-worldwide
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
ms.date: 2026-02-02T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-business
ms.localizationpriority: high
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
- okr_smb
- AdminTemplateSet
- admindeeplinkEXCHANGE
- business_assist
- has-azure-ad-ps-ref
- azure-ad-ref-level-one-done
- user-accounts
description: Create a shared mailbox to enable multiple users in your business to share the responsibility of reading and answering email sent to one address.
locale: en-us
document_id: db2dbb29-38c4-afe4-bc0d-3bbc195f6288
document_version_independent_id: bcfee113-ecfe-e358-974e-6f9cd76b8d35
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/email/create-a-shared-mailbox.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/email/create-a-shared-mailbox
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/email/create-a-shared-mailbox.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 473fee98-bf35-951e-98ca-d286ae1043b4
---

# Create a shared mailbox - Microsoft 365 admin | Microsoft Learn

Note

If your organization uses a hybrid Exchange environment, you should use the on-premises [Exchange admin center](https://go.microsoft.com/fwlink/p/?linkid=2059104) to create and manage shared mailboxes. See [Create shared mailboxes in the Exchange admin center](/en-us/Exchange/collaboration/shared-mailboxes/create-shared-mailboxes?preserve-view=true.&amp;view=exchserver-2019)

If you're not sure if you should create a shared mailbox or a Microsoft 365 group for Outlook, see [Compare groups](../create-groups/compare-groups) for some guidance. It's not possible to migrate a shared mailbox to a Microsoft 365 group.

Create shared mailboxes so a group of people can monitor and send email from a common email addresses, like info@contoso.com. When a person in the group replies to a message sent to the shared mailbox, the email appears to be from the shared mailbox, not from the individual user.

Shared mailboxes include a shared calendar. Your team can use the shared calendar as a place for everyone to enter their appointments. For example, if you have 3 people who do customer visits, all can use the shared calendar to enter the customer visit information.

Before creating a shared mailbox, be sure to read [About shared mailboxes](about-shared-mailboxes) for more information.

## Create a shared mailbox and add members

1. Sign in with a user with Exchange admin role. If you get the message "**You don't have permission to access this page or perform this action**," then you aren't an admin.

::: moniker range="o365-worldwide"

1. In the admin center, go to the **Teams & Groups** &gt; [Shared mailboxes](https://go.microsoft.com/fwlink/p/?linkid=2066847) page. Select **Show all** in the left navigation pane if you don't see **Teams & Groups**.

::: moniker-end

::: moniker range="o365-21vianet"

1. In the [admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), go to the **Teams & Groups** &gt; **Shared mailboxes** page.

::: moniker-end

1. On the **Shared mailboxes** page, select **+ Add a shared mailbox**. Enter a name for the shared mailbox. This chooses the email address, but you can edit it if needed.
2. Select **Save changes**. It may take a few minutes before you can add members.
3. Under **Next steps**, select **Add members to this mailbox**. Members are the people who will be able to view the incoming mail to this shared mailbox, and the outgoing replies.
4. Select the **Add members** button. Select the people who you want to use this shared mailbox, and then select **Add**. and then close.

Note

By default, every new shared mailbox has sign-in blocked. For instructions on how to block sign-in for accounts using &gt;[Microsoft Graph PowerShell](/en-us/powershell/microsoftgraph/overview) (including many accounts at the same time), see [Block Microsoft 365 user accounts with PowerShell](../../enterprise/block-user-accounts-with-microsoft-365-powershell).

## Which permissions should you use?

You can use the following permissions with a shared mailbox:

- **Full Access**: The Full Access permission lets a user open the shared mailbox and act as the owner of that mailbox. After accessing the shared mailbox, a user can create calendar items, read, view, delete, and change email messages, and create tasks and calendar contacts. However, a user with Full Access permission can't send email from the shared mailbox unless they also have Send As or Send on Behalf permission.
- **Send As**: The Send As permission lets a user impersonate the shared mailbox when sending mail. For example, if Katerina logs into the shared mailbox Marketing Department and sends an email, it will look like the Marketing Department sent the email.
- **Send on Behalf**: The Send on Behalf permission lets a user send email on behalf of the shared mailbox. For example, if John logs into the shared mailbox Reception Building 32 and sends an email, it will look like the mail was sent by "John on behalf of Reception Building 32". You can use the EAC to grant Send on Behalf permissions or you can use the **Set-Mailbox** cmdlet with the *GrantSendonBehalf* parameter.

Note

The **Send As** and **Send on Behalf** permissions do not work in the Outlook desktop client with the *HiddenFromAddressListsEnabled* parameter on the mailbox set to **True**, since they require the mailbox to be visible in Outlook via the Global Address List.

### Use the EAC to edit shared mailbox delegation

1. In the [Exchange admin center](https://go.microsoft.com/fwlink/p/?linkid=2059104), go to **Recipients** &gt; **Mailboxes**. Select the shared mailbox, and then select **Edit**![Edit icon.](../../media/itpro-eac-editicon.png) .
2. Under **Mailbox permissions**, select **Manage mailbox delegation**.
3. To grant or remove Full Access and Send As permissions, select **Add**![Add Icon.](../../media/itpro-eac-addicon.png) or **Remove**![Remove icon.](../../media/itpro-eac-removeicon.gif) and then select the users you want to grant permissions to.

    Note

    The Full Access permission allows a user to open the mailbox as well as create and modify items in it. The Send As permission allows anyone other than the mailbox owner to send email from this shared mailbox. Both permissions are required for successful shared mailbox operation.
4. Select **Save** to save your changes.

## Add the shared mailbox to Outlook

If you have automapping enabled in your business (by default, most people do), the shared mailbox will appear in your user's Outlook app automatically after they close and restart Outlook.

Automapping is set on the user's mailbox, not the shared mailbox. This means if you try to use a security group to manage who has access to the shared mailbox, automapping won't work. So, if you want automapping, you have to assign permissions explicitly. Automapping is on by default. To learn how to turn it off, see [Remove automapping for a shared mailbox](/en-us/office365/troubleshoot/administration/remove-automapping-for-shared-mailbox).

To learn more about shared mailboxes in Outlook, see:

- [Open and use a shared mailbox in Outlook](https://support.microsoft.com/office/d94a8e9e-21f1-4240-808b-de9c9c088afd)
- [Add a shared mailbox to Outlook on the web](https://support.microsoft.com/office/98b5a90d-4e38-415d-a030-f09a4cd28207)
- [Add a shared mailbox to Outlook mobile](https://support.microsoft.com/office/f866242c-81b2-472e-8776-6c49c5473c9f)
- [Open a shared folder or mailbox in Outlook for Mac](https://support.microsoft.com/office/6ecc39c5-5577-4a1d-b18c-bbdc92972cb2)
- [Add rules to a shared mailbox](https://support.microsoft.com/office/b0963400-2a51-4c64-afc7-b816d737d164)

## Use a shared mailbox on a mobile device (phone or tablet)

You can access a shared mailbox on a mobile device in two ways:

- Add the shared mailbox in the [Outlook for iOS app](https://apps.apple.com/us/app/microsoft-outlook/id951937596) or the [Outlook for Android mobile app](https://play.google.com/store/apps/details?id=com.microsoft.office.outlook&amp;hl=en_US).

    For instructions, see [Add a shared mailbox to Outlook mobile](https://support.microsoft.com/office/f866242c-81b2-472e-8776-6c49c5473c9f).
- Open your browser, sign in, and then go to Outlook on the web. From Outlook on the web you'll be able to access the shared mailbox.

    For instructions, see [Add a shared mailbox to Outlook on the web](https://support.microsoft.com/office/98b5a90d-4e38-415d-a030-f09a4cd28207).

Note

Shared mailbox can only be added to Outlook for iOS app or the Outlook for Android mobile app

## Use the shared calendar

When you created the shared mailbox, you automatically created a shared calendar. We like the shared mailbox calendar rather than a SharePoint calendar for keeping track of appointments and where people are. A shared calendar is integrated with Outlook and it's much easier to use than a SharePoint calendar.

1. In the Outlook app, go to calendar view, and select the shared mailbox.
2. When you enter meetings or appointments, everyone who is a member of the shared mailbox will be able to see them.
3. Any member of the shared mailbox can create, view, and manage appointments on the calendar, just like they would their personal appointments. Everyone who is a member of shared mailbox can see their changes to the shared calendar.

## Remove a license from a shared mailbox

Shared mailboxes usually don't require a license. Follow these instructions to remove a license from a shared mailbox so that you can either assign it to a user or return the license so that you aren't paying for a license you don't need.

Note

An Exchange Online Plan 2 license is required in the following scenarios:

- The shared mailbox has more than 50 GB of storage in use.
- The shared mailbox uses in-place archiving.
- The shared mailbox is placed in litigation hold.

For step-by-step instructions on how to assign licenses, see [Assign licenses to users](/en-us/microsoft-365/admin/manage/assign-licenses-to-users).

## Remove the license

::: moniker range="o365-worldwide"

1. In the admin center, go to the **Users** &gt; [Active users](https://go.microsoft.com/fwlink/p/?linkid=834822) page.

    Note

    You need to remove the license from the Active users page. You can't remove the license from the Shared mailbox page because licenses are user settings.

::: moniker-end

::: moniker range="o365-21vianet"

1. In the admin center, go to the **Users** &gt; [Active users](https://go.microsoft.com/fwlink/p/?linkid=850628) page.

    Note

    You need to remove the license from the Active users page. You can't remove the license from the Shared mailbox page because licenses are user settings.

::: moniker-end

1. Select the shared mailbox.
2. One the **Licenses and Apps** tab, expand **Licenses** and uncheck the box for the license you want to remove.
3. Select **Save changes**.
4. When you return to the **Active users** page, the status of the shared mailbox will be **Unlicensed**.
5. You're still paying for the license. To stop paying for it, [remove the license from your subscription](../../commerce/licenses/buy-licenses).