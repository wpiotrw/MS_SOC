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
ms.date: 2026-11-12T00:00:00.0000000Z
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
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/19ec6774-09b8-473e-a17e-b17b518bbad7
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ade36b61-c646-4bd8-87ee-f3a843461962
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
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
| **SQL Server linked server connections might remain open**Connections to external databases such as Oracle and PostgreSQL can accumulate over time | OS Build 26200.9711[KB5127648](https://support.microsoft.com/help/5127648)2026-10-13 | Confirmed | 2026-11-11 15:37 PT |
| **USB audio devices might fail to start or produce no sound**Some USB Audio Class 1.0 devices display Code 10 or fail in multichannel audio modes after installing the Sept. 8 update | OS Build 26200.9445[KB5124008](https://support.microsoft.com/help/5124008)2026-09-08 | Resolved[KB5132061](https://support.microsoft.com/help/5132061) | 2026-11-10 10:27 PT |
| **Remote Desktop connections might fail for non-admin users with error 0xC000000D**This issue affects non-admin users connecting through Remote Desktop with Administrator protection enabled. | OS Build 26200.9550[KB5124010](https://support.microsoft.com/help/5124010)2026-09-22 | Resolved[KB5127936](https://support.microsoft.com/help/5127936) | 2026-10-28 22:02 PT |

## Issue details

### November 2026

#### SQL Server linked server connections might remain open

| **Status** | **Originating update** | **History** |
| --- | --- | --- |
 Confirmed | OS Build 26200.9711[KB5127648](https://support.microsoft.com/help/5127648)2026-10-13 | Last updated: 2026-11-11, 15:37 PTOpened: 2026-11-11, 15:11 PT |

After Windows updates released October 13, 2026 ([KB5127648](https://support.microsoft.com/help/5127648)), and later are installed on server devices, connections created by SQL Server linked server queries might remain open after the queries complete. As additional queries are performed, connections to external databases can accumulate instead of closing as expected. This can slow or degrade server performance after prolonged run time.

This issue affects SQL Server linked server queries that use OLE DB providers to connect to external databases. Oracle and PostgreSQL connections are among those known to be affected. In affected environments, administrators might observe an increasing number of open connections to external databases, even when the associated SQL Server linked server queries are no longer running.

If idle connections can be identified, it is possible to manually close them in order to temporarily relieve server load. It is also possible to temporarily restore system stability by restarting the SQL service. However, these steps can also interrupt active queries or transactions, and the problem can resurface again after sufficient operation time.

**Workaround:** A mitigation is available for affected enterprise devices. To apply this mitigation in your organization, contact [Microsoft Support for business](https://support.microsoft.com/contactus).

**Next steps**: We will address this issue with an out-of-band update that will be released in the next few days. We will update this documentation once the update is released.

**Affected platforms:**

- ​Client: Windows 11, version 26H1; Windows 11, version 25H2; Windows 11, version 24H2; Windows 11, version 23H2; Windows 10, version 1809; Windows 10 Enterprise LTSC 2019
- ​Server: Windows Server 2025; Windows Server 2022; Windows Server, version 1809; Windows Server 2016; Windows Server 2012 R2; Windows Server 2012

Back to top

#### USB audio devices might fail to start or produce no sound

| **Status** | **Originating update** | **History** |
| --- | --- | --- |
 Resolved [KB5132061](https://support.microsoft.com/help/5132061) | OS Build 26200.9445[KB5124008](https://support.microsoft.com/help/5124008)2026-09-08 | Resolved: 2026-11-10, 10:00 PTOpened: 2026-11-09, 16:04 PT |

After installing the September 8, 2026, Windows security update ([KB5124008](https://support.microsoft.com/help/5124008)), some [USB Audio Class 1.0](/en-us/windows-hardware/drivers/audio/usb-audio-class-system-driver--usbaudio-sys-) devices might fail to start or produce audio. Affected devices might experience one or more of the following symptoms: 

- ​The device displays an error in Device Manager: "This device cannot start (Code 10).”
- ​No audio output.
- ​Volume controls are unresponsive or remain at zero.
- ​Sound settings are unresponsive or unavailable.
- ​Some devices might function in standard stereo configurations but fail when using multichannel audio features, including 8-channel or 3D audio modes. Some customers have reported that they're able to restore audio in these cases by switching to 2-channel mode. *(\*Note: This behavior is resolved in the out-of-band update released on September 14, 2026. See ****Resolution**** section below.)*

This issue is limited to USB Audio Class 1.0 devices.

**Resolution: **The symptoms experienced on devices using 8-channel or 3D audio modes (last bullet point in the list of symptoms documented in this entry) are resolved in the out-of-band (OOB) update released on September 14, 2026, and updates released after this date. The remaining symptoms are resolved in the Windows security update released on November 10, 2026 ([KB5132061](https://support.microsoft.com/help/5132061)) and later updates. We recommend you install the latest security update for your device as it contains important improvements and issue resolutions, including this one. 

If you are an IT administrator that contacted [Microsoft Support for Business](https://support.microsoft.com/support-for-business) to obtain an immediate workaround, you do not need to use the [Known Issue Rollback (KIR)](/en-us/troubleshoot/windows-server/installing-updates-features-roles/known-issue-rollback) or special group policy to resolve this issue.

**Affected platforms:**

- ​Client: Windows 11, version 26H2; Windows 11, version 26H1; Windows 11, version 25H2; Windows 11, version 24H2; Windows 11, version 23H2; Windows 10, version 22H2; Windows 10, version 21H2; Windows 10 Enterprise LTSC 2019; Windows 10 Enterprise LTSC 2016

- ​Server: Windows Server 2025; Windows Server 2022; Windows Server 2019; Windows Server 2016; Windows Server 2012 R2; Windows Server 2012

Back to top

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

## Report a problem with Windows updates

To report an issue to Microsoft at any time, use the [Feedback Hub](feedback-hub:) app. To learn more, see [Send feedback to Microsoft with the Feedback Hub app](https://support.microsoft.com/windows/send-feedback-to-microsoft-with-the-feedback-hub-app-f59187f8-8739-22d6-ba93-f66612949332). 

## Need help with Windows updates?

Search, browse, or ask a question on the [Microsoft Support Community](https://answers.microsoft.com/). If you are an IT pro supporting an organization, visit Windows release health on the [Microsoft 365 admin center](/en-us/windows/deployment/update/check-release-health) for additional details. 

For direct help with your home PC, use the Get Help app in Windows or contact [Microsoft Support](https://support.microsoft.com/). Organizations can request immediate support through [Support for business](https://support.serviceshub.microsoft.com/supportforbusiness/onboarding). 

## View this site in your language

This site is available in [11 languages](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/windows-release-health-now-localized-in-10-languages/ba-p/2530167): English, Chinese Traditional, Chinese Simplified, French (France), German, Italian, Japanese, Korean, Portuguese (Brazil), Russian, and Spanish (Spain). All text will appear in English if your browser default language is not one of the 11 supported languages. To manually change the display language, scroll down to the bottom of this page, click on the current language displayed on the bottom left of the page, and select one of the 11 supported languages from the list.