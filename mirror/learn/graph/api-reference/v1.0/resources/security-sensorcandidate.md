---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: sensorCandidate resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/security-sensorcandidate?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: samuelbenichou
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a Microsoft Defender for Identity sensor that's ready to be activated.
ms.date: 2025-10-22T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 1661f881-5a05-89eb-109c-3e7e8015a8ee
document_version_independent_id: 7c8e7dc3-ebc8-5c87-ea80-40e90377a2cd
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/security-sensorcandidate.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/security-sensorcandidate
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/security-sensorcandidate.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5711eaa5-435f-4c40-8d89-924ef7945eec
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ee4d551-d6c4-4e91-986e-0f1afd52559f
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: ea9dc9de-9de7-477b-f5d7-3c77517eed07
---

# sensorCandidate resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.security

Represents a Microsoft Defender for Identity sensor that's ready to be activated.

Inherits from [microsoft.graph.entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../security-identitycontainer-list-sensorcandidates) | [microsoft.graph.security.sensorCandidates](security-sensorcandidate) collection | Get a list of the sensorCandidate objects and their properties. |
| [Activate](../security-sensorcandidate-activate) | None | Activate Microsoft Defender for Identity sensors. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| computerDnsName | String | The DNS name of the computer associated with the sensor. |
| domainName | String | The domain name of the sensor. |
| id | String | The unique identifier for the sensor candidate. Inherited from [microsoft.graph.entity](entity). Inherits from [entity](entity) |
| lastSeenDateTime | DateTimeOffset | The date and time when the sensor was last seen. |
| senseClientVersion | String | The version of the Defender for Identity sensor client. Supports `$filter` (`eq`). |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.security.sensorCandidate",
  "id": "String (identifier)",
  "computerDnsName": "String",
  "senseClientVersion": "String",
  "lastSeenDateTime": "String (timestamp)",
  "domainName": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/security-sensorcandidate?view=graph-rest-beta&accept=text/markdown)
