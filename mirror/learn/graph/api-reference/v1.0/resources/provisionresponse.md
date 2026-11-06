---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: provisionResponse resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/provisionresponse?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: mjsantani
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-directory-management
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents the response returned by the provision action when an approved Virtual Desktop Infrastructure (VDI) provider provisions a device.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-09-24T00:00:00.0000000Z
locale: en-us
document_id: 65012c56-cb57-3a22-89e8-043fc3671fac
document_version_independent_id: d78754cc-083b-9eac-15d6-fe06811e6887
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/provisionresponse.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/provisionresponse
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/provisionresponse.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 33e13a75-2fa5-5db7-038c-32a877057199
---

# provisionResponse resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents the response returned by the [provision](../device-provision) action of the [device](device) resource.

An approved Virtual Desktop Infrastructure (VDI) provisioning service receives this response after it provisions a device and passes it to the device so that the device can complete its registration with the directory.

## Methods

None.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| challenge | String | The cryptographic challenge that the device uses to complete its registration with the directory. |
| deviceId | String | The unique identifier of the provisioned device. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.provisionResponse",
  "challenge": "String",
  "deviceId": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/provisionresponse?view=graph-rest-beta&accept=text/markdown)
