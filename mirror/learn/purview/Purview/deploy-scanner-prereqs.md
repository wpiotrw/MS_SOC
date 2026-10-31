---
layout: Conceptual
title: Get started with the information protection scanner | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/deploy-scanner-prereqs
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords: 
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-10-26T00:00:00.0000000Z
audience: Admin
ms.topic: get-started
ms.service: purview
ms.subservice: purview-information-protection
ms.collection:
- purview-compliance
description: Lists prerequisites for installing and deploying the Microsoft Purview Information Protection scanner.
locale: en-us
document_id: 395b4de2-27da-333e-ae49-5ec791bb73f9
document_version_independent_id: 395b4de2-27da-333e-ae49-5ec791bb73f9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/deploy-scanner-prereqs.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: deploy-scanner-prereqs
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/deploy-scanner-prereqs.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/cbe4ca68-43ac-4375-aba5-5945a6394c20
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/fc3f72c2-fb6f-4cea-95ee-b444e52254ee
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ced846cc-6a3c-4c8f-9dfb-3de0e90e2742
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f12cf087-582d-48ac-a085-0c19adf1e391
platformId: 52aec4ad-c021-792e-88b4-e019f5c34d4e
---

# Get started with the information protection scanner | Microsoft Learn

Note

There's a new version of the information protection scanner. For more information, see [Upgrade the Microsoft Purview Information Protection scanner](upgrade-scanner-migrate).

Before you install the scanner from Microsoft Purview Information Protection, make sure that your system complies with [requirements for the Azure Rights Management service](rights-management-requirements).

Additionally, the following requirements are specific for the scanner:

- Windows Server requirements
- Service account requirements
- SQL server requirements
- Information protection client requirements
- Label configuration requirements
- SharePoint requirements
- Microsoft Office requirements
- File path requirements

If you can't meet all the requirements listed for the scanner because they are prohibited by your organization's policies, see the alternative configurations section.

When deploying the scanner in production or testing the performance for multiple scanners, see Storage requirements and capacity planning for SQL Server.

When you're ready to start installing and deploying your scanner, continue with [Configuring and installing the information protection scanner](deploy-scanner-configure-install).

## Windows Server requirements

You must have a Windows Server computer to run the scanner, which has the following system specifications:

| Specification | Details |
| --- | --- |
| **Processor** | 4 core processors |
| **RAM** | 8 GB |
| **Disk space** | 10-GB free space (average) for temporary files. The scanner requires sufficient disk space to create temporary files for each file that it scans, four files per core. The recommended disk space of 10 GB allows for 4 core processors scanning 16 files that each have a file size of 625 MB. |
| **Operating system** | A 64-bit version of Windows Server that is supported under the Microsoft Lifecycle Policy, including versions in extended support. To confirm whether a specific version is supported, see [Windows Server release information](/en-us/windows/release-health/windows-server-release-info). **Note**: For testing or evaluation purposes in a non-production environment, you can also use any Windows operating system that is [supported by the information protection client](information-protection-client#requirements-for-deploying-the-information-protection-client).  Server Core and Nano Server aren't supported. |
| **- Network connectivity** | Your scanner computer can be a physical or virtual computer with a fast and reliable network connection to the data stores to be scanned.  If internet connectivity is not possible because of your organization policies, see Deploying the scanner with alternative configurations. Otherwise, make sure that this computer has internet connectivity that allows the following URLs over HTTPS (port 443):- \*.aadrm.com - \*.azurerms.com- \*.informationprotection.azure.com  - informationprotection.hosting.portal.azure.net  - \*.aria.microsoft.com - \*.protection.outlook.com - \*.events.data.microsoft.com - config.edge.skype.com |
| **NFS shares** | To support scans on NFS shares, services for NFS must be deployed on the scanner machine. On your machine, navigate to the **Windows Features (Turn Windows features on or off)** settings dialog, and select the following items: **Services for NFS** &gt; **Administrative Tools** and **Client for NFS**. |
| **Microsoft Office iFilter** | When your scanner is installed on a Windows server machine, you must also install the Microsoft Office iFilter in order to scan .zip files for sensitive information types. For more information, see the [Microsoft download site](https://www.microsoft.com/download/details.aspx?id=17062). |

## Service account requirements

You must have a service account to run the scanner service on the Windows Server computer, as well as authenticate to Microsoft Entra ID and download the scanner's policy.

Your service account must be an Active Directory account and synchronized to Microsoft Entra ID.

If you cannot synchronize this account because of your organization policies, see Deploying the scanner with alternative configurations.

This service account has the following requirements:

| Requirement | Details |
| --- | --- |
| **Log on locally** user right assignment | Required to install and configure the scanner, but not required to run scans. Once you've confirmed that the scanner can discover, classify, and protect files, you can remove this right from the service account. If granting this right even for a short period of time is not possible because of your organization policies, see Deploying the scanner with alternative configurations. |
| **Log on as a service** user right assignment. | This right is automatically granted to the service account during the scanner installation and this right is required for the installation, configuration, and operation of the scanner. |
| **Permissions to the data repositories** | - **File shares or local files**: Grant **Read**, **Write**, and **Modify** permissions for scanning the files and then applying classification and protection as configured. - **SharePoint**: You must grant **Full Control** permissions for scanning the files and then applying classification and protection to the files that meet the conditions in the Azure Information Protection policy. - **Discovery mode**: To run the scanner in discovery mode only, **Read** permission is sufficient. |
| **For labels that reprotect or remove protection** | To ensure that the scanner always has access to encrypted files, make this account a [super user](encryption-super-users) for the Azure Rights Management service, and ensure that the super user feature is enabled. Additionally, if you've implemented [onboarding controls](/en-us/azure/information-protection/activate-service#configuring-onboarding-controls-for-a-phased-deployment) for a phased deployment, make sure that the service account is included in the onboarding controls you've configured. |
| **Specific URL level scanning** | To scan and discover sites and subsites under a specific URL, grant **Site Collector Auditor** rights to the scanner account on the farm level. |
| **License for information protection** | Required to provide file classification, labeling, or protection capabilities to the scanner service account. For more information, see the [Microsoft 365 guidance for security & compliance](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance#information-protection-sensitivity-labeling). |

## SQL server requirements

To store the scanner configuration data, use an SQL server with the following requirements:

- **A local or remote instance.**

    We recommend hosting the SQL server and the scanner service on different machines, unless you're working with a small deployment. Additionally, we recommend having a dedicated SQL instance that serves the scanner database only, and that is not shared with other applications.

    If you're working on a shared server, make sure that the recommended number of cores are free for the scanner database to work.

    SQL Server 2016 is the minimum version for the following editions:

    - SQL Server Enterprise
    - SQL Server Standard
    - SQL Server Express (recommended for test environments only)
- **An account with Sysadmin role to install the scanner.**

    The Sysadmin role enables the installation process to automatically create the scanner configuration database and grant the required **db\_owner** role to the service account that runs the scanner.

    If you cannot be granted the Sysadmin role or your organization policies require databases to be created and configured manually, see Deploying the scanner with alternative configurations.
- **Capacity.** For capacity guidance, see Storage requirements and capacity planning for SQL Server.
- **[Case insensitive collation](/en-us/sql/relational-databases/collations/collation-and-unicode-support).**

Note

Multiple configuration databases on the same SQL server are supported when you specify a custom cluster name for the scanner, or when you use the preview version of the scanner.

### Storage requirements and capacity planning for SQL Server

The amount of disk space required for the scanner's configuration database and the specification of the computer running SQL Server can vary for each environment, so we encourage you to do your own testing. Use the following guidance as a starting point.

For more information, see [Optimizing the performance of the scanner](deploy-scanner-configure-install#optimize-scanner-performance).

The disk size for the scanner configuration database will vary for each deployment. Use the following equation as guidance:

```cli
100 KB + <file count> *(1000 + 4* <average file name length>)
```

For example, to scan 1 million files that have an average file name length of 250 bytes, allocate 2-GB disk space.

For multiple scanners:

- **Up to 10 scanners**, use:

    - 4 core processors
    - 8-GB RAM recommended
- **More than 10 scanners** (maximum 40), use:

    - 8 core processes
    - 16-GB RAM recommended

## Information protection client requirements

For a production network, you must have the [current general availability version](information-protection-client-relnotes) of the Microsoft Purview Information Protection client installed on the Windows Server computer.

For more information, see the [Install or upgrade the information protection client](information-protection-client#install-or-upgrade-the-information-protection-client).

Important

You must install the full client for the scanner. Do not install the client with just the PowerShell module.

## Label configuration requirements

You must have at least one sensitivity label configured in the Microsoft Purview portal for the scanner account, to apply classification and, optionally, encryption.

The *scanner account* is the account that you'll specify in the **DelegatedUser** parameter of the [Set-Authentication](/en-us/powershell/module/purviewinformationprotection/set-authentication) cmdlet, run when configuring your scanner.

If your labels don't have auto-labeling conditions, see the instructions for alternative configurations below.

For more information, see:

- [Learn about sensitivity labels](sensitivity-labels)
- [Automatically apply a sensitivity label to Microsoft 365 data](apply-sensitivity-label-automatically)
- [Restrict access to content by using encryption in sensitivity labels](encryption-sensitivity-labels)
- [Configuring and installing the information protection scanner](deploy-scanner-configure-install)

## SharePoint requirements

To scan SharePoint document libraries and folders, ensure that your SharePoint server complies with the following requirements:

| Requirement | Description |
| --- | --- |
| **Supported versions** | SharePoint Server Subscription Edition (SPSE) in extended support. For more information see the SharePoint Server Support Policy [updated product servicing policy for SharePoint Server SE](/en-us/sharepoint/product-servicing-policy/updated-product-servicing-policy-for-sharepoint-server-se#policy-overview). |
| **Versioning** | When you use [versioning](/en-us/sharepoint/governance/versioning-content-approval-and-check-out-planning), the scanner inspects and labels the last published version. If the scanner labels a file and [content approval](/en-us/sharepoint/governance/versioning-content-approval-and-check-out-planning#plan-content-approval) is required, that labeled file must be approved to be available for users. |
| **Large SharePoint farms** | For large SharePoint farms, check whether you need to increase the list view threshold (by default, 5,000) for the scanner to access all files. For more information, see [Manage large lists and libraries in SharePoint](https://support.office.com/article/manage-large-lists-and-libraries-in-sharepoint-b8588dae-9387-48c2-9248-c24122f07c59#__bkmkchangelimit&amp;ID0EAABAAA=Server). |
| **Long file paths** | If you have long file paths in SharePoint, ensure that your SharePoint server's [httpRuntime.maxUrlLength](/en-us/dotnet/api/system.web.configuration.httpruntimesection.maxurllength) value is larger than the default 260 characters. For more information, see the next section, Avoid scanner timeouts in SharePoint. |

### Avoid scanner timeouts in SharePoint

If you have long file paths in SharePoint version 2013 or higher, ensure that your SharePoint server's [httpRuntime.maxUrlLength](/en-us/dotnet/api/system.web.configuration.httpruntimesection.maxurllength) value is larger than the default 260 characters.

This value is defined in the **HttpRuntimeSection** class of the `ASP.NET` configuration.

**To update the HttpRuntimeSection class**:

1. Back up your **web.config** configuration.
2. Update the **maxUrlLength** value as needed. For example:

    ```c
    <httpRuntime maxRequestLength="51200" requestValidationMode="2.0" maxUrlLength="5000"  />
    ```
3. Restart your SharePoint web server and verify that it loads correctly.

    For example, in Windows Internet Information Servers (IIS) Manager, select your site, and then under **Manage Website**, select **Restart**.

## Microsoft Office requirements

To scan Office documents, your documents must be in one of the following formats:

- Microsoft Office 97-2003
- Office Open XML formats for Word, Excel, and PowerPoint

For more information, see [Supported file types](information-protection-client#supported-file-types).

## File path requirements

By default, to scan files, your file paths must have a maximum of 260 characters.

To scan files with file paths of more than 260 characters, install the scanner on a computer with one of the following Windows versions, and configure the computer as needed:

| Windows version | Description |
| --- | --- |
| **Windows 2016 or later** | Configure the computer to support long paths |
| **Windows 10 or Windows Server 2016** | Define the following [group policy setting](/en-us/archive/blogs/jeremykuhne/net-4-6-2-and-long-paths-on-windows-10): **Local Computer Policy** &gt; **Computer Configuration** &gt; **Administrative Templates** &gt; **All Settings** &gt; **Enable Win32 long paths**. For more information long file path support in these versions, see the [Maximum Path Length Limitation](/en-us/windows/desktop/FileIO/naming-a-file#maximum-path-length-limitation) section from the Windows 10 developer documentation. |
| **Windows 10, version 1607 or later** | Opt in for the updated **MAX\_PATH** functionality. For more information, see [Enable Long Paths in Windows 10 versions 1607 and later](/en-us/windows/win32/fileio/naming-a-file#enable-long-paths-in-windows-10-version-1607-and-later). |

## Deploying the scanner with alternative configurations

The prerequisites listed above are the default requirements for the scanner deployment, and recommended because they support the simplest scanner configuration.

The default requirements should be suitable for initial testing, so that you can check the capabilities of the scanner.

However, in a production environment, your organization's policies may be different than the default requirements. The scanner can accommodate the following changes with additional configuration:

- Discover and scan all sites and subsites under a specific URL
- Restriction: The scanner server cannot have internet connectivity
- Restriction: The scanner service account cannot be synchronized to Microsoft Entra ID but the server has internet connectivity
- Restriction: The service account for the scanner cannot be granted the **Log on locally** right
- Restriction: You cannot be granted Sysadmin or databases must be created and configured manually
- Restriction: Your labels do not have auto-labeling conditions

### Discover and scan all SharePoint sites and subsites under a specific URL

The scanner can discover and scan all SharePoint sites and subsites under a specific URL with the following configuration:

1. Start **SharePoint Central Administration**.
2. On the **SharePoint Central Administration** website, in the **Application Management** section, click **Manage web applications**.
3. Click to highlight the web application whose permission policy level you want to manage.
4. Choose the relevant farm and then select **Manage Permissions Policy Levels**.
5. Select **Site Collection Auditor** in the **Site Collection Permissions** options, then grant **View Application Pages** in the Permissions list, and finally, name the new policy level **Scanner site collection auditor and viewer**.
6. Add your scanner user to the new policy and grant **Site collection** in the Permissions list.
7. Add a URL of the SharePoint that hosts sites or subsites that need to be scanned. For more information, see [Configure the scanner settings](deploy-scanner-configure-install#configure-the-scanner-settings).

To learn more about how to manage your SharePoint policy levels see, [manage permission policies for a web application](/en-us/sharepoint/administration/manage-permission-policies-for-a-web-application).

### Restriction: The scanner server cannot have internet connectivity

While the information protection client can't apply encryption without an internet connection, the scanner can still apply labels based on imported policies.

To support a disconnected computer, use one of the following methods:

- Use the Microsoft Purview portal (recommended when possible)
- Use PowerShell

#### Use the Microsoft Purview portal with a disconnected computer

To support a computer that can't connect to the Microsoft Purview portal, perform the following steps:

1. Configure labels in your policy, and then use the [procedure to support disconnected computers](information-protection-client#support-for-disconnected-computers) to enable offline classification and labeling.
2. Enable offline management for content jobs as follows:

    **Enable offline management for content scan jobs**:

    1. Set the scanner to function in **offline** mode, using the [Set-ScannerConfiguration](/en-us/powershell/module/purviewinformationprotection/set-scannerconfiguration) cmdlet.
    2. Configure the scanner in the Microsoft Purview portal by creating a scanner cluster. For more information, see [Configure the scanner settings](deploy-scanner-configure-install#configure-the-scanner-settings).
    3. Export your content job from the **Information protection - Content scan jobs** pane using the **Export** option.
    4. Import the policy using the [Import-ScannerConfiguration](/en-us/powershell/module/purviewinformationprotection/import-scannerconfiguration) cmdlet.

    Results for offline content scan jobs are located at: **%localappdata%\Microsoft\MSIP\Scanner\Reports**

#### Use PowerShell with a disconnected computer

Perform the following procedure to support a disconnected computer using PowerShell only.

Important

Admins of [Azure China 21Vianet scanner servers](/en-us/microsoft-365/admin/services-in-china/parity-between-azure-information-protection#manage-azure-information-protection-content-scan-jobs)*must* use this procedure in order to manage their content scan jobs.

**Manage your content scan jobs using PowerShell only**:

1. Set the scanner to function in **offline** mode, using the [Set-ScannerConfiguration](/en-us/powershell/module/purviewinformationprotection/set-scannerconfiguration) cmdlet.
2. Create a new content scan job using the [Set-ScannerContentScan](/en-us/powershell/module/purviewinformationprotection/set-scannercontentscan) cmdlet, making sure to use the mandatory `-Enforce On` parameter.
3. Add your repositories using the [Add-ScannerRepository](/en-us/powershell/module/purviewinformationprotection/add-scannerrepository) cmdlet, with the path to the repository you want to add.

    Tip

    To prevent the repository from inheriting settings from your content scan job, add the `OverrideContentScanJob On` parameter, as well as values for additional settings.

    To edit details for an existing repository, use the [Set-ScannerRepository](/en-us/powershell/module/purviewinformationprotection/set-scannerrepository) command.
4. Use the [Get-ScannerContentScan](/en-us/powershell/module/purviewinformationprotection/get-scannercontentscan) and [Get-ScannerRepository](/en-us/powershell/module/purviewinformationprotection/get-scannerrepository) cmdlets to return information about your content scan job's current settings.
5. Use the [Set-ScannerRepository](/en-us/powershell/module/purviewinformationprotection/set-scannerrepository) command to update details for an existing repository.
6. Run your content scan job immediately if needed, using the [Start-Scan](/en-us/powershell/module/purviewinformationprotection/start-scan) cmdlet.

    Results for offline content scan jobs are located at: **%localappdata%\Microsoft\MSIP\Scanner\Reports**
7. If you need to remove a repository or an entire content scan job, use the following cmdlets:

    - [Remove-ScannerContentScan](/en-us/powershell/module/purviewinformationprotection/remove-scannercontentscan)
    - [Remove-ScannerRepository](/en-us/powershell/module/purviewinformationprotection/remove-scannerrepository)

### Restriction: You cannot be granted Sysadmin or databases must be created and configured manually

Use the following procedures to manually create databases and grant the **db\_owner** role, as needed.

- Procedure for the scanner database

If you can be granted the Sysadmin role *temporarily* to install the scanner, you can remove this role when the scanner installation is complete.

Do one of the following, depending on your organization's requirements:

| Restriction | Description |
| --- | --- |
| **You can have the Sysadmin role temporarily** | If you temporarily have the Sysadmin role, the database is automatically created for you and the service account for the scanner is automatically granted the required permissions. However, the user account that configures the scanner still requires the **db\_owner** role for the scanner configuration database. If you only have the Sysadmin role until the scanner installation is complete, grant the **db\_owner** role to the user account manually. |
| **You cannot have the Sysadmin role at all** | If you cannot be granted the Sysadmin role even temporarily, you must ask a user with Sysadmin rights to manually create a database before you install the scanner. For this configuration, the **db\_owner** role must be assigned to the following accounts: - Service account for the scanner- User account for the scanner installation- User account for scanner configuration Typically, you will use the same user account to install and configure the scanner. If you use different accounts, they both require the **db\_owner** role for the scanner configuration database. Create this user and rights as needed. If you specify your own cluster name, the configuration database is named **AIPScannerUL\_&lt;cluster\_name&gt;**. |

Additionally:

- You must be a local administrator on the server that will run the scanner
- The service account that will run the scanner must be granted Full Control permissions to the following registry keys:

    - `HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\MSIPC\Server`
    - `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\MSIPC\Server`

If, after configuring these permissions, you see an error when you install the scanner, the error can be ignored and you can manually start the scanner service.

#### Manually create a database and user for the scanner, and grant db\_owner rights

If you need to manually create your scanner database and/or create a user and grant **db\_owner** rights on the database, ask your Sysadmin to perform the following steps:

1. Create a database for scanner:

    ```sql
    **CREATE DATABASE AIPScannerUL_[clustername]**
    
    **ALTER DATABASE AIPScannerUL_[clustername] SET TRUSTWORTHY ON**
    ```
2. Grant rights to the user that runs the installation command and is used to run scanner management commands. Use the following script:

    ```sql
    if not exists(select * from master.sys.server_principals where sid = SUSER_SID('domain\user')) BEGIN declare @T nvarchar(500) Set @T = 'CREATE LOGIN ' + quotename('domain\user') + ' FROM WINDOWS ' exec(@T) END
    USE DBName IF NOT EXISTS (select * from sys.database_principals where sid = SUSER_SID('domain\user')) BEGIN declare @X nvarchar(500) Set @X = 'CREATE USER ' + quotename('domain\user') + ' FROM LOGIN ' + quotename('domain\user'); exec sp_addrolemember 'db_owner', 'domain\user' exec(@X) END
    ```
3. Grant rights to scanner service account. Use the following script:

    ```sql
    if not exists(select * from master.sys.server_principals where sid = SUSER_SID('domain\user')) BEGIN declare @T nvarchar(500) Set @T = 'CREATE LOGIN ' + quotename('domain\user') + ' FROM WINDOWS ' exec(@T) END
    ```

### Restriction: The service account for the scanner cannot be granted the **Log on locally** right

If your organization policies prohibit the **Log on locally** right for service accounts, use the *OnBehalfOf* parameter with Set-Authentication.

For more information, see [Run information protection labeling cmdlets unattended](/en-us/powershell/azure/aip/setup-information-protection-client-powershell#run-information-protection-labeling-cmdlets-unattended).

### Restriction: The scanner service account cannot be synchronized to Microsoft Entra ID but the server has internet connectivity

You can have one account to run the scanner service and use another account to authenticate to Microsoft Entra ID:

- **For the scanner service account**, use a local Windows account or an Active Directory account.
- **For the Microsoft Entra account**, specify the Microsoft Entra user in the [Set-Authentication](/en-us/powershell/module/purviewinformationprotection/set-authentication) cmdlet, in the *DelegatedUser* parameter.

    If you are running the scan under any user other than the scanner account, make sure to specify the scanner account in *OnBehalfOf* parameter as well.

    For more information, see [Run information protection labeling cmdlets unattended](/en-us/powershell/azure/aip/setup-information-protection-client-powershell#run-information-protection-labeling-cmdlets-unattended).

### Restriction: Your labels do not have auto-labeling conditions

If your labels do not have any auto-labeling conditions, plan to use one of the following options when configuring your scanner:

| Option | Description |
| --- | --- |
| **Discover all info types** | In your [content scan job](deploy-scanner-configure-install#create-a-content-scan-job), set the **Info types to be discovered** option to **All**. This option sets the content scan job to scan your content for all sensitive information types. |
| **Use recommended labeling** | In your [content scan job](deploy-scanner-configure-install#create-a-content-scan-job), set the **Treat recommended labeling as automatic** option to **On**. This setting configures the scanner to automatically apply all recommended labels on your content. |
| **Define a default label** | Define a default label in your [policy](sensitivity-labels#what-label-policies-can-do), [content scan job](deploy-scanner-configure-install#create-a-content-scan-job), or [repository](deploy-scanner-configure-install#apply-a-default-label-to-all-files-in-a-data-repository). In this case the scanner applies the default label on all files found. |