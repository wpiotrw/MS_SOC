---
layout: Conceptual
title: Troubleshooting known issues with HPC and GPU VMs - Azure Virtual Machines - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/high-performance-compute/hb-hc-known-issues
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
author: Padmalathas
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: padmalathas
ms.update-cycle: 1095-days
description: Learn about troubleshooting known issues with HPC and GPU virtual machine (VM) sizes in Azure.
ms.service: azure-virtual-machines
ms.subservice: hpc
ms.custom: linux-related-content
ms.topic: troubleshooting
ms.date: 2026-09-25T00:00:00.0000000Z
locale: en-us
document_id: c54ece87-a44f-cdd6-6488-354fe5eb8f1f
document_version_independent_id: a35a586a-7c4e-6e50-9b2f-e4f4612b97cb
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/high-performance-compute/hb-hc-known-issues.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/high-performance-compute/hb-hc-known-issues
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/high-performance-compute/hb-hc-known-issues.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 04127287-d583-86ca-227f-e41ee302c755
---

# Troubleshooting known issues with HPC and GPU VMs - Azure Virtual Machines - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows VMs ✔️ Flexible scale sets ✔️ Uniform scale sets

This article attempts to list recent common issues and their solutions when using the [HB-series](../overview#high-performance-compute) and [N-series](../overview#gpu-accelerated) HPC and GPU VMs.

## AMD NVv5 V710 and NGv1 V620 Linux GPU drivers NULL Pointer Dereference (CVE-2026-43603) might cause denial-of-service

A vulnerability in the AMD Linux GPU driver (CVE-2026-43603) could allow a local user to trigger a kernel crash and denial of service through a NULL pointer dereference. Azure plans to release updated Linux guest drivers for NVv5 V710 and NGv1 V620 by September 28, 2026. For more information, see the AMD Security Bulletin SB-6034 [Linux GPU Driver NULL Pointer Dereference](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-6034.html).

## NVIDIA-SMI Not Showing Full Telemetry on NCv6 (RTX Pro 6000) virtual machines

Running the `nvidia-smi` will not show full telemetry of the RTX Pro 6000 Blackwell GPU(s) on a NCv6-series virtual machine. Specifically, power and utilization statistics will not be exposed. This is due to the use of an SRIOV-based exposure of the GPU(s) to the virtual machine, as opposed to passthrough mode. This is a known limitation of NVIDIA's SRIOV driver supporting "vGPU" functionality.

## InfiniBand RDMA and NUMA Node Affinity on HBv5 virtual machines

On certain HBv5 virtual machines (VMs), the InfiniBand RDMA device names (such as mlx5\_[0-3]) may not align correctly with their respective NUMA node affinities. Ideally, each RDMA device should be mapped as follows:

- mlx5\_0 is on NUMA node: 0
- mlx5\_1 is on NUMA node: 4
- mlx5\_2 is on NUMA node: 8
- mlx5\_3 is on NUMA node: 12

However, an incorrect mapping example could be:

- mlx5\_0 is on NUMA node: 4
- mlx5\_1 is on NUMA node: 8
- mlx5\_2 is on NUMA node: 12
- mlx5\_3 is on NUMA node: 0

This misalignment can lead to performance degradation, particularly when running multinode MPI workloads.

To confirm whether your RDMA devices are correctly mapped to NUMA nodes, execute the following script:

```bash
for d in /sys/class/infiniband/*;
do
dev=$(basename "$d")
node=$(cat "$d/device/numa_node")
echo "$dev is on NUMA node: $node"
done
```

Compare the output with the ideal mapping listed above.

Solution: Persistent device naming with Udev rules

To remediate the misalignment issue, follow these steps:

1. Create a new file in /etc/udev/rules.d/, for example: 99-rdma-persistent-naming.rules
2. Add the following lines to the file: 

    ```bash
    ACTION=="add", SUBSYSTEMS=="pci", KERNELS=="0101:00:00.0", PROGRAM="rdma_rename %k NAME_FIXED mlx5_ib0"
    ACTION=="add", SUBSYSTEMS=="pci", KERNELS=="0102:00:00.0", PROGRAM="rdma_rename %k NAME_FIXED mlx5_ib1"
    ACTION=="add", SUBSYSTEMS=="pci", KERNELS=="0103:00:00.0", PROGRAM="rdma_rename %k NAME_FIXED mlx5_ib2"
    ACTION=="add", SUBSYSTEMS=="pci", KERNELS=="0104:00:00.0", PROGRAM="rdma_rename %k NAME_FIXED mlx5_ib3"
    ```
3. Reload udev rules and trigger device events: 

    ```bash
    # udevadm control --reload
    # udevadm trigger --type=devices --action=add
    ```

This solution ensures that RDMA device naming persists across VM reboots.

## Cache topology on Standard\_HB120rs\_v3

`lstopo` displays incorrect cache topology on the Standard\_HB120rs\_v3 VM size. It may display that there’s only 32 MB L3 per nonuniform memory access (NUMA) node. However, in practice, there's indeed 120 MB L3 per NUMA as expected since the same 480 MB of L3 to the entire VM is available as with the other constrained-core HBv3 VM sizes. This incorrect display is a cosmetic error and shouldn't affect workloads.

## Access Restriction on queue pair 0

To prevent low-level hardware access that can result in security vulnerabilities, Queue Pair 0 isn't accessible to guest VMs. This restriction should only affect actions typically associated with administration of the ConnectX InfiniBand network interface card (NIC) and running some InfiniBand diagnostics like ibdiagnet, but not end-user applications.

## Accelerated Networking on InfiniBand-equipped virtual machines

[Azure Accelerated Networking](https://azure.microsoft.com/blog/maximize-your-vm-s-performance-with-accelerated-networking-now-generally-available-for-both-windows-and-linux/) allows enhanced throughput and latencies over the Azure Ethernet network. Though Accelerated Networking is separate from the InfiniBand network, its use may affect behavior of certain MPI implementations when running jobs over InfiniBand. Specifically, the InfiniBand interface on some VMs may have a slightly different name (mlx5\_1 as opposed to earlier mlx5\_0). This issue may require tweaking of the MPI command lines, especially when using the UCX interface (commonly with OpenMPI and HPC-X).

For more information on this issue, see the [TechCommunity article with instructions on how to address any observed issues](https://techcommunity.microsoft.com/t5/azure-compute/accelerated-networking-on-hb-hc-and-hbv2/ba-p/2067965).

## Cache Cleaning

On HPC systems, it's often useful to clean up memory after a job finishes before the next user is assigned the same node. After running applications in Linux, you may find that your available memory reduces while your buffer memory increases, despite not running any applications.

![Screenshot of command prompt before cleaning](../../media/hpc/cache-cleaning-1.png)

Using `numactl -H` shows which NUMAnodes the memory is buffered with (possibly all). In Linux, users can clean the caches in three ways to return buffered or cached memory to ‘free’. You need to be root or have sudo permissions.

```bash
sudo echo 1 > /proc/sys/vm/drop_caches [frees page-cache]
sudo echo 2 > /proc/sys/vm/drop_caches [frees slab objects e.g. dentries, inodes]
sudo echo 3 > /proc/sys/vm/drop_caches [cleans page-cache and slab objects]
```

![Screenshot of command prompt after cleaning](../../media/hpc/cache-cleaning-2.png)

- Read about the latest announcements, HPC workload examples, and performance results at the [Azure Compute Tech Community Blogs](https://techcommunity.microsoft.com/t5/azure-compute/bg-p/AzureCompute).
- For a higher-level architectural view of running HPC workloads, see [High Performance Computing (HPC) on Azure](/en-us/azure/architecture/topics/high-performance-computing/).