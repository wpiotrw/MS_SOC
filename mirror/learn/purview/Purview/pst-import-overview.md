---
layout: Conceptual
title: Learn about importing organization PST files | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/pst-import-overview
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use the Import service in the Microsoft Purview portal to bulk-import email data (PST files) to user mailboxes.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-11T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-exchange-legacy
ms.collection:
- purview-compliance
- import
search.appverid: MET150
ai-usage: ai-assisted
locale: en-us
document_id: 72f5be7d-4213-5f13-b3d2-38a4f173d914
document_version_independent_id: 72f5be7d-4213-5f13-b3d2-38a4f173d914
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/pst-import-overview.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: pst-import-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/pst-import-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf9b82c5-b6dc-45f3-b005-b1bc5fc03bea
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c85d34e-bfd2-4466-957c-f0b61e9692df
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 94994be9-a0d3-c6ce-d20b-c542e8b4a560
---

# Learn about importing organization PST files | Microsoft Learn

Note

This article is for administrators. Are you trying to import PST files to your own mailbox? See [Import email, contacts, and calendar from an Outlook .pst file](https://go.microsoft.com/fwlink/p/?LinkID=785075).

Use the Import service in the Microsoft Purview portal to quickly bulk-import PST files to Exchange Online mailboxes in your organization. You can import PST files to Microsoft 365 in two ways:

- **Network upload**: Upload the PST files over the network to a temporary Azure Storage location in the Microsoft cloud. Then use the Microsoft 365 Import service to import the PST data to mailboxes in your organization.
- **Drive shipping**: Copy the PST files to a BitLocker-encrypted hard drive and then physically ship the drive to Microsoft. When Microsoft receives the hard drive, data center personnel upload the data to a temporary Azure Storage location in the Microsoft cloud. Then use the Microsoft 365 Import service to import the data to mailboxes in your organization.

## Why import email data to Microsoft 365?

- Import your organization's archival messaging data to Microsoft 365.
- Use the [Intelligent Import](pst-import-filter-data) feature to filter the items in PST files that get imported to the target mailboxes. This feature lets you trim the imported data by setting filters.
- Importing email data to Microsoft 365 helps address your organization's compliance needs by letting you:
    - Enable [archive mailboxes](enable-archive-mailboxes) and [auto-expanding archiving](autoexpanding-archiving) to give users additional mailbox storage space.
    - Place mailboxes on [Litigation Hold](/en-us/exchange/policy-and-compliance/holds/litigation-holds) to retain content.
    - Use the [Content Search tool](ediscovery-content-search) to search for mailbox content.
    - Use [eDiscovery cases](ediscovery-standard-get-started) to manage your organization's legal investigations.
    - Use [retention policies](retention) in the Microsoft Purview portal to control how long mailbox content is retained, and then delete content after the retention period expires.
- Importing data to Microsoft 365 helps protect against data loss. Email data that you import to Microsoft 365 inherits the high availability features of Exchange Online.
- Because you store email data in the cloud, users can access it from all their devices.

## Select your import method

Use the following table to help decide which import method is best for your organization:

| Factor | Network upload | Drive shipping |
| --- | --- | --- |
| Cost | Free | Costs apply - see [Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description) for details |
| Region availability | United States, Canada, Brazil, United Kingdom, France, Germany, Switzerland, Norway, Europe, India, East Asia, Southeast Asia, Japan, Republic of Korea, Australia, UAE, Israel, Mexico, Taiwan, New Zealand | United States, Canada, Brazil, United Kingdom, Europe, India, East Asia, Southeast Asia, Japan, Republic of Korea, Australia, Mexico, Taiwan, New Zealand (not available in Germany or Switzerland) |
| Licensing | All commercial licensing agreements | Microsoft Enterprise Agreement (EA) only. Not available through Microsoft Products and Services Agreement (MPSA). |
| Max data volume | Unlimited (network dependent) | 10 TB per drive, maximum 10 drives per import job |
| Upload time | Several hours per TB (depends on your network capacity) | 7-10 business days after Microsoft receives the drive |
| Best for | Ongoing imports or smaller migrations | Large one-time data migrations |

## Requirements and limits

Before you import PST files, review the following requirements and limits that apply to both import methods.

### Permissions

To create import jobs and import PST files, you need the following roles:

- **Mailbox Import Export** role in Exchange Online. By default, no role group has this role assigned. You can add it to the **Organization Management** role group, or create a new role group and assign the role.
- **Mail Recipients** role in Exchange Online. By default, the **Organization Management** and **Recipient Management** role groups have this role assigned.

    Or
- You're a global administrator in your organization.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

Tip

Consider creating a new role group in Exchange Online specifically for importing PST files. Assign the **Mailbox Import Export** and **Mail Recipients** roles to the new role group, and then add members.

### PST file format

Both ANSI and Unicode PST file formats are supported. Import files that use the Unicode PST file format. However, you can also import files that use the ANSI PST file format, such as those for languages that use a double-byte character set (DBCS). You can import PST files from Outlook 2007 and later versions to Microsoft 365.

For more information about ANSI PST files, see Step 4 in [Use network upload to import PST files](pst-import-network-upload#step-4-create-the-pst-import-mapping-file) or Step 3 in [Use drive shipping to import PST files](pst-import-drive-shipping#step-3-create-the-pst-import-mapping-file).

### Message size limit

If a PST file contains a mailbox item that's larger than 150 MB, the import process skips the item and doesn't import it. Items larger than 150 MB aren't imported because 150 MB is the message size limit in Exchange Online. For more information, see [Message limits in Exchange Online](/en-us/office365/servicedescriptions/exchange-online-service-description/exchange-online-limits#message-limits).

### Folder hierarchy limit

You can't import a PST file that has 300 or more levels of nested folders.

### Supported mailbox scenarios

You can import PST files to the following mailbox types:

- **Inactive mailboxes**: You can import PST files to an inactive mailbox in Microsoft 365 by using either network upload or drive shipping. Specify the GUID of the inactive mailbox in the `Mailbox` parameter of the PST Import mapping file.
- **Online archive mailboxes in hybrid deployments**: You can import PST files to a cloud-based archive mailbox for a user whose primary mailbox is on-premises. Specify the email address for the user's on-premises mailbox in the `Mailbox` parameter, and set the `IsArchive` parameter to **TRUE** in the PST Import mapping file.
- **Public folders**: You can't import PST files to public folders.

### PST file size

Upload or copy PST files that are no larger than 20 GB. Large PST files can affect the performance of the import process.

### Archive mailbox import limit

When you import PST files to a user's archive mailbox (the `IsArchive` parameter set to **TRUE**), data is imported into the user's main archive mailbox only. The import doesn't target auto-expanding archive storage, because auto-expanding archive storage is provisioned on demand rather than in advance.

As a result, you can't import more than 100 GB of data into a user's archive in a single import. To import more than 100 GB, divide the data across multiple imports and allow time for the archive to auto-expand between imports. For more information, see [Learn about auto-expanding archiving](autoexpanding-archiving).

## Plan your import

Before you start importing PST files, review the following planning considerations.

### Import rate

A Microsoft 365 mailbox imports a PST file at a rate of about 24 GB per day. This rate isn't guaranteed and can vary based on server workload and transient performance issues. If this rate doesn't meet your needs, consider other methods for migrating email data to Microsoft 365. For more information, see [Ways to migrate multiple email accounts to Microsoft 365](/en-us/Exchange/mailbox-migration/mailbox-migration).

If you import different PST files to different target mailboxes, the import process runs in parallel (each PST/mailbox pair is imported simultaneously). If you import multiple PST files to the same mailbox, the process imports them sequentially (one at a time).

### Retention hold after import

After you import PST files to a Microsoft 365 mailbox, the retention hold setting for the mailbox is turned on indefinitely. This setting means that the retention policy assigned to the mailbox isn't processed until you turn off the retention hold or set a date to turn off the hold. If messages you import to a mailbox are old, the retention settings configured for the mailbox might cause those messages to be permanently deleted (purged). Placing the mailbox on retention hold gives the mailbox owner time to manage the newly imported messages, or gives you time to change the retention settings for the mailbox.

### MaxReceiveSize property

By default, a Microsoft 365 mailbox can receive messages up to 35 MB. However, Microsoft 365 supports a maximum message receive size of 150 MB. If you import a PST file that contains an item larger than 35 MB, the Microsoft 365 Import service automatically sets the *MaxReceiveSize* property on the target mailbox to 150 MB.

Tip

To check the message receive size for a mailbox, run this command in Exchange Online PowerShell: `Get-Mailbox <user mailbox> | FL MaxReceiveSize`.

## How the PST import process works

Here's an illustration and description of the complete PST import process. The illustration shows the primary workflow and highlights the differences between the network upload and drive shipping methods.

![Workflow of PST import process.](media/76997b69-67d7-433a-a0ca-9389f85a36a1.png)

1. **Download the PST import tools and key to private Azure Storage location**: Download the tool and access key you use to upload the PST files or copy them to a hard drive. Get these items from the **Import** page in the Microsoft Purview portal. The key provides you (or Microsoft data center personnel in the case of drive shipping) with the necessary permissions to upload PST files to a private and secure Azure Storage location. This access key is unique to your organization and helps prevent unauthorized access to your PST files after you upload them to the Microsoft cloud. Importing PST files to Microsoft 365 doesn't require your organization to have a separate Azure subscription.
2. **Upload or copy the PST files**: The next step depends on whether you're using network upload or drive shipping to import PST files. In both cases, use the tool and secure storage key that you obtained in the previous step.

    - **Network upload**: Use the AzCopy.exe tool (downloaded in step 1) to upload and store your PST files in an Azure Storage location in the Microsoft cloud. The Azure Storage location that you upload your PST files to is located in the same regional Microsoft datacenter as your organization.

        To upload them, the PST files that you want to import must be located in a file share or file server in your organization.
    - **Drive shipping**: Use the WAImportExport.exe tool (downloaded in step 1) to copy your PST files to the hard drive. This tool encrypts the hard drive with BitLocker and then copies the PSTs to the hard drive. Like network upload, the PST files that you want to copy to the hard drive must be located in a file share or file server in your organization.
3. **Create a PST import mapping file**: After you upload the PST files to the Azure Storage location or copy them to a hard drive, create a comma-separated value (CSV) file that specifies which user mailboxes the PST files go to (and a PST file can go to a user's primary mailbox or their archive mailbox). [Download a copy of the PST Import mapping file](https://go.microsoft.com/fwlink/p/?LinkId=544717). The Microsoft 365 Import service uses the information to import the PST files.
4. **Create a PST import job**: Create a PST import job on the **Import PST files** page in the Microsoft Purview portal and submit the PST import mapping file you created in the previous step. For network upload (because the PST files are uploaded to Azure) Microsoft 365 analyzes the data in the PST files and then gives you an opportunity to set filters that control what data actually gets imported to the mailboxes specified in the PST import mapping file.

    For drive shipping, a few other things happen at this point in the process.

    - You physically ship the hard drive to a Microsoft data center (the shipping address for the Microsoft data center is displayed when the import job is created).
    - When Microsoft receives the hard drive, data center personnel upload the PST files on the hard drive to the Azure Storage location for your organization. As previously explained, your PST files are uploaded to an Azure Storage location that resides in the same regional Microsoft datacenter where your organization is located.

        Note

        The PST files on the hard drive are uploaded to Azure within 7 to 10 business days after Microsoft receives the hard drive.

        Like the network upload process, Microsoft 365 then analyzes the data in the PST files and gives you an opportunity to set filters that control what data actually gets imported to the mailboxes specified in the PST import mapping file.
    - Microsoft ships the hard drive back to you.
5. **Filter the PST data that will be imported to mailboxes**: After you create the import job (and after the PST files from a drive shipping job are uploaded to the Azure Storage location) Microsoft 365 analyzes the data in the PST files (safely and securely) by identifying the age of the items and the different message types included in the PST files. When the analysis is completed and the data is ready to import, you have the option to import all the data contained in the PST files or you can trim the data that's imported by setting filters that control what data gets imported.
6. **Start the PST import job**: After you start the import job, Microsoft 365 uses the information in the PST import mapping file to import the PST files from the Azure Storage location to user mailboxes. Status information about the import job (including information about each PST file being imported) is displayed on the **Import PST files** page in the Microsoft Purview portal. When the import job finishes, the status for the job is set to **Complete**.

## Step-by-step instructions

For detailed, step-by-step instructions for bulk-importing your organization's PST files to Microsoft 365, see one of the following articles:

- [Use network upload to import PST files to Microsoft 365](pst-import-network-upload)
- [Use drive shipping to import PST files](pst-import-drive-shipping)

## Import SharePoint data to Microsoft 365

You can also import files and documents to SharePoint sites and OneDrive accounts in your organization. For more information, see the following articles:

- [Migrate to SharePoint Online](/en-us/sharepointmigration/migrate-to-sharepoint-online)
- [Introducing the SharePoint Migration Tool](/en-us/sharepointmigration/introducing-the-sharepoint-migration-tool)
- [Migrate to SharePoint Online using PowerShell](/en-us/sharepointmigration/overview-spmt-ps-cmdlets)
- [Migrate your file share content to SharePoint Online using the Azure Data Box](/en-us/sharepointmigration/how-to-migrate-file-share-content-to-spo-using-azuredatabox)

## Frequently asked questions

For frequently asked questions about importing PST files, including duplicate handling, message properties, and common issues, see [FAQ about importing PST files](pst-import-faq).