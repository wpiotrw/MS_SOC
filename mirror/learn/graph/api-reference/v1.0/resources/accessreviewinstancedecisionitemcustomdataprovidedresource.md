---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: accessReviewInstanceDecisionItemCustomDataProvidedResource resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/accessreviewinstancedecisionitemcustomdataprovidedresource?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: jyothig123
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents customer-provided resources for which access is represented through an accessReviewInstanceDecisionItem object.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-08-31T00:00:00.0000000Z
locale: en-us
document_id: 1ebd6673-b1ef-998c-7b70-b4bf9fc7ec3c
document_version_independent_id: 62959842-a449-2549-e332-6981284f5da5
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/accessreviewinstancedecisionitemcustomdataprovidedresource.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/accessreviewinstancedecisionitemcustomdataprovidedresource
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/accessreviewinstancedecisionitemcustomdataprovidedresource.md
platformId: 18479412-241d-1f07-9df5-d3afe071f79c
---

# accessReviewInstanceDecisionItemCustomDataProvidedResource resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

In an [accessReviewInstanceDecisionItem](accessreviewinstancedecisionitem), the **resource** property can contain an **accessReviewInstanceDecisionItemCustomDataProvidedResource** object for an external customer-provided resource. This open type allows other properties to be passed in.

Inherits from [accessReviewInstanceDecisionItemResource](accessreviewinstancedecisionitemresource).

## Properties

| Property | Type | Description |
| --- | --- | --- |
| customData | String | Custom data to include with the decision. |
| description | String | The description of the custom data provided resource. Inherited from [accessReviewInstanceDecisionItemResource](accessreviewinstancedecisionitemresource). |
| displayName | String | The display name of the custom data provided resource. Inherited from [accessReviewInstanceDecisionItemResource](accessreviewinstancedecisionitemresource). |
| id | String | The identifier of the custom data provided resource. Inherited from [accessReviewInstanceDecisionItemResource](accessreviewinstancedecisionitemresource). |
| scopeDisplayName | String | The name of the scope for the decision. |
| scopeId | String | The identifier of the scope for the decision. |
| type | String | The type of the custom data provided resource. Inherited from [accessReviewInstanceDecisionItemResource](accessreviewinstancedecisionitemresource). |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.accessReviewInstanceDecisionItemCustomDataProvidedResource",
  "id": "String",
  "displayName": "String",
  "type": "String",
  "description": "String",
  "customData": "String",
  "scopeId": "String",
  "scopeDisplayName": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/accessreviewinstancedecisionitemcustomdataprovidedresource?view=graph-rest-beta&accept=text/markdown)
