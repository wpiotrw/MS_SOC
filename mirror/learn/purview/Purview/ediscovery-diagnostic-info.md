---
layout: Conceptual
title: Collect eDiscovery diagnostic information | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-diagnostic-info
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about how to collect eDiscovery diagnostic information for a Microsoft Support case.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
ms.custom:
- seo-marvel-apr2020
- admindeeplinkCOMPLIANCE
locale: en-us
document_id: 42eab27f-8eed-e5ee-2d68-5307f3e0185b
document_version_independent_id: 42eab27f-8eed-e5ee-2d68-5307f3e0185b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-diagnostic-info.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-diagnostic-info
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-diagnostic-info.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 164b97de-9016-8cd6-df7b-ffeefbce3ad8
---

# Collect eDiscovery diagnostic information | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Occasionally Microsoft Support engineers require specific information about your issue when you open a support case related to Microsoft Purview eDiscovery (Standard) or Microsoft Purview eDiscovery (Premium). This article provides guidance on how to collect diagnostic information to help support engineers investigate and resolve issues. Typically, you don't need to collect this information until asked to do so by a Microsoft Support engineer.

Important

The output from the cmdlets and diagnostic information described in this article may include sensitive information about litigation or internal investigations in your organization. Before sending the raw diagnostic information to Microsoft Support, you should review the information and redact any sensitive information (such as names or other information about parties to litigation or investigation) by replacing it with `XXXXXXX`. Using this method will also indicate to the Microsoft Support engineer that information was redacted.

## Collect diagnostic information for eDiscovery (Standard)

Collecting diagnostic information for eDiscovery (Standard) is cmdlet-based, so you'll have to use Security & Compliance PowerShell. The following PowerShell examples will run cmdlets and then save the output to a specified text file. In most support cases, you should only have to run one of these commands.

To run the following cmdlets, [connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell). After you're connected, run one or more of the following commands and be sure to replace placeholders with the actual object names.

After reviewing the generated text file and redacting sensitive information, send it to the Microsoft Support engineer working on your case.

Note

You can also run the commands in this section to collect diagnostic information for the searches and exports listed on the **Content search** page in the Microsoft Purview portal.

### Collect information about searches

The following command collects information that's helpful when investigating issues with a Content search or a search associated with an eDiscovery (Standard) case.

```powershell
Get-ComplianceSearch "<Search name>" | FL > "ComplianceSearch.txt"
```

### Collect information about search actions

The following command collects information to investigate problems with previewing, exporting, or purging the results of a Content search or a search associated with an eDiscovery (Standard) case. You can identify the name of the search action by selecting an export that's listed on the **Exports** tab. To identify the names of preview and purge actions, you can run the **Get-ComplianceSearchAction** cmdlet to display a list of all actions. The format for the search action name is constructed by appending `_Preview`, `_Export`, or `_Purge` to the name of the corresponding search.

```powershell
Get-ComplianceSearchAction "<Search action name>" | FL > "ComplianceSearchAction.txt"
```

### Collect information about eDiscovery holds

When an eDiscovery hold associated with an eDiscovery (Standard) case isn't functioning as expected, run the following command to collect information about the Case Hold Policy and associated Case Hold Rule for the eDiscovery hold. The *Case hold policy name* in the following command is the same as the name of the eDiscovery hold. You can identify this name on the **Holds** tabs in the eDiscovery (Standard) case.

```powershell
Get-CaseHoldPolicy "<Case hold policy name>" | %{"--CaseHoldPolicy--";$_|FL;"--CaseHoldRule--";Get-CaseHoldRule -Policy $_.Name | FL} > "eDiscoveryCaseHold.txt"
```

### Collect all case information

Sometimes, it's not apparent what information is required by Microsoft Support to investigate your issue. In this situation, you can collect all of the diagnostics information for an eDiscovery (Standard) case. The *eDiscovery (Standard) case name* in the following command is the same as the name of a case that's displayed on the **eDiscovery (Standard)** page in the Microsoft Purview portal.

```powershell
Get-ComplianceCase "<eDiscovery (Standard) case name>"| %{$_|fl;"`t==Searches==";Get-ComplianceSearch -Case $_.Name | FL;"`t==Search Actions==";Get-ComplianceSearchAction -Case $_.Name |FL;"`t==Holds==";Get-CaseHoldPolicy -Case $_.Name | %{$_|FL;"`t`t ==$($_.Name) Rules==";Get-CaseHoldRule -Policy $_.Name | FL}} > "eDiscoveryCase.txt"
```

## Collect diagnostic information for eDiscovery (Premium)

### Collect case information

The **Settings** tab in an eDiscovery (Premium) case lets you quickly copy the diagnostic information for the case. The diagnostic information is saved to the clipboard so you can paste it to a text file and send to Microsoft Support.

1. Go to the Microsoft Purview portal, and select **eDiscovery** &gt; [**Advanced**](https://go.microsoft.com/fwlink/p/?linkid=2174006).
2. Select a case and then select the **Settings** tab.
3. Under **Case Information**, select **Select**.
4. On the flyout page, select **Actions** &gt; **Copy support information** to copy the information to the clipboard.
5. Open a text file (in Notepad) and then paste the information in the text file.
6. Save the text file and name it something like `eDP Diagnostic Info YYYY.MM.DD` (for example, `eDP Diagnostic Info 2020.11.03`).

After reviewing the file and redacting sensitive information, send it to the Microsoft Support engineer working on your case.

### Collect job information

1. While in a case, select the **Jobs** tab.
2. Scroll down to the Job that failed and select it to open the job information pane.
3. Select **Copy support information** to copy the job diagnostics information to the clipboard.
4. Open a text file (in Notepad) and then paste the information into the text file.
5. Save the text file and name it something like `eDP Job Diagnostic Info YYYY.MM.DD` (for example, `eDP Diagnostic Info 2020.11.03`).

After reviewing the file and redacting sensitive information, send it to the Microsoft Support engineer working on your case.