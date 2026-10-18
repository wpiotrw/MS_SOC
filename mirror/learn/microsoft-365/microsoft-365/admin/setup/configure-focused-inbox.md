---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Configure Focused Inbox for Everyone in Your Organization - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/setup/configure-focused-inbox?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: kwekua
author: kwekuako
manager: scotv
ms.date: 2026-05-07T00:00:00.0000000Z
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
- operations-pod
ms.custom:
- AdminSurgePortfolio
- AdminTemplateSet
- admindeeplinkMAC
- user-accounts
description: Learn how to configure Focused Inbox for everyone in your organization so critical messages stay visible. Follow these steps to set it up now.
locale: en-us
document_id: 88a29483-a070-ccc1-b064-176dfa49d5e9
document_version_independent_id: bad082c0-9ca2-0ade-6b1f-0ba5ac26017b
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/setup/configure-focused-inbox.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/setup/configure-focused-inbox
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/setup/configure-focused-inbox.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
platformId: 88eb8aa4-f195-00f6-aeeb-69a41fca7fd8
---

# Configure Focused Inbox for Everyone in Your Organization - Microsoft 365 admin | Microsoft Learn

If you're responsible for configuring how email works for **everyone** in a business, this article is for you. It explains how to customize Focused Inbox or turn it off for your business, and answers frequently asked questions.

To turn off Focused Inbox just for yourself, see [Turn off Focused Inbox](https://support.microsoft.com/office/f714d94d-9e63-4217-9ccb-6cb2986aa1b2).

If you want to be sure that your users receive business-specific email messages, such as those from HR or payroll, you can configure Focused Inbox so these messages reach the Focused view. You can also control whether users in your organization see the Focused Inbox in their mailbox.

## Turn Focused Inbox on or off in your organization

Use PowerShell to turn Focused Inbox on or off for everyone in your organization. Want to use this feature in the Microsoft 365 admin center? Let our Engineering team know. **[Vote here!](https://go.microsoft.com/fwlink/?linkid=862489)**

### To turn off Focused Inbox

The following PowerShell example turns Focused Inbox **Off** in your organization. However, it doesn't block the availability of the feature for your users. If they want, they can still re-enable Focused Inbox on each of their clients.

1. [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. You need to be assigned permissions before you can perform this procedure or procedures. To see what permissions you need, see the "Transport rules" entry in [Messaging policy and compliance permissions](/en-us/exchange/messaging-policy-and-compliance-permissions-exchange-2013-help).
3. Run the **Get-OrganizationConfig** cmdlet.

    ```powershell
    Get-OrganizationConfig
    ```
4. Look for **FocusedInboxOn** to view its current setting:

    [![Screenshot of PowerShell output showing the FocusedInboxOn setting in Get-OrganizationConfig.](../../media/419d8caa-89b9-45c5-91d9-8c023297456e.png)](../../media/419d8caa-89b9-45c5-91d9-8c023297456e.png#lightbox)
5. Run the following cmdlet to turn off Focused Inbox.

    ```powershell
    Set-OrganizationConfig -FocusedInboxOn $false
    ```
6. Run the **Get-OrganizationConfig** cmdlet again and you see that FocusedInboxOn is set to $false, which means it's turned off.

### To turn on Focused Inbox

- In Step 5, run the following cmdlet to turn on Focused Inbox.

    ```powershell
    Set-OrganizationConfig -FocusedInboxOn $true
    ```

## What do users see after I turn on Focused Inbox?

Your users see the Focused view only after they close and restart Outlook. When they restart Outlook, they see a tip in the Outlook user interface that gives them the option to use the new Focused Inbox.

[![Screenshot of Focused Inbox in Outlook on the web when a user first sees the feature prompt.](../../media/f6ef79e7-0f4c-4a23-b6f0-7c15d927b5f0.png)](../../media/f6ef79e7-0f4c-4a23-b6f0-7c15d927b5f0.png#lightbox)

If you're switching from Clutter to Focused Inbox, users can decide to enable it ("Try it") or dismiss the feature. If the user has multiple supported clients, they can enable or disable Focused Inbox individually on each one. The tip looks like this:

[![Screenshot of the Focused Inbox rollout tip shown after Outlook is reopened for users.](../../media/c034f969-d650-4333-88f1-dd10ade0a94c.png)](../../media/c034f969-d650-4333-88f1-dd10ade0a94c.png#lightbox)

When a user decides to start using Focused Inbox, the feature automatically disables Clutter. The Clutter folder converts into a standard folder that the user can rename or delete.

## Turn Focused Inbox on or off for specific users

This example turns Focused Inbox **Off** for Tim Matthew in the Contoso organization. However, it doesn't block the availability of the feature to Tim. Tim can still re-enable Focused Inbox on each of his clients.

1. [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. You need to be assigned permissions before you can perform this procedure or procedures. To see what permissions you need, see the "Transport rules" entry in the Messaging policy and compliance permissions article.
3. Run the **Get-FocusedInbox** cmdlet, for example:

    ```powershell
    Get-FocusedInbox -Identity <tim@contoso.com>
    ```
4. Look for `FocusedInboxOn` to view its current setting:

    ![Screenshot of PowerShell output showing the FocusedInboxOn setting for the selected mailbox.](../../media/419d8caa-89b9-45c5-91d9-8c023297456e.png)
5. Run the following cmdlet to turn off Focused Inbox:

    ```powershell
    Set-FocusedInbox -Identity <tim@contoso.com> -FocusedInboxOn $false
    ```

    OR, run the following cmdlet to turn it on:

    ```powershell
    Set-FocusedInbox -Identity <tim@contoso.com> -FocusedInboxOn $true
    ```

## Use the UI to create a transport rule to direct email messages to the Focused view for all your users

1. Go to the [Exchange admin center](https://go.microsoft.com/fwlink/p/?linkid=2059104).
2. Navigate to **Mail flow** &gt; **Rules**. Select **Add a rule** and then select **Create a new rule...**.
3. After you finish creating the new rule, select **Save** to start the rule.

## Use PowerShell to create a transport rule that directs email messages to the Focused view for all your users

1. [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. You need to be assigned permissions before you can perform this procedure or procedures. To see what permissions you need, see the "Transport rules" entry in [Messaging policy and compliance permissions](/en-us/exchange/messaging-policy-and-compliance-permissions-exchange-2013-help).
3. Run the following command to deliver all messages from "Payroll Department," for example, to the Focused Inbox.

    ```powershell
    New-TransportRule -Name <name_of_the_rule> -From "Payroll Department" -SetHeaderName "X-MS-Exchange-Organization-BypassFocusedInbox" -SetHeaderValue "true"
    ```

Important

In this example, both "X-MS-Exchange-Organization-BypassFocusedInbox" and "true" are case sensitive. Also, Focused Inbox honors the X-header that bypasses Clutter. So if you use this setting in Clutter, it's used in the Focused Inbox. For detailed syntax and parameter information, see [New-TransportRule](/en-us/powershell/module/exchangepowershell/new-transportrule).

### How do you know if this rule worked?

You can check email message headers to see if the email messages are landing in the Inbox due to the Focused Inbox transport rule bypass. Pick an email message from a mailbox in your organization that has the Focused Inbox transport rule applied. Look at the headers stamped on the message, and you should see the **X-MS-Exchange-Organization-BypassFocusedInbox: true** header. This header means the bypass is working. For info on how to find the header information, see [View the Internet header information for an email message](https://go.microsoft.com/fwlink/p/?LinkId=822530).

### What does the user see?

If a transport rule is in place, a notification shows for the override. Outlook on the web disables the **Always move to Other** option and shows a tooltip. Outlook clients on desktop allow you to select **Always move to Other** from a pop-up dialog.

## Turn on or off Clutter

Microsoft received reports that Clutter suddenly stopped working for some users. If Clutter stops working, you can enable it again for specific users. See [Configure Clutter for your organization](../email/configure-clutter).

## FAQ for Focused Inbox

Here are answers to frequently asked questions about Focused Inbox.

#### Can I control how I roll out Focused Inbox in my organization?

Yes. You can turn Focused Inbox on or off for your entire organization, or you can turn it on or off for specified users.

#### Is the Focused Inbox feature only available for Office 2016 clients?

Yes, only users with Office 2016 are affected. The feature isn't going to be backported to Outlook 2013 or earlier.

#### How long does it take for Focused Inbox changes to take place in Outlook?

Once you turn on or turn off Focused Inbox, the settings take effect when your users close and restart Outlook.

#### What happens to Clutter once I turn on Focused Inbox?

After switching, you no longer receive less actionable email in the Clutter folder. Instead, email is split between the Focused and Other tabs in your inbox. The same algorithm that moved items to the Clutter folder now powers Focused Inbox, meaning that any emails that were set to move to Clutter are now moved to Other. Any messages already in your Clutter folder remain there until you decide to delete or move them.

Check out this post by [Tony Redmond](https://www.petri.com/author/tony-redmond), Microsoft MVP: [How the Focused Inbox Replaces Clutter Inside Office 365](https://www.petri.com/focused-inbox-office-365).

#### Can I keep users on Clutter? What is Microsoft's recommendation when it comes to using Clutter vs Focused Inbox?

Yes, you can keep users on Clutter and disable Focused Inbox. However, eventually Clutter is fully replaced with Focused Inbox so Microsoft recommends moving to Focused Inbox now. To learn more about when you use Clutter with Exchange Online, see this blog post: [Update on Focused Inbox and our plans for Clutter](https://techcommunity.microsoft.com/t5/Outlook-Blog/Update-on-Focused-Inbox-and-our-plans-for-Clutter/ba-p/136448).

#### Should I disable Clutter for my end users if we're going to move everyone to Focused Inbox?

No. You can explicitly disable Clutter for a mailbox by running the Set-Clutter cmdlet. However, if you disable Clutter, the mailbox owner sees messages that were previously redirected to the Clutter folder remain in the Inbox. They have to process those messages until their client is upgraded to a version that supports the Focused Inbox. It's best not to disable Clutter until the upgraded clients are available.

#### Why are there two different cmdlets for managing Focused Inbox?

Focused Inbox has two associated states:

- **Organization Level**: Focused Inbox state, and an associated last update timestamp.
- **Mailbox Level**: Focused Inbox state, and an associated last update timestamp.

#### How does Outlook decide to show the Focused Inbox experience with these two states?

Outlook decides which experience to show by choosing the cmdlet with the latest timestamp. By default, both timestamps are null, and in this case, the feature is enabled.

#### Why does the Get-FocusedInbox cmdlet return "true" when I turn off Focused Inbox in my organization?

Two cmdlets control Focused Inbox. When you run `Get-FocusedInbox` for a mailbox, it returns the mailbox level state of the feature. Outlook chooses the experience based on which cmdlet state was last modified.

#### Can I run a script to see who turned on Focused Inbox?

No, and this limitation is by design. Focused Inbox enablement is a client-side setting, so the cmdlet can only tell you if the user's mailbox is eligible for the client experience. It's possible for the feature to be simultaneously enabled in some clients and disabled in others. For example, it can be enabled in Outlook app and Outlook Mobile but disabled in Outlook on the web.