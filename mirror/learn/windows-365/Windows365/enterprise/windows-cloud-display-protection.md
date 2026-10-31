---
layout: Conceptual
title: Display Protection for Windows 365 and Azure Virtual Desktop | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/windows-cloud-display-protection
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn how to configure display protection for Windows 365 and Azure Virtual Desktop to help protect against screen capture malware on users' devices.
keywords: 
author: Fragnightmist
ms.author: ryclar
ai-usage: ai-assisted
manager: pratikshah
ms.date: 2026-10-28T00:00:00.0000000Z
ms.topic: how-to
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
locale: en-us
document_id: 86c3fb60-8ee9-bb4d-bfbc-c0876deb8cc0
document_version_independent_id: 86c3fb60-8ee9-bb4d-bfbc-c0876deb8cc0
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/windows-cloud-display-protection.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/windows-cloud-display-protection
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/windows-cloud-display-protection.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/7814ca69-56be-4667-8a46-86327796c328
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://authoring-docs-microsoft.poolparty.biz/devrel/f15dfcd0-2664-48ba-bb88-f1f86eadbfd1
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: c2caa5f8-b652-fabd-630b-48078c5a95aa
---

# Display Protection for Windows 365 and Azure Virtual Desktop | Microsoft Learn

Important

Display protection is in preview. For legal terms that apply to features that are in beta, preview, or otherwise not yet released into general availability, see the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). Visit this page to learn more about [previews in Windows 365](../public-preview)

**Applies to:**

- Windows 365 Cloud PCs
- Azure Virtual Desktop session hosts

## Overview

Display protection helps protect Windows 365 Cloud PC and Azure Virtual Desktop session video from screen capture malware on the user's local Windows device. The local device is the physical Windows device running Windows App. It supports both managed endpoints and unmanaged or bring-your-own-device (BYOD) endpoints.

Display protection doesn't require a GPU-enabled Cloud PC. Hardware-based protection uses a compatible GPU on the endpoint.

The feature uses Microsoft PlayReady to encrypt remote-session video and protect its decryption on the endpoint. Depending on the configured protection level and endpoint capabilities, it uses either hardware DRM (digital rights management) or software DRM:

- **Hardware DRM (SL3000)** uses hardware-backed PlayReady protection with a compatible endpoint GPU, which can be discrete or integrated.
- **Software DRM (SL2000)** uses software-based PlayReady protection. Software fallback is allowed only when the configured protection level permits it.

For background on these security levels, see [PlayReady security levels](/en-us/playready/overview/security-level).

Note

Input protection is a separate component of Input and Output Protection that protects keyboard input against keylogger threats. Input protection is configured independently from display protection. For more information, see [Input Protection](windows-cloud-input-protection).

## How display protection works

Display protection adds a protected video path between the remote session and the endpoint's PlayReady decryption environment. The feature includes:

- **Protected video decryption**: Remote-session video is encrypted before it leaves the Cloud PC or session host. PlayReady protects decryption on the endpoint.
- **Protection-level enforcement**: A connection is allowed only when Windows App can establish the configured PlayReady protection level.
- **Configurable protection levels**: Organizations can allow hardware or software DRM, or require hardware DRM and block endpoints that can't meet that requirement.
- **Session-specific protection**: Protection applies to remote-session video, not to other applications running locally on the endpoint.

### Protection boundaries

Hardware DRM and High-bandwidth Digital Content Protection (HDCP) protect different parts of the display path. Hardware DRM protects video decryption on the endpoint. HDCP concerns the physical output connection from the endpoint to a connected display, such as an HDMI or DisplayPort connection.

Display protection **doesn't currently enforce HDCP**, including when **Hardware enforcement required** is selected. That setting requires hardware DRM, not HDCP-capable monitors, docks, or adapters. Non-HDCP equipment isn't automatically rejected because it lacks HDCP support.

HDCP enforcement for external display connections is planned as a separate configuration option in a future update. It isn't available in the current release.

The feature is designed to help protect against malware on the device running Windows App, not to prevent a user from intentionally disclosing content they can view. It doesn't authenticate external displays or capture devices, guarantee that external capture hardware can't record the output, or prevent someone from photographing the screen. Don't treat a successful hardware DRM connection as proof that the external display path is protected.

## Supported configurations

This feature supports the following configurations:

- **Cloud PC or session host**: Windows 365 Cloud PC or Azure Virtual Desktop session host running a supported Windows client OS version or Windows Server.
- **Supported clients**: Windows App on Windows, when running on a physical Windows 11 device.
- **Not supported clients**: Virtual endpoint devices (VMs), macOS, iOS, Android, web browsers.

## Prerequisites

Before you configure display protection, ensure the following requirements are met:

- **Windows App**: Version 2.0.1236.0 or newer on Windows. Update to the latest version from the Microsoft Store.

## Configure display protection

Enable display protection only for the Cloud PCs or Azure Virtual Desktop session hosts you want to include in preview validation. Use the relevant configuration path for Azure Virtual Desktop or Windows 365.

### Display protection levels

Both Azure Virtual Desktop and Windows 365 support the following protection levels. The hardware and software labels refer to PlayReady protection on the endpoint, not to HDCP enforcement on connected displays.

| Level | Description |
| --- | --- |
| **Not configured** | Display protection isn't enabled for the Cloud PC or session host. |
| **Hardware or software enforcement** | Uses hardware DRM (SL3000) when available. If the endpoint can't provide hardware DRM, software DRM (SL2000) is allowed. |
| **Hardware enforcement required** | Requires hardware DRM (SL3000). If the endpoint can't provide it, the connection is blocked and the user sees an error. This level doesn't permit software DRM fallback. |

### Configure display protection for Azure Virtual Desktop

For Azure Virtual Desktop, add the display protection RDP property in the host pool advanced settings:

1. In the Azure portal, open the target host pool.
2. Go to **RDP properties** &gt; **Advanced** tab.
3. Add the following RDP property:

    `enableWindowsCloudIODisplayProtection:i:<value>`

    Where `<value>` is: `0` (not configured), `1` (hardware or software enforcement), or `2` (hardware enforcement required).

    ![Screenshot of the RDP Properties Advanced tab showing the enableWindowsCloudIODisplayProtection property.](media/windows-cloud-display-protection/rdp-properties-advanced.png)

This property enables server-side verification that Display Protection is enforced on the endpoint.

### Configure display protection for Windows 365

For Windows 365, configure display protection in Microsoft Intune:

1. Sign in to the [Microsoft Intune admin center](https://intune.microsoft.com).
2. Go to **Devices** &gt; **Manage Windows 365 Cloud PCs** &gt; **Cloud PC Settings**.
3. Under **IO Protection**, select the desired level for **Display Protection**.

    ![Screenshot showing the display protection level selection under IO Protection.](media/windows-cloud-display-protection/intune-config-selection.png)

When you enable display protection or change its level in Intune or in host pool RDP properties, the setting is delivered to the endpoint device through the connection (RDP) properties and is cached on the device. To apply an updated configuration immediately, select **Refresh** in Windows App. Otherwise, configuration changes can take up to 8 hours to reach an endpoint.

If a connection is unexpectedly blocked with an incompatible-client error shortly after you enable or change display protection, select **Refresh** in Windows App to pull the latest configuration, or wait for it to propagate—up to 8 hours—and then try to connect again.

## Validate protection

After you configure display protection on the target Cloud PCs or session hosts:

1. From a Windows 11 physical endpoint, open Windows App (version 2.0.1236.0 or newer).
2. Connect to a Cloud PC or session host that has display protection enabled.
3. Verify that the connection succeeds without an error message.
4. Attempt to use a screen capture tool on the endpoint while the remote session is active. The captured content from the remote session should be blocked or appear blank.

This capture test evaluates behavior on the endpoint. It doesn't validate HDCP enforcement or show that an external capture device is blocked.

To monitor display protection across your tenant, use [Cloud PC monitoring](cloud-pc-monitoring-overview) (preview) and review the `DisplayProtectionState` connection event on the **Connection health** page. For steps, see [Monitor Input and Output Protection](windows-cloud-io-protection#monitor-input-and-output-protection).

## Troubleshoot display protection

If display protection can't be established at the configured level, the connection is blocked and an error appears on the endpoint. Check the following:

- Use a supported physical Windows 11 endpoint and Windows App version.
- If you recently enabled or changed display protection, select **Refresh** in Windows App to retrieve the updated configuration, or allow up to 8 hours for propagation.
- If you require hardware enforcement, verify that the endpoint can provide hardware DRM. This requirement is separate from the HDCP capability of the attached display.

For help with connection errors, see [Troubleshoot connection errors](/en-us/troubleshoot/windows-365/connection-errors). If the issue continues, contact Microsoft support and provide the activity ID, timestamp of the failure, and steps to reproduce the issue.

## Limitations and considerations

- **Physical devices only**: Display protection requires a physical Windows 11 endpoint. Virtual machines aren't supported as endpoint devices.
- **Supported clients**: Windows App on Windows is the only supported client for display protection.
- **Not supported clients**: Virtual endpoint devices (VMs), macOS, iOS, Android, web browsers, and other non-Windows App on Windows clients, including Windows 365 Link devices.
- **External displays, docks, and adapters**: HDCP support alone doesn't determine whether an endpoint meets the configured PlayReady protection level. Don't assume that display protection blocks a non-HDCP monitor, a DisplayLink dock, or a USB display adapter. Validate the endpoint and display setup against your selected protection level; this doesn't establish protection against external capture devices.
- **Performance with software DRM**: When hardware DRM isn't available and the configured level allows software DRM, the session uses software DRM. Software DRM can increase the time needed to establish a session. If hardware enforcement is required instead, the connection is blocked rather than falling back.
- **Display resolution**: Display protection supports resolutions up to 4K (3840 x 2160). 5K monitors aren't currently supported. Use a 4K or lower-resolution monitor for protected sessions.

## Related features

- [Input Protection](windows-cloud-input-protection): Protects keyboard input against keylogger threats. Input protection is a separate component of Input and Output Protection and is configured independently from display protection.
- [Enable screen capture protection](/en-us/azure/virtual-desktop/screen-capture-protection?context=/windows-365/context/pr-context): A separate screen capture protection feature for Azure Virtual Desktop.
- [Watermarking](watermarking): Adds visible watermarks to remote sessions to discourage photo-based screen capture.