---
layout: Conceptual
title: Configuration and Optimization of InfiniBand enabled H-series and N-series Azure Virtual Machines - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/high-performance-compute/configure
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
author: iamwilliew
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: mattmcinnes
ms.author: wwilliams
ms.update-cycle: 1095-days
description: Learn about configuring and optimizing the InfiniBand enabled H-series and N-series VMs for HPC.
ms.service: azure-virtual-machines
ms.subservice: hpc
ms.custom: linux-related-content
ms.topic: concept-article
ms.date: 2026-09-25T00:00:00.0000000Z
locale: en-us
document_id: 0bc7dad5-befc-cf92-c942-4239dbff1854
document_version_independent_id: d6ebfcdc-2bfa-7e6f-1724-b858c7a0bb93
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/high-performance-compute/configure.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/high-performance-compute/configure
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/high-performance-compute/configure.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: b8056ba4-b4ae-d3f4-9823-b72054d74754
---

# Configuration and Optimization of InfiniBand enabled H-series and N-series Azure Virtual Machines - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs ✔️ Windows VMs ✔️ Flexible scale sets ✔️ Uniform scale sets

This article shares some guidance on configuring and optimizing the InfiniBand-enabled [HB-series](../overview#high-performance-compute) and [N-series](../overview#gpu-accelerated) VMs for HPC.

## VM images

On InfiniBand (IB) enabled VMs, the appropriate IB drivers are required to enable RDMA.

- The Ubuntu-HPC VM images in the Marketplace come preconfigured with the appropriate NVIDIA IB drivers and GPU drivers.
- The AlmaLinux-HPC VM images in the Marketplace come preconfigured with the appropriate NVIDIA IB drivers and GPU drivers.

These VM images are based on the base Ubuntu and AlmaLinux marketplace VM images. Scripts used in the creation of these VM images from their base marketplace images are on the [azhpc-images repo](https://github.com/Azure/azhpc-images/).

On GPU enabled [N-series](../overview#gpu-accelerated) VMs, the appropriate GPU drivers are additionally required. This can be available by the following methods:

- Use the Ubuntu-HPC VM images or AlmaLinux-HPC VM images that come preconfigured with the NVIDIA GPU drivers and GPU compute software stack (CUDA, NCCL).
- Add the GPU drivers through the [VM extensions](../../extensions/hpccompute-gpu-linux).
- Install the GPU drivers [manually](../../linux/n-series-driver-setup).
- Some other VM images on the Marketplace also come preinstalled with the NVIDIA GPU drivers, including some VM images from NVIDIA.

Depending on the workloads' Linux distro and version needs, Ubuntu-HPC VM images and AlmaLinux-HPC VM images on the Marketplace are the easiest way to get started with HPC and AI workloads on Azure. It's also recommended to create [custom VM images](../../linux/tutorial-custom-images) with workload specific customization and configuration for reuse.

### VM sizes supported by the HPC VM images

#### InfiniBand OFED support

The latest Azure HPC marketplace images come with Mellanox OFED 5.1 and above, which do not support ConnectX3-Pro InfiniBand cards. ConnectX-3 Pro InfiniBand cards require MOFED 4.9 LTS version. These VM images only support ConnextX-5 and newer InfiniBand cards. The following VM size support matrix for the InfiniBand OFED in these HPC VM images:

- [HB-series](../overview#high-performance-compute): HB, HC, HBv2, HBv3, HBv4
- [N-series](../overview#gpu-accelerated): NDv2, NDv4

#### GPU driver support

Currently only the Ubuntu-HPC VM images and AlmaLinux-HPC VM images come preconfigured with the NVIDIA GPU drivers and GPU compute software stack (CUDA, NCCL).

The VM size support matrix for the GPU drivers in supported HPC VM images is as follows:

- [N-series](../overview#gpu-accelerated): NDv2, NDv4 VM sizes are supported with the NVIDIA GPU drivers and GPU compute software stack (CUDA, NCCL).
- The other 'NC' and 'ND' VM sizes in the [N-series](../overview#gpu-accelerated) are supported with the NVIDIA GPU drivers.

All of the VM sizes in the N-series support [Gen 2 VMs](../../generation-2), though some older ones also support Gen 1 VMs. Gen 2 support is also indicated with a "01" at the end of the image URN or version.

### SR-IOV enabled VMs

#### Ubuntu-HPC VM images

For SR-IOV enabled [RDMA capable VMs](../overview#high-performance-compute), Ubuntu-HPC VM images versions 18.04, 20.04, and 22.04 are suitable. These VM images come preconfigured with the Mellanox OFED drivers for RDMA, NVIDIA GPU drivers, GPU compute software stack (CUDA, NCCL), and commonly used MPI libraries and scientific computing packages. Refer to the VM size support matrix.

- The available or latest versions of the VM images can be listed with the following information using [CLI](/en-us/cli/azure/vm/image#az-vm-image-list) or [Marketplace](https://azuremarketplace.microsoft.com/marketplace/apps/microsoft-dsvm.ubuntu-hpc?tab=overview).

    ```output
    "publisher": "Microsoft-DSVM",
    "offer": "Ubuntu-HPC",
    ```
- Scripts used in the creation of the Ubuntu-HPC VM images from a base Ubuntu Marketplace image are on the [azhpc-images repo](https://github.com/Azure/azhpc-images/tree/master).

#### AlmaLinux-HPC VM images

For SR-IOV enabled [RDMA capable VMs](../overview#high-performance-compute), AlmaLinux-HPC VM images versions 8.5, 8.6, and 8.7 are suitable. These VM images come preconfigured with the Mellanox OFED drivers for RDMA, NVIDIA GPU drivers, GPU compute software stack (CUDA, NCCL), and commonly used MPI libraries and scientific computing packages. Refer to the VM size support matrix.

- The available or latest versions of the VM images can be listed with the following information using [CLI](/en-us/cli/azure/vm/image#az-vm-image-list) or [Marketplace](https://azuremarketplace.microsoft.com/marketplace/apps/almalinux.almalinux-hpc?tab=overview).

    ```output
    "publisher": "AlmaLinux",
    "offer": "AlmaLinux-HPC",
    ```
- Scripts used in the creation of the AlmaLinux-HPC VM images from a base AlmaLinux Marketplace image are on the [azhpc-images repo](https://github.com/Azure/azhpc-images/tree/master).

Additionally, more details on what's included in the Ubuntu-HPC VM images and AlmaLinux-HPC VM images, and how to deploy them are in [Azure HPC VM images](azure-hpc-vm-images).

### RHEL VM images

The base RHEL-based non-HPC VM images on the Marketplace can be configured for use on the SR-IOV enabled [RDMA capable VMs](../overview#high-performance-compute). Learn more about [enabling InfiniBand](../../extensions/enable-infiniband) and [setting up MPI](setup-mpi) on the VMs.

### Ubuntu VM images

The base Ubuntu Server 20.04 LTS and 22.04 LTS VM images in the Marketplace are supported for both SR-IOV and non-SR-IOV [RDMA capable VMs](../overview#high-performance-compute). Learn more about [enabling InfiniBand](../../extensions/enable-infiniband) and [setting up MPI](setup-mpi) on the VMs.

- Instructions for enabling InfiniBand on the Ubuntu VM images are in a [TechCommunity article](https://techcommunity.microsoft.com/t5/azure-compute/configuring-infiniband-for-ubuntu-hpc-and-gpu-vms/ba-p/1221351).

Note

Mellanox OFED 5.1 and above don't support ConnectX3-Pro InfiniBand cards on SR-IOV enabled N-series VM sizes with FDR InfiniBand (e.g. NCv3). Please use LTS Mellanox OFED version 4.9-0.1.7.0 or older on the N-series VM's with ConnectX3-Pro cards. For more information, see [Linux InfiniBand Drivers](https://www.mellanox.com/products/infiniband-drivers/linux/mlnx_ofed).

### SUSE Linux Enterprise Server VM images

SLES 12 SP3 for HPC, SLES 12 SP3 for HPC (Premium), SLES 12 SP1 for HPC, SLES 12 SP1 for HPC (Premium), SLES 12 SP4 and SLES 15 VM images in the Marketplace are supported. These VM images come preloaded with the Network Direct drivers for RDMA (on the non-SR-IOV VM sizes) and Intel MPI version 5.1. Learn more about [setting up MPI](setup-mpi) on the VMs.

## Optimize VMs

The following are some optional optimization settings for improved performance on the VM.

### Update LIS

If necessary for functionality or performance, [Linux Integration Services (LIS) drivers](../../linux/endorsed-distros) can be installed or updated on supported OS distros, especially is deploying using a custom image or an older OS version such as RHEL 6.x or earlier version of 7.x.

```bash
wget https://aka.ms/lis
tar xzf lis
pushd LISISO
sudo ./upgrade.sh
```

### Reclaim memory

Improve performance by automatically reclaiming memory to avoid remote memory access.

```bash
sudo echo 1 >/proc/sys/vm/zone_reclaim_mode
```

Keep reclaim memory mode persistent after VM reboots:

```bash
sudo echo "vm.zone_reclaim_mode = 1" >> /etc/sysctl.conf sysctl -p
```

### Disable firewall and SELinux

```bash
sudo systemctl stop iptables.service
sudo systemctl disable iptables.service
sudo systemctl mask firewalld
sudo systemctl stop firewalld.service
sudo systemctl disable firewalld.service
sudo iptables -nL
sudo sed -i -e's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
```

### Disable cpupower

```bash
sudo service cpupower status
```

If enabled, disable it:

```bash
sudo service cpupower stop
sudo systemctl disable cpupower
```

### Configure WALinuxAgent

```bash
sudo sed -i -e 's/# OS.EnableRDMA=y/OS.EnableRDMA=y/g' /etc/waagent.conf
```

Optionally, the WALinuxAgent may be disabled before running a job then enabled post-job for maximum VM resource availability to the HPC workload.