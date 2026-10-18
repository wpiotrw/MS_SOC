---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Pin apps to your users app launcher - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/pin-apps-to-app-launcher?view=o365-worldwide
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
manager: dansimp
ms.date: 2026-04-30T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.collection:
- Tier3
- scotvorg
- Adm_O365
- M365-subscription-management
- Adm_TOC
- operations-pod
ms.service: microsoft-365-business
ms.custom:
- admindeeplinkMAC
- integrated-apps
ms.localizationpriority: medium
description: Lean how to pin up to three apps to your users app launcher.
locale: en-us
document_id: 8a45a41e-f5f7-7ff6-c200-c37bd792fb9d
document_version_independent_id: bd5f0764-2960-3da0-0ff4-696eac622902
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/pin-apps-to-app-launcher.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/pin-apps-to-app-launcher
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/pin-apps-to-app-launcher.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 5fd9dc1c-673a-0b69-6809-f8b1413c7fe1
---

# Pin apps to your users app launcher - Microsoft 365 admin | Microsoft Learn

Use the controls in the Microsoft Entra admin center to pin up to three apps to Microsoft365.com and the app launcher for all the users in your organization. You can also organize groups of applications. Any app you add can later be unpinned by the user at any time. To pin an app for your users, you must be a Cloud application administrator or Application administrator in Microsoft Entra ID. For more information about admin roles, see [Microsoft Entra built-in roles](/en-us/azure/active-directory/roles/permissions-reference) and [admin roles in Microsoft 365](../add-users/about-admin-roles).

For more information about the app launcher and Microsoft365.com, see [meet the app launcher](https://support.microsoft.com/office/79f12104-6fed-442f-96a0-eb089a3f476a) and [updates to office.com and the-Office 365 app launcher](https://techcommunity.microsoft.com/t5/office-365-blog/updates-to-office-com-and-the-office-365-app-launcher/ba-p/1150503) blog article.

## Use the Microsoft Entra admin center to pin apps

Note

Microsoft 365 productivity apps are excluded from this list since they're already displayed in the App launcher.

1. Go to the Microsoft 365 admin center at [https://admin.cloud.microsoft](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the left nav, choose **Show all**. Under **Admin centers**, choose **Identity**.
3. In Microsoft Entra admin center on the left nav, select **Enterprise Apps**.
4. Next, choose **App launchers**, and then choose **Settings**.
5. In the **Microsoft 365 settings** section, choose **Add application**.
6. Choose the applications you want to pin to the users' app launcher, and then choose **Add**.

### Pin a custom app

Note

The user interface indicates if you need to purchase more Microsoft Entra ID licenses to use this feature. For more information, see [Microsoft Entra pricing](https://azure.microsoft.com/pricing/details/active-directory/).

1. Go to the Microsoft 365 admin center at [https://admin.cloud.microsoft](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the left nav, choose **Show all**. Under **Admin centers**, choose **Identity**.
3. In Microsoft Entra admin center on the left nav, select **Enterprise apps**.
4. On **All applications**, select an existing application or choose **New application**.
5. If you choose an existing application, follow the steps to add users and groups, provision users, and secure access.
6. If you choose a new application, follow the steps to create the new application. Then, follow the steps to add users and groups, provision users, and secure access.

## Create application collections

You can also create application collections for the users in your organization. For instructions, see [Create collections on the My Apps portal](/en-us/azure/active-directory/manage-apps/access-panel-collections).