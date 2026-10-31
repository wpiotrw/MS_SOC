---
layout: Conceptual
title: Use Microsoft Purview APIs for eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-ref-api-guide
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about using Microsoft Purview APIs for eDiscovery tasks and workflows.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-05-06T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- SPO160
- MOE150
- MET150
ai-usage: ai-assisted
ms.custom: sfi-image-nochange
locale: en-us
document_id: d8de9a05-09c6-44ed-2df5-0bd9cb55bce2
document_version_independent_id: d8de9a05-09c6-44ed-2df5-0bd9cb55bce2
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-ref-api-guide.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-ref-api-guide
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-ref-api-guide.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: f43a19d0-da76-df87-c64f-e1fd370a1aed
---

# Use Microsoft Purview APIs for eDiscovery | Microsoft Learn

The [Microsoft Purview Application Programming Interface](/en-us/purview/developer/microsoft-purview-sdk-documentation-overview) (API) for [eDiscovery](edisc) in [Microsoft Graph](/en-us/graph/overview) enables your organization to automate repetitive tasks and integrate with your existing eDiscovery tools to build repeatable workflows that industry regulations might require. This article provides guidance on how to configure the required prerequisites to enable access to the Microsoft Purview APIs for eDiscovery. This guidance is based on using app-only access to the APIs, with either a client secret or a self-signed certificate to authenticate the requests.

## Microsoft Purview APIs

The Microsoft Purview APIs for eDiscovery include two separate APIs:

- **Microsoft Graph**: Part of the `Microsoft.Graph.Security` namespace and used for working with [eDiscovery cases](edisc-cases-manage).
- **Microsoft Purview eDiscovery API**: Used exclusively to programmatically download packages created when exporting from [searches](edisc-search-export) and [review sets](edisc-review-set-export) in eDiscovery.

eDiscovery APIs in Microsoft Graph support eDiscovery cases with and without [premium features enabled](edisc-settings-general). Delegated authentication supports [core eDiscovery capabilities](edisc#features-and-capabilities) such as cases, holds, searches, and exports. App-only authentication is available for cases with premium features enabled and supports advanced operations such as review sets, tagging, and analytics.

For a list of supported API calls within the Microsoft Graph calls, see [Use the Microsoft Purview eDiscovery API](/en-us/graph/api/resources/security-ediscovery-apioverview?view=graph-rest-1.0).

## Application access to data

Before you can make any calls to the Microsoft Purview APIs for eDiscovery, you must first register an app in the Microsoft Identity Platform, [Entra ID](/en-us/entra/fundamentals/what-is-entra).

An application can access data in two ways:

- **Delegated access**: An app acting on behalf of a signed-in user.
- **App-only access**: An app acting with its own identity.

For more information about access scenarios, see [Authentication and authorization basics](/en-us/graph/auth/auth-concepts).

Important

App-only authentication requires an eDiscovery case with premium features enabled. Delegated authentication is available for [core eDiscovery capabilities](edisc#features-and-capabilities) including cases, legal holds, searches, and exports. Premium API operations (review sets, tagging, analytics) require premium features enabled regardless of authentication method. For more information about subscription requirements, see [subscription requirements for eDiscovery](https://aka.ms/M365EnterprisePlans).

## Microsoft Graph API

### Prerequisites for Microsoft Graph API

Implementing app-only accessinvolves registering an app in Azure portal, creating client secret/certificates, assigning API permissions, setting up a service principal, and then using app-only access to call Microsoft Graph APIs. To register an app, create client secret/certificates and assign API permissions the account must be a [*Cloud Application Administrator*](/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator).

For more information about registering an app in the Azure portal, see [Register an application with the Microsoft identity platform](/en-us/entra/identity-platform/quickstart-register-app?tabs=certificate).

Granting tenant-wide admin consent for Microsoft Purview eDiscovery API application permissions requires you to sign in as a user that is authorized to consent on behalf of your organization. For more information, see [Grant tenant-wide admin consent to an application](/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal).

Setting up a service principal requires the following prerequisites:

- A machine with the [ExchangeOnlineManagement module](https://www.powershellgallery.com/packages/ExchangeOnlineManagement) installed.
- An account that has the *Role Management* role [assigned in Microsoft Purview](/en-us/defender-office-365/scc-permissions?toc=/purview/toc.json&amp;bc=/purview/breadcrumb/toc.json).

For detailed steps on implementing app-only access for eDiscovery, see [Set up app-only access for Microsoft Purview eDiscovery](/en-us/graph/security-ediscovery-appauthsetup).

### Connecting to Microsoft Graph API using app-only access

Use the [Connect-MgGraph](/en-us/powershell/module/microsoft.graph.authentication/connect-mggraph?view=graph-powershell-1.0) cmdlet in PowerShell to authenticate and connect to Microsoft Graph using the app-only access method. This cmdlet enables your app to interact with Microsoft Graph securely and enables you to explore the Microsoft Purview eDiscovery APIs.

#### Connecting via client secret

To connect using a client secret, update and run the following example PowerShell code.

```powershell
$clientSecret = "<client secret>" ## Update with client secret added to the registered app
$appID = "<APP ID>" ## Update with Application ID of registered/Enterprise app
$tenantId = "<Tenant ID>" ## Update with tenant ID
$ClientSecretPW = ConvertTo-SecureString "$clientSecret" -AsPlainText -Force
$clientSecretCred = New-Object System.Management.Automation.PSCredential -ArgumentList ("$appID", $clientSecretPW)
Connect-MgGraph -TenantId "$tenantId" -ClientSecretCredential $clientSecretCred
```

#### Connecting via certificate

To connect using a certificate, update and run the following example PowerShell code.

```powershell
$certPath = "Cert:\currentuser\my\<xxxxxxxxxx>" ## Update with the cert thumbnail
$appID = "<APP ID>" ## Update with Application ID of registered/Enterprise app
$tenantId = "<Tenant ID>" ## Update with tenant ID
$ClientCert = Get-ChildItem $certPath
Connect-MgGraph -TenantId $TenantId -ClientId $appId -Certificate $ClientCert
```

### Invoke Microsoft Graph API calls

After you connect, you can start making calls to the Microsoft Graph API.

For example, you can list the eDiscovery cases within the tenant by using the [ediscoveryCases](/en-us/graph/api/security-casesroot-list-ediscoverycases?view=graph-rest-beta&amp;tabs=http) API. The guidance for each operation lists the following information:

- Permissions required to make the API call
- HTTP request and method
- Request header and body information
- Response
- Examples (HTTP, C#, CLI, Go, Java, PHP, PowerShell, Python)

Because you're connected through the Microsoft Graph PowerShell module, you can use either the HTTP or PowerShell method.

First, let's look at the [PowerShell](/en-us/graph/api/security-casesroot-list-ediscoverycases?view=graph-rest-beta&amp;tabs=powershell#examples) example.

![PowerShell example for list of eDiscovery cases.](media/ediscovery-api-1.png)

As you can see, it returns a list of all the cases within the tenant. When delving deeper into a case, it's important to record the case *ID*. You need this ID for future API calls.

Now, let's look at an [HTTP](/en-us/graph/api/security-casesroot-list-ediscoverycases?view=graph-rest-beta&amp;tabs=http#examples) example. You use the [Invoke-MgGraphRequest](/en-us/powershell/module/microsoft.graph.authentication/invoke-mggraphrequest?view=graph-powershell-1.0) cmdlet to make the call by using PowerShell.

First, store the URL in a variable:

`$uri = "https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases"`

Then use the Invoke-MgGraphRequest cmdlet to make the API call.

```powershell
Invoke-MgGraphRequest -Method Get -Uri $uri
```

As you can see from the following output, you need to extract the values from the returned response.

![PowerShell example for URL output.](media/ediscovery-api-2.png)

You can save the *Value* elements of the response to a new variable by using the following command.

```powershell
$cases = (Invoke-MgGraphRequest -Method Get -Uri $uri).value
```

![PowerShell example for extracting URL.](media/ediscovery-api-3.png)

![PowerShell example for extracting URL for cases.](media/ediscovery-api-4.png)

This command returns a collection of hash tables. Optionally, you can run a small bit of PowerShell code to convert the hash tables into PowerShell objects for easier use with cmdlet parameters such as *format-table* and *format-list*.

```powershell
$CasesAsObjects = @()
foreach($i in $cases) {$CasesAsObjects += [pscustomobject]$i}
$CasesAsObjects | ft displayname,id,status
```

![PowerShell example to convert hash tables.](media/ediscovery-api-5.png)

## Microsoft Purview eDiscovery API

You can configure the Microsoft Purview eDiscovery API to enable the programmatic download of export packages and the reports from an export process in an eDiscovery case.

### Prerequisites for Microsoft Purview eDiscovery API

Before you execute the configuration steps in this section, complete and validate the configuration detailed in the Microsoft Graph API section. Extend the previously registered app in Microsoft Entra ID to include the required permissions to achieve programmatic download of the export package.

This configuration already provides the following prerequisites:

- Registered app in Azure portal configured with the appropriate client secret or certificate.
- Service principal in Microsoft Purview assigned the relevant eDiscovery roles.
- Microsoft eDiscovery API permissions configured for the Microsoft Graph.

To extend the existing registered app's API permissions to enable programmatic download, complete the following steps:

- Register a new Microsoft Application and service principal in the tenant.
- Assign additional API permissions to the previously registered app in the Azure portal.

To grant tenant-wide admin consent for Microsoft Purview eDiscovery APIs application permissions, sign in as a user that is authorized to consent on behalf of the organization. For more information, see [Grant tenant-wide admin consent to an application](/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal).

### Configuration steps

#### Step 1: Register the MicrosoftPurviewEDiscovery app in Microsoft Entra ID

Complete the following steps:

1. Validate that the **MicrosoftPurviewEDiscovery** app isn't already registered. Sign in to the Azure portal and go to **Microsoft Entra ID** &gt; **Enterprise Applications**.
2. Change the **Application type** filter to show *Microsoft Applications*.
3. In the search box, enter *MicrosoftPurviewEDiscovery*. The **MicrosoftPurviewEDiscovery** app should be displayed. If the **MicrosoftPurviewEDiscovery** app isn't listed, register the app in Microsoft Entra ID.

    To register the app, complete the following steps:

    - Use the Microsoft.Graph PowerShell Module to register the **MicrosoftPurviewEDiscovery** app in Microsoft Entra ID. For more information, see [Install the Microsoft Graph PowerShell SDK](/en-us/powershell/microsoftgraph/installation?view=graph-powershell-1.0).
    - After the module is installed on a machine, run the following cmdlet to connect to Microsoft Graph using PowerShell:

    ```powershell
    Connect-MgGraph -scopes "Application.ReadWrite.All"
    ```

    If this is the first time using Microsoft Graph PowerShell cmdlets, you might be prompted to consent to required permissions.

    To register the **MicrosoftPurviewEDiscovery** app, run the following PowerShell commands:

    ```powershell
    $spId = @{"AppId" = "00001111-aaaa-2222-bbbb-3333cccc4444" }
    ```

    ```powershell
    New-MgServicePrincipal -BodyParameter $spId;
    ```

Note

Use the [PowerShell script](https://complianceclientsdf.blob.core.windows.net/scripts/RegisterApp.ps1) to register a new application in Microsoft Entra ID and assign the Microsoft Purview eDiscovery API permissions for application authentication if applicable. After you register the application, you need to configure the client secret or certificate and grant admin consent through the portal.

#### Step 2: Assign additional MicrosoftPurviewEDiscovery permissions to the registered app

Now that the service principal is added, update the permissions on your previously registered app created in the Microsoft Graph API section of this article. Sign in to the Azure portal and go to **Microsoft Entra ID** &gt; **App Registrations**.

1. Find and select the app you created in the Microsoft Graph API section of this article.
2. Select **API Permissions** from the navigation menu.
3. Select **Add a permission** and then **APIs my organization uses**.
4. Search for MicrosoftPurviewEDiscovery and select it.
5. Select **Application Permissions**.
6. Select the check box for **eDiscovery.Download.Read**.
7. Select **Add Permissions**.
8. On **API permissions**, select **Grant Admin Consent (your organization)** to approve the added permissions.

After admin consent is granted, the status of the added permissions is updated for your organization.

### Downloading the export packages and reports

#### Retrieving the case ID and export job ID

To download the export packages and reports of an export process in an eDiscovery case, you need the case ID and the operation or job ID for the export job.

To gather this information by using the Microsoft Purview portal:

- Open an eDiscovery case.
- Locate the export process.
- Select **Copy support information**.
- Add this information into a text editor (like Notepad).

Alternatively, access this information programmatically by using the following Graph API calls to locate the case ID and the job ID you want to export:

1. Connect to Microsoft Graph by following the steps in the Connecting to Microsoft Graph API using app-only access section of this article.
2. Use the eDiscovery Graph PowerShell cmdlets with the following command if you know the case name:

    ```powershell
    Get-MgSecurityCaseEdiscoveryCase | where {$_.displayname -eq "<Name of case>"}
    ```
3. After you have the case ID, look up the operations in the case to identify the job ID for the export by using the following command:

    ```powershell
    Get-MgSecurityCaseEdiscoveryCaseOperation -EdiscoveryCaseId "<case ID>"
    ```

Export jobs are logged under an action of *exportResult* for a direct export from search or *ContentExport* for an export from a review set. The name of the export jobs isn't returned by this API call. To find the name of the export process, you must query the specific operation ID. Use the following command to find the name of the export process:

```powershell
Get-MgSecurityCaseEdiscoveryCaseOperation -EdiscoveryCaseId "<case ID>" -CaseOperationId “<operation ID>”
```

The name of the export operation is included in the **AdditionalProperties** field.

To make the HTTP API calls directly to list cases in your organization, see [List ediscoveryCases](/en-us/graph/api/security-casesroot-list-ediscoverycases?view=graph-rest-1.0&amp;tabs=http#examples).

To make the HTTP API calls directly to list the operations for a case, see [List caseOperations](/en-us/graph/api/security-ediscoverycase-list-operations?view=graph-rest-1.0&amp;tabs=http).

Use the case ID in the API call to indicate which case to list the operations from. For example:

`https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/<CaseID>/operations/`

The name of the export jobs isn't returned with this API call. To find the name of the export process, you must query the specific job ID. For example:

`https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/<CaseID>/operations/<OperationID>`

### Downloading an export package

#### Retrieving the download URLs for export packages

The *exportFileMetaData* property contains the URL you need to download the export packages and reports. To get the URL, you need the case *ID* of the eDiscovery case where you ran the export process and the operation *ID* for the export process.

Use the following eDiscovery Graph PowerShell cmdlets to find this information:

```powershell
$operation = Get-MgSecurityCaseEdiscoveryCaseOperation -EdiscoveryCaseId "<case ID>" -CaseOperationId “<operation ID>”
```

```powershell
$Operation.AdditionalProperties.exportFileMetadata
```

To make the HTTP API calls directly to return the *exportFileMetaData* information for an operation, see [List caseOperations](/en-us/graph/api/security-ediscoverycase-list-operations?view=graph-rest-1.0&amp;tabs=http).

Each export package in the Microsoft Purview portal has an entry in the *exportFileMetaData* property. Each entry lists the following information:

- The export package file name
- The downloadUrl to retrieve the export package
- The size of the export package

### Example scripts to download the export package

Because the Microsoft Purview eDiscovery API is separate from Microsoft Graph API, you need a separate authentication token to authorize a download request. Use the **MSAL.PS PowerShell Module** and the **Get-MSALToken** cmdlet to get a separate token. You also need to connect to the Microsoft Graph APIs by using the [Connect-MgGraph](/en-us/powershell/module/microsoft.graph.authentication/connect-mggraph?view=graph-powershell-1.0) cmdlet.

The following example scripts can be used as a reference when developing your own scripts to enable the programmatic download of the export packages.

#### Connecting with a client secret

If you configured your app to use a client secret, use the following example script as a reference to download the export package and reports programmatically. Copy the contents into Notepad and save it as `DownloadExportUsingApp.ps1`.

```powershell
[CmdletBinding()]
param (
    [Parameter(Mandatory = $true)]
    [string]$tenantId,
    [Parameter(Mandatory = $true)]
    [string]$appId,
    [Parameter(Mandatory = $true)]
    [string]$appSecret,
    [Parameter(Mandatory = $true)]
    [string]$caseId,
    [Parameter(Mandatory = $true)]
    [string]$exportId,
    [Parameter(Mandatory = $true)]
    [string]$path = "D:\Temp",
    [ValidateSet($null, 'USGov', 'USGovDoD')]
    [string]$environment = $null
)

if (-not(Get-Module -Name Microsoft.Graph -ListAvailable)) {
    Write-Host "Installing Microsoft.Graph module"
    Install-Module Microsoft.Graph -Scope CurrentUser
}

if (-not(Get-Module -Name MSAL.PS -ListAvailable)) {
    Write-Host "Installing MSAL.PS module"
    Install-Module MSAL.PS -Scope CurrentUser
}

$password = ConvertTo-SecureString $appSecret -AsPlainText -Force
$clientSecretCred = New-Object System.Management.Automation.PSCredential -ArgumentList ($appId, $password)

if (-not(Get-MgContext)) {
    Write-Host "Connect with credentials of a ediscovery admin (token for graph)"
    if (-not($environment)) {
        Connect-MgGraph -TenantId $TenantId -ClientSecretCredential $clientSecretCred
    }
    else {
        Connect-MgGraph -TenantId $TenantId -ClientSecretCredential $clientSecretCred -Environment $environment
    }
}

Write-Host "Connect with credentials of a ediscovery admin (token for export)"
$exportToken = Get-MsalToken -ClientId $appId -Scopes "00001111-aaaa-2222-bbbb-3333cccc4444/.default" -TenantId $tenantId -RedirectUri "http://localhost" -ClientSecret $password

$uri = "/v1.0/security/cases/ediscoveryCases/$($caseId)/operations/$($exportId)"

$export = Invoke-MgGraphRequest -Uri $uri;
if (-not($export)){
    Write-Host "Export not found"
    exit
}
else{
    $export.exportFileMetadata | % {
        Write-Host "Downloading $($_.fileName)"
        Invoke-WebRequest -Uri $_.downloadUrl -OutFile "$($path)\$($_.fileName)" -Headers @{"Authorization" = "Bearer $($exportToken.AccessToken)"; "X-AllowWithAADToken" = "true" }
    }
}
```

Save the script and open a new PowerShell window with the following PowerShell modules installed:

- Microsoft.Graph
- MSAL.PS

Browse to the directory where you saved the script and run the following command:

```powershell
.\DownloadExportUsingApp.ps1 -tenantId “<tenant ID>” -appId “<App ID>” -appSecret “<Client Secret>” -caseId “<CaseID>” -exportId “<ExportID>” -path “<Output Path>”
```

Review the folder you specified as the path to view the downloaded files.

#### Connecting with a certificate

If you configured your app to use a certificate, use the following example script as a reference to download the export package and reports programmatically. Copy the contents into a text editor and save it as `DownloadExportUsingAppCert.ps1`.

```powershell
[CmdletBinding()]
param (
    [Parameter(Mandatory = $true)]
    [string]$tenantId,
    [Parameter(Mandatory = $true)]
    [string]$appId,
    [Parameter(Mandatory = $true)]
    [String]$certPath,
    [Parameter(Mandatory = $true)]
    [string]$caseId,
    [Parameter(Mandatory = $true)]
    [string]$exportId,
    [Parameter(Mandatory = $true)]
    [string]$path = "D:\Temp",
    [ValidateSet($null, 'USGov', 'USGovDoD')]
    [string]$environment = $null
)

if (-not(Get-Module -Name Microsoft.Graph -ListAvailable)) {
    Write-Host "Installing Microsoft.Graph module"
    Install-Module Microsoft.Graph -Scope CurrentUser
}

if (-not(Get-Module -Name MSAL.PS -ListAvailable)) {
    Write-Host "Installing MSAL.PS module"
    Install-Module MSAL.PS -Scope CurrentUser
}

##$password = ConvertTo-SecureString $appSecret -AsPlainText -Force
##$clientSecretCred = New-Object System.Management.Automation.PSCredential -ArgumentList ($appId, $password)

$ClientCert = Get-ChildItem $certPath

if (-not(Get-MgContext)) {
    Write-Host "Connect with credentials of a ediscovery admin (token for graph)"
    if (-not($environment)) {
        Connect-MgGraph -TenantId $TenantId -ClientId $appId -Certificate $ClientCert
    }
    else {
        Connect-MgGraph -TenantId $TenantId -ClientId $appId -Certificate $ClientCert -Environment $environment
    }
}

Write-Host "Connect with credentials of a ediscovery admin (token for export)"

$connectionDetails = @{
    'TenantId'          = $tenantId
    'ClientId'          = $appID
    'ClientCertificate' = $ClientCert
    'Scope' = "00001111-aaaa-2222-bbbb-3333cccc4444/.default"
}

$exportToken = Get-MsalToken @connectionDetails

$uri = "/v1.0/security/cases/ediscoveryCases/$($caseId)/operations/$($exportId)"

$export = Invoke-MgGraphRequest -Uri $uri;
if (-not($export)){
    Write-Host "Export not found"
    exit
}
else{
    $export.exportFileMetadata | % {
        Write-Host "Downloading $($_.fileName)"
        Invoke-WebRequest -Uri $_.downloadUrl -OutFile "$($path)\$($_.fileName)" -Headers @{"Authorization" = "Bearer $($exportToken.AccessToken)"; "X-AllowWithAADToken" = "true" }
    }
}
```

When you save the script, open a new PowerShell window with the following PowerShell modules installed:

- Microsoft.Graph
- MSAL.PS

Browse to the directory where you saved the script and run the following command.

```powershell
.\DownloadExportUsingAppCert.ps1 -tenantId “<tenant ID>” -appId “<App ID>” -certPath “<Certificate Path>” -caseId “<CaseID>” -exportId “<ExportID>” -path “<Output Path>”
```

Review the folder you specified as the path to view the downloaded files.