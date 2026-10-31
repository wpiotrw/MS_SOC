---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: entraDriftIdentityInfo resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/entradriftidentityinfo?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: suhanigupta
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents identity information from Microsoft Entra in an access drift record.
ms.date: 2026-09-04T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: b94e052f-d4a6-12d4-96b6-03b9ceff3c59
document_version_independent_id: 6e63b4e3-332f-411c-75f1-e05860ffa066
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/entradriftidentityinfo.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/entradriftidentityinfo
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/entradriftidentityinfo.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: f9706b41-28f0-1dc5-fc15-6486d92e011f
---

# entraDriftIdentityInfo resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents identity information from Microsoft Entra in an access drift record.

This object can be returned in the **identities** relationship of [accessDriftDetail](accessdriftdetail).

Inherits from [driftIdentityInfo](driftidentityinfo).

## Methods

None.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| displayName | String | The display name of the identity. Inherited from [driftIdentityInfo](driftidentityinfo). |
| identifier | String | The unique identifier for the identity. Inherited from [driftIdentityInfo](driftidentityinfo). |
| identityType | String | The type of identity. The possible values are `user` and `group`. |
| principalName | String | The principal name of the identity. Inherited from [driftIdentityInfo](driftidentityinfo). |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.entraDriftIdentityInfo",
  "identifier": "String (identifier)",
  "identityType": "String",
  "principalName": "String",
  "displayName": "String"
}
```