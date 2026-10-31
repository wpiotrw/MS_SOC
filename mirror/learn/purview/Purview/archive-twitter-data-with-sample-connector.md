---
layout: Conceptual
title: Set up a connector to archive Twitter data | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/archive-twitter-data-with-sample-connector
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how administrators can set up and use a native connector to import Twitter data into Microsoft 365.
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
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 5a8dd522-10b5-d60c-5f24-bdb6e91ec44d
document_version_independent_id: 5a8dd522-10b5-d60c-5f24-bdb6e91ec44d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/archive-twitter-data-with-sample-connector.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: archive-twitter-data-with-sample-connector
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/archive-twitter-data-with-sample-connector.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 460903cc-aa52-64b8-9aaa-5b8234ae02b9
---

# Set up a connector to archive Twitter data | Microsoft Learn

Use a connector to import and archive data from Twitter to Microsoft 365. After you set up and configure the connector, it connects to your organization's Twitter account (on a scheduled basis), converts the content of an item to an email message format, and then imports those items to a mailbox in Microsoft 365. Before you begin, make sure you have a Twitter account for your organization, a valid Azure subscription, and the Data Connector Admin role in the Microsoft Purview portal.

After Twitter data is imported, you can apply Microsoft Purview features such as Litigation Hold, eDiscovery, In-Place Archiving, Auditing, Communication Compliance, and Microsoft 365 retention policies to the data stored in the mailbox. For example, you can search Twitter data using eDiscovery or associate the mailbox where the data is stored with a custodian in an eDiscovery case. Using a connector to import and archive Twitter data in Microsoft 365 can help your organization stay compliant with government and regulatory policies.

## Before you begin

Complete the following prerequisites before you set up and configure a connector in the [Microsoft Purview portal](purview-portal) to import and archive data from your organization's Twitter account.

- You need a Twitter account for your organization. You need to sign in to this account when setting up the connector.
- Your organization must have a valid Azure subscription. If you don't have an existing Azure subscription, you can sign up for one of these options:

    - [Sign up for a free one year Azure subscription](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn)
    - [Sign up for a Pay-As-You-Go Azure subscription](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go/)
- The Twitter connector can import a total of 200,000 items in a single day. If there are more than 200,000 Twitter items in a day, none of those items are imported to Microsoft 365.
- The user who sets up the Twitter connector in the Microsoft Purview portal (in Step 5) must be assigned the Data Connector Admin role. This role is required to add connectors on the **Data connectors** page in the Microsoft Purview portal. Multiple role groups include this role by default. For a list of these role groups, see [Roles in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance). Alternatively, an admin in your organization can create a custom role group, assign the Data Connector Admin role, and then add the appropriate users as members. For instructions, see [Permissions in the Microsoft Purview portal](purview-permissions) and [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions).

## Step 1: Create an app in Microsoft Entra ID

First, register a new app in Microsoft Entra ID. This app corresponds to the web app resource that you implement in Step 2 for the Twitter connector.

For more information, see [Create an app in Microsoft Entra ID](archive-twitter-data#step-1-create-an-app-in-microsoft-entra-id).

When you complete this step, save the following information to a text file. You'll use these values in later steps in the deployment process.

- Microsoft Entra application ID
- Microsoft Entra application secret
- Tenant Id

## Step 2: Deploy connector web service from GitHub repository to your Azure account

Next, deploy the source code for the Twitter connector app that uses the Twitter API to connect to your Twitter account and extract data so you can import it to Microsoft 365. The Twitter connector that you deploy for your organization uploads the items from your organization's Twitter account to the Azure Storage location that you create in this step. After you create a Twitter connector in the Microsoft Purview portal (in Step 5), the Microsoft 365 Import service copies the Twitter data from the Azure Storage location to a mailbox in Microsoft 365. You must have a valid Azure subscription to create an Azure Storage account.

To deploy the source code for the Twitter connector app:

1. Go to the [Microsoft 365 sample Twitter connector repository on GitHub](https://github.com/microsoft/m365-sample-twitter-connector-csharp-aspnet).
2. Select **Deploy to Azure**.

For more information, see [Deploy the connector web service from GitHub to your Azure account](archive-twitter-data#step-2-deploy-the-connector-web-service-from-github-to-your-azure-account).

When you complete this step, provide the following information:

- APISecretKey: Create this secret during the completion of this step. You use it in Step 5.
- tenantId: The tenant ID of your Microsoft 365 organization that you copied after creating the Twitter app in Microsoft Entra ID in Step 1.

After you complete this step, be sure to copy the app Service URL (for example, `https://twitterconnector.azurewebsites.net`). You need to use this URL to complete Step 3, Step 4, and Step 5.

## Step 3: Create developer app on Twitter

Create and configure a developer app on Twitter. The custom connector you create in Step 7 uses the Twitter app to interact with the Twitter API and obtain data from your organization's Twitter account.

For step-by-step instructions, see [Create the Twitter app](archive-twitter-data#step-3-create-the-twitter-app).

When you complete this step, save the following information to a text file. You'll use these values to configure the Twitter connector app in Step 4.

- Twitter API Key
- Twitter API Secret Key
- Twitter Access Token
- Twitter Access Token Secret

## Step 4: Configure the Twitter connector app

Add configuration settings to the Twitter connector app that you deployed in Step 2. Go to the home page of your connector app and configure it.

For step-by-step instructions, see [Configure the connector web app](archive-twitter-data#step-4-configure-the-connector-web-app).

When you complete this step, provide the following information. You copied this information to a text file after completing the previous steps:

- Twitter API Key (obtained in Step 3)
- Twitter API Secret Key (obtained in Step 3)
- Twitter Access Token (obtained in Step 3)
- Twitter Access Token Secret (obtained in Step 3)
- Microsoft Entra application ID (the Microsoft Entra application ID obtained in Step 1)
- Microsoft Entra application secret (the Microsoft Entra application secret obtained in Step 1)

## Step 5: Set up a Twitter connector in the Microsoft Purview portal

In this step, you set up the Twitter connector in the Microsoft Purview portal. The connector imports data from your organization's Twitter account to a specified mailbox in Microsoft 365. When you finish this step, the Microsoft 365 Import service starts importing data from your organization's Twitter account to Microsoft 365.

For step-by-step instructions, see [Set up a Twitter connector](archive-twitter-data#step-5-set-up-a-twitter-connector).

As you complete this step, provide the following information and save it in a text file:

- Azure app service URL (obtained in Step 2; for example, `https://twitterconnector.azurewebsites.net`)
- APISecretKey (created in Step 2)