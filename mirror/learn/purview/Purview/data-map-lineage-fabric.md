---
layout: Conceptual
title: Metadata and Lineage from Fabric into Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-lineage-fabric
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2025-01-08T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn the data lineage extraction from Microsoft Fabric as a source into Microsoft Purview.
locale: en-us
document_id: afdf679b-676e-9706-ec6e-b74ee5f26840
document_version_independent_id: afdf679b-676e-9706-ec6e-b74ee5f26840
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-lineage-fabric.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-lineage-fabric
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-lineage-fabric.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e7cd09c2-9e9a-4f0d-b160-c15783f45b1f
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1d337399-0ca4-4b4c-acef-8df37820e018
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
platformId: 8ae9ced3-4970-ef40-c6cb-14d9d476980f
---

# Metadata and Lineage from Fabric into Microsoft Purview | Microsoft Learn

This article explains data lineage for Microsoft Fabric items in Microsoft Purview.

## Prerequisites

To see data lineage in Microsoft Purview for Fabric items, you must first [register and scan your Fabric tenant](register-scan-fabric-tenant).

## Supported capabilities

Scanning a Microsoft Fabric tenant will automatically bring in metadata and lineage from Fabric items including Power BI into Microsoft Purview Unified Catalog.

- For all Fabric items besides Power BI, only item level metadata and lineage can be scanned.
- For Lakehouse tables and files, sub-item level metadata scanning is now available in preview but sub-item level lineage is still not supported.

## Lineage of Fabric items in Microsoft Purview

Once the [scan of your Fabric tenant](register-scan-fabric-tenant) is complete, following Fabric items are inventoried in Microsoft Purview:

| Experiences | Fabric items | Available in scan | Available in[live view](data-gov-live-view)(same tenant only) |
| --- | --- | --- | --- |
| Real-Time Analytics | Kusto Query Language (KQL) Database | Yes | Yes |
|  | KQL Queryset | Yes | Yes |
| Data Science | Experiment | Yes | Yes |
|  | ML model | Yes | Yes |
| Data Factory | Data pipeline | Yes | Yes |
|  | Dataflow Gen2 | Yes | Yes |
| Data Engineering | Lakehouse | Yes | Yes |
|  | Notebook | Yes | Yes |
|  | Spark Job Definition | Yes | Yes |
|  | SQL analytics endpoint | Yes | Yes |
| Data Warehouse | Warehouse | Yes | Yes |
| Power BI | Dashboard | Yes | Yes |
|  | Dataflow | Yes | Yes |
|  | Datamart | Yes | Yes |
|  | Semantic model (Dataset) | Yes | Yes |
|  | Report | Yes | Yes |
|  | Paginated report | Yes |  |

To see lineage for Fabric items in Microsoft Purview:

1. Select Unified Catalog -&gt; Browse -&gt; Source Types -&gt; Microsoft Fabric -&gt; Fabric Workspaces
2. Select the particular Fabric workspace, select the experience, and then the Fabric item of interest

    [![Screenshot showing the Fabric workspaces button in the Unified Catalog.](media/how-to-lineage-fabric/fabric-workspaces.png)](media/how-to-lineage-fabric/fabric-workspaces.png#lightbox)

    [![Screenshot showing a Fabric source with its full list of experiences.](media/how-to-lineage-fabric/extended-artifacts.png)](media/how-to-lineage-fabric/extended-artifacts.png#lightbox)

    Alternatively, users can search for a Fabric item by name, description, or other details to see relevant results.
3. Select the Lineage tab. Asset relationships are shown with the upstream and downstream dependencies.

    [![Screenshot showing lineage from one lakehouse to another.](media/how-to-lineage-fabric/lakehouse-to-lakehouse.png)](media/how-to-lineage-fabric/lakehouse-to-lakehouse.png#lightbox)

### Lineage of Power BI artifacts in Microsoft Purview

Refer to [Power BI lineage](data-map-lineage-power-bi) for key details and limitations around Power BI lineage in Fabric.

### Known limitations

- For non-Power BI Fabric items, external data sources as upstream sources in lineage aren't yet supported.
- Cross workspace lineage for non-Power BI items isn't supported.
- Notebook -&gt; Pipeline lineage isn't supported.