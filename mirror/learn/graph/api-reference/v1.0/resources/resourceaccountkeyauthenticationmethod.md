---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: resourceAccountKeyAuthenticationMethod resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/resourceaccountkeyauthenticationmethod?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: akgoel
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-sign-in
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a resource account key credential that enables a shared device to sign in to Microsoft Entra ID without user interaction.
ms.date: 2026-09-25T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 9c80528a-248e-f2ba-a27e-0f2297516b59
document_version_independent_id: d96793ff-eb0a-629d-1476-efedfc6addb9
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/resourceaccountkeyauthenticationmethod.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/resourceaccountkeyauthenticationmethod
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/resourceaccountkeyauthenticationmethod.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 684870b2-8265-6ea8-b128-4a2046c28afc
---

# resourceAccountKeyAuthenticationMethod resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents a resource account key credential registered on a shared device (such as a Teams Meeting Room or Teams phone) for passwordless authentication. Resource account keys enable shared devices to silently sign in to Microsoft Entra ID without user interaction.

Inherits from [authenticationMethod](authenticationmethod).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../authentication-list-resourceaccountkeyauthenticationmethods) | [resourceAccountKeyAuthenticationMethod](resourceaccountkeyauthenticationmethod) collection | Get a list of the resourceAccountKeyAuthenticationMethod objects and their properties. |
| [Get](../resourceaccountkeyauthenticationmethod-get) | [resourceAccountKeyAuthenticationMethod](resourceaccountkeyauthenticationmethod) | Read the properties and relationships of a resourceAccountKeyAuthenticationMethod object. |
| [Delete](../resourceaccountkeyauthenticationmethod-delete) | None | Delete a resourceAccountKeyAuthenticationMethod object. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| createdDateTime | DateTimeOffset | The date and time when the resource account key was registered. Inherited from [authenticationMethod](authenticationmethod). |
| displayName | String | The display name of the resource account key credential as shown in the Teams Room interface. |
| id | String | A unique identifier for this instance of an authentication method. Inherited from [entity](entity). |
| isUsable | Boolean | Indicates whether the method is usable for sign-in. **Returned by default.** |
| lastUsedDateTime | DateTimeOffset | The date and time when this authentication method was last used for sign-in. **Requires `$select`.** Inherited from [authenticationMethod](authenticationmethod). |
| methodUsabilityReason | String | The reason for the usability state. Possible values are: `EnabledByPolicy`, `DisabledByPolicy`. **Returned by default.** |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| device | [device](device) | The registered device on which this resource account key resides. Supports `$expand`. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.resourceAccountKeyAuthenticationMethod",
  "id": "String (identifier)",
  "createdDateTime": "String (timestamp)",
  "displayName": "String",
  "isUsable": "Boolean",
  "lastUsedDateTime": "String (timestamp)",
  "methodUsabilityReason": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/resourceaccountkeyauthenticationmethod?view=graph-rest-beta&accept=text/markdown)
