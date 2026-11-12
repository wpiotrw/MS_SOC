---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: resourceQuota resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/resourcequota?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: marcotuliorr
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-directory-management
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a quota configuration for a resource type in a Microsoft Entra organization.
ms.date: 2026-08-25T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 5d1cccac-10c1-fa43-a60d-3c765bb651a4
document_version_independent_id: fe2daef8-01e8-5011-279a-9b5f52fd996f
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/resourcequota.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/resourcequota
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/resourcequota.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 6065ac96-3daf-6ab7-bf52-7578a6fc7cf8
---

# resourceQuota resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents a quota configuration for a resource type in a Microsoft Entra organization. Configure this object through the **resourceQuotas** property of an [organization](organization) resource.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| maxPercentage | Int32 | The maximum percentage of the organization's `directorySizeQuota.total` that this resource type can consume. The value must be between `0` and `100`. A value of `0` blocks creation of new resources of this type. If omitted for supported resource types, the default is `80`. |
| resourceType | [resourceQuotaType](enums#resourcequotatype-values) | The resource type to which the quota applies. Each value must be unique within the organization's **resourceQuotas** collection. The possible values are: `agentIdentityBlueprint`, `agentIdentity`, `managedIdentity`, `unknownFutureValue`. |
| total | Int32 | The effective maximum number of resources allowed, calculated from `directorySizeQuota.total` and **maxPercentage**. This value is read-only and changes when the organization's overall quota changes. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.resourceQuota",
  "resourceType": "String",
  "maxPercentage": "Int32",
  "total": "Int32"
}
```