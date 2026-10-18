---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Exchange Email App Usage Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/email-apps-usage-ww?view=o365-worldwide
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
ms.custom: 
search.appverid:
- BCS160
- MET150
- MOE150
- GEA150
ms.assetid: c2ce12a2-934f-4dd4-ba65-49b02be4703d
ai-usage: ai-assisted
description: The Exchange email app usage report reveals connected apps and Outlook versions. Discover how to find unsupported clients and upgrade users today.
ms.date: 2026-05-18T00:00:00.0000000Z
locale: en-us
document_id: 4b2a5f97-f6fd-c403-85b6-553d96c2ba96
document_version_independent_id: 4b2a5f97-f6fd-c403-85b6-553d96c2ba96
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/email-apps-usage-ww.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/email-apps-usage-ww
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/email-apps-usage-ww.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 75f174ea-9617-c63e-b790-d3e5861d4378
---

# Exchange Email App Usage Report - Microsoft 365 admin | Microsoft Learn

The Exchange email app usage report provides details about how many email apps connect to Exchange Online. You can view the version information of Outlook apps that users are using. This information helps you follow up with those users who are using unsupported versions to install supported versions of Outlook.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Exchange email app usage report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **Exchange**, and then select the **Email app usage** tab.

## Interpret the Exchange email app usage report

The report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date, not the date the report generated. The data in each report usually covers up to the last 24 to 48 hours.

[![Screenshot of the Exchange email app usage report showing connected apps and Outlook versions in Microsoft 365.](../../media/email-apps-report.png)](../../media/email-apps-report.png#lightbox)

The **Users** chart shows the number of unique users that connected to Exchange Online by using any email app. The Y axis is the total count of unique users that connected to an app on any day of the reporting period. The X axis is the number of unique users that used the app for that reporting period.

The **Apps** chart shows the number of unique users by app over the selected time period. The Y axis is the total count of unique users who used a specific app during the reporting period. The X axis is the list of apps in your organization.

The **Versions** chart shows the number of unique users for each version of Outlook in Windows. The Y axis is the total count of unique users using a specific version of Outlook desktop. If the report can't resolve the version number of Outlook, the quantity shows as **Undetermined**. The X axis is the list of apps in your organization.

You can filter the series you see on the charts by selecting an item in the legend. You might not see all the items in the list in the columns until you add them.

To add or remove columns from the report, select **Choose columns**.

[![Screenshot of the Exchange Email apps usage report column options.](../../media/041bd6ff-27e8-409d-9608-282edcfa2316.png)](../../media/041bd6ff-27e8-409d-9608-282edcfa2316.png#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

The following table contains definitions of the metrics available in the report.

| Metric | Definition |
| --- | --- |
| Username | The name of the email app's owner. |
| Last activity date | The latest date the user read or sent an email message. |
| Mac mail, Mac Outlook, Outlook, Outlook mobile, and Outlook on the web | Examples of email apps you might have in your organization. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).