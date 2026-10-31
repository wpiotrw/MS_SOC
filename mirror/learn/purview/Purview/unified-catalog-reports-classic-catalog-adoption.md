---
layout: Conceptual
title: Classic Catalog Adoption Report in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-reports-classic-catalog-adoption
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-01-14T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn about the classic catalog adoption report in Microsoft Purview, and how it can be used to govern and manage your data estate.
locale: en-us
document_id: f6a18734-2f07-5e4b-fc93-d307e13a5bb9
document_version_independent_id: f6a18734-2f07-5e4b-fc93-d307e13a5bb9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-reports-classic-catalog-adoption.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-reports-classic-catalog-adoption
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-reports-classic-catalog-adoption.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: c3032929-46ca-7b47-eeba-8636e92814b8
---

# Classic Catalog Adoption Report in Unified Catalog | Microsoft Learn

As described in the [insights concepts](concept-insights), the catalog adoption report is part of the "Health" section of classic Microsoft Purview Data Estate Insights. This report offers a one-stop shop experience for administrators to determine if and how the classic Microsoft Purview Data Catalog is being used. It helps answer questions like:

- What are my users searching for?
- How many people used the catalog last month?
- What are the most used data assets?

## Prerequisites

Before getting started with Data Estate Insights, make sure that you complete the following steps:

- Set up a storage resource and populate the account with data.
- Set up and complete a scan of your storage source. For more information about creating and completing a scan, see [manage data sources in Microsoft Purview](data-map-data-sources-register-manage).
- Have the right permissions depending on your current experience:
    - [If using the classic Microsoft Purview Data Catalog](use-microsoft-purview-governance-portal), you need the [data curator role or insight reader role](data-gov-classic-permissions#roles).
    - [If using the new Microsoft Purview Unified Catalog](unified-catalog), you need [data health reader](data-governance-roles-permissions#unified-catalog-permissions) permissions.

## Understand your data estate and catalog health in Data Estate Insights

In Data Estate Insights, you can get an overview of all assets inventoried in the Data Map, and any key gaps that governance stakeholders can close for better governance of the data estate.

1. Open the Microsoft Purview portal.
2. If you're using the [classic Microsoft Purview portal](use-microsoft-purview-governance-portal), select **Data estate insights**. If you're using the [new Microsoft Purview portal](purview-portal) open **Unified Catalog**, select **Health Management**, then select **Reports**.
3. Select **Classic catalog adoption**.

## View catalog adoption dashboard

The catalog adoption dashboard has several curated tiles and charts to identify:

- How many active users your catalog had in the last month.
- How many total searches were performed in the last month.
- Which catalog features are being used.
- Most viewed assets.
- Top searched keywords in catalog.

[![Screenshot of the catalog adoption dashboard page.](media/catalog-adoption-insights/catalog-adoption-page-inline.png)](media/catalog-adoption-insights/catalog-adoption-page-large.png#lightbox)

### Monthly active users

The **Monthly active users** count is the number of unique users who perform any action, such as search, browse, or curation.

The **Monthly active users** tile shows how many users took at least one action in the catalog in the last 30 days. An action in the catalog includes searching for a term, browsing in the catalog, and updating an asset in the catalog. This tile also includes an indicator of a percentage increase or decrease in users from the previous month.

### Total searches

The **Total searches** tile shows a count of all searches performed in the catalog over the last 30 days. The tile also shows the percentage increase or decrease in the number of searches from the previous month.

### Active users by feature category

The **Active users by feature category** chart helps you monitor user activity trends in the catalog. Here's an example of the chart:

![Screenshot of the Active users by feature category table, showing the daily date range selected and a line graph of activity.](media/catalog-adoption-insights/active-users-by-feature-category.png)

At the top of the chart, select your date range to view user activity on a daily, weekly, or monthly basis.

The chart shows the number of users in the date range who perform actions in one of three categories:

- **Search and browse**: The count of users per action category (search or browse). A user may appear in both counts if they perform both actions. For example, if a user performs both search and browse, the same user is counted twice in this number (once under search, once under browse). One user can contribute two counts in Search/Browse, but still counts as one in Monthly Active Users. This is why **Search and browse** can be higher than **Monthly active users**.
- **Asset curation**: The count of users who performed at least any one of these actions on an asset:

    - Added, removed, or updated a rating
    - Added or removed a tag
    - Added or removed a glossary term
    - Added or removed a classification
    - Edited an asset's name or description
    - Added or removed a certification
    - Added or removed a column level classification, glossary term, description, name, or data type
    - Added or removed manual lineage
    - Added or removed a contact
- **All**: The count of users who performed both a search or browse action, *and* at least one asset curation action within the date range.

### Most viewed assets

The most viewed assets table shows the top assets in the catalog, by sum of views in the last 30 days.

![Screenshot of the Most viewed assets table, showing the top five viewed assets, their curation status, and the number of views in the last month.](media/catalog-adoption-insights/most-viewed-assets.png)

This table allows you to select through to your most viewed assets for more information, but the table also provides these other details:

- Curation status - There are three possible statuses: **Fully curated**, **Partially curated**, and **Not curated**, based on certain attributes of assets being present. An asset is **Fully curated** if it has at least one classification tag, an assigned Data Owner, and a description. If any of these attributes is missing, but not all, then the asset is categorized as **Partially curated** and if all of them are missing, then it's **Not curated**. For more information about the curation status of your data assets, see the [data stewardship dashboard](unified-catalog-reports-classic-data-stewardship).
- Views - count of the number of views the asset received in the last 30 days.

### Top searched keywords

The top searched keywords table shows your top keywords both for searches that produced results, and searches that didn't. That way you can know what users are finding with the catalog, and what they're still looking for.

![Screenshot of the Top searched keywords table, showing the top searched keywords with search results.](media/catalog-adoption-insights/top-searched-keywords.png)

At the top of the table, you can select one of the two radio buttons to select whether to show keywords for searches with results, or searches without results.

You can select any of the keywords to run the search in the catalog and see the results for yourself as well.

The table also provides search volume, which is the number of times that keyword was searched in the last 30 days.

### Report generated timestamp

The timestamp displayed, such as, "Report generated on December 4, 2025 at 11:37 AM", indicates when the page was loaded or refreshed. It doesn't represent the time when the backend actually computed the KPI data. The actual calculation time comes from the backend timePoint field (for example, 2025-11-05T06:59:48) from the API response.

### Monthly aggregation behavior for usage metrics

The **Monthly active users** and **Total searches** metrics display data from the previous fully completed month. For example, December views show November data. The KPI is updated during the job run after the month changes, even though the job runs every week.