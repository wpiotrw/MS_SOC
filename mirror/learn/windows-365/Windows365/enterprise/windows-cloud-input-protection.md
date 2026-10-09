---
layout: Conceptual
title: Input Protection | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/windows-cloud-input-protection
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Input Protection secures keyboard input for Windows 365 Cloud PCs and Azure Virtual Desktop by encrypting keystrokes at the kernel level to protect against keylogger malware.
ai-usage: ai-assisted
author: Fragnightmist
ms.author: ryclar
manager: pratikshah
ms.service: windows-365
ms.topic: how-to
ms.date: 2026-07-21T00:00:00.0000000Z
ms.subservice: windows-365-enterprise
locale: en-us
document_id: 90ee0215-42d8-e93c-05d1-64b0844036a7
document_version_independent_id: 90ee0215-42d8-e93c-05d1-64b0844036a7
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/windows-cloud-input-protection.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/windows-cloud-input-protection
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/windows-cloud-input-protection.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 2cec60ce-d2a8-266e-88da-c7f9fada7f97
---

# Input Protection | Microsoft Learn

Important

Input protection is in public preview. See the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) for legal terms that apply to Azure features that are in beta, preview, or otherwise not yet released into general availability. Visit this page to learn more about [previews in Windows 365](../public-preview).

## Overview

Windows 365 Cloud PCs already encrypt sessions and enforce identity-based authentication methods like multifactor authentication (MFA) to prevent hijacking and man-in-the-middle attacks. However, reducing the risks from threats that may reside on the connect device, such as keyloggers, can still compromise sensitive data, leading to compliance risks and financial loss.

Input protection addresses this gap with a kernel-level driver and system-level encryption that securely routes keystrokes directly to the Cloud PC, bypassing OS layers vulnerable to malware. When you enable this feature on a Cloud PC or Azure Virtual Desktop session host, it enforces a strict trust model:

- Only protected endpoint physical devices can connect.
- Endpoints must have the input protection MSI installed.
- Endpoints must be registered with your organization (Microsoft Entra registered or Microsoft Entra joined).

If the MSI is missing or the endpoint isn't registered with your organization, the connection is blocked and an error message appears. This model ensures a secure channel between Windows App and the Cloud PC or Azure Virtual Desktop session host, delivering uncompromised input protection.

## Supported configurations

This feature supports the following configurations:

- **Cloud PC or session host**: Windows 365 Cloud PC or Azure Virtual Desktop session host running a supported Windows client OS version or Windows Server.
- **Supported clients**: Windows App on Windows, when running on a physical Windows 11 device and with the input protection MSI installed.
- **Not supported clients**: Virtual endpoint devices (VMs), macOS, iOS, Android, web browsers, and Windows devices that don't have the Input Protection MSI installed, including Windows 365 Link devices.

## Install the input protection MSI

### Prerequisites

- The endpoint must be a physical device (virtual machines aren't supported) running Windows 11.
- The user must have **Local Admin** rights to install the MSI.
- Windows App version 2.0.1236.0 or newer. Update to the latest version from the Microsoft Store.
- The endpoint must be registered with the same organization (Microsoft Entra tenant) that provides the protected Cloud PC or session host—that is, the device must be Microsoft Entra registered or Microsoft Entra joined. For steps, see Register the endpoint device.

### Install the MSI

1. When a user tries to connect from a physical device without the input protection MSI to a Windows 365 Cloud PC or Azure Virtual Desktop session host, the following error message appears:

    ![Screenshot of error message because keyboard protection client isn't installed.](media/windows-cloud-input-protection/input-protection-error-message.png)
2. Download and install the appropriate MSI:

    - [Windows x64](https://go.microsoft.com/fwlink/?linkid=2336167)
    - [Windows ARM 64](https://go.microsoft.com/fwlink/?linkid=2342309)

## Register the endpoint device

Important

Input protection requires the connecting endpoint to be registered with the same organization (Microsoft Entra tenant) that provides the protected Cloud PC or Azure Virtual Desktop session host. The device must be Microsoft Entra registered or Microsoft Entra joined. If the endpoint isn't registered, connection validation fails and the user receives error code `0x705`, which indicates that the endpoint isn't registered.

To register the endpoint, add a work or school account for the organization that provides the protected resource:

1. On the endpoint, open **Settings** &gt; **Accounts** &gt; **Access work or school**.
2. Select **Connect**, and then sign in with the credentials for the organization that provides the protected Cloud PC or session host.
3. After registration finishes, restart Windows App or reconnect.

Note

Immediately after you register the device, the first connection attempts might fail with error code `0x702`. If this happens, sign out of Windows App, remove the account from Windows App, sign in again, and then reconnect.

## Configure input protection

You can configure input protection for Azure Virtual Desktop (Azure Portal) and for Windows 365 (Intune).

Note

If you previously enabled this feature by using the registry key `fWCIOKeyboardInputProtection`, follow these steps to remove it. Registry key support for Azure Virtual Desktop and Windows 365 will be deprecated in favor of RDP properties.

1. Open the Registry Editor app.
2. Navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services`.
3. Delete `fWCIOKeyboardInputProtection`.

### Configure for Azure Virtual Desktop

1. Sign in to the [Azure portal](https://portal.azure.com/).
2. Navigate to **Host Pool** &gt; **RDP Properties** &gt; **Advanced** tab.
3. Enter `enablewindowscloudiokeyboardinputprotection:i:1` as shown in the following screenshot:

    ![Screenshot of the enablewindowscloudiokeyboardinputprotection setting in Azure portal RDP properties.](media/windows-cloud-input-protection/image.png)

    To stop enforcing input protection for the host pool, set the property value to `enablewindowscloudiokeyboardinputprotection:i:0`.

### Configure for Windows 365

1. Sign in to the [Microsoft Intune admin center](https://intune.microsoft.com).
2. Navigate to **Devices** &gt; **Windows 365** &gt; **Settings** &gt; **Create** &gt; **Remote Connection Experience (preview)**.

    ![Screenshot showing Win365 RDP Properties Remote Connection Experience.](media/windows-cloud-input-protection/win365-rdp-properties-remote-connection-experience.png)
3. Create a Remote Connection Experience object and navigate to **Configuration Settings** to enable **input protection**.

    ![Screenshot showing Win365 RDP Properties Input Protection setting.](media/windows-cloud-input-protection/win-365-rdp-properties-input-protection.png)
4. After you create the Remote Connection Experience object and select **Enable** for **input protection**, the setting takes effect. 2.In the Assignments section select an Entra group containing the Cloud PC, not the user.

    To disable input protection, remove or unassign the Remote Connection Experience setting from the target Cloud PCs.

## Validate protection

After you enable input protection, confirm that enforcement works as expected:

1. From a Windows 11 physical endpoint using Windows App that has the input protection MSI installed, connect to a Cloud PC or session host that has input protection enabled. The connection succeeds.
2. From a Windows 11 endpoint using Windows App that doesn't have the MSI installed, try to connect to the same protected resource. The connection is blocked and an error message appears.
3. Confirm that connections to resources that don't have input protection enabled continue to work from both endpoints.

To monitor input protection across your tenant, use [Cloud PC monitoring](cloud-pc-monitoring-overview) (preview) and review the `KeyboardInputProtectionState` connection event on the **Connection health** page. For steps, see [Monitor Input and Output Protection](windows-cloud-io-protection#monitor-input-and-output-protection).

## Troubleshoot input protection

If a connection fails or the MSI doesn't install as expected, collect the following information before you contact Microsoft support:

- **MSI installation log**: `%TEMP%\msi*.log`, generated during MSI installation.
- **Endpoint logs**: `C:\Program Files\Windows Cloud IO Protection\logs`.
- **Client and package versions**: The Windows App version and the installed MSI version.
- **Endpoint architecture**: x64 or ARM64.
- **Resource type**: Windows 365 Cloud PC or Azure Virtual Desktop host pool.
- **Activity ID**: On a connection error, select **See details**, and then copy the activity ID.

If keyboard input seems unresponsive in a session, select inside the remote session window and try again before you collect logs.