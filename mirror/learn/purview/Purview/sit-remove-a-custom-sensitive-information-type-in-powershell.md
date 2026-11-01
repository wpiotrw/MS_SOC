---
layout: Conceptual
title: Remove a custom sensitive information type using PowerShell | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-remove-a-custom-sensitive-information-type-in-powershell
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-sensitive-information-types
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Remove a custom sensitive information type in Security & Compliance PowerShell by deleting it from a rule package or removing the entire package. Includes prerequisite checks to avoid breaking DLP policies or mail flow rules.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 1a81aa8f-99fb-6c27-e4ce-ea023053724b
document_version_independent_id: 1a81aa8f-99fb-6c27-e4ce-ea023053724b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-remove-a-custom-sensitive-information-type-in-powershell.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-remove-a-custom-sensitive-information-type-in-powershell
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-remove-a-custom-sensitive-information-type-in-powershell.md
cmProducts: []
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
platformId: 68d23674-94d8-49db-cc55-eb6845797af6
---

# Remove a custom sensitive information type using PowerShell | Microsoft Learn

In Security & Compliance PowerShell, there are two methods to remove custom sensitive information types:

- **Remove individual custom sensitive information types**: Use the method documented in [Modify a custom sensitive information type using PowerShell](sit-modify-a-custom-sensitive-information-type-in-powershell#modify-a-custom-sensitive-information-type-using-powershell). Export the custom rule package containing the custom sensitive information type. Remove the sensitive information type from the XML file, and then import the updated XML file back into the existing custom rule package.
- **Remove a custom rule package and all custom sensitive information types that it contains**: Removing an entire custom rule package is documented in this section.

Note

Before your remove a custom sensitive information type, verify that no DLP policies or Exchange mail flow rules (also known as transport rules) still reference the sensitive information type.

1. [Security & Compliance PowerShell](/en-us/powershell/exchange/exchange-online-powershell)
2. To remove a custom rule package, use the [Remove-DlpSensitiveInformationTypeRulePackage](/en-us/powershell/module/exchange/remove-dlpsensitiveinformationtyperulepackage) cmdlet. Run the following command to remove the specified rule package when you no longer need it or want to replace it:

    ```powershell
    Remove-DlpSensitiveInformationTypeRulePackage -Identity "RulePackageIdentity"
    ```

    You can use the Name value (for any language) or the `RulePack id` (GUID) value to identify the rule package.

    The following example removes a custom rule package named "Employee ID Custom Rule Pack":

    ```powershell
    Remove-DlpSensitiveInformationTypeRulePackage -Identity "Employee ID Custom Rule Pack"
    ```

    For detailed syntax and parameter information, see the [Remove-DlpSensitiveInformationTypeRulePackage cmdlet reference](/en-us/powershell/module/exchange/remove-dlpsensitiveinformationtyperulepackage).
3. To verify that you've successfully removed a custom sensitive information type, do any of the following steps:

    - Run the [Get-DlpSensitiveInformationTypeRulePackage](/en-us/powershell/module/exchange/get-dlpsensitiveinformationtyperulepackage) cmdlet and verify the rule package is no longer listed:

        ```powershell
        Get-DlpSensitiveInformationTypeRulePackage
        ```
    - Run the [Get-DlpSensitiveInformationType](/en-us/powershell/module/exchange/get-dlpsensitiveinformationtype) cmdlet to verify the sensitive information types in the removed rule package are no longer listed:

        ```powershell
        Get-DlpSensitiveInformationType
        ```

        For custom sensitive information types, the Publisher property value will be something other than "Microsoft Corporation".
    - Replace &lt;Name&gt; with the Name value of the sensitive information type (for example, Employee ID) and run the [Get-DlpSensitiveInformationType](/en-us/powershell/module/exchange/get-dlpsensitiveinformationtype) cmdlet to verify the sensitive information type is no longer listed:

        ```powershell
        Get-DlpSensitiveInformationType -Identity "<Name>"
        ```

## Related resources

- [Learn about Microsoft Purview Data Loss Prevention](dlp-learn-about-dlp)
- [Sensitive information type entity definitions](sit-sensitive-information-type-entity-definitions)
- [Sensitive information type functions](sit-functions)