---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Change your email address to use your custom domain - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/email/change-email-address?view=o365-worldwide
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
ms.date: 2025-04-23T00:00:00.0000000Z
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
- Adm_O365_Setup
- operations-pod
ms.custom:
- MSStore_Link
- AdminSurgePortfolio
- AdminTemplateSet
- adminvideo
- user-accounts
search.appverid:
- BCS160
- MET150
- MOE150
- BEA160
- GEA150
ms.assetid: f4d8cae9-6d06-4c4b-b4e5-6581fd05ea82
description: Change your email address to a friendly email address like tom@fourthcoffee.com by buying a domain name and adding it to Microsoft 365.
locale: en-us
document_id: d1394eba-4e78-2fd6-84f3-4ee64aedab51
document_version_independent_id: 0ba9ff8c-20a8-58a9-dce7-a3bb0627c134
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/email/change-email-address.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/email/change-email-address
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/email/change-email-address.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: db4d0fbf-683d-830d-b6ef-f0b61dd35b2c
---

# Change your email address to use your custom domain - Microsoft 365 admin | Microsoft Learn

Check out [Microsoft 365 small business help](https://go.microsoft.com/fwlink/?linkid=2197659) on YouTube.

**[Check the Domains FAQ](../setup/domains-faq)** if you don't find what you're looking for.

::: moniker range="o365-worldwide"

Your initial email address in Microsoft 365 includes .onmicrosoft.com, like tom@fourthcoffee.onmicrosoft.com. You can change it to a friendlier address like tom@fourthcoffee.com. You'll need your own domain name, like fourthcoffee.com first. If you already have one, great! If not, you can learn how to [buy one from a domain registrar](../get-help-with-domains/buy-a-domain-name).

::: moniker-end

::: moniker range="o365-21vianet"

Your initial email address in Microsoft 365 operated by 21Vianet includes partner.onmschina.cn, like tom@fourthcoffee.partner.onmschina.cn. You can change it to a friendlier address like tom@fourthcoffee.cn. You'll need your own domain name, like fourthcoffee.cn first. If you already have one, great! If not, you can learn how to [buy one from a domain registrar](../get-help-with-domains/buy-a-domain-name).

::: moniker-end

When you change your domain's email to come to Microsoft 365, by updating your domain's MX record during setup, ALL email sent to that domain will start coming to Microsoft 365. Make sure you've added users and created mailboxes in Microsoft 365 for everyone who has email on your domain BEFORE you change the MX record. Don't want to move email for everyone on your domain to Microsoft 365? You can take steps to [pilot Microsoft 365 with just a few email addresses instead](../misc/pilot-microsoft-365-from-my-custom-domain).

## Set up business email with a new domain

Check out this video and others on our [YouTube channel](https://go.microsoft.com/fwlink/p/?linkid=2198215).

Buy a new domain name for your email address and set up the email addresses with Microsoft 365.

1. Buy a new domain name for your email address by providing your contact information for the new domain name, choosing your payment method, and then placing your order.
2. Change the first part of the address (before the @ sign) or leave it as is.
3. Sign out of Microsoft 365, and then sign back in with your new email address. Your employee email addresses are updated with the new domain.

## Set up business email with an existing domain

Use a domain name you already own whether you're using it for a website address or an email address at another provider.

1. Sign into the website that hosts your domain. Click a button to verify automatically or update the domain manually.
2. Customize the email address or leave it as is.
3. Sign out of Microsoft 365, and then sign back in with your new email address. Your employee email addresses are updated with the new domain.

## Change your email address to use your custom domain using the Microsoft 365 admin center

You must be a global admin to perform these steps.

Important

Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

::: moniker range="o365-worldwide"

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).

::: moniker-end

::: moniker range="o365-21vianet"

1. Go to the admin center at [https://portal.partner.microsoftonline.cn](https://go.microsoft.com/fwlink/p/?linkid=850627).

::: moniker-end

1. Go to the **Settings** &gt; **Domains** page.
2. On the **Domains** page, select **Add domain**.
3. Follow the steps to confirm that you own your domain. You'll be guided to get everything set up correctly with your domain in Microsoft 365.
4. Go to **Users** &gt; **Active users**.
5. Select a user to edit their username and change it to the domain you just added.

Note

If you are not using an Exchange license, you cannot use the domain to send or receive emails from the Microsoft 365 tenant.