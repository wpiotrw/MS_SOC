---
layout: Conceptual
title: Data Observability in Microsoft Purview Unified Catalog (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-observability
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: nidought
ms.date: 2025-04-11T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn about data observability (preview) in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 69c75a13-d4e8-e550-e998-509d913ad2a8
document_version_independent_id: 69c75a13-d4e8-e550-e998-509d913ad2a8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-observability.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-observability
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-observability.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 2de10a18-45bb-c4a3-8e68-235f02e55e51
---

# Data Observability in Microsoft Purview Unified Catalog (preview) | Microsoft Learn

Data observability in Microsoft Purview Unified Catalog provides a bird's eye view into the health of the data estate as data flows between sources. Data stewards, experts, and those accountable for data health can view their data estate in a single screen, providing the ability to view the lineage of data assets all the way up to the structure of the governance domains. This single view helps users understand where data starts and ends, what the issues are, and where there's an effect on reporting obligations.

## How data observability works

The visualizations in data observability bring together all of the metadata from Microsoft Purview Unfiied Catalog for things like technical data lineage and data quality. Data observability provides contextual views and on-demand custom views in a single diagram.

Having the right view of the metadata in a single place allows you to dig into questions about how data quality is changing across your data estate, and how your data's being used and by whom. Viewing the entire data estate at one time enables the central data team or federated data teams to quickly identify improvements in metadata, ownership, data quality, or data architecture.

Note

Data observability doesn't create any of the lineage or metadata used in the visualization. If you haven't added lineage, or haven't yet created governance domains and business concepts, the screen shows a limited amount of the data estate to view.

## Where observability shows up in Unified Catalog

You see an **Observability** tab when you look at a details page for a governance domain, a data product, and a glossary term. Also, the **Data observability (preview)** page under **Health management** in the left navigation provides a custom view of your entire data estate. See [Observability views](unified-catalog-observability-views) for details.

Note

You need certain roles to see and work with data observability. See [Unified Catalog roles](data-governance-roles-permissions#unified-catalog-roles) for details.