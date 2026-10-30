---
layout: Conceptual
title: Create Virtual Machine restore points - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/create-restore-points
breadcrumb_path: ../breadcrumb/azure-compute/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/94/azure-virtual-machines/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/ec2f1827-be25-ec11-b6e6-000d3a4f0f1c
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
author: shsangal
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: shsangal
ms.update-cycle: 365-days
ms.service: azure-virtual-machines
description: Creating Virtual Machine Restore Points with API
ms.subservice: recovery
ms.date: 2026-10-22T00:00:00.0000000Z
ai-usage: ai-assisted
ms.topic: quickstart
ms.custom: template-quickstart
locale: en-us
document_id: 4243beb1-2b2d-d022-09f3-e2382450b5d6
document_version_independent_id: 33ea1e8c-72ca-2f06-7bc0-943b5f712351
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/create-restore-points.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/create-restore-points
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/create-restore-points.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 7433b592-afb4-7972-83b8-99f60020e35b
---

# Create Virtual Machine restore points - Azure Virtual Machines | Microsoft Learn

Use the Azure Compute REST APIs to create application-consistent or crash-consistent restore points for a VM, in the same region or cross-region.

API references: [Restore Points](/en-us/rest/api/compute/restore-points) | [Restore Point Collections](/en-us/rest/api/compute/restore-point-collections) | [PowerShell](/en-us/powershell/module/az.compute/new-azrestorepoint)

## Prerequisites

- [Learn more](concepts-restore-points) about the requirements for a VM restore point.
- Review the [support requirements](/en-us/azure/virtual-machines/concepts-restore-points) and [limitations](/en-us/azure/virtual-machines/virtual-machines-create-restore-points#limitations) before creating restore points.

## Create VM restore points

The following sections outline the steps you need to take to create VM restore points with the Azure Compute REST APIs.

You can find more information in the [Restore Points](/en-us/rest/api/compute/restore-points), [PowerShell](/en-us/powershell/module/az.compute/new-azrestorepoint), and [Restore Point Collections](/en-us/rest/api/compute/restore-point-collections) API documentation.

### Step 1: Create a VM restore point collection

A restore point collection is the parent resource that holds all restore points for a VM.

Call the [Restore Point Collections — Create or Update](/en-us/rest/api/compute/restore-point-collections/create-or-update) API:

```http
PUT https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/restorePointCollections/{collectionName}?api-version=2025-04-01
```

**Request body:**

```json
  {
    "location": "<region>",
    "properties": {
      "source": {
        "id": "<VM Arm Id>"
      },
      "instantAccess": true
    }
  }
```

- Set `location` to the VM's region for a local collection, or to the target region for a cross-region collection (and include the source restore point collection's ARM resource ID in `source.id`).
- To enable Instant Access, add `"instantAccess": true` to `properties`. Instant Access applies only to VMs with Premium SSD v2 or Ultra Disks as data disks. It supports both application-consistent and multi-disk crash-consistent (in preview) restore points created in the collection and requires API version `2025-04-01` or later.

### Step 2: Create a VM restore point

Call the [Restore Points — Create](/en-us/rest/api/compute/restore-points/create) API within the collection created in Step 1:

```http
PUT https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/restorePointCollections/{collectionName}/restorePoints/{restorePointName}?api-version=2025-04-01
```

**Request body:**

```json
  {
    "name": "<restorePointName>",
    "properties": {
      "instantAccessDurationMinutes": 120
    }
  }
```

> 
> **Note:** instantAccessDurationMinutes is an optional parameter. Default is 300 (5 hours). Can be set to a lower value, but not higher than 300. This is applicable for future restore points and NOT for existing restore points already created.

**Key request body properties:**

| Property | Description |
| --- | --- |
| `consistencyMode` | Omit for application-consistent (default). Set to `CrashConsistent` for crash-consistent restore points. |
| `excludeDisks` | Optional. Array of disk identifiers to exclude from the restore point, to reduce storage cost. |
| `instantAccessDurationMinutes` | Optional. *(Instant Access only)* Duration in minutes for Instant Access. Valid range: 60–300. Default: 300 minutes (5 hours). |

To create a multi-disk crash-consistent restore point with a 120-minute Instant Access duration (in preview), use the following request body in the Instant Access-enabled collection from step 1:

```json
{
  "properties": {
    "consistencyMode": "CrashConsistent",
    "instantAccessDurationMinutes": 120
  }
}
```

### Step 3: Track the status of the VM restore point creation

**Local restore points** complete within a few seconds. Check `provisioningState` on the restore point — it transitions from `Creating` to `Succeeded` (or `Failed`).

**Cross-region restore points** are a long-running operation. Poll the [Restore Points — Get](/en-us/rest/api/compute/restore-points/get) API with `$expand=instanceView` to check per-disk copy progress (`completionPercent`). The restore point is usable only after all disk restore points have completed replication.

```http
GET https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/restorePointCollections/{collectionName}/restorePoints/{restorePointName}?$expand=instanceView&api-version=2025-04-01
```

**Instant Access status:** If the collection has Instant Access enabled, check `instantAccessState` on the restore point to validate the consolidated access state across all disk restore points. A value of `InstantAccess` or `AvailableWithInstantAccess` means the restore point is ready for fast disk restoration. Use the per-disk `snapshotAccessState` in `instanceView` only when you need to inspect the state of an individual disk restore point.

### Step 4: Disable Instant Access

Use the following REST API call to disable IA enabled on the VM.

```http
PATCH https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/restorePointCollections/{restorePointCollectionName}?api-version=2025-04-01
```

**Request body:**

```json
  {
    "location": "<region>",
    "properties": {
      "source": {
        "id": "<VM Arm Id>"
      },
      "instantAccess": false
    }
  }
```