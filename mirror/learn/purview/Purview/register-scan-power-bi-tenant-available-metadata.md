---
layout: Conceptual
title: Available metadata for PowerBI in Microsoft Purview Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-power-bi-tenant-available-metadata
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: chigupta
ms.date: 2025-05-21T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Find a list of metadata available for a Power BI tenant in the Microsoft Purview Unified Catalog.
locale: en-us
document_id: 35c546b2-ef70-f0c0-a92f-4af5c923baf5
document_version_independent_id: 35c546b2-ef70-f0c0-a92f-4af5c923baf5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-power-bi-tenant-available-metadata.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-power-bi-tenant-available-metadata
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-power-bi-tenant-available-metadata.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
platformId: 353e3cc8-0617-969e-0be4-32d568d40ab0
---

# Available metadata for PowerBI in Microsoft Purview Unified Catalog | Microsoft Learn

This article lists the metadata that is available for a Power BI tenant in the Microsoft Purview Unified Catalog.

## Power BI

| Metadata | Population method | Source of truth | Asset type | Editable | Upstream metadata |
| --- | --- | --- | --- | --- | --- |
| Classification | Manual | Microsoft Purview | All types | Yes | N/A |
| Sensitivity Labels | Automatic | Microsoft Purview | All types | No |  |
| Glossary terms | Manual | Microsoft Purview | All types | Yes | N/A |
| Collection | Automatic | Microsoft Purview | All types | Yes | N/A |
| Hierarchy | Automatic | Microsoft Purview | All types | No | N/A |
| qualifiedName | Automatic | Microsoft Purview | All types | No | N/A |
| Asset Description | Automatic/Manual\* | Microsoft Purview | All types | Yes | N/A |
| Contacts - Expert | Manual | Microsoft Purview | All types | Yes | N/A |
| Contacts - Owner | Manual | Microsoft Purview | All types | Yes | N/A |
| name | Automatic | Power BI | Power BI Dashboard | Yes | dashboard.DisplayName |
| isReadOnly | Automatic | Power BI | Power BI Dashboard | No | dashboard.IsReadOnly |
| embedUrl | Automatic | Power BI | Power BI Dashboard | No | dashboard.EmbedUrl |
| tileNames | Automatic | Power BI | Power BI Dashboard | No | TileTitles |
| users | Automatic | Power BI | Power BI Dashboard | No | dashboard.Users |
| Lineage | Automatic | Power BI | Power BI Dashboard | No | N/A |
| name | Automatic | Power BI | Power BI Dataflow | Yes | dataflow.Name |
| description | Automatic | Power BI | Power BI Dataflow | Yes | dataflow.Description |
| configuredBy | Automatic | Power BI | Power BI Dataflow | No | dataflow.ConfiguredBy |
| modifiedBy | Automatic | Power BI | Power BI Dataflow | No | dataflow.ModifiedBy |
| modifiedDateTime | Automatic | Power BI | Power BI Dataflow | No | dataflow.ModifiedDateTime |
| Endorsement | Automatic | Power BI | Power BI Dataflow | No | dataflow.EndorsementDetails |
| users | Automatic | Power BI | Power BI Dataflow | No | dataflow.Users |
| Lineage | Automatic | Microsoft Purview | Power BI Dataflow | No |  |
| name | Automatic | Power BI | Power BI Datamart | Yes | datamart.Name |
| description | Automatic | Power BI | Power BI Datamart | Yes | datamart.Description |
| configuredBy | Automatic | Power BI | Power BI Datamart | No | datamart.ConfiguredBy |
| modifiedBy | Automatic | Power BI | Power BI Datamart | No | datamart.ModifiedBy |
| modifiedDateTime | Automatic | Power BI | Power BI Datamart | No | datamart.ModifiedDateTime |
| Endorsement | Automatic | Power BI | Power BI Datamart | No | datamart.EndorsementDetails |
| users | Automatic | Power BI | Power BI Datamart | No | datamart.Users |
| Lineage | Automatic | Microsoft Purview | Power BI Datamart | No |  |
| name | Automatic | Power BI | Power BI Dataset | Yes | dataset.Name |
| description | Automatic | Power BI | Power BI Dataset | Yes | dataset.Description |
| isRefreshable | Automatic | Power BI | Power BI Dataset | No | dataset.IsRefreshable |
| configuredBy | Automatic | Power BI | Power BI Dataset | No | dataset.ConfiguredBy |
| contentProviderType | Automatic | Power BI | Power BI Dataset | No | dataset.ContentProviderType |
| createdDate | Automatic | Power BI | Power BI Dataset | No | dataset.CreatedDateTime |
| targetStorageMode | Automatic | Power BI | Power BI Dataset | No | dataset.TargetStorageMode |
| Schema | Automatic/Manual | Power BI | Power BI Dataset |  | tables & columns |
| Endorsement | Automatic | Power BI | Power BI Dataset | No | dataset.EndorsementDetails |
| users | Automatic | Power BI | Power BI Dataset | No | dataset.Users |
| Lineage | Automatic | Microsoft Purview | Power BI Dataset | No |  |
| name | Automatic | Power BI | Power BI Report | Yes | report.Name |
| description | Automatic | Power BI | Power BI Report | Yes | report.Description |
| createdDateTime | Automatic | Power BI | Power BI Report | No | report.CreatedDateTime |
| webUrl | Automatic | Power BI | Power BI Report | No | report.WebUrl |
| embedUrl | Automatic | Power BI | Power BI Report | No | report.EmbedUrl |
| PBIDatasetId | Automatic | Power BI | Power BI Report | No | report.DatasetId |
| modifiedBy | Automatic | Power BI | Power BI Report | No | report.ModifiedBy |
| modifiedDateTime | Automatic | Power BI | Power BI Report | No | report.ModifiedDateTime |
| reportType | Automatic | Power BI | Power BI Report | No | report.ReportType |
| Endorsement | Automatic | Power BI | Power BI Report | No | report.EndorsementDetails |
| users | Automatic | Power BI | Power BI Report | No | report.Users |
| Lineage | Automatic | Microsoft Purview | Power BI Report | No | N/A |
| name | Automatic | Power BI | Power BI Workspace | Yes | workspace.Name |
| description | Automatic | Power BI | Power BI Workspace | Yes | workspace.Description |
| state | Automatic | Power BI | Power BI Workspace | No | workspace.State |
| type | Automatic | Power BI | Power BI Workspace | No | ResourceType.Workspace |
| IsReadOnly | Automatic | Power BI | Power BI Workspace | No | workspace.IsReadOnly |
| IsOnDedicatedCapacity | Automatic | Power BI | Power BI Workspace | No | workspace.IsOnDedicatedCapacity |
| users | Automatic | Power BI | Power BI Workspace | No | workspace.Users |