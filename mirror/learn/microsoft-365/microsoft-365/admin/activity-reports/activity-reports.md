---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft 365 Admin Center Usage Reports Overview - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/activity-reports?view=o365-worldwide
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
ms.reviewer: cmcatee
audience: Admin
ms.topic: overview
ms.service: microsoft-365-business
ms.localizationpriority: high
ms.collection:
- M365-subscription-management
- Adm_O365
ms.custom:
- adminvideo
- AdminTemplateSet
- GAUpdates
search.appverid:
- MET150
- MOE150
- GEA150
ai-usage: ai-assisted
ms.assetid: 0d6dfb17-8582-4172-a9a9-aed798150263
description: Monitor user activity, track license usage, and identify trends with Microsoft 365 admin center usage reports. Learn how to optimize your Microsoft 365 environment and improve productivity.
ms.date: 2026-08-28T00:00:00.0000000Z
locale: en-us
document_id: 1eaa6e98-66e9-aad3-2d67-543c22f4ce4b
document_version_independent_id: 26bddf9e-f338-329f-76e5-302a1343f7f1
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/activity-reports/activity-reports.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/activity-reports/activity-reports
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/activity-reports/activity-reports.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e4b2d8-b70c-4019-b49a-d1f8881e2aea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/67b2ba1a-6f74-4044-a48a-f0f8ad076b8f
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 3becf4fd-6055-a3e6-61e0-7c183d82e888
---

# Microsoft 365 Admin Center Usage Reports Overview - Microsoft 365 admin | Microsoft Learn

Check out [Microsoft 365 small business help](https://go.microsoft.com/fwlink/?linkid=2197659) on YouTube.

Microsoft 365 admin center usage reports provide insight into how people in your organization use Microsoft 365 for business services. For example, you can see who uses a service to the fullest extent and who barely uses it and might not need a Microsoft 365 license.

Note

Usage reports don't include perpetual license models.

Usage reports are generally available for the last 7, 30, 90, and 180 days. For details about specific report availability, see the individual usage report articles. Data doesn't exist for all reporting periods right away. The reports typically become available within 24 to 72 hours, but might sometimes take several days to become available.

## Watch: Act on a usage report in Microsoft 365

Check out this and other videos on our [YouTube channel](https://go.microsoft.com/fwlink/?linkid=2198103).

## Before you begin

To view usage reports, you must have one of the following permissions:

- Global Administrator 
    Important

    Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).
- Exchange Administrator
- SharePoint Administrator
- Usage Summary Reports Reader (with no user details). By default, this role has read access to user, groups, and other settings in the Microsoft 365 admin center, because the role is based on Microsoft Entra.
- Reports Reader
- Teams Administrator
- Teams Communications Administrator
- User Experience Success Manager (with no user details)
- AI Administrator

For more information, see [About admin roles](../add-users/about-admin-roles) and [Assign admin roles](../add-users/assign-admin-roles).

## View the Reports dashboard

::: moniker range="o365-21vianet"

Tip

If you're using Microsoft 365 operated by 21Vianet in China, use the following link to access the admin center: [https://portal.partner.microsoftonline.cn/](https://go.microsoft.com/fwlink/p/?linkid=513813)

::: moniker-end

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Reports**. If you don't see **Reports**, select **Show all**, and then select **Reports**.
3. Select [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756).
4. Select **View more** from the at-a-glance activity card for a service (such as email or OneDrive) to see the report details page. On that page, different reports for the service are provided in tabs.

    [![Screenshot of the Usage dashboard showing Microsoft 365 service activity cards and analytics.](../../media/activity-usage-analytics3.png)](../../media/4c0f966d-9d2b-4a6f-a106-a6e2b9a2de07.png#lightbox)

## Available usage reports in the Microsoft 365 admin center

Depending on your subscription, the following reports are available in all environments:

| Report | Public | GCC | GCC-High | DoD | Microsoft 365 operated by 21Vianet |
| --- | --- | --- | --- | --- | --- |
| [Active Users](active-users-ww) | Yes | Yes | Yes | Yes | Yes |
| [Microsoft browser usage](browser-usage-report) | Yes | N/A^1^ | N/A^1^ | N/A^1^ | N/A^1^ |
| [Microsoft Copilot readiness](microsoft-365-copilot-readiness) | Yes | N/A^1^ | N/A^1^ | N/A^2^ | N/A^2^ |
| [Microsoft Copilot usage](microsoft-365-copilot-usage) | Yes | Yes | Yes | Yes | N/A^2^ |
| [Microsoft Copilot Agent usage](microsoft-365-copilot-agents) | Yes | N/A^1^ | N/A^1^ | N/A^2^ | N/A^2^ |
| [Microsoft Copilot Chat usage](microsoft-copilot-usage) | Yes | Yes | Yes | Yes | N/A^2^ |
| [Microsoft 365 Copilot Connectors usage](microsoft-365-copilot-connectors-usage) | Yes | N/A^1^ | N/A^1^ | N/A^1^ | N/A^2^ |
| [Microsoft Copilot credits](microsoft-365-copilot-credits) | Yes | N/A | N/A | N/A | N/A |
| [Microsoft Copilot Search usage](microsoft-365-copilot-search-usage) | Yes | N/A^1^ | N/A^1^ | N/A^1^ | N/A^2^ |
| [Cowork usage](cowork-usage-report) | Yes | N/A^2^ | N/A^2^ | N/A^2^ | N/A^2^ |
| [Email activity](email-activity-ww) | Yes | Yes | Yes | Yes | Yes |
| [Email apps usage](email-apps-usage-ww) | Yes | Yes | Yes | Yes | Yes |
| [Mailbox usage](mailbox-usage) | Yes | Yes | Yes | Yes | Yes |
| [Microsoft 365 Groups](office-365-groups-ww) | Yes | Yes | Yes | Yes | Yes |
| [Microsoft 365 Apps usage](microsoft365-apps-usage-ww) | Yes | Yes | N/A^1^ | N/A^1^ | Yes |
| [Office activations](microsoft-office-activations-ww) | Yes | Yes | Yes | Yes | Yes |
| [OneDrive user activity](onedrive-for-business-activity-ww) | Yes | Yes | Yes | Yes | Yes |
| [OneDrive usage](onedrive-for-business-usage-ww) | Yes | Yes | Yes | Yes | Yes |
| [SharePoint site usage](sharepoint-site-usage-ww) | Yes | Yes | Yes | Yes | Yes |
| [SharePoint activity](sharepoint-activity-ww) | Yes | Yes | Yes | Yes | Yes |
| [SharePoint storage](sharepoint-storage-reports) | Yes | Yes | Yes | Yes | Yes |
| [Microsoft Teams user activity](microsoft-teams-user-activity-preview) | Yes | Yes | Yes | Yes | N/A^1^ |
| [Microsoft Teams device usage](microsoft-teams-device-usage-preview) | Yes | Yes | Yes | Yes | N/A^1^ |
| [Microsoft Teams team activity](microsoft-teams-usage-activity) | Yes | Yes | Yes | Yes | N/A^1^ |
| [Viva Engage activity](viva-engage-activity-report-ww) | Yes | Yes | N/A^2^ | N/A^2^ | N/A^2^ |
| [Viva Engage device usage](viva-engage-device-usage-report-ww) | Yes | Yes | N/A^2^ | N/A^2^ | N/A^2^ |
| [Viva Engage groups activity](viva-engage-groups-activity-report-ww) | Yes | Yes | N/A^2^ | N/A^2^ | N/A^2^ |
| [Forms activity](forms-activity-ww) | Yes | Yes | N/A^1^ | N/A^1^ | N/A^1^ |
| [Dynamics 365 Customer Voice activity](forms-pro-activity-ww) | Yes | Yes | N/A^2^ | N/A^2^ | N/A^2^ |
| [Skype for Business Online activity](/en-us/SkypeForBusiness/skype-for-business-online-reporting/activity-report) | N/A^2^ | N/A^2^ | N/A^2^ | N/A^2^ | N/A^2^ |
| [Skype for Business Online conference organized activity](/en-us/SkypeForBusiness/skype-for-business-online-reporting/conference-organizer-activity-report) | N/A^2^ | N/A^2^ | N/A^2^ | N/A^2^ | N/A^2^ |
| [Skype for Business Online conference participant activity](/en-us/SkypeForBusiness/skype-for-business-online-reporting/conference-participant-activity-report) | N/A^2^ | N/A^2^ | N/A^2^ | N/A^2^ | N/A^2^ |
| [Skype for Business Online peer-to-peer activity](/en-us/SkypeForBusiness/skype-for-business-online-reporting/peer-to-peer-activity-report) | N/A^2^ | N/A^2^ | N/A^2^ | N/A^2^ | N/A^2^ |
| [Viva Learning activity](viva-learning-activity) | Yes | N/A^2^ | N/A^2^ | N/A^2^ | N/A^2^ |
| [Viva Insights activity](viva-insights-activity) | Yes | Yes | N/A^1^ | N/A^1^ | N/A^2^ |
| [Planner activity](planner-activity) | Yes | Yes | Yes | Yes | N/A^2^ |
| [Project activity](project-activity) | Yes | Yes | N/A^1^ | N/A^1^ | N/A^2^ |
| [Visio activity](visio-activity) | Yes | Yes | N/A^1^ | N/A^1^ | N/A^2^ |
| [Viva Goals activity](viva-goals-activity) | Yes | N/A^2^ | N/A^2^ | N/A^2^ | N/A^2^ |

N/A^1^: The report will be released in the future. The [Microsoft 365 Roadmap](https://www.microsoft.com/microsoft-365/roadmap?filters=) will be updated before the release.

N/A^2^: The service isn't available in the environment; hence, there's no plan to release the report.

## View licensing information

To see how many licenses you assigned and unassigned, use the following steps:

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Billing** &gt; [Licenses](https://go.microsoft.com/fwlink/p/?linkid=842264).

To see who is licensed, unlicensed, or a guest, use the following steps:

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Users** &gt; [Active users](https://go.microsoft.com/fwlink/p/?linkid=834822).

## View usage information for a specific user

Use the service reports to research to what extent a specific user is using the service. For example, to find out how much mailbox storage a specific user consumed, open the Mailbox usage report, and sort the users by name. If you have thousands of users, export the report to Excel, Power BI, or use the Microsoft Graph reports API.

You can't generate a report where you enter a user's account and then get a list of which services they're using and how much.

New users sometimes display as **unknown**. This problem usually happens because of occasional delays in creating user profiles.

## Show user, group, or site details in usage reports

Reports provide information about your organization's usage data. By default, all reports hide user information such as usernames, display names, groups, and sites to help companies support local privacy laws.

By default, your user list looks like the following screenshot:

[![Screenshot of the anonymized user list.](../../media/2ed99bce-4978-4ee3-9ea2-4a8db26eef02.png)](../../media/2ed99bce-4978-4ee3-9ea2-4a8db26eef02.png#lightbox)

The organization setting that hides or shows this information applies to the following properties:

| Property | Attributes |
| --- | --- |
| Properties for user-level in many reports | User IDs, Usernames, and User principal names |
| Properties for OneDrive and SharePoint site usage reports | Site IDs and Site URLs |
| Properties for Microsoft 365 apps Group usage report | Group IDs and Group names |
| Properties for Viva Engage group usage report | Group name and Group admin |
| Properties for Teams team usage report | Team names |

Other reports, such as some reports in the Microsoft Teams admin center, follow this organization setting.

Global administrators can update the settings to display concealed information if your organization's privacy practices allow it.

Important

Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](/en-us/microsoft-365/admin/add-users/about-admin-roles).

It takes a few minutes for these changes to take effect. This setting also applies to the Microsoft 365 usage reports in [Microsoft Graph](/en-us/graph/api/resources/report) and [Power BI](/en-us/microsoft-365/admin/usage-analytics/usage-analytics) and to [the usage reports in Microsoft Teams Admin center](/en-us/microsoftteams/teams-analytics-and-reports/teams-reporting-reference). Showing identifiable user information is a logged event in the Microsoft Purview portal audit log.

### Use the Microsoft 365 admin center to show user, group, or site details

1. Go to the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339).
2. In the navigation menu, select **Settings**. If you don't see **Settings**, select **Show all**, and then select **Settings**.
3. Select [Org Settings](https://go.microsoft.com/fwlink/p/?linkid=2053743).
4. On the **Services** tab, select **Reports**.
5. In the **Reports** panel, uncheck the checkbox next to **Conceal user, group, and site names in all reports**.
6. Select **Save**.

### Use adminReportSettings to show user, group, or site details

Admins can use an API in all environments to change this setting without needing to visit the Microsoft 365 admin center. For more information, see [adminReportSettings resource type](/en-us/graph/api/resources/adminreportsettings?view=graph-rest-beta&amp;preserve-view=true).

Two methods are approved for this API:

[![Screenshot of the API methods to change settings without using the Microsoft 365 admin center.](../../media/api-show-details.png)](../../media/api-show-details.png#lightbox)

The report only contains a **Privacy Setting** property. For more information about Graph API, see [Use the Microsoft Graph API](/en-us/graph/use-the-api). You can use the Software Development Kit (SDK) or directly call the API by using any programming language with network ability, like [Graph Explorer](/en-us/graph/graph-explorer/graph-explorer-overview).

## What happens to usage data when I delete a user account?

When you delete a user account, Microsoft deletes that user's usage data within 30 days. The usage chart totals still include deleted users for the periods they were active, but they don't appear in the User Details table.

However, when you select a particular day (up to 28 days from the current date), the report shows the user's usage for that day in the User Details table.

## How do I interpret the last activity date in user, group, or site details in the usage reports?

The last activity date in user, group, or site details represents the most recent date on which a user performed any intentional activity within the app, regardless of the selected time period of the past 7, 30, 90, or 180 days.