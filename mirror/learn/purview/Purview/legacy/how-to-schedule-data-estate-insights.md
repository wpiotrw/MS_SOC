---
layout: Conceptual
title: Schedule Data Estate Insights report refresh | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-schedule-data-estate-insights
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article provides the steps to schedule your Data Estate Insights report refresh rate in the Microsoft Purview governance portal.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: suvirdi
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: how-to
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
locale: en-us
document_id: bb2fc473-bf62-26a8-cfe9-1c2aef8acfb4
document_version_independent_id: bb2fc473-bf62-26a8-cfe9-1c2aef8acfb4
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-schedule-data-estate-insights.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-schedule-data-estate-insights
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-schedule-data-estate-insights.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: e4442774-b3bd-ac76-2eb7-5ac5cec2750f
---

# Schedule Data Estate Insights report refresh | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Microsoft Purview Data Estate Insights automatically creates reports that help you to identify governance gaps in your data estate. However, you can set the schedule for this automatic refresh to fit your reporting patterns and needs. In this article, we'll describe how you can schedule your refresh and what options are available.

If you would like to disable Data Estate Insights for a time, you can follow our article to [disable Data Estate Insights](../disable-data-estate-insights).

Important

The Data Estate Insights application is **on** by default when you create a Microsoft Purview account.

**Refresh Schedule** is set to a weekly refresh that begins 7 days after the account is created.

As the Data Map is populated and curated, Insights App shows data in the reports. The reports are ready for consumption to anyone with Insights Reader role.

## Permissions needed

To update the report refresh schedule for Data Estate Insights, you need **[data curator permissions](../data-gov-classic-permissions#roles) on the [root collection](../data-governance-glossary)**.

## How to update the refresh schedule

Important

Report refresh rate does impact your billing.

1. If you're using the [Microsoft Purview portal](../purview-portal), the schedule can't be changed; all classic reports are set to refresh weekly by default. Classic reports in the new Microsoft Purview don't impact your billing.
2. In the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/), go to the **Management** section.

    ![Screenshot of the Microsoft Purview governance portal Management section highlighted.](../media/how-to-schedule-data-estate-insights/locate-management.png)
3. Then select **Overview**.
4. In the **Insights refresh** menu, locate Data Estate Insights, and select the **Edit** pencil. For more information about the insights refresh menu, see the insights refresh menu section below.

    Note

    If the State is currently set to **Off** you need to first turn it **On** before you can update the refresh schedule.

    ![Screenshot of the Overview window in the Management section of the Microsoft Purview governance portal with the refresh frequency dropdown highlighted for Data Estate Insights feature options.](../media/how-to-schedule-data-estate-insights/refresh-frequency.png)
5. In the **Edit** menu, select **Recurring**.
6. Then select your time zone, set your recurrence to **Month(s)**, **Weeks(s)**, or **Days(s)**, select your day and time to run, specify a start time, and optionally specify an end time. For more information about the schedule options, see the schedule options section below.

    ![Screenshot of the Data Estate Insights edit page, with the Recurring radio button highlighted and set to Recurring.](../media/how-to-schedule-data-estate-insights/set-recurrance.png)
7. Select **Continue**. If prompted, review the updates and select **Save**.
8. Now you can see your schedule is set. Selecting **More info** in the schedule columns give you the recurrence details.

    ![Screenshot of the management page, with the Data Estate Insights information row highlighted.](../media/how-to-schedule-data-estate-insights/schedule-set.png)

## Does the refresh schedule affect billing?

Yes. You're billed when Microsoft Purview Data Estate Insights checks for updates in your environment and when a report is generated.

1. A check for updates to your Microsoft Purview instance is made at your scheduled report refresh time. You'll always be billed for this check at your report refresh time.
2. If updates have been made, you'll be billed to generate your insights report. If no updates were made since the last report, you'll not be billed to generate a report.

    Note

    An asset is considered to be **updated** if it's updated in Microsoft Purview. An update in Microsoft Purview means a change in the following properties: asset name, description, schema, classifications, experts, owners, etc. New rows in a data asset and a re-scan won't result in an update to your insights reports if the metadata properties haven't changed.

For more information about billing for Data Estates Insights, see our [pricing guidelines](../concept-guidelines-pricing-data-estate-insights).

## Schedule options

Below are listed all the schedule options currently available when you modify your refresh schedule:

- Recurring or off
- Time zone
- Recurrence
- Start at
- End date (optional)

### Recurring or off

- **Recurring** - your Data Estate Insights report refreshes on the recurrence schedule you specify below, based on the time zone you indicate.
- **Off** - your Data Estate Insights reports will no longer refresh information, but the current reports remain available. For more information, see our [disable Data Estate Insights article.](../disable-data-estate-insights#disable-report-refresh)

    ![Screenshot of the Edit refresh page recurrence and off options, showing recurrence selected.](../media/how-to-schedule-data-estate-insights/recurring-off.png)

### Time zone

Select the time zone you'd like to align your refresh schedule with. If the time zone you select observes daylight savings, your trigger auto-adjusts for the difference.

![Screenshot of the Edit refresh page time zone options, showing the time set to Pacific Standard.](../media/how-to-schedule-data-estate-insights/time-zone.png)

### Recurrence

You can select a daily, weekly, or monthly refresh recurrence.

Important

No matter what you set your refresh recurreance to, Data Estate Insights run a check before refreshing to see if any updates have been made to the assets. If no update has been made, the reports won't refresh.

An asset is considered to be **updated** only if it is updated in Microsoft Purview. An update in Microsoft Purview means a change in the following properties: asset name, description, schema, classifications, experts, owners, etc... New rows in a data asset and a re-scan won't result in an update to your insights reports if the metadata properties of the asset have not changed.

- **Daily recurrence** - schedule daily recurrence by setting recurrence to every (1-5) days, and choosing the time of day you would like to refresh the report. For example, the below report refreshes every other day at 12 AM UTC.

    ![Screenshot of the Edit refresh page recurrence options, showing a daily recurrence set.](../media/how-to-schedule-data-estate-insights/daily-recurrence.png)
- **Weekly recurrence** - schedule weekly recurrence by setting recurrence to every (1-5) weeks, and choosing the day of the week and time of day you would like to refresh the report. For example, the below report refreshes on Monday every two weeks, at six AM.

    ![Screenshot of the Edit refresh page recurrence options, showing a weekly recurrence set.](../media/how-to-schedule-data-estate-insights/weekly-recurrence.png)
- **Monthly recurrence** - schedule monthly recurrence by setting recurrence to every (1-5) months, and choosing the day of the month and time of day you would like to refresh the report. Choose **Last** to always run on the last day of the month, and **1** to always run on the first day of the month. For example, the below report refreshes on the last day of every month at five PM.

    ![Screenshot of the Edit refresh page recurrence options, showing a monthly recurrence set.](../media/how-to-schedule-data-estate-insights/monthly-recurrence.png)

Set **Scan at this time** to the time of day you'd like to begin your refresh.

Tip

The time you select will be the time that the report begins its refresh. Microsoft Purview will adjust compute for the amount of data being aggregated, but **schedule your recurrence a little before you will need the report** so the report has time to fully refresh and will be ready.

### Start at

The **Start at** option allows you to set when your reports will begin their refresh schedule, and is relative to the time zone you selected. Set it for the current date and time to set the schedule immediately.

![Screenshot of the Edit refresh page start at option, showing a date and time selected.](../media/how-to-schedule-data-estate-insights/start-at.png)

### Specify an end date

If you want your reports to stop refreshing after a certain amount of time, you can enable this option by selecting the check box and providing an end date. For example: a monthly recurrence schedule refreshing on the first of the month with the below end date would refresh on September 1 2023, and wouldn't refresh again in October.

![Screenshot of the Edit refresh page specify an end date option, with the option selected and the date selected.](../media/how-to-schedule-data-estate-insights/specify-an-end-date.png)

## Insights refresh menu

In the management menu of the Microsoft Purview governance portal, you'll find the Insights refresh menu that lets you set your Data Estate Insights report availability. Here's all the information you can find there:

| Feature | State | Schedule | Configuration date | Edit |
| --- | --- | --- | --- | --- |
| Lists the feature your settings are for | Either **On** or **Off**. For more information about turning off reports, see our [disable Data Estate Insights article.](../disable-data-estate-insights#disable-report-refresh) | Select **More info** to see your recurrence schedule, start time, and end time. | The day your recurrence schedule was last set. By default this will be the creation date of your Microsoft Purview account. | Allows you to update your recurrence schedule when reports are turned on. |

![Screenshot of the insights refresh menu.](../media/how-to-schedule-data-estate-insights/insights-refresh-menu.png)