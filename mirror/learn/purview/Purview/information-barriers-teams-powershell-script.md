---
layout: Conceptual
title: Change Information Barriers modes with a PowerShell script | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/information-barriers-teams-powershell-script
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use this PowerShell script after you deploy Information Barriers to update the mode from open to implicit for all groups in your tenant.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.topic: article
ms.date: 2026-03-30T00:00:00.0000000Z
ms.service: purview
ms.subservice: purview-information-barriers
audience: Admin
f1.keywords:
- NOCSH
search.appverid: MET150
ms.collection:
- purview-compliance
- M365-collaboration
ai-usage: ai-assisted
ms.custom: sfi-ga-nochange
locale: en-us
document_id: 02dd46df-0a94-9302-d07a-f46da635d2cb
document_version_independent_id: 02dd46df-0a94-9302-d07a-f46da635d2cb
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/information-barriers-teams-powershell-script.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: information-barriers-teams-powershell-script
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/information-barriers-teams-powershell-script.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 4607567c-2983-546e-e204-c9032e5746a8
---

# Change Information Barriers modes with a PowerShell script | Microsoft Learn

Use this PowerShell script to update the Information Barriers (IB) mode for all Teams-connected groups in your tenant. You need to update the mode for these groups after you deploy Information Barriers. Groups created before you enable IB are assigned the *Open* mode. In *Open* mode, there aren't any applicable IB policies. After you enable IB, *Implicit* becomes the default mode for any new groups you create. However, existing groups still keep *Open* mode configuration. Run this script to change these existing groups to *Implicit* mode.

In this script, you use the [Get-UnifiedGroup](/en-us/powershell/module/exchange/Get-UnifiedGroup?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) cmdlet, which is in the Exchange Online PowerShell module to update the mode. For more information about managing Teams using PowerShell, see [Teams PowerShell overview](/en-us/microsoftteams/teams-powershell-overview?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

## Prerequisites

Before you run this script, make sure you have the following prerequisites:

- The [Exchange Online PowerShell module](/en-us/powershell/exchange/exchange-online-powershell-v2?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) installed.
- A work or school account that has the global administrator role for your tenant.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

## Run the script

Complete the following steps to update the IB mode for all existing Teams-connected groups:

1. Connect to Exchange Online PowerShell:

    ```powershell
    Connect-ExchangeOnline
    ```
2. Copy and run the following script. The script identifies all Teams-connected groups in *Open* mode and updates them to *Implicit* mode.
3. After the script finishes, review the output for the number of groups successfully updated. If any groups fail to update, check the `BackfillFailedTeams.csv` file generated in your current directory for details and retry the failed groups.

## Sample script

```powershell
<#
.SYNOPSIS
This script updates the IB mode for all Teams-connected groups in your tenant at the same time.
.DESCRIPTION
Use this script to update the info barrier mode from open to implicit across the groups in your tenant.
#>

$teams = Get-UnifiedGroup -Filter {ResourceProvisioningOptions -eq "Team"} -ResultSize Unlimited

Write-Output ([string]::Format("Number of Teams = {0}", @($teams).Length))

$teamsToUpdate = New-Object System.Collections.ArrayList

foreach($team in $teams)
{
  if ($team.InformationBarrierMode -eq "Open")
  {
    $teamsToUpdate.Add($team.ExternalDirectoryObjectId) | out-null
  }
}

Write-Output ([string]::Format("Number of Teams to be backfilled = {0}", @($teamsToUpdate).Length))

$outfile = "BackfillFailedTeams.csv"

if (!(Test-Path "$outfile"))
{
  $newcsv = {} | Select "ExternalDirectoryObjectId", "ExceptionDetails" | Export-Csv $outfile -NoTypeInformation
}
else
{
  $dateTime = Get-Date
  $newEntry = "{0},{1}" -f "New session started", $dateTime
  $newEntry | add-content $outfile
}

$SuccessfullyBackfilledGroup = 0

for($i = 0; $i -lt @($teamsToUpdate).Length; $i++)
{
  Invoke-Command { Set-UnifiedGroup $teamsToUpdate[$i] -InformationBarrierMode "Implicit" } -ErrorVariable ErrorOutput

  if ($ErrorOutput)
  {
    # saving the errors in a csv file
    $errorBody = $ErrorOutput[0].ToString() -replace "`n"," " -replace "`r"," " -replace ",", " "
    $newEntry = "{0},{1}" -f $teamsToUpdate[$i].ToString(), '"' + $errorBody + '"'
    $newEntry | add-content $outfile
  }
  else
  {
    $SuccessfullyBackfilledGroup++
  }

  if (($i+1) % 100 -eq 0)
  {
    # print the number of teams backfilled after the batch of 100 updates
    Write-Output ([string]::Format("Number of Teams processed= {0}", $i+1))
  }
}

Write-Output ([string]::Format("Backfill completed. Groups backfilled: {0}, Groups failed to backfill: {1}", $SuccessfullyBackfilledGroup, @($teamsToUpdate).Length - $SuccessfullyBackfilledGroup))

if (!($SuccessfullyBackfilledGroup -eq @($teamsToUpdate).Length))
{
  Write-Output ([string]::Format("Check the failed teams in BackfillFailedTeams.csv, retry to backfill the failed teams."))
}

```