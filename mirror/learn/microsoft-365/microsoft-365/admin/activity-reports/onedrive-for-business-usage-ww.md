---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: OneDrive Usage Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/onedrive-for-business-usage-ww?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
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
- AdminTemplateSet
search.appverid:
- BCS160
- MST160
- MET150
- MOE150
ai-usage: ai-assisted
description: The OneDrive Usage report in Microsoft 365 admin center gives you insights into accounts, files, and storage. Monitor trends and export data for deeper analysis.
ms.date: 2026-04-24T00:00:00.0000000Z
locale: en-us
document_id: bc749017-c324-2da2-1076-407da1a3eef8
document_version_independent_id: bc749017-c324-2da2-1076-407da1a3eef8
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/onedrive-for-business-usage-ww.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/onedrive-for-business-usage-ww
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/onedrive-for-business-usage-ww.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: d41a06ca-4125-6b7b-a7da-0a3d526fabe2
---

# OneDrive Usage Report - Microsoft 365 admin | Microsoft Learn

The OneDrive Usage report provides a high-level view of the value you get from OneDrive. The report includes details about the total number of accounts, files, and storage used across your organization. You can drill into it to understand the trends of active OneDrive accounts, how many files users are interacting with, and the amount of storage used. It also gives you details for each user's OneDrive.

Important

The report only includes users who have a valid OneDrive license.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the OneDrive Usage report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the **Usage** page, under **Reports**, select **OneDrive**.
5. On the report page, select the **Usage** tab.

## Interpret the OneDrive Usage report

The report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date, not the date the report generated.

[![Screenshot of the Microsoft OneDrive usage report.](../../media/3cdaf2fb-1817-479b-a0e1-2afa228690cf.png)](../../media/3cdaf2fb-1817-479b-a0e1-2afa228690cf.png#lightbox)

To add or remove columns from the report, select **Choose columns**.

[![Screenshot of the columns available for the OneDrive usage report.](../../media/9ee80f25-cfe3-411d-8e31-08f1507d18c1.png)](../../media/9ee80f25-cfe3-411d-8e31-08f1507d18c1.png#lightbox)

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

| Metric | Definition |
| --- | --- |
| URL | The web address for the user's OneDrive. Note: URL is temporarily empty. |
| Deleted | The deletion status of the OneDrive. It takes at least seven days for accounts to be marked as deleted. |
| Owner | The username of the primary administrator of the OneDrive. |
| Owner principal name | The email address of the owner of the OneDrive. |
| Last activity date (UTC) | The latest date a file activity was performed in the OneDrive. If the OneDrive has no file activity, the value is blank. |
| Files | The number of files in the OneDrive. |
| Active files | The number of active files within the time period.**NOTE:** If you remove files during the specified time period for the report, the number of active files shown in the report might be larger than the current number of files in OneDrive. Deleted users continue to appear in reports for 180 days. |
| Storage used (MB) | The amount of storage the OneDrive uses in MB. |
| Site ID | The site ID of the site. |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).

Note

The OneDrive site URL might not display in related usage reports. You can use PowerShell to display the site URL. For more information, see [Use PowerShell to resolve site URLs](resolve-site-urls).