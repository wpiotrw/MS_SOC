---
layout: Conceptual
title: Create the schema for exact data match based sensitive information types | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-get-started-exact-data-match-create-schema
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
description: Learn how to define and upload an EDM schema with searchable fields, case-insensitive matching, and ignored delimiters for exact data match based sensitive information types in Microsoft Purview.
ms.custom: seo-marvel-apr2020, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 7aade2d2-1f04-e5ad-0d6d-f923b11c3fda
document_version_independent_id: 7aade2d2-1f04-e5ad-0d6d-f923b11c3fda
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-get-started-exact-data-match-create-schema.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-get-started-exact-data-match-create-schema
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-get-started-exact-data-match-create-schema.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: fee2216e-1278-75b3-9f2d-ff438cb75e03
---

# Create the schema for exact data match based sensitive information types | Microsoft Learn

## Applicability for classic EDM schema creation

This procedure applies to the classic exact data match (EDM) sensitive information type (SIT) creation experience.

To simplify schema file creation, you can use the exact data match schema and sensitive information type pattern tool.

If you aren't familiar with EDM-based SITS or their implementation, you should familiarize yourself with:

- [Learn about sensitive information types](sit-sensitive-information-type-learn-about#learn-about-sensitive-information-types)
- [Learn about exact data match based sensitive information types](sit-learn-about-exact-data-match-based-sits#learn-about-exact-data-match-based-sensitive-information-types)
- [Get started with exact data match based sensitive information types](sit-get-started-exact-data-match-based-sits-overview)

A single EDM schema can be used in multiple sensitive information types that use the same sensitive data table. You can create up to 10 different EDM schemas in a Microsoft 365 tenant.

## Use the Exact Data Match Schema and Sensitive Information Type Tool

You can use the exact data match schema and sensitive information type tool to help simplify the schema file creation process.

## Prerequisites

- Perform the steps in [Export source data for exact data match based sensitive information type](sit-get-started-exact-data-match-export-data#export-source-data-for-exact-data-match-based-sensitive-information-types).

## Use the exact data match schema and sensitive information type pattern tool

Perform the following steps to create an EDM schema by using the pattern tool:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Information Protection** &gt; **Classifiers** &gt; **EDM classifiers** &gt; **EDM schemas** (available when the **New EMD experience** is toggled to **Off**).
2. Choose **Create EDM schema** to open the schema tool configuration flyout.

    ![Screenshot of the EDM schema creation wizard configuration flyout showing fields for defining schema name, description, and field settings.](media/edm-schema-wizard-1.png)
3. Fill in an appropriate **Name** and **Description**.
4. Choose **Ignore delimiters and punctuation for all schema fields** if you want to apply the **Ignore...** behavior for the entire schema. For more information about configuring EDM to ignore case or delimiters, see Using the caseInsensitive and ignoredDelimiters fields for more details on this feature.
5. Fill in your desired values for your **Schema field #1** and add more fields as needed. Each schema field must be identical to the column headers in your sensitive information source file.
6. If you want, set the per-field values for the following:

    - **Field is searchable**
    - **Field is case-insensitive**
    - **Choose delimiters and punctuation to ignore for this field**
    - **Enter custom delimiters and punctuation for this field**

    Important

    At least one, but no more than ten, of your schema fields must be designated as searchable.
7. Choose **Save**. Your schema is now listed and available for use.

    Important

    If you want to remove a schema that is already associated with an EDM SIT, you must first delete the EDM SIT. Deleting a schema that has a data store associated with it also deletes the data store within 24 hours.

## Exporting the EDM schema file in XML format

If you created the EDM schema in the EDM schema tool, you must export the schema file in XML format. You'll need the XML file to complete the [Hash and upload the sensitive information source table for exact data match sensitive information types](sit-get-started-exact-data-match-hash-upload#hash-and-upload-the-sensitive-information-source-table-for-exact-data-match-sensitive-information-types) phase.

1. [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).
2. To export the EDM schema to a local XML file so you can review or modify its field definitions, use this syntax:

    ```powershell
    $Schema = Get-DlpEdmSchema -Identity "[your EDM Schema name]"
    Set-Content -Path ".\Schemafile.xml" -Value $Schema.EdmSchemaXML
    ```
3. Save this file for later use.

## Create and upload the exact data match schema file manually

As you create your schema file, your column headers (data fields) must adhere to the following naming requirements:

- Must start with a letter and must consist of at least three alphanumeric characters.
- Must include only alphanumeric characters.

Use the following syntax for each column/data field:

```xml
<Field name="FieldName" searchable="true/false" caseInsensitive="true/false" ignoredDelimiters="delimiter characters" />

```

### Using the caseInsensitive and ignoredDelimiters fields

The following XML schema example uses the `caseInsensitive` and `ignoredDelimiters` fields to show how EDM handles case differences and delimiter characters.

When you include the `caseInsensitive` field set to the value of `true` in your schema definition, EDM won't exclude an item based on case differences. For example, EDM sees the values **FOO-1234** and **fOo-1234** as being identical for the `PatientID` field.

When you include the `ignoredDelimiters` field with supported characters, EDM ignores those characters. So EDM sees the values **FOO-1234** and **FOO#1234** as being identical for the `PatientID` field.

When both `caseInsensitive` and `ignoredDelimiters` are used together, EDM sees **FOO-1234** and **fOo#1234** as identical and classifies the item as a patient record sensitive information type.

Both `caseInsensitive` and `ignoredDelimiters` are used on a per-field basis.

Important

If you configure *spaces* to be ignored, that configuration will only be effective for primary field columns for which a sensitive information type that can detect multi-word strings is defined. Otherwise, the comparison will be made against each individual word in the content being analyzed.

The `ignoredDelimiters` flag supports any nonalphanumeric character, here are some examples:

- -
- /
- \_
- \*
- ^
- #
- [
- ]
- {
- }
- \
- ~

The `ignoredDelimiters` flag doesn't support:

- characters 0-9
- A-Z
- a-z
- "
- ,
- Delimiters used as *Token Separators*

Important

When defining your EDM sensitive information type, `ignoredDelimiters` will not affect how the Classification sensitive information type associated with the primary element in an EDM pattern identifies content in an item. So, if you configure `ignoredDelimiters` for a searchable field, you have to make sure the sensitive information type used for a primary element based on that field will pick strings both with and without those characters present.

The number of columns in your sensitive information source table and the number of fields in your schema must match, order doesn't matter.

The characters that are used as *token separators* behave differently than the other delimiters. Here are some examples:

- \ (space)
- \t
- ,
- .
- ;
- ?
- !
- \r
- \n

When you include a *token separator*, EDM breaks the token where the separator is. For example, EDM sees the value **Middle-Last Name** into **Middle-Last** and **Name** for the `LastName` field. If the `ignoredDelimiters` is included for the `LastName` field with the character '-', that action only happens after the value is broken. In the end, EDM would see the following values **MiddleLast** and **Name**.

To use the following characters as `ignoredDelimiters` and not *token separators*, a SIT that matches the corresponding format needs to be associated with the field. For example, a SIT that detects a multi-word string with dashes in it needs to be associated with the `LastName` field.

- .
- ;
- !
- ?
- \

It's possible to associate sensitive information types (SITs) with secondary elements using PowerShell.

1. Define the schema in XML format (similar to the following example). Name this schema file **edm.xml** and then configure it such that, for each column in the sensitive information source table, there's a line that uses the syntax:

    `\<Field name="" searchable=""/\>`.

    - Use column names for *Field name* values.
    - Use `searchable="true"` for the fields that you want to be searchable and primary fields up to a maximum of five fields. At least one field must be searchable.

    As an example, the following XML file defines the schema for a patient records database, with five fields specified as searchable: `PatientID`, `MRN`, `SSN`, `Phone`, and `DOB`.

    (You can copy, modify, and use our example.)

    ```xml
    <EdmSchema xmlns="http://schemas.microsoft.com/office/2018/edm">
          <DataStore name="PatientRecords" description="Schema for patient records" version="1">
                <Field name="PatientID" searchable="true" caseInsensitive="true" ignoredDelimiters="-,/,*,#,^" />
                <Field name="MRN" searchable="true" />
                <Field name="FirstName" />
                <Field name="LastName" />
                <Field name="SSN" searchable="true" />
                <Field name="Phone" searchable="true" />
                <Field name="DOB" searchable="true" />
                <Field name="Gender" />
                <Field name="Address" />
          </DataStore>
    </EdmSchema>
    ```

    Once you have created the EDM schema file in XML format, you have to upload it to the cloud service.
2. [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).
3. To upload the database schema, run the following command:

    ```powershell
    New-DlpEdmSchema -FileData ([System.IO.File]::ReadAllBytes('.\\edm.xml')) -Confirm:$true
    ```

    You'll be prompted to confirm, as follows:

> 
> **Confirm**
> 
> **Are you sure you want to perform this action?**
> 
> **New EDM Schema for the data store 'patientrecords' will be imported**.
> 
> **[Y] Yes [A] Yes to All [N] No [L] No to All [?] Help (default is "Y"):**

    Tip

    If you want your changes to occur without confirmation, don't use `-Confirm:$true` in Step 3.

Note

It can take between 10-60 minutes to update the EDMSchema with additions. The update must complete before you execute steps that use the additions.