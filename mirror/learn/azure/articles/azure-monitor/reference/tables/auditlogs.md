---
layout: Conceptual
title: Azure Monitor Logs reference - AuditLogs - Azure Monitor | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/auditlogs
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
description: Reference for AuditLogs table in Azure Monitor Logs.
ms.topic: generated-reference
ms.subservice: logs
ms.date: 2026-08-27T00:00:00.0000000Z
locale: en-us
document_id: 3e8a08ac-da92-a6f0-ad8d-995c7fbe3ca0
document_version_independent_id: f8c6739a-2ddb-19d1-1bb6-b084981dc70a
original_content_git_url: https://github.com/MicrosoftDocs/azure-monitor-docs-pr/blob/live/articles/azure-monitor/reference/tables/auditlogs.md
site_name: Docs
depot_name: Learn.azure-monitor
page_type: conceptual
toc_rel: ../toc.json
asset_id: azure-monitor/reference/tables/auditlogs
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-monitor/reference/tables/auditlogs.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/9949a35d-c893-4f91-bf98-ae940fc30f5f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/21f7bb14-0703-4e59-a64b-65dd13773dd3
platformId: 653b3712-3fa9-e08d-c491-4af990b6927e
---

# Azure Monitor Logs reference - AuditLogs - Azure Monitor | Microsoft Learn

Audit log for Microsoft Entra ID. Includes system activity information about user and group management managed applications and directory activities.

## Table attributes

| Attribute | Value |
| --- | --- |
| **Resource types** | microsoft.azureadgraph/tenants,microsoft.graph/tenants |
| **Categories** | Azure Resources, Security |
| **Solutions** | LogManagement |
| **Basic** table support | No |
| **Auxiliary / Lake** table support | Yes |
| **DCR workspace transformation** support | Yes |
| **Ingestion API** support | No |
| **Sample Queries** | - |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| AADOperationType | string | Type of the operation. Possible values are Add Update Delete and Other. |
| AADTenantId | string | ID of the ADD tenant |
| ActivityDateTime | datetime | Date and time the activity was performed in UTC. |
| ActivityDisplayName | string | Activity name or the operation name. Examples include Create User and Add member to group. For full list see Azure AD activity list. |
| AdditionalDetails | dynamic | Indicates additional details on the activity. |
| \_BilledSize | real | The record size in bytes |
| Category | string | Currently Audit is the only supported value. |
| CorrelationId | string | Optional GUID that's passed by the client. Can help correlate client-side operations with server-side operations and is useful when tracking logs that span services. |
| DurationMs | long | Property is not used and can be ignored. |
| Id | string | GUID that uniquely identifies the activity. |
| Identity | string | Identity from the token that was presented when the request was made. The identity can be a user account system account or service principal. |
| InitiatedBy | dynamic | User or app initiated the activity. |
| \_IsBillable | string | Specifies whether ingesting the data is billable. When \_IsBillable is `false` ingestion isn't billed to your Azure account |
| Level | string | Message type. This is currently always Informational. |
| Location | string | Location of the datacenter. |
| LoggedByService | string | Service that initiated the activity (For example: Self-service Password Management Core Directory B2C Invited Users Microsoft Identity Manager Privileged Identity Management. |
| OperationName | string | Name of the operation. |
| OperationVersion | string | REST API version that's requested by the client. |
| Resource | string |  |
| ResourceGroup | string |  |
| ResourceId | string |  |
| ResourceProvider | string |  |
| Result | string | Result of the activity. Possible values are: success failure timeout unknownFutureValue. |
| ResultDescription | string | Additional description of the result. |
| ResultReason | string | Describes cause of failure or timeout results. |
| ResultSignature | string | Property is not used and can be ignored. |
| ResultType | string | Result of the operation. Possible values are Success and Failure. |
| SourceSystem | string | The type of agent the event was collected by. For example, `OpsManager` for Windows agent, either direct connect or Operations Manager, `Linux` for all Linux agents, or `Azure` for Azure Diagnostics |
| TargetResources | dynamic | Indicates information on which resource was changed due to the activity. Target Resource Type can be User Device Directory App Role Group Policy or Other. |
| TimeGenerated | datetime | Date and time the record was created. |
| Type | string | The name of the table |