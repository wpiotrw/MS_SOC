---
layout: Conceptual
title: GPU Cloud PCs in Windows 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/gpu-cloud-pc
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn about GPU-enabled Cloud PCs in Windows 365.
keywords: 
author: heetpalod13
ms.author: hpalod
manager: dougeby
ms.date: 2026-05-19T00:00:00.0000000Z
ms.topic: overview
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: sefriend
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: d831ca2d-c3b8-d69c-ddcb-2555513df789
document_version_independent_id: d831ca2d-c3b8-d69c-ddcb-2555513df789
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/gpu-cloud-pc.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/gpu-cloud-pc
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/gpu-cloud-pc.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c450d479-44e5-4a9c-9b93-e6f9b69dd42d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68e273b0-a43e-4cc8-9bf9-67d4d6a1e869
platformId: 2918c3e5-1fd0-2bbf-ea37-e68ddbbf450d
---

# GPU Cloud PCs in Windows 365 | Microsoft Learn

Windows 365 offers GPU-enabled Cloud PCs that are suitable for graphics intense workloads that need to be performance optimized. These offerings can help with graphic design, image and video rendering, 3D modeling, and data processing and visualization applications that require a GPU to perform.

Four GPU offerings are available for Windows 365 Enterprise (including FedRamp) and Windows 365 Flex Cloud PCs in both dedicated & shared mode:

| GPU offering | Minimum specs | Powered by | Intended for |
| --- | --- | --- | --- |
| Windows 365 Enterprise GPU Select | 6 vCPU, 26-GB RAM, 4-GB vRAM, 256 GB | NVIDIA | Applications optimized for multimedia, UI, and productivity acceleration— supporting one 1920x1080 @ 30fps display. |
| Windows 365 Enterprise GPU Standard | 4 vCPU, 16-GB RAM, 8-GB vRAM, 512 GB (with 176-GB temporary storage) | NVIDIA | Applications that benefit from basic graphic acceleration on one 3840x2160 display or up to two 1920x1080p displays. |
| Windows 365 Enterprise GPU Super | 8 vCPU, 56-GB RAM, 12-GB vRAM, 1 TB (with 352-GB temporary storage) | NVIDIA | Applications with greater specification requirements and high-end graphics workloads on up to four 3840x2160 displays. |
| Windows 365 Enterprise GPU Max | 16 vCPU, 110-GB RAM, 16-GB vRAM, 1 TB (with 352-GB temporary storage) | NVIDIA | Graphics intensive workloads that demand high performance and have strict latency requirements. |

For more information on these offerings, see [Cloud PC size recommendations](cloud-pc-size-recommendations).

Since regional capacity is dynamic, Microsoft uses available capacity when and where it's needed. Sometimes, this might result in GPU Cloud PCs exceeding their license specified minimum specifications. To see your Cloud PC’s GPU specifications, visit the performance tab of Task Manager.

![Task manager performance for GPU Cloud PC](media/gpu-cloud-pc/performance.png)

GPU Cloud PCs don't support nested virtualization. Due to which, customers cannot use the following systems on their Windows 365 Enterprise GPU Cloud PCs:

- Windows Subsystem for Linux (WSL)
- Sandbox
- Hyper-V

For more information, see [Set up virtualization-based workloads on your Windows 365 Cloud PC.](nested-virtualization)

For purchasing the GPU offerings, contact your account team. GPU offerings aren't available from the web direct channel.

## GPU Cloud PC hosting and d: drive storage details

Microsoft hosts Windows 365 GPU-enabled Cloud PCs using the latest version of Microsoft Hyper-V.

Each of these Cloud PCs comes with an SSD storage drive (c:) for data and applications plus a large ephemeral disk (d:).

The ephemeral disk (d: drive) is deleted and recreated every time the Cloud PC reboots. Never use it to store your data. Instead, you can use it as a cache drive to store temporary files. This strategy is helpful to improve the performance of applications that need scratch disks to process large data sets.

## Registry keys and drivers on GPU Cloud PCs

Registry keys are automatically set during the provisioning process.

Supported drivers are automatically installed as part of the provisioning process. You don't need to manually install drivers. However, drivers aren't automatically updated, so you must manually update drivers as needed.

## Allowlist

You must allow the following URLs on each Windows 365 GPU Cloud PC:

| URL | Hardware |
| --- | --- |
| download.microsoft.com | Nvidia, AMD |
| go.microsoft.com | Nvidia, AMD |
| raw.githubusercontent.com/Azure/azhpc-extensions/master/NvidiaGPU/resources.json(Nvidia driver resource file) | Nvidia |
| raw.githubusercontent.com/Azure/azhpc-extensions/master/AmdGPU/resources.json (AMD driver resource file) | AMD |

## Supported regions

GPU offerings (Standard, Super & Max) are available in all [Windows 365 supported regions](requirements?tabs=enterprise,ent#supported-azure-regions-for-cloud-pc-provisioning) except for the following regions:

- Central US
- Norway East
- West Europe (Windows 365 Enterprise GPU Standard is available in this region)
- Mexico Central
- Japan West
- Spain Central
- Israel Central

Note that the West US 2 region is supported but is a restricted region.

The GPU Select and GPU Flex Cloud PCs (in shared mode) offerings are available in the following regions:

- Australia East
- Brazil South
- East Asia
- India Central
- Italy North
- Japan East
- Korea Central
- Poland Central
- South Africa North
- Southeast Asia
- Sweden Central

Note that the West Europe & East US 2 regions are supported but are restricted regions.

## Recommendations when using GPU Cloud PCs

For optimal performance of GPU-enabled Cloud PCs, consider these recommendations:

- Make sure that your network is configured to turn on UDP by default. For more information about UDP, see [RDP Shortpath](/en-us/azure/virtual-desktop/rdp-shortpath?tabs=public-networks#network-configuration).
- Make sure that you're running your GPU Cloud PC in full screen mode. Minimized windows require extra processing and coordination with the local device that can impede the session performance.
- Use the Windows app for optimal connection experience.
- Use Windows 11 Cloud PCs.
- GPU-enabled Cloud PCs come pre-provisioned with the correct driver needed for the best experience. For information about installing drivers, see [Install NVIDIA GPU drivers on N-series VMs running Windows](/en-us/azure/virtual-machines/windows/n-series-driver-setup) and [Install AMD GPU drivers on N-series VMs running Windows](/en-us/azure/virtual-machines/windows/n-series-amd-driver-setup) (for the Standard SKU only in limited regions). The use of any external drivers, including drivers from NVIDIA and AMD websites, isn't supported.
- Don’t use the Multimedia Redirection extension for the browser or for Teams. By default, this extension is uninstalled for GPU-enabled Cloud PCs during provisioning.
- GPU offerings aren't designed for game development. These offerings are optimized for graphics applications typically used in Enterprise scenarios. For more information with game development scenarios, see [Create a Game Development Virtual Machine with other Game Engines](/en-us/gaming/azure/).
- If you want to guarantee that all your users have the exact same GPU configuration, instead of using Cloud PCs, you can use Azure Virtual Desktop (AVD). AVD can help customers who prefer hardware specific configurations over workload focused configurations. For a complete list of Azure’s GPU offerings, see [Sizes for virtual machines in Azure - GPU accelerated](/en-us/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist#gpu-accelerated).
- By default, GPU-enabled Cloud PCs are provisioned to use GPU-accelerated remote frame encoding. For more information about different hardware-accelerated graphics encoding profiles and how to manage them on your GPU-enabled Cloud PCs, see [Enable GPU Acceleration](/en-us/azure/virtual-desktop/graphics-enable-gpu-acceleration?tabs=intune).

    - The following table lists compatibility of Windows 365 Cloud PC SKUs with our two different GPU-accelerated graphics encoding profiles:

| Windows 365 Enterprise GPU | Supported GPU-accelerated remote frame encoders |
| --- | --- |
| Max | HEVC/H.265AVC/H.264 |
| Super | HEVC/H.265AVC/H.264 |
| Standard | HEVC/H.265AVC/H.264 |
| Select | HEVC/H.265AVC/H.264 |