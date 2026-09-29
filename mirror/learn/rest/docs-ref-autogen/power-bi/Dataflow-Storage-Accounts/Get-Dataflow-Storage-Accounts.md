---
layout: Reference
title: Dataflow Storage Accounts - Get Dataflow Storage Accounts - REST API (Power BI Power BI REST APIs) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/rest/api/power-bi/dataflow-storage-accounts/get-dataflow-storage-accounts
uid: api.powerbi.com.power-bi.dataflowstorageaccounts.getdataflowstorageaccounts
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
description: 'Returns a list of dataflow storage accounts that the user has access to. Required Scope StorageAccount.Read.All or StorageAccount.ReadWrite.All '
locale: en-us
document_id: f3faaa5a-09ce-6449-8322-fe6f8935030d
document_version_independent_id: f902dc12-4bae-d69f-5b66-c51f32c818f3
original_content_git_url: https://github.com/MicrosoftDocs/powerbi-rest-api-docs-pr/blob/live/docs-ref-autogen/power-bi/Dataflow-Storage-Accounts/Get-Dataflow-Storage-Accounts.yml
site_name: Docs
depot_name: MSDN.powerbi-rest-api
page_type: rest
page_kind: operation
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.powerbi-rest-api/{branchName}{pdfName}
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/power-bi/dataflow-storage-accounts/get-dataflow-storage-accounts
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs-ref-autogen/power-bi/Dataflow-Storage-Accounts/Get-Dataflow-Storage-Accounts.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
platformId: b7a94cf9-0fd1-db93-0ad2-1e002e6750c2
---

# Dataflow Storage Accounts - Get Dataflow Storage Accounts

- Service:
    - Power BI REST APIs

- API Version:
    - v1.0

Returns a list of dataflow storage accounts that the user has access to.

## Required Scope

StorageAccount.Read.All or StorageAccount.ReadWrite.All 

```http
GET https://api.powerbi.com/v1.0/myorg/dataflowStorageAccounts
```

## Responses

| Name | Type | Description |
| --- | --- | --- |
| 200 OK | DataflowStorageAccounts | OK |

## Examples

### Example

#### Sample request

```http
GET https://api.powerbi.com/v1.0/myorg/dataflowStorageAccounts
```

#### Sample response

- Status code:
    - 200

```json
{
  "value": [
    {
      "id": "d692ae06-708c-485e-9987-06ff0fbdbb1f",
      "name": "MyDataflowStorageAccount",
      "isEnabled": true
    }
  ]
}
```

## Definitions

| Name | Description |
| --- | --- |
| DataflowStorageAccount | A Power BI dataflow storage account |
| DataflowStorageAccounts | OData response wrapper for Power BI dataflow storage account list |

### DataflowStorageAccount

Object

A Power BI dataflow storage account

| Name | Type | Description |
| --- | --- | --- |
| id | string (uuid) | The Power BI dataflow storage account ID |
| isEnabled | boolean | Whether workspaces can be assigned to this storage account |
| name | string | The Power BI dataflow storage account name |

### DataflowStorageAccounts

Object

OData response wrapper for Power BI dataflow storage account list

| Name | Type | Description |
| --- | --- | --- |
| @odata.context | string |  |
| value | DataflowStorageAccount[] | The Power BI dataflow storage account list |