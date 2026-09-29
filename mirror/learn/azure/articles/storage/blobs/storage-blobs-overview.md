---
layout: Conceptual
title: About Blob (object) storage - Azure Storage | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-overview
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/125/azure-blob-storage/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/a8bb4a47-3525-ec11-b6e6-000d3a4f0f84
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
adobe-target: true
learn_banner_products:
- azure
manager: akashdubey
ms.reviewer: akashdubey-ms
description: Azure Blob storage stores massive amounts of unstructured object data, such as text or binary data. Blob storage also supports Azure Data Lake Storage for big data analytics.
services: storage
author: normesta
ms.service: azure-blob-storage
ms.topic: overview
ms.date: 2026-05-18T00:00:00.0000000Z
ms.author: normesta
locale: en-us
document_id: 9c46acf7-4e08-a595-e2c5-98aac7a12f71
document_version_independent_id: cf7379f9-241c-ef84-0680-c5fdbe5de827
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/storage/blobs/storage-blobs-overview.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: storage/blobs/storage-blobs-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/storage/blobs/storage-blobs-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ea957f26-244e-4bd1-9b19-105f0a0a73d6
- https://authoring-docs-microsoft.poolparty.biz/devrel/de8ce683-cbe1-461b-bae7-77db0888ec6d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/85dd85bb-c2e5-412e-96b2-f2765a3fe51c
- https://authoring-docs-microsoft.poolparty.biz/devrel/a06cf482-4ca9-4582-a142-bcf842258d42
platformId: 1ba86c9d-d598-7809-a8cb-5e0af215d7d0
---

# About Blob (object) storage - Azure Storage | Microsoft Learn

Azure Blob Storage is Microsoft's object storage solution for the cloud. Blob Storage is optimized for storing massive amounts of unstructured data. Unstructured data is data that doesn't adhere to a particular data model or definition, such as text or binary data.

## About Blob Storage

Blob Storage is designed for:

- Serving images or documents directly to a browser.
- Storing files for distributed access.
- Streaming video and audio.
- Writing to log files.
- Storing data for backup and restore, disaster recovery, and archiving.
- Storing data for analysis by an on-premises or Azure-hosted service.

Users or client applications can access objects in Blob Storage via HTTP or HTTPS from anywhere in the world. You can access objects in Blob Storage through the [Azure Storage REST API](/en-us/rest/api/storageservices/blob-service-rest-api), [Azure PowerShell](/en-us/powershell/module/az.storage), [Azure CLI](/en-us/cli/azure/storage), or an Azure Storage client library. Client libraries are available for different languages, including:

- [.NET](/en-us/dotnet/api/overview/azure/storage)
- [Java](/en-us/java/api/overview/azure/storage)
- [Node.js](https://github.com/Azure/azure-sdk-for-js/tree/master/sdk/storage)
- [Python](storage-quickstart-blobs-python)
- [Go](https://github.com/Azure/azure-sdk-for-go/tree/main/sdk/storage/azblob)

Clients can also securely connect to Blob Storage by using SSH File Transfer Protocol (SFTP) and mount Blob Storage containers by using the Network File System (NFS) 3.0 protocol.

## About Azure Data Lake Storage

Blob Storage supports Azure Data Lake Storage, Microsoft's enterprise big data analytics solution for the cloud. Azure Data Lake Storage offers a hierarchical file system as well as the advantages of Blob Storage, including:

- Low-cost, tiered storage
- High availability
- Strong consistency
- Disaster recovery capabilities

For more information about Data Lake Storage, see [Introduction to Azure Data Lake Storage](data-lake-storage-introduction).