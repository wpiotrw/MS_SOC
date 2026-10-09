---
layout: Conceptual
title: Automated provisioning steps for Windows 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/automated-provisioning-steps
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn about the automated steps that Windows 365 conducts to provision a Cloud PC.
keywords: 
author: ErikjeMS
ms.author: scottduf
manager: dougeby
ms.date: 2024-07-31T00:00:00.0000000Z
ms.topic: overview
ms.service: windows-365
ms.subservice: windows-365-enterprise
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: mattsha
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: 455a0979-f43c-3cd3-71f0-3dbe6a8fc35f
document_version_independent_id: 455a0979-f43c-3cd3-71f0-3dbe6a8fc35f
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/automated-provisioning-steps.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/automated-provisioning-steps
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/automated-provisioning-steps.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: fd99b2d0-177d-4cf9-ead9-057901d35155
---

# Automated provisioning steps for Windows 365 | Microsoft Learn

As an admin, you create provisioning policies and Azure network connections to set up Windows 365 to provision Cloud PCs. Using this information, Windows 365 provisions Cloud PCs for your licensed users. This article explains all of the steps that Windows 365 completes automatically in the provisioning process.

There are three stages that Windows 365 automatically completes for Cloud PC provisioning:

1. **Core provisioning**: Core provisioning performs every task required to stand up a VM and get it to the point of successful user sign-in.
2. **Post-provisioning configuration**: Windows 365 makes Configuration changes to optimize the Cloud PC end-user experience.
3. **Assignment**: Windows 365 assigns the user to the Cloud PC and the user can now sign in.

## Core provisioning

Windows 365 optimizes core provisioning to only perform necessary steps to make sure a Cloud PC is provisioned successfully.

1. **Allocate Azure capacity**: When provisioning first begins, Windows 365 allocates Azure capacity in the customer’s supported region of choice. Customers don’t need to manage capacity and allocation manually.
2. **Create VM**: Windows 365 creates a virtual machine based on the Windows 365 license assigned to the user. Each Windows 365 license includes hardware capacity information. The VM is created with these specifications.
3. **Attach the VM to the appropriate network**: When Windows 365 creates the VM, a virtual NIC is also created. If the provisioning policy specifies a Microsoft hosted network, the NIC is attached to an existing or new virtual network in the selected region specifically for the customer. If the provisioning policy specifies an Azure network connection, the NIC is injected into the customers provided vNet. This step lets the Cloud PC connect to the customers on-premises network.
4. **Join to Microsoft Entra ID**: After the VM is running, the device joins Microsoft Entra ID in one of two ways:

    - Through Microsoft Entra join: the device performs the Microsoft Entra join operation and has no Windows Server Active Directory dependency.
    - Through Microsoft Entra hybrid join: the device performs the domain join operation on the customer’s domain and is then registered to Microsoft Entra ID through synchronization or federation. In this step, we wait for the computer object to appear in Microsoft Entra ID before proceeding.
5. **Intune MDM enroll**: After the Microsoft Entra ID object is available, the Cloud PC enrolls in Intune. This device enrollment doesn't need user credentials.
6. **Primary user assignment**: The Windows 365 service assigns the Cloud PC user to the Intune primary user to make sure self service and reporting scenarios work seamlessly.

## Post provisioning configuration

After core provisioning is complete, Windows 365 optimizes the configuration to ensure the best end-user Cloud PC experience.

1. **Hide Start Menu power icons**: Hide the shutdown button in the start menu (`HKLM:\Software\Microsoft\PolicyManager\default\Start\HideShutDown\value`) and Hide the shutdown button in the sign-in screen (`HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System\ShutDownWithoutLogon`).
2. **Disable Windows reset action**: reagentc.exe /disable
3. **Assign user as administrator (when applicable)**: `$Member = 'user@contoso.com'  # use OnPremisesUserPrincipalName``Add-LocalGroupMember -Group "Administrators" -Member $Member`
4. **Set Teams for VDI mode**: Hosted desktop optimization (`HKLM:\Software\Microsoft\Teams\IsWVDEnvironment`).
5. **Enable time zone Redirection**: Enable the setting (`HKLM:\Software\Policies\Microsoft\Windows NT\Terminal Services\fEnabletimezoneRedirection`).
6. **Resize OS disk partition to match license**: Resize the OS disk to match the size of the Azure Managed Disk.

    ```
    $MaxSize = (Get-PartitionSupportedSize -DriveLetter $DriveLetter -ErrorAction Stop).SizeMax
    if((Get-Partition -DriveLetter $DriveLetter).Size -lt $MaxSize){
    Resize-Partition -DriveLetter $DriveLetter -Size $MaxSize
    }```
    
    ```
7. **Disable port 3389 by default**: To help secure your Windows 365 environment, by default Windows 365 disables open inbound port 3389 on your Cloud PCs. Windows 365 doesn't require an open inbound port. If you must open port 3389 for troubleshooting purposes, it's best to use just-in-time access.
8. **Enable OneDrive**: Enable the following [OneDrive policies](/en-us/sharepoint/use-group-policy#list-of-policies-by-string-id): SilentAccountConfig, FilesonDemandEnabled, MinDiskSpaceLimitInMB, EnableAutomaticUploadBandwidthManagement, KFMSilentOptIn
9. **PowerShell execution policy**: Windows 365 sets the PowerShell execution policy to RemoteSigned at the LocalMachine scope during provisioning. This allows locally created scripts and scripts run through the Custom Script Extension (CSE) to run, while requiring downloaded scripts to be digitally signed. If the execution policy is set to AllSigned through Intune or Group Policy (MachinePolicy), it can override this default and cause provisioning and related operations to fail.

Unlike core provisioning, if one or more of these optimizations fail for some reason, provisioning will still succeed. The Cloud PC will be marked as **Success with warnings** and the process will move onto the assignment stage.

If an optimization fails, you can manually trigger a reprovisioning if you prefer to see post provisioning configuration succeed.

## Assignment

After core provisioning and post provisioning configuration workflows are complete, Windows 365 assigns the relevant user to the Cloud PC.

At this point, the user can sign in to https://windows365.microsoft.com and access their Cloud PC.