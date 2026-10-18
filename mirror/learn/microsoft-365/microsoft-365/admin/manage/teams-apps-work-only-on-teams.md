---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Teams apps that only work on Teams - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/teams-apps-work-only-on-teams?view=o365-worldwide
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
ms.date: 2025-08-26T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- Adm_TOC
- operations-pod
ms.custom:
- AdminSurgePortfolio
- integrated-apps
search.appverid: MET150
ROBOTS: NOINDEX, NOFOLLOW
description: How to block and unblock apps Teams apps that only work on Teams through controls in the integrated apps portal.
locale: en-us
document_id: 2371eb0d-35d8-941e-04d0-5a4656a444f1
document_version_independent_id: 2371eb0d-35d8-941e-04d0-5a4656a444f1
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/teams-apps-work-only-on-teams.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/teams-apps-work-only-on-teams
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/teams-apps-work-only-on-teams.md
platformId: d8d5ee34-4bd6-6239-0816-10df9b099d26
---

# Teams apps that only work on Teams - Microsoft 365 admin | Microsoft Learn

Some Teams apps cannot be surfaced in Outlook or the Microsoft Copilot application, either because the app wouldn't make sense in those hosts or because they use a manifest version less than 1.13. These apps, which are sometimes called "pure Teams apps" or "Teams only apps" to distinguish them from [cross application apps](teams-apps-work-on-outlook-and-m365), can be identified in the integrated apps portal by the availability status **Some or all users in the organization can install** in the **Available Apps** list. Admins cannot preinstall or remove these apps, but they can block or unblock them.

## Before you begin

- These apps only show up on the Available Apps list based on your settings in Teams admin center. Verify if your settings in the Teams admin center are for non-Microsoft apps.
    - If access to non-Microsoft apps on Teams admin center is turned on, admins can start seeing these apps on the integrated apps portal in the **Available apps** and **Blocked apps** lists based on their setting in Teams admin center.
    - If access to non-Microsoft apps on Teams admin center is turned off, no such apps are visible on the integrated apps portal.
- These apps always have the availability status of **Some or all users in the organization can install**. These apps always have only Teams as the host product. To know more about which users can access this app on Teams, visit the Teams admin center.

Important

Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

## How to block a Teams app on Teams

1. Sign into Microsoft 365 admin center as a global administrator.
2. Select **Settings**, and then select **Integrated Apps**.
3. Select the **Available Apps** list.
4. Select an app with the status **Some or all users in the organization can install** from the **Available Apps** list to open the overview pane. These apps will always have only Teams listed as host product.
5. Select **Block app**.
6. Consent to blocking the app by selecting **Yes, I'm sure I want to block this app**.
7. Select **Block**. You can now see this app in the **Blocked Apps** list. When the admin blocks such an app, it's blocked for all users in the organization on the Teams client.

## How to unblock a Teams app on Teams?

1. Sign into Microsoft 365 admin center as a global administrator.
2. Select **Settings**, and then select **Integrated Apps**.
3. Select the **Blocked Apps** list.
4. Select an app from the **Blocked Apps** list to open the overview pane.
5. Select **Unblock app**.
6. Read the availability and deployment status that the app will revert to after unblocking. These statutes are the last saved ones of the app before it was blocked.
7. Select **Unblock**. You can now see this app in the **Available Apps** list and/or the **Deployed Apps** list based on the last saved setting.

When the admin unblocks such an app, it's reverted to the last saved setting as set by the admin in Teams admin center. Visit Teams admin center to know the latest status of the app on Teams.

Note

Teams apps with availability status as **Some or all users in the organization can install** can only be blocked on unblocked on the integrated apps portal for the Teams client. For any other management actions on these apps or to view how these apps show up on Teams to users in your organization, please visit the Teams admin center.