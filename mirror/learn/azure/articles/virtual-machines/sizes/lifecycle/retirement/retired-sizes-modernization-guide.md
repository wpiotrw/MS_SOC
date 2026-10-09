---
layout: Conceptual
title: Retired VM sizes modernization guide - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/lifecycle/retirement/retired-sizes-modernization-guide
breadcrumb_path: ../../../../breadcrumb/azure-compute/toc.json
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
ms.reviewer: mattmcinnes
ms.author: mattmcinnes
ms.update-cycle: 1095-days
description: Modernization guide for retired VM size series
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.topic: concept-article
ms.date: 2026-09-25T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: 819bac3e-b4c0-c93a-3894-44666b79a89f
document_version_independent_id: 81d5179f-86ad-377c-43a8-dbafedddf851
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/lifecycle/retirement/retired-sizes-modernization-guide.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../../toc.json
asset_id: virtual-machines/sizes/lifecycle/retirement/retired-sizes-modernization-guide
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/lifecycle/retirement/retired-sizes-modernization-guide.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/a3955c7b-f5ee-420d-aff5-d7119738f38b
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31948f4-2f38-404b-ac93-c3c8c5b3ae33
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: ee372b9e-efdc-a6c5-0399-d7a95a5f707a
---

# Retired VM sizes modernization guide - Azure Virtual Machines | Microsoft Learn

This modernization guide is designed for users of Azure virtual machines (VMs) scheduled for retirement. This guide helps you transition to Current or Extended VM series, helping you minimize disruptions while optimizing cost and performance. The guide covers General Purpose, Storage Optimized, and other VM series. It also surfaces critical information for HPC HBv2-series VMs undergoing retirement; specialized workload validation is recommended when modernizing HPC workloads.

This guide covers:

- Recommended replacement VM series
- Detailed modernization steps
- Common questions and guidance on handling RIs.

By modernizing to newer VM series, you gain access to improved price-performance ratios, broader regional availability, and the latest hardware capabilities.

## Recommended Replacement VM Series

| Current VM Series | Target VM Series | Differences in Specification in Target VM\* |
| --- | --- | --- |
| DDsDv2Dsv2 | Dsv5/Ddsv5/Dasv5/Dadsv5Dasv6/Dadsv6/Dsv6/Ddsv6Dasv7/Dadsv7Esv6/Edsv6/Easv6/Eadsv6Easv7/Eadsv7 | D/Ev5 disk controller type: SCSI  D/Ev6, D/Ev7 disk controller type: NVMeLocal Storage Throughput: 9000 IOPS / 125 MBpsRemote Storage Throughput: 3750 IOPS / 82 MBps |
| Dv3Dsv3 | Dv5/Dsv5/Ddv5/Ddsv5/Dasv5/Dadsv5v6 and v7 D-family series | For the smoothest transition, see [Modernize to the v5 VM series](../sizes-v5-modernization-overview). For the latest features and performance, see [Modernize to the v6 and v7 VM series](../sizes-v6-v7-modernization-overview). |
| Ev3Esv3 | Ev5/Esv5/Edv5/Edsv5/Easv5/Eadsv5v6 and v7 E-family series | For the smoothest transition, see [Modernize to the v5 VM series](../sizes-v5-modernization-overview). For the latest features and performance, see [Modernize to the v6 and v7 VM series](../sizes-v6-v7-modernization-overview). |
| Ls | Lsv3/Lasv3Lsv4/Lasv4 | Local Storage: Supported - NVMeRemote Storage Throughput: 12800 IOPS / 200 MBps Disk Controller Type: SCSI and NVMe |
| Av2Amv2 | Bsv2/Basv2Dsv5/Ddv5/Dasv5Esv5/Edv5/Easv5Dsv6/Ddsv6/Dasv6Esv6/Edsv6/Easv6 | B/Bav2, D/Ev5 disk controller type: SCSI  D/Ev6 disk controller type: NVMeRemote Storage Throughput: 3750 IOPS / 85 MBps |
| Bv1 | Bsv2/Basv2Dlsv5/Dldsv5/Dalsv5/Daldsv5Dlsv6/Dldsv6/Dalsv6/Daldsv6 | B/Bav2, D/Ev5 disk controller type: SCSI  D/Ev6 disk controller type: NVMeRemote Storage Throughput: 3750 IOPS / 85 MBpsDisk Controller Type: SCSI |
| FFsFsv2 | Dlsv6/Dldsv6/Dalsv6/Daldsv6Falsv6Dldsv5/Dlsv5/Dsv5/Ddsv5 | D/Ev5 disk controller type: SCSI  D/Ev6 disk controller type: NVMe  Remote Storage Throughput: 4167 IOPS / 124 MBps |
| GGs | Lsv3/Lasv3Lsv4/Lasv4 | Lv3/Lv4 controller type: SCSI and NVMe Remote Storage Throughput: 12800 IOPS / 200 MBps |
| Lsv2 | Lsv3/Lasv3Lasv4/Lasv4 | Local Storage: NVMeRemote Storage Throughput: 12800 IOPS / 200 MBpsDisk Controller Type: SCSI and NVMe |
| HBv2 | HBv5HXHBv4HBv3 | Transition to newer AMD EPYC generations (Milan/Genoa/Zen4) and newer InfiniBand fabrics (HDR on HBv3 → NDR on HBv4/HBv5). Validate MPI workload performance, memory bandwidth requirements, and RDMA compatibility on the target series. |
| NP-series(Standard\_NP10sStandard\_NP20sStandard\_NP40s) | [NDv2](../../gpu-accelerated/ndv2-series)[NCads_H100_v5](../../gpu-accelerated/ncadsh100v5-series)[NCasT4_v3](../../gpu-accelerated/ncast4v3-series) | GPU type: NVIDIA V100 (NDv2), H100 (NCads\_H100\_v5), or T4 (NCasT4\_v3) vs. AMD Xilinx Alveo U250 FPGANVLink interconnect: Available on NDv2; not applicable on FPGA-based NP-seriesDisk controller: NVMe/SCSI (GPU families) vs. SCSI (NP-series)Note: Workloads must be ported from FPGA-based acceleration (XRT/Vitis) to CUDA/GPU-based frameworks. |

\*Refers to the smallest VM size in the given target VM series. Full VM specifications are available on each target VM series' product sizes page.

\*Refers to the smallest VM size in the given target VM series. Full VM specifications are available on each target VM series' product sizes page.

Important

The following SKUs aren't available in the Sovereign clouds: Bsv2, Bpsv2, Basv2

## Recommended Replacement Isolated VM Sizes

| Current VM Size | Target VM Sizes | Differences in Specification in Target VM\* |
| --- | --- | --- |
| Standard\_E64i\_v3Standard\_E64is\_v3 | Standard\_E192is\_v6Standard\_E192ids\_v6Standard\_E104i\_v5Standard\_E104id\_v5Standard\_E104is\_v5Standard\_E104ids\_v5Standard\_E80is\_v4Standard\_E80ids\_v4 | Local Storage: Supported - NVMeLocal Storage Throughput: 37,500 IOPS / 180 MBpsRemote Storage Throughput: 3,750 IOPS / 106 MBps Disk Controller Type: NVMe |

\*Refers to the smallest VM size in the given target VM series. Full VM specifications are available on each target VM series' product sizes page.

For optimal performance and experience, we recommend using the Current v6 or Extended v5 general purpose and memory optimized VM series. This ensures you have access to the latest features such as Premium Storage, Accelerated Networking, and Nested Virtualization. While the v6 VM series is preferred, there are certain scenarios where you might want to consider the v5 or even the v4 VM series. Here are some reasons why:

- v6 VMs require [enabling NVMe](/en-us/azure/virtual-machines/nvme-overview) which means that you must have a [supported OS](/en-us/azure/virtual-machines/enable-nvme-interface).
- v6 VMs support [Generation 2 VMs only](/en-us/azure/virtual-machines/generation-2).
- v6 VMs require MANA ([Microsoft Azure Network Adapter](/en-us/azure/virtual-network/accelerated-networking-mana-overview)) and a MANA supported operating system.
- v6 VMs may not have available capacity in the regions and zones you need.

Note that Lasv5 and Laosv5 series are the Current L-series VMs.

Use the [Azure VM size documentation](/en-us/azure/virtual-machines/sizes) to help identify suitable VM sizes.

## Modernization steps

#### Optional: For Reserved Instance (RI) customers only

- Review your current reservations using the [Azure Reservation Management](/en-us/azure/cost-management-billing/reservations/manage-reserved-vm-instance) page.
- If applicable, exchange existing reservations for newer VM series or trade in your reservations for an **Azure Savings Plan for compute**.
- **HBv2 customers**: 1-year and 3-year HBv2 Reserved Instance purchases ended on April 2, 2026. If you have active HBv2 RIs, consider exchanging them for supported HPC series RIs (such as HBv3, HBv4, HBv5, or HX) or trading them in for an Azure Savings Plan for compute before the retirement date of May 31, 2027.
- **NP-series customers**: 1-year and 3-year NP-series Reserved Instance purchases ended on April 2, 2026. If you have active NP-series RIs, consider exchanging them for supported GPU series RIs or trading them in for an Azure Savings Plan for compute before the retirement date of May 31, 2027.
- For customers using Reserved Instances (RIs) on VM series such as One-year and three-year RIs for the VM series Dv3, Dsv3, Ev3, and Esv3. One-year RIs for the VM series Av2, Amv2, Bv1, D, Ds, Dv2, Dsv2, F, Fs, Fsv2, G, Gs, Ls, and Lsv2. Existing RIs will remain valid through the end of their original term. However, once an RI expires after July 1, 2026, it cannot be purchased or renewed for these VM series. At that point, workloads will transition to pay as you go pricing unless another cost optimization option is selected. Customers are encouraged to either transition to Azure Savings Plan for compute or modernize workloads to newer VM generations, which continue to support both Reserved Instances and Savings Plans. Customers should plan their modernization ahead of RI expiration to avoid unintended cost increases.

#### Identify the Target VM Size

- Evaluate your current VM's workload and performance requirements.
- Select a comparable size from the above table that meets your CPU, memory, and storage needs.

#### GPU workload modernization (NP-series customers)

NP-series customers should validate their workload GPU requirements (CUDA cores, memory bandwidth, and interconnect needs) before selecting a target VM family. Consider the following recommended alternatives and their key characteristics:

- **[NDv2 VMs](../../gpu-accelerated/ndv2-series)** – Best for training and large-scale AI/HPC workloads. Features NVIDIA V100 GPUs with NVLink for GPU-to-GPU communication and high memory bandwidth.
- **[NCads_H100_v5 VMs](../../gpu-accelerated/ncadsh100v5-series)** – Best for modern AI training and batch inference requiring the latest GPU generation. Features NVIDIA H100 GPUs.
- **[NCasT4_v3 VMs](../../gpu-accelerated/ncast4v3-series)** – Best for inference, interactive graphics, and cost-sensitive workloads. Features NVIDIA T4 GPUs.

Important

NP-series VMs use FPGA-based acceleration (Xilinx/AMD Alveo U250). Modernizing to GPU-based VM families requires porting your workloads from FPGA frameworks (such as Vitis/XRT) to GPU-based frameworks (such as CUDA). Perform thorough test validation before resizing production workloads.

#### Check and Request Quota Increases

- Before resizing, verify that your subscription has sufficient quota for the target v6 VM series.
- Request more quota through the [Azure portal](/en-us/azure/azure-portal/supportability/per-vm-quota-requests) if needed.

#### Resize the Virtual Machine

You can resize your VM through the Azure portal, Azure CLI, or PowerShell. Follow these steps:

1. **Stop (deallocate) the VM**.
2. **Resize** the VM to your selected v6 series.
3. **Start the VM** after resizing.

Refer to the full [Azure VM resizing guide](/en-us/azure/virtual-machines/sizes/resize-vm?tabs=portal) for more detailed instructions.

## FAQ

#### Q: Which sizes are being retired?

To review retired sizes, see [retired and retiring VM size series](../retirements-and-capacity-restrictions#retired-and-retiring-vm-size-series). View retired isolated sizes at [Isolation for VMs in Azure](/en-us/azure/virtual-machines/isolation).

Note

HPC HBv2-series VMs are also retiring. See the HBv2 row in the table below for the applicable dates.

| VM Series | 3 YR RI expiration date | 1 YR RI expiration date | Retirement Date |
| --- | --- | --- | --- |
| Av2 | 11/15/2025 | 07/01/2026 | 11/15/2028 |
| Amv2 | 11/15/2025 | 07/01/2026 | 11/15/2028 |
| Bv1 | 11/15/2025 | 07/01/2026 | 11/15/2028 |
| D | 05/01/2025 | 07/01/2026 | 05/01/2028 |
| Ds | 05/01/2025 | 07/01/2026 | 05/01/2028 |
| Dsv2 | 05/01/2025 | 07/01/2026 | 05/01/2028 |
| Dsv3 | 07/01/2026 | 07/01/2026 | 11/15/2029 |
| Dv2 | 05/01/2025 | 07/01/2026 | 05/01/2028 |
| Dv3 | 07/01/2026 | 07/01/2026 | 11/15/2029 |
| Esv3 | 07/01/2026 | 07/01/2026 | 11/15/2029 |
| Ev3 | 07/01/2026 | 07/01/2026 | 11/15/2029 |
| F | 11/15/2025 | 07/01/2026 | 11/15/2028 |
| Fs | 11/15/2025 | 07/01/2026 | 11/15/2028 |
| Fsv2 | 11/15/2025 | 07/01/2026 | 11/15/2028 |
| G | 11/15/2025 | 07/01/2026 | 11/15/2028 |
| Gs | 11/15/2025 | 07/01/2026 | 11/15/2028 |
| HBv2 | 04/02/2026 | 04/02/2026 | 05/31/2027 |
| Ls | 05/01/2025 | 07/01/2026 | 05/01/2028 |
| Lsv2 | 11/15/2025 | 07/01/2026 | 11/15/2028 |
| NP-series | 04/02/2026 | 04/02/2026 | 05/31/2027 |

Note

Purchases of 1-year and 3-year Azure Reserved VM Instances for NP-series ended on 04/02/2026.

#### Q: Why should I modernize my VM?

Modernization is mandatory to avoid unexpected shutdown. Additionally, modernization yields the following benefits:

- **Performance**: Newer VM series offer better price-to-performance ratios.
- **Regional Availability**: The v5 and v6 series has broader regional support across Azure data centers.
- **Future-proofing**: Modernize ahead of the retirement schedule to avoid disruption.

#### Q: When do Dv3, Dsv3, Ev3, and Esv3 retire, and how are Reserved Instance (RI) purchases and renewals changing?

The Dv3, Dsv3, Ev3, and Esv3 series retire on November 15, 2029. The retirement affects all 32 sizes in these series. After that date, you can't create, resize into, run, or purchase these sizes. This retirement doesn't apply to Azure Government, Azure operated by 21Vianet, or sovereign cloud regions.

One-year and three-year RIs for these series are no longer available for new purchases or renewals after July 1, 2026. Existing RIs continue through the end of their term. If you continue to use these series before retirement, Azure savings plan for compute is the primary recommendation.

The retirement is separate from the [capacity growth restrictions](../retirements-and-capacity-restrictions) that began in July 2026.

For the smoothest transition, move Dv3 and Dsv3 workloads to Dv5, Dsv5, Ddv5, Ddsv5, Dasv5, or Dadsv5, and move Ev3 and Esv3 workloads to Ev5, Esv5, Edv5, Edsv5, Easv5, or Eadsv5. For more information, see [Modernize to the v5 VM series](../sizes-v5-modernization-overview). For the latest features and performance, see [Modernize to the v6 and v7 VM series](../sizes-v6-v7-modernization-overview).

#### Q: What will happen to my VM if I do not resize my VM to a target size within the retirement timeline?

After retirement, VMs using this size will be deallocated and stop incurring charges. The size is no longer supported or covered by an SLA; in‑memory and temporary disk data is lost, but managed disk data is preserved. To resume service, you may resize to a supported size and restart the VM.

Specifically for HBv2-series: after May 31, 2027, HBv2-series VMs (Standard\_HB120rs\_v2 and derived sizes) will be automatically set to a deallocated state. After that date, HBv2 VMs will stop working, lose SLA and support, and stop incurring billing charges.

Specifically for NP-series: after May 31, 2027, NP-series VMs (Standard\_NP10s, Standard\_NP20s, Standard\_NP40s) will be automatically set to a deallocated state. They'll stop working, lose SLA and support, and stop incurring billing charges. Managed disk data is preserved, but workloads won't resume until you resize to a supported VM size.

#### Q: Can I recover my VM after it has been deallocated?

Yes, you can resize and restart your deallocated VM following the [Azure VM resizing guide](/en-us/azure/virtual-machines/sizes/resize-vm?tabs=portal).

#### Q: Will VM modernization disrupt pay-as-you-go or Savings Plan Pricing billing?

No. If you’re using pay-as-you-go or a savings plan, modernizing to a newer VM type won't disrupt your current billing. The modernization process remains seamless with no changes required in your subscription or payment plan.

#### Q: How can I modernize my VM if I am on Reserved Instances (RIs) with a retired VM?

If you have active Reserved Instances for any of listed the series in FAQ chart, follow these steps:

Step 1: Review Current Reservations

- Check your active RIs in the [Azure portal](/en-us/azure/cost-management-billing/reservations/manage-reserved-vm-instance).

Identify which RIs are expiring or will be affected by the VM retirement.

Step 2: Modernize and manage your RIs

Depending on your business needs, consider these options:

1. **Exchange Existing Reservations**:

    - Swap current RIs for a new VM series without any penalties.
    - Refer to the [RI Exchange Guide](/en-us/azure/cost-management-billing/reservations/exchange-and-refund-azure-reservations)
2. **Trade-In for Savings Plan**:

    - Convert your existing RIs into an **Azure Savings Plan for compute**.
    - This offers flexibility across VM families and regions.
    - Follow the [Azure RI Trade-In Tutorial](/en-us/azure/cost-management-billing/savings-plan/reservation-trade-in).
3. **Purchase New RIs**:

    - Buy new reservations that align with your new v6 VM series.
    - Consider shorter terms (1-year) for flexibility.