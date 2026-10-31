---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: objectConnection resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/synchronization-objectconnection?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: madipanz
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-applications
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a connector data store linkage record for an object in a synchronization job.
ms.date: 2026-10-13T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 9d221a1e-789a-a321-aacb-74382bbc47c1
document_version_independent_id: 9cd35ca5-d58b-4b1c-c1d1-40dda8df656c
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/synchronization-objectconnection.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/synchronization-objectconnection
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/synchronization-objectconnection.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: c4974dd3-b74b-25ca-43df-84bcf78c1454
---

# objectConnection resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents a connector data store linkage record for an object in a [synchronizationJob](synchronization-synchronizationjob).

Use this resource to inspect the cached linkage between a source object and its target identifier, or clear a stale linkage so the object is re-evaluated during a later synchronization cycle. Connections are created by the synchronization engine and their properties are read-only.

During public preview, collection listing isn't supported. Retrieve an individual connection using a known **objectId**. A GET request to the **objectConnections** collection returns `400 Bad Request`.

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [Get](../synchronization-objectconnection-get) | [objectConnection](synchronization-objectconnection) | Get the cached linkage record for a known object in a synchronization job. |
| [Delete](../synchronization-synchronizationjob-delete-objectconnections) | None | Clear the cached linkage record for an object in a synchronization job. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| displayName | String | Display name of the connected object. Nullable. Read-only. |
| objectId | String | Identifier supplied in the request to look up the connection. Can be the source or target identifier for the object in the synchronization job. Key. Not nullable. Read-only. |
| objectTypeName | String | Logical object type, such as `User` or `Group`. Not nullable. Read-only. |
| sourceAnchor | String | Anchor or join value in the source directory. Not nullable. Read-only. |
| targetAnchor | String | Anchor or transformed identifier in the target space. Not nullable. Read-only. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.objectConnection",
  "objectId": "String (identifier)",
  "sourceAnchor": "String",
  "targetAnchor": "String",
  "displayName": "String",
  "objectTypeName": "String"
}
```