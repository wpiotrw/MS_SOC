---
layout: Reference
title: Apps - Get Apps - REST API (Power BI Power BI REST APIs) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/rest/api/power-bi/apps/get-apps
uid: api.powerbi.com.power-bi.apps.getapps
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
description: "Returns a list of installed apps. Required Scope App.Read.All Limitations Service principal authentication isn't supported. "
locale: en-us
document_id: f278b4e5-8e91-752f-6c45-0b8c7910953a
document_version_independent_id: 7d9925bb-f60a-9f97-98e9-91a7195ecf4d
original_content_git_url: https://github.com/MicrosoftDocs/powerbi-rest-api-docs-pr/blob/live/docs-ref-autogen/power-bi/Apps/Get-Apps.yml
site_name: Docs
depot_name: MSDN.powerbi-rest-api
page_type: rest
page_kind: operation
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.powerbi-rest-api/{branchName}{pdfName}
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/power-bi/apps/get-apps
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs-ref-autogen/power-bi/Apps/Get-Apps.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
platformId: b41e179b-baa5-6462-505a-8ccd80f73831
---

# Apps - Get Apps

- Service:
    - Power BI REST APIs

- API Version:
    - v1.0

Returns a list of installed apps.

## Required Scope

App.Read.All

## Limitations

Service principal authentication isn't supported. 

```http
GET https://api.powerbi.com/v1.0/myorg/apps
```

## Responses

| Name | Type | Description |
| --- | --- | --- |
| 200 OK | Apps | OK |

## Examples

### Example

#### Sample request

```http
GET https://api.powerbi.com/v1.0/myorg/apps
```

#### Sample response

- Status code:
    - 200

```json
{
  "value": [
    {
      "id": "f089354e-8366-4e18-aea3-4cb4a3a50b48",
      "description": "The finance app",
      "name": "Finance",
      "publishedBy": "Bill",
      "lastUpdate": "2019-01-13T09:46:53.094+02:00"
    },
    {
      "id": "3d9b93c6-7b6d-4801-a491-1738910904fd",
      "description": "The marketing app",
      "name": "Marketing",
      "publishedBy": "Ben",
      "lastUpdate": "2018-11-13T09:46:53.094+02:00"
    }
  ]
}
```

## Definitions

| Name | Description |
| --- | --- |
| App | A Power BI installed app |
| Apps | The OData response wrapper for a list of Power BI installed apps |

### App

Object

A Power BI installed app

| Name | Type | Description |
| --- | --- | --- |
| description | string | The app description |
| id | string (uuid) | The app ID |
| lastUpdate | string (date-time) | The date and time the app was last updated |
| name | string | The app name |
| publishedBy | string | The app publisher |

### Apps

Object

The OData response wrapper for a list of Power BI installed apps

| Name | Type | Description |
| --- | --- | --- |
| @odata.context | string | OData context |
| value | App[] | The list of installed apps |