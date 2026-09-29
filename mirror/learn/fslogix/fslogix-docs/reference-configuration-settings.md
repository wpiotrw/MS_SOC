---
layout: Conceptual
title: Configuration Settings - FSLogix | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/fslogix/reference-configuration-settings
uhfHeaderId: MSDocsHeader-FSLogix
breadcrumb_path: /fslogix/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://aka.ms/avdideas
ms.service: fslogix
description: Provides the various configuration settings and descriptions used in FSLogix
author: msft-jasonparker
ms.author: japarker
ms.topic: reference
ms.date: 2025-08-26T00:00:00.0000000Z
ms.custom: sfi-ropc-nochange
locale: en-us
document_id: 01eecaa9-373c-0b07-ea97-4f818ff3a117
document_version_independent_id: 01eecaa9-373c-0b07-ea97-4f818ff3a117
original_content_git_url: https://github.com/MicrosoftDocs/fslogix-docs-pr/blob/live/fslogix-docs/reference-configuration-settings.md
site_name: Docs
depot_name: MSDN.fslogix-docs
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.fslogix-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: reference-configuration-settings
moniker_range_name: 
monikers: []
item_type: Content
source_path: fslogix-docs/reference-configuration-settings.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57ef615f-6bf1-4904-b6dc-96bb1d32c7e9
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1aea571c-6f95-42f8-b87e-c4d3aaf4bd7d
platformId: 12567974-27f3-5455-7152-3dfbde9d7c20
---

# Configuration Settings - FSLogix | Microsoft Learn

Important

An upcoming change to Windows, included in the April 2026 Windows Server update, the default Kerberos encryption type is changing from RC4 to AES-SHA1.

File shares hosting FSLogix containers that aren't upgraded to AES-SHA1 might have access issues after this change is applied. To avoid disruption, complete the upgrade to AES-SHA1 before installing the update.

Customers who have already upgraded to AES-SHA1 aren't affected.

For more information, see the FSLogix blog: [Action required: Windows Kerberos hardening (RC4) may affect FSLogix profiles on SMB storage](https://techcommunity.microsoft.com/blog/fslogix-blog/action-required-windows-kerberos-hardening-rc4-may-affect-fslogix-profiles-on-sm/4506378).

This article outlines the various registry settings applicable to FSLogix that includes, but not limited to:

- App Services
- Profile containers
- ODFC containers
- Cloud Cache
- Logging

## Default settings

After [installing](how-to-install-fslogix) FSLogix, the installer will create a base set of registry keys and values, which provides the framework for **adding** configuration settings. FSLogix doesn't create **ANY** configuration setting value names as part of the installation. Any configuration setting listed on this page which has a '**Default value**' doesn't need to be created or configured as FSLogix will automatically use the default value as listed.

For example, the `RoamIdentity` setting has a default value as '`0`'. FSLogix won't roam identity data as a default behavior and doesn't need an Administrator to create or add the registry value name and value. Only if the desire is to change the default behavior of the setting would the Administrator create or add the registry value name and value.

### Base registry keys and value names

- `[HKEY_LOCAL_MACHINE\SOFTWARE\FSLogix]`
    - `\Apps`
        - `"InstallPath"="C:\Program Files\FSLogix\Apps\"`
        - `"InstallVersion"="version_number"`
    - `\Logging`
    - `\Profiles`
    - `\SystemInfo`
    - `\Telemetry`
    - `\UserModeDll`
- [`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\FSLogix]`
    - `\ODFC`

## Custom environment variables

Some FSLogix settings accept environment variables. These settings accept the list of custom environment variables and any variables available during the user's sign in.

**FSLogix custom variables**:

| Variable | Description |
| --- | --- |
| `%username%` | SAMAcountName for the signed in user. |
| `%userdomain%` | NETBIOS domain name where the user's account resides. |
| `%sid%` | Security Identifier |
| `%osmajor%` | Major version of the operating systems as seen in: `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\CurrentMajorVersionNumber` |
| `%osminor%` | Minor version of the operating systems as seen in: `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\CurrentMinorVersionNumber` |
| `%osbuild%` | Build version of the operating systems as seen in: `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\CurrentBuildNumber` |
| `%osservicepack%` | Legacy to Windows service packs, no longer used. |
| `%profileversion%` | [Version of profile](/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj649079%28v=ws.11%29#appendix-b-profile-version-reference-information) based on Windows version. |
| `%clientname%` | The COMPUTERNAME of the client initiating the connection to the host. |

## App Services Settings

The following settings are applicable to FSLogix and not specific to profile or ODFC containers or Cloud Cache.

### CleanupInvalidSessions

**Registry Hive**: HKEY\_LOCAL\_MACHINE

**Registry Path**: SOFTWARE\FSLogix\Apps

**Value Name**: CleanupInvalidSessions

**Value Type**: DWORD

**Enabled Value**: 1

**Disabled Value**: 0 *(default)*

In cases where a user's session terminates abruptly, the VHD(x) mounted for the user's profile isn't properly detached and the user's next sign in may not successfully attach their VHD(x) container. Enable this setting and FSLogix attempts to clean up these invalid sessions and allow a successful sign-in. This setting affects both Profile and ODFC containers.

### RoamRecycleBin

**Registry Hive:** HKEY\_LOCAL\_MACHINE

**Registry Path:** SOFTWARE\FSLogix\Apps

**Value Name:** RoamRecycleBin

**Value Type:** DWORD

**Enabled Value:** 1 *(default)*

**Disabled Value:** 0

When enabled, this setting creates a redirection for the user's specific Recycle Bin into the VHD(x) container. This allows the user to restore items regardless of the machine from where they were deleted.

### VHDCompactDisk

**Registry Hive:** HKEY\_LOCAL\_MACHINE

**Registry Path:** SOFTWARE\FSLogix\Apps

**Value Name:** VHDCompactDisk

**Value Type:** DWORD

**Enabled Value:** 1 *(default)*

**Disabled Value:** 0

When enabled, this setting attempts to compact the VHD disk during the sign out operation and is designed to automatically decrease the `Size On Disk` of the user's container depending on a predefined threshold. For more information, see the [VHD Disk Compaction](concepts-vhd-disk-compaction) documentation.

## FSLogix Settings (Profile, ODFC, Cloud Cache, Logging)

# [Profile Settings](#tab/profiles)
### Profile container Settings

The following settings are applicable to profile containers and are created in the following location:

- **Registry Hive:** HKEY\_LOCAL\_MACHINE
- **Registry Path:** SOFTWARE\FSLogix\Profiles

#### AccessNetworkAsComputerObject

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: default – attach as user.
- 1: attach as computer - folder must have permissions for computer objects.

Caution

Don't use this configuration setting unless your storage provider or architecture will NOT work with user-level permissions to the VHD(x) container locations. This setting allows the virtual machine to access all the VHD(x) files on the storage provider, creating a potential security risk.

#### AttachVHDSDDL

**Type**: REG\_SZ

**Default Value**: N/A

**Data values and use**:

SDDL string representing the ACLs to use when attaching the VHD(x).

#### CleanOutNotifications

**Type**: DWORD

**Default Value**: 1

**Data values and use**:

- 0: No action.
- 1: Cleans out stale notification entries.

This setting cleans out stale entries created by the Windows Push Notification Platform (WPN) and Windows Notification Facility (WFN), which under some conditions leads to slow sign-ins.

#### DeleteLocalProfileWhenVHDShouldApply

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: No action.
- 1: Deletes local profile if it exists and matches the profile container.

Important

When FSLogix determines a user should have an FSLogix profile container, and a local profile exists, FSLogix will permanently delete the local profile.

#### DiffDiskParentFolderPath

**Type**: REG\_SZ

**Default Value**: %TEMP%

**Data values and use**:

Specifies the path where difference disks are created when **ProfileType** is configured to use them. The path supports the use of the FSLogix custom variables or any environment variables that are available to the user during the sign in process.

#### Enabled

**(required setting)**

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: Profile containers disabled.
- 1: Profile containers enabled.

#### FlipFlopProfileDirectoryName

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: SID folder is created as `%sid%_%username%`
- 1: SID folder is created as `%username%_%sid%`

Important

Be sure you understand how conflicting settings are applied and prioritized.

- This setting will *OVERRIDE* both **SIDDirNameMatch** and **SIDDirNamePattern**
- This setting has *NO EFFECT* when **NoProfileContainingFolder** is enabled
- *NoProfileContainingFolder* &gt; *FlipFlopProfileDirectoryName* &gt; (*SIDDirNameMatch and SIDDirNamePattern*)

Warning

This setting determines the profile folder name format FSLogix uses to create folders and locate user profile containers. Changing it after profile containers already exist causes FSLogix to look for profile folders using a different naming convention. When the profile folder can't be found, FSLogix creates a new profile directory and container(s). The user's original profile data is not lost and is located in the original profile folder. Recovery requires reverting the setting or manually moving the user's container to the new folder.

#### GroupPolicyState

**Type**: DWORD

**Default Value**: 1

**Data values and use**:

- 0: Don't roam Group Policy state, provides synchronous policy processing at sign-in.
- 1: Roam Group Policy state, provides asynchronous policy processing at sign-in.

Note

This setting can't be set using Group Policy.

#### IgnoreNonWVD

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: FSLogix is enabled for any session.
- 1: FSLogix is enabled for Azure Virtual Desktop (AVD) sessions only.

Note

Windows Virtual Desktop (WVD) is now known as Azure Virtual Desktop (AVD), though the name of the setting uses the legacy name.

#### InstallAppxPackages

**Type**: DWORD

**Default Value**: 1

**Data values and use**:

When enabled **(1)**, this setting reads the AppxPackages.xml manifest file from the user's profile and installs / re-registers the list of applications. The AppxPackages.xml file can be found at: `%LocalAppData%\FSLogix\AppxPackages.xml`. This setting does control the global behavior in Windows for all AppX applications. This only improves functionality when used with FSLogix.

Warning

The AppxPackages.xml file isn't meant to be edited or modified. Editing this file might cause unexpected results and the file is overwritten at each sign out.

#### IsDynamic

**Type**: DWORD

**Default Value**: 1

**Data values and use**:

- 0: VHD(x) is of a fixed size and the size on disk is fully allocated.
- 1: VHD(x) is dynamic and only increases the size on disk as necessary.

Note

- This setting is used with the **SizeInMBs** setting to manage the size of profile containers. Setting **IsDynamic** to **1** causes the Profile container to use the minimum space on disk, regardless of the allocated **SizeInMBs**. As space is consumed, the size on disk grows up to the size specified in **SizeInMBs**. **SizeInMBs** is the maximum size that a user is allowed to use on disk. If the user's profile container grows beyond what is specified in **SizeInMBs** the user experiences errors.
- Setting **IsDynamic** to **1** does NOT allow the Profile container to grow larger than what is specified in **SizeInMBs**.

#### KeepLocalDir

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: The `local_%username%` is deleted during sign out.
- 1: The `local_%username%` folder will be left on the system, after sign out. It's also used again if the same user signs on.

#### LockedRetryCount

**Type**: DWORD

**Default Value**: 12

**Data values and use**:

Specifies the number of retries attempted when a VHD(x) file is locked (open by another process or computer).

#### LockedRetryInterval

**Type**: DWORD

**Default Value**: 5

**Data values and use**:

Specifies the number of seconds to wait between retries (see LockedRetryCount).

#### NoProfileContainingFolder

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: Disabled.
- 1: Profile container doesn't use or create a SID containing folder for the VHD(x) file.

This setting is intended for situations where storage provides a location that is already unique per-user.

Important

Be sure you understand how conflicting settings are applied and prioritized.

- This setting overrides *ANY OTHER*setting related to container folders.
    - **SIDDIRNameMatch** has *NO EFFECT* when used in conjunction with this setting.
    - **SIDDIRNamePattern** has *NO EFFECT* when used in conjunction with this setting.
    - **FlipFlopProfileDirectoryName** has *NO EFFECT* when used in conjunction with this setting.

#### OutlookCachedMode

**Type**: DWORD

**Default Value**: 1

**Data values and use**:

- 0: Prevents FSLogix from doing anything with cached mode.
- 1: Only when the Profile container is attached, the Outlook setting that enables cached mode is temporarily set until the container is detached. This setting ensures cached mode is used only when the container is attached.

Important

- Outlook must be configured for online mode for this feature to work. This insures if FSLogix gets disabled, that large OST files won't be downloaded.
- Online mode registry entry: `HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\office\16.0\Outlook\OST\NoOST:DWORD = 2`.
- FSLogix overrides this setting for the current user.

#### PreventLoginWithFailure

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

When enabled **(1)** FSLogix loads the FRXShell if there's a failure attaching to, or using an existing profile VHD(x). The user receives the default prompt to call support, and the users only option is to sign out.

#### PreventLoginWithTempProfile

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

When enabled **(1)** FSLogix loads the FRXShell if it determines a temp profile has been created. The user receives the default prompt to call support, and the users only option is to sign out.

#### ProfileDirSDDL

**Type**: REG\_SZ

**Default Value**: N/A

**Data values and use**:

SDDL string representing the ACLs to use when creating the profile directory.

#### ProfileType

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: Normal profile behavior.
- 1: Machine should only be the RW profile instance.
- 2: Machine should only be the RO profile instance.
- 3: Machine should try to take the RW role and if it can't, it should fall back to a RO role.

Important

- All sessions trying to use the VHD concurrently should have a matching **ProfileType** setting for the best experience. Using various **ProfileType** values across devices requires advance knowledge of the interaction. Don't mix `0` and any other **ProfileType**. If the VHD isn't accessed concurrently, **ProfileType** should be 0.
- OneDrive doesn't support multiple simultaneous connections/multiple concurrent connections using the same profile under any circumstances. For more information, see [Use the sync app on virtual desktops](/en-us/onedrive/sync-vdi-support/).

#### ReAttachRetryCount

**Type**: DWORD

**Default Value**: 60

**Data values and use**:

Specifies the number of times the system should attempt to reattach the VHD(x) container if it disconnects unexpectedly.

#### ReAttachIntervalSeconds

**Type**: DWORD

**Default Value**: 10

**Data values and use**:

Specifies the number of seconds to wait between retries when attempting to reattach the VHD(x) container if it's disconnected unexpectedly.

#### RebootOnUserLogoff

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: Disabled.
- 1: Reboot when any user signs out.
- 2: Reboot when an FSLogix profile user signs out.

#### RedirectType

**Type**: DWORD

**Default Value**: 2

**Data values and use**:

- 1: Use legacy redirection.
- 2: Use FSLogix advanced redirection.

Caution

Don't use this setting unless directed by Microsoft Support.

#### RedirXMLSourceFolder

**Type**: REG\_SZ

**Default Value**: N/A

**Data values and use**:

Path where FSLogix looks for the redirections.xml file to copy from and into the user's profile. The path supports the use of the FSLogix custom variables or any environment variables that are available to the user during the sign in process. For example, `C:\Windows\System32` or `\\<server-name>\<share-name>`

Note

Don't add the file name to the path. This setting is a folder path only.

#### RemoveOrphanedOSTFilesOnLogoff

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: Disabled.
- 1: Duplicate OST files are deleted during sign out.

Note

In rare cases, duplicate OST files are created for a user. This circumstance has been documented to occur with and without the use of a non-persistent profile. When the profile is stored in the standard file system, administrators might remove orphaned or stale OST files by deleting them. When using FSLogix, the OST file is in the container and isn't as visible. Over long periods of time, duplicate OST files might consume incremental disk space. When enabled **(1)**, FSLogix deletes all OST files in a VHD(x), except the OST with the latest modify date. Administrators should be familiar with the use of OST files, and potential implications, before choosing to enable this setting.

#### RoamIdentity

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: Don't roam identity data. *(recommended)*
- 1: Enables legacy roaming for identity data.

Under some identity and authentication scenarios, user's may be required to authenticate to their Microsoft 365 applications at every sign-in. Enabling this setting is one way to resolve the issue. We recommend working towards true single sign-on which allows your Windows sign-in to pass its credential to your Microsoft 365 applications.

For more details, refer to our [deletion based profile exclusions](concepts-container-types#deletion-based-exclusions).

Important

- The default setting is to **not roam identity data** which is the recommended setting.
- **Do NOT enable this setting if you use Microsoft Intune to manage your devices or if your devices are Microsoft Entra joined.**

#### RoamSearch

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: Disabled.
- 1: Enable single-user search.
- 2: Enable multi-user search.

For more information, see [Configure Windows Search database roaming](how-to-configure-search-roaming).

Important

- FSLogix search roaming functionality is no longer necessary in newer versions of Windows^1^
- RoamSearch is set prior to GPOs being applied. It isn't possible to rely on GPOs to set RoamSearch in environments where a GoldImage is applied at boot.

^1 Windows Server 2019 version 1809 and later, Windows 10 and 11 multi-session^

#### SetTempToLocalPath

**Type**: DWORD

**Default Value**: 3

**Data values and use**:

- 0: Disabled.
- 1: Redirect TEMP and TMP to the local drive.
- 2: Redirect INetCache to the local drive.
- 3: Redirect TEMP, TMP, and INetCache to the local drive.

#### ShutdownOnUserLogoff

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: Disabled.
- 1: Shut down when any user signs out.
- 2: Shut down when an FSLogix user signs out.

#### SIDDirNameMatch

**Type**: REG\_SZ

**Default Value**: `%sid%_%username%`

**Data values and use**:

Specifies a string pattern used when matching a profile or ODFC container folder. Use this setting to define how FSLogix attempts to locate a user's profile or ODFC container. FSLogix uses the **VHDLocations** or **CCDLocations** as the location **where** to search and this setting defines **what** to search. The path supports the use of the FSLogix custom variables or any environment variables that are available to the user during the sign in process.

Important

Be sure you understand how conflicting settings are applied and prioritized.

- When using this configuration setting, be sure the **SIDDIRNamePattern**value matches this setting.
    - This setting has *NO EFFECT* when **FlipFlopProfileDirectoryName** is enabled.
    - This setting has *NO EFFECT* when **NoProfileContainingFolder** is enabled.
    - *NoProfileContainingFolder* &gt; *FlipFlopProfileDirectoryName* &gt; *SIDDirNameMatch* (this setting)

#### SIDDirNamePattern

**Type**: REG\_SZ

**Default Value**: `%sid%_%username%`

**Data values and use**:

Specifies a string pattern used when creating a profile or ODFC container folder. Use this setting to define how FSLogix attempts to create a user's profile or ODFC container folder. FSLogix uses the **VHDLocations** or **CCDLocations** as the location **where** to create and this setting defines **what** to create. The path supports the use of the FSLogix custom variables or any environment variables that are available to the user during the sign in process.

Important

Be sure you understand how conflicting settings are applied and prioritized.

- When using this configuration setting, be sure the **SIDDIRNameMatch**value matches this setting.
    - This setting has *NO EFFECT* when **FlipFlopProfileDirectoryName** is enabled.
    - This setting has *NO EFFECT* when **NoProfileContainingFolder** is enabled.
    - *NoProfileContainingFolder* &gt; *FlipFlopProfileDirectoryName* &gt; *SIDDirNamePattern* (this setting)

#### SIDDirSDDL

**Type**: REG\_SZ

**Default Value**: N/A

**Data values and use**:

SDDL string representing the ACLs to use when creating the SID container folder.

#### SizeInMBs

**Type**: DWORD

**Default Value**: 30000

**Data values and use**:

Specifies the maximum size of the user's container in megabytes. Newly created VHD(x) containers are of this size. Existing containers are extended automatically to this size during user sign in. You can increase this value at any time, but can't decrease it. Decreasing this value doesn't cause existing VHD(x) containers to shrink.

#### VHDNameMatch

**Type**: REG\_SZ

**Default Value**: `Profile*`

**Data values and use**:

Specifies a string pattern used when *matching* a users profile container. Use this setting to define how FSLogix attempts to *locate* a users profile container (VHD(x) file). FSLogix uses the **VHDLocations** or **CCDLocations** as the location **where** to search and this setting defines **what** to *search*. The path supports the use of the FSLogix custom variables or any environment variables that are available to the user during the sign in process.

Important

When using this configuration setting, be sure the **VHDNamePattern** value matches this setting.

#### VHDNamePattern

**Type**: REG\_SZ

**Default Value**: `Profile_%username%`

**Data values and use**:

Specifies a string pattern used when *creating* a users profile container. Use this setting to define how FSLogix attempts to *create* a users profile container (VHD(x) file). FSLogix uses the **VHDLocations** or **CCDLocations** as the location **where** to search and this setting defines **what** to *create*. The path supports the use of the FSLogix custom variables or any environment variables that are available to the user during the sign in process.

Important

When using this configuration setting, be sure the **VHDNameMatch** value matches this setting.

#### VHDLocations

**(required setting)**

**Type**: MULTI\_SZ or REG\_SZ

**Default Value**: N/A

**Data values and use**:

A list of [SMB](concepts-fslogix-terminology) locations to search for the user's profile VHD(x) file. If one isn't found, one is created in the first listed location. If the VHD path doesn't exist, it creates it before it checks if a VHD(x) exists in the path. The path supports the use of the FSLogix custom variables or any environment variables that are available to the user during the sign in process. When specified as a REG\_SZ value, multiple locations must be separated with a semi-colon (`;`).

#### VHDXSectorSize

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: Uses system default.
- 512: VHD(x) is formatted using 512-byte allocation.
- 4096: VHD(x) is formatted using 4096-byte allocation.

Caution

Don't use this setting unless directed by Microsoft Support. A mismatch in disk sector sizes can lead to a system [BSOD](concepts-fslogix-terminology).

#### VolumeType

**Type**: REG\_SZ

**Default Value**: vhd

**Data values and use**:

A value of **vhd** means that newly created files should be of type **VHD**. A value of **vhdx** means that newly created files should be of type **VHDX**.

#### VolumeWaitTimeMS

**Type**: DWORD

**Default Value**: 20000

**Data values and use**:

Specifies the number of milliseconds the system should wait for the volume to arrive after the VHD(x) attaches. Default value of 20000 = 20 seconds

# [ODFC Settings](#tab/odfc)
### ODFC container Settings

The following settings are applicable to ODFC containers and are created in the following location:

- **Registry Hive:** HKEY\_LOCAL\_MACHINE
- **Registry Path:** SOFTWARE\Policies\FSLogix\ODFC

#### AccessNetworkAsComputerObject

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: default – attach as user.
- 1: attach as computer - folder must have permissions for computer objects.

Caution

Don't use this configuration setting unless your storage provider or architecture will NOT work with user-level permissions to the VHD(x) container locations. This setting allows the virtual machine to access all the VHD(x) files on the storage provider, creating a potential security risk.

#### AttachVHDSDDL

**Type**: REG\_SZ

**Default Value**: N/A

**Data values and use**:

SDDL string representing the ACLs to use when attaching the VHD.

#### DiffDiskParentFolderPath

**Type**: REG\_SZ

**Default Value**: %TEMP%

**Data values and use**:

Specifies the path where difference disks are created when **VHDAccessMode** is configured to use them. The path supports the use of the FSLogix custom variables or any environment variables that are available to the user during the sign in process.

#### Enabled

**(required setting)**

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: ODFC containers disabled.
- 1: ODFC containers enabled

#### FlipFlopProfileDirectoryName

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: SID folder is created as `%sid%_%username%`
- 1: SID folder is created as `%username%_%sid%`

Important

Be sure you understand how conflicting settings are applied and prioritized.

- This setting will *OVERRIDE* both **SIDDirNameMatch** and **SIDDirNamePattern**
- This setting has *NO EFFECT* when **NoProfileContainingFolder** is enabled
- *NoProfileContainingFolder* &gt; *FlipFlopProfileDirectoryName* &gt; (*SIDDirNameMatch and SIDDirNamePattern*)

Warning

This setting determines the profile folder name format FSLogix uses to create folders and locate user profile containers. Changing it after profile containers already exist causes FSLogix to look for profile folders using a different naming convention. When the profile folder can't be found, FSLogix creates a new profile directory and container(s). The user's original profile data is not lost and is located in the original profile folder. Recovery requires reverting the setting or manually moving the user's container to the new folder.

#### IgnoreNonWVD

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: FSLogix is enabled for any session.
- 1: FSLogix is enabled for Azure Virtual Desktop (AVD) sessions only.

Note

Windows Virtual Desktop (WVD) is now known as Azure Virtual Desktop (AVD), though the name of the setting uses the legacy name.

#### IncludeOfficeActivation

**Type**: DWORD

**Default Value**: 1

**Data values and use**:

- 0: Office activation data isn't redirected to the container.
- 1: Office activation data is redirected to the container.

Note

This setting is specific to Office 2016 and later

#### IncludeOneDrive

**Type**: DWORD

**Default Value**: 1

**Data values and use**:

- 0: OneDrive cache isn't redirected to the container.
- 1: OneDrive cache is redirected to the container.

Important

OneDrive doesn't support multiple simultaneous connections / multiple concurrent connections, using the same profile, under any circumstances. For more information, see [Use the sync app on virtual desktops](/en-us/onedrive/sync-vdi-support/).

#### IncludeOneNote

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: OneNote notebook files aren't redirected to the container.
- 1: OneNote notebook files are redirected to the container.

#### IncludeOneNote\_UWP

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: OneNote UWP notebook files aren't redirected to the container.
- 1: OneNote UWP notebook files are redirected to the container.

#### IncludeOutlook

Important

- The `IncludeOutlook` setting supports both *classic* and [Microsoft Outlook for Windows](/en-us/microsoft-365-apps/outlook/get-started/virtualized-desktop-infrastructure).
- The `IncludeOutlook` setting only applies to ODFC container configurations.

**Type**: DWORD

**Default Value**: 1

**Data values and use**:

- 0: Outlook data isn't redirected to the container.
- 1: Outlook data is redirected to the container.

Note

Microsoft Outlook profile data redirection paths.

Outlook (*classic*):

- `%AppData%\Roaming\Microsoft\Outlook`
- `%AppData%\Local\Microsoft\Outlook`

Outlook for Windows (**new**):

- `%LocalAppData%\Packages\Microsoft.OutlookForWindows_8wekyb3d8bbwe\`
- `%LocalAppData%\Microsoft\olk`

#### IncludeOutlookPersonalization

Note

The `IncludeOutlookPersonalization` setting does **NOT** apply to [Microsoft Outlook for Windows](/en-us/microsoft-365-apps/outlook/get-started/virtualized-desktop-infrastructure).

**Type**: DWORD

**Default Value**: 1

**Data values and use**:

- 0: Outlook personalization data isn't redirected to the container.
- 1: Outlook personalization data is redirected to the container.

#### IncludeSharepoint

**Type**: DWORD

**Default Value**: 1

**Data values and use**:

- 0: Sharepoint data isn't redirected to the container.
- 1: Sharepoint data is redirected to the container.

#### IncludeSkype

**Type**: DWORD

**Default Value**: 1

**Data values and use**:

- 0: Skype for Business Global Address List isn't redirected to the container.
- 1: Skype for Business Global Address List is redirected to the container.

#### IncludeTeams

Important

The `IncludeTeams` setting is for both *classic* and **new** Microsoft Teams.

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: Teams data isn't redirected to the ODFC container and **new** Teams AppX package isn't registered during sign-in.
- 1: Teams data is redirected to the ODFC container and **new** Teams AppX package is registered by family name during sign-in.

Note

Microsoft Teams profile data redirection paths.

Teams (*classic*):

- `%AppData%\Local\Microsoft\Teams`
- `%AppData%\Roaming\Microsoft\Teams`

Teams (**new**):

- `%LocalAppData%\Packages\MSTeams_8wekyb3d8bbwe\LocalCache`

#### IsDynamic

**Type**: DWORD

**Default Value**: 1

**Data values and use**:

- 0: VHD(x) is of a fixed size and the size on disk is fully allocated.
- 1: VHD(x) is dynamic and only increases the size on disk as necessary.

Note

- This setting is used with the **SizeInMBs** setting to manage the size of ODFC containers. Setting **IsDynamic** to **1** causes the ODFC container to use the minimum space on disk, regardless of the allocated **SizeInMBs**. As space is consumed, the size on disk grows up to the size specified in **SizeInMBs**. **SizeInMBs** is the maximum size that a user is allowed to use on disk. If the user's ODFC container grows beyond what is specified in **SizeInMBs** the user experiences errors.
- Setting **IsDynamic** to **1** does NOT allow the ODFC container to grow larger than what is specified in **SizeInMBs**.

#### LockedRetryCount

**Type**: DWORD

**Default Value**: 12

**Data values and use**:

Specifies the number of retries attempted when a VHD(x) file is locked (open by another process or computer).

#### LockedRetryInterval

**Type**: DWORD

**Default Value**: 5

**Data values and use**:

Specifies the number of seconds to wait between retries (see LockedRetryCount).

#### MirrorLocalOSTToVHD

Note

The `MirrorLocalOSTToVHD` setting does **NOT** apply to [Microsoft Outlook for Windows](/en-us/microsoft-365-apps/outlook/get-started/virtualized-desktop-infrastructure).

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: Disabled.
- 1: When a new VHD is created and there are contents in the local OST folder, they're copied to the VHD before the user is given access.
- 2: When a new VHD is created and there are contents in the local OST folder, they're moved to the VHD before the user is given access.

#### NoProfileContainingFolder

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: Disabled.
- 1: ODFC container doesn't use or create a SID containing folder for the VHD(x) file.

This setting is intended for situations where storage provides a location that is already unique per-user.

Important

Be sure you understand how conflicting settings are applied and prioritized.

- This setting will override *ANY OTHER*setting related to container folders.
    - **SIDDIRNameMatch** has *NO EFFECT* when used in conjunction with this setting.
    - **SIDDIRNamePattern** has *NO EFFECT* when used in conjunction with this setting.
    - **FlipFlopProfileDirectoryName** has *NO EFFECT* when used in conjunction with this setting.

#### NumSessionVHDsToKeep

**Type**: DWORD

**Default Value**: 2

**Data values and use**:

This setting is used when **VHDAccessMode** is set to **(3)**. This controls the number of session VHDs that are persistent. For example, if set to **(2)** and the user creates a third session, a new session VHD is created, but it's deleted when the third session ends.

#### OutlookCachedMode

Note

The `OutlookCachedMode` setting does **NOT** apply to [Microsoft Outlook for Windows](/en-us/microsoft-365-apps/outlook/get-started/virtualized-desktop-infrastructure).

**Type**: DWORD

**Default Value**: 1

**Data values and use**:

- 0: Prevents FSLogix from doing anything with cached mode.
- 1: Only when the ODFC container is attached, the Outlook setting that enables cached mode is temporarily set until the container is detached. This setting ensures cached mode is used only when the container is attached.

Important

- Outlook must be configured for online mode for this feature to work. This insures if FSLogix gets disabled, that large OST files won't be downloaded.
- Online mode registry entry: `HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\office\16.0\Outlook\OST\NoOST:DWORD = 2`.
- FSLogix will override this setting for the current user.

#### OutlookFolderPath

Note

The `OutlookFolderPath` setting does **NOT** apply to [Microsoft Outlook for Windows](/en-us/microsoft-365-apps/outlook/get-started/virtualized-desktop-infrastructure).

**Type**: REG\_SZ

**Default Value**: `%userprofile%\AppData\Local\Microsoft\Outlook`

**Data values and use**:

The path to the user's Outlook folder. The path supports the use of the FSLogix custom variables or any environment variables that are available to the user during the sign in process.

#### PreventLoginWithFailure

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

When enabled **(1)** FSLogix loads the FRXShell if there's a failure attaching to, or using an existing ODFC VHD(x). The user receives the default prompt to call support, and the users only option is to sign out.

#### PreventLoginWithTempProfile

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

When enabled **(1)** FSLogix loads the FRXShell if it's determined a temp profile has been created. The user receives the default prompt to call support, and the users only option is to sign out.

#### ReAttachRetryCount

**Type**: DWORD

**Default Value**: 60

**Data values and use**:

Specifies the number of times the system should attempt to reattach the VHD(x) container if it's disconnected unexpectedly.

#### ReAttachIntervalSeconds

**Type**: DWORD

**Default Value**: 10

**Data values and use**:

Specifies the number of seconds to wait between retries when attempting to reattach the VHD(x) container if disconnects unexpectedly.

#### RedirectType

**Type**: DWORD

**Default Value**: 2

**Data values and use**:

- 1: Use legacy redirection.
- 2: Use FSLogix advanced redirection.

Caution

Do not use this setting unless directed by Microsoft Support.

#### RefreshUserPolicy

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: Disabled.
- 1: ODFC container overwrites the previous user setting with the GPO setting.

If a GPO is configured for an Office Product that is included in ODFC container, there may be a conflict with a previous user setting. Standard behavior is for the GPO to be applied, but when the ODFC container is read, the GPO is overwritten using the setting in ODFC container. If the desire is for the GPO change to be universally applied, then this setting should be set to 1 prior to the GPO update being applied.

Important

There's a performance implication to setting RefreshUserPolicy to 1. RefreshUserPolicy shouldn't be set, or should be set to 0, unless there's a specific GPO event. After the GPO event, the setting should be reverted to default.

#### RemoveOrphanedOSTFilesOnLogoff

Note

The `RemoveOrphanedOSTFilesOnLogoff` setting does **NOT** apply to [Microsoft Outlook for Windows](/en-us/microsoft-365-apps/outlook/get-started/virtualized-desktop-infrastructure).

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: Disabled.
- 1: Duplicate OST files are deleted during sign out.

Note

In rare cases, duplicate OST files are created for a user. This circumstance has been documented to occur with and without the use of a non-persistent profile. When the profile is stored in the standard file system, administrators may remove orphaned or stale OST files by deleting them. When using FSLogix the OST file is in the container and isn't as visible. Over long periods of time, duplicate OST files may consume incremental disk space. When enabled **(1)** FSLogix deletes all OST files in a VHD(x), except the OST with the latest modify date. Administrators should be familiar with the use of OST files, and potential implications, before choosing to enable this setting.

#### RoamSearch

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: Disabled.
- 1: Enable single-user search.
- 2: Enable multi-user search.

For more information, see [Configure Windows Search database roaming](how-to-configure-search-roaming).

Important

- FSLogix search roaming functionality is no longer necessary in newer versions of Windows^1^
- RoamSearch is set prior to GPOs being applied. It isn't possible to rely on GPOs to set RoamSearch in environments where a GoldImage is applied at boot.

^1 Windows Server 2019 version 1809 and later, Windows 10 and 11 multi-session^

#### SIDDirNameMatch

**Type**: REG\_SZ

**Default Value**: `%sid%_%username%`

**Data values and use**:

Specifies a string pattern used when matching a profile or ODFC container folder. Use this setting to define how FSLogix attempts to locate a user's profile or ODFC container. FSLogix uses the **VHDLocations** or **CCDLocations** as the location **where** to search and this setting defines **what** to search. The path supports the use of the FSLogix custom variables or any environment variables that are available to the user during the sign in process.

Important

Be sure you understand how conflicting settings are applied and prioritized.

- When using this configuration setting, be sure the **SIDDIRNamePattern**value matches this setting.
    - This setting has *NO EFFECT* when **FlipFlopProfileDirectoryName** is enabled.
    - This setting has *NO EFFECT* when **NoProfileContainingFolder** is enabled.
    - *NoProfileContainingFolder* &gt; *FlipFlopProfileDirectoryName* &gt; *SIDDirNameMatch* (this setting)

#### SIDDirNamePattern

**Type**: REG\_SZ

**Default Value**: `%sid%_%username%`

**Data values and use**:

Specifies a string pattern used when creating a profile or ODFC container folder. Use this setting to define how FSLogix attempts to create a user's profile or ODFC container folder. FSLogix uses the **VHDLocations** or **CCDLocations** as the location **where** to create and this setting defines **what** to create. The path supports the use of the FSLogix custom variables or any environment variables that are available to the user during the sign in process.

Important

Be sure you understand how conflicting settings are applied and prioritized.

- When using this configuration setting, be sure the **SIDDIRNameMatch**value matches this setting.
    - This setting has *NO EFFECT* when **FlipFlopProfileDirectoryName** is enabled.
    - This setting has *NO EFFECT* when **NoProfileContainingFolder** is enabled.
    - *NoProfileContainingFolder* &gt; *FlipFlopProfileDirectoryName* &gt; *SIDDirNamePattern* (this setting)

#### SIDDirSDDL

**Type**: REG\_SZ

**Default Value**: N/A

**Data values and use**:

SDDL string representing the ACLs to use when creating the SID container folder.|

#### SizeInMBs

**Type**: DWORD

**Default Value**: 30000

**Data values and use**:

Specifies the maximum size of the user's container in megabytes. Newly created VHD(x) containers are of this size. Existing containers are extended automatically to this size during user sign in. You can increase this value at any time, but can't decrease it. Decreasing this value doesn't cause existing VHD(x) containers to shrink.

#### VHDAccessMode

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: Normal direct access behavior. This is the simplest access model, but only allows one concurrent session.
- 1: A difference disk is used on the network. This allows for simultaneous session access. This mode shouldn't be used if the ODFC container is being used with Outlook Cached Exchange mode.
- 2: A difference disk is used on the local machine. This allows for simultaneous session access. This mode shouldn't be used if the ODFC container is being used with Outlook Cached Exchange mode.
- 3: A unique VHD(x) is used for each concurrent session. These VHD(x) files will typically persist so that they can be used the next time a user creates a session.

To control the number of VHD(x) files that persist, see the NumSessionVHDsToKeep setting.

Important

- All sessions trying to use the VHD concurrently must have a matching **VHDAccessMode** setting. If the VHD isn't accessed concurrently, **VHDAccessMode** should be 0.
- If the ODFC container is being used with Outlook cache mode, **VHDAccessMode** 0 or 3 must be used.
- OneDrive doesn't support multiple simultaneous connections / multiple concurrent connections, using the same profile, under any circumstances. For more information, see [Use the sync app on virtual desktops](/en-us/onedrive/sync-vdi-support/).

#### VHDNameMatch

**Type**: REG\_SZ

**Default Value**: `ODFC*`

**Data values and use**:

Specifies a string pattern used when *matching* a users ODFC container. Use this setting to define how FSLogix attempts to *locate* a users ODFC container (VHD(x) file). FSLogix uses the **VHDLocations** or **CCDLocations** as the location **where** to search and this setting defines **what** to *search*. The path supports the use of the FSLogix custom variables or any environment variables that are available to the user during the sign in process.

Important

When using this configuration setting, be sure the **VHDNamePattern** value matches this setting.

#### VHDNamePattern

**Type**: REG\_SZ

**Default Value**: `ODFC_%username%`

**Data values and use**:

Specifies a string pattern used when *creating* a users ODFC container. Use this setting to define how FSLogix attempts to *create* a users ODFC container (VHD(x) file). FSLogix uses the **VHDLocations** or **CCDLocations** as the location **where** to search and this setting defines **what** to *create*. The path supports the use of the FSLogix custom variables or any environment variables that are available to the user during the sign in process.

Important

When using this configuration setting, be sure the **VHDNameMatch** value matches this setting.

#### VHDLocations

**(required setting)**

**Type**: MULTI\_SZ or REG\_SZ

**Default Value**: N/A

**Data values and use**:

A list of [SMB](concepts-fslogix-terminology) locations to search for the user's ODFC VHD(x) file. If one isn't found, one is created in the first listed location. If the VHD path doesn't exist, it creates it before it checks if a VHD(x) exists in the path. The path supports the use of the FSLogix custom variables or any environment variables that are available to the user during the sign in process. When specified as a REG\_SZ value, multiple locations must be separated with a semi-colon (`;`).

#### VHDXSectorSize

**Type**: DWORD

**Data values and use**:

- 0: Uses system default.
- 512: VHD(x) is formatted using 512-byte allocation.
- 4096: VHD(x) is formatted using 4096-byte allocation.

Note

Values are listed in decimal not hex.

#### VolumeType

**Type**: REG\_SZ

**Default Value**: vhd

**Data values and use**:

A value of `vhd` means that newly created files should be of type `VHD`. A value of `vhdx` means that newly created files should be of type `VHDX`.

#### VolumeWaitTimeMS

**Type**: DWORD

**Default Value**: 20000

**Data values and use**:

Specifies the number of milliseconds the system should wait for the volume to arrive after the VHD(x) attaches. Default value of 20000 = 20 seconds

# [Cloud Cache Settings](#tab/ccd)
### Cloud Cache Settings

The following settings are applicable to Cloud Cache configurations.

### Global Cloud Cache Settings

The following configuration settings are Cloud Cache specific and are used for **ALL** Cloud Cache implementations whether applied to Profile or ODFC containers.

#### CacheDirectory

**Registry Hive:** HKEY\_LOCAL\_MACHINE

**Registry Path:** SYSTEM\CurrentControlSet\Services\frxccd\Parameters

**Value Name:** CacheDirectory

**Value Type:** REG\_SZ

**Default Value:**`C:\ProgramData\FSLogix\Cache`

**Data values and use**:

This value specifies the location of the local cache VHD(x).

Important

- **CacheDirectory** and **ProxyDirectory** MUST NOT be the same location as the Proxy File and the Cache File are the same name and will conflict.
- It's critical to locate the local cache VHD(x) on storage that is highly available and high performing. Storage that is appropriate for the local cache VHD(x) will have performance and availability characteristics similar to SSD or NVMe attached storage. **CacheDirectory** is set prior to Group Policy being applied. It isn't possible to rely on Group Policy to set **CacheDirectory** in environments where a "gold image" is applied at boot.

#### WriteCacheDirectory

**Registry Hive:** HKEY\_LOCAL\_MACHINE

**Registry Path:** SYSTEM\CurrentControlSet\Services\frxccds\Parameters

**Value Name:** WriteCacheDirectory

**Value Type:** REG\_SZ

**Default Value**: `C:\ProgramData\FSLogix\Cache`

**Data values and use**:

This setting specifies where the files are located that control what data needs to be written to the **CCDLocations**. These files contain a list of sectors that need to be written to the **CCDLocations**. For each set, the data is read from the local cache VHD(x) in the **CacheDirectory** then written to the **CCDLocations**. Each location has its own write cache list since they may flush at different speeds.

#### ProxyDirectory

**Registry Hive:** HKEY\_LOCAL\_MACHINE

**Registry Path:** SYSTEM\CurrentControlSet\Services\frxccds\Parameters

**Value Name:** ProxyDirectory

**Value Type:** REG\_SZ

**Default Value**: `C:\ProgramData\FSLogix\Proxy`

**Data values and use**:

Specifies the location of the local proxy stub file.

Important

- **CacheDirectory** and **ProxyDirectory** MUST NOT be the same location as the Proxy File and the Cache File are the same name and will conflict.
- Although it's possible to change the location of the **ProxyDirectory** setting, it's strongly recommended that this is only done when there is no C drive.
- This location contains no data.

#### SilenceACLWarning

**Registry Hive:** HKEY\_LOCAL\_MACHINE

**Registry Path:** SYSTEM\CurrentControlSet\Services\frxccds\Parameters

**Value Name:** SilenceACLWarning

**Value Type:** DWORD

**Default Value**: 0

**Data values and use**:

- 0: Disabled.
- 1: Disables the event log warning when the proxy or cache ACLs don't match the default values.

### Container Specific Settings

A Cloud Cache configuration may be used for Profile and / or ODFC container(s).

- **Profiles Registry Key**: HKLM\SOFTWARE\FSLogix\Profiles
- **ODFC Registry Key**: HKLM\SOFTWARE\Policies\FSLogix\ODFC

Important

- **CCDLocations** and **VHDLocations** must not both be present at the same time.
- Cloud Cache settings are only valid when used with **CCDLocations** in either profiles or ODFC configurations.

#### CCDLocations

**(Required Setting)**

**Type**: REG\_SZ / MULTI\_SZ

**Default Value**: N/A

**Data values and use**:

Specifies the storage type and location of Cloud Cache remote containers. **CCDLocations** should be used instead of **VHDLocations**. **CCDLocations** supports SMB and Azure Blob types with up to four remote container locations. When setting **CCDLocations**, the first location is the primary storage provider and is the only provider used for read operations, unless it becomes unhealthy. All storage providers are used when content needs to be written to the VHD(x) files.

Tip

- Don't use spaces around delimiters.
- Parameters and values are case sensitive.
    - **For example:**
    - `type=smb` (**correct**)
    - `type=SMB` (incorrect)
    - `connectionString=\\<server-name-1>\<share-name>` (**correct**)
    - `connectionstring=\\<server-name-1>\<share-name>` (incorrect)

**CCDLocations** are formatted using a type, name, and connectionString separated using a `;` as the delimiter. The type accepts either `smb` or `azure`. Name is an optional value used to describe the storage provider. Use `"` when the name contains a `space`. The connectionString for `smb` type must include the full UNC path to the file share. The connectionString for `azure` type must include the name of the [protected key](how-to-protect-connection-string).

- CCDLocations using SMB: `type=smb,name="SMB PROVIDER 1",connectionString=\\<server-name-1>\<share-name>`
- CCDLocations using Azure (**secure**): `type=azure,name="AZURE BLOB 1",connectionString="|fslogix/azureblob1|"`

Caution

Don't use the plain-text connectionString for Azure page blob storage providers. For more information, see [Tutorial: Configure profile containers with Cloud Cache](tutorial-cloud-cache-containers) and [Protect Azure page blob connection string](how-to-protect-connection-string).

#### CcdMaxCacheSizeInMBs (retired)

Important

This setting has been retired as of February 11, 2025 and is no longer supported. Please review the [**feature deprecation**](troubleshooting-feature-deprecation) page for additional information.

#### ClearCacheOnLogoff

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

By default, the local cache VHD(x) isn't removed when the user signs out. If a user accesses a system where it's desirable to have the local cache VHD(x) deleted when they sign out, set this value to **1**.

#### Cloud Cache provider registration settings overview

Caution

Please read the following section before attempting to use these settings.

Traditionally, Cloud Cache had rigid behavior when all defined providers weren't available at user sign-in and sign out. Specifically, users would never trigger an error during sign-in, even if no Cloud Cache providers were available. Also, at sign out, if any Cloud Cache provider wasn't available the user's sign out would be prevented indefinitely. In most scenarios, where Cloud Cache providers point to highly available storage that would rarely, if ever, be unavailable for extended periods, these settings are ideal for insuring data integrity. In some scenarios, users have expressed a desire for more granular control over these behaviors. The following settings allow configuration of Cloud Cache behavior during disk register (associated with user sign-in) and disk unregister (associated with user sign out) events. When configuring any settings associated with disk register or unregister events, verify that you're familiar with the concepts, and that the configurations achieve your data integrity goals. Various setting combinations could cause local profile data to be discarded with no Cloud Cache providers being updated. The result of clearing the local cache, without flushing to a Cloud Cache provider, is the permanent deletion of the user's session data stored in the local cache.

The following settings may be used, with Profile container and/or ODFC container when using Cloud Cache.

#### HealthyProvidersRequiredForRegister

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

Defines the number of required 'healthy' storage providers necessary for a successful user sign-in. When set to **0**, users are always allowed to sign in even if no Cloud Cache providers are available.

This setting specifies the number of healthy Cloud Cache providers required to allow a sign-in. If a user signs in with no available providers, FSLogix assumes that one or more Cloud Cache providers become available prior to the user signing out. If a Cloud Cache provider doesn't become available during the time of the user session, then the user is prevented from signing out (*discussed in HealthyProviderRequiredForUnregister*). If it's desired to block a user from signing in and a minimum number of Cloud Cache providers aren't available, the **HealthyProvidersRequiredForRegister** may be set to the number of providers required for a sign-in. If the minimum number of providers required for registration aren't available, then the sign-in fails. When setting **HealthyProvidersRequiredForRegister** to anything other than **0**, then **PreventLoginWithFailure** and / or **PreventLoginWithTempProfile** should be used in order to create the desired user experience.

#### HealthyProvidersRequiredForUnregister

**Type**: DWORD

**Default Value**: 1

**Data values and use**:

Defines the number of required 'healthy' storage providers necessary for a successful user sign out. If the number of available providers at sign out is less than the number set, the user's sign out is prevented for the time specified in **CcdUnregisterTimeout**.

Note

Although **HealthyProvidersRequiredForUnregister** may be set to **0**, it is *NOT* recommended. When set to **0**, **ClearCacheOnForcedUnregister** and **CcdUnregisterTimeout** will have *NO EFFECT*. Setting the value to **0** may cause the permanent deletion of the user session data stored in the local cache, without the protections built in through **CcdUnregisterTimeout** and **ClearCacheOnForcedUnregister**.

#### CcdUnregisterTimeout

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: The user sign out is held until the number of providers specified in **HealthyProvidersRequiredForUnregister** are available.

Change the value to the number of seconds a user's sign out is delayed if the number of available providers is less than the value specified in **HealthyProvidersRequiredForUnregister**.

Caution

When set to **0** and the number of providers specified in **HealthyProvidersRequiredForUnregister** is not met, then the user's sign out may be held infinitely.

#### ClearCacheOnForcedUnregister

**Type**: DWORD

**Default Value**: 0

**Data values and use**:

- 0: Retains the local cache when the storage provider is unregistered when the **CcdUnregisterTimeout** expires.
- 1: Removes all local cache when the storage provider is unregistered when the **CcdUnregisterTimeout** expires.

CCDUnregisterTimeout is set to specify the number of seconds to wait prior to allowing a user session to be closed, even if a successful flush to a Cloud Cache provider hasn't occurred. If ClearCacheOnLogoff is set, the local cache is deleted, even if the data in the local cache hasn't been flushed to a Cloud Cache provider. To preserve the user data in the local cache, when a user session is forced to close, local cache is NOT deleted in this scenario (*Even if ClearCacheOnLogoff is set*). This allows user data to be recovered from the local cache, however the local cache VHD(x) must then be managed (deleted) manually after user data is restored.

Caution

Setting **ClearCacheOnForcedUnregister** to **1** may result in user data saved in the registry during the current session to be lost. It is important to understand that this data isn't recoverable if the local cache is cleared in this scenario. Verify that you understand the implications of changing the default value of this setting prior to making changes.

# [Log Settings](#tab/logging)
### Log Settings

Note

A new install (or an install after an uninstall) will reset the logging levels back to default. An upgrade install will leave all logging settings as they exist before the upgrade install.

The following settings are applicable to FSLogix and not specific to Profile or ODFC containers or Cloud Cache. The settings are created in the following location:

- **Registry Hive:** HKEY\_LOCAL\_MACHINE
- **Registry Path:** SOFTWARE\FSLogix\Logging

#### LoggingEnabled

**Value Name**: LoggingEnabled

**Value Type**: REG\_DWORD

**Default Value**: 2

When set to **'0'**, the specific settings for each log file are ignored and all log files are disabled. When set to **'1'** Only Component-specific logs are created. When set to **'2'**, the specific settings for each log file are ignored and all log files are enabled.

#### LogDir

**Value Name**: LogDir

**Value Type**: REG\_SZ

**Default Value**: %ProgramData%\FSLogix\Logs

Specifies the location where log files should be stored. Local and UNC paths are accepted. Logging is done as SYSTEM when logging to a local drive, and as the Computer Object when logging to a network share. **When configuring logging to a network share, be sure to grant access for the Computer Object to the network share and the folder.**

Note

Changing the location of the log file, it is required to reboot the system or restart the FSLogix Service.

#### LogFileKeepingPeriod

**Value Name**: LogFileKeepingPeriod

**Value Type**: REG\_DWORD

**Default Value**: 2

**Max Value**: 180

A new log file is created each day. This specifies how many to keep.

#### LoggingLevel

**Value Name**: LoggingLevel

**Value Type**: REG\_DWORD

**Default Value**: 1

- 0: Verbose log file output that includes DBG, INFO, WARN, and ERROR messages.
- 1: **Default** log file output that includes: INFO, WARN, and ERROR messages.
- 2: Minimal log file output that includes: WARN and ERROR messages.
- 3: Errors only log file output.

#### RobocopyLogPath

**Value Name**: RobocopyLogPath

**Value Type**: REG\_SZ

**Default Value**: None

Specifies a log file name and path where the output of the robocopy commands (for example, during mirroring of data in or out of a VHD) are stored. If the value is nonexistent, then the robocopy results aren't logged at all. This setting is recommended for troubleshooting only.

### Component-specific log files

These settings are only applicable if the LoggingEnabled setting is set to **1**.

#### ConfigTool

**Value Name**: ConfigTool

**Value Type**: REG\_DWORD

**Enable Value**: 1 *(default)*

**Disabled Value**: 0

#### IEPlugin

**Value Name**: IEPlugin

**Value Type**: REG\_DWORD

**Enable Value**: 1

**Disabled Value**: 0 *(default)*

#### RuleEditor

**Value Name**: RuleEditor

**Value Type**: REG\_DWORD

**Enable Value**: 1

**Disabled Value**: 0 *(default)*

#### JavaRuleEditor

**Value Name**: JavaRuleEditor

**Value Type**: REG\_DWORD

**Enable Value**: 1

**Disabled Value**: 0 *(default)*

#### Service

**Value Name**: Service

**Value Type**: REG\_DWORD

**Enable Value**: 1

**Disabled Value**: 0 *(default)*

#### Profile

**Value Name**: Profile

**Value Type**: REG\_DWORD

**Enable Value**: 1 *(default)*

**Disabled Value**: 0

#### FrxLauncher

**Value Name**: FrxLauncher

**Value Type**: REG\_DWORD

**Enable Value**: 1

**Disabled Value**: 0 *(default)*

#### ODFC

**Value Name**: ODFC

**Value Type**: REG\_DWORD

**Enable Value**: 1

**Disabled Value**: 0 *(default)*

#### RuleCompilation

**Value Name**: RuleCompilation

**Value Type**: REG\_DWORD

**Enable Value**: 1

**Disabled Value**: 0 *(default)*

#### Font

**Value Name**: Font

**Value Type**: REG\_DWORD

**Enable Value**: 1

**Disabled Value**: 0 *(default)*

#### Network

**Value Name**: Network

**Value Type**: REG\_DWORD

**Enable Value**: 1

**Disabled Value**: 0 *(default)*

#### Printer

**Value Name**: Printer

**Value Type**: REG\_DWORD

**Enable Value**: 1

**Disabled Value**: 0 *(default)*

#### AdsComputerGroup

**Value Name**: AdsComputerGroup

**Value Type**: REG\_DWORD

**Enable Value**: 1

**Disabled Value**: 0 *(default)*

#### DriverInterface

**Value Name**: DriverInterface

**Value Type**: REG\_DWORD

**Enable Value**: 1

**Disabled Value**: 0 *(default)*

#### Search

**Value Name**: Search

**Value Type**: REG\_DWORD

**Enable Value**: 1 *(default)*

**Disabled Value**: 0

#### SearchPlugin

**Value Name**: SearchPlugin

**Value Type**: REG\_DWORD

**Enable Value**: 1

**Disabled Value**: 0 *(default)*

#### ProcessStart

**Value Name**: ProcessStart

**Value Type**: REG\_DWORD

**Enable Value**: 1

**Disabled Value**: 0 *(default)*

---