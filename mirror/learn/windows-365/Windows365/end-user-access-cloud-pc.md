---
layout: Conceptual
title: Accessing Cloud PCs | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/end-user-access-cloud-pc
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn how users can access their Cloud PC.
keywords: 
author: davidbel
ms.author: davidbel
manager: philge
ms.date: 2026-07-09T00:00:00.0000000Z
ms.topic: how-to
ms.service: windows-365
ms.subservice: 
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: ivivano
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier1
locale: en-us
document_id: bdb58563-68e8-e212-7ccc-979263860b07
document_version_independent_id: bdb58563-68e8-e212-7ccc-979263860b07
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/end-user-access-cloud-pc.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: end-user-access-cloud-pc
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/end-user-access-cloud-pc.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 337b826f-41f8-c1a2-663a-e3808d108ba4
---

# Accessing Cloud PCs | Microsoft Learn

Users can access their Cloud PCs in accordance with the following matrix:

| Windows 365 Edition | [Windows App](/en-us/windows-app/overview) | https://windows.cloud.microsoftweb client | Microsoft Remote Desktop | LG Web OS |
| --- | --- | --- | --- | --- |
| Windows 365 Business | X | X | X\* | X |
| Windows 365 Enterprise | X | X | X\* | X |
| Windows 365 Flex | X | X |  |  |
| Windows 365 Government | X | X |  |  |

\*\ Microsoft Remote Desktop support will end in March, 2026. For more information, see Remote Desktop.

For information on hardware requirements, see [End user hardware requirements](end-user-hardware-requirements).

Note

The Remote Desktop Connection client (mstsc.exe) is not a supported connection method for Windows 365 users. It may work for troubleshooting, but it should not be used for daily access. Use a supported client such as the Windows App or the Microsoft Remote Desktop app for the best experience.

## Windows App

Windows App is the recommended application to connect to Windows 365 Cloud PCs and can be used on any device. For more information about the requirements of running and using Windows App, see [What is Windows App?](/en-us/windows-app/overview)

## Windows 365 web site

Windows 365 users can navigate to https://windows.cloud.microsoft to access their Cloud PCs.

### Software requirements

To access their Cloud PC from this website, the user's device must meet the following requirements:

- Supported operating systems: Windows, macOS, ChromeOS, Linux
- A modern browser like Microsoft Edge, Google Chrome, Safari, Mozilla Firefox (v55.0 and later), or LG webOS 23.

### Home page

On their Windows 365 home page, users see the Cloud PCs they have access to in the **Your Cloud PCs** section.

![Windows 365 home.](business/media/get-started-windows-365-business/cloud-pc-home.png)

From this page, users have two options to connect to your Cloud PC:

- Select **Open in browser** to open their Cloud PC in the web client (not available for mobile devices).
- Select **Open in Remote Desktop app** to open their Cloud PC in Remote Desktop. For more information, see Remote Desktop.

### User actions

While on windows.cloud.microsoft, users can take actions on their Cloud PCs by selecting the gear icon on a Cloud PC card.

![Card menu.](business/media/get-started-windows-365-business/cloud-pc-gear.png)

- **Rename**: Changes the name of the Cloud PC shown to the user on the web site. This action doesn't affect any name in Microsoft Intune, Microsoft Entra ID, on the device, or in the Remote Desktop Apps.
- **Reset**:

    - Reinstalls Windows (with the option to choose between Windows 11 and Windows 10).
    - Removes your personal files.
    - Removes any changes you made to settings.
    - Removes your apps.

        Important

        Before resetting your Cloud PC, make sure to back up any important files you need to keep to a cloud storage service or external storage. Resetting your Cloud PC deletes these files.
- **Restart**: Restarts the Cloud PC. For Cloud PCs created after January 31, 2024, you can also restart or shut down by using the keyboard combination CTRL+ALT+DEL.
- **Troubleshoot**: Troubleshoot and attempt to resolve any issues that may be preventing a user from connecting to their Cloud PC. The checks run include:

    - Check whether any files or agents required for connectivity are correctly installed.
    - Make sure that the Azure resources are available.

    | Return state | Description |
    | --- | --- |
    | No issues detected | None of the checks discovered an issue with the Cloud PC. |
    | Issues resolved | An issue was detected and fixed. |
    | Can't connect to Cloud PC. We're working to fix it, try again later. | A Microsoft service required for connectivity is unavailable. Try connecting again later. |
    | We couldn't fix issues with your Cloud PC. Contact your administrator. | An issue was detected but it couldn't be fixed. This issue exists because of an ongoing Windows update or another issue. If this error persists for an extended period of time, the Cloud PC may need to be reset. |
- **System Information**: Displays information about the Cloud PC specification.

### Dark mode

To switch the windows.cloud.microsoft site to dark mode:

1. Go to windows.cloud.microsoft.
2. Select the gear icon and then under **Choose your mode**, select **Dark**.

    ![Screenshot of dark mode option.](media/end-user-access-cloud-pc/dark-mode.png)

### In session settings

When you select **Open in browser** for a Cloud PC on the windows.cloud.microsoft web site, the **In Session Settings** window appears, where you can choose multiple options before connecting to your Cloud PC:

1. Select which devices and features on your physical device that your Cloud PC can access:
    - Printer
    - Microphone
    - Clipboard
    - Location (preview)
2. Select **Show advanced settings**to see the following options:
    - Alternative keyboard layout
3. Select **Connect**. The Cloud PC opens in the web client (browser).

### Change settings in Cloud PC

To change settings from within the Cloud PC:

1. Select the gear icon.
2. Select the options you want change &gt; **Update**.

The changes will appear the next time you restart the Cloud PC.

### User feedback

Users can provide feedback about their Cloud PC experience by using the feedback icon in the upper right corner.

### Connection details

Users can view and download connection details.

1. Select the **Connection details** icon &gt; **Show details**.

    ![Screenshot of Connection icon.](media/end-user-access-cloud-pc/connection.png)
2. To download a text file containing the connection details, select **Download report**.

    ![Screenshot of connection details.](media/end-user-access-cloud-pc/connection-details.png)

### Transfer files to and from a Cloud PC

To transfer files from the local device to the Cloud PC, select the upload icon to launch File Explorer. Select the files to transfer them to the \This PC\Windows365 virtual drive\Uploads folder on the Cloud PC.

To transfer files from the Cloud PC to the local device, copy the files to the Downloads folder on the Cloud PC. The files are automatically copied to the \This PC\Windows365 virtual drive\Downloads folder of the local device.

#### Restrict users from transferring files to and from Cloud PCs

You can restrict users from transferring files by using RDP drive redirection. For more information, see [Manage RDP device redirections for Cloud PCs](enterprise/manage-rdp-device-redirections).

### Collect user logs

Users can collect logs of their Cloud PC sessions. The logs are collected from the browser and the user can choose the save location.

To turn on log collection, in the client, select the information icon &gt; **Capture logs**.

![Capture logs.](media/get-users-started/settings-logs.png)

### Hardware acceleration

You can turn on hardware acceleration when using the web client to access your Cloud PC. This option decreases network latency, improving the web client Cloud PC experience. This option is turned on by default.

To turn hardware acceleration on or off, in the client, select the gear icon &gt; **Use hardware acceleration**.

### High DPI

You can use the **High DPI** toggle to render the web client using the native resolution of the physical device. High DPI is a good option to turn on if you're using a high resolution screen, like 4K or UHD monitors.

The High Dots Per Inch (DPI) setting adjusts the display resolution to match the physical size of the screen and the distance between the user and the screen.

To choose this option, select the gear icon &gt; **High DPI**.

### Alternative keyboard layout

Use this option if you're using a nonstandard keyboard that includes special characters (like Chinese (Traditional) or Spanish (Mexico)).

1. In the Windows 365 web client **In Session Settings** window, choose **Show advanced settings** &gt; **Alternative keyboard layout** &gt; **On**.

    ![Screencap of In Sessions Settings window Alternative Keyboard Layout.](media/end-user-access-cloud-pc/alternative-keyboard-layout.png)
2. In the drop-down list, select the language that matches the keyboard.

By default, **Alternative keyboard layout** is turned off. If using a standard keyboard that doesn't require special layouts, the user can deselect this option. Deselecting the option in the middle of a session requires reconnecting.

### Location (preview)

Location redirection lets Cloud PCs access your approximate location safely without privacy concerns. By turning on the location service, you let your Cloud PC use the location of your physical device for most apps (the Weather widget isn't currently supported).

For more information about location services, see [Windows location service and privacy](https://support.microsoft.com/en-us/windows/windows-location-service-and-privacy-3a8eee0a-5b0b-dc07-eede-2a5ca1c49088).

Location redirection requires local admin privileges on the Cloud PC. For more information, see [Assign user as a local admin](enterprise/assign-users-as-local-admin).

To turn on location redirection, follow these steps:

1. On your physical device, go to **Settings** &gt; **Privacy & Security** &gt; **Location**.
2. For **Location services**, set the toggle to **On**.
3. For **Let apps access your location**, set the toggle to **On**.
4. For each app that you want your Cloud PC to have location information, set the toggle to **On**.
5. Go to windows.cloud.microsoft.
6. Under **Your Cloud PCs**, select **Open in a browser** for your Cloud PC.
7. Under **In Session Settings**, select **Location (Preview)** &gt; **Connect**.

    ![Screenshot of Location redirection option.](media/end-user-access-cloud-pc/location.png)
8. In the **windows.cloud.microsoft wants to Know your location** confirmation box, select **Allow**.

Organizational settings might override the location settings for your device. For example, your organization might disable location redirection for all Cloud PCs they manage.

### Keyboard shortcuts (preview)

While accessing your Cloud PC using the web client, you can set your Cloud PCs to use special keyboard shortcuts (combination keys with the Windows key, ESC, and so on). For a full list of shortcuts, see [Keyboard shortcuts in Windows](https://support.microsoft.com/en-us/windows/keyboard-shortcuts-in-windows-dcc61a57-8ff0-cffe-9796-cb9706c75eec).

Keyboard shortcuts are in [public preview](public-preview).

To turn on keyboard shortcuts for your Cloud PC:

1. Go to windows.cloud.microsoft.
2. Under **Your Cloud PCs**, select **Open in a browser** for your Cloud PC.
3. Under **In Session Settings**, select **Keyboard shortcuts (Preview)** &gt; **Connect**. [![Screencap of In Sessions Settings Keyboard shortcuts.](media/end-user-access-cloud-pc/keyboard-shortcuts.png)](media/end-user-access-cloud-pc/keyboard-shortcuts.png#lightbox)

When **Keyboard shortcuts** is turned on, the web client opens in full-screen mode. Keyboard shortcuts only work in full-screen mode. Full screen using F11 isn't supported. You must use the full screen mode from the toolbar.

To turn off keyboard shortcuts, in your web client, select **Settings** &gt; deselect **Keyboard shortcuts** &gt; **Update**.

### LG webOS 23

The Windows 365 web client can be accessed through LG TV with the latest webOS 23.

To launch the web client on an LG TV (with LG webOS 23), navigate to **Home Office** &gt; **Windows 365**.

The following Windows 365 features aren't available on LG TV:

- File Transfer
- Clipboard
- Location redirection
- Collected error logs
- Hardware acceleration
- Keyboard shortcuts

## Remote Desktop

The Microsoft Remote Desktop app is an alternative to Windows App that lets users access and control a remote PC, including a Cloud PC.

For a list of clients by operating system, see [Remote Desktop clients](/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients). For a comparison of features by client, see [Compare the clients: features](/en-us/azure/virtual-desktop/compare-remote-desktop-clients).

Important

Starting March 27, 2026, the Remote Desktop client for Windows (MSI) will no longer be supported. Users should begin migrating to Windows App to make sure they have continued access to their Azure Virtual Desktop and Windows 365 resources after this date. For more information on known limitations of Windows App, see [Known issues and limitations of Windows App](/en-us/windows-app/troubleshoot-known-issues-limitations?tabs=windows). This list is updated as Remote Desktop client features are supported in Windows App. Starting May 27, 2025, the Remote Desktop app for Windows from the Microsoft Store will no longer be supported or available for download and installation. Users must transition to Windows App to make sure they have continued access to Windows 365, Azure Virtual Desktop, and Microsoft Dev Box. For more information, see [Get started with Windows App to connect to devices and apps](/en-us/windows-app/get-started-connect-devices-desktops-apps).