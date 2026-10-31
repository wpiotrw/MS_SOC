---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: federatedTokenValidationPolicy resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/federatedtokenvalidationpolicy?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: vimrang
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-sign-in
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a policy to control enabling or disabling validation of federation authentication tokens.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-03-30T00:00:00.0000000Z
locale: en-us
document_id: 38efcebf-bbac-5696-e1ae-8b5e5d739f45
document_version_independent_id: dbc4b906-338f-2fc5-1f0e-cd02d19f7ecb
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/federatedtokenvalidationpolicy.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/federatedtokenvalidationpolicy
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/federatedtokenvalidationpolicy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1cfdec6-b0c3-4209-818c-736879856e0e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d0723c1-cf38-4c30-ab3d-5df787b33270
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 5bd07a8e-e6c8-0292-5db6-975ce33879d0
---

# federatedTokenValidationPolicy resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents a policy to control enabling or disabling validation of federation authentication tokens. It allows matching an on-premises federated account and a mapped Microsoft Entra ID account's root domain. When enabled, Microsoft Entra ID rejects an authentication request if the on-premises federated account and the mapped Microsoft Entra ID account's root domain don't match.

Inherits from [directoryObject](directoryobject).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [Get](../federatedtokenvalidationpolicy-get) | [federatedTokenValidationPolicy](federatedtokenvalidationpolicy) | Read the properties and relationships of a [federatedTokenValidationPolicy](federatedtokenvalidationpolicy) object. |
| [Update](../federatedtokenvalidationpolicy-update) | [federatedTokenValidationPolicy](federatedtokenvalidationpolicy) | Update the properties of a [federatedTokenValidationPolicy](federatedtokenvalidationpolicy) object. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| deletedDateTime | DateTimeOffset | Date and time when this object was deleted. Always `null` when the object wasn't deleted. Inherited from [directoryObject](directoryobject). |
| id | String | The unique identifier for the object. Key. Not nullable. Read-only. Inherited from [directoryObject](directoryobject). |
| validatingDomains | [validatingDomains](validatingdomains) | Verified Microsoft Entra ID domains that Microsoft Entra ID validates that the federated account's root domain matches with the mapped Microsoft Entra account's root domain. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.federatedTokenValidationPolicy",
  "id": "String (identifier)",
  "deletedDateTime": "String (timestamp)",
  "validatingDomains": {
    "@odata.type": "#microsoft.graph.validatingDomains",
    "rootDomains": "String"
  }
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/federatedtokenvalidationpolicy?view=graph-rest-beta&accept=text/markdown)
