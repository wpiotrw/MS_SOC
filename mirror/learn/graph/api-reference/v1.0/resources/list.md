---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: List resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/list?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: spgraph-docs-team
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: sharepoint
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
ms.localizationpriority: medium
description: Represents a list in a site.
doc_type: resourcePageType
ms.date: 2024-07-22T00:00:00.0000000Z
locale: en-us
document_id: abc5a9ce-652e-1dc5-c3a8-8b9e342efafb
document_version_independent_id: 04c8824e-5e0c-0086-a972-97f3a890ab47
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/list.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/list
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/list.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: a78b43d4-f5d3-f8e7-f3c6-0984539e8c8d
---

# List resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents a list in a [site](site). This resource contains the top level properties of the list, including template and field definitions.

## Methods

| Method | Return Type | Description |
| --- | --- | --- |
| [Get list](../list-get) | [list](list) | Get the metadata for a **list**. |
| [Create list](../list-create) | [list](list) | Create a new **list** in a **site**. |
| [Get items](../listitem-list) | [listItem](listitem) collection | Get the collection of [listItems](listitem) in a **list**. |
| [List activities](../itemactivity-list) | [itemActivity](itemactivity) collection | List the recent [activities](itemactivity) that took place on a [drive](drive), [list](list), item, or within an item hierarchy. |
| [Update](../listitem-update) | [listItem](listitem) | Update the properties on a [listItem](listitem). |
| [Delete](../listitem-delete) | None | Delete a [listItem](listitem) from a **list**. |
| [Create item](../listitem-create) | [listItem](listitem) | Create a new [listItem](listitem) in a **list**. |
| [Get websocket endpoint](../subscriptions-socketio) | [subscription](subscription) | Get near-real-time change notifications for a [drive](drive) and **list** using [socket.io](https://socket.io/). |
| [List operations](../list-list-operations) | [richLongRunningOperation](richlongrunningoperation) collection | Get a list of [rich long-running operations](richlongrunningoperation) associated with a **list**. |
| [List permissions](../list-list-permissions) | [permission](permission) collection | Get a list of the [permission](permission) objects associated with a [list](list). |
| [Create permission](../list-post-permissions) | [permission](permission) | Create a new [permission](permission) object on a [list](list). |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| createdBy | [identitySet](identityset) | Identity of the creator of this item. Read-only. Inherited from [baseItem](baseitem). |
| createdDateTime | DateTimeOffset | The date and time when the item was created. Read-only. Inherited from [baseItem](baseitem). |
| description | String | The descriptive text for the item. Inherited from [baseItem](baseitem). |
| displayName | String | The displayable title of the list. |
| eTag | String | ETag for the item. Inherited from [baseItem](baseitem). |
| id | String | The unique identifier of the item. Read-only. Inherited from [baseItem](baseitem). |
| lastModifiedBy | [identitySet](identityset) | Identity of the last modifier of this item. Read-only. Inherited from [baseItem](baseitem). |
| lastModifiedDateTime | DateTimeOffset | The date and time when the item was last modified. Read-only. Inherited from [baseItem](baseitem). |
| list | [listInfo](listinfo) | Contains more details about the list. |
| name | String | The name of the item. Read-only. Inherited from [baseItem](baseitem). |
| parentReference | [itemReference](itemreference) | Parent information if the item has a parent. Read-write. Inherited from [baseItem](baseitem). |
| sharepointIds | [sharepointIds](sharepointids) | Returns identifiers useful for SharePoint REST compatibility. Read-only. |
| system | [systemFacet](systemfacet) | If present, indicates that the list is system-managed. Read-only. |
| webUrl | String | URL that displays the item in the browser. Read-only. Inherited from [baseItem](baseitem). |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| columns | [columnDefinition](columndefinition) collection | The collection of field definitions for this list. |
| contentTypes | [contentType](contenttype) collection | The collection of content types present in this list. |
| drive | [drive](drive) | Allows access to the list as a **drive** resource with [driveItems](driveitem). Only present on document libraries. |
| items | [listItem](listitem) collection | All items contained in the list. |
| operations | [richLongRunningOperation](richlongrunningoperation) collection | The collection of long-running operations on the list. |
| permissions | [permission](permission) collection | The set of permissions for the item. Read-only. Nullable. |
| subscriptions | [subscription](subscription) collection | The set of subscriptions on the list. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "createdBy": { "@odata.type": "microsoft.graph.identitySet" },
  "createdDateTime": "String (timestamp)",
  "description": "String",
  "displayName": "String",
  "eTag": "String",
  "id": "String (identifier)",
  "lastModifiedBy": { "@odata.type": "microsoft.graph.identitySet" },
  "lastModifiedDateTime": "String (timestamp)",
  "list": { "@odata.type": "microsoft.graph.listInfo" },
  "name": "String",
  "parentReference": { "@odata.type": "microsoft.graph.itemReference" },
  "sharepointIds": { "@odata.type": "microsoft.graph.sharepointIds" },
  "system": "Boolean",
  "webUrl": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/list?view=graph-rest-beta&accept=text/markdown)
