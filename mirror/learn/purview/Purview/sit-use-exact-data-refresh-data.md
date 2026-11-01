---
layout: Conceptual
title: Refresh your exact data match sensitive information source table file | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-use-exact-data-refresh-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-sensitive-information-types
ms.date: 2026-06-22T00:00:00.0000000Z
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Learn how to refresh your sensitive information source table file on a one time basis or set up automated recurring refresh cycles.
ms.custom: msecd-doc-authoring-1014, seo-marvel-apr2020, sfi-ropc-nochange
ai-usage: ai-assisted
locale: en-us
document_id: 6cd8e46d-d858-6fb4-2af7-485af80b6efb
document_version_independent_id: 6cd8e46d-d858-6fb4-2af7-485af80b6efb
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-use-exact-data-refresh-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-use-exact-data-refresh-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-use-exact-data-refresh-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/60932d05-feee-4685-a73b-595e25dd9318
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/c43bb58b-1190-419b-8d18-e6052371b599
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 2dd7de67-c46a-156d-262b-8f4aebff4f7b
---

# Refresh your exact data match sensitive information source table file | Microsoft Learn

## Refresh an exact data match sensitive information database

This article explains how to refresh the sensitive information source table used by exact data match (EDM) sensitive information types in Microsoft Purview. Use this procedure when your source data changes and you need to update the uploaded data. Compliance administrators can refresh the database up to 5 times in every 24-hour period by rehashing and reuploading the sensitive information source table. Each refresh overwrites the existing sensitive information source table with the new one.

1. Re-export the sensitive data to an app, such as Microsoft Excel, and save the file in .csv, .tsv format or pipe-delimited (|) format. Keep the same file name and location you used when you previously hashed and uploaded the file. See, [Export source data for exact data match based sensitive information types](sit-get-started-exact-data-match-export-data#export-source-data-for-exact-data-match-based-sensitive-information-types) for details on exporting your sensitive data and getting it into the correct format.

    Note

    If there are no changes to the structure (field names) of the sensitive information source table file, you won't need to make any changes to your database schema file when you refresh the data. But if you must make changes, make sure to edit the database schema and your rule package accordingly. See, [Manage your exact data match schema](sit-use-exact-data-manage-schema#manage-your-exact-data-match-schema) for the steps to edit or remove a schema. To learn how to dit or remove your EDM SIT/rule package, see [Create exact data match sensitive information type/rule package](sit-get-started-exact-data-match-create-rule-package#create-exact-data-match-sensitive-information-typerule-package).
2. Use the procedures in [Hash and upload the sensitive information source table for exact data match sensitive information types](sit-get-started-exact-data-match-hash-upload#hash-and-upload-the-sensitive-information-source-table-for-exact-data-match-sensitive-information-types) to upload your sensitive information table source file.
3. You can use [Task Scheduler](/en-us/windows/desktop/TaskSchd/task-scheduler-start-page) to automate the [Hash and upload the sensitive information source table for exact data match sensitive information types](sit-get-started-exact-data-match-hash-upload#hash-and-upload-the-sensitive-information-source-table-for-exact-data-match-sensitive-information-types) procedure. You can schedule tasks using several methods:

    | Method | What to do |
    | --- | --- |
    | PowerShell | See the [ScheduledTasks](/en-us/powershell/module/scheduledtasks/) documentation and the Example PowerShell script for Task Scheduler |
    | Task Scheduler API | See the [Task Scheduler](/en-us/windows/desktop/TaskSchd/using-the-task-scheduler) documentation |
    | Windows user interface | In Windows, click **Start**, and type Task Scheduler. Then, in the list of results, right-click **Task Scheduler**, and choose **Run as administrator**. |

## Example PowerShell script for Task Scheduler

The following examples include PowerShell scripts you can use to schedule tasks for hashing data and uploading hashed data:

### Schedule hashing and upload in a combined step

Use the following PowerShell script to schedule hashing and upload as a single combined task:

```powershell
param(\[string\]$dataStoreName,\[string\]$fileLocation)
\# Assuming current user is also the user context to run the task
$user = "$env:USERDOMAIN\\$env:USERNAME"
$edminstallpath = 'C:\\Program Files\\Microsoft\\EdmUploadAgent\\'
$edmuploader = $edminstallpath + 'EdmUploadAgent.exe'
$csvext = '.csv'
$schemaext = '.xml'
\# Assuming file name is same as data store name and file is in .csv format
$dataFile = "$fileLocation\\$dataStoreName$csvext"
\# Assuming location to store hash file is same as the location of csv file
$hashLocation = $fileLocation
\# Assuming Schema file name is same as data store name
$schemaFile = "$fileLocation\\$dataStoreName$schemaext"
$uploadDataArgs = '/UploadData /DataStoreName ' + $dataStoreName + ' /DataFile ' + $dataFile + ' /HashLocation' + $hashLocation + ' /Schema ' + $schemaFile
\# Set up actions associated with the task
$actions = @()
$actions += New-ScheduledTaskAction -Execute $edmuploader -Argument $uploadDataArgs -WorkingDirectory $edminstallpath
\# Set up trigger for the task
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 2am
\# Set up task settings
$principal = New-ScheduledTaskPrincipal -UserId $user -LogonType S4U -RunLevel Highest
$settings = New-ScheduledTaskSettingsSet -RunOnlyIfNetworkAvailable -StartWhenAvailable -WakeToRun
\# Create the scheduled task
$scheduledTask = New-ScheduledTask -Action $actions -Principal $principal -Trigger $trigger -Settings $settings
\# Get credentials to run the task
$creds = Get-Credential -UserName $user -Message "Enter credentials to run the task"
$password=\[Runtime.InteropServices.Marshal\]::PtrToStringAuto(\[Runtime.InteropServices.Marshal\]::SecureStringToBSTR($creds.Password))
\# Register the scheduled task
$taskName = 'EDMUpload\_' + $dataStoreName
Register-ScheduledTask -TaskName $taskName -InputObject $scheduledTask -User $user -Password $password
```

### Schedule hashing and upload as separate steps

Use the following PowerShell script to schedule hashing and upload as separate tasks:

```powershell
param(\[string\]$dataStoreName,\[string\]$fileLocation)
\# Assuming current user is also the user context to run the task
$user = "$env:USERDOMAIN\\$env:USERNAME"
$edminstallpath = 'C:\\Program Files\\Microsoft\\EdmUploadAgent\\'
$edmuploader = $edminstallpath + 'EdmUploadAgent.exe'
$csvext = '.csv'
$edmext = '.EdmHash'
$schemaext = '.xml'
\# Assuming file name is same as data store name and file is in .csv format
$dataFile = "$fileLocation\\$dataStoreName$csvext"
$hashFile = "$fileLocation\\$dataStoreName$edmext"
\# Assuming Schema file name is same as data store name
$schemaFile = "$fileLocation\\$dataStoreName$schemaext "

\# Assuming location to store hash file is same as the location of csv file
$hashLocation = $fileLocation
$createHashArgs = '/CreateHash' + ' /DataFile ' + $dataFile + ' /HashLocation ' + $hashLocation + ' /Schema ' + $schemaFile
$uploadHashArgs = '/UploadHash /DataStoreName ' + $dataStoreName + ' /HashFile ' + $hashFile
\# Set up actions associated with the task
$actions = @()
$actions += New-ScheduledTaskAction -Execute $edmuploader -Argument $createHashArgs -WorkingDirectory $edminstallpath
$actions += New-ScheduledTaskAction -Execute $edmuploader -Argument $uploadHashArgs -WorkingDirectory $edminstallpath
\# Set up trigger for the task
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 2am
\# Set up task settings
$principal = New-ScheduledTaskPrincipal -UserId $user -LogonType S4U -RunLevel Highest
$settings = New-ScheduledTaskSettingsSet -RunOnlyIfNetworkAvailable -StartWhenAvailable -WakeToRun
\# Create the scheduled task
$scheduledTask = New-ScheduledTask -Action $actions -Principal $principal -Trigger $trigger -Settings $settings
\# Get credentials to run the task
$creds = Get-Credential -UserName $user -Message "Enter credentials to run the task"
$password=\[Runtime.InteropServices.Marshal\]::PtrToStringAuto(\[Runtime.InteropServices.Marshal\]::SecureStringToBSTR($creds.Password))
\# Register the scheduled task
$taskName = 'EDMUpload\_' + $dataStoreName
Register-ScheduledTask -TaskName $taskName -InputObject $scheduledTask -User $user -Password $password
```