---
layout: Reference
title: Capacities - Get Capacities - REST API (Power BI Power BI REST APIs) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/rest/api/power-bi/capacities/get-capacities
uid: api.powerbi.com.power-bi.capacities.getcapacities
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
description: Returns a list of capacities that the user has access to. Permissions This API call can be called by a service principal profile.
locale: en-us
document_id: 19fe9e14-c1f3-8028-4bfe-badb0ab8421b
document_version_independent_id: dfb5df66-ec32-5a2d-6400-3659b918c840
original_content_git_url: https://github.com/MicrosoftDocs/powerbi-rest-api-docs-pr/blob/live/docs-ref-autogen/power-bi/Capacities/Get-Capacities.yml
site_name: Docs
depot_name: MSDN.powerbi-rest-api
page_type: rest
page_kind: operation
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.powerbi-rest-api/{branchName}{pdfName}
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/power-bi/capacities/get-capacities
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs-ref-autogen/power-bi/Capacities/Get-Capacities.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
platformId: efdf4982-db90-b0bb-8bc3-ca9bf144e849
---

# Capacities - Get Capacities

- Service:
    - Power BI REST APIs

- API Version:
    - v1.0

Returns a list of capacities that the user has access to.

## Permissions

This API call can be called by a service principal profile. For more information see: [Service principal profiles in Power BI Embedded](/en-us/power-bi/developer/embedded/embed-multi-tenancy). The profile creator must have capacity permissions.

## Required Scope

Capacity.Read.All or Capacity.ReadWrite.All 

```http
GET https://api.powerbi.com/v1.0/myorg/capacities
```

## Responses

| Name | Type | Description |
| --- | --- | --- |
| 200 OK | Capacities | OK |

## Examples

### Example

#### Sample request

```http
GET https://api.powerbi.com/v1.0/myorg/capacities
```

#### Sample response

- Status code:
    - 200

```json
{
  "value": [
    {
      "id": "0f084df7-c13d-451b-af5f-ed0c466403b2",
      "displayName": "MyCapacity",
      "admins": [
        "john@contoso.com"
      ],
      "sku": "A1",
      "state": "Active",
      "region": "West Central US",
      "capacityUserAccessRight": "Admin"
    }
  ]
}
```

## Definitions

| Name | Description |
| --- | --- |
| Capacities | OData response wrapper for a Power BI capacity list |
| Capacity | A Power BI capacity |
| CapacityState | The capacity state |
| capacityUserAccessRight | The access right that the user has on the capacity |
| TenantKey | Encryption key information |

### Capacities

Object

OData response wrapper for a Power BI capacity list

| Name | Type | Description |
| --- | --- | --- |
| @odata.context | string |  |
| value | Capacity[] | The capacity list |

### Capacity

Object

A Power BI capacity

| Name | Type | Description |
| --- | --- | --- |
| admins | string[] | An array of capacity admins |
| capacityUserAccessRight | capacityUserAccessRight | The access right a user has on the capacity |
| displayName | string | The display name of the capacity |
| id | string (uuid) | The capacity ID |
| region | string | The Azure region where the capacity was provisioned |
| sku | string | The capacity SKU |
| state | CapacityState | The capacity state |
| tenantKey | TenantKey | Encryption key information (only applies to admin routes) |
| tenantKeyId | string (uuid) | The ID of an encryption key (only applicable to the admin route) |

### CapacityState

Enumeration

The capacity state

| Value | Description |
| --- | --- |
| NotActivated | Unsupported |
| Active | The capacity is ready to use |
| Provisioning | Activation of the capacity is in progress |
| ProvisionFailed | Provisioning of the capacity failed |
| PreSuspended | Unsupported |
| Suspended | Use of the capacity is suspended |
| Deleting | Deletion of the capacity is in progress |
| Deleted | The capacity was deleted and is unavailable |
| Invalid | The capacity can't be used |
| UpdatingSku | A capacity SKU change is in progress |

### capacityUserAccessRight

Enumeration

The access right that the user has on the capacity

| Value | Description |
| --- | --- |
| None | User doesn't have access to the capacity |
| Assign | User has contributor rights and can assign workspaces to the capacity |
| Admin | User has administrator rights on the capacity |

### TenantKey

Object

Encryption key information

| Name | Type | Description |
| --- | --- | --- |
| createdAt | string (date-time) | The creation date and time of the encryption key |
| id | string (uuid) | The ID of the encryption key |
| isDefault | boolean | Whether the encryption key is the default key for the entire tenant. Any newly created capacity inherits the default key. |
| keyVaultKeyIdentifier | string | The URI that uniquely specifies the encryption key in Azure Key Vault |
| name | string | The name of the encryption key |
| updatedAt | string (date-time) | The last update date and time of the encryption key |