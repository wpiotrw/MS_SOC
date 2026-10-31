---
layout: Conceptual
title: Export Cloud PC names for Windows 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/export-cloud-pc-names
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn how to export Cloud PC names for Windows 365
keywords: 
author: ErikjeMS
ms.author: stdowns
manager: dougeby
ms.date: 2024-08-28T00:00:00.0000000Z
ms.topic: how-to
ms.service: windows-365
ms.subservice: 
ms.localizationpriority: high
ms.assetid: 
ms.reviewer: naramkri
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier2
locale: en-us
document_id: da381ae3-98b0-5990-fb64-54879ddd38a4
document_version_independent_id: da381ae3-98b0-5990-fb64-54879ddd38a4
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/export-cloud-pc-names.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: export-cloud-pc-names
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/export-cloud-pc-names.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 8f49e239-3945-a559-1e3b-5e3523088b8c
---

# Export Cloud PC names for Windows 365 | Microsoft Learn

You can export the Cloud PC name of every Cloud PC on your tenant.

1. Sign in to a Cloud PC with a user who has at least the Cloud PC reader RBAC role within Intune.
2. Open PowerShell and type `Install-Module Microsoft.Graph -Scope CurrentUser`.
3. Enter **Y** in all confirmation dialogs.
4. Wait for the installation to finish then close PowerShell.
5. Open a text editor like Visual Studio Code.
6. In a new file paste the following script:

```
param(
    [Parameter(Mandatory)]
    [string]$Output
)

Select-MgProfile -Name "beta"
Connect-MgGraph -Scopes "CloudPC.Read.All"
$CloudPCs = Get-MgDeviceManagementVirtualEndpointCloudPC -Property "DisplayName"
$DisplayNames = $CloudPCs | Select -ExpandProperty DisplayName
Write-Output $DisplayNames

$Outarray = @()

foreach ( $Name in $DisplayNames )
{
    $Outarray += New-Object PsObject -property @{
    'DisplayName' = $Name
     }
}
$Outarray | Export-Csv -Path $Output -NoTypeInformation
Disconnect-MgGraph
```

1. Save the file as “GetCloudPCNames.ps1” in a location of your choice.
2. In the file explorer, navigate to your file location.
3. Right-click on the file and select **Run with PowerShell**.
4. A PowerShell window will pop up. In the window, type “CloudPCNames.csv” and then press enter.
5. When the authentication Window pops up, sign in with the same account you used to access the Cloud PC.

When the PowerShell window closes, the script has finished running. Go back to the location of your script and there will be a file called “CloudPCNames.csv”. This file includes the list of all Cloud PC names on your tenant.