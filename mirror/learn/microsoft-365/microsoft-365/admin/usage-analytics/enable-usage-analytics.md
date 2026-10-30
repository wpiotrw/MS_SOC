---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Enable Microsoft 365 usage analytics - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/usage-analytics/enable-usage-analytics?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- CSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2026-04-29T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: m365-core
ms.subservice: activity-reports
ms.localizationpriority: medium
ms.collection:
- Tier2
- M365-subscription-management
- Adm_O365
- Adm_TOC
- operations-pod
ms.custom:
- AdminTemplateSet
- admindeeplinkMAC
search.appverid:
- BCS160
- MET150
- MOE150
ms.assetid: 9db96e9f-a622-4d5d-b134-09dcace55b6a
description: Learn how to start collecting data for your tenant by using the Microsoft 365 Usage Analytics template app in Power BI.
locale: en-us
document_id: 65732911-21e9-0902-51fa-0d3ae0caaa7a
document_version_independent_id: 3682fff5-36fc-1d69-96ef-88f7f73225d5
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/usage-analytics/enable-usage-analytics.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/usage-analytics/enable-usage-analytics
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/usage-analytics/enable-usage-analytics.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
platformId: 806bcf22-a99f-cef9-fd5d-5057a428a320
---

# Enable Microsoft 365 usage analytics - Microsoft 365 admin | Microsoft Learn

To enable Microsoft 365 usage analytics in a Microsoft 365 US Government Community Cloud (GCC) tenant, see [Connect to Microsoft 365 Government Community Cloud (GCC) data with Usage Analytics](connect-to-gcc-data-with-usage-analytics).

## Before you begin

To get started with Microsoft 365 usage analytics, you must first make the data available in the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339), then select **Reports** &gt; **Usage** and initiate the template app in Power BI.

## Get Power BI

If you don't already have Power BI, you can [sign up for Power BI Pro](https://go.microsoft.com/fwlink/p/?linkid=845347). Select **Try free** to sign up for a trial, or **Buy now** to get Power BI Pro.

You can also expand **Products** to buy a version of Power BI.

Note

You must have a Power BI Pro license to install, customize, and distribute a template app. For more information, please see [Prerequisites](/en-us/power-bi/service-template-apps-install-distribute?source=docs#prerequisites).

To share your data, both you and the people who you share the data with need a Power BI Pro license. Or the content needs to be in a workspace in a [Power BI premium service](/en-us/power-bi/service-premium-what-is).

## Enable the template app

To enable the template app, you have to be a **Global administrator**.

Important

Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

For more information, see [about admin roles](../add-users/about-admin-roles).

1. Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
2. From the left navigation bar, select **... Show all**, and then select **Settings** to expand it.
3. Under **Settings**, select [**Org Settings**](https://admin.cloud.microsoft/?#/Settings/SecurityPrivacy).
4. In the **Org Settings** page, select the **Services** tab, and then select **Reports**.
5. Under **Microsoft 365 usage analytics** in the **Reports** panel, select the option **Make report data available to Microsoft 365 usage analytics for Power BI**.
6. Select **Save**.

The data collection process completes in two to 48 hours depending on the size of your tenant. The **Go to Power BI** button is enabled (no longer gray) when data collection is complete. Once complete, the app provides historical usage data at your organization level.

Note

The data for the **"User Activity"** tab is only refreshed after the 15th day of the current month and the first day of the next month, so it will remain empty initially until the first refresh is completed.

## Start the template app

To start the template app, you have to have one of the following roles:

- [**Report Reader**](/en-us/entra/identity/role-based-access-control/permissions-reference#reports-reader).
- [**Exchange Administrator**](/en-us/entra/identity/role-based-access-control/permissions-reference#exchange-administrator).
- [**Skype for Business Administrator**](/en-us/entra/identity/role-based-access-control/permissions-reference#skype-for-business-administrator).
- [**SharePoint Administrator**](/en-us/entra/identity/role-based-access-control/permissions-reference#sharepoint-administrator).

1. Copy the tenant ID and select **Go to Power BI**.
2. When you get to Power BI, sign in. Then **Select Apps**-&gt;**Get apps** from the navigation menu.
3. In the **Apps** tab, type Microsoft 365 in the search box and then select **Microsoft 365 usage analytics** &gt; **Get it now**.

    [![Select Get it now.](../../media/78102250-9874-4a32-8365-436f13560b52.png)](https://app.powerbi.com/groups/me/getapps/services/cia_microsoft365.microsoft-365-usage-analytics)
4. Once the app is installed, open it by selecting the tile.
5. Select **Explore app** to view the app with sample data. Choose **Connect** to connect the app to your organization's data.
6. Choose **Connect**, on the **Connect to Microsoft 365 usage analytics** screen, then type in the tenant ID (without dashes) you copied in step (1), and select **Next**.
7. On the next screen, select **OAuth2** as the **Authentication method** &gt; **Sign in**. If you choose any other authentication method, the connection to the template app fails.

    ![Choose Microsoft account as authentication method.](../../media/ab6f0463-c3f7-4088-a605-67c699fa86adnew.png)
8. After the template app is instantiated, the Microsoft 365 usage analytics dashboard is available in Power BI on the web. The initial loading of the dashboard takes between 2 to 30 minutes.

Tenant level aggregates will be available in all reports after opting in. **User-level details will only become available around the 5th of the next calendar month after opting in**. This impacts all reports under User Activity (See [Navigate and utilize the reports in Microsoft 365 usage analytics](navigate-and-utilize-reports) for tips on how to view and use these reports).

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](../activity-reports/activity-reports#show-user-group-or-site-details-in-usage-reports).