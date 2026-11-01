---
layout: Conceptual
title: Modify a keyword dictionary | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-modify-keyword-dictionary
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
ms.custom: seo-marvel-apr2020, msecd-doc-authoring-1014
description: Learn how to modify a keyword dictionary.
ai-usage: ai-assisted
locale: en-us
document_id: da91f5ef-761f-2744-92cb-5b01c2e52f69
document_version_independent_id: da91f5ef-761f-2744-92cb-5b01c2e52f69
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-modify-keyword-dictionary.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-modify-keyword-dictionary
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-modify-keyword-dictionary.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 0ba5bbcb-d49c-c3d3-3e9c-75ffad6cd1bf
---

# Modify a keyword dictionary | Microsoft Learn

This article explains how to modify keywords in custom or built-in keyword dictionaries used by sensitive information types (SITs) in Microsoft Purview. You can modify a keyword dictionary by using the Microsoft Purview portal or PowerShell.

## Modify a keyword dictionary in the portals

Keyword dictionaries can be used as **Primary elements** or **Supporting elements** in sensitive information type (SIT) patterns. You can edit a keyword dictionary while creating a SIT or in an existing custom SIT. For example to edit an existing keyword dictionary:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Information Protection** &gt; **Classifiers** &gt; **Sensitive info types**.
2. Choose the SIT that uses the keyword dictionary you want to update.
3. Select **Edit**.
4. Choose **Next**.
5. **Edit** the pattern that has the keyword dictionary you want to update.
6. Edit the keyword dictionary in the **Primary element** or the **Supporting element** sections. Make your edits, using one keyword per line.

    ![Screenshot of the keyword dictionary editor showing keyword entries listed one per line for editing in a sensitive information type pattern.](media/edit-keyword-dictionary.png)
7. Choose **Done**.

## Modify a keyword dictionary using PowerShell

For example, we'll modify some terms in PowerShell, save the terms locally where you can modify them in an editor, and then update the previous terms in place.

First, retrieve the dictionary object:

```powershell
$dict = Get-DlpKeywordDictionary -Name "Diseases"
```

Printing `$dict` will show the various properties. The keywords themselves are stored in an object on the backend, but `$dict.KeywordDictionary` contains a string representation of them, which you'll use to modify the dictionary.

Before you modify the dictionary, you need to turn the string of terms back into an array using the `.split(',')` method. Then you'll clean up the unwanted spaces between the keywords with the `.trim()` method, leaving just the keywords to work with.

```powershell
$terms = $dict.KeywordDictionary.split(',').trim()
```

Now you'll remove some terms from the dictionary. Because the example dictionary has only a few keywords, you could as easily skip to exporting the dictionary and editing it in Notepad, but dictionaries generally contain a large amount of text, so you'll first learn this way to edit them easily in PowerShell.

In the previous command, you saved the keywords to the `$terms` array. There are several ways to [remove items from an array](/en-us/previous-versions/windows/it-pro/windows-powershell-1.0/ee692802%28v=technet.10%29), but as a straightforward approach, you'll create an array of the terms you want to remove from the dictionary, and then copy only the dictionary terms to it that aren't in the list of terms to remove.

Run the command `$terms` to show the current list of terms. The output of the command looks like this:

```powershell
aarskog's syndrome
abandonment
abasia
abderhalden-kaufmann-lignac
abdominalgia
abduction contracture
abetalipoproteinemia
abiotrophy
ablatio
ablation
ablepharia
abocclusion
abolition
aborter
abortion
abortus
aboulomania
abrami's disease
```

Run this command to specify the terms that you want to remove:

```powershell
$termsToRemove = @('abandonment','ablatio')
```

Run this command to actually remove the terms from the list:

```powershell
$updatedTerms = $terms | Where-Object {$_ -notin $termsToRemove}
```

Run the command `$updatedTerms` to show the updated list of terms. The output of the command looks like this (the specified terms have been removed):

```powershell
aarskog's syndrome
abasia
abderhalden-kaufmann-lignac
abdominalgia
abduction contracture
abetalipoproteinemia
abiotrophy
ablation
ablepharia
abocclusion
abolition
aborter
abortion
abortus
aboulomania
abrami's disease
```

Now save the dictionary locally and add a few more terms. You could add the terms right here in PowerShell, but you'll still need to export the file locally to ensure it's saved with Unicode encoding and contains the BOM.

Save the dictionary locally by running the following:

```powershell
Set-Content $updatedTerms -Path "C:\myPath\terms.txt"
```

Now open the file, add your other terms, and save with Unicode encoding (UTF-16). Now you'll upload the updated terms and update the dictionary in place.

```powershell
Set-DlpKeywordDictionary -Identity "Diseases" -FileData ([System.IO.File]::ReadAllBytes('C:myPath\terms.txt'))
```

Now the dictionary has been updated in place. The `Identity` field takes the name of the dictionary. If you wanted to also change the name of your dictionary using the `Set-` cmdlet, you would just need to add the `-Name` parameter to the `Set-DlpKeywordDictionary` command with your new dictionary name.