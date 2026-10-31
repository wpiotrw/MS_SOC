---
layout: Conceptual
title: Set up a connector to archive Facebook data | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/archive-facebook-data-with-sample-connector
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to set up & use a connector in the Microsoft Purview portal to import & archive data from Facebook Business pages to Microsoft 365.
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
document_id: c88a9e79-3b68-9097-6ba5-9dd356bad9b2
document_version_independent_id: c88a9e79-3b68-9097-6ba5-9dd356bad9b2
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/archive-facebook-data-with-sample-connector.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: archive-facebook-data-with-sample-connector
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/archive-facebook-data-with-sample-connector.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: e99cea7f-02c9-ef93-a69f-65a8b2ad79df
---

# Set up a connector to archive Facebook data | Microsoft Learn

Use a connector to import and archive data from Facebook Business pages to Microsoft 365. After you set up and configure the connector, it connects to the Facebook Business page on a scheduled basis, converts the content of Facebook items to an email message format, and then imports those items to a mailbox in Microsoft 365.

After the Facebook data is imported, you can apply Microsoft Purview features such as Litigation Hold, eDiscovery, In-Place Archiving, Auditing, Communication Compliance, and Microsoft 365 retention policies to the Facebook data. For example, when you place a mailbox on Litigation Hold or assign it to a retention policy, the Facebook data is preserved. You can search third-party data by using eDiscovery or associate the mailbox where the Facebook data is stored with a custodian in a Microsoft Purview eDiscovery (Premium) case. Using a connector to import and archive Facebook data in Microsoft 365 can help your organization stay compliant with government and regulatory policies.

## Before you begin for setting up a connector for Facebook Business pages

Complete the following prerequisites before setting up and configuring a connector in the [Microsoft Purview portal](purview-portal) to import and archive data from your organization's Facebook Business pages.

- You need a Facebook account for your organization's business pages. You need to sign in to this account when setting up the connector. Currently, you can only archive data from Facebook Business pages; you can't archive data from individual Facebook profiles.
- Your organization must have a valid Azure subscription. If you don't have an existing Azure subscription, you can sign up for one of these options:

    - [Sign up for a free one year Azure subscription](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn)
    - [Sign up for a Pay-As-You-Go Azure subscription](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go/)
- The connector for Facebook Business pages can import a total of 200,000 items in a single day. If there are more than 200,000 Facebook Business items in a day, none of those items are imported to Microsoft 365.
- The user who sets up the custom connector in the Microsoft Purview portal (in Step 5) must be assigned the Data Connector Admin role. This role is required to add connectors on the **Data connectors** page in the Microsoft Purview portal. Multiple role groups include this role by default. For a list of these role groups, see [Roles in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions#roles-in-microsoft-defender-for-office-365-and-microsoft-purview-compliance). Alternatively, an admin in your organization can create a custom role group, assign the Data Connector Admin role, and then add the appropriate users as members. For instructions, see [Permissions in the Microsoft Purview portal](purview-permissions) and [Roles and role groups in Microsoft Defender for Office 365 and Microsoft Purview](/en-us/microsoft-365/security/office-365-security/scc-permissions).

## Step 1: Create an app in Microsoft Entra ID

First, register a new app in Microsoft Entra ID. This app corresponds to the Azure web app resource used by the Facebook connector, which you deploy in Step 2 and configure in Step 4.

For more information, see [Create an app in Microsoft Entra ID](archive-facebook-data#step-1-create-an-app-in-azure-active-directory).

When you complete this step, save the following information to a text file. You'll use these values in later steps in the deployment process.

- Microsoft Entra application ID
- Microsoft Entra application secret
- Tenant Id

## Step 2: Deploy the connector web service from GitHub to your Azure account

Next, deploy the source code for the Facebook Business pages connector app. This app uses the Facebook API to connect to your Facebook account and extract data so you can import it to Microsoft 365. The Facebook connector that you deploy for your organization uploads the items from your Facebook Business pages to the Azure Storage location that you create in this step. After you create a Facebook business pages connector in the Microsoft Purview portal (in Step 5), the Import service copies the Facebook business pages data from the Azure Storage location to a mailbox in your Microsoft 365 organization. As explained in the Before you begin section, you must have a valid Azure subscription to create an Azure Storage account.

For more information, see [Deploy the connector web service from GitHub to your Azure account](archive-facebook-data#step-2-deploy-the-connector-web-service-from-github-to-your-azure-account).

When you complete this step, provide the following information:

- APISecretKey: Create this secret during the completion of this step. It's used in Step 5.
- TenantId: The tenant ID of your Microsoft 365 organization that you copied after creating the Facebook connector app in Microsoft Entra ID in Step 1.

After you complete this step, copy the Azure app service URL (for example, `https://fbconnector.azurewebsites.net`). You need to use this URL to complete Step 3, Step 4, and Step 5.

## Step 3: Register the web app on Facebook

Create and configure a new app on Facebook. The Facebook business pages connector that you create in Step 5 uses the Facebook web app to interact with the Facebook API to obtain data from your organization's Facebook Business pages.

For more information, see [Register the Facebook app](archive-facebook-data#step-3-register-the-facebook-app).

When you complete this step, save the following information to a text file. You use these values to configure the Facebook connector app in Step 4.

- Facebook application ID
- Facebook application secret
- Facebook webhooks verify token

## Step 4: Configure the Facebook connector app

Add configuration settings to the Facebook connector app that you deployed as an Azure web app resource in Step 2. Go to the home page of the Facebook connector Azure web app and configure the connector app.

For more information, see [Configure the Facebook connector app](archive-facebook-data-with-sample-connector#step-4-configure-the-facebook-connector-app).

When you complete this step, provide the following information (that you copied to a text file after completing the previous steps):

- Facebook application ID (obtained in Step 3)
- Facebook application secret (obtained in Step 3)
- Facebook webhooks verify token (obtained in Step 3)
- Microsoft Entra application ID (the Microsoft Entra application ID obtained in Step 1)
- Microsoft Entra application secret (the Microsoft Entra application secret obtained in Step 1)

## Step 5: Set up a Facebook Business pages connector in the Microsoft Purview portal

In this step, you set up the connector in the Microsoft Purview portal that imports data from your Facebook Business pages to a specified mailbox in Microsoft 365. When you finish this step, the Microsoft 365 Import service starts importing data from your Facebook Business pages to Microsoft 365.

For more information, see [Step 5: Set up a Facebook connector in the Microsoft Purview portal](archive-facebook-data#step-5-set-up-a-facebook-connector).

As you complete this step, you provide the following information, which you copy to a text file after completing the steps:

- Microsoft Entra application ID (obtained in Step 1)
- Azure app service URL (obtained in Step 2; for example, `https://fbconnector.azurewebsites.net`)
- APISecretKey (created in Step 2)