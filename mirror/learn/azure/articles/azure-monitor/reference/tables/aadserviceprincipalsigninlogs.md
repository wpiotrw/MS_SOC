---
layout: Conceptual
title: Azure Monitor Logs reference - AADServicePrincipalSignInLogs - Azure Monitor | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/aadserviceprincipalsigninlogs
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
description: Reference for AADServicePrincipalSignInLogs table in Azure Monitor Logs.
ms.topic: generated-reference
ms.subservice: logs
ms.date: 2026-08-27T00:00:00.0000000Z
locale: en-us
document_id: 97ea94e4-45ce-858f-0c1b-d4e0855378b5
document_version_independent_id: 0c7694cb-79bb-3003-9714-fa389ea89436
original_content_git_url: https://github.com/MicrosoftDocs/azure-monitor-docs-pr/blob/live/articles/azure-monitor/reference/tables/aadserviceprincipalsigninlogs.md
site_name: Docs
depot_name: Learn.azure-monitor
page_type: conceptual
toc_rel: ../toc.json
asset_id: azure-monitor/reference/tables/aadserviceprincipalsigninlogs
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-monitor/reference/tables/aadserviceprincipalsigninlogs.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1cfdec6-b0c3-4209-818c-736879856e0e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d0723c1-cf38-4c30-ab3d-5df787b33270
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: f72b4e1b-5a97-4949-9942-d0f612d36fef
---

# Azure Monitor Logs reference - AADServicePrincipalSignInLogs - Azure Monitor | Microsoft Learn

Service principal Microsoft Entra ID sign-in logs.

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
| **Sample Queries** | [Yes](/en-us/azure/azure-monitor/reference/queries/aadserviceprincipalsigninlogs) |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| AADTenantId | string | ID of the AAD tenant. |
| Agent | string | Details of agentic sign-in. |
| AppId | string | Unique GUID representing the app ID in the Microsoft Entra ID |
| AppOwnerTenantId | string | The tenant identifier of the owenr of the application in Microsoft Entra ID |
| AuthenticationContextClassReferences | string | The authentication contexts of the sign-in |
| AuthenticationProcessingDetails | string | Provides the details associated with authentication processor |
| AutonomousSystemNumber | string | Autonomous System Number for the network. |
| \_BilledSize | real | The record size in bytes |
| Category | string | Category of the sign-in event |
| ClientCredentialType | string | The type of client credential used. Examples include client assertion, client secret, etc. |
| ConditionalAccessAudiences | string | Details of the conditional access audiences being applied for the sign-in. |
| ConditionalAccessPolicies | string | Details of the conditional access policies being applied for the sign-in |
| ConditionalAccessStatus | string | Status of all the conditionalAccess policies related to the sign-in |
| CorrelationId | string | ID to provide sign-in trail |
| CreatedDateTime | datetime | Datetime of the sign-in activity. |
| DurationMs | long | The duration of the operation in milliseconds |
| FederatedCredentialId | string | Th identifier of an application's federated identity credential if a federated identity credential was used to sign in. |
| Id | string | Unique ID representing the sign-in activity |
| Identity | string | The identity from the token that was presented when you made the request. It can be a user account, system account, or service principal |
| IPAddress | string | IP address of the client used to sign in |
| \_IsBillable | string | Specifies whether ingesting the data is billable. When \_IsBillable is `false` ingestion isn't billed to your Azure account |
| Level | string | The severity level of the event |
| Location | string | The region of the resource emitting the event |
| LocationDetails | string | Details of the sign-in location |
| NetworkLocationDetails | string | Provides the details associated with Authentication processor. |
| OperationName | string | For sign-ins, this value is always Sign-in activity |
| OperationVersion | string | The REST API version that's requested by the client |
| ResourceDisplayName | string | Name of the resource that the service principal signed into |
| ResourceGroup | string | Resource group for the logs |
| ResourceIdentity | string | ID of the resource that the service principal signed into |
| ResourceOwnerTenantId | string | The tenant identifier of the owner of the resource referenced in the sign in |
| ResourceServicePrincipalId | string | Service Principal Id of the resource |
| ResultDescription | string | Provides the error description for the sign-in operation |
| ResultSignature | string | Contains the error code, if any, for the sign-in operation |
| ResultType | string | The result of the sign-in operation can be Success or Failure |
| ServicePrincipalCredentialKeyId | string | Key id of the service principal that initiated the sign-in |
| ServicePrincipalCredentialThumbprint | string | Thumbprint of the service principal that initiated the sign-in |
| ServicePrincipalId | string | ID of the service principal who initiated the sign-in |
| ServicePrincipalName | string | Service Principal Name of the service principal who initiated the sign-in |
| SessionId | string | Id of the session that was generated during the signIn. |
| SourceSystem | string | The type of agent the event was collected by. For example, `OpsManager` for Windows agent, either direct connect or Operations Manager, `Linux` for all Linux agents, or `Azure` for Azure Diagnostics |
| TenantId | string | The Log Analytics workspace ID |
| TimeGenerated | datetime | The date and time of the event in UTC |
| Type | string | The name of the table |
| UniqueTokenIdentifier | string | Unique token identifier for the request |
| UserAgent | string | User Agent for the sign-in |