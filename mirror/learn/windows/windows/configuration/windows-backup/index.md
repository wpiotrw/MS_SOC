---
layout: Conceptual
title: Windows settings backup and restore Overview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/configuration/windows-backup/
recommendations: true
adobe-target: true
ms.collection:
- tier2
breadcrumb_path: /windows/resources/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Windows
ms.subservice: itpro-configure
ms.service: windows-client
manager: bpardi
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/windows/send-feedback-to-microsoft-with-the-feedback-hub-app-f59187f8-8739-22d6-ba93-f66612949332
description: Learn how to configure devices to use Windows settings backup and restore.
ms.date: 2026-10-29T00:00:00.0000000Z
ms.topic: overview
ms.author: shnaran
author: shilpasawhney-beep
locale: en-us
document_id: 0aec5cdd-0063-c4a3-2542-b11bac8c924c
document_version_independent_id: 0aec5cdd-0063-c4a3-2542-b11bac8c924c
original_content_git_url: https://github.com/MicrosoftDocs/windows-docs-pr/blob/live/windows/configuration/windows-backup/index.md
site_name: Docs
depot_name: TechNet.win-configuration
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/TechNet.win-configuration/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: windows-backup/index
moniker_range_name: 
monikers: []
item_type: Content
source_path: windows/configuration/windows-backup/index.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aebdc4a3-c54b-4eea-94e3-663d5e166f57
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1baec8e6-ab38-4b56-bb59-f6282d94f311
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 13080a43-37c3-7c66-5345-168068be2efc
---

# Windows settings backup and restore Overview | Microsoft Learn

Windows settings backup and restore is an enterprise-grade feature that streamlines device transitions by securely preserving user settings and Microsoft Store app configurations. Whether you're upgrading from Windows 10 or refreshing PCs, it delivers a consistent user experience and enhances business continuity through robust backup and rapid recovery capabilities.

Note

Windows Backup for Organizations is now **Windows settings backup and restore**. You'll start seeing the new name, Windows settings backup and restore, as we update documentation and policy surfaces. During this transition, some references might still use **Windows Backup for Organizations**.

Note

Starting with Windows 11, version 26H2, Windows settings backup is **enabled by default** for eligible devices. Any existing administrator-configured policy (enabled or disabled) continues to be honored. This change establishes backup as a baseline capability, helping user environments stay protected without requiring setup. The feature preserves the settings and Microsoft Store app list, so users can move to a new device and resume work quickly. This change applies only to backup policies; admins must still configure restore policies. For more details, see [Windows settings backup becoming a new resilience baseline](https://aka.ms/NewResilienceBaseline).

Note

Starting July 2026, **Enterprise State Roaming** (ESR) management is part of Windows settings backup and restore. For more information, see [Enterprise State Roaming](catalog-esr).

Objectives of Windows settings backup and restore:

- Help organizations accelerate PC refresh cycle, transition to Windows 11, or deployment of AI-powered PCs.
- Help organizations transition to a cloud-first approach for managing devices and user settings.

## System requirements

The following sections list the requirements to use Windows settings backup and restore.

### Backup requirements

The backup feature is available to users signed in with Microsoft Entra ID on devices that meet the following requirements:

- Windows 10, version 22H2 build [19045.6216](https://support.microsoft.com/topic/19045-6216-96d99cf6-f8b5-4798-9892-4e3eb8f11548) or later
- Windows 11, version 22H2 build [22621.5768](https://support.microsoft.com/topic/22621-5768-c67aac47-127c-4bd1-b92d-ebd9093f031d) or later
- Windows 11, version 23H2 build [22631.5768](https://support.microsoft.com/topic/22631-5768-c67aac47-127c-4bd1-b92d-ebd9093f031d) or later
- Windows 11, version 24H2 build [26100.4946](https://support.microsoft.com/topic/26100-4946-e4b87262-75c8-4fef-9df7-4a18099ee294) or later
- Must be [Microsoft Entra joined](/en-us/entra/identity/devices/concept-directory-join) or [Microsoft Entra hybrid joined](/en-us/entra/identity/devices/concept-hybrid-join)

The default-on behavior applies to devices that meet all these conditions:

- Running Windows 11, version 26H2 or later. *Note*: Devices originally running Windows 11, version 26H1 will receive the same default-on treatment starting with the following feature update.
- Not in privacy sensitive countries or regions.
- Not in sovereign or restricted cloud environments.
- With the backup policy in a **Not Configured** state under Windows settings backup and restore. *Note*: Devices with the backup policy explicitly enabled or disabled continue to honor that explicit setting.

### Restore requirements during device setup (OOBE)

The restore feature is available during OOBE on devices that meet the following requirements:

- Windows 11, version 22H2 build [22621.3958](https://support.microsoft.com/topic/de3e1e24-0c07-4210-9777-8e03a1446bae) or later
- Windows 11, version 23H2 build [22631.3958](https://support.microsoft.com/topic/de3e1e24-0c07-4210-9777-8e03a1446bae) or later
- Windows 11, version 24H2 build [26100.4770](https://support.microsoft.com/topic/9c5bc200-52b6-4c1a-be70-80df6bbfe9c3) or later
- The user has at least one backup profile
- If Autopilot is used, the profile must be configured to use [user-driven mode](/en-us/autopilot/user-driven), not self-deploying mode
- Must be [Microsoft Entra joined](/en-us/entra/identity/devices/concept-directory-join)

Tip

If devices are running a build older than July 2025, ensure that you enable the [**Install Windows quality updates** policy](https://aka.ms/W11QualityUpdates/OOBE). This setting allows devices to receive the latest quality updates and use the restore feature.

### Restore requirements during first sign-in

- Windows 11, version 24H2 build [26100.7922](https://support.microsoft.com/en-us/topic/february-24-2026-kb5077241-os-builds-26200-7922-and-26100-7922-preview-b8cc7bc8-d640-4f18-9437-3ee59298b970) or later
- Windows 11, version 25H2 build [26200.7922](https://support.microsoft.com/en-us/topic/february-24-2026-kb5077241-os-builds-26200-7922-and-26100-7922-preview-b8cc7bc8-d640-4f18-9437-3ee59298b970) or later
- The device already completed enrollment.
- The user signs in for the first time after enrollment.
- The user has at least one backup profile.
- The device is **Microsoft Entra joined or Microsoft Entra Hybrid joined**.

Tip

If devices are running a build older than March 2026, ensure that you enable the **[Install Windows quality updates policy](https://aka.ms/W11QualityUpdates/OOBE)**. This setting allows devices to receive the latest quality updates during the out-of-box experience (OOBE) and use the restore feature.

### Cloud and regional availability

This feature is currently unavailable for GCCH and Sovereign clouds or China.

## How it works

Windows settings backup and restore is an opt-in feature and is disabled by default. To use this feature, an IT administrator must first configure backup and restore policies.

### Backup process

The backup and restore process is designed to be seamless and user-friendly. The following steps outline the backup process:

1. An administrator configures the policy settings for backup.
2. The backup scheduled task runs every eight days automatically. It backs up the user settings, preferences, and the list of installed Microsoft Store apps.
3. Alternatively, users can initiate a backup manually by searching for the Windows Backup app in the Windows search box and selecting **Back up**.

[![Screenshot of the Windows backup app showing a backup of user settings in progress.](images/windows-backup.png)](images/windows-backup.png#lightbox)

### Restore process

You can initiate the restore process for a device in two ways. One way is at the time of device enrollment during the out-of-box experience (OOBE). The other way is during first sign-in after the device completes enrollment and when a user signs in with their Microsoft Entra ID account. The following steps outline the restore process:

1. An administrator enables the restore policy setting. This policy is disabled by default via Group Policy or mobile device management (MDM).
2. The user signs in during OOBE or first sign-in with the same work or school account (Entra ID) that they used during the backup flow.

1. After the sign-in screen, the restore page appears. The user can choose to restore a backup profile from a previous device or to configure the device as new.

[![Screenshot of the Windows 11 OOBE showing the option to pick a PC to restore user settings from.](images/oobe-restore-select.png)](images/oobe-restore-select.png#lightbox)

1. To restore settings and Microsoft Store apps (if any) from a previous device, the user selects the device and then selects **Continue**.

[![Screenshot of the Windows 11 OOBE showing the restore spinning wheel.](images/oobe-restore.png)](images/oobe-restore.png#lightbox)

1. The device completes the setup process. This process automatically restores any previously backed-up user settings and Microsoft Store apps.

## Configure Windows settings backup and restore

Configure Windows settings backup and restore before using it. The configuration process involves setting up backup and restore policies for devices to enable the feature.

### Backup configuration

The following instructions provide details about how to configure your devices. Select the option that best suits your needs.

# [Intune](#tab/intune)
To configure devices with Microsoft Intune, [create a Settings catalog policy](/en-us/mem/intune/configuration/settings-catalog) and use the following settings:

| Category | Setting name | Value |
| --- | --- | --- |
| **Administrative Templates\Windows Components\Sync your settings** | **Enable Windows Backup** | Enabled |

Assign the policy to a group that contains as members the devices or users that you want to configure.

# [CSP](#tab/csp)
You can configure devices with the [Policy CSP](/en-us/windows/client-management/mdm/policy-csp-settingssync).

| Setting |
| --- |
| - **OMA-URI:**`./Device/Vendor/MSFT/Policy/Config/SettingsSync/`[EnableWindowsbackup](/en-us/windows/client-management/mdm/policy-csp-settingssync#enablewindowsbackup)- **Data type:** string- **Value:**`<enabled/>` |

# [GPO](#tab/gpo)
To configure a device with group policy, use the [Local Group Policy Editor](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc731745%28v=ws.10%29). To configure multiple devices joined to Active Directory, [create or edit](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc754740%28v=ws.11%29) a group policy object (GPO) and use the following settings:

| Group policy path | Group policy setting | Value |
| --- | --- | --- |
| **Computer Configuration\Administrative Templates\Windows Components\Sync your settings** | **Enable Windows Backup** | Enabled |

Group policies can be [linked](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc732979%28v=ws.10%29) to domains or organizational units, [filtered using security groups](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc752992%28v=ws.10%29), or [filtered using WMI filters](/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/jj717288%28v=ws.11%29).

---

After you apply the backup policy to the device, the backup runs automatically every eight days.

Note

You can control which settings to back up by configuring the backup policy settings. For more information, see [Windows Backup for Organizations policy settings](policy-settings).

**Additional configuration checks**

To ensure that Windows settings backup works as expected, don't set the following policies to **Disabled**.

You can configure these policies through Group Policy (GP) or MDM (such as Microsoft Intune), depending on how you manage devices for your organization.

**1. Policy names:**

i) EnableActivityFeed

ii) PublishUserActivities

iii) UploadUserActivities

**Location:** Computer Configuration &gt; Administrative Templates &gt; System &gt; OS Policies

**2. Policy name:** EnableCDP

**Location:**[ADMX_GroupPolicy Policy CSP](/en-us/windows/client-management/mdm/policy-csp-admx-grouppolicy)

**3. Policy name:** AllowConnectedDevices

**Location:**[Connectivity Policy CSP](/en-us/windows/client-management/mdm/policy-csp-connectivity)

Don't set these policies to **Disabled**. If you disable any of these policies, Windows Backup doesn't apply.

### Restore configuration

By default, the restore option is disabled. For Microsoft Entra joined devices and Microsoft Entra Hybrid joined devices enrolled in Intune, use Intune policies to manage Windows Backup for Organizations.

There are *two* different ways to enable and configure the restore policy in Intune:

##### Option 1: Enrollment policy

- It's a **tenant-wide policy, *only* applied at device enrollment**. It helps ensure that the policy is available on the machine in time for the **OOBE restore experience**. Any changes to the enrollment policy configuration don't apply to devices already enrolled in Intune. This tenant-wide policy takes effect before standard MDM policy configurations.
- It applies to *all* devices that you enroll in Intune.

The following instructions provide details about how to configure your devices. Select the option that best suits your needs.

# [Intune](#tab/intune)
To configure the Intune tenant-level policy:

1. Sign in to the [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431).
2. Select **Devices** &gt; **Enrollment** &gt; **Windows Backup and Restore**.
3. Under **Show restore page**, select **On** to enable the restore option during OOBE.
4. Select **Save** to apply the changes.

Note

Restore setting configuration in enrollment requires Intune Service administrator or Global administrator roles.

# [CSP](#tab/csp)
You can configure devices with the [WindowsBackupAndRestore CSP](/en-us/windows/client-management/mdm/windowsbackupandrestore-csp). To enable the restore option during OOBE device enrollment, use the following OMA-URI:

| Setting |
| --- |
| - **OMA-URI:**`./Device/Vendor/MSFT/WindowsBackupAndRestore/EnableWindowsRestore`- **Data type:** boolean- **Value:**`True` |

Note

If your organization uses an MDM provider other than Microsoft Intune, configure this CSP as part of your standard Windows MDM onboarding XML. To learn more, see [XML Provisioning Schema](/en-us/openspecs/windows_protocols/ms-mde2/35e1aca6-1b8a-48ba-bbc0-23af5d46907a).

# [GPO](#tab/gpo)
This policy isn't available in GPO.

---

##### Option 2: Policy applied after device enrollment

- This device configuration policy is applied *after* device enrollment. Any changes to the policy are applied to the devices during regular policy refresh intervals.

The following instructions provide details about how to configure your devices. Select the option that best suits your needs.

# [Intune](#tab/intune)
To configure devices with Microsoft Intune, [create a Settings catalog policy](/en-us/mem/intune/configuration/settings-catalog) and use the following settings:

| Category | Setting name | Value |
| --- | --- | --- |
| **Windows Backup And Restore** | **Enable Windows Restore** | Enabled |

Assign the policy to a group that contains as members the devices or users that you want to configure.

# [CSP](#tab/csp)
You can configure devices with the [WindowsBackupAndRestore CSP](/en-us/windows/client-management/mdm/windowsbackupandrestore-csp). To enable the restore option during regular policy refresh intervals, use the following OMA-URI:

| Setting |
| --- |
| - **OMA-URI:**`./Device/Vendor/MSFT/WindowsBackupAndRestore/EnableWindowsRestore`- **Data type:** boolean- **Value:**`True` |

# [GPO](#tab/gpo)
To configure a device with group policy, use the [Local Group Policy Editor](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc731745%28v=ws.10%29). To configure multiple devices joined to Active Directory, [create or edit](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc754740%28v=ws.11%29) a group policy object (GPO) and use the following settings:

| Group policy path | Group policy setting | Value |
| --- | --- | --- |
| **Computer Configuration\Administrative Templates\Windows Components\Sync your settings** | **Enable Windows Restore** | Enabled |

Group policies can be [linked](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc732979%28v=ws.10%29) to domains or organizational units, [filtered using security groups](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc752992%28v=ws.10%29), or [filtered using WMI filters](/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/jj717288%28v=ws.11%29).

---

## Policy conflicts from multiple policy sources

Configure Windows settings backup and restore by using either GPO or CSP, but not a combination of both. Avoid mixing GPO and CSP policy settings for Windows settings backup and restore, as it can lead to unexpected results.

## Conditional Access policy interference

If you enable [conditional access](/en-us/entra/identity/conditional-access/) for cloud applications, it might prevent the Microsoft Entra user from obtaining an access token. This condition results in the following error.

| Error title | Error description |
| --- | --- |
| You don't have access to this. | Your sign-in was successful but you don't have the permissions to access this resource. |
| You can't get there from here. | This application contains sensitive information and can only be accessed from: Devices or client applications that meet Contoso engagement compliance policy. If this is a personal device, you can choose to let Contoso manage your device by going to **Settings** &gt; **Accounts** &gt; **Access work or school** and selecting **Connect**. When you're done come back and try again. |

To fix this error, create a custom policy that allows the Microsoft service (app ID: `d32c68ad-72d2-4acb-a0c7-46bb2cf93873`) to enable the restore flow to proceed. Verify that the app ID is listed in the custom policy before you proceed further.

## PRMFA/Hyper-V virtual machine authentication

A user might encounter a Phishing-Resistant Multifactor Authentication (PRMFA) prompt during OOBE for the restore experience app (`74d197dc-b84d-4d43-a1b2-b5bf3bb91c11`) under the following circumstances:

- Your organization enforces PRMFA through a Microsoft Entra ID [authentication strength](/en-us/entra/identity/authentication/concept-authentication-strengths) policy.
- You exclude the Microsoft Intune apps (`0000000a-0000-0000-c000-000000000000` and `d4ebce55-015a-49b5-a083-c84d1797ae8c`) from that policy.
- User enrolls a device during OOBE without using a strong authentication method.

Tip

In virtual machine (VM) scenarios such as Hyper-V, it's difficult to perform PRMFA during OOBE. Consider Temporary Access Pass (TAP) for authentication.

## User experience

After you enable the feature, users can manage their backup settings directly through **Settings** by going to **Accounts** &gt; **Windows backup**.

- To stop backing up preferences, users can turn off the **Remember my preferences** toggle.
- To stop backing up the list of installed Microsoft Store apps, users can turn off the **Remember my apps** toggle.

Note

These toggles control both Windows settings backup and restore and Enterprise State Roaming. They're only actionable if IT admins enabled either backup or roaming. If IT admins doesn't enable any of these controls, the toggles are grayed out and not actionable.

Use the settings category toggles under **Remember my preferences** to control which settings to include in backups.

Prevent users from modifying the Windows backup options by using [policy settings](policy-settings).

## Introducing restore summary in Windows settings backup and restore

Starting with Windows 11, version 24H2, users can view a restore summary after completing the restore process through Windows settings backup and restore. The restore summary provides an on-device view of the content restored from the selected backup profile. It helps users understand what was recovered and quickly resume work on their new device. This experience is available after completing the restore process during device setup (OOBE) or first sign-in.

The restore summary includes:

- Personalization settings that were restored from the user's backup profile.
- The Microsoft Store app list associated with the backup profile and restored to the device.

Note

> 
> Restore summary is designed to provide visibility into the restore experience. The summary primarily lists restored user-customized personalization settings and Microsoft Store app list. In some cases, the summary also displays settings that retain their default values (not customized by the user). This behavior is by design.

By making restore outcomes visible, restore summary helps users confirm that their settings and Microsoft Store app list are restored successfully. By reducing post-setup verification, users can get back to work faster, bringing greater clarity to the recovery experience, and accelerating time to productivity.

## View restore summary

After a restore process ends on a new device, users can review a summary of the content restored from their selected backup profile.

To view restore summary:

1. During device setup (OOBE) or first sign-in, select a backup profile.
2. Allow restore and any remaining setup steps to complete so you reach the Windows desktop.
3. When restore is complete, the restore summary notification appears on the device.

    [![Screenshot of a popup notification message inviting users to review the restore summary.](media/index/restore-notification.png)](media/index/restore-notification.png#lightbox)

    Alternatively, users can directly view restore summary by visiting **Settings** &gt; **Accounts** &gt; **Windows backup**.

    [![Screenshot of a new restore summary option available from Windows backup settings.](media/index/windows-backup-settings.png)](media/index/windows-backup-settings.png#lightbox)
4. From the notification, select **View** or from Settings, select the link icon next to **Restore summary** to open the restore summary and review the restored content.

    [![Screenshot of the restore summary report appearing in the web browser.](media/index/restore-summary.png)](media/index/restore-summary.png#lightbox)

## Restore summary availability

Restore summary becomes available approximately one hour after a successful restore process. You can access it from the Windows notification or directly from the Settings page for a limited period of seven days following device setup.

Once the visibility period expires, you can no longer view the restore summary.

## Turn off Windows settings backup and delete user data

The following instructions provide details about how to configure your devices. Select the option that best suits your needs.

# [Intune](#tab/intune)
To configure devices with Microsoft Intune, [create a Settings catalog policy](/en-us/mem/intune/configuration/settings-catalog) and use the following settings:

| Category | Setting name | Value |
| --- | --- | --- |
| **Administrative Templates\Windows Components\Sync your settings** | **Enable Windows Backup** | Disabled |

Assign the policy to a group that contains as members the devices or users that you want to configure.

# [CSP](#tab/csp)
You can configure devices with the [CSP](/en-us/windows/client-management/mdm/policy-csp-settingssync).

| Setting |
| --- |
| - **OMA-URI:**`./Device/Vendor/MSFT/Policy/Config/SettingsSync/`[EnableWindowsbackup](/en-us/windows/client-management/mdm/policy-csp-settingssync#enablewindowsbackup)- **Data type:** string- **Value:**`<disabled/>` |

# [GPO](#tab/gpo)
To configure a device with group policy, use the [Local Group Policy Editor](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc731745%28v=ws.10%29). To configure multiple devices joined to Active Directory, [create or edit](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc754740%28v=ws.11%29) a group policy object (GPO) and use the following settings:

| Group policy path | Group policy setting | Value |
| --- | --- | --- |
| **Computer Configuration\Administrative Templates\Windows Components\Sync your settings** | **Enable Windows Backup** | Disabled |

Group policies can be [linked](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc732979%28v=ws.10%29) to domains or organizational units, [filtered using security groups](/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc752992%28v=ws.10%29), or [filtered using WMI filters](/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/jj717288%28v=ws.11%29).

---

When you disable the backup policy, the scheduled backup stops running.

You can view, export, or delete the backed up data from the organization tenant's data store. Use the Microsoft Graph beta APIs directly or the PowerShell scripts that wrap them.

**Option 1: Microsoft Graph APIs**

- Prerequisites: For request authorization, follow [Get access on behalf of a user](/en-us/graph/auth-v2-user?tabs=http#prerequisites) to consent to the relevant permissions and acquire an access token for the requests.
- To read and export data, see [Get windowsSetting](/en-us/graph/api/windowssetting-get?view=graph-rest-beta&amp;preserve-view=true&amp;tabs=http). The permission `UserWindowsSettings.Read.All` is required.
- To delete a user's backup data, see [Delete windowsSetting](/en-us/graph/api/windowssetting-delete?view=graph-rest-beta&amp;preserve-view=true&amp;tabs=http). The permission `UserWindowsSettings.ReadWrite.All` is required.

**Option 2: PowerShell scripts (simpler alternative)**

For an easier experience, use the PowerShell scripts that wrap the same APIs. They let you view, export, and delete a user's Windows settings backup data without calling Graph directly. Available on [GitHub](https://github.com/microsoft/windows-backup-admin-scripts) and the [PowerShell Gallery](https://www.powershellgallery.com/packages/WindowsBackupAdmin/1.0.0).

- Install the module (one time): Install-Module WindowsBackupAdmin -Scope CurrentUser
- View and export a user's backup data: Get-WindowsBackup -UserId user@contoso.com
- Delete a user's backup data: Remove-WindowsBackup -UserId user@contoso.com

### ![](../images/icons/feedback.svg) Provide feedback

To report a bug or share suggestions, submit this [form](https://forms.office.com/pages/responsepage.aspx?id=v4j5cvGGr0GRqy180BHbR5hPS1INazpFmbOc5GnaZbRUNEY5TTIyU0VQSFNIWk1FMEtLT1ZMQjRYRy4u&amp;route=shorturl). Our team reviews submissions weekly, and the more details you provide, the faster we can act. If we need more information, we follow up via email.