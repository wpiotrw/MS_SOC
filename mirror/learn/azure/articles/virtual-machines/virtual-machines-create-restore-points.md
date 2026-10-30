---
layout: Conceptual
title: Use virtual machine restore points - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/virtual-machines-create-restore-points
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
description: Learn how to use virtual machine restore points.
ms.subservice: recovery
ms.topic: concept-article
ms.date: 2026-10-22T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: conceptual
locale: en-us
document_id: 03f36fb1-d6a5-3d93-3296-6279178a8f6b
document_version_independent_id: 1da7700f-2c1b-4345-51b5-04fc0f8e7092
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/virtual-machines-create-restore-points.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/virtual-machines-create-restore-points
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/virtual-machines-create-restore-points.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 11a69b67-6f6d-47b4-9b5d-f76438d710d8
---

# Use virtual machine restore points - Azure Virtual Machines | Microsoft Learn

Virtual Machine restore points capture the configuration and point-in-time disk snapshots of a virtual machine, enabling granular backup and recovery. You can create restore points at regular intervals to reduce data loss exposure and meet recovery time objectives (RTOs).

For a broader comparison of backup options, see [Backup and restore options for Virtual Machines in Azure](/en-us/azure/virtual-machines/backup-recovery).

## About Virtual Machine restore points

A Virtual Machine restore point stores:

- The Virtual Machine configuration at the time of capture.
- Point-in-time snapshots of all attached managed disks—one **disk restore point** per disk.

Virtual Machine restore points are grouped into **restore point collections**, an Azure Resource Manager resource scoped to a specific Virtual Machine. For ARM template examples, see the [Virtual-Machine-Restore-Points](https://github.com/Azure/Virtual-Machine-Restore-Points) repository.

Restore points are **incremental**: the first restore point is a full copy; each subsequent one captures only the changes since the previous snapshot. You can exclude individual disks to reduce storage costs.

Each disk of the Virtual Machine has a corresponding disk restore points within the restore points. For example, if a Virtual Machine has three disks (One OS disk and two data disks) and each restore point has three disk restore points in it.

Once the disk restore points are created, Azure automatically initiates a background data copy from source disk to snapshot.

### Consistency modes

| Mode | How it works | Set via |
| --- | --- | --- |
| **Application-consistent** | Uses Volume Shadow Copy Service (VSS) writers (Windows) or pre/post scripts (Linux) to flush in-flight application data before the snapshot. | Default when `consistencyMode` is omitted. |
| **Crash-consistent** | Captures a write-order-consistent snapshot of all disks, equivalent to Virtual Machine state after a power outage or crash. | Set `consistencyMode` to `CrashConsistent` in the creation request. |

### Instant Access

For virtual machine restore points, [Instant Access](disks-instant-access-snapshots?tabs=azure-cli,azure-cli-snapshot-state) applies only to VMs with Premium SSD v2 or Ultra Disks as data disks. It supports both application-consistent and multi-disk crash-consistent (in preview) restore points. When you enable Instant Access on the restore point collection, you can start restoring disks immediately from the snapshot without waiting for full hydration, which significantly reduces RTOs.

### Key concepts in Instant Access

| Property | Description |
| --- | --- |
| `instantAccess` | Boolean property set on the restore point **collection**. Set to `true` to enable Instant Access for all restore points in the collection. Default is `false`. |
| `instantAccessDurationMinutes` | Integer property set on each **restore point**. Specifies how long Instant Access remains active, in minutes. Valid range: 60–300 minutes. Default: 300 (5 hours). |
| `snapshotAccessState` | Read-only property on an individual disk restore point. Indicates the Instant Access state of that specific disk. |
| `instantAccessState` | Read-only property that indicates the consolidated access status of all disk restore points within a restore point. Possible values: **Pending**: The restore point can't be used for restore, copy, or offline download. This state applies if any disk restore point has a `snapshotAccessState` of `Pending`. **Available**: The restore point can be used for restore, cross-region copy, and offline download. This state applies when all disk restore points have a `snapshotAccessState` of `Available`, typically after `instantAccessDurationMinutes` expires. **InstantAccess**: The restore point supports fast disk restore but can't be copied or downloaded. This state applies when all disk restore points have a `snapshotAccessState` of `InstantAccess`. **AvailableWithInstantAccess**: The restore point supports fast disk restore and can also be copied and downloaded. This state applies when all disk restore points have a `snapshotAccessState` of `AvailableWithInstantAccess` and `instantAccessDurationMinutes` hasn't expired. |
| API Version | **2025-04-01 or later** |
| Supported regions | All public regions. For restore point availability, see the [support matrix](concepts-restore-points). |
| Pricing | Instant access snapshots are billed using a usage‑based model with two types of charges:  1. Snapshot storage charge  2. One‑time restore operation charge. **Snapshot storage charge**: You are billed only for the additional storage used by an instant access snapshot while it is active. When an instant access snapshot is first created, it does not incur any storage cost. The snapshot initially shares data with the source disk. As data on the source disk is modified or deleted over time, the snapshot preserves the original point‑in‑time data, and its storage usage grows. As a result, you pay only for the changed data, not for a full copy of the disk. If no data is modified on the source disk, the snapshot continues to incur no additional storage charges. **Restore operation charge** Each time you restore a disk from an instant access snapshot, a one‑time restore fee is charged. This fee is calculated based on the provisioned size of the disk at the time of restore, providing predictable and transparent pricing for restore operations. Learn more about Instant Access Snapshot billing in [here](https://azure.microsoft.com/pricing/details/managed-disks/) |

## Restore points for Virtual Machine in scale sets and availability sets

Restore points are created per individual Virtual Machine. To back up all instances in a virtual machine scale set (Flexible orchestration mode) or an availability set, create restore points for each Virtual Machine separately.

> 
> **Note:** Virtual machine scale sets with **Uniform orchestration** are not supported.

## Throttling limits for Restore points

| **Scope** | **Operation** | **Limit per hour** |
| --- | --- | --- |
| Virtual Machine | RestorePoints.RestorePointOperation.PUT (Create new **Application Consistent**) | 3 |
| Virtual Machine | RestorePoints.RestorePointOperation.PUT (Create new **Crash Consistent**) | 3 |
| Target restore point collection | RestorePoints.RestorePointOperation.PUT (Copy any Virtual Machine Restore Point) | 3 |

Note

Requests that exceed limits return HTTP 429. Retry after the interval specified in the response.

## Limitations

**General:**

- Restore points are supported only for managed disks.
- Write-accelerated disks, ephemeral OS disks, and shared disks aren't supported for crash consistency mode.
- Multi-disk crash-consistent restore points aren't supported on VMs with NVMe disk controllers or VMs running on Azure Boost hardware, regardless of disk type.
- Multi-disk crash consistency for VMs with Premium SSD v2 or Ultra data disks is supported in public preview for SCSI VMs only, subject to the [preview requirements](concepts-restore-points#multi-disk-crash-consistency-for-premium-ssd-v2-and-ultra-disks-public-preview). This preview doesn't change existing support for Standard HDD, Standard SSD, and Premium SSD disks.
- Ephemeral OS disks, and shared disks aren't supported for application consistency mode.
- A maximum of 500 Virtual Machine restore points can be retained at any time for a Virtual Machine, irrespective of the number of restore point collections or consistency type.
- Concurrent creation of restore points for the same Virtual Machine isn't supported.
- Restore points for virtual machine scale sets in Uniform orchestration mode aren't supported.
- Movement of Virtual Machines between resource groups or subscriptions isn't supported when the Virtual Machine has restore points. Moving the Virtual Machine between resource groups or subscriptions doesn't update the source Virtual Machine reference in the restore point and causes a mismatch of Resource Manager IDs between the actual Virtual Machine and the restore points.

**Cross-region copy (Preview):**

- Private links aren't supported when copying restore points across regions.
- CMK-encrypted restore points are copied as PMK-encrypted in the target region.

**Instant Access:**

- Applies only to VMs with Premium SSD v2 or Ultra Disks as data disks, for both application-consistent and multi-disk crash-consistent (in preview) restore points.
- Maximum 50 concurrent Instant Access restore point creations per subscription per region.
- Currently supported via REST API, Azure SDK, CLI, and ARM templates. Currently not supported via Portal.

For a complete list of limitations, disk type support, OS support, and API version requirements, see [Support matrix for VM restore points](/en-us/azure/virtual-machines/concepts-restore-points).

## Troubleshoot Virtual Machine restore points

Most common restore point failures are attributed to the communication with the VM agent and extension. To resolve failures, follow the steps in [Troubleshoot restore point failures](restore-point-troubleshooting).