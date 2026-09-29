---
layout: Conceptual
title: Understand Azure Disk Storage billing - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/disks-understand-billing
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
description: Learn about the billing factors that affect Azure managed disks, including Ultra Disk, Premium SSD v2, Premium SSD, Standard SSD, and Standard HDD.
ms.date: 2026-09-16T00:00:00.0000000Z
ms.topic: concept-article
ai-usage: ai-assisted
locale: en-us
document_id: d1410344-899e-4083-4473-4babb35c5323
document_version_independent_id: d2ad1bf5-0971-ecae-daaf-7bb1da795c25
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/disks-understand-billing.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: toc.json
asset_id: virtual-machines/disks-understand-billing
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/disks-understand-billing.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/92b2ad1c-e9f4-4efc-9995-033db4d8e4a1
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/0811fd70-54cc-4b30-9df4-d821a6be00ca
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/deb7f546-d791-43c4-a74b-a8b1bcca9da4
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/e026b98e-678e-4406-bc80-b3daea608acc
platformId: 920c0061-3f6c-36ca-1b92-e7b08396133e
---

# Understand Azure Disk Storage billing - Azure Virtual Machines | Microsoft Learn

This article helps you understand how Azure managed disks are billed and how billing is laid out in your Azure Disk Storage bill. Some disks have unique attributes that affect their billing, but most disk types have the same set of attributes and are affected differently by these attributes depending on the disk type. You can also take snapshots of your disks, which are reflected in your bill.

For detailed Azure Disk Storage pricing information, see [Azure Disks pricing page](https://azure.microsoft.com/pricing/details/managed-disks/).

## Snapshot billing

There are two kinds of snapshots offered for Azure managed disks: full snapshots and incremental snapshots. Full snapshots can be stored on Standard HDD or Premium SSD storage, while incremental snapshots are only stored on Standard HDD storage. With snapshots, you're billed based on the used size of data. So if you take a full snapshot of a 500-GiB disk but only 50 GiB of that capacity is being used, then your snapshot is billed only for the used size of 50 GiB. Incremental snapshots are more cost efficient than full snapshots, as each snapshot you take only consists of the differences since the last snapshot.

Managed disk snapshots have two redundancy options, locally redundant storage (LRS) and zone-redundant storage (ZRS). For snapshots, the pricing for each redundancy option is the same.

## Ultra Disk

The price of an Ultra Disk is determined by the combination of how large the disk is (its disk size) and what performance you select (IOPS and throughput) for your disk. If you share an Ultra Disk between multiple VMs that can affect its price as well. The following sections focus on these factors as they relate to the price of your Ultra Disk. For more information on how these factors work, see the [Ultra Disk](disks-types#ultra-disks) section of the [Azure managed disk types](disks-types) article.

### Ultra Disk capacity billing

Ultra Disk capacities range from 4 GiB to 64 TiB, in 1-GiB increments. You're billed on a per-GiB basis.

### Ultra Disk IOPS billing

The price of an Ultra Disk increases as you provision more IOPS to your disk. Ultra Disk supports 1,000 IOPS/GiB, up to a maximum of 400,000 IOPS per disk.

### Ultra Disk throughput billing

The price of an Ultra Disk increases as you increase the disk's throughput limit. Ultra Disk supports 0.25 MB/s for each provisioned IOPS, up to a maximum of 10,000 MB/s per disk (where MB/s = 10^6 bytes per second). The minimum guaranteed throughput of an Ultra Disk is 1 MB/s.

### Shared Ultra Disk billing

Ultra Disk supports shared-disk configurations, where you attach one disk to multiple VMs. There isn't an extra charge for each VM that the disk is mounted to. A shared Ultra Disk is billed on the total IOPS and MB/s that the disk is configured for. Normally, an Ultra Disk has two performance throttles that determine its total IOPS/MB/s. However, when configured as a shared Ultra Disk, two more performance throttles are exposed, for a total of four. These two extra throttles allow for increased performance at an extra expense and each meter has a default value, which raises the performance and cost of the disk. For more information, see [Share an Azure managed disk](disks-shared).

### Ultra Disk billing example

In this example, we provisioned an Ultra Disk with LRS redundancy with a total provisioned capacity of 3 TiB, a target performance of 100,000 IOPS and 2,000 MB/s of throughput. We also created and stored incremental snapshots for our used capacity. We're billed for the provisioned capacity of the disk, the extra IOPS and throughput past the baseline values, and the used snapshot capacity that shows as the following tier and meters in our bill:

| Tier | Meter |
| --- | --- |
| Ultra Disks | Ultra LRS provisioned capacity |
| Ultra Disks | Ultra LRS provisioned IOPS |
| Ultra Disks | Ultra LRS provisioned throughput (MB/s) |
| Standard HDD managed disks | ZRS snapshots |

## Premium SSD v2

The price of an Azure Premium SSD v2 is determined by the combination of how large the disk is (its capacity) and what performance you select (IOPS and throughput) for your disk. If you share a Premium SSD v2 between multiple VMs that can affect its price as well. The following sections focus on these factors as they relate to the price of your Premium SSD v2. For more information on how these factors work, see the [Premium SSD v2](disks-types#premium-ssd-v2) section of the [Azure managed disk types](disks-types) article.

### Premium SSD v2 capacity billing

Premium SSD v2 capacities range from 1 GiB to 64 TiB, in 1-GiB increments. You're billed on a per-GiB basis. See the [pricing page](https://azure.microsoft.com/pricing/details/managed-disks/) for details.

### Premium SSD v2 IOPS billing

All Premium SSD v2 disks have a baseline IOPS of 3,000 that is free of charge. After 6 GiB, the maximum IOPS a disk can have increases at a rate of 500 per GiB, up to 80,000 IOPS. So an 8-GiB disk can have up to 4,000 IOPS, and a 10-GiB disk can have up to 5,000 IOPS. To set 80,000 IOPS on a disk, that disk must have at least 160 GiB. Increasing your IOPS beyond 3,000 increases the price of your disk.

### Premium SSD v2 throughput billing

All Premium SSD v2 disks have a baseline throughput of 125 MB/s that is free of charge. After 6 GiB, the maximum throughput that can be provisioned increases by 0.25 MB/s per provisioned IOPS. If a disk has 3,000 IOPS, the max throughput it can set is 750 MB/s. To raise the throughput for this disk beyond 750 MB/s, its IOPS must be increased. For example, if you increased the IOPS to 4,000, then the max throughput that can be set is 1,000 MB/s. 2,000 MB/s is the maximum throughput supported for disks that have 8,000 IOPS or more. Increasing your provisioned throughput beyond 125 MB/s increases the price of your disk.

### Shared Premium SSD v2 billing

Premium SSD v2 managed disks can be used as shared disks, where you attach one disk to multiple VMs. For Premium SSD v2 disks there isn't an extra charge for each VM that the disk is mounted to. Premium SSD v2 disks that are shared are billed on the total IOPS and MB/s that the disk is configured for. Normally, a Premium SSD v2 has two performance throttles that determine its total IOPS/MB/s. However, when configured as a shared Premium SSD v2, two more performance throttles are exposed, for a total of four. These two extra throttles allow for increased performance at an extra expense and each meter has a default value, which raises the performance and cost of the disk. For more information, see [Share an Azure managed disk](disks-shared).

### Premium SSD v2 billing example

In this example, we provision a Premium SSD v2 with LRS redundancy with a total provisioned capacity of 512 GiB, a target performance of 40,000 IOPS and 200 MB/s of throughput. We also create and store incremental snapshots for our current used capacity. We're billed for the provisioned capacity of the disk, the IOPS and throughput past the baseline values, and the used snapshot capacity that show as the following tier and meters in our bill:

| Tier | Meter |
| --- | --- |
| Azure Premium SSD v2 | Premium LRS provisioned capacity |
| Azure Premium SSD v2 | Premium LRS provisioned IOPS |
| Azure Premium SSD v2 | Premium LRS provisioned throughput (MB/s) |
| Standard HDD managed disks | LRS snapshots |

## Premium SSD

The price of an Azure Premium SSD is determined by the performance tier of the disk, whether bursting is enabled, what redundancy options you select, and whether or not you share the disk between multiple VMs. The following sections focus on these factors as they relate to the price of your Premium SSD. For more information about how these factors work, see the [Premium SSD](disks-types#premium-ssds) section of the [Azure managed disk types](disks-types) article.

### Premium SSD performance tier billing

The initial billing of Premium SSD is determined by the performance tier of the disk. Generally, you set the performance tier when you select the capacity you require (if you deploy a 1 TiB Premium SSD, it has the P30 tier by default) but certain disk sizes can select higher performance tiers. When you select a higher performance tier, your disk is billed at that tier until you change its performance tier again. To learn more about performance tiers, see [Performance tiers for managed disks](disks-change-performance).

### Premium SSD bursting billing

Premium SSD offers [two bursting models](disk-bursting#disk-level-bursting), credit-based bursting and [on-demand bursting](disks-enable-bursting). Only on-demand bursting affects billing and you must explicitly enable on-demand bursting. Premium SSD managed disks that use on-demand bursting incur an hourly burst enablement flat fee, and transaction costs apply to any burst transactions that go beyond the provisioned target. Transaction costs use a pay-as-you-go model and are based on uncached disk IOs, including reads and writes that exceed provisioned targets.

### Premium SSD transaction billing

For Premium SSD managed disks, each I/O operation less than or equal to 256 KiB of throughput is considered a single I/O operation. I/O operations larger than 256 KiB of throughput are considered multiple I/Os of size 256 KiB. Unless you enable on-demand bursting, there are no transaction costs for Premium SSD.

### Premium SSD redundancy billing

Premium SSD managed disks can be deployed either with [locally redundant storage (LRS)](disks-redundancy#locally-redundant-storage-for-managed-disks) or [zone-redundant storage (ZRS)](disks-redundancy#zone-redundant-storage-for-managed-disks). The redundancy you select for your disk changes its pricing. For details see the [Azure pricing page](https://azure.microsoft.com/pricing/details/managed-disks/).

### Shared Premium SSD billing

You can use Premium SSD managed disks as shared disks, where you attach one disk to multiple VMs. For a shared Premium SSD, there's a charge that increases with each VM the SSD is mounted to. For more information, see [managed disks pricing](https://azure.microsoft.com/pricing/details/managed-disks/).

### Premium SSD billing example

In this example, we provision a Premium SSD at 512 GiB with LRS redundancy with bursting enabled.

We're billed for the provisioned capacity of the Premium SSD, the burst enablement flat fee, and transaction costs apply to any burst transactions beyond the provisioned target that show as the following tier and meters in our bill:

| Tier | Meter |
| --- | --- |
| Premium SSD managed disks | P20 LRS Disk |
| Premium SSD managed disks | LRS Burst Enablement\* |
| Premium SSD managed disks | LRS Burst Transactions\* |

\*To see a more detailed example of how bursting is billed, see [Disk-level bursting](disk-bursting#disk-level-bursting).

## Standard SSD

The price of an Azure Standard SSD depends on the performance tier of the disk, the number of transactions, the redundancy options you select, and whether you share the disk between multiple VMs. The following sections focus on these factors as they relate to the price of your Standard SSD. For more information about how these factors work, see the [Standard SSD](disks-types#standard-ssds) section of the [Azure managed disk types](disks-types) article.

### Standard SSD performance tier billing

You pay for Standard SSD based on the performance tier. You set the performance tier when you select the capacity you want (if you deploy a 1 TiB Standard SSD, it has the E30 tier), and your disk is billed at that tier. If you increase the capacity of your disk into the next tier, you pay at that tier. For example, if you increase your 1-TiB disk to a 3-TiB disk, you pay at the E50 tier.

### Standard SSD transaction billing

For Standard SSD managed disks, each I/O operation less than or equal to 256 KiB of throughput is considered a single I/O operation. I/O operations larger than 256 KiB of throughput are considered multiple I/Os of size 256 KiB. These transactions incur a billable cost but, there's an hourly limit on the number of transactions that can incur a billable cost. If that hourly limit is reached, extra transactions during that hour no longer incur a cost. For details, see the [blog post](https://aka.ms/billedcapsblog).

### Standard SSD redundancy billing

You can deploy Standard SSD with either [locally redundant storage (LRS)](disks-redundancy#locally-redundant-storage-for-managed-disks) or [zone-redundant storage (ZRS)](disks-redundancy#zone-redundant-storage-for-managed-disks). The redundancy you select for your disk changes its pricing. For details, see the [Azure pricing page](https://azure.microsoft.com/pricing/details/managed-disks/).

### Shared Standard SSD billing

You can use Standard SSD as a shared disk, where you attach one disk to multiple VMs. For a shared Standard SSD, there's a charge that increases with each VM the SSD is mounted to. See [managed disks pricing](https://azure.microsoft.com/pricing/details/managed-disks/) for details.

### Standard SSD billing example

In this example, we provision a 1 TiB Standard SSD with LRS redundancy, where we also have snapshots created on the current used data capacity of 120 GiB. You're billed for the provisioned capacity of the SSD disk, the transactions performed on the disk, and the used snapshot capacity that will show as the following tier and meters in our bill:

| Tier | Meter |
| --- | --- |
| Standard SSD managed disks | E30 LRS Disk |
| Standard SSD managed disks | E4 LRS Disk Operations |
| Standard HDD managed disks | LRS snapshots |

## Standard HDD

The price of an Azure Standard HDD is determined by the performance tier of the disk and the number of transactions. The following sections focus on these factors as they relate to the price of your Standard HDD. For more information about how these factors work, see the [Standard HDD](disks-types#standard-hdds) section of the [Azure managed disk types](disks-types) article.

### Standard HDD performance tier billing

The initial billing of Standard HDD is determined by the performance tier. You set the performance tier when you select the capacity you require. For example, if you deploy a 1 TiB Standard HDD, it has the S30 tier, and your disk is billed at that tier. If you increase the capacity of your disk into the next tier, your disk is billed at that tier. For example, if you increase your 1-TiB disk to a 3-TiB disk, your disk is billed at the S50 tier.

### Standard HDD transaction billing

For Standard HDD managed disks, each I/O operation less than or equal to 16 KiB of throughput is considered a single billable transaction. I/O operations larger than 16 KiB of throughput are considered multiple billable transactions of size 16 KiB for billing purposes. Cost is incurred for every 10,000 billable transactions but, there’s an hourly limit on the number of billable transactions that can incur a billable cost. If your individual disk’s billable transactions reach that hourly limit, any additional billable transactions during that hour don’t incur a cost. For details, see the [blog post](https://aka.ms/hddtossd).

### Standard HDD billing example

In this example, we provision a 512 GiB Standard HDD with LRS redundancy. We're billed for the provisioned capacity of the HDD disk and the transactions performed on the disk, which shows as the following tier and meters in our bill:

| Tier | Meter |
| --- | --- |
| Standard HDD managed disks | S20 LRS Disk |
| Standard HDD managed disks | S4 LRS Disk Operations |

## Empty managed disk billing

When you first create an empty managed disk, Azure initially stores only the disk metadata. The underlying storage isn't allocated until the disk is first used, such as when you attach the disk to a VM or upload a VHD to it. At that point, storage is allocated and the disk begins incurring billing charges.

If an empty disk hasn't been used and no underlying storage has been allocated to it, it doesn't incur disk storage charges.