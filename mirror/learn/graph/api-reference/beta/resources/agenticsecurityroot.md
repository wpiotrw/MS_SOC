---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: agenticSecurityRoot resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/agenticsecurityroot?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: berver
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Provides access to playbook definitions and agentic security sessions.
ms.date: 2026-10-22T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: f273a11f-d452-947b-1ef0-a16efcc9c8d8
document_version_independent_id: 7c0e45f3-070a-09af-18d0-a7af15db31ee
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/agenticsecurityroot.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/agenticsecurityroot
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/agenticsecurityroot.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 8fcdae5e-2043-7213-9ad8-88393b33bf73
---

# agenticSecurityRoot resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Provides access to playbook definitions and agentic security sessions. Use its child collections; reading, updating, or deleting this container directly isn't supported.

Inherits from [entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List playbookDefinitions](../agenticsecurityroot-list-playbookdefinitions) | [playbookDefinition](playbookdefinition) collection | Get the playbook catalog. |
| [List sessions](../agenticsecurityroot-list-sessions) | [investigationSession](investigationsession) collection | Get the caller's sessions. |
| [Create session](../agenticsecurityroot-post-sessions) | [investigationSession](investigationsession) | Start a playbook execution. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| id | String | The unique, read-only identifier of the resource. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| playbookDefinitions | [playbookDefinition](playbookdefinition) collection | The read-only playbook catalog. Supports list and keyed GET with `$select`. Doesn't support `$filter`, `$orderby`, `$search`, `$expand`, `$count`, `$top`, `$skip`, or delta tracking. |
| sessions | [investigationSession](investigationsession) collection | The agentic sessions visible to the caller. Supports list with `$filter` on **status** (`eq`, `or`, `in`), `$top`, and `$select`; session creation; and keyed reads. Doesn't support `$count`, `$orderby`, `$search`, `$expand`, `$skip`, or delta tracking. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.agenticSecurityRoot",
  "id": "String (identifier)"
}
```