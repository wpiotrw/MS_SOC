---
layout: Conceptual
title: Configure scanner redirection over the Remote Desktop Protocol - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/redirection-configure-scanners
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
zone_pivot_group_filename: virtual-desktop/zone-pivot-groups.json
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: jordanmarchese
manager: eliotgra
ms.author: jordanm
ms.service: azure-virtual-desktop
description: Learn how to redirect scanners from a local device to a remote session over the Remote Desktop Protocol. It applies to Azure Virtual Desktop, Windows 365, and Microsoft Dev Box.
ms.topic: how-to
zone_pivot_groups: rdp-products-features
ms.date: 2026-09-11T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: c23a1836-d77d-7f5b-9705-44ecbfd7702a
document_version_independent_id: c23a1836-d77d-7f5b-9705-44ecbfd7702a
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/redirection-configure-scanners.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: redirection-configure-scanners
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/redirection-configure-scanners.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e10a756b-c002-4cbb-8cf6-f0fab0633697
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a741da3-90b9-472d-8fd6-830aafecaac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 4ed9bcd0-4c92-f47c-227d-33a4762decae
---

# Configure scanner redirection over the Remote Desktop Protocol - Azure Virtual Desktop | Microsoft Learn

Tip

This article is shared for services and products that use the Remote Desktop Protocol (RDP) to provide remote access to Windows desktops and apps.

Select a product using the buttons at the top of this article to show the relevant content.

You can configure the redirection behavior of scanners from a local device to a remote session over the Remote Desktop Protocol (RDP). Scanner redirection uses high-level peripheral reflection and supports TWAIN.

This article provides information about supported redirection methods and how to configure scanner redirection. To learn more about how redirection works, see [Peripheral and resource redirection over the Remote Desktop Protocol](redirection-remote-desktop-protocol).

Note

Scanner redirection over RDP is in preview.

## Prerequisites

Before you configure scanner redirection, you need:

::: zone pivot="azure-virtual-desktop"

- An existing host pool with session hosts.
- A Microsoft Entra ID account that's assigned the [Desktop Virtualization Host Pool Contributor](rbac#desktop-virtualization-host-pool-contributor) built-in role-based access control (RBAC) role on the host pool as a minimum.

::: zone-end

::: zone pivot="windows-365"

- An existing Cloud PC.

::: zone-end

::: zone pivot="dev-box"

- An existing dev box.

::: zone-end

- A TWAIN scanner available on the local device. You need to make sure the scanner driver is installed correctly on the local device.
- To configure Microsoft Intune, you need:

    - A Microsoft Entra ID account that's assigned the [Policy and Profile manager](/en-us/mem/intune/fundamentals/role-based-access-control-reference#policy-and-profile-manager) built-in RBAC role.
    - A group containing the devices you want to configure.
- To configure Group Policy, you need:

    - A domain account that has permission to create or edit Group Policy objects.
    - A security group or organizational unit (OU) containing the devices you want to configure.
- You need to connect to a remote session from a supported app and platform. Windows App for Windows devices must be on build 2.0.1070.0. To view redirection support in Windows App and the Remote Desktop app, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features#redirection) and [Compare Remote Desktop app features across platforms and devices](/en-us/previous-versions/remote-desktop-client/compare-remote-desktop-clients#redirection).

::: zone pivot="azure-virtual-desktop"

## Session host configuration

To configure a session host for scanner redirection, you need to do the following:

1. Review the default configuration:

    - Windows operating system: scanner redirection isn't blocked.
    - Session host: scanner redirection from the local device to a remote session is disabled.
    - Result: scanner redirection from the local device to a remote session is disabled.
2. On each session host, launch command line with admin privileges and run the following command:

    ```cmd
    reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services" /v fTWAINRedirectionEnabled /t REG_DWORD /d 1 /f
    ```
3. Install [`TwainRedirectorMsi-1.0.2603.17170.msi`](https://aka.ms/AVD-W365-TWAIN-Redirector-Download) on each session host.

::: zone-end

::: zone pivot="windows-365"

## Cloud PC configuration

To configure a Cloud PC for scanner redirection, you need to do the following:

1. Review the default configuration:

    - Windows operating system: scanner redirection isn't blocked.
    - Cloud PC: scanner redirection from the local device to a remote session is disabled.
    - Result: scanner redirection from the local device to a remote session is disabled.
2. On each Cloud PC, launch command line with admin privileges and run the following command:

    ```cmd
    reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services" /v fTWAINRedirectionEnabled /t REG_DWORD /d 1 /f
    ```
3. Install [`TwainRedirectorMsi-1.0.2603.17170.msi`](https://aka.ms/AVD-W365-TWAIN-Redirector-Download) on each Cloud PC.

::: zone-end

::: zone pivot="dev-box"

## Dev box configuration

To configure a dev box for scanner redirection, you need to do the following:

1. Review the default configuration:

    - Windows operating system: scanner redirection isn't blocked.
    - Dev box: scanner redirection from the local device to a remote session is disabled.
    - Result: scanner redirection from the local device to a remote session is disabled.
2. On each dev box, launch command line with admin privileges and run the following command:

    ```cmd
    reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services" /v fTWAINRedirectionEnabled /t REG_DWORD /d 1 /f
    ```
3. Install [`TwainRedirectorMsi-1.0.2603.17170.msi`](https://aka.ms/AVD-W365-TWAIN-Redirector-Download) on each dev box.

::: zone-end

## Local device configuration

To configure scanner redirection on the local device, set the following registry values:

1. Set `fTWAINRedirectionEnableMode` to control how scanner names appear in the remote session:

    - `1`: Enabled, and the real scanner name is visible.
    - `2`: Enabled, and the scanner appears as **Redirected TWAIN Scanner**.

    Choose the option that matches your app requirements. Use `1` if your app must see the real scanner name. Use `2` if your app works with the generic scanner profile.

    ```cmd
    reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services\Client" /v fTWAINRedirectionEnableMode /t REG_DWORD /d 1 /f
    ```
2. Optionally, set `TWAINSelectDeviceByName` to automatically select a default scanner by name. When configured, this setting prevents users from manually selecting a different redirected scanner in the remote session. Use required value name `8000`. Replace `"HP LaserJet Pro MFP M428"` with your scanner name. Keep the quotation marks in the command.

    ```cmd
    reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services\Client\TWAINSelectDeviceByName" /v 8000 /t REG_SZ /d "HP LaserJet Pro MFP M428" /f
    ```

## Test scanner redirection

To test scanner redirection:

1. Make sure a scanner is available on the local device and is working.
2. Connect to a remote session using Windows App or the Remote Desktop app on a platform that supports scanner redirection. For more information, see [Compare Windows App features across platforms and devices](/en-us/windows-app/compare-platforms-features#redirection) and [Compare Remote Desktop app features across platforms and devices](/en-us/previous-versions/remote-desktop-client/compare-remote-desktop-clients#redirection).
3. Check the scanners that are connected to the remote session. With the display in full screen, on the status bar select the icon to select devices to use. This icon shows when Scanner and/or USB redirection is correctly configured.

    ![A screenshot showing the status bar of Windows App with a red box around the select devices to use icon.](media/redirection-remote-desktop-protocol/windows-app-status-bar-device-redirection.png)
4. Check the box for the scanner you want to redirect to the remote session.
5. Open a TWAIN-compatible application in the remote session and perform a test scan to confirm the scanner works.