---
layout: Conceptual
title: Configure Windows App Updates on Windows - Windows App | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-app/configure-updates-windows
breadcrumb_path: /windows-app/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
uhfHeaderId: MSDocsHeader-Windows-App
manager: eliotgra
ms.service: windows-app
search.audiencetype: EndUser
description: Learn how to configure Windows App update behavior on Windows, including automatic updates and registry settings.
ms.topic: how-to
ai-usage: ai-assisted
ms.author: hilarybraun
author: hilarybr
ms.date: 2025-07-02T00:00:00.0000000Z
locale: en-us
document_id: 008a201a-68de-314e-ff7b-302269bda075
document_version_independent_id: 008a201a-68de-314e-ff7b-302269bda075
original_content_git_url: https://github.com/MicrosoftDocs/windows-app-pr/blob/live/windows-app/configure-updates-windows.md
site_name: Docs
depot_name: MSDN.windows-app
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: configure-updates-windows
moniker_range_name: 
monikers: []
item_type: Content
source_path: windows-app/configure-updates-windows.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/cd440f3c-1b78-40a7-97ba-aa00a1d79df7
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c828f7e0-89b4-459c-9bae-d7ab1c4bd9ad
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 82b99a41-9448-d8ed-9d73-a9adc7b72bab
---

# Configure Windows App Updates on Windows - Windows App | Microsoft Learn

Windows App on Windows comes with an update mechanism that ensures you have the latest features and security updates. When there are updates available to install for Windows App on Windows, the update mechanism depends on whether you installed it from the Microsoft Store or by from the standalone MSIX package. The update behavior works as follows:

- **Microsoft Store**: Updates are delivered from the Microsoft Store and aren't disruptive. There's also a background task that checks for updates every 8 hours and only installs the update when Windows App is closed.
- **Standalone MSIX package**: Updates are delivered from a Content Delivery Network (CDN) by default. Users can still manually update Windows App from the Microsoft Store. There's a background task that checks for updates every 8 hours and only when Windows App is closed.

You can configure the update behavior of Windows App on Windows by setting a registry value. This setting enables you to control whether automatic updates are enabled or disabled. If updates are enabled, you can also specify whether they come from the Microsoft Store only, from a CDN location only, or both.

If you install Windows App from the standalone MSIX package, you can disable automatic updates and users don't receive update notifications in Windows App. However, users can still manually update Windows App from the Microsoft Store, even if it was installed using the standalone MSIX package. You can't disable automatic updates in Windows App if it was originally installed from the Microsoft Store; it follows the Microsoft Store update settings.

Warning

Microsoft doesn't recommend that you disable automatic updates in Windows App. If you disable automatic updates, your organization is taking on responsibility to keep the Windows App up to date. Windows App updates contain security fixes in addition to performance and stability enhancements and new features. An out of date version of Windows App can expose your organization to significant security risk.

To preserve the integrity, security, and availability of services, we reserve the right to prevent outdated client versions from connecting to the services.

## Prerequisites

Before you begin, you need to meet the following prerequisites:

- Install Windows App from the Microsoft Store or from the [standalone MSIX package](/en-us/windows-app/whats-new?tabs=windows).
- Administrative permissions on the local Windows device to modify the registry.

### Configure update behavior

To configure the update behavior in Windows App on Windows, set one of the following registry values on the local Windows device:

- **Key**: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsApp`
- **Type**: `REG_DWORD`
- **Name**: `DisableAutomaticUpdates`
- **Data**:

    - `0`: Enables updates *(default value)*
    - `1`: Disable updates from all locations
    - `2`: Disable updates from the Microsoft Store
    - `3`: Disable updates from the CDN location

    Setting the key with a value of `2` or `3` only prevents Windows App from reaching out to the Microsoft Store to look for updates. If Windows App was downloaded from Microsoft Store, the Microsoft Store still pushes updates as usual, including Windows App.

You can configure the registry using an enterprise deployment tool such as Intune, Configuration Manager, or Group Policy, or use PowerShell.

To set this registry value using PowerShell:

1. Close Windows App if it's open.
2. Open a PowerShell prompt as an administrator, then run the following command. Be sure to replace `<value>` with the relevant registry value:

    ```powershell
    $path = "HKLM:\SOFTWARE\Microsoft\WindowsApp"
    If (!(Test-Path $path)) {
        New-Item -Path $path -Force
    }
    
    New-ItemProperty -Path $path -Name DisableAutomaticUpdates -PropertyType DWORD -Value '<value>' -Force
    ```
3. You don't need to restart the Windows device for the change to take effect. The next time Windows App launches it uses the configured update behavior.

### Insider Ring

The Insider release of the Windows App offers an early preview of features planned for the upcoming public release. Typically available two weeks in advance, the Insider release enables users to test new functionality before it becomes broadly available across supported devices. Users can opt in or out of Insider releases in the settings panel of the Windows App. Windows App will update when a newer version is available in the currently selected ring, Public or Insider.

Insider release will not be available if CDN updates are also blocked on the local Windows device. CDN updates can be disabled using the DisableAutomaticUpdates registry key or blocking network access to the [CDN endpoint](/en-us/azure/virtual-desktop/required-fqdn-endpoint?tabs=azure#end-user-devices).

### Disable or enforce Insider ring for Windows App

Setting the AdminReleaseRing registry value will disable the Insider toggle in the settings panel and prevent modification of the setting. To control the update behavior in Windows App on Windows for the Insider ring, set one of the following registry values on the local Windows device:

- **Key**: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsApp`
- **Type**: `REG_DWORD`
- **Name**: `AdminReleaseRing`
- **Data**:
    - `0`: Public Ring *(default value)*
    - `3`: Insider Ring