---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Step 3 - Wipe and block a former employee's mobile device - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/remove-former-employee-step-3?view=o365-worldwide
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
ms.date: 2025-10-28T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: m365-core
ms.subservice: identity
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
- user-accounts
description: Use the Exchange admin center to wipe and block a former employee's device so that all organization data is removed and it no longer connects to Microsoft 365.
locale: en-us
document_id: 9e2bdb60-b559-ddf3-0eec-be4943fc94fd
document_version_independent_id: 5b176c0f-6c35-a187-2ccb-53a23e154978
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/add-users/remove-former-employee-step-3.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/add-users/remove-former-employee-step-3
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/add-users/remove-former-employee-step-3.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 05237b04-dc9f-dba4-556d-5d03e2d8c4e4
---

# Step 3 - Wipe and block a former employee's mobile device - Microsoft 365 admin | Microsoft Learn

If an employee has left your organization and they had a business phone, you can use the [Exchange admin center](https://go.microsoft.com/fwlink/p/?linkid=2059104) to wipe and block that device. This action helps ensure that your business data is removed from the device and it can no longer connect to your organization's Microsoft 365 subscription.

If your organization uses Basic Mobility and Security to manage mobile devices, you can wipe and block those devices [using Basic Mobility and Security](/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-wipe-devices).

Note

You must have appropriate permissions through a an appropriate role, such as the [Directory Writers role](/en-us/entra/identity/role-based-access-control/permissions-reference#directory-writers) to perform the tasks in this article.

## Wipe mobile device using the Exchange admin center

1. In the [Exchange admin center](https://admin.exchange.microsoft.com/), go to &gt; **Recipients** &gt; **Mailboxes**. (Or, go directly to the [Mailboxes page](https://go.microsoft.com/fwlink/p/?linkid=2183135).)
2. Select the user, and under **Email apps & mobile devices**, select **Manage mobile devices**.
3. On the **Mobile Device Details** page, under **Mobile devices**, select a device. Then select an option, such as **Account Only Remote Wipe Device**, and then select **Block access**. See [Perform a remote wipe on a mobile phone in Exchange Online](/en-us/exchange/clients-and-mobile-in-exchange-online/exchange-activesync/remote-wipe-on-mobile-phone).
4. Save your changes.