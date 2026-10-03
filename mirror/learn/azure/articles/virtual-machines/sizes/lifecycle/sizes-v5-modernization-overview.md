---
layout: Conceptual
title: Modernize to the v5 VM series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/lifecycle/sizes-v5-modernization-overview
breadcrumb_path: ../../../breadcrumb/azure-compute/toc.json
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
author: mattmcinnes
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: mattmcinnes
ms.author: mattmcinnes
ms.update-cycle: 1095-days
description: Plan a transition from earlier D-family and E-family Azure VM series to the v5 series, including effort by starting point, target families, what changes, and transition methods.
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.topic: overview
ms.date: 2026-09-25T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: e57eefb5-6701-cb12-3200-b681c127e8cc
document_version_independent_id: eff1b8f1-3b3d-cfab-ae46-3712e0186160
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/lifecycle/sizes-v5-modernization-overview.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/lifecycle/sizes-v5-modernization-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/lifecycle/sizes-v5-modernization-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: cfbf4e5e-57e3-5e6b-ff8e-7de56d1eaeaf
---

# Modernize to the v5 VM series - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows VMs

The v5 Azure VM series is a straightforward modernization target for workloads running on earlier VM generations. It offers better CPU performance, storage, network bandwidth, and size choices.

This article describes the modernization journey for existing workloads that transition from earlier D-family and E-family generations, and for new deployments that require v5 compatibility or availability.

Note

The v5 series provides the smoothest transition for existing workloads. To access the latest features and performance, transition to the v6 or v7 series. In the [VM lifecycle](lifecycle-overview), v5 is in the *Extended* stage and v6 and v7 are in the *Current* stage. For v6 and v7 guidance, see [Modernize to the v6 and v7 VM series](sizes-v6-v7-modernization-overview).

If your workload runs on a size series in the *End of Life* stage, plan your transition before its retirement date. For affected series and dates, see [End of Life Azure VM size series](end-of-life-sizes-list).

Important

The Dv3, Dsv3, Ev3, and Esv3 series retire on November 15, 2029. After that date, you can't create, resize into, run, or purchase these sizes. The v5 series is the recommended transition target for these workloads. For retirement details, see the [Retired VM sizes modernization guide](retirement/retired-sizes-modernization-guide).

## Modernization effort by starting point

The effort depends less on the source series name than on the workload's use of local temporary storage, image age, networking configuration, disk performance, and deployment model.

| Starting point | What it usually means | Effort |
| --- | --- | --- |
| Earlier D, Ds, E, or Es series | Older processor platform and OS image. The workload might depend on local temporary storage or older network settings. | Moderate. Inventory dependencies, refresh the image and drivers as needed, and validate performance. |
| v2 or v3 | Often a close vCPU and memory mapping, but storage, networking, and local disk behavior can differ. | Low to moderate. |
| v4 | Usually similar guest compatibility and deployment patterns. | Low. Focus on size limits, local disk, availability, and performance validation. |
| New deployments | Deploy directly to a supported image and the selected v5 size. | Lowest. |

## Target VM families

Select a family based on workload profile, processor preference, local temporary disk requirements, and regional availability.

| Workload profile | Intel | AMD | Local temporary disk |
| --- | --- | --- | --- |
| General purpose | [Dv5 and Dsv5](../general-purpose/d-family#dv5-and-dsv5-series), [Ddv5 and Ddsv5](../general-purpose/d-family#ddv5-and-ddsv5-series) | [Dasv5 and Dadsv5](../general-purpose/d-family#dasv5-and-dadsv5-series) | Choose a *d* variant, such as Ddsv5 or Dadsv5, when the workload requires local temporary storage. |
| Memory optimized | [Ev5 and Esv5](../memory-optimized/e-family#ev5-and-esv5-series), [Edv5 and Edsv5](../memory-optimized/e-family#edv5-and-edsv5-series) | [Easv5 and Eadsv5](../memory-optimized/e-family#easv5-and-eadsv5-series) | Choose a *d* variant, such as Edsv5 or Eadsv5, when the workload requires local temporary storage. |

The D-family typically provides about 4 GiB of memory per vCPU. The E-family typically provides about 8 GiB of memory per vCPU. Some families also offer constrained vCPU sizes.

Don't select a target by matching only the vCPU count. To understand the performance gains of v5 over earlier generations, compare:

- Memory and CPU architecture.
- Maximum data disks, IOPS, and throughput.
- Maximum NIC count and network bandwidth.
- Local temporary storage capacity and performance.
- Premium SSD, Premium SSD v2, and Ultra Disk support.
- Measured workload performance against the improved performance baseline of newer VM families.
- Region, availability zone, quota, and current capacity.

For detailed specifications, see [Sizes for virtual machines in Azure](../overview) and [Azure VM sizes naming conventions](../../vm-naming-conventions).

## What changes when the VM family changes

Focus planning on the platform characteristics that can affect workload behavior:

- **Processor performance:** Newer-generation processors provide improved performance. Validate performance against your workload baseline before you select the final size.
- **Boot generation:** The D-family and E-family v5 series support both [Generation 1 and Generation 2 VMs](../../generation-2). A generation change isn't normally required for a resize. When you rebuild or refresh the image, consider Generation 2 and [Trusted Launch](../../trusted-launch).
- **Local temporary storage:** Many base v5 series, including Dv5, Dsv5, Dasv5, Ev5, Esv5, and Easv5, don't include a local temporary disk. Select a *d* variant when the workload requires local scratch space. Never place persistent data on the temporary disk.
- **Storage performance:** Storage performance increased significantly with v5. It's generally less of a concern unless the vCPU count changes substantially between the current and target sizes.
- **Networking:**[Accelerated Networking](/en-us/azure/virtual-network/accelerated-networking-overview) is required on the Intel D-family v5 series (Dv5, Dsv5, Ddv5, and Ddsv5) and supported on the AMD and E-family v5 series. Enable Accelerated Networking on the source VM before you resize to a series that requires it. Use a supported OS image and current drivers, and compare NIC count and expected bandwidth with the source size.
- **Image and operating system:** Confirm that the operating system is supported and current. Refresh older images and guest drivers before a broad transition.
- **Availability and commercial planning:** Confirm regional and zonal availability, quota, and capacity. Review reservations, savings plans, licensing, and any family-specific commercial commitments before the transition.

## Choose a transition method

The transition method depends on whether the existing VM configuration is compatible with the selected v5 size.

| Method | Use when | Main consideration |
| --- | --- | --- |
| Resize the existing VM | The current VM, disk configuration, boot generation, region, and availability configuration support the target size. | Usually requires a restart and might require deallocation. Confirm that the target size is available on the current cluster, or allow the VM to move to another host. For steps, see [Resize a virtual machine](../resize-vm). |
| Rebuild from a current image | The OS image or guest configuration needs modernization, or you want to adopt Generation 2 and Trusted Launch. | Move application configuration and data, and then cut over to the replacement VM. |
| Replace instances in a scale set | The workload uses Virtual Machine Scale Sets or immutable infrastructure. | Update the model or image, and roll out through [controlled upgrade batches](/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-configure-rolling-upgrades). |
| Replicate and cut over | The workload requires a separate transition path, extended testing, reduced cutover risk, or a move to a different region. | Plan replication, identity, networking, DNS, and rollback before cutover. |

## The modernization journey

1. **Assess.** Inventory source sizes, OS and image age, boot generation, disk layout, local temporary storage use, networking, availability configuration, and commercial commitments.
2. **Plan.** Select target families and sizes, choose resize or rebuild, confirm region and quota, define performance baselines, and prepare rollback.
3. **Transition.** Start with representative low-risk workloads, prove the transition pattern, and expand through controlled waves.
4. **Validate and optimize.** Validate boot, application health, disks, networking, performance, monitoring, backup, and workload-owner acceptance. Then right-size and optimize cost.

Workload patterns, wave planning, and rollback practices from the v6 and v7 journey also apply to a v5 transition. For more information, see [Discover modernization pattern by workload type](sizes-v6-v7-modernization-discover).