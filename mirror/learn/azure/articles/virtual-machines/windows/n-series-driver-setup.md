---
layout: Conceptual
title: Azure N-series NVIDIA GPU driver setup for Windows - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/windows/n-series-driver-setup
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
manager: jkabat
ms.reviewer: wwilliams
ms.author: yangnicole
ms.update-cycle: 365-days
description: How to set up NVIDIA GPU drivers for N-series VMs running Windows Server or Windows in Azure
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.collection: windows
ms.topic: how-to
ms.date: 2026-05-06T00:00:00.0000000Z
ms.custom: H1Hack27Feb2017
locale: en-us
document_id: 3c5bc749-3f68-e230-37ff-f74ce72efb59
document_version_independent_id: 2a382803-e085-82e2-4139-be5c8b9e1a0d
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/windows/n-series-driver-setup.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../toc.json
asset_id: virtual-machines/windows/n-series-driver-setup
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/windows/n-series-driver-setup.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 8ddaefda-1e5b-3ff3-0c85-1b355701b641
---

# Azure N-series NVIDIA GPU driver setup for Windows - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Windows VMs

To take advantage of the graphics processing unit (GPU) capabilities of an Azure N-series virtual machine (VM) backed by NVIDIA GPUs, you must install NVIDIA GPU drivers. The [NVIDIA GPU Driver Extension](../extensions/hpccompute-gpu-windows) installs appropriate NVIDIA Compute Unified Device Architecture (CUDA) or GRID drivers on an N-series VM. You can install and manage the extension using the Azure portal or tools such as Azure PowerShell. See the [NVIDIA GPU Driver Extension documentation](../extensions/hpccompute-gpu-windows) for supported operating systems (OS) and deployment steps.

To install NVIDIA GPU drivers manually, follow the steps outlined in this article. Manual driver setup information is also available for [Linux VMs](../linux/n-series-driver-setup).

For technical specifications, see [GPU Windows VM sizes](../sizes-gpu?toc=/azure/virtual-machines/windows/toc.json).

Warning

Installing NVIDIA drivers using methods other than those outlined in this guide may result in failure of the intended driver installation, and is unsupported by Microsoft and NVIDIA. To ensure proper functionality and support, please follow only the installation steps and use the driver versions specified in this article.

## CUDA Drivers

CUDA drivers are distributed by NVIDIA for NCasT4\_v3, NC\_A100\_v4, and NCads\_H100\_v5 VMs.

### Supported CUDA Drivers

For the latest CUDA drivers and supported OS, visit the [NVIDIA website](https://developer.nvidia.com/cuda-zone). Ensure that you install or upgrade to the latest supported CUDA driver for your distribution.

### CUDA Driver Installation

For CUDA driver installation instructions, visit the [NVIDIA website](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html#axzz4ZcwJvqYi).

## GRID Drivers

Microsoft redistributes NVIDIA GRID driver installers for NVv3, NCasT4\_v3, NVadsA10\_v5, and NCv6 RTX PRO 6000 BSE VMs used as virtual workstations or for virtual applications.

### Supported GRID Drivers

Install these GRID drivers only on these VMs and only on the operating systems listed in the following table. These drivers include licensing for GRID Virtual GPU (vGPU) software in Azure. You do not need to set up an NVIDIA vGPU software license server.

Warning

NVIDIA v17.x (R550) and v18.x (R570) GRID drivers are no longer supported for NVadsA10\_v5 VMs. Instead, use the v19.x and v20.x drivers listed in the following table.

| VM Series | GPU | GRID Driver | Supported Windows OS Versions |
| --- | --- | --- | --- |
| NCv6 RTX PRO 6000 BSE | NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96GB) | [vGPU20.2](https://download.microsoft.com/download/0f21fd13-2390-4c79-876a-87ae3dc724c6/596.86_grid_win10_win11_server2022_server2025_dch_64bit_international_azure_swl.exe) | • Windows 11 25H2 (including all supported Windows 11 releases up to 25H2)  • Windows 11 25H2 AVD  • Windows Server 2025  • Windows Server 2022 |
| NCasT4\_v3 | NVIDIA Tesla T4 GPU (16GB) | • [vGPU20.2](https://download.microsoft.com/download/0f21fd13-2390-4c79-876a-87ae3dc724c6/596.86_grid_win10_win11_server2022_server2025_dch_64bit_international_azure_swl.exe) • [vGPU19.6 (LTS)](https://download.microsoft.com/download/29a0b851-7631-445b-b829-f4a03042bd1b/582.78_grid_win10_win11_server2019_server2022_dch_64bit_international_azure_swl.exe) | • Windows 11 25H2 (including all supported Windows 11 releases up to 25H2)  • Windows 11 25H2 AVD  • Windows Server 2025  • Windows Server 2022 |
| NVadsA10\_v5 | NVIDIA A10 GPU (24GB) | • [vGPU20.2](https://download.microsoft.com/download/0f21fd13-2390-4c79-876a-87ae3dc724c6/596.86_grid_win10_win11_server2022_server2025_dch_64bit_international_azure_swl.exe) • [vGPU19.6 (LTS)](https://download.microsoft.com/download/29a0b851-7631-445b-b829-f4a03042bd1b/582.78_grid_win10_win11_server2019_server2022_dch_64bit_international_azure_swl.exe) | • Windows 11 25H2 (including all supported Windows 11 releases up to 25H2)  • Windows 11 25H2 AVD  • Windows Server 2025  • Windows Server 2022 |
| NVv3 ([retiring September 30th, 2026](/en-us/azure/virtual-machines/sizes/lifecycle/retirement/nvv3-series-retirement)) | NVIDIA Tesla M60 GPU (16GB) | [vGPU16 (LTS)](https://download.microsoft.com/download/a/3/1/a3186ac9-1f9f-4351-a8e7-b5b34ea4e4ea/538.46_grid_win10_win11_server2019_server2022_dch_64bit_international_azure_swl.exe) | • Windows 11 23H2 (including all supported Windows 11 releases up to 23H2)  • Windows 11 22H2 AVD  • Windows 11 23H2 AVD  • Windows Server 2019  • Windows Server 2022 |

For more information on the specific vGPU and driver branch versions, visit the [NVIDIA website](https://docs.nvidia.com/grid/).

### GRID Driver Installation

1. Connect by remote desktop to each N-series VM.
2. Within the virtual machine, download, extract, and install the supported driver for your Windows operating system.

After GRID driver installation is complete, restart the VM to ensure the proper functionality.

### Verify GRID Driver Installation

1. Open a command prompt and change to the C:\Program Files\NVIDIA Corporation\NVSMI directory.
2. Run `nvidia-smi`. If the driver is installed, Nvidia SMI will list the **GPU-Util** as N/A until you run a GPU workload on the VM.