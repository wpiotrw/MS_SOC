---
layout: Conceptual
title: Microsoft Purview Data Sharing FAQ | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-data-share-faq
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Microsoft Purview Data Sharing frequently asked questions (FAQ) and answers.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: how-to
ms.date: 2024-09-24T00:00:00.0000000Z
locale: en-us
document_id: 0ac2864a-6c31-add6-4448-70c0346bdeef
document_version_independent_id: 0ac2864a-6c31-add6-4448-70c0346bdeef
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-data-share-faq.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-data-share-faq
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-data-share-faq.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/7cf8f81d-2989-4e5d-aa91-5191d10a3323
- https://authoring-docs-microsoft.poolparty.biz/devrel/54918a83-0404-4863-9c91-715186c1f582
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/1cb9c90f-9a3f-4389-8367-0a20c542621f
- https://authoring-docs-microsoft.poolparty.biz/devrel/b26f5f7a-0913-4a95-8337-ed7543902f2d
platformId: 6edc31e8-a4e8-9538-7002-b09f04554f19
---

# Microsoft Purview Data Sharing FAQ | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Here are some frequently asked questions for Microsoft Purview Data Sharing.

## Is data sharing going to be retired?

Yes, Microsoft Purview Data Sharing will be retired in September 2025. To share data, use [Microsoft Fabric external data sharing](/en-us/fabric/governance/external-data-sharing-overview).

## Is data sharing available in the new Microsoft Purview Data Catalog?

No, data sharing is accessed through the [classic Microsoft Purview governance portal](../use-microsoft-purview-governance-portal): https://web.purview.azure.com

## What are the key terms related to data sharing?

- **Data Provider** - Organization that shares data.
- **Data Consumer** - Organization that receives shared data from a data provider.
- **Asset** - For storage in-place sharing, an asset is a storage account, and the list of files and folders you want to share from the storage account.
- **Share** - A share is a set of data that can be shared from provider to consumer. It's a set of assets. You can have one asset with files/folders from one storage account, and another asset with files/folders from a different storage account.
- **Collection** - A [collection](../data-gov-classic-permissions) is a tool Microsoft Purview uses to group assets, sources, shares, and other artifacts into a hierarchy for discoverability and to manage access control. A root collection is created automatically when you create your Microsoft Purview account and you're granted all the roles to the root collection. You can use the root collection (default) or create child collections for data sharing.
- **Recipient** - A recipient is a user or service principal to which the share is sent.

## Can I use the API or SDK for storage in-place sharing?

Yes, you can use [REST API](/en-us/rest/api/purview/) or [.NET SDK](/en-us/dotnet/api/overview/azure/purview) for programmatic experience to share data.

We have a [guide for getting started with the .NET SDK](../quickstart-data-share-dotnet).

## What are the roles and permissions required to share data or receive shares?

| **Operations** | **Roles and Permissions** |
| --- | --- |
| **Data provider**: create share, add asset and recipients, revoke access | **Microsoft Purview collection role**: minimum of Data Reader to use the Microsoft Purview portal experience, none to use API or SDK |
|  | **Storage account role** checked when adding and updating asset: Owner or Storage Blob Data Owner |
|  | **Storage account permissions** checked when adding and updating asset: Microsoft.Authorization/roleAssignments/write OR Microsoft.Storage/storageAccounts/blobServices/containers/blobs/modifyPermissions/ |
| **Data consumer**: Receive share, attach share, delete share | **Microsoft Purview collection role**: minimum of Data Reader to use the Microsoft Purview portal experience, none to use API or SDK |
|  | **Storage account role** checked when attaching share: Contributor OR Owner OR Storage Blob Data Contributor OR Storage Blob Data Owner |
|  | **Storage account permissions** checked when attaching share: Microsoft.Storage/storageAccounts/write OR Microsoft.Storage/storageAccounts/blobServices/containers/write |
| **Data consumer**: Access shared data | No share-specific role required. You can access shared data with regular storage account permission just like any other data. Data consumer's ability to apply ACLs for shared data is currently not supported. |

## How can I share data from containers?

When adding assets, you can select the container(s) that you would like to share.

## Can I share data in-place with storage account in a different Azure region?

Cross-region in-place data sharing isn't currently supported for storage account. Data provider and data consumer's storage accounts need to be in the same Azure region.

## Is there support for read-write shares?

Storage in-place sharing supports read-only shares. Data consumer can't write to the shared data.

To share data back to the data provider, the data consumer can create a share and share with the data provider.

## Can I access shared data from analytics tools like Azure Synapse?

You can access shared data from storage clients like Azure Synapse Analytics Spark and Databricks. You won't be able to access shared data using Azure Data Factory, Power BI, or AzCopy.

## Does the recipient of the share need to be a user's email address or can I share data with an application?

Through the UI, you can share data with recipient's Azure sign-in email or using service principal's object ID and tenant ID.

[Through API and SDK, you also send invitation to object ID of a user principal or service principal](../quickstart-data-share-dotnet#send-invitation-to-a-service). Also, you can optionally specify a tenant ID that you want the share to be received into.

## Is the recipient accepting the share only for themselves?

When the recipient attaches the share to a target storage account, any user or application that has access to the target storage account will be able to access shared data.

## If the recipient leaves the organization, what happens to the received share?

Once the received share is accepted and attached to a target storage account, any users with appropriate permissions to the target storage account can continue to access the shared data even after the recipient has left the organization.

Once the received share is accepted, any user with data reader permission to the Microsoft Purview collection that the share is received into can view and update the received share.

## How do I request an increase in limits for the number of shares?

Data provider's source storage account can support up to 20 targets, and data consumer's target storage account can support up to 100 sources. To request a limit increase, [contact support](https://azure.microsoft.com/support/create-ticket/).

## How do I troubleshoot data sharing issues?

To troubleshoot issues with sharing data, refer to the [troubleshooting section of the how to share data article](../how-to-share-data#troubleshoot). To troubleshoot issues with receiving share, refer to the [troubleshooting section of the how to receive share article](../how-to-receive-share#troubleshoot).

## Is there support for Private endpoints, VNET and IP restrictions?

Private endpoints, VNET, and IP restrictions are supported for data share for storage. Blob should be chosen as the target subresource when creating a private endpoint for storage accounts.