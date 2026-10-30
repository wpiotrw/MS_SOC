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
ms.date: 2026-10-30T00:00:00.0000000Z
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

**Current status as of October 28, 2026** 

[Windows 11, version 26H2](https://aka.ms/how-to-get-26H2) is now available for all eligible devices. We recommend updating to version 26H2 to stay up to date, secure, and productive. 

You can check for the update by going to **Settings **&gt;** Windows Update** and selecting [**Check for Windows updates**](https://support.microsoft.com/windows/deployment/updates-lifecycle/install-windows-updates). If Windows 11, version 26H2 is available for your device, select **Download & install**. If you want updates to be installed as soon as they’re available, turn on [**Get the latest updates as soon as they’re available**](https://support.microsoft.com/windows/get-windows-updates-as-soon-as-they-re-available-for-your-device-cad7b32b-001e-435b-9110-f18309b54168).

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
| **Remote Desktop connections might fail for non-admin users with error 0xC000000D**This issue affects non-admin users connecting through Remote Desktop with Administrator protection enabled. | OS Build 26200.9550[KB5124010](https://support.microsoft.com/help/5124010)2026-09-22 | Resolved[KB5127936](https://support.microsoft.com/help/5127936) | 2026-10-28 22:02 PT |
| **Devices might experience a black screen or desktop loading issues after sign-in**Microsoft has received reports of this issue occurring in some virtual desktop environments. | OS Build 26200.9278[KB5120998](https://support.microsoft.com/help/5120998)2026-08-27 | Resolved[KB5127648](https://support.microsoft.com/help/5127648) | 2026-10-13 10:13 PT |
| **Applications which require AC-3 audio decoding might close unexpectedly**This issue is more likely to occur in legacy applications, and unlikely for many modern applications. | OS Build 26200.9550[KB5124010](https://support.microsoft.com/help/5124010)2026-09-22 | Resolved[KB5127648](https://support.microsoft.com/help/5127648) | 2026-10-13 10:13 PT |
| **Domain-joined devices might lose their secure trust relationship with the domain**Some Credential Guard protected machine accounts might be unable to sign in interactively will valid domain credentials. | OS Build 26200.9445[KB5124008](https://support.microsoft.com/help/5124008)2026-09-08 | Resolved[KB5124010](https://support.microsoft.com/help/5124010) | 2026-10-08 17:44 PT |
| **Incorrect notifications that "Microsoft Defender Antivirus is turned off"**Microsoft Defender Antivirus remains active and functioning correctly despite notifications following the latest update. | N/A | Resolved | 2026-09-30 16:42 PT |
| **USB audio devices might fail to start or produce no sound**Some USB Audio Class 1.0 devices display Code 10 or fail in multichannel audio modes after installing the Sept. 8 update | OS Build 26200.9445[KB5124008](https://support.microsoft.com/help/5124008)2026-09-08 | Mitigated | 2026-09-29 10:12 PT |

## Issue details

### October 2026

#### Remote Desktop connections might fail for non-admin users with error 0xC000000D

| **Status** | **Originating update** | **History** |
| --- | --- | --- |
 Resolved [KB5127936](https://support.microsoft.com/help/5127936) | OS Build 26200.9550[KB5124010](https://support.microsoft.com/help/5124010)2026-09-22 | Resolved: 2026-10-28, 10:00 PTOpened: 2026-10-13, 09:43 PT |

After installing the September 2026 non-security preview update ([KB5124010](https://support.microsoft.com/help/5124010)), or later updates, non-admin users might be unable to establish Remote Desktop connections to remote devices that have [Administrator protection](/en-us/windows/security/application-security/application-control/administrator-protection/?tabs=intune) enabled. Attempts to connect might fail with error 0xC000000D and display the message, “The token that was passed to the function is invalid.” This issue primarily affects enterprise-managed remote devices used as Remote Desktop hosts with Administrator protection enabled, regardless of [how the feature was enabled](/en-us/windows/security/application-security/application-control/administrator-protection/?tabs=intune#configuration).

**Note**: If your organization uses [Windows security baselines](https://techcommunity.microsoft.com/blog/microsoft-security-baselines/windows-11-version-26h2-security-baseline/4560382), published through the [Microsoft Security Compliance Toolkit,](https://www.microsoft.com/download/details.aspx?id=55319) Administrator protection is enabled by default in Windows 11, version 24H2, 25H2, and 26H2 security baselines, unless your organization has configured the policy differently. 

**Resolution: **This issue was resolved by Windows updates released October 28, 2026 ([KB5127936](https://support.microsoft.com/help/5127936)), and later. We recommend you install the latest security update for your device as it contains important improvements and issue resolutions, including this one. 

If you install an update released October 28, 2026 ([KB5127936](https://support.microsoft.com/help/5127936)) or later, you do not need to use a workaround for this issue. If you are using an update released before this date, and have this issue, you have the option to apply the following workaround:

IT administrators can mitigate this issue on devices affected by the Remote Desktop connection failure by using their existing policy management method to temporarily turn off Administrator protection. Reset the *User Account Control Type Of Admin Approval Mode* policy in Microsoft Intune or Group Policy. For more information, see [Administrator protection on Windows 11](https://techcommunity.microsoft.com/blog/windows-itpro-blog/administrator-protection-on-windows-11/4303482).

**Affected platforms:**

- ​Client: Windows 11, version 26H2; Windows 11, version 26H1; Windows 11, version 25H2; Windows 11, version 24H2
- ​Server: None

Back to top

#### Devices might experience a black screen or desktop loading issues after sign-in

| **Status** | **Originating update** | **History** |
| --- | --- | --- |
 Resolved [KB5127648](https://support.microsoft.com/help/5127648) | OS Build 26200.9278[KB5120998](https://support.microsoft.com/help/5120998)2026-08-27 | Resolved: 2026-10-13, 10:00 PTOpened: 2026-10-13, 09:49 PT |

After installing the August 2026 Windows non-security preview update ([KB5120998](https://support.microsoft.com/help/5120998)) and subsequent updates, some devices might experience desktop loading issues. This issue has been primarily observed on Azure Virtual Desktop (AVD) hosts, using [FSLogix](/en-us/fslogix/overview-what-is-fslogix). This issue appears to occur more frequently with some existing user profiles.

Symptoms might include:

- ​A black screen appears after sign-in and the desktop session does not load automatically.
- ​Users might be unable to access their desktop until the desktop session is started manually.
- ​Application event logs might show Windows Explorer crashes.

**Resolution:** This issue was resolved by Windows updates released October 13, 2026 ([KB5127648](https://support.microsoft.com/help/5127648)), and updates released after that date. We recommend you install the latest update for your device as it contains important improvements and issue resolutions, including this one. 

If you install an update released October 13, 2026 ([KB5127648](https://support.microsoft.com/help/5127648)), or later, you do not need to use a workaround for this issue. If you are using an update released before October 13, and have this issue, you have the option to apply the following workaround. 

**Workaround**: Affected customers can apply one of the following workarounds to mitigate the issue:

1. ​**Manually launch explorer.exe: **Users can temporarily mitigate this issue by opening Task Manager (Ctrl+Shift+Esc), selecting **Run new task**, entering **explorer.exe**, and selecting **OK**.
2. ​**Mitigate through Known Issue Rollback (KIR): **This issue is mitigated using [Known Issue Rollback (KIR)](https://techcommunity.microsoft.com/blog/windows-itpro-blog/known-issue-rollback-helping-you-keep-windows-devices-protected-and-productive/2176831).

 For enterprise-managed devices where Windows updates are managed by IT departments, IT administrators can apply the KIR by installing and configuring the Group policy listed below. The special Group Policy can be found in **Computer Configuration &gt; Administrative Templates &gt; &lt;Group Policy name listed below&gt;**
 
 ***Group Policy downloads with Group Policy name:***
- ​*Download for Windows 11, version 26H1: *[*KB5124006 260924\_20071 Known Issue Rollback*](https://download.microsoft.com/download/09efb4c6-54f4-4e63-83c7-4314187230bf/Windows%2011%2026H1%20KB5124006%20260924_20071%20Known%20Issue%20Rollback.msi)
- ​*Download for Windows 11, version 26H2, Windows 11, version 25H2 and Windows 11, version 24H2: *[*KB5124010 260924\_20021 Known Issue Rollback*](https://download.microsoft.com/download/8c71622d-e0eb-4838-b25c-ddb99a7bf971/Windows%2011%2024H2,%20Windows%2011%2025H2%20and%20Windows%20Server%202025%20KB5124010%20260924_20021%20Known%20Issue%20Rollback.msi)

 **Important**: You will need to **install **and **configure** the Group Policy for your version of Windows to resolve this issue. You will also need to restart your device(s) to apply the group policy setting. Note that this Group Policy will disable the change causing this issue until a resolution is released in a future Windows update. 
 For information on deploying and configuring this special Group Policy, please see [How to use Group Policy to deploy a Known Issue Rollback](/en-us/troubleshoot/windows-client/group-policy/use-group-policy-to-deploy-known-issue-rollback)
**Affected platforms:**

- ​Client: Windows 11, version 26H2; Windows 11, version 26H1; Windows 11, version 25H2; Windows 11, version 24H2
- ​Server: None

Back to top

#### Applications which require AC-3 audio decoding might close unexpectedly

| **Status** | **Originating update** | **History** |
| --- | --- | --- |
 Resolved [KB5127648](https://support.microsoft.com/help/5127648) | OS Build 26200.9550[KB5124010](https://support.microsoft.com/help/5124010)2026-09-22 | Resolved: 2026-10-13, 10:00 PTOpened: 2026-10-08, 16:29 PT |

Following installation of Windows updates released September 22, 2026 ([KB5124010](https://support.microsoft.com/help/5124010)), and later, some applications which require the decoding of AC-3 (Dolby Digital) audio might close unexpectedly.

Incidence of this issue depends on the activity that these applications perform. In some cases the application can fail to launch, or close without warning. In other cases the application will work normally until certain features are used, such as playing music. Affected applications may vary and can include games, media players, and certain productivity applications.

Please note that many modern applications do not use Windows for this type of encoding and therefore will not encounter this issue. The code component involved in this issue is most commonly used in legacy applications that still rely on Windows built-in audio decoding. Many modern applications using this legacy codec frequently include their own audio decoding components.

**Resolution**: This issue was resolved by Windows updates released October 13, 2026 ([KB5127648](https://support.microsoft.com/help/5127648)), and later. We recommend you install the latest security update for your device as it contains important improvements and issue resolutions, including this one. 

**Affected platforms:**

- ​Client: Windows 11, version 26H2; Windows 11, version 25H2; Windows 11, version 24H2
- ​Server: None

Back to top

### September 2026

#### Domain-joined devices might lose their secure trust relationship with the domain

| **Status** | **Originating update** | **History** |
| --- | --- | --- |
 Resolved [KB5124010](https://support.microsoft.com/help/5124010) | OS Build 26200.9445[KB5124008](https://support.microsoft.com/help/5124008)2026-09-08 | Resolved: 2026-09-22, 10:00 PTOpened: 2026-09-16, 14:15 PT |

After installing the September 8, 2026, Windows security update ([KB5124008](https://support.microsoft.com/help/5124008)), or the September 14, 2026, Windows out-of-band update ([KB5129195](https://support.microsoft.com/help/5129195)), some [Credential Guard protected machine accounts](/en-us/windows-server/identity/ad-ds/manage/delegated-managed-service-accounts/credential-guard-protected-machine-accounts) might lose their secure channel with an on-premises Active Directory (AD) domain. Users might then be unable to sign in interactively with valid domain credentials and might receive a message stating that the trust relationship between the device and the domain failed. Offline sign-in using previously cached credentials might continue to work. AD replication and AD services on the domain controllers are not affected. 

This issue occurs because these updates enable the [Machine Identity Isolation](/en-us/windows-server/identity/ad-ds/manage/delegated-managed-service-accounts/credential-guard-protected-machine-accounts#machine-identity-isolation) feature. While the updates do not directly enable Machine Identity Isolation enforcement, it does cause Windows to begin honoring any existing or policy-provisioned settings that enabled Machine Identity Isolation enforcement. However, this feature is only supported for environments connected to domain controllers running at a Windows Server 2025 Domain Functional Level (DFL) and above. The feature should be disabled elsewhere. Any devices previously configured to use Machine Identity Isolation that are not connected to Windows Server 2025 domain controllers will experience this issue and will need to disable the feature. 

**Resolution:** This issue was resolved by Windows updates released September 22, 2026 ([KB5124010](https://support.microsoft.com/help/5124010)), and updates released after that date. This update prevents Machine Identity Isolation (MII) enforcement by disabling it completely while improvements are made to the feature. MII enforcement will be prevented regardless of the MII configuration.

If you install an update released September 22, 2026 ([KB5124010](https://support.microsoft.com/help/5124010)) or later, you do not need to use a workaround for this issue. If you are using an update released before September 22, 2026, and have this issue, you have the option to apply one of the following workarounds. 

**Workaround #1: Known Issue Rollback**

IT administrators can resolve the issue using[Known Issue Rollback (KIR)](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/known-issue-rollback-helping-you-keep-windows-devices-protected/ba-p/2176831) by installing and configuring the special Group Policy listed below.

**Group Policy downloads with Group Policy name: ** 

- ​[Download for Windows 11, version 24H2, 25H2, and 26H2](https://download.microsoft.com/download/a5cbc03a-ec77-4abd-a8bd-72b7fdf6177c/Windows%2011%2024H2,%20Windows%2011%2025H2%20and%20Windows%20Server%202025%20KB5124008%20260915_17123%20Known%20Issue%20Rollback.msi) — KB5124008 260915\_17123 Known Issue Rollback

The special Group Policy can be found in** Computer Configuration &gt; Administrative Templates &gt; KB5124008 260915\_17123 Known Issue Rollback &gt; Windows 11, version 24H2, 25H2. **After installing the Group Policy, configure the value for setting KB5124008 260915\_17123 Known Issue Rollback to **Disabled** and restart your device(s) to apply the Group Policy setting. For information on deploying and configuring the special Group Policy, please see [How to use Group Policy to deploy a Known Issue Rollback](/en-us/troubleshoot/windows-client/group-policy/use-group-policy-to-deploy-known-issue-rollback).

**Workaround #2: Disable Machine Identity Isolation manually**

*Important: This section contains information about modifying the registry. Before you modify the registry, back it up and make sure that you know how to restore it if a problem occurs. For more information, see *[*How to back up and restore the registry in Windows*](https://support.microsoft.com/help/322756)*.* 

To work around this issue, disable Machine Identity Isolation using the same management method that was used to enable it. Choose the applicable option below: 

1. ​If Machine Identity Isolation was enabled by Intune policy, [disable Machine Identity Isolation with Intune](/en-us/windows/client-management/mdm/policy-csp-deviceguard#machineidentityisolation).
2. ​If Machine Identity Isolation was enabled by group policy, [disable Machine Identity Isolation with group policy](/en-us/windows-server/identity/ad-ds/manage/delegated-managed-service-accounts/credential-guard-protected-machine-accounts#machine-identity-isolation).
3. ​If Machine Identity Isolation was enabled directly in the registry, use these steps to disable it:

- ​On the Windows 11, version 26H2 device, locate the following registry paths: 
    - ​HKLM\SYSTEM\CurrentControlSet\Control\Lsa\MachineIdentityIsolation
    - ​HKLM\SOFTWARE\Policies\Microsoft\Windows\DeviceGuard\MachineIdentityIsolation
- ​For either of these registry keys, if the value for MachineIdentityIsolation = 2, then set **MachineIdentityIsolation = 0**.

After you disable Machine Identity Isolation, restart the device. 

Then reset the secure channel using the following command:

```
	 'Test-ComputerSecureChannel -Repair -Credential (Get-Credential)' 
```

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

### August 2026

#### Incorrect notifications that "Microsoft Defender Antivirus is turned off"

| **Status** | **Originating update** | **History** |
| --- | --- | --- |
 Resolved | N/A | Resolved: 2026-09-30, 16:42 PTOpened: 2026-08-28, 15:34 PT |

After installing [Microsoft Defender Antivirus update (version 4.18.26070.9)](/en-us/defender-endpoint/microsoft-defender-endpoint-releases#release-details-65), released on August 5, 2026, notifications might appear stating that "Microsoft Defender Antivirus is turned off," even though the antivirus is functioning correctly and all settings show it as active. These notifications can appear when Windows starts and intermittently afterward. They persist even if notification settings are turned off.

This issue can be observed in any version of Windows or Windows Server with Microsoft Defender Antivirus running with the latest Defender updates.

**Resolution: **This issue was resolved in [Microsoft Defender Antivirus update (version 4.18.26080.4)](https://www.microsoft.com/wdsi/defenderupdates), released on September 17, 2026.

**Affected platforms:**

- ​Client: Windows 11, version 26H1; Windows 11, version 25H2; Windows 11, version 24H2; Windows 11, version 23H2; Windows 10, version 22H2; Windows 10, version 21H2; Windows 10 Enterprise LTSC 2019; Windows 10 Enterprise LTSC 2016
- ​Server: Windows Server 2025; Windows Server 2022; Windows Server 2019; Windows Server 2016; Windows Server 2012 R2; Windows Server 2012

Back to top

## Report a problem with Windows updates

To report an issue to Microsoft at any time, use the [Feedback Hub](feedback-hub:) app. To learn more, see [Send feedback to Microsoft with the Feedback Hub app](https://support.microsoft.com/windows/send-feedback-to-microsoft-with-the-feedback-hub-app-f59187f8-8739-22d6-ba93-f66612949332). 

## Need help with Windows updates?

Search, browse, or ask a question on the [Microsoft Support Community](https://answers.microsoft.com/). If you are an IT pro supporting an organization, visit Windows release health on the [Microsoft 365 admin center](/en-us/windows/deployment/update/check-release-health) for additional details. 

For direct help with your home PC, use the Get Help app in Windows or contact [Microsoft Support](https://support.microsoft.com/). Organizations can request immediate support through [Support for business](https://support.serviceshub.microsoft.com/supportforbusiness/onboarding). 

## View this site in your language

This site is available in [11 languages](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/windows-release-health-now-localized-in-10-languages/ba-p/2530167): English, Chinese Traditional, Chinese Simplified, French (France), German, Italian, Japanese, Korean, Portuguese (Brazil), Russian, and Spanish (Spain). All text will appear in English if your browser default language is not one of the 11 supported languages. To manually change the display language, scroll down to the bottom of this page, click on the current language displayed on the bottom left of the page, and select one of the 11 supported languages from the list.