---
layout: Conceptual
title: Connectivity Policy CSP | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-connectivity
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
description: Learn more about the Connectivity Area in Policy CSP.
ms.date: 2025-03-12T00:00:00.0000000Z
locale: en-us
document_id: 2e70a68f-210c-b27a-3224-2cfd80028e60
document_version_independent_id: c6a94ff0-9ab2-cd09-c053-e09304d0d16a
original_content_git_url: https://github.com/MicrosoftDocs/windows-docs-pr/blob/live/windows/client-management/mdm/policy-csp-connectivity.md
site_name: Docs
depot_name: TechNet.win-client-management
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/TechNet.win-client-management/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: mdm/policy-csp-connectivity
moniker_range_name: 
monikers: []
item_type: Content
source_path: windows/client-management/mdm/policy-csp-connectivity.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/e0ffb20c-01c6-407b-a9bd-29111652a1dc
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/3904bce4-d817-48cf-85fd-b6146fca83b7
platformId: 5f31d39e-b5e6-16a7-4441-55bcd15b7c0f
---

# Connectivity Policy CSP | Microsoft Learn

Tip

This CSP contains ADMX-backed policies which require a special SyncML format to enable or disable. You must specify the data type in the SyncML as `<Format>chr</Format>`. For details, see [Understanding ADMX-backed policies](../understanding-admx-backed-policies).

The payload of the SyncML must be XML-encoded; for this XML encoding, there are a variety of online encoders that you can use. To avoid encoding the payload, you can use CDATA if your MDM supports it. For more information, see [CDATA Sections](http://www.w3.org/TR/REC-xml/#sec-cdata-sect).

![Logo of Windows Insider.](images/insider.png)

Important

This CSP contains some settings that are under development and only applicable for [Windows Insider Preview builds](/en-us/windows-insider/). These settings are subject to change and may have dependencies on other features or services in preview.

## AllowBluetooth

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Connectivity/AllowBluetooth
```

Allows the user to enable Bluetooth or restrict access.

Note

This value isn't supported in Windows Phone 8. 1 MDM and EAS, Windows 10 for desktop, or Windows 10 Mobile. If this isn't set or it's deleted, the default value of 2 (Allow) is used. Most restricted value is 0.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 2 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Disallow Bluetooth. If this is set to 0, the radio in the Bluetooth control panel will be grayed out and the user won't be able to turn Bluetooth on. |
| 2 (Default) | Allow Bluetooth. If this is set to 2, the radio in the Bluetooth control panel will be functional and the user will be able to turn Bluetooth on. |

## AllowCellularData

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Connectivity/AllowCellularData
```

Allows the cellular data channel on the device. Device reboot isn't required to enforce the policy.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Don't allow the cellular data channel. The user can't turn it on. This value isn't supported in Windows 10, version 1511. |
| 1 (Default) | Allow the cellular data channel. The user can turn it off. |
| 2 | Allow the cellular data channel. The user can't turn it off. |

## AllowCellularDataRoaming

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Connectivity/AllowCellularDataRoaming
```

This policy setting prevents clients from connecting to Mobile Broadband networks when the client is registered on a roaming provider network.

- If this policy setting is enabled, all automatic and manual connection attempts to roaming provider networks are blocked until the client registers with the home provider network.
- If this policy setting isn't configured or is disabled, clients are allowed to connect to roaming provider Mobile Broadband networks.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Don't allow cellular data roaming. The user can't turn it on. This value isn't supported in Windows 10, version 1511. |
| 1 (Default) | Allow cellular data roaming. |
| 2 | Allow cellular data roaming on. The user can't turn it off. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | WCM\_DisableRoaming |
| Friendly Name | Prohibit connection to roaming Mobile Broadband networks |
| Location | Computer Configuration |
| Path | Network &gt; Windows Connection Manager |
| Registry Key Name | Software\Policies\Microsoft\Windows\WcmSvc\GroupPolicy |
| Registry Value Name | fBlockRoaming |
| ADMX File Name | WCM.admx |

**Validate**:

To validate, the enterprise can confirm by observing the roaming enable switch in the UX. It will be inactive if the roaming policy is being enforced by the enterprise policy. To validate on a device, perform the following steps:

1. Go to Cellular & SIM.
2. Click on the SIM (next to the signal strength icon) and select **Properties**.
3. On the Properties page, select **Data roaming options**.

## AllowConnectedDevices

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Connectivity/AllowConnectedDevices
```

Note

This policy requires reboot to take effect. Allows IT Admins the ability to disable the Connected Devices Platform (CDP) component. CDP enables discovery and connection to other devices (either proximally with BT/LAN or through the cloud) to support remote app launching, remote messaging, remote app sessions, and other cross-device experiences.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Disable (CDP service not available). |
| 1 (Default) | Allow (CDP service available). |

## AllowNFC

Note

This policy is deprecated and may be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | Not applicable | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Connectivity/AllowNFC
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
| 0 | Disabled. |
| 1 (Default) | Enabled. |

## AllowPhonePCLinking

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1803 [10.0.17134] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Connectivity/AllowPhonePCLinking
```

This policy allows IT admins to turn off the ability to Link a Phone with a PC to continue reading, emailing and other tasks that requires linking between Phone and PC.

- If you enable this policy setting, the Windows device will be able to enroll in Phone-PC linking functionality and participate in Continue on PC experiences.
- If you disable this policy setting, the Windows device isn't allowed to be linked to Phones, will remove itself from the device list of any linked Phones, and can't participate in Continue on PC experiences.
- If you don't configure this policy setting, the default behavior depends on the Windows edition. Changes to this policy take effect on reboot.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Don't link. |
| 1 (Default) | Allow phone-PC linking. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | EnableMMX |
| Friendly Name | Phone-PC linking on this device |
| Location | Computer Configuration |
| Path | System &gt; Group Policy |
| Registry Key Name | Software\Policies\Microsoft\Windows\System |
| Registry Value Name | EnableMmx |
| ADMX File Name | GroupPolicy.admx |

**Validate**:

If the Connectivity/AllowPhonePCLinking policy is configured to value 0, add a phone button in the Phones section in settings will be grayed out and clicking it will not launch the window for a user to enter their phone number.

Device that has previously opt-in to MMX will also stop showing on the device list.

## AllowUSBConnection

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ❌ Enterprise  ❌ Education  ❌ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Connectivity/AllowUSBConnection
```

Note

Currently, this policy is supported only in HoloLens 2, HoloLens (1st gen) Commercial Suite, and HoloLens (1st gen) Development Edition. Enables USB connection between the device and a computer to sync files with the device or to use developer tools to deploy or debug applications. Changing this policy doesn't affect USB charging. Both Media Transfer Protocol (MTP) and IP over USB are disabled when this policy is enforced. Most restricted value is 0.

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

## AllowVPNOverCellular

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Connectivity/AllowVPNOverCellular
```

Specifies what type of underlying connections VPN is allowed to use. Most restricted value is 0.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | VPN isn't allowed over cellular. |
| 1 (Default) | VPN can use any connection, including cellular. |

## AllowVPNRoamingOverCellular

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Connectivity/AllowVPNRoamingOverCellular
```

Prevents the device from connecting to VPN when the device roams over cellular networks. Most restricted value is 0.

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

## DiablePrintingOverHTTP

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1709 [10.0.16299] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Connectivity/DiablePrintingOverHTTP
```

This policy setting specifies whether to allow printing over HTTP from this client.

Printing over HTTP allows a client to print to printers on the intranet as well as the Internet.

Note

This policy setting affects the client side of Internet printing only. It doesn't prevent this computer from acting as an Internet Printing server and making its shared printers available via HTTP.

- If you enable this policy setting, it prevents this client from printing to Internet printers over HTTP.
- If you disable or don't configure this policy setting, users can choose to print to Internet printers over HTTP.

Also, see the "Web-based printing" policy setting in Computer Configuration/Administrative Templates/Printers.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `chr` (string) |
| Access Type | Add, Delete, Get, Replace |

Tip

This is an ADMX-backed policy and requires SyncML format for configuration. For an example of SyncML format, refer to [Enabling a policy](../understanding-admx-backed-policies#enabling-a-policy).

**ADMX mapping**:

| Name | Value |
| --- | --- |
| Name | DisableHTTPPrinting\_2 |
| Friendly Name | Turn off printing over HTTP |
| Location | Computer Configuration |
| Path | InternetManagement &gt; Internet Communication settings |
| Registry Key Name | Software\Policies\Microsoft\Windows NT\Printers |
| Registry Value Name | DisableHTTPPrinting |
| ADMX File Name | ICM.admx |

## DisableCellularOperatorSettingsPage

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows Insider Preview |

```Device
./Device/Vendor/MSFT/Policy/Config/Connectivity/DisableCellularOperatorSettingsPage
```

This policy makes all configurable settings in the 'Cellular' &gt; 'Mobile operator settings' page read-only.

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

## DisableCellularSettingsPage

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows Insider Preview |

```Device
./Device/Vendor/MSFT/Policy/Config/Connectivity/DisableCellularSettingsPage
```

This policy makes all configurable settings in the 'Cellular' Settings page read-only.

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

## DisableCrossDeviceResume

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ❌ Device  ✅ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows Insider Preview |

```User
./User/Vendor/MSFT/Policy/Config/Connectivity/DisableCrossDeviceResume
```

This policy allows IT admins to turn off CrossDeviceResume feature to continue tasks, such as browsing file, continue using 1P/ 3P apps that require linking between Phone and PC.

- If you enable this policy setting, the Windows device won't receive any CrossDeviceResume notification.
- If you disable this policy setting, the Windows device will receive notification to resume activity from linked phone.
- If you don't configure this policy setting, the default behavior is that the CrossDeviceResume feature is turned 'ON'. Changes to this policy take effect on reboot.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | CrossDeviceResume is Enabled. |
| 1 | CrossDeviceResume is Disabled. |

## DisableDownloadingOfPrintDriversOverHTTP

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1709 [10.0.16299] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Connectivity/DisableDownloadingOfPrintDriversOverHTTP
```

This policy setting specifies whether to allow this client to download print driver packages over HTTP.

To set up HTTP printing, non-inbox drivers need to be downloaded over HTTP.

Note

This policy setting doesn't prevent the client from printing to printers on the Intranet or the Internet over HTTP. It only prohibits downloading drivers that aren't already installed locally.

- If you enable this policy setting, print drivers can't be downloaded over HTTP.
- If you disable or don't configure this policy setting, users can download print drivers over HTTP.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `chr` (string) |
| Access Type | Add, Delete, Get, Replace |

Tip

This is an ADMX-backed policy and requires SyncML format for configuration. For an example of SyncML format, refer to [Enabling a policy](../understanding-admx-backed-policies#enabling-a-policy).

**ADMX mapping**:

| Name | Value |
| --- | --- |
| Name | DisableWebPnPDownload\_2 |
| Friendly Name | Turn off downloading of print drivers over HTTP |
| Location | Computer Configuration |
| Path | InternetManagement &gt; Internet Communication settings |
| Registry Key Name | Software\Policies\Microsoft\Windows NT\Printers |
| Registry Value Name | DisableWebPnPDownload |
| ADMX File Name | ICM.admx |

## DisableInternetDownloadForWebPublishingAndOnlineOrderingWizards

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1709 [10.0.16299] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Connectivity/DisableInternetDownloadForWebPublishingAndOnlineOrderingWizards
```

This policy setting specifies whether Windows should download a list of providers for the web publishing and online ordering wizards.

These wizards allow users to select from a list of companies that provide services such as online storage and photographic printing. By default, Windows displays providers downloaded from a Windows website in addition to providers specified in the registry.

- If you enable this policy setting, Windows doesn't download providers, and only the service providers that are cached in the local registry are displayed.
- If you disable or don't configure this policy setting, a list of providers are downloaded when the user uses the web publishing or online ordering wizards.

See the documentation for the web publishing and online ordering wizards for more information, including details on specifying service providers in the registry.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `chr` (string) |
| Access Type | Add, Delete, Get, Replace |

Tip

This is an ADMX-backed policy and requires SyncML format for configuration. For an example of SyncML format, refer to [Enabling a policy](../understanding-admx-backed-policies#enabling-a-policy).

**ADMX mapping**:

| Name | Value |
| --- | --- |
| Name | ShellPreventWPWDownload\_2 |
| Friendly Name | Turn off Internet download for Web publishing and online ordering wizards |
| Location | Computer Configuration |
| Path | InternetManagement &gt; Internet Communication settings |
| Registry Key Name | Software\Microsoft\Windows\CurrentVersion\Policies\Explorer |
| Registry Value Name | NoWebServices |
| ADMX File Name | ICM.admx |

## DisallowNetworkConnectivityActiveTests

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Connectivity/DisallowNetworkConnectivityActiveTests
```

This policy setting turns off the active tests performed by the Windows Network Connectivity Status Indicator (NCSI) to determine whether your computer is connected to the Internet or to a more limited network.

As part of determining the connectivity level, NCSI performs one of two active tests: downloading a page from a dedicated Web server or making a DNS request for a dedicated address.

- If you enable this policy setting, NCSI doesn't run either of the two active tests. This may reduce the ability of NCSI, and of other components that use NCSI, to determine Internet access.
- If you disable or don't configure this policy setting, NCSI runs one of the two active tests.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 1 | Allow. |
| 0 (Default) | Block. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | NoActiveProbe |
| Friendly Name | Turn off Windows Network Connectivity Status Indicator active tests |
| Location | Computer Configuration |
| Path | InternetManagement &gt; Internet Communication settings |
| Registry Key Name | Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator |
| Registry Value Name | NoActiveProbe |
| ADMX File Name | ICM.admx |

## HardenedUNCPaths

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Connectivity/HardenedUNCPaths
```

This policy setting configures secure access to UNC paths.

If you enable this policy, Windows only allows access to the specified UNC paths after fulfilling additional security requirements.

For more information, see [MS15-011: Vulnerability in Group Policy could allow remote code execution](https://support.microsoft.com/kb/3000483).

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `chr` (string) |
| Access Type | Add, Delete, Get, Replace |

Tip

This is an ADMX-backed policy and requires SyncML format for configuration. For an example of SyncML format, refer to [Enabling a policy](../understanding-admx-backed-policies#enabling-a-policy).

**ADMX mapping**:

| Name | Value |
| --- | --- |
| Name | Pol\_HardenedPaths |
| Friendly Name | Hardened UNC Paths |
| Location | Computer Configuration |
| Path | Network &gt; Network Provider |
| Registry Key Name | Software\Policies\Microsoft\Windows\NetworkProvider\HardenedPaths |
| ADMX File Name | NetworkProvider.admx |

## ProhibitInstallationAndConfigurationOfNetworkBridge

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1709 [10.0.16299] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Connectivity/ProhibitInstallationAndConfigurationOfNetworkBridge
```

Determines whether a user can install and configure the Network Bridge.

Important

This settings is location aware. It only applies when a computer is connected to the same DNS domain network it was connected to when the setting was refreshed on that computer. If a computer is connected to a DNS domain network other than the one it was connected to when the setting was refreshed, this setting doesn't apply.

The Network Bridge allows users to create a layer 2 MAC bridge, enabling them to connect two or more network segements together. This connection appears in the Network Connections folder.

If you disable this setting or don't configure it, the user will be able to create and modify the configuration of a Network Bridge. Enabling this setting doesn't remove an existing Network Bridge from the user's computer.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `chr` (string) |
| Access Type | Add, Delete, Get, Replace |

Tip

This is an ADMX-backed policy and requires SyncML format for configuration. For an example of SyncML format, refer to [Enabling a policy](../understanding-admx-backed-policies#enabling-a-policy).

**ADMX mapping**:

| Name | Value |
| --- | --- |
| Name | NC\_AllowNetBridge\_NLA |
| Friendly Name | Prohibit installation and configuration of Network Bridge on your DNS domain network |
| Location | Computer Configuration |
| Path | Network &gt; Network Connections |
| Registry Key Name | Software\Policies\Microsoft\Windows\Network Connections |
| Registry Value Name | NC\_AllowNetBridge\_NLA |
| ADMX File Name | NetworkConnections.admx |

## UseCellularWhenWiFiPoor

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows Insider Preview |

```Device
./Device/Vendor/MSFT/Policy/Config/Connectivity/UseCellularWhenWiFiPoor
```

This policy allows the use of a cellular connection when Wi-Fi connectivity is limited.

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