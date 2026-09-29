---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: embeddingInput resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/embeddinginput?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: jcksonhe
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: A set of precomputed embedding vectors produced by a single embedding model for the request text.
ms.date: 2026-08-31T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 64518227-0fe1-8fe1-d96c-bdefb3e0fbff
document_version_independent_id: 1dc81af9-b2a4-c91e-0e20-dee33b5ccca6
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/embeddinginput.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/embeddinginput
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/embeddinginput.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 61cba157-2d3c-8601-3fe5-67c3c220fd7f
---

# embeddingInput resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

A set of precomputed embedding vectors produced by a single embedding model for the request text. Provide one **embeddingInput** per model in the [textClassificationRequest](textclassificationrequest)**embeddings** collection so the service can skip recomputing embeddings.

## Methods

None.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| chunkOffsets | [chunkOffsets](chunkoffsets) | Optional offset metadata for the text chunks that produced this embedding data. The **starts** property is required when **chunkOffsets** is present. When **lengths** is also present, the decoded element counts must match and pair by index. |
| data | String | The embedding vectors the model produced for the text, encoded as a base64 string of little-endian 32-bit floats. Every vector the model emitted (for example, one per text chunk) is concatenated in order; each contributes exactly the modelType's embedding dimension worth of float components, so the decoded length must be a whole multiple of that dimension. |
| modelType | String | The embedding model identifier drawn from the service allow-list (for example: text-embedding-3-small-512). Unique (case-insensitive) within the embeddings collection; entries whose modelType is outside the allow-list are rejected with a 400. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.embeddingInput",
  "modelType": "String",
  "data": "String",
  "chunkOffsets": {
    "@odata.type": "microsoft.graph.chunkOffsets"
  }
}
```