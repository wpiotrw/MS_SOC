---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: 'user: attest - Microsoft Graph v1.0 | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/user-attest?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: faithwins
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Attest to the continued need for a guest user in the organization.
ms.date: 2026-11-03T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: apiPageType
locale: en-us
document_id: bf53ecf9-f953-996b-ee13-ecc16f74b64a
document_version_independent_id: 3cf747ac-3d18-570a-13c6-71c210da14da
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/api/user-attest.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/user-attest
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/api/user-attest.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: a18b73b3-758f-05e1-af07-9a057dc772bd
---

# user: attest - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.identityGovernance

Attest to the continued need for a guest [user](resources/user) in the organization.

## API availability

This API is available in the following [national cloud deployments](/en-us/graph/deployments).

| Global service | US Government L4 | US Government L5 (DOD) | China operated by 21Vianet |
| --- | --- | --- | --- |
| ✅ | ❌ | ❌ | ❌ |

## Permissions

This API supports delegated access only. Application (app-only) access isn't supported.

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](/en-us/graph/permissions-reference).

| Permission type | Least privileged permissions | Higher privileged permissions |
| --- | --- | --- |
| Delegated (work or school account) | LifecyclePolicies-Guests.ReadWrite.All | Not available. |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | Not supported. | Not supported. |

Important

Guest user attestation supports delegated access only. Application access is rejected even with the `LifecyclePolicies-Guests.ReadWrite.All` application permission. No role, ownership, or sponsorship grants an application an exception.

The lifecycle workflows service accepts either of the following delegated authorization paths:

- **Administrator:** Both the `LifecyclePolicies-Guests.ReadWrite.All` delegated scope and a supported [Microsoft Entra role](/en-us/entra/identity/role-based-access-control/permissions-reference?toc=%2Fgraph%2Ftoc.json) are required. *Lifecycle Workflows Administrator* is the least privileged role supported for this path. Scope alone or role alone is insufficient. Global Reader doesn't qualify.
- **Sponsor:** The signed-in user must be a direct sponsor of the target guest or a direct member of a group sponsoring that guest. This path doesn't additionally require the preceding scope or admin role in the lifecycle workflows handler. Sponsorship must be successfully verified; a failed or forbidden sponsorship lookup doesn't grant access.

Ownership isn't an authorization path. The target user must exist, be a guest, and have an enabled account. Requests must also satisfy Microsoft Graph authentication and permission validation.

## HTTP request

```http
POST /users/{guestUserId}/microsoft.graph.identityGovernance.attest
```

## Request headers

| Name | Description |
| --- | --- |
| Authorization | Bearer {token}. Required. Learn more about [authentication and authorization](/en-us/graph/auth/auth-concepts). |

## Request body

Don't supply a request body for this method.

## Response

If successful, this action returns a `204 No Content` response code. It doesn't return anything in the response body.

## Examples

### Request

```http
POST https://graph.microsoft.com/v1.0/users/e4f5d67a-5a10-4c40-9734-0c5f2d83a1bf/microsoft.graph.identityGovernance.attest
```

### Response

```http
HTTP/1.1 204 No Content
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/user-attest?view=graph-rest-beta&accept=text/markdown)
