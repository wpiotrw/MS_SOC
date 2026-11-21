---
layout: Conceptual
title: Update Policy CSP | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-update
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
description: Learn more about the Update Area in Policy CSP.
ms.date: 2026-11-20T00:00:00.0000000Z
locale: en-us
document_id: 91ca58bd-f279-7739-0140-c4bd56784768
document_version_independent_id: 1d2ecc90-58a3-6bcd-84ae-ef04d7a3b7b4
original_content_git_url: https://github.com/MicrosoftDocs/windows-docs-pr/blob/live/windows/client-management/mdm/policy-csp-update.md
site_name: Docs
depot_name: TechNet.win-client-management
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/TechNet.win-client-management/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: mdm/policy-csp-update
moniker_range_name: 
monikers: []
item_type: Content
source_path: windows/client-management/mdm/policy-csp-update.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/e0ffb20c-01c6-407b-a9bd-29111652a1dc
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/3904bce4-d817-48cf-85fd-b6146fca83b7
platformId: edaf0986-f34e-b1fd-8897-c3c2053d78e8
---

# Update Policy CSP | Microsoft Learn

![Logo of Windows Insider.](images/insider.png)

Important

This CSP contains some settings that are under development and only applicable for [Windows Insider Preview builds](/en-us/windows-insider/). These settings are subject to change and may have dependencies on other features or services in preview.

Update CSP policies are listed below based on the group policy area:

- Windows Insider Preview
    - SetMaxPauseDays
- Other policies
    - IgnoreWindowsUpdateGroupPolicies
- Manage updates offered from Windows Update
    - AllowNonMicrosoftSignedUpdate
    - AllowOptionalContent
    - AutomaticMaintenanceWakeUp
    - BranchReadinessLevel
    - DeferFeatureUpdatesPeriodInDays
    - DeferQualityUpdatesPeriodInDays
    - DisableWUfBSafeguards
    - ExcludeWUDriversInQualityUpdate
    - ManagePreviewBuilds
    - PauseFeatureUpdates
    - PauseFeatureUpdatesStartTime
    - PauseQualityUpdates
    - PauseQualityUpdatesStartTime
    - ProductVersion
    - TargetReleaseVersion
- Manage updates offered from Windows Server Update Service
    - AllowUpdateService
    - DetectionFrequency
    - DoNotEnforceEnterpriseTLSCertPinningForUpdateDetection
    - FillEmptyContentUrls
    - SetPolicyDrivenUpdateSourceForDriverUpdates
    - SetPolicyDrivenUpdateSourceForFeatureUpdates
    - SetPolicyDrivenUpdateSourceForOtherUpdates
    - SetPolicyDrivenUpdateSourceForQualityUpdates
    - SetProxyBehaviorForUpdateDetection
    - UpdateServiceUrl
    - UpdateServiceUrlAlternate
- Manage end user experience
    - ActiveHoursEnd
    - ActiveHoursMaxRange
    - ActiveHoursStart
    - AllowAutoUpdate
    - AllowAutoWindowsUpdateDownloadOverMeteredNetwork
    - AllowMUUpdateService
    - AllowTemporaryEnterpriseFeatureControl
    - ConfigureDeadlineForFeatureUpdates
    - ConfigureDeadlineForQualityUpdates
    - ConfigureDeadlineGracePeriod
    - ConfigureDeadlineGracePeriodForFeatureUpdates
    - ConfigureDeadlineNoAutoRebootForFeatureUpdates
    - ConfigureDeadlineNoAutoRebootForQualityUpdates
    - ConfigureFeatureUpdateUninstallPeriod
    - NoUpdateNotificationsDuringActiveHours
    - ScheduledInstallDay
    - ScheduledInstallEveryWeek
    - ScheduledInstallFirstWeek
    - ScheduledInstallFourthWeek
    - ScheduledInstallSecondWeek
    - ScheduledInstallThirdWeek
    - ScheduledInstallTime
    - SetDisablePauseUXAccess
    - SetDisableUXWUAccess
    - SetEDURestart
    - UpdateNotificationLevel
- Manage updates with maintenance windows
    - MaintenanceWindowDurationHours
    - MaintenanceWindowEnabled
    - MaintenanceWindowMonthlyMonthBasedDayOfMonth
    - MaintenanceWindowMonthlySchedule
    - MaintenanceWindowMonthlyWeekBasedDayOfTheWeek
    - MaintenanceWindowMonthlyWeekBasedOccurrenceInMonth
    - MaintenanceWindowRepeatScheduleOption
    - MaintenanceWindowStartDate
    - MaintenanceWindowStartTime
    - MaintenanceWindowUpdateActions
    - MaintenanceWindowWeeklyFriday
    - MaintenanceWindowWeeklyMonday
    - MaintenanceWindowWeeklySaturday
    - MaintenanceWindowWeeklySunday
    - MaintenanceWindowWeeklyThursday
    - MaintenanceWindowWeeklyTuesday
    - MaintenanceWindowWeeklyWednesday
    - MaintenanceWindowDailyInterval
    - MaintenanceWindowMonthlyInterval
    - MaintenanceWindowWeeklyInterval
- Legacy Policies
    - AlwaysAutoRebootAtScheduledTimeMinutes
    - AutoRestartDeadlinePeriodInDays
    - AutoRestartDeadlinePeriodInDaysForFeatureUpdates
    - AutoRestartNotificationSchedule
    - AutoRestartRequiredNotificationDismissal
    - DeferUpdatePeriod
    - DeferUpgradePeriod
    - DisableDualScan
    - EngagedRestartDeadline
    - EngagedRestartDeadlineForFeatureUpdates
    - EngagedRestartSnoozeSchedule
    - EngagedRestartSnoozeScheduleForFeatureUpdates
    - EngagedRestartTransitionSchedule
    - EngagedRestartTransitionScheduleForFeatureUpdates
    - IgnoreMOAppDownloadLimit
    - IgnoreMOUpdateDownloadLimit
    - PauseDeferrals
    - PhoneUpdateRestrictions
    - RequireDeferUpgrade
    - RequireUpdateApproval
    - ScheduleImminentRestartWarning
    - ScheduleRestartWarning
    - SetAutoRestartNotificationDisable

## Windows Insider Preview

### SetMaxPauseDays

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows Insider Preview |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/SetMaxPauseDays
```

Configure the maximum number of days that updates can be paused. Supported values are 1-35. The default value is 35 (days).

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[1-35]` |
| Default Value | 35 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaxPauseDays |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | SetMaxPauseDays |

## Other policies

### IgnoreWindowsUpdateGroupPolicies

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 with [KB5101684](https://support.microsoft.com/help/5101684) [10.0.26100.8973] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/IgnoreWindowsUpdateGroupPolicies
```

When enabled, Group Policy settings for Windows Update are ignored and only MDM policy values are applied. This allows MDM-managed devices to bypass conflicting Group Policy configurations.

Note

If any Windows Update policies are delivered through GP and IgnoreWindowsUpdateGroupPolicies is enabled, those policies will be ignored. Therefore, this policy is optional for dual patch scenarios. If you wish to enable this policy, equivalent MDM policies should be configured.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Disabled. Group Policy settings are applied normally. |
| 1 | Enabled. Group Policy settings for Windows Update are ignored. |

## Manage updates offered from Windows Update

### AllowNonMicrosoftSignedUpdate

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/AllowNonMicrosoftSignedUpdate
```

Allows the IT admin to manage whether Automatic Updates accepts updates signed by entities other than Microsoft when the update is found at the UpdateServiceUrl location. This policy supports using WSUS for 3rd party software and patch distribution. This policy is specific to desktop and local publishing via WSUS for 3rd party updates (binaries and updates not hosted on Microsoft Update) and allows IT to manage whether Automatic Updates accepts updates signed by entities other than Microsoft when the update is found on an intranet Microsoft update service location.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Not allowed or not configured. Updates from an intranet Microsoft update service location must be signed by Microsoft. |
| 1 (Default) | Allowed. Accepts updates received through an intranet Microsoft update service location, if they're signed by a certificate found in the 'Trusted Publishers' certificate store of the local computer. |

### AllowOptionalContent

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 21H2 [10.0.19044.3757] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/AllowOptionalContent
```

This policy enables devices to get optional updates (including gradual feature rollouts (CFRs) - learn more by visiting aka.ms/AllowOptionalContent)

When the policy is configured.

- If "Automatically receive optional updates (including CFRs)" is selected, the device will get the latest optional updates automatically in line with the configured quality update deferrals. This includes optional cumulative updates and gradual feature rollouts (CFRs).
- If "Automatically receive optional updates" is selected, the device will only get optional cumulative updates automatically, in line with the quality update deferrals.
- If "Users can select which optional updates to receive" is selected, users can select which optional updates to get by visiting Settings &gt; Windows Update &gt; Advanced options &gt; Optional updates. Users can also enable the toggle "Get the latest updates as soon as they're available" to automatically receive optional updates and gradual feature rollouts.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Don't receive optional updates. |
| 1 | Automatically receive optional updates (including CFRs). |
| 2 | Automatically receive optional updates. |
| 3 | Users can select which optional updates to receive. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AllowOptionalContent |
| Friendly Name | Enable optional updates |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Update |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| Registry Value Name | SetAllowOptionalContent |
| ADMX File Name | WindowsUpdate.admx |

### AutomaticMaintenanceWakeUp

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1903 [10.0.18362] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/AutomaticMaintenanceWakeUp
```

This policy setting allows you to configure Automatic Maintenance wake up policy.

The maintenance wakeup policy specifies if Automatic Maintenance should make a wake request to the OS for the daily scheduled maintenance. Note, that if the OS power wake policy is explicitly disabled, then this setting has no effect.

- If you enable this policy setting, Automatic Maintenance will attempt to set OS wake policy and make a wake request for the daily scheduled time, if required.
- If you disable or don't configure this policy setting, the wake setting as specified in Security and Maintenance/Automatic Maintenance Control Panel will apply.

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
| Name | WakeUpPolicy |
| Friendly Name | Automatic Maintenance WakeUp Policy |
| Location | Computer Configuration |
| Path | Windows Components &gt; Maintenance Scheduler |
| Registry Key Name | Software\Policies\Microsoft\Windows\Task Scheduler\Maintenance |
| Registry Value Name | WakeUp |
| ADMX File Name | msched.admx |

### BranchReadinessLevel

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/BranchReadinessLevel
```

Enable this policy to specify when to receive Feature Updates.

Defer Updates | This enables devices to defer taking the next Feature Update available for their current product (or a new product if specified in the Select the target Feature Update version policy). You can defer a Feature Update for up to 14 days for all prerelease channels and up to 365 days for the General Availability Channel. To learn more about the current releases, please see aka.ms/WindowsTargetVersioninfo.

Pause Updates | To prevent Feature Updates from being offered to the device, you can temporarily pause Feature Updates. This pause will remain in effect for 35 days from the specified start date or until the field is cleared. Note, Quality Updates will still be offered even if Feature Updates are paused.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 16 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 2 | {0x2} - Windows Insider build - Fast (added in Windows 10, version 1709). |
| 4 | {0x4} - Windows Insider build - Slow (added in Windows 10, version 1709). |
| 8 | {0x8} - Release Windows Insider build (added in Windows 10, version 1709). |
| 16 (Default) | {0x10} - Semi-Annual Enterprise Channel (Preview). Device gets all applicable feature updates from Semi-Annual Enterprise Channel (Preview). |
| 32 | 2 {0x20} - Semi-Annual Enterprise Channel. Device gets feature updates from Semi-Annual Enterprise Channel. (\*Only applicable to releases prior to 1903, for all releases 1903 and after the Semi-Annual Enterprise Channel and Semi-Annual Enterprise Channel (Preview) into a single Semi-Annual Enterprise Channel with a value of 16). |
| 64 | {0x40} - Release Preview of Quality Updates Only. |
| 128 | {0x80} - Canary Channel. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DeferFeatureUpdates |
| Friendly Name | Select when Preview Builds and Feature Updates are received |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Update |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### DeferFeatureUpdatesPeriodInDays

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/DeferFeatureUpdatesPeriodInDays
```

Enable this policy to specify when to receive Feature Updates.

Defer Updates | This enables devices to defer taking the next Feature Update available for their current product (or a new product if specified in the Select the target Feature Update version policy). You can defer a Feature Update for up to 14 days for all prerelease channels and up to 365 days for the General Availability Channel. To learn more about the current releases, please see aka.ms/WindowsTargetVersioninfo.

Pause Updates | To prevent Feature Updates from being offered to the device, you can temporarily pause Feature Updates. This pause will remain in effect for 35 days from the specified start date or until the field is cleared. Note, Quality Updates will still be offered even if Feature Updates are paused.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[0-365]` |
| Default Value | 0 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DeferFeatureUpdates |
| Friendly Name | Select when Preview Builds and Feature Updates are received |
| Element Name | How many days after a Feature Update is released would you like to defer the update before it's offered to the device? |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Update |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### DeferQualityUpdatesPeriodInDays

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/DeferQualityUpdatesPeriodInDays
```

Enable this policy to specify when to receive quality updates.

You can defer receiving quality updates for up to 30 days.

To prevent quality updates from being received on their scheduled time, you can temporarily pause quality updates. The pause will remain in effect for 35 days or until you clear the start date field.

To resume receiving Quality Updates which are paused, clear the start date field.

If you disable or don't configure this policy, Windows Update won't alter its behavior.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[0-30]` |
| Default Value | 0 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DeferQualityUpdates |
| Friendly Name | Select when Quality Updates are received |
| Element Name | After a quality update is released, defer receiving it for this many days. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Update |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### DisableWUfBSafeguards

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1809 with [KB4577069](https://support.microsoft.com/help/4577069) [10.0.17763.1490] and later  ✅ Windows 10, version 1903 with [KB4577062](https://support.microsoft.com/help/4577062) [10.0.18362.1110] and later  ✅ Windows 10, version 1909 with [KB4577062](https://support.microsoft.com/help/4577062) [10.0.18363.1110] and later  ✅ Windows 10, version 2004 with [KB4577063](https://support.microsoft.com/help/4577063) [10.0.19041.546] and later  ✅ Windows 11, version 21H2 [10.0.22000] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/DisableWUfBSafeguards
```

This policy setting specifies that a Windows Update for Business device should skip safeguards.

Safeguard holds prevent a device with a known compatibility issue from being offered a new OS version. The offering will proceed once a fix is issued and is verified on a held device. The aim of safeguards is to protect the device and user from a failed or poor upgrade experience. The safeguard holds protection is provided by default to all the devices trying to update to a new Windows 10 Feature Update version via Windows Update.

IT admins can, if necessary, opt devices out of safeguard protections using this policy setting or via the **Disable safeguards for Feature Updates** Group Policy.

Note

Opting out of the safeguards can put devices at risk from known performance issues. We recommend opting out only in an IT environment for validation purposes. Further, you can leverage the Windows Insider Program for Business Release Preview Channel in order to validate the upcoming Windows 10 Feature Update version without the safeguards being applied.

The disable safeguards policy will revert to "Not Configured" on a device after moving to a new Windows 10 version, even if previously enabled. This ensures the admin is consciously disabling Microsoft's default protection from known issues for each new feature update.

Disabling safeguards doesn't guarantee your device will be able to successfully update. The update may still fail on the device and will likely result in a bad experience post upgrade, as you're bypassing the protection given by Microsoft pertaining to known issues.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Safeguards are enabled and devices may be blocked for upgrades until the safeguard is cleared. |
| 1 | Safeguards aren't enabled and upgrades will be deployed without blocking on safeguards. |

### ExcludeWUDriversInQualityUpdate

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ExcludeWUDriversInQualityUpdate
```

Enable this policy to not include drivers with Windows quality updates.

If you disable or don't configure this policy, Windows Update will include updates that have a Driver classification.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Allow Windows Update drivers. |
| 1 | Exclude Windows Update drivers. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | ExcludeWUDriversInQualityUpdate |
| Friendly Name | Do not include drivers with Windows Updates |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Update |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| Registry Value Name | ExcludeWUDriversInQualityUpdate |
| ADMX File Name | WindowsUpdate.admx |

### ManagePreviewBuilds

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1709 [10.0.16299] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ManagePreviewBuilds
```

Used to manage Windows 10 Insider Preview builds. Value type is integer.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 3 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Disable Preview builds. |
| 1 | Disable Preview builds once the next release is public. |
| 2 | Enable Preview builds. |
| 3 (Default) | Preview builds is left to user selection. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | ManagePreviewBuilds |
| Friendly Name | Manage preview builds |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Update |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### PauseFeatureUpdates

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/PauseFeatureUpdates
```

Enable this policy to specify when to receive Feature Updates.

Defer Updates | This enables devices to defer taking the next Feature Update available for their current product (or a new product if specified in the Select the target Feature Update version policy). You can defer a Feature Update for up to 14 days for all prerelease channels and up to 365 days for the General Availability Channel. To learn more about the current releases, please see aka.ms/WindowsTargetVersioninfo.

Pause Updates | To prevent Feature Updates from being offered to the device, you can temporarily pause Feature Updates. This pause will remain in effect for 35 days from the specified start date or until the field is cleared. Note, Quality Updates will still be offered even if Feature Updates are paused.

Note

We recommend that you use the Update/PauseFeatureUpdatesStartTime policy, if you're running Windows 10, version 1703 or later.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Feature Updates aren't paused. |
| 1 | Feature Updates are paused for 60 days or until value set to back to 0, whichever is sooner. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DeferFeatureUpdates |
| Friendly Name | Select when Preview Builds and Feature Updates are received |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Update |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### PauseFeatureUpdatesStartTime

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/PauseFeatureUpdatesStartTime
```

Specifies the date and time when the IT admin wants to start pausing the Feature Updates. Value type is string (yyyy-mm-dd, ex. 2018-10-28).

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `chr` (string) |
| Access Type | Add, Delete, Get, Replace |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DeferFeatureUpdates |
| Friendly Name | Select when Preview Builds and Feature Updates are received |
| Element Name | Pause Preview Builds or Feature Updates starting. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Update |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### PauseQualityUpdates

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/PauseQualityUpdates
```

Enable this policy to specify when to receive quality updates.

You can defer receiving quality updates for up to 30 days.

To prevent quality updates from being received on their scheduled time, you can temporarily pause quality updates. The pause will remain in effect for 35 days or until you clear the start date field.

To resume receiving Quality Updates which are paused, clear the start date field.

If you disable or don't configure this policy, Windows Update won't alter its behavior.

Note

We recommend that you use the Update/PauseQualityUpdatesStartTime policy, if you're running Windows 10, version 1703 or later.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Quality Updates aren't paused. |
| 1 | Quality Updates are paused for 35 days or until value set back to 0, whichever is sooner. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DeferQualityUpdates |
| Friendly Name | Select when Quality Updates are received |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Update |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### PauseQualityUpdatesStartTime

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/PauseQualityUpdatesStartTime
```

Specifies the date and time when the IT admin wants to start pausing the Quality Updates. Value type is string (yyyy-mm-dd, ex. 2018-10-28).

Note

When this policy is configured, Quality Updates will be paused for 35 days from the specified start date.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `chr` (string) |
| Access Type | Add, Delete, Get, Replace |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DeferQualityUpdates |
| Friendly Name | Select when Quality Updates are received |
| Element Name | Pause Quality Updates starting. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Update |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### ProductVersion

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 2004 with [KB5005101](https://support.microsoft.com/help/5005101) [10.0.19041.1202] and later  ✅ Windows 10, version 20H2 with [KB5005101](https://support.microsoft.com/help/5005101) [10.0.19042.1202] and later  ✅ Windows 10, version 21H1 with [KB5005101](https://support.microsoft.com/help/5005101) [10.0.19043.1202] and later  ✅ Windows 11, version 21H2 [10.0.22000] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ProductVersion
```

Enables IT administrators to specify the product version associated with the target feature update they would like their device(s) to move to and/or stay on until they reach end of service or reconfigure the policy. For details about different Windows 10 versions, see [Windows release information](/en-us/windows/release-health/release-information).

Supported value type is a string containing a Windows product. For example, "Windows 11" or "11" or "Windows 10". By using this Windows Update for Business policy to upgrade devices to a new product (for example, Windows 11) you're agreeing that when applying this operating system to a device:

1. The applicable Windows license was purchased through volume licensing, or
2. You're authorized to bind your organization and are accepting on its behalf the relevant [Microsoft Software License Terms](https://www.microsoft.com/Useterms).

Note

If no product is specified, the device will continue receiving newer versions of the Windows product it's currently on.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `chr` (string) |
| Access Type | Add, Delete, Get, Replace |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | TargetReleaseVersion |
| Friendly Name | Select the target Feature Update version |
| Element Name | Which Windows product version would you like to receive feature updates for? e.g., Windows 10. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Update |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### TargetReleaseVersion

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1803 with [KB4556807](https://support.microsoft.com/help/4556807) [10.0.17134.1488] and later  ✅ Windows 10, version 1809 with [KB4551853](https://support.microsoft.com/help/4551853) [10.0.17763.1217] and later  ✅ Windows 10, version 1903 with [KB4556799](https://support.microsoft.com/help/4556799) [10.0.18362.836] and later  ✅ Windows 10, version 1909 with [KB4556799](https://support.microsoft.com/help/4556799) [10.0.18363.836] and later  ✅ Windows 10, version 2004 [10.0.19041] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/TargetReleaseVersion
```

Enables IT administrators to specify which version they would like their device(s) to move to and/or stay on until they reach end of service or reconfigure the policy. For details about different Windows 10 versions, see [Windows 10 release information](/en-us/windows/release-health/release-information).

Supported value type is a string containing Windows version number. For example, `1809`, `1903`, etc.

Note

You need to set up the ProductVersion CSP along with the TargetReleaseVersion CSP for it to work.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `chr` (string) |
| Access Type | Add, Delete, Get, Replace |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | TargetReleaseVersion |
| Friendly Name | Select the target Feature Update version |
| Element Name | Target Version for Feature Updates. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Update |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

## Manage updates offered from Windows Server Update Service

### AllowUpdateService

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/AllowUpdateService
```

Specifies whether the device could use Microsoft Update, Windows Server Update Services (WSUS), or Microsoft Store. Even when Windows Update is configured to receive updates from an intranet update service, it will periodically retrieve information from the public Windows Update service to enable future connections to Windows Update, and other services like Microsoft Update or the Microsoft Store. Enabling this policy will disable that functionality, and may cause connection to public services such as the Microsoft Store to stop working.

Note

This policy applies only when the desktop or device is configured to connect to an intranet update service using the Specify intranet Microsoft update service location policy.

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
| Name | CorpWuURL |
| Friendly Name | Specify intranet Microsoft update service location |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Server Update Service |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### DetectionFrequency

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/DetectionFrequency
```

Specifies the hours that Windows will use to determine how long to wait before checking for available updates. The exact wait time is a sum of the specific value and a random variant of 0-4 hours.

If the status is set to Enabled, Windows will check for available updates at the specified interval.

If the status is set to Disabled or Not Configured, Windows will check for available updates at the default interval of 22 hours.

Note

The "Specify intranet Microsoft update service location" setting must be enabled for this policy to have effect.

Note

If the "Configure Automatic Updates" policy is disabled, this policy has no effect.

Note

This policy isn't supported on Windows RT. Setting this policy won't have any effect on Windows RT PCs.

This policy should be enabled only when UpdateServiceUrl is configured to point the device at a WSUS server rather than Microsoft Update.

Note

There is a random variant of 0-4 hours applied to the scan frequency, which cannot be configured.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[1-22]` |
| Default Value | 22 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DetectionFrequency\_Title |
| Friendly Name | Automatic Updates detection frequency |
| Element Name | interval (hours) |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Server Update Service |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate\AU |
| ADMX File Name | WindowsUpdate.admx |

### DoNotEnforceEnterpriseTLSCertPinningForUpdateDetection

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 with [KB4598231](https://support.microsoft.com/help/4598231) [10.0.10240.18818] and later  ✅ Windows 10, version 1607 with [KB4598243](https://support.microsoft.com/help/4598243) [10.0.14393.4169] and later  ✅ Windows 10, version 1703 with [KB4520010](https://support.microsoft.com/help/4520010) [10.0.15063.2108] and later  ✅ Windows 10, version 1709 with [KB4580328](https://support.microsoft.com/help/4580328) [10.0.16299.2166] and later  ✅ Windows 10, version 1803 with [KB4598245](https://support.microsoft.com/help/4598245) [10.0.17134.1967] and later  ✅ Windows 10, version 1809 with [KB4598230](https://support.microsoft.com/help/4598230) [10.0.17763.1697] and later  ✅ Windows 10, version 1903 [10.0.18362.1316] and later  ✅ Windows 10, version 1909 with [KB4598229](https://support.microsoft.com/help/4598229) [10.0.18363.1316] and later  ✅ Windows 10, version 2004 with [KB4598242](https://support.microsoft.com/help/4598242) [10.0.19041.746] and later  ✅ Windows 10, version 20H2 with [KB4598242](https://support.microsoft.com/help/4598242) [10.0.19042.746] and later  ✅ Windows 11, version 21H2 [10.0.22000] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/DoNotEnforceEnterpriseTLSCertPinningForUpdateDetection
```

Note

By default, certificate pinning for Windows Update client isn't enforced. To ensure the highest levels of security, we recommended using WSUS TLS certificate pinning on all devices.

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
| Name | CorpWuURL |
| Friendly Name | Specify intranet Microsoft update service location |
| Element Name | Don't enforce TLS certificate pinning for Windows Update client for detecting updates. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Server Update Service |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### FillEmptyContentUrls

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/FillEmptyContentUrls
```

Allows Windows Update Agent to determine the download URL when it's missing from the metadata. This scenario will occur when intranet update service stores the metadata files but the download contents are stored in the ISV file cache (specified as the alternate download URL).

Note

This setting should only be used in combination with an alternate download URL and configured to use ISV file cache. This setting is used when the intranet update service doesn't provide download URLs in the update metadata for files which are available on the alternate download server.

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
| Name | CorpWuURL |
| Friendly Name | Specify intranet Microsoft update service location |
| Element Name | Download files with no Url in the metadata if alternate download server is set. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Server Update Service |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### SetPolicyDrivenUpdateSourceForDriverUpdates

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ [10.0.20348.371] and later  ✅ Windows 10, version 2004 with [KB5005101](https://support.microsoft.com/help/5005101) [10.0.19041.1202] and later  ✅ Windows 10, version 20H2 with [KB5005101](https://support.microsoft.com/help/5005101) [10.0.19042.1202] and later  ✅ Windows 10, version 21H1 with [KB5005101](https://support.microsoft.com/help/5005101) [10.0.19043.1202] and later  ✅ Windows 10, version 21H2 [10.0.19044.1288] and later  ✅ Windows 10, version 22H2 [10.0.19045.2130] and later  ✅ Windows 11, version 21H2 [10.0.22000] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/SetPolicyDrivenUpdateSourceForDriverUpdates
```

Configure this policy to specify whether to receive **Windows Driver Updates** from Windows Update endpoint, managed by Windows Update for Business policies, or through your configured Windows Server Update Service (WSUS) server. If you configure this policy, also configure the scan source policies for other update types:

- SetPolicyDrivenUpdateSourceForFeatureUpdates
- SetPolicyDrivenUpdateSourceForQualityUpdates
- SetPolicyDrivenUpdateSourceForOtherUpdates

Note

If you haven't properly configured Update/UpdateServiceUrl correctly to point to your WSUS server, this policy has no effect.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Detect, download and deploy Driver Updates from Windows Update. |
| 1 (Default) | Detect, download and deploy Driver Updates from Windows Server Update Services (WSUS). |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | CorpWuURL |
| Friendly Name | Specify intranet Microsoft update service location |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Server Update Service |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### SetPolicyDrivenUpdateSourceForFeatureUpdates

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ [10.0.20348.371] and later  ✅ Windows 10, version 2004 with [KB5005101](https://support.microsoft.com/help/5005101) [10.0.19041.1202] and later  ✅ Windows 10, version 20H2 with [KB5005101](https://support.microsoft.com/help/5005101) [10.0.19042.1202] and later  ✅ Windows 10, version 21H1 with [KB5005101](https://support.microsoft.com/help/5005101) [10.0.19043.1202] and later  ✅ Windows 10, version 21H2 [10.0.19044.1288] and later  ✅ Windows 10, version 22H2 [10.0.19045.2130] and later  ✅ Windows 11, version 21H2 [10.0.22000] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/SetPolicyDrivenUpdateSourceForFeatureUpdates
```

Configure this policy to specify whether to receive **Windows Feature Updates** from Windows Update endpoint, managed by Windows Update for Business policies, or through your configured Windows Server Update Service (WSUS) server. If you configure this policy, also configure the scan source policies for other update types:

- SetPolicyDrivenUpdateSourceForQualityUpdates
- SetPolicyDrivenUpdateSourceForDriverUpdates
- SetPolicyDrivenUpdateSourceForOtherUpdates

Note

- If you haven't properly configured Update/UpdateServiceUrl correctly to point to your WSUS server, this policy has no effect.
- If you're also using the **Specify settings for optional component installation and component repair** ([ADMX_Servicing](policy-csp-admx-servicing)) policy to enable content for FoDs and language packs, see [How to make Features on Demand and language packs available when you're using WSUS or Configuration Manager](/en-us/windows/deployment/update/fod-and-lang-packs) to verify your policy configuration.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Detect, download and deploy Feature Updates from Windows Update. |
| 1 (Default) | Detect, download and deploy Feature Updates from Windows Server Update Services (WSUS). |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | CorpWuURL |
| Friendly Name | Specify intranet Microsoft update service location |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Server Update Service |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### SetPolicyDrivenUpdateSourceForOtherUpdates

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ [10.0.20348.371] and later  ✅ Windows 10, version 2004 with [KB5005101](https://support.microsoft.com/help/5005101) [10.0.19041.1202] and later  ✅ Windows 10, version 20H2 with [KB5005101](https://support.microsoft.com/help/5005101) [10.0.19042.1202] and later  ✅ Windows 10, version 21H1 with [KB5005101](https://support.microsoft.com/help/5005101) [10.0.19043.1202] and later  ✅ Windows 10, version 21H2 [10.0.19044.1288] and later  ✅ Windows 10, version 22H2 [10.0.19045.2130] and later  ✅ Windows 11, version 21H2 [10.0.22000] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/SetPolicyDrivenUpdateSourceForOtherUpdates
```

Configure this policy to specify whether to receive **Other Updates** from Windows Update endpoint, managed by Windows Update for Business policies, or through your configured Windows Server Update Service (WSUS) server. If you configure this policy, also configure the scan source policies for other update types:

- SetPolicyDrivenUpdateSourceForFeatureUpdates
- SetPolicyDrivenUpdateSourceForQualityUpdates
- SetPolicyDrivenUpdateSourceForDriverUpdates

Note

If you haven't properly configured Update/UpdateServiceUrl correctly to point to your WSUS server, this policy has no effect.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Detect, download and deploy other Updates from Windows Update. |
| 1 (Default) | Detect, download and deploy other Updates from Windows Server Update Services (WSUS). |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | CorpWuURL |
| Friendly Name | Specify intranet Microsoft update service location |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Server Update Service |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### SetPolicyDrivenUpdateSourceForQualityUpdates

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ [10.0.20348.371] and later  ✅ Windows 10, version 2004 with [KB5005101](https://support.microsoft.com/help/5005101) [10.0.19041.1202] and later  ✅ Windows 10, version 20H2 with [KB5005101](https://support.microsoft.com/help/5005101) [10.0.19042.1202] and later  ✅ Windows 10, version 21H1 with [KB5005101](https://support.microsoft.com/help/5005101) [10.0.19043.1202] and later  ✅ Windows 10, version 21H2 [10.0.19044.1288] and later  ✅ Windows 10, version 22H2 [10.0.19045.2130] and later  ✅ Windows 11, version 21H2 [10.0.22000] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/SetPolicyDrivenUpdateSourceForQualityUpdates
```

Configure this policy to specify whether to receive **Windows Quality Updates** from Windows Update endpoint, managed by Windows Update for Business policies, or through your configured Windows Server Update Service (WSUS) server. If you configure this policy, also configure the scan source policies for other update types:

- SetPolicyDrivenUpdateSourceForFeatureUpdates
- SetPolicyDrivenUpdateSourceForDriverUpdates
- SetPolicyDrivenUpdateSourceForOtherUpdates

Note

- If you haven't properly configured Update/UpdateServiceUrl correctly to point to your WSUS server, this policy has no effect.
- If you're also using the **Specify settings for optional component installation and component repair** ([ADMX_Servicing](policy-csp-admx-servicing)) policy to enable content for FoDs and language packs, see [How to make Features on Demand and language packs available when you're using WSUS or Configuration Manager](/en-us/windows/deployment/update/fod-and-lang-packs) to verify your policy configuration.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Detect, download and deploy Quality Updates from Windows Update. |
| 1 (Default) | Detect, download and deploy Quality Updates from Windows Server Update Services (WSUS). |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | CorpWuURL |
| Friendly Name | Specify intranet Microsoft update service location |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Server Update Service |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### SetProxyBehaviorForUpdateDetection

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 with [KB4577049](https://support.microsoft.com/help/4577049) [10.0.10240.18696] and later  ✅ Windows 10, version 1607 with [KB4577015](https://support.microsoft.com/help/4577015) [10.0.14393.3930] and later  ✅ Windows 10, version 1703 [10.0.15063.2500] and later  ✅ Windows 10, version 1709 with [KB4577041](https://support.microsoft.com/help/4577041) [10.0.16299.2107] and later  ✅ Windows 10, version 1803 with [KB4577032](https://support.microsoft.com/help/4577032) [10.0.17134.1726] and later  ✅ Windows 10, version 1809 with [KB4570333](https://support.microsoft.com/help/4570333) [10.0.17763.1457] and later  ✅ Windows 10, version 1903 with [KB4574727](https://support.microsoft.com/help/4574727) [10.0.18362.1082] and later  ✅ Windows 10, version 1909 with [KB4574727](https://support.microsoft.com/help/4574727) [10.0.18363.1082] and later  ✅ Windows 10, version 2004 with [KB4571756](https://support.microsoft.com/help/4571756) [10.0.19041.508] and later  ✅ Windows 11, version 21H2 [10.0.22000] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/SetProxyBehaviorForUpdateDetection
```

By default, HTTP WSUS servers scan only if system proxy is configured. This policy setting allows you to configure user proxy as a fallback for detecting updates while using an HTTP-based intranet server despite the vulnerabilities it presents.

This policy setting doesn't affect those customers who have, per Microsoft recommendation, secured their WSUS server with TLS/SSL protocol, thereby using HTTPS-based intranet servers to keep systems secure. That said, if a proxy is required, we recommend configuring a system proxy to ensure the highest level of security.

Note

Configuring this policy setting to 1 exposes your environment to potential security risk and makes scans unsecure.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Only use system proxy for detecting updates (default). |
| 1 | Allow user proxy to be used as a fallback if detection using system proxy fails. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | CorpWuURL |
| Friendly Name | Specify intranet Microsoft update service location |
| Element Name | Select the proxy behavior for Windows Update client for detecting updates. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Server Update Service |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### UpdateServiceUrl

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/UpdateServiceUrl
```

Allows the device to check for updates from a WSUS server instead of Microsoft Update. This is useful for on-premises MDMs that need to update devices that can't connect to the Internet.

The following list shows the supported values:

- Not configured: The device checks for updates from Microsoft Update.
- Set to a URL, such as `http://abcd-srv:8530`: The device checks for updates from the WSUS server at the specified URL.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `chr` (string) |
| Access Type | Add, Delete, Get, Replace |
| Default Value | CorpWSUS |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | CorpWuURL |
| Friendly Name | Specify intranet Microsoft update service location |
| Element Name | Set the intranet update service for detecting updates. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Server Update Service |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

**Example**:

```xml
<Replace>
    <CmdID>$CmdID$</CmdID>
    <Item>
        <Meta>
            <Format>chr</Format>
            <Type>text/plain</Type>
        </Meta>
        <Target>
            <LocURI>./Vendor/MSFT/Policy/Config/Update/UpdateServiceUrl</LocURI>
        </Target>
        <Data>http://abcd-srv:8530</Data>
    </Item>
</Replace>
```

### UpdateServiceUrlAlternate

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/UpdateServiceUrlAlternate
```

Specifies an alternate intranet server to host updates from Microsoft Update. You can then use this update service to automatically update computers on your network. This setting lets you specify a server on your network to function as an internal update service. The Automatic Updates client will search this service for updates that apply to the computers on your network. To use this setting, you must set two server name values: the server from which the Automatic Updates client detects and downloads updates, and the server to which updated workstations upload statistics. You can set both values to be the same server. An optional server name value can be specified to configure Windows Update agent, and download updates from an alternate download server instead of WSUS Server. Value type is string and the default value is an empty string, . If the setting isn't configured, and if Automatic Updates isn't disabled by policy or user preference, the Automatic Updates client connects directly to the Windows Update site on the Internet.

Note

If the Configure Automatic Updates Group Policy is disabled, then this policy has no effect. If the Alternate Download Server Group Policy isn't set, it will use the WSUS server by default to download updates. This policy isn't supported on Windows RT. Setting this policy won't have any effect on Windows RT PCs.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `chr` (string) |
| Access Type | Add, Delete, Get, Replace |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | CorpWuURL |
| Friendly Name | Specify intranet Microsoft update service location |
| Element Name | Set the alternate download server. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage updates offered from Windows Server Update Service |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

## Manage end user experience

### ActiveHoursEnd

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ActiveHoursEnd
```

- If you enable this policy, the PC won't automatically restart after updates during active hours. The PC will attempt to restart outside of active hours.

Note that the PC must restart for certain updates to take effect.

- If you disable or don't configure this policy and have no other reboot group policies, the user selected active hours will be in effect.

If any of the following two policies are enabled, this policy has no effect:

1. No auto-restart with logged-on users for scheduled automatic updates installations.
2. Always automatically restart at scheduled time.

Note that the default max active hours range is 18 hours from the active hours start time unless otherwise configured via the Specify active hours range for auto-restarts policy.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[0-23]` |
| Default Value | 17 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | ActiveHours |
| Friendly Name | Turn off auto-restart for updates during active hours |
| Element Name | End. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### ActiveHoursMaxRange

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ActiveHoursMaxRange
```

Enable this policy to specify the maximum number of hours from the start time that users can set their active hours.

The max active hours range can be set between 8 and 18 hours.

If you disable or don't configure this policy, the default max active hours range will be used.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[8-18]` |
| Default Value | 18 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | ActiveHoursMaxRange |
| Friendly Name | Specify active hours range for auto-restarts |
| Element Name | Max range. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### ActiveHoursStart

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ActiveHoursStart
```

- If you enable this policy, the PC won't automatically restart after updates during active hours. The PC will attempt to restart outside of active hours.

Note that the PC must restart for certain updates to take effect.

- If you disable or don't configure this policy and have no other reboot group policies, the user selected active hours will be in effect.

If any of the following two policies are enabled, this policy has no effect:

1. No auto-restart with logged-on users for scheduled automatic updates installations.
2. Always automatically restart at scheduled time.

Note that the default max active hours range is 18 hours from the active hours start time unless otherwise configured via the Specify active hours range for auto-restarts policy.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[0-23]` |
| Default Value | 8 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | ActiveHours |
| Friendly Name | Turn off auto-restart for updates during active hours |
| Element Name | Start. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### AllowAutoUpdate

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/AllowAutoUpdate
```

Enables the IT admin to manage automatic update behavior to scan, download, and install updates. Important. This option should be used only for systems under regulatory compliance, as you won't get security updates as well. If the policy isn't configured, end-users get the default behavior (Auto install and restart).

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 2 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Notify the user before downloading the update. This policy is used by the enterprise who wants to enable the end-users to manage data usage. With this option users are notified when there are updates that apply to the device and are ready for download. Users can download and install the updates from the Windows Update control panel. |
| 1 | Auto install the update and then notify the user to schedule a device restart. Updates are downloaded automatically on non-metered networks and installed during "Automatic Maintenance" when the device isn't in use and isn't running on battery power. If automatic maintenance is unable to install updates for two days, Windows Update will install updates immediately. If the installation requires a restart, the end-user is prompted to schedule the restart time. After the update is installed, if the user hasn't scheduled a restart, the device will attempt to restart automatically. The user will be notified about the scheduled restart and can reschedule it if the proposed time is inconvenient. Enabling the end-user to control the start time reduces the risk of accidental data loss caused by applications that don't shutdown properly on restart. |
| 2 (Default) | Auto install and restart. Updates are downloaded automatically on non-metered networks and installed during "Automatic Maintenance" when the device isn't in use and isn't running on battery power. If automatic maintenance is unable to install updates for two days, Windows Update will install updates right away. If a restart is required, then the device is automatically restarted when the device isn't actively being used. This is the default behavior for unmanaged devices. Devices are updated quickly, but it increases the risk of accidental data loss caused by an application that doesn't shutdown properly on restart. |
| 3 | Auto install and restart at a specified time. The IT specifies the installation day and time. If no day and time are specified, the default is 3 AM daily. Automatic installation happens at this time and device restart happens after a 15-minute countdown. If the user is logged in when Windows is ready to restart, the user can interrupt the 15-minute countdown to delay the restart. |
| 4 | Auto install and restart without end-user control. Updates are downloaded automatically on non-metered networks and installed during "Automatic Maintenance" when the device isn't in use and isn't running on battery power. If automatic maintenance is unable to install updates for two days, Windows Update will install updates right away. If a restart is required, then the device is automatically restarted when the device isn't actively being used. This setting option also sets the end-user control panel to read-only. |
| 5 | Turn off automatic updates. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AutoUpdateCfg |
| Friendly Name | Configure Automatic Updates |
| Element Name | Configure automatic updating. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate\AU |
| ADMX File Name | WindowsUpdate.admx |

### AllowAutoWindowsUpdateDownloadOverMeteredNetwork

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1709 [10.0.16299] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/AllowAutoWindowsUpdateDownloadOverMeteredNetwork
```

Enabling this policy will automatically download updates, even over metered data connections (charges may apply)

A significant number of devices primarily use cellular data and don't have Wi-Fi access, which leads to a lower number of devices getting updates. Since a large number of devices have large data plans or unlimited data, this policy can unblock devices from getting updates.

This policy is accessible through the Update setting in the user interface or Group Policy.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Not allowed. |
| 1 | Allowed. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AllowAutoWindowsUpdateDownloadOverMeteredNetwork |
| Friendly Name | Allow updates to be downloaded automatically over metered connections |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| Registry Value Name | AllowAutoWindowsUpdateDownloadOverMeteredNetwork |
| ADMX File Name | WindowsUpdate.admx |

### AllowMUUpdateService

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/AllowMUUpdateService
```

Allows the IT admin to manage whether to scan for app updates from Microsoft Update.

Note

- For a list of other Microsoft products that might be updated, see [Update other Microsoft products](/en-us/windows/deployment/update/update-other-microsoft-products).
- Setting this policy back to 0 or Not configured doesn't revert the configuration to receive updates from Microsoft Update automatically. In order to revert the configuration, you can run the PowerShell commands that are listed below to remove the Microsoft Update service:

```powershell
$MUSM = New-Object -ComObject "Microsoft.Update.ServiceManager"
$MUSM.RemoveService("7971f918-a847-4430-9279-4a52d1efe18d")
```

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Not allowed or not configured. |
| 1 | Allowed. Accepts updates received through Microsoft Update. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AutoUpdateCfg |
| Friendly Name | Configure Automatic Updates |
| Element Name | Install updates for other Microsoft products. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate\AU |
| ADMX File Name | WindowsUpdate.admx |

### AllowTemporaryEnterpriseFeatureControl

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 22H2 with [KB5022913](https://support.microsoft.com/help/5022913) [10.0.22621.1344] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/AllowTemporaryEnterpriseFeatureControl
```

Features introduced via servicing (outside of the annual feature update) are off by default for devices that have their Windows updates managed\*.

- If this policy is configured to "Enabled", then all features available in the latest monthly quality update installed will be on.
- If this policy is set to "Not Configured" or "Disabled" then features that are shipped via a monthly quality update (servicing) will remain off until the feature update that includes these features is installed.

\*Windows update managed devices are those that have their Windows updates managed via policy; whether via the cloud using Windows Update for Business or on-premises with Windows Server Update Services (WSUS).

Note

In Intune, this setting is known as **Allow Temporary Enterprise Feature Control** and is available in the Settings Catalog. By default, all features introduced via servicing that are behind the commercial control are off for Windows-Update-managed devices. When set to Allowed, these features are enabled and turned on. For more information, see [Blog: Commercial control for continuous innovation](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/commercial-control-for-continuous-innovation/ba-p/3737575).

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Not allowed. |
| 1 | Allowed. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AllowTemporaryEnterpriseFeatureControl |
| Friendly Name | Enable features introduced via servicing that are off by default |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| Registry Value Name | AllowTemporaryEnterpriseFeatureControl |
| ADMX File Name | WindowsUpdate.admx |

### ConfigureDeadlineForFeatureUpdates

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1903 [10.0.18362] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ConfigureDeadlineForFeatureUpdates
```

Number of days before feature updates are installed on devices automatically regardless of active hours. Before the deadline passes, users can schedule restarts, and automatic restarts can happen outside of active hours. When set to 0, updates will download and install immediately, but might not finish within the day due to device availability and network connectivity.

Note

- After the deadline passes, restarts will occur regardless of active hours and users won't be able to reschedule.
- When this policy is used, the download, installation, and reboot settings from Update/AllowAutoUpdate are ignored.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[0-30]` |
| Default Value | 2 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | ComplianceDeadlineForFU |
| Friendly Name | Specify deadline for automatic updates and restarts for feature update |
| Element Name | Deadline (days) |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### ConfigureDeadlineForQualityUpdates

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1903 [10.0.18362] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ConfigureDeadlineForQualityUpdates
```

Number of days before quality updates are installed on devices automatically regardless of active hours. Before the deadline passes, users can schedule restarts, and automatic restarts can happen outside of active hours. When set to 0, updates will download and install immediately, but might not finish within the day due to device availability and network connectivity.

Note

- After the deadline passes, restarts will occur regardless of active hours and users won't be able to reschedule.
- When this policy is used, the download, installation, and reboot settings from Update/AllowAutoUpdate are ignored.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[0-30]` |
| Default Value | 1 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | ComplianceDeadline |
| Friendly Name | Specify deadline for automatic updates and restarts for quality update |
| Element Name | Deadline (days) |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### ConfigureDeadlineGracePeriod

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1903 [10.0.18362] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ConfigureDeadlineGracePeriod
```

Minimum number of days from update installation until restarts occur automatically for quality updates. This policy only takes effect when Update/ConfigureDeadlineForQualityUpdates is configured. If Update/ConfigureDeadlineForQualityUpdates is configured but this policy isn't, then the default value of 2 days will take effect.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[0-7]` |
| Default Value | 2 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | ComplianceDeadline |
| Friendly Name | Specify deadline for automatic updates and restarts for quality update |
| Element Name | Grace period (days) |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### ConfigureDeadlineGracePeriodForFeatureUpdates

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1809 with [KB5000854](https://support.microsoft.com/help/5000854) [10.0.17763.1852] and later  ✅ Windows 10, version 1909 with [KB5000850](https://support.microsoft.com/help/5000850) [10.0.18363.1474] and later  ✅ Windows 10, version 2004 with [KB5000842](https://support.microsoft.com/help/5000842) [10.0.19041.906] and later  ✅ Windows 10, version 20H2 with [KB5000842](https://support.microsoft.com/help/5000842) [10.0.19042.906] and later  ✅ Windows 11, version 21H2 [10.0.22000] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ConfigureDeadlineGracePeriodForFeatureUpdates
```

Minimum number of days from update installation until restarts occur automatically for feature updates. This policy only takes effect when Update/ConfigureDeadlineForFeatureUpdates is configured. If Update/ConfigureDeadlineForFeatureUpdates is configured but this policy isn't, then the value configured by Update/ConfigureDeadlineGracePeriod will be used. If Update/ConfigureDeadlineGracePeriod is also not configured, then the default value of 7 days will take effect.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[0-7]` |
| Default Value | 7 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | ComplianceDeadlineForFU |
| Friendly Name | Specify deadline for automatic updates and restarts for feature update |
| Element Name | Grace Period (days) |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### ConfigureDeadlineNoAutoRebootForFeatureUpdates

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 22H2 [10.0.22621] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ConfigureDeadlineNoAutoRebootForFeatureUpdates
```

This policy lets you specify the number of days before feature updates are installed on devices automatically, and a grace period after which required restarts occur automatically.

Set deadlines for feature updates and quality updates to meet your compliance goals. Updates will be downloaded and installed as soon as they're offered and automatic restarts will be attempted outside of active hours. Once the deadline has passed, restarts will occur regardless of active hours, and users won't be able to reschedule. If the deadline is set to 0 days, the update will be installed immediately upon offering, but might not finish within the day due to device availability and network connectivity.

Set a grace period for feature updates to guarantee users a minimum time to manage their restarts once updates are installed. Users can schedule restarts during the grace period and Windows can still automatically restart outside of active hours if users choose not to schedule restarts. The grace period might not take effect if users already have more than the number of days set as grace period to manage their restart, based on deadline configurations.

You can set the device to delay restarting until both the deadline and grace period have expired.

If you disable or don't configure this policy, devices will get updates and will restart according to the default schedule.

This policy overrides the following policies:

1. Specify deadline before auto restart for update installation
2. Specify Engaged restart transition and notification schedule for updates.
3. Always automatically restart at the scheduled time
4. Configure Automatic Updates.

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
| Name | ComplianceDeadlineForFU |
| Friendly Name | Specify deadline for automatic updates and restarts for feature update |
| Element Name | Don't auto-restart until end of grace period. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### ConfigureDeadlineNoAutoRebootForQualityUpdates

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 22H2 [10.0.22621] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ConfigureDeadlineNoAutoRebootForQualityUpdates
```

This policy lets you specify the number of days before quality updates are installed on devices automatically, and a grace period after which required restarts occur automatically.

Set deadlines for quality updates to meet your compliance goals. Updates will be downloaded and installed as soon as they're offered and automatic restarts will be attempted outside of active hours. Once the deadline has passed, restarts will occur regardless of active hours, and users won't be able to reschedule. If the deadline is set to 0 days, the update will be installed immediately upon offering, but might not finish within the day due to device availability and network connectivity.

Set a grace period for quality updates to guarantee users a minimum time to manage their restarts once updates are installed. Users can schedule restarts during the grace period and Windows can still automatically restart outside of active hours if users choose not to schedule restarts. The grace period might not take effect if users already have more than the number of days set as grace period to manage their restart, based on deadline configurations.

You can set the device to delay restarting until both the deadline and grace period have expired.

If you disable or don't configure this policy, devices will get updates and will restart according to the default schedule.

This policy overrides the following policies:

1. Specify deadline before auto restart for update installation
2. Specify Engaged restart transition and notification schedule for updates.
3. Always automatically restart at the scheduled time
4. Configure Automatic Updates.

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
| Name | ComplianceDeadline |
| Friendly Name | Specify deadline for automatic updates and restarts for quality update |
| Element Name | Don't auto-restart until end of grace period. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### ConfigureFeatureUpdateUninstallPeriod

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1803 [10.0.17134] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ConfigureFeatureUpdateUninstallPeriod
```

Enable enterprises/IT admin to configure feature update uninstall period.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[2-60]` |
| Default Value | 10 |

### NoUpdateNotificationsDuringActiveHours

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 22H2 [10.0.22621] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/NoUpdateNotificationsDuringActiveHours
```

0 (default) - Use the default Windows Update notifications 1 - Turn off all notifications, excluding restart warnings 2 - Turn off all notifications, including restart warnings.

This policy allows you to define what Windows Update notifications users see. This policy doesn't control how and when updates are downloaded and installed.

Important if you choose not to get update notifications and also define other Group policy so that devices aren't automatically getting updates, neither you nor device users will be aware of critical security, quality, or feature updates, and your devices may be at risk.

If you select "Apply only during active hours" in conjunction with Option 1 or 2, then notifications will only be disabled during active hours. You can set active hours by setting "Turn off auto-restart for updates during active hours" or allow the device to set active hours based on user behavior. To ensure that the device stays secure, a notification will still be shown if this option is selected once "Specify deadlines for automatic updates and restarts" deadline has been reached if configured, regardless of active hours.

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
| Name | UpdateNotificationLevel |
| Friendly Name | Display options for update notifications |
| Element Name | Apply only during active hours. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### ScheduledInstallDay

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ScheduledInstallDay
```

Enables the IT admin to schedule the day of the update installation. The data type is a integer.

Note

This policy will only take effect if Update/AllowAutoUpdate has been configured to option 3 or 4 for scheduled installation.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Every day. |
| 1 | Sunday. |
| 2 | Monday. |
| 3 | Tuesday. |
| 4 | Wednesday. |
| 5 | Thursday. |
| 6 | Friday. |
| 7 | Saturday. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AutoUpdateCfg |
| Friendly Name | Configure Automatic Updates |
| Element Name | Scheduled install day. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate\AU |
| ADMX File Name | WindowsUpdate.admx |

### ScheduledInstallEveryWeek

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1709 [10.0.16299] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ScheduledInstallEveryWeek
```

Enables the IT admin to schedule the update installation on the every week. Value type is integer.

Note

This policy will only take effect if Update/AllowAutoUpdate has been configured to option 3 or 4 for scheduled installation.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | No update in the schedule. |
| 1 (Default) | Update is scheduled every week. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AutoUpdateCfg |
| Friendly Name | Configure Automatic Updates |
| Element Name | Every week. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate\AU |
| ADMX File Name | WindowsUpdate.admx |

### ScheduledInstallFirstWeek

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1709 [10.0.16299] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ScheduledInstallFirstWeek
```

Enables the IT admin to schedule the update installation on the first week of the month. Value type is integer.

The ScheduledInstall\*week policies operate on numeric days.

- ScheduledInstallFirstWeek: First week of the month (Days 1-7).
- ScheduledInstallSecondWeek: Second week of the month (Days 8-14).
- ScheduledInstallThirdWeek: Third week of the month (Days 15-21).
- ScheduledInstallFourthWeek: Fourth week of the month (Days 22-31).

These policies aren't exclusive and can be used in any combination. Together with ScheduledInstallDay, it defines the ordinal number of a weekday in a month. E.g., ScheduledInstallSecondWeek + ScheduledInstallDay = 3 is second Tuesday of the month. If the device is unavailable at the scheduled time, it can postpone installation of updates until the next month.

Note

This policy will only take effect if Update/AllowAutoUpdate has been configured to option 3 or 4 for scheduled installation.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | No update in the schedule. |
| 1 | Update is scheduled every first week of the month. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AutoUpdateCfg |
| Friendly Name | Configure Automatic Updates |
| Element Name | First week of the month. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate\AU |
| ADMX File Name | WindowsUpdate.admx |

### ScheduledInstallFourthWeek

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1709 [10.0.16299] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ScheduledInstallFourthWeek
```

Enables the IT admin to schedule the update installation on the fourth week of the month. Value type is integer.

The ScheduledInstall\*week policies operate on numeric days.

- ScheduledInstallFirstWeek: First week of the month (Days 1-7).
- ScheduledInstallSecondWeek: Second week of the month (Days 8-14).
- ScheduledInstallThirdWeek: Third week of the month (Days 15-21).
- ScheduledInstallFourthWeek: Fourth week of the month (Days 22-31).

These policies aren't exclusive and can be used in any combination. Together with ScheduledInstallDay, it defines the ordinal number of a weekday in a month. E.g., ScheduledInstallSecondWeek + ScheduledInstallDay = 3 is second Tuesday of the month. If the device is unavailable at the scheduled time, it can postpone installation of updates until the next month.

Note

This policy takes effect only when Update/AllowAutoUpdate is configured with option 3 or 4 for scheduled installation.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | No update in the schedule. |
| 1 | Update is scheduled every fourth week of the month. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AutoUpdateCfg |
| Friendly Name | Configure Automatic Updates |
| Element Name | Fourth week of the month. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate\AU |
| ADMX File Name | WindowsUpdate.admx |

### ScheduledInstallSecondWeek

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1709 [10.0.16299] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ScheduledInstallSecondWeek
```

Enables the IT admin to schedule the update installation on the second week of the month. Value type is integer.

The ScheduledInstall\*week policies operate on numeric days.

- ScheduledInstallFirstWeek: First week of the month (Days 1-7).
- ScheduledInstallSecondWeek: Second week of the month (Days 8-14).
- ScheduledInstallThirdWeek: Third week of the month (Days 15-21).
- ScheduledInstallFourthWeek: Fourth week of the month (Days 22-31).

These policies aren't exclusive and can be used in any combination. Together with ScheduledInstallDay, it defines the ordinal number of a weekday in a month. E.g., ScheduledInstallSecondWeek + ScheduledInstallDay = 3 is second Tuesday of the month. If the device is unavailable at the scheduled time, it can postpone installation of updates until the next month.

Note

This policy takes effect only when Update/AllowAutoUpdate is configured with option 3 or 4 for scheduled installation.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | No update in the schedule. |
| 1 | Update is scheduled every second week of the month. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AutoUpdateCfg |
| Friendly Name | Configure Automatic Updates |
| Element Name | Second week of the month. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate\AU |
| ADMX File Name | WindowsUpdate.admx |

### ScheduledInstallThirdWeek

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1709 [10.0.16299] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ScheduledInstallThirdWeek
```

Enables the IT admin to schedule the update installation on the third week of the month. Value type is integer.

The ScheduledInstall\*week policies operate on numeric days.

- ScheduledInstallFirstWeek: First week of the month (Days 1-7).
- ScheduledInstallSecondWeek: Second week of the month (Days 8-14).
- ScheduledInstallThirdWeek: Third week of the month (Days 15-21).
- ScheduledInstallFourthWeek: Fourth week of the month (Days 22-31).

These policies aren't exclusive and can be used in any combination. Together with ScheduledInstallDay, it defines the ordinal number of a weekday in a month. E.g., ScheduledInstallSecondWeek + ScheduledInstallDay = 3 is second Tuesday of the month. If the device is unavailable at the scheduled time, it can postpone installation of updates until the next month.

Note

This policy takes effect only when Update/AllowAutoUpdate is configured with option 3 or 4 for scheduled installation.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | No update in the schedule. |
| 1 | Update is scheduled every third week of the month. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AutoUpdateCfg |
| Friendly Name | Configure Automatic Updates |
| Element Name | Third week of the month. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate\AU |
| ADMX File Name | WindowsUpdate.admx |

### ScheduledInstallTime

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ScheduledInstallTime
```

Enables the IT admin to schedule the time of the update installation. The data type is a integer. Supported values are 0-23, where 0 = 12 AM and 23 = 11 PM. The default value is 3.

Note

- This policy takes effect only when Update/AllowAutoUpdate is configured with option 3 or 4 for scheduled installation.
- There's a window of approximately 30 minutes to allow for higher success rates of installation.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[0-23]` |
| Default Value | 3 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AutoUpdateCfg |
| Friendly Name | Configure Automatic Updates |
| Element Name | Scheduled install time. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate\AU |
| ADMX File Name | WindowsUpdate.admx |

### SetDisablePauseUXAccess

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1809 [10.0.17763] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/SetDisablePauseUXAccess
```

This setting allows to remove access to "Pause updates" feature.

Once enabled user access to pause updates is removed.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 1 | Enable. |
| 0 (Default) | Disable. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisablePauseUXAccess |
| Friendly Name | Remove access to "Pause updates" feature |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| Registry Value Name | SetDisablePauseUXAccess |
| ADMX File Name | WindowsUpdate.admx |

### SetDisableUXWUAccess

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1809 [10.0.17763] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/SetDisableUXWUAccess
```

This setting allows you to remove access to scan Windows Update.

If you enable this setting user access to Windows Update scan, download and install is removed.

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
| Name | DisableUXWUAccess |
| Friendly Name | Remove access to use all Windows Update features |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| Registry Value Name | SetDisableUXWUAccess |
| ADMX File Name | WindowsUpdate.admx |

### SetEDURestart

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/SetEDURestart
```

Enabling this policy for EDU devices that remain on Carts overnight will skip power checks to ensure update reboots will happen at the scheduled install time.

Enabling this policy will restrict updates to download and install outside of Active Hours. Updates are allowed to start even if there's a signed-in user or the device is on battery power, providing there's more than 70% battery capacity. Windows will schedule the device to wake from sleep 1 hour after the ActiveHoursEnd time with a 60-minute random delay. Devices will reboot immediately after the updates are installed. If there are still pending updates, the device continues to retry every hour for 4 hours.

The following rules are followed regarding battery power:

- Above 70% - allowed to start work;
- Above 40% - allowed to reboot;
- Above 20% - allowed to continue work.

This setting overrides the install deferral behavior of AllowAutoUpdate.

These settings are designed for education devices that remain in carts overnight that are left in sleep mode. It isn't designed for 1:1 devices.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Not configured. |
| 1 | Configured. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | SetEDURestart |
| Friendly Name | Update Power Policy for Cart Restarts |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| Registry Value Name | SetEDURestart |
| ADMX File Name | WindowsUpdate.admx |

### UpdateNotificationLevel

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1809 [10.0.17763] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/UpdateNotificationLevel
```

0 (default) - Use the default Windows Update notifications 1 - Turn off all notifications, excluding restart warnings 2 - Turn off all notifications, including restart warnings.

This policy allows you to define what Windows Update notifications users see. This policy doesn't control how and when updates are downloaded and installed.

Important if you choose not to get update notifications and also define other Group policy so that devices aren't automatically getting updates, neither you nor device users will be aware of critical security, quality, or feature updates, and your devices may be at risk.

If you select "Apply only during active hours" in conjunction with Option 1 or 2, then notifications will only be disabled during active hours. You can set active hours by setting "Turn off auto-restart for updates during active hours" or allow the device to set active hours based on user behavior. To ensure that the device stays secure, a notification will still be shown if this option is selected once "Specify deadlines for automatic updates and restarts" deadline has been reached if configured, regardless of active hours.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Use the default Windows Update notifications. |
| 1 | Turn off all notifications, excluding restart warnings. |
| 2 | Turn off all notifications, including restart warnings. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | UpdateNotificationLevel |
| Friendly Name | Display options for update notifications |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Manage end user experience |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| Registry Value Name | SetUpdateNotificationLevel |
| ADMX File Name | WindowsUpdate.admx |

## Manage updates with maintenance windows

### MaintenanceWindowDurationHours

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 with [KB5077181](https://support.microsoft.com/help/5077181) [10.0.26100.7840] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowDurationHours
```

Configure the duration of the maintenance window in hours. Minimum value is 2, maximum value is 24.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[2-24]` |
| Default Value | 2 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowDurationHours |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowDurationHours |

### MaintenanceWindowEnabled

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 with [KB5077181](https://support.microsoft.com/help/5077181) [10.0.26100.7840] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowEnabled
```

Specifies whether maintenance window is enabled.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Disable. |
| 1 | Enable. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowEnabled |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowEnabled |

### MaintenanceWindowMonthlyMonthBasedDayOfMonth

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 with [KB5077181](https://support.microsoft.com/help/5077181) [10.0.26100.7840] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowMonthlyMonthBasedDayOfMonth
```

If the maintenance window repeat schedule is set to monthly, and set to repeat on the same date each month, configure the day of the month to repeat maintenance window occurrence (for example, 2 = repeat on the 2nd day of the month). Maximum value is 28.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[1-28]` |
| Default Value | 1 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowMonthlyMonthBasedDayOfMonth |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowMonthlyMonthBasedDayOfMonth |

### MaintenanceWindowMonthlySchedule

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 with [KB5077181](https://support.microsoft.com/help/5077181) [10.0.26100.7840] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowMonthlySchedule
```

If the maintenance window repeat schedule is set to monthly, configure whether to repeat on the same date each month (the 1st of every month), a day within a specific week (for example, the second Tuesday of every month), or on the last day of each month. 1=repeat on same date each month, 2=repeat on a day of a specific week, 3=repeat on the last day of each month.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 1 (Default) | Date-based. |
| 2 | Week-based. |
| 3 | Last day of the month. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowMonthlySchedule |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowMonthlySchedule |

### MaintenanceWindowMonthlyWeekBasedDayOfTheWeek

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 with [KB5077181](https://support.microsoft.com/help/5077181) [10.0.26100.7840] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowMonthlyWeekBasedDayOfTheWeek
```

If the maintenance window repeat schedule is set to monthly, and set to repeat on the a specific day of a specific week, configure the specific day of the week to repeat maintenance window occurrence: 1=Sunday, 2=Monday, 3=Tuesday, 4=Wednesday, 5=Thursday, 6=Friday, 7=Saturday.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 1 (Default) | Sunday. |
| 2 | Monday. |
| 3 | Tuesday. |
| 4 | Wednesday. |
| 5 | Thursday. |
| 6 | Friday. |
| 7 | Saturday. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowMonthlyWeekBasedDayOfTheWeek |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowMonthlyWeekBasedDayOfTheWeek |

### MaintenanceWindowMonthlyWeekBasedOccurrenceInMonth

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 with [KB5077181](https://support.microsoft.com/help/5077181) [10.0.26100.7840] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowMonthlyWeekBasedOccurrenceInMonth
```

If the maintenance window repeat schedule is set to monthly, and set to repeat on the a specific day of a specific week, configure the specific week to repeat maintenance window occurrence. 1=first week, 2=second week, 3=third week, 4=fourth week, 5=last week.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 1 (Default) | First. |
| 2 | Second. |
| 3 | Third. |
| 4 | Fourth. |
| 5 | Last. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowMonthlyWeekBasedOccurrenceInMonth |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowMonthlyWeekBasedOccurrenceInMonth |

### MaintenanceWindowRepeatScheduleOption

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 with [KB5077181](https://support.microsoft.com/help/5077181) [10.0.26100.7840] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowRepeatScheduleOption
```

Configure whether and how often the maintenance window repeats, 1=no repeat, 2=daily, 3=weekly, 4=monthly. Daily/weekly/monthly schedule will be repeated every day/week/month.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 1 (Default) | No repeat. |
| 2 | Daily. |
| 3 | Weekly. |
| 4 | Monthly. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowRepeatScheduleOption |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowRepeatScheduleOption |

### MaintenanceWindowStartDate

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 with [KB5077181](https://support.microsoft.com/help/5077181) [10.0.26100.7840] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowStartDate
```

Configure the start date for the maintenance window in the format of YYYY-MM-DD (for example, 2025-12-16). This field will only be honored for a non-repeating maintenance window. Repeating maintenance windows will start on the earliest date that meets the configured schedule.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `chr` (string) |
| Access Type | Add, Delete, Get, Replace |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowStartDate |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowStartDate |

### MaintenanceWindowStartTime

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 with [KB5077181](https://support.microsoft.com/help/5077181) [10.0.26100.7840] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowStartTime
```

Configure the start time for the maintenance window in HH:MM format (for example, 23:30).

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `chr` (string) |
| Access Type | Add, Delete, Get, Replace |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowStartTime |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowStartTime |

### MaintenanceWindowUpdateActions

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 with [KB5077181](https://support.microsoft.com/help/5077181) [10.0.26100.7840] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowUpdateActions
```

Specifies which update operations are allowed only during the maintenance window, 1 = Download, install and restart, 2 = Install and restart, 3 = Restart only.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 1 (Default) | Download, install and restart. |
| 2 | Install and restart. |
| 3 | Restart only. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowUpdateActions |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowUpdateActions |

### MaintenanceWindowWeeklyFriday

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 with [KB5077181](https://support.microsoft.com/help/5077181) [10.0.26100.7840] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowWeeklyFriday
```

If the maintenance window repeat schedule is set to weekly, configure whether Friday is included in the weekly schedule.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Disable. |
| 1 | Enable. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowWeeklyFriday |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowWeeklyFriday |

### MaintenanceWindowWeeklyMonday

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 with [KB5077181](https://support.microsoft.com/help/5077181) [10.0.26100.7840] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowWeeklyMonday
```

If the maintenance window repeat schedule is set to weekly, configure whether Monday is included in the weekly schedule.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Disable. |
| 1 | Enable. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowWeeklyMonday |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowWeeklyMonday |

### MaintenanceWindowWeeklySaturday

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 with [KB5077181](https://support.microsoft.com/help/5077181) [10.0.26100.7840] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowWeeklySaturday
```

If the maintenance window repeat schedule is set to weekly, configure whether Saturday is included in the weekly schedule.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Disable. |
| 1 | Enable. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowWeeklySaturday |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowWeeklySaturday |

### MaintenanceWindowWeeklySunday

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 with [KB5077181](https://support.microsoft.com/help/5077181) [10.0.26100.7840] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowWeeklySunday
```

If the maintenance window repeat schedule is set to weekly, configure whether Sunday is included in the weekly schedule.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Disable. |
| 1 | Enable. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowWeeklySunday |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowWeeklySunday |

### MaintenanceWindowWeeklyThursday

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 with [KB5077181](https://support.microsoft.com/help/5077181) [10.0.26100.7840] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowWeeklyThursday
```

If the maintenance window repeat schedule is set to weekly, configure whether Thursday is included in the weekly schedule.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Disable. |
| 1 | Enable. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowWeeklyThursday |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowWeeklyThursday |

### MaintenanceWindowWeeklyTuesday

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 with [KB5077181](https://support.microsoft.com/help/5077181) [10.0.26100.7840] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowWeeklyTuesday
```

If the maintenance window repeat schedule is set to weekly, configure whether Tuesday is included in the weekly schedule.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Disable. |
| 1 | Enable. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowWeeklyTuesday |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowWeeklyTuesday |

### MaintenanceWindowWeeklyWednesday

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 24H2 with [KB5077181](https://support.microsoft.com/help/5077181) [10.0.26100.7840] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowWeeklyWednesday
```

If the maintenance window repeat schedule is set to weekly, configure whether Wednesday is included in the weekly schedule.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Disable. |
| 1 | Enable. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowWeeklyWednesday |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowWeeklyWednesday |

### MaintenanceWindowDailyInterval

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows Insider Preview |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowDailyInterval
```

Specifies the repeat interval in days for daily maintenance window schedule.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[1-90]` |
| Default Value | 1 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowDailyInterval |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowDailyInterval |

### MaintenanceWindowMonthlyInterval

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows Insider Preview |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowMonthlyInterval
```

Specifies the repeat interval in months for monthly maintenance window schedule.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[1-3]` |
| Default Value | 1 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowMonthlyInterval |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowMonthlyInterval |

### MaintenanceWindowWeeklyInterval

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows Insider Preview |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/MaintenanceWindowWeeklyInterval
```

Specifies the repeat interval in weeks for weekly maintenance window schedule.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[1-12]` |
| Default Value | 1 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | MaintenanceWindowWeeklyInterval |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | MaintenanceWindowWeeklyInterval |

## Legacy Policies

### AlwaysAutoRebootAtScheduledTimeMinutes

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 22H2 [10.0.22621] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/AlwaysAutoRebootAtScheduledTimeMinutes
```

- If you enable this policy, a restart timer will always begin immediately after Windows Update installs important updates, instead of first notifying users on the login screen for at least two days.

The restart timer can be configured to start with any value from 15 to 180 minutes. When the timer runs out, the restart will proceed even if the PC has signed-in users.

- If you disable or don't configure this policy, Windows Update won't alter its restart behavior.

If the "No auto-restart with logged-on users for scheduled automatic updates installations" policy is enabled, then this policy has no effect.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[15-180]` |
| Default Value | 15 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AlwaysAutoRebootAtScheduledTime |
| Friendly Name | Always automatically restart at the scheduled time |
| Element Name | work (minutes) |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Legacy Policies |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate\AU |
| ADMX File Name | WindowsUpdate.admx |

### AutoRestartDeadlinePeriodInDays

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/AutoRestartDeadlinePeriodInDays
```

Specify the deadline before the PC will automatically restart to apply updates. The deadline can be set 2 to 14 days past the default restart date.

The restart may happen inside active hours.

If you disable or don't configure this policy, the PC will restart according to the default schedule.

Enabling either of the following two policies will override the above policy:

1. No auto-restart with logged-on users for scheduled automatic updates installations.
2. Always automatically restart at scheduled time.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[2-30]` |
| Default Value | 7 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AutoRestartDeadline |
| Friendly Name | Specify deadline before auto-restart for update installation |
| Element Name | Quality Updates (days) |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Legacy Policies |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### AutoRestartDeadlinePeriodInDaysForFeatureUpdates

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1809 [10.0.17763] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/AutoRestartDeadlinePeriodInDaysForFeatureUpdates
```

Specify the deadline before the PC will automatically restart to apply updates. The deadline can be set 2 to 14 days past the default restart date.

The restart may happen inside active hours.

If you disable or don't configure this policy, the PC will restart according to the default schedule.

Enabling either of the following two policies will override the above policy:

1. No auto-restart with logged-on users for scheduled automatic updates installations.
2. Always automatically restart at scheduled time.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[2-30]` |
| Default Value | 7 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AutoRestartDeadline |
| Friendly Name | Specify deadline before auto-restart for update installation |
| Element Name | Feature Updates (days) |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Legacy Policies |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### AutoRestartNotificationSchedule

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/AutoRestartNotificationSchedule
```

Enable this policy to specify when auto-restart reminders are displayed.

You can specify the amount of time prior to a scheduled restart to notify the user.

If you disable or don't configure this policy, the default period will be used.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 15 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 15 (Default) | 15 Minutes. |
| 30 | 30 Minutes. |
| 60 | 60 Minutes. |
| 120 | 120 Minutes. |
| 240 | 240 Minutes. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AutoRestartNotificationConfig |
| Friendly Name | Configure auto-restart reminder notifications for updates |
| Element Name | Period (min) |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Legacy Policies |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### AutoRestartRequiredNotificationDismissal

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/AutoRestartRequiredNotificationDismissal
```

Enable this policy to specify the method by which the auto-restart required notification is dismissed. When a restart is required to install updates, the auto-restart required notification is displayed. By default, the notification is automatically dismissed after 25 seconds.

The method can be set to require user action to dismiss the notification.

If you disable or don't configure this policy, the default method will be used.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 1 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 1 (Default) | Auto Dismissal. |
| 2 | User Dismissal. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AutoRestartRequiredNotificationDismissal |
| Friendly Name | Configure auto-restart required notification for updates |
| Element Name | Method. |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Legacy Policies |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### DeferUpdatePeriod

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/DeferUpdatePeriod
```

Note

Don't use this policy for Windows 10, version 1607 or later devices. You can continue to use DeferUpdatePeriod for Windows 10, version 1511 devices.

Allows IT Admins to specify update delays for up to four weeks. Supported values are 0-4, which refers to the number of weeks to defer updates.

- If the **Specify intranet Microsoft update service location** policy is enabled, then the "Defer upgrades by", "Defer updates by" and "Pause Updates and Upgrades" settings have no effect.
- If the **Allow Telemetry** policy is enabled and the Options value is set to 0, then the "Defer upgrades by", "Defer updates by" and "Pause Updates and Upgrades" settings have no effect.

OS upgrade:

- Maximum deferral: Eight months
- Deferral increment: One month
- Update type/notes:
    - Upgrade - 3689BDC8-B205-4AF4-8D4A-A63924C5E9D5

Update:

- Maximum deferral: One month
- Deferral increment: One week
- Update type/notes: If a machine has Microsoft Update enabled, any Microsoft Updates in these categories will also observe Defer / Pause logic:

    - Security Update - 0FA1201D-4330-4FA8-8AE9-B877473B6441
    - Critical Update - E6CF1350-C01B-414D-A61F-263D14D133B4
    - Update Rollup - 28BC880E-0592-4CBF-8F95-C79B17911D5F
    - Service Pack - 68C5B0A3-D1A6-4553-AE49-01D3A7827828
    - Tools - B4832BD8-E735-4761-8DAF-37F882276DAB
    - Feature Pack - B54E7D24-7ADD-428F-8B75-90A396FA584F
    - Update - CD5FFD1E-E932-4E3A-BF74-18BF0B1BBD83
    - Driver - EBFC1FC5-71A4-4F7B-9ACA-3B9A503104A0

Other/can't defer:

- Maximum deferral: No deferral
- Deferral increment: No deferral
- Update type/notes: Any update category not enumerated above falls into this category. - Definition Update - E0789628-CE08-4437-BE74-2495B842F43B

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[0-4]` |
| Default Value | 0 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DeferUpgrade |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | DeferUpdatePeriodId |

### DeferUpgradePeriod

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/DeferUpgradePeriod
```

Allows IT Admins to specify additional upgrade delays for up to 8 months. Supported values are 0-8, which refers to the number of months to defer upgrades.

- If the **Specify intranet Microsoft update service location** policy is enabled, then the Defer upgrades by, Defer updates by and Pause Updates and Upgrades settings have no effect.
- If the **Allow Telemetry** policy is enabled and the Options value is set to 0, then the Defer upgrades by, Defer updates by and Pause Updates and Upgrades settings have no effect.

Note

Don't use this policy for Windows 10, version 1607 or later devices. You can continue to use DeferUpgradePeriod for Windows 10, version 1511 devices.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[0-8]` |
| Default Value | 0 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DeferUpgrade |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | DeferUpgradePeriodId |

### DisableDualScan

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/DisableDualScan
```

Enable this policy to not allow update deferral policies to cause scans against Windows Update.

- If this policy is disabled or not configured, then the Windows Update client may initiate automatic scans against Windows Update while update deferral policies are enabled.

Note

This policy applies only when the intranet Microsoft update service this computer is directed to is configured to support client-side targeting. If the "Specify intranet Microsoft update service location" policy is disabled or not configured, this policy has no effect.

Note

For more information about dual scan, see [Demystifying "Dual Scan"](/en-us/archive/blogs/wsus/demystifying-dual-scan) and [Improving Dual Scan on 1607](/en-us/archive/blogs/wsus/improving-dual-scan-on-1607).

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Allow scan against Windows Update. |
| 1 | Don't allow update deferral policies to cause scans against Windows Update. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisableDualScan |
| Friendly Name | Do not allow update deferral policies to cause scans against Windows Update |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Legacy Policies |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| Registry Value Name | DisableDualScan |
| ADMX File Name | WindowsUpdate.admx |

### EngagedRestartDeadline

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/EngagedRestartDeadline
```

Enable this policy to control the timing before transitioning from Auto restarts scheduled outside of active hours to Engaged restart, which requires the user to schedule. The period can be set between 0 and 30 days from the time the restart becomes pending.

You can specify the number of days a user can snooze Engaged restart reminder notifications. The snooze period can be set between 1 and 3 days.

You can specify the deadline in days before automatically scheduling and executing a pending restart regardless of active hours. The deadline can be set between 2 and 30 days from the time the restart becomes pending. If configured, the pending restart will transition from Auto-restart to Engaged restart (pending user schedule) to automatically executed, within the specified period.

If you don't specify a deadline or if the deadline is set to 0, the PC won't automatically restart and will require the person to schedule it prior to restart.

If you disable or don't configure this policy, the PC will restart following the default schedule.

Enabling any of the following policies will override the above policy:

1. No auto-restart with logged-on users for scheduled automatic updates installations
2. Always automatically restart at scheduled time.
3. Specify deadline before auto-restart for update installation.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[2-30]` |
| Default Value | 14 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | EngagedRestartTransitionSchedule |
| Friendly Name | Specify Engaged restart transition and notification schedule for updates |
| Element Name | Deadline (days) |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Legacy Policies |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### EngagedRestartDeadlineForFeatureUpdates

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1809 [10.0.17763] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/EngagedRestartDeadlineForFeatureUpdates
```

Enable this policy to control the timing before transitioning from Auto restarts scheduled outside of active hours to Engaged restart, which requires the user to schedule. The period can be set between 0 and 30 days from the time the restart becomes pending.

You can specify the number of days a user can snooze Engaged restart reminder notifications. The snooze period can be set between 1 and 3 days.

You can specify the deadline in days before automatically scheduling and executing a pending restart regardless of active hours. The deadline can be set between 2 and 30 days from the time the restart becomes pending. If configured, the pending restart will transition from Auto-restart to Engaged restart (pending user schedule) to automatically executed, within the specified period.

If you don't specify a deadline or if the deadline is set to 0, the PC won't automatically restart and will require the person to schedule it prior to restart.

If you disable or don't configure this policy, the PC will restart following the default schedule.

Enabling any of the following policies will override the above policy:

1. No auto-restart with logged-on users for scheduled automatic updates installations
2. Always automatically restart at scheduled time.
3. Specify deadline before auto-restart for update installation.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[2-30]` |
| Default Value | 14 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | EngagedRestartTransitionSchedule |
| Friendly Name | Specify Engaged restart transition and notification schedule for updates |
| Element Name | Deadline (days) |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Legacy Policies |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### EngagedRestartSnoozeSchedule

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/EngagedRestartSnoozeSchedule
```

Enable this policy to control the timing before transitioning from Auto restarts scheduled outside of active hours to Engaged restart, which requires the user to schedule. The period can be set between 0 and 30 days from the time the restart becomes pending.

You can specify the number of days a user can snooze Engaged restart reminder notifications. The snooze period can be set between 1 and 3 days.

You can specify the deadline in days before automatically scheduling and executing a pending restart regardless of active hours. The deadline can be set between 2 and 30 days from the time the restart becomes pending. If configured, the pending restart will transition from Auto-restart to Engaged restart (pending user schedule) to automatically executed, within the specified period.

If you don't specify a deadline or if the deadline is set to 0, the PC won't automatically restart and will require the person to schedule it prior to restart.

If you disable or don't configure this policy, the PC will restart following the default schedule.

Enabling any of the following policies will override the above policy:

1. No auto-restart with logged-on users for scheduled automatic updates installations
2. Always automatically restart at scheduled time.
3. Specify deadline before auto-restart for update installation.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[1-3]` |
| Default Value | 3 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | EngagedRestartTransitionSchedule |
| Friendly Name | Specify Engaged restart transition and notification schedule for updates |
| Element Name | Snooze (days) |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Legacy Policies |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### EngagedRestartSnoozeScheduleForFeatureUpdates

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1809 [10.0.17763] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/EngagedRestartSnoozeScheduleForFeatureUpdates
```

Enable this policy to control the timing before transitioning from Auto restarts scheduled outside of active hours to Engaged restart, which requires the user to schedule. The period can be set between 0 and 30 days from the time the restart becomes pending.

You can specify the number of days a user can snooze Engaged restart reminder notifications. The snooze period can be set between 1 and 3 days.

You can specify the deadline in days before automatically scheduling and executing a pending restart regardless of active hours. The deadline can be set between 2 and 30 days from the time the restart becomes pending. If configured, the pending restart will transition from Auto-restart to Engaged restart (pending user schedule) to automatically executed, within the specified period.

If you don't specify a deadline or if the deadline is set to 0, the PC won't automatically restart and will require the person to schedule it prior to restart.

If you disable or don't configure this policy, the PC will restart following the default schedule.

Enabling any of the following policies will override the above policy:

1. No auto-restart with logged-on users for scheduled automatic updates installations
2. Always automatically restart at scheduled time.
3. Specify deadline before auto-restart for update installation.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[1-3]` |
| Default Value | 3 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | EngagedRestartTransitionSchedule |
| Friendly Name | Specify Engaged restart transition and notification schedule for updates |
| Element Name | Snooze (days) |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Legacy Policies |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### EngagedRestartTransitionSchedule

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/EngagedRestartTransitionSchedule
```

Enable this policy to control the timing before transitioning from Auto restarts scheduled outside of active hours to Engaged restart, which requires the user to schedule. The period can be set between 0 and 30 days from the time the restart becomes pending.

You can specify the number of days a user can snooze Engaged restart reminder notifications. The snooze period can be set between 1 and 3 days.

You can specify the deadline in days before automatically scheduling and executing a pending restart regardless of active hours. The deadline can be set between 2 and 30 days from the time the restart becomes pending. If configured, the pending restart will transition from Auto-restart to Engaged restart (pending user schedule) to automatically executed, within the specified period.

If you don't specify a deadline or if the deadline is set to 0, the PC won't automatically restart and will require the person to schedule it prior to restart.

If you disable or don't configure this policy, the PC will restart following the default schedule.

Enabling any of the following policies will override the above policy:

1. No auto-restart with logged-on users for scheduled automatic updates installations
2. Always automatically restart at scheduled time.
3. Specify deadline before auto-restart for update installation.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[0-30]` |
| Default Value | 7 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | EngagedRestartTransitionSchedule |
| Friendly Name | Specify Engaged restart transition and notification schedule for updates |
| Element Name | Transition (days) |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Legacy Policies |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### EngagedRestartTransitionScheduleForFeatureUpdates

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1809 [10.0.17763] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/EngagedRestartTransitionScheduleForFeatureUpdates
```

Enable this policy to control the timing before transitioning from Auto restarts scheduled outside of active hours to Engaged restart, which requires the user to schedule. The period can be set between 0 and 30 days from the time the restart becomes pending.

You can specify the number of days a user can snooze Engaged restart reminder notifications. The snooze period can be set between 1 and 3 days.

You can specify the deadline in days before automatically scheduling and executing a pending restart regardless of active hours. The deadline can be set between 2 and 30 days from the time the restart becomes pending. If configured, the pending restart will transition from Auto-restart to Engaged restart (pending user schedule) to automatically executed, within the specified period.

If you don't specify a deadline or if the deadline is set to 0, the PC won't automatically restart and will require the person to schedule it prior to restart.

If you disable or don't configure this policy, the PC will restart following the default schedule.

Enabling any of the following policies will override the above policy:

1. No auto-restart with logged-on users for scheduled automatic updates installations
2. Always automatically restart at scheduled time.
3. Specify deadline before auto-restart for update installation.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[0-30]` |
| Default Value | 7 |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | EngagedRestartTransitionSchedule |
| Friendly Name | Specify Engaged restart transition and notification schedule for updates |
| Element Name | Transition (days) |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Legacy Policies |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### IgnoreMOAppDownloadLimit

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/IgnoreMOAppDownloadLimit
```

Specifies whether to ignore the MO download limit (allow unlimited downloading) over a cellular network for apps and their updates. If lower-level limits (for example, mobile caps) are required, those limits are controlled by external policies.

Warning

Setting this policy might cause devices to incur costs from MO operators.

To validate this policy:

1. Enable the policy and ensure the device is on a cellular network.
2. Run the scheduled task on your device to check for app updates in the background. For example, on a device, run the following commands in [TShell](/en-us/windows-hardware/manufacture/desktop/factoryos/connect-using-tshell):

    ```TShell
    exec-device schtasks.exe -arguments '/run /tn "\Microsoft\Windows\WindowsUpdate\Automatic App Update" /I'
    ```

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Don't ignore MO download limit for apps and their updates. |
| 1 | Ignore MO download limit (allow unlimited downloading) for apps and their updates. |

### IgnoreMOUpdateDownloadLimit

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/IgnoreMOUpdateDownloadLimit
```

Specifies whether to ignore the MO download limit (allow unlimited downloading) over a cellular network for OS updates. If lower-level limits (for example, mobile caps) are required, those limits are controlled by external policies.

Warning

Setting this policy might cause devices to incur costs from MO operators.

To validate this policy:

1. Enable the policy and ensure the device is on a cellular network.
2. Run the scheduled task on your device to check for app updates in the background. For example, on a device, run the following commands in [TShell](/en-us/windows-hardware/manufacture/desktop/factoryos/connect-using-tshell):

    ```TShell
    exec-device schtasks.exe -arguments '/run /tn "\Microsoft\Windows\WindowsUpdate\Automatic App Update" /I'
    ```

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Don't ignore MO download limit for OS updates. |
| 1 | Ignore MO download limit (allow unlimited downloading) for OS updates. |

### PauseDeferrals

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/PauseDeferrals
```

Note

Don't use this policy for Windows 10, version 1607 or later devices. You can continue to use PauseDeferrals for Windows 10, version 1511 devices. Allows IT Admins to pause updates and upgrades for up to 5 weeks. Paused deferrals will be reset after 5 weeks. If the Specify intranet Microsoft update service location policy is enabled, then the Defer upgrades by, Defer updates by and Pause Updates and Upgrades settings have no effect. If the Allow Telemetry policy is enabled and the Options value is set to 0, then the Defer upgrades by, Defer updates by and Pause Updates and Upgrades settings have no effect.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Deferrals aren't paused. |
| 1 | Deferrals are paused. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DeferUpgrade |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | PauseDeferralsId |

### PhoneUpdateRestrictions

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/PhoneUpdateRestrictions
```

This policy is deprecated. Use Update/RequireUpdateApproval instead.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | Range: `[0-4]` |
| Default Value | 4 |

### RequireDeferUpgrade

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/RequireDeferUpgrade
```

Note

Don't use this policy for Windows 10, version 1607 or later devices. You can continue to use RequireDeferUpgrade for Windows 10, version 1511 devices. Allows the IT admin to set a device to Semi-Annual Enterprise Channel train.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | User gets upgrades from Semi-Annual Enterprise Channel (Preview). |
| 1 | User gets upgrades from Semi-Annual Enterprise Channel. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DeferUpgrade |
| Path | WindowsUpdate &gt; AT &gt; WindowsComponents &gt; WindowsUpdateCat |
| Element Name | DeferUpgradePeriodId |

### RequireUpdateApproval

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/RequireUpdateApproval
```

Note

If you previously used the Update/PhoneUpdateRestrictions policy in previous versions of Windows, it has been deprecated. Please use this policy instead. Allows the IT admin to restrict the updates that are installed on a device to only those on an update approval list. It enables IT to accept the End User License Agreement (EULA) associated with the approved update on behalf of the end-user. EULAs are approved once an update is approved.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Not configured. The device installs all applicable updates. |
| 1 | The device only installs updates that are both applicable and on the Approved Updates list. Set this policy to 1 if IT wants to control the deployment of updates on devices, such as when testing is required prior to deployment. |

### ScheduleImminentRestartWarning

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ScheduleImminentRestartWarning
```

Enable this policy to control when notifications are displayed to warn users about a scheduled restart for the update installation deadline. Users aren't able to postpone the scheduled restart once the deadline has been reached and the restart is automatically executed.

Specifies the amount of time prior to a scheduled restart to display the warning reminder to the user.

You can specify the amount of time prior to a scheduled restart to notify the user that the auto restart is imminent to allow them time to save their work.

If you disable or don't configure this policy, the default notification behaviors will be used.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 15 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 15 (Default) | 15 Minutes. |
| 30 | 30 Minutes. |
| 60 | 60 Minutes. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | RestartWarnRemind |
| Friendly Name | Configure auto-restart warning notifications schedule for updates |
| Element Name | Warning (mins) |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Legacy Policies |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### ScheduleRestartWarning

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/ScheduleRestartWarning
```

Enable this policy to control when notifications are displayed to warn users about a scheduled restart for the update installation deadline. Users aren't able to postpone the scheduled restart once the deadline has been reached and the restart is automatically executed.

Specifies the amount of time prior to a scheduled restart to display the warning reminder to the user.

You can specify the amount of time prior to a scheduled restart to notify the user that the auto restart is imminent to allow them time to save their work.

If you disable or don't configure this policy, the default notification behaviors will be used.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 4 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 2 | 2 Hours. |
| 4 (Default) | 4 Hours. |
| 8 | 8 Hours. |
| 12 | 12 Hours. |
| 24 | 24 Hours. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | RestartWarnRemind |
| Friendly Name | Configure auto-restart warning notifications schedule for updates |
| Element Name | Reminder (hours) |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Legacy Policies |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |

### SetAutoRestartNotificationDisable

Note

This is a legacy policy and isn't applicable for Windows 11. Legacy policies might be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1703 [10.0.15063] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/Update/SetAutoRestartNotificationDisable
```

This policy setting allows you to control whether users receive notifications for auto restarts for update installations including reminder and warning notifications.

Enable this policy to turn off all auto restart notifications.

If you disable or don't configure this policy, the default notification behaviors will be unchanged.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Enabled. |
| 1 | Disabled. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AutoRestartNotificationDisable |
| Friendly Name | Turn off auto-restart notifications for update installations |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Update &gt; Legacy Policies |
| Registry Key Name | Software\Policies\Microsoft\Windows\WindowsUpdate |
| ADMX File Name | WindowsUpdate.admx |