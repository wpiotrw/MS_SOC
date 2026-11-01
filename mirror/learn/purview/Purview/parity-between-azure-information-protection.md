---
layout: Conceptual
title: Microsoft Purview Information Protection for Office 365 operated by 21Vianet | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/parity-between-azure-information-protection
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
ms.reviewer: tommoser
manager: laurawi
ms.date: 2026-10-26T00:00:00.0000000Z
audience: Admin
ms.topic: reference
ms.service: purview
ms.subservice: purview-encryption
ms.collection:
- purview-compliance
description: Learn how to configure Microsoft Purview Information Protection for tenants in China.
locale: en-us
document_id: 5e3f2697-b8a4-edbb-0d82-cd4d6c4290de
document_version_independent_id: 5e3f2697-b8a4-edbb-0d82-cd4d6c4290de
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/parity-between-azure-information-protection.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: parity-between-azure-information-protection
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/parity-between-azure-information-protection.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6ab06385-661e-4214-8870-bbe4071c960d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/131ba09e-4280-4ae7-8622-1f9f1c0daad1
platformId: 730d60b1-4222-dcf7-fd7d-175746ee1fbd
---

# Microsoft Purview Information Protection for Office 365 operated by 21Vianet | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

This article covers the differences between Microsoft Purview Information Protection support for Office 365 operated by 21Vianet and commercial offerings that are limited to offering previously known as Azure Information Protection (AIP), as well as specific configuration instructions for customers in China— including how to install the information protection scanner and manage content scan jobs.

## Differences between 21Vianet and commercial offerings

While our goal is to deliver all commercial features and functionality to customers in China with our Microsoft Purview Information Protection support for Office 365 operated by 21Vianet offer, there's some missing functionality:

- Active Directory Rights Management Services (AD RMS) encryption is supported only in Microsoft 365 Apps for enterprise (build 11731.10000 or later). Office Professional Plus doesn't support AD RMS.
- Migration from AD RMS to the Azure Rights Management service isn't currently available.
- Sharing encrypted email between organizations in Office 365 operated by 21Vianet and the commercial cloud is supported in both directions when you use Microsoft Purview Message Encryption. Recipients must use the encrypted message portal and authenticate by using a one-time passcode. Native consumption in Outlook clients isn't supported. For more information, see [Manage the use of one-time passcodes for the encrypted message portal](manage-office-365-message-encryption#manage-the-use-of-one-time-pass-codes-for-the-encrypted-message-portal).
- Sharing of documents and email attachments with users in the commercial cloud isn't currently available. This includes Office 365 operated by 21Vianet users in the commercial cloud, non-Office 365 operated by 21Vianet users in the commercial cloud, and users with an RMS for Individuals license.
- IRM with SharePoint (IRM-protected sites and libraries) isn't currently available.
- The Mobile Device Extension for AD RMS isn't currently available.
- The [Microsoft Purview Information Protection viewer](https://support.microsoft.com/topic/view-protected-files-with-microsoft-purview-information-protection-viewer-9fb56fae-7989-48b0-850f-f446e057cf73) for iOS and Android isn't supported by Azure China 21Vianet.
- The scanner area of the Microsoft Purview portal is unavailable to customers in China. Use PowerShell commands instead of performing actions in the portal, such as managing and running your content scan jobs.
- Network endpoints for the Microsoft Purview Information Protection client within the 21Vianet environment are different than the endpoints required for other cloud services. Network connectivity from clients to the following endpoints is required:

    - Download label and label policies: `*.protection.partner.outlook.cn`
    - Azure Rights Management service: `*.aadrm.cn`
- Document Tracking and Revocation *by users* isn't currently available.

## Configuration for customers in 21Vianet

To configure Microsoft Purview Information Protection support for Office 365 operated by 21Vianet:

1. Enable Rights Management for the tenant.
2. Add the Microsoft Information Protection Sync Service service principal.
3. Configure DNS encryption.
4. Install and configure the Microsoft Purview Information Protection client.
5. Configure Windows settings.
6. Install the information protection scanner and manage content scan jobs.

### Step 1: Enable Rights Management for the tenant

For the encryption to work correctly, the Azure Rights Management service must be enabled for the tenant.

1. Check if this service is enabled:

    1. Launch PowerShell as an administrator.
    2. If the AIPService module isn't installed, run `Install-Module AipService`.
    3. Import the module using `Import-Module AipService`.
    4. Connect to the service using `Connect-AipService -environmentname azurechinacloud`.
    5. Run `(Get-AipServiceConfiguration).FunctionalState` and check if the state is `Enabled`.
2. If the functional state is `Disabled`, run `Enable-AipService`.

### Step 2: Add the Microsoft Information Protection Sync Service service principal

The **Microsoft Information Protection Sync Service** service principal isn't available in Azure China tenants by default, and is required for Microsoft Purview Information Protection. Create this service principal manually via the Azure Az PowerShell module.

1. If you don't have the Azure Az module installed, install it or use a resource where the Azure Az module comes preinstalled, such as [Azure Cloud Shell](/en-us/azure/cloud-shell/overview). For more information, see [Install the Azure Az PowerShell module](/en-us/powershell/azure/install-az-ps).
2. Connect to the service using the [Connect-AzAccount](/en-us/powershell/module/az.accounts/Connect-AzAccount) cmdlet and the `azurechinacloud` environment name:

    ```powershell
    Connect-azaccount -environmentname azurechinacloud
    ```
3. Create the **Microsoft Information Protection Sync Service** service principal manually using the [New-AzADServicePrincipal](/en-us/powershell/module/az.resources/new-azadserviceprincipal) cmdlet and the `870c4f2e-85b6-4d43-bdda-6ed9a579b725` application ID for the Microsoft Purview Information Protection Sync Service:

    ```powershell
    New-AzADServicePrincipal -ApplicationId 870c4f2e-85b6-4d43-bdda-6ed9a579b725
    ```
4. After adding the service principal, add the relevant permissions required to the service.

### Step 3: Configure DNS encryption

For encryption to work correctly, Office client applications must connect to the China instance of the service and bootstrap from there. To redirect client applications to the right service instance, the tenant admin must configure a DNS SRV record with information about the URL for the Azure Rights Management service. Without the DNS SRV record, the client application attempts to connect to the public cloud instance by default and will fail.

Also, the assumption is that users will log in with a username based off the tenant-owned domain (for example, `joe@contoso.cn`), and not the `onmschina` username (for example, `joe@contoso.onmschina.cn`). The domain name from the username is used for DNS redirection to the correct service instance.

#### Configure DNS encryption - Windows

1. Get the Azure Rights Management service ID:

    1. Launch PowerShell as an administrator.
    2. If the AIPService module isn't installed, run `Install-Module AipService`.
    3. Connect to the service using `Connect-AipService -environmentname azurechinacloud`.
    4. Run `(Get-AipServiceConfiguration).RightsManagementServiceId` to get the service ID.
2. Log in to your DNS provider, navigate to the DNS settings for the domain, and then add a new SRV record.

    - Service = `_rmsredir`
    - Protocol = `_http`
    - Name = `_tcp`
    - Target = `[GUID].rms.aadrm.cn` (where GUID is the Azure Rights Management service ID)
    - Priority, Weight, Seconds, TTL = default values
3. Associate the custom domain with the tenant in the [Azure portal](https://portal.azure.cn/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Domains). This adds an entry in DNS, which might take several minutes to get verified after you add the value to the DNS settings.
4. Log in to the Microsoft 365 admin center with the corresponding Compliance Administrator credentials and add the domain (for example, `contoso.cn`) for user creation. In the verification process, additional DNS changes might be required. Once verification is done, users can be created.

#### Configure DNS encryption - Mac, iOS, Android

Log in to your DNS provider, navigate to the DNS settings for the domain, and then add a new SRV record.

- Service = `_rmsdisco`
- Protocol = `_http`
- Name = `_tcp`
- Target = `api.aadrm.cn`
- Port = `80`
- Priority, Weight, Seconds, TTL = default values

### Step 4: Install and configure the labeling client

Download and install the Microsoft Purview Information Protection client from the [Microsoft Download Center](https://www.microsoft.com/download/details.aspx?id=53018).

For more information, see:

- [Extend sensitivity labeling on Windows](information-protection-client)
- [Microsoft Purview Information Protection client - Release management and supportability](information-protection-client-relnotes)

### Step 5: Configure Windows settings

Windows needs the following registry key for authentication to point to the correct sovereign cloud for Azure China:

- Registry node = `HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\MSIP`
- Name = `CloudEnvType`
- Value = `6` (default = 0)
- Type = `REG_DWORD`

Important

Make sure you don't delete the registry key after an uninstall. If the key is empty, incorrect, or non-existent, the functionality will behave as the default value (default value = 0 for the commercial cloud). If the key is empty or incorrect, a print error is also added to the log.

### Step 6: Install the information protection scanner and manage content scan jobs

Install the Microsoft Purview Information Protection scanner to scan your network and content shares for sensitive data, and apply classification and protection labels as configured in your organization's policy.

When configuring and managing your content scan jobs, use the following procedure instead of the [Microsoft Purview portal](deploy-scanner-configure-install) that's used by the commercial offerings.

For more information, see [Learn about the information protection scanner](deploy-scanner) and [Manage your content scan jobs using PowerShell only](deploy-scanner-prereqs#use-powershell-with-a-disconnected-computer).

**To install and configure your scanner**:

1. Sign in to the Windows Server computer that will run the scanner. Use an account that has local administrator rights and that has permissions to write to the SQL Server master database.
2. Start with PowerShell closed. If you've previously installed the information protection scanner, make sure the Microsoft Purview Information Protection Scanner service is stopped.
3. Open a Windows PowerShell session with the **Run as an administrator** option.
4. Run the [Install-Scanner](/en-us/powershell/module/purviewinformationprotection/install-scanner) cmdlet, specifying your SQL Server instance on which to create a database for the Microsoft Purview Information Protection scanner, and a meaningful name for your scanner cluster.

    ```PowerShell
    Install-Scanner -SqlServerInstance <name> -Cluster <cluster name>
    ```

    Tip

    You can use the same cluster name in the [Install-Scanner](/en-us/powershell/module/purviewinformationprotection/install-scanner) command to associate multiple scanner nodes to the same cluster. Using the same cluster for multiple scanner nodes enables multiple scanners to work together to perform your scans.
5. Verify that the service is now installed by using **Administrative Tools** &gt; **Services**.

    The installed service is named **Microsoft Purview Information Protection Scanner** and is configured to run by using the scanner service account that you created.
6. Get an Azure token to use with your scanner. A Microsoft Entra token allows the scanner to authenticate to the Azure Rights Management encryption service, enabling the scanner to run non-interactively.

    1. Open the Azure portal and create a Microsoft Entra application to specify an access token for authentication. For more information, see [Run information protection labeling cmdlets unattended](/en-us/powershell/azure/aip/setup-information-protection-client-powershell#run-information-protection-labeling-cmdlets-unattended).

        Tip

        When creating and configuring Microsoft Entra applications for the [Set-Authentication](/en-us/powershell/module/purviewinformationprotection/set-authentication) command, the **Request API permissions** pane shows the **APIs my organization uses** tab instead of the **Microsoft APIs** tab. Select the **APIs my organization uses** to then select **Azure Rights Management Services**.
    2. From the Windows Server computer, if your scanner service account has been granted the **Log on locally** right for the installation, sign in with this account and start a PowerShell session.

        If your scanner service account can't be granted the **Log on locally** right for the installation, use the *OnBehalfOf* parameter with [Set-Authentication](/en-us/powershell/module/purviewinformationprotection/set-scannerconfiguration), as described in [Run information protection labeling cmdlets unattended](/en-us/powershell/azure/aip/setup-information-protection-client-powershell#run-information-protection-labeling-cmdlets-unattended).
    3. Run [Set-Authentication](/en-us/powershell/module/purviewinformationprotection/set-authentication), specifying values copied from your Microsoft Entra application:

        ```PowerShell
        Set-Authentication -AppId <ID of the registered app> -AppSecret <client secret sting> -TenantId <your tenant ID> -DelegatedUser <Microsoft Entra account>
        ```

        For example:

        ```PowerShell
        $pscreds = Get-Credential CONTOSO\scanner
        Set-Authentication -AppId "00001111-aaaa-2222-bbbb-3333cccc4444" -AppSecret "OAkk+rnuYc/u+]ah2kNxVbtrDGbS47L4" -DelegatedUser scanner@contoso.com -TenantId "aaaabbbb-0000-cccc-1111-dddd2222eeee" -OnBehalfOf $pscreds
        Acquired application access token on behalf of CONTOSO\scanner.
        ```

    The scanner now has a token to authenticate to Microsoft Entra ID. This token is valid for one year, two years, or never, according to your configuration of the **Web app /API** client secret in Microsoft Entra ID. When the token expires, you must repeat this procedure.
7. Run the [Set-ScannerConfiguration](/en-us/powershell/module/purviewinformationprotection/set-scannerconfiguration) cmdlet to set the scanner to function in offline mode. Run:

    ```powershell
    Set-ScannerConfiguration -OnlineConfiguration Off
    ```
8. Run the [Set-ScannerContentScanJob](/en-us/powershell/module/purviewinformationprotection/set-scannercontentscan) cmdlet to create a default content scan job.

    The only required parameter in the **Set-ScannerContentScanJob** cmdlet is **Enforce**. However, you may want to define other settings for your content scan job at this time. For example:

    ```powershell
    Set-ScannerContentScanJob -Schedule Manual -DiscoverInformationTypes PolicyOnly -Enforce Off -DefaultLabelType PolicyDefault -RelabelFiles Off -PreserveFileDetails On -IncludeFileTypes '' -ExcludeFileTypes '.msg,.tmp' -DefaultOwner <account running the scanner>
    ```

    The syntax above configures the following settings while you continue the configuration:

    - Keeps the scanner run scheduling to *manual*
    - Sets the information types to be discovered based on the sensitivity labeling policy
    - Does *not* enforce a sensitivity labeling policy
    - Automatically labels files based on content, using the default label defined for the sensitivity labeling policy
    - Does *not* allow for relabeling files
    - Preserves file details while scanning and auto-labeling, including *date modified*, *last modified*, and *modified by* values
    - Sets the scanner to exclude .msg and .tmp files when running
    - Sets the default owner to the account you want to use when running the scanner
9. Use the [Add-ScannerRepository](/en-us/powershell/module/purviewinformationprotection/add-scannerrepository) cmdlet to define the repositories you want to scan in your content scan job. For example, run:

    ```powershell
    Add-ScannerRepository -OverrideContentScanJob Off -Path 'c:\repoToScan'
    ```

    Use one of the following syntaxes, depending on the type of repository you're adding:

    - For a network share, use `\\Server\Folder`.
    - For a SharePoint library, use `http://sharepoint.contoso.com/Shared%20Documents/Folder`.
    - For a local path: `C:\Folder`
    - For a UNC path: `\\Server\Folder`

    Note

    Wildcards aren't supported and WebDav locations aren't supported.

    To modify the repository later on, use the [Set-ScannerRepository](/en-us/powershell/module/purviewinformationprotection/set-scannerrepository) cmdlet instead.

Continue with the following steps as needed:

- [Run a discovery cycle and view reports for the scanner](deploy-scanner-manage#run-a-discovery-cycle-and-view-reports-for-the-scanner)
- [Use PowerShell to configure the scanner to apply classification and protection](/en-us/purview/deploy-scanner-configure-install?tabs=azure-portal-only#use-powershell-to-configure-the-scanner-to-apply-classification-and-protection)
- [Use PowerShell to configure a DLP policy with the scanner](/en-us/purview/deploy-scanner-configure-install?tabs=azure-portal-only#use-powershell-to-configure-a-dlp-policy-with-the-scanner)

The following table lists PowerShell cmdlets that are relevant for installing the scanner and managing your content scan jobs:

| Cmdlet | Description |
| --- | --- |
| [Add-ScannerRepository](/en-us/powershell/module/purviewinformationprotection/add-scannerrepository) | Adds a new repository to your content scan job. |
| [Get-ScannerConfiguration](/en-us/powershell/module/purviewinformationprotection/get-scannerconfiguration) | Returns details about your cluster. |
| [Get-ScannerContentScan](/en-us/powershell/module/purviewinformationprotection/get-scannercontentscan) | Gets details about your content scan job. |
| [Get-ScannerRepository](/en-us/powershell/module/purviewinformationprotection/get-scannerrepository) | Gets details about repositories defined for your content scan job. |
| [Remove-ScannerContentScan](/en-us/powershell/module/purviewinformationprotection/remove-scannercontentscan) | Deletes your content scan job. |
| [Remove-ScannerRepository](/en-us/powershell/module/purviewinformationprotection/remove-scannerrepository) | Removes a repository from your content scan job. |
| [Set-ScannerContentScan](/en-us/powershell/module/purviewinformationprotection/set-scannercontentscan) | Defines settings for your content scan job. |
| [Set-ScannerRepository](/en-us/powershell/module/purviewinformationprotection/set-scannerrepository) | Defines settings for an existing repository in your content scan job. |

For more information, see:

- [Learn about the information protection scanner](deploy-scanner)
- [Configuring and installing the information protection scanner](/en-us/purview/deploy-scanner-configure-install?tabs=powershell-only)
- [Manage your content scan jobs using PowerShell only](deploy-scanner-prereqs#use-powershell-with-a-disconnected-computer)