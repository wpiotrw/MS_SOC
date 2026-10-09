---
layout: Conceptual
title: Compare Windows App features across platforms and devices - Windows App | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-app/compare-platforms-features
breadcrumb_path: /windows-app/breadcrumb/toc.json
feedback_system: Standard
permissioned-type: public
uhfHeaderId: MSDocsHeader-Windows-App
manager: eliotgra
ms.service: windows-app
search.audiencetype: EndUser
description: Learn about which features of Windows App are supported on which platforms and devices.
ms.topic: article
zone_pivot_groups: windows-app-connections-cloud-services
author: hilarybr
ms.author: avdcontent
ms.date: 2026-09-11T00:00:00.0000000Z
locale: en-us
document_id: 592bac75-f03d-2c64-2f52-a8688a0630a0
document_version_independent_id: 592bac75-f03d-2c64-2f52-a8688a0630a0
original_content_git_url: https://github.com/MicrosoftDocs/windows-app-pr/blob/live/windows-app/compare-platforms-features.md
site_name: Docs
depot_name: MSDN.windows-app
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: compare-platforms-features
moniker_range_name: 
monikers: []
item_type: Content
source_path: windows-app/compare-platforms-features.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/cd440f3c-1b78-40a7-97ba-aa00a1d79df7
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c828f7e0-89b4-459c-9bae-d7ab1c4bd9ad
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 3c4e193f-a19a-a886-3b3f-3a3629d68bec
---

# Compare Windows App features across platforms and devices - Windows App | Microsoft Learn

Windows App is supported on Windows, macOS, iOS/iPadOS, Android/Chrome OS, and in a web browser. However, support for some features differs across these platforms. This article details which features are supported on which platforms for each cloud service.

Tip

Select what you want to connect to using the buttons at the top of this article for the correct information.

## Experience

The following table compares which Windows App experience features are supported on which platforms:

::: zone pivot="azure-virtual-desktop"

| Feature | Windows | macOS | iOS/iPadOS | Android/Chrome OS | Webbrowser | MetaQuest |
| --- | --- | --- | --- | --- | --- | --- |
| Dark or light appearance | ✅ | ✅ | ✅ | ✅ | ✅ | ❌¹ |
| Integrated apps | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Localization² | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Favorite | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Search | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Uniform Resource Identifier (URI) schemes | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

::: zone-end

::: zone pivot="windows-365"

| Feature | Windows | macOS | iOS/iPadOS | Android/Chrome OS | Webbrowser | MetaQuest |
| --- | --- | --- | --- | --- | --- | --- |
| Appearance (dark or light) | ✅ | ✅ | ✅ | ✅ | ✅ | ❌¹ |
| Localization² | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Favorite | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Pin to taskbar | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Search | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Windows 365 Boot | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Windows 365 Flex | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Windows 365 Switch | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

::: zone-end

::: zone pivot="dev-box"

| Feature | Windows | macOS | iOS/iPadOS | Android/Chrome OS | Webbrowser | MetaQuest |
| --- | --- | --- | --- | --- | --- | --- |
| Appearance (dark or light) | ✅ | ✅ | ✅ | ✅ | ✅ | ❌¹ |
| Localization² | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Favorite | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Pin to taskbar | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Search | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

::: zone-end

1. Only light appearance is available.
2. For more information, see Localization and languages.

The following table provides a description for each of the experience features:

::: zone pivot="azure-virtual-desktop"

| Feature | Description |
| --- | --- |
| [Appearance (dark or light)](display-settings) | Change the appearance of Windows App to be light or dark. |
| [Integrated apps](/en-us/azure/virtual-desktop/publish-applications) | Individual apps using RemoteApp in Azure Virtual Desktop are integrated with the local device as if they are running locally. |
| Localization | User interface available in languages other than *English (United States)*. |
| [Favorite](device-actions) | Pin your favorite devices and apps to the **Favorites** tab for quick access. |
| Search | Quickly search for devices or apps. |
| [Uniform Resource Identifier (URI) schemes](/en-us/azure/virtual-desktop/uri-scheme) | Start Windows App with specific parameters and values with a URI. |

::: zone-end

::: zone pivot="windows-365"

| Feature | Description |
| --- | --- |
| [Appearance (dark or light)](display-settings) | Change the appearance of Windows App to be light or dark. |
| Localization | User interface available in languages other than *English (United States)*. |
| [Favorite](device-actions) | Pin your favorite Cloud PCs to the **Favorites** tab for quick access. |
| [Pin to taskbar](device-actions) | Pin your favorite Cloud PCs to the **Windows taskbar** for quick access. |
| Search | Quickly search for devices or apps. |
| [Windows 365 Boot](/en-us/windows-365/enterprise/windows-365-boot-overview) | Boot directly to a Cloud PC, not the local device. |
| [Windows 365 Flex](/en-us/windows-365/enterprise/introduction-windows-365-flex) | Share a Cloud PC for shift and part-time workers. |
| [Windows 365 Switch](/en-us/windows-365/enterprise/windows-365-switch-overview) | Easily switch between your local device and a Cloud PC with the **Windows 11 Task view**. |

::: zone-end

::: zone pivot="dev-box"

| Feature | Description |
| --- | --- |
| [Appearance (dark or light)](display-settings) | Change the appearance of Windows App to be light or dark. |
| Localization | User interface available in languages other than *English (United States)*. |
| [Favorite](device-actions) | Pin your favorite dev boxes to the **Favorites** tab for quick access. |
| [Pin to taskbar](device-actions) | Pin your favorite dev boxes to the **Windows taskbar** for quick access. |
| Search | Quickly search for devices or apps. |

::: zone-end

## Display

The following table compares which display features are supported on which platforms:

| Feature | Windows | macOS | iOS/iPadOS | Android/Chrome OS | Webbrowser | MetaQuest |
| --- | --- | --- | --- | --- | --- | --- |
| Dynamic resolution | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ |
| External monitor | ✅ | ✅ | ✅ | ✅¹ | ❌ | ❌ |
| Multiple monitors | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Selected monitors | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ |
| Smart sizing | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |

1. Depends on the capabilities of the local device.

The following table provides a description for each of the display features:

| Feature | Description |
| --- | --- |
| [Dynamic resolution](display-settings) | The resolution and orientation of local displays is dynamically reflected in the remote session for desktops. If the session is running in *windowed* mode, the desktop is dynamically resized to the size of the window. |
| [External display](display-settings) | Enables the use of an external display for a remote session. |
| [Multiple displays](display-settings) | Enables the remote session to use all local displays. |
| [Selected displays](display-settings) | Specifies which local displays to use for the remote session. |
| [Smart sizing](display-settings) | A desktop in *windowed* mode is dynamically scaled to the window's size. |

## Multimedia

The following table shows which multimedia features are available on each platform:

| Feature | Windows | macOS | iOS/iPadOS | Android/Chrome OS | Webbrowser | MetaQuest |
| --- | --- | --- | --- | --- | --- | --- |
| Multimedia redirection (video playback) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Multimedia redirection (calls) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Microsoft Teams media optimizations (WebRTC) | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Microsoft Teams media optimizations (SlimCore) | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |

The following table provides a description for each of the multimedia features:

::: zone pivot="azure-virtual-desktop"

| Feature | Description |
| --- | --- |
| [Multimedia redirection](/en-us/azure/virtual-desktop/multimedia-redirection-video-playback-calls?pivots=azure-virtual-desktop) | Redirect video playback and calls from the desktop or app to the physical machine for faster processing and rendering. |
| [Teams media optimizations](/en-us/azure/virtual-desktop/teams-on-avd) | Optimized Microsoft Teams calling and meeting experience. |

::: zone-end

::: zone pivot="windows-365,dev-box"

| Feature | Description |
| --- | --- |
| [Multimedia redirection](/en-us/azure/virtual-desktop/multimedia-redirection-video-playback-calls?pivots=windows-365) | Redirect video playback and calls from the Cloud PC or dev box to the physical machine for faster processing and rendering. |
| [Teams media optimizations](/en-us/windows-365/enterprise/teams-on-cloud-pc) | Optimized Microsoft Teams calling and meeting experience. |

::: zone-end

## Redirection

The following sections detail the redirection support available on each platform.

Important

Redirection of these devices and resources is dependent on whether your administrator has allowed and configured them to be redirected. For example, your administrator can configure whether you can use your local printer in a remote session, or whether you can use your local clipboard in a remote session. For more information, please talk to your administrator. Redirection also depends on:

- The peripheral or resource type for which you want to control redirection.
- The platform of the local device, including what's available in the user interface or configured by another means, such as a policy.
- Where the remote session you connect to is hosted, for example Azure Virtual Desktop or Windows 365.
- Where in the redirection process you want to control behavior, for example on the local device or in the remote session.

A more restrictive setting takes precedence wherever it's configured. For example, if an administrator configures the clipboard to be redirected by default for all remote sessions, but the local device is configured to disable clipboard redirection, the clipboard isn't available in the remote session. For comprehensive details on configuring redirection for administrators, see:

- [Redirect local devices, audio, and folders in Windows App](device-audio-folder-redirection-teams).
- [Redirection over the Remote Desktop Protocol](/en-us/azure/virtual-desktop/redirection-remote-desktop-protocol), where you can also find links in the [Related content](/en-us/azure/virtual-desktop/redirection-remote-desktop-protocol#related-content) section to articles that explain how to configure redirection for specific peripheral and resource types.
- To prevent against accidental data loss on BYOD, you can use Intune MAM in addition to redirections set in the remote session. See [Require local client device security compliance](/en-us/windows-app/require-device-security-compliance-intune) and [Manage local device redirection settings](/en-us/windows-app/manage-device-redirection-intune). Redirections set by Intune MAM are not a substitute for securing redirections in the remote session. Drive, clipboard, printer and USB drive redirection is disabled by default. Evaluate alternatives before enabling those redirections. For example,
    - [Clipboard transfer direction and data type](/en-us/azure/virtual-desktop/clipboard-transfer-direction-data-types) if you require clipboard
    - [Universal Print](/en-us/universal-print/discover-universal-print) instead of printer redirection.

### Device redirection

The following table shows which local devices you can redirect to a remote session on each platform:

| Device type | Windows | macOS | iOS/iPadOS | Android/Chrome OS | Webbrowser | MetaQuest |
| --- | --- | --- | --- | --- | --- | --- |
| Cameras | ✅ | ✅ | ✅ | ✅ | ✅¹ | ✅ |
| Local drive/storage | ✅ | ✅ | ✅ | ✅ | ✅² | ✅ |
| Microphones | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Printers | ✅³ | ✅⁴ | ❌ | ❌ | ✅ | ❌ |
| Scanners⁵ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Smart cards | ✅ | ✅ | ✅⁶ | ❌ | ❌ | ❌ |
| Speakers | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

1. Camera redirection in a web browser is in preview.
2. Limited to uploading and downloading files through a web browser.
3. RAW printing is in preview for Azure Virtual Desktop only. For more information, see [RAW printing](/en-us/azure/virtual-desktop/redirection-configure-printers#raw-print-support).
4. Windows App on macOS supports the *Publisher Imagesetter* printer driver by default (*Common UNIX Printing System* (CUPS) only). Native printer drivers aren't supported.
5. TWAIN scanner redirection is in preview. For more information, see [Configure TWAIN scanner redirection](/en-us/azure/virtual-desktop/redirection-configure-scanners).
6. Smart card redirection for iOS/iPadOS is in preview. Only YubiKey is supported due to iOS/iPadOS limitations. For more information, see [YubiKey smart card redirection (preview)](device-audio-folder-redirection-teams#yubikey-smart-card-redirection-preview).

The following table provides a description for each type of device you can redirect:

| Device type | Description |
| --- | --- |
| [Cameras](device-audio-folder-redirection-teams) | Redirect a local camera to use with apps like Microsoft Teams. |
| [Local drive/storage](device-audio-folder-redirection-teams) | Access local disk drives in a remote session. |
| [Microphones](device-audio-folder-redirection-teams) | Redirect a local microphone to use with apps like Microsoft Teams. |
| [Printers](device-audio-folder-redirection-teams) | Print from a remote session to a local printer. |
| [Scanners](device-audio-folder-redirection-teams) | Access a local scanner in a remote session. |
| [Smart cards](device-audio-folder-redirection-teams) | Use smart cards in a remote session. |
| [Speakers](device-audio-folder-redirection-teams) | Play audio in the remote session or on local device. |

### Input redirection

The following table shows which input methods you can redirect:

| Feature | Windows | macOS | iOS/iPadOS | Android/Chrome OS | Webbrowser | MetaQuest |
| --- | --- | --- | --- | --- | --- | --- |
| Keyboard | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Keyboard input language | ✅ | ✅ | ❌ | ❌ | ✅¹ | ❌ |
| Keyboard shortcuts | ✅ | ✅ | ✅ | ✅² | ✅ | ✅ |
| Mouse/trackpad | ✅ | ✅ | ✅³ | ✅⁴ | ✅ | ❌ |
| Multi-touch | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ |
| Pen | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Touch | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |

1. Enabled by [alternative keyboard layout](input-keyboard-mouse-touch-pen?tabs=web#alternative-keyboard-layout-and-input-method-editor-ime).
2. For keyboard shortcuts limitations, see [Keyboard and keyboard shortcuts](input-keyboard-mouse-touch-pen?tabs=android#keyboard-and-keyboard-shortcuts).
3. For more information, see [Use keyboard, mouse, touch, and pen in Windows App](input-keyboard-mouse-touch-pen?tabs=ios-ipados#mouse-and-trackpad-device-support-1).
4. Mouse only.

The following table provides a description for each type of input you can redirect:

| Input type | Description |
| --- | --- |
| [Keyboard](input-keyboard-mouse-touch-pen) | Redirect keyboard inputs to the remote session. |
| [Mouse/trackpad](input-keyboard-mouse-touch-pen) | Redirect mouse or trackpad inputs to the remote session. |
| [Multi-touch](input-keyboard-mouse-touch-pen) | Redirect multiple touches simultaneously to the remote session. |
| [Pen](input-keyboard-mouse-touch-pen) | Redirect pen inputs, including pressure, to the remote session. |
| [Touch](input-keyboard-mouse-touch-pen) | Redirect touch inputs to the remote session. |

### Port redirection

The following table shows which ports you can redirect:

| Port type | Windows | macOS | iOS/iPadOS | Android/Chrome OS | Webbrowser | MetaQuest |
| --- | --- | --- | --- | --- | --- | --- |
| Serial | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| USB | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

The following table provides a description for each port you can redirect:

| Port type | Description |
| --- | --- |
| [Serial](device-audio-folder-redirection-teams) | Redirect serial (COM) ports on the local device to the remote session. |
| [USB](device-audio-folder-redirection-teams) | Redirect supported USB devices on the local device to the remote session. |

### Other redirection

The following table shows which other features you can redirect:

| Feature | Windows | macOS | iOS/iPadOS | Android/Chrome OS | Webbrowser | MetaQuest |
| --- | --- | --- | --- | --- | --- | --- |
| Clipboard - bidirectional | ✅ | ✅ | ✅¹ | ✅² | ✅² | ✅² |
| Clipboard - unidirectional³ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ |
| Location | ✅⁴ | ❌ | ✅ | ✅ | ✅ | ❌ |
| Third-party virtual channel plugins | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Time zone | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| WebAuthn | ✅ | ✅⁵ | ✅⁵ | ✅⁵ | ❌ | ❌ |
| Screen capture | ❌ | ✅⁶ | ❌ | ❌ | ❌ | ❌ |

1. Text and images only.
2. Text only.
3. macOS support is native in Windows App. All other platforms require remote session configuration. For more information, see [Configure the clipboard transfer direction and types of data that can be copied](/en-us/azure/virtual-desktop/clipboard-transfer-direction-data-types).
4. From a local device running Windows 11 only.
5. Requires the following versions of Windows App.
    1. macOS: In preview, using version 11.4.2 or higher. WebAuthn redirection is only supported for Windows 365 and Azure Virtual Desktop connections. Only passkey sign-ins to Entra ID (both login.microsoftonline.com and login.microsoftonline.us) are currently supported. You can turn on WebAuthn redirection for RemoteApps through the Windows App's Settings menu, and for desktops through the connection's *Device & Audio* settings.
    2. iOS: In preview, using version 11.3.7 or higher. WebAuthn redirection is only supported for Windows 365 and Azure Virtual Desktop connections. Only passkey sign-ins to Entra ID (both login.microsoftonline.com and login.microsoftonline.us) are currently supported. You can turn on WebAuthn redirection through the Windows App's Settings menu.
    3. Android: In preview, using version 11.0.0.119 or higher. WebAuthn redirection is only supported for Windows 365 and Azure Virtual Desktop connections, and the passkey must be stored on the Android device through a (software-based) passkey provider like Microsoft Authenticator. Using passkeys from other devices (such as a physical security key or through QR code) is not supported. Only passkey sign-ins to Entra ID (both login.microsoftonline.com and login.microsoftonline.us) are currently supported. You can turn on WebAuthn redirection through the Windows App's Settings menu.
6. Screen capture is in preview on macOS.

The following table provides a description for each other redirection feature you can redirect:

| Feature | Description |
| --- | --- |
| [Clipboard - bidirectional](/en-us/azure/virtual-desktop/redirection-configure-clipboard) | Redirect the clipboard on the local device is to the remote session and from the remote session to the local device. |
| [Clipboard - unidirectional](/en-us/azure/virtual-desktop/clipboard-transfer-direction-data-types) | Control the direction in which the clipboard can be used and restrict the types of data that can be copied. |
| [Location](/en-us/azure/virtual-desktop/redirection-configure-location) | The location of the local device can be available in a remote session. |
| Third-party virtual channel plugins | Enables third-party virtual channel plugins to extend Remote Desktop Protocol (RDP) capabilities. |
| Time zone | The time zone of the local device can be available in the remote session. |
| [WebAuthn](/en-us/azure/virtual-desktop/redirection-configure-webauthn) | Authentication requests in the remote session can be redirected to the local device allowing the use of security devices such as Windows Hello for Business or a security key. |

## Localization and languages

The following table shows which locales are available for each platform. The language is set by the language of the local device and isn't set independently.

| Name | Locale code | Windows | macOS | iOS/iPadOS | Android/Chrome OS | Webbrowser | MetaQuest |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Chinese (Simplified, China) | zh-CN | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Chinese (Traditional, Taiwan) | zh-TW | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Czech (Czech Republic) | cs-CZ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Danish (Denmark) | da-DK | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Dutch (Netherlands) | nl-NL | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| English (United Kingdom) | en-GB | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |
| English (United States) | en-US | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Finnish (Finland) | fi-FI | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |
| French (France) | fr-FR | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| German (Germany) | de-DE | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Hungarian (Hungary) | hu-HU | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Indonesian | id-ID | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Italian (Italy) | it-IT | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Japanese (Japan) | ja-JP | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Korean (Korea) | ko-KR | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Norwegian, Bokmål (Norway) | nb-NO | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Polish (Poland) | pl-PL | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Portuguese (Brazil) | pt-BR | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Portuguese (Portugal) | pt-PT | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Romanian (Romania) | ro-RO | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Russian (Russia) | ru-RU | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Spanish (Mexico) | es-MX | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Spanish (Spain) | es-ES | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Swedish (Sweden) | sv-SE | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Turkish (Türkiye) | tr-TR | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |

## Identity

The following table details the identity support available on each platform and provides a description for each identity type:

| Identity type | Description |
| --- | --- |
| [Hybrid identity](/en-us/entra/identity/hybrid/whatis-hybrid-identity) | Users or devices that are created in on-premises Active Directory Domain Services, then synchronized to Microsoft Entra ID. |
| [Cloud-only identity](/en-us/microsoft-365/enterprise/manage-microsoft-365-accounts#cloud-only) | Users or devices that are created and only exist in Microsoft Entra ID. |
| [Federated identity](/en-us/entra/identity/devices/device-join-plan#federated-environment) | Users that are created in a third-party identity provider, other than Microsoft Entra ID or Active Directory Domain Services, then federated with Microsoft Entra ID. |
| [External identity](/en-us/entra/external-id/identity-providers) | Users who are created and managed outside of your Microsoft Entra tenant but are invited in to your Microsoft Entra tenant to access your organization's resources. |

| Identity type | Windows | macOS | iOS/iPadOS | Android/Chrome OS | Webbrowser | MetaQuest |
| --- | --- | --- | --- | --- | --- | --- |
| Hybrid identity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Cloud-only identity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Federated identity | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| External identity | ✅¹ | ✅¹ | ✅¹ | ✅¹ | ✅¹ | ❌ |

1. Requires the following versions of Windows App. For more information, see [External identity](/en-us/windows-365/enterprise/identity-authentication#external-identity-preview).
    1. Windows: To successfully sign in to Microsoft Azure for US Government as an external identity, you can do so in one of two ways:
        - Sign in using the steps from [Add a work or school account](user-account-settings-add-remove-manage?tabs=windows#add-a-work-or-school-account) with your user account.
        - Configure the following registry key on the Windows device running the Windows App to **Sign in with another account for US government** when using the [Add a work or school account](user-account-settings-add-remove-manage?tabs=windows#add-a-work-or-school-account)flow:
            - Registry Hive: HKEY\_CURRENT\_USER
            - Registry Path: SOFTWARE\Microsoft\WindowsApp
            - Value Name: EnableGovernmentNationalCloudSignInOption
            - Value Type: DWORD
            - Enabled Value: 1 (for US Government)
            - Disabled Value: 0 (default)
    2. Web browser: Generally available, using latest version of the browser.
    3. macOS: Generally available, using version 11.4.2 or higher.
    4. iOS: In preview, using version 11.3.7 or higher. Account type limitations:
        - You can only sign in as an external identity that is a work or school account, or that is a Microsoft account that is signed into Authenticator as a 'Connected account'.
    5. Android/Chrome OS: Generally available, using version 11.0.0.119 or higher of Windows App. Account type limitations:
        - You can only sign in as an external identity that is a work or school account, or that is a Microsoft account that is signed into Authenticator as a 'Connected account'.
    6. If your administrator sent you a `https://myapplications.microsoft.com/` redemption link with the `domain_hint` parameter, enter that link and redeem your invite in a web browser before signing into the Windows App.

## Authentication

The following sections detail the authentication support available on each platform and the following table provides a description for each credential type:

| Credential type | Description |
| --- | --- |
| [Passkeys (FIDO2)](/en-us/entra/identity/authentication/concept-authentication-passwordless#passkeys-fido2) | Passkeys provide a standards-based passwordless authentication method that comes in many form factors, including FIDO2 security keys. Passkeys incorporate the web authentication (WebAuthn) standard. |
| [Microsoft Authenticator](/en-us/entra/identity/authentication/howto-authentication-passwordless-phone) | The Microsoft Authenticator app helps sign in to Microsoft Entra ID without using a password, or provides an additional verification option for multifactor authentication. Microsoft Authenticator uses key-based authentication to enable a user credential that is tied to a device, where the device uses a PIN or biometric. |
| [Windows Hello for Business certificate trust](/en-us/windows/security/identity-protection/hello-for-business/#comparing-key-based-and-certificate-based-authentication) | Uses an enterprise managed public key infrastructure (PKI) for issuing and managing end user certificates. |
| [Windows Hello for Business cloud trust](/en-us/windows/security/identity-protection/hello-for-business/#comparing-key-based-and-certificate-based-authentication) | Uses Microsoft Entra Kerberos, which enables a simpler deployment when compared to the key trust model. |
| [Windows Hello for Business key trust](/en-us/windows/security/identity-protection/hello-for-business/#comparing-key-based-and-certificate-based-authentication) | Uses hardware-bound keys created during the provisioning experience. |

### Cloud service authentication

The authentication to the service, which includes subscribing to your resources and authenticating to the Gateway, is with Microsoft Entra ID. For more information about the service components of Azure Virtual Desktop, see [Azure Virtual Desktop service architecture and resilience](/en-us/azure/virtual-desktop/service-architecture-resilience).

The following table shows which credential types are available for each platform:

| Credential type | Windows | macOS | iOS/iPadOS | Android/Chrome OS | Webbrowser | MetaQuest |
| --- | --- | --- | --- | --- | --- | --- |
| Passkeys (FIDO2) | ✅ | ✅¹ | ✅¹ | ✅¹ | ✅ | ❌ |
| Microsoft Authenticator | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Password | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Smart card with Active Directory Federation Services | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ |
| Smart card with Microsoft Entra certificate-based authentication | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ |
| Windows Hello for Business certificate trust | ✅ | ❌ | ❌ | ❌ | ✅³ | ❌ |
| Windows Hello for Business cloud trust | ✅ | ❌ | ❌ | ❌ | ✅³ | ❌ |
| Windows Hello for Business key trust | ✅ | ❌ | ❌ | ❌ | ✅³ | ❌ |

1. Requires the following versions of Windows App. For more information, see [Support for FIDO2 authentication with Microsoft Entra ID](/en-us/entra/identity/authentication/concept-fido2-compatibility#native-application-support).
    1. macOS: version 10.9.10 (2291) or later.
    2. iOS: version 10.5.2 (179) or later.
    3. Android: version 1.0.0.152 or later.
2. Available when using a web browser on a local Windows device only.

### Remote session authentication

When connecting to a remote session, there are multiple ways to authenticate. If single sign-on (SSO) is enabled, the credentials used to sign into the cloud service are automatically passed through when connecting to the remote session. The following table shows which types of credential that can be used to authenticate to the remote session if single sign-on is disabled:

| Credential type | Windows | macOS | iOS/iPadOS | Android/Chrome OS | Webbrowser | MetaQuest |
| --- | --- | --- | --- | --- | --- | --- |
| Passkeys (FIDO2) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Microsoft Authenticator | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Password | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Smart card | ✅¹ | ✅² | ❌ | ❌ | ❌ | ❌ |
| Windows Hello for Business certificate trust | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Windows Hello for Business cloud trust | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Windows Hello for Business key trust | ✅³ | ❌ | ❌ | ❌ | ❌ | ❌ |

1. Requires smart card redirection.
2. Requires smart card redirection with Network Level Authentication (NLA) disabled.
3. Requires a [certificate for Remote Desktop Protocol (RDP) sign-in](/en-us/windows/security/identity-protection/hello-for-business/hello-deployment-rdp-certs).

### In-session authentication

The following table shows which types of credential are available when authenticating within a remote session:

| Credential type | Windows | macOS | iOS/iPadOS | Android/Chrome OS | Webbrowser | MetaQuest |
| --- | --- | --- | --- | --- | --- | --- |
| Passkeys (FIDO2) | ✅¹ | ✅¹ | ✅¹ | ✅¹ | ❌ | ❌ |
| Password | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Smart card | ✅² | ✅² | ❌ | ❌ | ❌ | ❌ |
| Windows Hello for Business certificate trust | ✅¹ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Windows Hello for Business cloud trust | ✅¹ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Windows Hello for Business key trust | ✅¹ | ❌ | ❌ | ❌ | ❌ | ❌ |

1. Requires WebAuthn redirection.
2. Requires smart card redirection.

## Security

The following table shows which security features are available on each platform:

| Feature | Windows | macOS | iOS/iPadOS | Android/Chrome OS | Webbrowser |
| --- | --- | --- | --- | --- | --- |
| Screen capture protection | ✅ | ✅ | ✅¹ | ✅¹ | ❌ |
| Watermarking | ✅ | ✅ | ✅ | ✅ | ✅ |
| Input Protection | ✅³ | ❌ | ❌ | ❌ | ❌ |
| Display Protection | ✅³ | ❌ | ❌ | ❌ | ❌ |
| Token protection | ✅² | ❌ | ❌ | ❌ | ❌ |

1. Requires [Microsoft Intune Mobile Application Management](/en-us/windows-app/require-device-security-compliance-intune). Not available for Chrome OS.
2. Requires Windows App on Windows version 2.0.379.0 or later. For more information, see [Microsoft Entra Conditional Access token protection](/en-us/entra/identity/conditional-access/concept-token-protection).
3. In preview. Available only when you connect to Windows 365 or Azure Virtual Desktop, and requires Windows App on Windows version 2.0.1236.0 or later together with Cloud PC or session host configuration. Input Protection also requires the Windows Cloud Input Protect MSI on the device. Not applicable to Microsoft Dev Box.

The following table provides a description for each security feature:

::: zone pivot="azure-virtual-desktop"

| Feature | Description |
| --- | --- |
| [Screen capture protection](/en-us/azure/virtual-desktop/screen-capture-protection) | Helps prevent sensitive information in the remote session from being screen captured from the physical device. Requires session host configuration. |
| [Watermarking](/en-us/azure/virtual-desktop/watermarking) | Helps protect sensitive information from being stolen or altered. |
| [Input Protection](/en-us/windows-365/enterprise/windows-cloud-input-protection) | Helps protect keyboard input in the remote session from keyloggers on the physical device by routing keystrokes through a protected channel. In preview. Requires session host configuration and the Windows Cloud Input Protect MSI on the device. |
| [Display Protection](/en-us/windows-365/enterprise/windows-cloud-display-protection) | Helps prevent the remote session's display output from being captured or recorded on the physical device. In preview. Requires session host configuration. |

::: zone-end

::: zone pivot="windows-365"

| Feature | Description |
| --- | --- |
| [Screen capture protection](/en-us/azure/virtual-desktop/screen-capture-protection?context=%2Fwindows-365%2Fcontext%2Fpr-context) | Helps prevent sensitive information in the remote session from being screen captured from the physical device. Requires Cloud PC configuration. |
| [Watermarking](/en-us/azure/virtual-desktop/watermarking?context=%2Fwindows-365%2Fcontext%2Fpr-context) | Helps protect sensitive information from being stolen or altered. |
| [Input Protection](/en-us/windows-365/enterprise/windows-cloud-input-protection) | Helps protect keyboard input in the remote session from keyloggers on the physical device by routing keystrokes through a protected channel. In preview. Requires Cloud PC configuration and the Windows Cloud Input Protect MSI on the device. |
| [Display Protection](/en-us/windows-365/enterprise/windows-cloud-display-protection) | Helps prevent the remote session's display output from being captured or recorded on the physical device. In preview. Requires Cloud PC configuration. |

::: zone-end

::: zone pivot="dev-box"

| Feature | Description |
| --- | --- |
| [Screen capture protection](/en-us/azure/virtual-desktop/screen-capture-protection?context=%2Fwindows-365%2Fcontext%2Fpr-context) | Helps prevent sensitive information in the remote session from being screen captured from the physical device. Requires dev box configuration. |
| [Watermarking](/en-us/azure/virtual-desktop/watermarking?context=%2Fwindows-365%2Fcontext%2Fpr-context) | Helps protect sensitive information from being stolen or altered. |

::: zone-end

## Network

The following table shows which network features are available on each platform:

::: zone pivot="azure-virtual-desktop"

| Feature | Windows | macOS | iOS/iPadOS | Android/Chrome OS | Webbrowser | MetaQuest |
| --- | --- | --- | --- | --- | --- | --- |
| Connection information | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ |
| RDP Shortpath for managed networks | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| RDP Shortpath for public networks (STUN) | ✅ | ✅³ | ❌ | ✅ | ❌ | ✅ |
| RDP Shortpath for public networks (TURN) | ✅ | ✅³ | ❌ | ✅ | ❌ | ✅ |
| RDP Multipath with UDP | ✅¹ | ✅³ | ❌ | ❌ | ❌ | ❌ |
| RDP Multipath with UDP and TCP | ✅² | ❌ | ❌ | ❌ | ❌ | ❌ |
| Private Link | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |

1. Requires Windows App, version 2.0.559.0 or later.
2. Requires Windows App, version 2.0.1069.0 or later.
3. Requires Windows App for macOS, [Beta version 11.3.8 (3048)](https://install.appcenter.ms/orgs/rdmacios-k2vy/apps/microsoft-remote-desktop-for-mac/distribution_groups/udp%20test)

::: zone-end

::: zone pivot="windows-365,dev-box"

| Feature | Windows | macOS | iOS/iPadOS | Android/Chrome OS | Webbrowser | MetaQuest |
| --- | --- | --- | --- | --- | --- | --- |
| Connection information | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ |
| RDP Shortpath for managed networks | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| RDP Shortpath for public networks (STUN) | ✅ | ✅³ | ❌ | ✅ | ❌ | ✅ |
| RDP Shortpath for public networks (TURN) | ✅ | ✅³ | ❌ | ✅ | ❌ | ✅ |
| RDP Multipath with UDP | ✅¹ | ✅³ | ❌ | ❌ | ❌ | ❌ |
| RDP Multipath with UDP and TCP | ✅² | ❌ | ❌ | ❌ | ❌ | ❌ |
| Private Link | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |

1. Requires Windows App, version 2.0.559.0 or later.
2. Requires Windows App, version 2.0.1069.0 or later.
3. Requires Windows App for macOS, [Beta version 11.3.8 (3048)](https://install.appcenter.ms/orgs/rdmacios-k2vy/apps/microsoft-remote-desktop-for-mac/distribution_groups/udp%20test)

::: zone-end

The following table provides a description for each network feature:

::: zone pivot="azure-virtual-desktop"

| Feature | Description |
| --- | --- |
| Connection information | See the connection information of the remote session. |
| [RDP Shortpath for managed networks](/en-us/azure/virtual-desktop/rdp-shortpath?tabs=managed-networks) | Better connection reliability and more consistent latency through direct UDP-based transport on a private/managed network connection. |
| [RDP Shortpath for public networks](/en-us/azure/virtual-desktop/rdp-shortpath?tabs=public-networks) | Better connection reliability and more consistent latency through direct UDP-based transport on a public network connection. |
| [RDP Multipath](/en-us/azure/virtual-desktop/rdp-multipath) | RDP Multipath maintains reliable connectivity by using multiple network paths at the same time, helping minimize disruptions and improve user experience during network issues. |
| [Private Link](/en-us/azure/virtual-desktop/private-link-overview) | Connect a remote session over a private connection. |

::: zone-end

::: zone pivot="windows-365"

| Feature | Description |
| --- | --- |
| Connection information | See the connection information of the remote session. |
| [RDP Shortpath for managed networks](/en-us/windows-365/enterprise/rdp-shortpath-private-networks) | Better connection reliability and more consistent latency through direct UDP-based transport on a private/managed network connection. |
| [RDP Shortpath for public networks](/en-us/windows-365/enterprise/rdp-shortpath-public-networks) | Better connection reliability and more consistent latency through direct UDP-based transport on a public network connection. |
| [RDP Multipath](/en-us/windows-365/enterprise/rdp-multipath) | RDP Multipath maintains reliable connectivity by using multiple network paths at the same time, helping minimize disruptions and improve user experience during network issues. |

::: zone-end

::: zone pivot="dev-box"

| Feature | Description |
| --- | --- |
| Connection information | See the connection information of the remote session. |
| RDP Shortpath for managed networks | Better connection reliability and more consistent latency through direct UDP-based transport on a private/managed network connection. |
| RDP Shortpath for public networks | Better connection reliability and more consistent latency through direct UDP-based transport on a public network connection. |
| RDP Multipath | RDP Multipath maintains reliable connectivity by using multiple network paths at the same time, helping minimize disruptions and improve user experience during network issues. |

::: zone-end

## Intune mobile application management

The following table shows which Windows App settings you can manage centrally using Microsoft Intune mobile application management (MAM). To learn more, see [Manage local device redirection settings with Microsoft Intune](manage-device-redirection-intune).

| Setting | Windows | macOS | iOS/iPadOS | Android/Chrome OS | Webbrowser¹ | MetaQuest |
| --- | --- | --- | --- | --- | --- | --- |
| Camera redirection | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ |
| Clipboard redirection | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ |
| Local drive/storage redirection | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ |
| Microphone redirection | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ |
| Printer redirection | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Screen capture protection | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ |

1. Supported for Windows App in a web browser using Microsoft Edge only.