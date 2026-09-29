---
layout: Reference
title: Reports - Get Reports - REST API (Power BI Power BI REST APIs) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/rest/api/power-bi/reports/get-reports
uid: api.powerbi.com.power-bi.reports.getreports
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
description: Returns a list of reports from My workspace. This API also returns shared reports and reports from shared apps.
locale: en-us
document_id: e96df0b2-311c-e6ae-b7a2-7d679683fd45
document_version_independent_id: ff025f37-6bab-6ce0-101f-71ee4d65b5cb
original_content_git_url: https://github.com/MicrosoftDocs/powerbi-rest-api-docs-pr/blob/live/docs-ref-autogen/power-bi/Reports/Get-Reports.yml
site_name: Docs
depot_name: MSDN.powerbi-rest-api
page_type: rest
page_kind: operation
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.powerbi-rest-api/{branchName}{pdfName}
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/power-bi/reports/get-reports
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs-ref-autogen/power-bi/Reports/Get-Reports.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
platformId: 774fdee3-03c2-c066-ab92-c8284e395553
---

# Reports - Get Reports

- Service:
    - Power BI REST APIs

- API Version:
    - v1.0

Returns a list of reports from **My workspace**.

This API also returns shared reports and reports from shared apps. Reports that reside in shared workspaces can be accessed using the [Get Reports In Group API](/en-us/rest/api/power-bi/reports/get-reports-in-group).

Since paginated reports (RDL) don't have a dataset, the dataset ID value in the API response for paginated reports isn't displayed.

## Required Scope

Report.ReadWrite.All or Report.Read.All 

```http
GET https://api.powerbi.com/v1.0/myorg/reports
```

## Responses

| Name | Type | Description |
| --- | --- | --- |
| 200 OK | Reports | OK |

## Examples

### Example

#### Sample request

```http
GET https://api.powerbi.com/v1.0/myorg/reports
```

#### Sample response

- Status code:
    - 200

```json
{
  "value": [
    {
      "datasetId": "cfafbeb1-8037-4d0c-896e-a46fb27ff229",
      "id": "5b218778-e7a5-4d73-8187-f10824047715",
      "name": "SalesMarketing",
      "webUrl": "https://app.powerbi.com//reports/5b218778-e7a5-4d73-8187-f10824047715",
      "embedUrl": "https://app.powerbi.com/reportEmbed?reportId=5b218778-e7a5-4d73-8187-f10824047715"
    }
  ]
}
```

## Definitions

| Name | Description |
| --- | --- |
| PrincipalType | The principal type |
| Report | A Power BI report. The API returns a subset of the following list of report properties. The subset depends on the API called, caller permissions, and the availability of data in the Power BI database. |
| Reports | The OData response wrapper for a Power BI report collection |
| ReportUser | A Power BI user access right entry for a report |
| ReportUserAccessRight | The access right that the user has for the report (permission level) |
| ServicePrincipalProfile | A Power BI service principal profile. Only relevant for [Power BI Embedded multi-tenancy solution](/en-us/power-bi/developer/embedded/embed-multi-tenancy). |
| Subscription | An email subscription for a Power BI item (such as a report or a dashboard) |
| SubscriptionUser | A Power BI email subscription user |

### PrincipalType

Enumeration

The principal type

| Value | Description |
| --- | --- |
| None | No principal type. Use for whole organization level access. |
| User | User principal type |
| Group | Group principal type |
| App | Service principal type |

### Report

Object

A Power BI report. The API returns a subset of the following list of report properties. The subset depends on the API called, caller permissions, and the availability of data in the Power BI database.

| Name | Type | Description |
| --- | --- | --- |
| appId | string | The app ID, returned only if the report belongs to an app |
| datasetId | string | The dataset ID of the report |
| description | string | The report description |
| embedUrl | string | The embed URL of the report |
| format | string | The report definition format type. For **PowerBIReport**:<br><br>- [PBIR](/en-us/power-bi/developer/projects/projects-report?tabs=v2,desktop#pbir-format)<br>- [PBIRLegacy](/en-us/power-bi/developer/projects/projects-report?tabs=v2,desktop#reportjson)<br><br><br>For **PaginatedReport**:<br><br>- [`RDL`](/en-us/power-bi/paginated-reports/report-definition-language) |
| id | string (uuid) | The report ID |
| isOwnedByMe | boolean | Indicates whether the current user has the ability to either modify or create a copy of the report. |
| name | string | The name of the report. App reports start with the prefix [App]. |
| originalReportId | string (uuid) | The actual report ID when the workspace is published as an app. |
| reportType | enum:<br>- PaginatedReport<br>- PowerBIReport | The report type |
| subscriptions | Subscription[] | (Empty Value) The subscription details for a Power BI item (such as a report or a dashboard). This property will be removed from the payload response in an upcoming release. You can retrieve subscription information for a Power BI report by using the [Get Report Subscriptions as Admin](/en-us/rest/api/power-bi/admin/reports-get-report-subscriptions-as-admin) API call. |
| users | ReportUser[] | (Empty value) The user access details for a Power BI report. This property will be removed from the payload response in an upcoming release. You can retrieve user information on a Power BI report by using the [Get Report Users as Admin](/en-us/rest/api/power-bi/admin/reports-get-report-users-as-admin) API call, or the [PostWorkspaceInfo](/en-us/rest/api/power-bi/admin/workspace-info-post-workspace-info) API call with the `getArtifactUsers` parameter. |
| webUrl | string | The web URL of the report |

### Reports

Object

The OData response wrapper for a Power BI report collection

| Name | Type | Description |
| --- | --- | --- |
| @odata.context | string | OData context |
| value | Report[] | The report collection |

### ReportUser

Object

A Power BI user access right entry for a report

| Name | Type | Description |
| --- | --- | --- |
| displayName | string | Display name of the principal |
| emailAddress | string | Email address of the user |
| graphId | string | Identifier of the principal in Microsoft Graph. Only available for admin APIs. |
| identifier | string | Identifier of the principal |
| principalType | PrincipalType | The principal type |
| profile | ServicePrincipalProfile | A Power BI service principal profile. Only relevant for [Power BI Embedded multi-tenancy solution](/en-us/power-bi/developer/embedded/embed-multi-tenancy). |
| reportUserAccessRight | ReportUserAccessRight | The access right that the user has for the report (permission level) |
| userType | string | Type of the user. |

### ReportUserAccessRight

Enumeration

The access right that the user has for the report (permission level)

| Value | Description |
| --- | --- |
| None | No permission to content in report |
| Read | Grants Read access to content in report |
| ReadWrite | Grants Read and Write access to content in report |
| ReadReshare | Grants Read and Reshare access to content in report |
| ReadCopy | Grants Read and Copy access to content in report |
| Owner | Grants Read, Write and Reshare access to content in report |

### ServicePrincipalProfile

Object

A Power BI service principal profile. Only relevant for [Power BI Embedded multi-tenancy solution](/en-us/power-bi/developer/embedded/embed-multi-tenancy).

| Name | Type | Description |
| --- | --- | --- |
| displayName | string | The service principal profile name |
| id | string (uuid) | The service principal profile ID |

### Subscription

Object

An email subscription for a Power BI item (such as a report or a dashboard)

| Name | Type | Description |
| --- | --- | --- |
| artifactDisplayName | string | The name of the subscribed Power BI item (such as a report or a dashboard) |
| artifactId | string (uuid) | The ID of the subscribed Power BI item (such as a report or a dashboard) |
| artifactType | string | The type of Power BI item (for example a `Report`, `Dashboard`, or `Dataset`) |
| attachmentFormat | string | Format of the report attached in the email subscription |
| endDate | string (date-time) | The end date and time of the email subscription |
| frequency | string | The frequency of the email subscription |
| id | string (uuid) | The subscription ID |
| isEnabled | boolean | Whether the email subscription is enabled |
| linkToContent | boolean | Whether a subscription link exists in the email subscription |
| previewImage | boolean | Whether a screenshot of the report exists in the email subscription |
| startDate | string (date-time) | The start date and time of the email subscription |
| subArtifactDisplayName | string | The page name of the subscribed Power BI item, if it's a report. |
| title | string | The app name |
| users | SubscriptionUser[] | The details of each email subscriber. When using the [Get User Subscriptions As Admin](/en-us/rest/api/power-bi/admin/users-get-user-subscriptions-as-admin) API call, the returned value is an empty array (null). This property will be removed from the payload response in an upcoming release. You can retrieve subscription information on a Power BI report or dashboard by using the [Get Report Subscriptions As Admin](/en-us/rest/api/power-bi/admin/reports-get-report-subscriptions-as-admin) or [Get Dashboard Subscriptions As Admin](/en-us/rest/api/power-bi/admin/dashboards-get-dashboard-subscriptions-as-admin) API calls. |

### SubscriptionUser

Object

A Power BI email subscription user

| Name | Type | Description |
| --- | --- | --- |
| displayName | string | Display name of the principal |
| emailAddress | string | Email address of the user |
| graphId | string | Identifier of the principal in Microsoft Graph. Only available for admin APIs. |
| identifier | string | Identifier of the principal |
| principalType | PrincipalType | The principal type |
| profile | ServicePrincipalProfile | A Power BI service principal profile. Only relevant for [Power BI Embedded multi-tenancy solution](/en-us/power-bi/developer/embedded/embed-multi-tenancy). |
| userType | string | Type of the user. |