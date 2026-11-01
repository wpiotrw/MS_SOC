---
layout: Conceptual
title: Create an EDM SIT schema and rule package (New experience) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-create-edm-sit-unified-ux-schema-rule-package
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
description: Create an exact data match (EDM) schema and sensitive information type (SIT) rule package in Microsoft Purview by using the new experience unified workflow.
ms.custom: seo-marvel-apr2020, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 4d9f014b-049a-bc67-94e2-13dd67abf141
document_version_independent_id: 4d9f014b-049a-bc67-94e2-13dd67abf141
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-create-edm-sit-unified-ux-schema-rule-package.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-create-edm-sit-unified-ux-schema-rule-package
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-create-edm-sit-unified-ux-schema-rule-package.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: d03d15f4-2a3a-7a4d-ac08-45c62f71d1db
---

# Create an EDM SIT schema and rule package (New experience) | Microsoft Learn

You can create both the exact data match (EDM) schema and EDM sensitive information type (SIT) in the new experience by using a single workflow in the Microsoft Purview Portal.

## Supported experiences

- New experience

If you want to create an EDM SIT using the classic experience, see [Create an EDM SIT (Classic experience)](sit-create-edm-sit-classic-ux-workflow). If you need help deciding whether to use the new experience or the classic experience, see [Choosing the right EDM SIT creation experience for you](sit-get-started-exact-data-match-based-sits-overview#choosing-the-right-edm-sit-creation-experience-for-you).

## Before you begin

Make sure to complete the steps in the following articles before beginning the procedures described in this article.

1. [Export source data for exact data match based sensitive information types](sit-get-started-exact-data-match-export-data)
2. [Create the EDM SIT sample file (New experience)](sit-create-edm-sit-unified-ux-sample-file)

If you aren't familiar with EDM-based SITs or their implementation, ***it's essential*** to familiarize yourself with the concepts in the following articles:

- [Learn about sensitive information types](sit-sensitive-information-type-learn-about#learn-about-sensitive-information-types)
- [Learn about exact data match based sensitive information types](sit-learn-about-exact-data-match-based-sits#learn-about-exact-data-match-based-sensitive-information-types)
- [Learn about multi-token matching](sit-learn-about-exact-data-match-based-sits#multi-token-matching)
- [Get started with exact data match based sensitive information types](sit-get-started-exact-data-match-based-sits-overview)
- [Create an exact data match SIT (New experience)](sit-create-edm-sit-unified-ux-workflow)
- [Sensitive information type entity definitions](sit-sensitive-information-type-entity-definitions)

### Permissions

To create, test, and deploy a custom sensitive information type (which an EDM SIT is) in the Microsoft Purview portal, use an account that is in *one* of these roles:

- Compliance administrator
- Global administrator

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

For more information about roles and permissions, see [About admin roles in Office 365](/en-us/office365/admin/add-users/about-admin-roles).

## Important considerations

Following are several important considerations you should take into account when creating your [EDM schema](sit-learn-about-exact-data-match-based-sits#schema) and EDM-based SITs.

- **Before selecting your primary elements,** review the [built-in SITs](sit-sensitive-information-type-entity-definitions) to get an idea of which ones best meet your needs.
- **For each EDM SIT, you must select at least one primary element** and no more than 10 primary elements. If you have a multi-token corroborative data field, choose one of the following options:

    1. Select **Multi-token matching**.
    2. Map the elements in your multi-token fields to a SIT that can detect that content. (The more fields with unique values that you map, the more accurate your EDM SIT will be. Mapping multiple fields also helps improve performance, reduce the processing load, and avoid system timeouts.)
- When selecting the primary elements for your SIT, **select fields that ensure each row in your data table is unique**. For example, **don't** use fields like `FirstName` or `DateOfBirth`. Why? Because first names and dates of birth are likely to be duplicated throughout your sensitive data table. Instead, use fields with unique values, such as `SocialSecurityNumber` or `BankAccountNumber`.
- **Recommendation:** Build your EDM schema [from a sample data file](sit-create-edm-sit-unified-ux-sample-file#create-an-edm-sit-sample-file-new-experience). If you build your EDM schema from a sample data file, make sure that the file adheres to the following requirements:

    - Data must be organized as a table, with columns and rows. Use your field names for the column headers. (The rows in your table correspond with your individual data items.)
    - Field names can include only alphanumeric characters.
    - Field names must start with a letter and must consist of at least three alphanumeric characters.
    - If these naming requirements are not met, errors may occur when uploading your sample data file.
- If you use a sample file of sensitive information to configure your EDM SIT, the system suggests the existing SIT for each field that best detects the uploaded data, if such a SIT is available. Microsoft Purview defaults to single-token matching for detecting sensitive content. So, if no existing SITs are able to detect the data for a field in your EDM schema, it applies the single-token matching mode. ***It is critical*** that you make sure that the SIT suggested for each element will detect the exact string you want to monitor:

    1. Make sure that the suggested SIT **doesn't contain any surrounding characters that differ from the content you want to detect**.
    2. Make sure that the suggested SIT **doesn't exclude any valid portion of the string as stored in your sensitive information table**.
    3. Make sure that the SIT you use **closely matches the *format*** of the data you want to detect. For example, look for something like `Nine digits with optional hyphens or spaces` rather than simply `digits`, or check for `A combination of 32 characters consisting of letters and digits` rather than simply `text strings`.  Using SITs that closely match the format of the data you're trying to detect is another way to improve the accuracy of your results and shorten the time it takes for the matching to complete.

Note

All of your data is saved as you navigate forward (**Next**) and backward (**Back**) through the tool while making your selections. Backward navigation only supports moving from top-level page to top-level page and from sub-page to sub-page. You can't navigate backward from a top-level page to the preceding sub-page or from a sub-page to a preceding top-level page.

## Create your EDM schema and SIT

The following procedure provides step-by step guidance for creating your EDM schema and SITs using the new experience. For a conceptual overview and diagram of the EDM schema and SIT creation workflow, see [Overview of the EDM workflow (New experience)](sit-create-edm-sit-unified-ux-workflow#overview-of-the-edm-workflow-new-experience).

### Create the EDM schema and sensitive information type

Follow these steps to create an EDM classifier in the Microsoft Purview portal:

1. Open **Data classification** &gt; **EDM classifiers**.
2. Make sure the **New EDM experience** toggle is set to **On**.
3. Choose **+ Create EDM classifier**.
4. Name the SIT and add a description. The system uses this name, appended with the word *schema*, for the associated schema it generates.
5. Choose **Next**.
6. Select the method you want to use for your schema: either **Upload a file containing sample data**, or **Manually define your data structure**. (Best practice is to upload a sample data file. The rest of this procedure assumes that you upload a sample data file.) *In either case,* you need the information discussed in [Create an EDM SIT sample file (New experience)](sit-create-edm-sit-unified-ux-sample-file) for your sample file.
7. Choose **Next**.
8. Select your sample file and then select **Upload file**. Choose **Next**.  (If errors display during the upload, address them and then try again.)
9. On the **Select primary elements** page:

    1. In the **Primary element** column, select your primary element. Each primary element must be mapped to a SIT. Best practice is to select fields that show **Full match** under the **Match Validation** column.
    2. In the **Match mode**column for each field, designate which of the following matching options to apply:
        - **Option 1:** Do nothing to accept the system-suggested SIT.
        - **Option 2:** Expand the dropdown menu. Under **Sensitive Info type (SIT)**, choose the pencil (**Edit**) icon and then select another existing SIT.
        - **Option 3:** Under **Match mode** select **Single token**.
        - **Option 4:** Under **Match mode** select **Multi-token**.
10. Choose **Next**.
11. **Configure settings for data in selected columns**.

    - The toggle **Use the same settings for all columns** is set to **On** by default. If you want to use separate settings for each data field, set the toggle to **Off**.
    - The **Data in columns are case-insensitive** option is selected by default. To enforce **case-sensitive** detection, uncheck this box.
    - If needed, select the option to **Ignore delimiters and punctuation for data in all columns** You can then either select the delimiters and punctuation marks you want to ignore from a list or you can enter custom delimiters and punctuation marks to ignore.

    Important

    If you select the **Ignore Delimiters** option for the primary element column in your schema, make sure that the SIT you map it to is designed to match data both with and without the selected delimiters.
12. **Configure detection rules for primary elements**.

    - Specify the **proximity limit** in terms of the number of characters within which the supporting element should be found in proximity of the primary element. By default, it's set at 300.
    - Select the **proximity detection mode**.
        - **Wide Mode:** Matches the primary element against supporting elements from all primary matches within the defined proximity range. This mode provides a broader context, which can increase the likelihood of detecting relevant associations.
        - **Narrow Mode:** Matches the primary element only against its own supporting element within the proximity range. This mode focuses on tighter, more specific matches, reducing the chance of false positives.
    - Select the **unique counting mode**.
        - **Primary Match-level Counting:** Counts each matching combination of primary and supporting elements separately—even within the same row. Choose this if you want a detailed view of all sensitive matches.
        - **Row-level Counting:** Counts each row only once, even if multiple elements match in it. Use this when you care about how many unique records (rows) are sensitive, not how many elements matched.
    - Define the **detection rules for high, medium, and low confidence levels**. The high confidence rule should include more supporting elements within close proximity of the primary element, whereas a low confidence rule would contain little to no supporting elements in close proximity
13. Choose **Submit**.

 Once you're finished, EDM automatically generates one detection rule for each of the primary elements you identified. EDM also creates a *high-confidence* rule and a *medium-confidence* rule. High-confidence rules have more matching requirements than medium-confidence rules, which, in turn, have more requirements than low-confidence rules. (Low-confidence rules must be created manually.) You can review and edit these rules on the **Configure detection rules for primary elements** page. 

Tip

Those elements that are not selected as primary can still be used as corroborative (supporting) evidence. The more supporting elements found that are in a defined proximity to primary elements, the higher the confidence that the match is a true positive.

## Recommendations

Keep the following recommendations in mind when creating, downloading, and testing your EDM schema and SIT.

- Wait at least one hour after creating or editing a schema before downloading and using it for the EDM data upload. This helps ensure that the schema has synced with the system. If a schema is downloaded too soon, an error message might display when attempting to download the schema via the command line.
- Do not use the EDM Upload Agent to download, manually edit, and then re-upload a schema. Doing so results in an error because using the EDM Upload Agent to download a schema adds tags to the schema that don't pass schema creation checks.
- To help ensure that all corroborative evidence is detected, take one of the following actions: - Trim multi-token corroborative evidence fields to the maximum number of tokens supported by the multi-token feature (currently five tokens). - Map the multi-token field to a SIT that can fully detect the multi-token data. - After creating or editing your EDM SIT, test it using the following PowerShell cmdlet and then wait 24 hours before testing it in a data loss prevention (DLP) policy solution.

```powershell
Test-DataClassification  -ClassificationNames “[Your EDM sensitive info type]” -TexttoClassify “[your own text to scan for matches]” 
```