---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: relatedPerson resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/relatedperson?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: kevinbellinger
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: people
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: relatedPerson resource type
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2024-06-11T00:00:00.0000000Z
locale: en-us
document_id: 0a7303e9-fb9b-00e1-1393-bc456e6fa277
document_version_independent_id: 10b71ed7-c6ec-4487-1f06-45d193a309e6
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/relatedperson.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/relatedperson
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/relatedperson.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: da582a3d-b57a-8dbf-fbb3-884956f27acf
---

# relatedPerson resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents information about people related to information within a given entity in a [profile](profile) for a user.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| displayName | String | Name of the person. |
| relationship | String | The possible values are: `manager`, `colleague`, `directReport`, `dotLineReport`, `assistant`, `dotLineManager`, `alternateContact`, `friend`, `spouse`, `sibling`, `child`, `parent`, `sponsor`, `emergencyContact`, `other`, `unknownFutureValue`. |
| relationshipLabel | String | Information (free-text) describing the relationship between the user and the related person. This property provides additional context beyond the predefined relationship values and can be used by clients, including AI-powered experiences, to better understand and reason about the relationship. |
| userId | String | The user's directory object ID (Microsoft Entra ID or CID). |
| userPrincipalName | String | Email address or reference to person within the organization. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "displayName": "String",
  "relationship": "String",
  "relationshipLabel": "String",
  "userId": "String",
  "userPrincipalName": "String"
}
```