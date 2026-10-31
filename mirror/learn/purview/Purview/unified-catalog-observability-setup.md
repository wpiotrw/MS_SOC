---
layout: Conceptual
title: Observability Setup in Microsoft Purview Unified Catalog (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-observability-setup
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: nidought
ms.date: 2026-06-25T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to configure settings for observability (preview) in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 0af4d0ea-756d-80b9-0572-7d3922fb5d65
document_version_independent_id: 0af4d0ea-756d-80b9-0572-7d3922fb5d65
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-observability-setup.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-observability-setup
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-observability-setup.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 45109820-19dd-09b2-86c0-b31dd03f0586
---

# Observability Setup in Microsoft Purview Unified Catalog (preview) | Microsoft Learn

To start generating visualizations in Microsoft Purview Unified Catalog, complete the following setup steps. This setup enables two snapshot jobs that collect metadata needed to render the diagrams.

## Prerequisites

1. Assign the Data Governance Administrator role in the [Data Governance role group](data-governance-roles-permissions#tenant-level-role-groups).
2. Create assets in Microsoft Purview Data Map, and create governance domains and concepts in the Unified Catalog.

## Setup steps

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) using credentials for a *Data Governance Administrator* role.
2. Go to **Settings**, then select **Unified Catalog**.
3. Select **Data Observability**.
4. Select **Enable** next to the **Catalog Snapshot Job** heading.
5. Select **Enable** next to the **Data Quality Snapshot Job** heading.

The snapshot jobs take a few minutes to run before the visualizations are enabled. The catalog snapshot job refreshes the view of metadata and lineage every 1440 minutes. The data quality snapshot job refreshes the view of data quality scores every 10 minutes.

Important

There's a known limitation in browser performance that prevents rendering a large snapshot of more than 500 MB.

Tip

You don't have to enable the data quality snapshot job if you're not working on data quality. You can turn on this job later.