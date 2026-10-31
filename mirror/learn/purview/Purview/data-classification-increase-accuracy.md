---
layout: Conceptual
title: Increase Classifier Accuracy | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-classification-increase-accuracy
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: purview
ms.collection:
- purview-compliance
search.appverid:
- MET150
description: Review classifier matches, mark items as Match or Not a match, and submit feedback to tune sensitive information types and trainable classifiers.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: c6b3446f-fefa-09e0-fbed-4ea207e3e1b6
document_version_independent_id: c6b3446f-fefa-09e0-fbed-4ea207e3e1b6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-classification-increase-accuracy.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-classification-increase-accuracy
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-classification-increase-accuracy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: f216e9cb-d2a9-32da-17a2-785efa0d2462
---

# Increase Classifier Accuracy | Microsoft Learn

Classifiers, such as [sensitive information types](sit-sensitive-information-type-learn-about) (SIT) and [trainable classifiers](trainable-classifiers-learn-about), are used in various types of policies to identify sensitive information. Like most such models, sometimes they identify an item as being sensitive that isn't. Or, they may not identify an item as being sensitive when it actually is. These are called false positives and false negatives.

This article shows you how to confirm whether items matched by a classifier are true positives (a **Match**) or false positives (**Not a match**) and provide **Match**/**Not a match** feedback. You can use that feedback to tune your classifiers to increase accuracy. You can also send redacted versions of the document as well as the **Match**, **Not a Match** feedback to Microsoft if you want to help increase the accuracy of the classifiers that Microsoft provides.

The **Match**, **Not a match** and **Contextual Summary** experiences are available in:

- Data Explorer - for SharePoint sites, OneDrive sites
- Content Explorer - for SharePoint sites, OneDrive sites
- Sensitive Information Type Matched Items page - for SharePoint sites, OneDrive sites
- Trainable Classifier Matched Items page - for SharePoint sites, OneDrive sites
- Microsoft Purview Data Loss Prevention (DLP) Alerts page - for SharePoint sites, OneDrive, and emails in Exchange
- Microsoft Threat Protection (MTP) Alerts page - for SharePoint sites, OneDrive sites, and emails in Exchange

The standalone **Contextual Summary** capability is also available in the following location:

- Microsoft Purview Information Protection (MIP) Auto-labeling simulation matched items - for SharePoint sites, OneDrive sites

## Supported classifiers and feedback capabilities

| Classifier | Contextual summary | Redacted preview panel | Match and Not a Match |
| --- | --- | --- | --- |
| SIT | Yes | Yes | Yes |
| Custom SIT | Yes | No | Yes |
| Fingerprint SIT | No | No | Yes |
| Exact data match SIT | No\* | No | No |
| Named entities | No\* | No | No |
| Credential scan | No | No | No |
| Built-in Trainable classifiers | Yes \*\* | Yes | Yes |
| Custom trainable classifier | No | No | Yes |

\* These classifiers are supported in MIP Auto-labeling simulation matched items - for SharePoint sites and OneDrive sites.

\*\* List of [Built-in Trainable classifiers](trainable-classifiers-definitions) and which support contextual summary.

Important

The match/not a match feedback and contextual summary experience support items in: SharePoint sites & OneDrive sites - for Content Explorer, Sensitive Information Type and Trainable Classifier Matched Items, DLP Alerts and MTP Alerts. Emails in Exchange - for DLP Alerts and MTP Alerts. The contextual summary experience supports items in: SharePoint sites and OneDrive sites - for MIP simulation matched items

## Licensing requirements for classifier accuracy tuning

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

## Known limitations

The following limitations apply to the contextual summary and feedback experience:

- The contextual summary only shows a limited number of matches in any given item, not all matches.
- The contextual summary and feedback experience is only available for items created or updated after the feedback experience was enabled for the tenant. Items that were classified before the feature was enabled may not have the contextual summary and feedback experience available.

## How to evaluate match accuracy and provide feedback

The contextual summary experience, where you indicate whether a matched item is a true positive (**Match**) or a false positive (**Not a match**), is similar in Content Explorer, Sensitive Information Type Matched Items, Trainable Classifier Matched Items, DLP Alerts, and MTP Alerts.

Important

You must have already deployed DLP policies that use either SITs or trainable classifiers to OneDrive sites, SharePoint sites, or Exchange mailboxes. You must also have had items match before any items appear in the **Contextual summary** page.

### Using Content Explorer

This example shows you how to use the **Contextual Summary** tab to give feedback.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Data Lifecycle Management** &gt; **Explorers** &gt; **Content explorer**.
2. Type the name of the SIT or trainable classifier that you want to check matches for in **Filter on labels, info types, or categories**.
3. Select the SIT.
4. Select the location and make sure that there's a non-zero value in the **Files** column. (The only supported locations are SharePoint and OneDrive.)
5. Open the folder and then select a document.
6. Select the link in the **Sensitive info type** column for the document to see which SITs the item matched and the [confidence level](sit-sensitive-information-type-learn-about#more-on-confidence-levels).
7. Choose **Close**
8. Open a document and select the **Contextual Summary** tab.
9. Review the item and confirm whether or not it's a match.
10. If it's a match, choose **Close**. You're finished.
11. If it's not a match, choose **Not a match**.
12. If you make a mistake and chose the wrong option, select **Withdraw feedback** next to **Close**. This puts the item back into the **Not a match**/**Match** state.
13. Review the item and redact or un-redact any text.
14. Choose **Close**.

### Using the Sensitive Information Type Matched Items page

You can access the same **Match**, **Not a match**, and **Contextual Summary** feedback options on the **Sensitive Info types** page.

1.[Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Data Lifecycle Management** &gt; **Classifiers** &gt; **Sensitive info types**.

1. In the **Search** field, enter the name of the SIT whose accuracy you want to check.
2. Open the SIT. This brings up **Overview** tab. Here you can see the count of the number of items that match, a count of the number of items that aren't a match, and the number of items with feedback.
3. Select the **Matched items** tab.
4. Open the folder and select a document. Only SharePoint, OneDrive are supported locations here. Make sure that there's a non-zero value in the **Files** column.
5. Select the link in the **Sensitive info type** column for an item to see which SITs the item matched and the [confidence level](sit-sensitive-information-type-learn-about#more-on-confidence-levels).
6. Choose **Close**.
7. Open a document and then select the **Contextual Summary** tab.
8. Review the item and confirm whether it's a match.
9. If it's a match, choose **Match** and then **Close**.
10. If it isn't a match, choose **Not a Match**.
11. If you make a mistake and select the wrong option, select **Withdraw feedback** next to **Close**. This puts the item back into the **Not a match**/**Match** state.
12. Choose **Close**.

### Using the Trainable Classifier Matched Items page

Use the Trainable Classifier Matched Items page to review matches and provide feedback:

1.[Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Data Lifecycle Management** &gt; **Classifiers** &gt; **Trainable classifiers**.

1. Select the trainable classifier whose accuracy you want to check.
2. Open the trainable classifier. This brings up **Overview** tab. Here you can see the count of the number of items that match, a count of the number of items that aren't a match, and the number of items with feedback.
3. Select the **Matched items** tab.
4. Open the folder and open a document. Only SharePoint, OneDrive are supported locations here. Make sure that there's a non-zero value in the **Files** column.
5. Open a document and then select the **Contextual Summary** tab.
6. Review the item and confirm whether it's a match.
7. If it's a match, choose **Match** and then choose **Close**.
8. If it isn't a match, choose **Not a Match**.
9. If you make a mistake and select the wrong option, choose **Withdraw feedback** next to **Close**. This puts the item back into the **Not a match**/**Match** state.
10. Choose **Close**.

### Using the Data Loss Prevention Alerts page

Use a DLP alert to review the matched item and submit feedback:

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Data loss prevention** &gt; **Alerts**.
2. Choose an alert.
3. Choose **View details**.
4. Choose the **Events** tab.
5. Maximize the **Details** tab.
6. Review the item and confirm whether it's a match.
7. Choose **Actions**.
8. If it's a match, close the window. You're finished.
9. If it's not a match, choose **Actions** and then **Not a match**.
10. Review the item and redact or un-redact any text.
11. Close the window.

## Using the feedback to tune your classifiers

If your SITs or trainable classifiers are returning too many false positives based on the feedback, try some of these options to refine them and increase their accuracy.

### Tune trainable classifiers with feedback

Retraining custom classifiers is no longer supported. If you need to improve the accuracy of the trainable classifiers you created, remove the classifier and begin fresh with larger sample sets. For more information, see [Get started with trainable classifiers](trainable-classifiers-get-started-with#get-started-with-trainable-classifiers).

### Tune sensitive information types with feedback

To improve sensitive information type accuracy, consider the following tuning options:

- Increase the thresholds of sensitive information types found to determine severity. It's okay to use different thresholds for individual classifiers.
- Understand confidence levels and how they're defined. Try using a low confidence with high instance count, or a higher confidence level with a low instance count.
- Clone and modify the built-in SITs to include other conditions, such as the presences of keywords, more stringent value matching, or stronger formatting requirements.
- Modify a custom SIT to exclude known prefixes, suffixes, or patterns. For example, a custom SIT to detect phone numbers might trigger for every email if your email signatures or document headers include phone numbers. Excluding your organization's phone number sequences from your custom SIT can prevent the rule from triggering for every email or document.
- Include more dictionary-based SITs as conditions to narrow down the matches to those items that talk about the relevant articles. For example, a rule for matching patient diagnostics may be enhanced by requiring the presence of words like diagnostic, diagnosis, condition, symptom, and patient.
- For named-entity SITs, like **All Full Names**, it’s best to set a higher instance count threshold, like 10 or 50. If both the person names and the Social Security Numbers (SSNs) are detected together, it’s more likely that the SSNs are truly SSNs, and we reduce the risk that the policy doesn’t trigger because too few SSNs are detected.