---
layout: Conceptual
title: Learn about advanced label based protection | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-learn-about-advanced-label-protection
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-07-15T00:00:00.0000000Z
audience: ITPro
ms.topic: article
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- highpri
- purview-compliance
search.appverid:
- MET150
description: Learn how to protect your files with encryption without slowing down workflow.
locale: en-us
document_id: f2b79cb2-cb1e-e044-b6d3-96ba4c0cf6b6
document_version_independent_id: f2b79cb2-cb1e-e044-b6d3-96ba4c0cf6b6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-learn-about-advanced-label-protection.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-learn-about-advanced-label-protection
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-learn-about-advanced-label-protection.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: d32d663b-197d-6492-e7aa-62d1b310696f
---

# Learn about advanced label based protection | Microsoft Learn

This setting enhances productivity for users that label and encrypt file types other than those for Office and PDF by using the [Microsoft Purview Information Protection client](information-protection-client). Typical examples of file types other than Office and PDF include .txt, .jpg, .csv, and files from third-party applications.

When users label and encrypt these files with the information protection client and without this setting for advanced label-based protection:

- The encrypted file changes its file name extension and becomes read-only, and can no longer be opened by apps that support the original file name extension. Instead, the file opens in the [Microsoft Purview Information Protection viewer](https://support.microsoft.com/topic/view-protected-files-with-the-azure-information-protection-viewer-9fb56fae-7989-48b0-850f-f446e057cf73). To make any changes to the file, users must manually remove the label with encryption.
- Although the encryption can include restrictive permissions, such as not allowing copy and save for specific users, not all files can support these restrictions. As a result, when these files are opened in the information protection viewer, users are informed of the configured permissions, but the permissions can’t be enforced. This type of encryption is referred to as generic, rather than native.

For a better understanding of the file name extension changes for encrypted files, see [Supported file types](information-protection-client?tabs=devices,install-client-exe,protection-file-types,excluded-folders#supported-file-types) from the information protection client documentation. Also be aware of the standard client exceptions for [files that are critical for computer operations](information-protection-client?tabs=devices,install-client-exe,classification-file-types,excluded-folders#excluded-folders-and-file-types).

When you configure users for the endpoint data loss prevention setting **Advanced label-based protection for all files on devices** and use the information protection client, the following changes occur for file types that aren’t supported by Office or that are PDF files:

- When a user selects a sensitivity label that applies encryption, the file name extension now doesn't change. As a result, there's no change to the user workflow because they can continue to view and edit the file in their standard application. Endpoint DLP tracks and monitors the file, enforcing configured permissions without requiring the information protection viewer.

Note

Because the file name extension hasn't changed, users can confirm that the label is applied by using the [Microsoft Purview Information Protection File Labeler](https://support.microsoft.com/topic/label-and-protect-files-in-file-explorer-in-windows-67829155-2d0e-4122-9677-7c53c8cba18a).

- Only if the user copies or moves the file from the computer, does the file name change:
    - If the file is copied or moved to a network drive or USB device, the file there has the changed file name extension that requires the information protection viewer to open it.
    - If the file is copied or moved to any other location (Bluetooth device, over remote desktop, or uploaded to the cloud), a local copy of the file is created with the changed file name extension that requires the information protection viewer to open it. Endpoint DLP informs the user that they must use this version of the file to manually copy or move it to the new location.
    - If the operation to encrypt the file fails, the copy or move activity is blocked to ensure that the unencrypted file remains on the device and isn't exfiltrated.

Here's a summary of the differences when you label files other than Office and PDF and you use just the information protection client rather than the client with endpoint DLP advanced label-based protection:

| Labeling behavior | Just the client | The client with endpoint DLP setting enabled |
| --- | --- | --- |
| Files labeled with encryption retain their original file name extension | No The file name extension always changes | Yes The file extension is changed when egress happens. |
| Files labeled with encryption can be opened and edited with the original application or others that support the original file type | No Always requires the information protection viewer | Yes  The file extension is changed when egress happens. |
| Configured permissions for labeled and encrypted files are enforced | Native encryption: Yes Generic encryption: No | Yes  The following permissions are enforced until egress: view, extract, print |

## Prepare your Windows devices

Make sure that the Windows devices that you need to onboard meet these requirements:

- Anti-malware Client Version 4.18.25050 or newer is required.
- Window build:

    - Windows 10: [See update details](https://support.microsoft.com/en-us/topic/june-10-2025-kb5060533-os-builds-19044-5965-and-19045-5965-eeae388c-ca1c-4569-95d7-3d7be2e0b8ba)
    - Windows 11 22H2: [See update details](https://support.microsoft.com/en-us/topic/june-10-2025-kb5060999-os-builds-os-builds-22621-5472-and-22631-5472-97dbff21-2edb-4566-be47-18f732a218b9)
    - Windows 11 23H2: [See update details](https://support.microsoft.com/en-us/topic/june-10-2025-kb5060999-os-builds-os-builds-22621-5472-and-22631-5472-97dbff21-2edb-4566-be47-18f732a218b9)
    - Windows 11 24H2: [See update details](https://support.microsoft.com/en-us/topic/june-11-2025-kb5063060-os-build-26100-4351-out-of-band-b1746442-8c6c-425d-ac5a-3a8f51e372f3)
- Information protection client version: 3.1.309 or newer is required.

## User experience

| Labeling scenario | Activity | User experience | Activity explorer |
| --- | --- | --- | --- |
| File being labeled | Information protection File Labeler | A user right-clicks to open Information Protection Viewer to label specific file. The user can assign a label through the Viewer, Endpoint DLP will assign the label to the file but keep the file in original extension. | Label applied, no DLP Rule Matched, no Alert |
| Labeled file being moved off of the device | File copied to removable media, File copied to network share | A user moves a labeled file to a removable media or network share, the file will be encrypted, e.g. .ptxt file extension, when land on the network share or removable media with a Windows toast. This version of the file must be opened with the information protection viewer and can't be monitored by DLP. | File copied to USB removable device or File copied to a network share, no DLP Rule Matched, no Alert |
| Labeled file being moved off of the device | File transferred through Bluetooth, File transferred over remote desktop, or File uploaded to the cloud | A user uploads a labeled file out of the machine through listed channels, the activity will be blocked, a copy of the file will be created, and the copied file will be encrypted, e.g. .ptxt file extension, a toast will pop up asking the user to retry the operation with the labeled new copy. This version of the file must be opened with the information protection viewer and can't be monitored by DLP. The original file on the computer retains the .txt file extension and can still be opened and edited with any text editor. DLP continues to monitor this file. | File copied or moved using unallowed Bluetooth app or File copied or moved using RDP or File copied to cloud app |
| Encrypted file being moved on the device that is using this feature, for example .ptxt | Information protection Viewer | A user moves an encrypted labeled file into a machine that has this feature onboarded, the file will be kept in encrypted extension, the user can double-click to open the Information Protection Viewer. The Information Protection Viewer will pop up a notification, user can click Continue button to decrypt the file to original file extension with label assigned. |  |
| Encrypted file being moved on the device that is using this feature onboarded, for example .ptxt | Information protection File Labeler | A user moves an encrypted labeled file into a machine that has this feature onboarded, the file will be kept in encrypted extension, the user can right-click to open the Information Protection Viewer. The user can change the label through the Viewer, the file will be kept in encrypted format. | Label changed, Label removed, Protection applied, Protection removed. |
| Labeled file being opened through a native application | N/A | A user opens a labeled file through a native application, and perform Print or Copy activity which violate the permission associated with the label, the activity will be blocked with a toast. | File copied to clipboard or File printed, no DLP Rule Matched, no Alert |

## Considerations

- Supported only for sensitivity labels that apply encryption. For sensitivity labels without encryption, the behavior and supported file types are the [same as for the information protection client](information-protection-client?tabs=devices,install-client-exe,classification-file-types,excluded-folders#supported-file-types).
- Not supported for labeling files on network locations or USB drives.
- The applied sensitivity labels won't be detected as [conditions in DLP policies](dlp-sensitivity-label-as-condition) before egress.
- When multiple files are selected for labeling, and they include Office files or PDF files, the Office files, and PDF files won't be labeled or encrypted. User will see failure message on the Information Protection File Labeler application.
- Endpoint DLP doesn't enforce all [rights management usage rights](rights-management-usage-rights#usage-rights-and-descriptions) before egress: VIEW, EXTRACT, and PRINT are supported.
- The Save As option doesn't automatically inherit the current label and encryption settings. The user must label the new file.
- The [Microsoft Purview Information Protection PowerShell module](/en-us/powershell/module/purviewinformationprotection) doesn't recognize the DLP setting. Labeling files using PowerShell will encrypt and change the file extension. Only use the [Microsoft Purview Information Protection File Labeler](https://support.microsoft.com/topic/label-and-protect-files-in-file-explorer-in-windows-67829155-2d0e-4122-9677-7c53c8cba18a) when you enable the DLP setting.