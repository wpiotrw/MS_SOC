---
layout: Conceptual
title: Upgrade Microsoft Identity Manager 2016 From Service Pack 2 to Service Pack 3 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-identity-manager/microsoft-identity-manager-2016-upgrade-from-service-pack-2-to-service-pack-3
breadcrumb_path: /enterprise-mobility/toc.json
feedback_system: Standard
author: henrymbuguakiarie
ms.author: henrymbugua
description: Learn how to upgrade an existing MIM 2016 deployment from Service Pack 2 (SP2) to Service Pack 3 (SP3), including Sync Service, MIM Service, Portal on SharePoint SE, PCNS, and Add-ins & Extensions.
keywords: 
ms.date: 2026-03-17T00:00:00.0000000Z
ms.topic: how-to
ms.service: microsoft-identity-manager
ms.assetid: 735dc357-dfba-4f68-a5b3-d66d6c018803
ms.reviewer: quievey
ms.suite: ems
locale: en-us
document_id: 1c465eb2-2d7c-047e-8b19-d1778743ce55
document_version_independent_id: 1c465eb2-2d7c-047e-8b19-d1778743ce55
original_content_git_url: https://github.com/MicrosoftDocs/MIMDocs-pr/blob/live/MIMDocs/microsoft-identity-manager-2016-upgrade-from-service-pack-2-to-service-pack-3.md
site_name: Docs
depot_name: Azure.MIMDocs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: microsoft-identity-manager-2016-upgrade-from-service-pack-2-to-service-pack-3
moniker_range_name: 
monikers: []
item_type: Content
source_path: MIMDocs/microsoft-identity-manager-2016-upgrade-from-service-pack-2-to-service-pack-3.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fecfc034-c4c2-43e6-be47-948bd4addcea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/16cf36da-59bd-4744-91e9-295292c63e5e
platformId: c2bde7af-4216-f3cc-8a8f-896b2a846f58
---

# Upgrade Microsoft Identity Manager 2016 From Service Pack 2 to Service Pack 3 | Microsoft Learn

This article guides you through upgrading an existing Microsoft Identity Manager (MIM) 2016 environment from Service Pack 2 (SP2) to Service Pack 3 (SP3). The following components support in-place upgrade when installed on supported operating systems:

- MIM Synchronization Service
- Standalone MIM Service
- Privileged Access Management (PAM)
- Password Change Notification Service (PCNS)
- MIM Reporting
- MIM Client Extensions

The MIM Portal requires a new deployment on SharePoint Subscription Edition and can't be upgraded.

Note

If all MIM components are deployed on a single server (all-in-one), an in-place upgrade isn't available. Follow the new installation procedure instead.

## Prerequisites

Before you start the upgrade:

- **Supported operating systems**: All servers hosting MIM SP3 components must run Windows Server 2019 or Windows Server 2022. Windows Server 2016 and earlier versions aren't supported. Upgrade the operating system before you apply SP3 if any component is currently hosted on an unsupported platform. Windows Server 2025 isn't currently supported for SP3.
- **Required upgrade baseline**: You can perform an in-place upgrade to SP3 only from the latest released build of MIM 2016 SP2 (version **4.6.673.0**). If a component runs SP1 or an older SP2 update, upgrade it to version 4.6.673.0 first.
- Schedule a maintenance window.
- Back up all MIM databases (for example, **MIMService** and **MIMSynchronizationService**) and the MIM Synchronization encryption keys.
- Back up all installation directories.
- Install .NET Framework 3.5.
- Install .NET Framework 4.6.2 or .NET Framework 4.8.
- Install the Microsoft Visual C++ 2015–2022 Redistributable (x64).
- Install Microsoft OLE DB Driver for SQL Server.
- If not already downloaded, download a copy of the MIM 2016 SP2 installation media (ISO) from the MSDN Subscription download site or Microsoft 365 Admin Center.
- Download the original MIM installation media (baseline ISO) used when initially setting up MIM from the MSDN Subscription download site or Microsoft 365 Admin Center.
- Download the relevant MIM 2016 SP3 upgrade MSP files.

Important

**Recommended upgrade order**

1. Upgrade Synchronization Service
2. Upgrade standalone MIM Service (if applicable)
3. Deploy the new MIM Portal environment
4. Upgrade remaining components.

## Determine the baseline ISO for the upgrade

### Understand why the “baseline ISO” matters for SP3 upgrades

Upgrading Microsoft Identity Manager (MIM) 2016 from Service Pack 2 (SP2) to Service Pack 3 (SP3) is performed using Windows Installer patch (.MSP) files, rather than a full installation.

Because of this, the upgrade process depends on the baseline MSI that Windows Installer associates with the installed components. This baseline determines which installation source (ISO) must be provided during the upgrade.

In practice, this means the upgrade may require access to the original installation media used when MIM was first installed, not simply the most recent service pack level currently installed.

### Determine which ISO baseline you should use

If you already know your baseline ISO then you can skip this step. Otherwise, run the PowerShell script below in order to determine which baseline ISO you should use.

```powershell
# Find MIM product
$prod = Get-ChildItem `
    "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
    "HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall" |
    Get-ItemProperty |
    Where-Object {
        $_.PSObject.Properties['DisplayName'] -and
        $_.DisplayName -like "*Microsoft Identity Manager*" -and
        $_.DisplayName -notlike '*Connector*'
    } |
    Select-Object -First 1

if (-not $prod) {
    throw "Microsoft Identity Manager not found in registry"
}

# Extract ProductCode from UninstallString
if ($prod.UninstallString -match '\{[0-9A-F-]+\}') {
    $productCode = $matches[0]
} else {
    throw "Could not extract ProductCode from UninstallString"
}

# Use Windows Installer COM object
$installer = New-Object -ComObject WindowsInstaller.Installer

# Get cached MSI path
$msiPath = $installer.ProductInfo($productCode, "LocalPackage")

if (-not (Test-Path $msiPath)) {
    throw "Cached MSI not found at $msiPath"
}

# Open MSI database
$database = $installer.GetType().InvokeMember(
    "OpenDatabase", "InvokeMethod", $null, $installer, @($msiPath, 0)
)

# Query ProductVersion
$query = "SELECT Value FROM Property WHERE Property='ProductVersion'"
$view = $database.OpenView($query)
$view.Execute()
$record = $view.Fetch()

if ($record) {
    $productVersion = $record.StringData(1)
    Write-Output $productVersion
} else {
    throw "ProductVersion not found in MSI"
}

$view.Close()
```

Map the version you will get from running the sccript to the versions table below.

| Baseline MSI Version | Corresponding Package Name |
| --- | --- |
| 4.3.1935.0 | Microsoft Identity Manager Release To Market (RTM) |
| 4.4.1302.0 | Microsoft Identity Manager Service Pack 1 (SP1) |
| 4.6.31.0 | Microsoft Identity Manager Service Pack 2 Release Candidate (SP2 RC) |
| 4.6.34.0 | Microsoft Identity Manager Service Pack 2 (SP2) |
| 4.6.421.0 | Microsoft Identity Manager Azure Active Directory Premium (AADP) |

## Prepare the SP2 installation source for SP3 patching

Many MIM components that support in-place upgrade to SP3 are updated by using Windows Installer patches (`.msp` files). Before you apply any SP3 patch, you must ensure that the original SP2 installation source is available and that the correct SP2 baseline MSI is present. Windows Installer requires this baseline to validate the installed product and sequence the update correctly.

If the SP2 baseline MSI isn't present or is replaced by an SP3 MSI, the patch might fail or incorrectly determine that the product is already upgraded.

You can prepare the installation source by following the manual steps in this section or by using an automation script.

### Automate installation source preparation (optional)

You can use the Microsoft-provided PowerShell script to automate the preparation of the SP2 installation source and application of the SP3 patch.

The script performs the following actions:

- Detects installed MIM components and their installation source
- Validates and prepares the `InstallSource` path
- Verifies the SP2 baseline MSI version
- Copies required files from SP2 and SP3 installation media
- Backs up and restores the installation source
- Applies the SP3 patch using Windows Installer

Important

The script requires:

- An elevated PowerShell session (run as administrator)
- A supported SP2 baseline installation
- Access to both SP2 and SP3 installation media and SP3 MSP patch file
- A writable installation source path (mounted ISO paths aren't supported)

Download the script:

- [Download UpgradeToSP3.ps1 from Microsoft Download Center](https://www.microsoft.com/download/details.aspx?id=108637)

If you use the script, it replaces the manual steps in this section (Step 1 through Step 3). The script will prompt you for the required inputs during execution.

### Manual installation source preparation

If you choose not to use the automation script, follow the manual steps in this section.

Perform the following preparation on each server or workstation that hosts a MIM component (for example, Sync Server, Portal servers, or Service servers) before you run any SP3 MSP update.

The following example demonstrates how to update the MIM 2016 Synchronization Service from SP2 to SP3. The steps are the same for all MIM system components (for example, MIM Service).

#### Step 1 - Identify the installation source

Run the following PowerShell command in an elevated session to determine the installation source path for the MIM component:

```powershell
Get-ChildItem HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall, `
HKLM:\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall |
Get-ItemProperty |
Where-Object { $_.DisplayName -like "Microsoft Identity*" } |
Select InstallSource
```

This command returns the `InstallSource` path used by the original installation.

![Screenshot of a PowerShell window showing the Get-ChildItem command output with the InstallSource path E:\Synchronization Service\ for the Microsoft Identity Manager component.](media/upgrade/installation-source-powershell-output.png)

Record the `InstallSource` value for each MIM component. This location is where Windows Installer expects to find the original SP2 MSI files during the SP3 upgrade.

##### Step 1.1 - Verify the drive exists

Verify that the drive of the `InstallSource` returned in the previous step exists.

- If the drive exists, proceed to Step 2 - Copy the component folder.
- If the drive doesn't exist, continue to Step 1.2 to create it.

##### Step 1.2 - Create the required drive (if missing)

Create a folder that will act as the mapped drive using the following command:

```cmd
mkdir C:\Patch
```

![Screenshot of File Explorer showing the C:\Patch folder created on the Windows C: drive.](media/upgrade/create-patch-folder.png)

##### Step 1.3 - Create the virtual drive

Use the `SUBST` command to create a virtual drive mapping. Run the following command in a Command Prompt window (non-admin):

```cmd
SUBST E: C:\Patch
```

Then run the same command again in an elevated Command Prompt:

```cmd
SUBST E: C:\Patch
```

![Screenshot of a Command Prompt window showing the SUBST E: C:\Patch command executed successfully.](media/upgrade/virtual-drive-command-execution.png)

After you run the command, a new E: drive should appear.

![Screenshot of the PC view in File Explorer showing the new Windows E: virtual drive alongside other drives.](media/upgrade/virtual-drive-created.png)

#### Step 2 - Copy the component folder

1. Create a backup for the `InstallSource`.
2. Prepare the installation media:

    - If you obtained the artifacts from **Volume Licensing (ISO)**:
        - Mount or open the MIM SP3 ISO.
    - If you obtained the artifacts from the **Microsoft Entra ID P1 or P2 customer**download page:
        - The files are in `.zip` format. Extract the contents to a local path (for example, `C:\Downloads\Synchronization Service`).
3. Locate the component folder. For example, if you're upgrading the Synchronization Service, locate the **Synchronization Service** folder in the extracted contents or mounted ISO.
4. Copy the entire component folder to the `InstallSource` path (for example, `E:\Synchronization Service`).

The folder structure must match the `InstallSource` path identified in Step 1.

![Screenshot of File Explorer showing the contents of the E:\Synchronization Service folder after copying SP3 files, including the setup files and batch files.](media/upgrade/synchronization-service-folder-contents.png)

#### Step 3 - Build the installation source

Important

This step ensures the baseline MSI is in place alongside the SP3 patch file. If the MSI is from SP3 instead of SP2, the patch will fail.

##### Step 3.1 - Replace the MSI file

1. Open the MIM 2016 baseline ISO.
2. Locate the MSI file for your component. For the Synchronization Service, the file is `Synchronization Service.msi`.
3. Copy this file to the `InstallSource` folder (for example, `E:\Synchronization Service`). When prompted, replace the existing MSI file.

Use the following table as a reference for MSI file locations (here we are using MIM SP2 as our baseline)

| Component | SP2 MSI to copy |
| --- | --- |
| Synchronization Service | `SP2:\Synchronization Service\Synchronization Service.msi` |
| Service and Portal | `SP2:\Service & Portal\Service & Portal.msi` |
| PCNS | `SP2:\Password Change Notification Service\x64\Password Change Notification Service.msi` |
| Add-ins and Extensions | `SP2:\Add-ins and extensions\x64\Add-ins and extensions.msi` |
| Language Packs | `SP2:\LANGUAGE Packs\Add-ins and Extensions Language Pack\x64\Add-ins and Extensions Language.msi` |
| Certificate Management | `SP2:\Certificate Management\x64\Certificate Management.msi` |
| CM Client | `SP2:\CM Client\x64\CM Client.msi` |
| CM Bulk Client | `SP2:\CM Bulk Client\CM Bulk Client.msi` |

If your deployment uses x86 components or non-English languages, select the folder that matches the installed architecture and language.

##### Step 3.2 - Copy the SP3 patch file

Copy the SP3 patch (MSP) file to the same `InstallSource` folder. For the Synchronization Service, the file is `MIMSyncService_x64_KB5085154.msp`.

##### Step 3.3 - Verify installation files

Verify that the `InstallSource` folder contains both required files:

- The SP2 MSI (for example, `Synchronization Service.msi`) copied from the SP2 ISO
- The SP3 MSP (for example, `MIMSyncService_x64_KB5085154.msp`) patch file

![Screenshot of File Explorer showing the E:\Synchronization Service folder with the Synchronization Service.msi file from SP2 and the MIMSyncService_x64 MSP patch file from SP3 both present.](media/upgrade/sync-service-verified-installation-files.png)

## Upgrade the Synchronization Service

After you complete the preparation steps, apply the SP3 patch to the Synchronization Service.

1. **Verify platform and version**

    Confirm the OS and installed MIM version meet the prerequisites.
2. **Stop the Synchronization Service**

    From an elevated PowerShell session, run:

    ```powershell
    Stop-Service FIMSynchronizationService
    ```

    Stopping the service prevents synchronization activity and releases the file locks required for patching. Confirm that the service shows a Stopped status before you continue.
3. **Back up the Sync environment**

    Back up the Sync database and installation directory. SP3 patches can't be rolled back with a standard uninstall.
4. **Eject the SP2 ISO (if mounted)**

    Before you apply the patch, ensure the MIM 2016 SP2 ISO isn't mounted. Unmount it if necessary to prevent the installer from referencing the wrong source files.
5. **Apply the SP3 patch**

    From an elevated command prompt, navigate to the `InstallSource` folder and run the following command:

    ```cmd
    msiexec /p MIMSyncService_x64_KB5085154.msp REINSTALLMODE=emus REINSTALL=ALL /l*v log.txt
    ```

    ![Screenshot of an elevated Command Prompt showing the msiexec patch command being run from the E:\Synchronization Service folder.](media/upgrade/windows-installer-patch-command.png)

    Important

    Before you run the command, verify that the MSP file name in the command matches the actual SP3 patch file name in the folder (for example, `MIMSyncService_x64_KB5085154.msp`). Update the command accordingly if the name differs.

    These `msiexec` switches control how the installer reinstalls features and updates files and registry values:

    - `/p` — Applies the specified patch.
    - `REINSTALL=ALL` — Reinstalls all features.
    - `REINSTALLMODE=emus` — Reevaluates and overwrites registry entries and files.
    - `/l*v log.txt` — Generates a verbose log file.
6. Download and copy the latest [MIM Synchronization Service utility tools versions](https://www.microsoft.com/download/details.aspx?id=108645) to the bin folder in the program files for the Microsoft Identity Manager Synchronization Service.
7. **Restart the Synchronization Service**

    If the patch installs successfully, the installation completion screen will appear.

    ![Screenshot of the Microsoft Identity Manager Synchronization Service Setup Wizard showing the completion screen with a message that the setup finished successfully.](media/upgrade/sync-service-setup-complete.png)

    After the patch installs successfully, start the service:

    ```powershell
    Start-Service FIMSynchronizationService
    ```

    Verify the service starts without errors.
8. **Validate synchronization functionality**

    Open **Synchronization Service Manager**, confirm Management Agents load, and run a **Full Import (Stage Only)**. Successful execution confirms a healthy upgrade.
9. **Remove temporary source mapping (if used)**

    If you created a temporary drive mapping earlier, remove it by running:

    ```cmd
    SUBST E: /D
    ```

## Resolve common upgrade errors

This section describes common issues that can occur when you apply SP3 patches and how to resolve them.

### Insert Disk error

If you receive an **Insert Disk** error, the installer might be looking for a specific volume label.

![Screenshot of a dialog box showing a Please insert the disk message from the Microsoft Identity Manager 2016 Synchronization Service installer.](media/upgrade/insert-disk-error-dialog.png)

The volume label can usually be found in the `log.txt` file generated by the installer. To resolve this issue, remove the volume label from the registry by running the following PowerShell command:

```powershell
Get-ChildItem HKLM:\SOFTWARE\Classes\Installer\Products -Recurse |
Get-ItemProperty |
Where-Object {$_.PSObject.Properties.Value -match "MIM-X22-20157"} |
ForEach-Object {
    $path = $_.PSPath
    $_.PSObject.Properties |
    Where-Object {$_.Value -match "MIM-X22-20157"} |
    ForEach-Object {
        Remove-ItemProperty -Path $path -Name $_.Name -ErrorAction SilentlyContinue
    }
}
```

After you run the command, run the patch command again.

### Source file not found error

If you receive a **Source file not found** error, verify that the SP2 installation media isn't still mounted. Having SP2 mounted can cause a conflict where the installer attempts to reference files from the incorrect source path, resulting in the missing file error.

![Screenshot of an error dialog from the Microsoft Identity Manager 2016 Service and Portal installer showing a source file not found message.](media/upgrade/source-file-not-found-error.png)

Unmount the SP2 ISO and run the patch command again.

## Upgrade a standalone MIM Service

Use this procedure only when the MIM Service is **not** co‑located with the MIM Portal. Ensure the server runs Windows Server 2019 or 2022 and the MIM SP2 4.6.673.0 baseline is installed.

Before you begin, complete the preparation steps for the MIM Service component on this server.

1. **Confirm the MIM Service is not co-located with the MIM portal**

    Verify that the MIM Service is installed on its own server and not sharing the system with the MIM Portal. If it's co‑located, follow the Deploy the MIM Service when it's installed with the Portal procedure instead.
2. **Verify prerequisites on the server**

    Confirm that the following components are installed before you continue:

    - Microsoft .NET Framework 4.8
    - Microsoft OLE DB Driver for SQL Server
    - Microsoft Visual C++ 2015–2022 Redistributable (x64)

    These components enable the SP3 update package to install and register assemblies successfully.
3. **Back up the MIM Service environment**

    Back up the following items before you continue:

    - The FIMService database
    - The installation directory at `%ProgramFiles%\Microsoft Forefront Identity Manager\2010\Service`
    - The encryption keys (use `miiskmu.exe` if you haven't already secured them)

    Because SP3 installs as a patch, you must restore from backup to roll back the upgrade. Completing this step ensures you have a recovery path before you modify the installation.
4. **Stop the MIM Service and IIS**

    From an elevated PowerShell session, run the following commands to stop the MIM Service and IIS:

    ```powershell
    Stop-Service FIMService
    iisreset /stop
    ```
5. **Apply the SP3 patch**

    From an elevated command prompt in the folder that contains the MSP, run:

    ```cmd
    msiexec /p MIMService_x64_KB5085154.msp REINSTALL=ALL REINSTALLMODE=emus /l*v MIMServiceSP3.log 
    ```

    This command instructs Windows Installer to update all installed features and overwrite the existing binaries with the SP3 versions while preserving the current configuration. Allow the installation to finish without interruption. A successful installation returns exit code 0 and generates the specified log file.
6. **Restart services**

    Restart IIS and the MIM Service components by running the following commands:

    ```powershell
    iisreset /start
    Start-Service FIMService
    ```
7. **Verify the upgrade**

    Confirm that the upgrade completed successfully by performing the following checks:

    - Open **Services** and verify that the **Forefront Identity Manager Service** is running.
    - Review the **Application** event log for any installation or configuration errors.
    - Launch the **MIM Portal** (if it connects to this Service) and confirm that it communicates successfully.
    - Run a test workflow or object update to validate Service functionality.
    - Verify that the file version of **Microsoft.ResourceManagement.Service.exe** reflects the SP3 build.

    Successfully completing these checks confirms that the Service tier is running with the updated binaries and existing configuration.
8. **Remove temporary source mapping (if used)**

    If you created a temporary drive mapping earlier, remove it by running:

    ```powershell
    SUBST E: /D
    ```

    This command removes the mapping and returns the system to its original configuration.

## Deploy the MIM Portal on SharePoint Subscription Edition

MIM 2016 SP3 Portal requires **SharePoint Subscription Edition (SE)**. Because SharePoint 2016 and 2019 can't be upgraded in place to Subscription Edition, you must deploy the MIM Portal to a new SharePoint SE environment rather than upgrade it on the existing server. If the MIM Service is installed on the same server as the Portal, you must also redeploy it.

This guide doesn't include the detailed installation procedures for SharePoint SE, the MIM Portal, or a co‑located MIM Service. You can find those procedures in the MIM 2016 SP3 Deployment Guide, and you must follow them to ensure a supported configuration.

To complete the Portal deployment, use the following documentation:

- [Deploy SharePoint Subscription Edition for Microsoft Identity Manager 2016 SP3](prepare-server-sharepoint)
- [Install the MIM 2016 SP3 Portal on SharePoint Subscription Edition](install-mim-service-portal)

## Deploy the MIM Service when it's installed with the Portal

If your existing environment hosted the MIM Service on the same server as the MIM Portal, you must install a new MIM Service instance as part of the SharePoint Subscription Edition deployment. You must take this approach because you can't reuse the original server after you redeploy the Portal.

Follow the detailed MIM Service installation steps in the Deployment Guide, with one important exception related to database configuration. During installation, when the setup prompts you to configure the MIM Service database, specify the existing FIMService database from the current environment instead of creating a new one. Reusing the existing database preserves configuration data, schema, policies, and workflows, and it's the supported approach when transitioning to SP3 in this topology.

All other installation steps, prerequisites, and configuration settings should match the guidance in the Deployment Guide.

To complete this deployment, refer to:

- [Install the MIM 2016 SP3 Service](install-mim-service-portal)

After installation completes, verify that the Service starts successfully and can communicate with the reused database before you continue with Portal validation.

## Upgrade Password Change Notification Service (PCNS)

Upgrade PCNS on each domain controller where it's installed. Unlike other components, PCNS is upgraded by running the **SP3 MSI** directly (not an MSP). Perform upgrades sequentially across domain controllers to maintain password sync availability.

1. **Verify platform and version**

    Confirm that the domain controller is running Windows Server 2019 or Windows Server 2022 and that the installed PCNS version matches the latest MIM 2016 SP2 release. This verification ensures the server meets the supported baseline before you install SP3.
2. **Confirm a system state backup exists**

    Verify that a recent system state backup of the domain controller is available. PCNS installs a password filter DLL, and restoring the domain controller provides the required rollback method if you need to revert the upgrade.
3. **Stop the PCNS service**

    From an elevated PowerShell session, run:

    ```powershell
    Stop-Service FIMPCNS
    ```

    Confirm that the service status shows Stopped before you continue.
4. **Run the SP3 PCNS installer**

    Run the PCNS installation package directly on the domain controller from the SP3 media:

    ```cmd
    SP3 Media:\Password Change Notification Service\x64\Password Change Notification Service.msi
    ```

    Launch the MSI from an elevated command prompt or by right‑clicking it and selecting Run as administrator. The installer detects the existing SP2 installation and upgrades it in place.
5. **Restart the domain controller if prompted**

    Some environments require a restart to reload the updated password filter. If the installer prompts you to reboot, restart the server before you continue.
6. **Validate password change notification**

    Reset a test user’s password, confirm local DC logging, and verify the Sync Service receives and processes the notification.

## Upgrade Add-ins and Extensions

Upgrade Add-ins and Extensions after you update core roles. These components use the SP3 MSP patch model and the same SP2 baseline validation you used for Sync Service and MIM Service.

1. **Verify platform and version requirements**

    Confirm the OS and installed MIM version meet the baseline requirements.
2. **Close dependent applications**

    Close Microsoft Outlook, MMC consoles, and any applications that use MIM integrations before you apply the update. Closing these applications prevents file locks that could cause the patch to fail or trigger a repair during installation.
3. **Apply the SP3 patch**

    From an elevated command prompt in the folder that contains the MSP, run:

    ```cmd
    msiexec /p MIMAddinsExtensions_x64_KB5085154.msp REINSTALL=ALL REINSTALLMODE=emus /l*v AddinsSP3.log 
    ```

    This command updates the installed binaries while preserving the existing configuration.
4. **Restart the system**

    Reboot to ensure updated assemblies load and register correctly.
5. **Validate functionality**

    Open Outlook (if applicable), launch admin tools that rely on extensions, verify certificate/portal integrations, and review the Application event log for Windows Installer repair actions.