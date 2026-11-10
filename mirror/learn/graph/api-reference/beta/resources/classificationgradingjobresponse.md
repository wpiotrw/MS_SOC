---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: classificationGradingJobResponse resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/classificationgradingjobresponse?view=graph-rest-beta
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
description: Represents classification results for grading.
ms.date: 2026-11-04T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 2562eeae-ddd6-a545-44b7-f3b64382cbfe
document_version_independent_id: 0f339465-81a1-adf9-1060-024e36d624c1
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/classificationgradingjobresponse.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/classificationgradingjobresponse
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/classificationgradingjobresponse.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 64df808b-1a81-29b4-a4a8-cc5de933f676
---

# classificationGradingJobResponse resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents classification results for grading. Inherits from `classificationJobResponse` without adding properties.

The inherited **result** retains the existing classification response structure. Eligible matches at `result.classification[].matches[]` use [classificationGradingContentLocation](classificationgradingcontentlocation) to include **contextText**.

## Methods

Retrieve the job with `GET /dataClassification/jobs/{job-id}`. For asynchronous requests, follow the returned `Location` URL and poll until the job reaches a terminal status. No separate methods or new permissions are introduced.

## Properties

All properties, including **id**, **status**, **error**, and **result**, are inherited from `classificationJobResponse`. Only the job identifier is expanded below.

| Property | Type | Description |
| --- | --- | --- |
| id | String | The inherited job identifier. |

## Relationships

None.

## JSON representation

This abbreviated representation shows the type and job identifier. The other inherited properties, including **result**, aren't expanded.

```json
{
  "@odata.type": "#microsoft.graph.classificationGradingJobResponse",
  "id": "String (identifier)"
}
```