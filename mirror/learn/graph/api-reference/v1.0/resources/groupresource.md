---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: groupResource resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/groupresource?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: shea3100
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents the group resource in Privileged Identity Management (PIM) for groups.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-08-25T00:00:00.0000000Z
locale: en-us
document_id: aa45c4aa-ad46-8662-f0bb-3614c07c2cab
document_version_independent_id: f8d66640-c731-61bb-11f4-71fa38427c5a
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/groupresource.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/groupresource
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/groupresource.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: f008464e-2939-1328-0839-b3388652c228
---

# groupResource resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents the [group](group) resource in PIM for groups. This entity extends [directoryObject](directoryobject).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [Get](../groupresource-get) | [groupResource](groupresource) | Read the properties of a [groupResource](groupresource) object. |
| [List](../privilegedaccessgroup-list-resources) | [groupResource](groupresource) collection | Retrieve a list of [groupResource](groupresource) objects. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| deletedDateTime | DateTimeOffset | `null`. Inherited from [directoryObject](directoryobject). |
| id | String | The unique identifier for the group. Inherited from [entity](entity). |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.groupResource",
  "deletedDateTime": "String (timestamp)",
  "id": "String (identifier)"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/groupresource?view=graph-rest-beta&accept=text/markdown)
