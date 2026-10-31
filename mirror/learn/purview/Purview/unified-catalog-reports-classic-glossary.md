---
layout: Conceptual
title: Classic Glossary Report in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-reports-classic-glossary
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2025-05-06T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to view and use Microsoft Purview Data Estate Insights glossary reporting on your data.
locale: en-us
document_id: b4234c65-f42e-9394-be7b-cf44fe219180
document_version_independent_id: b4234c65-f42e-9394-be7b-cf44fe219180
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-reports-classic-glossary.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-reports-classic-glossary
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-reports-classic-glossary.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: fe7513b7-b672-f152-fad3-af7b8e1613d7
---

# Classic Glossary Report in Unified Catalog | Microsoft Learn

This article describes how to access, view, and filter Microsoft Purview glossary insight reports for your data. In this how-to guide, you learn how to:

- Find Data Estate Insights.
- Get a bird's eye view of your data.

## Prerequisites

Before getting started with Data Estate Insights glossary insights, make sure that you complete the following steps:

- Set up a storage resource and populate the account with data.
- [Set up and complete a scan your storage source](data-map-data-sources-register-manage).
- Set up at least one [business glossary term](how-to-create-manage-glossary-term) and attach it to an asset.
- Permissions depending on your current experience:
    - [If using the classic Microsoft Purview Catalog](use-microsoft-purview-governance-portal), you need the [data curator role or insight reader role](data-gov-classic-permissions#roles).
    - [If using the new Microsoft Purview Unified Catalog](unified-catalog), you need [data health reader](data-governance-roles-permissions#unified-catalog-permissions) permissions.

## Use Microsoft Purview glossary insights

In Microsoft Purview, you can [create glossary terms and attach them to assets](how-to-create-manage-glossary-term). As you make use of these terms in your data map, you can view the glossary distribution in glossary insights. These insights give you the state of your glossary based on:

- Number of terms attached to assets.
- Status of terms.
- Distribution of roles by users.

## View glossary insights

1. Open the Microsoft Purview portal.
2. If you're using the [classic Microsoft Purview portal](use-microsoft-purview-governance-portal), select **Data estate insights**. If you're using the [new Microsoft Purview portal](purview-portal) open **Unified Catalog**, select **Health Management**, then select **Reports**.
3. Select the **Classic glossary** report.
4. The report starts with **High-level KPIs** that shows ***Total terms*** in your Microsoft Purview account, ***Approved terms without assets***, and ***Expired terms with assets***. Each of these values helps you understand the current health of your Glossary.

    ![Screenshot showing glossary KPI charts.](media/glossary-insights/glossary-kpi.png)
5. The **Snapshot of terms** section (displayed above) shows the term status as ***Draft***, ***Approved***, ***Alert***, and ***Expired*** for terms with assets and terms without assets.
6. Select **View details** to see the term names with various status and more details about ***Stewards*** and ***Experts***.

    ![Screenshot of terms with and without assets.](media/glossary-insights/glossary-view-more.png)
7. When you select "View more" for ***Approved terms with assets***, Data Estate Insights allows you to navigate to the **Glossary** term detail page, from where you can further navigate to the list of assets with the attached terms.

    ![Screenshot of Data Estate Insights to glossary.](media/glossary-insights/navigate-to-glossary-detail.png)
8. In Glossary insights page, view a distribution of **Incomplete terms** by type of information missing. The graph shows count of terms with ***Missing definition***, ***Missing expert***, ***Missing steward***, and ***Missing multiple*** fields.
9. Select ***View more*** from **Incomplete terms**, to view the terms that have missing information. You can navigate to Glossary term detail page to input the missing information and ensure the glossary term is complete.