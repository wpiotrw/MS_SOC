---
layout: Conceptual
title: Azure Storage in-place data sharing with Microsoft Purview (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/concept-data-share
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article describes Microsoft Purview Data Sharing and its features.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: concept-article
ms.date: 2024-09-24T00:00:00.0000000Z
locale: en-us
document_id: 41d4fc92-964a-99a1-aeb4-b0bcc633a69c
document_version_independent_id: 41d4fc92-964a-99a1-aeb4-b0bcc633a69c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/concept-data-share.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/concept-data-share
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/concept-data-share.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/7cf8f81d-2989-4e5d-aa91-5191d10a3323
- https://authoring-docs-microsoft.poolparty.biz/devrel/54918a83-0404-4863-9c91-715186c1f582
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/1cb9c90f-9a3f-4389-8367-0a20c542621f
- https://authoring-docs-microsoft.poolparty.biz/devrel/b26f5f7a-0913-4a95-8337-ed7543902f2d
platformId: 8693093c-f338-cfbd-f818-609a60017710
---

# Azure Storage in-place data sharing with Microsoft Purview (preview) | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently being retired, with support provided until September 2025 to allow for migration to [Microsoft Fabric external data sharing](/en-us/fabric/governance/external-data-sharing-overview).

Traditionally, organizations have shared data with internal teams or external partners by generating data feeds, requiring investment in data copy and refresh pipelines. The result is higher cost for data storage and movement, data proliferation (that is, multiple copies of data), and delay in access to time-sensitive data.

With Microsoft Purview Data Sharing, data providers can now share data **in-place** from Azure Data Lake Storage Gen2 and Azure Storage accounts, both within and across organizations. Share data directly with users and partners without data duplication and centrally manage your sharing activities from within Microsoft Purview.

With Microsoft Purview Data Sharing, data consumers can now have near real-time access to shared data. Storage data access and transactions are charged to the data consumers based on what they use, and at no more cost to the data providers.

## Get started

Get started with Microsoft Purview in-place data sharing for Azure Storage by reviewing the next steps or following the [Data Sharing Quickstart](../quickstart-data-share).

Important

Data sharing is accessed through the [classic Microsoft Purview governance portal](../use-microsoft-purview-governance-portal): https://web.purview.azure.com

## Available sources

| Supported data store | Data Sharing |
| --- | --- |
| [Azure Blob Storage](../register-scan-azure-blob-storage-source) | [Yes](../register-scan-azure-blob-storage-source#data-sharing) |
| [Azure Data Lake Storage Gen2](../register-scan-adls-gen2) | [Yes](../register-scan-adls-gen2#data-sharing) |

## How in-place data sharing works

Microsoft Purview enables sharing of files and folders in-place from ADLS Gen2 and Blob storage accounts.

![Flow chart showing a data provider with a source store sharing an invitation to a data consumer with a target store. Connecting the source store and target store is an arrow labeled in-place access that points from the target to the source.](../media/concept-data-share/data-share-flow.png)

A data provider creates a share by selecting a data source that is registered in Microsoft Purview, choosing which files and folders to share, and who to share them with. Microsoft Purview then sends an invitation to each data consumer.

When a consumer accepts the invitation, they specify a target storage account in their own Azure subscription that they'll use to access the shared data. This establishes a sharing relationship between the provider and consumer storage accounts. This sharing relationship provides data consumer read-only access to shared data through the consumer’s storage account. Any changes to the data in the provider’s source storage account is reflected in near real-time in the consumer’s storage account.

The data provider pays for data storage and their own data access, while the data consumer pays for their own data access transactions.

Data providers can revoke access to the shared data at any time, or set a share expiration time for time-bound access to data. Data consumers can also terminate access to the share at any time.

## Where data is stored

Microsoft Purview Data Sharing only stores metadata about your share. It doesn't store a copy of the shared data itself. The data is stored in the underlying source storage account that is being shared. You can have your storage accounts in a different Azure region than your Microsoft Purview account.

## Key capabilities

- Share data within the organization or with partners and customers outside of the organization (within the same Azure tenant or across different Azure tenants).
- Share data from ADLS Gen2 or Blob storage in-place without data duplication.
- Share data with multiple recipients.
- Access shared data in near real time.
- Manage sharing relationships and keep track of who the data is shared with/from, for each ADLSGen2 or Blob Storage account.
- Terminate share access at any time.
- Flexible experience through Microsoft Purview governance portal or via REST APIs.

## Data sharing scenarios

Microsoft Purview Data Sharing can help with various data sharing scenarios, including:

- Collaborate with external business partners while maintaining data security in your own environment.
- Outsource data transformation and processing to third party ISVs or data aggregators by sharing raw data and receiving normalized data and analytics results back.
- Automate sharing of big data (for example: IoT data, scientific data, satellite and surveillance images or videos, financial market data) in near real time and without data duplication.
- Share data between different departments within the organization.

## Support

If you have any questions, please reach out to your account manager or customer support. If you have a support plan and you need technical help, create a [support request](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest).

1. For **Issue type**, select *Technical*.
2. For **Subscription**, select your subscription.
3. For **Service**, select *My services*, then select *Service type*.
4. Select the Microsoft Purview resource that you are creating a support request for.
5. For **Summary**, type a description of your issue or question.
6. For **Problem type**, select *Data Share*.
7. For **Problem subtype**, select appropriately.