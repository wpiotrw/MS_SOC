---
layout: Conceptual
title: Running the Microsoft Purview Information Protection scanner | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/deploy-scanner-manage
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords: 
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2024-06-28T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-information-protection
ms.collection:
- purview-compliance
description: Instructions for running the scanner from Microsoft Purview Information Protection to discover, classify, and protect files on data stores.
locale: en-us
document_id: 3cf98017-f2f1-6252-e685-7f4be3283f29
document_version_independent_id: 3cf98017-f2f1-6252-e685-7f4be3283f29
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/deploy-scanner-manage.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: deploy-scanner-manage
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/deploy-scanner-manage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 6f6d26ff-8fbb-b2ed-75e0-20a965095dd8
---

# Running the Microsoft Purview Information Protection scanner | Microsoft Learn

Note

There's a new version of the information protection scanner. For more information, see [Upgrade the Microsoft Purview Information Protection scanner](upgrade-scanner-migrate).

Once you've confirmed your [system requirements](deploy-scanner-prereqs) and [configured and installed your scanner](deploy-scanner-configure-install), run a discovery scan to get started.

Use other steps detailed below to manage your scans moving forward.

- Stop a scan
- Rescanning files

For more information, see [Learn about the Microsoft Purview Information Protection scanner](deploy-scanner).

Tip

While most customers will perform these procedures in the admin portal, you may need to work in PowerShell only.

For example, if you are working in an environment without access to the Azure portal, such as [Azure China 21Vianet scanner servers](/en-us/azure/information-protection/parity-between-azure-information-protection), authenticate to the [PurviewInformationProtection](/en-us/powershell/module/purviewinformationprotection) PowerShell module, and then continue with instructions in this article for PowerShell only.

## Run a discovery cycle and view reports for the scanner

Use the following procedure after you've [configured and installed your scanner](deploy-scanner-configure-install) to get an initial understanding of your content.

Perform these steps again as needed when your content changes.

1. Start a scan on your content scan job.

    Do either of the following to start a content scan job:

    - **Use the Microsoft Purview portal.** On the **Information protection scanner - Content scan jobs** pane, select your content scan jobs, and then select the **Scan now** option. The **Scan now** option only appears once a content scan job is selected.
    - **Use a PowerShell command.** Run `Start-Scan` to start the scan.
2. Wait for the scanner to complete its cycle. The scan completes when the scanner has crawled through all the files in the specified data stores.

    Do either of the following to monitor scanner progress:

    - **Use the Microsoft Purview portal.** On the **Information protection scanner - Content scan jobs** pane, select **Refresh**.

        Wait until you see values for the **LAST SCAN RESULTS** column and the **LAST SCAN (END TIME)** column.
    - **Use a PowerShell command.** Run `Get-ScanStatus` to monitor the status change.
3. When the scan is complete, review the reports stored in the **%*localappdata*%\Microsoft\MSIP\Scanner\Reports** directory.

    - The .txt summary files include the time taken to scan, the number of scanned files, and how many files had a match for the information types.
    - The .csv files have more details for each file. This folder stores up to 60 reports for each scanning cycle and all but the latest report is compressed to help minimize the required disk space.

        When a scan is completed, a `Summary_<x>.txt` file is created with the scan summary.

Note

Scanners send collected data information to Microsoft Purview Information Protection every five minutes, so that you can view the results in near real time from the admin portal.

The admin portal displays information about the last scan only. If you need to see the results of previous scans, return to the reports that are stored on the scanner computer, in the %*localappdata*%\Microsoft\MSIP\Scanner\Reports folder.

[Initial configurations](deploy-scanner-configure-install#configure-the-scanner-settings) instruct you to set the **Info types to be discovered** to **Policy only**. This configuration means that only files that meet the conditions you've configured for automatic classification are included in the detailed reports.

If you don't see any labels applied, check that your label configuration includes automatic rather than recommended classification, or enable **Treat recommended labeling as automatic** (available in scanner version 2.7.x.x and above).

If the results are still not as you expect, you might need to reconfigure the conditions that you specified for your labels. If that's the case, reconfigure the conditions as needed, and repeat this procedure until you're satisfied with the results. Then, update your configuration automatically, and optionally protection.

### Changing log levels or locations

Change the level of logging by using the *ReportLevel* parameter with [Set-ScannerConfiguration](/en-us/powershell/module/purviewinformationprotection/set-scannerconfiguration).

The report folder location or name can't be changed. If you want to store reports in a different location, consider using a directory junction for the folder.

For example, use the [Mklink](/en-us/windows-server/administration/windows-commands/mklink) command: `mklink /j D:\Scanner_reports C:\Users\aipscannersvc\AppData\Local\Microsoft\MSIP\Scanner\Reports`

If you've performed these steps after an initial configuration and installation, continue with [Configure the scanner to apply classification and protection](deploy-scanner-configure-install#configure-the-scanner-to-apply-classification-and-protection).

## Stopping a scan

To stop a currently running scan before it's complete, use either of the following methods:

- **Microsoft Purview portal.** Select **Stop scan**:
- **Run a PowerShell command.** Run the following command:

    ```PowerShell
    Stop-Scan
    ```

## Rescanning files

For the first scan cycle, the scanner inspects all files in the configured data stores. For subsequent scans, only new or modified files are inspected.

It's useful to inspect all files again when you want the reports to include all files, when you have changes that you want to apply across all files, and when the scanner runs in discovery mode.

**To manually run a full rescan in the Microsoft Purview portal**:

1. Navigate to the **Information protection scanner - Content scan jobs** pane in the Microsoft Purview portal.
2. Select your content scan job from the list, and then select the **Rescan all files** option:

When a full scan is complete, the scan type automatically changes to incremental so that for subsequent scans, only new or modified files are scanned again.

Tip

If you've made changes to your [content scan job](deploy-scanner-configure-install#create-a-content-scan-job), the portal will prompt you to skip a full rescan. To ensure that your rescan occurs, make sure to select **No** in the prompt that appears.

### Trigger a full rescan by modifying your settings

Earlier versions of the scanner scanned all files whenever the scanner detected new or changed settings for automatic and recommended labeling. The scanner automatically refreshed the policy every four hours.

In scanner versions 2.8.85.0 or later, the information protection scanner skips the full rescan for updated settings to ensure consistent performance. Make sure that you run a full rescan manually as needed.

For example, if you’ve changed **Sensitivity policy** settings from **Enforce = Off** to **Enforce = On**, make sure to run a full rescan to apply your labels across your content.

Note

In scanner [version 2.7.101.0](information-protection-client-relnotes) and lower, you may want to refresh the policy sooner than every four hours, such as while testing. In such cases, manually delete the contents of the **%LocalAppData%\Microsoft\MSIP\mip&lt;processname&gt;\mip** directory and restart the Microsoft Purview Information Protection Scanner service.

If you've also changed encryption settings for your sensitivity labels, wait an extra 15 minutes from when you saved the updated encryption settings before restarting the Microsoft Purview Information Protection Scanner service.