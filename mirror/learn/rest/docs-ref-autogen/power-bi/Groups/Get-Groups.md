---
layout: Reference
title: Groups - Get Groups - REST API (Power BI Power BI REST APIs) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/rest/api/power-bi/groups/get-groups
uid: api.powerbi.com.power-bi.groups.getgroups
breadcrumb_path: /rest/breadcrumb/toc.json
rest_product: Power BI
ms.service: powerbi
products:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
author: rloutlaw
ms.author: routlaw
ms.devlang: rest-api
ms.date: 2018-03-14T00:00:00.0000000Z
uhfHeaderId: MSDocsHeader-MSPowerBI
feedback_system: None
enable_rest_try_it: true
ms.topic: generated-reference
description: Returns a list of workspaces the user has access to. Permissions This API call can be called by a service principal profile.
locale: en-us
document_id: c41a115e-b63a-fdc2-2ccc-8b6bc5d7bc5a
document_version_independent_id: 6e52c2d3-43ca-e4d1-2726-f9f2a6db6815
original_content_git_url: https://github.com/MicrosoftDocs/powerbi-rest-api-docs-pr/blob/live/docs-ref-autogen/power-bi/Groups/Get-Groups.yml
site_name: Docs
depot_name: MSDN.powerbi-rest-api
page_type: rest
page_kind: operation
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.powerbi-rest-api/{branchName}{pdfName}
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/power-bi/groups/get-groups
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs-ref-autogen/power-bi/Groups/Get-Groups.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
platformId: 1b4be012-f7cf-a6fd-805d-835fc1758134
---

# Groups - Get Groups

- Service:
    - Power BI REST APIs

- API Version:
    - v1.0

Returns a list of workspaces the user has access to.

## Permissions

This API call can be called by a service principal profile. For more information see: [Service principal profiles in Power BI Embedded](/en-us/power-bi/developer/embedded/embed-multi-tenancy).

## Required Scope

Workspace.Read.All or Workspace.ReadWrite.All

## Limitations

- User permissions for workspaces take time to get updated and may not be immediately available when using API calls. To refresh user permissions, use the [Refresh User Permissions](/en-us/rest/api/power-bi/users/refresh-user-permissions) API call.

```http
GET https://api.powerbi.com/v1.0/myorg/groups
```

 With optional parameters: 

```http
GET https://api.powerbi.com/v1.0/myorg/groups?$filter={$filter}&$top={$top}&$skip={$skip}
```

## URI Parameters

| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| $filter | query |  | string | Returns a subset of a results based on [Odata](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part2-url-conventions.html#sec_SystemQueryOptions) filter query parameter condition. |
| $skip | query |  | integer (int32) | Skips the first n results |
| $top | query |  | integer (int32) | Returns only the first n results |

## Responses

| Name | Type | Description |
| --- | --- | --- |
| 200 OK | Groups | OK |

## Examples

| Example |
| --- |
| Get a list of workspaces using a filter example |

### Example

#### Sample request

```http
GET https://api.powerbi.com/v1.0/myorg/groups
```

#### Sample response

- Status code:
    - 200

```json
{
  "value": [
    {
      "id": "f089354e-8366-4e18-aea3-4cb4a3a50b48",
      "isReadOnly": false,
      "isOnDedicatedCapacity": false,
      "name": "sample group"
    },
    {
      "id": "3d9b93c6-7b6d-4801-a491-1738910904fd",
      "isReadOnly": false,
      "isOnDedicatedCapacity": true,
      "capacityId": "0f084df7-c13d-451b-af5f-ed0c466403b2",
      "defaultDatasetStorageFormat": "Small",
      "name": "marketing group"
    },
    {
      "id": "a2f89923-421a-464e-bf4c-25eab39bb09f",
      "isReadOnly": false,
      "isOnDedicatedCapacity": true,
      "capacityId": "0f084df7-c13d-451b-af5f-ed0c466403b2",
      "defaultDatasetStorageFormat": "Large",
      "name": "contoso",
      "dataflowStorageId": "d692ae06-708c-485e-9987-06ff0fbdbb1f"
    }
  ]
}
```

### Get a list of workspaces using a filter example

#### Sample request

```http
GET https://api.powerbi.com/v1.0/myorg/groups?$filter=contains(name,'marketing')%20or%20name%20eq%20'contoso'
```

#### Sample response

- Status code:
    - 200

```json
{
  "value": [
    {
      "id": "3d9b93c6-7b6d-4801-a491-1738910904fd",
      "isReadOnly": false,
      "isOnDedicatedCapacity": false,
      "name": "marketing group"
    },
    {
      "id": "a2f89923-421a-464e-bf4c-25eab39bb09f",
      "isReadOnly": false,
      "isOnDedicatedCapacity": false,
      "name": "contoso",
      "dataflowStorageId": "d692ae06-708c-485e-9987-06ff0fbdbb1f"
    }
  ]
}
```

## Definitions

| Name | Description |
| --- | --- |
| AzureResource | A response detailing a user-owned Azure resource such as a Log Analytics workspace. |
| DefaultDatasetStorageFormat | The default dataset storage format in the group |
| Group | A Power BI group |
| Groups | The OData response wrapper for a list of Power BI groups |

### AzureResource

Object

A response detailing a user-owned Azure resource such as a Log Analytics workspace.

| Name | Type | Description |
| --- | --- | --- |
| id | string (uuid) | An identifier for the resource within Power BI. |
| resourceGroup | string | The resource group within the subscription where the resource resides. |
| resourceName | string | The name of the resource. |
| subscriptionId | string (uuid) | The Azure subscription where the resource resides. |

### DefaultDatasetStorageFormat

Enumeration

The default dataset storage format in the group

| Value | Description |
| --- | --- |
| Small | Small dataset storage format |
| Large | Large dataset storage format |

### Group

Object

A Power BI group

| Name | Type | Description |
| --- | --- | --- |
| capacityId | string (uuid) | The capacity ID |
| dataflowStorageId | string (uuid) | The Power BI dataflow storage account ID |
| defaultDatasetStorageFormat | DefaultDatasetStorageFormat | The default dataset storage format in the workspace. Returned only when `isOnDedicatedCapacity` is `true` |
| id | string (uuid) | The workspace ID |
| isOnDedicatedCapacity | boolean | Whether the group is assigned to a dedicated capacity |
| isReadOnly | boolean | Whether the group is read-only |
| logAnalyticsWorkspace | AzureResource | The Log Analytics workspace assigned to the group. This is returned only when retrieving a single group. |
| name | string | The group name |

### Groups

Object

The OData response wrapper for a list of Power BI groups

| Name | Type | Description |
| --- | --- | --- |
| @odata.context | string | OData context |
| value | Group[] | The list of groups |