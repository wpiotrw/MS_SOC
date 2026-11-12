---
layout: Conceptual
title: Data quality actions in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-actions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how data quality actions are managed in Microsoft Purview Unified Catalog to help advance your data quality goals.
locale: en-us
document_id: e6e8ae1c-1a05-c5ea-2d16-2dc2cf14d419
document_version_independent_id: e6e8ae1c-1a05-c5ea-2d16-2dc2cf14d419
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-actions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-actions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-actions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 76989995-f416-279a-3c3b-ecf68b477280
---

# Data quality actions in Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

The quality of data directly affects the quality of decision making. Good quality data provides business process insights, a better understanding of customers, and faster problem identification. Data quality actions identify problems that you should address to improve data quality in your data estate.

## Required roles

- To see data quality actions in your environment, users need the [data quality reader role](data-governance-roles-permissions#how-to-assign-governance-domain-roles).
- To assign and modify actions, users need the [data quality steward role](data-governance-roles-permissions#how-to-assign-governance-domain-roles).

## Data quality action types

The types of data quality actions generated are:

- A rule that falls below default thresholds.
- A global data quality score that falls below the threshold.
- A data quality scanning and data quality profiling job that fails.
- A data quality scanning and data quality profiling job that skips due to no changes on data since the last run.
- Outlier presence in profiled columns.
- Too many nulls in the profiled data asset.

## Data quality actions severity

Data quality actions have a severity level and color indicator depending on the data quality score:

- **High (red)**: Data quality score is less than **25**.
- **Medium (orange)**: Data quality score is less than **50**.
- **Low (yellow)**: Data quality score is less than **75**.

## View and manage data quality actions for governance domains

Data quality actions roll up from the data asset level to the governance domain level. To browse actions and assign them to users for further action:

1. In Microsoft Purview Unified Catalog, select **Health Management**, then select **Data quality**.
2. Select a governance domain from the list.
3. The **Action items** button shows the number of action items for the domain. Select **Action items** to view all data quality actions.
4. Select an action from the list of actions to view the action's details page.
5. From here, you can assign the action to a user to investigate and resolve. The **Recommendation** section suggests the action to take and provides queries to find the low quality data.

    Note

    - Not every action has a SQL query because not all actions are data related or related to a data quality rule. Some actions are system related, such as a failed or skipped data quality job.
    - If a custom rule exception occurs, which means that the data quality score generated from the custom rule doesn't meet the defined threshold, an action is created. However, a SQL query isn't suggested.

    ![Screenshot of a data quality action detail.](media/data-quality-actions/action-detail.png)
6. Update the *Status*\*, then select **Save**.

## View and manage data quality actions for data assets

You can browse data quality actions for a data asset and assign them to users from the data quality overview page:

1. In Microsoft Purview Unified Catalog, select the **Health Management** menu and **Data quality** submenu.
2. Select a governance domain from the list.
3. Select a **data product** from the list, then select a **data asset** from the list of assets.
4. On the data asset's details page, select **View all** on the **Actions** tile to see all actions for the data asset.
5. Browse through the list of **Active**, **In progress**, **Resolved**, and **My items** actions.

    [![Screenshot of the data quality actions for the selected asset.](media/data-quality-actions/data-asset-action-list-inline.png)](media/data-quality-actions/data-asset-action-list.png#lightbox)
6. Select an action to see its details and assign it to a user to investigate and resolve. an individual for remedy. The **Recommendation** section suggests the action to take and provides queries to find the low quality data.

    Note

    - Not every action has a SQL query because not all actions are data related or related to a data quality rule. Some actions are system related, such as a failed or skipped data quality job.
    - If a custom rule exception occurs, which means the data quality score generated from the custom rule doesn't meet the defined threshold, an action is created. However, a SQL query isn't suggested.

    [![Screenshot of the asset level action details.](media/data-quality-actions/asset-level-action-details-inline.png)](media/data-quality-actions/asset-level-action-details.png#lightbox)
7. Update the **Status**, then select **Save**.

## Resources

- [Best practices for data quality](unified-catalog-plan#improve-the-trustworthiness-of-your-data-with-data-quality).