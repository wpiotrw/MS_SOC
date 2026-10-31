---
layout: Conceptual
title: eDiscovery (Premium) dashboard for review sets | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-dashboard
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use the Microsoft Purview eDiscovery (Premium) dashboard for review sets to quickly analyze your corpus to identify trends or key statistics that will help you develop your review strategy.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
locale: en-us
document_id: 1189aae1-b109-6e07-98ee-79bc303446f5
document_version_independent_id: 1189aae1-b109-6e07-98ee-79bc303446f5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-dashboard.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-dashboard
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-dashboard.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 3aedc57d-5117-4284-ce92-d1354a0a8edf
---

# eDiscovery (Premium) dashboard for review sets | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Important

Search profile view has been retired as of March 31, 2024 and is not available in new eDiscovery cases.

For some cases in Microsoft Purview eDiscovery (Premium), you may have a large volume of documents and email messages that need to be reviewed. Before you start the review process, you may want to quickly analyze your corpus to identify trends or key statistics that will help you develop your review strategy. To do this, you can use the eDiscovery (Premium) dashboard for review sets to quickly analyze your corpus.

## Step 1: Create a widget on the review set dashboard

1. In the Microsoft Purview portal, go to **eDiscovery &gt; eDiscovery (Premium)** to display the list of cases in your organization.
2. Select an existing case.
3. Select the **Review Set** tab, and then select a review set.
4. In the **Individual results** dropdown list, select **Search profile view**.

    ![DashboardPivot.](media/dashboardpivot.png)

    The **Search profile view** page is displayed; the first time you display this page, three default widgets are displayed.

    ![Dashboard.](media/dashboardonly.png)
5. Select the **New widget** and then select one of the following items:

    ![New widget dropdown list.](media/newwidgetdropdownbox.png)

    - **Choose from library:** Displays a default library of widgets. You select a widget and then select **Add** to add it to the widgets on the **Search profile view** page.
    - **Create custom widget:** Displays a flyout page that you can use to set up a custom widget.
6. To create a custom widget, do the following on the **Add widget** flyout page:

    ![Create Widget.](media/addwidget.png)

    a. Type a name for the widget, which is displayed in the widget title bar. Naming a widget is required, but it's helpful to identify the widget data.

    b. Select a property in the **Choose pivot** dropdown list that will be used for the widget data. The items in this list are the searchable properties for the items in the review set. For a description of these properties, see [Document metadata fields in eDiscovery (Premium)](ediscovery-document-metadata-fields). The pivot options for the widget are listed in the **Searchable field name** column in this topic.

    c. Select a chart type to display the data from the selected pivot property.
7. Select **Add** to create the custom widget and display it on the **Search profile view** page.

## Step 2: Create a review set search query

1. Select **...** in the widget title bar, and then select **Apply condition**.

    ![Dashboard home.](media/searchprofilehome.png)
2. On the flyout page, select an element on the widget key or widget chart to create a filter.

    ![CreateFilter.](media/applyconditionfilter.png)
3. Repeat steps 1-2 for other widgets multiple widgets.
4. When you're done, select **Save as query** to save your conditions as a new search query for the review set.

    ![Query.](media/savequery.png)
5. Close the **Search profile view** to return to the search results view.

    If you have created any visual filters, the resulting query is applied to the search results that are displayed, and the search query that you saved in step 4 is displayed under **Saved queries**. For more information about review set queries, see [Query the data in a review set](ediscovery-review-set-search).