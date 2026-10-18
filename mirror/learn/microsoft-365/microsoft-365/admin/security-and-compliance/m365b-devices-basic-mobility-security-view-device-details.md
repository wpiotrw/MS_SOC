---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: View device details in Basic Mobility and Security - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-view-device-details?view=o365-worldwide
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
ms.topic: how-to
ms.service: microsoft-365-security
ms.localizationpriority: medium
ms.collection:
- Tier3
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- basic-mobility-security
- trust-pod
ms.custom:
- AdminSurgePortfolio
- has-azure-ad-ps-ref
- azure-ad-ref-level-one-done
- basic-mobility-security
search.appverid:
- MET150
description: Admins can learn how to view details about devices enrolled in Basic Mobility and Security in the Microsoft 365 admin center and in Microsoft Graph PowerShell.
locale: en-us
document_id: 16ce4e64-4f48-28d1-0b84-3c90d5118302
document_version_independent_id: 16ce4e64-4f48-28d1-0b84-3c90d5118302
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-view-device-details.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/security-and-compliance/m365b-devices-basic-mobility-security-view-device-details
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/security-and-compliance/m365b-devices-basic-mobility-security-view-device-details.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: cea86103-5552-9055-0136-9ff3575a910d
---

# View device details in Basic Mobility and Security - Microsoft 365 admin | Microsoft Learn

In Basic Mobility and Security in Microsoft 365 for Business Basic and Business Standard, you can use the **Active devices** page in the Microsoft 365 admin center or [Microsoft Graph PowerShell](/en-us/powershell/microsoftgraph/overview) to get details about the devices in your organization.

For more information about Basic Mobility and Security, see [Overview of Basic Mobility and Security in Microsoft 365 for business](m365b-devices-basic-mobility-security-overview).

## What do you need to know before you begin?

- You open the **Active devices** page for Basic Mobility and Security at https://admin.microsoft.com/Adminportal/Home?#/IntuneDevices/?isMifo=true.
- If you haven't already, install the Microsoft Graph PowerShell SDK by running the following command in an elevated PowerShell window (a PowerShell window you open by selecting **Run as administrator**):

    ```powershell
    Install-Module Microsoft.Graph -Scope AllUsers
    ```

    Answer yes to any directives about installing the NuGet provider or installing from the PSGallery.
- To run the upcoming script, the PowerShell execution policy on your computer needs to be set to RemoteSigned (it isn't by default). For instructions, see [Set the PowerShell execution policy to RemoteSigned](/en-us/powershell/exchange/exchange-online-powershell-v2#set-the-powershell-execution-policy-to-remotesigned).
- You need to be assigned permissions before you can do the procedures in this article. You have the following options:

    - [Microsoft Entra permissions](/en-us/entra/identity/role-based-access-control/manage-roles-portal): Membership in the **Global Administrator**^\*^ or **Directory Readers** roles gives users the required permissions *and* permissions for other features in Microsoft 365.

        Important

        ^\*^ Microsoft recommends that you use roles with the fewest permissions. Using lower permissioned accounts helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role.
- You can't use a delegated admin account to manage Basic Mobility and Security. For more information about delegated administration, see [Partners: Offer delegated administration](https://support.microsoft.com/office/partners-offer-delegated-administration-26530dc0-ebba-415b-86b1-b55bc06b073e).
- Questions? See the [Basic Mobility and Security FAQ](m365b-devices-basic-mobility-security-overview#basic-mobility-and-security-faq).

## Use the Active devices page to view device details

On the **Overview** tab of the Basic Mobility and Security page at https://compliance.microsoft.com/basicmobilityandsecurity, select **Manage devices**. Or, to go directly to the **Active devices** page, use https://admin.microsoft.com/Adminportal/Home?#/IntuneDevices/?isMifo=true.

On the **Fully managed** tab of the **Active Devices** page, the following properties are displayed in the list of devices:

- **Device name**
- **Display name**
- **Username**
- **OS**
- **Device action**
- **Last check-in**

To change the list of devices from normal to compact spacing, select ![](../../media/m365-cc-sc-standard-icon.png)**Change list spacing to compact or normal**, and then select ![](../../media/m365-cc-sc-compact-icon.png)**Compact list**.

Use the ![](../../media/m365-cc-sc-search-icon.png)**Search** box and a corresponding value to find specific devices.

To view details about a specific device, click anywhere in the row other than the check box next to the first column. The details flyout that opens contains the following information:

- **Display name**
- **Username**
- **OS version**
- **Device action**
- **Last check-in**
- **Management type**
- **Serial number**

Tip

To take action on a device (![](../../media/m365-cc-sc-factory-reset-icon.png)**Factory reset**, ![](../../media/m365-cc-sc-remove-company-data-icon.png)**Remove company data**, or ![](../../media/m365-cc-sc-delete-icon.png)**Delete**), see [Wipe devices enrolled in Basic Mobility and Security](m365b-devices-basic-mobility-security-wipe-devices).

## Use Microsoft Graph PowerShell to view device details

Device cmdlets in Microsoft Graph PowerShell show the enrollment and compliance status of recognized devices:

- *isManaged*property:
    - **True**: The device is enrolled in Basic Mobility and Security.
    - **False**: The device isn't enrolled in Basic Mobility and Security.
- *isCompliant*property:
    - **True**: The device is compliant with the [settings of the applicable policy](m365b-devices-basic-mobility-security-overview#policy-settings-in-basic-mobility-and-security) in Basic Mobility and Security.
    - **False**: The device isn't compliant with the settings of the applicable policy in Basic Mobility and Security.

This information is illustrated in the following diagram:

[![Diagram showing the device enrollment and device compliance states in Basic Mobility and Security.](../../media/basic-mobility-security-device-info.png)](../../media/basic-mobility-security-device-info.png#lightbox)

### Use the Get-MgDevice cmdlet to view device details

1. Open a PowerShell window and connect to your Microsoft 365 organization in Microsoft Graph by running the following command:

    ```powershell
    Connect-MgGraph -Scopes Device.Read.All,User.Read.All
    ```

    For more information about connecting, see [Sign in to Microsoft Graph PowerShell](/en-us/powershell/microsoftgraph/get-started#sign-in).
2. Run the following command:

    ```powershell
    Get-MgDevice -All -ExpandProperty "registeredOwners" | Where-Object {($_.RegisteredOwners -ne $null) -and ($_.RegisteredOwners.Count -gt 0)}
    ```

Depending on the width of your screen, the width of the PowerShell window, and the font size in the PowerShell window, the following information is shown:

- DeletedDateTime
- Id
- AccountEnabled
- ApproximateLastSignInDateTime
- ComplianceExpirationDateTime
- DeviceId
- DeviceMetadata
- DeviceVersion
- DisplayName
- IsCompliant
- IsManaged

For detailed syntax and parameter information, see [Get-MgDevice](/en-us/powershell/module/microsoft.graph.identity.directorymanagement/get-mgdevice).

### Create a PowerShell script to get device details

1. Copy the following text into Notepad and save it as `Get-MgGraphDeviceOwnership.ps1` (a PowerShell script file) in a place that's easy to find. For example, save the file to the C:\My Documents folder.

    ```powershell
    param (
        [Parameter(Mandatory = $false)]
        [PSObject[]]$Users = @(),
        [Parameter(Mandatory = $false)]
        [Switch]$Export,
        [Parameter(Mandatory = $false)]
        [String]$ExportFileName = "UserDeviceOwnership_" + (Get-Date -Format "yyMMdd_HHMMss") + ".csv",
        [Parameter(Mandatory = $false)]
        [String]$ExportPath = [Environment]::GetFolderPath("Desktop")
    )
    
    #Clearing the screen
    Clear-Host
    
    #Preparing the output object
    $deviceOwnership = @()

    if ($users.Count -eq 0) {
        Write-Output "No user has been provided, gathering data for all devices in the tenant"
        #Getting all Devices and their registered owners
        $devices = Get-MgDevice -All -Property * -ExpandProperty registeredOwners
    
        #For each device which has a registered owner, extract the device data and the registered owner data
        foreach ($device in $devices) {
            $DeviceOwners = $device | Select-Object -ExpandProperty 'RegisteredOwners'
            #Checking if the DeviceOwners Object is empty
            if ($DeviceOwners -ne $null) {
                foreach ($DeviceOwner in $DeviceOwners) {
                    $OwnerDictionary = $DeviceOwner.AdditionalProperties
                    $OwnerDisplayName = $OwnerDictionary.Item('displayName')
                    $OwnerUPN = $OwnerDictionary.Item('userPrincipalName')
                    $OwnerID = $deviceOwner.Id
                    $deviceOwnership += [PSCustomObject]@{
                        DeviceDisplayName             = $device.DisplayName
                        DeviceId                      = $device.DeviceId
                        DeviceOSType                  = $device.OperatingSystem
                        DeviceOSVersion               = $device.OperatingSystemVersion
                        DeviceTrustLevel              = $device.TrustType
                        DeviceIsCompliant             = $device.IsCompliant
                        DeviceIsManaged               = $device.IsManaged
                        DeviceObjectId                = $device.Id
                        DeviceOwnerID                 = $OwnerID
                        DeviceOwnerDisplayName        = $OwnerDisplayName
                        DeviceOwnerUPN                = $OwnerUPN
                        ApproximateLastLogonTimestamp = $device.ApproximateLastSignInDateTime
                    }
                }
            }
    
        }
    }
    
    else {
        #Checking that userid is present in the users object
        Write-Output "List of users has been provided, gathering data for all devices owned by the provided users"
        foreach ($user in $users) {
            $devices = Get-MgUserOwnedDevice -UserId $user.Id -Property *
            foreach ($device in $devices) {
                $DeviceHashTable = $device.AdditionalProperties
                $deviceOwnership += [PSCustomObject]@{
                    DeviceId                      = $DeviceHashTable.Item('deviceId')
                    DeviceOSType                  = $DeviceHashTable.Item('operatingSystem')
                    DeviceOSVersion               = $DeviceHashTable.Item('operatingSystemVersion')
                    DeviceTrustLevel              = $DeviceHashTable.Item('trustType')
                    DeviceDisplayName             = $DeviceHashTable.Item('displayName')
                    DeviceIsCompliant             = if ($DeviceHashTable.ContainsKey('isCompliant')) {$DeviceHashTable.Item('isCompliant')} else {$null}
                    DeviceIsManaged               = if ($DeviceHashTable.ContainsKey('isManaged')) {$DeviceHashTable.Item('isManaged')} else {$null}
                    DeviceObjectId                = $device.Id
                    DeviceOwnerUPN                = $user.UserPrincipalName
                    DeviceOwnerID                 = $user.Id
                    DeviceOwnerDisplayName        = $user.DisplayName
                    ApproximateLastLogonTimestamp = $DeviceHashTable.Item('approximateLastSignInDateTime')
                }
            }
        }
    
    }
    
    $deviceOwnership
    
    if ($export) {
        $exportFile = Join-Path -Path $exportPath -ChildPath $exportFileName
        $deviceOwnership | Export-Csv -Path $exportFile -NoTypeInformation
        Write-Output "Data has been exported to $exportFile"
    }
    ```
2. Open a PowerShell window and connect to your Microsoft 365 organization in Microsoft Graph by running the following command:

    ```powershell
    Connect-MgGraph -Scopes Device.Read.All,User.Read.All
    ```

    For more information about connecting, see [Sign in to Microsoft Graph PowerShell](/en-us/powershell/microsoftgraph/get-started#sign-in).
3. Use the following syntax to run the script:

    ```powershell
    & <path to script>\Get-MgGraphDeviceOwnership.ps1 [-Users <UserIds>] [-Export] [-ExportPath "<File path>"] [-ExportFileName "<FileName>"]
    ```

    - If you don't use the *Users* parameter the script returns information about all devices in the organization. The upcoming examples show how to use the *Users* parameter for individual users or group members.
    - The *Export* switch exports the results of the script to a CSV file. If you don't use the *ExportPath* or *ExportFileName* parameters, the default path is the Desktop folder, and the default filename is `UserDeviceOwnership_<Date>_<Time>.csv`.
    - If you go to the folder where the script is located (for example, run the command `cd C:\My Documents` in the PowerShell window), you can replace `& C:\My Documents\` with `.\` in all commands when you run the script.

This example returns device details for the specified user.

```powershell
& C:\My Documents\Get-MgGraphDeviceOwnership.ps1 -Users (Get-MgUser -UserId "laura@contoso.com")
```

This example returns device details for users in the FinanceStaff security group and exports the results to the specified file and location.

```powershell
$groupId = Get-MgGroup -Filter "displayName eq 'FinanceStaff'" | Select-Object -ExpandProperty Id

$Users = Get-MgGroupMember -GroupId $groupId | Select-Object -ExpandProperty Id | ForEach-Object {Get-MgUser -UserId $_}

& C:\My Documents\Get-MgGraphDeviceOwnership.ps1 -User $Users -Export -ExportPath "C:\My Documents" -ExportFileName "Contoso FinanceStaff Devices 2024-12-19.csv"
```