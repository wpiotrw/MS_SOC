---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: teamworkCustomEmoji resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/teamworkcustomemoji?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: mea
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: teams
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a custom emoji that was uploaded to the teamwork messaging of the organization.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-06-10T00:00:00.0000000Z
locale: en-us
document_id: c0e5469a-609d-836c-0ccb-a4c2e945df0f
document_version_independent_id: 19d1a2db-493a-567d-58f5-0d8da4131a6b
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/teamworkcustomemoji.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/teamworkcustomemoji
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/teamworkcustomemoji.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 4029ea18-1e26-5d9c-9c88-05e3ffa7d42b
---

# teamworkCustomEmoji resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents a custom emoji that was uploaded to the teamwork messaging of the organization. Custom emojis can be used in chat messages and channel messages.

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../teamworkmessaging-list-customemojis) | [teamworkCustomEmoji](teamworkcustomemoji) collection | Get a list of [custom emojis](teamworkcustomemoji) available in the teamwork messaging of the organization. |
| [Create](../teamworkmessaging-post-customemojis) | [teamworkCustomEmoji](teamworkcustomemoji) | Create a new [custom emoji](teamworkcustomemoji) in the teamwork messaging of the organization, which adds the custom emoji to Teams for the tenant. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| contentBytes | String | The base64-encoded image content of the emoji. Supported formats include PNG and GIF. |
| createdBy | [customEmojiFromIdentitySet](customemojifromidentityset) | Identity of the user who created the emoji. |
| createdDateTime | DateTimeOffset | The date and time when the emoji was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024, is `2024-01-01T00:00:00Z`. |
| displayName | String | The unique display name of the custom emoji. Key. Must be unique and must not conflict with existing emoji names. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
    "@odata.type": "#microsoft.graph.teamworkCustomEmoji",
    "displayName": "String (identifier)",
    "contentBytes": "String",
    "createdDateTime": "String (timestamp)",
    "createdBy": {
        "@odata.type": "microsoft.graph.customEmojiFromIdentitySet"
    }
}
```