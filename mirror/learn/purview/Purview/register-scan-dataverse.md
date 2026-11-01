---
layout: Conceptual
title: Connect to and manage Microsoft Dataverse in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-dataverse
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article outlines the process to register a Microsoft Dataverse environment in Microsoft Purview including instructions to authenticate and interact with the Microsoft Dataverse source.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: shjia
ms.service: purview
ms.subservice: purview-data-map
ms.topic: how-to
ms.date: 2026-02-02T00:00:00.0000000Z
ms.custom:
- template-how-to
- sfi-image-nochange
locale: en-us
document_id: 18844b16-53d5-6335-4305-9eca0b195cd6
document_version_independent_id: 18844b16-53d5-6335-4305-9eca0b195cd6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-dataverse.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-dataverse
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-dataverse.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/0ceb3227-2ff7-4d97-8e75-3d7b9ccc937a
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/4d680e1a-c470-4772-a236-5c714bd09be0
platformId: 12d3d168-665d-3f79-b116-cf0b2251d4af
---

# Connect to and manage Microsoft Dataverse in Microsoft Purview | Microsoft Learn

This article outlines the process to register and govern a Microsoft Dataverse environment data source in Microsoft Purview including instructions to authenticate and interact with the Microsoft Dataverse source.

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | No | Yes |

When scanning Dataverse source, Microsoft Purview supports extracting technical metadata including:

- Environment
- Tables, including columns

When setting up a scan, you can choose to scope the scan by selecting tables as needed.

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

### Known limitations

- When object is deleted from the data source, currently the subsequent scan won't automatically remove the corresponding asset in Microsoft Purview.
- Dataverse integration with Microsoft Purview Data Map isn't available in sovereign clouds.

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You need to be a Data Source Administrator and Data Reader to register a source and manage it in the classic Microsoft Purview governance portal. See our [Microsoft Purview Permissions page](data-gov-classic-permissions) for details.
- You need to have the permission in your Dataverse environment to [create an application user](/en-us/power-platform/admin/manage-application-users#create-an-application-user) and assign the Service Reader role for the user.

## Register

This section describes how to register Dataverse in Microsoft Purview. Before you create a scan, it’s necessary to register the data source in Microsoft Purview.

### Prerequisites for register

- You need to be a Data Source Admin and one of the other Purview roles (for example, Data Reader or Data Share Contributor) to register a source and manage it in the classic Microsoft Purview governance portal. See our [Microsoft Purview Permissions page](data-gov-classic-permissions) for details.

### Steps to register

It's important to register the data source in Microsoft Purview prior to setting up a scan for the data source.

1. Go to the classic Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Select the classic [**Microsoft Purview governance portal**](https://web.purview.azure.com/).
2. Navigate to the **Data Map --&gt; Sources**

    ![Screenshot that shows the link to open classic Microsoft Purview governance portal.](media/register-scan-dataverse/register-dataverse-open-purview-studio.png)

    ![Screenshot that navigates to the Sources link in the Data Map.](media/register-scan-dataverse/register-dataverse-sources.png)
3. Create the [Collection hierarchy](data-map-collections-create-classic) using the **Collections** menu and assign permissions to individual subcollections, as required

    ![Screenshot that shows the collection menu to create collection hierarchy.](media/register-scan-dataverse/register-dataverse-collections.png)
4. Navigate to the appropriate collection under the **Sources** menu and select the **Register** icon to register a new Dataverse data source

    ![Screenshot that shows the collection used to register the data source.](media/register-scan-dataverse/register-dataverse-register-source.png)
5. Select the **Dataverse** data source and select **Continue**

    ![Screenshot that allows selection of the data source.](media/register-scan-dataverse/register-dataverse-select-data-source.png)
6. Provide a suitable **Name** for the data source. Fill in the Web API endpoint for your Dataverse environment as **Environment URL** and select a **collection** and select **Apply**.

    ![Screenshot that shows the details to be entered in order to register the data source.](media/register-scan-dataverse/register-dataverse-data-source-details.png)

    You can get the Web API endpoint from [Developer resources](/en-us/power-apps/developer/data-platform/view-download-developer-resources) from the Microsoft Power Apps maker portal.

    ![Screenshot that shows how to find developer resources in order to register the data source.](media/register-scan-dataverse/register-dataverse-sources-developer-resources.png)

    ![Screenshot that shows how to find Web API endpoint in developer resources.](media/register-scan-dataverse/register-dataverse-sources-developer-resources-sample.png)
7. The Dataverse source is shown under the selected Collection

## Scan

### Authentication method

Currently Microsoft Purview supports the following options to scan Dataverse:

- **System assigned managed identity (SAMI)**. This is an identity that's associated directly with your Microsoft Purview account. The SAMI is created when your Microsoft Purview resource is created. It's managed by Azure and uses your Microsoft Purview account's name.
- **Service principal**. A service principal is an application that can be assigned permissions like any other group or user, without being associated directly with a person.

# [System assigned managed identity](#tab/MI)
#### Using a system assigned managed identity for scanning

The system-assigned managed identity needs permission to get metadata from Dataverse environments. It must also be authorized to query the Dataverse tables to sample for classification. There are several steps to allow Microsoft Purview to use system-assigned managed identity to scan your Dataverse environment.

##### Get the application ID for the system-assigned managed identity

1. Go to **Data Map** &gt; **Sources** to view the collection hierarchy.
2. Select the **New Scan** icon under the Dataverse source that you registered earlier.
3. For **Credential**, select **Microsoft Purview MSI (system)** from the drop-down list then select **Show more** to view details about the system assigned managed identity.

    ![Screenshot that shows how to select sami auth.](media/register-scan-dataverse/scan-dataverse-config-sami-auth-select.png)

    ![Screenshot that shows how to show more for sami auth.](media/register-scan-dataverse/scan-dataverse-config-sami-auth-show-more.png)
4. Record the managed identity application ID.

    ![Screenshot that shows how to find sami.](media/register-scan-dataverse/scan-dataverse-config-sami-auth-record-id.png)

##### Create and enable an application user in Power Platform Admin Center

An application user is needed to be created in the Dataverse environment that you want to scan in Microsoft Purview. Follow the steps in [Create An Application User](/en-us/power-platform/admin/manage-application-users#create-an-application-user) to create the user with the application ID you recorded and assign the security role **Service Reader** to it.

![Screenshot that shows how to create application user.](media/register-scan-dataverse/scan-dataverse-config-create-app-user.png)

You can check the application user in the Details page. Now the application user is bound with the system assigned managed identity created with your Microsoft Purview resource.

# [Service Principal](#tab/SP)
#### Using Service Principal for scanning

There are several steps to allow Microsoft Purview to use a service principal to scan your Dataverse environment.

##### Create or use an existing service principal

To use a service principal, you can use an existing one or create a new one. If you're going to use an existing service principal, skip to the next step. If you have to create a new Service Principal, follow these steps as described in [App registration](data-map-service-principal#app-registration):

1. Navigate to your Azure portal.
2. Select **Microsoft Entra ID** from the left-hand side menu.
3. Select **App registrations** and + **New application registration**.
4. Enter a name for the **application** (the service principal name).
5. Select **Accounts in this organizational directory only**.
6. For **Redirect URI** select **Web** and enter any URL you want. If you have an authentication endpoint for your organization you want to use, this is the place.
7. Then select **Register**.
8. Copy the **Application (client) ID** value.

Then follow the steps as described in [Adding a secret to the client credentials](data-map-service-principal#add-a-secret-to-the-client-credentials) and copy the value of the **Secret value**.

Record the properties below after you finish the app registration and this information will be used in the next step to create an application user in Power Platform:

- Directory (tenant) ID
- Application (client) ID
- Secret value Note: the secret should be recorded immediately when registration is completed. You won't be able to check the secret again after leaving the screen.

##### Create and enable an application user in Power Platform Admin Center

An application user is needed to be created in the Dataverse environment that you want to scan in Microsoft Purview. Follow the steps in [Create An Application User](/en-us/power-platform/admin/manage-application-users#create-an-application-user) to create the user with the application ID you recorded, and assign the security role **Service Reader** to it.

![Screenshot that shows how to create application user.](media/register-scan-dataverse/scan-dataverse-config-create-app-user.png)

You can check the application user in the Details page. Now the application user is bound with the Microsoft Entra application that was created earlier.

##### Create a credential in Microsoft Purview

Follow these steps to create a new credential.

1. Go to your key vault in the Azure portal. If you don’t have a key vault, refer to [Quickstart - Create an Azure Key Vault with the Azure portal](/en-us/azure/key-vault/general/quick-create-portal).
2. Select **Settings** &gt; **Secrets**, and then select + **Generate/Import**.

    ![Screenshot that shows the access control for the storage account.](media/register-scan-dataverse/scan-dataverse-kv-generate.png)
3. For **Name**, create a name for the secret.
4. For **Value**, input the secret value you recorded when you finished the app registration.
5. Select **Create**.

    If your key vault isn't connected to Microsoft Purview yet, [create a new key vault connection](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account). Identify your Azure Key Vault permission model from Access Policies settings in the Key Vault menu and follow steps below based on relevant permission model to assign access to the **Microsoft Purview system assigned managed identity (SAMI)**:

    ![Screenshot that shows assign access in Azure Key Vault.](media/register-scan-dataverse/scan-dataverse-kv-assign-access.png)

    [Option 1 - Assign access using Key Vault Access Policy](data-map-data-scan-credentials#option-1---assign-access-using-key-vault-access-policy)

    [Option 2 - Assign access using Key Vault Azure role-based access control](data-map-data-scan-credentials#option-2---assign-access-using-key-vault-azure-role-based-access-control)
6. Create a new credential by using the key to set up your scan.

    ![Screenshot that shows how to create a credential in Microsoft Purview.](media/register-scan-dataverse/scan-dataverse-create-credential.png)

    - Choose **Service Principal** as **Authentication method**.
    - Fill in the Directory (tenant) ID recorded before during app registration as **Tenant ID**.
    - Fill in Application (client) ID recorded before during app registration as **Service principal ID**.
    - Choose your key vault connection.
    - Fill in the name of the secret you created in your key vault as **Secret name**.

    ![Screenshot that shows a sample for creating a credential in Microsoft Purview.](media/register-scan-dataverse/scan-dataverse-create-credential-detail.png)
7. Select **Create**.

---

### Create the scan

1. Go to **Data Map** &gt; **Sources** to view the collection hierarchy.
2. Select the **New Scan** icon under the Dataverse source that you registered earlier.
3. For **Name**, provide a name for the scan.
4. For **Integration runtime**, see the [list of supported data sources for scans](data-map-integration-runtime-choose#supported-data-sources) to choose right integration runtime according to the scenario.
5. For **Credential**, select the credential you prepared earlier.

- If system-assigned managed identity is configured for authentication, then select **Microsoft Purview MSI (system)** from the drop-down list.
- If service principal is configured for authentication, then select the credential you created before from the drop-down list.

1. For **Select a collection**, choose the appropriate collection for the scan.
2. Select **Test connection** to validate the connection. After the connection is successful, select **Continue**.

    ![Screenshot that shows how to create a scan.](media/register-scan-dataverse/scan-dataverse-create-scan.png)

### Scope and run the scan

1. You can scope your scan to specific Dataverse tables by choosing the appropriate items in the list.

    ![Screenshot that shows how to scope your scan.](media/register-scan-dataverse/scan-dataverse-create-scan-scope.png)
2. Choose your scan trigger. You can set up a schedule or run the scan once.
3. Review your scan, and then select **Save and run**.

#### View and manage a scan

To check the status of a scan, go to the data source in the collection, and then select **View details**. The scan details indicate the progress of the scan in **Last run status**, along with the number of assets scanned and classified. **Last run status** is updated to **In progress** and then **Completed** after the entire scan runs successfully. After you run a scan, you can use the run history to manage it. In the run history, you have options for running the scan again, editing it, or deleting it.

## Browse, search, and view Dataverse assets

Once the scan is completed, you can go to Microsoft Purview Unified Catalog to browse or search the Dataverse related assets, and view related details.

![Screenshot that shows how to browse data assets by source types.](media/register-scan-dataverse/scan-dataverse-browse-by-source.png)

![Screenshot that shows data asset detail.](media/register-scan-dataverse/scan-dataverse-browse-asset-detail.png)