---
layout: Conceptual
title: Use drive shipping to import PST files | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/pst-import-drive-shipping
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Admin can learn how to bulk-import PST files to Microsoft 365 mailboxes by copying PST files to a hard drive and then shipping it to Microsoft.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-04-06T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-exchange-legacy
ms.collection:
- purview-compliance
- import
search.appverid:
- MOE150
- MET150
ai-usage: ai-assisted
locale: en-us
document_id: 0c2623c7-5228-f181-1a5c-6f86c1f777c0
document_version_independent_id: 0c2623c7-5228-f181-1a5c-6f86c1f777c0
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/pst-import-drive-shipping.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: pst-import-drive-shipping
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/pst-import-drive-shipping.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/de8ce683-cbe1-461b-bae7-77db0888ec6d
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/a06cf482-4ca9-4582-a142-bcf842258d42
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 652b1f8c-b538-febe-6407-df61544bee01
---

# Use drive shipping to import PST files | Microsoft Learn

**This article is for administrators. Are you trying to import PST files to your own mailbox? See [Import email, contacts, and calendar from an Outlook .pst file](https://go.microsoft.com/fwlink/p/?LinkID=785075).**

Use the Microsoft 365 Import service and drive shipping to bulk-import PST files to user mailboxes. Drive shipping means that you copy the PST files to a hard disk drive and then physically ship the drive to Microsoft. When Microsoft receives your hard drive, data center personnel copy the data from the hard drive to a storage area in the Microsoft cloud. Then you can trim the PST data that's imported to the target mailboxes by setting filters that control what data gets imported. After you start the import job, the Import service imports the PST data from the storage area to user mailboxes. Using drive shipping to import PST files to user mailboxes is one way to migrate your organization's email to Microsoft 365.

Here are the steps required to use drive shipping to import PST files to Microsoft 365 mailboxes:

- Step 1: Download the PST Import tool
- Step 2: Copy the PST files to the hard drive
- Step 3: Create the PST Import mapping file
- Step 4: Create a PST Import job
- Step 5: Ship the hard drive to Microsoft
- Step 6: Filter data and start the PST Import job

Important

You perform Step 1 once to download the import tool. After you perform these steps, follow Step 2 through Step 6 each time you want to ship a hard drive to Microsoft.

For frequently asked questions about using drive shipping to import PST files to Microsoft 365, see [FAQs for using drive shipping to import PST files](pst-import-faq#drive-shipping).

## Before you import PST files

Before you begin, review the [requirements, limits, and planning guidance](pst-import-overview#requirements-and-limits) for importing PST files. The following prerequisites are specific to the drive shipping method:

- You need to store the PST files on a file server or shared folder in your organization. In Step 2, you run the Azure Import Export tool (WAImportExport.exe) to copy the PST files from this file server or shared folder to the hard drive.
- The Microsoft 365 Import service supports only 2.5-inch solid-state drives (SSDs) or 2.5-inch or 3.5-inch SATA II/III internal hard drives. You can use hard drives up to 10 TB. For import jobs, the service processes only the first data volume on the hard drive. You must format the data volume with NTFS. When you copy data to a hard drive, you can attach it directly by using a 2.5-inch SSD or 2.5-inch or 3.5-inch SATA II/III connector, or you can attach it externally by using an external 2.5-inch SSD or 2.5-inch or 3.5-inch SATA II/III USB adapter.

    Important

    The Microsoft 365 Import service doesn't support external hard drives that come with a built-in USB adapter. Additionally, the disk inside the casing of an external hard drive can't be used. Don't ship external hard drives.
- You must encrypt the hard drive that you copy the PST files to by using BitLocker. The WAImportExport.exe tool that you run in Step 2 helps you set up BitLocker. It also generates a BitLocker encryption key that Microsoft data center personnel use to access the drive to upload the PST files to the Azure Storage area in the Microsoft cloud.
- You or your organization must have an account with FedEx or DHL.

    - Organizations in the United States, Brazil, and Europe must have FedEx accounts.
    - Organizations in East Asia, Southeast Asia, Japan, Republic of Korea, and Australia must have DHL accounts.

        Microsoft uses (and charges) this account to return the hard drive back to you.
- The hard drive that you ship to Microsoft might cross international borders. In this case, you're responsible for ensuring that the hard drive and the data it contains are imported and exported in accordance with the applicable laws. Before shipping a hard drive, check with your advisors to verify that your drive and data can legally be shipped to the identified Microsoft data center. This check helps ensure that it reaches Microsoft in a timely manner.
- This procedure involves copying and saving a BitLocker encryption key. Take precautions to protect these keys like you protect passwords or other security-related information. For example, you might save them to a password-protected Microsoft Word document or save them to an encrypted USB drive. See the More information section for an example of these keys.

## Step 1: Download the PST Import tool

The first step is to download the tool. You use this tool in Step 2 to copy PST files to the hard drive.

Important

To successfully import PST files by using the drive shipping method, use Azure Import/Export tool version 1 (WAimportExportV1). Version 2 of the Azure Import/Export tool isn't supported. Using it results in incorrectly preparing the hard drive for the import job. Be sure to download the Azure Import/Export tool from the Microsoft Purview portal by following the procedures in this step.

1. Go to https://purview.microsoft.com and sign in by using the credentials for an administrator account in your organization.
2. In the left navigation of the Microsoft Purview portal, select **Data lifecycle management** &gt; **Microsoft 365** &gt; **Import**.

    Note

    As previously stated, you need the appropriate permissions to access the **Import** page in the Microsoft Purview portal.
3. On the **Import** tab, select ![Add Icon.](media/itpro-eac-addicon.gif)**New import job**.
4. In the import job wizard, type a name for the PST import job, and then select **Next**. Use lowercase letters, numbers, hyphens, and underscores. You can't use uppercase letters or include spaces in the name.
5. On the **Select import job type** page, select **Ship hard drives to one of our physical locations** and then select **Next**.

    ![Ship hard drives to one of our physical locations to create a drive shipping import job.](media/1584fdc5-cd4c-4e47-932e-db6c8e07f5f8.png)
6. On the **Import data** page, complete the following steps:

    **Download the Azure Import/Export tool** to download and install the Azure Import/Export (version 1) tool.

    - In the pop-up window, select **Save** &gt; **Save as** to save the WaImportExportV1.zip file to a folder on your local computer.
    - Extract the WaImportExportV1.zip file.
7. Select **Cancel** to close the wizard.

    You return to the **Import** page in the Microsoft Purview portal when you create the import job in Step 4.

## Step 2: Copy the PST files to the hard drive

In this step, use the WAImportExport.exe tool to copy PST files to the hard drive. This tool encrypts the hard drive by using BitLocker, copies the PSTs to the hard drive, and creates a journal file that stores information about the copy process. To complete this step, you need to locate the PST files in a file share or file server in your organization. This location is known as the source directory in the following procedure.

Each PST file that you copy to the hard drive should be no larger than 20 GB. PST files larger than 20 GB might affect the performance of the PST import process that you start in Step 6.

Important

After you run the WAImportExport.exe tool the first time for a hard drive, use a different syntax each time after that. Step 4 explains this syntax to copy PST files to the hard drive.

1. Open a Command Prompt on your local computer.

    Tip

    If you run the command prompt as an administrator (by selecting **Run as administrator** when you open it), error messages display in the command prompt window. This information can help you resolve issues running the WAImportExport.exe tool.
2. Go to the directory where you installed the WAImportExport.exe tool in Step 1.
3. Run the following command the first time that you use the WAImportExport.exe to copy PST files to a hard drive.

    ```powershell
    WAImportExport.exe PrepImport /j:<Name of journal file> /t:<Drive letter> /id:<Name of session> /srcdir:<Location of PST files> /dstdir:<PST file path> /blobtype:BlockBlob /encrypt /logdir:<Log file location>
    ```

    The following table describes the parameters and their required values.

    | Parameter | Description | Example |
    | --- | --- | --- |
    | `/j:` | Specifies the name of the journal file.The tool saves this file to the same folder where the WAImportExport.exe tool is located. Each hard drive you ship to Microsoft must have one journal file. Every time you run the WAImportTool.exe to copy PST files to a hard drive, the tool appends information to the journal file for that drive.  Microsoft data center personnel use the information in the journal file to associate the hard drive with the import job that you create in Step 4, and to upload the PST files to the Azure Storage area in the Microsoft cloud. | `/j:PSTHDD1.jrn` |
    | `/t:` | Specifies the drive letter of the hard drive when it's connected to your local computer. | `/t:h` |
    | `/id:` | Specifies the name of the copy session. A session is defined as each time you run the WAImportExport.exe tool to copy files to the hard drive. The PST files are copied to a folder named with the session name specified by this parameter. | `/id:driveship1` |
    | `/srcdir:` | Specifies the source directory in your organization that contains the PST files that the tool copies during the session. Surround the value of this parameter with double-quotation marks (" "). | `/srcdir:"\\FILESERVER01\PSTs"` |
    | `/dstdir:` | Specifies the destination directory in the Azure Storage area in the Microsoft cloud where the PSTs are uploaded. Use the value `ingestiondata/`. Surround the value of this parameter with double-quotation marks (" ").  Optionally, you can also add an extra file path to the value of this parameter. For example, you can use the file path of the source directory on the hard drive (converted to a URL format), which is specified in the `/srcdir:` parameter. For example, `\\FILESERVER01\PSTs` is changed to `FILESERVER01/PSTs`. In this case, you still must include `ingestiondata` in the file path. So in this example, the value for the `/dstdir:` parameter would be `"ingestiondata/FILESERVER01/PSTs"`.  One reason to add the additional file path is if you have PST files with the same filename.  &gt; [!NOTE]&gt; If you include the optional pathname, the namespace for a PST file after it's uploaded to the Azure Storage area includes the pathname and the name of the PST file; for example, `FILESERVER01/PSTs/annb.pst`. If you don't include a pathname, the namespace is only the PST filename; for example `annb.pst`. | `/dstdir:"ingestiondata/"` Or `/dstdir:"ingestiondata/FILESERVER01/PSTs"` |
    | `/blobtype:` | Specifies the type of blobs in the Azure Storage area to import the PST files to. For importing PST files, use the value **BlockBlob**. This parameter is required. | `/blobtype:BlockBlob` |
    | `/encrypt` | This switch turns on BitLocker for the hard drive. This parameter is required the first time you run the WAImportExport.exe tool.  The BitLocker encryption key is copied to the journal file and the log file that is created if you use the `/logfile:` parameter. As previously explained, the journal file is saved to the same folder where the WAImportExport.exe tool is located. | `/encrypt` |
    | `/logdir:` | This optional parameter specifies a folder to save log files to. If not specified, the log files are saved to the same folder where the WAImportExport.exe tool is located. Surround the value of this parameter with double-quotation marks (" "). | `/logdir:"c:\users\admin\desktop\PstImportLogs"` |

    Here's an example of the syntax for the WAImportExport.exe tool using actual values for each parameter:

    ```powershell
    WAImportExport.exe PrepImport /j:PSTHDD1.jrn /t:f /id:driveship1 /srcdir:"\\FILESERVER01\PSTs" /dstdir:"ingestiondata/" blobtype:BlockBlob /encrypt /logdir:"c:\users\admin\desktop\PstImportLogs"
    ```

    After you run the command, status messages display that show the progress of copying the PST files to the hard drive. A final status message shows the total number of files that you successfully copied.
4. Run this command each subsequent time you run the WAImportExport.ext tool to copy PST files to the same hard drive.

    ```powershell
    WAImportExport.exe PrepImport /j:<Name of journal file> /id:<Name of new session> /srcdir:<Location of PST files> /dstdir:<PST file path> /blobtype:BlockBlob
    ```

    Here's an example of the syntax for running subsequent sessions to copy PST files to the same hard drive.

    ```powershell
    WAImportExport.exe PrepImport /j:PSTHDD1.jrn /id:driveship2 /srcdir:"\\FILESERVER01\PSTs\SecondBatch" /dstdir:"ingestiondata/" /blobtype:BlockBlob
    ```

## Step 3: Create the PST Import mapping file

After Microsoft data center personnel upload the PST files from the hard drive to the Azure Storage area, the Import service uses the information in the PST Import mapping file, which is a comma-separated value (CSV) file, to know which user mailboxes to import the PST files to. You submit this CSV file in the next step when you create a PST Import job.

1. [Download a copy of the PST Import mapping file](https://go.microsoft.com/fwlink/p/?LinkId=544717).
2. Open or save the CSV file to your local computer. The following example shows a completed PST Import mapping file (opened in NotePad). It's easier to use Microsoft Excel to edit the CSV file.

    ```text
    Workload,FilePath,Name,Mailbox,IsArchive,TargetRootFolder,ContentCodePage,SPFileContainer,SPManifestContainer,SPSiteUrl
    Exchange,FILESERVER01/PSTs,annb.pst,annb@contoso.onmicrosoft.com,FALSE,/,,,,
    Exchange,FILESERVER01/PSTs,annb_archive.pst,annb@contoso.onmicrosoft.com,TRUE,/ImportedPst,,,,
    Exchange,FILESERVER01/PSTs,donh.pst,donh@contoso.onmicrosoft.com,FALSE,/,,,,
    Exchange,FILESERVER01/PSTs,donh_archive.pst,donh@contoso.onmicrosoft.com,TRUE,/ImportedPst,,,,
    Exchange,FILESERVER01/PSTs,pilarp.pst,pilarp@contoso.onmicrosoft.com,FALSE,/,,,,
    Exchange,FILESERVER01/PSTs,pilarp_archive.pst,pilarp@contoso.onmicrosoft.com,TRUE,/ImportedPst,,,,
    Exchange,,tonyk.pst,tonyk@contoso.onmicrosoft.com,FALSE,/,,,,
    Exchange,,tonyk_archive.pst,tonyk@contoso.onmicrosoft.com,TRUE,,,,,
    Exchange,,zrinkam.pst,zrinkam@contoso.onmicrosoft.com,FALSE,/,,,,
    Exchange,,zrinkam_archive.pst,zrinkam@contoso.onmicrosoft.com,TRUE,,,,,
    ```

    The first row, or header row, of the CSV file lists the parameters that the PST Import service uses to import the PST files to user mailboxes. Each parameter name is separated by a comma. Each row under the header row represents the parameter values for importing a PST file to a specific mailbox. You need a row for each PST file that you copied to the hard drive. Be sure to replace the placeholder data in the mapping file with your actual data.

    Note

    Don't change anything in the header row, including the SharePoint parameters; the PST Import process ignores them.
3. Use the information in the following table to populate the CSV file with the required information.

    | Parameter | Description | Example |
    | --- | --- | --- |
    | `Workload` | Specifies the service that data is imported to.To import PST files to user mailboxes, use `Exchange`. | `Exchange` |
    | `FilePath` | Specifies the folder location in the Azure Storage area that PST files are copied to when the hard drive is shipped to Microsoft.  What you add in this column in the CSV file depends on what you specified in for the `/dstdir:` parameter in the previous step. If you have subfolders on the source location, then the value in the `FilePath` parameter must contain the relative path for the subfolder; for example, /folder1/user1/.  If you used `/dstdir:"ingestiondata/"`, then leave this parameter blank in the CSV file.  If you included an optional pathname for the value of the `/dstdir:` parameter (for example, `/dstdir:"ingestiondata/FILESERVER01/PSTs"`, then use that pathname (not including "ingestiondata") for this parameter in the CSV file. The value for this parameter is case-sensitive.  Either way, *don't* include "ingestiondata" in the value for the `FilePath` parameter. Leave this parameter blank or specify only the optional pathname.  &gt; [!IMPORTANT]&gt; The case for the file path name must be the same case that you specified in the `/dstdir:` parameter in the previous step. For example, if you used `"ingestiondata/FILESERVER01/PSTs"` for the subfolder name in the previous step, but then used `fileserver01/psts` in the `FilePath` parameter in CSV file, the import for the PST file fails. Be sure to use the same case in both instances. | (leave blank)  Or `FILESERVER01/PSTs` |
    | `Name` | Specifies the name of the PST file that is imported to the user mailbox. The value for this parameter is case-sensitive.  &gt; [!IMPORTANT]&gt; The case for the PST file name in the CSV file must be the same as the PST file that was uploaded to the Azure Storage location in Step 2. For example, if you use `annb.pst` in the `Name` parameter in the CSV file, but the name of the actual PST file is `AnnB.pst`, the import for that PST file fails. Be sure that the name of the PST in the CSV file uses the same case as the actual PST file. | `annb.pst` |
    | `Mailbox` | Specifies the email address of the mailbox that the PST file is imported to. You can't specify a public folder because the PST Import Service doesn't support importing PST files to public folders.  To import a PST file to an inactive mailbox, you have to specify the mailbox GUID for this parameter. To obtain this GUID, run the following PowerShell command in Exchange Online: `Get-Mailbox <identity of inactive mailbox> -InactiveMailboxOnly | FL Guid` &gt; [!NOTE]&gt; Sometimes, you have multiple mailboxes with the same email address, where one mailbox is an active mailbox and the other mailbox is in a soft-deleted (or inactive) state. In these situations, you have to specify the mailbox GUID to uniquely identify the mailbox to import the PST file to. To obtain this GUID for active mailboxes, run the following PowerShell command: `Get-Mailbox <identity of active mailbox> | FL Guid`. To obtain the GUID for soft-deleted (or inactive) mailboxes, run this command: `Get-Mailbox <identity of soft-deleted or inactive mailbox> -SoftDeletedMailbox | FL Guid`. | `annb@contoso.onmicrosoft.com` Or `2d7a87fe-d6a2-40cc-8aff-1ebea80d4ae7` |
    | `IsArchive` | Specifies whether to import the PST file to the user's archive mailbox. There are two options: **FALSE** Imports the PST file to the user's primary mailbox. **TRUE** Imports the PST file to the user's archive mailbox. This assumes that the [user's archive mailbox is enabled](enable-archive-mailboxes). If you set this parameter to `TRUE` and the user's archive mailbox isn't enabled, the import for that user fails. If an import fails for one user (because their archive isn't enabled and this property is set to `TRUE`), the other users in the import job isn't affected.  If you leave this parameter blank, the PST file is imported to the user's primary mailbox. **Note:** To import a PST file to a cloud-based archive mailbox for a user whose primary mailbox is on-premises, just specify `TRUE` for this parameter and specify the email address for the user's on-premises mailbox for the `Mailbox` parameter. | `FALSE` Or `TRUE` |
    | `TargetRootFolder` | Specifies the mailbox folder that the PST file is imported to.  If you leave this parameter blank, the PST is imported to a new folder named **Imported** located at the root level of the mailbox (the same level as the Inbox folder and the other default mailbox folders).  If you specify `/`, items in the PST file are imported directly in to the user's Inbox folder.  If you specify `/<foldername>`, items in the PST file are imported to a folder named *&lt;foldername&gt;*. For example, if you use `/ImportedPst`, items would be imported to a folder named **ImportedPst**. This folder is located in the user's mailbox at the same level as the Inbox folder. | (leave blank)  Or `/` Or `/ImportedPst` |
    | `ContentCodePage` | This optional parameter specifies a numeric value for the code page to use for importing PST files in the ANSI file format. This parameter is used for importing PST files from Chinese, Japanese, and Korean (CJK) organizations because these languages typically use a double byte character set (DBCS) for character encoding. If this parameter isn't used to import PST files for languages that use DBCS for mailbox folder names, the folder names are often garbled after they're imported.  For a list of supported values to use for this parameter, see [Code Page Identifiers](/en-us/windows/win32/intl/code-page-identifiers).  &gt; [!NOTE]&gt; As previously stated, this is an optional parameter and you don't have to include it in the CSV file. Or you can include it and leave the value blank for one or more rows. | (leave blank)  Or `932` (which is the code page identifier for ANSI/OEM Japanese) |
    | `SPFileContainer` | For PST Import, leave this parameter blank. | Not applicable |
    | `SPManifestContainer` | For PST Import, leave this parameter blank. | Not applicable |
    | `SPSiteUrl` | For PST Import, leave this parameter blank. | Not applicable |

## Step 4: Create a PST Import job

Next, create the PST Import job in the Import service in Microsoft 365. Submit the PST Import mapping file that you created in Step 3. After you create the job, the Import service uses the information in the mapping file to import the PST files to the specified user mailbox. The Import service imports the PST files after you copy the PST files from the hard drive to the Azure Storage area and you create and start the import job.

1. Go to https://purview.microsoft.com and sign in by using the credentials for an administrator account in your organization.
2. In the left navigation of the Microsoft Purview portal, select **Data lifecycle management** &gt; **Microsoft 365** &gt; **Import**.
3. On the **Import** tab, select ![Add Icon.](media/itpro-eac-addicon.gif)**New import job**.

    Note

    As previously stated, you need the appropriate permissions to access the **Import** page in the Microsoft Purview portal.
4. Type a name for the PST import job, then select **Next**. Use lowercase letters, numbers, hyphens, and underscores. You can't use uppercase letters or include spaces in the name.
5. On the **Select import job type** page, select **Ship hard drives to one of our physical locations** and then select **Next**.
6. Select the **I've prepared my hard drives and have access to the necessary drive journal files** and **I have access to the mapping file** check boxes, then select **Next**.

    ![Select the two check boxes in step 6.](media/fad43078-ea68-4acd-b2ed-75a800183262.png)
7. On the **Select the drive file** page, select **Select drive file**, then go to the same folder where the WAImportExport.exe tool is located. The journal file that you created in Step 2 is in this folder.

    ![Select drive file to submit the journal file that was created when you ran the WAImportExport.exe tool.](media/1ea35c04-bd88-4d7e-b7d9-dc390149d94f.png)
8. Select the journal file, such as `PSTHDD1.jrn`.

    Tip

    When you ran the WAImportExport.exe tool in Step 2, you specified the name of the journal file by using the `/j:` parameter.
9. After the name of the drive file appears under **Drive file name**, select **Validate** to check your drive file for errors.

    ![Validate to validate the drive file that you selected.](media/4b707f5a-152a-4e74-b9f5-449c88d1fec4.png)

    You must successfully validate the drive file to create a PST Import job. The file name changes to green after it's successfully validated. If the validation fails, select the **View log** link. A validation error report opens, with an error message that explains why the file failed.

    Note

    You must add and validate a journal file for each hard drive you ship to Microsoft.
10. After adding and validating a journal file for each hard drive that you ship to Microsoft, select **Next**.
11. Select ![Add Icon.](media/itpro-eac-addicon.gif)**Select mapping file** to submit the PST Import mapping file that you created in Step 3.

    ![Select mapping file to submit the CSV file you created for the import job.](media/d30b1d73-80bb-491e-a642-a21673d06889.png)
12. After the name of the CSV file appears under **Mapping file name**, select **Validate** to check your CSV file for errors.

    ![Validate to check the CSV file for errors.](media/4680999d-5538-4059-b878-2736a5445037.png)

    You must successfully validate the CSV file to create a PST Import job. The file name changes to green after it's successfully validated. If the validation fails, select the **View log** link. A validation error report opens, with an error message for each row in the file that failed.
13. After the PST mapping file is successfully validated, select **Next**.
14. On the **Provide contact information** page, type your contact information in the applicable boxes.

    The address for the Microsoft location that you ship your hard drives to is displayed. This address is autogenerated based on your Microsoft datacenter location. Copy this address to a file or take a screenshot.
15. Read the terms and conditions document, select the checkbox, then select **Save** to submit the import job.

    When the import job is successfully created, a status page is displayed that explains the next steps of the drive shipping process.
16. On the **Import** tab, select ![Refresh icon.](media/o365-mdm-policy-refreshicon.gif)**Refresh** to show the new drive shipping import job in the list of import jobs. The status is **Waiting for tracking number**. You can also select the import job to display the status flyout page, which contains more detailed information about the import job.

## Step 5: Ship the hard drive to Microsoft

In this step, you ship the hard drive to Microsoft. You also provide the tracking number for the shipment and return shipment information for the drive shipping job. After Microsoft receives the drive, data center personnel take between 7 and 10 business days to upload your PST files to the Azure Storage area for your organization.

Note

If you don't provide the tracking number and return shipment information within 14 days of creating the import job, the import job expires. If this happens, you need to create a new drive shipping import job (see Step 4: Create a PST Import job) and re-submit the drive file and the PST import mapping file.

### Ship the hard drive

Keep the following things in mind when you ship hard drives to Microsoft:

- Don't ship the SATA-to-USB adapter; you only need to ship the hard drive.
- Package the hard drive properly; for example, use an anti-static bag or bubble wrap.
- Use a delivery carrier of your choice to ship the hard drive to Microsoft.
- Ship the hard drive to the address for the Microsoft location that displays when you create the import job in Step 4. Be sure to include "Microsoft 365 Import Service" in the ship-to address.
- After you ship the hard drive, be sure to write down the name of the delivery carrier and the tracking number. You provide these in the next step.

### Enter the tracking number and other shipping information

After you ship the hard drive to Microsoft, complete the following procedure on the Import service page.

1. Go to https://purview.microsoft.com and sign in by using the credentials for an administrator account in your organization.
2. In the left navigation of the Microsoft Purview portal, select **Data lifecycle management** &gt; **Microsoft 365** &gt; **Import**.
3. On the **Import** tab, select the job for the drive shipment that you want to enter the tracking number for.
4. On the status flyout page, select **Enter tracking number**.
5. Provide the following shipping information:

    1. **Delivery carrier** Type the name of the delivery carrier that you used to ship the hard drive to Microsoft.
    2. **Tracking number** Type the tracking number for the hard drive shipment.
    3. **Return carrier account number** Type your organization's account number for the carrier that listed under **Return carrier**. Microsoft uses (and charges) this account to ship your hard drive back to you. Organizations in the USA and Europe, must have an account with FedEx. Organizations in Asia and the rest of the world, must have an account with DHL.
6. Select **Save** to save this information for the import job.

    1. On the **Import** tab, select ![Refresh icon.](media/o365-mdm-policy-refreshicon.gif)**Refresh** to update the information for your drive shipping import job. Notice that status is now set to **Drives in transit**.

## Step 6: Filter data and start the PST Import job

After Microsoft receives your hard drive, the status for the import job on the **Import PST files** page changes to **Drives received**. Data center personnel use the information in the journal file to upload your PST files to the Azure Storage area for your organization. At this point, the status changes to **Import in-progress**. As previously stated, it takes between 7 and 10 business days after receiving your hard drive to upload the PST files.

After uploading the PST files to Azure, the status changes to **Analysis in progress**. This status indicates that Microsoft 365 is analyzing the data in the PST files (in a safe and secure manner) to identify the age of the items and the different message types included in the PST files. When the analysis completes and the data is ready to import, the status changes to **Analysis completed**. At this point, you can import all the data contained in the PST files or trim the data by setting filters that control what data gets imported.

1. Go to https://purview.microsoft.com and sign in by using the credentials for an administrator account in your organization.
2. In the left navigation of the Microsoft Purview portal, select **Data lifecycle management** &gt; **Microsoft 365** &gt; **Import**.
3. On the **Import** tab, select the import job that you created in Step 4 and select **Import to Microsoft 365**.

    A flyout page appears with information about the PST files and other information about the import job.
4. Select **Import to Microsoft 365**.
5. The **Filter your data** page appears. It contains the data insights resulting from the analysis performed on the PST files by Microsoft 365, including information about the age of the data. At this point, you can filter the data that you want to import or import all the data as is.

    ![You can trim the data in the PST files or import all of it.](media/287fc030-99e9-417b-ace7-f64617ea5d4e.png)
6. Do one of the following steps:

    1. To trim the data that you import, select **Yes, I want to filter it before importing**.

        For detailed step-by-step instructions about filtering the data in the PST files and then starting the import job, see [Filter data when importing PST files to Microsoft 365](pst-import-filter-data).

        Or
    2. To import all data in the PST files, select **No, I want to import everything,** and select **Next**.
7. If you chose to import all the data, select **Import data** to start the import job.

    The status of the import job appears on the **Import PST files** page. Select ![Refresh icon.](media/o365-mdm-policy-refreshicon.gif)**Refresh** to update the status information that's displayed in the **Status** column. Select the import job to display the status flyout page, which displays status information about each PST file being imported. When the import completes and PST files are imported to user mailboxes, the status changes to **Completed**.

## View a list of the PST files uploaded to Microsoft 365

Install and use Microsoft Azure Storage Explorer, a free, open-source tool, to view the list of PST files that Microsoft data center personnel uploaded to the Azure Storage area for your organization. Use this list to verify that PST files from the hard drives you sent to Microsoft were successfully uploaded to the Azure Storage area.

Important

You can't use Azure Storage Explorer to upload or modify PST files. The only supported method for importing PST files to Microsoft 365 is to use AzCopy. Also, you can't delete PST files that you upload to the Azure blob. If you try to delete a PST file, you receive an error about not having the required permissions. All PST files are automatically deleted from your Azure Storage area. If there are no import jobs in progress, the system deletes all PST files in the **ingestiondata** container 30 days after the most recent import job was created.

Perform the following steps to get the Shared Access Signature (SAS) URL for your organization. This URL combines the network URL for the Azure Storage location in the Microsoft cloud for your organization with an SAS key. This key provides you with the necessary permissions to access your organization's Azure Storage location.

To install Azure Storage Explorer and connect to your Azure Storage area:

1. Go to https://purview.microsoft.com and sign in by using the credentials for an administrator account in your organization.
2. In the left pane of the Microsoft Purview portal, select **Data lifecycle management** &gt; **Microsoft 365** &gt; **Import**.
3. On the **Import** tab, select ![Add Icon.](media/itpro-eac-addicon.gif)**New import job**.
4. In the import job wizard, type a name for the PST import job, and then select **Next**. Use lowercase letters, numbers, hyphens, and underscores. You can't use uppercase letters or include spaces in the name.
5. On the **Select import job type** page, select **Upload your data**, then select **Next**.
6. In step 2, select **Show network upload SAS URL**.
7. After the URL is displayed, copy it and save it to a file. Be sure to copy the entire URL.

    Important

    Be sure to take precautions to protect the SAS URL. Anyone can use this URL to access the Azure storage area for your organization.
8. Select **Cancel** to close the import job wizard.
9. Download and install the [Microsoft Azure Storage Explorer tool](https://go.microsoft.com/fwlink/p/?LinkId=544842).
10. Start Microsoft Azure Storage Explorer, right-click **Storage Accounts** in the left pane, then select **Connect to Azure Storage**.

    ![Right-click Storage Accounts and then select Connect to Azure Storage.](media/75b80cc3-c336-4f96-ad32-54ac9b96a7af.png)
11. Select **Use a shared access signature (SAS) URI or connection string** and select **Next**.
12. Select **Use a SAS URI**, paste the SAS URL that you obtained in step 1 into the box under **URI**, then select **Next**.
13. On the **Connection summary** page, review the connection information, then select **Connect**.

    The **ingestiondata** container opens. It contains the PST files from your hard drive. The **ingestiondata** container is located under **Storage Accounts** &gt; **(SAS-Attached Services)** &gt; **Blob Containers**.

    ![Azure Storage Explorer displays a list of the PST files that you uploaded.](media/12376fed-13a5-4a09-8fe6-e819e011b334.png)
14. When you're finished using Microsoft Azure Storage Explorer, right-click **ingestiondata**, then select **Detach** to disconnect from your Azure Storage area. Otherwise, you receive an error the next time you try to attach.

    ![Right-click ingestion and select Detach to disconnect from your Azure Storage area.](media/1e8e5e95-4215-4ce4-a13d-ab5f826a0510.png)

## Resolve common import errors

- **What happens if the import job fails because of errors in the PST Import CSV mapping file?** If an import job fails because of errors in the mapping file, you don't need to reship the hard drive to Microsoft to create an import job. That's because the PST files from the hard drive that you submitted for the drive shipping import job are already uploaded to the Azure Storage area for your organization. In this case, you only need to fix the errors in the PST Import CSV mapping file, then create a new "network upload" import job and submit the revised CSV mapping file. For more information, see [Step 5: Create a PST Import job in Microsoft 365](pst-import-network-upload#step-5-create-a-pst-import-job) and [Step 6: Filter data and start the PST Import job](pst-import-network-upload#step-6-filter-data-and-start-the-pst-import-job).

    Note

    To help resolve errors in the PST Import CSV mapping file, use the Azure Storage Explorer tool to view the folder structure in the **ingestiondata** container for the PST files from your hard drive that you uploaded to the Azure storage area. Mapping file errors typically occur because of an incorrect value in the FilePath parameter. This parameter specifies the location of a PST file in the Azure storage area. See the description of the FilePath parameter in table in Step 3. As previously explained, the location of PST files in the Azure storage area is specified by the `/dstdir:` parameter when you run the WAImportExport.exe tool in Step 2.

## More information

- Drive shipping is an effective way to import large amounts of archival messaging data to Microsoft 365 so you can take advantage of the compliance features that are available to your organization. After archival data is imported to user mailboxes, you can:

    - Enable [archive mailboxes](enable-archive-mailboxes) and [auto-expanding archiving](enable-autoexpanding-archiving) to give users more mailbox storage space for the data.
    - Place mailboxes on [Litigation Hold](/en-us/exchange/policy-and-compliance/holds/litigation-holds) to retain the data.
    - Use Microsoft [eDiscovery tools](ediscovery-content-search-overview) to search the data.
    - Apply [Microsoft 365 retention policies](retention) to control how long the data is retained, and what action to take after the retention period expires.
    - Search the [audit log](audit-search) for events related to this data.
    - Import data to [inactive mailboxes](inactive-mailboxes-in-office-365) to archive data for compliance purposes.
    - Protect your organization against [data loss](dlp-learn-about-dlp) of sensitive information.
- Here's an example of the secure storage account key and a BitLocker encryption key. This example also contains the syntax for the WAImportExport.exe command that you run to copy PST files to a hard drive. Be sure to take precautions to protect these just like you would protect passwords or other security-related information.

    ```text
    Secure storage account key:
    
    yaNIIs9Uy5g25Yoak+LlSHfqVBGOeNwjqtBEBGqRMoidq6/e5k/VPkjOXdDIXJHxHvNoNoFH5NcVUJXHwu9ZxQ==
    
    BitLocker encryption key:
    
    397386-221353-718905-535249-156728-127017-683716-083391
    
    COMMAND SYNTAX
    
    First time:
    
    WAImportExport.exe PrepImport /j:<Name of journal file> /t:<Drive letter> /id:<Name of session> /srcdir:<Location of PST files> /dstdir:<PST file path> /blobtype:BlockBlob /encrypt /logdir:<Log file location>
    
    Subsequent times:
    
    WAImportExport.exe PrepImport /j:<Name of journal file> /id:<Name of new session> /srcdir:<Location of PST files> /dstdir:<PST file path> /blobtype:BlockBlob
    
    EXAMPLES
    
    First time:
    
    WAImportExport.exe PrepImport /j:PSTHDD1.jrn /t:f /id:driveship1 /srcdir:"\\FILESERVER1\PSTs" /dstdir:"ingestiondata/"
    /blobtype:BlockBlob /encrypt /logdir:"c:\users\admin\desktop\PstImportLogs"
    
    Subsequent times:
    
    WAImportExport.exe PrepImport /j:PSTHDD1.jrn /id:driveship2 /srcdir:"\\FILESERVER1\PSTs\SecondBatch" /dstdir:"ingestiondata/" /blobtype:BlockBlob
    ```
- As previously explained, the Microsoft 365 Import service turns on the retention hold setting (for an indefinite duration) after PST files are imported to a mailbox. This setting means the *RetentionHoldEnabled* property is set to `True` so that the retention policy assigned to the mailbox isn't processed. This setting gives the mailbox owner time to manage the newly imported messages by preventing a deletion or archive policy from deleting or archiving older messages. Here are some steps you can take to manage this retention hold:

    - After a certain period of time, you can turn off the retention hold by running the `Set-Mailbox -RetentionHoldEnabled $false` command. For instructions, see [Place a mailbox on retention hold](/en-us/exchange/security-and-compliance/messaging-records-management/mailbox-retention-hold).
    - You can configure the retention hold so that it's turned off on some date in the future. You do this by running the `Set-Mailbox -EndDateForRetentionHold <date>` command. For example, assuming that today's date is June 1, 2016 and you want the retention hold turned off in 30 days, you would run the following command: `Set-Mailbox -EndDateForRetentionHold 7/1/2016`. In this scenario, you would leave the *RetentionHoldEnabled* property set to *True*. For more information, see [Set-Mailbox](/en-us/powershell/module/exchange/set-mailbox).
    - You can change the settings for the retention policy that's assigned to the mailbox so that older items that were imported aren't immediately deleted or moved to the user's archive mailbox. For example, you could lengthen the retention age for a deletion or archive policy that's assigned to the mailbox. In this scenario, you turn off the retention hold on the mailbox after you change the settings of the retention policy. For more information, see [Set up an archive and deletion policy for mailboxes in your organization](set-up-an-archive-and-deletion-policy-for-mailboxes).