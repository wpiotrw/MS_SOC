---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Manage user email settings in Microsoft 365 - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/email/office-365-user-email-settings?view=o365-worldwide
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
ms.topic: overview
ms.service: microsoft-365-business
ms.collection:
- Tier1
- scotvorg
- Adm_O365
- Adm_TOC
- operations-pod
ms.custom:
- AdminSurgePortfolio
- user-accounts
ms.localizationpriority: medium
search.appverid:
- MET150
ms.assetid: 03083fdf-bc52-409a-b2ac-2a5f5c308fa0
description: Learn how to manage email settings for your users in Microsoft 365, including mailbox permissions, email forwarding, automatic replies, and more.
locale: en-us
document_id: a1a56d4e-5b63-a2b8-5225-abf9d91aaf90
document_version_independent_id: 467e8269-ef0c-ee69-0c3b-74221ab06e39
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/email/office-365-user-email-settings.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/email/office-365-user-email-settings
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/email/office-365-user-email-settings.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 8c2fff0f-5a29-f901-95af-6d88850dd47a
---

# Manage user email settings in Microsoft 365 - Microsoft 365 admin | Microsoft Learn

As the admin of an organization, you can manage user email settings in Microsoft 365 to control mailbox permissions, email forwarding, automatic replies, and more. This article explains how to configure these settings for your users.

## Activate an existing business email address

If you already registered a business email domain and need to activate email in Microsoft 365, use the setup flow first. After setup is complete, return to this article to manage mailbox settings.

1. Add and verify your domain by following [Add a custom domain to Microsoft 365](../setup/add-domain).
2. Add users and assign licenses by following [Add users and assign licenses](../add-users/add-users).
3. Sign in to Outlook by following [Set up Outlook for Microsoft 365 for business email](../setup/setup-outlook).

## Manage email settings

1. Go to [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. Go to **Users** &gt; **Active users** and select the user for whom you want to manage email settings.
3. In the new pane, select **Mail** to manage email settings.

## Summary of email settings in Microsoft 365

This table explains the various email settings you can change for a user in Microsoft 365.

| Mail setting | Description |
| --- | --- |
| Mailbox permissions | **Read and manage permissions** - Set whether people can read and manage other people's mailboxes. You can also set **Send as permissions** and **Send on behalf of permissions** for a person. For more details, see [Give mailbox permissions to another user in Microsoft 365 - Admin Help](../add-users/give-mailbox-permissions-to-another-user). |
| Email apps | Choose the apps a user can use to access their Microsoft email. |
| Show in global address list | Enable or disable the visibility of the user's mailbox in the organization's address list. |
| Email forwarding | Add a forwarding email address to a user. Use this feature if the person has multiple email addresses and they want to receive emails at all their email addresses. For more details, see [Configure email forwarding in Microsoft 365](configure-email-forwarding). |
| Automatic replies | Set an automatic reply when someone sends an email to the person's email address. Use this feature if an employee leaves your company and you want to let the email sender know. |
| More actions | **Convert to shared mailbox** - Convert the user's mailbox to a shared mailbox. Use this feature if the person leaves your organization and you want to keep their mailbox data around for a while. For more information, see [Convert a user mailbox to a shared mailbox](convert-user-mailbox-to-shared-mailbox) and [Open and use a shared mailbox](https://support.microsoft.com/office/d94a8e9e-21f1-4240-808b-de9c9c088afd).**Edit Exchange properties** - Manage other Exchange Online tasks by using the Exchange admin center. Read about [managing user mailboxes in Exchange Online](/en-us/exchange/recipients-in-exchange-online/manage-user-mailboxes/manage-user-mailboxes). You can turn on Manage litigation hold when you want to retain user mailbox data. Users can purge items from their mailbox, but Microsoft 365 still retains those items. |

Note

You can only manage email apps for mailboxes that are hosted fully in Microsoft 365. You can't use this feature to manage email apps for mailboxes that are hosted on-premises.