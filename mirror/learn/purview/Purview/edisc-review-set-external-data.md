---
layout: Conceptual
title: Import external data into a review set in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-review-set-external-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to import external data to a review set for analysis in an eDiscovery case.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-19T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- tier1
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
ms.custom: seo-marvel-apr2020, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 0f1ef946-fb4b-63b2-9a1d-e8c107d4c7f6
document_version_independent_id: 0f1ef946-fb4b-63b2-9a1d-e8c107d4c7f6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-review-set-external-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-review-set-external-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-review-set-external-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 5dcc7179-5cbb-946b-0ecc-cbe57cb2cc84
---

# Import external data into a review set in eDiscovery | Microsoft Learn

Not all documents that you need to analyze in [Microsoft Purview eDiscovery](edisc) are in Microsoft 365. With the import external data feature in eDiscovery with premium features, you can upload documents that aren't in Microsoft 365 to a review set. This article shows you how to bring your external data into eDiscovery for analysis.

## Requirements to import external data

To use the import external data feature in eDiscovery, you need the following requirements:

- eDiscovery with [eDiscovery premium features enabled](edisc-settings-general) in your organization.
- All custodians that you want to associate external data to must have the appropriate license. For more information, see [Get started with eDiscovery](edisc-get-started).
- An existing eDiscovery case.
- External data must be a file type supported by eDiscovery. For more information, see [Supported file types in eDiscovery](edisc-ref-supported-file-types).
- All files that you upload to a review set must be located in folders, where each folder is associated with a specific custodian. The names for these folders must use the following naming format: *alias@domainname*. The alias@domainname must be the user's Microsoft 365 alias and domain. You can collect all the alias@domainname folders in a root folder. The root folder can only contain the alias@domainname folders. Loose files in the root folder aren't supported.

    The folder structure for the external data that you want to upload is similar to the following example:
- c:\nonO365\abraham.mcmahon@contoso.com
- c:\nonO365\jewell.gordon@contoso.com

    - c:\nonO365\staci.gonzalez@contoso.com

    Where abraham.mcmahon@contoso.com, jewell.gordon@contoso.com, and staci.gonzalez@contoso.com are the SMTP addresses of custodians in the case.

    ![Diagram of the required external data upload folder structure for importing files into a review set.](media/3f2dde84-294e-48ea-b44b-7437bd25284c.png)
- An account that's assigned to the eDiscovery Manager role group (and added as eDiscovery Administrator). For more information about role groups, see [Assign permissions in eDiscovery](edisc-permissions).
- The AzCopy tool installed on a computer that has access to the external data folder structure. To install AzCopy, see [Get started with AzCopy](/en-us/azure/storage/common/storage-use-azcopy-v10). Be sure to install AzCopy in the default location, which is **%ProgramFiles(x86)%\Microsoft SDKs\Azure\AzCopy**. Use the latest version of AzCopy. Other versions of AzCopy might not work when loading external data in eDiscovery.

## Import external data into eDiscovery

To import external data content into eDiscovery, complete the following steps:

1. Go to the [Microsoft Purview portal](https://purview.microsoft.com) and sign in with the credentials for a user account assigned eDiscovery *Administrator* permissions.
2. Select the **eDiscovery** solution card and then select **Cases** in the left navigation.
3. Select a case, then select the **Review sets** tab.
4. Select the review set that you want to import.
5. In the review set, select **Manage**, and then select **Import external data**.
6. Select **Upload files** to start the data import workflow. The first step in the workflow prepares a secure Microsoft-provided Azure Storage location to upload the files to. When the preparation is completed, **Next: Upload files** becomes active.
7. Select **Next: Upload files**.
8. On the **Upload files** page, complete the following steps:

    - In the **Path to location of files** box, verify or type the location of the root folder where you stored the external data you want to upload. For example, for the location of the example files shown in the Requirements to import external data section, type **%USERPROFILE%\Downloads\nonO365**. Providing the correct location ensures the AzCopy command displayed in the box under the path is properly updated.
    - Select **Copy to clipboard** to copy the command that is displayed in the box.
9. Start a Windows command prompt, paste the command that you copied in the previous step, and then select **Enter** to start the AzCopy command. After you start the command, the external data files are uploaded to the Azure Storage location that was prepared in step 6.

    ![Screenshot of the AzCopy command used to upload external data to Azure Storage.](media/504e2dbe-f36f-4f36-9b08-04aea85d8250.png)

    ```
      > [!IMPORTANT]
    ```

> 
> Use the latest version of AzCopy to successfully use the command that's provided on the **Upload files** page.
10. Go back to the Microsoft Purview portal, and select **Next: Process files** in the workflow. Selecting **Next: Process files** initiates processing, text extraction, and indexing of the external data files that you uploaded to the Azure Storage location.
11. Track the progress of processing the files on the **Process files** page or on the [Process manager](edisc-process-managers) by viewing a job named **Adding external data to a review set**. After the job finishes, the new files are available in the review set.
12. After the processing finishes, you can close the workflow.

## Review the upload process report

Use [Process Manager](edisc-process-managers) to track the upload process. When the process finishes, download a [process report](edisc-process-report) that provides information about the imported external data.

The upload Non-Office 365 process report includes both a [Summary CSV](edisc-process-report-use#summary-csv-report) and an [Items CSV](edisc-process-report-use#items-csv-report) report. These reports provide details about the upload process and a list of items added to the review set and associated metadata.