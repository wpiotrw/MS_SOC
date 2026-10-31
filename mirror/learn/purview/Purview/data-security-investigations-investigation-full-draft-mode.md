---
layout: Conceptual
title: Create an investigation using full draft mode in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-investigation-full-draft-mode
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to create an investigation using full draft mode in Data Security Investigations. Customize data sources, queries, and scope for flexible analysis.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-11T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-security-investigations
ms.collection:
- purview-compliance
- data-security-investigations
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: b6908154-e1f6-4c66-5281-007d09a5c8bf
document_version_independent_id: b6908154-e1f6-4c66-5281-007d09a5c8bf
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-investigation-full-draft-mode.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-investigation-full-draft-mode
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-investigation-full-draft-mode.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 6ac4497c-4044-cd5c-18db-9dd07de127d0
---

# Create an investigation using full draft mode in Data Security Investigations | Microsoft Learn

When you create an investigation by using full draft mode in Data Security Investigations, you get the most flexibility and options for analyzing a data security incident. With this process, you can customize the data sources and query in your investigation.

## Use full draft mode

Complete the following steps to create an investigation and configure the investigation scope by using the *full draft mode*. The user who creates the investigation is automatically added as a member. Members of the investigation can access the investigation in the Microsoft Purview portal and perform Data Security Investigations tasks.

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in with the credentials for a user account assigned [Data Security Investigations permissions](data-security-investigations-permissions). Members of the *Compliance Administrator*, *Organization Management*, *Data Security Management*, and *Insider Risk Management* role groups can also create investigations.
2. Select **Investigations** in the left navigation.
3. Select **Create investigation**.
4. On the **Create an investigation** dialog, complete the following fields:

    - **Title**: Enter a name for the investigation (required). The investigation name must be unique in your organization.
    - **Description**: Add an optional description to help others understand this investigation.
    - **Additional context for AI**: Enter [additional context](data-security-investigations-investigation#ai-context-for-investigations) to help AI focus your investigation on specific areas and issues.
5. Select **Switch to full draft mode**.
6. Select **Add data sources**
7. On the **Manage data sources** flyout pane, search and add data sources for your investigation query. You can filter to scope data sources to help you choose one or more users or group sources to add to the investigation.

    Use one or more of the following options in the **Search for people, groups, locations, or tenant locations** field to select from the following default filters:

    - *All people and groups (default)*
    - *All apps*
    - *All public folders*

    If needed, enter specific people, groups, locations, or tenant locations to reduce the scope of sources to specific resources in your organization.
8. Select **Save**.
9. Use the [query builder](data-security-investigations-search#use-the-query-builder) to create a new search query for the investigation.
10. Select **Review scope** to review statistics about the results from the query
11. Select **Add to scope** to add data items to the investigation scope.