---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: activityMetadata resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/activitymetadata?view=graph-rest-1.0
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
description: Represents metadata about a specific user activity being evaluated, including the activity type and location.
ms.date: 2025-04-08T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: e8681759-e9f6-11b0-acb3-76effc35e2cb
document_version_independent_id: dd605ed5-669a-fc9a-1775-d62ba8f856c2
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/activitymetadata.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/activitymetadata
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/activitymetadata.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: f3b226e1-b50f-d7ce-a7e7-7956456f204f
---

# activityMetadata resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents metadata about a specific user activity being evaluated, including the activity type and location.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| activity | microsoft.graph.security.userActivityType | The type of user activity. Possible values are `uploadText`, `uploadFile`, `downloadText`, `downloadFile`, `unknownFutureValue`, `copyToClipboard`, `pasteFromClipboard`, `print`, `accessDebugTools`. Use the `Prefer: include-unknown-enum-members` request header to get the following values in this evolvable enum: `copyToClipboard`, `pasteFromClipboard`, `print`, `accessDebugTools`. Required. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.activityMetadata",
  "activity": "String",
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/activitymetadata?view=graph-rest-beta&accept=text/markdown)
