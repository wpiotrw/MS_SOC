---
layout: Conceptual
title: Modify a custom sensitive information type using PowerShell | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-modify-a-custom-sensitive-information-type-in-powershell
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
description: Learn how to modify a custom sensitive information type in Security & Compliance PowerShell by exporting its rule package, editing the XML, and reimporting the updated package.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 1e244045-aa18-acc0-c1c0-574bef04f40d
document_version_independent_id: 1e244045-aa18-acc0-c1c0-574bef04f40d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-modify-a-custom-sensitive-information-type-in-powershell.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-modify-a-custom-sensitive-information-type-in-powershell
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-modify-a-custom-sensitive-information-type-in-powershell.md
cmProducts: []
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: ced02b38-4a75-6688-6f81-bc45afd7a580
---

# Modify a custom sensitive information type using PowerShell | Microsoft Learn

Before you begin, connect to Security & Compliance PowerShell. For instructions, see [Security & Compliance PowerShell](/en-us/powershell/exchange/exchange-online-powershell).

In Security & Compliance PowerShell, modifying a custom sensitive information type requires you to:

1. Export the existing rule package that contains the custom sensitive information type to an XML file (or use the existing XML file if you have it).
2. Modify the custom sensitive information type in the exported XML file.
3. Import the updated XML file back into the existing rule package.

To connect to Security & Compliance PowerShell, see [Security & Compliance PowerShell](/en-us/powershell/exchange/exchange-online-powershell).

## Step 1: Export the existing rule package to an XML file

Use the following steps to export the existing rule package to an XML file.

Note

If you have a copy of the XML file (for example, if you just created and imported it), you can skip to Step: 2 Modify the sensitive information type in the exported XML file.

1. If you don't already know the name of the custom rule package, run the [Get-DlpSensitiveInformationTypeRulePackage](/en-us/powershell/module/exchange/get-dlpsensitiveinformationtype) cmdlet to find it:

    ```powershell
    Get-DlpSensitiveInformationTypeRulePackage
    ```

    Note

    The built-in rule package that contains the built-in sensitive information types is named *Microsoft Rule Package*. The rule package that contains the custom sensitive information types that you created in the Compliance center UI is named *Microsoft.SCCManaged.CustomRulePack*.
2. Use the [Get-DlpSensitiveInformationTypeRulePackage](/en-us/powershell/module/exchange/get-dlpsensitiveinformationtyperulepackage) cmdlet to store the custom rule package to a variable:

    ```powershell
    $rulepak = Get-DlpSensitiveInformationTypeRulePackage -Identity "RulePackageName"
    ```

    For example, if the name of the rule package is "Employee ID Custom Rule Pack", run the following cmdlet:

    ```powershell
    $rulepak = Get-DlpSensitiveInformationTypeRulePackage -Identity "Employee ID Custom Rule Pack"
    ```
3. Use the following syntax to export the custom rule package to an XML file:

    ```powershell
    [System.IO.File]::WriteAllBytes('XMLFileAndPath', $rulepak.SerializedClassificationRuleCollection)
    ```

    This example exports the rule package to the file named ExportedRulePackage.xml in the C:\My Documents folder.

    ```powershell
    [System.IO.File]::WriteAllBytes('C:\My Documents\ExportedRulePackage.xml', $rulepak.SerializedClassificationRuleCollection)
    ```

## Step 2: Modify the sensitive information type in the exported XML file

For XML schema details and editing guidance, see [Customize a built-in sensitive information type](sit-customize-a-built-in-sensitive-information-type).

## Step 3: Import the updated XML file back into the existing rule package

To import the updated XML back into the existing rule package, use the [Set-DlpSensitiveInformationTypeRulePackage](/en-us/powershell/module/exchange/set-dlpsensitiveinformationtyperulepackage) cmdlet:

```powershell
Set-DlpSensitiveInformationTypeRulePackage -FileData ([System.IO.File]::ReadAllBytes('C:\My Documents\External Sensitive Info Type Rule Collection.xml'))
```

For detailed syntax and parameter information, see [Set-DlpSensitiveInformationTypeRulePackage](/en-us/powershell/module/exchange/set-dlpsensitiveinformationtyperulepackage).