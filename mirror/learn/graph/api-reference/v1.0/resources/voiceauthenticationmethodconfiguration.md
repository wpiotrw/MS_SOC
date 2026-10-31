---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: voiceAuthenticationMethodConfiguration resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/voiceauthenticationmethodconfiguration?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: luc-msft
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-sign-in
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a voice call authentication methods policy.
ms.reviewer: intelligentaccesspm
ms.localizationpriority: medium
doc_type: resourcePageType
toc.title: Voice
ms.date: 2024-07-22T00:00:00.0000000Z
locale: en-us
document_id: 8e349cc5-490b-5124-a570-5ace22ad8fbc
document_version_independent_id: 365a3342-99fe-2324-1f22-282348e315d7
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/voiceauthenticationmethodconfiguration.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/voiceauthenticationmethodconfiguration
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/voiceauthenticationmethodconfiguration.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
2PlusCloud:
- Azure
- M365
- Power
__autotagging_hash:
- D939C5FFC3323BFD9F1C3012E46DD96985416C0C6217877B728581A82D3436E2
platformId: 875cb739-5889-dca9-8bf6-7465fc5ac0cf
---

# voiceAuthenticationMethodConfiguration resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents a voice call authentication methods policy. Authentication methods policies define configuration settings and users or groups that are enabled to use the authentication method.

Inherits from [authenticationMethodConfiguration](authenticationmethodconfiguration).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [Get](../voiceauthenticationmethodconfiguration-get) | [voiceAuthenticationMethodConfiguration](voiceauthenticationmethodconfiguration) | Read the properties and relationships of a [voiceAuthenticationMethodConfiguration](voiceauthenticationmethodconfiguration) object. |
| [Update](../voiceauthenticationmethodconfiguration-update) | None | Update the properties of a [voiceAuthenticationMethodConfiguration](voiceauthenticationmethodconfiguration) object. |
| [Delete](../voiceauthenticationmethodconfiguration-delete) | None | Revert the [voiceAuthenticationMethodConfiguration](voiceauthenticationmethodconfiguration) object to its default configuration. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| excludeTargets | [excludeTarget](excludetarget) collection | Groups of users that are excluded from the policy. |
| id | String | The authentication method policy identifier. |
| isOfficePhoneAllowed | Boolean | `true` if users can register office phones, otherwise, `false`. |
| state | authenticationMethodState | Represents whether users can register this authentication method. The possible values are: `enabled`, `disabled`. |
| telecomProviderSettings | [telecomProviderSettings](telecomprovidersettings) | Settings for routing voice authentication traffic through a telecom provider integration. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| includeTargets | [authenticationMethodTarget](authenticationmethodtarget) collection | A collection of groups that are enabled to use the authentication method. Expanded by default. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.voiceAuthenticationMethodConfiguration",
  "id": "String (identifier)",
  "state": "String",
  "excludeTargets": [
    {
      "@odata.type": "microsoft.graph.excludeTarget"
    }
  ],
  "isOfficePhoneAllowed": "Boolean",
  "telecomProviderSettings": {
    "@odata.type": "microsoft.graph.telecomProviderSettings"
  }
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/voiceauthenticationmethodconfiguration?view=graph-rest-beta&accept=text/markdown)
