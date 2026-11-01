---
layout: Conceptual
title: Common usage scenarios for sensitive information types | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-common-scenarios
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
description: Implement common sensitive information type scenarios using example procedures that you can adapt to your organization's needs.
ms.custom: seo-marvel-apr2020, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: bb965195-8666-d213-230f-ad8ce50d00db
document_version_independent_id: bb965195-8666-d213-230f-ad8ce50d00db
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-common-scenarios.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-common-scenarios
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-common-scenarios.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/60932d05-feee-4685-a73b-595e25dd9318
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/c43bb58b-1190-419b-8d18-e6052371b599
platformId: acaf298c-a8f1-84c4-14f9-a0594372b3ee
---

# Common usage scenarios for sensitive information types | Microsoft Learn

This article describes how to implement some common sensitive information type (SIT) use case scenarios. You can use these procedures as examples and adapt them to your specific needs.

## Protect credit card numbers

Contoso Bank needs to classify the credit card numbers that they issue as sensitive. Their credit cards start with a set of six-digit patterns. They would like to customize the out-of-the-box credit card definition to detect only those credit card numbers starting with their six-digit patterns.

**Suggested solution**

1. Create a copy of the credit card SIT. Use the steps to [copy and modify an existing SIT](sit-create-a-custom-sensitive-information-type#copy-and-modify-an-existing-sit) to copy the credit card SIT.
2. Edit the high confidence pattern. Follow the steps in [Edit or delete a SIT pattern](sit-get-started-exact-data-match-create-rule-package#edit-or-delete-a-sit-pattern).
3. Add the **starts with** check and add the list of pattern digits (formatted & unformatted). For example to ensure that the SIT only considers credit cards starting with 411111 & 433512 should be considered valid, add the following to the list 4111 11, 4111-11, 411111, 4335 12, 4335-12, 433512.
4. Repeat step 2 & 3 for the low confidence pattern.

## Test numbers similar to Social Security numbers

Contoso has identified a few nine-digit test numbers that trigger false positive matches in the Social Security Number (SSN) Microsoft Purview Data Loss Prevention (DLP) policy. They would like to exclude these numbers from the list of valid matches SSN matches.

**Suggested solution**

1. Create a copy of the SSN SIT. Use the steps to [copy and modify an existing SIT](sit-create-a-custom-sensitive-information-type#copy-and-modify-an-existing-sit) to copy the SSN SIT.
2. Edit the high confidence pattern. Follow the steps in [Edit or delete a SIT pattern](sit-get-started-exact-data-match-create-rule-package#edit-or-delete-a-sit-pattern).
3. Add the numbers you want to exclude in the **exclude specific values** check. For example, to exclude 239-23-532 & 23923532, just adding 23923532 is sufficient.
4. Repeat step 2 & 3 for other confidence patterns as well

## Prevent phone numbers in signatures from triggering matches

Australia-based Contoso finds that phone numbers in email signatures are triggering a match for their Australia company number DLP policy.

**Suggested solution**

Add a 'NOT' group in supporting elements using a keyword list containing commonly used keywords in email signatures, such as *Phone*, *Mobile*, *email*, *Thanks and regards*, etc. Keep the proximity of this keyword list to a smaller value (for instance, 50 characters) for better accuracy. For more information, see [Get started with custom sensitive information types](sit-create-a-custom-sensitive-information-type).

## Troubleshoot why an ABA routing policy doesn't trigger

DLP policy is unable to trigger ABA routing number policy in large excel files because the required keyword isn't within 300 characters.

**Suggested solution**

Create a copy of the built-in SIT and edit it to change the proximity of the keyword list from *300 characters* to *Anywhere in the document*.

Tip

You may edit the keyword list to include/exclude keywords that are relevant to your organization.

## Unable to detect credit card numbers with unusual delimiters

Contoso Bank has noticed some of their employees share credit card numbers with ‘/’ as a delimiter, for example, 4111/1111/1111/1111, which the out-of-the-box credit card definition doesn't detect. Contoso would like to define their own regex and validate it using LuhnCheck.

**Suggested solution**

1. Create a copy of the credit card SIT using the steps in [Customize a built-in sensitive information type](sit-customize-a-built-in-sensitive-information-type)
2. Add a new pattern
3. In the primary element, select **regular expression**
4. Define the regular expression that includes ‘/’ as part of the regular expression; choose **validator** and then select **luhncheck** or **func\_credit\_card** to ensure the regex also passes the LuhnCheck.

## Ignore disclaimer notices when configuring sensitive information type detection

Many organizations add legal disclaimers, disclosure statements, signatures, or other information to the top or bottom of email messages that enter or leave their organizations. In some cases, emails sent within an organization itself can contain such text. For example, employees might add signatures with motivational quotes, social messages, and so on. A disclaimer or signature can contain the terms that are present in the lexicon of a CC and might generate many false positives.

For example, a typical disclaimer might contain words like *sensitive*, or *confidential*. Policies looking for sensitive info will detect such disclaimers as incidents, leading to lot of false positives. Thus, providing customers with an option to ignore disclaimers can reduce the number of false positives and increase the efficiency of the compliance team.

### Review an example disclaimer notice

Consider the following disclaimer:

"IMPORTANT NOTICE: This e-mail message is intended to be received only by persons entitled to receive the confidential information it may contain. E-mail messages to clients of Contoso may contain information that is confidential and legally privileged. Please do not read, copy, forward, or store this message unless you are an intended recipient. If you have received this message in error, please forward it to the sender and delete it completely from your computer system."

If the SIT is configured to detect *confidential* as a keyword, the SIT pattern invokes a match every time an email includes the disclaimer, leading to considerable number of false positives.

### Ignore disclaimer using prefix and suffix in SIT

One way to ignore keyword instances in disclaimer text is to exclude keywords that are preceded by a specific prefix and followed by a specific suffix.

Consider this disclaimer:

"IMPORTANT NOTICE: This e-mail message is intended to be received only by persons *entitled to receive the* confidential **information it may contain**. E-mail messages to clients of Contoso may contain information that is confidential and legally privileged. Please do not read, copy, forward, or store this message unless you are an intended recipient. If you have received this message in error, please forward it to the sender and delete it completely from your computer system."

Say we have two instances of the keyword *confidential*. If we configure the SIT to ignore instances of the keyword *confidential* that are preceded by prefixes (italicized in the example) and followed by suffixes (bolded in the example), then we can successfully ignore disclaimers in most cases.

To ignore the disclaimer using prefix and suffix:

1. Add additional checks in the current SIT to exclude prefix and suffix text to the keyword that we want to ignore in the disclaimer.
2. Choose to exclude the prefix and in the **Prefixes** text box enter **contain information that is**.
3. Choose to exclude the suffix and in the **Suffixes** text box enter **and legally privileged**.
4. Repeat this process for other instances of the keywords in the disclaimer, as shown in the following graphic.

### Ignore disclaimer by excluding secondary elements

Another way to add a list of supporting elements (keyword instances found in disclaimer text) that need to be excluded is to exclude secondary elements.

Consider this disclaimer:

"IMPORTANT NOTICE: This e-mail message is intended to be received only by persons entitled to receive the confidential information it may contain. E-mail messages to clients of Contoso may contain information that is confidential and legally privileged. Please do not read, copy, forward, or store this message unless you are an intended recipient. If you have received this message in error, please forward it to the sender and delete it completely from your computer system."

We have two instances of the keyword “confidential” in this example. If we configure the SIT to ignore instances of this keyword in the disclaimer (underlined as red in the following image), we can achieve ignoring disclaimers in most of the cases.

![You can add more conditions to the pattern to exclude additional instances in the disclaimer.](media/sit-scenario-edit-pattern.png)

To ignore the disclaimer using secondary elements:

1. Select **Not any of these** group in the supporting elements.
2. Add the instances of disclaimer that we want to ignore as a keyword list/dictionary.
3. Add the keywords as a new line that we want to ignore. Remember that the length of each text can't be more than 50 characters.
4. Set the proximity of this element to be within 50-60 characters of the primary element.