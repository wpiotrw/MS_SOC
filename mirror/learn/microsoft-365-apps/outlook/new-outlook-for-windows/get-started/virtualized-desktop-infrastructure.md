---
layout: Conceptual
title: Deploy the New Outlook for Windows on VDI | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365-apps/outlook/get-started/virtualized-desktop-infrastructure
breadcrumb_path: /microsoft-365-apps/outlook/breadcrumb/m365-apps-outlook/toc.json
feedback_system: Standard
permissioned-type: public
uhfHeaderId: MSDocsHeader-Outlook
ms.service: outlook
author: Cloud-Writer
ms.author: meerak
manager: dcscontentpm
audience: ITPro
ms.topic: overview
ms.collection:
- Tier3
- virtualized-desktop-infrastructure.md
ms.localizationpriority: medium
ms.custom: intro-overview
ms.reviewer: jhollander
recommendations: true
description: Provides an overview of the new Outlook for Windows for VDI
ms.date: 2026-04-14T00:00:00.0000000Z
locale: en-us
document_id: c39a98d5-3d93-81ac-695e-b6de76fbb91f
document_version_independent_id: 8ab5f770-ab4a-d50a-9cfb-68c106ea064f
original_content_git_url: https://github.com/MicrosoftDocs/outlook-pr/blob/live/outlook/new-outlook-for-windows/get-started/virtualized-desktop-infrastructure.md
site_name: Docs
depot_name: Learn.m365-apps-outlook
page_type: conceptual
toc_rel: ../new-windows-toc/toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: get-started/virtualized-desktop-infrastructure
moniker_range_name: 
monikers: []
item_type: Content
source_path: outlook/new-outlook-for-windows/get-started/virtualized-desktop-infrastructure.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: e0fb6a85-fd3d-9848-4ec2-9c674acb2a8a
---

# Deploy the New Outlook for Windows on VDI | Microsoft Learn

This article outlines the requirements, limitations, and deployment guidance for using the new Outlook for Windows in Virtualized Desktop Infrastructure (VDI) environments.

## Requirements

| Requirement | Version |
| --- | --- |
| **Windows** | - Windows 10.0.19041.0 (2004) or later - Windows Server 2022 (20348.2402) or later |
| **WebView2** | Update to the latest version. For more information, see [Enterprise management of WebView2 Runtimes](/en-us/microsoft-edge/webview2/concepts/enterprise). |
| **.NET Framework** | 4.7.2 or later |

Note

Windows Server 2019 and Windows Server 2016 are not supported.

## Virtualization Provider Requirements

The following sections outline the requirements for virtualization providers that support the new Outlook for Windows.

### Azure Virtual Desktop and Windows 365

The following minimum versions are required for the new Outlook for Windows:

- Windows App on Windows: 2.0.285.0
- Windows App on macOS: 11.0.0

### Citrix Virtual Apps and Desktops and Citrix DaaS Requirements

The following sections describe the requirements for Citrix Workspace App and Citrix Virtual Delivery Agent (VDA) to support the new Outlook for Windows.

#### Citrix Workspace App

- Windows 2203 LTSR (and any CU)
- Windows 2302 CR

#### Citrix Virtual Delivery Agent (VDA)

- 2203 LTSR (and any CU)
- 2212 CR
- 1912 CU6 (latest CU recommended; note that App Sharing is not supported on 1912)

### VMware Horizon and Workspace ONE Requirements

The following minimum version is required for the new Outlook for Windows:

- Horizon 8 2111 ESB (8.4)

## Deploy the New Outlook for Windows

Note

The new Outlook for Windows is installed as part of Windows, starting with Windows 11, version 24H2.

To deploy the new Outlook for Windows:

1. Download the `.exe` installer.
2. Use a distribution method such as Intune, Microsoft Endpoint Configuration Manager, Group Policy, or a non-Microsoft tool to distribute the installer.
3. Run the installer on each computer.

For detailed instructions, see [Deploy New Outlook](/en-us/microsoft-365-apps/outlook/get-started/deployment-new-outlook).

Note

If **AllowAllTrustedApps** is disabled, the new Outlook app installation fails. This issue was fixed in the October cumulative update KB5031455 for [Windows 11](https://support.microsoft.com/topic/october-31-2023-kb5031455-os-builds-22621-2506-and-22631-2506-preview-6513c5ec-c5a2-4aaf-97f5-44c13d29e0d4) and [Windows 10](https://support.microsoft.com/topic/october-26-2023-kb5031445-os-build-19045-3636-preview-03f350cb-57f9-45e6-bfd7-438895d3c7fa). If this update is unavailable, the November security update includes the fix.

For more information, see [Installation issues due to policy restrictions](../troubleshoot/troubleshoot-deployment-new-outlook#installation-issues-due-to-policy-restrictions).

## Disk Footprint - Key Folders and Location

### Install Location

The MSIX installer installs the new Outlook app in the WindowsApps folder. This location provides enhanced protection against attacks that attempt to alter the Outlook app installation.

The folder name where the new Outlook app is installed changes with each version update. It starts with ***Microsoft.OutlookForWindows*\_**, ends with **\_*8wekyb3d8bbwe***, and includes the version number and machine architecture. For example: ***Microsoft.OutlookForWindows\_1.2024.717.400\_x64\_8wekyb3d8bbwe***.

To find the current version's install location, run the following PowerShell command:

```powershell
(get-appxpackage Microsoft.OutlookForWindows).InstallLocation
```

Note

The MSIX installer and all files in the directory are signed with a Microsoft certificate.

### Profile and Cache Locations for the New Outlook for Windows

All user settings and configurations are stored in:

- `C:\Users\<username>\AppData\Local\Packages\Microsoft.OutlookForWindows_8wekyb3d8bbwe\`
- `C:\Users\<username>\AppData\Local\Microsoft\olk\`

## Folder Exclusions for Roaming

### Recommended for Exclusion

| **Folder** | **Folder Path** | **Purpose** | **Exclusion Impact** |
| --- | --- | --- | --- |
| Logs and Telemetry Cache | `%LocalAppData%/Microsoft/olk/logs``%LocalAppData%/Microsoft/olk/cache` | Diagnostics and performance logs. | No effect. |
| WebStorage | `%LocalAppData%/Microsoft/olk/EbWebView/default/WebStorage` | Cache for web app usage in iframes. | Slower app reload. |

### Considerations for Exclusion

| **Folder** | **Folder Path** | **Purpose** | **Exclusion Impact** |
| --- | --- | --- | --- |
| Service Worker | `%LocalAppData%/Microsoft/olk/EBWebView/default/Service Worker/CacheStorage``%LocalAppData%/Microsoft/olk/EBWebView/default/Code Cache` | Stores cached web/JS scripts. | Slower app launches due to redownload of scripts. |
| IndexedDB and Local Storage | `%LocalAppData%/Microsoft/olk/EBWebView/default/IndexedDB``%LocalAppData%\Microsoft\olk\EBWebView\Default\Local Storage``%LocalAppData%/Microsoft/olk/Attachments` | Stores user and app data. | Increased app launch time and repeated sign-ins. |
| Cache | `%LocalAppData%/Microsoft/olk/EBWebView/default/Cache` | Caches network call contents. | Resources need to be redownloaded. |

Other than the folders in this section, avoid excluding extra directories.