---
layout: Conceptual
title: Redundancy options for Azure managed disks - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/disks-redundancy
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
author: roygara
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: rogarana
ms.update-cycle: 365-days
ms.service: azure-disk-storage
description: Learn about zone-redundant storage and locally redundant storage for Azure managed disks.
ms.date: 2026-10-20T00:00:00.0000000Z
ai-usage: ai-assisted
ms.topic: how-to
ms.custom: references_regions
locale: en-us
document_id: 2ca709b7-462b-66c0-ed1b-c757e786061f
document_version_independent_id: 972b31ed-cb41-ad74-27ce-4e1fe2656c1b
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/disks-redundancy.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/disks-redundancy
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/disks-redundancy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/92b2ad1c-e9f4-4efc-9995-033db4d8e4a1
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/deb7f546-d791-43c4-a74b-a8b1bcca9da4
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 6697d51e-8566-e0b4-ac62-dac63b407cd9
---

# Redundancy options for Azure managed disks - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows VMs ✔️ Flexible scale sets ✔️ Uniform scale sets

Azure managed disks offer two storage redundancy options, zone-redundant storage (ZRS), and locally redundant storage. ZRS provides higher availability for managed disks than locally redundant storage (LRS) does. However, the write latency for LRS disks is better than ZRS disks because LRS disks synchronously write data to three copies in a single data center.

## Locally redundant storage for managed disks

Locally redundant storage (LRS) replicates your data three times within a single data center in the selected region. LRS protects your data against server rack and drive failures. LRS disks provide at least 99.999999999% (11 9's) of durability over a given year. To protect an LRS disk from a zonal failure like a natural disaster or other issues, take the following steps:

- Use applications that can synchronously write data to two zones, and automatically failover to another zone during a disaster.
    - An example would be SQL Server Always On.
- Take frequent backups of LRS disks with ZRS snapshots.
- Enable cross-zone disaster recovery for LRS disks via [Azure Site Recovery](/en-us/azure/site-recovery/azure-to-azure-how-to-enable-zone-to-zone-disaster-recovery). However, cross-zone disaster recovery doesn't provide zero Recovery Point Objective (RPO).

If your workflow doesn't support application-level synchronous writes across zones, or your application must meet zero RPO, then ZRS disks are appropriate.

## Zone-redundant storage for managed disks

Zone-redundant storage (ZRS) synchronously replicates your Azure managed disk across three Azure availability zones in the region you select. Each availability zone is a separate physical location with independent power, cooling, and networking. ZRS disks provide at least 99.9999999999% (12 9's) of durability over a given year.

A ZRS disk lets you recover from failures in availability zones. If a zone goes down and your virtual machine (VM) isn't affected, then your workloads continue running. But if your VM is affected by an outage and you want to recover before it's resolved, you can [force detach](/en-us/rest/api/compute/virtual-machines/attach-detach-data-disks?tabs=HTTP#diskdetachoptiontypes) your ZRS data disks from the failed VM, freeing them to attach to another VM. Force detach doesn't support OS disks.

[Zone resilience for Azure VMs (Preview)](zone-resilience) lets you initiate failover of an eligible standalone zonal VM to another availability zone in the same region. The VM retains its resource identity and supported configuration.

As a prerequisite, the OS disk and every attached data disk must use supported ZRS managed disks, and you must enable zone resilience before an outage. For more details, refer to the [zone resilience documentation](zone-resilience#requirements).

Important

Zone resilience for Azure VMs is in preview. Use this preview only for evaluation and testing with nonproduction VMs. Don't use it for production VMs. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

See the [preview requirements and limitations](zone-resilience#requirements).

ZRS disks can also be shared between VMs for improved availability with clustered or distributed applications like SQL FCI, SAP ASCS/SCS, or GFS2. A shared ZRS disk can be attached to primary and secondary VMs in different zones to take advantage of both ZRS and [availability zones](/en-us/azure/reliability/availability-zones-overview). If your primary zone fails, you can quickly fail over to the secondary VM by using [SCSI persistent reservation](disks-shared-enable#supported-scsi-persistent-reservation-commands).

For more information on ZRS disks, see [Zone-redundant storage option for Azure managed disks for high availability](https://youtu.be/RSHmhmdHXcY).

### ZRS limitations

ZRS for managed disks is only supported with Premium SSD and Standard SSD managed disks. ZRS for managed disks isn't supported with Premium SSD v2 managed disks or Ultra Disks. Force detach only supports data disks.

### ZRS regional availability

ZRS disks are available in all regions that have availability zone support. For a list of these regions, see [Azure regions list](/en-us/azure/reliability/regions-list#azure-regions-list-1).

### ZRS billing implications

For details see the [Azure pricing page](https://azure.microsoft.com/pricing/details/managed-disks/).

### Compare ZRS and LRS disks

Except for more write latency, disks using ZRS are identical to disks using LRS, they have the same scale targets. [Benchmark your disks](disks-benchmarks) to simulate the workload of your application and compare the latency between LRS and ZRS disks.