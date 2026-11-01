---
layout: Conceptual
title: Connect to and manage a Power BI tenant in Microsoft Purview (cross-tenant) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-power-bi-tenant-cross-tenant
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: chigupta
ms.date: 2025-05-21T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to connect to a Power BI tenant in a cross-tenant scenario. You use Microsoft Purview to scan and manage your Power BI tenant source.
ms.custom: sfi-image-nochange
locale: en-us
document_id: 89baf2ec-68a7-10cd-7aee-47be9fca8a38
document_version_independent_id: 89baf2ec-68a7-10cd-7aee-47be9fca8a38
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-power-bi-tenant-cross-tenant.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-power-bi-tenant-cross-tenant
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-power-bi-tenant-cross-tenant.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: b56fac87-c62d-cb7e-2f52-47ebe9dcd417
---

# Connect to and manage a Power BI tenant in Microsoft Purview (cross-tenant) | Microsoft Learn

This article outlines how to register a Power BI tenant in a cross-tenant scenario, and how to authenticate and interact with the tenant in Microsoft Purview. If you're unfamiliar with the service, see [Learn about Microsoft Purview](purview).

Note

For scanning a Microsoft Fabric tenant, see our [Microsoft Fabric documentation](register-scan-fabric-tenant-cross-tenant).

## Supported capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan | Classification | Labeling | Access Policy | Lineage | Data Sharing | Live view |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Yes | Yes | Yes | Yes | No | No | No | [Yes](data-map-lineage-power-bi) | No | No |

\* Power BI items in a Microsoft Fabric tenant are available using live view.

When scanning Power BI source, Microsoft Purview supports:

- Extracting technical metadata including:

    - Workspaces
    - Dashboards
    - Reports
    - Datasets including the tables and columns
    - Dataflows
    - Datamarts
- Fetching static lineage on assets relationships among above Power BI artifacts and external data source assets. Learn more from [Power BI lineage](data-map-lineage-power-bi).

### Supported scenarios for Power BI scans

| **Scenario** | **Microsoft Purview public access** | **Power BI public access** | **Runtime option** | **Authentication option** | **Deployment checklist** |
| --- | --- | --- | --- | --- | --- |
| Public access with Azure integration runtime | Allowed | Allowed | Azure runtime | Delegated authentication / Service principal | Deployment checklist |
| Public access with self-hosted integration runtime | Allowed | Allowed | Self-hosted runtime | Delegated authentication / Service principal | Deployment checklist |
| Private access | Denied | Allowed | Managed VNet IR (v2 only) | Delegated authentication / Service principal | Review deployment checklist |
| Private access | Allowed | Denied | Self-hosted runtime | Delegated authentication / Service principal | Deployment checklist |
| Private access | Denied | Allowed | Self-hosted runtime | Delegated authentication / Service principal | Deployment checklist |
| Private access | Denied | Denied | Self-hosted runtime | Delegated authentication / Service principal | Deployment checklist |

### Known limitations

- If Power BI tenant is protected behind a private endpoint, [standard or kubernetes supported self-hosted runtimes](data-map-integration-runtime-choose) are the only options to scan.
- For the cross-tenant scenario, delegated authentication and service principal are the only supported authentication options for scanning.
- If the Power BI dataset schema isn't shown after the scan, it's due to one of the current limitations with the [Power BI metadata scanner](/en-us/power-bi/admin/service-admin-metadata-scanning).
- Empty workspaces are skipped.

## Prerequisites

Before you start, make sure you have the following:

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).

## Register the Power BI tenant

1. From the options on the left, select **Data Map**.
2. Select **Register**, and then select **Fabric** as your data source. It includes Power BI sources and assets.

    ![Screenshot that shows the list of data sources available to choose.](media/setup-power-bi-scan-catalog-portal/select-power-bi-data-source.png)
3. Give your data source a friendly name. The name must be 3 to 63 characters long, and must contain only letters, numbers, underscores, and hyphens. Spaces aren't allowed.
4. Edit the **Tenant ID** field, to replace with the tenant for the cross-tenant Power BI that you want to register and scan. By default, Microsoft Purview's tenant ID is populated.

    ![Screenshot that shows the registration experience for cross-tenant Power BI.](media/setup-power-bi-scan-catalog-portal/register-cross-tenant.png)
5. Select **Register**.

## Authenticate to Power BI tenant

In Microsoft Entra tenant, where Power BI tenant is located:

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

### Associate the security group with Power BI tenant

1. Log into the [Power BI admin portal](https://app.powerbi.com/admin-portal/tenantSettings).
2. Select the **Tenant settings** page.

    Important

    You need to be a Power BI Admin to see the tenant settings page.
3. Select **Admin API settings** &gt; **Allow service principals to use read-only Power BI admin APIs (Preview)**.
4. Select **Specific security groups**.

    ![Image showing how to allow service principals to get read-only Power BI admin API permissions.](media/setup-power-bi-scan-powershell/allow-service-principals-power-bi-admin.png)
5. Select **Admin API settings** &gt; **Enhance admin APIs responses with detailed metadata** and **Enhance admin APIs responses with DAX and mashup expressions** &gt; Enable the toggle to allow Microsoft Purview Data Map automatically discover the detailed metadata of Power BI datasets as part of its scans.

    Important

    After you update the Admin API settings on your power bi tenant, wait around 15 minutes before registering a scan and test connection.

    ![Image showing the Power BI admin portal config to enable subartifact scan.](media/setup-power-bi-scan-catalog-portal/power-bi-scan-sub-artifacts.png)

Caution

When you allow the security group you created (that has your Microsoft Purview managed identity as a member) to use read-only Power BI admin APIs, you also allow it to access the metadata (e.g. dashboard and report names, owners, descriptions, etc.) for all of your Power BI artifacts in this tenant. Once the metadata has been pulled into the Microsoft Purview, Microsoft Purview's permissions, not Power BI permissions, determine who can see that metadata.

    Note

    You can remove the security group from your developer settings, but the metadata previously extracted won't be removed from the Microsoft Purview account. You can delete it separately, if you wish.

## Scan cross-tenant Power BI

Delegated authentication and service principals are the only supported options for cross-tenant scanning. You can scan using either:

- The Azure integration runtime
- A self-hosted integration runtime

### Create scan for cross-tenant using Azure IR with delegated authentication

To create and run a new scan by using the Azure runtime, perform the following steps:

1. [Create a user account in the Microsoft Entra tenant where the Power BI tenant is located](/en-us/azure/active-directory/fundamentals/how-to-create-delete-users#create-a-new-user), and [assign the user to this role](/en-us/azure/active-directory/fundamentals/users-assign-role-azure-portal#assign-roles): **Fabric Administrator**. Take note of the username and sign in to change the password.
2. [Assign the proper Power BI license to the user.](/en-us/azure/active-directory/fundamentals/license-users-groups#assign-licenses-to-users-or-groups)
3. Go to the instance of Azure Key Vault in the tenant where Microsoft Purview is created.
4. Select **Settings** &gt; **Secrets**, and then select **+ Generate/Import**.

    ![Screenshot of the instance of Azure Key Vault.](media/setup-power-bi-scan-catalog-portal/power-bi-key-vault.png)
5. Enter a name for the secret. For **Value**, type the newly created password for the Microsoft Entra user. Select **Create** to complete.

    ![Screenshot that shows how to generate a secret in Azure Key Vault.](media/setup-power-bi-scan-catalog-portal/power-bi-key-vault-secret.png)
6. If your key vault isn't connected to Microsoft Purview yet, you need to [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account).
7. Create an app registration in your Microsoft Entra tenant where Power BI is located. Provide a web URL in the **Redirect URI**.

    ![Screenshot how to create App in Microsoft Entra ID for cross tenant.](media/setup-power-bi-scan-catalog-portal/power-bi-scan-cross-tenant-app-registration.png)
8. Take note of the client ID (app ID).

    ![Screenshot that shows how to create a service principal.](media/setup-power-bi-scan-catalog-portal/power-bi-create-service-principle.png)
9. From the Microsoft Entra dashboard, select the newly created application, and then select **App permissions**. Assign the application the following delegated permissions, and grant admin consent for the tenant:

    - Power BI Service Tenant.Read.All
    - Microsoft Graph openid
    - Microsoft Graph User.Read

    ![Screenshot of delegated permissions on Power BI and Microsoft Graph.](media/setup-power-bi-scan-catalog-portal/power-bi-delegated-permissions.png)
10. From the Microsoft Entra dashboard, select the newly created application, and then select **Authentication**. Under **Supported account types**, select **Accounts in any organizational directory (Any Microsoft Entra directory - Multitenant)**.

    ![Screenshot of account type support multitenant.](media/setup-power-bi-scan-catalog-portal/power-bi-multitenant.png)
11. Under **Implicit grant and hybrid flows**, select **ID tokens (used for implicit and hybrid flows)**.

    ![Screenshot of ID token hybrid flows.](media/setup-power-bi-scan-catalog-portal/power-bi-id-token-hybrid-flows.png)
12. Under **Advanced settings**, enable **Allow Public client flows**.
13. In the Microsoft Purview Studio, go to the **Data map** in the left menu. Go to **Sources**.
14. Select the registered Power BI source from cross-tenant.
15. Select **+ New scan**.
16. Give your scan a name. Then select the option to include or exclude the personal workspaces.

    Note

    If you switch the configuration of a scan to include or exclude a personal workspace, you trigger a full scan of the Power BI source.
17. Select **Azure AutoResolveIntegrationRuntime** from the dropdown list.

    ![Screenshot that shows the Power BI scan setup, using Azure integration runtime for cross-tenant.](media/setup-power-bi-scan-catalog-portal/power-bi-scan-cross-tenant.png)
18. For the **Credential**, select **Delegated authentication**, and then select **+ New** to create a new credential.
19. Create a new credential and provide the following required parameters:

    - **Name**: Provide a unique name for the credential.
    - **Client ID**: Use the service principal client ID (app ID) that you created earlier.
    - **User name**: Provide the username of the Fabric administrator that you created earlier.
    - **Password**: Select the appropriate Key Vault connection, and the **Secret name** where the Power BI account password was saved earlier.

    ![Screenshot that shows the Power BI scan setup, using delegated authentication.](media/setup-power-bi-scan-catalog-portal/power-bi-scan-delegated-authentication.png)
20. Select **Test connection** before continuing to the next steps.

    ![Screenshot that shows the test connection status.](media/setup-power-bi-scan-catalog-portal/power-bi-scan-cross-tenant-test.png)

    If the test fails, select **View Report** to see the detailed status and troubleshoot the problem:

    1. *Access - Failed* status means that the user authentication failed. Validate if the username and password are correct. Review if the credential contains the correct client (app) ID from the app registration.
    2. *Assets (+ lineage) - Failed* status means that the authorization between Microsoft Purview and Power BI has failed. Make sure that the user is added to the Fabric Administrator role (former Power BI Administrator role), and has the proper Power BI license assigned.
    3. *Detailed metadata (Enhanced) - Failed* status means that the Power BI admin portal is disabled for the following setting: **Enhance admin APIs responses with detailed metadata**.
21. Set up a scan trigger. Your options are **Recurring** or **Once**.

    ![Screenshot of the Microsoft Purview scan scheduler.](media/setup-power-bi-scan-catalog-portal/scan-trigger.png)
22. On **Review new scan**, select **Save and run** to launch your scan.

    ![Screenshot that shows how to save and run the Power BI source.](media/setup-power-bi-scan-catalog-portal/save-run-power-bi-scan.png)

Tip

To troubleshoot any issues with scanning:

1. Confirm you have completed the **deployment checklist for your scenario**.
2. Review our [**scan troubleshooting documentation**](register-scan-power-bi-tenant-troubleshoot).

### Create scan for cross-tenant using self-hosted IR with service principal

To create and run a new scan by using the self-hosted integration runtime, perform the following steps:

1. Create an app registration in your Microsoft Entra tenant where Power BI is located. Provide a web URL in the **Redirect URI**.

    ![Screenshot how to create App in Microsoft Entra ID for cross tenant.](media/setup-power-bi-scan-catalog-portal/power-bi-scan-cross-tenant-app-registration.png)
2. Take note of the client ID (app ID).

    ![Screenshot that shows how to create a service principal.](media/setup-power-bi-scan-catalog-portal/power-bi-create-service-principle.png)
3. From the Microsoft Entra dashboard, select the newly created application, and then select **App permissions**. Assign the application the following delegated permissions:

    - Microsoft Graph openid
    - Microsoft Graph User.Read

    ![Screenshot of delegated permissions on Microsoft Graph.](media/setup-power-bi-scan-catalog-portal/power-bi-scan-spn-api-permissions.png)
4. From the Microsoft Entra dashboard, select the newly created application, and then select **Authentication**. Under **Supported account types**, select **Accounts in any organizational directory (Any Microsoft Entra directory - Multitenant)**.

    ![Screenshot of account type support multitenant.](media/setup-power-bi-scan-catalog-portal/power-bi-multitenant.png)
5. Under **Implicit grant and hybrid flows**, select **ID tokens (used for implicit and hybrid flows)**.

    ![Screenshot of ID token hybrid flows.](media/setup-power-bi-scan-catalog-portal/power-bi-id-token-hybrid-flows.png)
6. Under **Advanced settings**, enable **Allow Public client flows**.
7. In the tenant where Microsoft Purview is created go to the instance of Azure Key Vault.
8. Select **Settings** &gt; **Secrets**, and then select **+ Generate/Import**.

    ![Screenshot of the instance of Azure Key Vault.](media/setup-power-bi-scan-catalog-portal/power-bi-key-vault.png)
9. Enter a name for the secret. For **Value**, type the newly created secret for the App registration. Select **Create** to complete.
10. Under **Certificates & secrets**, create a new secret and save it securely for next steps.
11. In Azure portal, navigate to your Azure key vault.
12. Select **Settings** &gt; **Secrets** and select **+ Generate/Import**.

    ![Screenshot how to navigate to Azure Key Vault.](media/setup-power-bi-scan-catalog-portal/power-bi-key-vault.png)
13. Enter a name for the secret and for **Value**, type the newly created secret for the App registration. Select **Create** to complete.

    ![Screenshot how to generate an Azure Key Vault secret for SPN.](media/setup-power-bi-scan-catalog-portal/power-bi-key-vault-secret-spn.png)
14. If your key vault isn't connected to Microsoft Purview yet, you need to [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account).
15. In the Microsoft Purview Studio, go to the **Data map** in the left menu. Go to **Sources**.
16. Select the registered Power BI source from cross-tenant.
17. Select **+ New scan**.
18. Give your scan a name. Then select the option to include or exclude the personal workspaces.

    Note

    If you switch the configuration of a scan to include or exclude a personal workspace, you trigger a full scan of the Power BI source.
19. Select your self-hosted integration runtime from the drop-down list.
20. For the **Credential**, select **Service Principal**, and then select **+ New** to create a new credential.
21. Create a new credential and provide the following required parameters:

    - **Name**: Provide a unique name for credential
    - **Authentication method**: Service principal
    - **Tenant ID**: Your Power BI tenant ID
    - **Client ID**: Use Service Principal Client ID (App ID) you created earlier

    ![Screenshot of the new credential menu, showing Power BI credential for SPN with all required values supplied.](media/setup-power-bi-scan-catalog-portal/power-bi-scan-spn-authentication.png)
22. Select **Test connection** before continuing to the next steps.

    If the test fails, select **View Report** to see the detailed status and troubleshoot the problem:

    1. *Access - Failed* status means that the user authentication failed. Validate if the App ID and secret are correct. Review if the credential contains the correct client (app) ID from the app registration.
    2. *Assets (+ lineage) - Failed* status means that the authorization between Microsoft Purview and Power BI has failed. Make sure that the user is added to the Fabric Administrator role (former Power BI Administrator role), and has the proper Power BI license assigned.
    3. *Detailed metadata (Enhanced) - Failed* status means that the Power BI admin portal is disabled for the following setting: **Enhance admin APIs responses with detailed metadata**.
23. Set up a scan trigger. Your options are **Recurring** or **Once**.

    ![Screenshot of the Microsoft Purview scan scheduler.](media/setup-power-bi-scan-catalog-portal/scan-trigger.png)
24. On **Review new scan**, select **Save and run** to launch your scan.

Tip

To troubleshoot any issues with scanning:

1. Confirm you have completed the **deployment checklist for your scenario**.
2. Review our [**scan troubleshooting documentation**](register-scan-power-bi-tenant-troubleshoot).

## Deployment checklist

The deployment checklist is a summary of all the steps you'll need to take to set up a cross-tenant Power BI source. You can use it during setup or for troubleshooting, to confirm you've followed all the necessary steps to connect.

# [Public access with Azure IR](#tab/Scenario1)
### Scan cross-tenant Power BI by using delegated authentication in a public network

1. Make sure the Power BI tenant ID is entered correctly during the registration. By default, the Power BI tenant ID that exists in the same Microsoft Entra instance as Microsoft Purview will be populated.
2. Make sure your [Power BI metadata model is up to date by enabling metadata scanning](/en-us/power-bi/admin/service-admin-metadata-scanning-setup#enable-tenant-settings-for-metadata-scanning).
3. From the Azure portal, validate if the Microsoft Purview account network is set to **public access**.
4. From the Power BI tenant admin portal, make sure the Power BI tenant is configured to allow a public network.
5. Check your instance of Azure Key Vault to make sure:

    1. There are no typos in the password or secret.
    2. Microsoft Purview managed identity has **get** and **list** access to secrets.
6. Review your credential to validate that the:

    1. Client ID matches the *Application (Client) ID* of the app registration.
    2. For **delegated auth**, username includes the user principal name, such as `johndoe@contoso.com`.
7. In the Power BI Microsoft Entra tenant, validate the following Power BI admin user settings:

    1. The user is assigned to the Fabric Administrator role (former Power BI Administrator role).
    2. At least one [Power BI license](/en-us/power-bi/admin/service-admin-licensing-organization#subscription-license-types) is assigned to the user.
    3. If the user is recently created, sign in with the user at least once, to make sure that the password is reset successfully, and the user can successfully initiate the session.
    4. There are no multifactor authentication or conditional access policies enforced on the user.
8. In the Power BI Microsoft Entra tenant, validate the following app registration settings:

    1. The app registration exists in your Microsoft Entra tenant where the Power BI tenant is located.
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
9. In Power BI tenant, from Microsoft Entra tenant, make sure Service Principal is member of the new security group.
10. On the Power BI Tenant Admin portal, validate if Allow service principals to use read-only Power BI admin APIs is enabled for the new security group.

# [Public access with Self-hosted IR](#tab/Scenario2)
### Scan cross-tenant Power BI by using delegated authentication in a public network

1. Make sure the Power BI tenant ID is entered correctly during the registration. By default, the Power BI tenant ID that exists in the same Microsoft Entra instance as Microsoft Purview will be populated.
2. Make sure your [Power BI metadata model is up to date by enabling metadata scanning](/en-us/power-bi/admin/service-admin-metadata-scanning-setup#enable-tenant-settings-for-metadata-scanning).
3. From the Azure portal, validate if the Microsoft Purview account Network is set to **public access**.
4. From the Power BI tenant admin portal, make sure the Power BI tenant is configured to allow a public network.
5. Check your instance of Azure Key Vault to make sure:

    1. There are no typos in the password.
    2. Microsoft Purview managed identity has **get** and **list** access to secrets.
6. Review your credential to validate that the:

    1. Client ID matches the *Application (Client) ID* of the app registration.
    2. Username includes the user principal name, such as `johndoe@contoso.com`.
7. In the Power BI Microsoft Entra tenant, validate the following app registration settings:

    1. The app registration exists in your Microsoft Entra tenant where the Power BI tenant is located.
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
8. If delegated authentication is used, in the Power BI Microsoft Entra tenant, validate the following Power BI admin user settings:

    1. The user is assigned to the Fabric Administrator role (former Power BI Administrator role).
    2. At least one [Power BI license](/en-us/power-bi/admin/service-admin-licensing-organization#subscription-license-types) is assigned to the user.
    3. If the user is recently created, sign in with the user at least once, to make sure that the password is reset successfully, and the user can successfully initiate the session.
    4. There are no multifactor authentication or conditional access policies enforced on the user.
9. Validate the following self-hosted runtime settings:

    1. The latest version of the [a self-hosted runtime](data-map-integration-runtime-choose) is installed on the VM.
    2. Network connectivity from the self-hosted runtime to the Power BI tenant is enabled. The following endpoints must be reachable from self-hosted runtime VM:

        - `*.powerbi.com`
        - `*.analysis.windows.net`
    3. Network connectivity from the self-hosted runtime to Microsoft services is enabled.
    4. [JDK 8 or later](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) is installed. Restart the machine after you newly install the JDK for it to take effect.
10. In Power BI tenant, from Microsoft Entra tenant, make sure Service Principal is member of the new security group.
11. On the Power BI Tenant Admin portal, validate if Allow service principals to use read-only Power BI admin APIs is enabled for the new security group.

# [Private access with Managed VNet IR (v2 only)](#tab/Scenario3)
### Scan cross-tenant Power BI using Managed VNet IR (v2 only) with Delegated Authentication or Service Principal in a private network

1. Make sure the Power BI tenant ID is entered correctly during the registration.
2. Make sure your [Power BI metadata model is up to date by enabling metadata scanning](/en-us/power-bi/admin/service-admin-metadata-scanning-setup#enable-tenant-settings-for-metadata-scanning).
3. Check your instance of Azure Key Vault to make sure:

    1. There are no typos in the password.
    2. Microsoft Purview managed identity has **get** and **list** access to secrets.
4. Review your credential to validate that the:

    1. Client ID matches the *Application (Client) ID* of the app registration.
    2. Username includes the user principal name, such as `johndoe@contoso.com`.
5. In the Power BI tenant, validate the following app registration settings:

    1. The app registration exists in your tenant where the Power BI tenant is located.
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

    1. The user is assigned to the Fabric Administrator role (former Power BI Administrator role).
    2. At least one [Power BI license](/en-us/power-bi/admin/service-admin-licensing-organization#subscription-license-types) is assigned to the user.
    3. If the user is recently created, sign in with the user at least once, to make sure that the password is reset successfully, and the user can successfully initiate the session.
    4. There are no multifactor authentication or conditional access policies enforced on the user.
7. From Microsoft Entra tenant, make sure Service Principal is member of the new security group.
8. On the Power BI Tenant Admin portal, validate if Allow service principals to use read-only Power BI admin APIs is enabled for the new security group.

# [Private access](#tab/Scenario4)
### Scan cross-tenant Power BI using self-hosted IR with Delegated Authentication or Service Principal in a private network

1. Make sure the Power BI tenant ID is entered correctly during the registration.
2. Make sure your [Power BI metadata model is up to date by enabling metadata scanning](/en-us/power-bi/admin/service-admin-metadata-scanning-setup#enable-tenant-settings-for-metadata-scanning).
3. Check your instance of Azure Key Vault to make sure:

    1. There are no typos in the password.
    2. Microsoft Purview managed identity has **get** and **list** access to secrets.
4. Review your credential to validate that the:

    1. Client ID matches the *Application (Client) ID* of the app registration.
    2. Username includes the user principal name, such as `johndoe@contoso.com`.
5. In the Power BI tenant, validate the following app registration settings:

    1. The app registration exists in your tenant where the Power BI tenant is located.
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

    1. The user is assigned to the Fabric Administrator role (former Power BI Administrator role).
    2. At least one [Power BI license](/en-us/power-bi/admin/service-admin-licensing-organization#subscription-license-types) is assigned to the user.
    3. If the user is recently created, sign in with the user at least once, to make sure that the password is reset successfully, and the user can successfully initiate the session.
    4. There are no multifactor authentication or conditional access policies enforced on the user.
7. Validate Self-hosted runtime settings:

    1. Latest version of [a self-hosted runtime](data-map-integration-runtime-choose) is installed on the VM.
    2. [JDK 8 or later](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) is installed. Restart the machine after you newly install the JDK for it to take effect.
8. Review network configuration and validate if:

    1. If your Power BI doesn't allow public access, make sure [private endpoint for Power BI tenant](/en-us/power-bi/enterprise/service-security-private-links) is deployed.
    2. All required [private endpoints for Microsoft Purview](data-gov-classic-private-link-end-to-end) are deployed.
    3. Network connectivity from Self-hosted runtime to Power BI tenant is enabled. The following endpoints must be reachable from self-hosted runtime VM:

        - `*.powerbi.com`
        - `*.analysis.windows.net`
    4. Network connectivity from the self-hosted runtime to Microsoft services is enabled.
9. From Microsoft Entra tenant, make sure Service Principal is member of the new security group.
10. On the Power BI Tenant Admin portal, validate if Allow service principals to use read-only Power BI admin APIs is enabled for the new security group.

---