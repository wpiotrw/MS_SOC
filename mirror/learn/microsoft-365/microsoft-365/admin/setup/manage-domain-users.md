---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Synchronize domain users to Microsoft 365 - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/setup/manage-domain-users?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: frankroj
author: frankroj
manager: dansimp
ms.date: 2026-04-23T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: microsoft-365-business
ms.subservice: m365-domains
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_TOC
- must-keep
- operations-pod
ms.custom:
- Adm_O365
- Core_O365Admin_Migration
- MiniMaven
- MSB365
- OKR_SMB_M365
- seo-marvel-mar
- AdminSurgePortfolio
- identity-models
search.appverid:
- BCS160
- MET150
- MOE150
description: Synchronize domain-controlled users with Microsoft 365 for business.
locale: en-us
document_id: 3fec6b1a-892f-4717-02d4-6ceaaabf6222
document_version_independent_id: f1c8418b-8b18-5db9-3376-7f1d65633dfe
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/setup/manage-domain-users.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/setup/manage-domain-users
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/setup/manage-domain-users.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/37da4cc9-0cfc-42a9-ba5e-805706b01ef8
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1cfdec6-b0c3-4209-818c-736879856e0e
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3661fb96-d414-4a4e-b7ad-9370637790dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d0723c1-cf38-4c30-ab3d-5df787b33270
platformId: 67924be8-8e91-9bad-db0b-eac79c709247
---

# Synchronize domain users to Microsoft 365 - Microsoft 365 admin | Microsoft Learn

## 1. Prepare for Directory Synchronization

Before you synchronize your users and computers from the local Active Directory Domain, review [Prepare for directory synchronization to Microsoft 365](../../enterprise/prepare-for-directory-synchronization). In particular:

- Make sure that no duplicates exist in your directory for the following attributes: **mail**, **proxyAddresses**, and **userPrincipalName**. These values must be unique and any duplicates must be removed.
- We recommend that you configure the **userPrincipalName** (UPN) attribute for each local user account to match the primary email address that corresponds to the licensed Microsoft 365 user. For example: *mary.shelley@contoso.com* rather than *mary@contoso.local*.
- If the Active Directory domain ends in a non-routable suffix like *.local* or *.lan*, instead of an internet routable suffix such as *.com* or *.org*, adjust the UPN suffix of the local user accounts first as described in [Prepare a non-routable domain for directory synchronization](../../enterprise/prepare-a-non-routable-domain-for-directory-synchronization).

The **Run IdFix** in the following steps makes sure that your on-premises Active Directory is ready for directory synchronization.

## 2. Install and configure Microsoft Entra Connect

To synchronize your users, groups, and contacts from the local Active Directory into Microsoft Entra ID, install Microsoft Entra Connect and set up directory synchronization.

1. In the [admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339), select **Setup** in the left nav.
2. Under **Sign-in and security**, select **Add or sync users to Microsoft Entra ID**.
3. On the **Add or sync users to your Microsoft account** page, choose **Get started**.
4. In the first step run IdFix tool to prepare for Directory sync.
5. Follow the wizard steps to download Microsoft Entra Connect and use it to synchronize your domain-controlled users to Microsoft 365.

See [Set up directory synchronization for Microsoft 365](../../enterprise/set-up-directory-synchronization) to learn more.

As you configure your options for Microsoft Entra Connect, we recommend that you enable **Password Synchronization**, **Seamless Single Sign-On**, and the **password writeback** feature, which is also supported in Microsoft 365 for business.

Note

There are some additional steps for password writeback beyond the check box in Microsoft Entra Connect. For more information, see [How-to: configure password writeback](/en-us/azure/active-directory/authentication/howto-sspr-writeback).

If you also want to manage domain-joined Windows 10 devices, see [Enable domain-joined Windows 10 devices to be managed by Microsoft 365 Business Premium](../../business-premium/m365bp-manage-windows-devices) to set up a Microsoft Entra hybrid join.