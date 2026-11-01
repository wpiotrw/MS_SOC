---
layout: Conceptual
title: Create EDM SIT sample file (New experience) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-create-edm-sit-unified-ux-sample-file
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
description: Learn how to create the sample file to use in the new exact data match experience.
ms.custom: seo-marvel-apr2020, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: c80a52d7-bb14-20a6-ebb0-2c9a25e5aa24
document_version_independent_id: c80a52d7-bb14-20a6-ebb0-2c9a25e5aa24
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-create-edm-sit-unified-ux-sample-file.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-create-edm-sit-unified-ux-sample-file
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-create-edm-sit-unified-ux-sample-file.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 102bc33f-9ccf-c0c5-0461-c9540cc4144d
---

# Create EDM SIT sample file (New experience) | Microsoft Learn

Creating and making an exact data match (EDM) based sensitive information type (SIT) available is a multi-phase process. EDM-based SITs can be used in Microsoft Purview data loss prevention policies, eDiscovery, and certain content governance tasks.

## Applies to: EDM SIT new experience

- New experience

If you want to create an EDM SIT using the classic experience see, [Create EDM SIT classic experience](sit-create-edm-sit-classic-ux-workflow).

## Before you begin

Before you create the sample file, complete the following prerequisite:

- Make sure you've complete the steps in [Export source data for exact data match based sensitive information type](sit-get-started-exact-data-match-export-data).

## Formatting the sample file

The system will extract the column names from the sample file to create the schema, and will recommend base SITs to map the sample field data to. The sample file must be formatted identically to your source sensitive information table file and should contain synthetic values that are representative of your actual data. The file can be saved in **.csv** (comma-separated values), **.tsv** (tab-separated values), or pipe-separated (**|**) format, but should be the same as your actual source sensitive information table file. The **.tsv** format is recommended in cases where your data values include commas, such as street addresses.

- Use about 10-20 rows of data to ensure that the system has enough samples to work with.
- Field values that contain commas must be enclosed in quotes *"*.
- The first row must be the header row and contain column names.
- The file must contain at least one row of data.
- Each row of data must contain the correct number of fields, corresponding to the headers.
- The sample file can contain up to 32 columns.
- The sample file can't exceed 2.5 MB in size.
- Column (field) names must start with a letter, be at least three characters long, and consist of only alphanumeric characters (A-Z, a-z, 0-9) and can’t include spaces, underscores, or other special characters.

For example, if your actual data uses tab delimited (**.tsv**) format and looks like this:

![Screenshot of a tab-separated values file containing sample data with four columns and three rows.](media/sit-edm-tsv-actual-file.png)

Then your sample file must have the same column headers, but use synthetic values for the rows, like this

| FirstName | LastName | PatientNumber | CreditCardNumber |
| --- | --- | --- | --- |
| Eric | Solomon | 987-65-4321 | 9000000000000000 |
| Lisa | Taylor | 123-45-6789 | 500000000000000 |
| Andre | Lawson | 234-56-7890 | 200000000000000 |

### How to use the sample file templates

If you're in the U.S. Healthcare, U.S. Financial Services, or U.S. Insurance industry verticals, you can start with the following sample file templates to speed up the sample file creation process. These files contain the most commonly used column headers across the respective industries as a well as synthetic values in the fields.

- [U.S. Healthcare data](https://go.microsoft.com/fwlink/?linkid=2224450)
- [U.S. Financial data](https://go.microsoft.com/fwlink/?linkid=2224770)
- [U.S. Insurance data](https://go.microsoft.com/fwlink/?linkid=2224769)

To use these templates:

1. Download the sample file template for your industry.
2. Compare the column headers in the template to your actual source data and pick the ones you want to use as primary fields in your customized sample file.
3. Compare the formatting of your actual source data with the formatting of the synthetic values. Change the formatting of the synthetic values to match the formatting of your source data values.
4. Save your customized sample file to use when you [create EDM SIT schema and rule package](sit-create-edm-sit-unified-ux-schema-rule-package).

Tip

When working in the new experience, you have the option to upload a sample file or enter the sample file values manually. We recommend creating the sample file.