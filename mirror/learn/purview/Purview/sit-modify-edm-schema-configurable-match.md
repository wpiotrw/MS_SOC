---
layout: Conceptual
title: Modify Exact Data Match schema for configurable matching | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-modify-edm-schema-configurable-match
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
description: Learn how to modify an EDM schema to use configurable matching.
ms.custom: seo-marvel-apr2020, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 927d11e5-a60c-fc21-ddd6-95377e0ed98a
document_version_independent_id: 927d11e5-a60c-fc21-ddd6-95377e0ed98a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-modify-edm-schema-configurable-match.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-modify-edm-schema-configurable-match
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-modify-edm-schema-configurable-match.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 0c0b8b21-6666-d8cb-bb55-5392b0395c40
---

# Modify Exact Data Match schema for configurable matching | Microsoft Learn

This article walks administrators through modifying an existing Exact Data Match (EDM) schema to enable configurable matching using PowerShell. By adding the `caseInsensitive` and `ignoredDelimiters` flags to your schema, you can allow Microsoft Purview to match sensitive data while ignoring case differences and specified delimiter characters.

## Applies to: EDM SIT creation with PowerShell

- Exact data match (EDM) sensitive information type (SIT) creation using PowerShell.

Exact Data Match (EDM) based classification enables you to create custom sensitive information types that refer to exact values in a database of sensitive information. When you need to allow for variants of an exact string, you can use *configurable matching* to tell Microsoft Purview to ignore case and some delimiters.

Important

Use this procedure to modify an existing EDM schema and data file to enable configurable matching using PowerShell. You must already have an EDM schema and uploaded data file before you begin.

1. Uninstall the **EdmUploadAgent.exe** from the computer that you use to connect to Microsoft 365 for EDM schema and data file upload purposes
2. Download the appropriate **EdmUploadAgent.exe** file for your subscription using the following links:

    - [Download EDM Upload Agent for Commercial + GCC](https://go.microsoft.com/fwlink/?linkid=2088639) - Most commercial customers should use this option
    - [Download EDM Upload Agent for GCC-High](https://go.microsoft.com/fwlink/?linkid=2137521) - This option is specifically for high-security government cloud subscribers
    - [Download EDM Upload Agent for DoD](https://go.microsoft.com/fwlink/?linkid=2137807) - This option is specifically for United States Department of Defense cloud customers
3. Authorize the EDM Upload Agent so it can perform schema export and data upload operations in your environment. Open a Command Prompt window (as an administrator) and run the following command:

    ```dos
    EdmUploadAgent.exe /Authorize
    ```
4. If you don't have a current copy of the existing schema, you need to download a copy of the existing schema. To do so, run this command:

    ```dos
    EdmUploadAgent.exe /SaveSchema /DataStoreName <dataStoreName> [/OutputDir [Output dir location]]
    ```
5. Customize the schema so each column utilizes `caseInsensitive` and / or `ignoredDelimiters`. The default value for `caseInsensitive` is "false" and for `ignoredDelimiters`, the default is an empty string.

    Note

    The underlying custom sensitive information type or built-in sensitive information type used to detect the general regex pattern must support detection of the input variations listed with ignoredDelimiters. For example, the built-in U.S. Social Security Number (SSN) sensitive information type can detect variations in the data that include dashes, spaces, or lack of spaces between the grouped numbers that make up the SSN. As a result, the only delimiters that are relevant to include in EDM’s `ignoredDelimiters` for SSN data are: dash and space.

    Here's a sample schema that simulates case-insensitive matching by creating the extra columns needed to recognize case variations in the sensitive data.

    ```xml
    <EdmSchema xmlns="http://schemas.microsoft.com/office/2018/edm">
      <DataStore name="PatientRecords" description="Schema for patient records policy" version="1">
               <Field name="PolicyNumber" searchable="true" />
               <Field name="PolicyNumberLowerCase" searchable="true" />
               <Field name="PolicyNumberUpperCase" searchable="true" />
               <Field name="PolicyNumberCapitalLetters" searchable="true" />
      </DataStore>
    </EdmSchema>
    ```

    In the sample schema with `PolicyNumberLowerCase`, `PolicyNumberUpperCase`, and `PolicyNumberCapitalLetters` columns, the variations of the original `PolicyNumber` column aren't necessary if both `caseInsensitive` and `ignoredDelimiters` are added.

    To update this schema so that EDM uses configurable matching, use the `caseInsensitive` and `ignoredDelimiters` flags. Here's how that looks:

    ```xml
    <EdmSchema xmlns="http://schemas.microsoft.com/office/2018/edm">
      <DataStore name="PatientRecords" description="Schema for patient records policy" version="1">
             <Field name="PolicyNumber" searchable="true" caseInsensitive="true" ignoredDelimiters="-,/,*,#,^" />
      </DataStore>
    </EdmSchema>
    ```

    For information on the characters supported by the `ignoredDelimiters` flag, see [Using the caseInsensitive and ignoredDelimiters fields](sit-get-started-exact-data-match-create-schema#using-the-caseinsensitive-and-ignoreddelimiters-fields).
6. [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell)

    Note

    If your organization has set up Customer Key for Microsoft 365 at the tenant level, Exact Data Match will make use of its encryption functionality automatically. This is available only to E5 licensed tenants in the Commercial cloud. For more information, see [Overview of Customer Key](customer-key-overview).
7. Import the updated schema XML back into Microsoft Purview to apply the configurable matching changes to the EDM datastore. Run the following command:

    ```powershell
    Set-DlpEdmSchema -FileData ([System.IO.File]::ReadAllBytes('.\\edm.xml')) -Confirm:$true
    ```
8. If necessary, update the data file to match the new schema version.

    Tip

    Optionally, you can run a validation against your CSV file before uploading it by running:

    `EdmUploadAgent.exe /ValidateData /DataFile [data file] /Schema [schema file]`

    For example: `EdmUploadAgent.exe /ValidateData /DataFile  C:\data\testdelimiters.csv /Schema C:\EDM\patientrecords.xml`

    For more information on all of the parameters supported by EdmUploadAgent.exe, run

    `EdmUploadAgent.exe /?`
9. Open a Command Prompt window (as an administrator) and run the following command to hash and upload your sensitive data:

    ```dos
    EdmUploadAgent.exe /UploadData /DataStoreName [DS Name] /DataFile [data file] /HashLocation [hash file location] /Salt [custom salt] /Schema [Schema file]
    ```