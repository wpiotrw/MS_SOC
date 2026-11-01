---
layout: Conceptual
title: Export source data for exact data match based sensitive information types | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-get-started-exact-data-match-export-data
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
description: Learn how to prepare and export a sensitive data table in CSV, TSV, or pipe-separated format, choose primary and secondary fields, and save the file so it can be used to create an EDM schema for exact data match based sensitive information types.
ms.custom: seo-marvel-apr2020, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 1f92d0a7-4f2d-f7f9-c10b-1b2bcc9a5270
document_version_independent_id: 1f92d0a7-4f2d-f7f9-c10b-1b2bcc9a5270
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-get-started-exact-data-match-export-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-get-started-exact-data-match-export-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-get-started-exact-data-match-export-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/97159432-14a9-4307-a469-d2f2c75f0e33
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/50565c62-5f6b-4687-be38-323113c72c2e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 37872ba0-f90d-d97a-057c-7687eba70ab3
---

# Export source data for exact data match based sensitive information types | Microsoft Learn

This article explains how to prepare and export your sensitive data table for use with exact data match (EDM) based sensitive information types in Microsoft Purview. You learn how to choose primary and secondary fields, structure your data, and save it in a supported format so you can create an EDM schema.

## Products and services this export procedure applies to

- [New experience](sit-create-edm-sit-unified-ux-workflow)
- [Classic experience](sit-create-edm-sit-classic-ux-workflow)

The sensitive data table is a text file containing rows of values against which you compare the content in your documents to identify sensitive data. These values might be personally identifiable information, product records, or other sensitive data in text form that you want to detect in your content and protect.

Once you export the data in your table (in one of the supported formats), you can create an EDM schema.

## Define your EDM sensitive information type

When you define your EDM sensitive type, one of the most critical decisions is to define which fields are your primary fields. Primary fields need to follow a detectable pattern and be defined as searchable fields (columns) in your EDM schema. Secondary fields don't need to follow any pattern since they'll be compared against all the text surrounding matches to the primary fields.

Use these rules to help you decide which columns you should use as primary fields:

- If you must detect sensitive data based on the presence of a single value matching a field in your sensitive data table, regardless of the presence of any other sensitive data surrounding it, that column must be defined as a primary element for an EDM SIT.
- If multiple combinations of different fields in your sensitive data table must be detected in content, identify the columns that are common to most such combinations and designate them as primary elements. Designate combinations of the other fields as secondary elements.
- If a column you want to use as a primary element doesn't follow a detectable pattern, like `any text string` or follows detectable patterns that would be present somewhere in a large percentage of documents or emails, choose other, better structured, columns as primary elements.

For example, if you have the columns `full name`, `date of birth`, `account number`, and `Social Security Number`, even if the first and last names are the columns that are common to the different combinations of data you want to detect, such strings don’t follow patterns that are easily identifiable and might be difficult to define as a sensitive information type. There are a number of reasons for this:

- some names might not start with an uppercase character
- some might be formed by two, three,or more words/strings
- some might contain numbers or other non-alphabetical characters. Dates of birth can be identified more easily but, since every email and most documents will contain at least one date, a `DateOfBirth` field is also not a good candidate. Instead, use fields such as Social Security numbers and account numbers, which are good candidates for primary fields.

### Sample file templates

To make selecting your primary fields easier, we've put together some sample file templates for:

- [U.S. Healthcare data](https://go.microsoft.com/fwlink/?linkid=2224450)
- [U.S. Financial data](https://go.microsoft.com/fwlink/?linkid=2224770)
- [U.S. Insurance data](https://go.microsoft.com/fwlink/?linkid=2224769)

These are comma separated value (.csv) files that have the most commonly used values across those industry verticals as column headers, along with Microsoft-generated synthetic values in the rows. Use the column headers to help you decide on your primary fields. Best practice is to export only the source data that is required. The column headers suggest the most relevant fields.

To learn how to use the sample file templates, see [How to use the sample file templates](sit-create-edm-sit-unified-ux-sample-file#how-to-use-the-sample-file-templates).

## Save sensitive data in *.csv*, *.tsv*, or *pipe-separated* format

Save your sensitive data as a supported text format by following these steps:

1. Identify the sensitive information you want to use. Export the data to an app such as Microsoft Excel and save the file as a text file. The file can be saved in any of the following formats: *.csv* (comma-separated values), *.tsv* (tab-separated values), or (*|*)(pipe-separated) format. The .tsv format is recommended in cases where your data values might include commas, such as street addresses. The data file can include a maximum of:

    - Up to 100 million rows of sensitive data
    - Up to 32 columns (fields) per data source
    - Up to 10 columns (fields) marked as searchable
2. Structure the sensitive data in the .csv or .tsv file such that the first row includes the names of the fields used for EDM-based classification. In your file you might have field names such as "ssn", "birthdate", "firstname", "lastname". The column header names can't include spaces or underscores. For example, a sample .csv file named *PatientRecords.csv*, and its columns include *PatientID*, *MRN*, *LastName*, *FirstName*, *SSN*, and more.
3. Pay attention to the format of the sensitive data fields; in particular, fields that might contain commas in their content. For example, a street address that contains the value "Seattle, WA" would be parsed as two separate fields if the .csv format is selected. To avoid this, use the .tsv format or surrounded the comma containing values by double quotes in the sensitive data table. If comma containing values also contain spaces, you need to create a custom SIT that matches the corresponding format. For example, a SIT that detects multi-word string with commas and spaces in it.