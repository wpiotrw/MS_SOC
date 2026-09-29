---
layout: Conceptual
title: Windows 11, version 25H2 known issues and notifications | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/release-health/status-windows-11-25h2
breadcrumb_path: /windows/release-health/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Windows
feedback_system: None
adobe-target: true
description: View announcements and review known issues and fixes for Windows 11, version 25H2
keywords:
- Windows 11
- issues
- fixes
- announcements
- advisories
- Windows 11, version 25H2
ms.service: windows-11
ms.topic: release-notes
ms.mktglfcycl: deploy
ms.sitesec: library
ms.localizationpriority: medium
ms.author: direek
author: WindowsCommunications
ms.date: 2026-09-29T00:00:00.0000000Z
locale: en-us
document_id: 23a22fef-6025-c344-f03d-d8b2b87db03f
document_version_independent_id: 23a22fef-6025-c344-f03d-d8b2b87db03f
original_content_git_url: https://github.com/MicrosoftDocs/windows-release-pr/blob/live/windows/release-information/status-windows-11-25H2.md
site_name: Docs
depot_name: TechNet.rel-info
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: status-windows-11-25h2
moniker_range_name: 
monikers: []
item_type: Content
source_path: windows/release-information/status-windows-11-25H2.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/19ec6774-09b8-473e-a17e-b17b518bbad7
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ade36b61-c646-4bd8-87ee-f3a843461962
platformId: a266b635-a4c6-9c45-d46b-83459037ab56
---

# Windows 11, version 25H2 known issues and notifications | Microsoft Learn

Find information on known issues and the status of the Windows 11, version 25H2 rollout. For immediate help with Windows update issues, [click here](ms-contact-support://smc-to-emerald/knownissues/) if you are using a Windows device to open the Get Help app or go to [support.microsoft.com](https://support.microsoft.com/). Follow [@WindowsUpdate](https://twitter.com/windowsupdate) on X for Windows release health updates. If you are an IT administrator and want to programmatically get information from this page, use the [Windows Updates API in Microsoft Graph](/en-us/graph/api/resources/windowsupdates-product?view=graph-rest-beta).

**Current status as of September 29, 2026** 

[Windows 11, version 26H2](https://aka.ms/how-to-get-26H2), also known as the Windows 11 2026 Update, is now available. We recommend you move to version 26H2 to stay up to date, secure, and productive. 

The rollout is phased and will expand over the next few months. Starting today, version 26H2 is available on eligible Windows 11, version 25H2 and version 24H2 devices for users who have turned on the setting [Get the latest updates as soon as they’re available](https://support.microsoft.com/windows/get-windows-updates-as-soon-as-they-re-available-for-your-device-cad7b32b-001e-435b-9110-f18309b54168). If the update is ready for your device, it will download and install automatically, and a single restart will complete the process. 

For more details on how to install Windows 11, version 26H2, [watch this video](https://aka.ms/video/W11/how-to-get-26H2).

- ![device desktop download blue](/en-us/office/media/icons/device-desktop-download-blue.png)

[How to get the Windows 11 2026 Update](https://aka.ms/how-to-get-26H2)
- ![whats new megaphone blue](/en-us/office/media/icons/whats-new-megaphone-blue.png)

[An IT pro’s guide to Windows 11, version 26H2](https://aka.ms/26H2-for-IT-pros)

[See all messages >](/en-us/windows/release-information/windows-message-center)

## Known issues

See open issues, content updated in the last 30 days, and information on [safeguard holds](https://support.microsoft.com/topic/kb5006965-how-to-check-information-about-safeguard-holds-affecting-your-device-265cf311-6c98-4413-956b-75b3044dfde9). To find a specific issue, use the search function on your browser (CTRL + F for Microsoft Edge).

| Summary | Originating update | Status | Last updated |
| --- | --- | --- | --- |
| **Devices might experience a black screen or desktop loading issues after sign-in**Microsoft has received reports of this issue occurring in some virtual desktop environments. | OS Build 26200.9278[KB5120998](https://support.microsoft.com/help/5120998)2026-08-27 | Mitigated | 2026-09-29 10:12 PT |
| **Domain-joined devices might lose their secure trust relationship with the domain**Some Credential Guard protected machine accounts might be unable to sign in interactively will valid domain credentials. | OS Build 26200.9445[KB5124008](https://support.microsoft.com/help/5124008)2026-09-08 | Mitigated | 2026-09-29 10:12 PT |
| **USB audio devices might fail to start or produce no sound**Some USB Audio Class 1.0 devices display Code 10 or fail in multichannel audio modes after installing the Sept. 8 update | OS Build 26200.9445[KB5124008](https://support.microsoft.com/help/5124008)2026-09-08 | Mitigated | 2026-09-29 10:12 PT |
| **Remote Desktop Services might stop responding after Sept. 2026 security update**Some Windows devices with Remote Desktop enabled might experience Remote Desktop Services (RDS) instability. | OS Build 26200.9445[KB5124008](https://support.microsoft.com/help/5124008)2026-09-08 | Resolved[KB5129195](https://support.microsoft.com/help/5129195) | 2026-09-17 19:22 PT |
| **Incorrect notifications that "Microsoft Defender Antivirus is turned off"**Microsoft Defender Antivirus remains active and functioning correctly despite notifications following the latest update. | N/A | Resolved | 2026-09-17 19:22 PT |
| **Host folder shares might be unavailable in Hyper-V-based Linux VMs**Plan9 host folder shares might not appear in the guest environment after installing the September 2026 security update. | OS Build 26200.9445[KB5124008](https://support.microsoft.com/help/5124008)2026-09-08 | Resolved[KB5129195](https://support.microsoft.com/help/5129195) | 2026-09-14 13:30 PT |
| **Microsoft Teams and Outlook might fail to launch on ARM-based devices**This most likely occurs on new PCs after installing the August Windows security update and does not affect other apps. | OS Build 26200.9168[KB5121003](https://support.microsoft.com/help/5121003)2026-08-11 | Resolved[KB5124008](https://support.microsoft.com/help/5124008) | 2026-09-08 11:37 PT |
| **Mouse customization is reset on non-English Windows devices**Custom cursors and cursor animations may intermittently revert | OS Build 26200.9278[KB5120998](https://support.microsoft.com/help/5120998)2026-08-27 | Resolved[KB5124008](https://support.microsoft.com/help/5124008) | 2026-09-08 10:41 PT |
| **Desktop background settings are lost or reset on some devices**For affected Windows installations, backgrounds might revert to a black solid color | OS Build 26200.9278[KB5120998](https://support.microsoft.com/help/5120998)2026-08-27 | Resolved[KB5124008](https://support.microsoft.com/help/5124008) | 2026-09-08 10:41 PT |

## Issue details

### September 2026

#### Devices might experience a black screen or desktop loading issues after sign-in

| **Status** | **Originating update** | **History** |
| --- | --- | --- |
 Mitigated | OS Build 26200.9278[KB5120998](https://support.microsoft.com/help/5120998)2026-08-27 | Last updated: 2026-09-29, 10:12 PTOpened: 2026-09-25, 19:38 PT |

After installing the August 2026 Windows non-security preview update ([KB5120998](https://support.microsoft.com/help/5120998)) and subsequent updates, some devices might experience desktop loading issues. This issue has been primarily observed on Azure Virtual Desktop (AVD) hosts, using [FSLogix](/en-us/fslogix/overview-what-is-fslogix). This issue appears to occur more frequently with some existing user profiles.

Symptoms might include:

- ​A black screen appears after sign-in and the desktop session does not load automatically.
- ​Users might be unable to access their desktop until the desktop session is started manually.
- ​Application event logs might show Windows Explorer crashes.

**Workaround**: Affected customers can apply one of the following workarounds to mitigate the issue:

1. ​**Manually launch explorer.exe: **Users can temporarily mitigate this issue by opening Task Manager (Ctrl+Shift+Esc), selecting **Run new task**, entering **explorer.exe**, and selecting **OK**.
2. ​**Mitigate through Known Issue Rollback (KIR): **This issue is mitigated using [Known Issue Rollback (KIR)](https://techcommunity.microsoft.com/blog/windows-itpro-blog/known-issue-rollback-helping-you-keep-windows-devices-protected-and-productive/2176831).

 For enterprise-managed devices where Windows updates are managed by IT departments, IT administrators can apply the KIR by installing and configuring the Group policy listed below. The special Group Policy can be found in **Computer Configuration &gt; Administrative Templates &gt; &lt;Group Policy name listed below&gt;**
 
***Group Policy downloads with Group Policy name:***

- ​*Download for Windows 11, version 26H1: *[*KB5124006 260924\_20071 Known Issue Rollback*](https://download.microsoft.com/download/09efb4c6-54f4-4e63-83c7-4314187230bf/Windows%2011%2026H1%20KB5124006%20260924_20071%20Known%20Issue%20Rollback.msi)
- ​*Download for Windows 11, version 26H2, Windows 11, version 25H2, and Windows 11, version 24H2: *[*KB5124010 260924\_20021 Known Issue Rollback*](https://download.microsoft.com/download/8c71622d-e0eb-4838-b25c-ddb99a7bf971/Windows%2011%2024H2,%20Windows%2011%2025H2%20and%20Windows%20Server%202025%20KB5124010%20260924_20021%20Known%20Issue%20Rollback.msi)

 **Important**: You will need to **install **and **configure** the Group Policy for your version of Windows to resolve this issue. You will also need to restart your device(s) to apply the group policy setting. Note that this Group Policy will disable the change causing this issue until a resolution is released in a future Windows update. 
 For information on deploying and configuring this special Group Policy, please see [How to use Group Policy to deploy a Known Issue Rollback](/en-us/troubleshoot/windows-client/group-policy/use-group-policy-to-deploy-known-issue-rollback)
**Next Steps: **We are working on a resolution for this issue, and it will be released in a future Windows update.

Affected platforms:

- ​Client: Windows 11, version 26H2; Windows 11, version 26H1; Windows 11, version 25H2; Windows 11, version 24H2
- ​Server: None

Back to top

#### Domain-joined devices might lose their secure trust relationship with the domain

| **Status** | **Originating update** | **History** |
| --- | --- | --- |
 Mitigated | OS Build 26200.9445[KB5124008](https://support.microsoft.com/help/5124008)2026-09-08 | Last updated: 2026-09-29, 10:12 PTOpened: 2026-09-25, 18:57 PT |

After installing the September 8, 2026, Windows security update ([KB5124008](https://support.microsoft.com/help/5124008)), or later updates, some [Credential Guard protected machine accounts](/en-us/windows-server/identity/ad-ds/manage/delegated-managed-service-accounts/credential-guard-protected-machine-accounts) might lose their secure channel with an on-premises Active Directory (AD) domain. Users might then be unable to sign in interactively with valid domain credentials and might receive a message stating that the trust relationship between the device and the domain failed. Offline sign-in using previously cached credentials might continue to work. AD replication and AD services on the domain controllers are not affected. 

This issue occurs because [KB5124008](https://support.microsoft.com/help/5124008) and later updates enable the [Machine Identity Isolation](/en-us/windows-server/identity/ad-ds/manage/delegated-managed-service-accounts/credential-guard-protected-machine-accounts#machine-identity-isolation) feature. While the update does not directly enable Machine Identity Isolation enforcement, it does cause Windows to begin honoring any existing or policy-provisioned settings that enabled Machine Identity Isolation enforcement. However, this feature is only supported for environments connected to domain controllers running at a Windows Server 2025 Domain Functional Level (DFL) and above. The feature should be disabled elsewhere. Any devices previously configured to use Machine Identity Isolation that are not connected to Windows Server 2025 domain controllers will experience this issue and will need to disable the feature. 

**Workaround**: *Important: This section contains information about modifying the registry. Before you modify the registry, back it up and make sure that you know how to restore it if a problem occurs. For more information, see *[*How to back up and restore the registry in Windows*](https://support.microsoft.com/help/322756)*.* 

To work around this issue, disable Machine Identity Isolation using the same management method that was used to enable it. Choose the applicable option below: 

1. ​If Machine Identity Isolation was enabled by Intune policy, [disable Machine Identity Isolation with Intune](/en-us/windows/client-management/mdm/policy-csp-deviceguard#machineidentityisolation).
2. ​If Machine Identity Isolation was enabled by group policy, [disable Machine Identity Isolation with group policy](/en-us/windows-server/identity/ad-ds/manage/delegated-managed-service-accounts/credential-guard-protected-machine-accounts#machine-identity-isolation).
3. ​If Machine Identity Isolation was enabled directly in the registry, use these steps to disable it:

- ​On the Windows 11, version 24H2 or 25H2 device, locate the following registry paths: 
    - ​HKLM\SYSTEM\CurrentControlSet\Control\Lsa\MachineIdentityIsolation
    - ​HKLM\SOFTWARE\Policies\Microsoft\Windows\DeviceGuard\MachineIdentityIsolation
- ​For either of these registry keys, if the value for MachineIdentityIsolation = 2, then set **MachineIdentityIsolation = 0**.

After you disable Machine Identity Isolation, restart the device. 

Then reset the secure channel using the following command:

```
	 'Test-ComputerSecureChannel -Repair -Credential (Get-Credential)' 
```

**Next Steps: **We plan to resolve this issue in a future Windows update by temporarily preventing Machine Identity Isolation enforcement while improvements are made to the feature.

**Affected platforms:**

- ​Client: Windows 11, version 26H2; Windows 11, version 26H1; Windows 11, version 25H2; Windows 11, version 24H2
- ​Server: None

Back to top

#### USB audio devices might fail to start or produce no sound

| **Status** | **Originating update** | **History** |
| --- | --- | --- |
 Mitigated | OS Build 26200.9445[KB5124008](https://support.microsoft.com/help/5124008)2026-09-08 | Last updated: 2026-09-29, 10:12 PTOpened: 2026-09-25, 18:40 PT |

After installing the September 8, 2026, Windows security update ([KB5124008](https://support.microsoft.com/help/5124008)), some [USB Audio Class 1.0](/en-us/windows-hardware/drivers/audio/usb-audio-class-system-driver--usbaudio-sys-) devices might fail to start or produce audio. Affected devices might experience one or more of the following symptoms: 

- ​The device displays an error in Device Manager: "This device cannot start (Code 10).”
- ​No audio output.
- ​Volume controls are unresponsive or remain at zero.
- ​Sound settings are unresponsive or unavailable.
- ​Some devices might function in standard stereo configurations but fail when using multichannel audio features, including 8-channel or 3D audio modes. Some customers have reported that they're able to restore audio in these cases by switching to 2-channel mode. *(\*Note: This behavior is resolved in the out-of-band update released on September 14, 2026. See ****Resolution**** section below.)*

This issue is limited to USB Audio Class 1.0 devices.

**Microsoft Support: **IT administrators who need an immediate workaround for the symptoms not addressed yet by the OOB update should contact [Microsoft Support for Business](https://support.microsoft.com/support-for-business) for assistance. 

**Resolution: **This issue is partially resolved in the out-of-band (OOB) update released on September 14, 2026, ([KB5129195](https://support.microsoft.com/help/5129195)), and updates released after this date. This OOB update resolves the symptoms experienced on devices using 8-channel or 3D audio modes (last bullet point in the list of symptoms documented in this entry). We are working to address the other symptoms and will update this documentation when more information is available. 

**Affected platforms:**

- ​Client: Windows 11, version 26H2; Windows 11, version 26H1; Windows 11, version 25H2; Windows 11, version 24H2; Windows 11, version 23H2; Windows 10, version 22H2; Windows 10, version 21H2; Windows 10 Enterprise LTSC 2019; Windows 10 Enterprise LTSC 2016
- ​Server: Windows Server 2025; Windows Server 2022; Windows Server 2019; Windows Server 2016; Windows Server 2012 R2; Windows Server 2012

Back to top

#### Remote Desktop Services might stop responding after Sept. 2026 security update

| **Status** | **Originating update** | **History** |
| --- | --- | --- |
 Resolved [KB5129195](https://support.microsoft.com/help/5129195) | OS Build 26200.9445[KB5124008](https://support.microsoft.com/help/5124008)2026-09-08 | Resolved: 2026-09-14, 10:00 PTOpened: 2026-09-11, 11:19 PT |

After installing the September 2026 Windows security update ([KB5124008](https://support.microsoft.com/help/5124008)), some organizations might experience issues with Remote Desktop Services (RDS).

In some environments, RDS might become unstable, resulting in RDP connections failing after several minutes, sign-in issues, or servers hanging at "Please wait for the Remote Desktop Configuration". Related tools, including Microsoft Management Console (MMC), RDS Licensing Diagnoser, and File Explorer might also become unresponsive. Additionally, the Windows Update page might stop responding and continuously display a loading indicator. 

**Note: **This issue does not affect Windows 365 or Azure Virtual Desktop.

**Resolution: **This issue is resolved by the out-of-band (OOB) update released on September 14, 2026 ([KB5129195](https://support.microsoft.com/help/5129195)), and in updates released after this date.

IT administrators who deployed a temporary mitigation through Group Policy do not need to take any action before installing this OOB update.

This OOB update is cumulative and includes all improvements and security protections contained in previous Windows updates. As a best practice, we recommend installing the latest update available for your devices, as it contains important improvements and issue resolutions, including this one.

**Affected platforms:**

- ​Client: Windows 11, version 26H1; Windows 11, version 25H2; Windows 11, version 24H2; Windows 11, version 23H2; Windows 10, version 22H2; Windows 10, version 21H2; Windows 10 Enterprise LTSC 2019; Windows 10 Enterprise LTSC 2016
- ​Server: Windows Server 2025; Windows Server 2022; Windows Server 2019; Windows Server 2016; Windows Server 2012 R2; Windows Server 2012

Back to top

#### Host folder shares might be unavailable in Hyper-V-based Linux VMs

| **Status** | **Originating update** | **History** |
| --- | --- | --- |
 Resolved [KB5129195](https://support.microsoft.com/help/5129195) | OS Build 26200.9445[KB5124008](https://support.microsoft.com/help/5124008)2026-09-08 | Resolved: 2026-09-14, 10:00 PTOpened: 2026-09-11, 02:22 PT |

**Updated (9/14):***The resolution section was updated. IT administrators that deployed a temporary mitigation through Group Policy must re-enable the Group Policy and install the out-of-band update to resolve the issue.*

After installing the September 2026 security update [KB5124008](https://support.microsoft.com/help/5124008), applications that use [HCS-managed](/en-us/virtualization/api/hcs/overview) virtual machines might experience issues when sharing host folder with Linux VMs using Plan9. Affected virtual machines start normally, but folders shared from the Windows host using Plan9 do not appear or cannot be accessed in the guest environment.

Applications or sandbox environments that depend on these shared folders might display an error indicating that no Plan9 drive shares were mounted. Claude Cowork and the Windows Subsystem for Linux (WSL) are two of the applications affected by this issue. Standard Hyper-V virtual machines that do not use the Plan9 feature are not affected by this issue.

**Resolution: **This issue is resolved by the out-of-band (OOB) update released on September 14, 2026 ([KB5129195](https://support.microsoft.com/help/5129195)), and in updates released after this date.

IT administrators who deployed a temporary mitigation through Group Policy must re-enable the Group Policy, install this OOB update, and restart to resolve this issue.

This OOB update is cumulative and includes all improvements and security protections contained in previous Windows updates. As a best practice, we recommend installing the latest update available for your devices, as it contains important improvements and issue resolutions, including this one.

**Affected platforms:**

- ​Client: Windows 11, version 26H1; Windows 11, version 25H2; Windows 11, version 24H2; Windows 11, version 23H2; Windows 10, version 22H2; Windows 10, version 21H2
- ​Server: None

[Click here](https://admin.microsoft.com/Adminportal/Home?#/windowsreleasehealth/:/wrhpreferences) to manage email notifications for Windows known issues. 

Back to top

#### Microsoft Teams and Outlook might fail to launch on ARM-based devices

| **Status** | **Originating update** | **History** |
| --- | --- | --- |
 Resolved [KB5124008](https://support.microsoft.com/help/5124008) | OS Build 26200.9168[KB5121003](https://support.microsoft.com/help/5121003)2026-08-11 | Resolved: 2026-09-08, 10:00 PTOpened: 2026-09-01, 18:46 PT |

After installing Windows security updates released on or after August 11, 2026, ([KB5121003](https://support.microsoft.com/help/5121003)), Microsoft Teams and the new Outlook for Windows might fail to launch or might close unexpectedly on ARM-based devices, such as Surface Pro 11 and Surface Laptop 7. Classic Outlook, Word, Excel, and other applications are not known to be affected. This issue is most likely to occur on new or freshly imaged PCs that have not yet installed any Microsoft Store updates.

**Resolution**: This issue was resolved by Windows updates released September 8, 2026 ([KB5124008](https://support.microsoft.com/help/5124008)), and updates released after that date. We recommend you install the latest update for your device as it contains important improvements and issue resolutions, including this one. 

If you install an update released September 8, 2026 ([KB5124008](https://support.microsoft.com/help/5124008)), or later, you do not need to use a workaround for this issue. If you are using an update released before September 8 and have this issue, you have the option to apply the following workaround. 

**Workaround: **To work around this issue:

1. ​Open **Microsoft Store**.
2. ​Select **Downloads** &gt; **Check for updates.**
3. ​Install the latest update for the [Auto Super Resolution Package](https://apps.microsoft.com/detail/9pgwvx8tm6xz) (version 1.0.19.0 or later).

**Affected platforms:**

- ​Client: Windows 11, version 26H1; Windows 11, version 25H2; Windows 11, version 24H2
- ​Server: None

Back to top

#### Desktop background settings are lost or reset on some devices

| **Status** | **Originating update** | **History** |
| --- | --- | --- |
 Resolved [KB5124008](https://support.microsoft.com/help/5124008) | OS Build 26200.9278[KB5120998](https://support.microsoft.com/help/5120998)2026-08-27 | Resolved: 2026-09-08, 10:00 PTOpened: 2026-09-02, 18:29 PT |

Following installation of Windows updates released August 27 2026 ([KB5120998](https://support.microsoft.com/help/5120998)), some Windows Desktop settings fail to load, resulting in desktop backgrounds displaying as a solid black color. It is possible other desktop settings may be affected, such as slideshow settings or contrast themes.

On affected devices, attempting to manually restore customized settings does not work. This is because the issue prevents the correct loading of settings, regardless of their value. In this case, a default black background is used instead.

**Resolution**: This issue was resolved by Windows updates released September 8, 2026 ([KB5124008](https://support.microsoft.com/help/5124008)), and later. We recommend you install the latest security update for your device as it contains important improvements and issue resolutions, including this one. 

**Affected platforms:**

- ​Client: Windows 11, version 25H2; Windows 11, version 24H2
- ​Server: None

Back to top

### August 2026

#### Incorrect notifications that "Microsoft Defender Antivirus is turned off"

| **Status** | **Originating update** | **History** |
| --- | --- | --- |
 Resolved | N/A | Resolved: 2026-09-17, 19:22 PTOpened: 2026-08-28, 15:34 PT |

After installing the [latest updates for Microsoft Defender Antivirus](/en-us/defender-endpoint/microsoft-defender-endpoint-releases#microsoft-defender-antivirus-releases), notifications might appear stating that "Microsoft Defender Antivirus is turned off," even though the antivirus is functioning correctly and all settings show it as active. These notifications can appear when Windows starts and intermittently afterward. They persist even if notification settings are turned off.

This issue can be observed in any version of Windows or Windows Server with Microsoft Defender Antivirus running with the latest Defender updates.

**Resolution: **This issue was resolved in the [Microsoft Defender Antivirus update (version 4.18.26080.4)](https://www.microsoft.com/wdsi/defenderupdates), released on September 17, 2026.

**Affected platforms:**

- ​Client: Windows 11, version 26H1; Windows 11, version 25H2; Windows 11, version 24H2; Windows 11, version 23H2; Windows 10, version 22H2; Windows 10, version 21H2; Windows 10 Enterprise LTSC 2019; Windows 10 Enterprise LTSC 2016
- ​Server: Windows Server 2025; Windows Server 2022; Windows Server 2019; Windows Server 2016; Windows Server 2012 R2; Windows Server 2012

Back to top

#### Mouse customization is reset on non-English Windows devices

| **Status** | **Originating update** | **History** |
| --- | --- | --- |
 Resolved [KB5124008](https://support.microsoft.com/help/5124008) | OS Build 26200.9278[KB5120998](https://support.microsoft.com/help/5120998)2026-08-27 | Resolved: 2026-09-08, 10:00 PTOpened: 2026-08-28, 15:36 PT |

Following installation of Windows updates released August 27 2026 ([KB5120998](https://support.microsoft.com/help/5120998)), mouse personalization settings are being reverted to certain standard settings. This includes cursor and cursor animations that are selected in the Mouse Properties options under Windows.

Our investigation indicates that this issue is caused by code components used in non-English Windows installations. In impacted locales, these settings will fail to load, causing a default to be used instead. Attempting to manually restore the settings values is not successful, as the issue prevents loading these settings regardless of their value. 

**Resolution**: This issue was resolved by Windows updates released September 8, 2026 ([KB5124008](https://support.microsoft.com/help/5124008)), and later. We recommend you install the latest security update for your device as it contains important improvements and issue resolutions, including this one. 

**Affected platforms:**

- ​Client: Windows 11, version 25H2; Windows 11, version 24H2
- ​Server: None

Back to top

## Report a problem with Windows updates

To report an issue to Microsoft at any time, use the [Feedback Hub](feedback-hub:) app. To learn more, see [Send feedback to Microsoft with the Feedback Hub app](https://support.microsoft.com/windows/send-feedback-to-microsoft-with-the-feedback-hub-app-f59187f8-8739-22d6-ba93-f66612949332). 

## Need help with Windows updates?

Search, browse, or ask a question on the [Microsoft Support Community](https://answers.microsoft.com/). If you are an IT pro supporting an organization, visit Windows release health on the [Microsoft 365 admin center](/en-us/windows/deployment/update/check-release-health) for additional details. 

For direct help with your home PC, use the Get Help app in Windows or contact [Microsoft Support](https://support.microsoft.com/). Organizations can request immediate support through [Support for business](https://support.serviceshub.microsoft.com/supportforbusiness/onboarding). 

## View this site in your language

This site is available in [11 languages](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/windows-release-health-now-localized-in-10-languages/ba-p/2530167): English, Chinese Traditional, Chinese Simplified, French (France), German, Italian, Japanese, Korean, Portuguese (Brazil), Russian, and Spanish (Spain). All text will appear in English if your browser default language is not one of the 11 supported languages. To manually change the display language, scroll down to the bottom of this page, click on the current language displayed on the bottom left of the page, and select one of the 11 supported languages from the list.