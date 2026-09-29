---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: distributionList resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/distributionlist?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: rwaithera
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: outlook
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a personal distribution list in the user's mailbox.
ms.date: 2026-08-03T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: f88745da-f857-e4a1-21ea-30bdb4470c9a
document_version_independent_id: 0d42c314-0f15-95aa-cb90-8ab20a9bcbc3
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/distributionlist.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/distributionlist
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/distributionlist.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: c7e862ee-59eb-04ed-0b5e-ffccd44f9c98
---

# distributionList resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents a personal distribution list in the user's mailbox. A distribution list enables users to group email recipients together so they can send a message to all members at once, without entering each address individually.

Inherits from [outlookItem](outlookitem).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../user-list-distributionlists) | [distributionList](distributionlist) collection | Get a list of the [distributionList](distributionlist) objects in the user's mailbox. |
| [Create](../user-post-distributionlists) | [distributionList](distributionlist) | Create a new [distributionList](distributionlist) in the user's mailbox. |
| [Get](../distributionlist-get) | [distributionList](distributionlist) | Read the properties and relationships of a [distributionList](distributionlist) object. |
| [Update](../distributionlist-update) | [distributionList](distributionlist) | Update the properties of a [distributionList](distributionlist) object. |
| [Delete](../distributionlist-delete) | None | Delete a [distributionList](distributionlist) object. |
| [Add members](../distributionlist-addmembers) | [distributionList](distributionlist) | Add members to a [distributionList](distributionlist). |
| [Delete members](../distributionlist-deletemembers) | [distributionList](distributionlist) | Remove members from a [distributionList](distributionlist). |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| categories | String collection | The categories associated with the distribution list. Inherited from [outlookItem](outlookitem). |
| changeKey | String | Version identifier used for optimistic concurrency control via the `If-Match` header. Read-only. Inherited from [outlookItem](outlookitem). |
| createdDateTime | DateTimeOffset | The date and time when the distribution list was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024, is `2024-01-01T00:00:00Z`. Read-only. Inherited from [outlookItem](outlookitem). |
| displayName | String | The display name of the distribution list. |
| id | String | The unique identifier for the distribution list. Read-only. Inherited from [outlookItem](outlookitem). |
| lastModifiedDateTime | DateTimeOffset | The date and time when the distribution list was last modified. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024, is `2024-01-01T00:00:00Z`. Read-only. Inherited from [outlookItem](outlookitem). |
| notes | String | Notes about the distribution list. |
| personIdentifier | String | The unique identifier of the distribution list in the mailbox. Read-only. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| members | [distributionListMember](distributionlistmember) collection | The members of the distribution list. Not returned by default; use `$expand=members` to include. Read-only. |
| singleValueExtendedProperties | [singleValueLegacyExtendedProperty](singlevaluelegacyextendedproperty) collection | The collection of single-value extended properties defined for the distribution list. Read-only. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.distributionList",
  "id": "string (identifier)",
  "createdDateTime": "string (timestamp)",
  "lastModifiedDateTime": "string (timestamp)",
  "changeKey": "string",
  "categories": [
    "string"
  ],
  "displayName": "string",
  "notes": "string",
  "personIdentifier": "string"
}
```