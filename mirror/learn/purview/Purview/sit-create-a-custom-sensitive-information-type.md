---
layout: Conceptual
title: Create custom sensitive information types | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-create-a-custom-sensitive-information-type
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
ms.date: 2026-06-22T00:00:00.0000000Z
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Learn how to create, and modify custom sensitive information types in the Microsoft Purview portal.
ms.custom: seo-marvel-apr2020, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: aee8b417-1106-4482-d56e-776d054112f5
document_version_independent_id: aee8b417-1106-4482-d56e-776d054112f5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-create-a-custom-sensitive-information-type.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-create-a-custom-sensitive-information-type
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-create-a-custom-sensitive-information-type.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: e0322bdb-9d14-e78d-ca6d-b8cf1d33d027
---

# Create custom sensitive information types | Microsoft Learn

If the preconfigured sensitive information types (SITs) don't meet your needs, you can create and define customized SITs that meet your needs. You can also copy and then edit a built-in SIT.

The custom SITs are added to the `Microsoft.SCCManaged.CustomRulePack` rule package.

There are two methods for creating a new SIT:

- Create a new SIT from scratch
- Copy and modify an existing SIT

## Before you begin

- You should be familiar with sensitive information types and what they're composed of. To get this understanding, see, [Learn about sensitive information types](sit-sensitive-information-type-learn-about). It's critical to understand the roles of:

    - [regular expressions](https://www.boost.org/doc/libs/1_68_0/libs/regex/doc/html/) - Microsoft 365 sensitive information types uses the Boost.RegEx 5.1.3 engine
    - keyword lists - you can create your own as you define your sensitive information type or choose from existing keyword lists
    - [keyword dictionary](sit-create-a-keyword-dictionary)
    - [Sensitive information type functions](sit-functions)
    - [confidence levels](sit-sensitive-information-type-learn-about#more-on-confidence-levels)
- Familiarize yourself with [Sensitive information type limits](sit-limits).

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

Important

Microsoft Customer Service & Support can't assist with creating custom classifications or regular expression patterns. Support engineers can provide limited support for the feature, such as, providing sample regular expression patterns for simulation purposes, or helping to troubleshoot an existing regular expression pattern that's not triggering as expected. However, they can't provide assurances that any custom content-matching development fulfills your requirements or obligations.

### Create a custom SIT from scratch

Note

Microsoft Purview supports creating custom SITs that use double-byte character languages, such as Chinese, Japanese, and Korean. Because these languages don't use delimiters the way that single-byte languages do, Purview adds a space between each word in languages that use double-byte characters. It also removes special characters, such as punctuation.

Use the following procedure to fully define a brand new sensitive information type.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. In the Microsoft Purview portal, navigate to **Information Protection** &gt; **Classifiers** &gt; **Sensitive info types** and choose **Create sensitive info type**.
3. Fill in values for **Name** and **Description** and choose **Next**.
4. Choose **Create pattern**. You can create multiple patterns, each with different elements and confidence levels, as you define your new sensitive information type.
5. Choose the default confidence level for the pattern. The values are **Low confidence**, **Medium confidence**, and **High confidence**.
6. Choose and define the **Primary element**. The primary element can be a **Regular expression** with an optional validator, a **Keyword list**, a **Keyword dictionary**, or one of the preconfigured **Functions**. For more information on the SIT functions used for data loss prevention, see [Sensitive information type functions](sit-functions). For more information on the date and the checksum validators, see [Sensitive Information Type regular expression validators](sit-regex-validators-additional-checks#sensitive-information-type-regular-expression-validators).

    Important

    Custom SIT regex patterns must follow these rules:

    - **Don't use positional anchors** like `^` and `$`. When content is scanned, there are no guarantees about where in the content the starting and ending anchors correspond to.
    - Use **one primary capturing group** (the only capturing group), for example: `(?:prefix)(primary capturing group)(?:suffix)` (use noncapturing groups for any additional grouping).
    - Handle all match variants **inside** that single group using `|` (alternation). Multiple capturing groups separated by `|` at the top level are **not supported** and are blocked during validation.

    **Invalid pattern** (three top-level capturing groups):

    `(?:[\s,;])([A-Z]{2}[0-9]{3})(?:[\s,;])|(?:[\s,;])([A-Z]{2}[A-Z]{4}[0-9])(?:[\s,;])|(?:[\s,;])([A-Z]{2}[0-9]{5})(?:[\s,;])`

    **Valid pattern** (single capturing group with alternation):

    `(?:[\s,;])([A-Z]{2}[0-9]{3}|[A-Z]{2}[A-Z]{4}[0-9]|[A-Z]{2}[0-9]{5})(?:[\s,;])`

    For more information on limits, see [Sensitive information type limits](sit-limits).
7. Fill in a value for **Character proximity**.
8. (Optional) Add supporting elements if you have any. Supporting elements can be a regular expression with an optional validator, a keyword list, a keyword dictionary or one of the predefined functions. Supporting elements can have their own **Character proximity** configuration.
9. (Optional) Add any [**sensitive information type additional checks**](sit-regex-validators-additional-checks#sensitive-information-type-additional-checks) from the list of available checks.
10. Choose **Create**.
11. Choose **Next**.
12. Choose the **recommended confidence level** for this sensitive information type.
13. Check your settings and choose **Save**.

    Important

    Microsoft 365 uses the search crawler to identify and classify sensitive information in SharePoint and OneDrive sites. To identify your new custom sensitive information type in existing content, the content must be recrawled. Content is crawled based on a schedule, but you can manually recrawl content for a site collection, list, or library. For more information, see [Manually request crawling and reindexing of a site, a library, or a list](/en-us/sharepoint/crawl-site-content).
14. The **Sensitive info types** tab of the **Classifiers** page, lists all of the sensitive information types. Choose **Refresh** and then or use the search tool or browse the list to find your new SIT.

### Copy and modify an existing SIT

This procedure explains how to copy and modify an existing SIT using the Purview Portal.

Alternatively, you can copy and modify custom SITs using PowerShell and using Purview's Exact Data Match (EDM) capabilities. To learn more about those methods, see:

- [Create a custom sensitive information type in Microsoft Purview PowerShell](sit-create-a-custom-sensitive-information-type-in-scc-powershell)
- [Learn about exact data match based sensitive information types](sit-learn-about-exact-data-match-based-sits#learn-about-exact-data-match-based-sensitive-information-types)

Note

These SITs can't be copied:

- Canada driver's license number
- EU driver's license number
- EU national identification number
- EU passport number
- EU social security number or equivalent identification
- EU tax identification number
- International classification of diseases (ICD-10-CM)
- International classification of diseases (ICD-9-CM)
- U.S. driver's license number

When you have 10 text processors or restricted text processors, such as keyword lists, regex, keyword dictionaries, or functions, you won't be able to copy the SIT from the UI directly. Instead, you need to use PowerShell for this task. To learn more about how to clone or copy your SIT using PowerShell, see [Modify a custom sensitive information type using PowerShell](sit-modify-a-custom-sensitive-information-type-in-powershell)

#### Copy and modify an existing SIT using the Microsoft Purview portal

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. **Information Protection** &gt; **Classifiers** &gt; **Sensitive info types** and select the sensitive information type that you want to copy.
3. The overview page for the sensitive information type opens. Choose **Copy**. When the copy is ready, a message stating that the copy was created appears with an option to edit it. Choose **Yes**.
4. Give your new sensitive information type a new **Name** and **Description**.
5. You can choose to create a new pattern, or edit or remove some or all of the existing patterns.

    1. To create a new pattern, choose **Create**.
    2. To edit an existing pattern, choose the **Edit** (pencil) icon next to the pattern you want to change.
    3. To remove a pattern, choose the **Delete** icon next to the pattern you want to remove.
6. When creating or editing a pattern, choose the default confidence level for the pattern. The values are **Low confidence**, **Medium confidence**, and **High confidence**.
7. Choose and define **Primary element**. The primary element can be a **Regular expression**, a **Keyword list**, a **Keyword dictionary**, or one of the preconfigured **Functions**. See, [Sensitive information type functions](sit-functions).
8. Fill in a value for **Character proximity**.
9. (Optional) If you have **Supporting elements** or any [sensitive information type additional checks](sit-regex-validators-additional-checks#sensitive-information-type-additional-checks) you want to run, add them. If needed, you can organize your **Supporting elements** into groups.
10. If you're creating a new pattern, choose **Create**. If you're editing an existing pattern, choose **Update**.
11. Choose **Next**.
12. Confirm the confidence level selection for this sensitive information type and then choose **Next**.
13. Review your settings and then choose **Save**.
14. Your new sensitive information type is created. At the confirmation message, choose \**Done*

Note

Microsoft Purview Information Protection supports double byte character set languages for:

- Chinese (simplified)
- Chinese (traditional)
- Korean
- Japanese

This support is available for sensitive information types. For more information, see [Information protection support for double byte character sets release notes (preview)](mip-dbcs-relnotes).

Tip

To detect patterns containing Chinese/Japanese characters and single byte characters, or to detect patterns containing Chinese/Japanese and English, define two variants of the keyword or regex.

- For example, to detect a keyword like "机密的document", use two variants of the keyword; one with a space between the Japanese and English text and another without a space between the Japanese and English text. So, the keywords to be added in the SIT should be "机密的 document" and "机密的document". Similarly, to detect a phrase "東京オリンピック2020", two variants should be used; "東京オリンピック 2020" and "東京オリンピック2020".

Along with Chinese/Japanese/double byte characters, if the list of keywords/phrases also contain non Chinese/Japanese words also (for instance, English only), creating two dictionaries/keyword lists is recommended. Create one for keywords containing Chinese/Japanese/double byte characters and another for English-only.

- For example, if you want to create a keyword dictionary/list with three phrases "Highly confidential", "機密性が高い", and "机密的document", you should create two keyword lists.
    1. Highly confidential
    2. 機密性が高い, 机密的document and 机密的 document

While creating a regex using a double byte hyphen or a double byte period, make sure to escape both the characters in the same way that you would escape a hyphen or period in a regex. Here's a sample regex for reference:

`(?<!\d)([4][0-9]{3}[\-?\-\t]*[0-9]{4})`

Double-byte special characters shouldn't be used in the keyword.

We recommend using a string match instead of a word match in a keyword list.