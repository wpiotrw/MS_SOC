---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: List accessDriftSummary - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/accessdriftsummary-list?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: suhanigupta
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Get a list of the accessDriftSummary objects and their properties.
ms.date: 2026-10-09T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: apiPageType
locale: en-us
document_id: 74c4a6c3-2dec-0004-273d-8085ea5e82bb
document_version_independent_id: b1628fd1-851a-40ae-4ceb-b4a6c02f1d9f
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/api/accessdriftsummary-list.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/accessdriftsummary-list
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/api/accessdriftsummary-list.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 9ef33608-3908-76d4-cf09-19a89c8ecced
---

# List accessDriftSummary - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Get a list of the [accessDriftSummary](resources/accessdriftsummary) objects and their properties.

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](/en-us/graph/permissions-reference).

| Permission type | Least privileged permissions | Higher privileged permissions |
| --- | --- | --- |
| Delegated (work or school account) | EntitlementManagement.Read.All | EntitlementManagement.ReadWrite.All |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | EntitlementManagement.Read.All | EntitlementManagement.ReadWrite.All |

Tip

For delegated access using a work or school account, the signed-in user must have access to the relevant entitlement management catalog. The least privileged [role in the Entitlement Management system](/en-us/entra/id-governance/entitlement-management-delegate) is *Catalog reader*.

When the request identifies a catalog, access is evaluated for that catalog. Otherwise, the results are limited to catalogs that the signed-in user can access.

In app-only scenarios, the calling app must have the `EntitlementManagement.Read.All` or `EntitlementManagement.ReadWrite.All` application permission. An entitlement management catalog role doesn't replace the required application permission.

## HTTP request

```http
GET /identityGovernance/insights/accessDriftSummary
```

## Optional query parameters

This method supports the `$filter`, `$search`, `$top`, `$skip`, `$orderby`, `$count`, and `$expand` OData query parameters to help customize the response. For general information, see [OData query parameters](/en-us/graph/query-parameters).

Every `$filter` expression must include `resource/type`. You can combine it with `resource/catalogIdentifier` and `driftSource`. Currently, the supported value for `driftSource` is `entra`.

The `$search` parameter performs a case-insensitive substring search against `resource/catalogName` and `resource/displayName`. For example, `$search=fin` matches a catalog or resource name that contains `Finance`.

The `$orderby` parameter supports `createdDateTime`, `driftCounts/missing`, `driftCounts/total`, `driftCounts/unauthorized`, `resource/displayName`, and `resource/identifier`. You can combine multiple properties and specify `asc` or `desc` for each one.

The maximum value for `$top` is `1000`. When you use `$expand=details`, the maximum value for `$top` is `100`.

When you use `$expand=details`, each summary includes up to five access drift details. If more details are available for a summary, that summary includes a `details@odata.nextLink` property that identifies the contained details collection.

The following examples show supported query patterns:

- Filter by resource type: `$filter=resource/type eq 'application'`
- Filter by resource type and drift source: `$filter=resource/type eq 'application' and driftSource eq 'entra'`
- Search catalog and resource names: `$search=Sales`
- Expand details: `$expand=details`
- Order by resource name: `$orderby=resource/displayName`
- Order by unauthorized count: `$orderby=driftCounts/unauthorized desc`

## Request headers

| Name | Description |
| --- | --- |
| Authorization | Bearer {token}. Required. Learn more about [authentication and authorization](/en-us/graph/auth/auth-concepts). |

## Request body

Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and a collection of [accessDriftSummary](resources/accessdriftsummary) objects in the response body.

## Examples

### Request

The following example shows a request.

```http
GET https://graph.microsoft.com/beta/identityGovernance/insights/accessDriftSummary?$filter=resource/type eq 'application' and driftSource eq 'entra'
```

### Response

The following example shows the response.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "value": [
    {
      "@odata.type": "#microsoft.graph.accessDriftSummary",
      "id": "v1_e4c2b24ce2c799a6ce199b1988b8fbf880766cdf21a3d288743082c3822b06f2",
      "resource": {
        "@odata.type": "#microsoft.graph.applicationDriftResourceInfo",
        "catalogName": "Business applications",
        "identifier": "app-xyz-001",
        "displayName": "Salesforce",
        "type": "application",
        "catalogIdentifier": "cat-001"
      },
      "driftSource": "entra",
      "driftCounts": {
        "@odata.type": "#microsoft.graph.driftCounts",
        "total": 19,
        "unauthorized": 12,
        "missing": 7
      },
      "createdDateTime": "2026-04-27T03:15:42Z"
    }
  ]
}
```