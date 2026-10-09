---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: ediscoveryAddToReviewSetOperation resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/security-ediscoveryaddtoreviewsetoperation?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: SeunginLyu
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: ediscovery
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents an operation to add an eDiscoverySearch to an eDiscoveryReviewSet.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2024-10-30T00:00:00.0000000Z
locale: en-us
document_id: b7bf9403-6d72-c79b-192e-b1c5c64d02f9
document_version_independent_id: e4e91b5a-4c3f-28b4-6444-84c696a8127c
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/security-ediscoveryaddtoreviewsetoperation.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/security-ediscoveryaddtoreviewsetoperation
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/security-ediscoveryaddtoreviewsetoperation.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/8a94907f-2511-4271-b5ca-ec7f2e75067c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/bffa8e88-f633-409d-a24d-083bdbc68872
platformId: 5e3ea40c-202b-bf53-357f-e127b23c62aa
---

# ediscoveryAddToReviewSetOperation resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.security

Represents an operation to add an [eDiscoverySearch](security-ediscoverysearch) to an [eDiscoveryReviewSet](security-ediscoveryreviewset).

Inherits from [caseOperation](security-caseoperation).

## Methods

None.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| action | [microsoft.graph.security.caseAction](security-caseoperation#caseaction-values) | The type of action the operation represents. The possible values are: `contentExport`, `applyTags`, `convertToPdf`, `index`, `estimateStatistics`, `addToReviewSet`, `holdUpdate`, `unknownFutureValue`, `purgeData`, `exportReport`, `exportResult`, `holdPolicySync`. Use the `Prefer: include-unknown-enum-members` request header to get the following values from this [evolvable enum](/en-us/graph/best-practices-concept#handling-future-members-in-evolvable-enumerations): `purgeData`, `exportReport`, `exportResult`, `holdPolicySync`. Inherited from [caseOperation](security-caseoperation). |
| additionalDataOptions | microsoft.graph.security.additionalDataOptions | The options to add items to the review set. The possible values are: `allVersions`, `linkedFiles`, `unknownFutureValue`, `advancedIndexing`, `listAttachments`, `htmlTranscripts`, `messageConversationExpansion`, `locationsWithoutHits`, `allItemsInFolder`, `cloudNativeHtmlConversion`. Use the `Prefer: include-unknown-enum-members` request header to get the following values from this [evolvable enum](/en-us/graph/best-practices-concept#handling-future-members-in-evolvable-enumerations): `advancedIndexing`, `listAttachments`, `htmlTranscripts`, `messageConversationExpansion`, `locationsWithoutHits`, `allItemsInFolder`, `cloudNativeHtmlConversion`. |
| cloudAttachmentVersion | microsoft.graph.security.cloudAttachmentVersion | Specifies the number of most recent versions of cloud attachments to collect. The possible values are: `latest`, `recent10`, `recent100`, `all`, `unknownFutureValue`. |
| completedDateTime | DateTimeOffset | The date and time the operation was completed. Inherited from [caseOperation](security-caseoperation). |
| createdBy | [identitySet](identityset) | The user that created the operation. Inherited from [caseOperation](security-caseoperation). |
| createdDateTime | DateTimeOffset | The date and time the operation was created. Inherited from [caseOperation](security-caseoperation). |
| documentVersion | microsoft.graph.security.documentVersion | Specifies the number of most recent versions of SharePoint documents to collect. The possible values are: `latest`, `recent10`, `recent100`, `all`, `unknownFutureValue`. |
| id | String | The ID for the operation. Read-only. Inherited from [caseOperation](security-caseoperation). |
| itemsToInclude | microsoft.graph.security.itemsToInclude | The items to include in the review set. The possible values are: `searchHits`, `partiallyIndexed`, `unknownFutureValue`. |
| percentProgress | Int32 | The progress of the operation. Inherited from [caseOperation](security-caseoperation). |
| reportFileMetadata | [microsoft.graph.security.reportFileMetadata](security-ediscoveryreportfilemetadata) collection | Contains the properties for report file metadata, including **downloadUrl**, **fileName**, and **size**. |
| resultInfo | [resultInfo](resultinfo) | Contains success and failure-specific result information. Inherited from [caseOperation](security-caseoperation). |
| status | microsoft.graph.security.caseOperationStatus | The status of the case operation. The possible values are: `notStarted`, `submissionFailed`, `running`, `succeeded`, `partiallySucceeded`, `failed`, `unknownFutureValue`. Inherited from [caseOperation](security-caseoperation). |

### additionalDataOptions values

| Name | Description |
| --- | --- |
| allVersions | Include all versions of a SharePoint document that match the source collection query. Caution: SharePoint versions can significantly increase the volume of items. |
| linkedFiles | Include linked files shared in Outlook, Teams, or Engage messages by attaching a link to the file. |
| unknownFutureValue | Evolvable enumeration sentinel value. Don't use. |
| advancedIndexing | To reduce false matches, perform advanced indexing during export. |
| listAttachments | Include list attachments. |
| htmlTranscripts | Contextual chat messages are threaded into HTML transcript. |
| messageConversationExpansion | Include conversation context around a hit. |
| locationsWithoutHits | Look for unindexed items even in locations without hits. |
| allItemsInFolder | Include all content in the folder if the folder itself matches a query. |
| cloudNativeHtmlConversion | Convert items to cloud-native HTML format during review set collection. |

### itemsToInclude values

| Member | Description |
| --- | --- |
| searchHits | Include indexed items that match. |
| partiallyIndexed | Include unindexed items that might not match the query. |
| unknownFutureValue | Evolvable enumeration sentinel value. Don't use. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| reviewSet | [microsoft.graph.security.ediscoveryReviewSet](security-ediscoveryreviewset) | eDiscovery review set to which items matching source collection query gets added. |
| search | [microsoft.graph.security.ediscoverySearch](security-ediscoverysearch) | eDiscovery search that gets added to review set. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.security.ediscoveryAddToReviewSetOperation",
  "action": "String",
  "additionalDataOptions": "String",
  "cloudAttachmentVersion": "String",
  "completedDateTime": "String (timestamp)",
  "createdBy": {"@odata.type": "microsoft.graph.identitySet"},
  "createdDateTime": "String (timestamp)",
  "documentVersion": "String",
  "id": "String (identifier)",
  "itemsToInclude": "String",
  "percentProgress": "Int32",
  "reportFileMetadata": [{"@odata.type": "microsoft.graph.reportFileMetadata"}],
  "resultInfo": {"@odata.type": "microsoft.graph.resultInfo"},
  "status": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/security-ediscoveryaddtoreviewsetoperation?view=graph-rest-beta&accept=text/markdown)
