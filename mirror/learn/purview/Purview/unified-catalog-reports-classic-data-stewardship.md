---
layout: Conceptual
title: Classic Data Stewardship Report in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-reports-classic-data-stewardship
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2025-04-15T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn about the data stewardship report in Microsoft Purview, and how it can be used to govern and manage your data estate.
locale: en-us
document_id: a164b2b6-e3a9-247d-874d-bdff2dea789d
document_version_independent_id: a164b2b6-e3a9-247d-874d-bdff2dea789d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-reports-classic-data-stewardship.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-reports-classic-data-stewardship
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-reports-classic-data-stewardship.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: eea8be9d-626e-9f17-7260-ecb1d6bed995
---

# Classic Data Stewardship Report in Unified Catalog | Microsoft Learn

As described in the [insights concepts](concept-insights), the data stewardship report is part of the "Health" section of Data Estate Insights. This report offers a one-stop shop experience for data, governance, and quality focused users like chief data officers and data stewards to get actionable insights into key areas of gap in their data estate.

In this guide, you learn how to:

- Navigate and view data stewardship report from your Microsoft Purview account.
- Drill down for more asset count details.

## Prerequisites

Before getting started with Data Estate Insights, make sure that you complete the following steps:

- Set up a storage resource and populate the account with data.
- Set up and complete a scan your storage source. For more information on how to create and complete a scan, see [Manage data sources in Microsoft Purview](data-map-data-sources-register-manage).
- Permissions depending on your current experience:
    - [If using the classic Microsoft Purview Catalog](use-microsoft-purview-governance-portal), you need the [data curator role or insight reader role](data-gov-classic-permissions#roles).
    - [If using the new Microsoft Purview Unified Catalog](unified-catalog), you need [data health reader](data-governance-roles-permissions#unified-catalog-permissions) permissions.

## Understand your data estate and catalog health in Data Estate Insights

In Data Estate Insights, you can get an overview of all assets inventoried in Data Map, and any key gaps that governance stakeholders can close for better governance of the data estate.

1. Open the Microsoft Purview portal.
2. If you're using the [classic Microsoft Purview portal](use-microsoft-purview-governance-portal), select **Data estate insights**. If you're using the [new Microsoft Purview portal](purview-portal) open **Unified Catalog**, select **Health Management**, then select **Reports**.
3. Select **Classic data stewardship**.

## View data stewardship dashboard

The dashboard is purpose-built for governance and quality-focused users, like data stewards and chief data officers, to understand the health management of their organization. The dashboard shows high-level KPIs that help reduce governance risks:

- **Asset curation**: The dashboard categorizes all data assets into three areas: "Fully curated," "Partially curated," and "Not curated," based on certain attributes of assets being present. An asset is "Fully curated" if it has at least one classification tag, an assigned data owner, and a description. If any of these attributes is missing, but not all, then the asset is categorized as "Partially curated" and if all of them are missing, then it's "Not curated."
- **Asset data ownership**: The dashboard categorizes assets that have the owner attribute within the "Contacts" tab as blank as "No owner". Otherwise, it categorizes them as "Owner assigned".

    [![Screenshot of the data stewardship insights summary graphs, showing the three main KPI charts.](media/data-stewardship/kpis-small.png)](media/data-stewardship/data-stewardship-kpis-large.png#lightbox)

### Health management

Health management is a scorecard view that helps management and governance focused users, like chief data officers, understand critical governance metrics that can be looked at by collection hierarchy.

[![Screenshot of the data stewardship health management table in the middle of the dashboard.](media/data-stewardship/data-estate-health-small.png)](media/data-stewardship/data-estate-health-large.png#lightbox)

You can view the following metrics:

- **Assets**: Count of assets by collection drill-down.
- **With sensitive classifications**: Count of assets with any system classification applied.
- **Fully curated assets**: Count of assets that have a data owner, at least one classification, and a description.
- **Owner assigned**: Count of assets with data owner assigned on them.
- **No classifications**: Count of assets with no classification tag.
- **Out of date**: Percentage of assets that haven't been updated in over 365 days.
- **New**: Count of new assets pushed in the Data Map in the last 30 days.
- **Updated**: Count of assets updated in the Data Map in the last 30 days.
- **Deleted**: Count of deleted assets from the Data Map in the last 30 days.

You can also drill down by collection paths. As you hover on each column name, it provides description of the column, provides recommended percentage ranges, and takes you to the detailed graph for further drill-down.

![Screenshot of the data stewardship health management table, with the fully curated column hovered over. A summary is show, and the view more in Stewardship insights option is selected.](media/data-stewardship/hover-menu.png)

![Screenshot of the asset curation detailed view, as shown after selecting the view more in stewardship insights option is selected.](media/data-stewardship/detailed-view.png)

### Asset curation

The system categorizes all data assets into three areas: **Fully curated**, **Partially curated**, and **Not curated**, based on whether assets have certain attributes.

[![Screenshot of the data stewardship insights health dashboard, with the asset curation bar chart highlighted.](media/data-stewardship/asset-curation-small.png)](media/data-stewardship/asset-curation-large.png#lightbox)

An asset is ***Fully curated*** if it has at least one classification tag, an assigned data owner, and a description.

If an asset is missing any of these attributes, but not all, the system categorizes it as **Partially curated**. If an asset is missing all of these attributes, the system lists it as **Not curated**.

You can drill down by collection hierarchy.

![Screenshot of the data stewardship asset curation chart, with the collection filter opened to show all available collections.](media/data-stewardship/asset-curation-collection-filter.png)

For further information about which assets aren't fully curated, you can select **View details** link that takes you into the deeper view.

![Screenshot of the data stewardship asset curation chart, with the view details button highlighted below the chart.](media/data-stewardship/asset-curation-view-details.png)

In the **View details** page, if you select a specific collection, it lists all assets with attribute values or blanks that make up the ***fully curated*** assets.

![Screenshot of the asset curation detailed view, shown after selecting View Details beneath the asset curation chart.](media/data-stewardship/asset-curation-select-collection.png)

The detail page shows two key pieces of information:

First, it tells you what the ***classification source*** is, if the asset is classified. It's **Manual** if a curator or data owner applies the classification manually. It's **Automatic** if the system classifies the asset during scanning. This page only provides the last applied classification state.

Second, if an asset is unclassified, it tells us why it's not classified, in the column ***Reasons for unclassified***. Currently, Data Estate Insights can provide one of the following reasons:

- No match found
- Low confidence score
- Not applicable

![Screenshot of the collection detail view, with the classification source and reasons for unclassified columns highlighted.](media/data-stewardship/collection-detail-view-columns.png)

You can select any asset and add missing attributes, without leaving the **Data estate insights** app.

![Screenshot of the asset list page, with an asset selected and the edit menu open.](media/data-stewardship/edit-asset.png)

### Trends and gap analysis

This graph shows how the assets and key metrics have been trending over different time periods:

- Last 30 days: The graph uses the last run of the day or the recording of the last run across days as a data point.
- Last six weeks: The graph uses the last run of the week, with the week ending on Sunday. If there's no run on Sunday, the graph uses the last recorded run.
- Last 12 months: The graph uses the last run of the month.
- Last four quarters: The graph uses the last run of the calendar quarter.

[![Screenshot of the data stewardship insights summary graphs, with data estate selected, showing the trends and gap analysis graph at the bottom of the page.](media/data-stewardship/trends-and-gap-analysis-small.png)](media/data-stewardship/trends-and-gap-analysis-large.png#lightbox)