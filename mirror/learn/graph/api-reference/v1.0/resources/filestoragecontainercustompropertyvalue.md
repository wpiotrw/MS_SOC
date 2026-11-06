---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: fileStorageContainerCustomPropertyValue resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/filestoragecontainercustompropertyvalue?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: tonchan-msft
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: onedrive
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Contains the custom property values stored in a fileStorageContainerCustomPropertyDictionary resource.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-09-25T00:00:00.0000000Z
locale: en-us
document_id: fb6b25f1-f976-08f3-3c1e-b1d159b40d7c
document_version_independent_id: dfb98761-71ca-7e43-b51c-5a437b3241db
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/filestoragecontainercustompropertyvalue.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/filestoragecontainercustompropertyvalue
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/filestoragecontainercustompropertyvalue.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/54918a83-0404-4863-9c91-715186c1f582
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/b26f5f7a-0913-4a95-8337-ed7543902f2d
platformId: 5bdf69d3-81b0-10fa-1702-e3c377499736
---

# fileStorageContainerCustomPropertyValue resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Contains the custom property values stored in a [fileStorageContainerCustomPropertyDictionary](filestoragecontainercustompropertydictionary) resource.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| isPatternToken | Boolean | Indicates whether **value** is a `urlTemplate` pattern (for example, a token such as `{itemId}` used to configure redirect behavior when opening files), rather than a literal value that consumers must resolve before use. Optional. The default value is `false`. |
| isSearchable | Boolean | Indicates whether the custom property is searchable. Optional. The default value is `false`. |
| value | String | Value of the custom property. Required. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.fileStorageContainerCustomPropertyValue",
  "isPatternToken": "Boolean",
  "isSearchable": "Boolean",
  "value": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/filestoragecontainercustompropertyvalue?view=graph-rest-beta&accept=text/markdown)
