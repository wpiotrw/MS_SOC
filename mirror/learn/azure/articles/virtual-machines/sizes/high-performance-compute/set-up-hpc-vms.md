---
layout: Conceptual
title: Set up Azure HPC or AI VMs - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/high-performance-compute/set-up-hpc-vms
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
author: sherrywangms
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: mattmcinnes
ms.author: sherrywang
ms.update-cycle: 1095-days
description: How to set up an Azure HPC or AI virtual machine with NVIDIA or AMD GPUs using the Azure portal.
ms.service: azure-virtual-machines
ms.subservice: hpc
ms.topic: how-to
ms.date: 2026-09-25T00:00:00.0000000Z
locale: en-us
document_id: fcc8f2b7-b446-e4d5-9818-f0b0c30754dc
document_version_independent_id: 80914bf3-9fb9-f253-557b-2bd7e4efa6ab
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/sizes/high-performance-compute/set-up-hpc-vms.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../../toc.json
asset_id: virtual-machines/sizes/high-performance-compute/set-up-hpc-vms
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/sizes/high-performance-compute/set-up-hpc-vms.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 83a8c32e-dd9c-9e3e-25cc-102937e13300
---

# Set up Azure HPC or AI VMs - Azure Virtual Machines | Microsoft Learn

This how-to guide explains how to create a basic Azure virtual machine (VM) for HPC and AI with NVIDIA or AMD GPUs. These VM sizes are intended for workloads that require high-performance computing (HPC sizes), or GPU-accelerated computing (AI sizes).

## Choose your VM size

Azure VMs have many different options, called [VM sizes](../overview). There are different series of [VM sizes for HPC](../overview#high-performance-compute) and [VM sizes GPU-optimized computing](../overview#gpu-accelerated). Select the appropriate VM size for the workload you want to use. For help with selecting sizes, see the [VM selector tool](https://azure.microsoft.com/pricing/vm-selector/).

Not all Azure products are available in all Azure regions. For more information, see the current list of [products available by region](https://azure.microsoft.com/global-infrastructure/services/).

## Create your VM

Before you can deploy a workload, you need to create your VM through the Azure portal.

Depending on your VM's operating system, review either the [Linux VM quickstart](../../linux/quick-create-portal) or [Windows VM quickstart](../../windows/quick-create-portal). Then, create your VM with the following settings:

1. For **Subscription**, select the Azure subscription that you want to use for this VM.
2. For **Region**, select a region with capacity available for your VM size.
3. For **Image**, select the image of the VM you chose in the previous section.

    Note

    For the purpose of example, this guide uses the image **NVIDIA GPU-Optimized Image for AI & HPC – v21.04.1 – Gen 1**. If you're using another image, you might need to install other software, like the NVIDIA driver and Docker, before proceeding.
4. For **Size**, select the HPC or GPU instance type. For more information, see how to choose your VM size.
5. For **SSH public key source**, select **Generate a new key pair**.
6. Wait for key validation to complete.
7. When prompted, select **Download private key and create resource**.

    Note

    Downloading the key pair is necessary to SSH into your VM for later configuration.
8. For **Key pair name**, enter a name for your key pair.
9. Under the **Networking** tab, make sure **Accelerated Networking** is disabled.
10. Optionally, add a data disk to your VM. For more information, see how to add a data disk [to a Linux VM](/en-us/azure/virtual-machines/linux/attach-disk-portal) or [to a Windows VM](/en-us/azure/virtual-machines/windows/attach-managed-disk-portal).

    Note

    Adding a data disk helps you store models, data sets, and other necessary components for benchmarking.
11. Select **Review + create** to create your VM.

## Connect to your VM

Connect to your new VM using SSH, which allows you to perform further configuration. Some connection methods include:

- [Connect over SSH on Linux or macOS](../../linux/mac-create-ssh-keys#ssh-into-your-vm)
- [Connect over SSH on Windows](../../linux/ssh-from-windows#connect-to-your-vm)
- [Connect over SSH using Azure Bastion](/en-us/azure/bastion/bastion-connect-vm-ssh-linux)

## Set up VM

Set up your new VM for HPC or AI workloads. Install the newest NVIDIA or AMD GPU driver, which maps to your VM size.

- [Install NVIDIA GPU drivers on N-series VMs running Linux](../../linux/n-series-driver-setup)
- [Install NVIDIA GPU drivers on N-series VMs running Windows](../../windows/n-series-driver-setup)
- [Install AMD GPU drivers on N-series VMs running Windows](../../windows/n-series-amd-driver-setup)