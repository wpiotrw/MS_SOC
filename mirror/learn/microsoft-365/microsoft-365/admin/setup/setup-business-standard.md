---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Set up Microsoft 365 Business Standard with your domain - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/setup/setup-business-standard?view=o365-worldwide
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
ms.date: 2026-03-27T00:00:00.0000000Z
audience: Admin
ms.topic: install-set-up-deploy
ms.service: microsoft-365-business
ms.localizationpriority: high
ms.collection:
- Tier1
- scotvorg
- highpri
- M365-subscription-management
- Adm_O365
- Adm_TOC
- Adm_O365_Setup
- TRN_SMB
- operations-pod
ms.custom:
- VSBFY23
- TRN_M365B
- OKR_SMB_Videos
- AdminSurgePortfolio
- AdminTemplateSet
- admindeeplinkMAC
- admindeeplinkEXCHANGE
description: Set up Microsoft 365 Business Standard with a domain you own or buy a new one during sign-up. Follow these steps to get business email running quickly.
locale: en-us
document_id: fc903dd4-94b0-1461-d9a4-5b457d5ac3b6
document_version_independent_id: 7a8eff98-2ba7-81f7-2a3d-71bdd7e1994a
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/setup/setup-business-standard.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/setup/setup-business-standard
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/setup/setup-business-standard.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/82f69bd7-5cb0-4163-9fd6-9103bb1a8352
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f003597a-dab2-429a-8639-1d2acd9c0371
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: c101e071-c121-14e7-96ef-c49780cad1dd
---

# Set up Microsoft 365 Business Standard with your domain - Microsoft 365 admin | Microsoft Learn

When you purchase Microsoft 365 Business Standard, you can add a domain. The domain can be one you already own or a new one that you purchase. For more information about signing up for Microsoft 365 Business Standard, see [Sign up for Microsoft 365 Business Standard](../simplified-signup/signup-business-standard). This article explains how to set up your Microsoft 365 Business Standard subscription with a domain. By the end of this article, your domain will be connected and users can send and receive business email.

Tip

If you have a Microsoft 365 Business Premium subscription, see [Set up Microsoft 365 Business Premium](../../business-premium/m365-business-premium-setup).

## Set up Microsoft 365 for business

## Before you begin

To add, modify, or remove domains, you must be a [Domain Name Administrator](/en-us/entra/identity/role-based-access-control/permissions-reference#domain-name-administrator).

Important

The person who signs up for Microsoft 365 for business automatically becomes the technical administrator of the organization. You can add other administrators later to help manage your Microsoft 365 services. For more information, see [Assign admin roles](../add-users/assign-admin-roles).

## Watch: Add an existing domain to your Microsoft 365 Business Standard subscription

## Watch: Set up business email with a new domain

## Add an existing domain to your Microsoft 365 Business Standard subscription

1. If you don't have a Microsoft 365 Business Standard subscription yet, sign up for one by following the steps in [Sign up for Microsoft 365 Business Standard](../simplified-signup/signup-business-standard).
2. Once you're signed up for Microsoft 365 Business Standard, follow the steps in the article [Add a custom domain to Microsoft 365](add-domain) to add a domain to your account. These steps also guide you through the process of connecting your domain to Microsoft 365 by adding the necessary DNS records.

## Add users and assign licenses

Assigning licenses to your users gives them access to the services included in your subscription. After you add your domain, you can add users and assign licenses to them through the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339). To add users and assign licenses, follow the steps in [Add users and assign licenses](../add-users/add-users).

If your subscription already has existing users, make sure that licenses are also assigned to them.

## Set up users with Microsoft 365 services

For steps on setting up your users on Microsoft 365 services such as Outlook, Microsoft Teams, and OneDrive, see [User quick setup in Microsoft 365 for business](https://support.microsoft.com/office/7f34c318-e772-46a5-8c0a-ab86661542d1).

For more information, see the following articles:

- [Set up Outlook for Microsoft 365 for business email](setup-outlook).
- [Set up OneDrive included with Microsoft 365](https://support.microsoft.com/office/937e3ac8-b396-4a70-a561-6eaa479a4720).

## Watch: Set up Outlook for email

The following video shows how to set up Outlook for email with your Microsoft 365 Business Standard subscription:

## Watch: Import and redirect email

The following video shows how to import your previous email, calendar, and contacts from previous email accounts into your new Microsoft 365 account:

## Import email

In Outlook, you can import your previous email, calendar, and contacts from previous email accounts into your new Microsoft 365 account.

1. Export your old email account to create a backup file:

    1. In Outlook, select **File** &gt; **Open & Export** &gt; **Import/Export**.
    2. Select **Export to a File** and then follow the steps to export your Outlook data. The exported data is saved as a **.pst** file.
2. After exporting your old email account, import the data into your new Microsoft 365 account:

    1. In Outlook, select **File** &gt; **Open & Export** &gt; **Import/Export**.
    2. Select **Import from another program or file**. Follow the steps to import the backup **.pst** file you created when you exported your old email.

For more information, see [Move your old email, calendars, and contacts to Microsoft 365](https://support.microsoft.com/office/365-2c37f0b7-2915-423c-b35e-9e03267f23dc).

You can also use the [Exchange admin center](https://go.microsoft.com/fwlink/p/?linkid=2059104) to import users' email. For more information, see [Ways to migrate multiple email accounts to Microsoft 365 or Office 365](/en-us/Exchange/mailbox-migration/mailbox-migration).

## Invite users to join your subscription and organization

After you set up your organization on Microsoft 365, invite other users to join your Microsoft 365 business subscription so they can access all the features of the subscription. For more information, see [Invite users to my subscription](../simplified-signup/admin-invite-business-standard).

To join your organization and subscription, users can follow the steps in the following articles:

- [Accept an email invitation](../simplified-signup/user-invite-business-standard).
- [Accept an email invitation using an Outlook, Yahoo, Gmail, or other account (User)](../simplified-signup/user-invite-msa-nodomain-join).