---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: forwardingProfile resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/networkaccess-forwardingprofile?view=graph-rest-beta
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
description: A forwarding profile determines which types of traffic are routed through the Global Secure Access services and which ones are skipped. The handling of specific traffic is determined by the forwarding policies that are added to the forwarding profile.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2024-08-01T00:00:00.0000000Z
locale: en-us
document_id: 9bea1046-6bff-a36e-17cf-4448e4873e9d
document_version_independent_id: da443956-d177-574f-14d2-2742f038f401
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/networkaccess-forwardingprofile.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/networkaccess-forwardingprofile
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/networkaccess-forwardingprofile.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: a974a835-f9e1-ce40-4c70-0257349d1188
---

# forwardingProfile resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph.networkaccess

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

A forwarding profile determines which types of traffic are routed through the Global Secure Access services and which ones are skipped. The handling of specific traffic is determined by the forwarding policies that are added to the forwarding profile.

Inherits from [microsoft.graph.networkaccess.profile](networkaccess-profile).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../networkaccess-networkaccessroot-list-forwardingprofiles) | [microsoft.graph.networkaccess.forwardingProfile](networkaccess-forwardingprofile) collection | Get a list of the [microsoft.graph.networkaccess.forwardingProfile](networkaccess-forwardingprofile) objects and their properties. |
| [Get](../networkaccess-forwardingprofile-get) | [microsoft.graph.networkaccess.forwardingProfile](networkaccess-forwardingprofile) | Read the properties and relationships of a [microsoft.graph.networkaccess.forwardingProfile](networkaccess-forwardingprofile) object. |
| [List forwarding profiles for branch (deprecated)](../networkaccess-branchsite-list-forwardingprofiles) | [microsoft.graph.networkaccess.forwardingProfile](networkaccess-forwardingprofile) collection | Get a list of the [microsoft.graph.networkaccess.forwardingProfile](networkaccess-forwardingprofile) objects for a branch and their properties. |
| [Create forwarding profile for branch (deprecated)](../networkaccess-branchsite-post-forwardingprofiles) | [microsoft.graph.networkaccess.forwardingProfile](networkaccess-forwardingprofile) | Create a [microsoft.graph.networkaccess.forwardingProfile](networkaccess-forwardingprofile) object for a branch. |
| [Update forwarding profile for branch (deprecated)](../networkaccess-forwardingprofile-update) | None | Update the properties of a [microsoft.graph.networkaccess.forwardingProfile](networkaccess-forwardingprofile) object for a branch. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| associations | [microsoft.graph.networkaccess.association](networkaccess-association) collection | Specifies the users, groups, devices, and remote networks whose traffic is associated with the given traffic forwarding profile. |
| description | String | Profile description. Inherited from [microsoft.graph.networkaccess.profile](networkaccess-profile). |
| id | String | Identifier for the profile. Inherited from [microsoft.graph.entity](entity). |
| lastModifiedDateTime | DateTimeOffset | Profile last modified time. Inherited from [microsoft.graph.networkaccess.profile](networkaccess-profile). |
| name | String | Profile name. Inherited from [microsoft.graph.networkaccess.profile](networkaccess-profile). |
| priority | Int32 | Profile priority. |
| state | microsoft.graph.networkaccess.status | Determines whether the profile is active or inactive. Inherited from [microsoft.graph.networkaccess.profile](networkaccess-profile). The possible values are: `enabled`, `disabled`. |
| trafficForwardingType | [microsoft.graph.networkaccess.trafficForwardingType](enums-networkaccess#trafficforwardingtype-values) | Profile traffic type. The possible values are: `m365`, `internet`, `private`, `unknownFutureValue`, `entra`. Use the `Prefer: include-unknown-enum-members` request header to get the following value or values in this evolvable enum: `entra`. |
| version | String | Version. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| policies | [microsoft.graph.networkaccess.policyLink](networkaccess-policylink) collection | The collection of policies that are linked to this traffic forwarding profile. Inherited from [microsoft.graph.networkaccess.profile](networkaccess-profile). Supports `$expand` and a nested `$expand` to retrieve the policy. That is `/forwardingProfiles?$expand=policies($expand=policy)`. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.networkaccess.forwardingProfile",
  "id": "String (identifier)",
  "name": "String",
  "description": "String",
  "state": "String",
  "version": "String",
  "lastModifiedDateTime": "String (timestamp)",
  "trafficForwardingType": "String",
  "associations": [
    {
      "@odata.type": "microsoft.graph.networkaccess.association"
    }
  ],
  "priority": "Integer"
}
```