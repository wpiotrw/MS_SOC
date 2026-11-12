---
layout: Conceptual
title: Health Management Actions (Preview) Page in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-health-management-actions-page
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
description: Learn how to understand and manage data health from the Actions (preview) page in Microsoft Purview Unified Catalog.
locale: en-us
document_id: d374e5e3-40bc-aa5c-3b8b-85319082d32b
document_version_independent_id: d374e5e3-40bc-aa5c-3b8b-85319082d32b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-health-management-actions-page.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-health-management-actions-page
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-health-management-actions-page.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: a92e5c0e-3dad-3432-eb4e-38c8476e42c5
---

# Health Management Actions (Preview) Page in Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

The **Actions (preview)** page in Microsoft Purview Unified Catalog displays all health management actions related to catalog metadata, controls, and data quality. Health management actions give you and your users steps to take to improve data health and governance across your data estate. These actions correspond to the checks made to calculate a data product's [data governance health control score](unified-catalog-controls). Addressing these actions raises your health score and promotes a more useful and discoverable Unified Catalog.

## Prerequisites

- You need [data health reader](data-governance-roles-permissions#unified-catalog-permissions) permissions to view data health information.
- You need [data health owner](data-governance-roles-permissions#unified-catalog-permissions) permissions to update and assign health actions.

## View health management actions

To view health management actions, go to **Unified Catalog** &gt; **Health Management** &gt; **Actions**. The **Actions (preview)** page shows a list of actions, how long they're active, the target for each action, and the owner.

You can search by keyword or filter these actions by many values, including: assigned to, governance domains, active since, action types, and more.

You can also group actions by selecting **Group by** to view actions by:

- Severity
    - High
    - Medium
    - Low
- Finding types and subtypes
- Finding subtype
- Finding name

Tip

- If you don't see the actions you expect, check the applied filters and group.
- You need the **Data Quality Metadata Reader** role to see the **Target entity** related to the action. The target entity provides a deep link to browse for remediation action.
- You won't see the **Target entity** if it's deleted from the governance domain or data product, or if you don't have the **Data Quality Metadata Reader** role.

## Available actions

The actions available are determined by [control rules](unified-catalog-controls) or [data quality rules](unified-catalog-data-quality-rules). Learn more about [data quality actions](unified-catalog-data-quality-actions).

Here's a list of actions that are available from metadata quality:

| Finding type | Finding subtype | Finding Name | Severity |
| --- | --- | --- | --- |
| Access and use | Compliant data use | Missing terms of use on data products | Medium |
|  | Self-serve access enablement | Missing access policy on data products | Medium |
| Discoverability | Data cataloging | Data product not linked to data assets | High |
|  |  | Missing description on data products | High |
|  |  | Missing published glossary terms on data products | High |
|  |  | Missing use case on data products | High |
|  | Data products connection | Data product not linked to data assets | Medium |
| Estate curation | Classification and labeling | Missing classification on data assets | Medium |
| Health observability | Health management monitoring, alerting, and insights |  |  |
| Metadata quality management | Data product usability | Governance domain description length is fewer than 100 characters | Medium |
|  |  | Data product description length is fewer than 100 characters | Medium |
|  |  | Published glossary term's description length is fewer than 25 characters | Medium |
|  | Linked assets | Data product description length is fewer than 100 characters | Medium |
|  |  | Missing published glossary terms on data product | High |
| Trusted data | Data product certification | Data product isn't endorsed | Low |
|  | Data product ownership | Missing owners on data assets | High |
|  |  | Missing owners on data products | High |
|  | Data quality enablement | Missing data quality scores on data assets | Medium |
| Value creation | Business OKRs alignment | Missing OKRs on data products | Medium |

Tip

If the actions you see don't match up with these values and severities, check [metadata quality](unified-catalog-metadata-quality). Your organization might have implemented custom checks and severities.

## Action details

To see an action's details, select it. You see the action owners, the associated data product and governance domain, as well as its reason and any potential recommendations for resolving it.

## Resolve an action

To resolve an action:

1. Assign owners who take steps to resolve the recommendations.
2. The owners investigate the issue based on the provided information and recommendation.
3. The owners update the status to reflect their current progress.
4. When they make the suggested updates, they update the action's status to **Resolved** and save the action.

As the entire health management refreshes in the next scheduled run, it reconciles all resolved actions from the catalog. If you artificially mark an action as resolved but the issue in the catalog remains, the action status changes and is added back to the health actions queue.