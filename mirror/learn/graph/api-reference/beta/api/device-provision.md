---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: 'device: provision - Microsoft Graph beta | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/device-provision?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: mjsantani
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-directory-management
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Provision a device on behalf of an approved Virtual Desktop Infrastructure (VDI) provider.
ms.localizationpriority: medium
doc_type: apiPageType
ms.date: 2026-06-19T00:00:00.0000000Z
locale: en-us
document_id: 13bb3799-948a-6ba8-65e5-d30bdcec8e16
document_version_independent_id: f5493fb5-c5ad-7507-e3df-db72744918e4
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/api/device-provision.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/device-provision
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/api/device-provision.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/4b132a0c-342a-42eb-91ff-8159e1ed413d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f2b71146-ce8e-46a8-9965-8aa8b3aa8235
platformId: 1d41dea7-1f77-1575-5389-2c7c9d08ea93
---

# device: provision - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Provision a [device](resources/device) on behalf of an approved Virtual Desktop Infrastructure (VDI) provider.

This action wraps the Zero Touch Deployment (ZTD) protocol to create a device in a pending state in the customer's directory. The device can't be used for authentication until it completes its registration. The created device is stamped with a system label that identifies the approved VDI provider.

Only VDI applications on Microsoft's approved list of VDI providers can successfully call this action. Calls from other applications are blocked even when the application is granted the required permission.

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](/en-us/graph/permissions-reference).

| Permission type | Least privileged permissions | Higher privileged permissions |
| --- | --- | --- |
| Delegated (work or school account) | Device.ProvisionForVDI | Not available. |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | Not supported. | Not supported. |

Important

For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. *Cloud Device Administrator* is the least privileged role supported for this operation.

In addition to the permission, the calling application must be on Microsoft's approved list of VDI providers.

## HTTP request

```http
POST /devices/provision
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
| provisioningBlob | String | An opaque blob, generated by the Microsoft Entra device identity runtime library and shared with approved VDI providers, that contains the information required to provision the device. Required. |

## Response

If successful, this action returns a `201 Created` response code and a [provisionResponse](resources/provisionresponse) in the response body. The response also includes a `Location` header that contains the URI of the created device object.

## Examples

### Request

The following example shows a request.

```http
POST https://graph.microsoft.com/beta/devices/provision
Content-Type: application/json

{
  "provisioningBlob": "eyJ2ZXIiOiIxLjAiLCJub25jZSI6IjJkZjg1ZTdmYTk0ZjQ3In0"
}
```

### Response

The following example shows the response.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "@odata.context": "https://graph.microsoft.com/beta/$metadata#microsoft.graph.provisionResponse",
  "challenge": "Y2hhbGxlbmdlVmFsdWVFeGFtcGxl",
  "deviceId": "2ec25e3b-9243-4f3c-8c83-2e2a9b8a4f1a"
}
```