---
layout: Conceptual
title: Extend sensitivity labeling on Windows | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/information-protection-client
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-10-26T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-information-protection
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Extend sensitivity labels to more file types on Windows, using the Microsoft Purview Information Protection client.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 08f2a33d-ae06-1f82-2b36-9618192b846a
document_version_independent_id: 08f2a33d-ae06-1f82-2b36-9618192b846a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/information-protection-client.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: information-protection-client
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/information-protection-client.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/5cf46315-b33f-4e99-8224-a1592697eff9
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/715d24c3-3683-4219-82c5-1e3c813fb7fc
platformId: ef5f9c57-95f3-1754-db28-beaee61c4f21
---

# Extend sensitivity labeling on Windows | Microsoft Learn

The Microsoft Purview Information Protection client extends [sensitivity labels](sensitivity-labels) beyond labels that are built into Microsoft 365 apps and services, and supports a wider range of file types.

This client runs on Windows only and replaces the Azure Information Protection (AIP) unified labeling client. It has the following components:

| Component | Description |
| --- | --- |
| [Information protection scanner](deploy-scanner) | Used to discover, label, and encrypt files on data stores such as network shares and SharePoint Server libraries. |
| [Information protection file labeler](https://support.microsoft.com/topic/label-and-protect-files-in-file-explorer-in-windows-67829155-2d0e-4122-9677-7c53c8cba18a) | Used to apply sensitivity labels and encryption using File Explorer. |
| [Information protection viewer](https://support.microsoft.com/topic/view-protected-files-with-the-azure-information-protection-viewer-9fb56fae-7989-48b0-850f-f446e057cf73) | Used to view files that are encrypted. |
| [Microsoft Purview Information Protection PowerShell module](/en-us/powershell/module/purviewinformationprotection) | Used to adjust sensitivity labels on files, and install and configure Microsoft Purview Information Protection scanner. |

There's no Office Add-in with the Microsoft Purview Information Protection client because this functionality is replaced with [sensitivity labels that are built into Office](sensitivity-labels-office-apps).

For the latest release information and support timelines for each client version, see [Microsoft Purview Information Protection client - Release management and supportability](information-protection-client-relnotes).

## Requirements for deploying the information protection client

To use the Microsoft Purview Information Protection client, install this client on Windows computers where you want to use the client components.

You also must meet the following requirements:

# [Operating Systems](#tab/devices)
The Microsoft Purview Information Protection client supports 64-bit versions of Windows and Windows Server that are supported under the Microsoft Lifecycle Policy, including versions in extended support:

- **Windows**, including Windows Enterprise multi-session. Handwriting isn't supported on Windows 10 RS4 and later.
- **Windows Server**.

To confirm whether a specific version is supported, see the [Windows lifecycle FAQ](/en-us/lifecycle/faq/windows) and [Windows Server release information](/en-us/windows/release-health/windows-server-release-info).

ARM64 is supported for the viewer and file labeler, but isn't supported for the scanner or PowerShell.

# [Virtual Machines](#tab/virtual-machines)
If you're working with virtual machines, check whether the software publisher for your virtual desktop solution has other configuration requirements for running the information protection client.

For example, for Citrix solutions, you might need to disable the Citrix Application Programming Interface (API) hooks for Office and the Microsoft Purview Information Protection client.

The following applications use these files, respectively: Word (winword.exe), Excel (excel.exe), Outlook (outlook.exe), PowerPoint (powerpnt.exe), Information Protection File Labeler (msip.app.exe), and Information Protection Viewer (msip.viewer.exe).

# [Remote Desktop Services](#tab/devices/servers)
Remote Desktop Services supports the information protection client on 64-bit versions of Windows Server that are supported under the Microsoft Lifecycle Policy, including versions in extended support. To confirm whether a specific version is supported, see [Windows Server release information](/en-us/windows/release-health/windows-server-release-info).

If you delete user profiles when you use the information protection client with Remote Desktop Services, make sure to **keep the *%Appdata%\Microsoft\Protect* folder**.

# [Subscription](#tab/subscription)
You must have a cloud-based subscription for sensitivity labeling using the Microsoft Purview Information Protection client or scanner. For more information, see:

- [Microsoft 365 licensing guidance for security & compliance](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance#information-protection)
- [Modern Work Plan Comparison (PDF download)](https://go.microsoft.com/fwlink/?linkid=2139145)

# [Microsoft Entra](#tab/microsoft-entra)
To support authentication and authorization for Microsoft Purview Information Protection, you must have a Microsoft Entra ID. To use user accounts from your on-premises directory, you must also configure directory integration.

- **Single sign-on (SSO)** is supported for Microsoft Purview Information Protection, so that users aren't repeatedly prompted for their credentials. If you use another vendor solution for federation, check with that vendor for instructions on configuring it for Microsoft Entra ID. WS-Trust is commonly required for these solutions to support single sign-on.
- **Multi-factor authentication (MFA)** is supported with Microsoft Purview Information Protection when you have the required client software and that the MFA-supporting infrastructure is configured correctly.

Other prerequisites are required for specific scenarios, such as when using certificate-based or multifactor authentication, or when UPN values don't match user email addresses.

For more information, see:

- [Microsoft Entra requirements](rights-management-requirements#microsoft-entra-requirements)
- [What is Microsoft Entra Directory?](/en-us/azure/active-directory/fundamentals/active-directory-whatis)
- [Integrate on-premises Active Directory domains with Microsoft Entra ID](/en-us/azure/architecture/reference-architectures/identity/azure-ad)

# [Additional](#tab/additional-requirements)
To install the information protection client, you must have local administrative permissions on the client computer, and the following additional requirements.

### Microsoft .NET Framework requirements

The full installation of the client requires a minimum version of Microsoft .NET Framework 4.7.2.

If this framework is missing, the setup wizard from the executable installer tries to download and install this prerequisite. When this prerequisite is installed as part of the client installation, the computer must be restarted.

## Windows PowerShell minimum requirements

The PowerShell module for the client requires a minimum version of Windows PowerShell 4.0.

If you're working on an older operating system, you might need to install PowerShell manually. For more information, see [How to Install Windows PowerShell 4.0](https://social.technet.microsoft.com/wiki/contents/articles/21016.how-to-install-windows-powershell-4-0.aspx).

Important

The installer doesn't check or install this prerequisite for you.

To confirm the version of Windows PowerShell that you are running, type `$PSVersionTable` in a PowerShell session.

## Screen resolution requirements

Windows computers with monitor resolutions of **800x600** and lower can't fully display the file labeler dialog box when you right-click a file or folder in File Explorer.

---

## Install or upgrade the information protection client

If you install the Microsoft Purview Information client interactively and the Azure Information Protection (AIP) unified labeling client is detected, you can upgrade the older client after you acknowledge the AIP Add-in for Office will be removed.

Note

Upgrades by using Microsoft Update Catalog or any other non-interactive installation require a registry key configuration if any Azure Information Protection client versions are present on the local computer.

There are two options for installing the information protection client:

- Installing the information protection client using the **.exe** installer
- Installing the information protection client using the **.msi** installer

If you're upgrading the information protection scanner, either from the Azure Information Protection (AIP) unified labeling client or a previous version of the information protection client, see [Upgrade the Microsoft Purview Information Protection scanner](upgrade-scanner-migrate) before using these client installation instructions.

# [Install using the .exe installer](#tab/install-client-exe)
To install the information protection client with the .exe file:

1. Download the executable version of the Microsoft Purview Information Protection client from the [Microsoft Download Center](https://www.microsoft.com/download/details.aspx?id=53018). For example, **PurviewInfoProtection.exe**.

    Important

    If there is a preview version available, use that version only for testing. It is not intended for end users in a production environment.
2. For a default installation, simply run the executable. To view all installation options, first run the executable with **/help**. For example:`PurviewInfoProtection.exe **/help**`

    1. To silently install the client, run: `PurviewInfoProtection.exe /quiet`
    2. To silently install only the PowerShell cmdlets, run: `PurviewInfoProtection.exe PowerShellOnly=true /quiet`

    Note

    By default, the option to send usage statistics to Microsoft is enabled. To disable this option, make sure to take one of the following steps:

    - During installation, specify **AllowTelemetry=0**
    - After installation, update the registry key as follows: **EnableTelemetry=0**.
3. To complete the installation, restart any instances of File Explorer.
4. Confirm that the installation was successful by checking the install log file, which is created in the **%temp%** folder by default.

    The install log file has the following naming format: `Microsoft_Azure_Information_Protection_<number>_<number>_MSIP.Setup.Main.msi.log`

    For example: **Microsoft\_Azure\_Information\_Protection\_20161201093652\_000\_MSIP.Setup.Main.msi.log**

    In the log file, search for the following string: **Product: Microsoft Purview Information Protection--Installation completed successfully**. If the installation failed, this log file contains details to help you identify and resolve any problems.

    Tip

    You can change the location of the installation log file with the **/log** installation parameter.

# [Install using the .msi installer](#tab/install-client-msi)
For central deployment, use the following information that is specific to the .msi installation version of the information protection client. If you use Microsoft Intune for your software deployment method, use these instructions together with [Add apps with Microsoft Intune](/en-us/mem/intune/apps/apps-add).

**To install the information protection client with the .msi file**

1. Download the .msi version of the Microsoft Purview Information Protection client from the [Microsoft Download Center](https://www.microsoft.com/download/details.aspx?id=53018). For example, **PurviewInfoProtection.msi**.

    Important

    If there is a preview version available, use that version only for testing. It is not intended for end users in a production environment.
2. For each computer that runs the .msi file, make sure that the following software dependency is installed. Package it with the .msi version of the client or only deploy to computers that have the following software already installed:

    | Office version | Operating system | Software |
    | --- | --- | --- |
    | All versions except Office 365 1902 or later | Windows 10 version 1809 only, operation system builds older than 17763.348 | [KB 4482887](https://support.microsoft.com/help/4482887/windows-10-update-kb4482887) |
3. For a default installation, run the .msi with **/quiet**, for example: `PurviewInfoProtection.msi /quiet.`

Note

By default, the option to send usage statistics to Microsoft is enabled. To disable this option, make sure to take one of the following steps:

- During installation, specify **AllowTelemetry=0**
- After installation, update the registry key as follows: **EnableTelemetry=0**.

---

## Log file locations

Client and scanner log files are located in the following locations on the Windows computer:

- **\ProgramFiles (x86)\Microsoft Purview Information Protection** (64-bit operating systems only)
- **\Program Files\Microsoft Purview Information Protection** (32-bit operating systems only)
- **%localappdata%\Microsoft\MSIP**

## Supported languages

The information protection client supports the same languages that Office 365 supports. For a list of these languages, see the [International availability](https://products.office.com/business/international-availability) page from Office.

For these languages, menu options, dialog boxes, and messages from the Microsoft Purview Information Protection client display in the user's language. There's a single installer that detects the language, so no additional configuration is required to install the information protection client for different languages.

However, label names and descriptions that you specify aren't automatically translated when you configure labels in the admin portal. For users to see labels in their preferred language, provide your own translations and configure them for the labels by using PowerShell and the *LocaleSettings* parameter for [Set-Label](/en-us/powershell/module/exchange/set-label). For more information, see [Example configuration to configure a sensitivity label for different languages](create-sensitivity-labels#example-configuration-to-configure-a-sensitivity-label-for-different-languages).

## Supported file types

This section lists the file types supported by the Microsoft Purview Information Protection client. For the listed file types, WebDav locations aren't supported.

Tip

When you encrypt file types that don't have built-in support for encryption and so use generic encryption, we recommend that you assign the permission of co-owner to these files.

# [Sensitivity labels without encryption](#tab/classification-file-types)
The following file types can be labeled without encryption.

- **Adobe Portable Document Format:** .pdf
- **Microsoft Project:** .mpp, .mpt
- **Microsoft Publisher:** .pub
- **Microsoft XPS:** .xps .oxps
- **Images:** .jpg, .jpe, .jpeg, .jif, .jfif, .jfi. png, .tif, .tiff
- **Autodesk Design Review 2013:** .dwfx
- **Adobe Photoshop:** .psd
- **Digital Negative:** .dng
- **Microsoft Office:** The following file types, including 97-2003 file formats and Office Open XML formats for Word, Excel, and PowerPoint.

    | Word | Excel | PowerPoint | Visio |
    | --- | --- | --- | --- |
    | .doc | .xls | .potm | .vdw |
    | .docm | .xlsb | .potx | .vsd |
    | .docx | .xlsm | .pps | .vsdm |
    | .dot | .xlsx | .ppsm | .vsdx |
    | .dotx | .xltm | .ppsx | .vss |
    |  | .xltx | .ppt | .vssm |
    |  |  | .pptx | .vst |
    |  |  |  | .vstm |
    |  |  |  | .vssx |
    |  |  |  | .vstx |

# [Sensitivity labels with encryption](#tab/protection-file-types)
The information protection client supports encryption at two different levels, as described in the following table.

| Type of encryption | Native | Generic |
| --- | --- | --- |
| **Description** | For text, image, Microsoft Office (Word, Excel, PowerPoint) files, .pdf files, and other application file types that support a Rights Management service, native encryption provides a strong level of protection with encryption and enforcement of rights (permissions). | Generic encryption provides a level of protection for other file types. Generic encryption uses file encapsulation with the .pfile file type and authentication to verify whether a user is authorized to open the file. |
| **Encryption** | File protection is enforced in the following ways:  - Before encrypted content is rendered, successful authentication must occur for those users who receive the file through email or are given access to it through file or share permissions.  - Additionally, usage rights and policy that were set by the content owner when the files were encrypted are enforced when the content is rendered in either the information protection viewer (for encrypted text and image files) or the associated application (for all other supported file types). | File protection is enforced in the following ways:  - Before encrypted content is rendered, successful authentication must occur for people who are authorized to open the file and given access to it. If authorization fails, the file doesn't open.  - Usage rights and policy set by the content owner are displayed to inform authorized users of the intended usage policy.  - Audit logging of authorized users opening and accessing files occurs. However, usage rights aren't enforced. |
| **Default for file types** | Default level of encryption for the following file types:  - Text and image files  - Microsoft Office (Word, Excel, PowerPoint) files  - Portable document format (.pdf) | Default encryption for all other file types (such as .vsd, .rtf, and so on) that aren't supported by native encryption. |

### Supported file types for native encryption

The following table lists a subset of file types that support native encryption when the information protection client applies a sensitivity label with encryption.

These file types are identified separately because, when they're natively encrypted, the original file name extension is changed and these files become read-only. When files are generically encrypted, the original file name extension is always changed to .p*filetype*.

Warning

If you have firewalls, web proxies, or security software that inspect and take action according to file name extensions, you might need to reconfigure these network devices and software to support these new file name extensions.

| Original filename extension | Encrypted file name extension |
| --- | --- |
| .bmp | .pbmp |
| .gif | .pgif |
| .jfif | .pjfif |
| .jpe | .pjpe |
| .jpeg | .pjpeg |
| .jpg | .pjpg |
| .jt | .pjt |
| .png | .ppng |
| .tif | .ptif |
| .tiff | .ptiff |
| .txt | .ptxt |
| .xla | .pxla |
| .xlam | .pxlam |
| .xml | .pxml |

**File types supported by Office**

The following list includes the remaining file types that support labeling and native encryption by the information protection client. You'll recognize these as file types for Microsoft Office apps. The supported file formats for these file types are the 97-2003 file formats and Office Open XML formats for the following Office programs: Word, Excel, and PowerPoint.

For these files, the file name extension remains the same after the file is encrypted.

| Word | Excel | PowerPoint | Visio |
| --- | --- | --- | --- |
| .doc | .xls | .potm | .vdw |
| .docm | .xlsb | .potx | .vsdm |
| .docx | .xlst | .pps | .vsdx |
| .dot | .xlsm | .ppsm | .vss |
| .doctm | .xlsx | .ppsx | .vssm |
| .dotx | .xltm |  | .vst |
|  | .xltx |  | .vstm |
|  |  |  | .vssx |
|  |  |  | .vstx |

---

## Excluded folders and file types

To help prevent users from changing files that are critical for computer operations, some file types and folders are automatically excluded from classifying and labeling. If users try to label these files by using the information protection client, they see a message that those files are excluded.

# [Excluded folders](#tab/excluded-folders)
The following folders are excluded from classifying and labeling by the information protection client:

- Windows
- Program Files (\Program Files and \Program Files (x86))
- \ProgramData
- \AppData (for all users)

# [Excluded file types](#tab/excluded-file-types)
The following file types are excluded from classifying and labeling by the information protection client:

| Extension | Extension | Extension | Extension |
| --- | --- | --- | --- |
| .bat | .dll | .ini | .pdb |
| .cmd | .drm | .jar | .pst |
| .com | .drv | .lnk | .sca |
| .cpl | .exe | .msi | .sys |
| .dat | .inf | .msp | .tmp |

# [Excluded by the scanner](#tab/excluded-by-scanner)
By default, the scanner excludes the same file types from being labeled as the information protection client. It also excludes these file types:

- .msg
- .rtf
- .rar

To change the file types included or excluded for file inspection by the scanner, configure the **File types to scan** in the [content scan job](deploy-scanner-configure-install#configure-the-scanner-settings).

---

### File types that can't be encrypted by default

Any file that is password-protected can't be natively encrypted by the client unless the file is currently open in the application that applies the encryption. You most often see PDF files that are password-protected but other applications, such as Office apps, also offer this functionality.

### File types supported for inspection

The information protection client uses Windows IFilter to inspect the contents of documents. Windows IFilter is used by Windows Search for indexing. As a result, the following file types can be inspected when you use the [Set-FileLabel -Autolabel](https://go.microsoft.com/fwlink/?linkid=2259827) PowerShell command.

| Application type | File type |
| --- | --- |
| Word | .doc, .docx, .docm, .dot, .dotx |
| Excel | .xls, .xlt, .xlsx, .xlsm, .xlsb |
| PowerPoint | .ppt, .pps, .pot, .pptx |
| PDF | .pdf |
| Text | .txt, .xml, .csv |

### Scanning .ZIP files

You can use the information protection scanner or the [Set-FileLabel](https://go.microsoft.com/fwlink/?linkid=2259827) PowerShell command to inspect .zip files.

Note

When your information protection scanner is installed on a Windows server computer, you must also install the Microsoft Office iFilter in order to scan .zip files for sensitive information types. For more information, see the [Microsoft download site](https://www.microsoft.com/download/details.aspx?id=17062).

After finding sensitive information, if the .zip file should be labeled and encrypted with a label, from the scanner deployment instructions, specify the .zip file name extension with the PowerShell **PFileSupportedExtensions** advanced setting.

**Example scenario:**

A file named *accounts.zip* contains Excel spreadsheets with credit card numbers. You have a sensitivity label named *Confidential \ Finance*, which is configured to discover credit card numbers and automatically apply the label with encryption that restricts access to the Finance group.

After inspecting the file, the client from your PowerShell session labels this file as *Confidential \ Finance*. Next, the client applies generic encryption to the file so that only members of the Finance groups can unzip it, and renames the file *accounts.zip.pfile*.

## Integration with Endpoint data loss prevention

The Endpoint data loss prevention (DLP) setting **Advanced label-based protection for all files on devices** enhances productivity for users who label and encrypt file types other than those for Office and PDF.

For these files, although access and any usage restrictions from the encryption settings are enforced by DLP when the label is applied, the encryption is applied when the files leave the computer. As a result, the file name extension for the local files don't change and users can continue to view and edit the files in their standard application.

For more information, see [Learn about Advanced Label Based Protection](dlp-learn-about-advanced-label-protection).

## Support for disconnected computers

By default, the information protection client automatically tries to connect to the internet to download sensitivity labels and sensitivity label policy settings from Microsoft Purview.

If you have computers that can't connect to the internet for a period of time, you can export and copy files that manually manages the policy for the information protection client.

**To support disconnected computers from the information protection client**:

1. Choose or create a user account in Microsoft Entra ID that you will use to download labels and policy settings that you want to use on your disconnected computer.
2. As an additional label policy setting for this account, turn off sending audit data to Microsoft Purview by using the *EnableAudit* PowerShell advanced setting with [Set-LabelPolicy](/en-us/powershell/module/exchange/set-labelpolicy) from Security & Compliance PowerShell.

    We recommend this step because if the disconnected computer does have periodic internet connectivity, it will send logging information to Microsoft Purview that includes the user name from step 1. That user account might be different from the local account you're using on the disconnected computer.
3. From a computer with internet connectivity that has the information protection client installed and signed in with the user account from step 1, download the labels and policy settings.
4. From this computer, export the log files.

    For example, run the [Export-DebugLogs](/en-us/powershell/module/purviewinformationprotection/export-debuglogs) cmdlet, or use the **Export Logs** option from the client's **Help and Feedback** dialog box from file labeler.

    The log files are exported as a single compressed file.
5. Open the compressed file, and from the MSIP folder, copy any files that have an .xml file name extension.
6. Paste these files into the **%localappdata%\Microsoft\MSIP** folder on the disconnected computer.
7. If your chosen user account is one that usually connects to the internet, enable sending audit data again, by setting the **EnableAudit** value to **True**.

Be aware that if a user on this computer selects the **Reset Settings** option from **Help and feedback** in the file labeler, this action deletes the policy files and leaves the client inoperable until you manually replace the files or the client connects to the internet so it can download the files it needs.

The Information Protection client requires an active internet connection to apply encryption; therefore, the disconnected computers solution is supported only for labels that do not apply encryption.

If your disconnected computer is running the information protection scanner, there are additional configuration steps you must take. For more information, see [Restriction: The scanner server cannot have internet connectivity](deploy-scanner-prereqs#restriction-the-scanner-server-cannot-have-internet-connectivity) from the scanner deployment instructions.

## Supported customizations

The information protection client supports PowerShell advanced settings and some registry settings that might be needed for specific scenarios or users.

For the PowerShell advanced settings that are supported with [New-Label](/en-us/powershell/module/exchange/new-label) or [Set-Label](/en-us/powershell/module/exchange/set-label), and [New-LabelPolicy](/en-us/powershell/module/exchange/new-labelpolicy) or [Set-LabelPolicy](/en-us/powershell/module/exchange/set-labelpolicy) from Security & Compliance PowerShell, see [Advanced settings for Microsoft Purview Information Protection client](/en-us/powershell/exchange/client-advanced-settings).

Use the following sections to help you configure the registry for supported customizations.

### Enable non-interactive upgrade from the Azure Information Protection client

If you install the Microsoft Purview Information Protection client and the Azure Information Protection unified labeling client is detected, an interactive installation of the client requires you to acknowledge that the AIP Add-in for Office from the older client will be removed.

To use a non-interactive installation for the client, such as Microsoft Update Catalog, Group Policy, or scripting, you must either first uninstall the Azure Information Protection client, or create and configure the following registry key for the local computer:

**HKEY\_LOCAL\_MACHINE\SOFTWARE\WOW6432Node\Microsoft\MSIP\AllowMajorVersionUpgrade** (DWORD)

Set the value to **1** to silently allow the upgrade and uninstall the AIP Office add-in; **0** blocks the upgrade if the Azure Information Protection client is installed.

### Change the local logging level

By default, the Purview Information Protection client writes client log files to the **%localappdata%\Microsoft\MSIP** folder. These files are intended for troubleshooting by Microsoft Support.

To change the logging level for these files, locate the following value name in the registry and set the value data to the required logging level:

**HKEY\_CURRENT\_USER\SOFTWARE\Microsoft\MSIP\LogLevel**

Set the logging level to one of the following values:

- **Off**: No local logging.
- **Error**: Errors only.
- **Warn**: Errors and warnings.
- **Info**: Minimum logging, which includes no event IDs (the default setting for the scanner).
- **Debug**: Full information.
- **Trace**: Detailed logging (the default setting for clients).

This registry setting doesn't change the information that's sent to Microsoft Purview auditing.

### Enable data boundary settings

Following Microsoft's commitment to EU data boundary, EU customers who use the Microsoft Purview Information Protection client can send their data to the EU to be stored and processed.

Turn on this feature in the information protection client by changing the following registry key that specifies the location to send events:

- Registry key: **HKEY\_LOCAL\_MACHINE\SOFTWARE\WOW6432Node\Microsoft\MSIP\DataBoundary (DWORD)**
- Values:
    - `Default = 0`
    - `North_America = 1`
    - `European_Union = 2`

### Enable system default browser for authentication

Use the system default browser for authentication in Microsoft Purview Information Protection client. By default, the information protection client opens Microsoft Edge for authentication.

Turn on this feature in the information protection client by enabling the following registry key:

- Registry key: **HKEY\_LOCAL\_MACHINE\SOFTWARE\WOW6432Node\Microsoft\MSIP\MSALUseSytemDefaultBrowserAuth (DWORD)**
- Values:
    - `Disabled = 0`
    - `Enabled = 1`

### Hide the "Apply sensitivity label with Microsoft Purview" menu option in File Explorer

To hide the **Apply sensitivity label with Microsoft Purview** right-click menu option in File Explorer, create the following DWORD registry key that has the value name of **LegacyDisable** and any value data:

**HKEY\_CLASSES\_ROOT\AllFilesystemObjects\shell\Microsoft.Azip.RightClick**

## How to apply sensitivity labels using the information protection client

After the Microsoft Purview Information Protection client is installed, you can apply sensitivity labels that you've [created and published](create-sensitivity-labels), by using:

- [File Explorer](https://support.microsoft.com/topic/label-and-protect-files-in-file-explorer-in-windows-67829155-2d0e-4122-9677-7c53c8cba18a)
- [PowerShell](/en-us/powershell/module/purviewinformationprotection)
- The [information protection scanner](deploy-scanner), after installing and configuring it

    Important

    If you are upgrading from the Azure Information Protection (AIP) unified labeling client, see [Upgrade the scanner from the Azure Information Protection client (version 2.x)](upgrade-scanner-migrate#upgrade-the-scanner-from-the-azure-information-protection-client-version-2x).

To view encrypted documents, see [View protected files with the Microsoft Purview Information Protection viewer](https://support.microsoft.com/topic/view-protected-files-with-the-azure-information-protection-viewer-9fb56fae-7989-48b0-850f-f446e057cf73).