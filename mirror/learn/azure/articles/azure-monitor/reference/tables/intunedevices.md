---
layout: Conceptual
title: Azure Monitor Logs reference - IntuneDevices - Azure Monitor | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/intunedevices
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
description: Reference for IntuneDevices table in Azure Monitor Logs.
ms.topic: generated-reference
ms.subservice: logs
ms.date: 2026-07-27T00:00:00.0000000Z
locale: en-us
document_id: 0fdcebe5-a6e1-fc9d-e47d-987684bcca59
document_version_independent_id: c2f23993-ba6d-252b-509e-bc7a55c93a9e
original_content_git_url: https://github.com/MicrosoftDocs/azure-monitor-docs-pr/blob/live/articles/azure-monitor/reference/tables/intunedevices.md
site_name: Docs
depot_name: Learn.azure-monitor
page_type: conceptual
toc_rel: ../toc.json
asset_id: azure-monitor/reference/tables/intunedevices
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-monitor/reference/tables/intunedevices.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/9949a35d-c893-4f91-bf98-ae940fc30f5f
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/21f7bb14-0703-4e59-a64b-65dd13773dd3
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 87e16019-fc65-63d3-d2b7-70eb26a056ae
---

# Azure Monitor Logs reference - IntuneDevices - Azure Monitor | Microsoft Learn

Intune devices specialist report.

## Table attributes

| Attribute | Value |
| --- | --- |
| **Resource types** | - |
| **Categories** | IT & Management Tools |
| **Solutions** | LogManagement |
| **Basic** table support | Yes |
| **Auxiliary / Lake** table support | Yes |
| **DCR workspace transformation** support | Yes |
| **Ingestion API** support | No |
| **Sample Queries** | - |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| AADTenantId | string | The AAD Tenant ID |
| AndroidPatchLevel | string | The Android patch level of the device |
| BatchId | string | The unique ID for the exported report |
| \_BilledSize | real | The record size in bytes |
| CategoryName | string | The category name of the device |
| CompliantState | string | The compliant state of the device |
| CreatedDate | string | The date and time of the device entry was created |
| DeviceId | string | The ID of the device |
| DeviceName | string | The name of the device |
| DeviceRegistrationState | string | The registration state of the device |
| DeviceState | string | The state of the device |
| EasID | string | The Emergency Alert System Identification of the device |
| EncryptionStatusString | string | String describing whether the device is encrypted |
| GraphDeviceIsManaged | bool | Boolean describing whether the graph device is managed |
| IMEI | string | The international mobile equipment identifier of the device |
| InGracePeriodUntil | string | The device grace period end time |
| IntuneAccountId | string | The Intune Account ID |
| \_IsBillable | string | Specifies whether ingesting the data is billable. When \_IsBillable is `false` ingestion isn't billed to your Azure account |
| JailBroken | string | String describing whether the device is jail broken |
| JoinType | string | The device join type |
| LastContact | string | The date and time of last contact |
| ManagedBy | string | The authority that the device is managed by |
| ManagedDeviceName | string | The managed device name |
| Manufacturer | string | The manufacturer of the device |
| MEID | string | The mobile equipment identifier of the device |
| Model | string | The model of the device |
| OperationName | string | The name of the operation |
| OS | string | The operating system of the device |
| OSVersion | string | The version of the operating system |
| Ownership | string | The ownership of the device |
| PhoneNumber | string | The phone number |
| PrimaryUser | string | The ID of the primary user |
| ReferenceId | string | The AAD Device ID |
| Result | string | The result of the operation |
| SerialNumber | string | The serial number of the device |
| SkuFamily | string | The stock-keeping unit family of the device |
| SourceSystem | string | The type of agent the event was collected by. For example, `OpsManager` for Windows agent, either direct connect or Operations Manager, `Linux` for all Linux agents, or `Azure` for Azure Diagnostics |
| Stats | dynamic | Statistics about the export, including the number of records exported per export |
| StorageFree | long | The free storage size of the device |
| StorageTotal | long | The total storage size of the device |
| SubscriberCarrierNetwork | string | The subscriber carrier network |
| SupervisedStatusString | string | String describing whether the device is supervised |
| TenantId | string | The Log Analytics workspace ID |
| TimeGenerated | datetime | Date and time when the report was generated (UTC) |
| Type | string | The name of the table |
| UPN | string | The user principal name |
| UserEmail | string | The user email address |
| UserName | string | The user name |
| WifiMacAddress | string | The WiFi MAC address of the device |