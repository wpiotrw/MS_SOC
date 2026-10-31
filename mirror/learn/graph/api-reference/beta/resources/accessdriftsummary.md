---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: accessDriftSummary resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/accessdriftsummary?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: suhanigupta
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents an aggregated view of access drift for a governed resource.
ms.date: 2026-08-25T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 65e0ffa6-69c9-f125-bfd4-0446ec558496
document_version_independent_id: ed6defde-0417-a641-0ad8-b6aa9785ee46
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/accessdriftsummary.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/accessdriftsummary
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/accessdriftsummary.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: c0c248c7-56a7-f902-3aa2-ce05823bfaaf
---

# accessDriftSummary resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents an aggregated view of access drift for a governed resource. Each summary captures the drift state for a single resource and drift source combination, including counts of unauthorized and missing assignments.

Inherits from [entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List accessDriftSummary](../accessdriftsummary-list) | [accessDriftSummary](accessdriftsummary) collection | Get a list of the accessDriftSummary objects and their properties. |
| [Get accessDriftSummary](../accessdriftsummary-get) | [accessDriftSummary](accessdriftsummary) | Read the properties and relationships of an accessDriftSummary object. |
| [List details](../accessdriftsummary-list-details) | [accessDriftDetail](accessdriftdetail) collection | Get the access drift details from the details navigation property. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| createdDateTime | DateTimeOffset | The date and time when the drift snapshot was created. |
| driftCounts | [driftCounts](driftcounts) | The aggregate counts of unauthorized and missing assignments for this resource. |
| driftSource | [accessDriftSource](enums#accessdriftsource-values) | The comparison system that detected the drift. The possible values are: `entra`, `externalApplication`, `unknownFutureValue`. |
| id | String | The unique identifier for the access drift summary. Inherited from [entity](entity). |
| resource | [driftResourceInfo](driftresourceinfo) | The governed resource associated with this drift summary. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| details | [accessDriftDetail](accessdriftdetail) collection | The collection of access drift details for this summary. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.accessDriftSummary",
  "id": "String (identifier)",
  "resource": {"@odata.type": "microsoft.graph.driftResourceInfo"},
  "driftSource": "String",
  "driftCounts": {"@odata.type": "microsoft.graph.driftCounts"},
  "createdDateTime": "String (timestamp)"
}
```