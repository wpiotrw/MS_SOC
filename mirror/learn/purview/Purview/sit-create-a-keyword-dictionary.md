---
layout: Conceptual
title: Create a keyword dictionary | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-create-a-keyword-dictionary
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
ms.custom: seo-marvel-apr2020, admindeeplinkCOMPLIANCE, msecd-doc-authoring-1014
description: Learn the basic steps to creating a keyword dictionary.
ai-usage: ai-assisted
locale: en-us
document_id: 6b7a4e77-4484-51af-7d68-99cab3aef10c
document_version_independent_id: 6b7a4e77-4484-51af-7d68-99cab3aef10c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-create-a-keyword-dictionary.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-create-a-keyword-dictionary
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-create-a-keyword-dictionary.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
platformId: cb31ed69-e1df-1bf5-d4b8-506a3fda01c0
---

# Create a keyword dictionary | Microsoft Learn

Microsoft Purview can identify, monitor, and protect your sensitive items. Identifying sensitive items sometimes requires looking for keywords, particularly when identifying generic content (such as healthcare-related communication), or inappropriate or explicit language. Although you can create keyword lists when you [create custom sensitive information types](sit-create-a-custom-sensitive-information-type#create-custom-sensitive-information-types), keyword lists are limited in size and if you're [creating custom sensitive information types in PowerShell](sit-create-a-custom-sensitive-information-type-in-scc-powershell), require modifying XML to create or edit them.

In contrast, keyword dictionaries provide simpler management of keywords and at a larger scale, supporting up to 1 MB of terms (post-compression) in the dictionary. Additionally, keyword dictionaries can support any language. The tenant limit is also 1 MB after compression. A post-compression limit of 1 MB means that all dictionaries combined across a tenant can have close to one million characters.

## Keyword dictionary limits

You can create keyword dictionary, subject to a combined size limit of 1MB (post compression) per tenant. To find out how many keyword dictionaries you have in your tenant, [connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell) and then run this PowerShell script:

```powershell
$rawFile = $env:TEMP + "\rule.xml"

$kd = Get-DlpKeywordDictionary
$ruleCollections = Get-DlpSensitiveInformationTypeRulePackage
[System.IO.File]::WriteAllBytes((Resolve-Path $rawFile), $ruleCollections.SerializedClassificationRuleCollection)
$UnicodeEncoding = New-Object System.Text.UnicodeEncoding
$FileContent = [System.IO.File]::ReadAllText((Resolve-Path $rawFile), $unicodeEncoding)

if($kd.Count -gt 0)
{
$count = 0
$entities = $FileContent -split "Entity id"
for($j=1;$j -lt $entities.Count;$j++)
{
for($i=0;$i -lt $kd.Count;$i++)
{
$Matches = Select-String -InputObject $entities[$j] -Pattern $kd[$i].Identity -AllMatches
$count = $Matches.Matches.Count + $count
if($Matches.Matches.Count -gt 0) {break}
}
}

Write-Output "Total Keyword Dictionary SIT:"
$count
}
else
{
$Matches = Select-String -InputObject $FileContent -Pattern $kd.Identity -AllMatches
Write-Output "Total Keyword Dictionary SIT:"
$Matches.Matches.Count
}

Remove-Item $rawFile
```

## Basic steps to creating a keyword dictionary

Most commonly you compile your keywords for your dictionary in a file, such as a .csv or .txt list. You upload the dictionary file into a SIT during creation or editing or import them via a PowerShell cmdlet. Alternatively, you can start from an existing keyword dictionary. Lastly, you can enter keywords manually in the **Add keyword dictionary** dialog. When you create a keyword dictionary, you follow the same core steps:

## Create a keyword dictionary using the Microsoft Purview portal

Use these steps to create or import keywords for a custom dictionary:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com)**Information Protection** &gt; **Classifiers** &gt; **Sensitive info types**.
2. Select **+ Create sensitive info type** and then enter a **Name** and **Description** for your sensitive info type. Choose **Next**.
3. On the **Define patterns for this sensitive info type** page, choose **+ Create pattern**.
4. In the **New pattern** window, select a **Confidence level**.
5. Choose **Add a Primary element** and select **Keyword dictionary**.
6. On the **Add a keyword dictionary** flyout, you can:

    1. **Upload a dictionary** file in **TXT** or **CSV** format.
    2. **Choose from existing dictionaries**.
    3. or create a new dictionary by entering keywords manually and giving it a name.
7. Still in the **New Pattern** window, for **Character proximity**, specify how far away (in number of characters) that any supporting elements must be to be detected. The closer the primary and supporting elements are to each other, the more likely the detected content is going to be what you're looking for.
8. Add the **Supporting elements** you wish to use to increase the accuracy of detecting what you're looking for.
9. Add any **Additional checks** and then choose **Create**.
10. Choose **Next** to continue creating your sensitive information type. When you're finished, choose **Done**.

## Create a keyword dictionary from a file using PowerShell

Often when you need to create a large dictionary, it's so you can use keywords from a file or a list exported from some other source. This procedure creates a keyword dictionary containing a list of diseases to screen in external email. To begin, you need to [connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).

1. Copy your keywords into a text file and make sure that each keyword is on a separate line.
2. Save the text file with Unicode encoding. In Notepad, navigate to &gt; **Save As** &gt; **Encoding** &gt; **Unicode**.
3. Read the file into a variable by running this cmdlet:

    ```powershell
    $fileData = [System.IO.File]::ReadAllBytes('<filename>')
    ```
4. Create the dictionary by running this cmdlet:

    ```powershell
    New-DlpKeywordDictionary -Name <name> -Description <description> -FileData $fileData
    ```

## Using keyword dictionaries in custom sensitive information types and DLP policies

Keyword dictionaries can be used as part of the match requirements for a custom sensitive information type, or as a sensitive information type themselves. Both require you to create a [custom sensitive information type using PowerShell](sit-create-a-custom-sensitive-information-type-in-scc-powershell). Follow the instructions in [Create a custom sensitive information type using PowerShell](sit-create-a-custom-sensitive-information-type-in-scc-powershell) to create a sensitive information type. Once you have the XML, you need the GUID identifier from the XML in order to use the keyword dictionary.

```xml
<Entity id="00aa00aa-bb11-cc22-dd33-44ee44ee44ee" patternsProximity="300" recommendedConfidence="75">
    <Pattern confidenceLevel="75">
        <IdMatch idRef=". . ."/>
    </Pattern>
</Entity>
```

To get the identity of your dictionary, run this command and copy the **Identity** property value:

```powershell
Get-DlpKeywordDictionary -Name "Diseases"
```

The output of the command looks like this:

`RunspaceId        : 138e55e7-ea1e-4f7a-b824-79f2c4252255``Identity          : 8d2d44b0-91f4-41f2-94e0-21c1c5b5fc9f``Name              : Diseases``Description       : Names of diseases and injuries from ICD-10-CM lexicon``KeywordDictionary : aarskog's syndrome, abandonment, abasia, abderhalden-kaufmann-lignac, abdominalgia, abduction contracture, abetalipo``proteinemia, abiotrophy, ablatio, ablation, ablepharia,abocclusion, abolition, aborter, abortion, abortus, aboulomania,``abrami's disease, abramo``IsValid           : True``ObjectState       : Unchanged`

Paste the **identity** value into the XML for your custom sensitive information type as the **idRef**. Next, upload the XML file. Your dictionary now appears in your list of sensitive information types and you can use it right in your policy, specifying how many keywords are required to match.

```xml
<Entity id="11bb11bb-cc22-dd33-ee44-55ff55ff55ff" patternsProximity="300" recommendedConfidence="85">
      <Pattern confidenceLevel="85">
        <IdMatch idRef="8d2d44b0-91f4-41f2-94e0-21c1c5b5fc9f" />
      </Pattern>
    </Entity>
    <LocalizedStrings>
      <Resource idRef="11bb11bb-cc22-dd33-ee44-55ff55ff55ff">
        <Name default="true" langcode="en-us">Diseases</Name>
        <Description default="true" langcode="en-us">Detects various diseases</Description>
      </Resource>
    </LocalizedStrings>
```

Note

Microsoft 365 Information Protection supports double-byte character set languages for:

- Chinese (simplified)
- Chinese (traditional)
- Korean
- Japanese

This support is available for sensitive information types. See, [Information protection support for double byte character sets release notes (preview)](mip-dbcs-relnotes) for more information.

Tip

To detect patterns containing Chinese/Japanese characters and single byte characters or to detect patterns containing Chinese/Japanese and English, define two variants of the keyword or regex.

- For example, to detect a keyword like "机密的document", use two variants of the keyword; one with a space between the Japanese and English text and another without a space between the Japanese and English text. So, the keywords to be added in the SIT should be "机密的 document" and "机密的document". Similarly, to detect a phrase "東京オリンピック2020", two variants should be used; "東京オリンピック 2020" and "東京オリンピック2020".

Along with Chinese/Japanese/double byte characters, if the list of keywords/phrases also contains non-Chinese/Japanese words also (for instance, stand-alone English words), you should create two dictionaries/keyword lists. One for keywords containing Chinese/Japanese/double byte characters and another one for English words.

- For example, if you want to create a keyword dictionary/list with three phrases "Highly confidential", "機密性が高い" and "机密的document", you should create two keyword lists.
    1. Highly confidential
    2. 機密性が高い, 机密的document and 机密的 document

While creating a regex using a double byte hyphen or a double byte period, make sure to escape both the characters like one would escape a hyphen or period in a regex. Here's a sample regex for reference:

- `(?<!\d)([4][0-9]{3}[\-?\-\t]*[0-9]{4}`

We recommend using a string match instead of a word match in a keyword list.