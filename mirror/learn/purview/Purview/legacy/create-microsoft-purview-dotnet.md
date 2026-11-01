---
layout: Conceptual
title: 'Quickstart: Create Microsoft Purview (formerly Azure Purview) account using .NET SDK | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/create-microsoft-purview-dotnet
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article will guide you through creating a Microsoft Purview (formerly Azure Purview) account using .NET SDK.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: nayenama
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.devlang: csharp
ms.topic: quickstart
ms.date: 2025-02-26T00:00:00.0000000Z
ms.custom: mode-api, devx-track-dotnet
locale: en-us
document_id: d765a9c7-0ac1-2ba6-2f7c-5eeddaf333e3
document_version_independent_id: d765a9c7-0ac1-2ba6-2f7c-5eeddaf333e3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/create-microsoft-purview-dotnet.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/create-microsoft-purview-dotnet
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/create-microsoft-purview-dotnet.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/7696cda6-0510-47f6-8302-71bb5d2e28cf
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/69c76c32-967e-4c65-b89a-74cc527db725
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: b73655d6-8319-e13c-f596-3da9c9b67d9d
---

# Quickstart: Create Microsoft Purview (formerly Azure Purview) account using .NET SDK | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

You can only create one Microsoft Purview account per tenant. If your organization already has a Microsoft Purview account, you won't be able to create a new Microsoft Purview account unless your organization already had multiple accounts and is still under the [the preexisting quota](../classic-how-to-manage-quotas#classic-microsoft-purview-data-governance-limits). For more information, see [the FAQ](../data-governance-purview-portal-faq#can-i-create-new-microsoft-purview-accounts-in-my-subscription-).

In this quickstart, you'll use the [.NET SDK](/en-us/dotnet/api/overview/azure/purview) to create a Microsoft Purview (formerly Azure Purview) account.

The Microsoft Purview governance portal surfaces tools like the Microsoft Purview Data Map and Microsoft Purview Data Catalog that help you manage and govern your data landscape. By connecting to data across your on-premises, multicloud, and software-as-a-service (SaaS) sources, the Microsoft Purview Data Map creates an up-to-date map of your information. It identifies and classifies sensitive data, and provides end-to-end linage. Data consumers are able to discover data across your organization, and data administrators are able to audit, secure, and ensure right use of your data.

For more information about the classic governance capabilities of Microsoft Purview, [see our governance solutions overview page](../governance-solutions-overview).

## Prerequisites

- If you don't have an Azure subscription, create a [free subscription](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.
- A [Microsoft Entra tenant](/en-us/azure/active-directory/fundamentals/active-directory-access-create-new-tenant) associated with your subscription.
- The user account that you use to sign in to Azure must be a member of the *contributor* or *owner* role, or an *administrator* of the Azure subscription. To view the permissions that you have in the subscription, follow these steps:

    1. Go to the [Azure portal](https://portal.azure.com)
    2. Select your username in the upper-right corner.
    3. Select the ellipsis button ("**...**") for more options.
    4. Then select **My permissions**.
    5. If you have access to multiple subscriptions, select the appropriate subscription.

## Sign in to Azure

Sign in to the [Azure portal](https://portal.azure.com) with your Azure account.

### Visual Studio

The walkthrough in this article uses Visual Studio 2019. The procedures for Visual Studio 2013, 2015, or 2017 may differ slightly.

### Azure .NET SDK

Download and install [Azure .NET SDK](https://azure.microsoft.com/downloads/) on your machine.

## Create an application in Microsoft Entra ID

1. In [Create a Microsoft Entra application](/en-us/azure/active-directory/develop/howto-create-service-principal-portal#register-an-application-with-azure-ad-and-create-a-service-principal), create an application that represents the .NET application you're creating in this tutorial. For the sign-on URL, you can provide a dummy URL as shown in the article (`https://contoso.org/exampleapp`).
2. In [Get values for signing in](/en-us/azure/active-directory/develop/howto-create-service-principal-portal#sign-in-to-the-application), get the **application ID** and **tenant ID**, and note down these values that you use later in this tutorial.
3. In [Certificates and secrets](/en-us/azure/active-directory/develop/howto-create-service-principal-portal#set-up-authentication), get the **authentication key**, and note down this value that you use later in this tutorial.
4. In [Assign the application to a role](/en-us/azure/active-directory/develop/howto-create-service-principal-portal#assign-a-role-to-the-application), assign the application to the **Contributor** role at the subscription level so that the application can create data factories in the subscription.

## Create a Visual Studio project

Next, create a C# .NET console application in Visual Studio:

1. Launch **Visual Studio**.
2. In the Start window, select **Create a new project** &gt; **Console App (.NET Framework)**. .NET version 4.5.2 or above is required.
3. In **Project name**, enter **PurviewQuickStart**.
4. Select **Create** to create the project.

## Install NuGet packages

1. Select **Tools** &gt; **NuGet Package Manager** &gt; **Package Manager Console**.
2. In the **Package Manager Console** pane, run the following commands to install packages. For more information, see the [Microsoft.Azure.Management.Purview NuGet package](https://www.nuget.org/packages/Microsoft.Azure.Management.Purview/).

    ```powershell
    Install-Package Microsoft.Azure.Management.Purview
    Install-Package Microsoft.Azure.Management.ResourceManager -IncludePrerelease
    Install-Package Microsoft.IdentityModel.Clients.ActiveDirectory
    ```

Tip

If you are getting an error that reads: **Package &lt;package name&gt; is not found in the following primary sources(s):** and it is listing a local folder, you need to update your package sources in Visual Studio to include the nuget site as an online source.

1. Go to **Tools**
2. Select **NuGet Package Manager**
3. Select **Package Manage Settings**
4. Select **Package Sources**
5. Add https://nuget.org/api/v2/ as a source.

## Create a Microsoft Purview client

1. Open **Program.cs**, include the following statements to add references to namespaces.

    ```csharp
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using Microsoft.Rest;
    using Microsoft.Rest.Serialization;
       using Microsoft.Azure.Management.ResourceManager;
    using Microsoft.Azure.Management.Purview;
       using Microsoft.Azure.Management.Purview.Models;
       using Microsoft.IdentityModel.Clients.ActiveDirectory;
    ```
2. Add the following code to the **Main** method that sets the variables. Replace the placeholders with your own values. For a list of Azure regions in which Microsoft Purview is currently available, search on **Microsoft Purview** and select the regions that interest you on the following page: [Products available by region](https://azure.microsoft.com/global-infrastructure/services/).

    ```csharp
    // Set variables
    string tenantID = "<your tenant ID>";
    string applicationId = "<your application ID>";
    string authenticationKey = "<your authentication key for the application>";
    string subscriptionId = "<your subscription ID where the data factory resides>";
    string resourceGroup = "<your resource group where the data factory resides>";
    string region = "<the location of your resource group>";
    string purviewAccountName = 
        "<specify the name of purview account to create. It must be globally unique.>";
    ```
3. Add the following code to the **Main** method that creates an instance of **PurviewManagementClient** class. You use this object to create a Microsoft Purview Account.

    ```csharp
    // Authenticate and create a purview management client
    var context = new AuthenticationContext("https://login.windows.net/" + tenantID);
    ClientCredential cc = new ClientCredential(applicationId, authenticationKey);
    AuthenticationResult result = context.AcquireTokenAsync(
    "https://management.azure.com/", cc).Result;
    ServiceClientCredentials cred = new TokenCredentials(result.AccessToken);
    var client = new PurviewManagementClient(cred)
    {
       SubscriptionId = subscriptionId           
    };
    ```

## Create an account

Add the following code to the **Main** method that will create the **Microsoft Purview Account**.

```csharp
// Create a purview Account
Console.WriteLine("Creating Microsoft Purview Account " + purviewAccountName + "...");
Account account = new Account()
{
Location = region,
Identity = new Identity(type: "SystemAssigned"),
Sku = new AccountSku(name: "Standard", capacity: 4)
};            
try
{
  client.Accounts.CreateOrUpdate(resourceGroup, purviewAccountName, account);
  Console.WriteLine(client.Accounts.Get(resourceGroup, purviewAccountName).ProvisioningState);                
}
catch (ErrorResponseModelException purviewException)
{
Console.WriteLine(purviewException.StackTrace);
  }
  Console.WriteLine(
    SafeJsonConvert.SerializeObject(account, client.SerializationSettings));
  while (client.Accounts.Get(resourceGroup, purviewAccountName).ProvisioningState ==
         "PendingCreation")
  {
    System.Threading.Thread.Sleep(1000);
  }
Console.WriteLine("\nPress any key to exit...");
Console.ReadKey();
```

## Run the code

Build and start the application, then verify the execution.

The console prints the progress of creating Microsoft Purview Account.

### Sample output

```json
Creating Microsoft Purview Account testpurview...
Succeeded
{
  "sku": {
    "capacity": 4,
    "name": "Standard"
  },
  "identity": {
    "type": "SystemAssigned"
  },
  "location": "southcentralus"
}

Press any key to exit...
```

## Verify the output

Go to the **Microsoft Purview accounts** page in the [Azure portal](https://portal.azure.com) and verify the account created using the above code.

## Delete Microsoft Purview account

To programmatically delete a Microsoft Purview account, add the following lines of code to the program:

```csharp
Console.WriteLine("Deleting the Microsoft Purview Account");
client.Accounts.Delete(resourceGroup, purviewAccountName);
```

## Check if Microsoft Purview account name is available

To check availability of a purview account, use the following code:

```csharp
CheckNameAvailabilityRequest checkNameAvailabilityRequest = newCheckNameAvailabilityRequest()
{
    Name = purviewAccountName,
    Type =  "Microsoft.Purview/accounts"
};
Console.WriteLine("Check Microsoft Purview account name");
Console.WriteLine(client.Accounts.CheckNameAvailability(checkNameAvailabilityRequest).NameAvailable);
```

The above code with print 'True' if the name is available and 'False' if the name isn't available.