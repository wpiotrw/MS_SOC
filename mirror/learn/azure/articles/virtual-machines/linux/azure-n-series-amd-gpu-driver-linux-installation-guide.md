---
layout: Conceptual
title: Azure N-series AMD GPU Driver Setup for Linux - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/linux/azure-n-series-amd-gpu-driver-linux-installation-guide
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
author: nmagatala-MSFT
learn_banner_products:
- azure-virtual-machines
manager: rayoflores
ms.reviewer: wwilliams
ms.author: padmalathas
ms.update-cycle: 365-days
description: How to set up AMD Radeon PRO V710 NVv5 Linux Installation Guide.
services: virtual-machines
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.collection: linux
ms.topic: how-to
ms.custom: linux-related-content
ms.date: 2025-10-15T00:00:00.0000000Z
locale: en-us
document_id: 50a6b1f9-6eec-9626-68d8-93d80de9b8fb
document_version_independent_id: e6534027-19be-b88f-cdb6-85303e7fcb7f
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/linux/azure-n-series-amd-gpu-driver-linux-installation-guide.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../toc.json
asset_id: virtual-machines/linux/azure-n-series-amd-gpu-driver-linux-installation-guide
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/linux/azure-n-series-amd-gpu-driver-linux-installation-guide.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
- https://authoring-docs-microsoft.poolparty.biz/devrel/a3955c7b-f5ee-420d-aff5-d7119738f38b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31948f4-2f38-404b-ac93-c3c8c5b3ae33
platformId: 309d23c9-6c49-c3d0-f367-43c2002c99b1
---

# Azure N-series AMD GPU Driver Setup for Linux - Azure Virtual Machines | Microsoft Learn

**Applies to:** ✔️ Linux VMs

Important

To align with inclusive language practices, we've replaced the term "blacklist" with "blocklist" throughout this documentation. This change reflects our commitment to avoiding terminology that might carry unintended negative connotations or perceived racial bias. However, in code snippets and technical references where "blacklist" is part of established syntax or tooling (for example, configuration files, command-line parameters), the original term is retained to preserve functional accuracy. This usage is strictly technical and doesn't imply any discriminatory intent.

## NVads V710-series

To leverage the GPU capabilities of Azure’s new NVads V710-series virtual machines running Linux, you’ll need to install AMD GPU drivers. The AMD GPU driver extension streamlines this process by automating driver installation for NVv710-series VMs. You can manage the extension via the Azure portal, Azure PowerShell, or Azure Resource Manager (ARM) templates. For details on supported operating systems and deployment steps, see [AMD GPU Driver Extension](../extensions/hpccompute-amd-gpu-linux) documentation.

The [marketplace image](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/amdinc1746636494855.nvv5_v710_linux_rocm_image?tab=Overview) comes preloaded with the AMD GPU driver, helping accelerate VM setup. This guide explains how to install AMD GPU drivers on Azure NVads V710-series Linux virtual machines (VMs). It covers both automated and manual installation methods specifically for **Ubuntu**.

## ROCm

Note

Currently, Azure provides installation instructions for:

- Ubuntu 22.04
- Ubuntu 24.04

For other Linux distributions, see:

- [Quick start installation guide - ROCm installation (Linux)](https://rocm.docs.amd.com/en/latest/install/rocm.html?fam=radeon&amp;w=compute&amp;gpu=amd-radeon-pro-v710&amp;os=ubuntu&amp;ubuntu-ver=24.04.4&amp;i=pkgman&amp;gfx=gfx1101)
- [ROCm release history - ROCm Documentation](https://rocm.docs.amd.com/en/latest/release/versions.html#rocm-release-history)

Install the AMD Linux Driver to leverage the full capabilities of the AMD Radeon PRO V710 GPU on an NVv5-V710 GPU Linux instance in Microsoft Azure. The sections that follow provide detailed instructions for installing the Linux driver and running inference workloads using ROCm on this instance type.

## Quick start options

### Option 1: Use the AMD GPU driver extension

The simplest method is using the AMD GPU Driver Extension, which automates driver installation for NVv710-series VMs. You can deploy this extension through:

- Azure portal
- Azure PowerShell
- Azure Resource Manager templates

### Option 2: Use pre-configured marketplace image

A marketplace image is available with pre-installed AMD GPU drivers, allowing for faster VM deployment.

### Option 3: Manual installation

Follow these instructions for manual driver installation and configuration.

## ROCm driver installation

### Prerequisites

**System requirements:**

- Disk size must exceed 64GB for optimal performance
- Supported distributions: Ubuntu 22.04 or Ubuntu 24.04
- Virtual Function Device ID: 7461 (AMD Radeon PRO V710 GPU)

### Step 1: Verify your system

Follow these steps to verify that your GPU card is detected on your system.

1. Check your Linux distribution:

    ```bash
    cat /etc/*release
    ```
2. Check your kernel version:

    ```bash
    uname -srmv
    ```

> 
> - [ROCm Compatibility Matrix - ROCm Documentation](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html?fam=radeon&amp;gpu=amd-radeon-pro-v710&amp;os=ubuntu&amp;gfx=gfx1101)
> 

1. Verify your GPU card is detected:

    ```bash
    sudo lspci -d 1002:7461
    ```

    You should see output similar to:

    ```
    c3:00.0 Display controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 7461
    ```

### Step 2: Install the driver

The driver installation commands are slightly different depending on whether you're running Ubuntu 22.04 or 24.04.

#### For Ubuntu 24.04

```bash
#Driver Installation
sudo apt update
sudo apt install -y "linux-headers-$(uname -r)" "linux-modules-extra-$(uname -r)"
sudo usermod -a -G render,video $LOGNAME

sudo mkdir --parents --mode=0755 /etc/apt/keyrings
wget https://repo.radeon.com/rocm/rocm.gpg.key -O - | \
    gpg --dearmor | sudo tee /etc/apt/keyrings/rocm.gpg > /dev/null

sudo tee /etc/apt/sources.list.d/amdgpu.list <<'EOF'
deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/amdgpu/31.50/ubuntu noble main
EOF

sudo apt update
sudo apt install -y amdgpu-dkms
sudo reboot

#ROCM Installation
wget https://stable.repo.amd.com/rocm/gpg/packages.gpg -O - | \
    gpg --dearmor | sudo tee /etc/apt/keyrings/amdrocm.gpg > /dev/null

sudo tee /etc/apt/sources.list.d/amdrocm-stable.sources > /dev/null <<'EOF'
X-Repo-Id: amdrocm-stable
Types: deb
URIs: https://stable.repo.amd.com/rocm/core/packages/ubuntu2404/
Suites: stable
Components: main
Architectures: amd64
Signed-By: /etc/apt/keyrings/amdrocm.gpg
Enabled: yes
EOF

sudo apt update
sudo apt install -y amdrocm10.0-gfx1101
Check — re-login first so the shell picks up the new tools:
rocminfo | grep gfx                # gfx1101
amd-smi version                    # ROCm 10.0.0 | amdgpu 7.1.3.31500000
```

### Step 3: Load and verify the driver

Follow these steps to load and verify the driver.

1. Load the driver:

    ```bash
    sudo modprobe amdgpu
    ```
2. Check that the driver loaded successfully:

    ```bash
    sudo dmesg | grep amdgpu
    ```
3. Verify driver status with AMD-SMI:

    ```bash
    amd-smi monitor
    ```

### Step 4: Enable automatic loading on reboot

Follow these steps to enable automatic loading on reboot.

1. Search for blocklist entries:

    ```bash
    grep amdgpu /etc/modprobe.d/* -rn
    ```
2. If the driver is blocklisted, remove the blocklist:

    ```bash
    sudo nano /etc/modprobe.d/blacklist.conf
    ```
3. Delete the line containing `blacklist amdgpu`, then update initramfs:

    ```bash
    sudo update-initramfs -uk all
    ```
4. Reboot to apply changes:

    ```bash
    sudo reboot
    ```

## Graphics and ROCm installation

This section covers installing the AMD driver for graphics workloads with ROCm libraries and development tools.

### Prerequisites

**System requirements:**

- Ubuntu 24.04 with kernel 6.8
- Disk size greater than 64GB
- Desktop environment (for graphics workloads, use Ubuntu Desktop ISO)

### Pre-installation steps

Complete the following pre-installation steps.

1. Update package list:

    ```bash
    sudo apt update
    ```
2. Install Python packages:

    ```bash
    sudo apt install python3-setuptools python3-wheel
    ```
3. Add user to required groups:

    ```bash
    sudo usermod -a -G render,video $LOGNAME
    ```
4. Install kernel headers:

    ```bash
    sudo apt install "linux-headers-$(uname -r)" "linux-modules-extra-$(uname -r)"
    ```

### Install AMD driver with graphics support

Follow these steps to install the AMD driver with graphics support.

1. Upgrade the system:

    ```bash
    sudo apt upgrade
    ```
2. Download the installer:

    ```bash
    wget https://repo.radeon.com/.hidden/4beb847a345ee8f56d60594fcd2babe1/amdgpu-install/6.4.2.2/ubuntu/noble/amdgpu-install_6.4.2.2.60402-1_all.deb
    ```
3. If a previous driver exists, remove it:

    ```bash
    sudo amdgpu-uninstall
    sudo apt remove amdgpu-install --purge
    ```
4. Install the new driver:

    ```bash
    sudo apt-get install ./amdgpu-install_6.4.2.2.60402-1_all.deb
    sudo amdgpu-setup -b https://repo.radeon.com/.hidden/4beb847a345ee8f56d60594fcd2babe1
    sudo sed -i 's|https://repo\.radeon\.com/amdgpu/6\.4\.2|https://repo.radeon.com/.hidden/4beb847a345ee8f56d60594fcd2babe1/amdgpu/6.4.2.2|' /etc/apt/sources.list.d/amdgpu-proprietary.list
    sudo gpg --keyserver keyserver.ubuntu.com --recv-keys 9386B48A1A693C5C
    sudo gpg --export --armor 9386B48A1A693C5C | sudo tee /etc/apt/trusted.gpg.d/amdgpu.asc
    sudo amdgpu-install --usecase=workstation,rocm,amf --opencl=rocr --vulkan=pro --no-32 --accept-eula
    ```
5. Load the driver:

    ```bash
    sudo modprobe amdgpu
    ```
6. Verify installation:

    ```bash
    sudo dmesg | grep amdgpu
    ```

To remove a blocklist, see Enable automatic loading on reboot.

## X11 remote server configuration

After installing the graphics driver, follow these steps to configure a virtual display with hardware acceleration for remote access.

### Step 1: Install required packages

```bash
sudo apt install net-tools
sudo apt install x11vnc
```

### Step 2: Configure GDM3

Follow these steps to configure GDM3.

1. Edit the GDM3 configuration:

    ```bash
    sudo vim /etc/gdm3/custom.conf
    ```
2. Modify to include:

    ```ini
    [daemon]
    AutomaticLoginEnable=true
    AutomaticLogin=your_username
    WaylandEnable=false
    ```
3. Restart GDM3:

    ```bash
    sudo systemctl restart gdm3
    ```

### Step 3: Configure X11

Follow these steps to configure X11.

1. Get your GPU's Bus ID:

    ```bash
    lspci -d 1002: | awk '{print $1}'
    ```
2. Convert the hex Bus ID to decimal format. For example, `3a9e:00:00.0` becomes `3841536`.
3. Edit the X configuration file `/usr/share/X11/xorg.conf.d/00-amdgpu.conf`:

    ```
    Section "Device"
        Identifier "Card0"
        Driver "amdgpu"
        BusID "PCI:3841536:0:0"
    EndSection
    
    Section "Screen"
        Identifier "Screen0"
        Device "Card0"
        Monitor "Monitor0"
    EndSection
    ```
4. Edit `/usr/share/X11/xorg.conf.d/10-amdgpu.conf`:

    ```
    Section "OutputClass"
        Identifier "Card0"
        MatchDriver "amdgpu"
        Driver "amdgpu"
        Option "PrimaryGPU" "yes"
    EndSection
    ```
5. Reboot and load the driver:

    ```bash
    sudo reboot
    ```
6. After reboot, run the following commands:

    ```bash
    sudo systemctl stop gdm
    sudo modprobe amdgpu
    sudo systemctl start gdm
    ```

### Step 4: Start VNC server

To start the server, run the following command.

```bash
x11vnc --forever -find
```

Note

X11 configuration only works with Ubuntu Desktop images, not Server images.

## Troubleshooting

### Downgrade to kernel 6.8

You can downgrade to 6.8 for compatibility by following these steps.

1. Check loaded kernels:

    ```bash
    dpkg --list | egrep -i --color 'linux-image|linux-headers|linux-modules' | awk '{ print $2 }'
    ```
2. Install kernel 6.8:

    ```bash
    sudo apt install linux-image-6.8.0-1025-azure
    ```
3. Edit GRUB:

    ```bash
    sudo vim /etc/default/grub
    ```
4. Set kernel 6.8 as default:

    ```
    GRUB_DEFAULT="Advanced options for Ubuntu>Ubuntu, with Linux 6.8.0-1025-azure"
    ```
5. Update GRUB and reboot:

    ```bash
    sudo update-grub
    sudo reboot
    ```
6. Verify kernel version:

    ```bash
    uname -a
    ```
7. Remove kernel references to 6.17:

    ```bash
    sudo apt purge linux-headers-6.17.0-1011-azure linux-image-6.17.0-1011-azure linux-modules-6.17.0-1011-azure linux-modules-extra-6.17.0-1011-azure
    ```

## Uninstalling the ROCM & AMD GPU driver

To completely remove the AMD GPU driver, run the following commands:

```bash
dkms status
sudo amdgpu-install --uninstall
sudo amdgpu-uninstall
sudo apt autoremove --purge amdgpu-install
sudo reboot
```

Verify removal:

```bash
dkms status
```

Remove ROCm repositories.

Remove ROCm repositories

```bash
sudo rm -f /etc/apt/sources.list.d/amdrocm-stable.sources
```

Clear the cache and clean the system

```bash
sudo rm -rf /var/cache/apt/*
sudo apt clean all
sudo apt update
```