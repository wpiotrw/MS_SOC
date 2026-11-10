---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: classificationGradingContentLocation resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/classificationgradingcontentlocation?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: ysalib01
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a classification grading match with surrounding document context.
ms.date: 2026-11-04T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 001a08a7-99af-5d98-f27a-cf2e4be173b1
document_version_independent_id: b18b30d9-cb88-475a-5e29-cf8e3897552a
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/classificationgradingcontentlocation.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/classificationgradingcontentlocation
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/classificationgradingcontentlocation.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: e61d5d6a-1d85-0fb7-1460-58fd44d8773a
---

# classificationGradingContentLocation resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents a classification grading match with surrounding document context. In a [classificationGradingJobResponse](classificationgradingjobresponse), eligible matches at `result.classification[].matches[]` use this type.

Inherits from `sensitiveContentLocation` and adds **contextText** for eligible partial-document grading matches with accepted caller-supplied embeddings. This includes final pattern-match and retained AI-refined detections, but not Exact Data Match detections. The shared base type and ordinary classification responses are unchanged.

Context text can contain sensitive document content. Use it only for authorized grading and don't write it to diagnostic logs.

## Methods

None.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| confidence | Int32 | The match confidence level. Inherited from `sensitiveContentLocation`. |
| contextText | String | The complete match and surrounding text, clipped to document boundaries. The default context is up to 100 characters on each side. Read-only, nullable, and omitted when unavailable. |
| evidences | [sensitiveContentEvidence](sensitivecontentevidence) collection | Evidence associated with the match. Inherited from `sensitiveContentLocation`. |
| idMatch | String | The matched identifier text. Inherited from `sensitiveContentLocation`. |
| length | Int32 | The match length in the normalized classified text, not in **contextText**. Inherited from `sensitiveContentLocation`. |
| offset | Int32 | The match's start position in the normalized classified text, not in **contextText**. Inherited from `sensitiveContentLocation`. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.classificationGradingContentLocation",
  "confidence": "Integer",
  "evidences": [
    {
      "@odata.type": "microsoft.graph.sensitiveContentEvidence"
    }
  ],
  "idMatch": "String",
  "length": "Integer",
  "offset": "Integer",
  "contextText": "String"
}
```