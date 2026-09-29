---
layout: Reference
title: Admin - Get Power BI Encryption Keys - REST API (Power BI Power BI REST APIs) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/rest/api/power-bi/admin/get-power-bi-encryption-keys
uid: api.powerbi.com.power-bi.admin.getpowerbiencryptionkeys
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
description: Returns the encryption keys for the tenant. Permissions The user must be a Fabric administrator or authenticate using a service principal.
locale: en-us
document_id: 5147c86a-5f79-aa81-e5c3-b13a10e1eaa3
document_version_independent_id: 657f53a4-99c6-40d8-4913-9a16b96ace25
original_content_git_url: https://github.com/MicrosoftDocs/powerbi-rest-api-docs-pr/blob/live/docs-ref-autogen/power-bi/Admin/Get-Power-BI-Encryption-Keys.yml
site_name: Docs
depot_name: MSDN.powerbi-rest-api
page_type: rest
page_kind: operation
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.powerbi-rest-api/{branchName}{pdfName}
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/power-bi/admin/get-power-bi-encryption-keys
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs-ref-autogen/power-bi/Admin/Get-Power-BI-Encryption-Keys.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
platformId: 44ca5423-d8aa-ba11-f707-e24b0a4c3f72
---

# Admin - Get Power BI Encryption Keys

- Service:
    - Power BI REST APIs

- API Version:
    - v1.0

Returns the encryption keys for the tenant.

## Permissions

- The user must be a Fabric administrator or authenticate using a service principal.
- Delegated permissions are supported.

When running under service prinicipal authentication, an app **must not** have any admin-consent required premissions for Power BI set on it in the Azure portal.

## Required Scope

Tenant.Read.All or Tenant.ReadWrite.All

Relevant only when authenticating via a standard delegated admin access token. Must not be present when authentication via a service principal is used.

## Limitations

Maximum 200 requests per hour.

```http
GET https://api.powerbi.com/v1.0/myorg/admin/tenantKeys
```

## Responses

| Name | Type | Description |
| --- | --- | --- |
| 200 OK | TenantKeys | OK |

## Examples

### Example

#### Sample request

```http
GET https://api.powerbi.com/v1.0/myorg/admin/tenantKeys
```

#### Sample response

- Status code:
    - 200

```json
{
  "value": [
    {
      "id": "82d9a37a-2b45-4221-b012-cb109b8e30c7",
      "name": "Contoso Sales",
      "keyVaultKeyIdentifier": "https://contoso-vault2.vault.azure.net/keys/ContosoKeyVault/b2ab4ba1c7b341eea5ecaaa2wb54c4d2",
      "isDefault": true,
      "createdAt": "2019-04-30T21:35:15.867-07:00",
      "updatedAt": "2019-04-30T21:35:15.867-07:00"
    }
  ]
}
```

## Definitions

| Name | Description |
| --- | --- |
| TenantKey | Encryption key information |
| TenantKeys | Encryption keys information |

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

### TenantKeys

Object

Encryption keys information

| Name | Type | Description |
| --- | --- | --- |
| @odata.context | string |  |
| value | TenantKey[] | Encryption keys |