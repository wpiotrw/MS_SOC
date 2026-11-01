---
layout: Conceptual
title: Disable Data Estate Insights | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/disable-data-estate-insights
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article provides the steps to disable or enable Data Estate Insights in the Microsoft Purview governance portal.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: suvirdi
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: how-to
ms.date: 2023-10-04T00:00:00.0000000Z
locale: en-us
document_id: 0033aedf-9329-e5ca-31a6-9e68710f5541
document_version_independent_id: 0033aedf-9329-e5ca-31a6-9e68710f5541
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/disable-data-estate-insights.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/disable-data-estate-insights
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/disable-data-estate-insights.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 013fdac8-8fad-2e1e-d694-1233a3e1f773
---

# Disable Data Estate Insights | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Microsoft Purview Data Estate Insights automatically aggregates metrics and creates reports about your Microsoft Purview account and your data estate. When you scan registered sources and populate your Microsoft Purview Data Map, the Data Estate Insights application automatically identifies governance gaps and highlights them in its top metrics. It also provides drill-down experience that enables all stakeholders, such as data owners and data stewards, to take appropriate action to close the gaps.

These features are optional and can be enabled or disabled at any time. This article provides the specific steps required to enable or disable Microsoft Purview Data Estate Insights features.

To reschedule without disabling, see [the article to schedule Data Estate Insights reports](../how-to-schedule-data-estate-insights).

Important

The Data Estate Insights application is **on** by default when you create a Microsoft Purview account.

**State** is set to On.

**Refresh Schedule** is set to a weekly refresh that begins 7 days after the account is created.

As the Data Map is populated and curated, Insights App shows data in the reports. The reports are ready for consumption to anyone with Insights Reader role.

If you don't plan on using Data Estate Insights for a time, a **[data curator](../data-gov-classic-permissions#roles) on the [root collection](../data-governance-glossary)** can disable the Data Estate Insights in one of two ways:

- Disable the Data Estate Insights application - this will stop billing from both report generation and report consumption.
- Disable report refresh - Insights readers have access to current reports, but reports won't be refreshed. Billing will occur for report consumption but not report generation.

Steps for both methods, and for re-enablement, are below.

For more information about billing for Data Estates Insights, see our [pricing guidelines](../concept-guidelines-pricing-data-estate-insights).

## Disable the Data Estate Insights application

Note

To be able to disable this application, you will need to have the [data curator role](../data-gov-classic-permissions#roles) on your account's [root collection.](../data-governance-glossary)

Disabling Data Estate Insights will disable the entire application, including these reports:

- Stewardship
- Asset
- Glossary
- Classification
- Labeling

The application icon will still show in the menu, but insights readers won't have access to reports at all, and report generation jobs will be stopped. The Microsoft Purview account won't receive any bill for Data Estate Insights.

To disable the Data Estate Insights application, a user with the [data curator role](../data-gov-classic-permissions#roles) at the [root collection](../data-governance-glossary) can follow these steps:

1. If you're using the [Microsoft Purview portal](../purview-portal), the schedule can't be changed; all classic reports are set to refresh weekly by default. Classic reports in the new Microsoft Purview don't impact your billing.
2. In the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/), go to the **Management** section.

    ![Screenshot of the Microsoft Purview governance portal left menu, with the Management section highlighted and overview shown selected in the next menu.](../media/disable-data-estate-insights/locate-management.png)
3. Then select **Overview**.
4. In the **Feature options** menu, locate Data Estate Insights, and select the **State** toggle to change it to **Off**.

    ![Screenshot of the Overview window in the Management section of the Microsoft Purview governance portal with the State toggle highlighted for Data Estate Insights feature options.](../media/disable-data-estate-insights/disable-option.png)

Once you have disabled Data Estate Insights, the icon will still appear in the left hand menu, but users will receive a warning stating that the application has been disabled when attempting to access it.

![Screenshot of the Data Estate Insights section with Data Estate Insights disabled, showing no reports, and a message to contact your Data Curator to reinstate the reports.](../media/disable-data-estate-insights/disabled-warning.png)

## Disable report refresh

Note

To be able to disable or edit report refresh, you will need to have the [data curator role](../data-gov-classic-permissions#roles) on your account's [root collection.](../data-governance-glossary)

You can choose to disable report refreshes instead of disabling the entire Data Estate Insights application. When you disable report refreshes, users with the [insights reader role](../data-gov-classic-permissions#roles) will still be able view reports, but they'll see warning at the top of each report indicating that the data may not be current and the date of the last refresh.

Graphs that show data from the last 30 days will appear blank after 30 days while graphs showing snapshot of the data map will continue to show graphs and details.

![Screenshot of the report warning popup on the Data stewardship report insights page with the Report generated on date text highlighted.](../media/disable-data-estate-insights/report-warning.png)

To disable the Data Estate Insights report refresh, a user with the [data curator role](../data-gov-classic-permissions#roles) at the [root collection](../data-governance-glossary) can follow these steps:

1. In the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/), go to the **Management** section.

    ![Screenshot of the Microsoft Purview governance portal left menu, with the Management section highlighted.](../media/disable-data-estate-insights/locate-management.png)
2. Then select **Overview**.
3. In the **Insights refresh** menu, locate Data Estate Insights and select the **Edit pencil**

    ![Screenshot of the Overview window in the Management section of the Microsoft Purview governance portal with the edit pencil in the Data Estate Insights row highlighted.](../media/disable-data-estate-insights/disable-data-estate-insights.png)
4. Select the **Off** radio button and select **Continue**. If prompted, review your edits and select **Save.**

    ![Screenshot of the Data Estate Insights edit page, with the Recurring radio button highlighted and set to Off.](../media/disable-data-estate-insights/disable-recurrance.png)
5. You can now see under the **Schedule** column, the refresh schedule reads as **Disabled**.

## Re-enable Data Estate Insights and report refresh

Note

To enable Data Estate Insights, enable report refresh, or edit report refresh, you will need to have the [data curator role](../data-gov-classic-permissions#roles) on your account's [root collection.](../data-governance-glossary)

If Data Estate Insights or report refresh has been disabled in your Microsoft Purview governance portal environment, a user with the [data curator role](../data-gov-classic-permissions#roles) at the [root collection](../data-governance-glossary) can re-enable either at any time by following these steps:

1. In the [Microsoft Purview governance portal](https://web.purview.azure.com/resource/), go to the **Management** section.

    ![Screenshot of the Microsoft Purview governance portal Management section highlighted.](../media/disable-data-estate-insights/locate-management.png)
2. Then select **Overview**.
3. In the **Insights refresh** menu, locate Data Estate Insights, and select the **Edit** pencil.

    ![Screenshot of the Overview window in the Management section of the Microsoft Purview governance portal with the refresh frequency dropdown highlighted for Data Estate Insights feature options.](../media/disable-data-estate-insights/refresh-frequency.png)
4. In the **Edit** menu, select **Recurring**.
5. Then select your time zone, set your recurrence to **Month(s)** or **Weeks(s)**, select your day and time to run, specify a start time, and optionally specify an end time. For more information about the available options, see [the article to schedule Data Estate Insights reports](../how-to-schedule-data-estate-insights).

    ![Screenshot of the Data Estate Insights edit page, with the Recurring radio button highlighted and set to Recurring.](../media/disable-data-estate-insights/set-recurrance.png)
6. Select **Continue**. If prompted, review the updates and select **Save**.
7. Now you can see your schedule is set. Selecting **More info** in the schedule columns will give you the recurrence details.

    ![Screenshot of the management page, with the Data Estate Insights information row highlighted.](../media/disable-data-estate-insights/schedule-set.png)