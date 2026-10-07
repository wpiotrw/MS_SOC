---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: contentActivity resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/contentactivity?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: kylemar
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents audit data from content processing for Microsoft Purview to ensure compliance, track user actions, and detect unusual behavior.
ms.date: 2025-04-03T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: e5d6db79-572f-4d5f-6862-030f9b56f1eb
document_version_independent_id: 8e791d82-a6ce-4b57-d8be-cd269b87e336
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/contentactivity.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/contentactivity
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/contentactivity.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 698fb22a-3842-b52d-ba0f-3e340d3a2980
---

# contentActivity resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents audit data from content processing for Microsoft Purview to ensure compliance, track user actions, and detect unusual behavior.

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [Create](../activitiescontainer-post-contentactivities) | [contentActivity](contentactivity) | Create a new contentActivity object. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| contentMetadata | [processContentRequest](processcontentrequest) | Defines the input payload. It includes the relevant metadata about the activity, device, and integrated application. |
| id | String | Unique identifier. |
| scopeIdentifier | String | The scope identified from computed protection scopes. |
| userId | String | ID of the user. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.contentActivity",
  "id": "String (identifier)",
  "userId": "String",
  "scopeIdentifier": "String",
  "contentMetadata": {
    "@odata.type": "microsoft.graph.processContentRequest"
  }
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/contentactivity?view=graph-rest-beta&accept=text/markdown)
