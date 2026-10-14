---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: authentication resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/authentication?view=graph-rest-1.0
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
description: Exposes authentication method states for users and relationships that represent the authentication methods supported by Microsoft Entra ID.
ms.reviewer: intelligentaccesspm
ms.localizationpriority: medium
doc_type: resourcePageType
toc.title: Authentication states
ms.date: 2026-01-06T00:00:00.0000000Z
locale: en-us
document_id: 7bf36053-15b8-175a-38ea-7859940bfed1
document_version_independent_id: a3b8b007-78b0-d083-4d44-321bf3bf73f4
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/authentication.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/authentication
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/authentication.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/5686b492-7c45-4088-8291-ecc0458747d3
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/838f4f15-80c1-4d49-b873-501fe4ed2d28
platformId: 3629854a-6a6c-726c-11a0-d1bbad6b1b18
---

# authentication resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Exposes authentication method states for users and relationships that represent the authentication methods supported by Microsoft Entra ID.

Inherits from [entity](entity).

## Methods

None.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier. Read-only. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| emailMethods | [emailAuthenticationMethod](emailauthenticationmethod) collection | The email address registered to a user for authentication. |
| externalAuthenticationMethods | [externalAuthenticationMethod](externalauthenticationmethod) collection | Represents the external MFA registered to a user for authentication using an external identity provider. |
| fido2Methods | [fido2AuthenticationMethod](fido2authenticationmethod) collection | Represents the FIDO2 security keys registered to a user for authentication. |
| methods | [authenticationMethod](authenticationmethod) collection | Represents all authentication methods registered to a user. |
| microsoftAuthenticatorMethods | [microsoftAuthenticatorAuthenticationMethod](microsoftauthenticatorauthenticationmethod) collection | The details of the Microsoft Authenticator app registered to a user for authentication. |
| operations | [longRunningOperation](longrunningoperation) collection | Represents the status of a long-running operation, such as a password reset operation. |
| passwordMethods | [passwordAuthenticationMethod](passwordauthenticationmethod) collection | Represents the password registered to a user for authentication. For security, the password itself is never returned in the object, but action can be taken to reset a password. |
| platformCredentialMethods | [platformCredentialAuthenticationMethod](platformcredentialauthenticationmethod) collection | Represents a platform credential instance registered to a user on Mac OS. |
| phoneMethods | [phoneAuthenticationMethod](phoneauthenticationmethod) collection | The phone numbers registered to a user for authentication. |
| resourceAccountKeyAuthenticationMethods | [resourceAccountKeyAuthenticationMethod](resourceaccountkeyauthenticationmethod) collection | Represents the resource account key credentials registered to a user for authentication on shared devices. |
| softwareOathMethods | [softwareOathAuthenticationMethod](softwareoathauthenticationmethod) collection | The software OATH time-based one-time password (TOTP) applications registered to a user for authentication. |
| temporaryAccessPassMethods | [temporaryAccessPassAuthenticationMethod](temporaryaccesspassauthenticationmethod) collection | Represents a Temporary Access Pass registered to a user for authentication through time-limited passcodes. |
| windowsHelloForBusinessMethods | [windowsHelloForBusinessAuthenticationMethod](windowshelloforbusinessauthenticationmethod) collection | Represents the Windows Hello for Business authentication method registered to a user for authentication. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.authentication"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/authentication?view=graph-rest-beta&accept=text/markdown)
