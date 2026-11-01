---
layout: Conceptual
title: Connect to and manage a Microsoft Fabric tenant (cross-tenant) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-fabric-tenant-cross-tenant
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: chigupta
ms.date: 2026-04-28T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ai-usage: ai-assisted
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to connect to a Microsoft Fabric tenant that's in a different tenant from your Microsoft Purview resource.
ms.custom:
- sfi-image-nochange
- sfi-ropc-nochange
locale: en-us
document_id: b0f17d91-f950-74ad-5a5d-51ba3d836dd5
document_version_independent_id: b0f17d91-f950-74ad-5a5d-51ba3d836dd5
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-fabric-tenant-cross-tenant.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-fabric-tenant-cross-tenant
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-fabric-tenant-cross-tenant.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
platformId: bb862c3f-ae17-b52b-576d-7747ab733a25
---

# Connect to and manage a Microsoft Fabric tenant (cross-tenant) | Microsoft Learn

This article outlines how to register a Microsoft Fabric tenant that's in **a different tenant** from your Microsoft Purview resource, and how to authenticate and interact with the Fabric source in Microsoft Purview. For more information about Microsoft Purview in general, read the [introductory article](purview).

Note

Scanning a Microsoft Fabric tenant brings in metadata and lineage from Fabric items, including Power BI. Learn how to [scan a Power BI tenant](register-scan-power-bi-tenant-cross-tenant). The experience of registering a Fabric tenant and setting up a scan is similar to Power BI tenant and shared among all Fabric items.

## Supported capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan | Classification | Labeling | Access Policy | Lineage | Data Sharing | Live view |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Yes | Yes | Yes | Yes | No | No | No | Yes | No | No |

| Experiences | Fabric items | Available in scan | Available in[live view](data-gov-live-view)(same tenant only) |
| --- | --- | --- | --- |
| Real-Time Analytics | Kusto Query Language (KQL) Database | Yes | Yes |
|  | KQL Queryset | Yes | Yes |
| Data Science | Experiment | Yes | Yes |
|  | ML model | Yes | Yes |
| Data Factory | Data pipeline | Yes | Yes |
|  | Dataflow Gen2 | Yes | Yes |
| Data Engineering | Lakehouse | Yes | Yes |
|  | Notebook | Yes | Yes |
|  | Spark Job Definition | Yes | Yes |
|  | SQL analytics endpoint | Yes | Yes |
| Data Warehouse | Warehouse | Yes | Yes |
| Power BI | Dashboard | Yes | Yes |
|  | Dataflow | Yes | Yes |
|  | Datamart | Yes | Yes |
|  | Semantic model (Dataset) | Yes | Yes |
|  | Report | Yes | Yes |
|  | Paginated report | Yes |  |

### Supported scenarios for Fabric scans

| **Scenarios** | **Microsoft Purview public access allowed/denied** | **Fabric public access allowed /denied** | **Runtime option** | **Authentication option** | **Deployment checklist** |
| --- | --- | --- | --- | --- | --- |
| Public access with Azure IR | Allowed | Allowed | Azure Runtime | Delegated authentication / Service principal | Review deployment checklist |
| Public access with Self-hosted IR | Allowed | Allowed | SHIR or Kubernetes SHIR | Service principal | Review deployment checklist |
| Private access | Denied | Allowed | Managed Virtual Network IR (v2 only) | Delegated authentication / Service principal | Review deployment checklist |

Note

The supported scenarios above apply for non-Power BI items in Fabric. See the [Power BI documentation](register-scan-power-bi-tenant-cross-tenant#supported-scenarios-for-power-bi-scans) for supported scenarios applicable for Power BI items.

### Known limitations

- Currently for all Fabric items besides Power BI, only item level metadata and lineage will be scanned. For Lakehouse tables and files, sub-item level metadata scanning is available but sub-item level lineage is still not supported.
- For self-hosted integration runtime, the standard self-hosted integration runtime with minimal version 5.40.8836.1 or [Kubernetes supported self-hosted integration runtime](data-map-integration-runtime-kubernetes) is supported.
- Empty workspaces are skipped.

- Unsupported Parquet encodings: Microsoft Purview doesn't support schema extraction for Parquet files that use run-length encoding (RLE) in Microsoft Fabric Lakehouse. Tables containing RLE-encoded columns might fail to extract schema metadata, including tables, columns, and data types. The process still discovers asset-level metadata (L1). To enable full schema extraction, re-create the affected tables by using a supported encoding format, such as dictionary or plain encoding.

Note

For Fabric Lakehouse tables with schema-enabled databases, the schema name and table name are combined into a single segment in the qualified name using `%252F` (double-URL-encoded forward slash) as a separator. For example, a table at the OneLake path `Tables/dbo/my_table` will appear in Data Map with the qualified name `.../tables/dbo%252Fmy_table`, while the entity display name will show only the table name (for example, `my_table`) without the schema prefix.

## Prerequisites

Before you start, make sure you have the following:

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).

### Authentication options

- Service Principal
- Delegated Authentication

## Deployment checklist

The deployment checklist is a summary of all the steps you need to take to set up a cross-tenant Fabric source. You can use it during setup or for troubleshooting, to confirm you've followed all the necessary steps to connect.

# [Public access with Azure IR](#tab/Scenario1)
### Scan cross-tenant Fabric by using delegated authentication in a public network

1. Make sure the Fabric tenant ID is entered correctly during the registration. By default, the Fabric tenant ID that exists in the same Microsoft Entra instance as Microsoft Purview will be populated.
2. Make sure your [Fabric metadata model is up to date by enabling metadata scanning](/en-us/fabric/admin/metadata-scanning-setup#enable-tenant-settings-for-metadata-scanning).
3. From the Azure portal, validate if the Microsoft Purview account network is set to **public access**.
4. From the Fabric tenant admin portal, make sure the Fabric tenant is configured to allow a public network.
5. Check your instance of Azure Key Vault to make sure:

    1. There are no typos in the password or secret.
    2. Microsoft Purview managed identity has **get** and **list** access to secrets.
6. Review your credential to validate that the:

    1. Client ID matches the *Application (Client) ID* of the app registration.
    2. For **delegated auth**, username includes the user principal name, such as `johndoe@contoso.com`.
7. In the Fabric Microsoft Entra tenant, validate the following Fabric admin user settings:

    1. The user is assigned to the Fabric administrator role.
    2. If the user is recently created, sign in with the user at least once, to make sure that the password is reset successfully, and the user can successfully initiate the session.
    3. There are no multifactor authentication or conditional access policies enforced on the user.
8. In the Fabric Microsoft Entra tenant, validate the following app registration settings:

    1. The app registration exists in your Microsoft Entra tenant where the Fabric tenant is located.
    2. If service principal is used, under **API permissions**, the following **delegated permissions**are assigned with read for the following APIs:
        - Microsoft Graph openid
        - Microsoft Graph User.Read
    3. If delegated authentication is used, under **API permissions**, the following **delegated permissions** and **grant admin consent for the tenant**is set up with read for the following APIs:
        - Power BI Service Tenant.Read.All
        - Microsoft Graph openid
        - Microsoft Graph User.Read
    4. Under **Authentication**:
        1. **Supported account types** &gt; **Accounts in any organizational directory (Any Microsoft Entra directory - Multitenant)** is selected.
        2. **Implicit grant and hybrid flows** &gt; **ID tokens (used for implicit and hybrid flows)** is selected.
        3. **Allow public client flows** is enabled.
9. In Fabric tenant, from Microsoft Entra tenant, make sure Service Principal is member of the new security group.
10. On the Fabric Tenant Admin portal, validate if Allow service principals to use read-only admin APIs is enabled for the new security group.

# [Public access with Self-hosted IR](#tab/Scenario2)
### Scan cross-tenant Power BI by using delegated authentication in a public network

1. Make sure the Fabric tenant ID is entered correctly during the registration. By default, the Fabric tenant ID that exists in the same Microsoft Entra instance as Microsoft Purview will be populated.
2. Make sure your [Fabric metadata model is up to date by enabling metadata scanning](/en-us/fabric/admin/metadata-scanning-setup#enable-tenant-settings-for-metadata-scanning).
3. From the Azure portal, validate if the Microsoft Purview account Network is set to **public access**.
4. From the Fabric tenant admin portal, make sure the Fabric tenant is configured to allow a public network.
5. Check your instance of Azure Key Vault to make sure:

    1. There are no typos in the password.
    2. Microsoft Purview managed identity has **get** and **list** access to secrets.
6. Review your credential to validate that the:

    1. Client ID matches the *Application (Client) ID* of the app registration.
    2. Username includes the user principal name, such as `johndoe@contoso.com`.
7. In the Fabric Microsoft Entra tenant, validate the following app registration settings:

    1. The app registration exists in your Microsoft Entra tenant where the Fabric tenant is located.
    2. If service principal is used, under **API permissions**, the following **delegated permissions** are assigned with read for the following APIs:

        - Microsoft Graph openid
        - Microsoft Graph User.Read
    3. Under **Authentication**:

        1. **Supported account types** &gt; **Accounts in any organizational directory (Any Microsoft Entra directory - Multitenant)** is selected.
        2. **Implicit grant and hybrid flows** &gt; **ID tokens (used for implicit and hybrid flows)** is selected.
        3. **Allow public client flows** is enabled.
8. Validate the following self-hosted runtime settings:

    1. Latest version of [Self-hosted integration runtime](https://go.microsoft.com/fwlink/?linkid=2246619) or [Kubernetes supported self-hosted integration runtime](data-map-integration-runtime-kubernetes) is installed.
    2. Network connectivity from the self-hosted runtime to the Fabric tenant is enabled. The following endpoints must be reachable from self-hosted runtime:

        - `*.powerbi.com`
        - `*.analysis.windows.net`
    3. Network connectivity from the self-hosted runtime to Microsoft services is enabled.
    4. [JDK 8 or later](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) is installed. Restart the machine after you newly install the JDK for it to take effect.
9. In Fabric tenant, from Microsoft Entra tenant, make sure Service Principal is member of the new security group.
10. On the Fabric Tenant Admin portal, validate if Allow service principals to use read-only admin APIs is enabled for the new security group.

# [Private access with Managed Virtual Network IR (v2 only)](#tab/Scenario3)
### Scan cross-tenant Fabric using Managed Virtual Network IR (v2 only) with Delegated Authentication or Service Principal in a private network

1. Make sure the Fabric tenant ID is entered correctly during the registration.
2. Make sure your [Fabric metadata model is up to date by enabling metadata scanning](/en-us/fabric/admin/metadata-scanning-setup#enable-tenant-settings-for-metadata-scanning).
3. Check your instance of Azure Key Vault to make sure:

    1. There are no typos in the password.
    2. Microsoft Purview managed identity has **get** and **list** access to secrets.
4. Review your credential to validate that the:

    1. Client ID matches the *Application (Client) ID* of the app registration.
    2. Username includes the user principal name, such as `johndoe@contoso.com`.
5. In the Fabric tenant, validate the following app registration settings:

    1. The app registration exists in your tenant where the Fabric tenant is located.
    2. If service principal is used, under **API permissions**, the following **delegated permissions** are assigned with read for the following APIs:

        - Microsoft Graph openid
        - Microsoft Graph User.Read
    3. If delegated authentication is used, under **API permissions**, the following **delegated permissions** and **grant admin consent for the tenant** is set up with read for the following APIs:

        - Power BI Service Tenant.Read.All
        - Microsoft Graph openid
        - Microsoft Graph User.Read
    4. Under **Authentication**:

        1. **Supported account types** &gt; **Accounts in any organizational directory (Any Microsoft Entra directory - Multitenant)** is selected.
        2. **Implicit grant and hybrid flows** &gt; **ID tokens (used for implicit and hybrid flows)** is selected.
        3. **Allow public client flows** is enabled.
6. If delegated authentication is used, in the Power BI Microsoft Entra tenant, validate the following Power BI admin user settings:

    1. The user is assigned to the Fabric administrator role.
    2. If the user is recently created, sign in with the user at least once, to make sure that the password is reset successfully, and the user can successfully initiate the session.
    3. There are no multifactor authentication or conditional access policies enforced on the user.
7. From Microsoft Entra tenant, make sure Service Principal is member of the new security group.
8. On the Fabric Tenant Admin portal, validate if Allow service principals to use read-only admin APIs is enabled for the new security group.

---

## Register the Fabric tenant

1. From the options on the left, select **Data Map**.
2. Select **Register**, and then select **Fabric** as your data source.

    ![Screenshot that shows the list of data sources available to choose.](media/setup-fabric-scan-catalog-portal/select-fabric-data-source.png)
3. Give your Fabric instance a friendly name. The name must be 3 to 63 characters long, and must contain only letters, numbers, underscores, and hyphens. Spaces aren't allowed.
4. Edit the **Tenant ID** field, to replace with the tenant for the cross-tenant Fabric that you want to register and scan. By default, Microsoft Purview's tenant ID is populated.

    ![Screenshot that shows the registration experience for cross-tenant Fabric.](media/setup-fabric-scan-catalog-portal/register-cross-tenant.png)

## Authentication to scan

To be able to scan your Microsoft Fabric tenant and review its metadata, you'll first need to create a way to authenticate with the Fabric tenant, and then give Microsoft Purview the authentication information.

### Authenticate to Fabric tenant

In Microsoft Entra tenant, where Fabric tenant is located:

1. In the [Azure portal](https://portal.azure.com), search for **Microsoft Entra ID**.
2. Create a new security group in your Microsoft Entra ID, by following [Create a basic group and add members using Microsoft Entra ID](/en-us/azure/active-directory/fundamentals/active-directory-groups-create-azure-portal).

    Tip

    You can skip this step if you already have a security group you want to use.
3. Select **Security** as the **Group Type**.

    ![Screenshot of security group type.](media/setup-power-bi-scan-powershell/security-group.png)
4. Select **Members**, then select **+ Add members**.
5. Search for your Microsoft Purview managed identity or service principal and select it.

    ![Screenshot showing how to add catalog by searching for its name.](media/setup-power-bi-scan-powershell/add-catalog-to-group-by-search.png)

    You should see a success notification showing you that it was added.

    ![Screenshot showing successful addition of  catalog managed identity.](media/setup-power-bi-scan-powershell/success-add-catalog-msi.png)

### Associate the security group with Fabric tenant

1. Log into the [Fabric admin portal](https://app.fabric.microsoft.com/admin-portal/tenantSettings).
2. Select the **Tenant settings** page.

    Important

    You need to be a Fabric Admin to see the tenant settings page.
3. Select **Admin API settings** &gt; **Allow service principals to use read-only admin APIs**.
4. Select **Specific security groups**.
5. Select **Admin API settings** &gt; **Enhance admin APIs responses with detailed metadata** and **Enhance admin APIs responses with DAX and mashup expressions** &gt; Enable the toggle to allow Microsoft Purview Data Map automatically discover the detailed metadata of Fabric datasets as part of its scans.

    Important

    After you update the Admin API settings on your Fabric tenant, wait around 15 minutes before registering a scan and test connection.

Caution

When you allow the security group you created to use read-only admin APIs, you also allow it to access the metadata (such as dashboard and report names, owners, and descriptions) for all of your Fabric artifacts in this tenant. Once the metadata has been pulled into the Microsoft Purview, Microsoft Purview's permissions, not Fabric permissions, determine who can see that metadata.

    Note

    - You can remove the security group from your developer settings, but the metadata previously extracted won't be removed from the Microsoft Purview account. You can delete it separately if you wish.
    - If your Fabric item (such as lakehouse or mirrored catalog) has OneLake security enabled, then you must create a OneLake security role with **Read** permission assigned to the Microsoft Purview user. See [Get started with OneLake Security](/en-us/fabric/onelake/security/get-started-onelake-security) for step-by-step instructions.

### Configure credentials for scans in Microsoft Purview

#### Service principal

1. Create an app registration in your Microsoft Entra tenant where Fabric is located. Provide a web URL in the **Redirect URI**.

    ![Screenshot how to create App in Microsoft Entra ID for cross tenant.](media/setup-fabric-scan-catalog-portal/fabric-scan-cross-tenant-app-registration.png)
2. Take note of the client ID (app ID).

    ![Screenshot that shows how to create a service principal.](media/setup-fabric-scan-catalog-portal/fabric-create-service-principle.png)
3. From the Microsoft Entra dashboard, select the newly created application, and then select **App permissions**. Assign the application the following delegated permissions:

    - Microsoft Graph openid
    - Microsoft Graph User.Read

    ![Screenshot of delegated permissions on Microsoft Graph.](media/setup-fabric-scan-catalog-portal/fabric-scan-spn-api-permissions.png)
4. From the Microsoft Entra dashboard, select the newly created application, and then select **Authentication**. Under **Supported account types**, select **Accounts in any organizational directory (Any Microsoft Entra directory - Multitenant)**.

    ![Screenshot of account type support multitenant.](media/setup-fabric-scan-catalog-portal/fabric-multitenant.png)
5. Under **Implicit grant and hybrid flows**, select **ID tokens (used for implicit and hybrid flows)**.

    ![Screenshot of ID token hybrid flows.](media/setup-fabric-scan-catalog-portal/fabric-id-token-hybrid-flows.png)
6. Under **Advanced settings**, enable **Allow Public client flows**.
7. In the tenant where Microsoft Purview is created go to the instance of Azure Key Vault.
8. Select **Settings** &gt; **Secrets**, and then select **+ Generate/Import**.

    ![Screenshot of the instance of Azure Key Vault.](media/setup-fabric-scan-catalog-portal/fabric-key-vault.png)
9. Enter a name for the secret. For **Value**, type the newly created secret for the App registration. Select **Create** to complete.
10. Under **Certificates & secrets**, create a new secret and save it securely for next steps.
11. In Azure portal, navigate to your Azure key vault.
12. Select **Settings** &gt; **Secrets** and select **+ Generate/Import**.

    ![Screenshot how to navigate to Azure Key Vault.](media/setup-fabric-scan-catalog-portal/fabric-key-vault.png)
13. Enter a name for the secret and for **Value**, type the newly created secret for the App registration. Select **Create** to complete.

    ![Screenshot how to generate an Azure Key Vault secret for SPN.](media/setup-fabric-scan-catalog-portal/fabric-key-vault-secret-spn.png)
14. If your key vault isn't connected to Microsoft Purview yet, you need to [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account).
15. Next, in Microsoft Purview, go to the **Credentials** page under **Management** to create a new credential.

    Tip

    Alternatively, you can create a new credential during the scanning process.
16. Create your new Credential by selecting **+ New**.
17. Provide required parameters:

    - **Name**: Provide a unique name for credential
    - **Authentication method**: Service principal
    - **Tenant ID**: Your Fabric tenant ID
    - **Client ID**: Use Service Principal Client ID (App ID) you created earlier
    - **Key Vault Connection**: the Microsoft Purview connection to the Key Vault where you created your secret earlier.
    - **Secret name**: the name of the secret you created earlier.

    ![Screenshot of the new credential menu, showing Fabric credential for SPN with all required values supplied.](media/setup-fabric-scan-catalog-portal/fabric-scan-spn-authentication.png)
18. Once all the details have been filled in, select **Create**.

#### Delegated authentication

1. [Create a user account in the Microsoft Entra tenant where the Fabric tenant is located](/en-us/azure/active-directory/fundamentals/how-to-create-delete-users#create-a-new-user), and [assign the user to this role](/en-us/azure/active-directory/fundamentals/users-assign-role-azure-portal#assign-roles): **Fabric Administrator**. Take note of the username and sign in to change the password.
2. Go to the instance of Azure Key Vault in the tenant where Microsoft Purview is created.
3. Select **Settings** &gt; **Secrets**, and then select **+ Generate/Import**.

    ![Screenshot of the instance of Azure Key Vault.](media/setup-fabric-scan-catalog-portal/fabric-key-vault.png)
4. Enter a name for the secret. For **Value**, type the newly created password for the Microsoft Entra user. Select **Create** to complete.

    ![Screenshot that shows how to generate a secret in Azure Key Vault.](media/setup-fabric-scan-catalog-portal/fabric-key-vault-secret.png)
5. If your key vault isn't connected to Microsoft Purview yet, you need to [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account).
6. Create an app registration in your Microsoft Entra tenant where Fabric is located. Provide a web URL in the **Redirect URI**.

    ![Screenshot how to create App in Microsoft Entra ID for cross tenant.](media/setup-fabric-scan-catalog-portal/fabric-scan-cross-tenant-app-registration.png)
7. Take note of the client ID (app ID).

    ![Screenshot that shows how to create a service principal.](media/setup-fabric-scan-catalog-portal/fabric-create-service-principle.png)
8. From the Microsoft Entra dashboard, select the newly created application, and then select **App permissions**. Assign the application the following delegated permissions, and grant admin consent for the tenant:

    - Fabric Service Tenant.Read.All
    - Microsoft Graph openid
    - Microsoft Graph User.Read

    ![Screenshot of delegated permissions on Fabric and Microsoft Graph.](media/setup-fabric-scan-catalog-portal/fabric-delegated-permissions.png)
9. From the Microsoft Entra dashboard, select the newly created application, and then select **Authentication**. Under **Supported account types**, select **Accounts in any organizational directory (Any Microsoft Entra directory - Multitenant)**.

    ![Screenshot of account type support multitenant.](media/setup-fabric-scan-catalog-portal/fabric-multitenant.png)
10. Under **Implicit grant and hybrid flows**, select **ID tokens (used for implicit and hybrid flows)**.

    ![Screenshot of ID token hybrid flows.](media/setup-fabric-scan-catalog-portal/fabric-id-token-hybrid-flows.png)
11. Under **Advanced settings**, enable **Allow Public client flows**.
12. Next, in Microsoft Purview, go to the **Credentials** page under **Management** to create a new credential.

    Tip

    Alternatively, you can create a new credential during the scanning process.
13. Create your new Credential by selecting **+ New**.
14. Provide required parameters:

    - **Name**: Provide a unique name for credential
    - **Authentication method**: Delegated auth
    - **Client ID**: Use Service Principal Client ID (App ID) you created earlier
    - **User name**: Provide the username of Fabric Administrator you created earlier
    - **Key Vault Connection**: the Microsoft Purview connection to the Key Vault where you created your secret earlier.
    - **Secret name**: the name of the secret you created earlier.

    ![Screenshot of the new credential menu, showing Fabric credential for Delegated Auth with all required values supplied.](media/setup-fabric-scan-catalog-portal/fabric-scan-delegated-authentication.png)
15. Once all the details have been filled in, select **Create**.

## Create scan

1. In the Microsoft Purview Studio, go to the **Data map** in the left menu. Go to **Sources**.
2. Select the registered Fabric source from cross-tenant.
3. Select **+ New scan**.
4. Give your scan a name. Then select the option to include or exclude the personal workspaces.

    Note

    If you switch the configuration of a scan to include or exclude a personal workspace, you trigger a full scan of the Fabric source.
5. Select **Azure AutoResolveIntegrationRuntime** from the dropdown list.
6. For the **Credential**, select the credential you created for your service principal or delegated authentication.

    [![Screenshot that shows the Fabric scan setup, using Azure integration runtime for cross-tenant.](media/setup-fabric-scan-catalog-portal/fabric-scan-setup-cross-tenant.png)](media/setup-fabric-scan-catalog-portal/fabric-scan-setup-cross-tenant.png#lightbox)
7. Select **Test connection** before continuing to the next steps.

    If the test fails, select **View Report** to see the detailed status and troubleshoot the problem:

    1. *Access - Failed* status means that the user authentication failed. Validate if the username and password are correct. Review if the credential contains the correct client (app) ID from the app registration.
    2. *Assets (+ lineage) - Failed* status means that the authorization between Microsoft Purview and Fabric has failed. Make sure that the user is added to the Fabric administrator role.
    3. *Detailed metadata (Enhanced) - Failed* status means that the Fabric admin portal is disabled for the following setting: **Enhance admin APIs responses with detailed metadata**.

    Tip

    For more troubleshooting, see the deployment checklist to make sure you've covered every step in your scenario.
8. Set up a scan trigger. Your options are **Recurring** or **Once**.

    ![Screenshot of the Microsoft Purview scan scheduler.](media/setup-fabric-scan-catalog-portal/scan-trigger.png)
9. On **Review new scan**, select **Save and run** to launch your scan.

### View your scans and scan runs

To view existing scans:

1. Go to the Microsoft Purview portal. On the left pane, select **Data map**.
2. Select the data source. You can view a list of existing scans on that data source under **Recent scans**, or you can view all scans on the **Scans** tab.
3. Select the scan that has results you want to view. The pane shows you all the previous scan runs, along with the status and metrics for each scan run.
4. Select the run ID to check the [scan run details](data-map-scan-run-monitor-population#scan-run-details).

### Manage your scans

To edit, cancel, or delete a scan:

1. Go to the Microsoft Purview portal. On the left pane, select **Data Map**.
2. Select the data source. You can view a list of existing scans on that data source under **Recent scans**, or you can view all scans on the **Scans** tab.
3. Select the scan that you want to manage. You can then:

    - Edit the scan by selecting **Edit scan**.
    - Cancel an in-progress scan by selecting **Cancel scan run**.
    - Delete your scan by selecting **Delete scan**.

Note

- Deleting your scan does not delete catalog assets created from previous scans.