---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: clientCredentialAuthenticationInfo resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/clientcredentialauthenticationinfo?view=graph-rest-beta
config_moniker_range: graph-rest-beta
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
ms.date: 2026-07-13T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: cb6b2ee1-c7d0-956b-ad91-80eca5e80ca8
document_version_independent_id: f559a960-435e-424b-c8a9-d5719edafeb7
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/clientcredentialauthenticationinfo.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/clientcredentialauthenticationinfo
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/clientcredentialauthenticationinfo.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 4dd3f871-b7bc-5617-ab23-2ff115efc434
---

# clientCredentialAuthenticationInfo resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents client credential (OAuth 2.0 client credentials) authentication information used by Microsoft Entra Entitlement Management to connect to an external system, including the client identifier, the Azure Key Vault secret reference, and the token endpoint.

Inherits from [authenticationInfo](authenticationinfo).

## Properties

| Property | Type | Description |
| --- | --- | --- |
| accessTokenUrl | String | The URL endpoint used to obtain access tokens for authentication with the external system. |
| clientId | String | The client identifier used for authentication with the external system. |
| secretName | String | The name of the secret in Azure Key Vault that contains the client secret. |

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