---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Deploy Office Add-ins in Government Community Cloud High (GCC High) environments - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/deploy-addins-for-gcch?view=o365-worldwide
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
ms.date: 2026-06-05T00:00:00.0000000Z
audience: Admin
ms.topic: install-set-up-deploy
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
description: Deploy Office Add-ins in GCC High using a manifest URL or XML file in the Microsoft 365 admin center. Follow these steps to deploy your add-in now.
locale: en-us
document_id: 1b8484e6-f222-2a27-b938-02e5831d4077
document_version_independent_id: 1b8484e6-f222-2a27-b938-02e5831d4077
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/manage/deploy-addins-for-gcch.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/manage/deploy-addins-for-gcch
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/manage/deploy-addins-for-gcch.md
platformId: adec1216-26cc-94d1-9629-06429add3535
---

# Deploy Office Add-ins in Government Community Cloud High (GCC High) environments - Microsoft 365 admin | Microsoft Learn

Deploy Office Add-ins in Government Community Cloud High (GCC High) by using centralized deployment in the Microsoft 365 admin center. This article explains two deployment options so you can deploy add-ins when Marketplace access isn't available.

## Deploy an Office Add-in using the manifest XML URL

First try to deploy the add-in using the manifest XML URL. If the steps in this section fail, follow the steps in the next section Deploy an Office Add-in using the manifest XML file.

To deploy an Office Add-in using the manifest XML URL, follow these steps:

1. In your browser, go to the [Microsoft Marketplace](https://marketplace.microsoft.com/).
2. Search for and then select the tile of the add-in you want to deploy. Make sure to select the tile and not the **Get it now** button. The details page opens for the add-in.
3. In the URL for the details page, find and copy the AssetID value. The AssetID value is the value at the end of the URL:

    `https://marketplace.microsoft.com/<locale>/product/<AssetID>`

    For example, in the URL:

    `https://marketplace.microsoft.com/en-us/product/WA1234567989`

    The AssetID value is:

    `WA1234567989`
4. Paste the AssetID value to the following URL:

    `https://store.office.com/app/download?assetid=<AssetID>`

    For example, using the example AssetID value of `WA1234567989` from the previous step, the URL is:

    `https://store.office.com/app/download?assetid=WA1234567989`

    If you go to this URL, it displays the manifest XML for the add-in.
5. In a new browser window or tab, sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
6. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.
7. Under **Settings**, select [**Integrated apps**](https://admin.cloud.microsoft/?#/Settings/IntegratedApps).
8. In the **Integrated apps** page, make sure the **Deployed apps** tab is selected, and then select **Upload custom apps**.
9. In the **Upload Apps to deploy** page of the **Deploy New App** pane:

    1. In the **App type** dropdown menu, select **Office Add-in**.
    2. Under **Choose how to upload app**, select **Provide link to manifest file**, copy and paste the manifest XML URL previously determined into the text box, and then select **Validate**.
10. Once the manifest XML file is validated, the message **Manifest file validated** appears. Select **Next**.
11. In the **Add users** page of the **Deploy New App** pane, under **Assign users** select the users you want to have access to the add-in, and then select **Next**.
12. In the **Accept permissions requests** page of the **Deploy New App** pane, review the permissions that the add-in is requesting. If you accept the permissions, select **Next**.
13. In the **Review and finish deployment** page of the **Deploy New App** pane, review the deployment settings, and then select **Finish Deployment**.
14. When the deployment completes, the message **Deployment completed** appears. Select **Done**.

## Deploy an Office Add-in using the manifest XML file

If the deployment of the add-in using the manifest XML URL fails, use the steps in this section instead.

To deploy an Office Add-in using the manifest XML file, follow these steps:

1. In your browser, go to the [Microsoft Marketplace](https://marketplace.microsoft.com/).
2. Search for and then select the tile of the add-in you want to deploy. Make sure to select the tile and not the **Get it now** button. The details page opens for the add-in.
3. In the URL for the details page, find and copy the AssetID value. The AssetID value is the value at the end of the URL:

    `https://marketplace.microsoft.com/<locale>/product/<AssetID>`

    For example, in the URL:

    `https://marketplace.microsoft.com/en-us/product/WA1234567989`

    The AssetID value is:

    `WA1234567989`
4. Paste the AssetID value to the following URL:

    `https://store.office.com/app/download?assetid=<AssetID>`

    For example, using the example AssetID value of `WA1234567989` from the previous step, the URL is:

    `https://store.office.com/app/download?assetid=WA1234567989`
5. In a new browser window or tab, go to the URL determined in the previous step. The page at this URL displays the manifest XML for the add-in.
6. Right-click on the page, select **Save As** or **Save Page As** (depending on your browser), and then save the manifest XML file to a known location on your device. Make sure the file is saved as an `.xml` file with the `.xml` extension.
7. In a new browser window or tab, sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
8. From the left navigation bar, select **… Show all**, and then select **Settings** to expand it.
9. Under **Settings**, select [**Integrated apps**](https://admin.cloud.microsoft/?#/Settings/IntegratedApps).
10. In the **Integrated apps** page, select **Upload custom apps**.
11. In the **Upload Apps to deploy** page of the **Deploy New App** pane:

    1. In the **App type** dropdown menu, select **Office Add-in**.
    2. Under **Choose how to upload app**, select **Upload manifest file (.xml) from device** and then select **Choose File**.
    3. Browse to the location where you saved the manifest XML file, select the file, and then select **Open**.
12. Once the manifest XML file is validated, the message **Manifest file validated** appears. Select **Next**.
13. In the **Add users** page of the **Deploy New App** pane, under **Assign users** select the users you want to have access to the add-in, and then select **Next**.
14. In the **Accept permissions requests** page of the **Deploy New App** pane, review the permissions that the add-in is requesting. If you accept the permissions, select **Next**.
15. In the **Review and finish deployment** page of the **Deploy New App** pane, review the deployment settings, and then select **Finish Deployment**.
16. When the deployment completes, the message **Deployment completed** appears. Select **Done**.

Important

If there's an error concerning Admin Consent, the add-in isn't GCC High compatible. The Developer of the add-in should be contacted to allow their add-in to be GCC High compliant.