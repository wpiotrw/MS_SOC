---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: clientCredentialAuthenticationInfo resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/clientcredentialauthenticationinfo?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: vikama-microsoft
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents client credential authentication information used to connect to an external system from Microsoft Entra Entitlement Management.
ms.date: 2026-11-06T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 848f8800-b36f-9d66-5697-ce24d61e454a
document_version_independent_id: f559a960-435e-424b-c8a9-d5719edafeb7
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/clientcredentialauthenticationinfo.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/clientcredentialauthenticationinfo
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/clientcredentialauthenticationinfo.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/f488294d-f483-456e-94e3-755f933b811b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/02662057-0b9b-40f4-a3c7-537125b6d283
platformId: 4dd3f871-b7bc-5617-ab23-2ff115efc434
---

# clientCredentialAuthenticationInfo resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents client credential (OAuth 2.0 client credentials) authentication information used by Microsoft Entra Entitlement Management to connect to an external system, including the client identifier, the Azure Key Vault secret reference, and the token endpoint.

Inherits from [authenticationInfo](authenticationinfo). Use this concrete type for the **authenticationInfo** property of [externalSapAcConnectionInfo](externalsapacconnectioninfo). The **secretName** property identifies a stored secret; it doesn't contain the secret value.

## Methods

None.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| accessTokenUrl | String | The URL endpoint used to obtain access tokens for authentication with the external system. Nullable. |
| clientId | String | The client identifier used for authentication with the external system. Nullable. |
| secretName | String | The name of the secret in Azure Key Vault that contains the client secret. Nullable. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.clientCredentialAuthenticationInfo",
  "clientId": "String",
  "secretName": "String",
  "accessTokenUrl": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/clientcredentialauthenticationinfo?view=graph-rest-beta&accept=text/markdown)
