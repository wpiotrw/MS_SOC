---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: forwardingPolicy resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/networkaccess-forwardingpolicy?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: moti-ba
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-global-secure-access
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: A forwarding policy defines the specific traffic that is routed through the Global Secure Access services. It's then added to a forwarding profile.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2024-05-23T00:00:00.0000000Z
locale: en-us
document_id: e496ff39-51dd-bb15-29ce-3d1fd8394edc
document_version_independent_id: d7028b6d-144e-1b7e-b30f-44e313c86708
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/networkaccess-forwardingpolicy.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/networkaccess-forwardingpolicy
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/networkaccess-forwardingpolicy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 5512ebc1-ffd1-2c3e-38ca-17e51f0709b1
---

# forwardingPolicy resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph.networkaccess

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

A forwarding policy defines the specific traffic that is routed through the Global Secure Access services. It's then added to a [forwarding profile](networkaccess-forwardingprofile).

Inherits from [microsoft.graph.networkaccess.policy](networkaccess-policy).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../networkaccess-networkaccessroot-list-forwardingpolicies) | [microsoft.graph.networkaccess.forwardingPolicy](networkaccess-forwardingpolicy) collection | Get a list of the [microsoft.graph.networkaccess.forwardingPolicy](networkaccess-forwardingpolicy) objects and their properties. |
| [Get](../networkaccess-forwardingpolicy-get) | [microsoft.graph.networkaccess.forwardingPolicy](networkaccess-forwardingpolicy) | Read the properties and relationships of a [microsoft.graph.networkaccess.forwardingPolicy](networkaccess-forwardingpolicy) object. |
| [Update policy rules](../networkaccess-forwardingpolicy-updatepolicyrules) | [microsoft.graph.networkaccess.forwardingPolicy](networkaccess-forwardingpolicy) | Update the rules within a forwarding policy. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| description | String | Forwarding policy description. Inherited from [microsoft.graph.networkaccess.policy](networkaccess-policy). |
| id | String | Identifier for the forwarding policy. Inherited from [microsoft.graph.entity](entity). |
| name | String | Forwarding policy name. Inherited from [microsoft.graph.networkaccess.policy](networkaccess-policy). |
| trafficForwardingType | [microsoft.graph.networkaccess.trafficForwardingType](enums-networkaccess#trafficforwardingtype-values) | Traffic type for forwarding policy. The possible values are: `m365`, `internet`, `private`, `unknownFutureValue`, `entra`. Use the `Prefer: include-unknown-enum-members` request header to get the following value or values in this evolvable enum: `entra`. |
| version | String | Forwarding policy version. Inherited from [microsoft.graph.networkaccess.policy](networkaccess-policy). |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| policyRules | [microsoft.graph.networkaccess.policyRule](networkaccess-policyrule) collection | Represents the definition of the policy ruleset that makes up the core definition of a policy. Inherited from [microsoft.graph.networkaccess.policy](networkaccess-policy). Supports `$expand`. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.networkaccess.forwardingPolicy",
  "id": "String (identifier)",
  "name": "String",
  "description": "String",
  "version": "String",
  "trafficForwardingType": "String"
}
```