---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft Teams Apps App Usage Report - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-teams-apps-usage?view=o365-worldwide
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
- campaignIDs-batch1
search.appverid:
- BCS160
- MST160
- MET150
- MOE150
ai-usage: ai-assisted
description: The Microsoft Teams apps App usage report helps you understand app adoption per app and per user. Find out how to view and export this data in the admin center.
ms.date: 2026-06-11T00:00:00.0000000Z
locale: en-us
document_id: 406b87bb-aa1b-fc97-e53d-a55ba0d5110a
document_version_independent_id: 406b87bb-aa1b-fc97-e53d-a55ba0d5110a
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/microsoft-teams-apps-usage.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/microsoft-teams-apps-usage
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/microsoft-teams-apps-usage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
platformId: 9858e031-e532-6693-25ff-8f5f352cfa4c
---

# Microsoft Teams Apps App Usage Report - Microsoft 365 admin | Microsoft Learn

The Microsoft Teams apps App usage report provides insights into app activity across your organization. Use this report to understand which apps users install and actively use, and explore adoption trends at a per-app and per-user level.

For general information about usage reports in the Microsoft 365 admin center, and to see a list of all available reports, see [Microsoft 365 admin center usage reports overview](activity-reports).

## View the Microsoft Teams apps App usage report in the Microsoft 365 admin center

For information about the roles needed to view usage reports, see "Before you begin" in [Microsoft 365 admin center usage reports overview](activity-reports#before-you-begin)

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. On the dashboard homepage, on the Microsoft Teams apps activity card, select **View more**.

    [![Screenshot of the Microsoft Teams apps activity card.](../../media/teams-apps-tile.png)](../../media/teams-apps-tile.png#lightbox)
5. Or, on the **Usage** page, under **Reports**, select **Microsoft Teams apps**.
6. On the report page, select the **App usage** tab.

### Report considerations

- It can take about five days for usage and installs data for a newly published app to appear in the report. Data for a given day appears within 48 hours. For example, data for January 10 appears in the report by around January 12.
- The start date for all installs metrics is October 2021. The report only counts apps installed after that date.
- The report uses External (manifest) App IDs. For information about how to tie this ID to an app in the **Manage Apps** experience in Teams admin center, see [Manage app setup policies in Microsoft Teams](/en-us/microsoftteams/teams-app-setup-policies#install-apps).

To export the report data into an Excel .csv file, select **Export**. This action exports the usage data of all users and enables you to do simple sorting, filtering, and searching for further analysis.

## Interpret the Microsoft Teams apps App usage report

The Teams apps App usage report is available in the Microsoft 365 admin center and provides data through two separate reports:

- The **App usage** report
- The **User activity** report

### App usage tab

The **App usage** report helps answer the following questions:

- How many apps do users in your environment install?
- How many apps have at least one active user in your environment?
- How many apps are used by platform (Windows, Mac, Web, or mobile)?
- How many active users and active teams use the app?

To view the **App usage** report, select the **Apps usage** tab.

[![Screenshot of the App usage tab of the Microsoft Teams apps usage report showing installed and used app trends.](../../media/teams-apps-usage-tab.png)](../../media/teams-apps-usage-tab.png#lightbox)

At the top of the report, three charts describe cross-app trends across your organization.

- Apps installed
- Apps used
- Platform

The report displays trends over the last 7, 30, 90, or 180 days. However, if you select a particular day in the report, the table shows data for up to 28 days from the current date, not the date the report generated.

To filter all charts, use the time range picker in the top corner of the **App usage** tab.

[![Screenshot of the time range filter in the Microsoft Teams app usage report, used to filter charts by 7, 30, 90, or 180 days.](../../media/teams-apps-usage-filter.png)](../../media/teams-apps-usage-filter.png#lightbox)

#### Apps installed

The **Apps installed** chart shows the total number of apps installed across your organization up to each date within the selected period. For example, if you select January 28, 2026, the chart shows the total number of installs from October 2025 up to January 28, 2026.

[![Screenshot of the Apps installed chart in the Microsoft Teams apps usage report showing cumulative app install totals over time.](../../media/apps-installed.png)](../../media/apps-installed.png#lightbox)

#### Apps used

The **Apps used** chart shows the number of apps used across your organization on each date within the selected period. For example, if you select January 28, the chart shows the total number of apps used on January 28.

[![Screenshot of the Apps used chart in the Microsoft Teams apps usage report showing the number of apps used per day in the selected period.](../../media/apps-used.png)](../../media/apps-used.png#lightbox)

#### Platform

The **Platform** chart shows the number of apps used across your organization by platform for the selected period. Available platforms are Windows, Mac, Mobile (across iOS and Android), and Web.

[![Screenshot of the Platform chart in the Microsoft Teams apps usage report showing app usage broken down by Windows, Mac, Mobile, and Web.](../../media/platform.png)](../../media/platform.png#lightbox)

#### Apps usage details table

The **Apps usage details** table shows a per-app view with the following metrics for each app. By default, you see a subset of the metric columns.

To add or remove columns from the report, select **Choose columns**.

[![Screenshot of the Apps usage details table in the Microsoft Teams app usage report showing per-app metrics including active users and teams.](../../media/apps-usage-details.png)](../../media/apps-usage-details.png#lightbox)

| Metric | Definition | Included by default? |
| --- | --- | --- |
| App ID | The external app identifiers present in the app manifest. | Yes |
| Last used date | The date when anyone in your organization last used that app. | Yes |
| Teams using this app | The number of distinct Teams teams that have at least one user using this app. | Yes |
| Users using this app | The number of distinct users in your organization that are using this app. | Yes |
| Used on Windows | This value indicates whether at least one user in your organization used that app on Windows. | Yes |
| Used on Mobile | This value indicates whether at least one user in your organization used that app on mobile. | Yes |
| Used on Web | This value indicates whether at least one user in your organization used that app on Web. | Yes |
| Used on Mac | The number of ad hoc meetings a user organized during the specified time period. | No |
| App name | The name of this application as present in the app manifest. | No |
| Publisher | The publisher of this application as present in the app manifest. This metric is only available for apps published to the global Store. | No |

### User activity tab

- The **User activity** report helps answer the following questions:

    - How many users in your environment install at least one app?
    - How many users in your environment use at least one app?
    - How many users use an app across platforms (Windows, Mac, Web, and more)?
    - How many apps does each user use?

To view the **user activity** in the Teams app usage report, select the **User activity** tab.

[![Screenshot of the User activity tab in the Microsoft Teams apps usage report showing charts for users who installed and used apps.](../../media/teams-apps-user-activity.png)](../../media/teams-apps-user-activity.png#lightbox)

At the top of the report, three charts describe cross-app trends across your organization.

- Users who installed apps
- Users who used apps
- Platform

To filter all charts, use the time range picker in the top corner of the **User activity** tab.

[![Screenshot of the time range filter in the Microsoft Teams app usage report, used to filter charts by 7, 30, 90, or 180 days.](../../media/teams-apps-usage-filter.png)](../../media/teams-apps-usage-filter.png#lightbox)

#### Users who have installed apps

The **Users who have installed apps** chart shows the total number of unique users who install an app up to each date within the selected period. For example, if you select January 28, 2026, the chart shows the total number of users from October 2025 up to January 28, 2026.

[![Screenshot of the Users who have installed apps chart in the Microsoft Teams apps usage report showing cumulative unique user install counts.](../../media/users-who-installed-apps.png)](../../media/users-who-installed-apps.png#lightbox)

#### Users who have used apps

The **Users who have used apps** chart shows the number of unique users that use any app on each date within the selected period. For example, if you select January 28, the chart shows the total number of users on January 28.

[![Screenshot of the Users who have used apps chart in the Microsoft Teams apps usage report showing unique daily active app users over the selected period.](../../media/users-who-used-apps.png)](../../media/users-who-used-apps.png#lightbox)

#### Platform

The **Platform** chart shows the number of apps used across your organization by platform for the selected period. Available platforms are Windows, Mac, Mobile (across iOS and Android), and Web.

[![Screenshot of the Platform chart on the User activity tab of the Microsoft Teams apps usage report showing app usage by Windows, Mac, Mobile, and Web.](../../media/user-activity-platform.png)](../../media/user-activity-platform.png#lightbox)

#### User activity details table

The **User activity details** table shows a per-user view with the following metrics for each app. By default, it includes a subset of the metric columns.

To add or remove columns from the report, select **Choose columns**.

[![Screenshot of the User activity details table in the Microsoft Teams apps usage report showing per-user metrics for app installs and usage across platforms.](../../media/user-activity-details.png)](../../media/user-activity-details.png#lightbox)

| Metric | Definition | Included by default? |
| --- | --- | --- |
| User name | The user name for a unique user. The value is concealed by default. | Yes |
| Apps installed | The number of unique apps (across Store and custom) that the user installed. | Yes |
| Apps used | The number of unique apps (across Store and custom) that the user opened and used. | Yes |
| Apps used in a Team | The number of unique apps (across Store and custom) that the user opened and used in a team in Microsoft Teams. | Yes |
| Used on Windows | This value indicates whether that user used any app on Windows. | Yes |
| Used on Mobile | This value indicates whether that user used any app on Mobile (iOS or Android). | Yes |
| Used on Web | This value indicates whether that user used any app on Web. | Yes |
| Used on Mac | This value indicates whether that user used any app on Mac. | No |

Note

By default, user-specific information like usernames, display names, groups, and sites is hidden in usage reports. To learn how to display this information in usage reports, see [Show user, group, or site details in usage reports](activity-reports#show-user-group-or-site-details-in-usage-reports).

## Manage apps in the Teams admin center

For information about how to manage your Teams apps, see [About apps in Microsoft Teams](/en-us/microsoftteams/deploy-apps-microsoft-teams-landing-page).

To link an app in this report to the Manage Apps experience in the Teams admin center, use the following items:

- App Name
- External App ID

External App IDs are equivalent to the ID in the **Manage apps** page for Store apps. For custom apps, to view External App ID in the **Manage apps** page, follow the instructions on [Manage apps setup policies in Microsoft Teams](/en-us/microsoftteams/teams-app-setup-policies) to add the column in the column settings. You can also view it on the app details page for a custom app.

## FAQ

### I blocked the Teams app in the Teams admin center. Why does it still show usage in the apps usage report in Teams admin center?

Even if you block an app in the Teams admin center, usage signals might still appear in the [Teams app usage report](/en-us/microsoftteams/teams-analytics-and-reports/app-usage-report) or in the [Microsoft 365 Teams app usage report](microsoft-teams-apps-usage). This situation can happen due to passive user interactions, such as viewing a card posted by the app in a chat or channel. These interactions can generate telemetry without the user actively launching or interacting with the app.

### If I block a Teams app in the Teams admin center, is it still being used?

No. Blocking the app in the Teams admin center prevents users from launching or executing it. The app isn't running, and users can't interact with it directly. However, the usage report includes a broader range of signals beyond just app launches.

### Is the app usage report inaccurate?

The report is accurate, but it's intentionally inclusive. It reflects a wider set of usage types, including passive views of app content. This approach provides visibility into all the ways users might be exposed to app functionality, even if the app is blocked from active use.

### Does blocking an app in the Teams admin center stop all usage across Microsoft 365?

No. When you block an app in the Teams admin center, users can't install or launch it in Teams. This action doesn't block passive exposure or usage in other Microsoft 365 surfaces like Outlook or the Microsoft 365 app.

Block the app in both the Teams admin center and the Microsoft 365 admin center. If your organization uses [Unified app management](/en-us/microsoftteams/manage-apps-across-m365#what-is-unified-app-management), settings made in one admin center sync with the other. This synchronization doesn't prevent passive usage.

### Does the report differentiate between "passive" usage vs "actual" usage, so I can be certain there's no app usage occurring?

Currently, there are no plans to separate passive usage from active usage in the report.