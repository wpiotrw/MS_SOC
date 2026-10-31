---
layout: Conceptual
title: Review credentials examinations in Data Security Investigations | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-security-investigations-credentials
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to examine credentials in data security investigations, identify risks, and refine account management policies to strengthen your organization's security.
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
document_id: fd9a70ad-72cb-62fc-2dce-8924a0ec040d
document_version_independent_id: fd9a70ad-72cb-62fc-2dce-8924a0ec040d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-security-investigations-credentials.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-security-investigations-credentials
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-security-investigations-credentials.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 3748f44d-641e-b727-606a-22cfd5cf39a1
---

# Review credentials examinations in Data Security Investigations | Microsoft Learn

Understanding how credentials and other asset access information associate with a data security incident is an important part of identifying and mitigating risks.

For example, if you discover credentials within impacted data associated with the data security incident, a [Microsoft Entra](/en-us/entra/fundamentals/what-is-entra) admin in your organization can join the investigation, securely view the extracted credentials, and take necessary next steps to reset the accounts. You can also use investigation learnings to refine existing account management policies to strengthen your organization's security practices.

## Analyze data for credentials and asset access information

Complete the following steps to identify credentials and asset access data in items included in the investigation scope:

Important

[Add to scope](data-security-investigations-scope#automatic-vectorization) must complete before you can configure examinations.

1. Go to [Data Security Investigations](https://purview.microsoft.com/dsi) in the Microsoft Purview portal and sign in by using the credentials for a user account assigned [Data Security Investigations permissions](data-security-investigations-permissions).
2. Select **Investigations** in the left navigation.
3. Select an investigation, then select **Analysis** on the navigation bar.
4. Use vector search or categorization tools to identify data for credentials examination.
5. Select one or more items, then select **Examine** on the command bar.
6. In the **Examine** dialog, enter a name for your examination process in the **Name** field.
7. Enter a description for the examination process in the **Description** field.
8. Select *Credentials: Extract the credentials and access assets in selected evidence* in the **Choose a focus area** field.
9. Select **Examine** to start the AI analysis.

Note

The time estimates for the process to complete is based on the amount and size of the selected data. To reduce processing time, filter and exclude data not applicable to the investigation.

## Credentials examinations

After the AI processing completes for the selected data items, you can review credentials examinations to identify credential and asset access details for each item.

The credentials examinations include the following information for each item:

- **Subject/Title**: The subject or title of the data item.
- **Extracted credentials**: The credential details included in the data item. This information includes user names, passwords, and more.
- **Credential type**: The credential type. Might include user credentials, API tokens, MFA backup codes, and more.
- **Surrounding snippet**: The text or string values surrounding the credential details. This information helps with determining the context in which the credential is used in the data item.
- **Thought process**: A summary of the reasoning as to why the credentials associated with the item are important.
- **Errors**: A summary of any processing errors encountered when the AI process runs.

## Credentials examination example

The output of the examination might be a summary or annotation for each identified item. The examination highlights sentences or pieces of data in the content that are likely sensitive.

For example, the examination might return *In File X, the AI found what looks like 10 user passwords and 5 API keys* in a document. Or for an email, *Email Y contains a conversation about sharing database credentials*. This summary saves you from manually reading every line for each item and helps you triage risky content very quickly. Here’s an example of a deep examination output for an item with Credential Risk:

| File | String | Type | Extracted Value | Analysis |
| --- | --- | --- | --- | --- |
| EV-1.docx | T9!vX3p@7qLz | LoosePassword | T9!vX3p@7qLz | The string matches a typical password pattern, featuring uppercase, lowercase, numbers, and special characters. There are no other indicators, so it's classified as a `LoosePassword`. |

An item with cleartext passwords might be tagged as `Critical risk: Credentials exposed` by the system. These examinations are important and they align with what a human analyst would consider severe and they also include explanations.

You should also take the following actions:

- **Manually verify critical details**: While the examination process does the heavy lifting, you should manually verify the most critical pieces. If a specific password is identified in a document, open the document to confirm the context. You should verify that it's an actual active password, and whose password it is. For instance, the string `P@ssw0rd123` might be identified and it's labeled as a password. But by opening the file, you verify it’s in a table titled *VPN Credentials* and not in the content only as an example placeholder. This confirms it’s actionable and gives you the information needed to act.
- **Expand the scope**: Sometimes examinations reveal new clues that require pulling in more data. For example, you discover references to a project name or a user account you didn’t search for initially. You should consider another search for the project or user account to see if there are related items. A vector search for the project name might find related files that didn’t explicitly mention passwords, but are related to the security incident.