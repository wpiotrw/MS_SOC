---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Add custom tiles to the app launcher - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/customize-the-app-launcher?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- CSH
ms.author: twerner
author: twernermsft
manager: scotv
ms.date: 2026-04-30T00:00:00.0000000Z
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
- must-keep
- operations-pod
ms.custom:
- AdminSurgePortfolio
- okr_smb
- AdminTemplateSet
- integrated-apps
search.appverid:
- BCS160
- MET150
- MOE150
- GEA150
ms.assetid: 1136115a-75af-4497-b693-640c4ce70bc6
description: Create quick links to your email, documents, apps, SharePoint sites, external sites, and other resources by adding custom tiles to the app launcher.
locale: en-us
document_id: 9488caf7-b791-3002-8749-7fdc4b2ec8b3
document_version_independent_id: 08e61eb0-7bcd-f449-46ef-17e209138a8e
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/customize-the-app-launcher.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/customize-the-app-launcher
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/customize-the-app-launcher.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: de464245-af95-6a68-7c1e-f3115a2864fa
---

# Add custom tiles to the app launcher - Microsoft 365 admin | Microsoft Learn

You can add your own custom tiles to Apps that point to SharePoint sites, external sites, legacy apps, and more. The custom tile appears under the Apps section in Microsoft 365. Once your users launch the app, the app is added automatically to the list of app launcher apps for access. Adding apps to the app launcher makes it easy to find the relevant sites, apps, and resources to do your job.

Note

Adding apps to the app launcher capability is currently unavailable in the Microsoft Copilot App.

## Add a custom tile for Apps

1. Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
2. From the left navigation bar, select **... Show all**, and then select **Settings** to expand it.
3. Under **Settings**, select [**Org Settings**](https://admin.cloud.microsoft/?#/Settings/SecurityPrivacy).
4. In the **Org Settings** page, select the **Organization profile** tab, and then select **Custom tiles for Apps**.
5. In the **Custom tiles for Apps** pane, select **+ Add a custom tile**.
6. In the **Add a custom tile** pane:

    1. Enter a name for the new tile in the **Tile name** field. This name is the name that appears on the My apps page and app launcher.
    2. Enter a URL of the website for the new tile in the **URL of website** field. This URL is the location where you want your users to go when they select the tile on the app launcher. Use HTTPS in the URL.

        Tip

        If you're creating a tile for a SharePoint site, navigate to that site, copy the URL, and paste it here. The URL of your default team site looks like `https://<company_name>.sharepoint.com`.
    3. Enter a URL of the image for the new tile in the **Image URL** field. This image appears on the My apps page and app launcher.

        Tip

        The image should be 60x60 pixels and be available to everyone in your organization without requiring authentication.
    4. Enter a description for the new tile in the **Description** field. The description is displayed when you select the tile on the My apps page and select **App details**.
    5. Select **Save** to finish creating the custom tile.

Your custom tile appears for your users within 24 hours in the app launcher on the **All** tab and in Microsoft 365 Apps.

Note

If you don't see the custom tile created in the previous steps, make sure you have an Exchange Online mailbox assigned to you and that your mailbox has been signed into at least once. These steps are required for custom tiles in Microsoft 365.

## Edit or delete a custom tile

To edit an existing custom tile, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
2. From the left navigation bar, select **... Show all**, and then select **Settings** to expand it.
3. Under **Settings**, select [**Org Settings**](https://admin.cloud.microsoft/?#/Settings/SecurityPrivacy).
4. In the **Org Settings** page, select the **Organization profile** tab, and then select **Custom tiles for Apps**.
5. In the **Custom tiles for Apps** pane, find the custom tile you want to edit or delete, select the horizontal ellipsis (**...**) next to the custom tile, and then select **Edit custom tile**.
6. In the **Edit custom tile** pane, update the **Tile name**, **URL of website**, **URL of tile image**, or **Description** for the custom tile as needed.
7. Select **Save**.

To delete an existing custom tile, follow these steps:

1. Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
2. From the left navigation bar, select **... Show all**, and then select **Settings** to expand it.
3. Under **Settings**, select [**Org Settings**](https://admin.cloud.microsoft/?#/Settings/SecurityPrivacy).
4. In the **Org Settings** page, select the **Organization profile** tab, and then select **Custom tiles for Apps**.
5. In the **Custom tiles for Apps** pane, find the custom tile you want to edit or delete, select the horizontal ellipsis (**...**) next to the custom tile, and then select **Delete custom tile**.
6. In the **Delete custom tile?** window, select **Delete**.