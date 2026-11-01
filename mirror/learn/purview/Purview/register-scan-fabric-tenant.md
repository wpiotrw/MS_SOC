---
layout: Conceptual
title: Connect to your Microsoft Fabric tenant in same tenant as Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-fabric-tenant
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
description: Learn how to connect to a Microsoft Fabric tenant in the same tenant as Microsoft Purview, and use Microsoft Purview's features to scan and manage your Fabric tenant source.
locale: en-us
document_id: 1004471c-0191-368c-f290-5a008c8ef23b
document_version_independent_id: 1004471c-0191-368c-f290-5a008c8ef23b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-fabric-tenant.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-fabric-tenant
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-fabric-tenant.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: b5ed30ef-f1f6-eaf7-ad19-61779897af0a
---

# Connect to your Microsoft Fabric tenant in same tenant as Microsoft Purview | Microsoft Learn

This article outlines how to register a Microsoft Fabric tenant that's in **the same tenant** as your Microsoft Purview resource, and how to authenticate and interact with the Fabric source in Microsoft Purview. For more information about Microsoft Purview in general, read the [introductory article](purview).

Note

Scanning a Fabric tenant brings in metadata and lineage from Fabric items including Power BI. To learn more, see [scan a Power BI tenant](register-scan-power-bi-tenant). The experience of registering a Fabric tenant and setting up a scan is similar to Power BI tenant and shared among all Fabric items.

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | Yes | Yes |

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

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
| Public access with Azure IR | Allowed | Allowed | Azure Runtime | Managed Identity/ Delegated authentication / Service principal | Review deployment checklist |
| Public access with Self-hosted IR | Allowed | Allowed | SHIR or Kubernetes SHIR | Service principal | Review deployment checklist |
| Private access | Denied | Allowed | Managed Virtual Network IR (v2 only) | Managed Identity / Delegated authentication / Service principal | Review deployment checklist |

Note

The supported scenarios above apply for non-Power BI items in Fabric. See the [Power BI documentation](register-scan-power-bi-tenant#supported-scenarios-for-power-bi-scans) for supported scenarios that apply to Power BI items.

Support for scanning Fabric Lakehouses by using Managed Identity is now available. Hence, you can scan Fabric Lakehouses by using Service Principal or Managed Identity. Previously, only service principal was supported for Fabric Lakehouses. There's no change for other Fabric items.

Support for scanning Fabric Lakehouses by using Managed Virtual Network IR is now available.

### Known limitations

- Currently for all Fabric items besides Power BI, only item level metadata and lineage can be scanned. For Lakehouse tables and files, sub-item level metadata scanning is available but sub-item level lineage isn't supported.
- For self-hosted integration runtime, the standard self-hosted integration runtime with minimal version 5.47.9073.1 or [Kubernetes supported self-hosted integration runtime](data-map-integration-runtime-kubernetes) is supported.
- Empty workspaces are skipped.
- Microsoft Purview doesn't support Fabric DAX expressions as part of metadata scanning.
- You might get a **Too many requests** error while running multiple Fabric or Power BI scans. If so, reduce the concurrent scans and scatter the scans over different times to help resolve the error.
- In the incremental scan, you might see a non-zero count of assets ingested and assets discovered, even if there's no change in the data source. This behavior should be ignored. The data catalog and Data Map assets continue to reflect the true state of the data source.
- Fabric with tenant-level or workspace-level private links aren't supported.

- Unsupported Parquet encodings: Microsoft Purview doesn't support schema extraction for Parquet files that use run-length encoding (RLE) in Microsoft Fabric Lakehouse. Tables containing RLE-encoded columns might fail to extract schema metadata, including tables, columns, and data types. The process still discovers asset-level metadata (L1). To enable full schema extraction, re-create the affected tables by using a supported encoding format, such as dictionary or plain encoding.

Note

For Fabric Lakehouse tables with schema-enabled databases, the schema name and table name are combined into a single segment in the qualified name using `%252F` (double-URL-encoded forward slash) as a separator. For example, a table at the OneLake path `Tables/dbo/my_table` will appear in Data Map with the qualified name `.../tables/dbo%252Fmy_table`, while the entity display name will show only the table name (for example, `my_table`) without the schema prefix.

## Prerequisites

Before you start, make sure you have the following prerequisites:

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).

### Authentication options

- Managed Identity
- *Service Principal
- Delegated Authentication

## Deployment checklist

Use any of the following deployment checklists during the setup or for troubleshooting purposes, based on your scenario:

# [Public access with Azure IR](#tab/Scenario1)
### Scan same-tenant Fabric using Azure IR and Managed Identity in public network

1. Make sure Fabric and Microsoft Purview accounts are in the same tenant.
2. Make sure you enter the Fabric tenant ID correctly during the registration.
3. Make sure your [Fabric Metadata model is up to date by enabling metadata scanning.](/en-us/fabric/admin/metadata-scanning-setup#enable-tenant-settings-for-metadata-scanning)
4. From Azure portal, validate if Microsoft Purview account Network is set to public access.
5. From Fabric tenant Admin Portal, make sure Fabric tenant is configured to allow public network.
6. In Microsoft Entra tenant, create a security group.
7. From Microsoft Entra tenant, make sure Microsoft Purview account MSI is member of the new security group.
8. On the Fabric Tenant Admin portal, validate if Allow service principals to use read-only admin APIs is enabled for the new security group.
9. On the Fabric Tenant Admin portal, validate if **Tenant Settings** -&gt; **OneLake Settings** -&gt; [Users can access data stored in OneLake with apps external to Fabric](/en-us/fabric/admin/tenant-settings-index) is enabled.

# [Public access with self-hosted IR](#tab/Scenario2)
### Scan same-tenant Fabric using self-hosted IR with Service Principal in public network

1. Make sure Fabric and Microsoft Purview accounts are in the same tenant.
2. Make sure you enter the Fabric tenant ID correctly during the registration.
3. Make sure your [Fabric Metadata model is up to date by enabling metadata scanning.](/en-us/fabric/admin/metadata-scanning-setup#enable-tenant-settings-for-metadata-scanning)
4. From Azure portal, validate if Microsoft Purview account Network is set to public access.
5. From Fabric tenant Admin Portal, make sure Fabric tenant is configured to allow public network.
6. Check your Azure Key Vault to make sure:

    1. There are no typos in the password or secret.
    2. Microsoft Purview Managed Identity has get/list access to secrets.
7. Review your credential to validate:

    1. Client ID matches *Application (Client) ID* of the app registration.
    2. Username includes the user principal name such as `johndoe@contoso.com`.
8. Validate app registration settings to make sure:

    1. App registration exists in your Microsoft Entra tenant.
    2. If you use service principal, under **API permissions**, assign the following **delegated permissions** with read for the following APIs:

        - Microsoft Graph openid
        - Microsoft Graph User.Read
    3. Under **Authentication**, **Allow public client flows** is enabled.
9. Validate self-hosted runtime settings:

    1. Latest version of [Self-hosted integration runtime](https://go.microsoft.com/fwlink/?linkid=2246619) or [Kubernetes supported self-hosted integration runtime](data-map-integration-runtime-kubernetes) is installed.
    2. Network connectivity from self-hosted runtime to Fabric tenant is enabled. The following endpoints must be reachable from self-hosted runtime:

        - `*.powerbi.com`
        - `*.analysis.windows.net`
    3. Network connectivity from self-hosted runtime to Microsoft services is enabled.
    4. [JDK 8 or later](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) is installed. Restart the machine after you newly install the JDK for it to take effect.
10. In Microsoft Entra tenant, create a security group.
11. From Microsoft Entra tenant, make sure Service Principal is member of the new security group.
12. On the Fabric Tenant Admin portal, validate if Allow service principals to use read-only admin APIs is enabled for the new security group.
13. On the Fabric Tenant Admin portal, validate if **Tenant Settings** -&gt; **OneLake Settings** -&gt; [Users can access data stored in OneLake with apps external to Fabric](/en-us/fabric/admin/tenant-settings-index) is enabled.

# [Private access with Managed Virtual Network IR (v2 only)](#tab/Scenario3)
### Scan same-tenant Fabric using Managed Virtual Network IR (v2 only) with Managed Identity, Delegated Authentication or Service Principal in a private network

1. Make sure Fabric and Microsoft Purview accounts are in the same tenant.
2. Make sure you enter the Fabric tenant ID correctly during the registration.
3. Make sure your [Fabric Metadata model is up to date by enabling metadata scanning.](/en-us/fabric/admin/metadata-scanning-setup#enable-tenant-settings-for-metadata-scanning)
4. Check your Azure Key Vault to make sure:

    1. There are no typos in the password.
    2. Microsoft Purview Managed Identity has get/list access to secrets.
5. Review your credential to validate:

    1. Client ID matches *Application (Client) ID* of the app registration.
    2. Username includes the user principal name such as `johndoe@contoso.com`.
6. If you use Delegated Authentication, validate Fabric admin user settings to make sure:

    1. User is assigned to Fabric Administrator role.
    2. If user is recently created, sign in with the user at least once to make sure password is reset successfully, and user can successfully initiate the session.
    3. There's no MFA or Conditional Access Policies are enforced on the user.
7. Validate app registration settings to make sure:

    1. App registration exists in your Microsoft Entra tenant.
    2. If you use service principal, under **API permissions**, assign the following **delegated permissions** with read for the following APIs:

        - Microsoft Graph openid
        - Microsoft Graph User.Read
    3. If you use delegated authentication, under **API permissions**, assign the following **delegated permissions** and **grant admin consent for the tenant** with read for the following APIs:

        - Power BI Service Tenant.Read.All
        - Microsoft Graph openid
        - Microsoft Graph User.Read
    4. Under **Authentication**, **Allow public client flows** is enabled.
8. In Microsoft Entra tenant, create a security group.
9. From Microsoft Entra tenant, make sure Service Principal is member of the new security group.
10. On the Fabric Tenant Admin portal, validate if Allow service principals to use read-only admin APIs is enabled for the new security group.
11. On the Fabric Tenant Admin portal, validate if **Tenant Settings** -&gt; **OneLake Settings** -&gt; [Users can access data stored in OneLake with apps external to Fabric](/en-us/fabric/admin/tenant-settings-index) is enabled.

---

## Register Fabric tenant

This section describes how to register a Fabric tenant in Microsoft Purview for same-tenant scenario.

1. Select the **Data Map** on the left navigation.
2. Select **Register**.

    Select **Fabric** as your data source.

    ![Image showing the list of data sources available to choose with fabric selected.](media/setup-fabric-scan-catalog-portal/select-fabric-data-source.png)
3. Enter a friendly name for your Fabric instance and select a collection.

    The name must be between 3-63 characters long and can only contain letters, numbers, underscores, and hyphens. Don't use spaces.

    By default, the system finds the Fabric tenant that exists in the same Microsoft Entra tenant.

## Authentication to scan

To scan your Fabric tenant and review its metadata, you first need to create a way to authenticate by using the Fabric tenant. Then, provide Microsoft Purview with the authentication information.

### Authenticate to Fabric tenant

In the Microsoft Entra tenant where the Fabric tenant is located:

1. In the [Azure portal](https://portal.azure.com), search for **Microsoft Entra ID**.
2. Create a new security group in your Microsoft Entra ID, by following [Create a basic group and add members using Microsoft Entra ID](/en-us/azure/active-directory/fundamentals/active-directory-groups-create-azure-portal).

    Tip

    You can skip this step if you already have a security group you want to use.
3. Select **Security** as the **Group Type**.

    ![Screenshot of security group type.](media/setup-power-bi-scan-powershell/security-group.png)
4. Add any relevant users to the security group:

    - If you're using **Managed Identity** as the authentication method, add your Microsoft Purview managed identity to this security group. Select **Members**, and then select **Add members**.
    - If you're using **delegated authentication** or **service principal** as the authentication method, add your **service principal** to this security group. Select **Members**, and then select **Add members**.
5. Search for your Microsoft Purview managed identity or service principal and select it.

    ![Screenshot showing how to add catalog by searching for its name.](media/setup-power-bi-scan-powershell/add-catalog-to-group-by-search.png)

    You see a success notification that shows you it was added.

    ![Screenshot showing successful addition of  catalog managed identity.](media/setup-power-bi-scan-powershell/success-add-catalog-msi.png)

### Associate the security group with Fabric tenant

1. Sign in to the [Fabric admin portal](https://app.fabric.microsoft.com/admin-portal/tenantSettings).
2. Select the **Tenant settings** page.

    Important

    You need to be a Fabric Admin to see the tenant settings page.
3. Select **Admin API settings** &gt; **Allow service principals to use read-only admin APIs**.
4. Select **Specific security groups**.
5. Select **Admin API settings** &gt; **Enhance admin APIs responses with detailed metadata** and **Enhance admin APIs responses with DAX and mashup expressions** &gt; Enable the toggle to allow Microsoft Purview Data Map automatically discover the detailed metadata of Fabric datasets as part of its scans.

    Important

    After you update the Admin API settings on your Fabric tenant, wait about 15 minutes before registering a scan and testing connection.

Caution

When you allow the security group you created (that has your Microsoft Purview managed identity as a member) to use read-only admin APIs, you also allow it to access the metadata (such as dashboard and report names, owners, and descriptions) for all of your Fabric artifacts in this tenant. Once the metadata is pulled into Microsoft Purview, Microsoft Purview's permissions, not Fabric permissions, determine who can see that metadata.

    Note

    - You can remove the security group from your developer settings, but the metadata previously extracted won't be removed from the Microsoft Purview account. You can delete it separately if you wish.
    - If your Fabric item (such as lakehouse or mirrored catalog) has OneLake security enabled, then you must create a OneLake security role with **Read** permission assigned to the Microsoft Purview user. See [Get started with OneLake Security](/en-us/fabric/onelake/security/get-started-onelake-security) for step-by-step instructions.

### Configure credentials for scans in Microsoft Purview

#### Managed identity

If you follow all the steps in authenticate Microsoft Purview to Fabric, you don't need any other authentication steps for managed identities.

#### Service principal

1. In the [Azure portal](https://portal.azure.com), select **Microsoft Entra ID** and create an App Registration in the tenant. Provide a web URL in the **Redirect URI**. [For information about the Redirect URI see this documentation from Microsoft Entra ID](/en-us/azure/active-directory/develop/reply-url).

    ![Screenshot how to create an app registration in Microsoft Entra ID.](media/setup-fabric-scan-catalog-portal/fabric-scan-app-registration.png)
2. Take note of Client ID(App ID).

    ![Screenshot how to create a service principal with the client ID highlighted.](media/setup-fabric-scan-catalog-portal/fabric-create-service-principle.png)
3. From Microsoft Entra dashboard, select newly created application and then select **App registration**. From **API Permissions**, assign the application the following delegated permissions:

    - Microsoft Graph openid
    - Microsoft Graph User.Read

    ![Screenshot of delegated permissions on Microsoft Graph.](media/setup-fabric-scan-catalog-portal/fabric-scan-spn-api-permissions.png)
4. Under **Advanced settings**, enable **Allow Public client flows**.
5. Under **Certificates & secrets**, create a new secret and save it securely for next steps.
6. In Azure portal, navigate to your Key Vault.
7. Select **Settings** &gt; **Secrets** and select **+ Generate/Import**.

    ![Screenshot how to navigate to Azure Key Vault and generate a secret.](media/setup-fabric-scan-catalog-portal/fabric-key-vault.png)
8. Enter a name for the secret and for **Value**, type the newly created secret for the App registration. Select **Create** to complete.

    ![Screenshot how to generate an Azure Key Vault secret for SPN.](media/setup-fabric-scan-catalog-portal/fabric-key-vault-secret-spn.png)
9. If your key vault isn't connected to Microsoft Purview yet, you need to [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account).
10. Now that you created your secret, in Microsoft Purview, go to the **Credentials** page under **Management**.

    Tip

    Alternatively, you can create a new credential during the scanning process.
11. Select **New** to create your new credential.
12. Provide the required parameters:

    - **Name**: Provide a unique name for the credential.
    - **Authentication method**: Service principal
    - **Tenant ID**: Your Fabric tenant ID
    - **Client ID**: Use Service Principal Client ID (App ID) you created earlier.
    - **Key Vault Connection**: the Microsoft Purview connection to the Key Vault where you created your secret earlier.
    - **Secret name**: the name of the secret you created earlier.

    ![Screenshot of the new credential menu, showing Fabric credential for SPN with all required values supplied.](media/setup-fabric-scan-catalog-portal/fabric-scan-spn-authentication.png)
13. Once you fill in all the details, select **Create**.

#### Delegated authentication

1. Create a user account in Microsoft Entra tenant and assign the user to Microsoft Entra role, **Fabric Administrator**. Take note of username and sign in to change the password.
2. Go to your Key Vault.
3. Select **Settings** &gt; **Secrets** and select **+ Generate/Import**.

    ![Screenshot how to navigate to Azure Key Vault.](media/setup-fabric-scan-catalog-portal/fabric-key-vault.png)
4. Enter a name for the secret and for **Value**, type the newly created password for the Microsoft Entra user. Select **Create** to complete.

    ![Screenshot how to generate an Azure Key Vault secret.](media/setup-fabric-scan-catalog-portal/fabric-key-vault-secret.png)
5. If your key vault isn't connected to Microsoft Purview yet, you need to [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account)
6. Create an app registration in your Microsoft Entra tenant. Provide a web URL in the **Redirect URI**.

    ![Screenshot how to create App in Microsoft Entra ID.](media/setup-fabric-scan-catalog-portal/fabric-scan-app-registration.png)
7. Take note of Client ID(App ID).

    ![Screenshot how to create a service principal.](media/setup-fabric-scan-catalog-portal/fabric-create-service-principle.png)
8. From Microsoft Entra dashboard, select newly created application and then select **API permissions**. Assign the application the following delegated permissions, and grant admin consent for the tenant:

    - Fabric Service Tenant.Read.All
    - Microsoft Graph openid
    - Microsoft Graph User.Read

    ![Screenshot of delegated permissions on Fabric Service and Microsoft Graph.](media/setup-fabric-scan-catalog-portal/fabric-delegated-permissions.png)
9. Under **Advanced settings**, enable **Allow Public client flows**.
10. Next, in Microsoft Purview, go to the **Credentials** page under **Management** to create a new credential.

    Tip

    Alternatively, you can create a new credential during the scanning process.
11. Select **New** to create your new credential.
12. Provide the required parameters:

    - **Name**: Provide a unique name for the credential.
    - **Authentication method**: Delegated auth.
    - **Client ID**: Use Service Principal Client ID (App ID) you created earlier.
    - **User name**: Provide the username of Fabric Administrator you created earlier.
    - **Key Vault Connection**: the Microsoft Purview connection to the Key Vault where you created your secret earlier.
    - **Secret name**: the name of the secret you created earlier.

    ![Screenshot of the new credential menu, showing Fabric credential for Delegated Auth with all required values supplied.](media/setup-fabric-scan-catalog-portal/fabric-scan-delegated-authentication.png)
13. Once you fill in all the details, select **Create**.

## Create scan

1. In the Microsoft Purview portal, go to **Data Map**.
2. Go to **Sources**.
3. Select the registered Fabric source.
4. Select **+ New scan**.
5. Enter a name for your scan.
6. Select either your managed identity credential or the credential you created for your service principal or delegated authentication.

    [![Image showing Fabric scan setup.](media/setup-fabric-scan-catalog-portal/fabric-scan-setup-same-tenant.png)](media/setup-fabric-scan-catalog-portal/fabric-scan-setup-same-tenant.png#lightbox)
7. Select **Test Connection** before continuing to next steps. If **Test Connection** fails, select **View Report** to see the detailed status and troubleshoot the problem. 1. Access - Failed status means the user authentication failed. Scans that use managed identity always pass because no user authentication is required. If you use service principal or delegated authentication, make sure your Key Vault credential is set up correctly and that Microsoft Purview has access to the key vault. 1. Assets (+ lineage) - Failed status means the Microsoft Purview - Fabric authorization failed. Make sure the Microsoft Purview managed identity is added to the security group in the Fabric admin portal.

    1. Detailed metadata (Enhanced) - Failed status means the Fabric admin portal is disabled for the following setting - **Enhance admin APIs responses with detailed metadata**

    Tip

    For more troubleshooting, see the deployment checklist to make sure you covered every step in your scenario.
8. Set up a scan trigger. Your options are **Recurring** and **Once**.

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

## Glossary

**Items** and **sub-items** in Microsoft Fabric Lakehouse:

- **Items**: In Fabric, items are top-level workspace artifacts such as Lakehouse, Warehouse, Notebook, Pipeline, and Semantic Model. Each item acts as a single entity for lifecycle operations, including creation, deletion, and CI/CD tracking. A Lakehouse itself is an item. Tables (Delta and non-Delta), files, folders, and sometimes shortcuts within a Lakehouse are considered sub-items.
- **Sub-items**: These elements represent the actual data layer. You can view and query them through Spark and SQL endpoints. However, you can't manage or deploy them independently.