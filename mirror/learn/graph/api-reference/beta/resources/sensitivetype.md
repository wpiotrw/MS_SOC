---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: sensitiveType resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/sensitivetype?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: vipulyadav
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents information about a sensitive information type used to classify content.
ms.date: 2025-07-18T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: c5b35103-16df-2184-72bb-7e35bb706d6f
document_version_independent_id: 12c18108-90fa-9fa2-827d-5b3b69ba26c2
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/sensitivetype.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/sensitivetype
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/sensitivetype.md
platformId: d45fd6b0-97db-7c71-33da-9ec9976df3c2
---

# sensitiveType resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents information about a sensitive information type (SIT) used to classify content.

## Methods

None.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| classificationMethod | [classificationMethod](enums#classificationmethod-values) | The classification method. The possible values are: `patternMatch`, `exactDataMatch`, `fingerprint`, `machineLearning`, `privacyDataMatch`, `aiPowered`, `unknownFutureValue`. `privacyDataMatch` performs privacy data matching based on tenant data. `aiPowered` performs AI-powered classification and can benefit from supported caller-supplied embeddings. `unknownFutureValue` is an evolvable enumeration sentinel value. Don't use it. |
| description | String | The description of the sensitive information type. |
| id | String | The unique identifier for the sensitive information type. Inherited from [entity](entity). |
| lastModifiedDateTime | DateTimeOffset | The date and time when the sensitive information type was last modified. |
| name | String | The name of the sensitive information type. |
| publisherName | String | The name of the publisher. |
| rulePackageId | String | The identifier of the rule package. |
| rulePackageType | String | The type of the rule package. |
| scope | [sensitiveTypeScope](enums#sensitivetypescope-values) | The scope of the sensitive information type. The possible values are: `fullDocument`, `partialDocument`. |
| sensitiveTypeSource | [sensitiveTypeSource](enums#sensitivetypesource-values) | The source of sensitive type. The possible values are: `outOfBox`, `tenant`. |
| state | String | The state of the sensitive information type. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.sensitiveType",
  "id": "String (identifier)",
  "name": "String",
  "description": "String",
  "rulePackageId": "String",
  "rulePackageType": "String",
  "publisherName": "String",
  "state": "String",
  "scope": "String",
  "sensitiveTypeSource": "String",
  "classificationMethod": "String",
  "lastModifiedDateTime": "String (timestamp)"
}
```