---
layout: Conceptual
title: Review personal data examinations in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-personal-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to examine personal data in data security investigations, identify personally identifiable information (PII) exposure, assess risk levels, and support regulatory compliance obligations.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-11T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-data-security-investigations
ms.collection:
- purview-compliance
- data-security-investigations
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: dc4939d0-dab9-1748-1cbf-f5ba31d640d0
document_version_independent_id: dc4939d0-dab9-1748-1cbf-f5ba31d640d0
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-personal-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-personal-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-personal-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 44a3c311-b511-51cb-116c-ba05b788053f
---

# Review personal data examinations in Data Security Investigations | Microsoft Learn

Understanding what personal data is present in data associated with a security incident is a critical part of investigating and responding to data breaches. After a data security incident, one of the most time-consuming and high-stakes tasks for investigators is determining which personal data elements were exposed and whether regulatory notification obligations exist under frameworks such as the General Data Protection Regulation (GDPR), the Health Insurance Portability and Accountability Act (HIPAA), or state-level privacy laws.

For example, if you discover personal data within impacted data associated with a data security incident, you can quickly assess potential privacy exposure, support compliance reporting, and build defensible evidence chains from detection to action. You can also use investigation learnings to inform regulatory notification decisions and strengthen your organization's data protection practices.

Personal data examinations support common investigation scenarios, including:

- **Data breach privacy impact assessment**: Run personal data examinations on impacted files to quickly determine which personal data types were exposed and which individuals might be affected.
- **Regulatory compliance evidence**: Generate structured, auditable results showing what personal data was found, in which files, at what risk level, with AI-generated reasoning to support breach notification reporting.
- **Insider risk investigation**: Identify the types and risk levels of personal data present in data associated with risky user activities, helping prioritize which files require immediate attention and remediation.
- **Cross-functional incident response**: Provide security, legal, and privacy teams with a shared, actionable summary of personal data exposure that all teams can reference during incident response.
- **Post-incident audit**: Conduct a systematic review of past incidents to ensure personal data exposure was accounted for, validating or supplementing earlier manual review efforts.

## Analyze data for personal data

Complete the following steps to identify personal data in items included in the investigation scope:

Important

[Add to scope](data-security-investigations-scope#automatic-vectorization) must complete before you can configure examinations.

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in by using the credentials for a user account assigned [Data Security Investigations permissions](data-security-investigations-permissions).
2. Select **Investigations** in the left navigation.
3. Select an investigation, and then select **Analysis** on the navigation bar.
4. Use vector search or categorization tools to identify data for personal data examination.
5. Select one or more items, and then select **Examine** on the command bar.
6. In the **Examine** dialog, enter a name for your examination process in the **Name** field.
7. Enter a description for the examination process in the **Description** field.
8. Select *Personal data: Identify and extract the personally identifiable information in selected evidence* in the **Choose a focus area** field.
9. Select **Examine** to start the AI analysis.

Note

The time estimates for the process to complete are based on the amount and size of the selected data. To reduce processing time, filter and exclude data that aren't applicable to the investigation.

## Personal data examinations

After the AI finishes processing the selected data items, you can review the personal data examinations to identify personal data details for each item.

The personal data examinations include the following information for each item:

- **Subject/Title**: The subject or title of the data item.
- **Risk level**: The risk levels for all personal data found in the item. Values include *High*, *Medium*, and *Low*.
- **Contains Personal Data**: Indication if the data item contains personal data. Values are *Yes* or *No*.
- **Type of Personal Data**: A list of personal data types found in the data item. For more information, see Personal data types and risk level classification.
- **Personal Data Found**: A list of extracted personal data values from the data item.
- **Surrounding Snippet**: The text or string values surrounding the personal data details. This information helps with determining the context in which the personal data appears in the data item.
- **Thought Process**: A summary of the reasoning as to why the personal data associated with the item was classified and its risk level rationale.
- **Errors**: A summary of any processing errors encountered when the AI process runs.

### Personal data types and risk level classification

Each personal data finding is assigned a risk level based on the type of personal data identified. The risk level helps you prioritize which findings require immediate attention and remediation. The following table includes examples of personal data types for each risk level. These examples aren't a comprehensive list of all personal data types detected by the examination.

| Risk level | Example personal data types | Description |
| --- | --- | --- |
| **High** | SSN/National ID, bank account numbers, financial account numbers, routing numbers | Financial identifiers and government-issued identification numbers that pose the highest risk if exposed. |
| **Medium** | Email addresses, phone numbers, dates of birth, medical record numbers, insurance IDs | Contact information that can be used to identify or reach individuals. |
| **Low** | Full names, addresses, device identifiers | General identifying information that presents lower risk when exposed individually. |

Note

A single data item might contain multiple personal data instances of different types and risk levels. The process captures and reports personal data instances individually.

## Personal data examination example

The output of the examination might be a summary or annotation for each identified item. The examination highlights personal data elements in the content that are likely sensitive.

For example, the examination might return *In File X, what looks like 3 Social Security numbers and 5 email addresses were found* in a document. Or for an email, *Email Y contains a conversation where bank account details were shared*. This summary saves you from manually reading every line for each item and helps you triage risky content very quickly. Here's an example of a personal data examination output for an item:

| File | String | Type | Risk level | Analysis |
| --- | --- | --- | --- | --- |
| EV-2.docx | 555-12-3456 | SSN/National ID | High | The string matches a Social Security number pattern (XXX-XX-XXXX) found in a table titled *User Records*. It's associated with a full name in the adjacent column, confirming it as identifiable PII. |
| EV-3.msg | user1@contoso.com | EmailAddress | Medium | The email address appears in the body of the message as a recipient of shared financial documents, making it contextually relevant to the investigation. |

Take the following actions:

- **Manually verify critical details**: While the examination process does the heavy lifting, manually verify the most critical pieces. If the process identifies a specific personal data value in a document, open the document to confirm the context. For instance, the process might identify a Social Security number in a file, but by opening the file, you verify it's in a table titled *User Records* and not only in the content as an example placeholder. This verification confirms the finding is actionable and gives you the information needed to act.
- **Expand the scope**: Sometimes examinations reveal new clues that require pulling in more data. For example, you discover references to a user account or a department you didn't search for initially. Consider another search for the user account or department to see if there are related items. A vector search for the department name might find related files that didn't explicitly mention personal data but are related to the security incident.
- **Connect findings to the mitigation plan**: After reviewing personal data examination results, add specific data items to the [mitigation plan](data-security-investigations-mitigation-actions) to manage and track the mitigation status for each item. This approach creates an auditable chain from detection to remediation.
- **Consider regulatory implications**: Personal data exposure might trigger notification obligations under privacy regulations. Use the structured examination results, including risk levels, personal data types, and AI-generated reasoning, to support compliance reporting and regulatory notification decisions.