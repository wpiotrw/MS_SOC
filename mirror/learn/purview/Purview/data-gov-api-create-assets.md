---
layout: Conceptual
title: Create assets using the REST API | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-api-create-assets
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2025-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: This article describes how to create assets in the Microsoft Purview Data Map using the REST API.
locale: en-us
document_id: cc9a73e1-27f2-4123-a564-9a0af660fed6
document_version_independent_id: cc9a73e1-27f2-4123-a564-9a0af660fed6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-api-create-assets.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-api-create-assets
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-api-create-assets.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: d4669d96-68c7-14f4-1cd8-dddbb32dc87d
---

# Create assets using the REST API | Microsoft Learn

In this tutorial, you'll learn how to create assets in Microsoft Purview Data Map that users are able to search and browse in Microsoft Purview Unified Catalog.

Note

If you're using [the free version of Microsoft Purview](data-governance-free-version), only users in the [data curator role group](data-governance-roles-permissions#tenant-level-role-groups) will be able to access these assets.

If you already have your service principal and authentication token, you can skip directly to the steps to create assets using the REST API. Otherwise, follow this guide to call the REST API.

## Prerequisites

- If you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.
- You must have an existing Microsoft Purview account. If you don't, [check if your organization has access to the free version of Microsoft Purview](data-governance-free-version#access-the-free-version-of-microsoft-purview-governance-solutions), or use this [quickstart to create a Microsoft Purview account](create-microsoft-purview-portal).

## Create a service principal (application)

For a REST API client to access Microsoft Purview to create entities, the client must have a service principal (application), and an identity that Microsoft Purview recognizes and is configured to trust.

Customers who have used existing service principals (application IDs) have had a high rate of failure. Therefore, we recommend creating a new service principal for calling APIs.

To create a new service principal:

1. Sign in to the [Azure portal](https://portal.azure.com).
2. From the portal, search for and select **Microsoft Entra ID**.
3. From the **Microsoft Entra ID** page, select **App registrations** from the left pane.
4. Select **New registration**.
5. On the **Register an application** page:

    1. Enter a **Name** for the application (the service principal name).
    2. Select **Accounts in this organizational directory only (*&lt;your tenant's name&gt;* only - Single tenant)**.
    3. For **Redirect URI (optional)**, select **Web** and enter a value. This value doesn't need to be a valid endpoint. `https://exampleURI.com` will do.
    4. Select **Register**.
6. On the new service principal page, copy the values of the **Display name** and the **Application (client) ID** to save for later.

    The application ID is the `client_id` value in the sample code.

To use the service principal (application), you need to know the service principal's password:

1. Select your service principal (application) in the **App registrations** list.
2. Select **Certificates & secrets** from the left pane.
3. Select **New client secret**.
4. On the **Add a client secret** page, enter a **Description**, select an expiration time under **Expires**, and then select **Add**.
5. On the **Client secrets** page, the string in the **Value** column of your new secret is your password. Save this value.

## Set up authentication using service principal

Once the new service principal is created, you need to assign permissions so your service principal can access your Microsoft Purview account. The permissions you need to assign depend on whether you're using the [classic Microsoft Purview experience](use-microsoft-purview-governance-portal) or the [new Microsoft Purview portal](purview-portal).

Select the tab for the experience you're using.

# [Classic governance portal](#tab/classic-portal)
1. Navigate to your [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Select the Data Map in the left menu.
3. Select Collections.
4. Select the root collection in the collections menu. This is the top collection in the list, and will have the same name as your Microsoft Purview account.

    Note

    You can also assign your service principal permission to any sub-collections, instead of the root collection. However, all APIs will be scoped to that collection (and sub-collections that inherit permissions), and users trying to call the API for another collection will get errors.
5. Select the **Role assignments** tab.
6. Assign the Data Curator role to the service principal created previously. For detailed steps, see [Assign Azure roles using the Microsoft Purview governance portal](data-map-collections-manage-classic#add-role-assignments).

# [New Microsoft Purview portal](#tab/new-portal)
1. Add your service principal to a group so it can be assigned a role group in Microsoft Purview.
2. Add your service principal to the [data curator role group](data-governance-roles-permissions#tenant-level-role-groups) to have access to add entities. To add your service principal to the role group, [follow these instructions on the permissions page](purview-permissions#add-users-or-groups-to-a-microsoft-purview-built-in-role-group).

---

After you've assigned permissions, you'll need to gather your authentication token.

1. Send a POST request to the following URL to get access token:

    `https://login.microsoftonline.com/{your-tenant-id}/oauth2/token`

    You can find your Tenant ID by searching for **Tenant Properties** in the Azure portal. The ID is available on the tenant properties page.

    The following parameters need to be passed to the above URL:

    - **client\_id**: client ID of the application registered in Microsoft Entra ID and is assigned to a data plane role for the Microsoft Purview account.
    - **client\_secret**: client secret created for the above application.
    - **grant\_type**: This should be ‘client\_credentials’.
    - **resource**: This should be ‘https://purview.azure.net’

    Here's a sample POST request in PowerShell:

    ```azurepowershell
    $tenantID = "12a345bc-67d1-ef89-abcd-efg12345abcde"
    
    $url = "https://login.microsoftonline.com/$tenantID/oauth2/token"
    $params = @{ client_id = "00001111-aaaa-2222-bbbb-3333cccc4444"; client_secret = "abcd~a1234bcd56789012abcdabcd1234abcd"; grant_type = "client_credentials"; resource = ‘https://purview.azure.net’ }
    
    Invoke-WebRequest $url -Method Post -Body $params      -UseBasicParsing | ConvertFrom-Json
    ```

    Sample response token:

    ```json
    {
        "token_type": "Bearer",
        "expires_in": "86399",
        "ext_expires_in": "86399",
        "expires_on": "1621038348",
        "not_before": "1620951648",
        "resource": "https://purview.azure.net",
        "access_token": "<<access token>>"
    }
    ```

    Tip

    If you get an error message that reads: *Cross-origin token redemption is permitted only for the 'Single-Page Application' client-type.*

    - Check your request headers and confirm that your request **doesn't** contain the 'origin' header.
    - Confirm that your redirect URI is set to **web** in your service principal.
    - Make sure your software is up to date for the application you're using to send your POST request.
2. Use the access token above to call the Data plane APIs.

## Create assets using the REST API

Now that you have a token and can authenticate, you're ready to create your assets.

Important

Your request URL endpoints depend on what Microsoft Purview experience you're using: the [classic Microsoft Purview experience](use-microsoft-purview-governance-portal) or the [new Microsoft Purview portal](purview-portal)

### Create Azure assets

Here's an example you can use to create your entities for Azure resources. This example covers an Azure Storage account, but you can use it for any other Azure sources.

Important

To use this example for your Azure resources, replace these values in the payload:

- typeName
- Owner
- qualifiedName
- name
- Expert ID
- Expert Info
- Owner ID
- Owner Info
- Createdby
- Updatedby

# [Classic governance portal](#tab/classic-portal)
Request URL: `https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity`

# [New Microsoft Purview portal](#tab/new-portal)
Request URL: `https://api.purview-service.microsoft.com/catalog/api/atlas/v2/entity`

---

Method: POST

Authentication: Use the token from the previous step as your bearer token.

Payload example:

```json
{
  "referredEntities": {},
  "entity": {
    "typeName": "azure_storage_account",
    "attributes": {
      "owner": "ExampleOwner",
      "modifiedTime": 0,
      "createTime": 0,
      "qualifiedName": "https://exampleaccount.core.windows.net",
      "name": "ExampleStorageAccount",
      "description": null,
      "publicAccessLevel": null
    },
    "contacts": {
      "Expert": [
        {
          "id": "30435ff9-9b96-44af-a5a9-e05c8b1ae2d2",
          "info": "Example Expert Info"
        }
      ],
      "Owner": [
        {
          "id": " 30435ff9-9b96-44af-a5a9-e05c8b1ae2d2",
          "info": "Example Owner Info"
        }
      ]
    },
    "status": "ACTIVE",
    "createdBy": "ExampleCreator",
    "updatedBy": "ExampleUpdator",
    "version": 0
  }
}

```

### Create multicloud assets

Here's an example you can use to create your entities for multicloud resources. This example creates a Snowflake resource, but you can use it for any other sources

Important

To use this example for your Azure resources, replace these values in the payload:

- typeName
- Owner
- qualifiedName
- name
- type
- Expert ID
- Expert Info
- Owner ID
- Owner Info
- Createdby
- Updatedby

# [Classic governance portal](#tab/classic-portal)
Request URL: `https://{accountName}.purview.azure.com/catalog/api/atlas/v2/entity`

# [New Microsoft Purview portal](#tab/new-portal)
Request URL: `https://api.purview-service.microsoft.com/catalog/api/atlas/v2/entity`

---

Method: POST

Authentication: Use the token from the previous step as your bearer token.

Payload example:

```json
{
  "referredEntities": {},
  "entity": {
    "typeName": "snowflake_table",
    "attributes": {
      "owner": "ExampleOwner",
      "modifiedTime": 0,
      "createTime": 0,
      "qualifiedName": "snowflake://microsoft_partner.east-us-2.azure.snowflakecomputing.com/databases/AZUREPURVIEW_TESTDB/schemas/COMPANY/tables/PROJECT_INFO",
      "name": "PROJECT_INFO",
      "description": null,
      "type": "TABLE"
    },
    "contacts": {
      "Expert": [
        {
          "id": "30435ff9-9b96-44af-a5a9-e05c8b1ae2d2",
          "info": "Example Expert Info"
        }
      ],
      "Owner": [
        {
          "id": "4b27e65f-6a15-4925-a4ef-2e640445079b",
          "info": "Example Owner Info"
        }
      ]
    },
    "status": "ACTIVE",
    "createdBy": "ExampleCreator",
    "updatedBy": "ExampleUpdator",
    "version": 0
  }
}

```