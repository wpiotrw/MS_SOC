---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: chunkOffsets resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/chunkoffsets?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: quyenxhuynh
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Provides positional offset metadata for the text chunks that produced caller-supplied embedding data.
ms.date: 2026-08-31T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 1077cfbc-7b69-220b-6800-c48fbb90bb57
document_version_independent_id: f44c0a4e-b417-3ccd-cab3-e4cbb6e75be3
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/chunkoffsets.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/chunkoffsets
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/chunkoffsets.md
platformId: 9553aadf-68a3-45bc-375c-3c200940bdc5
---

# chunkOffsets resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Provides positional offset metadata for the text chunks that produced caller-supplied embedding data. This type is used by the **chunkOffsets** property of [embeddingInput](embeddinginput) and uses base64-encoded integer values instead of floats.

## Methods

None.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| lengths | String | An optional base64 string that encodes a packed sequence of little-endian signed 32-bit integers. Decoded values represent chunk lengths and must be nonnegative. The decoded byte count must be divisible by 4. When supplied, the decoded element count must match **starts**, and elements pair by index. |
| starts | String | A base64 string that encodes a packed sequence of little-endian signed 64-bit integers. Decoded values represent chunk start positions and must be nonnegative and in ascending order. The decoded byte count must be divisible by 8. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.chunkOffsets",
  "starts": "String",
  "lengths": "String"
}
```