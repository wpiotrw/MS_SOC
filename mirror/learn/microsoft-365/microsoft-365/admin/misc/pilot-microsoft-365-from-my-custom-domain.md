---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Pilot Microsoft 365 from my custom domain - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/misc/pilot-microsoft-365-from-my-custom-domain?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- CSH
ms.author: frankroj
author: frankroj
manager: dansimp
ms.date: 2026-04-23T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: microsoft-365-business
ms.subservice: m365-domains
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- Adm_O365
- Adm_TOC
- operations-pod
ms.custom:
- admindeeplinkMAC
- admindeeplinkEXCHANGE
search.appverid:
- BCS160
- MET150
- MOE150
description: Learn how to pilot email functionality from my custom domain to a Microsoft 365 mailbox by using only two test accounts.
locale: en-us
document_id: 738692b6-47ec-2a49-e576-bb6ff0cd3471
document_version_independent_id: c9d7a0ad-2db4-dda1-6021-831e5bb38098
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/misc/pilot-microsoft-365-from-my-custom-domain.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/misc/pilot-microsoft-365-from-my-custom-domain
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/misc/pilot-microsoft-365-from-my-custom-domain.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 5310e671-6439-8609-8192-65519bd409da
---

# Pilot Microsoft 365 from my custom domain - Microsoft 365 admin | Microsoft Learn

You can pilot Microsoft 365 with these requirements and limitations:

- Your current email provider must provide email forwarding.
- You must manage your Microsoft 365 DNS records at your DNS hosting provider, rather than have Microsoft 365 manage these records for you.

    To learn more, see [Add DNS records to connect your domain](../get-help-with-domains/create-dns-records-at-any-dns-hosting-provider).
- Free/busy information for users on the other email server is not available.
- Admins can't administer all user accounts from a single location.
- Users might not be able to use Microsoft 365 spam filtering.
- This is recommended for a very small number of users and only applies to the use of email for a pilot.

## Set up a Microsoft 365 pilot

Follow these steps to set up a Microsoft 365 pilot:

### Step 1: Sign in to the Microsoft 365 admin center

1. Sign in to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339) with your work or school account.
2. Select **Settings** &gt; **Domains** in the left navigation pane.

### Step 2: Verify that you own the domain you want to use

1. On the **Domains** page, select **Add domain**.
2. Type the domain name in the box, select **Use this domain**, and then select **Continue**.
3. Select the services you want to test with your domain, like email and instant messaging.
4. On the **Verify** domain page, follow the step-by-step instructions, and then select **Verify**.

    It takes between a few minutes and 72 hours for DNS changes to take effect.

    When verification is successful, you are asked to modify your DNS records.

### Step 3: Mark the domain as shared in Exchange Online

1. In the Exchange admin center, in the **Mail flow** section, select **Accepted domains**, and then select the domain you want to modify.
2. Double-click to open the window, and then select **Internal Relay**.
3. Select **Save**.

    This setting might require a few minutes to take effect.

### Step 4: Unblock the existing email server (optional)

All organizations with cloud mailboxes have default email protection for spam. Anti-spam protection might block your existing mail server if it detects a high volume of spam being forwarded by your current mail server. If you trust the spam protection for your other email provider, you can unblock the server in Microsoft 365.

Note

Unblocking your existing email server allows any spam that arrives through your original server to come to the Microsoft 365 mailboxes, and you can't evaluate how well Microsoft 365 prevents spam.

1. Sign in to Microsoft Defender XDR https://security.microsoft.com/antispam, select **Policies & rules**, Click on **Threat policies** and then select **Anti-spam policies**.
2. Select **Connection filter policy (Default)**, and click on Edit **Edit connection filter policy** and add the mail server IP address for your current email provider in the **Always allow messages from the following IP addresses or address range** Section.

### Step 5: Create user accounts and set the primary reply-to address

1. In the Microsoft 365 admin center left navigation, select **Users** &gt; [**Active users**](https://go.microsoft.com/fwlink/p/?linkid=834822).
2. Create two test accounts by adding two existing users.

    For each account, select **+ Add a user**, and fill out the required information, including the password method you want to test.

    To ensure a user's email stays the same, the **User name** field must match the user's current email address.
3. Choose the appropriate license, click **Next**, and then click **Finish adding**.
4. Next to **User name**, select your custom domain name from the drop-down list.
5. Select **Create** &gt; **Close**.

### Step 6: Configure mail to flow from Microsoft 365 or Office 365 to Email server

There are two steps for this:

1. Configure your Microsoft 365 or Office 365 environment.
2. Set up a connector from Microsoft 365 or Office 365 to your email server.

### 1. Configure your Microsoft 365 or Office 365 environment

Make sure you have completed the following in Microsoft 365 or Office 365:

1. To set up connectors, you need permissions assigned before you can begin. To check what permissions you need, see the Microsoft 365 and Office 365 connectors entry in the [Feature permissions in Exchange Online](/en-us/exchange/permissions-exo/feature-permissions) topic.
2. If you want Microsoft 365 to relay email from your email servers to the Internet, either:

    - Use a certificate configured with a subject name that matches an accepted domain in Microsoft 365 or Office 365. We recommend that your certificate's common name or subject alternative name matches the primary SMTP domain for your organization. For details, see [Prerequisites for your on-premises email environment](/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/set-up-connectors-to-route-mail#prerequisites-for-your-on-premises-email-environment).

    -OR-

    - Make sure that all your organization sender domains and subdomains are configured as accepted domains in Microsoft 365 or Office 365.

    For more information about defining accepted domains, see [Manage accepted domains in Exchange Online](/en-us/exchange/mail-flow-best-practices/manage-accepted-domains/manage-accepted-domains) and [Enable mail flow for subdomains in Exchange Online](/en-us/exchange/mail-flow-best-practices/manage-accepted-domains/enable-mail-flow-for-subdomains).
3. Decide whether you want to use mail flow rules (also known as transport rules) or domain names to deliver mail from Microsoft 365 or Office 365 to your email servers. Most businesses choose to deliver mail for all accepted domains. For more information, see [Scenario: Conditional mail routing in Exchange Online](/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/conditional-mail-routing).

Note

You can set up mail flow rules as described in [Mail flow rule actions in Exchange Online](/en-us/exchange/security-and-compliance/mail-flow-rules/mail-flow-rule-actions). For example, you might want to use mail flow rules with connectors if your mail is currently directed via distribution lists to multiple sites.

### 2. Set up a connector from Microsoft 365 or Office 365 to your email server

To create a connector in Microsoft 365 or Office 365, select **Admin** &gt; **Exchange** to go to the Exchange admin center. Next, select **mail flow** &gt; [**Connectors**](https://go.microsoft.com/fwlink/?linkid=2183136).

Set up connectors using the wizard.

To start the wizard, click the plus symbol **+**. On the first screen, choose **From** Office 365 and **To** Your Organization Mail server.

Click **Next**, and follow the instructions in the wizard. Click the **Help** or **Learn More** links if you need more information. The wizard will guide you through setup. At the end, make sure your connector validates. If the connector does not validate, double-click the message displayed to get more information, and see [Validate connectors](/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/validate-connectors) for help resolving issues.

### Step 7: Update DNS records at your DNS hosting provider

Sign in to your DNS hosting provider's website, and follow the instructions at [Add DNS records to connect your domain](../get-help-with-domains/create-dns-records-at-any-dns-hosting-provider).

**Make the following two exceptions:**

- Do not create a new MX record or change your existing MX record.
- If you already have a Sender Policy Framework (SPF) record for your previous email provider, instead of creating a new SPF (TXT) record for Exchange Online, add "include:spf.protection.outlook.com" to the current TXT record.

    For example, "v=spf1 mx include:adatum.com include:spf.protection.outlook.com ~all".

    If you don't have an SPF record, modify the one recommended by Microsoft 365 to include the domain for your current email provider, and add spf.protection.outlook.com. This authorizes outgoing messages from both email systems.

### Step 8: Set up email forwarding at your current provider

At your current email provider, set up forwarding for your users email accounts to your onmicrosoft.com domain:

- Forward User A mailbox to usera@yourcompany.onmicrosoft.com
- Forward User B mailbox to userb@yourcompany.onmicrosoft.com

When you complete this step, all email sent to usera@yourcompany.com and userb@yourcompany.com is available in Microsoft 365.

Note

Contact your current email provider for the exact steps to set up email forwarding. You don't need to keep a copy of messages at the current email provider. Most providers forward email by leaving the Reply-to address of the sender intact so that replies go to the original sender.

### Step 9: Test mail flow

1. Sign in to Outlook Web App using the credentials for User A.
2. Perform these tests:

    - Test local Microsoft email by sending an email, for example, to User B. The email is delivered immediately. In this scenario, the message is not routed to the mailbox for User B on your original server because the Microsoft 365 mailbox is local.
    - Test email to a user on the existing email system by sending an email, for example, to User C. The email is delivered to the mailbox for User C on your original mail server.
    - Verify that forwarding is set up properly from an outside account, or from an employee email account on the existing email system. For example, from the original server account for User C or a Hotmail account, send User A an email and verify that it arrives in the Microsoft 365 mailbox for User A.

### Step 10: Move mailbox contents

Because you are moving only two test users, and User A and User B are both using Outlook, you can move the email by opening the old .PST file in the new Outlook profile and copying the messages, calendar items, contacts, and so on. For more information, see [Import email, contacts, and calendar from an Outlook .pst file](https://support.microsoft.com/office/import-email-contacts-and-calendar-from-an-outlook-pst-file-431a8e9a-f99f-4d5f-ae48-ded54b3440ac).

After they're imported to the appropriate locations in the Microsoft 365 mailbox, the items can be accessed from any device, anywhere.