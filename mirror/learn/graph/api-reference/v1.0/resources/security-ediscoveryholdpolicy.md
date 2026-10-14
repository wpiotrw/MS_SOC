---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: ediscoveryHoldPolicy resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/security-ediscoveryholdpolicy?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: SeunginLyu
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: ediscovery
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: ediscoveryHoldPolicy resource type
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2024-10-28T00:00:00.0000000Z
locale: en-us
document_id: d8c4cf81-634a-4f41-311f-3b46cc131012
document_version_independent_id: 16818711-d44d-b578-5aa9-89736d3557a8
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/security-ediscoveryholdpolicy.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/security-ediscoveryholdpolicy
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/security-ediscoveryholdpolicy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: be33ad27-fef2-70f1-be10-c14366c30a71
---

# ediscoveryHoldPolicy resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.security

Represents a legal hold policy. Legal holds are holds that are tied to an eDiscovery case. Legal holds should not be confused with retention holds, which are used to control retention policies for Microsoft 365 content. eDiscovery legal holds are for holding content indefinitely for litigation, internal investigations, and other legal actions where content needs to be protected against deletion. For more information, see [Manage holds in eDiscovery (Premium)](/en-us/microsoft-365/compliance/managing-holds)

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../security-ediscoverycase-list-legalholds) | [microsoft.graph.security.ediscoveryHoldPolicy](security-ediscoveryholdpolicy) collection | Get a list of the [ediscoveryHoldPolicy](security-ediscoveryholdpolicy) objects and their properties. |
| [Create](../security-ediscoverycase-post-legalholds) | [microsoft.graph.security.ediscoveryHoldPolicy](security-ediscoveryholdpolicy) | Create a new [ediscoveryHoldPolicy](security-ediscoveryholdpolicy) object. |
| [Get](../security-ediscoveryholdpolicy-get) | [microsoft.graph.security.ediscoveryHoldPolicy](security-ediscoveryholdpolicy) | Read the properties and relationships of an [ediscoveryHoldPolicy](security-ediscoveryholdpolicy) object. |
| [Update](../security-ediscoveryholdpolicy-update) | [microsoft.graph.security.ediscoveryHoldPolicy](security-ediscoveryholdpolicy) | Update the properties of an [ediscoveryHoldPolicy](security-ediscoveryholdpolicy) object. |
| [Delete](../security-ediscoverycase-delete-legalholds) | None | Delete an [ediscoveryHoldPolicy](security-ediscoveryholdpolicy) object. |
| [Retry policy](../security-ediscoveryholdpolicy-retrypolicy) | None | Trigger a retry of an [eDiscovery hold policy](security-ediscoveryholdpolicy). |
| **Site sources** |  |  |
| [List](../security-ediscoveryholdpolicy-list-sitesources) | [microsoft.graph.security.siteSource](security-sitesource) collection | Get a list of the [siteSource](security-sitesource) objects associated with an [ediscoveryHoldPolicy](security-ediscoveryholdpolicy). |
| [Create](../security-ediscoveryholdpolicy-post-sitesources) | [microsoft.graph.security.siteSource](security-sitesource) | Create a new [siteSource](security-sitesource) object. |
| [Delete](../security-ediscoveryholdpolicy-delete-sitesources) | None | Delete a [siteSource](security-sitesource) object associated with an [ediscoveryHoldPolicy](security-ediscoveryholdpolicy). |
| **User sources** |  |  |
| [List](../security-ediscoveryholdpolicy-list-usersources) | [microsoft.graph.security.userSource](security-usersource) collection | Get a list of the [userSource](security-usersource) objects associated with an [ediscoveryHoldPolicy](security-ediscoveryholdpolicy). |
| [Create](../security-ediscoveryholdpolicy-post-usersources) | [microsoft.graph.security.userSource](security-usersource) | Create a new [userSource](security-usersource) object. |
| [Delete](../security-ediscoveryholdpolicy-delete-usersources) | None | Delete a [userSource](security-usersource) object associated with an [ediscoveryHoldPolicy](security-ediscoveryholdpolicy). |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| contentQuery | String | KQL query that specifies content to be held in the specified locations. To learn more, see [Keyword queries and search conditions for Content Search and eDiscovery](/en-us/microsoft-365/compliance/keyword-queries-and-search-conditions). To hold all content in the specified locations, leave **contentQuery** blank. |
| createdBy | [identitySet](identityset) | The user who created the legal hold. |
| createdDateTime | DateTimeOffset | The date and time the legal hold was created. |
| description | String | The legal hold description. |
| displayName | String | The display name of the legal hold. |
| errors | String collection | Lists any errors that happened while placing the hold. |
| id | String | The ID for the eDiscovery case. Read-only. Inherited from [entity](entity). |
| isEnabled | Boolean | Indicates whether the hold is enabled and actively holding content. |
| lastModifiedBy | [identitySet](identityset) | the user who last modified the legal hold. |
| lastModifiedDateTime | DateTimeOffset | The date and time the legal hold was last modified. |
| status | microsoft.graph.security.policyStatus | The status of the legal hold. The possible values are: `Pending`, `Error`, `Success`. |

### policyStatus values

| Member | Description |
| --- | --- |
| Pending | The hold distribution process is in progress. |
| Error | There was an error when the hold was applied. |
| Success | The hold was successfully applied and is holding the specified content. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| siteSources | [microsoft.graph.security.siteSource](security-sitesource) collection | Data sources that represent SharePoint sites. |
| userSources | [microsoft.graph.security.userSource](security-usersource) collection | Data sources that represent Exchange mailboxes. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.security.ediscoveryHoldPolicy",
  "id": "String (identifier)",
  "displayName": "String",
  "description": "String",
  "createdBy": {
    "@odata.type": "microsoft.graph.identitySet"
  },
  "createdDateTime": "String (timestamp)",
  "lastModifiedBy": {
    "@odata.type": "microsoft.graph.identitySet"
  },
  "lastModifiedDateTime": "String (timestamp)",
  "status": "String",
  "isEnabled": "Boolean",
  "contentQuery": "String",
  "errors": [
    "String"
  ]
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/security-ediscoveryholdpolicy?view=graph-rest-beta&accept=text/markdown)
