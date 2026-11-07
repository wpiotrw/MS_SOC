---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: place resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/place?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: tiwarisakshi02
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: outlook
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents different space types within a tenant.
ms.date: 2025-11-11T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 1521efeb-f96d-39e9-92f7-614881b350ec
document_version_independent_id: 44cfac3b-3d9f-0f26-5f50-e695da0fcea7
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/place.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/place
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/place.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: ea6efef6-06f4-ebc6-3f24-cf6ca481b08c
---

# place resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents different space types within a tenant. For more information, see [Working with the Places API in Microsoft Graph](places-api-overview).

Base type of [building](building), [desk](desk), [floor](floor), [room](room), [roomList](roomlist), [section](section), and [workspace](workspace).

Inherits from [entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../place-list) | [place](place) collection | Get a collection of the specified type of [place](place) objects defined in a tenant. |
| [Create](../place-post) | [place](place) | Create a new [place](place) object. |
| [Get](../place-get) | [place](place) | Read the properties of a [place](place) object. Returns the requested, derived type of **place**. |
| [Update](../place-update) | [place](place) | Update the properties of [place](place) object that can be a [building](building), [floor](floor), [section](section), [desk](desk), [room](room), [workspace](workspace), or [roomList](roomlist). |
| [Delete](../place-delete) | None | Delete a [place](place) object. |
| [Descendants](../place-descendants) | [place](place) collection | Get all the descendants of a specific type under a [place](place). |
| [Create check-in claim](../place-post-checkins) | [checkInClaim](checkinclaim) | Create a new [checkInClaim](checkinclaim) object to record the check-in status for a specific place, such as a [desk](desk) or a [room](room), associated with a specific calendar reservation. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| address | [physicalAddress](physicaladdress) | The physical address of the **place**, including the street, city, state, country or region, and postal code. |
| customProperties | [stringDictionary](stringdictionary) | Custom properties for the **place**. Each property has a string key and a string value. Nullable. |
| label | String | User-defined description of the **place**. |
| displayName | String | The name that is associated with the **place**. |
| geoCoordinates | [outlookGeoCoordinates](outlookgeocoordinates) | Specifies the **place** location in latitude, longitude, and (optionally) altitude coordinates. |
| id | String | The unique identifier for the **place**. Read-only. This identifier isn't immutable and can change if the mailbox or tenant configuration changes. |
| isWheelChairAccessible | Boolean | Indicates whether the **place** is wheelchair accessible. |
| lastUpdatedTime | DateTimeOffset | The date and time when the **place** was last updated. The timestamp is in ISO 8601 format and is always in UTC. Read-only. Nullable. |
| parentId | String | The ID of a parent **place**. |
| phone | String | The phone number of the **place**. |
| placeId | String | A stable service-level identifier for the **place** object used by Places workloads. |
| tags | String collection | Custom tags that are associated with the **place** for categorization or filtering. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| checkIns | [checkInClaim](checkinclaim) collection | A subresource of a **place** object that indicates the check-in status of an Outlook calendar event booked at the place. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.place",
  "address": {"@odata.type": "microsoft.graph.physicalAddress"},
  "customProperties": {"@odata.type": "microsoft.graph.stringDictionary"},
  "displayName": "String",
  "geoCoordinates": {"@odata.type": "microsoft.graph.outlookGeoCoordinates"},
  "id": "String (identifier)",
  "isWheelChairAccessible": "Boolean",
  "label": "String",
  "lastUpdatedTime": "String (timestamp)",
  "parentId": "String",
  "phone": "String",
  "placeId": "String",
  "tags": ["String"]
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/place?view=graph-rest-beta&accept=text/markdown)
