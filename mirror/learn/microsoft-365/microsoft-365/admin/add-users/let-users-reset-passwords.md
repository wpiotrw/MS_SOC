---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Let users reset their own passwords - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/let-users-reset-passwords?view=o365-worldwide
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
ms.date: 2026-01-05T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: m365-core
ms.subservice: identity
ms.localizationpriority: medium
ms.collection:
- Tier1
- scotvorg
- highpri
- M365-subscription-management
- Adm_O365
- Adm_TOC
ms.custom:
- VSBFY23
- MSStore_Link
- TRN_M365B
- OKR_SMB_Videos
- AdminSurgePortfolio
- okr_smb
- AdminTemplateSet
- adminvideo
- business_assist
- user-accounts
description: Learn how you can set a policy in the Microsoft 365 admin center to allow users to reset their own passwords using the self-service password reset tool.
locale: en-us
document_id: ad408574-36cc-9b96-f092-58a68708d3a0
document_version_independent_id: 97adbc3d-8f71-a6de-25c3-f9400125f885
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/add-users/let-users-reset-passwords.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/add-users/let-users-reset-passwords
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/add-users/let-users-reset-passwords.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 61eef887-7383-1677-70c6-b07a5fb75a4b
---

# Let users reset their own passwords - Microsoft 365 admin | Microsoft Learn

Check out all of our small business content on [Small business help & learning](https://go.microsoft.com/fwlink/?linkid=2224585).

Check out [Microsoft 365 small business video help](https://go.microsoft.com/fwlink/?linkid=2197659) on YouTube.

This article is for people who set password expiration policy for a business, school, or nonprofit. You can let people use the [self-service password reset tool](https://go.microsoft.com/fwlink/p/?LinkId=522677) so you don't have to reset passwords for them. Less work for you!

To complete these steps, you must be a [password administrator](about-admin-roles).

## Before you begin

- Self-service password reset is included with any Microsoft 365 business, education, or nonprofit paid plan. It doesn't work with Microsoft 365 trial.
- Self-service password reset uses Azure. There's no extra charge to turn on self-service password reset.
- If you're using Active Directory on premises, you can set up self-service password reset, but it requires a paid subscription to Microsoft Entra ID P1 or P2.

## Watch: Let users reset their own passwords

Check out this video and others on our [YouTube channel](https://go.microsoft.com/fwlink/?linkid=2198214).

## Steps: Let people reset their own passwords

1. In the [Microsoft 365 admin center](https://admin.cloud.microsoft/), in the left navigation pane, select **Settings** &gt; **Org settings**, and then select the **Security & privacy** tab. (Or, use this link to open that tab: [Security & privacy](https://go.microsoft.com/fwlink/p/?linkid=2072756)).
2. Select **Self-service password reset**, and then select **Go to the Azure portal to turn on self-service password reset**.

    [![Screenshot showing self-service password reset flyout.](../../media/let-users-reset-passwords/self-service-password-reset.png)](../../media/let-users-reset-passwords/self-service-password-reset.png#lightbox)

    This option takes you to the Password reset page in the Microsoft Entra admin center.
3. On the **Password reset | Properties** page, select an option, such as **All** or **Selected**.

    [![Screenshot showing password reset properties options.](../../media/let-users-reset-passwords/password-reset-properties.png)](../../media/let-users-reset-passwords/password-reset-properties.png#lightbox)

    If you choose **Selected**, specify groups to enable self-service password reset.
4. Select **Save**.
5. To specify authentication methods for users, see [Manage authentication methods for Microsoft Entra ID](/en-us/entra/identity/authentication/concept-authentication-methods-manage).