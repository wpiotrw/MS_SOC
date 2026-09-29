---
layout: Conceptual
title: Experience Policy CSP | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-experience
recommendations: true
adobe-target: true
ms.collection:
- tier2
breadcrumb_path: /windows/resources/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Windows
audience: ITPro
ms.service: windows-client
ms.subservice: itpro-manage
ms.topic: generated-reference
ms.author: odocspr
author: officedocspr5
manager: bpardi
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/windows/send-feedback-to-microsoft-with-the-feedback-hub-app-f59187f8-8739-22d6-ba93-f66612949332
description: Learn more about the Experience Area in Policy CSP.
ms.date: 2026-09-10T00:00:00.0000000Z
locale: en-us
document_id: 6e8ecbe3-ba72-ec44-0591-7f604d50b1e3
document_version_independent_id: 9d5ff118-d539-dd6e-ae3e-102392c22287
original_content_git_url: https://github.com/MicrosoftDocs/windows-docs-pr/blob/live/windows/client-management/mdm/policy-csp-experience.md
site_name: Docs
depot_name: TechNet.win-client-management
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/TechNet.win-client-management/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: mdm/policy-csp-experience
moniker_range_name: 
monikers: []
item_type: Content
source_path: windows/client-management/mdm/policy-csp-experience.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/e0ffb20c-01c6-407b-a9bd-29111652a1dc
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/3904bce4-d817-48cf-85fd-b6146fca83b7
platformId: 04c28dcf-0af9-a403-ea88-72e510dcd379
---

# Experience Policy CSP | Microsoft Learn

![Logo of Windows Insider.](images/insider.png)

Important

This CSP contains some settings that are under development and only applicable for [Windows Insider Preview builds](/en-us/windows-insider/). These settings are subject to change and may have dependencies on other features or services in preview.

## AllowClipboardHistory

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1809 [10.0.17763] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/AllowClipboardHistory
```

This policy setting determines whether history of Clipboard contents can be stored in memory.

- If you enable this policy setting, history of Clipboard contents are allowed to be stored.
- If you disable this policy setting, history of Clipboard contents aren't allowed to be stored.

Policy change takes effect immediately.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Not allowed. |
| 1 (Default) | Allowed. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AllowClipboardHistory |
| Friendly Name | Allow Clipboard History |
| Location | Computer Configuration |
| Path | System &gt; OS Policies |
| Registry Key Name | Software\Policies\Microsoft\Windows\System |
| Registry Value Name | AllowClipboardHistory |
| ADMX File Name | OSPolicy.admx |

**Validate**:

1. Configure Experience/AllowClipboardHistory to 0.
2. Open Notepad (or any editor app), select a text, and copy it to the clipboard.
3. Press Win+V to open the clipboard history UI.
4. You shouldn't see any clipboard item including current item you copied.
5. The setting under Settings App -&gt; System -&gt; Clipboard should be grayed out with policy warning.

## AllowCopyPaste

Note

This policy is deprecated and may be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | Not applicable | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/AllowCopyPaste
```

This policy is deprecated.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Not allowed. |
| 1 (Default) | Allowed. |

## AllowCortana

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/AllowCortana
```

This policy setting specifies whether Cortana is allowed on the device.

- If you enable or don't configure this setting, Cortana will be allowed on the device.
- If you disable this setting, Cortana will be turned off.

When Cortana is off, users will still be able to use search to find things on the device.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Not allowed. |
| 1 (Default) | Allowed. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AllowCortana |
| Friendly Name | Allow Cortana |
| Location | Computer Configuration |
| Path | Windows Components &gt; Search |
| Registry Key Name | SOFTWARE\Policies\Microsoft\Windows\Windows Search |
| Registry Value Name | AllowCortana |
| ADMX File Name | Search.admx |

## AllowDeviceDiscovery

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/AllowDeviceDiscovery
```

Allows users to turn on/off device discovery UX. When set to 0 , the projection pane is disabled. The Win+P and Win+K shortcut keys won't work on. Most restricted value is 0.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Disabled. |
| 1 (Default) | Enabled. |

## AllowFindMyDevice

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/AllowFindMyDevice
```

This policy turns on Find My Device.

When Find My Device is on, the device and its location are registered in the cloud so that the device can be located when the user initiates a Find command from account.microsoft.com. On devices that are compatible with active digitizers, enabling Find My Device will also allow the user to view the last location of use of their active digitizer on their device; this location is stored locally on the user's device after each use of their active digitizer.

When Find My Device is off, the device and its location aren't registered and the Find My Device feature won't work. The user will also not be able to view the location of the last use of their active digitizer on their device.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Not allowed. |
| 1 (Default) | Allowed. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | FindMy\_AllowFindMyDeviceConfig |
| Friendly Name | Turn On/Off Find My Device |
| Location | Computer Configuration |
| Path | Windows Components &gt; Find My Device |
| Registry Key Name | SOFTWARE\Policies\Microsoft\FindMyDevice |
| Registry Value Name | AllowFindMyDevice |
| ADMX File Name | FindMy.admx |

## AllowManualMDMUnenrollment

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/AllowManualMDMUnenrollment
```

Specifies whether to allow the user to delete the workplace account using the workplace control panel. If the device is Microsoft Entra joined and MDM enrolled (e. g. auto-enrolled), then disabling the MDM unenrollment has no effect.

Note

The MDM server can always remotely delete the account. Most restricted value is 0.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Not allowed. |
| 1 (Default) | Allowed. |

## AllowSaveAsOfOfficeFiles

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/AllowSaveAsOfOfficeFiles
```

This policy is deprecated.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Not allowed. |
| 1 (Default) | Allowed. |

## AllowScreenCapture

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/AllowScreenCapture
```

Allow screen capture.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Not allowed. |
| 1 (Default) | Allowed. |

## AllowScreenRecorder

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ❌ Device  ✅ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 [10.0.26100] and later |

```User
./User/Vendor/MSFT/Policy/Config/Experience/AllowScreenRecorder
```

This policy setting allows you to control whether screen recording functionality is available in the Windows Snipping Tool app.

- If you disable this policy setting, screen recording functionality won't be accessible in the Windows Snipping Tool app.
- If you enable or don't configure this policy setting, users will be able to access screen recording functionality.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Disabled. |
| 1 (Default) | Enabled. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AllowScreenRecorder |
| Friendly Name | Allow Screen Recorder |
| Location | User Configuration |
| Path | Windows Components &gt; Snipping Tool |
| Registry Key Name | Software\Microsoft\Windows\CurrentVersion\Policies\SnippingTool |
| Registry Value Name | AllowScreenRecorder |
| ADMX File Name | Programs.admx |

## AllowSharingOfOfficeFiles

Note

This policy is deprecated and may be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/AllowSharingOfOfficeFiles
```

This policy is deprecated.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Not allowed. |
| 1 (Default) | Allowed. |

## AllowSIMErrorDialogPromptWhenNoSIM

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/AllowSIMErrorDialogPromptWhenNoSIM
```

Allow SIM error dialog prompts when no SIM is inserted.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Not allowed. |
| 1 (Default) | Allowed. |

## AllowSpotlightCollection

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ❌ Device  ✅ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 21H2 [10.0.22000] and later |

```User
./User/Vendor/MSFT/Policy/Config/Experience/AllowSpotlightCollection
```

Specifies whether Spotlight collection is allowed as a Personalization-&gt;Background Setting.

- If you enable this policy setting, Spotlight collection will show as an option in the user's Personalization Settings, and the user will be able to get daily images from Microsoft displayed on their desktop.
- If you disable this policy setting, Spotlight collection won't show as an option in Personalization Settings, and the user won't have the choice of getting Microsoft daily images shown on their desktop.

The following list shows the supported values:

- When set to 0, Spotlight collection will not show as an option in Personalization Settings and therefore be unavailable on Desktop.
- When set to 1 (default), Spotlight collection will show as an option in Personalization Settings and therefore be available on Desktop, allowing Desktop to refresh for daily images from Microsoft.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[0-1]` |
| Default Value | 1 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisableSpotlightCollectionOnDesktop |
| Friendly Name | Turn off Spotlight collection on Desktop |
| Location | User Configuration |
| Path | Windows Components &gt; Cloud Content |
| Registry Key Name | Software\Policies\Microsoft\Windows\CloudContent |
| Registry Value Name | DisableSpotlightCollectionOnDesktop |
| ADMX File Name | CloudContent.admx |

## AllowSyncMySettings

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/AllowSyncMySettings
```

Allows or disallows all Windows sync settings on the device. For information about what settings are sync'ed, see [About sync setting on Windows 10 devices](https://windows.microsoft.com/windows-10/about-sync-settings-on-windows-10-devices).

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Sync settings aren't allowed. |
| 1 (Default) | Sync settings allowed. |

## AllowTailoredExperiencesWithDiagnosticData

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ❌ Device  ✅ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```User
./User/Vendor/MSFT/Policy/Config/Experience/AllowTailoredExperiencesWithDiagnosticData
```

This policy allows you to prevent Windows from using diagnostic data to provide customized experiences to the user.

- If you enable this policy setting, Windows won't use diagnostic data from this device to customize content shown on the lock screen, Windows tips, Microsoft consumer features, or other related features. If these features are enabled, users will still see recommendations, tips and offers, but they may be less relevant.
- If you disable or don't configure this policy setting, Microsoft will use diagnostic data to provide personalized recommendations, tips, and offers to tailor Windows for the user's needs and make it work better for them. Diagnostic data can include browser, app and feature usage, depending on the Diagnostic and usage data setting value.

Note

This setting doesn't control Cortana cutomized experiences because there are separate policies to configure it. Most restricted value is 0.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |
| Dependency [Experience\_AllowTailoredExperiencesWithDiagnosticData\_DependencyGroup] | Dependency Type: `DependsOn` Dependency URI: `User/Vendor/MSFT/Policy/Config/Experience/AllowWindowsSpotlight` Dependency Allowed Value: `[1]` Dependency Allowed Value Type: `Range` |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Not allowed. |
| 1 (Default) | Allowed. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisableTailoredExperiencesWithDiagnosticData |
| Friendly Name | Do not use diagnostic data for tailored experiences |
| Location | User Configuration |
| Path | Windows Components &gt; Cloud Content |
| Registry Key Name | Software\Policies\Microsoft\Windows\CloudContent |
| Registry Value Name | DisableTailoredExperiencesWithDiagnosticData |
| ADMX File Name | CloudContent.admx |

## AllowTaskSwitcher

Note

This policy is deprecated and may be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | Not applicable | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/AllowTaskSwitcher
```

This policy is deprecated.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Not allowed. |
| 1 (Default) | Allowed. |

## AllowThirdPartySuggestionsInWindowsSpotlight

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ❌ Device  ✅ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```User
./User/Vendor/MSFT/Policy/Config/Experience/AllowThirdPartySuggestionsInWindowsSpotlight
```

Specifies whether to allow app and content suggestions from third-party software publishers in Windows spotlight features like lock screen spotlight, suggested apps in the Start menu, and Windows tips. Users may still see suggestions for Microsoft features, apps, and services.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |
| Dependency [Experience\_AllowThirdPartySuggestionsInWindowsSpotlight\_DependencyGroup] | Dependency Type: `DependsOn` Dependency URI: `User/Vendor/MSFT/Policy/Config/Experience/AllowWindowsSpotlight` Dependency Allowed Value: `[1]` Dependency Allowed Value Type: `Range` |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Third-party suggestions not allowed. |
| 1 (Default) | Third-party suggestions allowed. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisableThirdPartySuggestions |
| Friendly Name | Do not suggest third-party content in Windows spotlight |
| Location | User Configuration |
| Path | Windows Components &gt; Cloud Content |
| Registry Key Name | Software\Policies\Microsoft\Windows\CloudContent |
| Registry Value Name | DisableThirdPartySuggestions |
| ADMX File Name | CloudContent.admx |

## AllowVoiceRecording

Note

This policy is deprecated and may be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | Not applicable | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/AllowVoiceRecording
```

This policy is deprecated.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Not allowed. |
| 1 (Default) | Allowed. |

## AllowWindowsConsumerFeatures

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/AllowWindowsConsumerFeatures
```

Prior to Windows 10, version 1803, this policy had User scope. This policy allows IT admins to turn on experiences that are typically for consumers only, such as Start suggestions, Membership notifications, Post-OOBE app install and redirect tiles. Most restricted value is 0.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |
| Dependency [Experience\_AllowWindowsConsumerFeatures\_DependencyGroup] | Dependency Type: `DependsOn` Dependency URI: `User/Vendor/MSFT/Policy/Config/Experience/AllowWindowsSpotlight` Dependency Allowed Value: `[1]` Dependency Allowed Value Type: `Range` |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Not allowed. |
| 1 (Default) | Allowed. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisableWindowsConsumerFeatures |
| Friendly Name | Turn off Microsoft consumer experiences |
| Location | Computer Configuration |
| Path | Windows Components &gt; Cloud Content |
| Registry Key Name | Software\Policies\Microsoft\Windows\CloudContent |
| Registry Value Name | DisableWindowsConsumerFeatures |
| ADMX File Name | CloudContent.admx |

## AllowWindowsSpotlight

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ❌ Device  ✅ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```User
./User/Vendor/MSFT/Policy/Config/Experience/AllowWindowsSpotlight
```

Specifies whether to turn off all Windows spotlight features at once.

- If you enable this policy setting, Windows spotlight on lock screen, Windows Tips, Microsoft consumer features and other related features will be turned off. You should enable this policy setting if your goal is to minimize network traffic from target devices.
- If you disable or don't configure this policy setting, Windows spotlight features are allowed and may be controlled individually using their corresponding policy settings. Most restricted value is 0.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Not allowed. |
| 1 (Default) | Allowed. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisableWindowsSpotlightFeatures |
| Friendly Name | Turn off all Windows spotlight features |
| Location | User Configuration |
| Path | Windows Components &gt; Cloud Content |
| Registry Key Name | Software\Policies\Microsoft\Windows\CloudContent |
| Registry Value Name | DisableWindowsSpotlightFeatures |
| ADMX File Name | CloudContent.admx |

## AllowWindowsSpotlightOnActionCenter

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ❌ Device  ✅ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```User
./User/Vendor/MSFT/Policy/Config/Experience/AllowWindowsSpotlightOnActionCenter
```

This policy allows administrators to prevent Windows spotlight notifications from being displayed in the Action Center.

- If you enable this policy, Windows spotlight notifications will no longer be displayed in the Action Center.
- If you disable or don't configure this policy, Microsoft may display notifications in the Action Center that will suggest apps or features to help users be more productive on Windows. Most restricted value is 0.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |
| Dependency [Experience\_AllowWindowsSpotlightOnActionCenter\_DependencyGroup] | Dependency Type: `DependsOn` Dependency URI: `User/Vendor/MSFT/Policy/Config/Experience/AllowWindowsSpotlight` Dependency Allowed Value: `[1]` Dependency Allowed Value Type: `Range` |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Not allowed. |
| 1 (Default) | Allowed. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisableWindowsSpotlightOnActionCenter |
| Friendly Name | Turn off Windows Spotlight on Action Center |
| Location | User Configuration |
| Path | Windows Components &gt; Cloud Content |
| Registry Key Name | Software\Policies\Microsoft\Windows\CloudContent |
| Registry Value Name | DisableWindowsSpotlightOnActionCenter |
| ADMX File Name | CloudContent.admx |

## AllowWindowsSpotlightOnSettings

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ❌ Device  ✅ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1803 [10.0.17134] and later |

```User
./User/Vendor/MSFT/Policy/Config/Experience/AllowWindowsSpotlightOnSettings
```

This policy allows IT admins to turn off Suggestions in Settings app. These suggestions from Microsoft may show after each OS clean install, upgrade or an on-going basis to help users discover apps/features on Windows or across devices, to make their experience productive. User setting is under Settings -&gt; Privacy -&gt; General -&gt; Show me suggested content in Settings app. User Setting is changeable on a per user basis. If the Group policy is set to off, no suggestions will be shown to the user in Settings app.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Not allowed. |
| 1 (Default) | Allowed. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisableWindowsSpotlightOnSettings |
| Friendly Name | Turn off Windows Spotlight on Settings |
| Location | User Configuration |
| Path | Windows Components &gt; Cloud Content |
| Registry Key Name | Software\Policies\Microsoft\Windows\CloudContent |
| Registry Value Name | DisableWindowsSpotlightOnSettings |
| ADMX File Name | CloudContent.admx |

## AllowWindowsSpotlightWindowsWelcomeExperience

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ❌ Device  ✅ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```User
./User/Vendor/MSFT/Policy/Config/Experience/AllowWindowsSpotlightWindowsWelcomeExperience
```

This policy setting lets you turn off the Windows spotlight Windows welcome experience feature. The Windows welcome experience feature introduces onboard users to Windows; for example, launching Microsoft Edge with a webpage that highlights new features.

- If you enable this policy, the Windows welcome experience will no longer be displayed when there are updates and changes to Windows and its apps.
- If you disable or don't configure this policy, the Windows welcome experience will be launched to inform onboard users about what's new, changed, and suggested. Most restricted value is 0.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |
| Dependency [Experience\_AllowWindowsSpotlightWindowsWelcomeExperience\_DependencyGroup] | Dependency Type: `DependsOn` Dependency URI: `User/Vendor/MSFT/Policy/Config/Experience/AllowWindowsSpotlight` Dependency Allowed Value: `[1]` Dependency Allowed Value Type: `Range` |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Not allowed. |
| 1 (Default) | Allowed. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisableWindowsSpotlightWindowsWelcomeExperience |
| Friendly Name | Turn off the Windows Welcome Experience |
| Location | User Configuration |
| Path | Windows Components &gt; Cloud Content |
| Registry Key Name | Software\Policies\Microsoft\Windows\CloudContent |
| Registry Value Name | DisableWindowsSpotlightWindowsWelcomeExperience |
| ADMX File Name | CloudContent.admx |

## AllowWindowsTips

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/AllowWindowsTips
```

Enables or disables Windows Tips / soft landing.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |
| Dependency [Experience\_AllowWindowsTips\_DependencyGroup] | Dependency Type: `DependsOn` Dependency URI: `User/Vendor/MSFT/Policy/Config/Experience/AllowWindowsSpotlight` Dependency Allowed Value: `[1]` Dependency Allowed Value Type: `Range` |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Disabled. |
| 1 (Default) | Enabled. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisableSoftLanding |
| Friendly Name | Do not show Windows tips |
| Location | Computer Configuration |
| Path | Windows Components &gt; Cloud Content |
| Registry Key Name | Software\Policies\Microsoft\Windows\CloudContent |
| Registry Value Name | DisableSoftLanding |
| ADMX File Name | CloudContent.admx |

## ConfigureChatIcon

Note

This policy is deprecated and may be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 21H2 [10.0.22000] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/ConfigureChatIcon
```

This policy setting allows you to configure the Chat icon on the taskbar.

- If you enable this policy setting and set it to Show, the Chat icon will be displayed on the taskbar by default. Users can show or hide it in Settings.
- If you enable this policy setting and set it to Hide, the Chat icon will be hidden by default. Users can show or hide it in Settings.
- If you enable this policy setting and set it to Disabled, the Chat icon won't be displayed, and users can't show or hide it in Settings.
- If you disable or don't configure this policy setting, the Chat icon will be configured according to the defaults for your Windows edition.

Note

Option 1 (Show) and Option 2 (Hide) only work on the first sign-in attempt. Option 3 (Disabled) works on all attempts.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Not Configured. |
| 1 | Show. |
| 2 | Hide. |
| 3 | Disabled. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | ConfigureChatIcon |
| Friendly Name | Configures the Chat icon on the taskbar |
| Element Name | State. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Chat |
| Registry Key Name | Software\Policies\Microsoft\Windows\Windows Chat |
| ADMX File Name | Taskbar.admx |

## ConfigureWindowsSpotlightOnLockScreen

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ❌ Device  ✅ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```User
./User/Vendor/MSFT/Policy/Config/Experience/ConfigureWindowsSpotlightOnLockScreen
```

This policy setting lets you configure Windows spotlight on the lock screen.

- If you enable this policy setting, "Windows spotlight" will be set as the lock screen provider and users won't be able to modify their lock screen. "Windows spotlight" will display daily images from Microsoft on the lock screen.

Additionally, if you check the "Include content from Enterprise spotlight" checkbox and your organization has setup an Enterprise spotlight content service in Azure, the lock screen will display internal messages and communications configured in that service, when available. If your organization doesn't have an Enterprise spotlight content service, the checkbox will have no effect.

- If you disable this policy setting, Windows spotlight will be turned off and users will no longer be able to select it as their lock screen. Users will see the default lock screen image and will be able to select another image, unless you have enabled the "Prevent changing lock screen image" policy.
- If you don't configure this policy, Windows spotlight will be available on the lock screen and will be selected by default, unless you have configured another default lock screen image using the "Force a specific default lock screen and logon image" policy.

Note

This policy is only available for Enterprise SKUs.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |
| Dependency [Experience\_ConfigureWindowsSpotlightOnLockScreen\_DependencyGroup] | Dependency Type: `DependsOn` Dependency URI: `User/Vendor/MSFT/Policy/Config/Experience/AllowWindowsSpotlight` Dependency Allowed Value: `[1]` Dependency Allowed Value Type: `Range` |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Windows spotlight disabled. |
| 1 (Default) | Windows spotlight enabled. |
| 2 | Windows spotlight is always enabled, the user can't disable it. |
| 3 | Windows spotlight is always enabled, the user can't disable it. For special configurations only. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | ConfigureWindowsSpotlight |
| Friendly Name | Configure Windows spotlight on lock screen |
| Location | User Configuration |
| Path | Windows Components &gt; Cloud Content |
| Registry Key Name | Software\Policies\Microsoft\Windows\CloudContent |
| Registry Value Name | ConfigureWindowsSpotlight |
| ADMX File Name | CloudContent.admx |

## DisableCloudOptimizedContent

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 21H2 [10.0.22000] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/DisableCloudOptimizedContent
```

This policy setting lets you turn off cloud optimized content in all Windows experiences.

- If you enable this policy, Windows experiences that use the cloud optimized content client component, will instead present the default fallback content.
- If you disable or don't configure this policy, Windows experiences will be able to use cloud optimized content.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Disabled. |
| 1 | Enabled. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisableCloudOptimizedContent |
| Friendly Name | Turn off cloud optimized content |
| Location | Computer Configuration |
| Path | Windows Components &gt; Cloud Content |
| Registry Key Name | Software\Policies\Microsoft\Windows\CloudContent |
| Registry Value Name | DisableCloudOptimizedContent |
| ADMX File Name | CloudContent.admx |

## DisableConsumerAccountStateContent

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 21H2 [10.0.22000] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/DisableConsumerAccountStateContent
```

This policy setting lets you turn off cloud consumer account state content in all Windows experiences.

- If you enable this policy, Windows experiences that use the cloud consumer account state content client component, will instead present the default fallback content.
- If you disable or don't configure this policy, Windows experiences will be able to use cloud consumer account state content.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Disabled. |
| 1 | Enabled. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisableConsumerAccountStateContent |
| Friendly Name | Turn off cloud consumer account state content |
| Location | Computer Configuration |
| Path | Windows Components &gt; Cloud Content |
| Registry Key Name | Software\Policies\Microsoft\Windows\CloudContent |
| Registry Value Name | DisableConsumerAccountStateContent |
| ADMX File Name | CloudContent.admx |

## DisableCopilotPinScreen

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows Insider Preview |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/DisableCopilotPinScreen
```

Prevents Windows from showing Microsoft 365 Copilot recommendations at sign-in. This doesn't disable Copilot or affect licensing.

- If you enable this setting, the Microsoft 365 Copilot setup guidance won't appear.
- If you disable or don't configure this setting, the Microsoft 365 Copilot setup guidance may appear.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | M365 Copilot Pinning is enabled. |
| 1 | M365 Copilot Pinning is disabled. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisableCopilotPinScreen |
| Path | CloudContent &gt; AT &gt; WindowsComponents &gt; CloudContent |

## DisableGetStarted

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 with [KB5089573](https://support.microsoft.com/help/5089573) [10.0.26100.8524] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/DisableGetStarted
```

Specifies whether Get Started is disabled for the current user.

- If you enable this setting, Get Started is disabled.
- If you disable or don't configure this setting, Get Started is enabled.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Get Started is enabled. |
| 1 | Get Started is disabled. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisableGetStarted |
| Path | CloudContent &gt; AT &gt; WindowsComponents &gt; CloudContent |

## DisableInlineCompose

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 [10.0.26100] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/DisableInlineCompose
```

This policy controls whether users can compose a message directly in the Share sheet after selecting Outlook.

- If the policy is enabled, Windows hides the message entry field and users must complete message composition within Outlook.
- If the policy is disabled or not configured, Windows may display a message entry field in the Share sheet.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Inline Compose on ShareSheet is Enabled. |
| 1 | Inline Compose on ShareSheet is Disabled. |

## DisableShareAppPromotions

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 [10.0.26100] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/DisableShareAppPromotions
```

This policy setting allow IT admins to control whether promotional apps are displayed in the Share sheet.

- If you enable this policy, Windows won't show promotional apps in the Share sheet.
- If you disable or don't configure this policy, Share sheet may show app suggestions and promotions when the Share sheet is opened.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Promotional Apps on ShareSheet are Enabled. |
| 1 | Promotional Apps on ShareSheet are Disabled. |

## DisableTextTranslation

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 [10.0.26100] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/DisableTextTranslation
```

Allows Text Translation feature to be enabled/disabled.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Enable Text Translation. |
| 1 | Disable Text Translation. |

## DoNotShowFeedbackNotifications

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/DoNotShowFeedbackNotifications
```

This policy setting allows an organization to prevent its devices from showing feedback questions from Microsoft.

- If you enable this policy setting, users will no longer see feedback notifications through the Windows Feedback app.
- If you disable or don't configure this policy setting, users may see notifications through the Windows Feedback app asking users for feedback.

Note

If you disable or don't configure this policy setting, users can control how often they receive feedback questions.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Feedback notifications aren't disabled. The actual state of feedback notifications on the device will then depend on what GP has configured or what the user has configured locally. |
| 1 | Feedback notifications are disabled. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DoNotShowFeedbackNotifications |
| Friendly Name | Do not show feedback notifications |
| Location | Computer Configuration |
| Path | WindowsComponents &gt; Data Collection and Preview Builds |
| Registry Key Name | Software\Policies\Microsoft\Windows\DataCollection |
| Registry Value Name | DoNotShowFeedbackNotifications |
| ADMX File Name | FeedbackNotifications.admx |

## DoNotSyncBrowserSettings

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1809 [10.0.17763] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/DoNotSyncBrowserSettings
```

Prevent the "browser" group from syncing to and from this PC. This turns off and disables the "browser" group on the "sync your settings" page in PC settings. The "browser" group contains settings and info like history and favorites.

If you enable this policy setting, the "browser" group, including info like history and favorites, won't be synced.

Use the option "Allow users to turn browser syncing on" so that syncing is turned off by default but not disabled.

If you don't set or disable this setting, syncing of the "browser" group is on by default and configurable by the user.

Related policy: PreventUsersFromTurningOnBrowserSyncing

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 2 | Disable Syncing. |
| 0 (Default) | Allow syncing. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisableWebBrowserSettingSync |
| Friendly Name | Do not sync browser settings |
| Location | Computer Configuration |
| Path | Windows Components &gt; Sync your settings |
| Registry Key Name | Software\Policies\Microsoft\Windows\SettingSync |
| Registry Value Name | DisableWebBrowserSettingSync |
| ADMX File Name | SettingSync.admx |

***Sync the browser settings automatically***

Set both **DoNotSyncBrowserSettings** and **PreventUsersFromTurningOnBrowserSyncing** to 0 (Allowed/turned on).

***Prevent syncing of browser settings and prevent users from turning it on***

1. Set **DoNotSyncBrowserSettings** to 2 (Prevented/turned off).
2. Set **PreventUsersFromTurningOnBrowserSyncing** to 1 (Prevented/turned off).

***Prevent syncing of browser settings and let users turn on syncing***

1. Set **DoNotSyncBrowserSettings** to 2 (Prevented/turned off).
2. Set **PreventUsersFromTurningOnBrowserSyncing** to 0 (Allowed/turned on).

***Turn syncing off by default but don’t disable***

Set **DoNotSyncBrowserSettings** to 2 (Prevented/turned off) and select the *Allow users to turn “browser” syncing* option.

## EnableOrganizationalMessages

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ❌ Device  ✅ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 22H2 with [KB5041582](https://support.microsoft.com/help/5041582) [10.0.19045.4842] and later  ✅ Windows 11, version 22H2 with [KB5020044](https://support.microsoft.com/help/5020044) [10.0.22621.900] and later  ✅ Windows 11, version 24H2 [10.0.26100] and later |

```User
./User/Vendor/MSFT/Policy/Config/Experience/EnableOrganizationalMessages
```

Organizational messages allow Administrators to deliver messages to their end users on selected Windows 11 experiences. Organizational messages are available to Administrators via services like Microsoft Endpoint Manager. By default, this policy is disabled. If you enable this policy, these experiences will show content booked by Administrators. Enabling this policy will have no impact on existing MDM policy settings governing delivery of content from Microsoft on Windows experiences.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Disabled. |
| 1 | Enabled. |

## PreventUsersFromTurningOnBrowserSyncing

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1809 [10.0.17763] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/PreventUsersFromTurningOnBrowserSyncing
```

By default, the "browser" group syncs automatically between the user's devices, letting users make changes. With this policy though, you can prevent the "browser" group from syncing and prevent users from turning on the **Sync your Settings** toggle in Settings. If you want syncing turned off by default but not disabled, select the **Allow syncing** option in the DoNotSyncBrowserSettings. For this policy to work correctly, you must enable the DoNotSyncBrowserSettings policy.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Allowed/turned on. Users can sync the browser settings. |
| 1 (Default) | Prevented/turned off. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisableWebBrowserSettingSync |
| Friendly Name | Do not sync browser settings |
| Element Name | Allow users to turn "browser" syncing on. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Sync your settings |
| Registry Key Name | Software\Policies\Microsoft\Windows\SettingSync |
| ADMX File Name | SettingSync.admx |

**Examples**:

***Sync the browser settings automatically***

Set both **DoNotSyncBrowserSettings** and **PreventUsersFromTurningOnBrowserSyncing** to 0 (Allowed/turned on).

***Prevent syncing of browser settings and prevent users from turning it on***

1. Set **DoNotSyncBrowserSettings** to 2 (Prevented/turned off).
2. Set **PreventUsersFromTurningOnBrowserSyncing** to 1 (Prevented/turned off).

***Prevent syncing of browser settings and let users turn on syncing***

1. Set **DoNotSyncBrowserSettings** to 2 (Prevented/turned off).
2. Set **PreventUsersFromTurningOnBrowserSyncing** to 0 (Allowed/turned on).

**Validate**:

1. Select **More &gt; Settings**.
2. See, if the setting is enabled or disabled based on your selection.

## ShowLockOnUserTile

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1903 [10.0.18362] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Experience/ShowLockOnUserTile
```

Shows or hides lock from the user tile menu.

- If you enable this policy setting, the lock option will be shown in the User Tile menu.
- If you disable this policy setting, the lock option will never be shown in the User Tile menu.
- If you don't configure this policy setting, users will be able to choose whether they want lock to show through the Power Options Control Panel.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | The lock option isn't displayed in the User Tile menu. |
| 1 (Default) | The lock option is displayed in the User Tile menu. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | ShowLockOption |
| Friendly Name | Show lock in the user tile menu |
| Location | Computer Configuration |
| Path | WindowsComponents &gt; File Explorer |
| Registry Key Name | Software\Policies\Microsoft\Windows\Explorer |
| Registry Value Name | ShowLockOption |
| ADMX File Name | WindowsExplorer.admx |