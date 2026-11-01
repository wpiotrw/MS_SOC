---
layout: Conceptual
title: Use network upload to import PST files | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/pst-import-network-upload
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: 'For administrators: Learn how to use network upload to bulk-import multiple PST files to user mailboxes in Microsoft 365.'
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-11T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-exchange-legacy
ms.collection:
- purview-compliance
- import
search.appverid:
- MOE150
- MED150
- MET150
ai-usage: ai-assisted
locale: en-us
document_id: d0dbb528-4c96-a757-bdd7-04a32b99cf89
document_version_independent_id: d0dbb528-4c96-a757-bdd7-04a32b99cf89
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/pst-import-network-upload.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: pst-import-network-upload
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/pst-import-network-upload.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/de8ce683-cbe1-461b-bae7-77db0888ec6d
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/766f70ec-319f-4c35-872d-89afd8c4d224
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/a06cf482-4ca9-4582-a142-bcf842258d42
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/66c6e6fb-a5a6-4608-a629-b6e94e89ef4d
platformId: 06cf3b74-bf0e-390d-24da-05c3f5a1c269
---

# Use network upload to import PST files | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Note

This article is for administrators. Are you trying to import PST files to your own mailbox? See [Import email, contacts, and calendar from an Outlook .pst file](https://go.microsoft.com/fwlink/p/?LinkID=785075).

Use the following step-by-step instructions to bulk-import multiple PST files to Microsoft 365 mailboxes by using network upload. For frequently asked questions about using network upload to bulk-import PST files to Microsoft 365 mailboxes, see [FAQs for using network upload to import PST files](pst-import-faq#network-upload). To import PST files by physically shipping a hard drive to Microsoft, see [Use drive shipping to import PST files](pst-import-drive-shipping).

- Step 1: Copy the SAS URL and download AzCopy
- Step 2: Upload your PST files to Microsoft 365
- Step 3 (Optional): View a list of the uploaded PST files
- Step 4: Create the PST Import mapping file
- Step 5: Create a PST Import job
- Step 6: Filter data and start the PST Import job

You only need to perform Step 1 once to import PST files to Microsoft 365 mailboxes. After you perform Step 1, follow Step 2 through Step 6 each time you want to upload and import a batch of PST files.

## Before you import PST files

Before you begin, review the [requirements, limits, and planning guidance](pst-import-overview#requirements-and-limits) for importing PST files. The following prerequisites are specific to the network upload method:

- The only supported method for importing PST files to Microsoft 365 is to use the AzCopy tool, as described in this article. You can't use the Azure Storage Explorer to upload PST files directly to the Azure Storage area.
- This procedure involves copying and saving a copy of a URL that contains an access key. You use this information in Step 2 to upload your PST files, and in Step 3 if you want to view a list of the PST files uploaded to Microsoft 365. Take precautions to protect this URL like you would protect passwords or other security-related information. For example, you might save it to a password-protected Microsoft Word document or to an encrypted USB drive. See the More information section for an example of this combined URL and key.
- For a high-level overview of the PST Import process, see How the import process works section in this article.

## Step 1: Copy the SAS URL and download AzCopy

First, download the AzCopy tool. Use this tool in Step 2 to upload PST files to Microsoft 365. Also, copy the SAS URL for your organization. This URL combines the network URL for the Azure Storage location in the Microsoft cloud for your organization and a Shared Access Signature (SAS) key. This key gives you the necessary permissions to upload PST files to an Azure Storage location. Protect the SAS URL. It's unique to your organization and you use it in Step 2.

Important

To import PST files by using the network upload method and command syntax documented in this article, use the version of AzCopy that you can download in step 6b in the following procedure. You can also download that same version of AzCopy from [here](https://aka.ms/downloadazcopylatest). Using a different version of AzCopy isn't supported.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) by using the credentials for an administrator account in your organization.
2. In the left navigation, select **Data lifecycle management** &gt; **Microsoft 365** &gt; **Import**.

    Note

    You must be assigned the appropriate permissions to access the **Import** page in the Microsoft Purview portal. See the **Before you begin** section for more information.
3. On the **Import** tab, select ![Add Icon.](media/itpro-eac-addicon.gif)**New import job**.

    The import job wizard is displayed.
4. Type a name for the PST import job, and then select **Next**. Use lowercase letters, numbers, hyphens, and underscores. You can't use uppercase letters or include spaces in the name.
5. On the **Do you want to upload or ship data?** page, select **Upload your data** and then select **Next**.

    ![Upload your data to create a network upload import job.](media/e59f9dc3-ccde-44ff-ac38-c4e39d76ae85.png)
6. On the **Import data** page, complete the following steps:

    ![Copy the SAS URL and download the AzCopy tool on the Import data page.](media/74411014-ec4b-4e25-9065-404c934cce17.png)

    1. In step 2, select **Show network upload SAS URL**. After the SAS URL is displayed, select **Copy to clipboard** and then paste it and save it to a file.
    2. In step 3, select **Download Azure AzCopy** to download the AzCopy tool to your local computer. This version of AzCopy is just an executable file, so there's nothing to install.

    Note

    You can leave the **Import data** page open in case you need to copy the SAS URL again or select **Cancel** to close it.

## Step 2: Upload your PST files to Microsoft 365

Now you're ready to use the AzCopy tool to upload PST files to Microsoft 365. This tool uploads and stores PST files in a Microsoft-provided Azure Storage location in the Microsoft cloud. As previously explained, the Azure Storage location that you upload your PST files to is located in the same regional Microsoft datacenter where your organization is located. To complete this step, the PST files must be located in a file share or file server in your organization or in an Azure Storage location managed by your organization. The PST storage location is known as the source location in this procedure. Each time you run the AzCopy tool, you can specify a different source location.

Note

As previously stated, each PST file that you upload to the Azure Storage location should be no larger than 20 GB. PST files larger than 20 GB might impact the performance of the PST import process that you start in Step 6. Also, each PST file must have a unique name.

1. Open a Command Prompt on your local computer.
2. Go to the directory where you downloaded the azcopy.exe file in Step 1.
3. Run the following command to upload the PST files to Microsoft 365.

    ```powershell
    azcopy.exe copy "<Source location of PST files>" "<SAS URL>"
    ```

    Important

    You can specify a directory or an Azure Storage location as the source location in the previous command; you can't specify an individual PST file. All PST files in the source location are uploaded.

    The following table describes the azcopy.exe fields and their required values. The information you obtained in the previous step is used in the values for these fields.

    | Field | Description |
    | --- | --- |
    | Source | The first field specifies the source directory in your organization that contains the PST files that you want to upload to Microsoft 365. Alternatively, you can specify an Azure Storage location as the source location of the PST files to upload.  Be sure to surround the value of this field with double-quotation marks (" "). **Examples**: `"\\FILESERVER01\PSTs"` Or `"https://storageaccountid.blob.core.windows.net/PSTs?sp=racwdl&st=2021-09-21T07:25:53Z&se=2021-09-21T15:25:53Z&sv=2020-08-04&sr=c&sig=xxxxxx"` |
    | Destination | Specifies the SAS URL that you obtained in Step 1.  Be sure to surround the value of this parameter with double-quotation marks (" ").**Note:** If you use the SAS URL in a script or batch file, watch out for certain characters that need to be escaped. For example, you have to change `%` to `%%` and change `&` to `^&`.**Tip:** (Optional) You can specify a subfolder in the Azure Storage location to upload the PST files to. You do this by adding a subfolder location (after "ingestiondata") in the SAS URL. The first example doesn't specify a subfolder. That means the PST files are uploaded to the root (named *ingestiondata*) of the Azure Storage location. The second example uploads the PST files to a subfolder (named *PSTFiles*) in the root of the Azure Storage location. **Examples**: `"https://3c3e5952a2764023ad14984.blob.core.windows.net/ingestiondata?sv=2012-02-12&amp;se=9999-12-31T23%3A59%3A59Z&amp;sr=c&amp;si=IngestionSasForAzCopy201601121920498117&amp;sig=Vt5S4hVzlzMcBkuH8bH711atBffdrOS72TlV1mNdORg%3D"` Or `"https://3c3e5952a2764023ad14984.blob.core.windows.net/ingestiondata/PSTFiles?sv=2012-02-12&amp;se=9999-12-31T23%3A59%3A59Z&amp;sr=c&amp;si=IngestionSasForAzCopy201601121920498117&amp;sig=Vt5S4hVzlzMcBkuH8bH711atBffdrOS72TlV1mNdORg%3D"` |
    | `--recursive` | This optional flag specifies the recursive mode so that the AzCopy tool copies PST files that are located in subfolders in the source directory that is specified by the source field. The default value for this flag is `true`. **Note:** If you include this flag, PST files in subfolders have a different file pathname in the Azure Storage location after they're uploaded. You have to specify the exact file pathname in the CSV file that you create in Step 4. |
    | `--s2s-preserve-access-tier` | This optional flag is only required when the source location is a general-purpose v2 Azure Storage location that supports access tiers. For the PST Import scenario, there's no need to preserve the access tier when you copy PST files from your Azure Storage account to the Microsoft-provided Azure Storage location. In this case, you can include this flag and use a value of `false`. You don't need to use this flag when copy PST files from a classic Azure Storage account, which doesn't support access tiers. |
    |  |  |

For more information about the **azcopy.exe copy** command, see [azcopy copy](/en-us/azure/storage/common/storage-ref-azcopy-copy).

Here are examples of the syntax for the AzCopy tool using actual values for each parameter.

### Example 1

This example shows a source directory located on a file server or local computer.

```powershell
azcopy.exe copy "\\FILESERVER1\PSTs" "https://3c3e5952a2764023ad14984.blob.core.windows.net/ingestiondata?sv=2012-02-12&amp;se=9999-12-31T23%3A59%3A59Z&amp;sr=c&amp;si=IngestionSasForAzCopy201601121920498117&amp;sig=Vt5S4hVzlzMcBkuH8bH711atBffdrOS72TlV1mNdORg%3D"
```

### Example 2

This example shows a source directory located in a classic Azure Storage account with subdirectories.

```powershell
azcopy.exe copy "https://storageaccountid.blob.core.windows.net/PSTs?sp=racwdl&st=2021-09-21T07:25:53Z&se=2021-09-21T15:25:53Z&sv=2020-08-04&sr=c&sig=xxxxxx" "https://3c3e5952a2764023ad14984.blob.core.windows.net/ingestiondata?sv=2012-02-12&amp;se=9999-12-31T23%3A59%3A59Z&amp;sr=c&amp;si=IngestionSasForAzCopy201601121920498117&amp;sig=Vt5S4hVzlzMcBkuH8bH711atBffdrOS72TlV1mNdORg%3D" --recursive
```

### Example 3

This example shows a source directory located in a general-purpose v2 Azure Storage account. Access tiers aren't preserved when you upload the PST files.

```powershell
azcopy.exe copy "https://storageaccountid.blob.core.windows.net/PSTs?sp=racwdl&st=2021-09-21T07:25:53Z&se=2021-09-21T15:25:53Z&sv=2020-08-04&sr=c&sig=xxxxxx" "https://3c3e5952a2764023ad14984.blob.core.windows.net/ingestiondata?sv=2012-02-12&amp;se=9999-12-31T23%3A59%3A59Z&amp;sr=c&amp;si=IngestionSasForAzCopy201601121920498117&amp;sig=Vt5S4hVzlzMcBkuH8bH711atBffdrOS72TlV1mNdORg%3D" --s2s-preserve-access-tier=false
```

When you run the command, status messages show the progress of uploading the PST files. A final status message shows the total number of files that you successfully uploaded.

Tip

After you successfully run the **azcopy.exe copy** command and verify that all the parameters are correct, save a copy of the command line syntax to the same secured file where you copied the information you obtained in Step 1. Then you can copy and paste this command in a Command Prompt each time that you want to run the AzCopy tool to upload PST files to Microsoft 365. The only value you might have to change is for the source field. This change depends on the source directory where the PST files are located.

## (Optional) Step 3: View a list of the uploaded PST files

As an optional step, you can install and use the Microsoft Azure Storage Explorer (a free, open-source tool) to view the list of PST files that you uploaded to the Azure blob. Two good reasons to do this are:

- Verify that PST files from the shared folder or file server in your organization were successfully uploaded to the Azure blob.
- Verify the filename (and the subfolder pathname if you included one) for each PST file uploaded to the Azure blob. This verification is helpful when you're creating the PST mapping file in the next step because you need to specify both the folder pathname and filename for each PST file. Verifying these names can help reduce potential errors in your PST mapping file.

The Azure Storage Explorer standalone application is generally available. You can download the latest version using the link in the following procedure.

Important

You can't use the Azure Storage Explorer to upload or modify PST files. The only supported method for importing PST files is to use AzCopy. Also, you can't delete PST files that you upload to the Azure blob. If you try to delete a PST file, you receive an error about not having the required permissions. All PST files are automatically deleted from your Azure storage area. If there are no import jobs in progress, all PST files in the **ingestiondata** container are deleted 30 days after the most recent import job was created.

To install the Azure Storage Explorer and connect to your Azure Storage area:

1. Download and install the [Microsoft Azure Storage Explorer tool](https://go.microsoft.com/fwlink/p/?LinkId=544842).
2. Start the Microsoft Azure Storage Explorer.
3. On the **Select Resource** page in the **Connect to Azure Storage** dialog, select **Blob container**.
4. On the **Select Authentication Method** page, select the **Shared access signature (SAS)** option, then select **Next**.
5. On the **Enter Connection Info** page, paste the SAS URL that you obtained in Step 1 into the box under **Blob container SAS URL**, then select **Next**. After you paste the SAS URL, the box under **Display name** is autopopulated with **ingestiondata**.
6. On the **Summary** page, review the connection information, then select **Connect**.

    The **ingestiondata** container opens. It contains the PST files that you uploaded in Step 2. The **ingestiondata** container is located under **Storage Accounts** &gt; **(Attached Containers)** &gt; **Blob Containers**.
7. When you're finished using the Microsoft Azure Storage Explorer, right-click **ingestiondata**, then select **Detach** to disconnect from your Azure Storage area. Otherwise, you receive an error the next time you try to attach.

## Step 4: Create the PST Import mapping file

After you upload the PST files to the Azure Storage location for your organization, create a comma-separated value (CSV) file that specifies which user mailboxes the PST files go to. You'll submit this CSV file in the next step when you create a PST Import job.

1. [Download a copy of the PST Import mapping file](https://go.microsoft.com/fwlink/p/?LinkId=544717).
2. Open or save the CSV file to your local computer. The following example shows a completed PST Import mapping file (opened in NotePad). It's easier to use Microsoft Excel to edit the CSV file.

    ```console
    Workload,FilePath,Name,Mailbox,IsArchive,TargetRootFolder,ContentCodePage,SPFileContainer,SPManifestContainer,SPSiteUrl
    Exchange,,annb.pst,annb@contoso.onmicrosoft.com,FALSE,/,,,,
    Exchange,,annb_archive.pst,annb@contoso.onmicrosoft.com,TRUE,,,,,
    Exchange,,donh.pst,donh@contoso.onmicrosoft.com,FALSE,/,,,,
    Exchange,,donh_archive.pst,donh@contoso.onmicrosoft.com,TRUE,,,,,
    Exchange,PSTFiles,pilarp.pst,pilarp@contoso.onmicrosoft.com,FALSE,/,,,,
    Exchange,PSTFiles,pilarp_archive.pst,pilarp@contoso.onmicrosoft.com,TRUE,/ImportedPst,,,,
    Exchange,PSTFiles,tonyk.pst,tonyk@contoso.onmicrosoft.com,FALSE,,,,,
    Exchange,PSTFiles,tonyk_archive.pst,tonyk@contoso.onmicrosoft.com,TRUE,/ImportedPst,,,,
    Exchange,PSTFiles,zrinkam.pst,zrinkam@contoso.onmicrosoft.com,FALSE,,,,,
    Exchange,PSTFiles,zrinkam_archive.pst,zrinkam@contoso.onmicrosoft.com,TRUE,/ImportedPst,,,,
    ```

    The first row, or header row, of the CSV file lists the parameters that the PST Import service uses to import the PST files to user mailboxes. Each parameter name is separated by a comma. Each row under the header row represents the parameter values for importing a PST file to a specific mailbox. You need a row for each PST file that you want to import to a user mailbox. You can have a maximum of 500 rows in the CSV mapping file. To import more than 500 PST files, create multiple mapping files and create multiple import jobs in Step 5.

    Note

    Don't change anything in the header row, including the SharePoint parameters; the PST Import process ignores them. Also, be sure to replace the placeholder data in the mapping file with your actual data.
3. Use the information in the following table to populate the CSV file with the required information.

    | Parameter | Description | Example |
    | --- | --- | --- |
    | `Workload` | Specifies the service that data is imported to. To import PST files to user mailboxes, use `Exchange`. | `Exchange` |
    | `FilePath` | Specifies the folder location in the Azure Storage location that you uploaded the PST files to in Step 2.  If you don't include an optional subfolder name in the SAS URL in the `/Dest:` parameter in Step 2, leave this parameter blank in the CSV file. If you include a subfolder name, specify it in this parameter (see the second example). The value for this parameter is case-sensitive.  Either way, *don't* include "ingestiondata" in the value for the `FilePath` parameter. **Important:** The case for the file path name must be the same as the case you used if you include an optional subfolder name in the SAS URL in the destination field in Step 2. For example, if you use `PSTFiles` for the subfolder name and then use `pstfiles` in the `FilePath` parameter in CSV file, the import for the PST file fails. Be sure to use the same case in both instances. | (leave blank)  Or `PSTFiles` |
    | `Name` | Specifies the name of the PST file that is imported to the user mailbox. The value for this parameter is case-sensitive. The file name of each PST file in the mapping file for an import job must be unique. **Important:** The case for the PST file name in the CSV file must be the same as the PST file that you uploaded to the Azure Storage location in Step 2. For example, if you use `annb.pst` in the `Name` parameter in the CSV file, but the name of the actual PST file is `AnnB.pst`, the import for that PST file fails. Be sure that the name of the PST in the CSV file uses the same case as the actual PST file. | `annb.pst` |
    | `Mailbox` | Specifies the email address of the mailbox that the PST file is imported to. You can't specify a public folder or unified group because the PST Import Service doesn't support importing PST files to unified groups or to public folders.  To import a PST file to an inactive mailbox, you have to specify the mailbox GUID for this parameter. To obtain this GUID, run the following PowerShell command in Exchange Online: `Get-Mailbox <identity of inactive mailbox> -InactiveMailboxOnly \FL ExchangeGuid`. | **Note:** Sometimes you have multiple mailboxes with the same email address, where one mailbox is an active mailbox and the other mailbox is in a soft-deleted (or inactive) state. In these situations, you have to specify the mailbox GUID to uniquely identify the mailbox to import the PST file to. To obtain this GUID for active mailboxes, run the following PowerShell command: `Get-Mailbox <identity of active mailbox> \| FL ExchangeGuid`. To obtain the GUID for soft-deleted (or inactive) mailboxes, run this command: `Get-Mailbox <identity of soft-deleted or inactive mailbox> -SoftDeletedMailbox \| FL ExchangeGuid` |
    | `IsArchive` | Specifies whether to import the PST file to the user's archive mailbox. There are two options: **FALSE:** Imports the PST file to the user's primary mailbox. **TRUE:** Imports the PST file to the user's archive mailbox. This assumes that the [user's archive mailbox is enabled](enable-archive-mailboxes). If you set this parameter to `TRUE` and the user's archive mailbox isn't enabled, the import for that user fails. If an import fails for one user (because their archive isn't enabled and this property is set to `TRUE`), the other users in the import job isn't affected.  If you leave this parameter blank, the PST file is imported to the user's primary mailbox. **Note:** To import a PST file to a cloud-based archive mailbox for a user whose primary mailbox is on-premises, just specify `TRUE` for this parameter and specify the email address for the user's on-premises mailbox for the `Mailbox` parameter. **Note:** When this parameter is `TRUE`, the PST file is imported into the user's main archive mailbox only, and a 100-GB-per-import limit applies. For more information, see [Archive mailbox import limit](pst-import-overview#archive-mailbox-import-limit). | `FALSE` Or `TRUE` |
    | `TargetRootFolder` | Specifies the mailbox folder that the PST file is imported to.  If you leave this parameter blank, the PST file is imported to a new folder named **Imported** at the root level of the mailbox (the same level as the Inbox folder and the other default mailbox folders).  If you specify `/`, the folders and items in the PST file are imported to the top of the folder structure in the target mailbox or archive. If a folder exists in the target mailbox (for example, default folders such as Inbox, Sent Items, and Deleted Items), the items in that folder in the PST are merged into the existing folder in the target mailbox. For example, if the PST file contains an Inbox folder, items in that folder are imported to the Inbox folder in the target mailbox. New folders are created if they don't exist in the folder structure for the target mailbox.  If you specify `/<foldername>`, items and folders in the PST file are imported to a folder named *&lt;foldername&gt;* . For example, if you use `/ImportedPst`, items would be imported to a folder named **ImportedPst**. This folder is located in the user's mailbox at the same level as the Inbox folder. **Tip:** Consider running a few test batches to experiment with this parameter so you can determine the best folder location to import PST files. | (leave blank)  Or `/` Or `/ImportedPst` |
    | `ContentCodePage` | This optional parameter specifies a numeric value for the code page to use for importing PST files in the ANSI file format. This parameter is used for importing PST files from Chinese, Japanese, and Korean (CJK) organizations because these languages typically use a double byte character set (DBCS) for character encoding. If this parameter isn't used to import PST files for languages that use DBCS for mailbox folder names, the folder names are often garbled after they're imported.  For a list of supported values to use for this parameter, see [Code Page Identifiers](/en-us/windows/win32/intl/code-page-identifiers). **Note:** As previously stated, this is an optional parameter and you don't have to include it in the CSV file. Or you can include it and leave the value blank for one or more rows. | (leave blank)  Or `932` (which is the code page identifier for ANSI/OEM Japanese) |
    | `SPFileContainer` | For PST Import, leave this parameter blank. | Not applicable |
    | `SPManifestContainer` | For PST Import, leave this parameter blank. | Not applicable |
    | `SPSiteUrl` | For PST Import, leave this parameter blank. | Not applicable |

## Step 5: Create a PST Import job

In this step, you create the PST import job in the Import service in Microsoft 365. As previously explained, you submit the PST import mapping file that you created in Step 4. After you create the job, Microsoft 365 analyzes the data in the PST files. Then, it gives you an opportunity to filter the data that actually gets imported to the mailboxes specified in the PST import mapping file (see Step 6).

1. Go to https://purview.microsoft.com and sign in with the credentials for an administrator account in your organization.
2. In the left pane of the Microsoft Purview portal, select **Data lifecycle management** &gt; **Microsoft 365** &gt; **Import**.
3. On the **Import** tab, select ![Add Icon.](media/itpro-eac-addicon.gif)**New import job**.

    Note

    You need the appropriate permissions to access the **Import** page in the Microsoft Purview portal and create an import job. For more information, see the **Before you import PST files** section.
4. Type a name for the PST import job, and then select **Next**. Use lowercase letters, numbers, hyphens, and underscores. You can't use uppercase letters or include spaces in the name.
5. On the **Do you want to upload or ship data?** page, select **Upload your data** and then select **Next**.
6. In step 4 on the **Import data** page, select the **I'm done uploading my files** and **I have access to the mapping file** check boxes, and then select **Next**.

    ![Select the two check boxes in step 4.](media/9f2427e8-3af2-4e27-95e6-a9f08430d3d8.png)
7. On the **Select the mapping file** page, select **Select mapping file** to submit the CSV mapping file that you created in Step 4.

    ![Select mapping file to submit the CSV file you created for the import job.](media/d30b1d73-80bb-491e-a642-a21673d06889.png)
8. After the name of the CSV file appears under **Mapping file name**, select **Validate** to check your CSV file for errors.

    ![Select Validate to check the CSV file for errors.](media/4680999d-5538-4059-b878-2736a5445037.png)

    The CSV file must pass validation to create a PST import job. The file name turns green after successful validation. If validation fails, select the **View log** link. A validation error report opens, with an error message for each row in the file that failed.

    Note

    As previously explained, a mapping file can have a maximum of 500 rows. Validation fails if the mapping file contains more than 500 rows. To import more than 500 PST files, create multiple mapping files and multiple import jobs.
9. After the mapping file is successfully validated, read the terms and conditions document, and then select the checkbox.
10. Select **Save** to submit the job, and then select **Close** after the job is successfully created.

    A status flyout page is displayed, with a status of **Analysis in progress**. The new import job is displayed in the list on the **Import PST files** page.
11. Select **Refresh**![Refresh icon.](media/o365-mdm-policy-refreshicon.gif) to update the status information displayed in the **Status** column. When the analysis completes and the data is ready to import, the status changes to **Analysis completed**.

    You can select the import job to display the status flyout page, which contains more detailed information about the import job such as the status of each PST file listed in the mapping file.

## Step 6: Filter data and start the PST Import job

After you create the import job in Step 5, Microsoft 365 safely and securely analyzes the data in the PST files. It identifies the age of the items and the different message types included in the PST files. When the analysis is complete and the data is ready to import, you can import all the data contained in the PST files or trim the data by setting filters that control what data gets imported.

1. On the **Import** tab in the Microsoft Purview portal, select the import jobs that you created in Step 5. Then select **Import to Microsoft 365**.

    The **Filter your data** page appears. It contains the data insights from the analysis of the PST files, including information about the age of the data. You can filter the data that you import or import all the data as is.

    ![You can trim the data in the PST files or import all of it.](media/287fc030-99e9-417b-ace7-f64617ea5d4e.png)
2. Do one of the following steps:

    1. To trim the data that you import, select **Yes, I want to filter it before importing**.

        For detailed step-by-step instructions about filtering the data in the PST files and then starting the import job, see [Filter data when importing PST files to Microsoft 365](pst-import-filter-data).

        Or
    2. To import all data in the PST files, select **No, I want to import everything,** and select **Next**.
3. If you chose to import all the data, select **Import data** to start the import job.

    The **Import PST files** page displays the status of the import job. Select ![Refresh icon.](media/o365-mdm-policy-refreshicon.gif)**Refresh** to update the status information in the **Status** column. Select the import job to display the status flyout page, which shows status information about each PST file being imported.

## More information

- Why import PST files to Microsoft 365?

    - It's a good way to import your organization's archival messaging data to Microsoft 365.
    - The data is available to the user from all devices because it's stored in the cloud.
    - It helps address compliance needs of your organization by letting you apply Microsoft Purview features to the data from the PST files that you imported. This benefit includes:
    - Enabling [archive mailboxes](enable-archive-mailboxes) and [auto-expanding archiving](enable-autoexpanding-archiving) to give users additional mailbox storage space to store the data that you imported.
    - Placing mailboxes on [Litigation Hold](/en-us/exchange/policy-and-compliance/holds/litigation-holds) to retain the data that you imported.
    - Using Microsoft [eDiscovery tools](ediscovery-content-search-overview) to search the data that you imported.
    - Using [Microsoft 365 retention policies](retention) to control how long the data that you imported will be retained, and what action to take after the retention period expires.
    - Searching the [audit log](audit-search) for mailbox-related events that affect the data that you imported.
    - Importing data to [inactive mailboxes](inactive-mailboxes-in-office-365) to archive data for compliance purposes.
    - Using [data loss prevention policies](dlp-learn-about-dlp) to prevent sensitive data from leaking outside your organization.
- As previously explained, the Microsoft 365 Import service turns on the retention hold setting (for an indefinite duration) after PST files are imported to a mailbox. This setting means the *RetentionHoldEnabled* property is set to **True** so that the retention policy assigned to the mailbox isn't processed. This setting gives the mailbox owner time to manage the newly imported messages by preventing a deletion or archive policy from deleting or archiving older messages. Here are some steps you can take to manage this retention hold:

    - After a certain time, turn off the retention hold by running the **Set-Mailbox -RetentionHoldEnabled $false** command. For instructions, see [Place a mailbox on retention hold](/en-us/exchange/security-and-compliance/messaging-records-management/mailbox-retention-hold).
    - Configure the retention hold so that it's turned off on some date in the future. Run the **Set-Mailbox -EndDateForRetentionHold *date*** command. For example, assuming that today's date is June 1, 2016 and you want the retention hold turned off in 30 days, run the following command: **Set-Mailbox -EndDateForRetentionHold 7/1/2016**. In this scenario, leave the **RetentionHoldEnabled** property set to *True*. For more information, see [Set-Mailbox](/en-us/powershell/module/exchange/set-mailbox).
    - Change the settings for the retention policy that's assigned to the mailbox so that older items that you imported aren't immediately deleted or moved to the user's archive mailbox. For example, you could lengthen the retention age for a deletion or archive policy that's assigned to the mailbox. In this scenario, turn off the retention hold on the mailbox after you change the settings of the retention policy. For more information, see [Set up an archive and deletion policy for mailboxes in your organization](set-up-an-archive-and-deletion-policy-for-mailboxes).

### How the import process works

Use the network upload option and the Microsoft 365 Import service to bulk-import PST files to user mailboxes. Network upload means that you upload the PST files to a temporary storage area in the Microsoft cloud. Then the Microsoft 365 Import service copies the PST files from the storage area to the target user mailboxes.

Here's an illustration and description of the network upload process to import PST files to mailboxes in Microsoft 365.

![Workflow of the network upload process to import PST files to Microsoft 365.](media/9e05a19e-1e7a-4f1f-82df-9118f51588c4.png)

1. **Download the PST import tool and key to private Azure Storage location:** Download the AzCopy command-line tool and an access key to upload the PST files to an Azure Storage location in the Microsoft cloud. Get these from the **Import** page in the Microsoft Purview portal. The key, called a secure access signature (SAS) key, gives you the necessary permissions to upload PST files to a private and secure Azure Storage location. This access key is unique to your organization and helps prevent unauthorized access to your PST files after you upload them to the Microsoft cloud. Importing PST files doesn't require your organization to have a separate Azure subscription.
2. **Upload the PST files to the Azure Storage location:** Use the azcopy.exe tool (downloaded in step 1) to upload and store your PST files in an Azure Storage location that resides in the same regional Microsoft datacenter where your organization is located. To upload them, the PST files that you want to import must be located in a file share or file server in your organization.

    You can optionally view the list of PST files after you upload them to the Azure Storage location.
3. **Create a PST import mapping file:** After you upload the PST files to the Azure Storage location, create a comma-separated value (CSV) file that specifies which user mailboxes the PST files go to. A PST file can go to a user's primary mailbox or their archive mailbox. The Microsoft 365 Import service uses the information in the CSV file to import the PST files.
4. **Create a PST import job:** Create a PST import job on the **Import PST files** page in the Microsoft Purview portal and submit the PST import mapping file you created. After you create the import job, Microsoft 365 analyzes the data in the PST files, then gives you an opportunity to set filters that control what data actually gets imported to the mailboxes specified in the PST import mapping file.
5. **Filter the PST data that you import to mailboxes:** After you create and start the import job, Microsoft 365 safely and securely analyzes the data in the PST files by identifying the age of the items and the different message types included in the PST files. When the analysis completes and the data is ready to import, you can import all the data contained in the PST files or trim the data by setting filters that control what data gets imported.
6. **Start the PST import job:** After you start the import job, Microsoft 365 uses the information in the PST import mapping file to import the PSTs files from the Azure Storage location to user mailboxes. The **Import PST files** page in the Microsoft Purview portal displays status information about the import job, including information about each PST file being imported. When the import job finishes, the status for the job is set to **Complete**.