---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: authenticationMethod resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/authenticationmethod?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: jpettere
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-sign-in
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: An abstract type that represents an authentication method registered to a user.
ms.localizationpriority: medium
ms.reviewer: intelligentaccesspm
doc_type: resourcePageType
ms.date: 2026-10-29T00:00:00.0000000Z
locale: en-us
document_id: 7dd72172-53de-da91-751d-d01923787904
document_version_independent_id: 96fcfe38-e14d-7362-4677-198d9d73122f
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/authenticationmethod.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/authenticationmethod
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/authenticationmethod.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 34c96b9e-368d-e8d1-0cf4-6059b21e6724
---

# authenticationMethod resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

An abstract type that represents an authentication method registered to a user. An [authentication method](/en-us/azure/active-directory/authentication/concept-authentication-methods) is something used by a user to authenticate or otherwise prove their identity to the system. Some examples include password, phone (usable via SMS or voice call), FIDO2 security keys, and more.

The **authenticationMethod** resource type is an abstract type that's inherited by the following derived types:

- [emailAuthenticationMethod](emailauthenticationmethod)
- [externalAuthenticationMethod](externalauthenticationmethod)
- [fido2AuthenticationMethod](fido2authenticationmethod)
- [microsoftAuthenticatorAuthenticationMethod](microsoftauthenticatorauthenticationmethod)
- [passwordAuthenticationMethod](passwordauthenticationmethod)
- [phoneAuthenticationMethod](phoneauthenticationmethod)
- [platformCredentialAuthenticationMethod](platformcredentialauthenticationmethod)
- [qrCodePinAuthenticationMethod](qrcodepinauthenticationmethod)
- [resourceAccountKeyAuthenticationMethod](resourceaccountkeyauthenticationmethod)
- [softwareOathAuthenticationMethod](softwareoathauthenticationmethod)
- [temporaryAccessPassAuthenticationMethod](temporaryaccesspassauthenticationmethod)
- [windowsHelloForBusinessAuthenticationMethod](windowshelloforbusinessauthenticationmethod)

Important

Listing users' authentication methods only returns methods supported on this API version and registered to the user. See [Microsoft Entra authentication methods API overview](authenticationmethods-overview) for a list of currently supported methods.

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../authentication-list-methods) | [authenticationMethod](authenticationmethod) collection | Read the properties and relationships of all of a user's **authenticationMethod** objects. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| createdDateTime | DateTimeOffset | Represents the date and time when an entity was created. Read-only. |
| id | String | The identifier of this instance of an authentication method registered to this user. Read-only. |
| lastUsedDateTime | DateTimeOffset | The date and time of the authentication method's latest successful use, when usage data is available. Read-only. Nullable. The timestamp uses ISO 8601 format and is always in UTC. For example, `2026-10-28T15:30:00Z`. |

The **lastUsedDateTime** value is populated on a best-effort basis and isn't guaranteed to reflect usage in real time. It can be `null` or absent when usage data is unavailable or the authentication method doesn't support usage tracking. A `null` or absent value doesn't mean that the method was never used. Failure to retrieve usage data doesn't cause the authentication-method request to fail.

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.authenticationMethod",
  "id": "String (identifier)",
  "createdDateTime": "String (timestamp)",
  "lastUsedDateTime": "String (timestamp)"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/authenticationmethod?view=graph-rest-beta&accept=text/markdown)
