---
layout: Conceptual
title: Azure Monitor Logs reference - AZFWNetworkRule - Azure Monitor | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/azfwnetworkrule
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
description: Reference for AZFWNetworkRule table in Azure Monitor Logs.
ms.topic: generated-reference
ms.subservice: logs
ms.date: 2026-07-27T00:00:00.0000000Z
locale: en-us
document_id: 9785e54e-abf4-6bd3-3ed4-019799b3b211
document_version_independent_id: 6c7f5b49-7ae0-c179-8b22-12d16a5af8bf
original_content_git_url: https://github.com/MicrosoftDocs/azure-monitor-docs-pr/blob/live/articles/azure-monitor/reference/tables/azfwnetworkrule.md
site_name: Docs
depot_name: Learn.azure-monitor
page_type: conceptual
toc_rel: ../toc.json
asset_id: azure-monitor/reference/tables/azfwnetworkrule
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-monitor/reference/tables/azfwnetworkrule.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/9949a35d-c893-4f91-bf98-ae940fc30f5f
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/21f7bb14-0703-4e59-a64b-65dd13773dd3
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: b31c82fa-add6-6f57-6283-bf1878a0a7cb
---

# Azure Monitor Logs reference - AZFWNetworkRule - Azure Monitor | Microsoft Learn

Contains all Network Rule log data. Each match between data plane and network rule creates a log entry with the data plane packet and the matched rule's attributes.

## Table attributes

| Attribute | Value |
| --- | --- |
| **Resource types** | microsoft.network/azurefirewalls |
| **Categories** | Security |
| **Solutions** | LogManagement |
| **Basic** table support | Yes |
| **Auxiliary / Lake** table support | Yes |
| **DCR workspace transformation** support | Yes |
| **Ingestion API** support | No |
| **Sample Queries** | [Yes](/en-us/azure/azure-monitor/reference/queries/azfwnetworkrule) |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| Action | string | Action taken by the firewall following the match with this Network Rule. For example: Firewall may Allow/Deny this specific packet. |
| ActionReason | string | When no rule is triggered for a packet, this field contains the reason for the action performed by the firewall. For example: a packet dropped because no rule matched will show `Default Action`. |
| \_BilledSize | real | The record size in bytes |
| DestinationIp | string | Packet's destination IP address. |
| DestinationPort | int | Packet's destination port. |
| \_IsBillable | string | Specifies whether ingesting the data is billable. When \_IsBillable is `false` ingestion isn't billed to your Azure account |
| Policy | string | Name of the policy in which the triggered rule resides. |
| Protocol | string | Packet's network protocol. For example: UDP, TCP. |
| \_ResourceId | string | A unique identifier for the resource that the record is associated with |
| Rule | string | Name of the triggered rule. |
| RuleCollection | string | Name of the rule collection in which the triggered rule resides. |
| RuleCollectionGroup | string | Name of the rule collection group in which the triggered rule resides. |
| SourceIp | string | Packet's source IP address. |
| SourcePort | int | Packet's source port. |
| SourceSystem | string | The type of agent the event was collected by. For example, `OpsManager` for Windows agent, either direct connect or Operations Manager, `Linux` for all Linux agents, or `Azure` for Azure Diagnostics |
| \_SubscriptionId | string | A unique identifier for the subscription that the record is associated with |
| TenantId | string | The Log Analytics workspace ID |
| TimeGenerated | datetime | Timestamp (UTC) when the data plane log was created. |
| Type | string | The name of the table |