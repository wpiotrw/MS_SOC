---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: directoryRoleManagementDeletedItemContainer resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/directoryrolemanagementdeleteditemcontainer?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: simransaxena21
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-directory-management
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Contains soft-deleted custom role definitions for Microsoft Entra directory role management.
ms.date: 2026-10-07T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 2c965a63-e22b-3f0f-c31a-231dc15d46d8
document_version_independent_id: dc9853e4-af3c-1003-622e-fddac7a52308
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/directoryrolemanagementdeleteditemcontainer.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/directoryrolemanagementdeleteditemcontainer
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/directoryrolemanagementdeleteditemcontainer.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 827da2df-b551-3a74-22bf-f551f955e80f
---

# directoryRoleManagementDeletedItemContainer resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Contains soft-deleted custom [unifiedRoleDefinition](unifiedroledefinition) objects for Microsoft Entra directory role management. Use this container to list, inspect, restore, or permanently delete custom role definitions that have been soft-deleted.

Inherits from [entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List roleDefinitions](../directoryrolemanagementdeleteditemcontainer-list-roledefinitions) | [unifiedRoleDefinition](unifiedroledefinition) collection | List soft-deleted custom role definitions. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| id | String | The unique identifier for the container. Inherited from [entity](entity). |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| roleDefinitions | [unifiedRoleDefinition](unifiedroledefinition) collection | The soft-deleted custom role definitions in the directory. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.directoryRoleManagementDeletedItemContainer",
  "id": "String (identifier)"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/directoryrolemanagementdeleteditemcontainer?view=graph-rest-beta&accept=text/markdown)
