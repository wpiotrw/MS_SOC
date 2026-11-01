---
layout: Conceptual
title: Hash and upload the sensitive information source table for exact data match sensitive information types | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-get-started-exact-data-match-hash-upload
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
ms.date: 2026-06-26T00:00:00.0000000Z
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Learn how to use the EDM Upload Agent to hash and upload your sensitive information source table for exact data match sensitive information types, including prerequisites, data formatting, and single or two-computer upload methods.
ms.custom: seo-marvel-apr2020, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 3d828827-ffef-25f6-b4d6-cba4cc6434f9
document_version_independent_id: 3d828827-ffef-25f6-b4d6-cba4cc6434f9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-get-started-exact-data-match-hash-upload.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-get-started-exact-data-match-hash-upload
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-get-started-exact-data-match-hash-upload.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/fc3f72c2-fb6f-4cea-95ee-b444e52254ee
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f12cf087-582d-48ac-a085-0c19adf1e391
platformId: 9502dc1f-7e55-a629-d078-c282a9eb4f2a
---

# Hash and upload the sensitive information source table for exact data match sensitive information types | Microsoft Learn

## Overview

This article shows you how to hash and upload your sensitive information source table as part of the exact data match (EDM) sensitive information type workflow. After you create an EDM schema and configure your sensitive information type, you use the EDM Upload Agent to hash your source data and securely upload it to Microsoft 365. The article covers prerequisites, data formatting requirements, and step-by-step instructions for both single-computer and two-computer upload methods. The procedures in this article apply to the following workflows:

## Products and services this hashing and upload procedure applies to

- [Create exact data match sensitive information type new experience](sit-create-edm-sit-unified-ux-workflow)
- [Create exact data match sensitive information type classic experience](sit-create-edm-sit-classic-ux-workflow)

## Hash and upload the sensitive information source table

In this phase, you:

1. Set up a custom security group and user account.
2. Set up the Exact Data Match (EDM) Upload Agent tool.
3. Use the EDM Upload Agent tool to hash, with a salt value, the sensitive information source table, and upload it.

To hash and upload your sensitive data, use either the **Two-computer method** or the **Single computer method** as described in Hash and upload your data. You can't use custom hashing for uploading data. You can only use these two methods as described in the documentation for hashing and uploading.

Best practice is to use two computers to separate the processes of hashing and uploading your sensitive data. Separating the steps across two computers helps ensure that your actual data is never available in clear text form on a computer that might be compromised due to its connection to the internet. Separating hashing and uploading across two computers also makes any issues you encounter easier to isolate.

## Prerequisites

Before you hash and upload your sensitive information source table, make sure you meet the following technology, account, schema, and data formatting requirements.

### Technology requirements

To use the EDM Upload Agent to hash and upload your sensitive data, ensure that the following requirements are in place.

- A work or school account for Microsoft 365. This account must be added to the **EDM\_DataUploaders** security group.
- A computer with one of the following operating systems. This computer runs the **EDM Upload Agent**.
    - Windows 10 and later versions
    - Windows server 2019 and later versions
    - Windows Server 2016 with .NET version 4.6.2
- A directory on the computer you use for uploading your data. This directory contains:
    - The EDM Upload Agent.
    - Your sensitive information data file in *.csv*, *.tsv*, or pipe (|) format. By default, the EDM Upload Agent expects your data file to be in .csv format. &gt; [!TIP] 

> 
> You can use a file with data that is separated by tabs or pipes (instead of commas), by indicating either the "(Tab)" or "(|)" options with the `/ColumnSeparated` parameter. For example: `EdmUploadAgent.exe /UploadData /DataStoreName PatientRecords /DataFile C:\Edm\Hash\PatientRecords.csv /HashLocation C:\Edm\Hash /Schema edm.xml /AllowedBadLinesPercentage 5`
    - The output hash and salt files that are created when completing the hash procedure.
    - The datastore name from the **edm.xml** file. Our example uses `PatientRecords`.

### Security group and user account requirements

The account you use to upload your sensitive information source table must be a member of one of these roles to create and manage the exact data match sensitive information types.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

| Role | Can create security groups and add members | Notes |
| --- | --- | --- |
| Groups Administrator | Yes | Best least privilege option |
| User Administrator | Yes | Most commonly used role |
| Global Administrator | Yes | Grants full control, don't use |

You can use an existing security group or create a new one for managing EDM data uploads.

1. Go to the admin center using the appropriate [portal link for your subscription](sit-get-started-exact-data-match-based-sits-overview#portal-links-for-your-subscription) and [create a security group](/en-us/office365/admin/email/create-edit-or-delete-a-security-group) called **EDM\_DataUploaders**.
2. Add one or more users to the **EDM\_DataUploaders** security group. These users manage the database of sensitive information.

### Exact Data Match Schema

If you used the [EDM schema and sensitive information type tool for the **new** experience](sit-create-edm-sit-unified-ux-schema-rule-package#create-your-edm-schema-and-sit) or the [EDM sensitive information type/rule package for the **classic** experience](sit-get-started-exact-data-match-create-rule-package#create-exact-data-match-sensitive-information-typerule-package), you **must** download that schema to hash your sensitive information source table. For more information, see [Exporting the EDM schema file in XML format](sit-get-started-exact-data-match-create-schema#exporting-the-edm-schema-file-in-xml-format).

To download the EDM schema file for your sensitive information type, open a Command Prompt window and run the following command:

`EdmUploadAgent.exe /SaveSchema /DataStoreName <schema name> /OutputDir <path to output folder>`

### Data formatting requirements

Before you hash and upload your sensitive data, run a search for any special characters in the table that might cause problems in parsing the content.

To catch formatting or column-mapping issues before you upload, validate the data file against the EDM schema by using the EDM Upload Agent with the following syntax:

```powershell
EdmUploadAgent.exe /ValidateData /DataFile [data file] /Schema [schema file]
```

#### Common formatting issues

The following formatting problems commonly cause validation or parsing errors when you prepare your sensitive information source table.

1. **Mismatched number of columns:** This issue can be due to the presence of commas or quote characters within values in the table that EDM interprets as column delimiters. Unless they're surrounding a whole value, single and double quotes can cause the tool to misidentify the start and end of individual columns.
2. **Single quote characters or commas inside a value:** For example, if a person's name includes a single quote such as *Tom O'Neil* or a city's name starts with an apostrophe such as *'s-Gravenhage*, you need to modify the data export process used to generate the sensitive information table and surround such columns with double quotes.
3. **Double quote characters inside values:** Best practice is to use the tab-delimited format for the table. Tab-delimited tables are less susceptible to such issues.

## Hash and upload your data

Select the appropriate EDM Upload Agent for your organization.

| EDM Upload Agent version | Description |
| --- | --- |
| [Commercial + GCC](https://download.microsoft.com/download/0e8c4b95-7d2f-4614-b378-f4103220e5c9/EdmUploadAgent.msi) | Most commercial customers should use this option. |
| [GCC-High](https://download.microsoft.com/download/628330dd-4fab-4d07-8124-33de1f5f428a/EdmUploadAgentGccHi.msi) | This option is specifically for high-security government cloud subscribers. |
| [DoD](https://download.microsoft.com/download/a1f7655f-ce55-4f2b-a865-749bb213b48e/EdmUploadAgentDoD.msi) | This option is specifically for United States Department of Defense cloud customers. |

Each version of the EDM Upload Agent automatically adds a salt value to your hashed data. If you choose, you can provide your own salt value by using the `/Salt` parameter when running the EDM Upload Agent.

Warning

If you choose to use your own salt value, you can't go back to use the standard version of the EDM Upload Agent for your use case. If you want to hash and upload from one computer, the computer you use must be able to connect directly to your Microsoft 365 tenant. Additionally, your clear-text sensitive information source table file must reside on this computer so that it can be hashed.

# [Two-computer method](#tab/two-computers)
Your sensitive information source table is formatted as clear-text. By using one computer for the hash step and a different computer for the upload step, you protect your data from being exposed in clear text on a computer with a direct connection to your Microsoft 365 tenant.

Important

The two-computer method requires that **the same version of the EDM Upload Agent must be installed on both computers**. You can then copy the hash file and the salt file from the secure machine to a computer that can connect directly to your Microsoft 365 tenant.

1. On the computer in the secure environment, run the following command in a Command Prompt window: `EdmUploadAgent.exe /CreateHash /DataFile [data file] /HashLocation [hash file location] /Schema [Schema file] /AllowedBadLinesPercentage [value]` For example: `EdmUploadAgent.exe /CreateHash /DataFile C:\Edm\Data\PatientRecords.csv /HashLocation C:\Edm\Hash /Schema edm.xml /AllowedBadLinesPercentage 5`

    This command outputs a hashed file and a salt file with these extensions if you didn't specify the `/Salt <saltvalue>` option:

    - EdmHash
    - EdmSalt
2. Securely copy these files to the computer you use to upload your sensitive information source table (for example, **PatientRecords.csv**) to your tenant.
3. Authorize the EDM Upload Agent:

    1. As an admin, open a Command Prompt window.
    2. Switch to the directory where the EDM Upload Agent is installed. (The recommended directory is **C:\EDM\Data**.)
    3. Run the following command:

    `EDM Upload Agent.exe /Authorize`

    Important

    You must run the EDM Upload Agent from the folder where it's installed and you must sindicate the full path to your data files.
4. Sign in with your work or school Microsoft 365 account. (The account that was added to the **EDM\_DataUploaders** security group). Your tenant information is extracted from the user account to make the connection.
5. To upload the hashed data, run the following command in a Command Prompt window:

    `EdmUploadAgent.exe /UploadHash /DataStoreName \<DataStoreName\> /HashFile \<HashedSourceFilePath\ /ColumnSeparator ["{Tab}"|"|"]`

    For example: `EdmUploadAgent.exe /UploadHash /DataStoreName PatientRecords /HashFile C:\\Edm\\Hash\\**PatientRecords.EdmHash**`
6. To verify that the upload of your sensitive data was successful, run the following command in a Command Prompt window:

    `EdmUploadAgent.exe /GetDataStore`

    If the upload was successful, a list of data stores and when they were last updated displays.
7. To display all of the data uploads to a particular store, and when they were updated, run the following command in a Command Prompt window:

    `EdmUploadAgent.exe /GetSession /DataStoreName <DataStoreName>`

Tip

To automate the hash and upload process after you have created it the first time, see [Refresh your exact data match sensitive information source table file](sit-use-exact-data-refresh-data).

# [Single computer method](#tab/single-computer)
1. Authorize the EDM Upload Agent:

    1. As an admin, open a Command Prompt window.
    2. Switch to the directory where the EDM Upload Agent is installed. (The recommended directory is **C:\EDM\Data**.)
    3. Run the following command:

    `EDM Upload Agent.exe /Authorize`
2. Sign in with your work or school Microsoft 365 account. (The account that was added to the **EDM\_DataUploaders** security group.) Your tenant information is extracted from the user account to make the connection.s
3. To hash and upload your sensitive data, run the following command in a Command Prompt window:

    `EdmUploadAgent.exe /UploadData /DataStoreName [DS Name] /DataFile [data file] /HashLocation [hash file location] /Schema [Schema file] /AllowedBadLinesPercentage [value]`

---

### Advanced multi-token configuration options

The following settings control how the EDM Upload Agent handles multi-token values during data upload. Configure these options in the **app.config** file.

Admins can upload upload values that exceed the multi-token limit by truncating the exceeding token to columns.

- **Configuration**: Controlled via **app.config**
- **Default Behavior**: Support is disabled by default

Admins can disable the minimum multi-token optimization feature.

- **Configuration**: Controlled via **app.config**
- **Default Behavior**: Optimization is enabled by default.

### EDM and double-byte character set languages

Exact data match supports double-byte characters, such as those used in Chinese, Japanese, and Korean. However, it doesn't support string matches for corroborative evidence encoded as double byte characters. Neither does it match multi-token CJK text detected in the classified content, unless globalization for EDM is enabled as described later in this document. In all cases, a SIT must be mapped to any multi-token text, both for the primary field and for corroborative evidence fields.

To invoke exact data matching for double-byte characters, take the following steps:

1. Create an EDM Sensitive Information Type (SIT) configured to match on the double-byte character set language, such as Japanese kanji.
2. Ensure that you download and install version 17.01.0495.0 (or later) of the EDM Upload Agent
3. Update the **EdmUploadAgent.exe.config** file’s globalization parameter to true: `<add key=" IsGlobalizationEnabled" value="true">`
4. Hash and upload a source table with the data to be matched.

### EDM Parse Quotes Scenarios

`ParseQuotesExhaustiveScenariosByDefault` is an optional configuration attribute that's available while uploading the data. It is designed to resolve data ingestion errors caused by complex formatting in source files, such as CSVs containing fields with embedded commas, inconsistent single/double quoting, or escaped characters. By default, the value of `ParseQuotesExhaustiveScenariosByDefault is false`. To enable this setting add the ParseQuotesExhaustiveScenariosByDefault="true" in the upload **EdmUploadAgent.exe.config** file.

- Double Quotes ("): If a field starts with a double quote, the parser looks for the matching closing double quote. Commas inside the quotes are treated as text, not separators. For example: Input row (Raw CSV) values are "ID",First Name,"Title, Role" then Parsed values (result) will be: `ID`, `First Name`, `Title, Role`. Double quotes have a higher hierarchy than single quotes. A single quote found inside a double-quoted string is treated as a literal character.
- Single Quotes ('): If a field starts with a single quote, the parser treats it as a delimited string similar to double quotes.
- No Quotes: If the field does not start with a quote, the data is ingested as-is until the next separator is found.