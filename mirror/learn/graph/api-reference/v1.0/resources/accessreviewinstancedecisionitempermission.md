---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: accessReviewInstanceDecisionItemPermission resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/accessreviewinstancedecisionitempermission?view=graph-rest-1.0
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
description: Represents the permission that grants a principal access to the resource in an accessReviewInstanceDecisionItem object.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-08-31T00:00:00.0000000Z
locale: en-us
document_id: 8983c75d-1e80-3fbc-eecb-81fa522b7c2a
document_version_independent_id: ecbbd548-0218-591a-6e54-64366aac5f12
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/accessreviewinstancedecisionitempermission.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/accessreviewinstancedecisionitempermission
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/accessreviewinstancedecisionitempermission.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 8f0535fa-0de7-155d-c8ea-ad3f21da9faa
---

# accessReviewInstanceDecisionItemPermission resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

In an [accessReviewInstanceDecisionItem](accessreviewinstancedecisionitem), the **permission** property represents the permission that grants a principal access to a resource.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| description | String | The description of the permission. |
| displayName | String | The display name of the permission. |
| id | String | The identifier of the permission. |
| type | String | The type of the permission. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.accessReviewInstanceDecisionItemPermission",
  "id": "String",
  "displayName": "String",
  "type": "String",
  "description": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/accessreviewinstancedecisionitempermission?view=graph-rest-beta&accept=text/markdown)
