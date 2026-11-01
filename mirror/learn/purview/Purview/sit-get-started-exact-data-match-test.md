---
layout: Conceptual
title: Test an exact data match sensitive information type | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-get-started-exact-data-match-test
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
ms.date: 2026-10-14T00:00:00.0000000Z
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Test an EDM using the test function in the sensitive information types section in the Microsoft Purview Portal.
ms.custom: seo-marvel-apr2020, msecd-doc-authoring-1030
ai-usage: ai-assisted
locale: en-us
document_id: 235849ad-dbcd-7a17-035a-f60e7c1bf002
document_version_independent_id: 235849ad-dbcd-7a17-035a-f60e7c1bf002
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-get-started-exact-data-match-test.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-get-started-exact-data-match-test
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-get-started-exact-data-match-test.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
- https://authoring-docs-microsoft.poolparty.biz/devrel/7e593268-8d01-46ef-aa78-9d1388e6a294
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
- https://authoring-docs-microsoft.poolparty.biz/devrel/264d03ab-bab8-454b-a56c-0fedead7f602
platformId: 07af4240-20fa-9593-bb5c-25e7cc885954
---

# Test an exact data match sensitive information type | Microsoft Learn

This article explains how to test an exact data match (EDM) sensitive information type (SIT) to verify that it correctly detects the sensitive data you want to protect. It covers testing methods available in the Microsoft Purview portal and PowerShell, as well as troubleshooting tips for common detection issues.

## Products and services this EDM testing article applies to

This article covers testing for both EDM experience versions:

For instructions on creating an EDM SIT before testing, see the workflow for your experience:

- [Create an EDM SIT using the new experience](sit-create-edm-sit-unified-ux-workflow)
- [Create an EDM SIT using the classic experience](sit-create-edm-sit-classic-ux-workflow)

## Overview of EDM SIT testing

This section explains how to verify that your exact data match (EDM) sensitive information type (SIT) correctly detects the information you want to protect. After your EDM SIT has been created, and an hour after verifying that your sensitive information table has finished uploading and indexing, you can test detection by using the **Test** function in the **Sensitive information types** section in the Microsoft Purview Portal.

Note

Changes in an existing EDM SIT can take some time to propagate across the system. If you're making changes to an EDM SIT in order to troubleshoot detection issues, make sure to wait at least one hour after making those changes before using the **Test** function to validate their impact.

Regardless of the method you use for testing, the test results include matches for both the specific EDM SIT and for the primary elements that are configured for that EDM SIT.

## Methods for testing your EDM SIT

There are two methods that you can use to test your EDM SIT.

| Method | Available in New EDM experience | Available in New and Classic EDM experience |
| --- | --- | --- |
| Sensitive information type (SIT) method | Yes | Yes |
| EDM classifiers method | Yes | No |

Note

If you're using the Classic EDM experience, you must use the SIT method.

### Testing an EDM SIT with the Sensitive Information Types method

To test an EDM SIT with the **Sensitive Information Types** method, take the following steps.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Information Protection** &gt; **Classifiers** &gt; **Sensitive info types**.
2. Select your EDM SIT from the list and then select the **Test** icon.
3. In the flyout pane, upload a file that contains data you want to detect. For example, create a file that contains a subset of the rows in your sensitive information table. If you used the *configurable match* feature in your schema to define ignored delimiters, make sure the sample file includes examples with and without those delimiters.
4. Choose **Test**.
5. After the file has been uploaded and scanned, check for matches to your EDM SIT.
6. If the **Test** function in the SIT detects a match, verify that the SIT isn't trimming it or extracting the matched item incorrectly. Common issues include SITs that:

    - Extract only a substring of the full string that should be detected
    - Pick up only the first word in a multi-word string
    - Include extra symbols or characters in the extraction

For details about the regular expressions used in SIT pattern definitions and extraction logic, see the [Regular Expression Language - Quick Reference](/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference).

### Test your EDM SIT with the EDM Classifier method

To test an EDM SIT with the **EDM Classifier** method, follow these steps.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Information Protection** &gt; **Classifiers** &gt; **EDM classifiers**.
2. Make sure that the **New EDM experience** toggle is set to **On**.
3. Select your EDM SIT from the list and then select the **Test** icon.
4. Upload a file that contains data you want to detect. For example, create a file that contains a subset of the rows in your sensitive information table. If you used the *configurable* match feature in your schema to define ignored delimiters, make sure your sample file includes examples with and without those delimiters.
5. After the file has been uploaded and scanned, check for matches to your EDM SIT.
6. If the **Test** function in the SIT detects a match, verify that the SIT isn't trimming it or extracting the matched item incorrectly. Common issues include SITs that:

    - Extract only a substring of the full string that should be detected
    - Pick up only the first word in a multi-word string
    - Include extra symbols or characters in the extraction

## Test your EDM SIT using PowerShell

Use the `Test-DataClassification` cmdlet to test your EDM sensitive information type against sample text and verify whether the classifier detects expected matches. For the `-ClassificationNames` parameter, supply the display name of the EDM sensitive information type you want to test. For `-TexttoClassify`, provide the sample text you want to scan for matches.

```powershell
Test-DataClassification  -ClassificationNames “[Your EDM sensitive info type]” -TexttoClassify “[your own text to scan for matches]” 
```

Regardless of the method you use for testing, the test results will include matches for both the specific EDM SIT and for the primary elements that are configured for that EDM SIT.

Note

An uploaded-file or text test doesn't refresh classification for existing SharePoint and OneDrive files. Changing an EDM SIT or its primary SIT doesn't by itself refresh classification for unchanged historical files. To update classification for those files, use [on-demand classification](on-demand-classification). Review the scan scope, EDM scan-cost considerations, and active-policy effects before starting a scan.

## Test your EDM SIT with information protection policies

You can see where your EDM SIT is being used, and how accurate it is in production, by using it in policies:

1. Create an [auto-labeling policy](apply-sensitivity-label-automatically#how-to-configure-auto-labeling-policies-for-sharepoint-onedrive-and-exchange) and run it in **Simulation overview**.
2. Add some content that triggers the EDM SIT, along with content that won't trigger the EDM SIT, to a location that your policy is monitoring.
3. Open the **Items to review** tab to check the matches.
4. Based on the simulation results, tune your policy conditions and EDM SIT settings as appropriate to improve detection accuracy.

Once you're satisfied with the results of your testing and tuning, your EDM-based custom SIT is ready for use in information protection policies, for instance:

- [DLP policies](dlp-create-deploy-policy)
- [Auto-labeling policies](apply-sensitivity-label-automatically#how-to-configure-auto-labeling-for-office-apps)
- [Microsoft Defender for Cloud Apps](/en-us/cloud-app-security/data-protection-policies)

## Troubleshooting tips

If your EDM SIT doesn't detect any matches in your data, the following tips might help you diagnose the problem.

| Issue | Troubleshooting tip |
| --- | --- |
| No matches found | Confirm that your sensitive data was uploaded correctly using the commands explained in [Hash and upload the sensitive information source table for exact data match sensitive information types](sit-get-started-exact-data-match-hash-upload#hash-and-upload-the-sensitive-information-source-table-for-exact-data-match-sensitive-information-types). |
| No matches found | Test the SIT you used when you configured the primary element in each of your patterns. This test verifies whether the SIT can match the examples in the item. Using an incorrectly defined SIT as the classification element of an EDM SIT is the most common cause for detection failures in EDM. |
| The SIT you selected for a primary element in the EDM type doesn't find a match in the item or finds fewer matches than you expected | Confirm that the SIT supports the separators and delimiters that occur in the content. Be sure to include the ignored delimiters defined in your schema. |
| The SIT associated with your primary element finds matches in your content, but the EDM SIT doesn't. | - Check whether your REGEX statements are catching whitespace delimiters at the start or end of an item you want to detect. For instance, look for statements that include the `\s` delimiter. If whitespace delimiters are included, the whitespace won't match the hashed value in the data table. Instead, use a word delimiter, such as `\b`.<br>- Check your REGEX statements to ensure that they capture the entire string you want to detect, not just a substring. For example, consider this pattern for email addresses: `\b[a-zA-Z]{2,30}@[a-zA-Z]{2,20}.[a-zA-Z]{2,3}\b`. This pattern will correctly match *user@contoso.com*, but will only capture *user@contoso.co.jp* in an incomplete form. |
| An EDM SIT with primary elements, but no defined secondary elements, detects items but doesn't detect matches (or detects fewer matches than expected) when both primary and secondary elements are required. | If values in a column used for secondary evidence aren't composed of a single word or of strings that don't contain spaces, commas, or other word separators, there are two ways to test: <br>1. Select the [multi-token matching](sit-learn-about-exact-data-match-based-sits#multi-token-matching) option.<br>2. Associate the values with a SIT that uses either a REGEX designed to detect multi-word strings that follow the desired pattern (for example, a fixed number of consecutive words that start with an uppercase character), or a keyword dictionary that lists all of the unique values in that column. For example, if there's an additional evidence column for a person's city or residence, you can create a list with all the unique city names from the table and then use it to create a dictionary-based sensitive information type.<br><br> Use this SIT as the classification element for the corresponding column in your EDM SIT by exporting and editing the EDM SIT definition in XML. For more information, see [Create a rule package manually](sit-get-started-exact-data-match-create-rule-package#create-a-rule-package-manually). |
| SIT test function doesn't detect any matches at all. | Verify that the SIT you selected includes requirements for additional keywords or other validations. For built-in SITs, see [Sensitive information type entity definitions](sit-sensitive-information-type-entity-definitions#sensitive-information-type-entity-definitions) to determine what the minimum requirements are for matching each type. |
| The **Test** functionality works but your SharePoint or OneDrive items aren't being detected in DLP or auto-labeling rules | Check the policy scope and conditions, and whether classification for the existing files reflects the SIT definitions you intend to use. A direct test doesn't establish classification coverage for stored files. For auto-labeling, see [Auto-labeling classification and simulation concepts](auto-label-classification-simulation); restarting simulation doesn't itself refresh classification. Use [on-demand classification](on-demand-classification) when classification needs updating, after reviewing scope, costs, and active-policy effects. |
| DLP or auto-labeling rules that require multiple matches don't trigger | Make sure that the proximity requirements for both your EDM SIT and the base SITs are met. For example, if the maximum distance between the primary element and supporting keywords is 300 characters, but the keywords are only present in the first row of a long table, only the first few rows of matching values are likely to meet the proximity requirements. Modify your SIT definitions to support more relaxed proximity rules or use the **Anywhere in the document** option for the additional evidence conditions. |
| Detection of an EDM SIT is inconsistent or erratic | Make sure that the SIT you used as the base for the primary element in your EDM SIT isn't detecting unnecessary content. Using a SIT that matches too much unrelated content, such as *any* word, *any* number, or *all* email addresses, can cause the service to ignore relevant matches. Check the number of content pieces that match the sensitive type you used for your primary elements in content explorer.  To estimate whether the SIT is matching too much content: <br>1. Divide the number of content items in the Microsoft Purview Content Explorer by the number of days since the sensitive type was created.<br>2. If the number of matches per day is in the range of hundreds of thousands or more, it's possible that the primary SIT is too broad. |

For recommendations and best practices on selecting the right sensitive information type for an EDM SIT, see [Learn about exact data match based sensitive information types](sit-learn-about-exact-data-match-based-sits#learn-about-exact-data-match-based-sensitive-information-types).