---
layout: Conceptual
title: Permissions for Data Estate Insights in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/insights-permissions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article describes what permissions are needed to access access and managed Data Estate Insights in Microsoft Purview.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: suvirdi
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.custom:
- event-tier1-build-2022
- sfi-image-nochange
ms.topic: how-to
ms.date: 2025-02-26T00:00:00.0000000Z
locale: en-us
document_id: 094123a6-90cf-0373-fa98-6fe6488f982a
document_version_independent_id: 094123a6-90cf-0373-fa98-6fe6488f982a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/insights-permissions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/insights-permissions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/insights-permissions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 9170ddb6-b605-cab4-ba1d-db9268d049e5
---

# Permissions for Data Estate Insights in Microsoft Purview | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Like all other permissions in Microsoft Purview, Data Estate Insights access is given through collections. This article describes what permissions are needed to access Data Estate Insights in Microsoft Purview.

## Insights reader role

The insights reader role gives users read permission to the Data Estate Insights application in Microsoft Purview. However, a user with this role will only have access to information for collections that they also have at least data reader access to.

As Data Estate Insights application gives a bird's eye view of your data estate and catalog usage from a governance and risk perspective, it's intended for users who need to manage and report on this high-level information, like a Chief Data Officer. You may not want, or need, all your data readers to have access to the Data Estate Insights dashboards.

## Role assignment

- **Insights Reader** role can be assigned to any Data Map user, by the **Data Curator of the root collection**. Users assigned the Data Curator role on subcollections don't have the privilege of assigning insights reader.

    ![Screenshot of root collection, showing the role assignments tab, with the add user button selected next to Insights reader.](../media/insights-permissions/insights-reader.png)
- A **Data Curator** of any collection also has read permission to Data Estate Insights application. Their scope of insights will be limited to the metadata assigned to collections. In other words, a Data Curator at a subcollection will only view KPIs and aggregations on collections they have access to. A Data Curator can still view and edit assets from Data Estate Insights app, without any extra permissions.
- A **Data Reader** at any collection node, can see Data Estate Insights app on the left navigation bar, however, when they hover on the icon, they'll receive a message saying they need to contact Data Curator at root collection for access. Once a Data Reader has been assigned the Insights Reader role, they can view KPIs and aggregations based on the collections they have Data Reader permission on. A Data Reader can't edit assets or select ***"Export to CSV"*** from the app.

Note

All roles other than Data Curator, will need explicit role assignment as **Insights Reader** to be able to click into the Data Estate Insights app.