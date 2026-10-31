---
layout: Conceptual
title: Install the AIPService PowerShell module for the Azure Rights Management service from Microsoft Purview Information Protection | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/install-aipservice-powershell
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
ms.reviewer: tommoser
manager: laurawi
ms.date: 2026-08-26T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-encryption
ms.collection:
- purview-compliance
description: Instructions to install PowerShell for the Azure Rights Management service from Microsoft Purview Information Protection. The name of this module is AIPService.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 21ec90db-397e-54f4-d17a-cbf2691ef1f5
document_version_independent_id: 21ec90db-397e-54f4-d17a-cbf2691ef1f5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/install-aipservice-powershell.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: install-aipservice-powershell
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/install-aipservice-powershell.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7696cda6-0510-47f6-8302-71bb5d2e28cf
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/69c76c32-967e-4c65-b89a-74cc527db725
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 0a5de073-2eef-3d26-58aa-c48175a1763d
---

# Install the AIPService PowerShell module for the Azure Rights Management service from Microsoft Purview Information Protection | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use the following information to help you install the PowerShell module for the Azure Right Management encryption service from Microsoft Purview Information Protection. The name of this module is AIPService, and it replaces the previous version that was named AADRM.

You can use this PowerShell module to administer the Azure Rights Management encryption service from the command line by using any Windows computer that has an internet connection and that meets the prerequisites listed in the following table. PowerShell for the Azure Rights Management service supports scripting for automation or might be necessary for advanced configuration scenarios. For more information about the administration tasks and configurations that the AIPService module supports, see [Administering the Azure Rights Management service by using PowerShell](administer-rights-management-powershell).

## Prerequisites

This table lists the prerequisites to install and use the AIPService PowerShell module for the Azure Rights Management encryption service.

| Requirement | More information |
| --- | --- |
| **Supported PowerShell versions** | Windows PowerShell 5.1, or PowerShell 7.4 and later. You can confirm the version you're running by typing `$PSVersionTable` in a PowerShell session. The `PSEdition` property shows `Desktop` for Windows PowerShell and `Core` for PowerShell 7. To install PowerShell 7, see [Installing PowerShell on Windows](/en-us/powershell/scripting/install/installing-powershell-on-windows).  PowerShell 7 requires AIPService version 3.1.0.0 or later. Earlier versions of the module support Windows PowerShell only. |
| **Minimum .NET version** | Windows PowerShell 5.1 requires Microsoft .NET Framework 4.8. This minimum version of the Microsoft .NET Framework is included with the later operating systems but if it's not already installed, you can download [Microsoft .NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48). This minimum version of the Microsoft .NET Framework is required for some of the classes that the AIPService module uses. PowerShell 7.4 and later includes the .NET version that the module requires, so no separate installation is needed. |
| **Required license** | You must have a product license to use this feature. For more information, see [Microsoft 365 licensing guidance for security & compliance - Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance#information-protection). |

## PowerShell editions

AIPService version 3.1.0.0 supports both PowerShell editions on Windows from a single package:

| Edition | Host | Runtime |
| --- | --- | --- |
| Desktop | Windows PowerShell 5.1 | .NET Framework 4.8 |
| Core | PowerShell 7.4 and later | .NET 8 |

The module selects the correct edition automatically when you import it, so the same `Install-Module` command works in both hosts. Cmdlet names, parameters, and output are the same in both editions.

Interactive sign-in differs between the two editions. Windows PowerShell 5.1 signs in through an embedded web view, while PowerShell 7 uses your default web browser and a local loopback address. On a computer with no default browser available, such as a Server Core installation, or in a remote session, use certificate-based or service principal authentication instead. For more information, see [Connect-AipService](/en-us/powershell/module/aipservice/connect-aipservice).

To confirm which editions your installed version supports, run:

```PowerShell
(Get-Module AIPService -ListAvailable).CompatiblePSEditions
```

## If you have the AADRM module installed

The AIPService module replaces the older module, AADRM. If you have the older module installed, uninstall it and then install the AIPService module.

The AIPService module has aliases to the cmdlet names in the AADRM module so that any existing scripts will continue to work. The AADRM module fell out of support on July 15, 2020.

If you installed the AADRM module from the PowerShell Gallery, to uninstall it, start a PowerShell session with the **Run as Administrator** option, and type:

```PowerShell
Uninstall-Module -Name AADRM
```

If you installed the AADRM module with the Azure Rights Management Administration Tool, use your Windows remove applications procedures to uninstall **Windows Azure AD Rights Management Administration**.

## How to install the AIPService module

The AIPService module is on the [PowerShell Gallery](https://www.powershellgallery.com/) and is not available from the Microsoft Download Center.

### To install the AIPService module from the PowerShell Gallery

If you're new to the PowerShell Gallery, see [Get Started with the PowerShell Gallery](/en-us/powershell/scripting/gallery/getting-started). Follow the PowerShell Gallery setup instructions, including installing the PowerShellGet module and the NuGet provider.

To see details about the AIPService module on the PowerShell Gallery, visit the [AIPService package in PowerShell Gallery](https://www.powershellgallery.com/packages/AIPService).

To install the AIPService module, start a PowerShell session with the **Run as Administrator** option, and type:

```PowerShell
Install-Module -Name AIPService
```

If you are warned about installing from an untrusted repository, you can press Y to confirm. Or, press N and configure the PowerShell Gallery as a trusted repository by using the command `Set-PSRepository -Name PSGallery -InstallationPolicy Trusted` and then rerun the command to install the AIPService module.

If you have a previous version of the AIPService module installed from the Gallery, update it to the latest by typing:

```PowerShell
Update-Module -Name AIPService
```

Note

To use the module in PowerShell 7, run `Install-Module -Name AIPService` from a PowerShell 7 session. Windows PowerShell and PowerShell 7 use separate per-user module folders, so a module that was installed for the current user in Windows PowerShell isn't available in PowerShell 7.