---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: planner resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/planner?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: TarkanSevilmis
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: planner
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: The **planner** resource is the entry point for the Planner object model. It returns a singleton **planner** resource.  It doesn't contain any usable properties.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2024-05-23T00:00:00.0000000Z
locale: en-us
document_id: 8898585b-748e-5378-3c37-75d956328491
document_version_independent_id: bdb485b1-dd0e-5260-c396-87d40b470aca
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/planner.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/planner
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/planner.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 0149a874-ea70-01a4-4979-ca46b48f67a0
---

# planner resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

The **planner** resource is the entry point for the Planner object model. It returns a singleton **planner** resource. It doesn't contain any usable properties.

## Methods

| Method | Return Type | Description |
| --- | --- | --- |
| [Create bucket](../planner-post-buckets) | [plannerBucket](plannerbucket) | Create a new **plannerBucket** by posting to the buckets collection. |
| [Create plan](../planner-post-plans) | [plannerPlan](plannerplan) | Create a new **plannerPlan** by posting to the plans collection. |
| [Create task](../planner-post-tasks) | [plannerTask](plannertask) | Create a new **plannerTask** by posting to the tasks collection. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| buckets | [plannerBucket](plannerbucket) collection | Read-only. Nullable. Returns a collection of the specified buckets |
| plans | [plannerPlan](plannerplan) collection | Read-only. Nullable. Returns a collection of the specified plans |
| tasks | [plannerTask](plannertask) collection | Read-only. Nullable. Returns a collection of the specified tasks |

## JSON representation

The following JSON representation shows the resource type.

```json
{
}
```

## Example

The **planner** resource is available at the root of the graph.

```http
GET https://graph.microsoft.com/v1.0/planner
```

```http
HTTP/1.1 200 OK
Content-type: application/json

{
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/planner?view=graph-rest-beta&accept=text/markdown)
