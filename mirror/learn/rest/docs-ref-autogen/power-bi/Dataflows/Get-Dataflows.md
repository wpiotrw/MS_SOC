---
layout: Reference
title: Dataflows - Get Dataflows - REST API (Power BI Power BI REST APIs) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/rest/api/power-bi/dataflows/get-dataflows
uid: api.powerbi.com.power-bi.dataflows.getdataflows
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
description: Returns a list of all dataflows from the specified workspace. Permissions This API call can be called by a service principal profile.
locale: en-us
document_id: e96b3810-8580-f397-c124-32cdbf081274
document_version_independent_id: 709e2d7b-b147-231b-d6c0-f790d22495c0
original_content_git_url: https://github.com/MicrosoftDocs/powerbi-rest-api-docs-pr/blob/live/docs-ref-autogen/power-bi/Dataflows/Get-Dataflows.yml
site_name: Docs
depot_name: MSDN.powerbi-rest-api
page_type: rest
page_kind: operation
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.powerbi-rest-api/{branchName}{pdfName}
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/power-bi/dataflows/get-dataflows
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs-ref-autogen/power-bi/Dataflows/Get-Dataflows.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
platformId: a0909ac9-aacf-1891-e752-37adcf14ec6d
---

# Dataflows - Get Dataflows

- Service:
    - Power BI REST APIs

- API Version:
    - v1.0

Returns a list of all dataflows from the specified workspace.

## Permissions

This API call can be called by a service principal profile. For more information see: [Service principal profiles in Power BI Embedded](/en-us/power-bi/developer/embedded/embed-multi-tenancy).

## Required Scope

Dataflow.ReadWrite.All or Dataflow.Read.All 

```http
GET https://api.powerbi.com/v1.0/myorg/groups/{groupId}/dataflows
```

## URI Parameters

| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| groupId | path | True | string (uuid) | The workspace ID |

## Responses

| Name | Type | Description |
| --- | --- | --- |
| 200 OK | Dataflows | OK |

## Examples

### Example

#### Sample request

```http
GET https://api.powerbi.com/v1.0/myorg/groups/a2f89923-421a-464e-bf4c-25eab39bb09f/dataflows
```

#### Sample response

- Status code:
    - 200

```json
{
  "value": [
    {
      "objectId": "bd32e5c0-363f-430b-a03b-5535a4804b9b",
      "name": "AdventureWorks",
      "description": "Our Adventure Works",
      "modelUrl": "https://MyDataflowStorageAccount.dfs.core.windows.net/powerbi/contoso/AdventureWorks/model.json"
    }
  ]
}
```

## Definitions

| Name | Description |
| --- | --- |
| Dataflow | The metadata of a dataflow. Below is a list of properties that may be returned for a dataflow. Only a subset of the properties will be returned depending on the API called, the caller permissions and the availability of the data in the Power BI database. |
| Dataflows | OData response wrapper for a dataflow metadata list |
| DataflowUser | A Power BI user access right entry for a dataflow |
| DataflowUserAccessRight | The access right that a user has for the dataflow (permission level) |
| PrincipalType | The principal type |
| ServicePrincipalProfile | A Power BI service principal profile. Only relevant for [Power BI Embedded multi-tenancy solution](/en-us/power-bi/developer/embedded/embed-multi-tenancy). |

### Dataflow

Object

The metadata of a dataflow. Below is a list of properties that may be returned for a dataflow. Only a subset of the properties will be returned depending on the API called, the caller permissions and the availability of the data in the Power BI database.

| Name | Type | Description |
| --- | --- | --- |
| configuredBy | string | The dataflow owner |
| description | string | The dataflow description |
| modelUrl | string | A URL to the dataflow definition file (model.json) |
| name | string | The dataflow name |
| objectId | string (uuid) | The dataflow ID |
| users | DataflowUser[] | (Empty value) The dataflow user access details. This property will be removed from the payload response in an upcoming release. You can retrieve user information on a Power BI dataflow by using the [Get Dataflow Users as Admin](/en-us/rest/api/power-bi/admin/dataflows-get-dataflow-users-as-admin) API call, or the [PostWorkspaceInfo](/en-us/rest/api/power-bi/admin/workspace-info-post-workspace-info) API call with the `getArtifactUser` parameter. |

### Dataflows

Object

OData response wrapper for a dataflow metadata list

| Name | Type | Description |
| --- | --- | --- |
| @odata.context | string |  |
| value | Dataflow[] | The dataflow metadata list |

### DataflowUser

Object

A Power BI user access right entry for a dataflow

| Name | Type | Description |
| --- | --- | --- |
| DataflowUserAccessRight | DataflowUserAccessRight | The access right that a user has for the dataflow (permission level) |
| displayName | string | Display name of the principal |
| emailAddress | string | Email address of the user |
| graphId | string | Identifier of the principal in Microsoft Graph. Only available for admin APIs. |
| identifier | string | Identifier of the principal |
| principalType | PrincipalType | The principal type |
| profile | ServicePrincipalProfile | A Power BI service principal profile. Only relevant for [Power BI Embedded multi-tenancy solution](/en-us/power-bi/developer/embedded/embed-multi-tenancy). |
| userType | string | Type of the user. |

### DataflowUserAccessRight

Enumeration

The access right that a user has for the dataflow (permission level)

| Value | Description |
| --- | --- |
| None | Removes permission to content in dataflow |
| Read | Grants Read access to content in dataflow |
| ReadWrite | Grants Read and Write access to content in dataflow |
| ReadReshare | Grants Read and Reshare access to content in dataflow |
| Owner | Grants Read, Write and Reshare access to content in dataflow |

### PrincipalType

Enumeration

The principal type

| Value | Description |
| --- | --- |
| None | No principal type. Use for whole organization level access. |
| User | User principal type |
| Group | Group principal type |
| App | Service principal type |

### ServicePrincipalProfile

Object

A Power BI service principal profile. Only relevant for [Power BI Embedded multi-tenancy solution](/en-us/power-bi/developer/embedded/embed-multi-tenancy).

| Name | Type | Description |
| --- | --- | --- |
| displayName | string | The service principal profile name |
| id | string (uuid) | The service principal profile ID |