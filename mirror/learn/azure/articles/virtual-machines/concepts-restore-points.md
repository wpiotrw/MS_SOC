---
layout: Conceptual
title: Support matrix for VM restore points - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/concepts-restore-points
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
ms.update-cycle: 1095-days
ms.service: azure-virtual-machines
description: Support matrix for VM restore points
ms.topic: concept-article
ms.date: 2026-10-22T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: template-concept
locale: en-us
document_id: 43d439a6-88a4-4737-7908-80ce29452672
document_version_independent_id: 566de138-f91e-2617-806a-61a888bf369e
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/concepts-restore-points.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/concepts-restore-points
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/concepts-restore-points.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/96f6b0a2-2fd7-4de1-936d-89ad6e0eb7cc
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/ef8b0a5a-ba0a-4ec0-8636-48246ccd954f
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 67ec1795-87d1-972c-5f5c-ca5b0833a322
---

# Support matrix for VM restore points - Azure Virtual Machines | Microsoft Learn

This article summarizes the support matrix and limitations of using [VM restore points](virtual-machines-create-restore-points).

## VM restore points support matrix

| **Scenarios** | **Supported by VM restore points** |
| --- | --- |
| VMs using managed disks | Yes |
| VMs using unmanaged disks | No |
| VM sizes | Crash consistency is supported for VM SKUs that support Premium storage. |
| VMs using Ultra Disks | Yes for application consistency. Multi-disk crash consistency is supported in public preview for VMs with SCSI disk controllers, subject to the preview requirements. |
| VMs using Premium SSD v2 disks | Yes for application consistency. Multi-disk crash consistency is supported in public preview for VMs with SCSI disk controllers, subject to the preview requirements. |
| VMs using Ephemeral OS Disks | No. Exclude these disks and create a VM restore point. |
| VMs using shared disks | No. Exclude these disks and create a VM restore point. |
| VMs with extensions | Yes |
| VMs with trusted launch OS disk | Yes |
| Data disks restored from Trusted launch enabled OS Disk | No |
| Confidential VMs | Supported for application consistency only with size [v6-series](/en-us/azure/confidential-computing/virtual-machine-options) in UAE North and Korea Central (**preview**)[v5-series](/en-us/azure/confidential-computing/virtual-machine-options) isn't supported.Not supported for crash consistency. |
| Generation 2 VMs (UEFI boot) | Yes |
| VMs with NVMe disks (Storage optimized - Lsv2-series) | Yes for Application consistent. Not supported for crash consistency. |
| VM Architecture - x64 | Application and crash consistent supported. |
| VM Architecture - ARM64 | Application supported for Linux images only. |
| VMs in Proximity placement groups | Yes |
| VMs in an availability set | Yes. You can create VM restore points for individual VMs within an availability set. You need to create restore points for all the VMs within an availability set to protect an entire availability set instance. |
| VMs inside VMSS with uniform orchestration | No |
| VMs inside VMSS with flexible orchestration | Yes. You can create VM restore points for individual VMs within the virtual machine scale set flex. However, you need to create restore points for all the VMs within the virtual machine scale set flex to protect an entire virtual machine scale set flex instance. |
| Spot VMs (Low priority VMs) | Yes |
| VMs with dedicated hosts | Yes |
| VMs with Host caching enabled | Yes |
| VMs created from marketplace images | Yes |
| VMs created from custom images | Yes |
| VM with HUB (Hybrid Use Benefit) license | Yes |
| VMs migrated from on-prem using Azure Migrate | Yes |
| VMs with RBAC policies | Yes |
| Temporary disk in VMs | Yes. You can create VM restore point for VMs with temporary disks. However, the restore points created don't contain the data from the temporary disks. |
| VMs with Standard HDDs | Yes for application consistency and multi-disk crash consistency. |
| VMs with Standard SSDs | Yes for application consistency and multi-disk crash consistency. |
| VMs with Premium SSDs | Yes for application consistency and multi-disk crash consistency. |
| VMs with ZRS disks | Yes |
| VMs with server-side encryption using service-managed keys | Yes. The encryption of source disk won't be enabled on the restore point. |
| VMs with server-side encryption using customer-managed keys | Yes. The encryption of source disk won't be enabled on the restore point. |
| VMs with double encryption at rest | Yes. The encryption of source disk won't be enabled on the restore point. |
| VMs with Host based encryption enabled with PMK/CMK/Double encryption | Yes. The encryption of source disk won't be enabled on the restore point. |
| VMs with ADE (Azure Disk Encryption) | Yes. The encryption of source disk won't be enabled on the restore point. |
| VMs using Accelerated Networking | Yes |
| VMs running on Azure [Boost](/en-us/azure/azure-boost/overview) hardware | Yes for application consistency. Not supported for multi-disk crash consistency, regardless of disk type, including VMs with SCSI disk controllers. See Azure Boost placement. |
| Minimum Frequency at which App consistent restore point can be taken | 3 hours |
| Minimum Frequency at which crash consistent restore points can be taken | 1 hour |
| API version for Application consistent restore point | 2021-03-01 or later |
| API version for Crash consistent restore point | 2021-07-01 or later |
| Instant Access for application-consistent restore points | Yes, only for VMs with Premium SSD v2 or Ultra Disks as data disks. API version 2025-04-01 or later. |
| Instant Access for multi-disk crash-consistent restore points (public preview) | Yes, only for VMs with Premium SSD v2 and Ultra Disks as data disks. API version 2025-04-01 or later. |

Note

Restore Points (App consistent or crash consistent) can be created by customer at the minimum supported frequency as mentioned above. Taking restore points at a frequency lower than supported would result in failure.

## Instant Access

Instant Access applies only to VMs with Premium SSD v2 or Ultra Disks as data disks. It supports both application-consistent and multi-disk crash-consistent restore points. Enable Instant Access on the restore point collection and set `consistencyMode` to `CrashConsistent` when you create a multi-disk crash-consistent restore point. Instant Access requires API version `2025-04-01` or later. For an example, see [Create VM restore points using APIs](create-restore-points).

## Multi-disk crash consistency for Premium SSD v2 and Ultra Disks (public preview)

The public preview extends existing multi-disk crash-consistent restore point support to VMs with **Premium SSD v2 or Ultra data disks**. For these data disk types, multi-disk crash consistency is supported in public preview only on VMs with **SCSI disk controllers**. The general restrictions on NVMe disk controllers and Azure Boost hardware apply regardless of disk type, not just to this preview. Existing support for Standard HDD, Standard SSD, and Premium SSD disks is unchanged.

The preview is available in all public regions except:

- South Central US.
- West US 3.
- East US 2.

### Azure Boost placement

A VM with a SCSI disk controller and Premium SSD v2 or Ultra data disks can land on newer-generation Azure Boost hardware in US regions. Creating a crash-consistent restore point on that hardware fails with `UserErrorCrashConsistentSnapshotNotSupportedForAzureBoostVms`.

Apply the `LegacyVMNVA` tag to the **VM** to prevent placement on Azure Boost hardware. For tag instructions, see [MANA support for Network Virtual Appliances (NVAs)](/en-us/azure/virtual-network/accelerated-networking-mana-network-virtual-appliance-opt-out). Applying the tag doesn't automatically move an existing VM off Azure Boost hardware.

For an existing VM:

1. Stop the VM.
2. Apply the `LegacyVMNVA` tag to the VM.
3. Redeploy the VM so that placement honors the tag and avoids Azure Boost hardware.
4. Retry creating the crash-consistent restore point.

Important

Plan for downtime when you stop and redeploy the VM. Applying the tag alone doesn't remediate an existing VM's placement.

## Operating system support for application consistency

### Windows

The following Windows operating systems are supported when creating restore points for Azure VMs running on Windows.

- Windows 10 Client (64 bit only)
- Windows Server 2022 (Datacenter/Datacenter Core/Standard)
- Windows Server 2019 (Datacenter/Datacenter Core/Standard)
- Windows Server 2016 (Datacenter/Datacenter Core/Standard)
- Windows Server 2012 R2 (Datacenter/Standard)
- Windows Server 2012 (Datacenter/Standard)
- OS that have reached [extended security update](/en-us/lifecycle/faq/extended-security-updates) won't be supported. Check your product's lifecycle [here](/en-us/lifecycle/products/)

Restore points don't support 32-bit operating systems.

### Linux

For Azure VM Linux VMs, restore points support the list of Linux [distributions endorsed by Azure](linux/endorsed-distros). Note the following:

- Restore points don't support Core OS Linux.
- Restore points don't support 32-bit operating systems.
- Other bring-your-own Linux distributions might work as long as the [Azure VM agent for Linux](extensions/agent-linux) is available on the VM, and as long as Python is supported.
- Restore points don't support a proxy-configured Linux VM if it doesn't have Python version 2.7 or higher installed.
- Restore points don't back up NFS files that are mounted from storage, or from any other NFS server, to Linux or Windows machines. It only backs up disks that are locally attached to the VM.

## Operating system support for crash consistency

- All Operating systems are supported.

## Other limitations

- Restore points are supported only for managed disks.
- Ephemeral OS disks, and Shared disks aren't supported via both consistency modes.
- Restore points APIs require an API of version 2021-03-01 or later for application consistency.
- Restore points APIs require an API of version 2021-03-01 or later for crash consistency.
- A maximum of 10,000 restore point collections can be retained at per subscription per region level.
- A maximum of 500 VM restore points can be retained at any time for a VM, irrespective of the number of restore point collections.
- Concurrent creation of restore points for a VM isn't supported.
- Movement of virtual machines between resource groups or subscriptions is supported when VM has restore points. New restore point creation will fail on the previous VM as the VM no longer exists after the movement. You need to clean up the restore point collection and restore points of the old VM if no longer needed.

## Confidential Virtual Machines (Preview)

| **Scenarios** | **Supported by VM restore points** |
| --- | --- |
| **Consistency type** | Application consistent restore points |
| **Regions supported** | UAE North and Korea Central |
| **VM Sizes** | [v6-series](/en-us/azure/confidential-computing/virtual-machine-options) is supported.[v5-series](/en-us/azure/confidential-computing/virtual-machine-options) isn't supported. |
| **Key rotation** | Supported.When key rotation occurs on a confidential virtual machine, the keys for the VM disks, related restore points, and snapshots update automatically.**Known issue:** The key rotation in this preview release might have performance issues or fail in the following scenarios: - More than 40 disks are attached to one DES when (only) restore points are associated with these disks. If you also directly create disk snapshots outside of Azure backup for these disks connected to the same DES, this lowers the safe threshold of 40 disks to DES mapping.**Recommendation:** Keep the number of disks connected to each DES to a minimum until the issue is resolved. |
| **Prerequisites** | Before you configure backup for CVM, ensure that the following prerequisites are met:Register for the preview feature in your Azure subscription - Name: `RestorePointSupportForConfidentialVMV2` Provider: `Microsoft.Compute`. The registration is autoapproved. You can follow the steps [here to do this on the portal](/en-us/azure/azure-resource-manager/management/preview-features).You can also run the following PowerShell cmdlet.`azurepowershell-interactive Register-AzProviderFeature -FeatureName "RestorePointSupportForConfidentialVMV2" -ProviderNamespace "Microsoft.Compute" `Identify or create a Confidential VM (CVM) in a supported region. See the [supported regions](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=virtual-machines). |

Note

Public preview of cross-region copy of VM restore points is available, with the following limitations:

- Private links aren't supported when copying restore points across regions or creating restore points in a region other than the source VM.
- Customer-managed key encrypted restore points, when copied to a target region or created directly in the target region are created as platform-managed key encrypted restore points.
- No portal support for cross region copy and cross region creation of restore points