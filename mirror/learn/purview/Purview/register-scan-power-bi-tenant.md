---
layout: Conceptual
title: Connect to and manage a Power BI tenant in Microsoft Purview (same tenant) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-power-bi-tenant
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
description: Learn how to connect to a Power BI tenant in the same tenant as Microsoft Purview, and use Microsoft Purview features to scan and manage your Power BI tenant source
locale: en-us
document_id: 2999b5ea-2686-cbb4-e2fd-b6801c4052e4
document_version_independent_id: 2999b5ea-2686-cbb4-e2fd-b6801c4052e4
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-power-bi-tenant.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-power-bi-tenant
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-power-bi-tenant.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: dd14e0bf-9041-23fe-12aa-6467db1113be
---

# Connect to and manage a Power BI tenant in Microsoft Purview (same tenant) | Microsoft Learn

This article outlines how to register a Power BI tenant in a **same-tenant scenario**, and how to authenticate and interact with the tenant in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

Note

The Power BI data source in Microsoft Purview has been renamed to Fabric in all regions. You can still use “Power BI” as the keyword to quickly locate the source to register a Power BI tenant and set up a scan.

Starting from December 13th 2023, scanning Fabric tenants registered with the Fabric data source in Microsoft Purview will capture metadata and lineage from Fabric items including Power BI. There are no other configuration steps needed to enable scanning Fabric items besides Power BI for existing scans. Fabric tenants and Power BI tenants will share the same data source and same experience to set up scans. For scanning a Fabric tenant, see our [Fabric documentation](register-scan-fabric-tenant).

![Graphic showing the renaming of Power BI data source to Fabric.](media/setup-power-bi-scan-catalog-portal/rename-power-bi-data-source.png)

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | Yes | Yes |

When scanning Power BI source, Microsoft Purview supports:

- Extracting technical metadata including:

    - Workspaces
    - Dashboards
    - Reports
    - Datasets including the tables and columns
    - Dataflows
    - Datamarts
- Fetching static lineage on assets relationships among above Power BI artifacts and external data source assets. Learn more from [Power BI lineage](data-map-lineage-power-bi).

See a list of [metadata available for Power BI](register-scan-power-bi-tenant-available-metadata).

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

### Supported scenarios for Power BI scans

| **Scenarios** | **Microsoft Purview public access allowed/denied** | **Power BI public access allowed /denied** | **Runtime option** | **Authentication option** | **Deployment checklist** |
| --- | --- | --- | --- | --- | --- |
| Public access with Azure IR | Allowed | Allowed | Azure Runtime | Managed Identity / Delegated authentication / Service principal | Review deployment checklist |
| Public access with Self-hosted IR | Allowed | Allowed | Self-hosted runtime | Delegated authentication / Service principal | Review deployment checklist |
| Private access | Denied | Allowed | Managed VNet IR (v2 only) | Managed Identity / Delegated authentication / Service principal | Review deployment checklist |
| Private access | Allowed | Denied | Self-hosted runtime | Delegated authentication / Service principal | Review deployment checklist |
| Private access | Denied | Allowed | Self-hosted runtime | Delegated authentication / Service principal | Review deployment checklist |
| Private access | Denied | Denied | Self-hosted runtime | Delegated authentication / Service principal | Review deployment checklist |

### Known limitations

- If Power BI tenant is protected behind a private endpoint, [standard or kubernetes supported self-hosted runtimes](data-map-integration-runtime-choose) are the only options to scan.
- Delegated authentication and service principal are the only supported authentication options when a self-hosted integration runtime is used during the scan.
- If Power BI dataset schema isn't shown after scan, it's due to one of the current limitations with [Power BI Metadata scanner](/en-us/power-bi/admin/service-admin-metadata-scanning).
- Empty workspaces are skipped.
- Other limits please refer to [Microsoft Purview limits](/en-us/purview/how-to-manage-quotas#microsoft-purview-limits).

## Prerequisites

Before you start, make sure you have the following prerequisites:

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).

## Authentication options

- Managed Identity
- Delegated Authentication
- Service Principal

## Deployment checklist

Use any of the following deployment checklists during the setup or for troubleshooting purposes, based on your scenario:

# [Public access with Azure IR](#tab/Scenario1)
### Scan same-tenant Power BI using Azure IR and Managed Identity in public network

1. Make sure Power BI and Microsoft Purview accounts are in the same tenant.
2. Make sure Power BI tenant ID is entered correctly during the registration.
3. Make sure your [Power BI Metadata model is up to date by enabling metadata scanning.](/en-us/power-bi/admin/service-admin-metadata-scanning-setup#enable-tenant-settings-for-metadata-scanning)
4. From Azure portal, validate if Microsoft Purview account Network is set to public access.
5. From Power BI tenant Admin Portal, make sure Power BI tenant is configured to allow public network.
6. In Microsoft Entra tenant, create a security group.
7. From Microsoft Entra tenant, make sure Microsoft Purview account MSI is member of the new security group.
8. On the Power BI Tenant Admin portal, validate if Allow service principals to use read-only Power BI admin APIs is enabled for the new security group.

# [Public access with Self-hosted IR](#tab/Scenario2)
### Scan same-tenant Power BI using self-hosted IR with Delegated Authentication or Service Principal in public network

1. Make sure Power BI and Microsoft Purview accounts are in the same tenant.
2. Make sure Power BI tenant ID is entered correctly during the registration.
3. Make sure your [Power BI Metadata model is up to date by enabling metadata scanning.](/en-us/power-bi/admin/service-admin-metadata-scanning-setup#enable-tenant-settings-for-metadata-scanning)
4. From Azure portal, validate if Microsoft Purview account Network is set to public access.
5. From Power BI tenant Admin Portal, make sure Power BI tenant is configured to allow public network.
6. Check your Azure Key Vault to make sure:

    1. There are no typos in the password or secret.
    2. Microsoft Purview Managed Identity has get/list access to secrets.
7. Review your credential to validate:

    1. Client ID matches *Application (Client) ID* of the app registration.
    2. Username includes the user principal name such as `johndoe@contoso.com`.
8. Validate App registration settings to make sure:

    1. App registration exists in your Microsoft Entra tenant.
    2. If service principal is used, under **API permissions**, the following **delegated permissions** are assigned with read for the following APIs:

        - Microsoft Graph openid
        - Microsoft Graph User.Read
    3. If delegated authentication is used, under **API permissions**, the following **delegated permissions** and **grant admin consent for the tenant** is set up with read for the following APIs:

        - Power BI Service Tenant.Read.All
        - Microsoft Graph openid
        - Microsoft Graph User.Read
    4. Under **Authentication**, **Allow public client flows** is enabled.
9. If delegated authentication is used, validate Power BI admin user settings to make sure:

    1. User is assigned to Fabric Administrator role (former Power BI Administrator role).
    2. At least one [Power BI license](/en-us/power-bi/admin/service-admin-licensing-organization#subscription-license-types) is assigned to the user.
    3. If user is recently created, sign in with the user at least once to make sure password is reset successfully, and user can successfully initiate the session.
    4. There's no MFA or Conditional Access Policies are enforced on the user.
10. Validate Self-hosted runtime settings:

    1. Latest version of [Self-hosted runtime](https://go.microsoft.com/fwlink/?linkid=2246619) is installed on the VM.
    2. Network connectivity from Self-hosted runtime to Power BI tenant is enabled. The following endpoints must be reachable from self-hosted runtime VM:

        - `*.powerbi.com`
        - `*.analysis.windows.net`
    3. Network connectivity from Self-hosted runtime to Microsoft services is enabled.
    4. [JDK 8 or later](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) is installed. Restart the machine after you newly install the JDK for it to take effect.
11. In Microsoft Entra tenant, create a security group.
12. From Microsoft Entra tenant, make sure Service Principal is member of the new security group.
13. On the Power BI Tenant Admin portal, validate if Allow service principals to use read-only Power BI admin APIs is enabled for the new security group.

# [Private access with Managed VNet IR (v2 only)](#tab/Scenario3)
### Scan same-tenant Power BI using Managed VNet IR (v2 only) with Managed Identity, Delegated Authentication or Service Principal in a private network

1. Make sure Power BI and Microsoft Purview accounts are in the same tenant.
2. Make sure Power BI tenant ID is entered correctly during the registration.
3. Make sure your [Power BI Metadata model is up to date by enabling metadata scanning.](/en-us/power-bi/admin/service-admin-metadata-scanning-setup#enable-tenant-settings-for-metadata-scanning)
4. Check your Azure Key Vault to make sure:

    1. There are no typos in the password.
    2. Microsoft Purview Managed Identity has get/list access to secrets.
5. Review your credential to validate:

    1. Client ID matches *Application (Client) ID* of the app registration.
    2. Username includes the user principal name such as `johndoe@contoso.com`.
6. If Delegated Authentication is used, validate Power BI admin user settings to make sure:

    1. User is assigned to Fabric Administrator role (former Power BI Administrator role).
    2. At least one [Power BI license](/en-us/power-bi/admin/service-admin-licensing-organization#subscription-license-types) is assigned to the user.
    3. If user is recently created, sign in with the user at least once to make sure password is reset successfully and user can successfully initiate the session.
    4. There's no MFA or Conditional Access Policies are enforced on the user.
7. Validate App registration settings to make sure:

    1. App registration exists in your Microsoft Entra tenant.
    2. If service principal is used, under **API permissions**, the following **delegated permissions** are assigned with read for the following APIs:

        - Microsoft Graph openid
        - Microsoft Graph User.Read
    3. If delegated authentication is used, under **API permissions**, the following **delegated permissions** and **grant admin consent for the tenant** is set up with read for the following APIs:

        - Power BI Service Tenant.Read.All
        - Microsoft Graph openid
        - Microsoft Graph User.Read
    4. Under **Authentication**, **Allow public client flows** is enabled.
8. In Microsoft Entra tenant, create a security group.
9. From Microsoft Entra tenant, make sure Service Principal is member of the new security group.
10. On the Power BI Tenant Admin portal, validate if Allow service principals to use read-only Power BI admin APIs is enabled for the new security group.

# [Private access with Self-hosted IR](#tab/Scenario4)
### Scan same-tenant Power BI using self-hosted IR with Delegated Authentication or Service Principal in a private network

1. Make sure Power BI and Microsoft Purview accounts are in the same tenant.
2. Make sure Power BI tenant ID is entered correctly during the registration.
3. Make sure your [Power BI Metadata model is up to date by enabling metadata scanning.](/en-us/power-bi/admin/service-admin-metadata-scanning-setup#enable-tenant-settings-for-metadata-scanning)
4. Check your Azure Key Vault to make sure:

    1. There are no typos in the password.
    2. Microsoft Purview Managed Identity has get/list access to secrets.
5. Review your credential to validate:

    1. Client ID matches *Application (Client) ID* of the app registration.
    2. Username includes the user principal name such as `johndoe@contoso.com`.
6. If Delegated Authentication is used, validate Power BI admin user settings to make sure:

    1. User is assigned to Fabric Administrator role (former Power BI Administrator role).
    2. At least one [Power BI license](/en-us/power-bi/admin/service-admin-licensing-organization#subscription-license-types) is assigned to the user.
    3. If user is recently created, sign in with the user at least once to make sure password is reset successfully and user can successfully initiate the session.
    4. There's no MFA or Conditional Access Policies are enforced on the user.
7. Validate Self-hosted runtime settings:

    1. Latest version of [Self-hosted runtime](https://go.microsoft.com/fwlink/?linkid=2246619) is installed on the VM.
    2. [JDK 8 or later](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) is installed. Restart the machine after you newly install the JDK for it to take effect.
8. Validate App registration settings to make sure:

    1. App registration exists in your Microsoft Entra tenant.
    2. If service principal is used, under **API permissions**, the following **delegated permissions** are assigned with read for the following APIs:

        - Microsoft Graph openid
        - Microsoft Graph User.Read
    3. If delegated authentication is used, under **API permissions**, the following **delegated permissions** and **grant admin consent for the tenant** is set up with read for the following APIs:

        - Power BI Service Tenant.Read.All
        - Microsoft Graph openid
        - Microsoft Graph User.Read
    4. Under **Authentication**, **Allow public client flows** is enabled.
9. Review network configuration and validate if:

    1. If your Power BI doesn't allow public access, make sure [private endpoint for Power BI tenant](/en-us/power-bi/enterprise/service-security-private-links) is deployed.
    2. All required [private endpoints for Microsoft Purview](data-gov-classic-private-link-end-to-end) are deployed.
    3. Network connectivity from Self-hosted runtime to Power BI tenant is enabled. The following endpoints must be reachable from self-hosted runtime VM:

        - `*.powerbi.com`
        - `*.analysis.windows.net`
    4. Network connectivity from Self-hosted runtime to Microsoft services is enabled through private network.
10. In Microsoft Entra tenant, create a security group.
11. From Microsoft Entra tenant, make sure Service Principal is member of the new security group.
12. On the Power BI Tenant Admin portal, validate if Allow service principals to use read-only Power BI admin APIs is enabled for the new security group.

---

## Register Power BI tenant

This section describes how to register a Power BI tenant in Microsoft Purview for same-tenant scenario.

1. Select the **Data Map** on the left navigation.
2. Then select **Register**.

    Select **Fabric** as your data source. It includes Power BI sources and assets.

    ![Image showing the list of data sources available to choose, with the Fabric source highlighted.](media/setup-power-bi-scan-catalog-portal/select-power-bi-data-source.png)
3. Give your data source a name.

    The name must be between 3-63 characters long and must contain only letters, numbers, underscores, and hyphens. Spaces aren't allowed.

    By default, the system will find the Fabric tenant that exists in the same Microsoft Entra tenant.
4. Select the collection where you want to register the source.
5. Select **Register**.

## Scan same-tenant Power BI

Tip

To troubleshoot any issues with scanning:

1. Confirm you have completed the **deployment checklist for your scenario**.
2. Review our [**scan troubleshooting documentation**](register-scan-power-bi-tenant-troubleshoot).

### Authenticate to Power BI tenant

In Microsoft Entra tenant, where Power BI tenant is located:

1. In the [Azure portal](https://portal.azure.com), search for **Microsoft Entra ID**.
2. Create a new security group in your Microsoft Entra ID, by following [Create a basic group and add members using Microsoft Entra ID](/en-us/azure/active-directory/fundamentals/active-directory-groups-create-azure-portal).

    Tip

    You can skip this step if you already have a security group you want to use.
3. Select **Security** as the **Group Type**.

    ![Screenshot of security group type.](media/setup-power-bi-scan-powershell/security-group.png)
4. Add relevant user to the security group:

    - If you're using **Managed Identity** as authentication method, add your Microsoft Purview managed identity to this security group. Select **Members**, then select **+ Add members**.

        ![Screenshot of how to add the catalog's managed instance to group.](media/setup-power-bi-scan-powershell/add-group-member.png)
    - If you're using **delegated authentication** or **service principal** as authentication method, add your **service principal** to this security group. Select **Members**, then select **+ Add members**.
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

### Create scan for same-tenant Power BI using Azure IR and Managed Identity

This is a suitable scenario, if both Microsoft Purview and Power BI tenant are configured to allow public access in the network settings.

To create and run a new scan, do the following:

1. In the Microsoft Purview Studio, navigate to the **Data map** in the left menu.
2. Navigate to **Sources**.
3. Select the registered Power BI source.
4. Select **+ New scan**.
5. Give your scan a name. Then select the option to include or exclude the personal workspaces.

    ![Image showing Power BI scan setup.](media/setup-power-bi-scan-catalog-portal/power-bi-scan-setup.png)

    Note

    Switching the configuration of a scan to include or exclude a personal workspace will trigger a full scan of Power BI source.
6. Select **Test Connection** before continuing to next steps. If **Test Connection** failed, select **View Report** to see the detailed status and troubleshoot the problem.

    1. Access - Failed status means the user authentication failed. Scans using managed identity will always pass because no user authentication required.
    2. Assets (+ lineage) - Failed status means the Microsoft Purview - Power BI authorization has failed. Make sure the Microsoft Purview managed identity is added to the security group associated in Power BI admin portal.
    3. Detailed metadata (Enhanced) - Failed status means the Power BI admin portal is disabled for the following setting - **Enhance admin APIs responses with detailed metadata**

    ![Screenshot of test connection status report page.](media/setup-power-bi-scan-catalog-portal/power-bi-test-connection-status-report.png)
7. Set up a scan trigger. Your options are **Recurring**, and **Once**.

    ![Screenshot of the Microsoft Purview scan scheduler.](media/setup-power-bi-scan-catalog-portal/scan-trigger.png)
8. On **Review new scan**, select **Save and run** to launch your scan.

    ![Screenshot of Save and run Power BI source using Managed Identity.](media/setup-power-bi-scan-catalog-portal/save-run-power-bi-scan-managed-identity.png)

### Create scan for same-tenant using self-hosted IR with service principal

This scenario can be used when Microsoft Purview and Power BI tenant or both, are configured to use private endpoint and deny public access. Additionally, this option is also applicable if Microsoft Purview and Power BI tenant are configured to allow public access.

For more information related to Power BI network, see [How to configure private endpoints for accessing Power BI](/en-us/power-bi/enterprise/service-security-private-links).

For more information about Microsoft Purview network settings, see [Use private endpoints for your Microsoft Purview account](data-gov-classic-private-link).

To create and run a new scan, do the following:

1. In the [Azure portal](https://portal.azure.com), select **Microsoft Entra ID** and create an App Registration in the tenant. Provide a web URL in the **Redirect URI**. [For information about the Redirect URI see this documentation from Microsoft Entra ID](/en-us/azure/active-directory/develop/reply-url).

    ![Screenshot how to create App in Microsoft Entra ID.](media/setup-power-bi-scan-catalog-portal/power-bi-scan-app-registration.png)
2. Take note of Client ID(App ID).

    ![Screenshot how to create a service principal.](media/setup-power-bi-scan-catalog-portal/power-bi-create-service-principle.png)
3. From Microsoft Entra dashboard, select newly created application and then select **App registration**. From **API Permissions**, assign the application the following delegated permissions:

    - Microsoft Graph openid
    - Microsoft Graph User.Read

    ![Screenshot of delegated permissions on Microsoft Graph.](media/setup-power-bi-scan-catalog-portal/power-bi-scan-spn-api-permissions.png)
4. Under **Advanced settings**, enable **Allow Public client flows**.
5. Under **Certificates & secrets**, create a new secret and save it securely for next steps.
6. In Azure portal, navigate to your Azure key vault.
7. Select **Settings** &gt; **Secrets** and select **+ Generate/Import**.

    ![Screenshot how to navigate to Azure Key Vault.](media/setup-power-bi-scan-catalog-portal/power-bi-key-vault.png)
8. Enter a name for the secret and for **Value**, type the newly created secret for the App registration. Select **Create** to complete.

    ![Screenshot how to generate an Azure Key Vault secret for SPN.](media/setup-power-bi-scan-catalog-portal/power-bi-key-vault-secret-spn.png)
9. If your key vault isn't connected to Microsoft Purview yet, you'll need to [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account)
10. In the Microsoft Purview Studio, navigate to the **Data map** in the left menu.
11. Navigate to **Sources**.
12. Select the registered Power BI source.
13. Select **+ New scan**.
14. Give your scan a name. Then select the option to include or exclude the personal workspaces.

    Note

    Switching the configuration of a scan to include or exclude a personal workspace will trigger a full scan of Power BI source.
15. Select your self-hosted integration runtime from the drop-down list.

    ![Image showing Power BI scan setup using SHIR for same tenant.](media/setup-power-bi-scan-catalog-portal/power-bi-scan-shir.png)
16. For the **Credential**, select **service principal** and select **+ New** to create a new credential.
17. Create a new credential and provide required parameters:

    - **Name**: Provide a unique name for credential
    - **Authentication method**: Service principal
    - **Tenant ID**: Your Power BI tenant ID
    - **Client ID**: Use Service Principal Client ID (App ID) you created earlier

    ![Screenshot of the new credential menu, showing Power BI credential for SPN with all required values supplied.](media/setup-power-bi-scan-catalog-portal/power-bi-scan-spn-authentication.png)
18. Select **Test Connection** before continuing to next steps. If **Test Connection** failed, select **View Report** to see the detailed status and troubleshoot the problem

    1. Access - Failed status means the user authentication failed. Scans using managed identity will always pass because no user authentication required.
    2. Assets (+ lineage) - Failed status means the Microsoft Purview - Power BI authorization has failed. Make sure the Microsoft Purview managed identity is added to the security group associated in Power BI admin portal.
    3. Detailed metadata (Enhanced) - Failed status means the Power BI admin portal is disabled for the following setting - **Enhance admin APIs responses with detailed metadata**

    ![Screenshot of test connection status report page.](media/setup-power-bi-scan-catalog-portal/power-bi-test-connection-status-report.png)
19. Set up a scan trigger. Your options are **Recurring**, and **Once**.

    ![Screenshot of the Microsoft Purview scan scheduler.](media/setup-power-bi-scan-catalog-portal/scan-trigger.png)
20. On **Review new scan**, select **Save and run** to launch your scan.

### Create scan for same-tenant using self-hosted IR with delegated authentication

This scenario can be used when Microsoft Purview and Power BI tenant or both, are configured to use private endpoint and deny public access. Additionally, this option is also applicable if Microsoft Purview and Power BI tenant are configured to allow public access.

For more information related to Power BI network, see [How to configure private endpoints for accessing Power BI](/en-us/power-bi/enterprise/service-security-private-links).

For more information about Microsoft Purview network settings, see [Use private endpoints for your Microsoft Purview account](data-gov-classic-private-link).

To create and run a new scan, do the following:

1. Create a user account in Microsoft Entra tenant and assign the user to Microsoft Entra role, **Fabric Administrator**. Take note of username and sign in to change the password.
2. Assign proper Power BI license to the user.
3. Navigate to your Azure key vault.
4. Select **Settings** &gt; **Secrets** and select **+ Generate/Import**.

    ![Screenshot how to navigate to Azure Key Vault.](media/setup-power-bi-scan-catalog-portal/power-bi-key-vault.png)
5. Enter a name for the secret and for **Value**, type the newly created password for the Microsoft Entra user. Select **Create** to complete.

    ![Screenshot how to generate an Azure Key Vault secret.](media/setup-power-bi-scan-catalog-portal/power-bi-key-vault-secret.png)
6. If your key vault isn't connected to Microsoft Purview yet, you'll need to [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account)
7. Create an App Registration in your Microsoft Entra tenant. Provide a web URL in the **Redirect URI**.

    ![Screenshot how to create App in Microsoft Entra ID.](media/setup-power-bi-scan-catalog-portal/power-bi-scan-app-registration.png)
8. Take note of Client ID(App ID).

    ![Screenshot how to create a service principal.](media/setup-power-bi-scan-catalog-portal/power-bi-create-service-principle.png)
9. From Microsoft Entra dashboard, select newly created application and then select **App registration**. Assign the application the following delegated permissions, and grant admin consent for the tenant:

    - Power BI Service Tenant.Read.All
    - Microsoft Graph openid
    - Microsoft Graph User.Read

    ![Screenshot of delegated permissions on Power BI Service and Microsoft Graph.](media/setup-power-bi-scan-catalog-portal/power-bi-delegated-permissions.png)
10. Under **Advanced settings**, enable **Allow Public client flows**.
11. In the Microsoft Purview Studio, navigate to the **Data map** in the left menu.
12. Navigate to **Sources**.
13. Select the registered Power BI source.
14. Select **+ New scan**.
15. Give your scan a name. Then select the option to include or exclude the personal workspaces.

    Note

    Switching the configuration of a scan to include or exclude a personal workspace will trigger a full scan of Power BI source.
16. Select your self-hosted integration runtime from the drop-down list.

    ![Image showing Power BI scan setup using SHIR for same tenant.](media/setup-power-bi-scan-catalog-portal/power-bi-scan-shir.png)
17. For the **Credential**, select **Delegated authentication** and select **+ New** to create a new credential.
18. Create a new credential and provide required parameters:

    - **Name**: Provide a unique name for credential
    - **Authentication method**: Delegated auth
    - **Client ID**: Use Service Principal Client ID (App ID) you created earlier
    - **User name**: Provide the username of Fabric Administrator you created earlier
    - **Password**: Select the appropriate Key vault connection and the **Secret name** where the Power BI account password was saved earlier.

    ![Screenshot of the new credential menu, showing Power B I credential with all required values supplied.](media/setup-power-bi-scan-catalog-portal/power-bi-scan-delegated-authentication.png)
19. Select **Test Connection** before continuing to next steps. If **Test Connection** failed, select **View Report** to see the detailed status and troubleshoot the problem

    1. Access - Failed status means the user authentication failed. Scans using managed identity will always pass because no user authentication required.
    2. Assets (+ lineage) - Failed status means the Microsoft Purview - Power BI authorization has failed. Make sure the Microsoft Purview managed identity is added to the security group associated in Power BI admin portal.
    3. Detailed metadata (Enhanced) - Failed status means the Power BI admin portal is disabled for the following setting - **Enhance admin APIs responses with detailed metadata**

    ![Screenshot of test connection status report page.](media/setup-power-bi-scan-catalog-portal/power-bi-test-connection-status-report.png)
20. Set up a scan trigger. Your options are **Recurring**, and **Once**.

    ![Screenshot of the Microsoft Purview scan scheduler.](media/setup-power-bi-scan-catalog-portal/scan-trigger.png)
21. On **Review new scan**, select **Save and run** to launch your scan.

    ![Screenshot of Save and run Power BI source.](media/setup-power-bi-scan-catalog-portal/save-run-power-bi-scan.png)

### Scope your scan

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

In the Scope your scan stage, data source administrators can scope the scans by specifying the workspaces as needed. Data source administrators can either select from the workspace list under the tenant or directly input the workspace GUIDs to scope the scan. No additional permission is required to use the scoped scan. There are two options available and by default the option "No" is selected and you can directly click on "Continue" to proceed to run a full scan or select the "Yes" to enable the scoped scan experience.

![Screenshot that shows the Scope your scan with option No selected.](media/setup-power-bi-scan-catalog-portal/scope-your-scan-no.png)

If the scoped scan is enabled, you will see a list of existing workspaces under the tenant on the left hand side (currently there’s a limitation that the UI selection experience only supports less than 5000 workspaces) and you can select the workspaces and add to the list on the right hand side. If personal workspace is configured as "Include", personal workspaces will show in the workspace list with a prefix "PersonalWorkspace ". You can directly click on the workspace(s) and click on the button "Add to list" to put the workspaces to the list of selected workspaces. You can input keyword of the workspace name or workspace GUID in the search box to filter out the workspace(s) for selection.

![Screenshot that shows the Scope your scan with option Yes selected.](media/setup-power-bi-scan-catalog-portal/scope-your-scan-yes.png)

You can also directly input the workspace GUID and add it to the list of selected workspaces.

![Screenshot that shows the Scope your scan with option Yes selected and manual input.](media/setup-power-bi-scan-catalog-portal/scope-your-scan-yes-manual.png)

Note

- Scoping scan by selecting from Microsoft Fabric or Power BI tenant is only supported when the total number of workspaces is less than 5000 (include or exclude personal workspaces will be considered), or you need to switch to manual input of workspace GUIDs to scope your scan.
- You can switch between selecting workspaces from Microsoft Fabric or Power BI tenant, or entering workspace GUID manually and the input will be merged into the same list of selected workspaces.
- Microsoft Purview will check whether the GUID input by user has a correct format but will not check whether the GUID represents a valid workspace in the Microsoft Fabric or Power BI tenant. If invalid GUIDs are included in scoped scan, the scan will complete with exceptions and you can find those invalid GUIDs in the scan log.
- If personal workspace is configured as “Exclude”, the GUIDs for personal workspaces can still be added to the list of selected workspaces but will be skipped in the scan and these GUIDs will be included in the scan log.
- If self-hosted integration runtime is used, version 5.40.8836.1 and above is required and only manual input of workspace GUIDs is supported in the scoped scan.
- If managed VNet integration runtime (v2) is used, only manual input of workspace GUIDs is supported in the scoped scan.