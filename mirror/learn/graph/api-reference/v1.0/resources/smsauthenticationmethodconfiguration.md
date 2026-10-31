---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: smsAuthenticationMethodConfiguration resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/smsauthenticationmethodconfiguration?view=graph-rest-1.0
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
description: Represents a text message authentication methods policy.
ms.reviewer: intelligentaccesspm
ms.localizationpriority: medium
doc_type: resourcePageType
toc.title: SMS
ms.date: 2024-07-22T00:00:00.0000000Z
locale: en-us
document_id: 88ec6ccf-a6cf-41de-c023-cdfbc87902d9
document_version_independent_id: 85b8cb09-1ae0-6455-098a-63039db32c09
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/smsauthenticationmethodconfiguration.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/smsauthenticationmethodconfiguration
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/smsauthenticationmethodconfiguration.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 8ed291a7-a0d8-6e39-c419-ea0d3ab38acc
---

# smsAuthenticationMethodConfiguration resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents a text message authentication methods policy. Authentication methods policies define configuration settings and users or groups that are enabled to use the authentication method.

Inherits from [authenticationMethodConfiguration](authenticationmethodconfiguration).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [Get](../smsauthenticationmethodconfiguration-get) | [smsAuthenticationMethodConfiguration](smsauthenticationmethodconfiguration) | Read the properties and relationships of an smsAuthenticationMethodConfiguration object. |
| [Update](../smsauthenticationmethodconfiguration-update) | None | Update the properties of an smsAuthenticationMethodConfiguration object. |
| [Delete](../smsauthenticationmethodconfiguration-delete) | None | Reverts the smsAuthenticationMethodConfiguration object to its default configuration. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| excludeTargets | [excludeTarget](excludetarget) collection | Groups of users that are excluded from the policy. |
| id | String | The authentication method policy identifier. |
| state | authenticationMethodState | The possible values are: `enabled`, `disabled`. |
| telecomProviderSettings | [telecomProviderSettings](telecomprovidersettings) | Settings for routing SMS authentication traffic through a telecom provider integration. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| includeTargets | [smsAuthenticationMethodTarget](smsauthenticationmethodtarget) collection | A collection of groups that are enabled to use the authentication method. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.smsAuthenticationMethodConfiguration",
  "id": "String (identifier)",
  "state": "String",
  "excludeTargets": [
    {
      "@odata.type": "microsoft.graph.excludeTarget"
    }
  ],
  "telecomProviderSettings": {
    "@odata.type": "microsoft.graph.telecomProviderSettings"
  }
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/smsauthenticationmethodconfiguration?view=graph-rest-beta&accept=text/markdown)
