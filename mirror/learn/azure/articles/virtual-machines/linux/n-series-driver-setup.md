---
layout: Conceptual
title: Azure N-series GPU driver setup for Linux - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/linux/n-series-driver-setup
breadcrumb_path: ../../breadcrumb/azure-compute/toc.json
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
author: yangnicole-ml
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: padmalathas, mattmcinnes
ms.author: yangnicole
ms.update-cycle: 365-days
description: How to set up NVIDIA GPU drivers for N-series VMs running Linux in Azure
services: virtual-machines
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.collection: linux
ms.topic: how-to
ms.custom: linux-related-content
ms.date: 2026-05-06T00:00:00.0000000Z
locale: en-us
document_id: 0e03790a-1bf9-146d-704b-6816d475064b
document_version_independent_id: ad5f6be7-e089-161f-306c-39d10e7ab0a0
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/linux/n-series-driver-setup.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../toc.json
asset_id: virtual-machines/linux/n-series-driver-setup
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/linux/n-series-driver-setup.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 4a3b3d1e-2753-97b3-cd7a-352006c3c998
---

# Azure N-series GPU driver setup for Linux - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs

Important

To align with inclusive language practices, this documentation replaces the term "blacklist" with "blocklist". This change reflects a commitment to avoiding terminology that might carry unintended negative connotations or perceived racial bias. However, in code snippets and technical references where "blacklist" is part of established syntax or tooling (for example, configuration files, command-line parameters), the original term is retained to preserve functional accuracy. This usage is strictly technical and doesn't imply any discriminatory intent.

To take advantage of the graphics processing unit (GPU) capabilities of an Azure N-series virtual machine (VM) backed by NVIDIA GPUs, you must install NVIDIA GPU drivers. The [NVIDIA GPU Driver Extension](../extensions/hpccompute-gpu-linux) installs appropriate NVIDIA Compute Unified Device Architecture (CUDA) or GRID drivers on an N-series VM. You can install and manage the extension by using the Azure portal or tools such as Azure PowerShell. For supported operating systems (OS) and deployment steps, see the [NVIDIA GPU Driver Extension documentation](../extensions/hpccompute-gpu-linux).

To install NVIDIA GPU drivers manually, follow the steps outlined in this article. Manual driver setup information is also available for [Windows VMs](../windows/n-series-driver-setup).

For technical specifications, see [GPU Linux VM sizes](../sizes-gpu?toc=/azure/virtual-machines/linux/toc.json).

Warning

Installing NVIDIA drivers by using methods other than those outlined in this article might result in failure of the intended driver installation. Microsoft and NVIDIA don't support this installation. To ensure proper functionality and support, follow only the installation steps and use the driver versions specified in this article.

## CUDA drivers

NVIDIA distributes CUDA drivers for NCasT4\_v3, NC\_A100\_v4, and NCads\_H100\_v5 VMs.

### Supported CUDA drivers

For the latest CUDA drivers and supported OS, visit the [NVIDIA website](https://developer.nvidia.com/cuda-zone). Ensure that you install or upgrade to the latest supported CUDA driver for your distribution.

### CUDA driver installation

For CUDA driver installation, visit the [NVIDIA website](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html).

### Verify CUDA driver installation

Run `nvidia-smi`. If the driver is installed, NVIDIA SMI lists the **GPU-Util** as N/A until you run a GPU workload on the VM.

## GRID drivers

Microsoft redistributes NVIDIA GRID driver installers for NVv3, NCasT4\_v3, NVadsA10\_v5, and NCv6 RTX PRO 6000 BSE VMs used as virtual workstations or for virtual applications.

### Supported GRID drivers

Install these GRID drivers only on these VMs and only on the operating systems listed in the following table. These drivers include licensing for GRID Virtual GPU (vGPU) software in Azure. You don't need to set up an NVIDIA vGPU software license server.

The NCasT4\_v3 and NCv6 RTX PRO 6000 BSE series are the only non-NV GPU VM series that support GRID drivers.

Warning

NVIDIA v17.x (R550) and v18.x (R570) GRID drivers are no longer supported for NVadsA10\_v5 VMs. Instead, use the v19.x and v20.x drivers listed in the following table.

| VM Series | GPU | GRID Driver | Supported Linux OS Versions |
| --- | --- | --- | --- |
| NCv6 RTX PRO 6000 BSE | NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96GB) | [vGPU20.2](https://download.microsoft.com/download/a7cb6d36-3bbc-43d6-9e88-e0842e6f9ab9/NVIDIA-Linux-x86_64-595.91.07-grid-azure.run) | • Ubuntu 24.04 LTS  • Ubuntu 22.04 LTS  • Ubuntu 20.04 LTS  • Red Hat Enterprise Linux (RHEL) 9.4, 9.6, 9.7  • Red Hat Enterprise Linux (RHEL) 8.10  • SUSE Linux Enterprise Server 15 SP7 |
| NCasT4\_v3 | NVIDIA Tesla T4 GPU (16GB) | • [vGPU20.2](https://download.microsoft.com/download/a7cb6d36-3bbc-43d6-9e88-e0842e6f9ab9/NVIDIA-Linux-x86_64-595.91.07-grid-azure.run) • [vGPU19.6 (LTS)](https://download.microsoft.com/download/4efc1974-7b6f-431f-ab2d-b8d99bb8a512/NVIDIA-Linux-x86_64-580.178.04-grid-azure.run) | • Ubuntu 24.04 LTS  • Ubuntu 22.04 LTS  • Ubuntu 20.04 LTS  • Red Hat Enterprise Linux (RHEL) 9.4, 9.6, 9.7  • Red Hat Enterprise Linux (RHEL) 8.10 |
| NVadsA10\_v5 | NVIDIA A10 GPU (24GB) | • [vGPU20.2](https://download.microsoft.com/download/a7cb6d36-3bbc-43d6-9e88-e0842e6f9ab9/NVIDIA-Linux-x86_64-595.91.07-grid-azure.run) • [vGPU19.6 (LTS)](https://download.microsoft.com/download/4efc1974-7b6f-431f-ab2d-b8d99bb8a512/NVIDIA-Linux-x86_64-580.178.04-grid-azure.run) | • Ubuntu 24.04 LTS  • Ubuntu 22.04 LTS  • Ubuntu 20.04 LTS  • Red Hat Enterprise Linux (RHEL) 9.4, 9.6, 9.7  • Red Hat Enterprise Linux (RHEL) 8.10 |
| NVv3 ([retiring September 30th, 2026](/en-us/azure/virtual-machines/sizes/lifecycle/retirement/nvv3-series-retirement)) | NVIDIA Tesla M60 GPU (16GB) | [vGPU16 (LTS)](https://download.microsoft.com/download/8/d/a/8da4fb8e-3a9b-4e6a-bc9a-72ff64d7a13c/NVIDIA-Linux-x86_64-535.161.08-grid-azure.run) | • Ubuntu 20.04 LTS  • Red Hat Enterprise Linux (RHEL) 8.6, 8.8, 8.9 |

For more information on the specific vGPU and driver branch versions, visit the [NVIDIA](https://docs.nvidia.com/grid/) website.

### GRID driver installation

1. Ensure that Secure Boot and vTPM are disabled.
2. Install prerequisites.

    Ubuntu:

    ```
    sudo apt update 
    sudo apt install -y build-essential 
    ```

    RHEL (8.10, 9.4, 9.6, 9.7):

    ```
    sudo yum check-update 
    sudo yum install -y make automake gcc gcc-c++ kernel-devel-$(uname -r) kernel-headers-$(uname -r) 
    ```
3. Download the Linux driver.

    a. For NCv6 RTX PRO 6000 BSE, NCasT4\_v3:

    ```
    wget -O ./NVIDIA-Linux-x86_64-595.58.03-grid-azure.run https://download.microsoft.com/download/51239696-ec04-4c02-a6b3-1d9c608fb57c/NVIDIA-Linux-x86_64-595.58.03-grid-azure.run
    ```

    b. For NVadsA10\_v5:

    ```
    wget -O ./NVIDIA-Linux-x86_64-570.211.01-grid-azure.run https://download.microsoft.com/download/2a04ca6a-9eec-40d9-9564-9cdea1ab795f/NVIDIA-Linux-x86_64-570.211.01-grid-azure.run
    ```

    c. For NVv3:

    ```
    wget -O ./NVIDIA-Linux-x86_64-535.161.08-grid-azure.run https://download.microsoft.com/download/8/d/a/8da4fb8e-3a9b-4e6a-bc9a-72ff64d7a13c/NVIDIA-Linux-x86_64-535.161.08-grid-azure.run
    ```
4. Install the driver.

    a. For NCv6 RTX PRO 6000 BSE:

    ```
    sudo chmod +x ./NVIDIA-Linux-x86_64-595.58.03-grid-azure.run
    sudo ./NVIDIA-Linux-x86_64-595.58.03-grid-azure.run -M open
    ```

    b. For NCasT4\_v3:

    ```
    sudo chmod +x ./NVIDIA-Linux-x86_64-595.58.03-grid-azure.run
    sudo ./NVIDIA-Linux-x86_64-595.58.03-grid-azure.run
    ```

    c. For NVadsA10\_v5:

    ```
    sudo chmod +x ./NVIDIA-Linux-x86_64-570.211.01-grid-azure.run
    sudo ./NVIDIA-Linux-x86_64-570.211.01-grid-azure.run
    ```

    d. For NVv3:

    ```
    sudo chmod +x ./NVIDIA-Linux-x86_64-535.161.08-grid-azure.run
    sudo ./NVIDIA-Linux-x86_64-535.161.08-grid-azure.run
    ```

### Verify GRID driver installation

Run `nvidia-smi`. If the driver is installed, NVIDIA SMI lists the **GPU-Util** as N/A until you run a GPU workload on the VM.

## Troubleshooting

- You can set persistence mode using `nvidia-smi` so the output of the command is faster when you need to query cards. To set persistence mode, run `nvidia-smi -pm 1`. If the VM is restarted, the mode setting goes away. You can always script the mode setting to run upon startup.
- If jobs are interrupted by ECC errors on the GPU (either correctable or uncorrectable), first check to see if the GPU meets any of Nvidia's [RMA criteria for ECC errors](https://docs.nvidia.com/deploy/dynamic-page-retirement/index.html#faq-pre). If the GPU is eligible for RMA, contact support about getting it serviced; otherwise, reboot your VM to reattach the GPU as described [here](https://docs.nvidia.com/deploy/dynamic-page-retirement/index.html#bl_reset_reboot). Less invasive methods, such as `nvidia-smi -r`, don't work with the virtualization solution deployed in Azure.