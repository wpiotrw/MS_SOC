---
layout: Conceptual
title: 'Quickstart: Share data using the .NET SDK | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/quickstart-data-share-dotnet
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article guides you through sharing and receiving data using Microsoft Purview Data Sharing account through the .NET SDK.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: sidnotha
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.devlang: csharp
ms.topic: quickstart
ms.date: 2024-09-24T00:00:00.0000000Z
ms.custom: mode-api, references-regions, devx-track-azurepowershell, devx-track-dotnet
locale: en-us
document_id: 33a09cd4-3a52-2bff-5ed9-4b82a5706f89
document_version_independent_id: 33a09cd4-3a52-2bff-5ed9-4b82a5706f89
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/quickstart-data-share-dotnet.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/quickstart-data-share-dotnet
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/quickstart-data-share-dotnet.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/7cf8f81d-2989-4e5d-aa91-5191d10a3323
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/1cb9c90f-9a3f-4389-8367-0a20c542621f
platformId: 3e78e363-53bf-df25-7697-59fc2bd40690
---

# Quickstart: Share data using the .NET SDK | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently being retired, with support provided until September 2025 to allow for migration to [Microsoft Fabric external data sharing](/en-us/fabric/governance/external-data-sharing-overview).

In this quickstart, you'll use the .NET SDK to share data and receive shares from Azure Data Lake Storage (ADLS Gen2) or Blob storage accounts. The article includes code snippets that allow you to create, accept, and manage shares using Microsoft Purview Data Sharing.

For an overview of how data sharing works, watch this short [demo](https://aka.ms/purview-data-share/overview-demo).

Note

This feature has been updated in February 2023, and the SDK and permissions needed to view and manage data shares in Microsoft Purview have changed.

- No permissions are now required in Microsoft Purview to use the SDK to create and manage shares. (Reader permissions are needed to use the Microsoft Purview Governance Portal for sharing data.)
- Permissions are still required on storage accounts.

See the updated NuGet package and updated code snippets to use the updated SDK.

## Prerequisites

### Microsoft Purview prerequisites

- [A Microsoft Purview account](../create-microsoft-purview-portal). You can also use two Microsoft Purview accounts, one for data provider and one for data consumer to test both scenarios.
- Your recipient's Azure sign-in email address that you can use to send the invitation to. The recipient's email alias won't work.

### Azure Storage account prerequisites

- Your Azure subscription must be registered for the **AllowDataSharing** preview feature. (If you haven't already registered this preview feature, consider using [Microsoft Fabric external data sharing](/en-us/fabric/governance/external-data-sharing-overview) instead, since Microsoft Purview Data Sharing will be retired in September 2025.) Or, [contact support](../concept-data-share#support).
- Source and target storage accounts **created after** the registration step is completed. **Both storage accounts must be in the same Azure region as each other**. Both storage accounts need to be ADLS Gen2 or Blob Storage accounts. Your storage accounts can be in a different Azure region from your Microsoft Purview account.
- Latest version of the storage SDK, PowerShell, CLI, and Azure Storage Explorer. Storage REST API version must be February 2020 or later.
- The storage accounts need to be registered in the collections where you'll send or receive the share. If you're using one Microsoft Purview account, this can be two different collections, or the same collection. For instructions to register, see the [ADLS Gen2](../register-scan-adls-gen2) or [Blob storage](../register-scan-azure-blob-storage-source) data source pages.
- If the source or target storage accounts are in a different Azure subscription than the one for Microsoft Purview account, the Microsoft. Purview resource provider is automatically registered in the Azure subscription where the data store is located at the time of share provider adding an asset or share consumer mapping an asset and **ONLY** if the user has permission to do the /register/action operation for the resource provider. The permission is included in the Contributor and Owner roles. 
    Note

    This registration is only needed the first time when sharing or receiving data into a storage account in the Azure subscription.

### Required roles

Here are required roles for sharing data and receiving shares.

| - | Azure Storage account roles | Microsoft Purview collection roles |
| --- | --- | --- |
| **Data provider** | One of the following roles: <br>- Owner<br>- Storage Blob Data Owner | Data Reader |
| **Data consumer** | One of the following roles: <br>- Contributor<br>- Owner<br>- Storage Blob Data Contributor<br>- Storage Blob Data Owner | Data Reader |

Note

If you created the Microsoft Purview account, you're automatically assigned all the roles to the root collection. Refer to [Microsoft Purview permissions](../data-gov-classic-permissions) to learn more about the Microsoft Purview collection and roles.

### Visual Studio

The walkthrough in this article uses Visual Studio 2022. The procedures for Visual Studio 2013, 2015, 2017, or 2019 may differ slightly.

### Azure .NET SDK

Download and install [Azure .NET SDK](https://azure.microsoft.com/downloads/) on your machine.

## Use a service principal

In the code snippets in this tutorial, you can authenticate either using your own credentials or using a service principal. To set up a service principal, follow these instructions:

1. In [Create a Microsoft Entra application](/en-us/azure/active-directory/develop/howto-create-service-principal-portal#register-an-application-with-azure-ad-and-create-a-service-principal), create an application that represents the .NET application you're creating in this tutorial. For the sign-on URL, you can provide a dummy URL as shown in the article (`https://contoso.org/exampleapp`).
2. In [Get values for signing in](/en-us/azure/active-directory/develop/howto-create-service-principal-portal#sign-in-to-the-application), get the **application ID**,**tenant ID**, and **object ID**, and note down these values that you use later in this tutorial.
3. In [Certificates and secrets](/en-us/azure/active-directory/develop/howto-create-service-principal-portal#set-up-authentication), get the **authentication key**, and note down this value that you use later in this tutorial.
4. [assign the application to these roles:](/en-us/azure/active-directory/develop/howto-create-service-principal-portal#assign-a-role-to-the-application)

    | User | Azure Storage account roles | Microsoft Purview collection roles |
    | --- | --- | --- |
    | **Data provider** | One of the following roles:<br>    - Owner<br>    - Blob Storage Data Owner | Data Share Contributor |
    | **Data consumer** | One of the following roles:<br>    - Contributor<br>    - Owner<br>    - Storage Blob Data Contributor<br>    - Blob Storage Data Owner | Data Share Contributor |

## Create a Visual Studio project

Next, create a C# .NET console application in Visual Studio:

1. Launch **Visual Studio**.
2. In the Start window, select **Create a new project** &gt; **Console App**. .NET version 6.0 or above is required.
3. In **Project name**, enter **PurviewDataSharingQuickStart**.
4. Select **Create** to create the project.

## Install NuGet packages

1. Select **Tools** &gt; **NuGet Package Manager** &gt; **Package Manager Console**.
2. In the **Package Manage Console** run the .NET cli add package command shown on this page to add the NuGet package: [Microsoft.Azure.Analytics.Purview.Sharing NuGet package](https://www.nuget.org/packages/Azure.Analytics.Purview.Sharing).
3. In the **Package Manager Console** pane, run the following commands to install packages.

    ```powershell
    Install-Package Azure.Analytics.Purview.Sharing -IncludePrerelease
    Install-Package Azure.Identity
    ```

    Tip

    If you get an error that reads "Could not find any project in..." when attempting these commands, you may just need to move a folder level down in your project. Try the command `dir` to list folders in your directory, then use 'cd &lt;name of the project folder&gt;' to move down a level to your project folder. Then try again.

## Create a sent share

This script creates a data share that you can send to internal or external users. To use it, be sure to fill out these variables:

- **SenderTenantId** - the [Azure Tenant ID](/en-us/partner-center/find-ids-and-domain-names#find-the-microsoft-azure-ad-tenant-id-and-primary-domain-name) for the sender's identity.
- **SenderPurviewAccountName** - the name of the Microsoft Purview account where the data will be sent from.
- **ShareName** - A display name for your sent share.
- **ShareDescription** - (optional) A description for your sent share.
- **SenderStorageKind** - either BlobAccount or AdlsGen2Account.
- **SenderStorageResourceId** - the [resource ID for the storage account](/en-us/azure/storage/common/storage-account-get-info#get-the-resource-id-for-a-storage-account) where the data will be sent from.
- **SenderStorageContainer** - the name of the container where the data to be shared is stored.
- **SenderPathToShare** - the file/folder path to the data to be shared.
- **UseServiceTokenCredentials** - (optional) If you want to use a service principal to create the shares, set this to **true**.
- **SenderClientId** - (optional) If using a service principal to create the shares, this is the Application (client) ID for the service principal.
- **SenderClientSecret** - (optional) If using a service principal to create the shares, add your client secret/authentication key.
- **SentShareID** - (optional) This option must be a GUID, and the current value generates one for you, but you can replace it with a different value if you would like.
- **ReceiverVisiblePath** - (optional) The name for the share the receiver will see. Currently set to a GUID, but GUID is not required.
- **SenderPurviewEndPoint** - If you're using If you're using the [classic Microsoft purview experience](../use-microsoft-purview-governance-portal), use `$"https://{SenderPurviewAccountName}.purview.azure.com"`; If you're using the [new Microsoft Purview experience](../purview-portal), use `https://api.purview-service.microsoft.com/`

```C
using Azure;
using Azure.Analytics.Purview.Sharing;
using Azure.Core;
using Azure.Identity;
using System.ComponentModel;

public static class PurviewDataSharingQuickStart
{
    // [REQUIRED INPUTS] Set To Actual Values.
    private static string SenderTenantId = "<Sender Identity's Tenant ID>";
    private static string SenderPurviewAccountName = "<Sender Purview Account Name>";

    private static string ShareName = "<Share Display Name>";
    private static string ShareDescription = "Share created using the SDK.";
    private static string SenderStorageKind = "<Sender Storage Account Kind (BlobAccount / AdlsGen2Account)>";
    private static string SenderStorageResourceId = "<Sender Storage Account Resource Id>";
    private static string SenderStorageContainer = "<Share Data Container Name>";
    private static string SenderPathToShare = "<File/Folder Path To Share>";

    // Set if using Service principal to create shares
    private static bool UseServiceTokenCredentials = false;
    private static string SenderClientId = "<Sender Application (Client) Id>";
    private static string SenderClientSecret = "<Sender Application (Client) Secret>";

    // [OPTIONAL INPUTS] Override Value If Desired.
    private static string SentShareId = Guid.NewGuid().ToString();
    private static string ReceiverVisiblePath = Guid.NewGuid().ToString();

    // General Configs
    private static string SenderPurviewEndPoint = $"https://{SenderPurviewAccountName}.purview.azure.com";
    private static string SenderShareEndPoint = $"{SenderPurviewEndPoint}/share";

    private static async Task Main(string[] args)
    {
        try
        {
            /// Replace all placeholder inputs above with actual values before running this program.
            /// This updated Share experience API will create Shares based on callers RBAC role on the storage account.
            /// To view/manage Shares via UX in Purview Studio. Storage accounts need to be registered (one time action) in Purview account with DSA permissions.

            Console.WriteLine($"{DateTime.Now.ToShortTimeString()}: CreateShare - START");
            await Sender_CreateSentShare();
            Console.WriteLine($"{DateTime.Now.ToShortTimeString()}: CreateShare - FINISH");
        }
        catch (Exception ex)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(ex);
            Console.ForegroundColor = Console.ForegroundColor;
        }
    }

    private static async Task<BinaryData> Sender_CreateSentShare()
    {

        TokenCredential senderCredentials = UseServiceTokenCredentials
                ? new ClientSecretCredential(SenderTenantId, SenderClientId, SenderClientSecret)
                : new DefaultAzureCredential(new DefaultAzureCredentialOptions { AuthorityHost = new Uri("https://login.windows.net"), TenantId = SenderTenantId });

        SentSharesClient? sentSharesClient = new SentSharesClient(SenderShareEndPoint, senderCredentials);

        if (sentSharesClient == null)
        {
            throw new InvalidEnumArgumentException("Invalid Sent Shares Client.");
        }

        // Create sent share
        var inPlaceSentShareDto = new
        {
            shareKind = "InPlace",
            properties = new
            {
                displayName = ShareName,
                description = ShareDescription,
                artifact = new
                {
                    storeKind = SenderStorageKind,
                    storeReference = new
                    {
                        referenceName = SenderStorageResourceId,
                        type = "ArmResourceReference"
                    },
                    properties = new
                    {
                        paths = new[]
                        {
                            new
                            {
                                receiverPath = ReceiverVisiblePath,
                                containerName = SenderStorageContainer,
                                senderPath = SenderPathToShare
                            }
                        }
                    }
                }
            },
        };

        Operation<BinaryData> sentShare = await sentSharesClient.CreateOrReplaceSentShareAsync(WaitUntil.Completed, SentShareId, RequestContent.Create(inPlaceSentShareDto));
        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine(sentShare.Value);
        Console.ForegroundColor = Console.ForegroundColor;
        return sentShare.Value;
    }
}
```

## Send invitation to a user

This script sends an email invitation for a share to a user. If you want to send an invitation to a service principal, see the next code example. To use it, be sure to fill out these variables:

- **RecipientUserEmailId** - Email address for the user to send the invitation to.
- **SenderTenantId** - the Azure Tenant ID for the share sender's identity.
- **SenderPurviewAccountName** - the name of the Microsoft Purview account where the data will be sent from.
- **SenderStorageResourceId** - the [resource ID for the storage account](/en-us/azure/storage/common/storage-account-get-info#get-the-resource-id-for-a-storage-account) where the data will be sent from.
- **SentShareDisplayName** - the name of the sent share you're sending an invitation for.
- **UseServiceTokenCredentials** - (optional) If you want to use a service principal to create the shares, set this to **true**.
- **SenderClientId** - (optional) If using a service principal to create the shares, this is the Application (client) ID for the service principal.
- **SenderClientSecret** - (optional) If using a service principal to create the shares, add your client secret/authentication key.
- **InvitationId** - (optional) This option must be a GUID, and the current value generates one for you, but you can replace it with a different value if you would like.
- **SenderPurviewEndPoint** - If you're using If you're using the [classic Microsoft purview experience](../use-microsoft-purview-governance-portal), use `$"https://{SenderPurviewAccountName}.purview.azure.com"`; If you're using the [new Microsoft Purview experience](../purview-portal), use `https://api.purview-service.microsoft.com/`

```C
using Azure;
using Azure.Analytics.Purview.Sharing;
using Azure.Core;
using Azure.Identity;
using System.ComponentModel;
using System.Text.Json;

public static class PurviewDataSharingQuickStart
{
    // [REQUIRED INPUTS] Set To Actual Values.
    private static string RecipientUserEmailId = "<Target User's Email Id>";

    private static string SenderTenantId = "<Sender Indentity's Tenant ID>";
    private static string SenderPurviewAccountName = "<Sender Purview Account Name>";
    private static string SenderStorageResourceId = "<Sender Storage Account Resource Id>";

    // Set if using Service principal to send invitation
    private static bool UseServiceTokenCredentials = false;
    private static string SenderClientId = "<Sender Application (Client) Id>";
    private static string SenderClientSecret = "<Sender Application (Client) Secret>";

    private static string SentShareDisplayName = "<Name of share you're sending an invite for.>";
    private static string InvitationId = Guid.NewGuid().ToString();

    // General Configs
    private static string SenderPurviewEndPoint = $"https://{SenderPurviewAccountName}.purview.azure.com";
    private static string SenderShareEndPoint = $"{SenderPurviewEndPoint}/share";
    private static int StepCounter = 0;

    private static async Task Main(string[] args)
    {
        try
        {

            Console.WriteLine($"{DateTime.Now.ToShortTimeString()}: SendtoUser - START");
            await Sender_CreateUserRecipient();
            Console.WriteLine($"{DateTime.Now.ToShortTimeString()}: SendtoUser - FINISH");
        }
        catch (Exception ex)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(ex);
            Console.ForegroundColor = Console.ForegroundColor;
        }
    }

    public static async Task<List<T>> ToResultList<T>(this AsyncPageable<T> asyncPageable)
    {
        List<T> list = new List<T>();

        await foreach (T item in asyncPageable)
        {
            list.Add(item);
        }

        return list;
    }

    private static async Task<BinaryData> Sender_CreateUserRecipient()
    {

        TokenCredential senderCredentials = UseServiceTokenCredentials
                ? new ClientSecretCredential(SenderTenantId, SenderClientId, SenderClientSecret)
                : new DefaultAzureCredential(new DefaultAzureCredentialOptions { AuthorityHost = new Uri("https://login.windows.net"), TenantId = SenderTenantId });

        SentSharesClient? sentSharesClient = new SentSharesClient(SenderShareEndPoint, senderCredentials);

        if (string.IsNullOrEmpty(RecipientUserEmailId))
        {
            throw new InvalidEnumArgumentException("Invalid Recipient User Email Id.");
        }

        // Create user recipient and invite
        var invitationData = new
        {
            invitationKind = "User",
            properties = new
            {
                expirationDate = DateTime.Now.AddDays(7).ToString(),
                notify = true, // Send invitation email
                targetEmail = RecipientUserEmailId
            }
        };

        var allSentShares = await sentSharesClient.GetAllSentSharesAsync(SenderStorageResourceId).ToResultList();

        Console.ForegroundColor = ConsoleColor.Yellow;
        Console.WriteLine("{0}. {1}...", ++StepCounter, "Get a Specific Sent Share");
        Console.ForegroundColor = Console.ForegroundColor;

        var mySentShare = allSentShares.First(sentShareDoc =>
        {
            var doc = JsonDocument.Parse(sentShareDoc).RootElement;
            var props = doc.GetProperty("properties");
            return props.GetProperty("displayName").ToString() == SentShareDisplayName;
        });

        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine("My Sent Share Id: " + JsonDocument.Parse(mySentShare).RootElement.GetProperty("id").ToString());
        Console.ForegroundColor = Console.ForegroundColor;

        var SentShareId = JsonDocument.Parse(mySentShare).RootElement.GetProperty("id").ToString();

        var sentInvitation = await sentSharesClient.CreateSentShareInvitationAsync(SentShareId, InvitationId, RequestContent.Create(invitationData));

        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine(sentInvitation.Content);
        Console.ForegroundColor = Console.ForegroundColor;

        return sentInvitation.Content;
    }
}
```

## Send invitation to a service

This script sends an email invitation for a share to a service principal. If you want to send an invitation to a user, see the previous sample. To use it, be sure to fill out these variables:

- **RecipientApplicationTenantId** - the Azure Tenant ID for the receiving service principal.
- **RecipientApplicationObjectId** - the object ID for the receiving service principal.
- **SenderTenantId** - the Azure Tenant ID for the share sender's identity.
- **SenderPurviewAccountName** - the name of the Microsoft Purview account where the data will be sent from.
- **SenderStorageResourceId** - the [resource ID for the storage account](/en-us/azure/storage/common/storage-account-get-info#get-the-resource-id-for-a-storage-account) where the data will be sent from.
- **SentShareDisplayName** - the name of the sent share you're sending an invitation for.
- **UseServiceTokenCredentials** - (optional) If you want to use a service principal to create the shares, set this to **true**.
- **SenderClientId** - (optional) If using a service principal to create the shares, this is the Application (client) ID for the service principal.
- **SenderClientSecret** - (optional) If using a service principal to create the shares, add your client secret/authentication key.
- **InvitationId** - (optional) This option must be a GUID, and the current value generates one for you, but you can replace it with a different value if you would like.
- **SenderPurviewEndPoint** - If you're using If you're using the [classic Microsoft purview experience](../use-microsoft-purview-governance-portal), use `$"https://{SenderPurviewAccountName}.purview.azure.com"`; If you're using the [new Microsoft Purview experience](../purview-portal), use `https://api.purview-service.microsoft.com/`

```C
using Azure;
using Azure.Analytics.Purview.Sharing;
using Azure.Core;
using Azure.Identity;
using System.ComponentModel;
using System.Text.Json;

public static class PurviewDataSharingQuickStart
{
    // [REQUIRED INPUTS] Set To Actual Values.
    private static string RecipientApplicationTenantId = "<Target Application's Tenant Id>";
    private static string RecipientApplicationObjectId = "<Target Application's Object Id>";

    private static string SentShareDisplayName = "<Name of share you're sending an invite for.>";
    private static string InvitationId = Guid.NewGuid().ToString();

    private static string SenderTenantId = "<Sender Indentity's Tenant ID>";
    private static string SenderPurviewAccountName = "<Sender Purview Account Name>";

    private static string SenderStorageResourceId = "<Resource ID for storage account that has been shared>";

    // Set if using Service principal to send invitation
    private static bool UseServiceTokenCredentials = false;
    private static string SenderClientId = "<Sender Application (Client) Id>";
    private static string SenderClientSecret = "<Sender Application (Client) Secret>";

    // General Configs
    private static string SenderPurviewEndPoint = $"https://{SenderPurviewAccountName}.purview.azure.com";
    private static string SenderShareEndPoint = $"{SenderPurviewEndPoint}/share";

    private static async Task Main(string[] args)
    {
        try
        {

            Console.WriteLine($"{DateTime.Now.ToShortTimeString()}: SendtoService - START");
            await Sender_CreateServiceRecipient();
            Console.WriteLine($"{DateTime.Now.ToShortTimeString()}: SendtoService - FINISH");
        }
        catch (Exception ex)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(ex);
            Console.ForegroundColor = Console.ForegroundColor;
        }
    }

    public static async Task<List<T>> ToResultList<T>(this AsyncPageable<T> asyncPageable)
    {
        List<T> list = new List<T>();

        await foreach (T item in asyncPageable)
        {
            list.Add(item);
        }

        return list;
    }

    private static async Task<BinaryData> Sender_CreateServiceRecipient()
    {

        TokenCredential senderCredentials = UseServiceTokenCredentials
                ? new ClientSecretCredential(SenderTenantId, SenderClientId, SenderClientSecret)
                : new DefaultAzureCredential(new DefaultAzureCredentialOptions { AuthorityHost = new Uri("https://login.windows.net"), TenantId = SenderTenantId });

        SentSharesClient? sentSharesClient = new SentSharesClient(SenderShareEndPoint, senderCredentials);

        if (!Guid.TryParse(RecipientApplicationTenantId, out Guid _))
        {
            throw new InvalidEnumArgumentException("Invalid Recipient Service Tenant Id.");
        }

        if (!Guid.TryParse(RecipientApplicationObjectId, out Guid _))
        {
            throw new InvalidEnumArgumentException("Invalid Recipient Service Object Id.");
        }

        // Create service recipient
        var invitationData = new
        {
            invitationKind = "Service",
            properties = new
            {
                expirationDate = DateTime.Now.AddDays(5).ToString(),
                targetActiveDirectoryId = RecipientApplicationTenantId,
                targetObjectId = RecipientApplicationObjectId
            }
        };

        var allSentShares = await sentSharesClient.GetAllSentSharesAsync(SenderStorageResourceId).ToResultList();
        var mySentShare = allSentShares.First(sentShareDoc =>
        {
            var doc = JsonDocument.Parse(sentShareDoc).RootElement;
            var props = doc.GetProperty("properties");
            return props.GetProperty("displayName").ToString() == SentShareDisplayName;
        });

        var SentShareId = JsonDocument.Parse(mySentShare).RootElement.GetProperty("id").ToString();

        var sentInvitation = await sentSharesClient.CreateSentShareInvitationAsync(SentShareId, InvitationId, RequestContent.Create(invitationData));
        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine(sentInvitation.Content);
        Console.ForegroundColor = Console.ForegroundColor;
        return sentInvitation.Content;
    }

}
```

## List sent shares

This script lists all the sent shares for a specific storage resource. To use it, be sure to fill out these variables:

- **SenderTenantId** - the Azure Tenant ID for the share sender's identity.
- **SenderPurviewAccountName** - the name of the Microsoft Purview account where the data was sent from.
- **SenderStorageResourceId** - the [resource ID for the storage account](/en-us/azure/storage/common/storage-account-get-info#get-the-resource-id-for-a-storage-account) where shares have been sent from.
- **UseServiceTokenCredentials** - (optional) If you want to use a service principal to create the shares, set this to **true**.
- **SenderClientId** - (optional) If using a service principal to create the shares, this is the Application (client) ID for the service principal.
- **SenderClientSecret** - (optional) If using a service principal to create the shares, add your client secret/authentication key.
- **SenderPurviewEndPoint** - If you're using If you're using the [classic Microsoft purview experience](../use-microsoft-purview-governance-portal), use `$"https://{SenderPurviewAccountName}.purview.azure.com"`; If you're using the [new Microsoft Purview experience](../purview-portal), use `https://api.purview-service.microsoft.com/`

```C
using Azure;
using Azure.Analytics.Purview.Sharing;
using Azure.Core;
using Azure.Identity;

public static class PurviewDataSharingQuickStart
{
    // [REQUIRED INPUTS] Set To Actual Values.
    private static string SenderTenantId = "<Sender Tenant ID>";
    private static string SenderPurviewAccountName = "<Name of the Microsoft Purview account>";
    private static string SenderStorageResourceId = "<Sender Storage Account Resource Id>";

    // Set if using Service principal to list shares
    private static bool UseServiceTokenCredentials = false;
    private static string SenderClientId = "<Sender Application (Client) Id>";
    private static string SenderClientSecret = "<Sender Application (Client) Secret>";

    // General Configs
    private static string SenderPurviewEndPoint = $"https://{SenderPurviewAccountName}.purview.azure.com";
    private static string SenderShareEndPoint = $"{SenderPurviewEndPoint}/share";

    private static async Task Main(string[] args)
    {

        try
        {
            TokenCredential senderCredentials = UseServiceTokenCredentials
                ? new ClientSecretCredential(SenderTenantId, SenderClientId, SenderClientSecret)
                : new DefaultAzureCredential(new DefaultAzureCredentialOptions { AuthorityHost = new Uri("https://login.windows.net"), TenantId = SenderTenantId });

            SentSharesClient? sentSharesClient = new SentSharesClient(SenderShareEndPoint, senderCredentials);

            var allSentShares = await sentSharesClient.GetAllSentSharesAsync(SenderStorageResourceId).ToResultList();
            Console.WriteLine(allSentShares);
        }
        catch (Exception ex)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(ex);
            Console.ForegroundColor = Console.ForegroundColor;
        }
    }

    public static async Task<List<T>> ToResultList<T>(this AsyncPageable<T> asyncPageable)
    {
        List<T> list = new List<T>();

        await foreach (T item in asyncPageable)
        {
            list.Add(item);
        }

        return list;
    }
}
```

## List all share recipients

This script lists all recipients for a specific share. To use it, be sure to fill out these variables:

- **SenderTenantId** - the Azure Tenant ID for the share sender's identity.
- **SenderPurviewAccountName** - the name of the Microsoft Purview account where the data was sent from.
- **SentShareDisplayName** - the name of the sent share you're listing recipients for.
- **SenderStorageResourceId** - the [resource ID for the storage account](/en-us/azure/storage/common/storage-account-get-info#get-the-resource-id-for-a-storage-account) where the data will be sent from.
- **UseServiceTokenCredentials** - (optional) If you want to use a service principal to create the shares, set this to **true**.
- **SenderClientId** - (optional) If using a service principal to create the shares, this is the Application (client) ID for the service principal.
- **SenderClientSecret** - (optional) If using a service principal to create the shares, add your client secret/authentication key.
- **SenderPurviewEndPoint** - If you're using If you're using the [classic Microsoft purview experience](../use-microsoft-purview-governance-portal), use `$"https://{SenderPurviewAccountName}.purview.azure.com"`; If you're using the [new Microsoft Purview experience](../purview-portal), use `https://api.purview-service.microsoft.com/`

```C
using Azure;
using Azure.Analytics.Purview.Sharing;
using Azure.Core;
using Azure.Identity;
using System.Text.Json;

public static class PurviewDataSharingQuickStart
{
    // [REQUIRED INPUTS] Set To Actual Values.
    private static string SentShareDisplayName = "<Name of share you're listing recipients for.>";
    private static string SenderTenantId = "<Sender Tenant ID>";
    private static string SenderPurviewAccountName = "<Name of the Microsoft Purview account>";

    private static string SenderStorageResourceId = "<Sender Storage Account Resource Id>";

    // Set if using Service principal to list recipients
    private static bool UseServiceTokenCredentials = false;
    private static string SenderClientId = "<Sender Application (Client) Id>";
    private static string SenderClientSecret = "<Sender Application (Client) Secret>";

    // General Configs
    private static string SenderPurviewEndPoint = $"https://{SenderPurviewAccountName}.purview.azure.com";
    private static string SenderShareEndPoint = $"{SenderPurviewEndPoint}/share";

    private static async Task Main(string[] args)
    {
        try
        {
            TokenCredential senderCredentials = UseServiceTokenCredentials
                ? new ClientSecretCredential(SenderTenantId, SenderClientId, SenderClientSecret)
                : new DefaultAzureCredential(new DefaultAzureCredentialOptions { AuthorityHost = new Uri("https://login.windows.net"), TenantId = SenderTenantId });

            SentSharesClient? sentSharesClient = new SentSharesClient(SenderShareEndPoint, senderCredentials);

            var allSentShares = await sentSharesClient.GetAllSentSharesAsync(SenderStorageResourceId).ToResultList();
            var mySentShare = allSentShares.First(sentShareDoc =>
            {
                var doc = JsonDocument.Parse(sentShareDoc).RootElement;
                var props = doc.GetProperty("properties");
                return props.GetProperty("displayName").ToString() == SentShareDisplayName;
            });

            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("My Sent Share Id: " + JsonDocument.Parse(mySentShare).RootElement.GetProperty("id").ToString());
            Console.ForegroundColor = Console.ForegroundColor;

            var SentShareId = JsonDocument.Parse(mySentShare).RootElement.GetProperty("id").ToString();

            var allRecipients = await sentSharesClient.GetAllSentShareInvitationsAsync(SentShareId).ToResultList();
            Console.WriteLine(allRecipients);

        }
        catch (Exception ex)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(ex);
            Console.ForegroundColor = Console.ForegroundColor;
        }
    }

    public static async Task<List<T>> ToResultList<T>(this AsyncPageable<T> asyncPageable)
    {
        List<T> list = new List<T>();

        await foreach (T item in asyncPageable)
        {
            list.Add(item);
        }

        return list;
    }
}
```

## Delete recipient

This script removes a share invitation, and therefore the share, for a recipient. To use it, be sure to fill out these variables:

- **SenderTenantId** - the Azure Tenant ID for the share sender's identity.
- **SenderPurviewAccountName** - the name of the Microsoft Purview account where the data was sent from.
- **SentShareDisplayName** - the name of the sent share you're removing a recipient for.
- **SenderStorageResourceId** - the [resource ID for the storage account](/en-us/azure/storage/common/storage-account-get-info#get-the-resource-id-for-a-storage-account) where the data will be sent from.
- **RecipientUserEmailId** - Email address for the user you want to delete.
- **UseServiceTokenCredentials** - (optional) If you want to use a service principal to create the shares, set this to **true**.
- **SenderClientId** - (optional) If using a service principal to create the shares, this is the Application (client) ID for the service principal.
- **SenderClientSecret** - (optional) If using a service principal to create the shares, add your client secret/authentication key.
- **SenderPurviewEndPoint** - If you're using If you're using the [classic Microsoft purview experience](../use-microsoft-purview-governance-portal), use `$"https://{SenderPurviewAccountName}.purview.azure.com"`; If you're using the [new Microsoft Purview experience](../purview-portal), use `https://api.purview-service.microsoft.com/`

```C
using Azure;
using Azure.Analytics.Purview.Sharing;
using Azure.Core;
using Azure.Identity;
using System.Text.Json;

public static class PurviewDataSharingQuickStart
{
    // [REQUIRED INPUTS] Set To Actual Values.
    private static string SentShareDisplayName = "<Name of share you're removing a recipient for.>";
    private static string SenderTenantId = "<Sender Tenant ID>";
    private static string SenderPurviewAccountName = "<Name of the Microsoft Purview account>";
    private static string RecipientUserEmailId = "<Target User's Email Id>";

    private static string SenderStorageResourceId = "<Sender Storage Account Resource Id>";

    // Set if using Service principal to delete recipients
    private static bool UseServiceTokenCredentials = false;
    private static string SenderClientId = "<Sender Application (Client) Id>";
    private static string SenderClientSecret = "<Sender Application (Client) Secret>";

    // General Configs
    private static string SenderPurviewEndPoint = $"https://{SenderPurviewAccountName}.purview.azure.com";
    private static string SenderShareEndPoint = $"{SenderPurviewEndPoint}/share";

    private static async Task Main(string[] args)
    {
        try
        {
            TokenCredential senderCredentials = UseServiceTokenCredentials
                ? new ClientSecretCredential(SenderTenantId, SenderClientId, SenderClientSecret)
                : new DefaultAzureCredential(new DefaultAzureCredentialOptions { AuthorityHost = new Uri("https://login.windows.net"), TenantId = SenderTenantId });

            SentSharesClient? sentSharesClient = new SentSharesClient(SenderShareEndPoint, senderCredentials);

            var allSentShares = await sentSharesClient.GetAllSentSharesAsync(SenderStorageResourceId).ToResultList();

            var mySentShare = allSentShares.First(sentShareDoc =>
            {
                var doc = JsonDocument.Parse(sentShareDoc).RootElement;
                var props = doc.GetProperty("properties");
                return props.GetProperty("displayName").ToString() == SentShareDisplayName;
            });

            var SentShareId = JsonDocument.Parse(mySentShare).RootElement.GetProperty("id").ToString();

            var allRecipients = await sentSharesClient.GetAllSentShareInvitationsAsync(SentShareId).ToResultList();

            var recipient = allRecipients.First(recipient =>
            {
                var doc = JsonDocument.Parse(recipient).RootElement;
                var props = doc.GetProperty("properties");
                return props.TryGetProperty("targetEmail", out JsonElement rcpt) && rcpt.ToString() == RecipientUserEmailId;
            });

            var recipientId = JsonDocument.Parse(recipient).RootElement.GetProperty("id").ToString();

            await sentSharesClient.DeleteSentShareInvitationAsync(WaitUntil.Completed, SentShareId, recipientId);

            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("Remove Id: " + JsonDocument.Parse(recipient).RootElement.GetProperty("id").ToString());
            Console.WriteLine("Complete");
            Console.ForegroundColor = Console.ForegroundColor;

        }

        catch (Exception ex)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(ex);
            Console.ForegroundColor = Console.ForegroundColor;
        }
    }

    public static async Task<List<T>> ToResultList<T>(this AsyncPageable<T> asyncPageable)
    {
        List<T> list = new List<T>();

        await foreach (T item in asyncPageable)
        {
            list.Add(item);
        }

        return list;
    }
}
```

## Delete sent share

This script deletes a sent share. To use it, be sure to fill out these variables:

- **SenderTenantId** - the Azure Tenant ID for the share sender's identity.
- **SenderPurviewAccountName** - the name of the Microsoft Purview account where the data was sent from.
- **SentShareDisplayName** - the name of the sent share you're listing recipients for.
- **SenderStorageResourceId** - the [resource ID for the storage account](/en-us/azure/storage/common/storage-account-get-info#get-the-resource-id-for-a-storage-account) where the data will be sent from.
- **UseServiceTokenCredentials** - (optional) If you want to use a service principal to create the shares, set this to **true**.
- **SenderClientId** - (optional) If using a service principal to create the shares, this is the Application (client) ID for the service principal.
- **SenderClientSecret** - (optional) If using a service principal to create the shares, add your client secret/authentication key.
- **SenderPurviewEndPoint** - If you're using If you're using the [classic Microsoft purview experience](../use-microsoft-purview-governance-portal), use `$"https://{SenderPurviewAccountName}.purview.azure.com"`; If you're using the [new Microsoft Purview experience](../purview-portal), use `https://api.purview-service.microsoft.com/`

```C
using Azure;
using Azure.Analytics.Purview.Sharing;
using Azure.Core;
using Azure.Identity;
using System.Text.Json;

public static class PurviewDataSharingQuickStart
{
    // [REQUIRED INPUTS] Set To Actual Values.
    private static string SenderTenantId = "<Sender Tenant ID>";
    private static string SenderPurviewAccountName = "<Name of the Microsoft Purview account>";
    private static string SentShareDisplayName = "<Name of share you're removing.>";

    private static string SenderStorageResourceId = "<Sender Storage Account Resource Id>";

    // Set if using Service principal to delete share
    private static bool UseServiceTokenCredentials = false;
    private static string SenderClientId = "<Sender Application (Client) Id>";
    private static string SenderClientSecret = "<Sender Application (Client) Secret>";

    // General Configs
    private static string SenderPurviewEndPoint = $"https://{SenderPurviewAccountName}.purview.azure.com";
    private static string SenderShareEndPoint = $"{SenderPurviewEndPoint}/share";

    private static async Task Main(string[] args)
    {
        try
        {
            TokenCredential senderCredentials = UseServiceTokenCredentials
                ? new ClientSecretCredential(SenderTenantId, SenderClientId, SenderClientSecret)
                : new DefaultAzureCredential(new DefaultAzureCredentialOptions { AuthorityHost = new Uri("https://login.windows.net"), TenantId = SenderTenantId });

            SentSharesClient? sentSharesClient = new SentSharesClient(SenderShareEndPoint, senderCredentials);

            var allSentShares = await sentSharesClient.GetAllSentSharesAsync(SenderStorageResourceId).ToResultList();

            var mySentShare = allSentShares.First(sentShareDoc =>
            {
                var doc = JsonDocument.Parse(sentShareDoc).RootElement;
                var props = doc.GetProperty("properties");
                return props.GetProperty("displayName").ToString() == SentShareDisplayName;
            });

            var SentShareId = JsonDocument.Parse(mySentShare).RootElement.GetProperty("id").ToString();

            await sentSharesClient.DeleteSentShareAsync(WaitUntil.Completed, SentShareId);

            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("Remove Id: " + SentShareId);
            Console.WriteLine("Complete");
            Console.ForegroundColor = Console.ForegroundColor;

        }
        catch (Exception ex)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(ex);
            Console.ForegroundColor = Console.ForegroundColor;
        }
    }

    public static async Task<List<T>> ToResultList<T>(this AsyncPageable<T> asyncPageable)
    {
        List<T> list = new List<T>();

        await foreach (T item in asyncPageable)
        {
            list.Add(item);
        }

        return list;
    }
}
```

## Create a received share

This script allows you to receive a data share. To use it, be sure to fill out these variables:

- **ReceiverTenantId** - the Azure Tenant ID for the user/service that is receiving the shared data.
- **ReceiverPurviewAccountName** - the name of the Microsoft Purview account where the data will be received.
- **ReceiverStorageKind** - either BlobAccount or AdlsGen2Account.
- **ReceiverStorageResourceId** - the [resource ID for the storage account](/en-us/azure/storage/common/storage-account-get-info#get-the-resource-id-for-a-storage-account) where the data will be received.
- **ReceiverStorageContainer** - the name of the container where the shared data will be stored.
- **ReceiverTargetFolderName** - the folder path to where the shared data will be stored.
- **ReceiverTargetMountPath** - the mount path you'd like to use to store your data in the folder.
- **UseServiceTokenCredentials** - (optional) If you want to use a service principal to receive the shares, set this to **true**.
- **ReceiverClientId** - (optional) If using a service principal to receive the shares, this is the Application (client) ID for the service principal.
- **ReceiverClientSecret** - (optional) If using a service principal to receive the shares, add your client secret/authentication key.
- **ReceivedShareId** - (optional) This option must be a GUID, and the current value will generate one for you, but you can replace it with a different value if you would like.
- **ReceiverVisiblePath** - (optional) Name you want to use for the path for your received share.
- **ReceivedShareDisplayName** - (optional) A display name for your received share.
- **ReceiverPurviewEndPoint** - If you're using If you're using the [classic Microsoft purview experience](../use-microsoft-purview-governance-portal), use `$"https://{ReceiverPurviewAccountName}.purview.azure.com"`; If you're using the [new Microsoft Purview experience](../purview-portal), use `https://api.purview-service.microsoft.com/`

```C
using Azure;
using Azure.Analytics.Purview.Sharing;
using Azure.Core;
using Azure.Identity;
using System.ComponentModel;
using System.Text.Json;

public static class PurviewDataSharingQuickStart
{
    // [REQUIRED INPUTS] Set To Actual Values.
    private static string ReceiverTenantId = "<Receiver Indentity's Tenant ID>";
    private static string ReceiverPurviewAccountName = "<Receiver Purview Account Name>";

    private static string ReceiverStorageKind = "<Receiver Storage Account Kind (BlobAccount / AdlsGen2Account)>";
    private static string ReceiverStorageResourceId = "<Receiver Storage Account Resource Id>";
    private static string ReceiverStorageContainer = "<Container Name To Receive Data Under>";
    private static string ReceiverTargetFolderName = "<Folder Name to Received Data Under>";
    private static string ReceiverTargetMountPath = "<Mount Path to store Received Data Under>";

    //Use if using a service principal to receive a share
    private static bool UseServiceTokenCredentials = false;
    private static string ReceiverClientId = "<Receiver Caller Application (Client) Id>";
    private static string ReceiverClientSecret = "<Receiver Caller Application (Client) Secret>";

    // [OPTIONAL INPUTS] Override Values If Desired.
    private static string ReceivedShareId = Guid.NewGuid().ToString();
    private static string ReceiverVisiblePath = "ReceivedSharePath";

    private static string ReceivedShareDisplayName = "ReceivedShare";

    // General Configs
    private static string ReceiverPurviewEndPoint = $"https://{ReceiverPurviewAccountName}.purview.azure.com";
    private static string ReceiverShareEndPoint = $"{ReceiverPurviewEndPoint}/share";

    private static async Task Main(string[] args)
    {
        try
        {

            Console.WriteLine($"{DateTime.Now.ToShortTimeString()}: CreateReceivedShare - START");
            await Receiver_CreateReceivedShare();
            Console.WriteLine($"{DateTime.Now.ToShortTimeString()}: CreateReceivedShare - FINISH");
        }
        catch (Exception ex)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(ex);
            Console.ForegroundColor = Console.ForegroundColor;
        }
    }

    private static async Task<BinaryData> Receiver_CreateReceivedShare()
    {

        TokenCredential receiverCredentials = UseServiceTokenCredentials
            ? new ClientSecretCredential(ReceiverTenantId, ReceiverClientId, ReceiverClientSecret)
            : new DefaultAzureCredential(new DefaultAzureCredentialOptions { AuthorityHost = new Uri("https://login.windows.net"), TenantId = ReceiverTenantId });

        ReceivedSharesClient? receivedSharesClient = new ReceivedSharesClient(ReceiverShareEndPoint, receiverCredentials);

        if (receivedSharesClient == null)
        {
            throw new InvalidEnumArgumentException("Invalid Received Shares Client.");
        }

        var results = await receivedSharesClient.GetAllDetachedReceivedSharesAsync().ToResultList();
        var detachedReceivedShare = results;

        if (detachedReceivedShare == null)
        {
            throw new InvalidOperationException("No received shares found.");
        }

        var myReceivedShare = detachedReceivedShare.First(recShareDoc =>
        {
            var doc = JsonDocument.Parse(recShareDoc).RootElement;
            var props = doc.GetProperty("properties");
            return props.GetProperty("displayName").ToString() == ReceivedShareDisplayName;
        });

        var ReceivedShareId = JsonDocument.Parse(myReceivedShare).RootElement.GetProperty("id").ToString();

        var attachedReceivedShareData = new
        {
            shareKind = "InPlace",
            properties = new
            {
                displayName = ReceivedShareDisplayName,
                sink = new
                {
                    storeKind = ReceiverStorageKind,
                    properties = new
                    {
                        containerName = ReceiverStorageContainer,
                        folder = ReceiverTargetFolderName,
                        mountPath = ReceiverTargetMountPath
                    },
                    storeReference = new
                    {
                        referenceName = ReceiverStorageResourceId,
                        type = "ArmResourceReference"
                    }
                }
            }
        };

        var receivedShare = await receivedSharesClient.CreateOrReplaceReceivedShareAsync(WaitUntil.Completed, ReceivedShareId, RequestContent.Create(attachedReceivedShareData));

        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine(receivedShare.Value);
        Console.ForegroundColor = Console.ForegroundColor;

        return receivedShare.Value;
    }

    public static async Task<List<T>> ToResultList<T>(this AsyncPageable<T> asyncPageable)
    {
        List<T> list = new List<T>();

        await foreach (T item in asyncPageable)
        {
            list.Add(item);
        }

        return list;
    }
}
```

## List all received shares

This script lists all received shares on a storage account. To use it, be sure to fill out these variables:

- **ReceiverTenantId** - the Azure Tenant ID for the user/service that is receiving the shared data.
- **ReceiverPurviewAccountName** - the name of the Microsoft Purview account where the data was received.
- **ReceiverStorageResourceId** - the [resource ID for the storage account](/en-us/azure/storage/common/storage-account-get-info#get-the-resource-id-for-a-storage-account) where the data has been shared.
- **UseServiceTokenCredentials** - (optional) If you want to use a service principal to receive the shares, set this to **true**.
- **ReceiverClientId** - (optional) If using a service principal to receive the shares, this is the Application (client) ID for the service principal.
- **ReceiverClientSecret** - (optional) If using a service principal to receive the shares, add your client secret/authentication key.
- **ReceiverPurviewEndPoint** - If you're using If you're using the [classic Microsoft purview experience](../use-microsoft-purview-governance-portal), use `$"https://{ReceiverPurviewAccountName}.purview.azure.com"`; If you're using the [new Microsoft Purview experience](../purview-portal), use `https://api.purview-service.microsoft.com/`

```C
using Azure;
using Azure.Analytics.Purview.Sharing;
using Azure.Core;
using Azure.Identity;

public static class PurviewDataSharingQuickStart
{
    // [REQUIRED INPUTS] Set To Actual Values.
    private static string ReceiverTenantId = "<Receiver Indentity's Tenant ID>";
    private static string ReceiverPurviewAccountName = "<Receiver Purview Account Name>";

    private static string ReceiverStorageResourceId = "<Storage Account Resource Id that is housing shares>";

    //Use if using a service principal to list shares
    private static bool UseServiceTokenCredentials = false;
    private static string ReceiverClientId = "<Receiver Caller Application (Client) Id>";
    private static string ReceiverClientSecret = "<Receiver Caller Application (Client) Secret>";

    // General Configs
    private static string ReceiverPurviewEndPoint = $"https://{ReceiverPurviewAccountName}.purview.azure.com";
    private static string ReceiverShareEndPoint = $"{ReceiverPurviewEndPoint}/share";

    private static async Task Main(string[] args)
    {
        try
        {
            TokenCredential receiverCredentials = UseServiceTokenCredentials
            ? new ClientSecretCredential(ReceiverTenantId, ReceiverClientId, ReceiverClientSecret)
            : new DefaultAzureCredential(new DefaultAzureCredentialOptions { AuthorityHost = new Uri("https://login.windows.net"), TenantId = ReceiverTenantId });

            ReceivedSharesClient? receivedSharesClient = new ReceivedSharesClient(ReceiverShareEndPoint, receiverCredentials);

            var allReceivedShares = await receivedSharesClient.GetAllAttachedReceivedSharesAsync(ReceiverStorageResourceId).ToResultList();
            Console.WriteLine(allReceivedShares);
        }
        catch (Exception ex)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(ex);
            Console.ForegroundColor = Console.ForegroundColor;
        }
    }

    public static async Task<List<T>> ToResultList<T>(this AsyncPageable<T> asyncPageable)
    {
        List<T> list = new List<T>();

        await foreach (T item in asyncPageable)
        {
            list.Add(item);
        }

        return list;
    }
}
```

## Update received share

This script allows you to update the storage location for a received share. Just like creating a received share, you add the information for the storage account where you want the data to be housed. To use it, be sure to fill out these variables:

- **ReceiverTenantId** - the Azure Tenant ID for the user/service that is receiving the shared data.
- **ReceiverPurviewAccountName** - the name of the Microsoft Purview account where the data will be received.
- **ReceiverStorageKind** - either BlobAccount or AdlsGen2Account.
- **ReceiverStorageResourceId** - the [resource ID for the storage account](/en-us/azure/storage/common/storage-account-get-info#get-the-resource-id-for-a-storage-account) where the data has been shared.
- **ReAttachStorageResourceId** - the [resource ID for the storage account](/en-us/azure/storage/common/storage-account-get-info#get-the-resource-id-for-a-storage-account) where the data will be received.
- **ReceiverStorageContainer** - the name of the container where the shared data will be stored.
- **ReceiverTargetFolderName** - the folder path to where the shared data will be stored.
- **ReceiverTargetMountPath** - the mount path you'd like to use to store your data in the folder.
- **ReceivedShareDisplayName** - The display name for your received share.
- **UseServiceTokenCredentials** - (optional) If you want to use a service principal to receive the shares, set this to **true**.
- **ReceiverClientId** - (optional) If using a service principal to receive the shares, this is the Application (client) ID for the service principal.
- **ReceiverClientSecret** - (optional) If using a service principal to receive the shares, add your client secret/authentication key.
- **ReceiverPurviewEndPoint** - If you're using If you're using the [classic Microsoft purview experience](../use-microsoft-purview-governance-portal), use `$"https://{ReceiverPurviewAccountName}.purview.azure.com"`; If you're using the [new Microsoft Purview experience](../purview-portal), use `https://api.purview-service.microsoft.com/`

```C
using Azure;
using Azure.Analytics.Purview.Sharing;
using Azure.Core;
using Azure.Identity;
using System.ComponentModel;
using System.Text.Json;

public static class PurviewDataSharingQuickStart
{
    // [REQUIRED INPUTS] Set To Actual Values.
    private static string ReceiverTenantId = "<Receiver Indentity's Tenant ID>";
    private static string ReceiverPurviewAccountName = "<Receiver Purview Account Name>";

    private static string ReceiverStorageKind = "<Receiver Storage Account Kind (BlobAccount / AdlsGen2Account)>";
    private static string ReceiverStorageResourceId = "<Storage Account Resource Id for the account where the share is currently attached.>";
    private static string ReAttachStorageResourceId = "<Storage Account Resource Id For Reattaching Received Share>";
    private static string ReceiverStorageContainer = "<Container Name To Receive Data Under>";
    private static string ReceiverTargetFolderName = "<Folder Name to Received Data Under>";
    private static string ReceiverTargetMountPath = "<Mount Path to Received Data Under>";

    private static string ReceivedShareDisplayName = "<Display name of your received share>";

    //Use if using a service principal to update the share
    private static bool UseServiceTokenCredentials = false;
    private static string ReceiverClientId = "<Receiver Caller Application (Client) Id>";
    private static string ReceiverClientSecret = "<Receiver Caller Application (Client) Secret>";

    // General Configs
    private static string ReceiverPurviewEndPoint = $"https://{ReceiverPurviewAccountName}.purview.azure.com";
    private static string ReceiverShareEndPoint = $"{ReceiverPurviewEndPoint}/share";

    private static async Task Main(string[] args)
    {
        try
        {

            Console.WriteLine($"{DateTime.Now.ToShortTimeString()}: UpdateReceivedShare - START");
            await Receiver_UpdateReceivedShare();
            Console.WriteLine($"{DateTime.Now.ToShortTimeString()}: UpdateReceivedShare - FINISH");
        }
        catch (Exception ex)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(ex);
            Console.ForegroundColor = Console.ForegroundColor;
        }
    }

    private static async Task<BinaryData> Receiver_UpdateReceivedShare()
    {

        TokenCredential receiverCredentials = UseServiceTokenCredentials
            ? new ClientSecretCredential(ReceiverTenantId, ReceiverClientId, ReceiverClientSecret)
            : new DefaultAzureCredential(new DefaultAzureCredentialOptions { AuthorityHost = new Uri("https://login.windows.net"), TenantId = ReceiverTenantId });

        ReceivedSharesClient? receivedSharesClient = new ReceivedSharesClient(ReceiverShareEndPoint, receiverCredentials);

        if (receivedSharesClient == null)
        {
            throw new InvalidEnumArgumentException("Invalid Received Shares Client.");
        }

        var attachedReceivedShareData = new
        {
            shareKind = "InPlace",
            properties = new
            {
                displayName = ReceivedShareDisplayName,
                sink = new
                {
                    storeKind = ReceiverStorageKind,
                    properties = new
                    {
                        containerName = ReceiverStorageContainer,
                        folder = ReceiverTargetFolderName,
                        mountPath = ReceiverTargetMountPath
                    },
                    storeReference = new
                    {
                        referenceName = ReAttachStorageResourceId,
                        type = "ArmResourceReference"
                    }
                }
            }
        };

        var allReceivedShares = await receivedSharesClient.GetAllAttachedReceivedSharesAsync(ReceiverStorageResourceId).ToResultList();

        var myReceivedShare = allReceivedShares.First(recShareDoc =>
        {
            var doc = JsonDocument.Parse(recShareDoc).RootElement;
            var props = doc.GetProperty("properties");
            return props.GetProperty("displayName").ToString() == ReceivedShareDisplayName;
        });

        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine("My Received Share Id: " + JsonDocument.Parse(myReceivedShare).RootElement.GetProperty("id").ToString());
        Console.ForegroundColor = Console.ForegroundColor;

        var ReceivedShareId = JsonDocument.Parse(myReceivedShare).RootElement.GetProperty("id").ToString();

        var receivedShare = await receivedSharesClient.CreateOrReplaceReceivedShareAsync(WaitUntil.Completed, ReceivedShareId, RequestContent.Create(attachedReceivedShareData));

        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine(receivedShare.Value);
        Console.ForegroundColor = Console.ForegroundColor;

        return receivedShare.Value;
    }

    public static async Task<List<T>> ToResultList<T>(this AsyncPageable<T> asyncPageable)
    {
        List<T> list = new List<T>();

        await foreach (T item in asyncPageable)
        {
            list.Add(item);
        }

        return list;
    }
}
```

## Delete received share

This script deletes a received share. To use it, be sure to fill out these variables:

- **ReceiverTenantId** - the Azure Tenant ID for the user/service that is receiving the shared data.
- **ReceiverPurviewAccountName** - the name of the Microsoft Purview account where the data will be received.
- **ReceivedShareDisplayName** - The display name for your received share.
- **ReceiverStorageResourceId** - the [resource ID for the storage account](/en-us/azure/storage/common/storage-account-get-info#get-the-resource-id-for-a-storage-account) where the data has been shared.
- **UseServiceTokenCredentials** - (optional) If you want to use a service principal to receive the shares, set this to **true**.
- **ReceiverClientId** - (optional) If using a service principal to receive the shares, this is the Application (client) ID for the service principal.
- **ReceiverClientSecret** - (optional) If using a service principal to receive the shares, add your client secret/authentication key.
- **ReceiverPurviewEndPoint** - If you're using If you're using the [classic Microsoft purview experience](../use-microsoft-purview-governance-portal), use `$"https://{ReceiverPurviewAccountName}.purview.azure.com"`; If you're using the [new Microsoft Purview experience](../purview-portal), use `https://api.purview-service.microsoft.com/`

```C
using Azure;
using Azure.Analytics.Purview.Sharing;
using Azure.Core;
using Azure.Identity;
using System.Text.Json;

public static class PurviewDataSharingQuickStart
{
    // [REQUIRED INPUTS] Set To Actual Values.
    private static string ReceiverTenantId = "<Receiver Indentity's Tenant ID>";
    private static string ReceiverPurviewAccountName = "<Receiver Purview Account Name>";

    private static string ReceivedShareDisplayName = "<Display name of your received share>";

    private static string ReceiverStorageResourceId = "<Storage Account Resource Id for the account where the share is currently attached.>";

    //Use if using a service principal to delete share.
    private static bool UseServiceTokenCredentials = false;
    private static string ReceiverClientId = "<Receiver Caller Application (Client) Id>";
    private static string ReceiverClientSecret = "<Receiver Caller Application (Client) Secret>";

    // General Configs
    private static string ReceiverPurviewEndPoint = $"https://{ReceiverPurviewAccountName}.purview.azure.com";
    private static string ReceiverShareEndPoint = $"{ReceiverPurviewEndPoint}/share";

    private static async Task Main(string[] args)
    {
        try
        {
            TokenCredential receiverCredentials = UseServiceTokenCredentials
            ? new ClientSecretCredential(ReceiverTenantId, ReceiverClientId, ReceiverClientSecret)
            : new DefaultAzureCredential(new DefaultAzureCredentialOptions { AuthorityHost = new Uri("https://login.windows.net"), TenantId = ReceiverTenantId });

            ReceivedSharesClient? receivedSharesClient = new ReceivedSharesClient(ReceiverShareEndPoint, receiverCredentials);

            var allReceivedShares = await receivedSharesClient.GetAllAttachedReceivedSharesAsync(ReceiverStorageResourceId).ToResultList();

            var myReceivedShare = allReceivedShares.First(recShareDoc =>
            {
                var doc = JsonDocument.Parse(recShareDoc).RootElement;
                var props = doc.GetProperty("properties");
                return props.GetProperty("displayName").ToString() == ReceivedShareDisplayName;
            });

            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("My Received Share Id: " + JsonDocument.Parse(myReceivedShare).RootElement.GetProperty("id").ToString());
            Console.ForegroundColor = Console.ForegroundColor;

            var ReceivedShareId = JsonDocument.Parse(myReceivedShare).RootElement.GetProperty("id").ToString();

            await receivedSharesClient.DeleteReceivedShareAsync(WaitUntil.Completed, ReceivedShareId);

            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("Delete Complete");
            Console.ForegroundColor = Console.ForegroundColor;
        }
        catch (Exception ex)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(ex);
            Console.ForegroundColor = Console.ForegroundColor;
        }
    }
    public static async Task<List<T>> ToResultList<T>(this AsyncPageable<T> asyncPageable)
    {
        List<T> list = new List<T>();

        await foreach (T item in asyncPageable)
        {
            list.Add(item);
        }

        return list;
    }
}
```

## Clean up resources

To clean up the resources created for the quick start, use the following guidelines:

1. Within Microsoft Purview portal, [delete the sent share](../how-to-share-data#delete-share).
2. Also [delete your received share](../how-to-receive-share#delete-received-share).
3. Once the shares are successfully deleted, delete the target container and folder Microsoft Purview created in your target storage account when you received shared data.