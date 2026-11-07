---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: telecomProviderSettings resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/telecomprovidersettings?view=graph-rest-1.0
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
description: Represents configuration for routing SMS and voice authentication traffic through a telecom provider integration.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-10-21T00:00:00.0000000Z
locale: en-us
document_id: 6d0b3d82-44c1-57fc-141c-60d91f5e84f9
document_version_independent_id: df39c1ec-5845-36ce-a128-a98ff86c0e0b
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/telecomprovidersettings.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/telecomprovidersettings
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/telecomprovidersettings.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 4a93b0e2-6736-855e-bf3a-c4e61ea2a531
---

# telecomProviderSettings resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents configuration for routing SMS and voice authentication traffic through a telecom provider integration. This complex type is used by the **telecomProviderSettings** property of the [smsAuthenticationMethodConfiguration](smsauthenticationmethodconfiguration) and [voiceAuthenticationMethodConfiguration](voiceauthenticationmethodconfiguration) resources.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| appId | Guid | The application (client) ID used to authenticate to the telecom provider. |
| isEvaluationModeEnabled | Boolean | `true` to run the telecom provider integration in evaluation (nonenforcing) mode; otherwise, `false`. |
| migrationPercentage | Int32 | The percentage of authentication traffic routed to the telecom provider. Valid values range from 0 through 100. |
| url | String | The endpoint URL of the telecom provider integration. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.telecomProviderSettings",
  "url": "String",
  "appId": "Guid",
  "isEvaluationModeEnabled": "Boolean",
  "migrationPercentage": "Integer"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/telecomprovidersettings?view=graph-rest-beta&accept=text/markdown)
