---
layout: Conceptual
title: Sensitive information type REGEX validators and additional checks | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-regex-validators-additional-checks
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
description: Learn how to use REGEX validators and additional checks in your sentisitve information types.
ms.custom: seo-marvel-apr2020, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: eec0bb21-e317-0348-63ec-e62233b399c8
document_version_independent_id: eec0bb21-e317-0348-63ec-e62233b399c8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-regex-validators-additional-checks.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-regex-validators-additional-checks
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-regex-validators-additional-checks.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8b896464-3b7d-4e1f-84b0-9bb45aeb5f64
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1d2d671-9549-46e8-918c-24349120dbf5
platformId: 8d934732-024c-7a99-dee2-25fd365e8306
---

# Sensitive information type REGEX validators and additional checks | Microsoft Learn

Important

Microsoft Customer Service & Support can't assist with creating custom classifications or regular expression patterns. Support engineers can provide limited support for the feature, such as providing sample regular expression patterns for testing the feature, or assisting with troubleshooting an existing regular expression pattern that's not triggering as expected. However, support engineers can't assure you that any custom content-matching development fulfills your requirements or obligations.

## Sensitive Information Type regular expression validators

### Checksum validator

To run a checksum on a digit in a regular expression, you can use the *checksum validator*. For example, if you need to create a SIT for an eight-digit license number where the last digit is a checksum digit validated using a mod 9 calculation, set up the checksum algorithm as shown in the following example:

```console
Sum = digit 1 * Weight 1 + digit 2 * weight 2 + digit 3 * weight 3 + digit 4 * weight 4 + digit 5 * weight 5 + digit 6 * weight 6 + digit 7 * weight 7 + digit 8 * weight 8
Mod value = Sum % 9
If Mod value == digit 8
    Account number is valid
If Mod value != digit 8
    Account number is invalid
```

1. Define the primary element with a regular expression that matches any eight-digit number:

    ```console
    \d{8}
    ```
2. Add the checksum validator.
3. Add the weight values separated by commas, the position of the check digit, and the mod value. For more information on the Modulo operation, see [Modulo operation](https://en.wikipedia.org/wiki/Modulo_operation).

    Note

    If the check digit isn't part of the checksum calculation, use 0 as the weight for the check digit. For example, in the eight-digit license number example, weight 8 is equal to 0 if the check digit won't be used for calculating the check digit.

    [![screenshot of configured checksum validator.](media/checksum-validator.png)](media/checksum-validator.png#lightbox)

#### Parameters

The following parameters define how the checksum validator performs its calculation:

- **Weights:** To define the series of numbers with which each digit starting from position 1 to last position of the regex needs to be multiplied. This calculates the sum product. Weight positions refer to the order of the digits only, it doesn't consider any nondigit characters like dashes.
- **Mod:** Perform Modulo operation on the result from previous operation.
- **ModCoefficient:** Perform addition or subtraction on the modulo result.
- **CheckDigit:** Define the position of the check digit with which the calculated number will be compared against.

### Advanced Checksum Validator

Advanced Checksum can be used without the need of scripting, by using parameters such as PositionBasedUpdate, UseAscii, MultiDigitResult, CheckDigitValue.

- **Digit Replacement Before Computation:** Define rules to replace digits based on position or value before checksum calculation.
- **Letter-to-ASCII Conversion:** Nondigit characters can now be converted to their ASCII values instead of being ignored, enabling checksum support for alphanumeric inputs.
- **Single-Digit Reduction of Multi-Digit Results:** Intermediate results can now be reduced to a single digit by summing their digits (12 → 1+2 = 3), allowing for more compact and consistent outputs.
- **Post-Processing of Two-Digit Results:** Apply mathematical operations like division or modulo to two-digit results to derive final values.
- **Exclusion of Specific Check Digit Values:** Define a list of disallowed check digit values. If the computed result matches one, the system modifies the input and rerun the checksum logic.
- **Final Check Digit Substitution:** Post-computation, specific check digit values can be substituted with alternatives.

#### Advanced Checksum Validator Parameters

The following parameters control advanced checksum validator behavior:

- **UseAscii:** Replace alphabets with their ascii value
- **PositionBasedUpdate:** Pre checksum computation. We update the digits based on the attributes, match-position-replacewith.
- **CheckDigitValue:** Post checksum computation. If checksum calculated is part of repeat list, perform defined operation on it.
- ltiDigitResult:\*\* Post/Intermediate checksum computation. If Post/intermediate calculation result is of multiple digits, perform the defined operation on it until it's a single digit.

For example, in the XML below, we have passed the following parameters: weights, mod, checkdigit, and ascii.

```console
<Validators id="Validator_test_id_card_number">
<Validator type="Checksum">
<Param name="Weights">1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1</Param>
<Param name="Mod">9</Param>
<Param name="CheckDigit">7</Param>
<Param name="UseAscii">1</Param>
</Validator>
</Validators>
```

##### Limitations

Be aware of the following limitations when using advanced checksum validation:

- No UI Support Creating or editing SITs with advanced checksum logic isn’t available via the UX.
- In alphanumeric SITs, letters are skipped if no weights are defined for them.

### Date validator

If a date value that's embedded in a regular expression is part of a new pattern you're creating, you can use the *date validator* to test whether that date value meets your criteria. For example, you want to create a SIT for a nine-digit employee identification number. The first six digits are the date of hire in DDMMYY format and the last three are randomly generated numbers. Use these steps to validate that the first six digits are in the correct format:

1. Define the primary element with this regular expression:

    ```console
    \d{9}
    ```
2. Add the date validator.
3. Select the date format and the start offset. Since the date string is the first six digits, the offset is `0`.

    [![screenshot of configured date validator.](media/date-validator.png)](media/date-validator.png#lightbox)

### Functional processors as validators

You can use function processors for some of the most commonly used SITs as validators. Using function processors allows you to define your own regular expressions while ensuring that they pass the additional checks required by the SIT. For example, Func\_India\_Aadhar ensures that the custom regular expression you defined passes the validation logic required for the Indian Aadhar card. For more information on the DLP functions that you can use as validators, see [Sensitive information type functions](sit-functions).

### Luhn check validator

You can use the Luhn check validator if you have a custom sensitive information type that includes a regular expression, which should pass the [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm).

## Sensitive information type additional checks

Here are the definitions and some examples for the available additional checks.

**Exclude specific matches**: This check lets you define keywords to exclude when detecting matches for the pattern you're editing. For example, you might exclude test credit card numbers like '4111111111111111' so that they're not matched as a valid number.

**Starts or doesn't start with characters**: This check lets you define the characters that the matched items must or must not start with. For example, if you want the pattern to detect only credit card numbers that start with 41, 42, or 43, select **Starts with** and add 41, 42, and 43 to the list, separated by commas.

**Ends or doesn't end with characters**: This check lets you define the characters that the matched items must or must not end with. For example, if your Employee ID number can't end with 0 or 1, select **Doesn't end with** and add 0 and 1 to the list, separated by commas.

**Exclude duplicate characters**: This check lets you ignore matches in which all the digits are the same. For example, if the six digit employee ID number can't have all the digits be the same, you can select **Exclude duplicate characters** to exclude 111111, 222222, 333333, 444444, 555555, 666666, 777777, 888888, 999999, and 000000 from the list of valid matches for the employee ID.

**Include or exclude prefixes**: This check lets you define the keywords that must or must not be found immediately before the matching entity. Depending on your selection, entities are matched or not matched if they're preceded by the prefixes you include here. For example, if you **Exclude** the prefix `GUID`, any entity that's preceded by **GUID:** won't match.

**Include or exclude suffixes**: This check lets you define the keywords that must or must not be found immediately after the matching entity. Depending on your selection, entities match or not match if they're followed by the suffixes you include here. For example, if you **Exclude** the suffix `GUID`, any text that's followed by `:GUID` won't match.