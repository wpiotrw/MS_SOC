---
layout: Conceptual
title: Use Content Search for a list of users on the mailbox & OneDrive site | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-search-mailboxes-and-onedrive-for-users
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use Content Search and the script in this article to search the mailboxes and OneDrive sites for a group of users.
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
- content-search
search.appverid:
- MOE150
- MET150
ms.custom:
- seo-marvel-apr2020
- sfi-ga-nochange
locale: en-us
document_id: f14694c9-bbd6-485d-db32-1cbc858b5ed7
document_version_independent_id: f14694c9-bbd6-485d-db32-1cbc858b5ed7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-search-mailboxes-and-onedrive-for-users.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-search-mailboxes-and-onedrive-for-users
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-search-mailboxes-and-onedrive-for-users.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: d4f90b66-d2a9-8761-6000-748975608b18
---

# Use Content Search for a list of users on the mailbox & OneDrive site | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Security & Compliance PowerShell provides numerous cmdlets that let you automate time-consuming eDiscovery-related tasks. Currently, creating a Content search in the Microsoft Purview portal to search a large number of custodian content locations takes time and preparation. Before you create a search, you have to collect the URL for each OneDrive site and then add each mailbox and OneDrive site to the search. This script prompts you for the name of your organization's MySite domain (for example, **contoso** in the URL `https://contoso-my.sharepoint.com`), a list of user email addresses, the name of the new Content Search, and the search query to use. The script gets the OneDrive URL for each user in the list, and then it creates and starts a Content Search that searches the mailbox and OneDrive site for each user in the list, using the search query that you provide.

## Permissions and script information

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

- You have to be a member of the eDiscovery Manager role group in the Microsoft Purview portal or the Microsoft Purview portal and a SharePoint global administrator to run the script in Step 3.
- Be sure to save the list of users that you create in Step 2 and the script in Step 3 to the same folder. This makes it easier to run the script.
- The script includes minimal error handling. Its primary purpose is to quickly and easily search the mailbox and OneDrive site of each user.
- The sample scripts provided in this article aren't supported under any Microsoft standard support program or service. The sample scripts are provided AS IS without warranty of any kind. Microsoft further disclaims all implied warranties including, without limitation, any implied warranties of merchantability or of fitness for a particular purpose. The entire risk arising out of the use or performance of the sample scripts and documentation remains with you. In no event shall Microsoft, its authors, or anyone else involved in the creation, production, or delivery of the scripts be liable for any damages whatsoever (including, without limitation, damages for loss of business profits, business interruption, loss of business information, or other pecuniary loss) arising out of the use of or inability to use the sample scripts or documentation, even if Microsoft has been advised of the possibility of such damages.

## Step 1: Install the SharePoint Management Shell

The first step is to install the SharePoint Management Shell. You don't have to use the shell in this procedure, but you have to install it because it contains prerequisites required by the script that you run in Step 3. These prerequisites allow the script to communicate with SharePoint to get the URLs for the OneDrive sites.

Go to [Set up the SharePoint Management Shell environment](/en-us/powershell/sharepoint/sharepoint-online/connect-sharepoint-online) and perform Step 1 and Step 2 to install the SharePoint Management Shell.

## Step 2: Generate a list of users

The script in Step 3 will create a Content Search to search the mailboxes and OneDrive accounts for a list of users. You can just type the email addresses in a text file, or you can run a command in PowerShell to get a list of email addresses and save them to a file (located in same folder that you'll save the script to in Step 3).

Here's an [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell) command that you can run to get a list of email addresses for all users in your organization and save it to a text file named `Users.txt`.

```powershell
Get-Mailbox -ResultSize unlimited -Filter { RecipientTypeDetails -eq 'UserMailbox'} | Select-Object PrimarySmtpAddress > Users.txt
```

After you run this command, be sure to open the file and remove the header that contains the property name, `PrimarySmtpAddress`. The text file should just contain a list of email addresses, and nothing else. Make sure there are no blank rows before or after the list of email addresses.

## Step 3: Run the script to create and start the search

When you run the script in this step, it prompts you for the following information. Be sure to have this information ready before you run the script.

- **Your user credentials** - The script uses your credentials to access SharePoint to get the OneDrive URLs and to connect to Security & Compliance PowerShell.
- **Name of your MySite domain** - The MySite domain is the domain that contains all the OneDrive sites in your organization. For example, if the URL for your MySite domain is **`https://contoso-my.sharepoint.com`**, then you would enter `contoso` when the script prompts you for the name of your MySite domain.
- **Pathname of the text file from Step 2** - The pathname of the text file that you created in Step 2. If the text file and the script are located in the same folder, then enter the name of the text file. Otherwise, enter the complete pathname for the text file.
- **Name of the Content Search** - The name of the Content Search that will be created by the script.
- **Search query** - The search query that is used with the Content Search is created and run. For more information about search queries, see [Keyword queries and search conditions for eDiscovery](ediscovery-keyword-queries-and-search-conditions).

**To run the script:**

1. Save the following text to a Windows PowerShell script file by using a filename suffix of .ps1; for example, `SearchEXOOD4B.ps1`. Save the file to the same folder where you saved the list of users in Step 2.

    ```powershell
    # This PowerShell script will prompt you for the following information:
    #    * Your user credentials
    #    * The name of your organization's MySite domain
    #    * The pathname for the text file that contains a list of user email addresses
    #    * The name of the Content Search created
    #    * The search query string
    # The script will then:
    #    * Find the OneDrive site for each user in the text file
    #    * Create and start a Content Search using the previous information
    # Get user credentials
    if (!$credentials)
    {
        $credentials = Get-Credential
    }
    # Get the user's MySite domain name.  We use this to create the admin URL and root URL for OneDrive
    $mySiteDomain = Read-Host "What is your organization's MySite domain?  For example,  'contoso' for 'https://contoso-my.sharepoint.com'"
    $AdminUrl = "https://$mySiteDomain-admin.sharepoint.com"
    $mySiteUrlRoot = "https://$mySiteDomain-my.sharepoint.com"
    # Get other required information
    $inputfile = read-host "Enter the file name of the text file that contains the email addresses for the users you want to search"
    $searchName = Read-Host "Enter the name for the new search"
    $searchQuery = Read-Host "Enter the search query you want to use"
    $emailAddresses = Get-Content $inputfile | where {$_ -ne ""}  | foreach{ $_.Trim() }
    # Connect to Security & Compliance PowerShell
    if (!$s -or !$a)
    {
        Import-Module ExchangeOnlineManagement
        Connect-IPPSSession
    }
    
    # Load the SharePoint assemblies from the SharePoint Management Shell
    # To install, go to https://go.microsoft.com/fwlink/p/?LinkId=255251
    if (!$SharePointClient -or !$SPRuntime -or !$SPUserProfile)
    {
        $SharePointClient = [System.Reflection.Assembly]::LoadWithPartialName("Microsoft.SharePoint.Client")
        $SPRuntime = [System.Reflection.Assembly]::LoadWithPartialName("Microsoft.SharePoint.Client.Runtime")
        $SPUserProfile = [System.Reflection.Assembly]::LoadWithPartialName("Microsoft.SharePoint.Client.UserProfiles")
        if (!$SharePointClient)
        {
            Write-Error "SharePoint Management Shell isn't installed, please install from: https://go.microsoft.com/fwlink/p/?LinkId=255251 and then run this script again"
            return;
        }
    }
    if (!$spCreds)
    {
        $spCreds = New-Object Microsoft.SharePoint.Client.SharePointOnlineCredentials($credentials.UserName, $credentials.Password)
    }
    # Add the path of the User Profile Service to the SPO admin URL, then create a new webservice proxy to access it
    $proxyaddr = "$AdminUrl/_vti_bin/UserProfileService.asmx?wsdl"
    $UserProfileService= New-WebServiceProxy -Uri $proxyaddr -UseDefaultCredential False
    $UserProfileService.Credentials = $credentials
    # Take care of auth cookies
    $strAuthCookie = $spCreds.GetAuthenticationCookie($AdminUrl)
    $uri = New-Object System.Uri($AdminUrl)
    $container = New-Object System.Net.CookieContainer
    $container.SetCookies($uri, $strAuthCookie)
    $UserProfileService.CookieContainer = $container
    Write-Host "Getting each user's OneDrive URL"
    $urls = @()
    foreach($emailAddress in $emailAddresses)
    {
        try
        {
            $prop = $UserProfileService.GetUserProfileByName("i:0#.f|membership|$emailAddress") | Where-Object { $_.Name -eq "PersonalSpace" }
            $url = $prop.values[0].value
            $furl = $mySiteUrlRoot + $url
            $urls += $furl
            Write-Host "-$emailAddress => $furl"
        }
        catch
        {
            Write-Warning "Could not locate OneDrive for $emailAddress"
        }
    }
    Write-Host "Creating and starting the search"
    $search = New-ComplianceSearch -Name $searchName -ExchangeLocation $emailAddresses -SharePointLocation $urls -ContentMatchQuery $searchQuery
    # Finally, start the search and then display the status
    if($search)
    {
        Start-ComplianceSearch $search.Name
        Get-ComplianceSearch $search.Name
    }
    ```
2. Open Windows PowerShell and go to the folder where you saved the script and the list of users from Step 2.
3. Start the script; for example:

    ```powershell
    .\SearchEXOOD4B.ps1
    ```
4. When prompted for your credentials, enter your email address and password, and then select **OK**.
5. Enter following information when prompted by the script. Type each piece of information and then press **Enter**.

    - The name of your MySite domain.
    - The pathname of the text file that contains the list of users.
    - A name for the Content Search.
    - The search query (leave this blank to return all items in the content locations).

    The script gets the URLs for each OneDrive site and then creates and starts the search. You can either run the **Get-ComplianceSearch** cmdlet in Security & Compliance PowerShell to display the search statistics and results, or you can go to the **Content search** page in the Microsoft Purview portal to view information about the search.