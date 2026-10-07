---
layout: Conceptual
title: Azure Monitor Logs reference - MicrosoftGraphActivityLogs - Azure Monitor | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/microsoftgraphactivitylogs
breadcrumb_path: ../../../breadcrumb/azure-monitor/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/20/azure-monitor/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/3887dc70-2025-ec11-b6e6-000d3a4f09d0
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
author: austinmccollum
learn_banner_products:
- azure
manager: tedhudek
ms.author: austinmc
ms.service: azure-monitor
description: Reference for MicrosoftGraphActivityLogs table in Azure Monitor Logs.
ms.topic: generated-reference
ms.subservice: logs
ms.date: 2026-07-27T00:00:00.0000000Z
locale: en-us
document_id: 68250dcd-a61e-a324-a09f-4c3ef9c18d5e
document_version_independent_id: 025a7ec8-c348-7a22-0b6a-7cd6f4ddbf62
original_content_git_url: https://github.com/MicrosoftDocs/azure-monitor-docs-pr/blob/live/articles/azure-monitor/reference/tables/microsoftgraphactivitylogs.md
site_name: Docs
depot_name: Learn.azure-monitor
page_type: conceptual
toc_rel: ../toc.json
asset_id: azure-monitor/reference/tables/microsoftgraphactivitylogs
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-monitor/reference/tables/microsoftgraphactivitylogs.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/9949a35d-c893-4f91-bf98-ae940fc30f5f
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/21f7bb14-0703-4e59-a64b-65dd13773dd3
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: fa733dca-dc5c-41df-2bc1-8bb6286ffc70
---

# Azure Monitor Logs reference - MicrosoftGraphActivityLogs - Azure Monitor | Microsoft Learn

Microsoft Graph Activity Logs provide details of API requests made to Microsoft Graph for resources in the tenant.

## Table attributes

| Attribute | Value |
| --- | --- |
| **Resource types** | - |
| **Categories** | Audit, Security |
| **Solutions** | LogManagement |
| **Basic** table support | Yes |
| **Auxiliary / Lake** table support | Yes |
| **DCR workspace transformation** support | Yes |
| **Ingestion API** support | No |
| **Sample Queries** | [Yes](/en-us/azure/azure-monitor/reference/queries/microsoftgraphactivitylogs) |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| AadTenantId | string | The Azure AD tenant ID. |
| ApiVersion | string | The API version of the event. |
| AppId | string | The identifier for the application. |
| ATContent | string | Reserved for future use. |
| ATContentH | string | Reserved for future use. |
| ATContentP | string | Reserved for future use. |
| \_BilledSize | real | The record size in bytes |
| ClientAuthMethod | int | Indicates how the client was authenticated. For a public client, the value is 0. If client ID and client secret are used, the value is 1. If a client certificate was used for authentication, the value is 2. |
| ClientRequestId | string | Optional. The client request identifier when sent. If no client request identifier is sent, the value will be equal to the operation identifier. |
| DeviceId | string | The identifier of the device from which the authentication request originated. |
| DurationMs | int | The duration of the request in milliseconds. |
| IdentityProvider | string | The identity provider that authenticated the subject of the token. |
| IPAddress | string | The IP address of the client from where the request occurred. |
| \_IsBillable | string | Specifies whether ingesting the data is billable. When \_IsBillable is `false` ingestion isn't billed to your Azure account |
| Location | string | The name of the region that served the request. |
| OperationId | string | The identifier for the batch. For non-batched requests, this will be unique per request. For batched requests, this will be the same for all requests in the batch. |
| RequestId | string | The identifier representing the request. |
| RequestMethod | string | The HTTP method of the event. |
| RequestUri | string | The URI of the request. |
| ResponseSizeBytes | int | The size of the response in Bytes. |
| ResponseStatusCode | int | The HTTP response status code for the event. |
| Roles | string | The roles in token claims. |
| Scopes | string | The scopes in token claims. |
| ServicePrincipalId | string | The identifier of the servicePrincipal making the request. |
| SessionId | string | The unique identifier for the authentication session. |
| SignInActivityId | string | The identifier representing the sign-in activitys. |
| SourceSystem | string | The type of agent the event was collected by. For example, `OpsManager` for Windows agent, either direct connect or Operations Manager, `Linux` for all Linux agents, or `Azure` for Azure Diagnostics |
| TenantId | string | The Log Analytics workspace ID |
| TimeGenerated | datetime | The date and time the request was received. |
| TokenIssuedAt | datetime | The timestamp the token was issued at. |
| Type | string | The name of the table |
| UniqueTokenId | string | The unique token identifier of the API call used to make the audited change. |
| UserAgent | string | The user agent information related to request. |
| UserId | string | The identifier of the user making the request. |
| Wids | string | Denotes the tenant-wide roles assigned to this user. |