---
layout: Conceptual
title: Device images in Windows 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/device-images
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn about device images in Windows 365.
keywords: 
author: astrader1
ms.author: astrader
manager: dougeby
ms.date: 2024-09-09T00:00:00.0000000Z
ms.topic: overview
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: shikhakhetan
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: 49447e0f-26ae-8d9b-59a9-16e2454e658d
document_version_independent_id: 49447e0f-26ae-8d9b-59a9-16e2454e658d
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/device-images.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/device-images
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/device-images.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 6369f81e-df0d-ba40-4d81-4e98cf1ab7be
---

# Device images in Windows 365 | Microsoft Learn

Windows 365 uses both default and custom operating system images to automatically create the virtual Cloud PCs that you provide to your end users. The default images are available from the gallery in Microsoft Intune as a part of creating your provisioning policy. You can also [upload custom images](add-device-images) that you create.

## Image requirements

Both marketplace and custom images must meet the following requirements:

- Supported versions of Windows 10 or Windows 11 Enterprise.
- Generation 2 images.

    Note

    We recently made the change to **generation 2** (Gen2) virtual machine images. Newly created custom images must be Gen2. Existing custom images uploaded based on generation 1 will remain active.
- The image must never have been Active Directory, Microsoft Entra ID joined, Intune-enrolled, or enrolled for co-management. For more information, see [Sysprep won't run correctly on a device that has been MDM enrolled](/en-us/troubleshoot/mem/intune/device-enrollment/troubleshoot-sysprep-windows-10-device-enrolled-mdm).
- Generalized VM image.
- Single Session VM images (multi-session isn’t supported).
- No recovery partition. For information about how to remove a recovery partition, see the [Windows Server command: delete partition](/en-us/windows-server/administration/windows-commands/delete-partition).
- Default 64-GB OS disk size. The OS disk size is automatically adjusted to the size specified in SKU description of the Windows 365 license.
- Data disks can't be attached to the VM prior to capturing the image.
- Cannot contain FSLogix components.
- Cannot contain more than 3,000 apps in the Start menu.

A custom image must also meet the following extra requirements:

- Exist in an Azure subscription.
- Is stored as a [managed image](/en-us/azure/virtual-machines/capture-image-resource) in Azure or in an Azure Compute Gallery (with security type set to Trusted Launch)

Note

Some editions of the Windows operating system, like N or long term service channel (LTSC) editions, aren't supported. For best results when you create a custom image, use one of the Cloud PC gallery images as a starting template.

Storing a managed image on Azure incurs storage costs. However, customers can delete the managed image from Azure once they've successfully uploaded it as a Custom Image to Microsoft Intune.

## Gallery images

Windows 365 provides a built-in gallery of Windows Enterprise images accessible through the [provisioning policy creation flow](create-provisioning-policy). Each image helps admins with preset audit policies already enabled, like account policies, logon/logoff, object access, and policy change. These images are harmonized in GPOs. Any differences are due to preinstalled apps.

They're replicated to all Azure regions to give you a quick provisioning experience. These images are updated monthly with:

- Optimizations for improved user experience.
- The latest security updates so that end users have a secure and seamless experience.

There are three sets of images available to choose from across the different versions of Windows Enterprise:

**Images with pre-installed Microsoft 365 Apps**: Microsoft 365 Apps and Teams optimizations are already installed. The following settings are preapplied:

- IsWVDEnvironment reg key (Teams).
- C++ Runtime (Teams).
- WebRTC Redirector (Teams).
- Microsoft Teams (Teams).
- Microsoft Edge settings like sleeping tabs, [forced browser sign-in](/en-us/deployedge/microsoft-edge-policies#browsersignin), startup boost, and first time optimizations based on Microsoft Entra ID and synchronization. For more information, see [Configure Microsoft Edge policy settings with Microsoft Intune](/en-us/deployedge/configure-edge-with-intune).
- Microsoft Outlook first-time configuration settings (auto log on based on Microsoft Entra profile, support for other profiles).

**Images with no preinstalled applications**: A plain image without any preinstalled applications (look for images without the **M365 Apps** in the name).

**Image with Developer Configuration with pre-installed Microsoft 365 Apps:** This image provides a consistent, ready-to-use developer environment by preinstalling essential development tools and applying the required configurations across Windows 365 CPC. The image is optimized for developers across both Windows and Linux workflows. By standardizing the image with the necessary tooling and setup, this approach reduces onboarding time, minimizes manual configuration, and ensures a reliable and productive developer experience from first sign-in. The image includes:

- Windows configuration and settings via registry.
- Desktop configuration settings
- File Explorer settings
- Taskbar settings
- Search and Start settings
- Service/features settings
- Install and set up Windows Subsystem for Linux (WSL) with a WSL Ubuntu
- A bash script to configure the user environment in WSL Ubuntu
- Installation of the same developer tools within the WSL environment
- If an uninstall of the 3rd-party dev tools is desired, [this script](https://github.com/microsoft/Windows365-PSScripts/tree/main/DevReadyImage-Uninstaller) can be used to uninstall them.
- Developer tools installation, including PowerShell 7, Visual Studio Code (with extensions ms-vscode.powershell, ms-python.python, ms-vscode-remote.remote-wsl, github.vscode-pull-request-github, ms-edgedevtools.vscode-edge-devtools, and mspythondeprem.python-dependency-remediation), PowerToys, Python, Node.js, npm, nvm, git, GitHub, GitHub Copilot CLI (with Work IQ and Windows Dev Skills), Oh My Posh, UV tools, Azure CLI, .NET Runtime, .NET SDK, Intelligent Terminal, Coreutils, and WinApp CLI. The versions of each tool available in the image is below:

| # | Tool Name | Current Version |
| --- | --- | --- |
| 1 | PowerShell7 | 7.6.5 |
| 2 | Visual Studio Code | 1.134.0 |
| 3 | Visual Studio Code Extensions for All Users | -- |
|  | ms-vscode.powershell | 2025.4.0 |
|  | ms-python.python | 2026.4.0 |
|  | ms-vscode-remote.remote-wsl | 0.104.3 |
|  | github.vscode-pill-request-github | 0.162.0 |
|  | ms-edgedevtools.vscode-edge-devtools | 2.1.10 |
|  | mspythondeprem.python-dependency-remediation | 1.2.3 |
| 4 | PowerToys | 0.101.2362.0 |
| 5 | Python | 3.14.7150.0 |
| 6 | Node.js | 24.19.0 |
| 7 | npm | 11.17.0 |
| 8 | nvm | 1.2.2 |
| 9 | git | 2.55.0.windows.3 |
| 10 | GitHub (gh) | 2.98.0 |
| 11 | GitHub Copilot CLI | 2.98.0 |
| 12 | Work IQ (GitHub Copilot CLI Plugin) | V2.0.2 |
| 13 | Oh my posh | 30.7.0 |
| 14 | UV tools | 0.12.5 (210d1f678 2026-08-14 x86\_64-pc-windows-msvc) |
| 15 | Azure CLI | 2.89.1 |
| 16 | .NET Runtime | Microsoft.AspNetCore.App 10.0.11 |
| 17 | .NET SDK | 10.0.400 |
| 18 | Unix Core Utils | 0.8.0 |
| 19 | WinAppCLI | 0.6.1 |
| 20 | Windows Dev Skill (GitHub Copilot CLI Plugin) | v0.5.0 |
| 21 | Intelligent Terminal | 0.2.2192.0 |

Note

1. This image is available for Windows 365 Enterprise and Windows 365 Flex Dedicated mode.
2. Customers are responsible for managing and maintaining third-party applications installed on the VM image, including monitoring for vulnerabilities, applying security updates, configuring settings, and ensuring compliance with organizational security and compliance requirements.
3. Preinstalled third-party applications included in the image are not currently manageable through Intune as packaged applications. Customers who require Intune-based application lifecycle management should uninstall the preinstalled applications and redeploy them through Intune.
4. This image is not supported on 2 vCPU or GPU licenses because they do not support nested virtualization.

### Gallery image update cycle

All supported Windows 365 gallery images are updated monthly after the security patch release schedule of Windows Servicing & Delivery. This update happens around the middle of each month. Updated Windows 365 images are made available in Intune for provisioning around the end of the third week of the month.

Each updated image includes:

- [Windows 10/11 monthly image updates](https://support.microsoft.com/topic/windows-10-release-on-azure-marketplace-update-history-da826e21-45ae-f6b9-de71-5f0ee2ec1563)
- [Microsoft 365 Apps security updates](/en-us/officeupdates/microsoft365-apps-security-updates) and [feature updates](/en-us/officeupdates/monthly-enterprise-channel)
    - Windows 365 gallery images include the latest Monthly Enterprise Channel release with the latest security updates.
- [Microsoft Teams updates](https://support.microsoft.com/office/what-s-new-in-microsoft-teams-d7092a6d-c896-424c-b362-a472d5f105de)
- [WebRTC redirector service updates](/en-us/azure/virtual-desktop/teams-on-avd#install-the-teams-websocket-service)

Applications that come pre-installed are the latest version that is available at the start of the second Tuesday of that month. Any app updates posted on that day are included in the image update of the subsequent month.

Newly provisioned Cloud PCs are automatically created with the latest images. For existing Cloud PCs, you can receive the updates by reprovisioning.

## Custom images

If none of the default gallery images meet your requirements, you can upload up to 20 of your own custom device images.

For more information on creating such a custom image, see [Create a managed image of a generalized VM in Azure](/en-us/azure/virtual-machines/windows/capture-image-resource).

A custom image can be created using [any of the images mentioned previously as a starting point](https://azuremarketplace.microsoft.com/marketplace/apps/microsoftwindowsdesktop.windows-ent-cpc). For example, you can start with one of those images and then install more applications and make more configuration changes.

Note

For custom images with Teams application, follow the instructions detailed in [Create a Cloud PC custom image that supports Microsoft Teams](create-custom-image-support-teams) to configure optimizations that are needed. Images with disk encryption sets aren't supported.

For more information about adding a device image to Windows 365, see [Add and delete custom device images](add-device-images).

When you upload a custom device image, Windows 365:

1. Copies the image to a temporary subscription.
2. Runs the following validation checks on the image:
    1. Verifies all the Windows 365 image requirements are met.
    2. Deploys a virtual machine and makes sure that the images can be booted and provisioned as a Cloud PC.
3. If you have a Microsoft Entra hybrid join connection, Windows 365 replicates the image across all Azure regions where you have an Azure network connection.
4. If you have a Microsoft Entra join connection, Windows 365 replicates the image to the provisioned region during provisioning.