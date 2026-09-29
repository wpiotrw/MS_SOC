---
layout: Reference
title: Pipelines - Get Pipelines - REST API (Power BI Power BI REST APIs) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/rest/api/power-bi/pipelines/get-pipelines
uid: api.powerbi.com.power-bi.pipelines.getpipelines
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
description: 'Returns a list of deployment pipelines that the user has access to. Required Scope Pipeline.Read.All or Pipeline.ReadWrite.All '
locale: en-us
document_id: 90970257-6669-12b5-2b38-40efe190ed46
document_version_independent_id: 023c3267-db73-e58b-a63c-9c15dbf9a618
original_content_git_url: https://github.com/MicrosoftDocs/powerbi-rest-api-docs-pr/blob/live/docs-ref-autogen/power-bi/Pipelines/Get-Pipelines.yml
site_name: Docs
depot_name: MSDN.powerbi-rest-api
page_type: rest
page_kind: operation
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.powerbi-rest-api/{branchName}{pdfName}
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/power-bi/pipelines/get-pipelines
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs-ref-autogen/power-bi/Pipelines/Get-Pipelines.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
platformId: 156c6e1e-3eca-5698-cfb3-3265883a6c92
---

# Pipelines - Get Pipelines

- Service:
    - Power BI REST APIs

- API Version:
    - v1.0

Returns a list of deployment pipelines that the user has access to.

## Required Scope

Pipeline.Read.All or Pipeline.ReadWrite.All 

```http
GET https://api.powerbi.com/v1.0/myorg/pipelines
```

## Responses

| Name | Type | Description |
| --- | --- | --- |
| 200 OK | Pipelines | OK |

## Examples

### Example

#### Sample request

```http
GET https://api.powerbi.com/v1.0/myorg/pipelines
```

#### Sample response

- Status code:
    - 200

```json
{
  "value": [
    {
      "id": "a5ded933-57b7-41f4-b072-ed4c1f9d5824",
      "displayName": "Marketing Deployment Pipeline",
      "description": "Power BI deployment pipeline to manage marketing reports"
    }
  ]
}
```

## Definitions

| Name | Description |
| --- | --- |
| Pipeline | A Power BI pipeline |
| Pipelines | OData response wrapper for a collection of Power BI deployment pipelines |
| PipelineStage | A Power BI deployment pipeline stage |

### Pipeline

Object

A Power BI pipeline

| Name | Type | Description |
| --- | --- | --- |
| description | string | The deployment pipeline description |
| displayName | string | The deployment pipeline display name |
| id | string (uuid) | The deployment pipeline ID |
| stages | PipelineStage[] | The collection of deployment pipeline stages. Only returned when `$expand` is set to `stages` in the request. |

### Pipelines

Object

OData response wrapper for a collection of Power BI deployment pipelines

| Name | Type | Description |
| --- | --- | --- |
| @odata.context | string | OData context |
| value | Pipeline[] | The collection of deployment pipelines |

### PipelineStage

Object

A Power BI deployment pipeline stage

| Name | Type | Description |
| --- | --- | --- |
| order | integer | The stage order, starting from zero. |
| workspaceId | string (uuid) | The assigned workspace ID. Only applicable when there's an assigned workspace. |
| workspaceName | string | The assigned workspace name. Only applicable when there's an assigned workspace and the user has access to the workspace. |