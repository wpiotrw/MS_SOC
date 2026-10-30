---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Troubleshooting Microsoft 365 Usage Analytics - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/usage-analytics/usage-analytics-errors?view=o365-worldwide
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
ms.date: 2026-06-12T00:00:00.0000000Z
audience: Admin
ms.topic: troubleshooting-general
ms.service: m365-core
ms.subservice: activity-reports
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- operations-pod
ms.custom: AdminSurgePortfolio
search.appverid:
- BCS160
- MET150
- MOE150
ms.assetid: a73632a1-62c8-4a13-8115-913773b30f93
description: Troubleshoot Microsoft 365 usage analytics errors in Power BI and the admin center. Use these fixes to restore access and get data working.
locale: en-us
document_id: 32d4d89d-05e0-b2f8-75af-6014364107f9
document_version_independent_id: 8aa9a383-6b58-c5ff-5661-5fc32ee2b3fe
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/usage-analytics/usage-analytics-errors.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/usage-analytics/usage-analytics-errors
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/usage-analytics/usage-analytics-errors.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
platformId: e0c025bd-f6c8-dcf3-8738-50917e0ef0a6
---

# Troubleshooting Microsoft 365 Usage Analytics - Microsoft 365 admin | Microsoft Learn

Use this article to troubleshoot common Microsoft 365 usage analytics errors in Power BI and the Microsoft 365 admin center.

## We are unable to process your request. You have to first subscribe to this data from the Microsoft 365 admin center

**Error code:** 422

**Where you see this message:** In Power BI when you connect to the Microsoft 365 Usage Analytics template app, or when you directly call the Microsoft 365 Reporting APIs.

**Cause:** Before you can connect to the app, you need to subscribe to the data from the Microsoft 365 admin center. If you don't complete this step, you can't connect to the template app, even if you provide your Microsoft 365 tenant ID.

**To fix this error:** To subscribe to the data:

1. Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
2. From the left navigation bar, select **… Show all**, and then select **Reports** to expand it.
3. Under **Reports**, select [**Usage**](https://admin.cloud.microsoft/?#/reportsUsage).
4. In the **Microsoft 365 usage analytics** section of the **Usage** page, select **Get Started**.
5. Under **Enable Power BI for usage analytics** in the **Reports** pane, select **Make organizational usage data available to Microsoft 365 usage analytics for Power BI**, and then select **Save**.

    [![Screenshot of the option to make organizational usage data available to Microsoft 365 Usage Analytics for Power BI in the admin center.](../../media/usage-analytics/make-data-available.png)](../../media/usage-analytics/make-data-available.png#lightbox)

    Selecting this option starts a process to make your organization's data accessible for this report. You might see a message that states **We're getting your data ready for Microsoft 365 usage analytics**. This process can take up to 24 hours to complete.

## We are processing your data

**Where you see this message:** In the **Microsoft 365 usage analytics** tile, on the **Usage** dashboard in the Microsoft 365 admin center.

**Cause:** When you [opt in to seeing data in the template app](enable-usage-analytics) from the Microsoft 365 admin center, the Microsoft 365 system starts generating historical usage data for your organization. Depending on the size of your tenant, this step can take anywhere from 2 hours to 48 hours.

**To fix this issue:** The data appears within three days. However, if the message doesn't change to **Your data is ready** after three days, [contact Microsoft 365 for business support](../get-help-support).

## We are unable to process your request at this time. We are still preparing the data for your organization

**Error code:** 423

**Where you see this message:** In Power BI, when you're connecting to the Microsoft 365 Usage Analytics template app or when directly calling the Microsoft 365 Reporting APIs.

**Cause:** When you [opt in to seeing data in the template app](enable-usage-analytics) from the admin center, the Microsoft 365 system starts generating historical usage data for your organization. Depending on the size of your tenant, this step can take anywhere from two hours to 48 hours.

**To fix this issue:** The data appears within three days. However, if the message doesn't change to **Your data is ready** after three days, [contact Microsoft 365 for business support](../get-help-support).

## The tenant ID you provided is not in the correct format

**Error code:** 400

**Where you see this message:** In Power BI, when you're connecting to the Microsoft 365 Usage Analytics template app or when directly calling the Microsoft 365 Reporting APIs.

**Cause:** The tenant ID is a GUID and must be in the format of xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx. If you enter any other string in the tenant input box, you get this error.

**To fix this error:**

1. Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
2. From the left navigation bar, select **… Show all**, and then select **Reports** to expand it.
3. Under **Reports**, select [**Usage**](https://admin.cloud.microsoft/?#/reportsUsage).
4. In the **Microsoft 365 usage analytics** section of the **Usage** page, the tenant ID is listed on the tile. You can copy it from here and paste it in the dialog box for connecting to the template app.

## The tenant ID you provided is not recognized by our system

**Error code:** 404

**Where you see this message:**

- When you connect to the Microsoft 365 Usage Analytics template app in Power BI.
- When you directly call the Microsoft 365 Reporting APIs.

**Cause:** The tenant ID you provided isn't valid or doesn't exist.

**To fix this error:**

1. Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
2. From the left navigation bar, select **… Show all**, and then select **Reports** to expand it.
3. Under **Reports**, select [**Usage**](https://admin.cloud.microsoft/?#/reportsUsage).
4. In the **Microsoft 365 usage analytics** section of the **Usage** page, the tenant ID is listed on the tile. You can copy it from here and paste it in the dialog box for connecting to the template app.

## Please re-enter your credentials to sign in to Power BI again

**Error code:** 302

**Where you see this message:**

- When you connect to the Microsoft 365 Usage Analytics template app in Power BI.
- When you directly call the Microsoft 365 Reporting APIs.

**Cause:** The authorization code failed and can require you to enter your credentials again.

**To fix this error:** Sign out of Power BI, and then sign in again.

## You do not have the right authorization to access to this data. To be able to gain access to the data from this service you need to be either a global admin or any one of the product admins

**Error code:** 403

**Where you see this message:**

- When you connect to the Microsoft 365 Usage Analytics template app in Power BI.
- When you directly call the Microsoft 365 Reporting APIs.

**Cause:** The authorization code fails because the user who tries to connect to the template app doesn't have the right level of authorization to access this data.

**To fix this error:** To connect to the template app, provide the credentials of a user who has one of the following roles in Microsoft 365:

- [**Exchange Administrator**](/en-us/entra/identity/role-based-access-control/permissions-reference#exchange-administrator).
- [**Skype for Business Administrator**](/en-us/entra/identity/role-based-access-control/permissions-reference#skype-for-business-administrator).
- [**SharePoint Administrator**](/en-us/entra/identity/role-based-access-control/permissions-reference#sharepoint-administrator).
- [**Global Reader**](/en-us/entra/identity/role-based-access-control/permissions-reference#global-reader).
- [**Reports Reader**](/en-us/entra/identity/role-based-access-control/permissions-reference#reports-reader).

For more information, see [About administrator roles in the Microsoft 365 admin center](../add-users/about-admin-roles).

Important

Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

## Refresh failed

**Where you see this message:** Email from Power BI or failed status in the refresh history.

**Cause:** Sometimes, the credentials of the user who connects to the template app reset but don't update in the connection settings of the template app. This problem causes the user to see refresh failure errors.

**To fix this error:**

1. In Power BI, find the dataset corresponding to the Microsoft 365 Usage Analytics template app.
2. Select **schedule refresh**.
3. Enter your admin credentials.

If that step doesn't work, clear the cache, and re-create the template app.