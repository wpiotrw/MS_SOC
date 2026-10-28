---
layout: Conceptual
title: Ebdsv5 and Ebsv5 series - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/memory-optimized/ebdsv5-ebsv5-series
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
description: Specifications for the Ebdsv5-series and Ebsv5-series Azure virtual machines.
ms.service: azure-virtual-machines
ms.date: 2024-07-08T00:00:00.0000000Z
ms.subservice: sizes
ms.topic: concept-article
ms.custom: references_regions
locale: en-us
document_id: a3950928-1977-9c38-3289-79fd011058f3
document_version_independent_id: b349d902-2b31-b303-6313-020da737a901
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/memory-optimized/ebdsv5-ebsv5-series.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/memory-optimized/ebdsv5-ebsv5-series
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/memory-optimized/ebdsv5-ebsv5-series.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/0811fd70-54cc-4b30-9df4-d821a6be00ca
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/e026b98e-678e-4406-bc80-b3daea608acc
platformId: fc008065-1b50-1c75-3999-5418ecf8e736
---

# Ebdsv5 and Ebsv5 series - Azure Virtual Machines | Microsoft Learn

The memory-optimized Ebsv5 and Ebdsv5 Azure virtual machine (VM) series deliver higher remote storage performance in each VM size than the [Ev4 series](ev4-series). The increased remote storage performance of the Ebsv5 and Ebdsv5 VMs is ideal for storage throughput-intensive workloads. For example, relational databases and data analytics applications.

The Ebsv5 and Ebdsv5 VMs offer up to 260000 IOPS and 8000 MBps of remote disk storage throughput. Both series also include up to 672 GiB of RAM. The Ebdsv5 series has local SSD storage up to 3800 GiB. Both series provide a 3X increase in remote storage performance of data-intensive workloads compared to prior VM generations. You can use these series to consolidate existing workloads on fewer VMs or smaller VM sizes while achieving potential cost savings. The Ebdsv5 series comes with a local disk and Ebsv5 is without a local disk. We recommend choosing Premium SSD, Premium SSD v2 or Ultra Disks to attain the published disk performance.

The Ebdsv5 and Ebsv5 series run on the Intel® Xeon® Platinum 8370C (Ice Lake) processors in a hyper-threaded configuration. The series are ideal for various memory-intensive enterprise applications. They feature:

- Up to 512 GiB of RAM
- [Intel® Turbo Boost Technology 2.0](https://www.intel.com/content/www/us/en/architecture-and-technology/turbo-boost/turbo-boost-technology.html)
- [Intel® Hyper-Threading Technology](https://www.intel.com/content/www/us/en/gaming/resources/hyper-threading.html)
- [Intel® Advanced Vector Extensions 512 (Intel® AVX-512)](https://www.intel.com/content/www/us/en/architecture-and-technology/avx-512-overview.html)
- Support for [Intel® Deep Learning Boost](https://software.intel.com/content/www/us/en/develop/topics/ai/deep-learning-boost.html)
- NVMe interface for higher remote disk storage IOPS and throughput performance

Important

- Accelerated networking is required and turned on by default on all Ebsv5 and Ebdsv5 VMs.
- Ebsv5 and Ebdsv5-series VMs can [burst their disk performance](../../disk-bursting) and get up to their bursting max for up to 30 minutes at a time.
- The E112i size is offered as NVMe only to provide the highest IOPS and throughput performance. See the NVMe VM spec table to see the improved performance details.

## Ebdsv5 series

Ebdsv5-series sizes run on the Intel® Xeon® Platinum 8370C (Ice Lake) processors. The Ebdsv5 VM sizes feature up to 672 GiB of RAM, in addition to fast and large local SSD storage (up to 3800 GiB). These VMs are ideal for memory-intensive enterprise applications and applications that benefit from high remote storage performance, low latency, high-speed local storage. Remote Data disk storage is billed separately from VMs.

- [Premium Storage](../../premium-storage-performance): Supported
- [Premium Storage caching](../../premium-storage-performance): Supported
- [Live Migration](../../maintenance-and-updates): Supported
- [Memory Preserving Updates](../../maintenance-and-updates): Supported
- [VM Generation Support](../../generation-2): Generation 1 and Generation 2
- [Accelerated Networking](/en-us/azure/virtual-network/create-vm-accelerated-networking-cli): Required
- [Ephemeral OS Disks](../../ephemeral-os-disks): Supported
- Nested virtualization: Supported
- NVMe Interface: Supported only on Generation 2 VMs
- SCSI Interface: Supported on Generation 1 and 2 VMs

## Ebdsv5 Series (NVMe)

| Size | vCPU | Memory: GiB | Temp storage (SSD) GiB | Max data disks | Max temp storage throughput: IOPS / MBps | Max uncached Premium SSD throughput: IOPS/MBps | Max burst uncached Premium SSD throughput: IOPS/MBps | Max uncached Ultra Disk and Premium SSD v2 throughput: IOPS/MBps | Max burst uncached Ultra Disk and Premium SSD v2 throughput: IOPS/MBps | Max NICs | Network bandwidth |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Standard\_E2bds\_v5 | 2 | 16 | 75 | 4 | 9000/125 | 8000/230 | 10000/1200 | 12000/300 | 15000/1200 | 2 | 12500 |
| Standard\_E4bds\_v5 | 4 | 32 | 150 | 8 | 19000/250 | 16000/460 | 20000/1200 | 21400/600 | 30000/1200 | 2 | 12500 |
| Standard\_E8bds\_v5 | 8 | 64 | 300 | 16 | 38000/500 | 33000/930 | 40000/1200 | 44200/1200 | 60000/1200 | 4 | 12500 |
| Standard\_E16bds\_v5 | 16 | 128 | 600 | 32 | 75000/1000 | 66000/1800 | 70000/2000 | 88400/2300 | 96000/2600 | 8 | 12500 |
| Standard\_E32bds\_v5 | 32 | 256 | 1200 | 32 | 150000/2000 | 130000/3700 | 140000/4000 | 174200/4800 | 180000/5200 | 8 | 16000 |
| Standard\_E48bds\_v5 | 48 | 384 | 1800 | 32 | 225000/3000 | 190000/5600 | 200000/6000 | 253300/7300 | 260000/7850 | 8 | 16000 |
| Standard\_E64bds\_v5 | 64 | 512 | 2400 | 32 | 300000/4000 | 220000/6000 | 230000/6500 | 294800/7800 | 310000/8500 | 8 | 20000 |
| Standard\_E96bds\_v5 | 96 | 672 | 3600 | 32 | 450000/4000 | 260000/7500 | 260000/8000 | 390000/8500 | 390000/9000 | 8 | 25000 |
| Standard\_E112ibds\_v5 | 112 | 672 | 3800 | 64 | 450000/4000 | 260000/8000 | 260000/8000 | 400000/10000 | 400000/10000 | 8 | 40000 |

## Ebdsv5 Series (SCSI)

| Size | vCPU | Memory: GiB | Temp storage (SSD) GiB | Max data disks | Max temp storage throughput: IOPS / MBps | Max uncached Premium SSD throughput: IOPS/MBps | Max burst uncached Premium SSD throughput: IOPS/MBps | Max uncached Ultra Disk and Premium SSD v2 throughput: IOPS/MBps | Max burst uncached Ultra Disk and Premium SSD v2 throughput: IOPS/MBps | Max NICs | Network bandwidth |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Standard\_E2bds\_v5 | 2 | 16 | 75 | 4 | 9000/125 | 6000/170 | 10000/1200 | 8000/170 | 15000/1200 | 2 | 12500 |
| Standard\_E4bds\_v5 | 4 | 32 | 150 | 8 | 19000/250 | 12100/350 | 20000/1200 | 16200/350 | 30000/1200 | 2 | 12500 |
| Standard\_E8bds\_v5 | 8 | 64 | 300 | 16 | 38000/500 | 24200/680 | 40000/1200 | 32400/680 | 60000/1200 | 4 | 12500 |
| Standard\_E16bds\_v5 | 16 | 128 | 600 | 32 | 75000/1000 | 48400/1370 | 64000/2000 | 64800/1370 | 96000/2000 | 8 | 12500 |
| Standard\_E32bds\_v5 | 32 | 256 | 1200 | 32 | 150000/2000 | 96800/2740 | 120000/4000 | 129700/2740 | 160000/4000 | 8 | 16000 |
| Standard\_E48bds\_v5 | 48 | 384 | 1800 | 32 | 225000/3000 | 120000/4000 | 120000/4000 | 160000/4000 | 160000/4000 | 8 | 16000 |
| Standard\_E64bds\_v5 | 64 | 512 | 2400 | 32 | 300000/4000 | 120000/4000 | 120000/4000 | 160800/6500 | 160800/6500 | 8 | 20000 |
| Standard\_E96bds\_v5 | 96 | 672 | 3600 | 32 | 450000/4000 | 120000/4000 | 120000/4000 | 180000/6500 | 180000/6500 | 8 | 25000 |

## Ebsv5 series

Ebsv5-series sizes run on the Intel® Xeon® Platinum 8272CL (Cascade Lake). These VMs are ideal for memory-intensive enterprise applications and applications that benefit from high remote storage performance but with no local SSD storage. Ebsv5-series VMs feature Intel® Hyper-Threading Technology. Remote Data disk storage is billed separately from VMs.

- [Premium Storage](../../premium-storage-performance): Supported
- [Premium Storage caching](../../premium-storage-performance): Supported
- [Live Migration](../../maintenance-and-updates): Supported
- [Memory Preserving Updates](../../maintenance-and-updates): Supported
- [VM Generation Support](../../generation-2): Generation 1 and Generation 2
- [Accelerated Networking](/en-us/azure/virtual-network/create-vm-accelerated-networking-cli): Required
- [Ephemeral OS Disks](../../ephemeral-os-disks): Not supported
- Nested virtualization: Supported
- NVMe Interface: Supported only on Generation 2 VMs
- SCSI Interface: Supported on Generation 1 and Generation 2 VMs

## Ebsv5 Series (NVMe)

| Size | vCPU | Memory: GiB | Max data disks | Max uncached Premium SSD throughput: IOPS/MBps | Max burst uncached Premium SSD throughput: IOPS/MBps | Max uncached Ultra Disk and Premium SSD v2 throughput: IOPS/MBps | Max burst uncached Ultra Disk and Premium SSD v2 throughput: IOPS/MBps | Max NICs | Network bandwidth |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Standard\_E2bs\_v5 | 2 | 16 | 4 | 8000/230 | 10000/1200 | 12000/300 | 15000/1200 | 2 | 12500 |
| Standard\_E4bs\_v5 | 4 | 32 | 8 | 16000/460 | 20000/1200 | 21400/600 | 30000/1200 | 2 | 12500 |
| Standard\_E8bs\_v5 | 8 | 64 | 16 | 33000/930 | 40000/1200 | 44200/1200 | 60000/1200 | 4 | 12500 |
| Standard\_E16bs\_v5 | 16 | 128 | 32 | 66000/1800 | 70000/2000 | 88400/2300 | 96000/2600 | 8 | 12500 |
| Standard\_E32bs\_v5 | 32 | 256 | 32 | 130000/3700 | 140000/4000 | 174200/4800 | 180000/5200 | 8 | 16000 |
| Standard\_E48bs\_v5 | 48 | 384 | 32 | 190000/5600 | 200000/6000 | 253300/7300 | 260000/7850 | 8 | 16000 |
| Standard\_E64bs\_v5 | 64 | 512 | 32 | 220000/6000 | 230000/6500 | 294800/7800 | 310000/8500 | 8 | 20000 |
| Standard\_E96bs\_v5 | 96 | 672 | 32 | 260000/7500 | 260000/8000 | 390000/8500 | 390000/9000 | 8 | 25000 |
| Standard\_E112ibs\_v5 | 112 | 672 | 64 | 260000/8000 | 260000/8000 | 400000/10000 | 400000/10000 | 8 | 40000 |

## Ebsv5 Series (SCSI)

| Size | vCPU | Memory: GiB | Max data disks | Max uncached Premium SSD throughput: IOPS/MBps | Max burst uncached Premium SSD throughput: IOPS/MBps | Max uncached Ultra Disk and Premium SSD v2 throughput: IOPS/MBps | Max burst uncached Ultra Disk and Premium SSD v2 throughput: IOPS/MBps | Max NICs | Network bandwidth |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Standard\_E2bs\_v5 | 2 | 16 | 4 | 6000/170 | 10000/1200 | 8000/170 | 15000/1200 | 2 | 12500 |
| Standard\_E4bs\_v5 | 4 | 32 | 8 | 12100/350 | 20000/1200 | 16200/350 | 30000/1200 | 2 | 12500 |
| Standard\_E8bs\_v5 | 8 | 64 | 16 | 24200/680 | 40000/1200 | 32400/680 | 60000/1200 | 4 | 12500 |
| Standard\_E16bs\_v5 | 16 | 128 | 32 | 48400/1370 | 64000/2000 | 64800/1370 | 96000/2000 | 8 | 12500 |
| Standard\_E32bs\_v5 | 32 | 256 | 32 | 96800/2740 | 120000/4000 | 129700/2740 | 160000/4000 | 8 | 16000 |
| Standard\_E48bs\_v5 | 48 | 384 | 32 | 120000/4000 | 120000/4000 | 160000/4000 | 160000/4000 | 8 | 16000 |
| Standard\_E64bs\_v5 | 64 | 512 | 32 | 120000/4000 | 120000/4000 | 160800/6500 | 160800/6500 | 8 | 20000 |
| Standard\_E96bs\_v5 | 96 | 672 | 32 | 120000/4000 | 120000/4000 | 180000/6500 | 180000/6500 | 8 | 25000 |

## Size table definitions

- Storage capacity is shown in units of GiB or 1024^3 bytes. When you compare disks measured in GB (1000^3 bytes) to disks measured in GiB (1024^3) remember that capacity numbers given in GiB may appear smaller. For example, 1023 GiB = 1098.4 GB.
- Disk throughput is measured in input/output operations per second (IOPS) and MBps where MBps = 10^6 bytes/sec.
- Data disks can operate in cached or uncached modes. For cached data disk operation, the host cache mode is set to **ReadOnly** or **ReadWrite**. For uncached data disk operation, the host cache mode is set to **None**.
- To learn how to get the best storage performance for your VMs, see [Virtual machine and disk performance](../../disks-performance).
- **Expected network bandwidth** is the maximum aggregated bandwidth allocated per VM type across all NICs, for all destinations. For more information, see [Virtual machine network bandwidth](/en-us/azure/virtual-network/virtual-machine-network-throughput).

    Upper limits aren't guaranteed. Limits offer guidance for selecting the right VM type for the intended application. Actual network performance will depend on several factors including network congestion, application loads, and network settings. For information on optimizing network throughput, see [Optimize network throughput for Azure virtual machines](/en-us/azure/virtual-network/virtual-network-optimize-network-bandwidth). To achieve the expected network performance on Linux or Windows, you may need to select a specific version or optimize your VM. For more information, see [Bandwidth/Throughput testing (NTTTCP)](/en-us/azure/virtual-network/virtual-network-bandwidth-testing).

## Ebsv5 NVMe FAQ

### How is the NVMe enabled Ebsv5 different from the L series VM that Azure offers?

The NVMe enabled Ebsv5 series is designed to offer the highest Azure managed disk storage performance. The L series VMs are designed to offer higher IOPS and throughout on the local NVMe disks, which are ephemeral. Refer to the [VM sizes documentation](/en-us/azure/virtual-machines/sizes) for details on the performance offered by the Ebsv5 and L series.

### What I/O size is recommended to achieve the published performance?

To achieve the maximum IOPS, we recommend using a 4 KiB or 8 KiB block size. For maximum performance throughput, you can choose to use one of the following block sizes: 64 KiB, 128 KiB, 256 KiB, 512 KiB or 1024 KiB. However, it's important to optimize the I/O size based on the specific requirements of your application and to use the recommended block sizes only as a guideline.

### What workloads benefit with NVMe on Ebsv5 family?

The Ebsv5 VM families are suitable for various workloads that require high I/O and improved remote storage performance. Some examples of such workloads include:

- Online transaction processing (OLTP) workloads: These workloads involve frequent, small, and fast database transactions, such as online banking, e-commerce, and point-of-sale systems.
- Online analytical processing (OLAP) workloads: These workloads involve complex queries and large-scale data processing, such as data mining, business intelligence, and decision support systems.
- Data warehousing workloads: These workloads involve collecting, storing, and analyzing large volumes of data from multiple sources, such as customer data, sales data, and financial data.
- Replication and disaster recovery workloads: These workloads involve replicating data between multiple databases or sites for backup and disaster recovery purposes.
- Database development and testing workloads: These workloads involve creating, modifying, and testing database schemas, queries, and applications.

### What platforms and generations support NVMe VMs?

NVMe VMs are only accessible on the platform with the 3rd Generation Intel® Xeon® Platinum 8370C (Ice Lake) processor. However, support for more platforms and generations is coming soon. Stay informed by following our product launch announcements in Azure updates.

### The Azure region I need doesn't support NVMe, when will NVMe be available?

Watch out for our product launch announcements in the Azure updates.

### What sizes in the Ebsv5 and Ebdsv5 family support NVMe?

The sizes E2-E112i support NVMe on Ebsv5 and Ebdsv5 families.

### What sizes in the Ebsv5 and Ebdsv5 family support SCSI?

All sizes (E2-E96) on the Ebsv5 and Ebsdv5 families support SCSI except E112i.

### I have a SCSI Ebsv5 VM. How do I switch to NVMe of the same VM size?

The steps to switch from SCSI to NVMe are the same as explained [here](../../enable-nvme-remote-faqs).

### How can I switch back to SCSI interface from NVMe VM?

To switch back to SCSI from NVMe, follow the same steps as explained [here](../../enable-nvme-remote-faqs).

### What is the price for NVMe Ebsv5 prices?

The NVMe enabled Ebsv5 and Ebdsv5 VMs are the same price as SCSI VMs. Refer to the pricing pages for [Windows](https://azure.microsoft.com/pricing/details/virtual-machines/windows/) and [Linux](https://azure.microsoft.com/pricing/details/virtual-machines/linux/). With NVMe, you get higher performance at no extra cost.

### How can I try before purchasing this VM series? Is preview still available?

The preview period for this offer is over, and it is now generally available for purchase. You can request a quota for one of the available Azure regions to try out the new NVMe Ebsv5 or Ebdsv5 sizes.

### Reporting Issues

#### My VMs don't reach the published performance limits. Where do I report this issue?

If you see performance issues, you can submit a [support ticket](https://azure.microsoft.com/support/create-ticket). Provide all relevant information on the ticket, such as the subscription, VM size used, region, logs, and screenshot.

![Screenshot of example of guest output for data disks.](../../media/enable-nvme/nvme-faq-10.png)

#### How can I get more help if I run into issues while setting up the VMs with the NVMe interface?

If you run into issues while creating or resizing Ebsv5 or Ebdsv5 to NVMe, and need assistance, you can submit a [support ticket](https://azure.microsoft.com/support/create-ticket).

![Screenshot of example for reporting issues for feature by submitting support ticket.](../../media/enable-nvme/nvme-faq-11.png)

![Screenshot of support ticket selection details.](../../media/enable-nvme/nvme-faq-12.png)

## Other sizes and information

- [General purpose](../overview#general-purpose)
- [Memory optimized](../overview#memory-optimized)
- [Storage optimized](../overview#storage-optimized)
- [GPU optimized](../overview#gpu-accelerated)
- [High performance compute](../overview#high-performance-compute)
- [End of Life sizes](../lifecycle/end-of-life-sizes-list)