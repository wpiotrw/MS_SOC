---
layout: Conceptual
title: Azure Monitor Logs reference - Usage - Azure Monitor | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/usage
breadcrumb_path: ../../../breadcrumb/azure-monitor/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/20/azure-monitor/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/3887dc70-2025-ec11-b6e6-000d3a4f09d0
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
author: austinmccollum
learn_banner_products:
- azure
manager: tedhudek
ms.author: austinmc
ms.service: azure-monitor
description: Reference for Usage table in Azure Monitor Logs.
ms.topic: generated-reference
ms.subservice: logs
ms.date: 2026-07-27T00:00:00.0000000Z
locale: en-us
document_id: 87b8e238-0182-cff2-9799-56dc47f9208a
document_version_independent_id: ef2bd326-ecab-3fa7-a9d9-abec60494157
original_content_git_url: https://github.com/MicrosoftDocs/azure-monitor-docs-pr/blob/live/articles/azure-monitor/reference/tables/usage.md
site_name: Docs
depot_name: Learn.azure-monitor
page_type: conceptual
toc_rel: ../toc.json
asset_id: azure-monitor/reference/tables/usage
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-monitor/reference/tables/usage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/9949a35d-c893-4f91-bf98-ae940fc30f5f
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/21f7bb14-0703-4e59-a64b-65dd13773dd3
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: e6d01cdd-e0a6-1777-e615-c4d860a1443b
---

# Azure Monitor Logs reference - Usage - Azure Monitor | Microsoft Learn

Hourly usage data for each table in the workspace.

## Table attributes

| Attribute | Value |
| --- | --- |
| **Resource types** | - |
| **Categories** | Azure Monitor |
| **Solutions** | LogManagement |
| **Basic** table support | No |
| **Auxiliary / Lake** table support | No |
| **DCR workspace transformation** support | No |
| **Ingestion API** support | No |
| **Sample Queries** | [Yes](/en-us/azure/azure-monitor/reference/queries/usage) |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| AvgLatencyInSeconds | real | Deprecated |
| BatchesCapped | long | Deprecated |
| BatchesOutsideSla | long | Deprecated |
| BatchesWithinSla | long | Deprecated |
| \_BilledSize | real | The record size in bytes |
| Computer | string | Deprecated |
| DataType | string | Table that usage is being reported about. |
| EndTime | datetime | End time of the one hour aggregation window. |
| IsBillable | bool | Logical flag to indicate whether we bill for this data record. |
| \_IsBillable | string | Specifies whether ingesting the data is billable. When \_IsBillable is `false` ingestion isn't billed to your Azure account |
| LinkedMeterId | string | Deprecated |
| LinkedResourceUri | string | Deprecated |
| MeterId | string | GUID of the meter used for billing. |
| Plan | string | Plan of this table (Analytics, Basic or Auxiliary). |
| Quantity | real | Size of data in Mbytes. |
| QuantityUnit | string | Value is alwais Mbytes. |
| ResourceUri | string | The URI of the workspace. This will be same for all records in this table in workspace. |
| Solution | string | Solution about which usage is being reported. |
| SourceSystem | string | The type of agent the event was collected by. For example, `OpsManager` for Windows agent, either direct connect or Operations Manager, `Linux` for all Linux agents, or `Azure` for Azure Diagnostics |
| StartTime | datetime | Start time of the 1 hour aggregation window (same as TimeGenerated). |
| TimeGenerated | datetime | Date and time the record was created. |
| TotalBatches | long | Deprecated |
| Type | string | The name of the table |