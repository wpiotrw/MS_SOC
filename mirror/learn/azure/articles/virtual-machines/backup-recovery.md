---
layout: Conceptual
title: Overview backup options for VMs - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/backup-recovery
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
author: iamwilliew
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: wwilliams
ms.update-cycle: 365-days
ms.service: azure-virtual-machines
description: Overview backup options for Azure virtual machines.
ms.subservice: recovery
ms.topic: overview
ms.date: 2026-10-20T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: c0212e2d-49be-5bdd-06c5-20baf06824af
document_version_independent_id: 341d7d31-9275-18a5-db19-e105d70fe3a6
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/backup-recovery.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/backup-recovery
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/backup-recovery.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aebdc4a3-c54b-4eea-94e3-663d5e166f57
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1baec8e6-ab38-4b56-bb59-f6282d94f311
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 2995b612-3243-d612-da9d-8c224869e367
---

# Overview backup options for VMs - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows VMs ✔️ Flexible scale sets

You can protect your data by taking backups at regular intervals. There are several backup options available for virtual machines (VMs), depending on your use-case.

## Choose a protection approach

Availability, failover, and backup address different risks. Use this comparison to choose an approach, and validate the supported configuration before combining protection features.

| Recovery need | Approach | Important distinction |
| --- | --- | --- |
| Keep an application available during a zone failure. | Deploy [multiple VMs across availability zones](disks-high-availability#deploy-vms-and-disks-across-three-availability-zones). | Configure application replication and traffic routing between healthy instances. |
| Move an eligible existing zonal VM to another zone in the same region. | [Zone resilience for Azure VMs (Preview)](zone-resilience). | Requires ZRS OS and data disks. Failover is customer-initiated and interrupts the workload. |
| Recover from a zone or regional outage through replication. | [Azure Site Recovery](/en-us/azure/site-recovery/site-recovery-overview). | Review the support requirements for zone-to-zone or region-to-region replication. |
| Recover point-in-time data after deletion or corruption. | Azure Backup, managed snapshots, or VM restore points, described in this article. | Replication doesn't replace historical backups, and backups don't keep an application continuously available. |

Important

Zone resilience for Azure VMs is in preview. Use this preview only for evaluation and testing with nonproduction VMs. Don't use it for production VMs. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

See the [preview limitations](zone-resilience#limitations).

## Azure Backup

You'll use Azure Backup for most use-cases involving backup operations on Azure VMs running production workloads. Azure Backup supports application-consistent backups for both Windows and Linux VMs. Azure Backup creates recovery points that are stored in geo-redundant recovery vaults. When you restore from a recovery point, you can restore entire VM or specific files.

For a simple, hands-on introduction to Azure Backup for Azure VMs, see the [Azure Backup quickstart](/en-us/azure/backup/quick-backup-vm-portal).

For more information on how Azure Backup works, see [Plan your VM backup infrastructure in Azure](/en-us/azure/backup/backup-azure-vms-introduction)

## Azure Site Recovery

Azure Site Recovery protects your VMs from a major disaster scenario. These scenarios may include widespread service interruptions or regional outages caused by natural disasters. You can configure Azure Site Recovery for your VMs so that your applications are recoverable in matter of minutes with a single click. You can replicate to an Azure region of your choice, since recovery isn't restricted to paired regions.

You can run disaster-recovery drills with on-demand test failovers, without affecting your production workloads or ongoing replication. Create recovery plans to orchestrate failover and failback of the entire application running on multiple VMs. The recovery plan feature is integrated with Azure Automation runbooks.

You can get started by [replicating your virtual machines](/en-us/azure/site-recovery/azure-to-azure-quickstart).

## Managed snapshots

In development and test environments, snapshots provide a quick and simple option for backing up VMs that use managed disks. A managed snapshot is a full, read-only copy of a managed disk. Snapshots exist independently of their source disks.

Snapshots can be used to create new managed disks when a VM is rebuilt. They're billed based on the used portion of the disk. For example, if you create a snapshot of a managed disk with provisioned capacity of 64 GB and actual used data size of 10 GB, snapshot will be billed only for the used data size of 10 GB.

For more information on creating snapshots, see:

- [Create copy of VHD stored as a managed disk](windows/snapshot-copy-managed-disk)

## Virtual machine restore points

At this time, you can use Azure REST APIs to back up and restore your VMs. This approach is most often used by independent software vendor (ISVs) or organizations with a relatively small number of VMs to manage.

You can use the API to create a VM restore point collection. The restore point collection itself contains individual restore points for specific VMs. Each restore point stores a VM's configuration and a snapshot for each attached managed disk. To save space and costs, you can exclude any disk from your VM restore points.

Once created, VM restore points can then be used to restore individual disks. To restore a VM, restore all relevant disks and attach them to a new VM.

Learn more about [working with VM restore points](virtual-machines-create-restore-points) and the [restore point collections](/en-us/rest/api/compute/restore-point-collections) API.