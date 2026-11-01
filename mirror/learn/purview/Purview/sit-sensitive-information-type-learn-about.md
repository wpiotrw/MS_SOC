---
layout: Conceptual
title: Learn about sensitive information types | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-learn-about
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-07-24T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom:
- msecd-doc-authoring-1017
audience: Admin
search.appverid: MET150
ms.topic: article
ms.service: purview
ms.subservice: purview-sensitive-information-types
ms.collection:
- highpri
- purview-compliance
description: This article gives an overview of sensitive information types and how they detect sensitive information like social security, credit card, or bank account numbers to identify sensitive items.
locale: en-us
document_id: 148fbe99-d83e-3f60-73b2-db25f18cc2a9
document_version_independent_id: 148fbe99-d83e-3f60-73b2-db25f18cc2a9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-sensitive-information-type-learn-about.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-sensitive-information-type-learn-about
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-sensitive-information-type-learn-about.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 96ac2ebd-cae8-c25e-ec1a-3b3b2e2b2ab4
---

# Learn about sensitive information types | Microsoft Learn

Identifying and classifying sensitive items that are under your organization's control is the first step in the [Information Protection discipline](information-protection). Microsoft Purview provides three ways of identifying items so that they can be classified:

- manually, by users
- via automated pattern recognition, as with sensitive information types
- via [machine learning](trainable-classifiers-learn-about)

Sensitive information types (SITs) are pattern-based classifiers. They detect sensitive information like social security, credit card, or bank account numbers to identify sensitive items, see [Sensitive information type entity definitions](sit-sensitive-information-type-entity-definitions) for a complete list of all SITs.

Microsoft provides a large number of preconfigured SITs or you can create your own.

## Licensing

E5 license is required to make use of credential scanning SITs. For a list of all the credential scanning SITs, see [All credentials sensitive information types](sit-defn-all-creds). This SIT contains all the credential scanning SITs that are available in the portal. Each member of this SIT is a credential scanning SIT and can be used as a standalone. For a list of many Microsoft created SITs, see [Sensitive information type entity definitions](sit-sensitive-information-type-entity-definitions).

## Sensitive information types are used in

- [Microsoft Purview Data Loss Prevention policies](dlp-learn-about-dlp)
- [Sensitivity labels](sensitivity-labels)
- [Retention labels](retention)
- [Insider risk management](insider-risk-management)
- [Communication compliance](communication-compliance)
- [Auto-labeling policies](apply-sensitivity-label-automatically#how-to-configure-auto-labeling-for-office-apps)
- [Microsoft Priva](/en-us/privacy/priva)

## Categories of sensitive information types

### Built in sensitive information types

Microsoft created these SITs and they show up in the Purview portal by default. These SITs can't be edited, but you can use them as templates by copying them to create custom sensitive information types. See, [Sensitive information type entity definitions](sit-sensitive-information-type-entity-definitions) for a full list of all SITs.

### Named entity sensitive information types

Named entity SITs also show up in the Purview portal by default. They detect person names, physical addresses, and medical terms and conditions. They can't be edited or copied. For more information, see [Learn about named entities](sit-named-entities-learn#learn-about-named-entities).

Named entity SITs come in two types:

**un-bundled**

These named entity SITs have a narrower focus, such as a single country or region, or a single class of terms. Use them when you need a data loss prevention (DLP) policy with a narrower detection scope. See, [Examples of named entity SITs](sit-named-entities-learn#examples-of-named-entity-sits).

**bundled**

Bundled named entity SITs detect all possible matches in a class, such as *All physical addresses*. Use them as broad criteria in your DLP policies for detecting sensitive items. See, [Examples of named entity SITs](sit-named-entities-learn#examples-of-named-entity-sits).

Tip

You must enable [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection)if you want to use a bundled SIT in an endpoint DLP policy. This requirement is specific to the combination of bundled SITS andendpoint DLP policies.

### Custom sensitive information types

If the preconfigured sensitive information types don't meet your needs, you can create your own custom sensitive information types that you fully define or you can copy one of the built-in ones and modify it. For more information, see

[Create a custom sensitive information type in the Microsoft Purview portal](sit-create-a-custom-sensitive-information-type).

### Exact data match sensitive information types

All exact data match (EDM)-based SITs are created from scratch. You use them to detect items that have exact values, which you define in a database of sensitive information. For more information, see [Learn about exact data match based sensitive information types](sit-learn-about-exact-data-match-based-sits#learn-about-exact-data-match-based-sensitive-information-types).

## Fundamental parts of a sensitive information type

Every sensitive information type (SIT) entity consists of the following fields:

- ***Name:*** Indicates how the sensitive information type is referred to.
- ***Description:*** Explanation of what the sensitive information type is looking for.
- ***Pattern:*** Defines what a SIT detects. It consists of the following components: primary element, supporting elements, confidence level, and proximity.

The following table describes each component of the patterns used in defining sensitive information types.

| Pattern component | Description |
| --- | --- |
| Primary element | The main element that the sensitive information type is looking for. It can be a **regular expression** with or without a checksum validation, a **keyword list**, a **keyword dictionary**, or a **function**.Each of these types of elements can either be selected from the list of existing SITs or can be custom-defined by a user with admin permissions. Once an element is defined, it appears in the list of existing elements, along with those that come built-in. |
| Supporting element | An element that acts as corroborative evidence. When included, supporting elements help increase the confidence level with respect to the accuracy of detected matches. For example, if the primary element is defined as `SSN` (composed of nine digits), and the keyword *Social Security Number (SSN)* is used as a supporting element when found in proximity to `SSN`, the confidence that the `SSN` detected is truly a Social Security number is higher than if the *Social Security Number (SSN)* keyword is not present.  A supporting element can be a regular expression (with or without a checksum validation), a keyword list, or a keyword dictionary. |
| Confidence Level | There are three confidence levels with respect to detected matches: high, medium, and low. The confidence level reflects how much supporting evidence is detected along with the primary element. The more supporting evidence a detected item contains, the higher the confidence that a matched item contains the sensitive info you're looking for. For more information about confidence levels, see the video included later in this article. |
| Proximity | Specifies how close a supporting element is to a primary element, in terms of the number of characters between them. |

### Understanding proximity

The following diagram shows how match detection works with respect to proximity. In this example, the primary element is the `SSN` field and the SIT definition requires that each instance of an `SSN` value must be within a specified proximity to at least one of the following elements: 

- `AccountNumber`
- `Name`
- `DateOfBirth`

In the diagram, we see that the data being checked includes three different instances of the `SSN` field: `SSN1`, `SSN2`, `SSN3`, and `SSN4`.

[![Diagram of corroborative evidence and proximity window](media/sit-proximity-diagram.png)](media/sit-proximity-diagram.png#lightbox).

To understand how proximity works, let’s start by taking a look at some sample detection criteria. Here, were want to detect nine-digit social security numbers. The detection criteria require that a nine-digit regular expression (primary element) is found in conjunction with supporting evidence (among the `AccountNumber`, `Name`, and `DateOfBirth` fields) that appears within 250 characters (the *proximity*).

As illustrated in the diagram, only the primary elements `SSN1` and `SSN4` meet the detection criteria described. Let's take a closer look.

- In the case of `SSN1`, the `AccountNumber` value is within the specified proximity window of 250 characters, so a match is detected.
- In both the cases of `SSN2` and `SSN3`, none of the supporting elements occur within 250 characters of the primary element, so those values aren't detected as a match. However, as you look at the proximity window for `SSN2` in the diagram, you might ask: *Why isn't there a match for `SSN2`? Doesn't the `SSN2` proximity window extend to the `Name` element?* This is a good question. The answer is: *Not quite*. While the proximity window ***extends into*** the `Name` value, it doesn't include the ***entire*** value, so the pattern doesn't match.
- Finally, in the case of `SSN4`, there are two supporting elements within the proximity window, both `Name` and `DateOfBirth`, so this pattern matches as well.

Learn more about confidence levels in this short video.

## Example sensitive information type

#### Argentina national identity (DNI) number

##### Format

Eight digits separated by periods

##### Pattern

Eight digits:

- two digits
- a period
- three digits
- a period
- three digits

##### Checksum

No

##### Definition

A DLP policy has medium confidence that it has detected this type of sensitive information if, within a proximity of 250 characters:

- The regular expression Regex\_argentina\_national\_id finds content that matches the pattern.
- A keyword from Keyword\_argentina\_national\_id is found.

```xml
<!-- Argentina National Identity (DNI) Number -->
<Entity id="00aa00aa-bb11-cc22-dd33-44ee44ee44ee" recommendedConfidence="75" patternsProximity="250">
   <Pattern confidenceLevel="75">
      <IdMatch idRef="Regex_argentina_national_id"/>
      <Match idRef="Keyword_argentina_national_id"/>
  </Pattern>
</Entity>
```

##### Keywords

###### Keyword\_argentina\_national\_id

- Argentina National Identity number
- Identity
- Identification National Identity Card
- DNI
- National Registry of Persons (NIC)
- Documento Nacional de Identidad
- Registro Nacional de las Personas
- Identidad
- Identificación

### More on confidence levels

In a sensitive information type entity definition, **confidence level** reflects how much supporting evidence is detected in addition to the primary element. The more supporting evidence an item contains, the higher the confidence that a matched item contains the sensitive info you're looking for. For example, matches with a high confidence level contain more supporting evidence in close proximity to the primary element, whereas matches with a low confidence level would contain little to no supporting evidence in close proximity.

A high confidence level returns the fewest false positives but might result in more false negatives. Low or medium confidence levels return more false positives but few to zero false negatives.

- **low confidence**: Matched items contain the fewest false negatives but the most false positives. Low confidence returns all low, medium, and high confidence matches. The low confidence level has a value of 65.
- **medium confidence**: Matched items contain an average number of false positives and false negatives. Medium confidence returns all medium, and high confidence matches. The medium confidence level has a value of 75.
- **high confidence**: Matched items contain the fewest false positives but the most false negatives. High confidence only returns high confidence matches and has a value of 85.

You should use high confidence level patterns with low counts, say five to 10, and low confidence patterns with higher counts, say 20 or more.

Note

If you have existing policies or custom sensitive information types (SITs) defined using number-based confidence levels (also known as *accuracy*), they'll automatically be mapped to the three discrete confidence levels; low confidence, medium confidence, and high confidence, across the Security @ Compliance Center UI.

- All policies with minimum accuracy or custom SIT patterns with confidence levels of between 76 and 100 will be mapped to high confidence.
- All policies with minimum accuracy or custom SIT patterns with confidence levels of between 66 and 75 will be mapped to medium confidence.
- All policies with minimum accuracy or custom SIT patterns with confidence levels less than or equal to 65 will be mapped to low confidence.

## Creating custom sensitive information types

You can choose from several options to create custom sensitive information types.

- **Use the UI** - You can set up a custom sensitive information type using the Purview portal UI. With this method, you can use regular expressions, keywords, and keyword dictionaries. To learn more, see [Create a custom sensitive information type](sit-create-a-custom-sensitive-information-type).
- **Use EDM** - You can set up custom sensitive information types using Exact Data Match (EDM)-based classification. This method enables you to create a dynamic sensitive information type using a secure database that you can refresh periodically. See [Learn about exact data match based sensitive information types](sit-learn-about-exact-data-match-based-sits#learn-about-exact-data-match-based-sensitive-information-types).
- **Use PowerShell** - You can set up custom sensitive information types using PowerShell. Although this method is more complex than using the UI, you have more configuration options. See [Create a custom sensitive information type in Security & Compliance PowerShell](sit-create-a-custom-sensitive-information-type-in-scc-powershell).

### Tuning trainable classifiers

Endpoint DLP classifies files based on all sensitive information types available in the tenant, including custom sensitive information types, regardless of their utilization in any DLP policies. This can cause excessive classification traffic if the sensitive information types aren't well tuned and end up matching many files. You should optimize all custom sensitive information types. Do this by removing unused sensitive information types and redesigning SITs if they match most of the files in your organization. For guidance on utilizing SIT Regex validators to tune SITs, see: [Sensitive information type REGEX validators and additional check](sit-regex-validators-additional-checks#sensitive-information-type-regex-validators-and-additional-checks)

## Double byte character set support

Improved confidence levels are available for immediate use within Microsoft Purview Data Loss Prevention services, information protection, Communication Compliance, data lifecycle management, and records management.

- Information Protection now supports double byte character set languages for:
- Chinese (simplified)
- Chinese (traditional)
- Korean
- Japanese

This support is available for sensitive information types. For more information, see [Information protection support for double byte character sets release notes](mip-dbcs-relnotes).

## Single byte character set support

To detect patterns containing Chinese/Japanese characters and single byte characters or to detect patterns containing Chinese/Japanese and English, define two variants of the keyword or regex.

For example, to detect a keyword like "机密的document", use two variants of the keyword; one with a space between the Japanese and English text and another without a space between the Japanese and English text. So, the keywords to be added in the SIT should be "机密的 document" and "机密的document". Similarly, to detect a phrase "東京オリンピック2020", two variants should be used; "東京オリンピック 2020" and "東京オリンピック2020".

Along with Chinese/Japanese/double byte characters, if the list of keywords/phrases also contains non-Chinese/Japanese words also (for instance, English only), you should create two dictionaries/keyword lists. One for keywords containing Chinese/Japanese/double byte characters and another one for English-only keywords. For example, if you want to create a keyword dictionary/list with three phrases "Highly confidential", "機密性が高い" and "机密的document", the you should create two keyword lists.

- Highly confidential
- 機密性が高い, 机密的document and 机密的 document While creating a regex using a double byte hyphen or a double byte period, make sure to escape both the characters like you would escape a hyphen or period in a regex. Here's a sample regex for reference: `(?<!\d)([4][0-9]{3}[\-?\-\t]*[0-9]{4}`

> 
> We recommend using string match instead of word match in a keyword list.

## Detection differences across workloads

The same sensitive information type can produce different results depending on where content is evaluated—for example, email in transit (Exchange), files at rest (SharePoint and OneDrive), and files on managed devices (Endpoint DLP). Endpoint DLP classifies files against *all* sensitive information types available in the tenant, and using a bundled SIT in an endpoint DLP policy requires [Advanced classification scanning and protection](dlp-configure-endpoint-settings#advanced-classification-scanning-and-protection).

Before you rely on a custom SIT in production, test it and validate detection in each workload where you intend to use it—for example, a mail flow rule, a SharePoint or OneDrive policy, and an endpoint policy. Detection can also be affected by content-extraction limits such as maximum file size and the number of characters scanned; see [DLP platform considerations](dlp-policy-reference#dlp-platform-considerations).

## Test sensitive information type

You can test the SIT by uploading a sample file. The test results show the number of matches for each confidence level. You can test built-in SITs, custom SITs, trainable classifiers, and exact data match.

[Test Built-in and Custom sensitive information type](sit-create-a-custom-sensitive-information-type)

[Test exact data match sensitive information type.](sit-get-started-exact-data-match-test)

To test any custom or default SIT tenant, there must be at least one Exchange Online license added to the tenant. Otherwise, the Test SIT option will be greyed out when any SIT is selected.

## Provide match/not a match accuracy feedback in sensitive info types

You can view the number of matches a SIT has in **Sensitive info types** and **Content explorer**. You can also provide feedback on whether an item is actually a match or not using the **Match**, **Not a Match** feedback mechanism and use that feedback to tune your SITs. For more information, see [Increase classifier accuracy](data-classification-increase-accuracy).

## For further information

- [Sensitive information type entity definitions](sit-sensitive-information-type-entity-definitions)
- [Create a custom sensitive information type](sit-create-a-custom-sensitive-information-type)
- [Create a custom sensitive information type in PowerShell](sit-create-a-custom-sensitive-information-type-in-scc-powershell)

To learn how to use sensitive information types to comply with data privacy regulations, see [Deploy information protection for data privacy regulations with Microsoft 365](/en-us/microsoft-365/solutions/information-protection-deploy) (aka.ms/m365dataprivacy).