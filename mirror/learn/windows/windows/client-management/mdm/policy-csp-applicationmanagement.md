---
layout: Conceptual
title: ApplicationManagement Policy CSP | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-applicationmanagement
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
description: Learn more about the ApplicationManagement Area in Policy CSP.
ms.date: 2026-02-27T00:00:00.0000000Z
locale: en-us
document_id: 64ac43f2-2742-087b-1512-1dd0f4e469e4
document_version_independent_id: f52b9d2b-c877-c18a-fd45-3a47e4c39e29
original_content_git_url: https://github.com/MicrosoftDocs/windows-docs-pr/blob/live/windows/client-management/mdm/policy-csp-applicationmanagement.md
site_name: Docs
depot_name: TechNet.win-client-management
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/TechNet.win-client-management/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: mdm/policy-csp-applicationmanagement
moniker_range_name: 
monikers: []
item_type: Content
source_path: windows/client-management/mdm/policy-csp-applicationmanagement.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/cd440f3c-1b78-40a7-97ba-aa00a1d79df7
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c828f7e0-89b4-459c-9bae-d7ab1c4bd9ad
platformId: 33ff52a9-4a31-6c77-91cb-1b8b26111b0f
---

# ApplicationManagement Policy CSP | Microsoft Learn

Tip

This CSP contains ADMX-backed policies which require a special SyncML format to enable or disable. You must specify the data type in the SyncML as `<Format>chr</Format>`. For details, see [Understanding ADMX-backed policies](../understanding-admx-backed-policies).

The payload of the SyncML must be XML-encoded; for this XML encoding, there are a variety of online encoders that you can use. To avoid encoding the payload, you can use CDATA if your MDM supports it. For more information, see [CDATA Sections](http://www.w3.org/TR/REC-xml/#sec-cdata-sect).

![Logo of Windows Insider.](images/insider.png)

Important

This CSP contains some settings that are under development and only applicable for [Windows Insider Preview builds](/en-us/windows-insider/). These settings are subject to change and may have dependencies on other features or services in preview.

## AllowAllTrustedApps

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/AllowAllTrustedApps
```

This policy setting allows you to manage the installation of trusted line-of-business (LOB) or developer-signed packaged Microsoft Store apps.

- If you enable this policy setting, you can install any LOB or developer-signed packaged Microsoft Store app (which must be signed with a certificate chain that can be successfully validated by the local computer).
- If you disable or don't configure this policy setting, you can't install LOB or developer-signed packaged Microsoft Store apps.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 65535 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Explicit deny. |
| 1 | Explicit allow unlock. |
| 65535 (Default) | Not configured. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AppxDeploymentAllowAllTrustedApps |
| Friendly Name | Allow all trusted apps to install |
| Location | Computer Configuration |
| Path | Windows Components &gt; App Package Deployment |
| Registry Key Name | Software\Policies\Microsoft\Windows\Appx |
| Registry Value Name | AllowAllTrustedApps |
| ADMX File Name | AppxPackageManager.admx |

## AllowAppStoreAutoUpdate

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/AllowAppStoreAutoUpdate
```

Specifies whether automatic update of apps from Microsoft Store are allowed. Most restricted value is 0.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 2 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Not allowed. |
| 1 | Allowed. |
| 2 (Default) | Not configured. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisableAutoInstall |
| Friendly Name | Turn off Automatic Download and Install of updates |
| Location | Computer Configuration |
| Path | Windows Components &gt; Store |
| Registry Key Name | Software\Policies\Microsoft\WindowsStore |
| Registry Value Name | AutoDownload |
| ADMX File Name | WindowsStore.admx |

## AllowAutomaticAppArchiving

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 11, version 21H2 [10.0.22000] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/AllowAutomaticAppArchiving
```

This policy setting controls whether the system can archive infrequently used apps.

- If you enable this policy setting, then the system will periodically check for and archive infrequently used apps.
- If you disable this policy setting, then the system won't archive any apps.
- If you don't configure this policy setting (default), then the system will follow default behavior, which is to periodically check for and archive infrequently used apps, and the user will be able to configure this setting themselves.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 65535 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Explicit deny. |
| 1 | Explicit enable. |
| 65535 (Default) | Not configured. User's Choice. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AllowAutomaticAppArchiving |
| Friendly Name | Archive infrequently used apps |
| Location | Computer Configuration |
| Path | Windows Components &gt; App Package Deployment |
| Registry Key Name | Software\Policies\Microsoft\Windows\Appx |
| Registry Value Name | AllowAutomaticAppArchiving |
| ADMX File Name | AppxPackageManager.admx |

## AllowDeveloperUnlock

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/AllowDeveloperUnlock
```

Allows or denies development of Microsoft Store applications and installing them directly from an IDE.

- If you enable this setting and enable the "Allow all trusted apps to install" Group Policy, you can develop Microsoft Store apps and install them directly from an IDE.
- If you disable or don't configure this setting, you can't develop Microsoft Store apps or install them directly from an IDE.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 65535 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Explicit deny. |
| 1 | Explicit allow unlock. |
| 65535 (Default) | Not configured. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AllowDevelopmentWithoutDevLicense |
| Friendly Name | Allows development of packaged Microsoft Store apps and installing them from an integrated development environment (IDE) |
| Location | Computer Configuration |
| Path | Windows Components &gt; App Package Deployment |
| Registry Key Name | Software\Policies\Microsoft\Windows\Appx |
| Registry Value Name | AllowDevelopmentWithoutDevLicense |
| ADMX File Name | AppxPackageManager.admx |

## AllowedNonAdminPackageFamilyNameRules

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows Insider Preview |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/AllowedNonAdminPackageFamilyNameRules
```

Allowed package family names for non-Administrator user Windows app package installation.

- If you enable this policy, you can enter a list of Windows app packages non-Administrators will be able to initiate installation of regardless of the configured "Prevent non-admin users from installing packaged Windows apps" policy.

The values provided will be treated as regular expressions (ECMA Script). A package family name like Contoso. ContosoApp\_8wekyb3d8bbwe is itself a valid regular expression that will match all packages in that family. A regular expression like ^Contoso.\*\_8wekyb3d8bbwe$ will also match Contoso. ContosoApp\_8wekyb3d8bbwe.

If the package family name of an installing Windows app package matches any rule it won't be blocked by the "Prevent non-admin users from installing packaged Windows apps" policy. Installation may still be blocked by other policy or settings.

- If you disable or don't configure this policy, all Windows app packages will be subject to the configured "Prevent non-admin users from installing packaged Windows apps" policy.

Default is 'disabled' (key not present).

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
| Name | AllowedNonAdminPackageFamilyNameRules |
| Friendly Name | Allowed package family names for non-admin user install |
| Location | Computer Configuration |
| Path | Windows Components &gt; App Package Deployment |
| Registry Key Name | Software\Policies\Microsoft\Windows\Appx\AllowedNonAdminPackageFamilyNameRules |
| ADMX File Name | AppxPackageManager.admx |

## AllowGameDVR

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/AllowGameDVR
```

Windows Game Recording and Broadcasting.

This setting enables or disables the Windows Game Recording and Broadcasting features. If you disable this setting, Windows Game Recording won't be allowed.

If the setting is enabled or not configured, then Recording and Broadcasting (streaming) will be allowed.

Note

 The policy is only enforced in Windows 10 for desktop.

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
| Name | AllowGameDVR |
| Friendly Name | Enables or disables Windows Game Recording and Broadcasting |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Game Recording and Broadcasting |
| Registry Key Name | Software\Policies\Microsoft\Windows\GameDVR |
| Registry Value Name | AllowGameDVR |
| ADMX File Name | GameDVR.admx |

## AllowSharedUserAppData

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/AllowSharedUserAppData
```

Manages a Windows app's ability to share data between users who have installed the app.

- If you enable this policy, a Windows app can share app data with other instances of that app. Data is shared through the SharedLocal folder. This folder is available through the `Windows.Storage` API.
- If you disable this policy, a Windows app can't share app data with other instances of that app. If this policy was previously enabled, any previously shared app data will remain in the SharedLocal folder.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Prevented/not allowed, but Microsoft Edge downloads book files to a per-user folder for each user. |
| 1 | Allowed. Microsoft Edge downloads book files into a shared folder. For this policy to work correctly, you must also enable the Allow a Windows app to share application data between users group policy. Also, the users must be signed in with a school or work account. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | AllowSharedLocalAppData |
| Friendly Name | Allow a Windows app to share application data between users |
| Location | Computer Configuration |
| Path | Windows Components &gt; App Package Deployment |
| Registry Key Name | Software\Policies\Microsoft\Windows\CurrentVersion\AppModel\StateManager |
| Registry Value Name | AllowSharedLocalAppData |
| ADMX File Name | AppxPackageManager.admx |

## AllowStore

Note

This policy is deprecated and may be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | Not applicable | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/AllowStore
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
| 0 | Disallow. |
| 1 (Default) | Allow. |

## ApplicationRestrictions

Note

This policy is deprecated and may be removed in a future release.

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | Not applicable | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/ApplicationRestrictions
```

This policy is deprecated.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `chr` (string) |
| Access Type | Add, Delete, Get, Replace |

## BlockNonAdminUserInstall

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 2004 [10.0.19041] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/BlockNonAdminUserInstall
```

Manages non-Administrator users' ability to install Windows app packages.

- If you enable this policy, non-Administrators will be unable to initiate installation of Windows app packages. Administrators who wish to install an app will need to do so from an Administrator context (for example, an Administrator PowerShell window). All users will still be able to install Windows app packages via the Microsoft Store, if permitted by other policies.
- If you disable or don't configure this policy, all users will be able to initiate installation of Windows app packages.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Disabled. All users will be able to initiate installation of Windows app packages. |
| 1 | Enabled. Non-administrator users won't be able to initiate installation of Windows app packages. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | BlockNonAdminUserInstall |
| Friendly Name | Prevent non-admin users from installing packaged Windows apps |
| Location | Computer Configuration |
| Path | Windows Components &gt; App Package Deployment |
| Registry Key Name | Software\Policies\Microsoft\Windows\Appx |
| Registry Value Name | BlockNonAdminUserInstall |
| ADMX File Name | AppxPackageManager.admx |

## ConfigureMSIXAuthenticationAuthorizedDomains

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows Insider Preview |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/ConfigureMSIXAuthenticationAuthorizedDomains
```

This policy setting determines whether an EntraID OAuth token will be included in HTTPS communications to a specified fully qualified domain name for performing an MSIX streaming installation.

- If you enable this policy setting, HTTPS communications to the predefined fully qualified domains will incorporate the user's EntraID OAuth token when performing a streaming MSIX install. The value provided is a regular expression (ECMA Script) that will be used to match against the uppercased, fully qualified domain of the URL.
- If you disable or don't configure this policy setting, the user's EntraID OAuth token will only be shared with the default configured domains.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `chr` (string) |
| Access Type | Add, Delete, Get, Replace |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | ConfigureMSIXAuthenticationAuthorizedDomains |
| Friendly Name | Set authorized domains for HTTPS authentication in MSIX streaming install |
| Location | Computer Configuration |
| Path | Windows Components &gt; App Package Deployment |
| Registry Key Name | Software\Policies\Microsoft\Windows\Appx |
| ADMX File Name | AppxPackageManager.admx |

## DisableStoreOriginatedApps

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/DisableStoreOriginatedApps
```

Disable turns off the launch of all apps from the Microsoft Store that came pre-installed or were downloaded. Apps won't be updated. Your Store will also be disabled. Enable turns all of it back on. This setting applies only to Enterprise and Education editions of Windows.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Enable launch of apps. |
| 1 | Disable launch of apps. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisableStoreApps |
| Friendly Name | Disable all apps from Microsoft Store |
| Location | Computer Configuration |
| Path | Windows Components &gt; Store |
| Registry Key Name | Software\Policies\Microsoft\WindowsStore |
| Registry Value Name | DisableStoreApps |
| ADMX File Name | WindowsStore.admx |

## EnableMsixAllowedZones

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ [10.0.26000] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/EnableMsixAllowedZones
```

This policy controls whether MSIX packages originating from specific URL Zones are allowed to install. A package's origin is determined by its URI and whether a Mart-of-the-Web (MotW) is present. If multiple URIs are involved, all of them are considered.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Disabled. Users will be able to install MSIX packages from any zone except for Untrusted. |
| 1 | Enabled. Users will be able to install MSIX packages according to the configuration for each zone. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | EnableMsixAllowedZones |
| Path | AppxPackageManager &gt; AT &gt; WindowsComponents &gt; AppxDeployment |

## EnableMsixSmartScreenCheck

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ [10.0.26000] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/EnableMsixSmartScreenCheck
```

This policy controls whether Microsoft SmartScreen check is performed when installing MSIX packages from specific URL zones.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 | Disabled. Microsoft SmartScreen won't be consulted before installing a package. |
| 1 | Enabled. The package URI will be evaluated with Microsoft SmartScreen before installation. This check is only done for packages that come from the internet. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | EnableMsixSmartScreenCheck |
| Path | AppxPackageManager &gt; AT &gt; WindowsComponents &gt; AppxDeployment |

## LaunchAppAfterLogOn

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1809 [10.0.17763] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/LaunchAppAfterLogOn
```

List of semi-colon delimited Package Family Names of Windows apps. Listed Windows apps are to be launched after logon.

This policy allows the IT admin to specify a list of applications that users can run after logging on to the device.

Note

This policy only works on modern apps.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `chr` (string) |
| Access Type | Add, Delete, Get, Replace |
| Allowed Values | List (Delimiter: `;`) |

For this policy to work, the Windows apps need to declare in their manifest that they'll use the startup task.

**Example**:

```xml
<desktop:Extension Category="windows.startupTask">
   <desktop:StartupTask TaskId="CoffeeStartupTask" Enabled="true" DisplayName="ms-resource:Description" />
</desktop:Extension>
```

## MSIAllowUserControlOverInstall

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1803 [10.0.17134] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/MSIAllowUserControlOverInstall
```

This policy setting permits users to change installation options that typically are available only to system administrators.

- If you enable this policy setting, some of the security features of Windows Installer are bypassed. It permits installations to complete that otherwise would be halted due to a security violation.
- If you disable or don't configure this policy setting, the security features of Windows Installer prevent users from changing installation options typically reserved for system administrators, such as specifying the directory to which files are installed.

If Windows Installer detects that an installation package has permitted the user to change a protected option, it stops the installation and displays a message. These security features operate only when the installation program is running in a privileged security context in which it has access to directories denied to the user.

This policy setting is designed for less restrictive environments. It can be used to circumvent errors in an installation program that prevents software from being installed.

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
| Name | EnableUserControl |
| Friendly Name | Allow user control over installs |
| Location | Computer Configuration |
| Path | Windows Components &gt; Windows Installer |
| Registry Key Name | Software\Policies\Microsoft\Windows\Installer |
| Registry Value Name | EnableUserControl |
| ADMX File Name | MSI.admx |

## MSIAlwaysInstallWithElevatedPrivileges

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ✅ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1803 [10.0.17134] and later |

```User
./User/Vendor/MSFT/Policy/Config/ApplicationManagement/MSIAlwaysInstallWithElevatedPrivileges
```

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/MSIAlwaysInstallWithElevatedPrivileges
```

This policy setting directs Windows Installer to use elevated permissions when it installs any program on the system.

- If you enable this policy setting, privileges are extended to all programs. These privileges are usually reserved for programs that have been assigned to the user (offered on the desktop), assigned to the computer (installed automatically), or made available in Add or Remove Programs in Control Panel. This profile setting lets users install programs that require access to directories that the user might not have permission to view or change, including directories on highly restricted computers.
- If you disable or don't configure this policy setting, the system applies the current user's permissions when it installs programs that a system administrator doesn't distribute or offer.

Note

This policy setting appears both in the Computer Configuration and User Configuration folders. To make this policy setting effective, you must enable it in both folders.

Caution

Skilled users can take advantage of the permissions this policy setting grants to change their privileges and gain permanent access to restricted files and folders. Note that the User Configuration version of this policy setting isn't guaranteed to be secure.

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
| Name | AlwaysInstallElevated |
| Friendly Name | Always install with elevated privileges |
| Location | Computer and User Configuration |
| Path | Windows Components &gt; Windows Installer |
| Registry Key Name | Software\Policies\Microsoft\Windows\Installer |
| Registry Value Name | AlwaysInstallElevated |
| ADMX File Name | MSI.admx |

## RemoveDefaultMicrosoftStorePackages

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows Insider Preview [11.0.26100] |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/RemoveDefaultMicrosoftStorePackages
```

Removes Default Microsoft Store packages from the system.

- If you enable this policy, the selected Microsoft Store apps in the provided list will be uninstalled from the system. You can make adjustments to the default settings.

Unselected apps in the list won't be removed.

Default is 'disabled' (key not present).

- If the policy is disabled or not configured, no Default Microsoft Store packages will be removed from the system.

- This is a headless app (no UI)

\*\* This app is the default handler for a common file type or protocol. Removing this app might result in a degraded user experience. We don't recommend removing this app.

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
| Name | RemoveDefaultMicrosoftStorePackages |
| Friendly Name | Remove Default Microsoft Store packages from the system. |
| Location | Computer Configuration |
| Path | Windows Components &gt; App Package Deployment |
| Registry Key Name | Software\Policies\Microsoft\Windows\Appx\RemoveDefaultMicrosoftStorePackages |
| Registry Value Name | Enabled |
| ADMX File Name | AppxPackageManager.admx |

## RequirePrivateStoreOnly

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ✅ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1607 [10.0.14393] and later |

```User
./User/Vendor/MSFT/Policy/Config/ApplicationManagement/RequirePrivateStoreOnly
```

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/RequirePrivateStoreOnly
```

Denies access to the retail catalog in the Microsoft Store, but displays the private store.

- If you enable this setting, users won't be able to view the retail catalog in the Microsoft Store, but they'll be able to view apps in the private store.
- If you disable or don't configure this setting, users can access the retail catalog in the Microsoft Store.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Allow both public and Private store. |
| 1 | Only Private store is enabled. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | RequirePrivateStoreOnly |
| Friendly Name | Only display the private store within the Microsoft Store |
| Location | Computer and User Configuration |
| Path | Windows Components &gt; Store |
| Registry Key Name | Software\Policies\Microsoft\WindowsStore |
| Registry Value Name | RequirePrivateStoreOnly |
| ADMX File Name | WindowsStore.admx |

## RestrictAppDataToSystemVolume

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/RestrictAppDataToSystemVolume
```

Prevent users' app data from moving to another location when an app is moved or installed on another location.

- If you enable this setting, all users' app data will stay on the system volume, regardless of where the app is installed.
- If you disable or don't configure this setting, then when an app is moved to a different volume, the users' app data will also move to this volume.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Not restricted. |
| 1 | Restricted. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | RestrictAppDataToSystemVolume |
| Friendly Name | Prevent users' app data from being stored on non-system volumes |
| Location | Computer Configuration |
| Path | Windows Components &gt; App Package Deployment |
| Registry Key Name | Software\Policies\Microsoft\Windows\Appx |
| Registry Value Name | RestrictAppDataToSystemVolume |
| ADMX File Name | AppxPackageManager.admx |

## RestrictAppToSystemVolume

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ✅ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1507 [10.0.10240] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/RestrictAppToSystemVolume
```

This policy setting allows you to manage installing Windows apps on additional volumes such as secondary partitions, USB drives, or SD cards.

- If you enable this setting, you can't move or install Windows apps on volumes that aren't the system volume.
- If you disable or don't configure this setting, you can move or install Windows apps on other volumes.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `int` |
| Access Type | Add, Delete, Get, Replace |
| Default Value | 0 |

**Allowed values**:

| Value | Description |
| --- | --- |
| 0 (Default) | Not restricted. |
| 1 | Restricted. |

**Group policy mapping**:

| Name | Value |
| --- | --- |
| Name | DisableDeploymentToNonSystemVolumes |
| Friendly Name | Disable installing Windows apps on non-system volumes |
| Location | Computer Configuration |
| Path | Windows Components &gt; App Package Deployment |
| Registry Key Name | Software\Policies\Microsoft\Windows\Appx |
| Registry Value Name | RestrictAppToSystemVolume |
| ADMX File Name | AppxPackageManager.admx |

## ScheduleForceRestartForUpdateFailures

| Scope | Editions | Applicable OS |
| --- | --- | --- |
| ✅ Device  ❌ User | ❌ Pro  ✅ Enterprise  ✅ Education  ✅ IoT Enterprise / IoT Enterprise LTSC | ✅ Windows 10, version 1809 [10.0.17763] and later |

```Device
./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/ScheduleForceRestartForUpdateFailures
```

To ensure apps are up-to-date, this policy allows the admins to set a recurring or one time date to restart apps whose update failed due to the app being in use allowing the update to be applied. Value type is string.

**Description framework properties**:

| Property name | Property value |
| --- | --- |
| Format | `chr` (string) |
| Access Type | Add, Delete, Get, Replace |

**Allowed values**:

Expand to see schema XML

```xml
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:simpleType name="recurrence" final="restriction">
    <xs:restriction base="xs:string">
      <xs:enumeration value="None" />
      <xs:enumeration value="Daily" />
      <xs:enumeration value="Weekly" />
      <xs:enumeration value="Monthly" />
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="daysOfWeek" final="restriction">
    <xs:restriction base="xs:unsignedByte">
      <xs:minInclusive value="1" />
      <xs:maxInclusive value="127" />
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="daysOfMonth" final="restriction">
    <xs:restriction base="xs:unsignedInt">
      <xs:minInclusive value="1" />
    </xs:restriction>
  </xs:simpleType>
  <xs:element name="ForceRestart">
    <xs:complexType>
      <xs:attribute name="StartDateTime" type="xs:dateTime" use="required" />
      <xs:attribute name="Recurrence" type="recurrence" use="required" />
      <xs:attribute name="RunIfTaskIsMissed" type="xs:boolean" use="required" />
      <xs:attribute name="DaysOfWeek" type="daysOfWeek" />
      <xs:attribute name="DaysOfMonth" type="daysOfMonth" />
    </xs:complexType>
  </xs:element>
</xs:schema>
```

**Example**:

```xml
<SyncML xmlns="SYNCML:SYNCML1.1">
  <SyncBody>
    <Add>
      <CmdID>2</CmdID>
      <Item>
        <Target>
          <LocURI> ./Device/Vendor/MSFT/Policy/Config/ApplicationManagement/ScheduleForceRestartForUpdateFailures
          </LocURI>
        </Target>
        <Meta>
          <Format xmlns="syncml:metinf">xml</Format>
        </Meta>
        <Data>
          <ForceRestart StartDateTime="2018-03-28T22:21:52Z"
                        Recurrence="[None/Daily/Weekly/Monthly]"
                        DayOfWeek=”1”
                        DayOfMonth=”12”
                        RunIfTaskIsMissed=”1”/>
        </Data>
      </Item>
    </Add>
  </SyncBody>
</SycnML>
```

Note

The check for recurrence is done in a case sensitive manner. For instance the value needs to be "Daily" instead of "daily". The wrong case will cause SmartRetry to fail to execute.