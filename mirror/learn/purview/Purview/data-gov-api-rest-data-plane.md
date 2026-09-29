---
layout: Conceptual
title: API authentication for Microsoft Purview data planes | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-api-rest-data-plane
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2024-04-30T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to authenticate APIs to access the contents of your Microsoft Purview.
ms.custom: sfi-image-nochange
locale: en-us
document_id: 07dfe94b-c677-de6d-7839-d34aec00e2fa
document_version_independent_id: 07dfe94b-c677-de6d-7839-d34aec00e2fa
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-api-rest-data-plane.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-api-rest-data-plane
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-api-rest-data-plane.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: cf119bf6-4295-6cf4-7988-acd08c461daf
---

# API authentication for Microsoft Purview data planes | Microsoft Learn

In this tutorial, you learn how to authenticate for the [Microsoft Purview data plane APIs](/en-us/rest/api/purview/). Anyone who wants to submit data to Microsoft Purview, include Microsoft Purview as part of an automated process, or build their own user experience on Microsoft Purview can use the APIs to do so.

## Prerequisites

- To get started, you must have an existing Microsoft Purview account. If you don't have a catalog, see the [quickstart for creating a Microsoft Purview account](create-microsoft-purview-portal).

## Create a service principal (application)

For an API client to access the Microsoft Purview data plane APIs, the client must have a service principal (application), and an identity that Microsoft Purview recognizes and is configured to trust. When you make API calls, that service principal's identity will be used for authorization.

Customers who have used existing service principals (application IDs) have had a high rate of failure. Therefore, we recommend creating a new service principal for calling APIs.

To create a new service principal:

1. Sign in to the [Azure portal](https://portal.azure.com).
2. From the portal, search for and select **Microsoft Entra ID**.
3. From the **Microsoft Entra ID** page, select **App registrations** from the left pane.
4. Select **New registration**.
5. On the **Register an application** page:

    1. Enter a **Name** for the application (the service principal name).
    2. For *Who can use this application or access this API?*, select the kinds of user accounts you expect to use this API. 
        Tip

        If you expect only users from your current Microsoft Entra ID tenant to use the REST API, select, **Accounts in this organizational directory only (*&lt;your tenant's name&gt;* only - Single tenant)**. Otherwise, consider the other options.
    3. For **Redirect URI (optional)**, select **Web** and enter a value. This value doesn't need to be a valid endpoint. `https://exampleURI.com` will do.
    4. Select **Register**.

    ![Screenshot of the application registration page, with the above options filled out.](media/tutorial-using-rest-apis/application-registration.png)
6. On the new service principal page, copy the values of the **Display name** and the **Application (client) ID** to save for later.

    The application ID is the `client_id` value in the sample code.

    ![Screenshot of the application page in the portal with the Application (client) ID highlighted.](media/tutorial-using-rest-apis/application-id.png)

To use the service principal (application), you need to know the service principal's password that can be found by:

1. From the Azure portal, search for and select **Microsoft Entra ID**, and then select **App registrations** from the left pane.
2. Select your service principal (application) from the list.
3. Select **Certificates & secrets** from the left pane.
4. Select **New client secret**.
5. On the **Add a client secret** page, enter a **Description**, select an expiration time under **Expires**, and then select **Add**.

    On the **Client secrets** page, the string in the **Value** column of your new secret is your password. Save this value.

    ![Screenshot showing a client secret.](media/tutorial-using-rest-apis/client-secret.png)

## Set up authentication using service principal

Once the new service principal is created, you need to assign the data plane roles of your purview account to the service principal created above. Follow the steps below to assign the correct role to establish trust between the service principal and the Purview account:

# [Data Map](#tab/datamap)
1. Navigate to your [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Select the Data Map in the left menu.
3. Select Collections.
4. Select the root collection in the collections menu. This will be the top collection in the list, and will have the same name as your Microsoft Purview account.

    Note

    You can also assign your service principal permission to any sub-collections, instead of the root collection. However, all APIs will be scoped to that collection (and sub-collections that inherit permissions), and users trying to call the API for another collection will get errors.
5. Select the **Role assignments** tab.
6. Assign the following roles to the service principal created previously to access various data planes in Microsoft Purview. For detailed steps, see [Assign Azure roles using the Microsoft Purview governance portal](data-map-collections-manage-classic#add-role-assignments).

- Data Curator role to access Catalog Data plane.
- Data Source Administrator role to access Scanning Data plane.
- Collection Admin role to access Account Data Plane and Metadata policy Data Plane.
- Policy Author role to access the DevOps policies API

    Note

    Only members of the Collection Admin role can assign data plane roles in Microsoft Purview. For more information about Microsoft Purview roles, see [Access Control in Microsoft Purview](data-gov-classic-permissions).

# [Unified Catalog](#tab/unifiedcatalog)
1. Navigate to your [Microsoft Purview governance portal](https://web.purview.azure.com/resource/).
2. Select **Unified Catalog** in the left menu.
3. Select **Catalog Management** &gt; **Governance domains**.
4. In **Filter by keyword** enter the name of your domain, and then select the domain from the search results.
5. Select the **Roles** tab.
6. Assign the following roles to the service principal created previously to access various data planes in Microsoft Purview. For detailed steps, see [Assign Azure roles using the Microsoft Purview governance portal](data-map-collections-manage-classic#add-role-assignments).

- Data Catalog Reader to access OKRs, Business Domains, Critical Data Elements, Data Product, Terms.
- Data Steward to access OKRs, Business Domains, Critical Data Elements, Data Product, Terms, Policy.
- Data Product Owner to access OKRs, Business Domains, Critical Data Elements, Data Product, Terms, Policy.
- Governance domain creator to access Business Domains.
- Governance domain owner to access Business Domains, Policy.

---

## Get token

You can send a POST request to the following URL to get access token.

`https://login.microsoftonline.com/{your-tenant-id}/oauth2/token`

You can find your Tenant ID by searching for **Tenant Properties** in the Azure portal. The ID will be available on the tenant properties page.

The following parameters need to be passed to the above URL:

- **client\_id**: client ID of the application registered in Microsoft Entra ID and is assigned to a data plane role for the Microsoft Purview account.
- **client\_secret**: client secret created for the above application.
- **grant\_type**: This should be ‘client\_credentials’.
- **resource**: ‘https://purview.azure.net’

Here's a sample POST request in PowerShell:

```azurepowershell
$tenantID = "12a345bc-67d1-ef89-abcd-efg12345abcde"

$url = "https://login.microsoftonline.com/$tenantID/oauth2/token"
$params = @{ client_id = "00001111-aaaa-2222-bbbb-3333cccc4444"; client_secret = "abcd~a1234bcd56789012abcdabcd1234abcd"; grant_type = "client_credentials"; resource = ‘https://purview.azure.net’ }

Invoke-WebRequest $url -Method Post -Body $params -UseBasicParsing | ConvertFrom-Json
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

Use the access token above to call the Data plane APIs.