---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: Get approverDelegate - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/approverdelegate-get?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: corey284
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Read the properties of the approverDelegate object that is configured for a user.
ms.localizationpriority: medium
doc_type: apiPageType
ms.date: 2026-08-20T00:00:00.0000000Z
locale: en-us
document_id: e0f98ff6-6aa9-1225-f41c-bc3064210231
document_version_independent_id: 2f938d8f-f364-af6a-af0b-0359532533f2
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/api/approverdelegate-get.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
interactive_type: msgraph
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/approverdelegate-get
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/api/approverdelegate-get.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: 523efe10-3d85-b3aa-798c-b512d3016a97
---

# Get approverDelegate - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Read the properties of the [approverDelegate](resources/approverdelegate) object that is configured for a [user](resources/user). The approver delegate identifies the user or group that can approve or deny Microsoft Entra entitlement management access package assignment requests and access reviews on behalf of the user, and the period during which the delegation is in effect.

Signed-in users can read their own approver delegate. Administrators can read the approver delegate of any user in the tenant.

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](/en-us/graph/permissions-reference).

| Permission type | Least privileged permissions | Higher privileged permissions |
| --- | --- | --- |
| Delegated (work or school account) | EntitlementManagement.Read.All | EntitlementManagement.ReadWrite.All |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | Not supported. | Not supported. |

Important

For delegated access using work or school accounts, the signed-in user must be assigned a supported [Microsoft Entra role](/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) or a custom role that grants the permissions required for this operation. This operation supports the following built-in roles, which provide only the least privilege necessary:

- Global Reader
- Identity Governance Administrator

No directory role is required to read your own approver delegate through the `/me` path.

## HTTP request

To read the approver delegate of the signed-in user:

```http
GET /me/identityGovernance/approverDelegate
```

To read the approver delegate of another user:

```http
GET /users/{user-id}/identityGovernance/approverDelegate
```

## Optional query parameters

This method doesn't support any [OData query parameters](/en-us/graph/query-parameters) to help customize the response.

## Request headers

| Name | Description |
| --- | --- |
| Authorization | Bearer {token}. Required. Learn more about [authentication and authorization](/en-us/graph/auth/auth-concepts). |

## Request body

Don't supply a request body for this method.

## Response

If successful, this method returns a `200 OK` response code and an [approverDelegate](resources/approverdelegate) object in the response body.

If no approver delegate is configured for the user, this method returns a `200 OK` response code and `null` in the response body.

## Examples

### Example 1: Get the approver delegate of the signed-in user

#### Request

The following example shows a request.

```msgraph
GET https://graph.microsoft.com/beta/me/identityGovernance/approverDelegate
```

#### Response

The following example shows the response.

```http
HTTP/1.1 200 OK
Content-type: application/json

{
  "@odata.context": "https://graph.microsoft.com/beta/$metadata#users('87ec4b08-df41-4e9c-8f0c-2e6c9e19b0d3')/identityGovernance/approverDelegate",
  "delegate": {
    "@odata.type": "#microsoft.graph.singleUser",
    "id": "d8f4bcd2-4d5a-4a1e-88a5-b0f1c98d2f27",
    "description": "Alex Wilber"
  },
  "schedule": {
    "startDateTime": "2026-08-31T08:21:41.338Z",
    "expiration": {
      "endDateTime": "2026-09-07T08:21:41.339Z",
      "type": "afterDateTime"
    }
  }
}
```

### Example 2: Get the approver delegate of another user

#### Request

The following example shows a request.

```http
GET https://graph.microsoft.com/beta/users/87ec4b08-df41-4e9c-8f0c-2e6c9e19b0d3/identityGovernance/approverDelegate
```

#### Response

The following example shows the response.

```http
HTTP/1.1 200 OK
Content-type: application/json

{
  "@odata.context": "https://graph.microsoft.com/beta/$metadata#users('87ec4b08-df41-4e9c-8f0c-2e6c9e19b0d3')/identityGovernance/approverDelegate",
  "delegate": {
    "@odata.type": "#microsoft.graph.groupMembers",
    "id": "1c5f0b3e-8d4a-4e39-9f2b-6a7c1d3e5f80",
    "description": "Contoso approvers"
  },
  "schedule": {
    "startDateTime": "2026-08-31T08:21:41.338Z",
    "expiration": {
      "type": "noExpiration"
    }
  }
}
```