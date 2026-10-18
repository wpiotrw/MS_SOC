---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Overview of Basic Mobility and Security - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-overview?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: vpattnaik
author: vpattnai
manager: dansimp
ms.date: 2025-08-14T00:00:00.0000000Z
audience: Admin
ms.topic: overview
ms.service: microsoft-365-security
ms.localizationpriority: medium
ms.collection:
- Tier3
- scotvorg
- highpri
- M365-subscription-management
- Adm_O365
- Adm_TOC
- basic-mobility-security
- trust-pod
ms.custom:
- VSBFY23
- AdminSurgePortfolio
- AdminTemplateSet
- basic-mobility-security
search.appverid:
- MET150
description: Manage and secure connected to your Microsoft 365 organization by setting up and using Basic Mobility and Security.
locale: en-us
document_id: 7ef712db-8d3f-229c-3140-fe605c7535df
document_version_independent_id: 7ef712db-8d3f-229c-3140-fe605c7535df
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-overview.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/security-and-compliance/m365b-devices-basic-mobility-security-overview
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-overview.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/a72e95ff-4b4f-4cc1-90c6-7dcba67ff05f
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/24dc3ccd-591a-4415-a1fe-8759afafcb12
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 79ad3034-679b-4483-93dd-56c1bcef18c5
---

# Overview of Basic Mobility and Security - Microsoft 365 admin | Microsoft Learn

Basic Mobility and Security is a subset of [Microsoft Intune](/en-us/intune/intune-service/fundamentals/what-is-intune) in Microsoft 365 Business Basic and Microsoft 365 Business Standard (and other Microsoft 365/Office 365 subscriptions). Basic Mobility and Security is a free mobile device management (MDM) solution that allows organizations to:

- Manage and secure devices in Microsoft 365.
- Control access to company resources (for example, email, calendar, contacts, and documents) using supported apps.

Tip

In contrast to MDM where the organization fully manages the device, mobile app management (MAM) leaves control of the device with the user, but policies control access only to company resources on the device. MAM is more suitable for personal devices (also known as bring your own device or BYOD), while MDM is more suitable for company owned devices. For example, you can't factory reset a device in MAM (which would delete personal data), but you can remove company resources from the device.

Microsoft Intune supports both MDM and MAM device management strategies, and supports more device platforms (for example, macOS and Linux). For a comparison of Basic Mobility and Security and Microsoft Intune, see the Comparison of Basic Mobility and Security and Microsoft Intune section later in this article.

The high-level steps to manage devices in Basic Mobility and Security are described in the following list:

1. An admin turns on Basic Mobility and Security in the organization and configures organization settings. For instructions, see [Set up Basic Mobility and Security](m365b-devices-basic-mobility-security-set-up).
2. An admin configures one or more policies in Basic Mobility and Security that specify required device settings and access to device features. For instructions, see [Configure policies in Basic Mobility and Security](m365b-devices-basic-mobility-security-policies-configure).
3. Users enroll their devices in Basic Mobility and security, or admins enroll the devices before they're given to users. Either way, enrollment happens on the device itself. For instructions, see [Enroll your device in Basic Mobility and Security](m365b-devices-basic-mobility-security-enroll-devices).
4. After the devices are enrolled, users can access company resources using supported apps, and admins can wipe devices and view details about devices, because the organization fully manages the devices. For more information, see the following articles:

    - [View device details in Basic Mobility and Security](m365b-devices-basic-mobility-security-view-device-details)
    - [Wipe devices in Basic Mobility and Security](m365b-devices-basic-mobility-security-wipe-devices)

    Admins can also modify the settings in existing policies, and modify the organization settings.

Although you can't turn off Basic Mobility and Security in an organization, you can effectively disable it and remove device management from devices. For instructions, see [Turn off Basic Mobility and Security enforcement](m365b-devices-basic-mobility-security-turn-off).

The rest of this article describes the supported devices and capabilities in Basic Mobility and Security.

## Supported device platforms in Basic Mobility and Security

You can manage the following device platforms in Basic Mobility and Security:

- **iOS/iPadOS devices**: For supported iOS and iPadOS version information, see [Apple operating systems supported in Microsoft Intune](/en-us/intune/intune-service/fundamentals/supported-devices-browsers#apple)
- **Android devices, including Samsung Knox on Samsung mobile devices**^\*^: For specific Android, Samsung Knox, and Android open source project device support information, see [Android operating systems supported in Microsoft Intune](/en-us/intune/intune-service/fundamentals/supported-devices-browsers#android).

    ^\*^Only Samsung Knox devices on Android version 9.0 or later support password settings management in Basic Mobility and Security.
- **Windows 10 and Windows 11 devices**: Both traditional PCs and Windows on ARM devices are supported. For more information about supported versions of Windows, see [Microsoft operating systems supported in Microsoft Intune](/en-us/intune/intune-service/fundamentals/supported-devices-browsers#microsoft).

Tip

Microsoft Intune supports other types of devices, including macOS and Linux computers. For more information, see the Comparison of Basic Mobility and Security and Microsoft Intune section later in this article.

## Policy types in Basic Mobility and Security

There are two different types of policies in Basic Mobility and Security. Both control access to company resources on supported devices platforms. The main difference is whether the user is prompted to enroll the device:

- **Allow access policies**: If a user tries to access company resources using a supported app on an unenrolled device, **the user is prompted to enroll the device in Basic Mobility and Security; device enrollment starts automatically**.

    This type of policy corresponds to the **Allow access (device enrollment required)** selection in the new policy wizard, and the **New-DeviceConfigurationPolicy** and **New-DeviceConfigurationRule** cmdlets in Security & Compliance PowerShell.
- **Block access policies**: If a user tries to access company resources using a supported app on an unenrolled device, access is blocked. **The user isn't prompted to enroll the device; they need to start the device enrollment manually**.

    This type of policy corresponds to the **Block access** selection in the new policy wizard, and the **New-DeviceConditionalAccessPolicy** and **New-DeviceConditionalAccessRule** cmdlets in Security & Compliance PowerShell.

    The following diagram shows what happens when a user tries to access company resources using the Microsoft 365 app on an unenrolled device. The applicable policy in Basic Mobility and Security is a **block access** policy, so the user is prompted to enroll the device before they can access company resources in the app.

    [![A conceptual diagram that explains the steps in access control from supported apps in Basic Mobility and Security.](../../media/microsoft-365-bsm-app-diagram.png)](../../media/microsoft-365-bsm-app-diagram.png#lightbox)

After the device is enrolled in Basic Mobility and Security, and the device meets any access requirement settings in the applicable policy, the user can access company resources on the device using supported apps as described in the next section.

Tip

After you create a policy, you can't change it from allow access to block access. You need to create a new policy with the same settings, and then delete the original policy.

## Apps that prompt users to enroll in Basic Mobility and Security

After an admin sets up Basic Mobility and Security and configures policies that identify users to enroll, certain apps are able to prompt users to enroll their devices in Basic Mobility and Security before they can access company resources in the app. These apps that support *access control* are described in the following table:

| App | iOS/iPadOS | Android phones | Android tablets | Windows |
| --- | --- | --- | --- | --- |
| The built-in email app | ✔ | ✔ | ✔ | ✔&lt;\*&gt; |
| The Microsoft 365 app | ✔ |  |  |  |
| OneDrive | ✔ | ✔ | ✔ |  |
| Excel | ✔ | ✔ | ✔ |  |
| Outlook | ✔ | ✔ | ✔ |  |
| PowerPoint | ✔ | ✔ | ✔ |  |
| Word | ✔ | ✔ | ✔ |  |

&lt;\*&gt; Requires extra Microsoft Entra P1 or P2 licenses. Launching the app in organizations with only Microsoft Entra Free licenses (included in Business Basic and Business Standard) doesn't prompt Windows users to enroll their devices in Basic Mobility and Security.

Important

Users aren't prompted to enroll their device and aren't blocked from accessing resources if they use a **mobile web browser** to access the following company resources:

- Microsoft 365 SharePoint sites.
- Documents in Microsoft 365 on the web.
- Information in Outlook on the web (formerly known as Outlook Web App or OWA).

## Policy settings in Basic Mobility and Security

For both **allow access policies** and **block access policies** in Basic Mobility and Security, the following types of policy settings are available when you create or modify policies:

- **Access requirement settings**: These settings are described in the Access requirement settings section. If the device doesn't meet the setting configuration (for example, password, encryption, or jail broken settings), users are prompted to update the device to continue to access company resources. If they don't update the setting, they can't access company resources on the device using supported apps.

    The following diagram shows what happens when a user tries to access company resources using the Office Mobile app on an enrolled device. The applicable policy requires a device password, but the device doesn't have a password.

    [![Basic Mobility and Security compliance message.](../../media/bms-2-device-not-compliant.png)](../../media/bms-2-device-not-compliant.png#lightbox)
- **Configuration settings**: These settings are described in the Configuration settings section. These settings control access to features on the device (for example, not allowing screen captures on supported devices) and are automatically configured on the device without user input.

For policy creation and management instructions, see [Configure policies in Basic Mobility and Security](m365b-devices-basic-mobility-security-policies-configure).

Tip

Although policies in Basic Mobility and Security support many settings, not all settings are supported on all device platforms.

Polices in Basic Mobility and Security override [mobile device mailbox polices](/en-us/exchange/clients-and-mobile-in-exchange-online/exchange-activesync/mobile-device-mailbox-policies) in Exchange Online. You configure these policies in the Exchange admin center at https://admin.exchange.microsoft.com/#/mobiledevicemailboxpolicy or in Exchange Online PowerShell using the **\*-MobileDeviceMailboxPolicy** or **\*-ActiveSyncMailboxPolicy** cmdlets. After a device is enrolled in Basic Mobility and Security, any applicable mobile device mailbox policies are ignored.

### Access requirement settings

The settings in the following table are required on enrolled devices. Users must update their settings to meet the requirements. Otherwise, they can't access company resources using supported apps.

These settings are available on the **Access requirements** page in the new policy wizard, in the **Access requirements** section in the details flyout of the policy, or in [Security & Compliance PowerShell](m365b-devices-basic-mobility-security-policies-configure#manage-policies-in-security--compliance-powershell).

Tip

- For **Windows**devices:
    - Supported settings on noncompliant Windows devices don't block users from accessing Microsoft 365 resources.
    - In **Allow access** policies, the first use of Outlook for Windows (new Outlook) or the Mail app to access a Microsoft 365 mailbox requires enrollment in Basic Mobility and security *only in organizations with Microsoft Entra P1 or P2 licenses* (not included in Business Basic or Business Standard).
    - Supported password settings apply to local accounts only, not to accounts in Active Directory or Microsoft Entra ID.

| Setting | iOS/iPadOS | Android | Samsung Knox | Windows | Comments |
| --- | --- | --- | --- | --- | --- |
| **Require a password** (*PasswordRequired*) | ✔ |  |  |  | Selected by default in new policies. This setting must be selected to configure any other password settings. |
| **Prevent simple passwords (iOS)** (*AllowSimplePassword*) | ✔ |  |  |  | Selected by default in new policies. |
| **Require an alphanumeric password (iOS)** (*PasswordMinComplexChars*) | ✔ |  |  | ✔ | The default value when you select this setting in new policies is: Password must include at least **4 character sets**. Valid values are 1 to 4. |
| **Require minimum password length** (*PasswordMinimumLength*) | ✔ | ✔ | ✔ | ✔ | The default value when you select this setting in new policies is: **4 characters**. Valid values are 4 to 14. |
| **Number of sign-in failures before device is wiped** (*MaxPasswordAttemptsBeforeWipe*) | ✔ | ✔ | ✔ | ✔ | The default value when you select this setting in new policies is: **4 attempts**. Valid values are 4 to 11. |
| **Lock devices if they are inactive for this many minutes** (*PasswordTimeout*) | ✔ |  |  | ✔ | The default value when you select this setting in new policies is: **4 minutes**. Valid values are 1 to 60. **Note**: This setting is no longer supported in Android and Samsung Knox. |
| **Password expiration** (*PasswordExpirationDays*) | ✔ | ✔ | ✔ | ✔ | The default value when you select this setting in new policies is: **4 days**. Valid values are 1 to 255. |
| **Remember password history and prevent reuse** (*PasswordHistoryCount*) | ✔ | ✔ | ✔ | ✔ | The default value when you select this setting in new policies is: Store up to **4 previous passwords**. Valid values are 1 to 24. |
| **Require data encryption on devices (Android, Samsung Knox)** (*PhoneMemoryEncrypted*) |  | ✔ | ✔ |  | In Samsung Knox, you can also require encryption on storage cards. |
| **Prevent jail broken ar rooted devices from connecting** (*AllowJailbroken*) | ✔ | ✔ | ✔ |  | This setting is always selected and you can't change it when you create or modify policies on the **Policies** tab of the **Basic Mobility and Security** page. If you create a **block access** policy (which corresponds to creating the policy using the **New-DeviceConditionalAccessPolicy** and **New-DeviceConditionalAccessRule** cmdlets in Security & Compliance PowerShell), you can modify this setting in PowerShell after the creation of the policy. For more information, see [Use PowerShell to create policies in Basic Mobility and Security](m365b-devices-basic-mobility-security-policies-configure#use-powershell-to-create-policies-in-basic-mobility-and-security). |
| **Require managing email profile (iOS - required for selective wipe)** (*RequireEmailProfile*) | ✔ |  |  |  | Blocks access to Microsoft 365 email using manually created email profiles. iOS/iPadOS device users must delete manually created email profiles before they can access their email. After they delete the profile, a new profile is automatically created. For instructions on how users can get compliant, see [Device already has an email profile installed](/en-us/troubleshoot/mem/intune/device-configuration/troubleshoot-email-profiles-in-microsoft-intune#device-already-has-an-email-profile-installed). |

### Configuration settings

These settings are automatically configured on the device without user input.

These settings are available on the **Configurations** page in the new policy wizard, in the **Configurations** section in the details flyout of the policy, or in [Security & Compliance PowerShell](m365b-devices-basic-mobility-security-policies-configure#manage-policies-in-security--compliance-powershell).

| Setting | iOS/iPadOS | Android | Samsung Knox | Windows | Comments |
| --- | --- | --- | --- | --- | --- |
| **Require encrypted backup (iOS)** (*ForceEncryptedBackup*) | ✔ |  |  |  | iOS/iPadOS encrypted backup is required. |
| **Block cloud backup (iOS supervised)** (*AllowiCloudBackup*) | ✔ |  |  |  | Block iCloud Backup on [supervised iOS/iPadOS devices](https://support.apple.com/102291). |
| **Block cloud document synchronization (iOS supervised)** (*AllowiCloudDocSync*) | ✔ |  |  |  | Block iCloud Drive synchronization on [supervised iOS/iPadOS devices](https://support.apple.com/102291). |
| **Block My Photo Stream (iOS)** (*AllowiCloudPhotoSync*) | ✔ |  |  |  | Block iCloud Photos synchronization. |
| **Block screen capture (iOS, Samsung Knox)** (*AllowScreenshot*) | ✔ |  | ✔ |  | Blocked when attempted. |
| **Block FaceTime (iOS supervised)** (*AllowVideoConferencing*) | ✔ |  |  |  | Block access to FaceTime on [supervised iOS/iPadOS devices](https://support.apple.com/102291). |
| **Block sending diagnostic data from devices (iOS, Samsung Knox)** (*AllowDiagnosticSubmission*) | ✔ |  | ✔ | ✔ | Block sending diagnostic and usage data. |
| **Block access to application store (iOS supervised, Samsung Knox)** (*AllowAppStore*) | ✔ |  | ✔ |  | Requires [supervised devices](https://support.apple.com/102291) for iOS/iPadOS.  App store icon is missing on Android home screens, disabled on supervised iOS/iPadOS device home screens. |
| **Require password when accessing application store (iOS)** (*ForceAppStorePassword*) | ✔ |  |  |  | Not selectable if **Block access to application store** is selected. |
| **Block connection with removable storage (Samsung Knox)** (*EnableRemovableStorage*) |  |  | ✔ |  | The SD card is grayed out in device settings. Apps installed on the SD card can't run. |
| **Block Bluetooth connection (Samsung Knox)** (*BluetoothEnabled*) |  |  | ✔ |  | Technically, we can't disable BlueTooth as a setting in Android. Instead, we disable all the transactions that require BlueTooth: <br>- Advanced Audio Distribution<br>- Audio/Video Remote Control<br>- Hands-free devices<br>- Headsets<br>- Phone Book Access<br>- Serial Port<br><br> A small toast message appears at the bottom of the screen when users attempt to connect to these devices or services. |

### Exclusive policy settings in Security & Compliance PowerShell

The settings in the following table are available only on the **New-DeviceConfigurationRule** or **Set-DeviceConfigurationRule** cmdlets (**allow access policies**) and **New-DeviceConditionalAccessRule** or **Set-DeviceConditionalAccessRule** cmdlets (**block access policies**) in [Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell):

| Setting | iOS/iPadOS | Android | Samsung Knox | Windows | Comments |
| --- | --- | --- | --- | --- | --- |
| *AllowAssistantWhileLocked* | ✔ |  |  |  | Block the use of Siri while iOS/iPadOS devices are locked. |
| *AllowConvenienceLogon* |  |  |  | ✔ | Block sign in using other methods (for example, fingerprints or facial recognition). |
| *AllowPassbookWhileLocked* | ✔ |  |  |  | Block the use of Apple Wallet while iOS/iPadOS devices are locked. |
| *AllowVoiceAssistant* | ✔ |  |  |  | Block the use of Siri on iOS/iPadOS devices. |
| *AllowVoiceDialing* | ✔ |  |  |  | Block voice-activated telephone dialing by Siri on iOS/iPadOS devices. |
| *AntiVirusSignatureStatus* |  |  |  | ✔ |  |
| *AntiVirusStatus* |  |  |  | ✔ |  |
| *AppsRating* | ✔ |  |  |  | Specifies the most restrictive rating for apps allowed on iOS/iPAadOS devices. For details, see [AppsRating](/en-us/powershell/module/exchangepowershell/new-deviceconfigurationrule#-appsrating). |
| *AutoUpdateStatus* |  |  |  | ✔ | Specifies the required update settings for devices. For details, see [AutoUpdateStatus](/en-us/powershell/module/exchangepowershell/new-deviceconfigurationrule#-autoupdatestatus). |
| *CameraEnabled* | ✔ | ✔ |  |  | Disables the camera. |
| *FirewallStatus* |  |  |  | ✔ | Specifies the acceptable firewall status on devices. The only available value is blank or `Required`. |
| *MaxPasswordGracePeriod* | ✔ |  |  |  | The time window in which users can reset expired passwords on iOS/iPadOS devices. |
| *MoviesRating* | ✔ |  |  |  | Specifies the most restrictive rating for movies allowed on iOS/iPAadOS devices. For details, see [MoviesRating](/en-us/powershell/module/exchangepowershell/new-deviceconfigurationrule#-moviesrating). |
| *PasswordQuality* |  | ✔ | ✔ |  | A numeric scale that indicates the security and complexity of the password. A higher value indicates a more secure password. |
| *RegionRatings* | ✔ |  |  |  | Specifies the rating system (country/region) to use for movie and television ratings with the MoviesRating and TVShowsRating parameters. For details, see [RegionRatings](/en-us/powershell/module/exchangepowershell/new-deviceconfigurationrule#-regionratings). |
| *SmartScreenEnabled* |  |  |  | ✔ |  |
| *SystemSecurityTLS* | ✔ |  |  |  | Specifies whether TLS encryption is required on iOS/iPadOS devices. |
| *TVShowsRating* | ✔ |  |  |  | Specifies the most restrictive rating for television shows allowed on iOS/iPadOS devices. For details, see [TVShowsRating](/en-us/powershell/module/exchangepowershell/new-deviceconfigurationrule#-tvshowsrating). |
| *UserAccountControlStatus* |  |  |  | ✔ | Specifies how UAC notifications are shown on devices. For details, see [UserAccountControlStatus](/en-us/powershell/module/exchangepowershell/new-deviceconfigurationrule#-useraccountcontrolstatus). |
| *WLANEnabled* |  |  |  | ✔ | Disables Wi-Fi on devices. |
| *WorkFoldersSyncUrl* |  |  |  | ✔ | Specifies the Work Folders URL on a Windows Server that's used to synchronize company resources on devices. For more information about Work Folders, see [Work Folders overview](/en-us/windows-server/storage/work-folders/work-folders-overview). |

For information about configuring policies in PowerShell, see [Use PowerShell to create policies in Basic Mobility and Security](m365b-devices-basic-mobility-security-policies-configure#use-powershell-to-create-policies-in-basic-mobility-and-security).

Tip

You can disable policies only in Security & Compliance PowerShell (the **Status** value of the policy is **Off** on the **Policies** tab of the **Basic Mobility and Security** page). For instructions, see [Use PowerShell to modify device policies](m365b-devices-basic-mobility-security-policies-configure#use-powershell-to-modify-device-policies).

## Privacy and security in Basic Mobility and Security

Microsoft Intune sends information to Microsoft 365 about the compliance status of each managed device. You can generate reports that show whether managed devices in your organization are compliant based on the applicable policies. To learn more about Microsoft's commitment to the privacy and security, see the [Microsoft Trust Center](https://www.microsoft.com/trust-center).

## Comparison of Basic Mobility and Security and Microsoft Intune

If you choose to upgrade the device protection capabilities in Basic Mobility and Security, the natural options are:

- Microsoft Defender for Business
- Microsoft Intune

    Tip

    After you purchase Microsoft Intune licenses, you can manage devices using both Intune and Basic Mobility and Security. *First, set up Basic Mobility and Security, then set up Intune*. This method allows you to choose Basic Mobility and Security or the more feature-rich Intune solution.
- Microsoft 365 Business Premium (which includes Defender for Business and Intune)

The following table compares the device protection features of Basic Mobility and Security and Intune. For more information on Intune actions, see [Microsoft Intune documentation](/en-us/intune/intune-service/).

| Feature area | Feature highlights | Basic Mobility and Security | Microsoft Intune |
| --- | --- | --- | --- |
| Supported device platforms | Manage different platforms and major management mode variants. | - iOS/iPadOS<br>- Android<br>- Samsung Knox<br>- Windows PCs | - iOS/iPadOS<br>- Android<br>- Samsung Knox<br>- Windows PCs<br>- macOS |
| Device compliance | Set and manage security policies, like device level PIN lock and jailbreak detection. | Limited^1^ | ✔ |
| Conditional access based on device compliance | Prevent noncompliant devices from accessing corporate email and data from the cloud. | Limited^2^ | ✔ |
| Device configuration | Configure device settings (for example, disabling the camera) | Limited^3^ | ✔ |
| Email profiles | Create a native email profile on the device. | ✔ | ✔ |
| Wi-Fi profiles | Create a native Wi-Fi profile on the device. |  | ✔ |
| VPN profiles | Create a native VPN profile on the device. |  | ✔ |
| Mobile application management (MAM) | Control how apps access and share data on mobile devices. For example, restrict actions like copy, cut, paste, and save as to apps approved for corporate data only. |  | ✔ |
| Mobile application deployment | Deploy your internal line-of-business apps and from apps stores to users. |  | ✔ |
| Managed browser | Enable more secure web browsing using the Microsoft Edge app. |  | ✔ |
| Zero touch enrollment programs (Autopilot) | Enroll large numbers of corporate-owned devices, while simplifying user setup. |  | ✔ |
| **Remote device actions** | Send commands to devices over the internet. |  |  |
| Remove company resources (retire) | Remove company resources and settings while leaving personal data. | ✔ | ✔ |
| Factory reset (full wipe) | Reset a device to its factory settings. | ✔ | ✔ |
| [Remote Windows Autopilot reset](/en-us/autopilot/windows-autopilot-reset#reset-devices-with-remote-windows-autopilot-reset) |  |  | ✔ |
| [BitLocker key recovery for Windows devices](https://support.microsoft.com/windows/6b71ad27-0b89-ea08-f143-056f5ab347d6) |  |  | ✔ |
| [Disable activation lock on Apple devices](/en-us/intune/intune-service/remote-actions/device-activation-lock-disable) |  |  | ✔ |
| [Enable Lost mode on iOS/iPadOS devices](/en-us/intune/intune-service/remote-actions/device-lost-mode) |  |  | ✔ |
| [Fresh Start on Windows devices](/en-us/intune/intune-service/remote-actions/device-fresh-start) |  |  | ✔ |
| [Locate lost or stolen devices](/en-us/intune/intune-service/remote-actions/device-locate) |  |  | ✔ |
| [PIN reset on Windows devices](/en-us/windows/security/identity-protection/hello-for-business/hello-feature-pin-reset) |  |  | ✔ |
| [Remote lock](/en-us/intune/intune-service/remote-actions/device-remote-lock) |  |  | ✔ |
| [Remotely restart devices](/en-us/intune/intune-service/remote-actions/device-restart) |  |  | ✔ |
| [Rename devices](/en-us/intune/intune-service/remote-actions/device-rename) |  |  | ✔ |
| [Reset or remove device passcodes](/en-us/intune/intune-service/remote-actions/device-passcode-reset) |  |  | ✔ |
| [Run Microsoft Defender Antivirus scans on Windows devices](/en-us/defender-endpoint/run-scan-microsoft-defender-antivirus#use-microsoft-intune-to-run-a-scan) |  |  | ✔ |
| [Send custom notifications on iOS/iPadOS and Android devices](/en-us/intune/intune-service/remote-actions/custom-notifications#send-a-custom-notification-to-a-single-device) |  |  | ✔ |
| [Synchronize devices](/en-us/intune/intune-service/remote-actions/device-sync) |  |  | ✔ |
| [TeamViewer (remote control)](/en-us/intune/intune-service/remote-actions/teamviewer-support) |  |  | ✔^4^ |

^1^ Limited on Android devices as previously described in the Access requirement settings section.

^2^ Not supported on Windows PCs. Limited to controlling access to Exchange Online, SharePoint, and Outlook.

^3^ Limited to settings previously described in the Configuration settings section. Intune settings are described in [Apply features and settings on your devices using device profiles in Microsoft Intune](/en-us/intune/intune-service/configuration/device-profiles).

^4^ Purchased separately.

## Basic Mobility and Security FAQ

### Q: How can I get Basic Mobility and Security? I don't see it in the Microsoft 365 admin center

A: Activate Basic Mobility and Security by going to the **Basic Mobility and Security** page at https://compliance.microsoft.com/basicmobilityandsecurity.

### Q: How can I get started with device management in Basic Mobility and Security?

A: For instructions, see [Set up Basic Mobility and Security in Microsoft 365 for business](m365b-devices-basic-mobility-security-set-up).

### Q: I'm trying to set up Basic Mobility and Security but it seems stuck. The Microsoft 365 Service Health has been showing "provisioning" for a while. What can I do?

A: It might take some time to get the service ready for you. When provisioning is complete, you see the **Basic Mobility and Security** page. If the status is still provisioning after 24 hours, contact Support so we can help you.

### Q: I'm running into issues when I try to enroll a device in Basic Mobility and Security. What can I do?

A: Check the following items:

- Verify the device isn't already enrolled in another mobile device management provider, such as Microsoft Intune.
- Verify the date and time on the device are correct.
- Connect to a different Wi-Fi or cellular network on the device.
- For Android or iOS/iPadOS devices, uninstall and reinstall the Intune Company Portal app on the device.

### Q: I'm having issues setting up Basic Mobility and Security on iOS/iPadOS devices. What can I do?

A: Check the following items:

- Verify you set up an APNs certificate. For more information, see [Create an Apple Push Notification service certificate for Apple devices](m365b-devices-basic-mobility-security-set-up#step-3-create-an-apple-push-notification-service-certificate-for-apple-devices).
- On the iOS/iPadOS device, go to **Settings** &gt; **General** &gt; **VPN & Device Management** and verify a **Management Profile** isn't already installed. If it is, remove it.
- **Device failed to enroll** error: Verify the user signed in to Microsoft 365 has a license assigned that includes an Exchange Online license.
- **Profile failed to install**error: Try one of the following steps:
    - Verify Safari is the default browser on the device and that cookies aren't disabled.
    - Reboot the device, open &lt;portal.manage.microsoft.com&gt;, sign in with your Microsoft 365 account, and then attempt to install the profile manually.

### Q: I'm having issues setting up Basic Mobility and Security on Windows PCs. What can I do?

A: Check the following items:

- Verify the custom domain for Microsoft 365 accounts is configured to work with Basic Mobility and Security. For instructions, see [Configure CNAME records in DNS for Basic Mobility and Security for custom Microsoft 365 domains](m365b-devices-basic-mobility-security-set-up#step-2-configure-cname-records-for-custom-microsoft-365-domains-in-basic-mobility-and-security).
- Unless you paid extra for Microsoft Entra ID P1 or P2, verify users select **Enroll in Device Management only** instead of **Connect**.

### Q: I'm having issues setting up Basic Mobility and Security on Android devices. What can I do?

A: Check the following items:

- Verify the device is running Android.
- Verify Chrome is the default browser on the device and that it's up to date.
- **We couldn't enroll this device** error: Verify the user signed in to Microsoft 365 has a license assigned that includes an Exchange Online license.
- Complete any actions in the Notification Area on the device.

### Q: What's the difference between Intune and Basic Mobility and Security?

A: The Intune service hosts Basic Mobility and Security as a free cloud-based solution for managing devices in your organization. Basic Mobility and Security is a subset of Intune services. For a comparison, see the Comparison of Basic Mobility and Security and Microsoft Intune section.

### Q: How do policies work for Basic Mobility and Security? How do I set them up? Disable them?

A: See the following articles:

- [Configure policies in Basic Mobility and Security](m365b-devices-basic-mobility-security-policies-configure)
- [Turn off Basic Mobility and Security enforcement](m365b-devices-basic-mobility-security-turn-off)

### Q: Can I switch from Exchange ActiveSync device management to Basic Mobility and Security for Microsoft 365?

A: Polices in Basic Mobility and Security override [mobile device mailbox polices](/en-us/exchange/clients-and-mobile-in-exchange-online/exchange-activesync/mobile-device-mailbox-policies) in Exchange Online. You create these policies in the Exchange admin center at https://admin.exchange.microsoft.com/#/mobiledevicemailboxpolicy or in Exchange Online PowerShell using the **\*-MobileDeviceMailboxPolicy** or **\*-ActiveSyncMailboxPolicy** cmdlets. After a device is enrolled in Basic Mobility and Security, any applicable mobile device mailbox policies are ignored.

### Q: I set up Basic Mobility and Security but now I want to remove it. What are the steps?

A: Although you can't completely turn off, disable, or unprovision Basic Mobility and Security in your organization, you can remove the enforcement of Basic Mobility and Security on devices. For instructions, see [Turn off Basic Mobility and Security enforcement](m365b-devices-basic-mobility-security-turn-off).