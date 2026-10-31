---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: processContentMetadataBase resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/processcontentmetadatabase?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: kylemar
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Abstract base type representing metadata for a content entry being processed, including identifiers, content details, and timestamps.
ms.date: 2025-04-08T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: b2f08639-c095-b714-a0b4-75bbceb2f6aa
document_version_independent_id: 5cba15d0-6b16-5aea-0199-c7a52895bad7
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/processcontentmetadatabase.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/processcontentmetadatabase
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/processcontentmetadatabase.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 4aacea1b-fa34-e60d-5f32-0c41bb80ad17
---

# processContentMetadataBase resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Abstract base type representing metadata for a content entry being processed, including identifiers, content details, and timestamps. Use [processConversationMetadata](processconversationmetadata) for conversation content and [processFileMetadata](processfilemetadata) for file content.

This is an abstract type from which the following resources derive:

- [processConversationMetadata](processconversationmetadata)
- [processFileMetadata](processfilemetadata)

## Properties

| Property | Type | Description |
| --- | --- | --- |
| content | [contentBase](contentbase) | Represents the actual content, either as text (`textContent`) or binary data (`binaryContent`). Optional if metadata alone is sufficient for policy evaluation. **Do not use for [contentActivities](../activitiescontainer-post-contentactivities).** |
| correlationId | String | An identifier used to group multiple related content entries (for example, different parts of the same file upload, messages in a conversation). |
| createdDateTime | DateTimeOffset | Required. Timestamp indicating when the original content was created (for example, file creation time, message sent time). |
| identifier | String | Required. A unique identifier for this specific content entry within the context of the calling application or enforcement plane (for example, message ID, file path/URL). |
| isTruncated | Boolean | Required. Indicates if the provided `content` has been truncated from its original form (for example, due to size limits). |
| length | Int64 | The length of the original content in bytes. |
| modifiedDateTime | DateTimeOffset | Required. Timestamp indicating when the original content was last modified. For ephemeral content like messages, this might be the same as `createdDateTime`. |
| name | String | Required. A descriptive name for the content (for example, file name, web page title, "Chat Message"). |
| sequenceNumber | Int64 | A sequence number indicating the order in which content was generated or should be processed, required when `correlationId` is used. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.processContentMetadataBase",
  "identifier": "String",
  "content": { "@odata.type": "microsoft.graph.contentBase" },
  "name": "String",
  "correlationId": "String",
  "sequenceNumber": "Int64",
  "length": "Int64",
  "isTruncated": "Boolean",
  "createdDateTime": "String (timestamp)",
  "modifiedDateTime": "String (timestamp)"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/processcontentmetadatabase?view=graph-rest-beta&accept=text/markdown)
