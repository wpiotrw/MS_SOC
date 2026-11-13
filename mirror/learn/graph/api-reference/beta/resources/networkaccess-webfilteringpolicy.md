---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: webFilteringPolicy resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/networkaccess-webfilteringpolicy?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: mialdrid
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-global-secure-access
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Defines a set of web filtering rules and default behavior for traffic evaluated by Global Secure Access.
ms.date: 2026-09-09T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 5dc66f60-7ac2-88a8-edcb-350513af3905
document_version_independent_id: fcac7fe2-cbc8-758f-5a7f-3dc7eacca88b
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/networkaccess-webfilteringpolicy.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/networkaccess-webfilteringpolicy
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/networkaccess-webfilteringpolicy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 6950c876-59f5-6a55-3a3e-e022bf23fc7a
---

# webFilteringPolicy resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph.networkaccess

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Defines a set of web filtering rules and the default action that Global Secure Access applies to traffic that does not match a rule.

Inherits from [microsoft.graph.networkaccess.policy](networkaccess-policy).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../networkaccess-networkaccessroot-list-webfilteringpolicies) | [microsoft.graph.networkaccess.webFilteringPolicy](networkaccess-webfilteringpolicy) collection | Get a list of the webFilteringPolicy objects and their properties. |
| [Create](../networkaccess-networkaccessroot-post-webfilteringpolicies) | [microsoft.graph.networkaccess.webFilteringPolicy](networkaccess-webfilteringpolicy) | Create a new webFilteringPolicy object. |
| [Get](../networkaccess-webfilteringpolicy-get) | [microsoft.graph.networkaccess.webFilteringPolicy](networkaccess-webfilteringpolicy) | Read the properties and relationships of [microsoft.graph.networkaccess.webFilteringPolicy](networkaccess-webfilteringpolicy) object. |
| [Update](../networkaccess-webfilteringpolicy-update) | [microsoft.graph.networkaccess.webFilteringPolicy](networkaccess-webfilteringpolicy) | Update the properties of a webFilteringPolicy object. |
| [Delete](../networkaccess-networkaccessroot-delete-webfilteringpolicies) | None | Delete a webFilteringPolicy object. |
| [List policyRules](../networkaccess-webfilteringpolicy-list-policyrules) | [microsoft.graph.networkaccess.webFilteringRule](networkaccess-webfilteringrule) collection | Get the rules associated with the web filtering policy. |
| [Create policyRule](../networkaccess-webfilteringpolicy-post-policyrules) | [microsoft.graph.networkaccess.webFilteringRule](networkaccess-webfilteringrule) | Create a new webFilteringRule object. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| description | String | The description of the web filtering policy. Inherited from [microsoft.graph.networkaccess.policy](networkaccess-policy). |
| id | String | The unique identifier for the web filtering policy. Inherited from [microsoft.graph.entity](entity). |
| lastModifiedDateTime | DateTimeOffset | The date and time when the web filtering policy was last modified. Read-only. |
| name | String | The display name of the web filtering policy. Inherited from [microsoft.graph.networkaccess.policy](networkaccess-policy). |
| settings | [microsoft.graph.networkaccess.webFilteringPolicySettings](networkaccess-webfilteringpolicysettings) | The default settings for the web filtering policy. |
| version | String | The version of the web filtering policy. Inherited from [microsoft.graph.networkaccess.policy](networkaccess-policy). |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| policyRules | [microsoft.graph.networkaccess.policyRule](networkaccess-policyrule) collection | The rules evaluated as part of the policy. Inherited from [microsoft.graph.networkaccess.policy](networkaccess-policy). |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.networkaccess.webFilteringPolicy",
  "id": "String (identifier)",
  "name": "String",
  "description": "String",
  "version": "String",
  "lastModifiedDateTime": "String (timestamp)",
  "settings": {
    "@odata.type": "microsoft.graph.networkaccess.webFilteringPolicySettings"
  }
}
```