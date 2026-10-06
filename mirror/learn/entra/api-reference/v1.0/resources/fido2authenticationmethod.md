---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: fido2AuthenticationMethod resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/fido2authenticationmethod?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: hanki71
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-sign-in
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: A representation of a passkey (FIDO2) registered to a user. Passkey (FIDO2) is a sign-in authentication method.
ms.reviewer: intelligentaccesspm
ms.localizationpriority: medium
doc_type: resourcePageType
toc.title: FIDO2
ms.date: 2026-03-04T00:00:00.0000000Z
locale: en-us
document_id: 1ad8f4f8-9cbb-399f-e124-7383f3c7b6d2
document_version_independent_id: 1b582073-59e7-3839-dbf2-22f07a145bf2
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/fido2authenticationmethod.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/fido2authenticationmethod
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/fido2authenticationmethod.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 67e3222f-7a66-9068-8913-5172416e69d7
---

# fido2AuthenticationMethod resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

A representation of a passkey (FIDO2) registered to a user. Passkey (FIDO2) is a sign-in authentication method.

This is a derived type that inherits from the [authenticationMethod](authenticationmethod) resource type.

Note

This resource has a [known issue](/en-us/graph/known-issues#fido2-provisioning-api-requires-self-service-setup-to-be-enabled) related to creating FIDO2 authentication methods that requires **Allow self-service setup** to be enabled in the FIDO2 authentication method policy.

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../fido2authenticationmethod-list) | [fido2AuthenticationMethod](fido2authenticationmethod) collection | Retrieve a list of a user's **fido2AuthenticationMethod** objects and their properties. |
| [Create](../authentication-post-fido2methods) | [fido2AuthenticationMethod](fido2authenticationmethod) | Create a new **fido2AuthenticationMethod** object for a user. |
| [Get](../fido2authenticationmethod-get) | [fido2AuthenticationMethod](fido2authenticationmethod) | Read the properties and relationships of a user's **fido2AuthenticationMethod** object. |
| [Delete](../fido2authenticationmethod-delete) | None | Delete a user's **fido2AuthenticationMethod** object. |
| [Creation options](../fido2authenticationmethod-creationoptions) | [webauthnCredentialCreationOptions](webauthncredentialcreationoptions) | Retrieve creation options required to generate and register a passkey for a user. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| aaGuid | String | Authenticator Attestation GUID, an identifier that indicates the type (such as make and model) of the authenticator. |
| attestationCertificates | String collection | The attestation certificate or certificates attached to this passkey. |
| attestationLevel | attestationLevel | The attestation level of this passkey (FIDO2). The possible values are: `attested`, `notAttested`, `unknownFutureValue`. |
| createdDateTime | DateTimeOffset | The timestamp when this key was registered to the user. Inherited from [authenticationMethod](authenticationmethod). |
| displayName | String | The display name of the key as given by the user. |
| id | String | The authentication method identifier. |
| model | String | The manufacturer-assigned model of the FIDO2 passkey. |
| passkeyType | passkeyType | The type of passkey. The possible values are: `deviceBound`, `synced`, `unknownFutureValue`. |
| publicKeyCredential | [webauthnPublicKeyCredential](webauthnpublickeycredential) | Contains the WebAuthn public key credential information being registered. This property is used only for write requests and isn't returned on read operations. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.fido2AuthenticationMethod",
  "aaGuid": "String",
  "attestationCertificates": [
    "String"
  ],
  "attestationLevel": "String",
  "createdDateTime": "String (timestamp)",
  "displayName": "String",
  "id": "String (identifier)",
  "model": "String",
  "passkeyType": "String",
  "publicKeyCredential": {
    "@odata.type": "microsoft.graph.webauthnPublicKeyCredential"
  }
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/fido2authenticationmethod?view=graph-rest-beta&accept=text/markdown)
