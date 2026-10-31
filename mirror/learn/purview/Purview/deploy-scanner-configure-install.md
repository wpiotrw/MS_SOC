---
layout: Conceptual
title: Configure and install the Microsoft Purview Information Protection scanner | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/deploy-scanner-configure-install
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords: 
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-01-27T00:00:00.0000000Z
audience: Admin
ms.topic: install-set-up-deploy
ms.service: purview
ms.subservice: purview-information-protection
ms.collection:
- purview-compliance
description: Learn how to install and configure the Microsoft Purview Information Protection scanner to discover, classify, and protect files on data stores.
locale: en-us
document_id: 148fa7e5-4ec7-0aed-7c18-aeadb8dab7e2
document_version_independent_id: 148fa7e5-4ec7-0aed-7c18-aeadb8dab7e2
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/deploy-scanner-configure-install.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: deploy-scanner-configure-install
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/deploy-scanner-configure-install.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/5cf46315-b33f-4e99-8224-a1592697eff9
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/715d24c3-3683-4219-82c5-1e3c813fb7fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: ad0dcde3-4202-dc92-3566-446cef844968
---

# Configure and install the Microsoft Purview Information Protection scanner | Microsoft Learn

This article describes how to configure and install the Microsoft Purview Information Protection scanner, formerly named *Azure Information Protection unified labeling scanner*, or the on-premises scanner.

Tip

While most customers will perform these procedures in the admin portal, you may need to work in PowerShell only.

For example, if you are working in an environment without access to the admin portal, such as [Azure China 21Vianet](/en-us/azure/information-protection/parity-between-azure-information-protection), follow the instructions in Use PowerShell to configure the scanner.

## Overview

Before you start, verify that your system complies with the [required prerequisites](deploy-scanner-prereqs).

Then, use the following steps to configure and install the scanner:

1. Configure the scanner settings
2. Install the scanner
3. Get a Microsoft Entra token for the scanner
4. Configure the scanner to apply classification and protection

Next, perform the following configuration procedures as needed for your system:

| Procedure | Description |
| --- | --- |
| Change which file types to protect | You may want to scan, classify, or protect different file types than the default. For more information, see [The scanning process](deploy-scanner#the-scanning-process). |
| Upgrading your scanner | Upgrade your scanner to use the latest features and improvements. |
| Editing data repository settings in bulk | Use import and export options to make changes in bulk for multiple data repositories. |
| Use the scanner with alternative configurations | Use the scanner without configuring labels with any conditions |
| Optimize performance | Guidance to optimize your scanner performance |

If you don't have access to the scanner pages in the Microsoft Purview portal, configure any scanner settings in PowerShell only. For more information, see Use PowerShell to configure the scanner and Supported PowerShell cmdlets.

## Configure the scanner settings

Before you install the scanner, or upgrade it from an older general availability version, configure or verify your scanner settings. For this configuration, you can use either the [Microsoft Purview portal](purview-portal).

**To configure your scanner in the Microsoft Purview portal:**

1. Sign in using one of the following roles:

- **Compliance Administrator**
    - **Compliance Data Administrator**
    - **Security Administrator**
    - **Organization Management**

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Settings** card &gt; **Information Protection** &gt; **Information protection scanner**.
2. Create a scanner cluster. This cluster defines your scanner and is used to identify the scanner instance, such as during installation, upgrades, and other processes.
3. Create a content scan job to define the repositories you want to scan.

### Create a scanner cluster

**To create a scanner cluster in the Microsoft Purview portal:**

1. From the tabs on the **Information protection scanner** page, select **Clusters**.
2. On the **Clusters** tab, select **Add**![add icon](media/i-add.png).
3. On the **New cluster** pane, enter a meaningful name for the scanner, and an optional description.

    The cluster name is used to identify the scanner's configurations and repositories. For example, you might enter **Europe** to identify the geographical locations of the data repositories you want to scan.

    You'll use this name later on to identify where you want to install or upgrade your scanner.
4. Select **Save** to save your changes.

### Create a content scan job

Deep dive into your content to scan specific repositories for sensitive content.

**To create your content scan job on the Microsoft Purview portal:**

1. From the tabs on the **Information protection scanner** page, select **Content scan jobs**.
2. On the **Content scan jobs** pane, select **Add**![add icon](media/i-add.png).
3. For this initial configuration, configure the following settings, and then select **Save**.

    | Setting | Description |
    | --- | --- |
    | **Content scan job settings** | - **Schedule**: Keep the default of **Manual**- **Info types to be discovered**: Change to **Policy only** |
    | **DLP policy** | If you're using a data loss prevention policy, set **Enable DLP rules** to **On**. For more information, see Use a DLP policy. |
    | **Sensitivity policy** | - **Enforce sensitivity labeling policy**: Select **Off**- **Label files based on content**: Keep the default of **On**- **Default label**: Keep the default of **Policy default**- **Relabel files**: Keep the default of **Off** |
    | **Configure file settings** | - **Preserve "Date modified", "Last modified" and "Modified by"**: Keep the default of **On**- **File types to scan**: Keep the default file types for **Exclude**- **Default owner**: Keep the default of **Scanner Account** - **Set repository owner**: Use this option only when using a DLP policy. |
    |  |  |
4. Open the content scan job that was saved, and select the **Repositories** tab to specify the data stores to be scanned.

    Specify UNC paths and SharePoint Server URLs for SharePoint on-premises document libraries and folders.

    Note

    SharePoint Server Subscription Edition (SPSE) with a Public Update (PU) in extended support are supported for SharePoint. For more information see the SharePoint Server Support Policy [updated product servicing policy for SharePoint Server SE](/en-us/sharepoint/product-servicing-policy/updated-product-servicing-policy-for-sharepoint-server-se#policy-overview).

    To add your first data store, while on the **Repositories** tab:

    1. On the **Repositories** pane, select **Add**:
    2. On the **Repository** pane, specify the path for the data repository, and then select **Save**.

        - For a network share, use `\\Server\Folder`.
        - For a SharePoint library, use `http://sharepoint.contoso.com/Shared%20Documents/Folder`.
        - For a local path: `C:\Folder`
        - For a UNC path: `\\Server\Folder`

    Note

    Wildcards are not supported and WebDav locations are not supported. Scanning of OneDrive locations as repositories is not supported.

    If you add a SharePoint path for **Shared Documents**:

    - Specify **Shared Documents** in the path when you want to scan all documents and all folders from Shared Documents. For example: `http://sp013/SharedDocuments`
    - Specify **Documents** in the path when you want to scan all documents and all folders from a subfolder under Shared Documents. For example: `http://sp013/Documents/SalesReports`
    - Or, specify only the **FQDN** of your SharePoint, for example `http://sp013` to [discover and scan all SharePoint sites and subsites under a specific URL](deploy-scanner-prereqs#discover-and-scan-all-sharepoint-sites-and-subsites-under-a-specific-url) and subtitles under this URL. Grant scanner **Site Collector Auditor** rights to enable this.

    For the remaining settings on this pane, don't change them for this initial configuration, but keep them as **Content scan job default**. The default setting means that the data repository inherits the settings from the content scan job.

    Use the following syntax when adding SharePoint paths:

    | Path | Syntax |
    | --- | --- |
    | **Root path** | `http://<SharePoint server name>`Scans all sites, including any site collections allowed for the scanner user. Requires [additional permissions](deploy-scanner-prereqs#discover-and-scan-all-sharepoint-sites-and-subsites-under-a-specific-url) to automatically discover root content |
    | **Specific SharePoint subsite or collection** | One of the following: - `http://<SharePoint server name>/<subsite name>`- `http://SharePoint server name>/<site collection name>/<site name>`Requires [additional permissions](deploy-scanner-prereqs#discover-and-scan-all-sharepoint-sites-and-subsites-under-a-specific-url) to automatically discover site collection content |
    | **Specific SharePoint library** | One of the following: - `http://<SharePoint server name>/<library name>`- `http://SharePoint server name>/.../<library name>` |
    | **Specific SharePoint folder** | `http://<SharePoint server name>/.../<folder name>` |
    |  |  |
5. Repeat the previous steps to add as many repositories as needed.

You're now ready to install the scanner with the content scanner job that you've created. Continue with Install the scanner.

## Install the scanner

After you've configured the scanner, perform the following steps to install the scanner. This procedure is performed fully in PowerShell.

1. Sign in to the Windows Server computer that will run the scanner. Use an account that has local administrator rights and that has permissions to write to the SQL Server master database.

    Important

    You must have the information protection client installed on your machine before installing the scanner.

    For more information, see [Prerequisites for installing and deploying the information protection scanner](deploy-scanner-prereqs).
2. Open a Windows PowerShell session with the **Run as an administrator** option.
3. Run the [Install-Scanner](/en-us/powershell/module/purviewinformationprotection/install-scanner) cmdlet, specifying your SQL Server instance on which to create a database for the information protection scanner, and the scanner cluster name that you specified in the preceding section:

    ```PowerShell
    Install-Scanner -SqlServerInstance <name> -Cluster <cluster name>
    ```

    Examples, using the scanner cluster name of **Europe**:

    - For a default instance: `Install-Scanner -SqlServerInstance SQLSERVER1 -Cluster Europe`
    - For a named instance: `Install-Scanner -SqlServerInstance SQLSERVER1\SCANNER -Cluster Europe`
    - For SQL Server Express: `Install-Scanner -SqlServerInstance SQLSERVER1\SQLEXPRESS -Cluster Europe`

    When you're prompted, provide the Active Directory credentials for the scanner service account.

    Use the following syntax: `domain\username`. For example: `contoso\scanneraccount`

    Important

    At this prompt, enter the on-premises Windows identity in `DOMAIN\username` format (not a UPN such as `scanneraccount@contoso.com`). The installer needs this format to resolve the SID, grant **Log on as a service**, configure the Windows service Run As account, and grant SQL permissions; using a UPN can lead to later identity-resolution or service-startup issues.

    Note

    To enable cluster-level scanner features (such as [Custom Reporting](deploy-scanner-custom-reporting)) at install time, add the `-FeatureSettings` parameter (preview). For example: `Install-Scanner -SqlServerInstance SQLSERVER1 -Cluster Europe -FeatureSettings @{CustomReporting=$true}`. For more information, see [Scanner feature control (preview)](deploy-scanner-feature-control).
4. Verify that the service is now installed by using **Administrative Tools** &gt; **Services**.

    The installed service is named **Microsoft Purview Information Protection Scanner** and is configured to run by using the scanner service account that you created.

Now that you've installed the scanner, you need to get a Microsoft Entra token for the scanner service account to authenticate, so that the scanner can run unattended.

## Get a Microsoft Entra token for the scanner

A Microsoft Entra token allows the scanner to authenticate to the Microsoft Purview Information Protection Scanner service, enabling the scanner to run unattended.

For more information, see [Run information protection labeling cmdlets unattended](/en-us/powershell/azure/aip/setup-information-protection-client-powershell#run-information-protection-labeling-cmdlets-unattended).

Note

Support for certificate-based authentication is in public preview. For more information, see Certificate-based authentication

**To get a Microsoft Entra token**:

1. Navigate to the Azure Portal and proceed to the **Microsoft Entra ID** Blade.
2. In the Microsoft Entra ID side pane, click **App Registrations**.
3. At the top, go ahead and click **+ New registration**.
4. In the Name section type in **InformationProtectionScanner**.
5. Leave **Supported account types** as default.
6. For the Redirect URI, leave the type as Web but type in **http://localhost** for the entry portion and click **Register**.
7. On the Overview page of this application, note down in your text editor of choice the following IDs: **Application (client) ID** and **Directory (tenant) ID**. You will need this later when setting up the Set-AIPAuthentication command.
8. On the side pane, navigate to **Certificates and Secrets**.
9. Click on **+ New client secret**.
10. In the dialog box that shows up, enter a description for your secret and set it to Expire **In 1 year** and then Add the secret.
11. You should see now under the client secrets section that there is an entry with the **Secret Value**. Go ahead and copy this value and store it in the file where you saved the Client ID and Tenant ID. This is the only time you will be able to see the secret value, it will not be recoverable if you don't copy it at this time.
12. On the side pane, navigate to **API Permissions**.
13. Go ahead and select **Add a permission**.
14. When the screen shows, select **Azure Rights Management Service**. Then select **Application Permissions**.
15. Click the drop down for **Content** and put checkmarks down for **Content.DelegatedReader** and **Content.DelegatedWriter**. Then at the bottom of the screen, click **Add Permissions**.
16. Navigate back the **API Permissions** section and add another permission.
17. This time, for the Select an API section, click on **APIs my organization uses**. In the search bar, type in **Microsoft Information Protection Sync Service** and select it.
18. Select **Application Permissions** and then in the **Unified Policy** drop down, checkmark the permission **UnifiedPolicy.Tenant.Read**. Then at the bottom of the screen, click **Add Permissions**.
19. Back on the **API Permissions** screen, click **Grant Admin Consent** and look for the operation being successful (signified by a green checkmark).
20. From the Windows Server computer, if your scanner service account has been granted the **Log on locally** right for the installation, sign in with this account and start a PowerShell session.

    Run [Set-Authentication](/en-us/powershell/module/purviewinformationprotection/set-authentication), specifying the values that you copied from the previous step:

    ```PowerShell
    Set-Authentication -AppId <ID of the registered app> -AppSecret <client secret sting> -TenantId <your tenant ID> -DelegatedUser <Microsoft Entra account>
    ```

    For example:

    ```PowerShell
    $pscreds = Get-Credential CONTOSO\scanner
    Set-Authentication -AppId "00001111-aaaa-2222-bbbb-3333cccc4444" -AppSecret "Aa1Bb~2Cc3.-Dd4Ee5Ff6Gg7Hh8Ii9_Jj0Kk1Ll2" -DelegatedUser scanner@contoso.com -TenantId "aaaabbbb-0000-cccc-1111-dddd2222eeee" -OnBehalfOf $pscreds
    Acquired application access token on behalf of CONTOSO\scanner.
    ```

Tip

If your scanner service account cannot be granted the **Log on locally** right for the installation, use the *OnBehalfOf* parameter with [Set-Authentication](/en-us/powershell/module/purviewinformationprotection/set-authentication), as described in as described in [Run information protection labeling cmdlets unattended](/en-us/powershell/azure/aip/setup-information-protection-client-powershell#run-information-protection-labeling-cmdlets-unattended).

The scanner now has a token to authenticate to Microsoft Entra ID. This token is valid for one year, two years, or never, according to your configuration of the **Web app /API** client secret in Microsoft Entra ID. When the token expires, you must repeat this procedure.

Continue using one of the following steps, depending on whether you're using the Microsoft Purview portal to configure your scanner, or PowerShell only:

# [Admin portal only](#tab/azure-portal-only)
You're now ready to run your first scan in discovery mode. For more information, see [Run a discovery cycle and view reports for the scanner](deploy-scanner-manage#run-a-discovery-cycle-and-view-reports-for-the-scanner).

Once you've run your initial discovery scan, continue with Configure the scanner to apply classification and protection.

# [PowerShell only](#tab/powershell-only)
If you are configuring and installing your scanner using PowerShell instead of the scanner pages in the Microsoft Purview portal, continue with step 5 in Use PowerShell to configure the scanner.

Then:

- [Run a discovery cycle and view reports for the scanner](deploy-scanner-manage#run-a-discovery-cycle-and-view-reports-for-the-scanner)
- Use PowerShell to configure the scanner to apply classification and protection
- Use PowerShell to configure a DLP policy with the scanner

---

For more information, see [Run information protection labeling cmdlets unattended](/en-us/powershell/azure/aip/setup-information-protection-client-powershell#run-information-protection-labeling-cmdlets-unattended).

## Configure the scanner to apply classification and protection

The default settings configure the scanner to run once, and in reporting-only mode. To change these settings, edit the content scan job.

Tip

If you're working in PowerShell only, see Configure the scanner to apply classification and protection - PowerShell only.

**To configure the scanner to apply classification and protection in the Microsoft Purview portal:**:

1. In the Microsoft Purview portal, on the **Content scan jobs** tab, select a specific content scan job to edit it.
2. Select the content scan job, change the following, and then select **Save**:

    - From the **Content scan job** section: Change the **Schedule** to **Always**
    - From the **Enforce sensitivity labeling policy** section: Change the radio button to **On**
3. Make sure a node for the content scan job is online, then start the content scan job again by selecting **Scan now**. The **Scan now** button only appears when a node for the selected content scan job is online.

The scanner is now scheduled to run continuously. When the scanner works its way through all configured files, it automatically starts a new cycle so that any new and changed files are discovered.

## Use a DLP policy

Using a data loss prevention policy enables the scanner to detect potential data leaks by matching DLP rules to files stored in file shares and SharePoint Server.

- **Enable DLP rules in your content scan job** to reduce the exposure of any files that match your DLP policies. When your DLP rules are enabled, the scanner may reduce file access to data owners only, or reduce exposure to network-wide groups, such as **Everyone**, **Authenticated Users**, or **Domain Users**.
- **In the Microsoft Purview portal**, determine whether you are just testing your DLP policy or whether you want your rules enforced and your file permissions changed according to those rules. For more information, see [Create and Deploy data loss prevention policies](dlp-create-deploy-policy)

DLP policies are configured in the Microsoft Purview portal. For more information about DLP licensing, see [Get started with the data loss prevention on-premises scanner](dlp-on-premises-scanner-get-started).

Tip

Scanning your files, even when just testing the DLP policy, also creates file permission reports. Query these reports to investigate specific file exposures or explore the exposure of a specific user to scanned files.

To use PowerShell only, see Use a DLP policy with the scanner - PowerShell only.

**To use a DLP policy with the scanner in the Microsoft Purview portal**:

1. In the Microsoft Purview portal, navigate to the **Content scan jobs** tab and select a specific content scan job. For more information, see Create a content scan job.
2. Under **Enable DLP policy rules**, set the radio button to **On**.

    Important

    Do not set **Enable DLP rules** to **On** unless you actually have a DLP policy configured in Microsoft 365.

    Turning this feature on without a DLP policy will cause the scanner to generate errors.
3. (Optional) Set the **Set repository owner** to **On**, and define a specific user as the repository owner.

    This option enables the scanner to reduce the exposure of any files found in this repository, which match the DLP policy, to the repository owner defined.

### DLP policies and *make private* actions

If you are using a DLP policy with a *make private* action, and are also planning to use the scanner to automatically label your files, we recommend that you also define the unified labeling client's [**UseCopyAndPreserveNTFSOwner**](/en-us/powershell/exchange/client-advanced-settings#usecopyandpreserventfsowner) advanced setting.

This setting ensures that the original owners retain access to their files.

For more information, see Create a content scan job and [Automatically apply a sensitivity label to Microsoft 365 data](apply-sensitivity-label-automatically).

## Change which file types to protect

By default the scanner protects Office file types and PDF files only.

Use PowerShell commands to change this behavior as needed, such as to configure the scanner to protect all file types, just as the client does, or to protect additional, specific file types.

For a label policy that applies to the user account downloading labels for the scanner, specify a PowerShell advanced setting named **PFileSupportedExtensions**.

For a scanner that has access to the internet, this user account is the account that you specify for the *DelegatedUser* parameter with the Set-Authentication command.

**Example 1**: PowerShell command for the scanner to protect all file types, where your label policy is named "Scanner":

```PowerShell
Set-LabelPolicy -Identity Scanner -AdvancedSettings @{PFileSupportedExtensions="*"}
```

**Example 2**: PowerShell command for the scanner to protect .xml files and .tiff files in addition to Office files and PDF files, where your label policy is named "Scanner":

```PowerShell
Set-LabelPolicy -Identity Scanner -AdvancedSettings @{PFileSupportedExtensions=ConvertTo-Json(".xml", ".tiff")}
```

For more information, see [Change which file types to protect](/en-us/powershell/exchange/client-advanced-settings#pfilesupportedextensions).

## Upgrade your scanner

If you've previously installed the scanner and want to upgrade, use the instructions described in [Upgrade the Microsoft Purview Information Protection scanner](upgrade-scanner-migrate).

Then, [configure](deploy-scanner-configure-install) and [use your scanner](deploy-scanner-manage) as usual, skipping the steps to install your scanner.

## Edit data repository settings in bulk

Use the **Export** and **Import** buttons to make changes for your scanner across several repositories.

This way, you don't need to make the same changes several times, manually, in the Microsoft Purview portal.

For example, if you've a new file type on several SharePoint data repositories, you may want to update the settings for those repositories in bulk.

**To make changes in bulk across repositories in the Microsoft Purview portal:**

1. In the Microsoft Purview portal, select a specific content scan job and navigate to the **Repositories** tab within the pane. Select the **Export** option.
2. Manually edit the exported file to make your change.
3. Use the **Import** option on the same page to import the updates back across your repositories.

## Use the scanner with alternative configurations

The scanner usually looks for conditions specified for your labels in order to classify and protect your content as needed.

In the following scenarios, the scanner is also able to scan your content and manage labels, without any conditions configured:

- Apply a default label to all files in a data repository
- Remove existing labels from all files in a data repository
- Identify all custom conditions and known sensitive information types

### Apply a default label to all files in a data repository

In this configuration, all unlabeled files in the repository are labeled with the default label specified for the repository or the content scan job. Files are labeled without inspection.

Configure the following settings:

| Setting | Description |
| --- | --- |
| **Label files based on content** | Set to **Off** |
| **Default label** | Set to **Custom**, and then select the label to use |
| **Enforce default label** | Select to have the default label applied to all files, even if they're already labeled by turning **Relabel files** and **Enforce default label** on |

### Remove existing labels from all files in a data repository

In this configuration, all existing labels are removed, including protection, if protection was applied with the label. Protection applied independently of a label is retained.

Configure the following settings:

| Setting | Description |
| --- | --- |
| **Label files based on content** | Set to **Off** |
| **Default label** | Set to **None** |
| **Relabel files** | Set to **On**, with the **Enforce default label** set to **On** |

### Identify all custom conditions and known sensitive information types

This configuration enables you to find sensitive information that you might not realize you had, at the expense of scanning rates for the scanner.

Set the **Info types to be discovered** to **All**.

To identify conditions and information types for labeling, the scanner uses any custom sensitive information types specified, and the list of built-in sensitive information types that are available to select, as defined in your labeling management center.

Important

**Sublabels under the same parent share the parent label’s priority**, switching between sublabels under the same parent label isn’t considered a downgrade. Therefore, **Allow label downgrade = Off** won’t block files from relabeled with lower priority sublabels when **Relabel files** is enabled.

## Optimize scanner performance

Note

If you're looking to improve the responsiveness of the scanner computer rather than the scanner performance, use an advanced client setting to [limit the number of threads used by the scanner](/en-us/powershell/exchange/client-advanced-settings#scannerconcurrencylevel).

Use the following options and guidance to help you optimize scanner performance:

| Option | Description |
| --- | --- |
| **Have a high speed and reliable network connection between the scanner computer and the scanned data store** | For example, place the scanner computer in the same LAN, or preferably, in the same network segment as the scanned data store. The quality of the network connection affects the scanner performance because, to inspect the files, the scanner transfers the contents of the files to the computer running the scanner Microsoft Purview Information Protection Scanner service. Reducing or eliminating the network hops required for the data to travel also reduces the load on your network. |
| **Make sure the scanner computer has available processor resources** | Inspecting the file contents and encrypting and decrypting files are processor-intensive actions. Monitor the typical scanning cycles for your specified data stores to identify whether a lack of processor resources is negatively affecting the scanner performance. |
| **Install multiple instances of the scanner** | The scanner supports multiple configuration databases on the same SQL server instance when you specify a custom cluster name for the scanner. **Tip**: Multiple scanners can also share the same cluster, resulting in quicker scanning times. If you plan to install the scanner on multiple machines with the same database instance, and want your scanners to run in parallel, you must install all your scanners using the same cluster name. |
| **Check your alternative configuration usage** | The scanner runs more quickly when you use the alternative configuration to apply a default label to all files because the scanner doesn't inspect the file contents. The scanner runs more slowly when you use the alternative configuration to identify all custom conditions and known sensitive information types. |

### Additional factors that affect performance

Additional factors that affect the scanner performance include:

| Factor | Description |
| --- | --- |
| **Load/response times** | The current load and response times of the data stores that contain the files to scan will also affect scanner performance. |
| **Scanner mode** (Discovery / Enforce) | Discovery mode typically has a higher scanning rate than enforce mode. Discovery requires a single file read action, whereas enforce mode requires read and write actions. |
| **Policy changes** | Your scanner performance may be affected if you've made changes to the autolabeling in the label policy. Your first scan cycle, when the scanner must inspect every file, will take longer than subsequent scan cycles that by default, inspect only new and changed files. If you change the conditions or autolabeling settings, all files are scanned again. For more information, see [Rescanning files](deploy-scanner-manage#rescanning-files). |
| **Regex constructions** | Scanner performance is affected by how your regex expressions for custom conditions are constructed.  To avoid heavy memory consumption and the risk of timeouts (15 minutes per file), review your regex expressions for efficient pattern matching. For example: - Avoid [greedy quantifiers](/en-us/dotnet/standard/base-types/quantifiers-in-regular-expressions)- Use non-capturing groups such as `(?:expression)` instead of `(expression)` |
| **Log level** | Log level options include **Debug**, **Info**, **Error** and **Off** for the scanner reports.- **Off** results in the best performance - **Debug** considerably slows down the scanner and should be used only for troubleshooting. For more information, see the *ReportLevel* parameter for the [Set-ScannerConfiguration](/en-us/powershell/module/purviewinformationprotection/set-scannerconfiguration) cmdlet. |
| **Files being scanned** | - With the exception of Excel files, Office files are more quickly scanned than PDF files. - Unprotected files are quicker to scan than protected files. - Large files obviously take longer to scan than small files. |

## Use PowerShell to configure the scanner

This section describes the steps required to configure and install the scanner when you don't have access to the scanner pages in the Microsoft Purview portal, and must use PowerShell only.

Important

- Some steps require Powershell whether or not you are able to access the scanner pages in the Microsoft Purview portal, and are identical. For these steps, see the earlier instructions in this article as indicated.
- If you're working with the scanner for Azure China 21Vianet, additional steps are required in addition to the instructions detailed here. For more information, see [Microsoft Purview Information Protection for Office 365 operated by 21Vianet](/en-us/azure/information-protection/parity-between-azure-information-protection).

For more information, see Supported PowerShell cmdlets.

**To configure and install your scanner**:

1. Start with PowerShell closed. If you've previously installed the information protection client and scanner, make sure that the **Microsoft Purview Information Protection Scanner** service is stopped.
2. Open a Windows PowerShell session with the **Run as an administrator** option.
3. Run the [Install-Scanner](/en-us/powershell/module/purviewinformationprotection/install-scanner) command to install your scanner on your SQL server instance, with the **Cluster** parameter to define your cluster name.

    This step is identical whether or not you're able to access the scanner pages in the Microsoft Purview portal. For more information, see the earlier instructions in this article: Install the scanner
4. Get an Azure token to use with your scanner, and then reauthenticate.

    This step is identical whether or not you're able to access the scanner pages in the Microsoft Purview portal. For more information, see the earlier instructions in this article: Get a Microsoft Entra token for the scanner.
5. Run the [Set-ScannerConfiguration](/en-us/powershell/module/purviewinformationprotection/set-scannerconfiguration) cmdlet to set the scanner to function in offline mode. Run:

    ```powershell
    Set-ScannerConfiguration -OnlineConfiguration Off
    ```
6. Run the [Set-ScannerContentScan](/en-us/powershell/module/purviewinformationprotection/set-scannercontentscan) cmdlet to create a default content scan job.

    The only required parameter in the **Set-ScannerContentScan** cmdlet is **Enforce**. However, you might want to define other settings for your content scan job at this time. For example:

    ```powershell
    Set-ScannerContentScan -Schedule Manual -DiscoverInformationTypes PolicyOnly -Enforce Off -DefaultLabelType PolicyDefault -RelabelFiles Off -PreserveFileDetails On -IncludeFileTypes '' -ExcludeFileTypes '.msg,.tmp' -DefaultOwner <account running the scanner>
    ```

    The syntax above configures the following settings while you continue the configuration:

    - Keeps the scanner run scheduling to *manual*
    - Sets the information types to be discovered based on the sensitivity label policy
    - Does *not* enforce a sensitivity label policy
    - Automatically labels files based on content, using the default label defined for the sensitivity label policy
    - Does *not* allow for relabeling files
    - Preserves file details while scanning and auto-labeling, including *date modified*, *last modified*, and *modified by* values
    - Sets the scanner to exclude .msg and .tmp files when running
    - Sets the default owner to the account you want to use when running the scanner
7. Use the [Add-ScannerRepository](/en-us/powershell/module/purviewinformationprotection/add-scannerrepository) cmdlet to define the repositories you want to scan in your content scan job. For example, run:

    ```powershell
    Add-ScannerRepository -OverrideContentScanJob Off -Path 'c:\repoToScan'
    ```

    Use one of the following syntaxes, depending on the type of repository you're adding:

    - For a network share, use `\\Server\Folder`.
    - For a SharePoint library, use `http://sharepoint.contoso.com/Shared%20Documents/Folder`.
    - For a local path: `C:\Folder`
    - For a UNC path: `\\Server\Folder`

    Note

    Wildcards are not supported and WebDav locations are not supported.

    To modify the repository later on, use the [Set-ScannerRepository](/en-us/powershell/module/purviewinformationprotection/set-scannerrepository) cmdlet instead.

    If you add a SharePoint path for **Shared Documents**:

    - Specify **Shared Documents** in the path when you want to scan all documents and all folders from Shared Documents. For example: `http://sp2013/SharedDocuments`
    - Specify **Documents** in the path when you want to scan all documents and all folders from a subfolder under Shared Documents. For example: `http://sp2013/Documents/SalesReports`
    - Or, specify only the **FQDN** of your SharePoint, for example `http://sp2013` to [discover and scan all SharePoint sites and subsites under a specific URL](deploy-scanner-prereqs#discover-and-scan-all-sharepoint-sites-and-subsites-under-a-specific-url) and subtitles under this URL. Grant scanner **Site Collector Auditor** rights to enable this.

    Use the following syntax when adding SharePoint paths:

    | Path | Syntax |
    | --- | --- |
    | **Root path** | `http://<SharePoint server name>`Scans all sites, including any site collections allowed for the scanner user. |
    | **Specific SharePoint subsite or collection** | One of the following: - `http://<SharePoint server name>/<subsite name>`- `http://SharePoint server name>/<site collection name>/<site name>` |
    | **Specific SharePoint library** | One of the following: - `http://<SharePoint server name>/<library name>`- `http://SharePoint server name>/.../<library name>` |
    | **Specific SharePoint folder** | `http://<SharePoint server name>/.../<folder name>` |

Continue with the following steps as needed:

- [Configuration for customers in China](/en-us/microsoft-365/admin/services-in-china/parity-between-azure-information-protection)
- [Run a discovery cycle and view reports for the scanner](deploy-scanner-manage#run-a-discovery-cycle-and-view-reports-for-the-scanner)
- Use PowerShell to configure the scanner to apply classification and protection
- Use PowerShell to configure a DLP policy with the scanner

### Use PowerShell to configure the scanner to apply classification and protection

1. Run the [Set-ScannerContentScan](/en-us/powershell/module/purviewinformationprotection/set-scannercontentscan) cmdlet to update your content scan job to set your scheduling to always and enforce your sensitivity policy.

    ```powershell
    Set-ScannerContentScan -Schedule Always -Enforce On
    ```

    Tip

    You may want to change other settings on this pane, such as whether file attributes are changed and whether the scanner can relabel files. For more information about the settings available, see the full [Set-ScannerContentScan documentation](/en-us/powershell/module/purviewinformationprotection/set-scannercontentscan).
2. Run the [Start-Scan](/en-us/powershell/module/purviewinformationprotection/start-scan) cmdlet to run your content scan job:

    ```PowerShell
    Start-Scan
    ```

The scanner is now scheduled to run continuously. When the scanner works its way through all configured files, it automatically starts a new cycle so that any new and changed files are discovered.

### Use PowerShell to configure a DLP policy with the scanner

Run the [Set-ScannerContentScan](/en-us/powershell/module/purviewinformationprotection/set-scannercontentscan) cmdlet again with the **-EnableDLP** parameter set to **On**, and with a specific repository owner defined.

For example:

```powershell
Set-ScannerContentScan -EnableDLP On -RepositoryOwner 'domain\user'
```

## Certificate-based authentication (Public Preview)

### Using certificate-based authentication with the information protection scanner

This section describes how to configure the Microsoft Purview Information Protection scanner to authenticate using a certificate instead of a client secret.

### Prerequisites

Before configuring certificate-based authentication, ensure you have:

- The Microsoft Purview Information Protection scanner installed
- Administrative access to the Windows Server running the scanner
- Access to the Microsoft Entra app registration used by the scanner
- Windows PowerShell 5.1

### Step 1: Obtain or create a certificate

You have two options for obtaining a certificate:

1. **CA-issued certificate**: Request a certificate from your organization's Certificate Authority.
2. **Self-signed certificate**: Create a self-signed certificate.

#### Option A: Using a CA-issued certificate (production)

Using a CA-issued certificate provides:

- Automatic trust via the existing PKI infrastructure
- Centralized certificate lifecycle management
- Compliance with organizational security policies
- No need to skip certificate chain validation

##### Certificate requirements

When requesting a certificate from your CA, ensure it meets these requirements:

| Requirement | Value |
| --- | --- |
| Key Algorithm | RSA |
| Key Length | 2048 bits minimum (4096 recommended) |
| Key Usage | Digital Signature |
| Private Key | Exportable (for backup) or marked for the machine |
| Validity | Per your organization's policy (typically 1-2 years) |

Review documentation from your CA for specific instructions on requesting a certificate with these parameters.

After obtaining the key from your enterprise CA, install the certificate in the Local Machine store on each Windows Server running the scanner. Make sure to install the certificate in the **Personal** store of the Local Machine.

##### Exporting the public key for Microsoft Entra

After the certificate is issued and installed, export the public key:

```powershell
# Find the certificate (adjust the subject filter as needed)
$cert = Get-ChildItem Cert:\LocalMachine\My | Where-Object { $_.Subject -like "*PurviewScanner*" }
Export-Certificate -Cert $cert -FilePath "C:\temp\PurviewScanner.cer"
```

#### Option B: Using a self-signed certificate

A self-signed certificate can be created on a single server, then imported to servers across the scanner cluster.

```powershell
# Create certificate in Local Machine store with RSA provider
$cert = New-SelfSignedCertificate `
    -Subject "CN=PurviewScanner" `
    -CertStoreLocation Cert:\LocalMachine\My `
    -KeyExportPolicy Exportable `
    -KeySpec Signature `
    -KeyLength 2048 `
    -KeyAlgorithm RSA `
    -HashAlgorithm SHA256 `
    -NotAfter (Get-Date).AddYears(2) `
    -Provider "Microsoft Enhanced RSA and AES Cryptographic Provider"

# Display the certificate details
Write-Host "Certificate created successfully"
Write-Host "Thumbprint: $($cert.Thumbprint)"
Write-Host "Subject: $($cert.Subject)"
```

Important

The `-Provider "Microsoft Enhanced RSA and AES Cryptographic Provider"` parameter is required. Using CNG (Cryptography Next Generation) providers will result in "Keyset does not exist" errors when the scanner attempts to authenticate.

##### Export the public key

Export the certificate's public key to upload to Microsoft Entra:

```powershell
# Export public key certificate (.cer file)
Export-Certificate -Cert $cert -FilePath "C:\temp\PurviewScanner.cer"
```

### Step 2: Grant private key permissions to the scanner service account

The scanner service account must have permission to read the certificate's private key. Without this permission, authentication will fail with "Keyset does not exist" errors.

#### Using the Certificate Manager UI

1. Open the Local Machine certificate store:

    - Press `Win + R`, type `certlm.msc`, and press Enter
2. Navigate to **Certificates - Local Computer**
3. Right-click on the certificate you created (e.g., "PurviewScanner") and select **All Tasks** &gt; **Manage Private Keys**
4. Click **Add** and enter the scanner service account name (e.g., `CONTOSO\ScannerService`)
5. Select the account and ensure **Read** permission is checked
6. Click **OK** to save

#### Using PowerShell

Alternatively, grant permissions using PowerShell. Make sure to replace the service account name with your actual scanner service account.

```powershell
# Get the certificate
$cert = Get-ChildItem Cert:\LocalMachine\My | Where-Object { $_.Subject -eq "CN=PurviewScanner" }

# Get the private key file path
$privateKey = [System.Security.Cryptography.X509Certificates.RSACertificateExtensions]::GetRSAPrivateKey($cert)
$keyPath = $privateKey.Key.UniqueName
$fullKeyPath = "$env:ALLUSERSPROFILE\Microsoft\Crypto\RSA\MachineKeys\$keyPath"

# Get current ACL
$acl = Get-Acl $fullKeyPath

# Add read permission for the scanner service account
$serviceAccount = "CONTOSO\ScannerService"  # Replace with your scanner service account
$accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule($serviceAccount, "Read", "Allow")
$acl.AddAccessRule($accessRule)

# Apply the updated ACL
Set-Acl $fullKeyPath $acl
```

### Step 3: Upload the certificate to Microsoft Entra

Register the certificate's public key with the app registration used by the scanner.

For detailed instructions on uploading a certificate to a Microsoft Entra app registration, see [Register a certificate with Microsoft Entra](/en-us/entra/identity-platform/howto-create-service-principal-portal#option-1-recommended-upload-a-trusted-certificate-issued-by-a-certificate-authority).

After uploading, note the certificate thumbprint displayed in the portal - it should match the thumbprint from Step 1.

### Step 4: Configure the scanner to use certificate authentication

Use the `Set-Authentication` cmdlet with certificate parameters instead of the `-AppSecret` parameter.

```powershell
# Get credentials for the scanner service account
$pscreds = Get-Credential CONTOSO\ScannerService

# Set authentication using certificate thumbprint
Set-Authentication `
    -AppId "your-app-id-guid" `
    -TenantId "your-tenant-id-guid" `
    -DelegatedUser "scanner@contoso.com" `
    -CertificateThumbprint "your-certificate-thumbprint" `
    -CertificateStoreLocation LocalMachine `
    -CertificateStoreName My `
    -OnBehalfOf $pscreds
```

The certificate chain is validated automatically for certificates issued by a trusted CA. If validation fails, ensure:

- The CA's root certificate is in the Trusted Root Certification Authorities store
- Any intermediate CA certificates are in the Intermediate Certification Authorities store

Note

If you're using a self-signed certificate, add the `-SkipCertificateChainValidation` parameter to bypass chain validation, which will fail for self-signed certificates.

#### Authenticate using certificate subject name

Alternatively, you can specify the certificate by its subject name:

```powershell
# Get credentials for the scanner service account
$pscreds = Get-Credential CONTOSO\ScannerService

# Set authentication using certificate subject name
Set-Authentication `
    -AppId "your-app-id-guid" `
    -TenantId "your-tenant-id-guid" `
    -DelegatedUser "scanner@contoso.com" `
    -CertificateSubjectName "PurviewScanner" `
    -CertificateStoreLocation LocalMachine `
    -CertificateStoreName My `
    -OnBehalfOf $pscreds
```

Note

If you're using a self-signed certificate, add the `-SkipCertificateChainValidation` parameter to bypass chain validation, which will fail for self-signed certificates.

### Parameter reference

| Parameter | Description |
| --- | --- |
| `-CertificateThumbprint` | The SHA-1 thumbprint of the certificate to use for authentication. Cannot be used with `-CertificateSubjectName`. |
| `-CertificateSubjectName` | The subject name (CN) of the certificate to use for authentication. Cannot be used with `-CertificateThumbprint`. |
| `-CertificateStoreLocation` | The certificate store location. Use `LocalMachine` for the scanner service. Valid values: `CurrentUser`, `LocalMachine`. Default: `CurrentUser`. |
| `-CertificateStoreName` | The certificate store name. Default: `My` (Personal store). |
| `-SkipCertificateChainValidation` | Skips certificate chain validation. Required for self-signed certificates. |

### Troubleshooting

#### "Keyset does not exist" error

This error typically indicates one of the following issues:

1. **Private key permissions**: The scanner service account doesn't have read access to the certificate's private key. See Step 2 to grant permissions.
2. **CNG provider**: The certificate was created with a CNG provider instead of an RSA provider. Recreate the certificate using the `-Provider "Microsoft Enhanced RSA and AES Cryptographic Provider"` parameter.

#### "Certificate not found" error

Verify that:

- The thumbprint or subject name is correct
- The certificate is in the specified store (`LocalMachine\My` by default)
- The certificate has not expired

#### "A certificate chain could not be built" error

For self-signed certificates, use the `-SkipCertificateChainValidation` parameter. For CA-issued certificates, ensure the full certificate chain (including intermediate CAs) is installed on the server.

#### 401 Unauthorized or "invalid\_client" error

Verify that:

- The certificate's public key is uploaded to the correct Microsoft Entra app registration
- The app registration ID matches the `-AppId` parameter
- The certificate has not expired
- The tenant ID is correct

### Migrating from secret to certificate authentication

To migrate an existing scanner from secret-based to certificate-based authentication:

1. Create and configure the certificate as described above
2. Run `Set-Authentication` with the certificate parameters
3. The new authentication configuration will overwrite the previous secret-based configuration
4. Restart the scanner service

```powershell
# Restart the scanner service after changing authentication
Restart-Service -Name "Microsoft Purview Information Protection Scanner"
```

### See also

- [Run information protection labeling cmdlets unattended](/en-us/powershell/azure/aip/setup-information-protection-client-powershell#run-information-protection-labeling-cmdlets-unattended)
- [Register a certificate with Microsoft Entra](/en-us/entra/identity-platform/howto-create-service-principal-portal#option-1-recommended-upload-a-trusted-certificate-issued-by-a-certificate-authority)

## Supported PowerShell cmdlets

This section lists PowerShell cmdlets supported for the information protection scanner and instructions for configuring and installing the scanner with PowerShell only.

Supported cmdlets for the scanner include:

- [Add-ScannerRepository](/en-us/powershell/module/purviewinformationprotection/add-scannerrepository)
- [Clear-Authentication](/en-us/powershell/module/purviewinformationprotection/clear-authentication)
- [Export-DebugLogs](/en-us/powershell/module/purviewinformationprotection/export-debuglogs)
- [Get-FileStatus](/en-us/powershell/module/purviewinformationprotection/get-filestatus)
- [Get-ScannerConfiguration](/en-us/powershell/module/purviewinformationprotection/get-scannerconfiguration)
- [Get-ScannerContentScan](/en-us/powershell/module/purviewinformationprotection/get-scannercontentscan)
- [Get-ScannerRepository](/en-us/powershell/module/purviewinformationprotection/get-scannerrepository)
- [Get-ScanStatus](/en-us/powershell/module/purviewinformationprotection/get-scanstatus)
- [Import-ScannerConfiguration](/en-us/powershell/module/purviewinformationprotection/import-scannerconfiguration)
- [Install-Scanner](/en-us/powershell/module/purviewinformationprotection/install-scanner)
- [New-CustomPermissions](/en-us/powershell/module/purviewinformationprotection/new-custompermissions)
- [Remove-FileLabel](/en-us/powershell/module/purviewinformationprotection/remove-filelabel)
- [Remove-ScannerContentScan](/en-us/powershell/module/purviewinformationprotection/remove-scannercontentscan)
- [Remove-ScannerRepository](/en-us/powershell/module/purviewinformationprotection/remove-scannerrepository)
- [Set-Authentication](/en-us/powershell/module/purviewinformationprotection/set-authentication)
- [Set-FileLabel](/en-us/powershell/module/purviewinformationprotection/set-filelabel)
- [Set-ScannerConfiguration](/en-us/powershell/module/purviewinformationprotection/set-scannerconfiguration)
- [Set-ScannerContentScan](/en-us/powershell/module/purviewinformationprotection/set-scannercontentscan)
- [Set-ScannerDatabase](/en-us/powershell/module/purviewinformationprotection/set-scannerdatabase)
- [Set-ScannerRepository](/en-us/powershell/module/purviewinformationprotection/set-scannerrepository)
- [Start-Scan](/en-us/powershell/module/purviewinformationprotection/start-scan)
- [Start-ScannerDiagnostics](/en-us/powershell/module/purviewinformationprotection/start-scannerdiagnostics)
- [Stop-Scan](/en-us/powershell/module/purviewinformationprotection/stop-scan)
- [Uninstall-Scanner](/en-us/powershell/module/purviewinformationprotection/uninstall-scanner)
- [Update-ScannerDatabase](/en-us/powershell/module/purviewinformationprotection/update-scannerdatabase)