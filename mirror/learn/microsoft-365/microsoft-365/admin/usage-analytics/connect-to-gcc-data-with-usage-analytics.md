---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Connect to Microsoft 365 Government Community Cloud (GCC) data with Usage Analytics - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/usage-analytics/connect-to-gcc-data-with-usage-analytics?view=o365-worldwide
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
ms.date: 2026-06-08T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
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
ms.custom:
- AdminSurgePortfolio
- AdminTemplateSet
search.appverid:
- BCS160
- MET150
- MOE150
ms.assetid: 9db96e9f-a622-4d5d-b134-09dcace55b6a
description: Connect to your Microsoft 365 Government Community Cloud GCC tenant data using the Usage Analytics template app in Power BI. Follow these steps to set up and publish your report.
locale: en-us
document_id: 6be7caf9-523d-2e84-fb17-14b1606aa97a
document_version_independent_id: 34a7cb37-5f79-c1d3-f40f-8afb91f48862
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/usage-analytics/connect-to-gcc-data-with-usage-analytics.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/usage-analytics/connect-to-gcc-data-with-usage-analytics
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/usage-analytics/connect-to-gcc-data-with-usage-analytics.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
platformId: 070852df-6846-47e9-7233-363fd927c852
---

# Connect to Microsoft 365 Government Community Cloud (GCC) data with Usage Analytics - Microsoft 365 admin | Microsoft Learn

Use the following procedures to connect to your Microsoft 365 Government Community Cloud (GCC) tenant data by using the Microsoft 365 Usage Analytics report in Power BI Desktop.

Note

These instructions are specifically for Microsoft 365 GCC tenants and aren't applicable to GCC High and DOD.

## Before you begin

To initially configure Microsoft 365 Usage Analytics:

- You must be a Microsoft 365 Global Administrator to enable data collection.

Important

Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

- You must have the [Power BI Desktop](https://powerbi.microsoft.com/desktop/) application to use the template file.
- You must have a [Power BI Pro license](https://go.microsoft.com/fwlink/p/?linkid=845347) or Premium capacity to publish and view the report.

## Step 1: Make your organization's data available for the Microsoft 365 Usage Analytics report

1. Sign in to the [Microsoft 365 admin center](https://admin.cloud.microsoft/).
2. From the left navigation bar, select **… Show all**, and then select **Reports** to expand it.
3. Under **Reports**, select [**Usage**](https://admin.cloud.microsoft/?#/reportsUsage).
4. In the **Microsoft 365 usage analytics** section of the **Usage** page, select **Get Started**.
5. Under **Enable Power BI for usage analytics** in the **Reports** pane, select **Make organizational usage data available to Microsoft 365 usage analytics for Power BI**, and then select **Save**.

    [![Screenshot of the option to make organizational usage data available to Microsoft 365 Usage Analytics for Power BI in the admin center.](../../media/usage-analytics/make-data-available.png)](../../media/usage-analytics/make-data-available.png#lightbox)

    Selecting this option starts a process to make your organization's data accessible for this report. You might see a message that states **We're getting your data ready for Microsoft 365 usage analytics**. This process can take 24 hours to complete.
6. When your organization's data is ready, refreshing the page shows a message stating that your data is now available, and provides your **tenant ID** number. You must use the tenant ID in a later step when you attempt to connect to your tenant data.

    [![Screenshot of the tenant ID displayed in the Microsoft 365 admin center after organizational usage data is ready for Usage Analytics.](../../media/usage-analytics/tenant-id-gcc.png)](../../media/usage-analytics/tenant-id-gcc.png#lightbox)

    Important

    When your data is available, don't select **Go to Power BI**. That option takes you to the Power BI Marketplace. The template app for this report that GCC tenants require isn't available in the Power BI Marketplace.

## Step 2: Download the Power BI template, connect to your data, and publish the report

Microsoft 365 GCC users can download and use the Microsoft 365 Usage Analytics report template file to connect to their data. You need Power BI Desktop to open and use the template file.

Note

A template app for the Microsoft 365 Usage Analytics report isn't available for GCC tenants in the Power BI Marketplace.

1. Download the [Power BI template](https://download.microsoft.com/download/7/8/2/782ba8a7-8d89-4958-a315-dab04c3b620c/Microsoft%20365%20Usage%20Analytics.pbit).
2. Once the Power BI template is downloaded, open it using Power BI Desktop.
3. When prompted for a **TenantID**, enter the tenant ID you received when you prepared your organization's data for this report in Step 1, and then select **Load**. It can take several minutes for your data to load.

    [![Screenshot of the TenantID prompt in Power BI Desktop where you enter your tenant ID to connect to Microsoft 365 usage data.](../../media/usage-analytics/add-tenant-id.png)](../../media/usage-analytics/add-tenant-id.png#lightbox)
4. When loading completes, your report is displayed, and you see an executive summary of your data.

    [![Screenshot of the executive summary view of the Microsoft 365 Usage Analytics report displayed in Power BI Desktop after data loads.](../../media/usage-analytics/exec-summary.png)](../../media/usage-analytics/exec-summary.png#lightbox)
5. Save your changes to the report.
6. Select **Publish** in the Power BI Desktop menu to publish the report to the Power BI service where it can be viewed. This feature requires either a Power BI Pro license or Power BI Premium capacity. As part of the [publish process](/en-us/power-bi/create-reports/desktop-upload-desktop-files#to-publish-a-power-bi-desktop-dataset-and-reports), you must select a destination to publish to an available workspace in the Power BI service.