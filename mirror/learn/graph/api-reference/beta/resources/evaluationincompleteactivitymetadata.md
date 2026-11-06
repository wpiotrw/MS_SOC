---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: evaluationIncompleteActivityMetadata resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/evaluationincompleteactivitymetadata?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: zhengnlu
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents metadata for a Secure by Default policy evaluation that couldn't be completed.
ms.date: 2026-09-10T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: d7290f72-fe4c-f97a-fc1e-8240aef5bafe
document_version_independent_id: 5eb4d0d3-4185-cf4d-a976-f3aa406a9518
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/evaluationincompleteactivitymetadata.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/evaluationincompleteactivitymetadata
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/evaluationincompleteactivitymetadata.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: dcb3eab2-5e54-a20d-a524-0b98d3d6c143
---

# evaluationIncompleteActivityMetadata resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents metadata for a Secure by Default (SBD) policy evaluation that couldn't be completed because of a platform limit, extraction or classification failure, supporting-service failure, or enforcement failure.

Inherits from [processContentMetadataBase](processcontentmetadatabase).

Use this type only in the **contentToProcess.contentEntries** collection of a request to [create a contentActivity](../activitiescontainer-post-contentactivities). This type isn't supported by the **processContent** or **processContentAsync** APIs. Use the `@odata.type` value `#microsoft.graph.evaluationIncompleteActivityMetadata` to identify an entry of this type.

The service derives the audit organization, workload, and operation from the authenticated tenant, **contentToProcess.integratedAppMetadata.name**, and **contentToProcess.activityMetadata.activity**, respectively. Item details reuse inherited properties such as **identifier**, **name**, and **length**. The service resolves additional audit context through runtime data lookups.

The service records this metadata as a `ComplianceEvaluationIncomplete` (`506`) audit record. You don't specify a record type in the request.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| content | [contentBase](contentbase) | The content that was evaluated, represented as text or binary data. Don't include this property when you create a content activity. Inherited from [processContentMetadataBase](processcontentmetadatabase). |
| contentCategory | [contentCategory](enums#contentcategory-values) | The type of content. The possible values are: `none`, `ai`, `unknownFutureValue`. The default value is `ai`, which refers to AI-generated content. Inherited from [processContentMetadataBase](processcontentmetadatabase). |
| correlationId | String | An identifier used to group related content entries or correlate the audit record with related evaluation telemetry. Inherited from [processContentMetadataBase](processcontentmetadatabase). |
| createdDateTime | DateTimeOffset | The date and time when the evaluated content or activity was created. Required. The timestamp is always in UTC. Inherited from [processContentMetadataBase](processcontentmetadatabase). |
| errorAction | [errorActions](enums#erroractions-values) | The action taken when policy evaluation couldn't be completed. Required. This flagged enumeration allows multiple members to be selected simultaneously. For example, `audit,block` indicates that the activity was audited and blocked. The possible values are: `none`, `audit`, `block`, `unknownFutureValue`. Don't combine `none` with another value. |
| identifier | String | A unique identifier for the content or activity in the enforcement plane; for example, a message ID, file path, or file URL. Required. Inherited from [processContentMetadataBase](processcontentmetadatabase). |
| inspectionIncompleteReason | [evaluationErrorDetail](evaluationerrordetail) | The structured reason why inspection couldn't be completed. Required. The object requires **errorCategory** and **errorType**. |
| isTruncated | Boolean | Indicates whether the supplied content was shortened from its original form. Required. Inherited from [processContentMetadataBase](processcontentmetadatabase). |
| length | Int64 | The length of the original content in bytes. Inherited from [processContentMetadataBase](processcontentmetadatabase). |
| modifiedDateTime | DateTimeOffset | The date and time when the evaluated content was last modified. Required. Inherited from [processContentMetadataBase](processcontentmetadatabase). |
| name | String | A descriptive name for the content or activity; for example, a file name or interaction name. Required. Inherited from [processContentMetadataBase](processcontentmetadatabase). |
| sensitivityLabels | [currentLabel](currentlabel) collection | Caller-supplied sensitivity labels describing the content. Inherited from [processContentMetadataBase](processcontentmetadatabase). |
| sequenceNumber | Int64 | A sequence number that indicates the order in which related content was generated or should be processed. Required when **correlationId** is used. Inherited from [processContentMetadataBase](processcontentmetadatabase). |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.evaluationIncompleteActivityMetadata",
  "content": { "@odata.type": "microsoft.graph.contentBase" },
  "contentCategory": "String",
  "correlationId": "String",
  "createdDateTime": "DateTimeOffset",
  "errorAction": "String",
  "identifier": "String",
  "inspectionIncompleteReason": {
    "@odata.type": "microsoft.graph.evaluationErrorDetail"
  },
  "isTruncated": "Boolean",
  "length": "Int64",
  "modifiedDateTime": "DateTimeOffset",
  "name": "String",
  "sequenceNumber": "Int64",
  "sensitivityLabels": [
    {
      "@odata.type": "microsoft.graph.currentLabel"
    }
  ]
}
```