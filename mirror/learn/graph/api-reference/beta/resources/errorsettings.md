---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: errorSettings resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/errorsettings?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: zhengnlu
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents settings that control enforcement behavior when policy evaluation can't be completed.
ms.date: 2026-09-23T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 36c3019b-7a4c-0080-8dbf-84793ca81d21
document_version_independent_id: 6cce4d5e-d354-8b06-4219-993d3867be88
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/errorsettings.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/errorsettings
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/errorsettings.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 5d8329c9-a64f-ea1c-dc46-4b5d0ce12d82
---

# errorSettings resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents settings that control enforcement behavior when policy evaluation can't be completed. This type is used by the **errorSettings** property of [policyConfiguration](policyconfiguration).

## Methods

None.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| errorAction | [errorActions](enums#erroractions-values) | The action that the enforcement plane takes when policy evaluation can't be completed. This flagged enumeration allows multiple members to be selected simultaneously. The possible values are: `none`, `audit`, `block`, `unknownFutureValue`. Don't combine `none` with another value. |
| isEnabled | Boolean | Indicates whether Secure by Default is enabled for the protection scope. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.errorSettings",
  "errorAction": "String",
  "isEnabled": "Boolean"
}
```