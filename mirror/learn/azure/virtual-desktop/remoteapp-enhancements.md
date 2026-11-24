---
layout: Conceptual
title: RemoteApp enhancements - Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/virtual-desktop/remoteapp-enhancements
uhfHeaderId: azure
breadcrumb_path: /azure/virtual-desktop/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
feedback_product_url: https://techcommunity.microsoft.com/t5/azure-virtual-desktop/idb-p/AzureVirtualDesktop
author: brandondombrowsky
manager: eliotgra
ms.author: bdombrowsky
ms.service: azure-virtual-desktop
description: Learn how to enable enhanced windowing and integration behaviors for RemoteApps (preview).
ms.topic: how-to
ms.date: 2026-11-13T00:00:00.0000000Z
locale: en-us
document_id: 0fbff5c4-e819-5513-f1f0-72727c2320da
document_version_independent_id: 0fbff5c4-e819-5513-f1f0-72727c2320da
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/virtual-desktop/remoteapp-enhancements.md
site_name: Docs
depot_name: Learn.azure-virtual-desktop
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: remoteapp-enhancements
moniker_range_name: 
monikers: []
item_type: Content
source_path: virtual-desktop/remoteapp-enhancements.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/19ec6774-09b8-473e-a17e-b17b518bbad7
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ade36b61-c646-4bd8-87ee-f3a843461962
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: f86b791a-718e-66b3-6cfe-792e2cb22f5c
---

# RemoteApp enhancements - Azure Virtual Desktop | Microsoft Learn

Upcoming enhancements to Azure Virtual Desktop RemoteApps and Windows 365 Cloud Apps include improved support for Windows Snap and full-screen mode, better multi-monitor handling, and refined visuals like borders, shadows, and theme integration.

Now that these enhancements have become generally available (GA), they'll be enabled by default on supported systems.

## Prerequisites

In order to take advantage of these enhancements, you need the following:

- An Azure Virtual Desktop deployment with [published RemoteApps](publish-applications-stream-remoteapp), or a Windows 365 deployment with [published Cloud Apps](/en-us/windows-365/enterprise/cloud-apps).
- Session hosts or Cloud PCs running an operating system that supports the enhancements:

    | Session host or Cloud PC operating system | Minimum version/required update |
    | --- | --- |
    | Windows 11 Enterprise, version 26H2 | [26300.9974 (KB5132061)](https://support.microsoft.com/en-us/servicing/os/windows-11/2025/12/december-1-2025-kb5070311-os-builds-26200-7309-and-26100-7309-preview) |
    | Windows 11 Enterprise, version 24H2 | [26100.7309 (KB5070311)](https://support.microsoft.com/topic/december-1-2025-kb5070311-os-builds-26200-7309-and-26100-7309-preview-5cd455bf-3291-47fa-b0bf-e5f60d0ea7af) |
    | Windows 11 Enterprise, version 25H2 | [26200.7309 (KB5070311)](https://support.microsoft.com/topic/december-1-2025-kb5070311-os-builds-26200-7309-and-26100-7309-preview-5cd455bf-3291-47fa-b0bf-e5f60d0ea7af) |
    | Windows 11 Enterprise, version 25H2 (Preview) | [26220.7051 (KB5067115)](https://blogs.windows.com/windows-insider/2025/10/31/announcing-windows-11-insider-preview-build-26220-7051-dev-beta-channels/) |
    | Windows 11 Enterprise multi-session, version 24H2 | [26100.7309 (KB5070311)](https://support.microsoft.com/topic/december-1-2025-kb5070311-os-builds-26200-7309-and-26100-7309-preview-5cd455bf-3291-47fa-b0bf-e5f60d0ea7af) |
    | Windows 11 Enterprise multi-session, version 25H2 | [26200.7309 (KB5070311)](https://support.microsoft.com/topic/december-1-2025-kb5070311-os-builds-26200-7309-and-26100-7309-preview-5cd455bf-3291-47fa-b0bf-e5f60d0ea7af) |
    | Windows 11 Enterprise multi-session, version 25H2 (Preview) | [26220.7051 (KB5067115)](https://blogs.windows.com/windows-insider/2025/10/31/announcing-windows-11-insider-preview-build-26220-7051-dev-beta-channels/) |
- Session hosts or Cloud PCs with [SxS Network Stack](whats-new-sxs) version 1.0.2608.28600 or newer installed.
- A local device running one of the following operating systems:

    - Windows 11, version 24H2
    - Windows 11, version 25H2
    - Windows 11, version 26H2
- A client running on the local device that supports the enhancements:

    | Client | Minimum version |
    | --- | --- |
    | [Windows App for Windows](/en-us/windows-app/whats-new#latest-release) | 2.0.864.0 |

Note

This minimum version build is what is required to run the RemoteApp enhancements. However, the latest version of the Windows App will provide the optimal experience.

## RemoteApp enhancements

Enhancements will now be enabled by default for host pools deployed in the production environment as part of a staged rollout.

1. Please ensure these Group Policies are enabled on session hosts or Cloud PCs::

    - Local Computer Policy &gt; Computer Configuration &gt; Administrative Templates &gt; Windows Components &gt; Remote Desktop Services &gt; Remote Desktop Session Host &gt; Remote Session Environment &gt; **Use advanced RemoteFX graphics for RemoteApp**
    - Local Computer Policy &gt; Computer Configuration &gt; Administrative Templates &gt; Windows Components &gt; Remote Desktop Services &gt; Remote Desktop Session Host &gt; Remote Session Environment &gt; **Enable enhanced shell experience for RemoteApp**
2. Reboot the session hosts or Cloud PCs (only if you are reenabling these policies).

## Verify RemoteApp enhancements are working

To check that the RemoteApp enhancements are enabled, open the Connection Information dialog in Windows App. You can verify that the remote session type is correct using the *Connection Information* dialog from the Windows App.

1. Using a supported client (see Prerequisites), connect to a published RemoteApp or Cloud App.
2. In the system tray (red), find your RemoteApp session (yellow) and right click. Hover over the *Contoso - RemoteApp* fly out:
3. Select the *Connection Information* option (green). From the dialogue box that pops up, select **See details**.
4. Check the "Remote session type" value:

    - If "Remote session type" has a value of **RemoteAppV2**, then the RemoteApp enhancements are working.
    - If "Remote session type" has any other value, then the RemoteApp enhancements aren't working (and the RemoteAppV2 has not been flighted to you, yet). Check that your client and host meet all the prerequisites, and check that you've correctly set the enablement registry value on the host.

## Known issues and limitations

- Certain RemoteApp enhancements aren't applied to Microsoft Edge and Chrome.
- RemoteApp windows set to "Always on top" may not stay in front or switch correctly with local windows.
- Closing a RemoteApp window sometimes changes the foreground window.