---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: 'recommendation: addTag - Microsoft Graph beta | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/recommendation-addtag?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: sanchariroy9197
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-monitoring-health
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Add a user-defined tag to a recommendation object.
ms.localizationpriority: medium
doc_type: apiPageType
ms.date: 2026-07-22T00:00:00.0000000Z
locale: en-us
document_id: 69bf945c-88a9-7444-1f88-185e187bf598
document_version_independent_id: f80e1d08-8e41-010d-1a55-860bc9a18831
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/api/recommendation-addtag.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/recommendation-addtag
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/api/recommendation-addtag.md
platformId: c85d192f-ef19-db1b-1b62-8dfe8acdafff
---

# recommendation: addTag - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Add a user-defined [tag](resources/recommendationtag) to a [recommendation](resources/recommendation) object. Tags help you organize, group, and filter recommendations in the Microsoft Entra admin center.

This API is available in the following [national cloud deployments](/en-us/graph/deployments).

| Global service | US Government L4 | US Government L5 (DOD) | China operated by 21Vianet |
| --- | --- | --- | --- |
| ✅ | ✅ | ✅ | ✅ |

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](/en-us/graph/permissions-reference).

| Permission type | Least privileged permissions | Higher privileged permissions |
| --- | --- | --- |
| Delegated (work or school account) | DirectoryRecommendations.ReadWrite.All | Not available. |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | DirectoryRecommendations.ReadWrite.All | Not available. |

Important

For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:

- Security Administrator
- Security Operator
- Application Administrator
- Cloud Application Administrator

## HTTP request

```http
POST /directory/recommendations/{recommendationId}/addTag
```

## Request headers

| Name | Description |
| --- | --- |
| Authorization | Bearer {token}. Required. Learn more about [authentication and authorization](/en-us/graph/auth/auth-concepts). |
| Content-Type | application/json. Required. |

## Request body

In the request body, supply a JSON representation of the parameters.

The following table shows the parameters that you can use with this action.

| Parameter | Type | Description |
| --- | --- | --- |
| displayName | String | The free-form label text to apply to the recommendation. All characters and Unicode (all languages) are supported. Required. |

## Response

If successful, this action returns a `200 OK` response code and a [recommendationTag](resources/recommendationtag) in the response body.

## Examples

### Request

The following example shows a request.

```http
POST https://graph.microsoft.com/beta/directory/recommendations/0cb31920-84b9-471f-a6fb-468c1a847088_Microsoft.Identity.IAM.Insights.TurnOffPerUserMFA/addTag
Content-Type: application/json

{
    "displayName": "Q3 remediation"
}
```

### Response

The following example shows the response.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "@odata.context": "https://graph.microsoft.com/beta/$metadata#recommendationTag",
    "@odata.type": "#microsoft.graph.recommendationTag",
    "id": "6f9a1e17-8e2f-4a2c-9f3b-1d0e5c7a2b34",
    "displayName": "Q3 remediation"
}
```