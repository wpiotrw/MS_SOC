---
layout: Conceptual
title: Deploy a connector to archive Twitter data | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/archive-twitter-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Administrators can set up a native connector to import and archive Twitter data to Microsoft 365. After this data is imported to Microsoft 365, you can use compliance features such as legal hold, eDiscovery, and retention policies to manage the governance of your organization's Twitter data.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-19T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-connectors
search.appverid:
- MET150
ms.collection:
- purview-compliance
- data-connectors
ms.custom: msecd-doc-authoring-1014, admindeeplinkCOMPLIANCE, sfi-ga-nochange, sfi-image-nochange
ROBOTS: NOINDEX, NOFOLLOW
ai-usage: ai-assisted
locale: en-us
document_id: f2c11c75-4531-45b5-f864-53face3a4699
document_version_independent_id: f2c11c75-4531-45b5-f864-53face3a4699
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/archive-twitter-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: archive-twitter-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/archive-twitter-data.md
platformId: 0b073907-081d-0732-2c36-c15214a47dcc
---

# Deploy a connector to archive Twitter data | Microsoft Learn

This article describes the process to deploy a connector that uses the Microsoft 365 Import service to import data from your organization's Twitter account to Microsoft 365. For a high-level overview of this process and a list of prerequisites required to deploy a Twitter connector, see [Set up a connector to archive Twitter data](archive-twitter-data-with-sample-connector).

## Step 1: Create an app in Microsoft Entra ID

1. Go to https://portal.azure.com and sign in with the credentials of a global admin account.

    Important

    Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

    ![Screenshot of the Azure portal sign-in page for global admin credentials.](media/tcimage01.png)
2. In the left navigation, select **Microsoft Entra ID**.

    ![Screenshot of the left navigation pane with Microsoft Entra ID selected in the Azure portal.](media/tcimage02.png)
3. In the left navigation, select **App registrations (Preview)**, then select **New registration**.

    ![Screenshot of the Microsoft Entra ID App registrations page with the New registration option.](media/tcimage03.png)
4. Register the application. Under **Redirect URI (optional)**, select **Web** in the application type dropdown list, then type `https://portal.azure.com` in the box for the URI.

    ![Screenshot of the app registration settings showing the redirect URI configured to the Azure portal.](media/tcimage04.png)
5. Copy the **Application (client) ID** and **Directory (tenant) ID** and save them to a text file or other safe location. You use these IDs in later steps.

    ![Screenshot of the app overview page showing the Application (client) ID and Directory (tenant) ID.](media/tcimage05.png)
6. Go to **Certificates & secrets for the new app** and under **Client secrets**, select **New client secret**.

    ![Screenshot of the Certificates &amp; secrets page with the option to create a new client secret.](media/tcimage06.png)
7. Create a new secret. In the description box, type the secret and then select an expiration period.

    ![Screenshot of the client secret form with the description field and expiration period options.](media/tcimage08.png)
8. Copy the value of the secret and save it to a text file or other storage location. This is the Microsoft Entra application secret that you use in later steps.

    ![Screenshot of the client secret value displayed for copying and saving.](media/tcimage09.png)

## Step 2: Deploy the connector web service from GitHub to your Azure account

1. Go to [this GitHub site](https://github.com/microsoft/m365-sample-twitter-connector-csharp-aspnet) and select **Deploy to Azure**.

    ![Screenshot of the GitHub repository page with the Deploy to Azure button highlighted.](media/fbcimage11.png)
2. After you select **Deploy to Azure**, you're redirected to an Azure portal with a custom template page. Fill in the **Basics** and **Settings** details, then select **Purchase**.

    ![Screenshot of the Azure portal custom template page with Basics and Settings fields for the connector deployment.](media/facebook-connector-custom-template-settings.png)

    - **Subscription:** Select your Azure subscription that you want to deploy the Twitter connector web service to.
    - **Resource group:** Select or create a new resource group. A resource group is a container that holds related resources for an Azure solution.
    - **Location:** Select a location.
    - **Web App Name:** Provide a unique name for the connector web app. The name must be between 3 and 18 characters in length. This name is used to create the Azure app service URL; for example, if you provide the Web app name of **twitterconnector** then the Azure app service URL is **twitterconnector.azurewebsites.net**.
    - **tenantId:** The tenant ID of your Microsoft 365 organization that you copied after creating the Twitter connector app in Microsoft Entra ID in Step 1.
    - **APISecretKey:** You can type any value as the secret. This value is used to access the connector web app in Step 5.
3. When the deployment succeeds, the page looks similar to the following screenshot:

    ![Screenshot of the Azure portal showing a successful connector web service deployment.](media/facebook-connector-deployment-successful.png)

## Step 3: Create the Twitter app

1. Go to https://developer.twitter.com, sign in with the credentials for the developer account for your organization, and select **Apps**.

    ![Screenshot of the Twitter developer portal home page with the Apps option.](media/tcimage25-5.png)
2. Select **Create an app**.

    ![Screenshot of the Twitter developer portal Apps page with the option to create a new app.](media/tcimage26.png)
3. Under **App details**, enter information about the application.

    ![Screenshot of the Twitter App details form for entering application information.](media/tcimage27.png)
4. On the Twitter developer dashboard, select the app that you just created, then select **Details**.

    ![Screenshot of the Twitter developer dashboard showing the app details and App ID.](media/tcimage28.png)
5. On the **Keys and tokens** tab, under **Consumer API keys**, copy both the API Key and the API secret key and save them to a text file or other storage location. Then select **Create** to generate an access token and an access token secret and copy these to a text file or other storage location.

    ![Screenshot of the Twitter developer app Keys and tokens page showing the API secret key.](media/tcimage29.png)

    Select **Create** to generate an access token and an access token secret, and copy these to a text file or other storage location.
6. Select the **Permissions** tab and configure the permissions as shown in the following screenshot:

    ![Screenshot of the Twitter app Permissions tab with the required permissions configured.](media/tcimage30.png)
7. After you save the permission settings, select the **App details** tab, then select **Edit &gt; Edit details**.

    ![Screenshot of the Twitter app details page with the Edit details option selected.](media/tcimage31.png)
8. Complete the following tasks:

    - Select the checkbox to allow the connector app to sign in to Twitter.
    - Add the OAuth redirect Uri using the following format: **&lt;connectorserviceuri&gt;/Views/TwitterOAuth**, where the value of *connectorserviceuri* is the Azure app service URL for your organization.

    ![Screenshot of Twitter app settings showing sign-in permission enabled and OAuth redirect URI configured.](media/tcimage32.png)

The Twitter developer app is now ready to use.

## Step 4: Configure the connector web app

1. Go to `https://<AzureAppResourceName>.azurewebsites.net` (where **AzureAppResourceName** is the name of your Azure app resource that you named in Step 2). The home page of the app looks like the following screenshot:

    ![Screenshot of the Azure-hosted connector web app home page.](media/facebook-connector-web-app-home.png)
2. Select **Configure** to display a sign in page.

    ![Screenshot of the connector web app sign-in page opened from the Configure option.](media/facebook-connector-configure-sign-in.png)
3. In the Tenant Id box, type or paste your Microsoft Entra tenant ID (the Directory (tenant) ID from the Microsoft Entra app registration). In the password box, type or paste the APISecretKey value from the Azure deployment template settings, then select **Set Configuration Settings** to display the configuration details page.

    ![Screenshot of the sign-in page with Tenant ID and API secret key fields.](media/tcimage35.png)
4. Enter the following configuration settings:

    - **Twitter Api Key:** The API key for the Twitter application that you created in Step 3.
    - **Twitter Api Secret Key:** The API secret key for the Twitter application that you created in Step 3.
    - **Twitter Access Token:** The access token that you created in Step 3.
    - **Twitter Access Token Secret:** The access token secret that you created in Step 3.
    - **Microsoft Entra Application ID:** The application ID for the Microsoft Entra app that you created in Step 1
    - **Microsoft Entra Application Secret:** The value of the Microsoft Entra application client secret that you created during the app registration in Microsoft Entra ID.
5. Select **Save** to save the connector settings.

## Step 5: Set up a Twitter connector

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select **Settings** &gt; **Data connectors**.
3. Select **My connectors**, then select **Add connector**.
4. From the list, select **Twitter**.
5. On the **Terms of service** page, select **Accept**.
6. On the **Add credentials for your connector app** page, enter the following information and then select **Validate connection**.

    - In the **Name** box, type a name for the connector, such as **Twitter help handle**.
    - In the **Connector URL** box, type or paste the Azure app service URL.
    - In the **Password** box, type or paste the APISecretKey value from the Azure deployment template settings.
    - In the **Azure App ID** box, type or paste the value of the Azure Application App Id (also called the *client ID*) that you obtained in Step 1.
7. After the connection is successfully validated, select **Next**.
8. On the **Authorize Microsoft 365 to import data** page, type or paste the APISecretKey again and then select **Login web app**.
9. Select **Login with Twitter**.
10. On the Twitter sign in page, sign in by using the credentials for your organization's Twitter account. After you sign in, the Twitter page displays the following message, "Twitter Connector Job Successfully set up."
11. Select **Continue** to complete setting up the Twitter connector.
12. On the **Set filters** page, you can apply a filter to initially import items that are a certain age. Select an age, and then select **Next**.
13. On the **Choose storage location** page, type the email address of Microsoft 365 mailbox that the Twitter items are imported to, and then select **Next**.
14. Select **Next** to review the connector settings and then select **Finish** to complete the connector setup.