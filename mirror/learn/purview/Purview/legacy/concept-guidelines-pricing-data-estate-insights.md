---
layout: Conceptual
title: Pricing guidelines for the classic Data Estate Insights | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/concept-guidelines-pricing-data-estate-insights
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article provides a guideline to understand pricing for the classic Data Estate Insights components of Microsoft Purview in the classic Microsoft Purview governance portal.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: suvirdi
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: article
ms.date: 2024-07-09T00:00:00.0000000Z
ms.custom: ignite-fall-2021
locale: en-us
document_id: 20b42134-e78b-dc9a-b03e-cf095f450775
document_version_independent_id: 20b42134-e78b-dc9a-b03e-cf095f450775
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/concept-guidelines-pricing-data-estate-insights.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/concept-guidelines-pricing-data-estate-insights
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/concept-guidelines-pricing-data-estate-insights.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 80dc4f4a-127e-f454-eac9-1b81f8e60e85
---

# Pricing guidelines for the classic Data Estate Insights | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

This guide covers pricing guidelines for the classic Data Estate Insights features in the classic [Microsoft Purview governance portal](../use-microsoft-purview-governance-portal).

Tip

There's a [new data estate health experience](../unified-catalog-data-health-management) in the new Microsoft Purview Data Catalog.

For a full pricing guideline details for classic data governance solutions in Microsoft Purview, see the [pricing guideline overview.](../data-gov-classic-pricing)

For specific price details, see the [classic data governance solutions in Microsoft Purview pricing page](https://azure.microsoft.com/pricing/details/purview/). This article guides you through the features and factors that affect pricing for Data Estate Insights.

## Guidelines

Data Estate Insights in the classic Microsoft Purview governance portal is billed on two dimensions:

- **Report generation** - this incorporates the job that checks for any changes in your environment and the jobs that aggregate metrics about your Microsoft Purview account that will appear in specific reports.

    - If you have [set your reports to refresh on a schedule](../how-to-schedule-data-estate-insights), at the time of refresh there will be a job to check if any updates have been made to your environment. You'll always be billed a small amount for this check.
    - If updates have been made to your environment, you're billed for the jobs that aggregate metrics and generate your report.

    Note

    On the [pricing page](https://azure.microsoft.com/pricing/details/purview/), you can find details for report generation pricing under Data Map Enrichment. ![Screenshot of the pricing page headers, showing Data Map Enrichment selected.](../media/concept-guidelines-pricing/data-map-enrichment.png)
- **Report consumption** - This incorporates access of the report features (currently served through the UX). On the [pricing page](https://azure.microsoft.com/pricing/details/purview/), you can find details for report generation pricing under Data Estate Insights. ![Screenshot of the pricing page headers, showing Data Estate Insights selected.](../media/concept-guidelines-pricing/data-estate-insights.png)

Important

The Data Estate Insights application is **on** by default when you create a Microsoft Purview account. This means, “State” is on and “Refresh Frequency” is set to automatic\*.

\* At this time automatic refresh is weekly.

If you want to reschedule or reduce how often your reports are refreshed, you can [schedule your Data Estate Insights reports](../how-to-schedule-data-estate-insights).

If you don't plan on using Data Estate Insights for a while, a **[data curator](../data-gov-classic-permissions#roles) on the [root collection](../data-governance-glossary)** can disable Data Estate Insights features in one of two ways:

- Disable the Data Estate Insights application - this stops billing from both report generation and report consumption.
- Disable report refresh - [insights readers](../data-gov-classic-permissions#roles) have access to current reports, but reports won't be refreshed. Billing occurs for report consumption but not report generation.

Note

The application or report refresh can be enabled again later at any time.

A **[data curator](../data-gov-classic-permissions#roles) on your account's [root collection](../data-governance-glossary)** can make these changes in the Management section of the Microsoft Purview governance portal in **Overview**, under **Feature options**. For specific steps, see the [disable Data Estates Insights article](../disable-data-estate-insights)

![Screenshot of the Overview window in the Management section of the Microsoft Purview governance portal. Under feature options, the data estate insights option is highlighted.](../media/concept-guidelines-pricing/disable-data-estate-insights.png)

### Schedule Report Refresh

Your reports can be scheduled to refresh daily, weekly, or monthly depending on your needs, and this will affect billing.

Firstly, on the date/time of your scheduled refresh, insights runs a job to check if any changes have been made in your environment since the last refresh. You'll always be billed for this job.

If changes have been made since the last report refresh, billing is calculated based on the amount of compute power that is used to generate the report, and is billed at the time of report generation. For more information about specific pricing, see the [pricing page](https://azure.microsoft.com/pricing/details/purview/)**under Data Map Enrichment.**

For more information about setting your refresh schedule, see [the schedule Data Estate Insights reports article](../how-to-schedule-data-estate-insights).

### Disable the Data Estate Insights application

Disabling Data Estate Insights disables the entire application, including these reports:

- Stewardship
- Asset
- Glossary
- Classification
- Labeling

The application icon will still show in the menu, but insights readers won't have access to reports at all, and report generation jobs are stopped. The Microsoft Purview account won't receive any bill for Data Estate Insights.

For steps to disable the Data Estate Insights application, see the [disable article.](../disable-data-estate-insights#disable-the-data-estate-insights-application)

### Disable report refresh

You can choose to disable report refreshes instead of disabling the entire Data Estate Insights application.

When you disable report refreshes, insight readers will be able view reports but they'll see a banner on top of each report, warning that the report might not be current. It will also indicate the date the report was last generated.

In this case, graphs showing data from last 30 days will appear blank after 30 days. Graphs showing snapshot of the data map will continue to show graph and details. When an [insights readers](../data-gov-classic-permissions#roles) accesses an insight report, report consumption meter will be triggered, and the Microsoft Purview account will be billed.

For steps to disable report refresh see the [disable article.](../disable-data-estate-insights#disable-report-refresh)