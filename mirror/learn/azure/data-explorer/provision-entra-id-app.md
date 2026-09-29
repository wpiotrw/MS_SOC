---
layout: Conceptual
title: Create a Microsoft Entra Application in Azure Data Explorer - Azure Data Explorer | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/data-explorer/provision-entra-id-app
breadcrumb_path: /azure/data-explorer/breadcrumb/toc.json
uhfHeaderId: azure
feedback_system: Standard
feedback_product_url: https://feedback.azure.com/d365community/forum/a952add5-eb24-ec11-b6e6-000d3a4f0da0
feedback_help_link_url: https://learn.microsoft.com/answers/topics/azure-data-explorer.html
feedback_help_link_type: get-help-at-qna
recommendations: true
author: spelluru
ms.author: spelluru
ms.service: azure-data-explorer
services: data-explorer
description: Learn how to create a Microsoft Entra application in Azure Data Explorer.
ms.topic: how-to
ms.date: 2026-02-12T00:00:00.0000000Z
locale: en-us
document_id: a737af4a-e2ef-072d-6763-5018fe1d2531
document_version_independent_id: 6dff791d-0eac-91fb-cd98-391c4923e936
original_content_git_url: https://github.com/MicrosoftDocs/dataexplorer-docs-pr/blob/live/data-explorer/provision-entra-id-app.md
site_name: Docs
depot_name: MSDN.dataexplorer-docs
page_type: conceptual
interactive_type: azurecli
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.dataexplorer-docs/{branchName}{pdfName}
asset_id: provision-entra-id-app
moniker_range_name: 
monikers: []
item_type: Content
source_path: data-explorer/provision-entra-id-app.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/26e1a60c-4ce1-41de-b2d1-e5f3b7e68e6e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad3bd485-5ca9-4865-afde-baec02586899
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: d5265097-ff98-5849-59b1-8efe859fdc89
---

# Create a Microsoft Entra Application in Azure Data Explorer - Azure Data Explorer | Microsoft Learn

Use [Microsoft Entra application authentication](/en-us/entra/identity-platform/howto-create-service-principal-portal) for applications, such as an unattended service or a scheduled flow, that need to access Azure Data Explorer without a user present. If you're connecting to an Azure Data Explorer database by using an application, such as a web app, authenticate by using service principal authentication. This article explains how to create and register a Microsoft Entra service principal and then authorize it to access an Azure Data Explorer database.

## Create Microsoft Entra application registration

Microsoft Entra application authentication requires creating and registering an application with Microsoft Entra ID. A service principal is automatically created when the application registration is created in a Microsoft Entra tenant.

The app registration can either be created in the Azure portal, or programatically with Azure CLI. Choose the tab that fits your scenario.

# [Portal](#tab/portal)
#### Register the app

1. Sign in to [Azure portal](https://portal.azure.com) and open **Microsoft Entra ID**.
2. In the left navigation pane, go to **Manage**. Select **App registrations** and then **New registration**.

    [![Screenshot showing how to start a new app registration.](includes/media/provision-entra-id-app/app-registrations.png)](includes/media/provision-entra-id-app/app-registrations.png#lightbox)
3. Enter a name for the application, such as "example-app".
4. Select a supported account type, which determines who can use the application.
5. Under **Redirect URI**, select **Web** for the type of application you want to create. The URI is optional and is left blank in this case.

    [![Screenshot showing how to register a new app registration.](includes/media/provision-entra-id-app/create-app-register-app.png)](includes/media/provision-entra-id-app/create-app-register-app.png#lightbox)
6. Select **Register**.

#### Set up authentication

Two types of authentication are available for service principals: password-based authentication (application secret) and certificate-based authentication. The following section describes using password-based authentication for the application's credentials. You can alternatively use an X509 certificate to authenticate your application. For more information, see [How to configure Microsoft Entra certificate-based authentication](/en-us/entra/identity/authentication/how-to-certificate-based-authentication).

In this section, you copy the following values: **Application ID** and **key value**. Paste these values somewhere, like a text editor, for use in the step configure client credentials to the database.

1. Browse to the **Overview** section.
2. Copy the **Application (client) ID** and the **Directory (tenant) ID**.

    Note

    You need the application ID and the tenant ID to authorize the service principal to access the database.
3. In the left navigation pane, go to **Manage**. Select **Certificates & secrets** and **New client secret**.

    [![Screenshot showing how to start the creation of client secret.](includes/media/provision-entra-id-app/new-client-secret.png)](includes/media/provision-entra-id-app/new-client-secret.png#lightbox)
4. Enter a description and expiration.
5. Select **Add**.
6. Copy the key value.

    Note

    When you leave this page, you can't access the key value.

You created your Microsoft Entra application and service principal.

# [Azure CLI](#tab/azurecli)
1. Sign in to your Azure subscription via Azure CLI. Then authenticate in the browser.

    ```azurecli
    az login
    ```
2. Choose the subscription to host the principal. This step is needed when you have multiple subscriptions.

    ```azurecli
    az account set --subscription YOUR_SUBSCRIPTION_GUID
    ```
3. Create the service principal. In this example, the service principal is called `my-service-principal`.

    ```azurecli
    az ad sp create-for-rbac -n "my-service-principal" --role Contributor --scopes /subscriptions/{SubID}
    ```
4. From the returned JSON data, copy the `appId`, `password`, and `tenant` for future use.

    ```json
    {
      "appId": "00001111-aaaa-2222-bbbb-3333cccc4444",
      "displayName": "my-service-principal",
      "name": "my-service-principal",
      "password": "00001111-aaaa-2222-bbbb-3333cccc4444",
      "tenant": "00001111-aaaa-2222-bbbb-3333cccc4444"
    }
    ```

You've created your Microsoft Entra application and service principal.

---

## Configure delegated permissions for the application - optional

If your application needs to access your database by using the credentials of the calling user, configure delegated permissions for your application. For example, if you're building a web API and you want to authenticate by using the credentials of the user who is *calling* your API.

If you only need access to an authorized data resource, you can skip this section and continue to Grant a service principal access to the database.

1. Browse to the **API permissions** section of your **App registration**.
2. Select **Add a permission**.
3. Select **APIs my organization uses**.
4. Search for and select **Azure Data Explorer**.

    [![Screenshot showing how to add Azure Data Explorer API permission.](includes/media/provision-entra-id-app/configure-delegated-add-api-permission.png)](includes/media/provision-entra-id-app/configure-delegated-add-api-permission.png#lightbox)
5. In **Delegated permissions**, select the **user\_impersonation** box.
6. Select **Add permissions**.

    [![Screenshot showing how to select delegated permissions with user impersonation.](includes/media/provision-entra-id-app/configure-delegated-click-add-permissions.png)](includes/media/provision-entra-id-app/configure-delegated-click-add-permissions.png#lightbox)

## Grant a service principal access to the database

After creating your application registration, grant the corresponding service principal access to your database. The following example grants viewer access. For other roles, see [Manage database permissions](/en-us/azure/data-explorer/manage-database-permissions).

1. Use the values of Application ID and Tenant ID as copied in a previous step.
2. Execute the following command in your query editor, replacing the placeholder values *ApplicationID* and *TenantID* with your actual values:

    ```kusto
    .add database <DatabaseName> viewers ('aadapp=<ApplicationID>;<TenantID>') '<Notes>'
    ```

    For example:

    ```kusto
    .add database Logs viewers ('aadapp=1234abcd-e5f6-g7h8-i9j0-1234kl5678mn;9876abcd-e5f6-g7h8-i9j0-1234kl5678mn') 'App Registration'
    ```

    The last parameter is a string that shows up as notes when you query the roles associated with a database.

    Note

    After creating the application registration, you might need to wait several minutes until it can be referenced. If you receive an error that the application isn't found, wait and try again.

For more information on roles, see [Role-based access control](/en-us/azure/data-explorer/kusto/access-control/role-based-access-control).

## Use application credentials to access a database

Use the application credentials to programmatically access your database by using the [client library](/en-us/azure/data-explorer/kusto/api/netfx/about-kusto-data).

```C
. . .
string applicationClientId = "<myClientID>";
string applicationKey = "<myApplicationKey>";
string authority = "<myApplicationTenantID>";
. . .
var kcsb = new KustoConnectionStringBuilder($"https://{clusterName}.kusto.windows.net/{databaseName}")
    .WithAadApplicationKeyAuthentication(
        applicationClientId,
        applicationKey,
        authority);
var client = KustoClientFactory.CreateCslQueryProvider(kcsb);
var queryResult = client.ExecuteQuery($"{query}");
```

Note

Specify the application ID and key of the application registration (service principal) that you created earlier.

For more information, see [How to authenticate with Microsoft Authentication Library (MSAL) in apps](/en-us/azure/data-explorer/kusto/api/rest/authenticate-with-msal) and [use Azure Key Vault with .NET Core web app](/en-us/azure/key-vault/tutorial-net-create-vault-azure-web-app#create-a-net-core-web-app).

## Troubleshooting

### Invalid resource error

If your application authenticates users or applications for access, set up delegated permissions for the service application. Declare that your application can authenticate users or applications for access. If you don't, an error occurs when you attempt authentication. The error message is similar to the following message:

`AADSTS650057: Invalid resource. The client has requested access to a resource which is not listed in the requested permissions in the client's application registration...`

Follow the instructions in configure delegated permissions for the application.

### Enable user consent error

Your Microsoft Entra tenant administrator might enact a policy that prevents tenant users from giving consent to applications. This situation results in an error similar to the following error when a user tries to sign in to your application:

`AADSTS65001: The user or administrator has not consented to use the application with ID '<App ID>' named 'App Name'`

Contact your Microsoft Entra administrator to grant consent for all users in the tenant, or enable user consent for your specific application.