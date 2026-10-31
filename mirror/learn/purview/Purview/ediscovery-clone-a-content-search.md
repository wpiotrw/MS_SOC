---
layout: Conceptual
title: Clone a Content Search | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-clone-a-content-search
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use the PowerShell script in this article to quickly clone an existing Content Search in the Microsoft Purview portal in Microsoft 365.
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
search.appverid:
- MOE150
- MED150
- MET150
ms.custom:
- seo-marvel-apr2020
ms.collection:
- purview-compliance
- content-search
locale: en-us
document_id: ee584883-0f4c-778e-9179-f37e9684d9c8
document_version_independent_id: ee584883-0f4c-778e-9179-f37e9684d9c8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-clone-a-content-search.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-clone-a-content-search
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-clone-a-content-search.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 7aae6aa2-fcd2-9507-888f-bd0e8e3c2c64
---

# Clone a Content Search | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Creating a Content Search in the Microsoft Purview portal in Microsoft 365 that searches many mailboxes or SharePoint and OneDrive for Business sites can take a while. Specifying the sites to search can also be prone to errors if you mistype a URL. To avoid these issues, you can use the Windows PowerShell script in this article to quickly clone an existing Content Search. When you clone a search, a new search (with a different name) is created that contains the same properties (such as the content locations and the search query) as the original search. Then you can edit the new search by changing the keyword query or the date range, and run it.

Why clone Content Searches?

- To compare the results of different keyword search queries run on the same content locations.
- To save you from having to reenter a large number of content locations when you create a new search.
- To decrease the size of the search results. For example, if you have a search that returns too many results to export, you can clone the search and then add a search condition based on a date range to reduce the number of search results.

## Script information

- You need to install the Exchange Online PowerShell module. For instructions, see [Install and maintain the Exchange Online PowerShell module](/en-us/powershell/exchange/exchange-online-powershell-v2#install-and-maintain-the-exchange-online-powershell-module).
- You have to be a member of the eDiscovery Manager role group in the Microsoft Purview portal to run the script described in this topic.
- The script includes minimal error handling. The primary purpose of the script is to quickly clone a content search.
- The script creates a new Content Search, but doesn't start it.
- This script takes into account whether the Content Search that you're cloning is associated with an eDiscovery case. If the search is associated with a case, the new search will also be associated with the same case. If the existing search isn't associated with a case, the new search will be listed on the **Content search** page in the Microsoft Purview portal.
- The sample script provided in this topic isn't supported under any Microsoft standard support program or service. The sample script is provided AS IS without warranty of any kind. Microsoft further disclaims all implied warranties including, without limitation, any implied warranties of merchantability or of fitness for a particular purpose. The entire risk arising out of the use or performance of the sample script and documentation remains with you. In no event shall Microsoft, its authors, or anyone else involved in the creation, production, or delivery of the scripts be liable for any damages whatsoever (including, without limitation, damages for loss of business profits, business interruption, loss of business information, or other pecuniary loss) arising out of the use of or inability to use the sample scripts or documentation, even if Microsoft has been advised of the possibility of such damages.

## Step 1: Run the script to clone a search

The script in this step will create a new Content Search by cloning an existing one. When you run this script, you'll be prompted for the following information:

- **Your user credentials** - The script will use your credentials to connect to Security & Compliance PowerShell. As previously stated, you have to be a member of the eDiscovery Manager role group in the Microsoft Purview portal to run the script.
- **The name of the existing search** - This is the Content Search that you want to clone.
- **The name of the new search that will be created** - If you leave this value blank, the script will create a name for the new search that is based on the name of the search that you're cloning.

To clone a search:

1. Save the following text to a Windows PowerShell script file by using a filename suffix of .ps1; for example, `CloneSearch.ps1`.

    ```powershell
    # This PowerShell script clones an existing content search in Microsoft Purview compliance.
    
    # Ask for the name of the search you want to clone
    $searchName = Read-Host 'Enter the name of the search that you want to clone'
    # Ask for the name of the new search
    $newSearchName = Read-Host 'Enter a name for the new search [leave blank to automatically generate a name]'
    $originalSearch = Get-ComplianceSearch $searchName -EA SilentlyContinue
    # Make sure we have a valid search before continuing
    if(!$originalSearch)
    {
        Write-Error "Couldn't find search: $searchName"
        return
    }
    $searchNameCounter = 1
    # Find a suitable name for the new search
    while(!$newSearchName)
    {
        $newSearchName = $originalSearch.Name + "_" + $searchNameCounter
        $tempSearch = Get-ComplianceSearch $newSearchName -EA SilentlyContinue
        if ($tempSearch)
        {
            $newSearchName = $null
            $searchNameCounter++
        }
    }
    $caseName
    # Determine if the search is part of a case; if so get the case name
    if ($originalSearch.CaseId)
    {
        $searchCase = Get-ComplianceCase $originalSearch.CaseId
        $caseName = $searchCase.Name
    }
    # Need to cast this value as a Boolean the old fashion way
    $allowNotFoundExchangeLocationsEnabled = $false
    if ($originalSearch.AllowNotFoundExchangeLocationsEnabled)
    {
        $allowNotFoundExchangeLocationsEnabled = $true
    }
    $newSearch = New-ComplianceSearch -Name $newSearchName -AllowNotFoundExchangeLocationsEnabled $allowNotFoundExchangeLocationsEnabled -Case $caseName -ContentMatchQuery $originalSearch.ContentMatchQuery -Description $originalSearch.Description -ExchangeLocation $originalSearch.ExchangeLocation -ExchangeLocationExclusion $originalSearch.ExchangeLocationExclusion -Language $originalSearch.Language -SharePointLocation $originalSearch.SharePointLocation -SharePointLocationExclusion $originalSearch.SharePointLocationExclusion -PublicFolderLocation $originalSearch.PublicFolderLocation
    if ($newSearch)
    {
        Write-Host $newSearch.Name "was successfully created" -ForegroundColor Yellow
    }
    ```
2. [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell). In the same PowerShell window, go to the folder where you saved the script.
3. Run the script; for example:

    ```powershell
    .\CloneSearch.ps1
    ```
4. Enter following information when prompted by the script. Type each piece of information and then press **Enter**.

    - The name of the existing search.
    - The name of the new search.

    The script creates the new Content Search, but doesn't start it. This gives you a chance to edit and run the search in the next step. You can view the properties of the new search by running the **Get-ComplianceSearch** cmdlet or by going to the **Content search** or **eDiscovery** page in the Microsoft Purview portal, depending on whether the new search is associated with a case.

## Step 2: Edit and run the cloned search in the Microsoft Purview portal

After you run the script to clone an existing Content Search, the next step is to go to the Microsoft Purview portal to edit and run the new search. As previously stated, you can edit a search by changing the keyword search query and adding or removing search conditions. For more information, see:

- [Content Search in Office 365](ediscovery-content-search)
- [Keyword queries and search conditions for Content Search](ediscovery-keyword-queries-and-search-conditions)
- [eDiscovery cases](ediscovery-standard-get-started)