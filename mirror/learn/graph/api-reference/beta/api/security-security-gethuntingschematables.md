---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: 'security: getHuntingSchemaTables - Microsoft Graph beta | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/security-security-gethuntingschematables?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: Nnachtomy
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Retrieve the advanced hunting tables accessible to the signed-in user.
ms.localizationpriority: medium
doc_type: apiPageType
ms.date: 2026-08-22T00:00:00.0000000Z
locale: en-us
document_id: cba5e353-e2ef-2030-7236-7c40138a4fe9
document_version_independent_id: 8a4c3860-2b07-f25c-1cda-274c66e8a085
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/api/security-security-gethuntingschematables.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
interactive_type: msgraph
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/security-security-gethuntingschematables
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/api/security-security-gethuntingschematables.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1577a46d-8446-40bd-bfae-0578362f4d94
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/cdf3f22d-5420-4d59-a2bf-66d6b3d9c828
platformId: 25566983-a77b-a1a6-9d63-ae0b9f01e97f
---

# security: getHuntingSchemaTables - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph.security

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Retrieve only the advanced hunting tables that the signed-in user is authorized to query in [advanced hunting](/en-us/microsoft-365/security/defender/advanced-hunting-overview?view=o365-worldwide&amp;preserve-view=true) with Microsoft Defender XDR.

The returned tables reflect the user's effective permissions. Each user within a tenant might have a different effective set of tables depending on their role and access level.

Unlike [getHuntingSchema](security-security-gethuntingschema), which returns both tables and functions in a single [huntingSchemaResult](resources/security-huntingschemaresult), this function returns the tables as a collection. Because the result is a collection, you can apply OData query parameters such as `$filter`, `$select`, and `$top` to retrieve only the tables and columns you need.

Common use cases include:

- **Preventing unauthorized queries**: Determine which tables a user can access before running a hunting query, which reduces the risk of authorization failures.
- **Permission-aware query generation**: Enable applications and tools to construct queries dynamically based on the tables available to the user.
- **Retrieving a targeted subset**: Use OData query parameters to request specific tables instead of the full schema.

## Permissions

Choose the permission or permissions marked as least privileged for this API. Use a higher privileged permission or permissions [only if your app requires it](/en-us/graph/permissions-overview#best-practices-for-using-microsoft-graph-permissions). For details about delegated and application permissions, see [Permission types](/en-us/graph/permissions-overview#permission-types). To learn more about these permissions, see the [permissions reference](/en-us/graph/permissions-reference).

| Permission type | Least privileged permissions | Higher privileged permissions |
| --- | --- | --- |
| Delegated (work or school account) | ThreatHunting.Read.All | Not available. |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | ThreatHunting.Read.All | Not available. |

Important

The signed-in user must also be assigned a [Microsoft Defender XDR Unified RBAC role](/en-us/microsoft-365/security/defender/manage-rbac) that grants permission to run advanced hunting queries, or one of the following Microsoft Entra ID roles which provide only the least privilege necessary: **Security Reader**, **Security Operator**, **Security Administrator**.

## HTTP request

```http
GET /security/getHuntingSchemaTables
GET /security/getHuntingSchemaTables(workspaceId={workspaceId})
```

## Function parameters

In the request URL, provide the following optional function parameter with values.

| Parameter | Type | Description |
| --- | --- | --- |
| workspaceId | Guid | Optional. The identifier of the workspace to scope the tables to. If you don't specify this parameter, the default workspace is used. |

This function supports the `$count`, `$filter`, `$select`, `$skip`, and `$top`[OData query parameters](/en-us/graph/query-parameters) to help customize the response.

## Request headers

| Name | Description |
| --- | --- |
| Authorization | \*\*\*\*\*\* Required. Learn more about [authentication and authorization](/en-us/graph/auth/auth-concepts). |

## Request body

Don't supply a request body for this method.

## Response

If successful, this function returns a `200 OK` response code and a collection of [microsoft.graph.security.huntingSchemaTable](resources/security-huntingschematable) objects in the response body.

## Examples

### Example 1: Retrieve all accessible hunting tables

#### Request

The following example shows a request.

```msgraph
GET https://graph.microsoft.com/beta/security/getHuntingSchemaTables
```

#### Response

The following example shows the response.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-type: application/json

{
  "@odata.context": "https://graph.microsoft.com/beta/$metadata#Collection(microsoft.graph.security.huntingSchemaTable)",
  "value": [
    {
      "name": "DeviceProcessEvents",
      "description": "Process creation and related events",
      "columns": [
        {
          "name": "Timestamp",
          "dataType": "DateTime",
          "description": "Date and time when the record was generated"
        },
        {
          "name": "DeviceId",
          "dataType": "String",
          "description": "Unique identifier for the device in the service"
        },
        {
          "name": "DeviceName",
          "dataType": "String",
          "description": "Fully qualified domain name (FQDN) of the device"
        }
      ]
    },
    {
      "name": "DeviceNetworkEvents",
      "description": "Network connection and related events",
      "columns": [
        {
          "name": "Timestamp",
          "dataType": "DateTime",
          "description": "Date and time when the record was generated"
        },
        {
          "name": "DeviceId",
          "dataType": "String",
          "description": "Unique identifier for the device in the service"
        }
      ]
    }
  ]
}
```

### Example 2: Retrieve the tables for a specific workspace

#### Request

The following example scopes the request to a single workspace.

```msgraph
GET https://graph.microsoft.com/beta/security/getHuntingSchemaTables(workspaceId=8fb6e2d6-1b0a-4d0b-9d9f-9f3e2a5c7b21)
```

#### Response

The following example shows the response.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 200 OK
Content-type: application/json

{
  "@odata.context": "https://graph.microsoft.com/beta/$metadata#Collection(microsoft.graph.security.huntingSchemaTable)",
  "value": [
    {
      "name": "DeviceProcessEvents",
      "description": "Process creation and related events",
      "columns": [
        {
          "name": "Timestamp",
          "dataType": "DateTime",
          "description": "Date and time when the record was generated"
        },
        {
          "name": "DeviceId",
          "dataType": "String",
          "description": "Unique identifier for the device in the service"
        }
      ]
    }
  ]
}
```

### Example 3: Retrieve only the names of the accessible tables

#### Request

The following example uses the `$select` query parameter to return only the table names.

```msgraph
GET https://graph.microsoft.com/beta/security/getHuntingSchemaTables?$select=name
```

#### Response

The following example shows the response.

```http
HTTP/1.1 200 OK
Content-type: application/json

{
  "@odata.context": "https://graph.microsoft.com/beta/$metadata#Collection(microsoft.graph.security.huntingSchemaTable)",
  "value": [
    {
      "name": "DeviceProcessEvents"
    },
    {
      "name": "DeviceNetworkEvents"
    }
  ]
}
```