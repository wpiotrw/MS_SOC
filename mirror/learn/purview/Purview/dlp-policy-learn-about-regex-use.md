---
layout: Conceptual
title: Learn about using regular expressions (regex) in DLP policies | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-policy-learn-about-regex-use
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords: CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-01-21T00:00:00.0000000Z
audience: ITPro
ms.topic: article
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- highpri
- purview-compliance
search.appverid:
- MET150
description: Learn about using regular expressions in DLP policies.
locale: en-us
document_id: c67c11df-d2db-a6b6-c973-9ac9d698f7ec
document_version_independent_id: c67c11df-d2db-a6b6-c973-9ac9d698f7ec
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-policy-learn-about-regex-use.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-policy-learn-about-regex-use
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-policy-learn-about-regex-use.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 6199f25a-b0c8-20a4-47da-d6759d55387f
---

# Learn about using regular expressions (regex) in DLP policies | Microsoft Learn

A *regular expression*, commonly referred to as a *regex*, is a sequence of characters that defines a search pattern. Regular expressions are primarily used for pattern matching with strings and in string matching; for example, in "find and replace" operations. You can use a regex in Microsoft Purview Data Loss Prevention (DLP) to define patterns that help you identify and classify sensitive data, or to help detect patterns in content. The most common regex uses in Microsoft Purview DLP are:

- Defining a [custom sensitive information types](sit-create-a-custom-sensitive-information-type#create-custom-sensitive-information-types).
- Leveraging the `SubjectOrBodyMatchesPatterns` condition in a DLP rule ([Read more here](/en-us/powershell/module/exchange/new-dlpcompliancerule).)

This article describes common issues that occur when working with regular expressions and how you can resolve them.

## Potential validation issue when using a regex with DLP

- Basic units of the pattern, such as literal characters, digits, whitespace, and punctuation marks can be represented by themselves or by special symbols called metacharacters, such as `\d` for any digit, `\s` for any whitespace, or `\.` for a literal dot.
- The basic units, when combined with quantifiers, specify how many times they can or must occur in a match. For example, `*` means zero or more, `+` means one or more, `?` means zero or one, and `{n,m}` means between `n`and `m` times. For example, `\d+` means one or more digits, `\s?` means optional whitespace, and `a{3,5}` means between three and five instances of the literal character **a**.
- A regex either uses a positive lookbehind or a negative lookbehind. A *lookbehind* is used to check whether there's a match before a certain position in the input string, without including the actual characters in the match. A positive lookbehind is used to match when the lookbehind pattern **is** present, while a negative lookbehind is used to match when the lookbehind pattern **is not** present.
- Consider this example: `(?<=^|\s|_)`. This example shows a lookbehind that includes three possibilities:
    1. `^` asserts the position. In this case, it requires the pattern matching to begin at the start of the line.
    2. `\s` detects any whitespace characters as a match.
    3. `_` matches the literal underscore character ( **\_** ).
- In the previous example, possibilities #2 and #3 will each match a single character. However, possibility #1 only indicates where the matching should start. It will not produce results with respect to any character matches.
- Take a second example, `^\d+$`. This regex will only detect a string composed entirely of digits, from start to end.
- Regex pattern validations in conditions are case insensitive by default. To honor the case sensitivity please add (?-i) to the pattern

## How to get extracted text

A regex is matched on the extracted text of the content, rather than on the content itself. So, even when the pattern appears to be on the content, it might not match when evaluating a DLP policy.

To ensure that you capture the appropriate matches, take the following steps:

1. Use the [Test-TextExtraction](/en-us/powershell/module/exchange/test-textextraction) cmdlet to get the extracted text, which will consist of a stream of strings.
2. Next, use the extracted text for matching the regular expression.

For instance:

```powershell
$data = ([System.IO.File]::ReadAllBytes('<FilePath>'))
$tr = Test-TextExtraction -FileData $data
$tr.ExtractedResults.ExtractedStreamText | Format-List
```

## How to verify sensitive information type detection

To verify sensitive information type (SIT) detection, we need to take the text we just extracted and then run the [Test-DataClassification](/en-us/powershell/module/exchange/test-dataclassification) cmdlet on it to verify detection. The results of running the cmdlet will indicate whether there are any SIT matches for the regex.

For example:

```powershell
$textStream = $tr.ExtractedResults.ExtractedStreamText | Out-String
$result = Test-DataClassification -TextToClassify $textStream
$result.ClassificationResults | Format-List
```

## Example of using a regex in a DLP policy rule

In this example, we will block email that contains strings starting with *ABC* followed by a number.

**Regex used:**`^ABC\d`

**DLP rule sample:**`New-DlpComplianceRule -Name "Rule_00" -Policy "Policy_00" -SubjectOrBodyMatchesPatterns "^ABC\d" - BlockAccess $True`

**Sample email**

![sample email for regex matching](media/dlp-regex-email-example.png)

While it seems that the regex will detect a match with this mail item, the extracted text looks like this:`Regex Test Email ABC123` As you can see, the extracted text begins with the content in the subject line of the email, rather than with the content in the body of the email. However, the inclusion of the assertion character, `^`, at the start of the regex requires that the *ABC...* string must be at the start of the extracted text for a match to be detected.

**To resolve this issue**, you can change the regex to `ABC\d`.

## Regex requirements for custom sensitive information types

When you define a regex for a [custom sensitive information type](sit-create-a-custom-sensitive-information-type), the pattern must follow a specific structure to work correctly with Microsoft Purview classification. This requirement applies whether you create the SIT through the Microsoft Purview portal or PowerShell.

The required structure is:

`(?:prefix)(primary capturing group)(?:suffix)`

Where:

- Use **exactly one** capturing group for the primary match. Use noncapturing groups `(?: ... )` for any prefix/suffix or other grouping.
- All match variants must be handled **inside** that single capturing group using `|` (alternation).
- Multiple capturing groups separated by `|` at the top level are **not supported** and are blocked during validation.

If your regex contains multiple top-level capturing groups, the SIT fails to classify content on Endpoint DLP and other workloads.

**Example of an invalid pattern:**

`(?:[\s,;])([A-Z]{2}[0-9]{3})(?:[\s,;])|(?:[\s,;])([A-Z]{2}[A-Z]{4}[0-9])(?:[\s,;])|(?:[\s,;])([A-Z]{2}[0-9]{5})(?:[\s,;])`

This pattern has three separate capturing groups at the top level. Instead, consolidate all variants into one capturing group:

**Example of a valid pattern:**

`(?:[\s,;])([A-Z]{2}[0-9]{3}|[A-Z]{2}[A-Z]{4}[0-9]|[A-Z]{2}[0-9]{5})(?:[\s,;])`

For more information on limits, see [Sensitive information type limits](sit-limits).

## Learn more about regular expressions

- [Regular Expression Language - Quick Reference](/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference)
- [Regex101 (an interactive tool for testing and learning regular expressions)](https://regex101.com/%28https://regex101.com/%29)
- ["Regular Expressions" from Mozilla Developer Network (a comprehensive guide to regular expressions)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)
- [Boost Article on *Lookbehind*](https://www.boost.org/doc/libs/1_65_1/libs/regex/doc/html/boost_regex/syntax/perl_syntax.html#boost_regex.syntax.perl_syntax.lookbehind)