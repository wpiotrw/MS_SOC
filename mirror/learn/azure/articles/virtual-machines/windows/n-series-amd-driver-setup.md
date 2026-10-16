---
layout: Conceptual
title: Azure N-series AMD GPU driver setup for Windows - Azure Virtual Machines | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-machines/windows/n-series-amd-driver-setup
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
author: magatala-MSFT
learn_banner_products:
- azure-virtual-machines
manager: jkabat
ms.reviewer: wwilliams
ms.author: v-nmagatala
ms.update-cycle: 365-days
description: How to set up AMD GPU drivers for N-series VMs running Windows Server or Windows in Azure
ms.service: azure-virtual-machines
ms.subservice: sizes
ms.collection: windows
ms.topic: how-to
ms.date: 2025-05-05T00:00:00.0000000Z
locale: en-us
document_id: b614e743-5405-47cd-ee21-b442b4acb44d
document_version_independent_id: 3aecf729-8f36-6e60-be76-b740df7aa7a6
original_content_git_url: https://github.com/MicrosoftDocs/azure-compute-docs-pr/blob/live/articles/virtual-machines/windows/n-series-amd-driver-setup.md
site_name: Docs
depot_name: Learn.azure-compute
page_type: conceptual
toc_rel: ../toc.json
asset_id: virtual-machines/windows/n-series-amd-driver-setup
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/virtual-machines/windows/n-series-amd-driver-setup.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/19ec6774-09b8-473e-a17e-b17b518bbad7
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ade36b61-c646-4bd8-87ee-f3a843461962
platformId: 5e645676-50b0-ed58-0ffb-9b3ebd4106bd
---

# Azure N-series AMD GPU driver setup for Windows - Azure Virtual Machines | Microsoft Learn

**Applies to:** Windows VMs ✔️ Flexible scale sets

Note

The [AMD GPU Driver Extension](../extensions/hpccompute-amd-gpu-windows) installs AMD GPU drivers on a NVads V710 v5 Series, NGads V620 Series and NVv4-series. Install or manage the extension using the Azure portal or tools such as Azure PowerShell or Azure Resource Manager templates. See the [AMD GPU Driver Extension documentation](../extensions/hpccompute-amd-gpu-windows) for supported operating systems and deployment steps.

## NVads V710 v5 Series

To take advantage of the GPU capabilities of the new Azure NVads V710 v5 series VMs running Windows, AMD GPU drivers must be installed. The [AMD GPU Driver Extension](../extensions/hpccompute-amd-gpu-windows) installs AMD GPU drivers on a NVads V710 v5-series VM. Install or manage the extension using the Azure portal or tools such as Azure PowerShell or Azure Resource Manager templates. See the [AMD GPU Driver Extension documentation](../extensions/hpccompute-amd-gpu-windows) for supported operating systems and deployment steps.

If you choose to install AMD GPU drivers manually, this article provides supported operating systems, drivers, and installation and verification steps.

Only GPU drivers published by Microsoft are supported on NVads V710 v5 series VMs. Don't install GPU drivers from any other source.

For basic specs, storage capacities, and disk details, see [GPU Windows VM sizes](../sizes-gpu?toc=/azure/virtual-machines/windows/toc.json).

| OS | Driver |
| --- | --- |
| Windows 11 23H2, 24H2, 25h2 | [25.Q4](https://download.microsoft.com/download/04605f8a-4b3e-4e08-9f88-b5b7d55d8cb5/v710-win11.exe) (.exe) |
| Windows Server 2025 24H2, Windows 11 EMS 23H2, 24H2, 25H2 | [25.Q4](https://download.microsoft.com/download/68cc41fd-fe9d-47ac-98ec-c9a921a11397/v710-winsvr2025.exe) (.exe) |
| Windows Server 2022 21H2 | [25.Q4](https://download.microsoft.com/download/8eb8c91e-6c08-4c76-99a9-042bb84a7e86/v710-winsvr2022.exe) (.exe) |

### VM Creation

Create the VMs using CLI. (Azure AMD GPU driver extensions don't support NVads V710 v5 Series during preview)

- Review the [CLI VM creation documentation](/en-us/azure/virtual-machines/windows/quick-create-cli).

### Driver installation

1. Connect by Remote Desktop to each NVads V710 v5-series VM.
2. Download the EXE file to a local drive.
3. If you need to uninstall the previous driver version, run "setup.exe -factoryresetinstall" from a command line.
4. For a first-time driver installation, double-click or run “setup.exe” from a command line.
5. Reboot the VM.

### Verify driver installation

You can verify driver installation in Device Manager. The following example shows successful configuration of the Radeon Pro V710 card on an NVads V710 v5 VM. The exact driver date and version will depend on the driver package released.

![Diagram that shows successful configuration of the Radeon Pro V710 card on an Azure NVads V710 v5 VM.](media/n-series-amd-driver-setup/v710-device-manager.jpg)

## NGads V620 Series

The AMD Software: Cloud Edition drivers must be installed to take advantage of the GPU capabilities of Azure NGads V620 Series VMs.

### Requirements

| OS | Driver |
| --- | --- |
| Windows 11 64-bit version 23H2, 24H2 | [25.1.1](https://download.microsoft.com/download/44ee0d6c-74dd-4214-b6d5-24fbf2eac33b/whql-amd-software-cloud-edition-25.1.1-win10-win11-azure-ngads-v620.exe) |
| Windows 11 EMS 64-bit 23H2, 24H2, 25H2  Windows Server 2022 21H2  Windows Server 2025 24H2 | [25.1.1](https://download.microsoft.com/download/6f834f98-109d-4dfc-89e6-d25ff02a9dd0/amd-software-cloud-edition-25.1.1-winsvr2022-azure-v620.exe) |

### VM Creation

Create the VMs using CLI. (Azure AMD GPU driver extensions don't support NGads V620 Series during preview)

1. Review the [CLI VM creation documentation](/en-us/azure/virtual-machines/windows/quick-create-cli).

### Driver installation

1. Connect by Remote Desktop to each NGads V620-series VM
2. Download the EXE file to a local drive
3. If you need to uninstall the previous driver version, run "setup.exe -factoryresetinstall" from a command line
4. For a first-time driver installation, double-click or run “setup.exe” from a command line
5. Reboot the VM

### Verify driver installation

1. You can verify driver installation in Device Manager. The following example shows successful configuration of the Radeon Pro V620 card on an Azure NGads V620 VM. The exact driver date and version will depend on the driver package released.

## NVv4 Series

To take advantage of the GPU capabilities of the new Azure NVv4 series VMs running Windows, AMD GPU drivers must be installed. The [AMD GPU Driver Extension](../extensions/hpccompute-amd-gpu-windows) installs AMD GPU drivers on a NVv4-series VM. Install or manage the extension using the Azure portal or tools such as Azure PowerShell or Azure Resource Manager templates. See the [AMD GPU Driver Extension documentation](../extensions/hpccompute-amd-gpu-windows) for supported operating systems and deployment steps.

If you choose to install AMD GPU drivers manually, this article provides supported operating systems, drivers, and installation and verification steps.

Only GPU drivers published by Microsoft are supported on NVv4 VMs. Don't install GPU drivers from any other source.

For basic specs, storage capacities, and disk details, see [GPU Windows VM sizes](../sizes-gpu?toc=/azure/virtual-machines/windows/toc.json).

### Supported operating systems and drivers

| OS | Driver |
| --- | --- |
| Windows 11 64-bit 24H2 | [26.Q3 MR 5](https://download.microsoft.com/download/e8798d81-12a2-42f6-9ae4-75d2e3d8e5f9/59578_Azure_NVv4_MI25_MR5-Win1064_Guest_Driver.zip) (.exe) |
| Windows Server 2022 | [26.Q3 MR 5](https://download.microsoft.com/download/830fc008-082c-4290-8bc2-bb0fa89a81bf/59578_Azure_NVv4_MI25_MR5-Win2022_Guest_Driver.zip) (.exe) |
| Windows Server 2019 | [26.Q3 MR 5](https://download.microsoft.com/download/ea9ba719-8c20-4e0c-b4f5-ebf3237a984e/59578_Azure_NVv4_MI25_MR5-Win2019_Guest_Driver.zip) (.exe) |

Previous supported driver versions for Windows builds up to 1909 are [20.Q4-1](https://download.microsoft.com/download/0/e/6/0e611412-093f-40b8-8bf9-794a1623b2be/AMD-Azure-NVv4-Driver-20Q4-1.exe) (.exe) and [21.Q2-1](https://download.microsoft.com/download/4/e/a/4ea28d3f-28e2-4eaa-8ef2-4f7d32882a0b/AMD-Azure-NVv4-Driver-21Q2-1.exe) (.exe)

Note

If you use build 1903/1909 then you may need to update the following group policy for optimal performance. These changes are not needed for any other Windows builds.

> 
> [Computer Configuration-&gt;Policies-&gt;Windows Settings-&gt;Administrative Templates-&gt;Windows Components-&gt;Remote Desktop Services-&gt;Remote Desktop Session Host-&gt;Remote Session Environment], set the Policy [Use WDDM graphics display driver for Remote Desktop Connections] to Disabled.

### Driver installation

1. Connect by Remote Desktop to each NVv4-series VM.
2. If you need to uninstall the previous driver version, download the [AMD cleanup utility](https://download.microsoft.com/download/4/f/1/4f19b714-9304-410f-9c64-826404e07857/AMDCleanupUtilityni.exe). Don't use the utility that comes with the previous version of the driver.
3. Download and install the latest driver.
4. Reboot the VM.

### Verify driver installation

1. You can verify driver installation in Device Manager. The following example shows successful configuration of the Radeon Instinct MI25 card on an Azure NVv4 VM.

![Screenshot that shows successful configuration of the Radeon Instinct MI25 card on an Azure NVv4 VM.](media/n-series-amd-driver-setup/device-manager.png)

1. You can use dxdiag to verify the GPU display properties including the video RAM. The following example shows a 1/2 partition of the Radeon Instinct MI25 card on an Azure NVv4 VM. ![Screenshot that shows a 1/2 partition of the Radeon Instinct MI25 card on an Azure NVv4 VM.](media/n-series-amd-driver-setup/dxdiag-output-new.png)
2. If you're running Windows 10 build 1903 or higher, dxdiag shows no information in the 'Display' tab. Use the 'Save All Information' option at the bottom and the output file shows the information related to AMD MI25 GPU.

![GPU driver properties](media/n-series-amd-driver-setup/dxdiag-details.png)

## Note for Windows EMS installation

Note

Follow these steps if you see "Error 184 - AMD Installer cannot continue due to an unsupported Operating System" error on Windows 10 EMS or Windows 11 EMS.

1. Make sure you extract the driver package. For an EXE package, run it to extract its content.
2. Locate the `display-driver` folder in the extracted package. Example path: `C:\AMD\AMD-Software-Installer\Packages\Drivers\Display\WT6A_INF`.
3. Right-click the applicable `.inf` file and select **Install**, then restart the VM.