---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: 'tenantProtectionScopeContainer: compute - Microsoft Graph v1.0 | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/tenantprotectionscopecontainer-compute?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: kylemar
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
toc.title: 'tenantProtectionScopeContainer: compute'
description: Compute the tenant-wide data protection policies and actions, including user or group scoping.
ms.date: 2026-02-06T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: apiPageType
locale: en-us
document_id: 654443f3-415b-fc37-d39a-6adc975af949
document_version_independent_id: 1f5c3187-e28f-06fb-f3e8-f8b967501011
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/api/tenantprotectionscopecontainer-compute.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/tenantprotectionscopecontainer-compute
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/api/tenantprotectionscopecontainer-compute.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: e15bef44-d308-3801-c1d2-3f253f0d7a9e
---

# tenantProtectionScopeContainer: compute - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Compute the tenant-wide data protection policies and actions, including user/group scoping.

This API is available in the following [national cloud deployments](/en-us/graph/deployments).

| Global service | US Government L4 | US Government L5 (DOD) | China operated by 21Vianet |
| --- | --- | --- | --- |
| ✅ | ✅ | ✅ | ❌ |

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](/en-us/graph/permissions-reference).

| Permission type | Least privileged permissions | Higher privileged permissions |
| --- | --- | --- |
| Delegated (work or school account) | ProtectionScopes.Compute.All | Not available. |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | ProtectionScopes.Compute.All | Not available. |

## HTTP request

```http
POST /security/dataSecurityAndGovernance/protectionScopes/compute
```

## Request headers

| Name | Description |
| --- | --- |
| Authorization | Bearer {token}. Required. Learn more about [authentication and authorization](/en-us/graph/auth/auth-concepts). |
| Content-Type | application/json. Required. |
| Client-Request-Id | String (GUID recommended). Optional. Unique identifier for this request, which is used for tracing and debugging in logs and support interactions. If an ID is not provided, one may be generated automatically. We recommend that you specify the ID to make tracing and debugging easier. The same ID that was sent in the request will be returned in the response. |

## Request body

In the request body, provide JSON object with the following parameters.

| Parameter | Type | Description |
| --- | --- | --- |
| activities | microsoft.graph.security.userActivityTypes | Optional. Flags specifying the user activities the calling application supports or is interested. Possible values are `none`, `uploadText`, `uploadFile`, `downloadText`, `downloadFile`, `unknownFutureValue`. This object is a multi-valued enumeration. |
| deviceMetadata | [deviceMetadata](resources/devicemetadata) | Optional. Information about the device context (type, OS) used for contextual policy evaluation. Not expected to be used when computing tenant protection scopes |
| integratedAppMetadata | [integratedApplicationMetadata](resources/integratedapplicationmetadata) | Optional. Information about the calling application (name, version) integrating with Microsoft Purview. |
| locations | [policyLocation](resources/policylocation) collection | Optional. List of specific locations the application is interested in. If provided, results are trimmed to policies covering these locations. Use [policy location application](resources/policylocationapplication) for application locations, [policy location domain](resources/policylocationdomain) for domain locations, or [policy location URL](resources/policylocationurl) for URL locations. You must specify the `@odata.type` property to declare the type of policyLocation. For example, `"@odata.type": "microsoft.graph.policyLocationApplication"`. |
| pivotOn | microsoft.graph.policyPivotProperty | Optional. Specifies how the results should be aggregated. If omitted or `none`, results might be less aggregated. Possible values are `activity`,`location`, `none`. |

## Response

If successful, this action returns a `200 OK` response code and a collection of [policyTenantScope](resources/policytenantscope) objects in the response body. Each object represents a set of locations and activities governed by a common set of policy actions and execution mode, along with the user/group bindings for that specific policy configuration.

## Examples

### Request

The following example computes the tenant-wide protection scope for text uploads and downloads, interested in a specific application.

```http
POST https://graph.microsoft.com/v1.0/security/dataSecurityAndGovernance/protectionScopes/compute
Content-type: application/json

{
    "activities": "uploadText,downloadText",
    "locations": [
        {
            "@odata.type": "microsoft.graph.policyLocationApplication",
            "value": "be121c8f-ecd8-4026-b699-669e0ce1bcbf"
        }
    ]
}
```

### Response

The following example shows the response. It indicates that uploadText or downloadText activities "All" users (tenant scope) with no exclusions require inline evaluation.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#Collection(microsoft.graph.policyTenantScope)",
    "value": [
        {
            "activities": "uploadText,downloadText",
            "executionMode": "evaluateOffline",
            "policyScope": {
                "inclusions": [
                    {
                        "identity": "All"
                    }
                ],
                "exclusions": [
                ]
            },
            "locations": [
                {
                    "value": "be121c8f-ecd8-4026-b699-669e0ce1bcbf"
                }
            ],
            "policyActions": [
            ]
        }
    ]
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/tenantprotectionscopecontainer-compute?view=graph-rest-beta&accept=text/markdown)
