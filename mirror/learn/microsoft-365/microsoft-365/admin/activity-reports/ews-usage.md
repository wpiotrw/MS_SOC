---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Exchange Web Services (EWS) Usage Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/ews-usage?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
ms.author: cmcatee
author: cmcatee-MSFT
manager: scotv
ms.reviewer: hlu
audience: Admin
ms.topic: concept-article
ms.service: microsoft-365-business
ms.localizationpriority: medium
ms.collection:
- M365-subscription-management
- Adm_O365
search.appverid:
- BCS160
- MST160
- MET150
- MOE150
ai-usage: ai-assisted
description: The Exchange Web Services (EWS) usage report helps Microsoft 365 admins track EWS SOAP actions, active apps, and call volume. Prepare now for the October 2026 EWS retirement.
ms.date: 2026-04-03T00:00:00.0000000Z
locale: en-us
document_id: 14fbf312-caec-c995-8c77-82cb15aec045
document_version_independent_id: 14fbf312-caec-c995-8c77-82cb15aec045
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/ews-usage.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/ews-usage
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/ews-usage.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 4df9310a-c219-78db-a52c-3843c00cd9b2
---

# Exchange Web Services (EWS) Usage Report - Microsoft 365 admin | Microsoft Learn

The Exchange Web Services (EWS) usage report displays the SOAP actions used by each application calling EWS in your organization. It also shows the successful-call volume for each SOAP action. This information enables you to coordinate with the application owners to ensure they're preparing for the [EWS deprecation in October 2026](https://techcommunity.microsoft.com/blog/exchange/retirement-of-exchange-web-services-in-exchange-online/3924440).

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the EWS usage report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Exchange**.
5. On the report page, select the **EWS usage** tab.

## Interpret the EWS usage report

You can filter the EWS usage report by the last 7, 30, or 90 days.

Note

Usage data is collected and aggregated weekly, not daily. It can take up to 10 days for usage to show in the report.

To review the applications that use EWS within your organization, examine the **Usage trend** and **Usage details** sections. Additionally, summarized information at the top provides an overview of the overall usage.

[![Screenshot of the Exchange Web Services (EWS) usage report.](../../media/exchange-web-usage-report.png)](../../media/exchange-web-usage-report.png#lightbox)

### Summary data

Two summary headers appear at the top of the page:

- **Active apps** shows the number of unique apps that sent at least one request to EWS during the selected period.
- **Daily average call volume** shows the average number of daily requests from active apps during the selected period.

### Usage trend chart

The usage trend chart displays the projected EWS usage trend in your tenant, using weekly data points that summarize all active apps in your tenant that use EWS during that week. The Y-axis represents the number of apps, and the X-axis indicates the first date of the week within the selected period.

### Usage details table

The following table provides a breakdown of the EWS usage per SOAP action by each active application in your tenant during the selected period. You can't customize the columns.

| Metric | Definition |
| --- | --- |
| Application ID | The Microsoft Entra identifier for the registered application |
| SOAP Action | The specific Exchange Web Service SOAP action executed |
| Call Volume | The number of SOAP action calls in the given period |
| Last Activity date (UTC) | The last date of activity recorded for that app and SOAP action |

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

For a list of Microsoft first-party client application IDs, see [Commonly used Microsoft first-party services and portal apps](/en-us/power-platform/admin/apps-to-allow). For Microsoft applications, Microsoft periodically updates those apps to remove EWS dependencies. Keep your client applications up-to-date. If you still can't find the Application ID, check your Enterprise Applications in Microsoft Entra ID. For more information, see [Quickstart: View enterprise applications](/en-us/entra/identity/enterprise-apps/view-applications-portal).