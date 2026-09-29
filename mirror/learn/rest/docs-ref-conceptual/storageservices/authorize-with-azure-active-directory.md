---
layout: Conceptual
title: Authorize with Microsoft Entra ID (REST API) - Azure Storage | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/rest/api/storageservices/authorize-with-azure-active-directory
enable_rest_try_it: true
rest_product: Azure
uhfHeaderId: azure
breadcrumb_path: ../../breadcrumb/toc.json
ms.author: pauljewell
manager: smmark
author: pauljewellmsft
ms.topic: reference
ms.devlang: rest-api
ms.date: 2025-03-27T00:00:00.0000000Z
products:
- https://authoring-docs-microsoft.poolparty.biz/devrel/de8ce683-cbe1-461b-bae7-77db0888ec6d
ms.service: azure-storage
description: Azure Storage provides integration with Microsoft Entra ID for identity-based authorization of requests to the Blob, File, Queue and Table services. With Microsoft Entra ID, you can use role-based access control (RBAC) to grant access to your Azure Storage resources to users, groups, or applications.
locale: en-us
moniker_definition_rel: ../../.monikers.Azure.AzureRestApi.json
document_id: 1e3062c1-ad6c-26ef-c8f7-1852cb62c8d0
document_version_independent_id: 6ca8afae-75a2-e7f7-e3e0-f473e59ad55e
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-rest-apis/blob/live/docs-ref-conceptual/storageservices/authorize-with-azure-active-directory.md
site_name: Docs
depot_name: Azure.AzureRestApi
page_type: conceptual
toc_rel: ../azure/toc.json
feedback_system: None
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/storageservices/authorize-with-azure-active-directory
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs-ref-conceptual/storageservices/authorize-with-azure-active-directory.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/de8ce683-cbe1-461b-bae7-77db0888ec6d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/a06cf482-4ca9-4582-a142-bcf842258d42
platformId: a0544483-f6e6-cf49-3601-cbac70d2f6be
---

# Authorize with Microsoft Entra ID (REST API) - Azure Storage | Microsoft Learn

Azure Storage provides integration with [Microsoft Entra ID](/en-us/azure/active-directory/fundamentals/active-directory-whatis) for identity-based authorization of requests to the Blob, File, Queue and Table services. With Microsoft Entra ID, you can use role-based access control (RBAC) to grant access to blob, file, queue and table resources to users, groups, or applications. You can grant permissions that are scoped to the level of an individual container, share, queue or table.

To learn more about Microsoft Entra ID integration in Azure Storage, see [Authorize access to Azure blobs and queues using Microsoft Entra ID](/en-us/azure/storage/common/storage-auth-aad).

For more information on the advantages of using Microsoft Entra ID in your application, see [Integrating with the Microsoft identity platform](/en-us/azure/active-directory/develop/active-directory-how-to-integrate).

Important

For optimal security, Microsoft recommends using Microsoft Entra ID with managed identities to authorize requests against blob, queue, and table data, whenever possible. Authorization with Microsoft Entra ID and managed identities provides superior security and ease of use over Shared Key authorization. To learn more about managed identities, see [What are managed identities for Azure resources](/en-us/entra/identity/managed-identities-azure-resources/overview).

For resources hosted outside of Azure, such as on-premises applications, you can use managed identities through Azure Arc. For example, apps running on Azure Arc-enabled servers can use managed identities to connect to Azure services. To learn more, see [Authenticate against Azure resources with Azure Arc-enabled servers](/en-us/azure/azure-arc/servers/managed-identity-authentication).

For scenarios where shared access signatures (SAS) are used, Microsoft recommends using a user delegation SAS. A user delegation SAS is secured with Microsoft Entra credentials instead of the account key. To learn about shared access signatures, see [Create a user delegation SAS](create-user-delegation-sas).

## Use OAuth access tokens for authentication

Azure Storage accepts [OAuth 2.0](/en-us/azure/active-directory/develop/active-directory-v2-protocols) access tokens from the Microsoft Entra tenant associated with the subscription that contains the storage account. Azure Storage accepts access tokens for:

- Users and groups
- Service principals
- Managed identities for Azure resources
- Applications using permissions delegated by users

Azure Storage exposes a single delegation scope named `user_impersonation` that permits applications to take any action allowed by the user.

To request tokens for Azure Storage, specify the value `https://storage.azure.com/` for the resource ID. For more information about the resource ID, see [Microsoft identity platform scopes, permissions, & consent](/en-us/azure/active-directory/develop/v2-permissions-and-consent).

For more information on requesting access tokens from Microsoft Entra ID for users and service principals, see [Authentication flows and application scenarios](/en-us/azure/active-directory/develop/authentication-flows-app-scenarios).

For more information about requesting access tokens for resources configured with managed identities, see [How to use managed identities for Azure resources on an Azure VM to acquire an access token](/en-us/azure/active-directory/managed-service-identity/how-to-use-vm-token).

## Call storage operations with OAuth tokens

To call Blob, File, Queue and Table service operations using OAuth access tokens, pass the access token in the **Authorization** header using the **Bearer** scheme, and specify a service version of 2017-11-09 (2022-11-02 for operations on [File](operations-on-files) resource and [Directory](operations-on-directories) resource or 2024-11-04 for operations on [FileService](operations-on-the-account--file-service-) resource and [FileShare](operations-on-shares--file-service-) resource) or higher, as shown in the following example:

```http
Request:
GET /container/file.txt
x-ms-version: 2017-11-09
Authorization: Bearer eyJ0eXAiO...V09ccgQ
User-Agent: PostmanRuntime/7.6.0
Accept: */*
Host: sampleoautheast2.blob.core.windows.net
accept-encoding: gzip, deflate

Response:
HTTP/1.1 200
status: 200
Content-Length: 28
Content-Type: text/plain
Content-MD5: dxG7IgOBzApXPcGHxGg5SA==
Last-Modified: Wed, 30 Jan 2019 07:21:32 GMT
Accept-Ranges: bytes
ETag: "0x8D686838F9E8BA7"
Server: Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id: 09f31964-e01e-00a3-8066-d4e6c2000000
x-ms-version: 2017-11-09
x-ms-creation-time: Wed, 29 Aug 2018 04:22:47 GMT
x-ms-lease-status: unlocked
x-ms-lease-state: available
x-ms-blob-type: BlockBlob
x-ms-server-encrypted: true
Date: Wed, 06 Mar 2019 21:50:50 GMT
Welcome to Azure Storage!!
```

## Bearer Challenge

Bearer challenge is part of the OAuth protocol [RFC 6750](https://www.rfc-editor.org/rfc/rfc6750.txt) and is used for authority discovery. For anonymous requests to the Blob service, or for requests made with an invalid OAuth bearer token, the server will return status code 401 (Unauthorized) with identity provider and resource information. Refer to [link](/en-us/azure/storage/common/storage-auth-aad-app?toc=/azure/storage/blobs/toc.json#well-known-values-for-authentication-with-azure-ad) for how to use these values during authentication with Microsoft Entra ID.

> 
> Azure Storage Blob and Queue services return a bearer challenge for version 2019-12-12 and newer. Azure Storage Table service returns a bearer challenge for version 2020-12-06 and newer. Azure Data Lake Storage Gen2 returns a bearer challenge for version 2017-11-09 and newer. Azure File service returns a bearer challenge from version 2022-11-02 and newer.

### Responses to anonymous read requests

When Blob Storage receives an anonymous request, that request will succeed if all of the following conditions are true:

- Anonymous public access is allowed for the storage account.
- The container is configured to allow anonymous public access.
- The request is for read access.

If any of those conditions are not true, then the request will fail. The response code on failure depends on whether the anonymous request was made with a version of the service that supports the bearer challenge. The bearer challenge is supported with service versions 2019-12-12 and newer:

- If the anonymous request was made with a service version that supports the bearer challenge, then the service returns error code 401 (Unauthorized).
- If the anonymous request was made with a service version that does not support the bearer challenge and anonymous public access is disallowed for the storage account, then the service returns error code 409 (Conflict).
- If the anonymous request was made with a service version that does not support the bearer challenge and anonymous public access is allowed for the storage account, then the service returns error code 404 (Not Found).

For more information about the bearer challenge, see [Bearer challenge](/en-us/rest/api/storageservices/authorize-with-azure-active-directory#bearer-challenge).

### Sample response to bearer challenge

The following is an example of a bearer challenge response when the client request does not include the bearer token in the anonymous download blob request:

```http
Request:
GET /container/file.txt
x-ms-version: 2019-12-12
Host: sampleoautheast2.blob.core.windows.net

Response:
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Bearer authorization_uri=https://login.microsoftonline.com/<tenant_id>/oauth2/authorize resource_id=https://storage.azure.com

<?xml version="1.0" encoding="utf-8"?>
<Error>
    <Code>NoAuthenticationInformation</Code>
    <Message>Server failed to authenticate the request. Please refer to the information in the www-authenticate header.
RequestId:ec4f02d7-1003-0006-21f9-c55bc8000000
Time:2020-01-08T08:01:46.2063459Z</Message>
</Error>
```

| Parameter | Description |
| --- | --- |
| authorization\_uri | The URI (physical endpoint) of the authorization server. This value is also used as a lookup key to get more information about the server from a discovery endpoint. The client must validate that the authorization server is trusted. When the resource is protected by Microsoft Entra ID, it is sufficient to verify that the URL begins with `https://login.microsoftonline.com` or other hostname that Microsoft Entra ID supports. A tenant-specific resource should always return a tenant-specific authorization URI. |
| resource\_id | Returns the unique identifier of the resource. The client application can use this identifier as the value of the resource parameter when it requests an access token for the resource. It is important for the client application to verify this value, otherwise a malicious service might be able to induce an elevation-of-privileges attack. The recommended strategy for preventing an attack is to verify that the resource\_id matches the base of the web API URL that being accessed. The Azure Storage resource ID is `https://storage.azure.com`. |

## Manage access rights with RBAC

Microsoft Entra ID handles the authorization of access to secured resources through RBAC. Using RBAC, you can assign roles to users, groups, or service principals. Each role encompasses a set of permissions for a resource. Once the role is assigned to the user, group, or service principal, they have access to that resource. You can assign access rights using the Azure portal, Azure command-line tools, and Azure Management APIs. For more information on RBAC, see [Get started with Role-Based Access Control](/en-us/azure/role-based-access-control/overview).

For Azure Storage, you can grant access to data in a container or queue in the storage account. Azure Storage offers these built-in RBAC roles for use with Microsoft Entra ID:

- [Storage Blob Data Owner](/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-owner)
- [Storage Blob Data Contributor](/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor)
- [Storage Blob Data Reader](/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-reader)
- [Storage Blob Delegator](/en-us/azure/role-based-access-control/built-in-roles#storage-blob-delegator)
- [Storage Queue Data Contributor](/en-us/azure/role-based-access-control/built-in-roles#storage-queue-data-contributor)
- [Storage Queue Data Reader](/en-us/azure/role-based-access-control/built-in-roles#storage-queue-data-reader)
- [Storage Queue Data Message Processor](/en-us/azure/role-based-access-control/built-in-roles#storage-queue-data-message-processor)
- [Storage Queue Data Message Sender](/en-us/azure/role-based-access-control/built-in-roles#storage-queue-data-message-sender)
- [Storage Table Data Reader](/en-us/azure/role-based-access-control/built-in-roles)
- [Storage Table Data Contributor](/en-us/azure/role-based-access-control/built-in-roles)
- [Storage File Data Privileged Contributor](/en-us/azure/role-based-access-control/built-in-roles#storage-file-data-privileged-contributor)
- [Storage File Data Privileged Reader](/en-us/azure/role-based-access-control/built-in-roles/storage#storage-file-data-privileged-reader)

For more information about how built-in roles are defined for Azure Storage, see [Understand role definitions for Azure resources](/en-us/azure/role-based-access-control/role-definitions).

You can also define custom roles for use with Blob storage and Azure Queues. For more information, see [Create custom roles for Azure Role-Based Access Control](/en-us/azure/role-based-access-control/custom-roles).

## Permissions for calling data operations

The following tables describe the permissions necessary for a Microsoft Entra user, group, managed identity, or service principal to call specific Azure Storage operations. To enable a client to call a particular operation, ensure that the client's assigned RBAC role offers sufficient permissions for that operation.

### Permissions for Blob service operations

| Blob service operation | RBAC action |
| --- | --- |
| [List Containers](list-containers2) | Microsoft.Storage/storageAccounts/blobServices/containers/read (scoped to the storage account or above) |
| [Set Blob Service Properties](set-blob-service-properties) | Microsoft.Storage/storageAccounts/blobServices/write |
| [Get Blob Service Properties](get-blob-service-properties) | Microsoft.Storage/storageAccounts/blobServices/read |
| [Preflight Blob Request](preflight-blob-request) | Anonymous |
| [Get Blob Service Stats](get-blob-service-stats) | Microsoft.Storage/storageAccounts/blobServices/read |
| [Get Account Information](get-account-information) | Microsoft.Storage/storageAccounts/blobServices/getInfo/action |
| [Get User Delegation Key](get-user-delegation-key) | Microsoft.Storage/storageAccounts/blobServices/generateUserDelegationKey/action |
| [Create Container](create-container) | Microsoft.Storage/storageAccounts/blobServices/containers/write |
| [Get Container Properties](get-container-properties) | Microsoft.Storage/storageAccounts/blobServices/containers/read |
| [Get Container Metadata](get-container-metadata) | Microsoft.Storage/storageAccounts/blobServices/containers/read |
| [Set Container Metadata](set-container-metadata) | Microsoft.Storage/storageAccounts/blobServices/containers/write |
| [Get Container ACL](get-container-acl) | Microsoft.Storage/storageAccounts/blobServices/containers/getAcl/action |
| [Set Container ACL](set-container-acl) | Microsoft.Storage/storageAccounts/blobServices/containers/setAcl/action |
| [Lease Container](lease-container) | Microsoft.Storage/storageAccounts/blobServices/containers/write |
| [Delete Container](delete-container) | Microsoft.Storage/storageAccounts/blobServices/containers/delete |
| [Restore Container](restore-container) | Microsoft.Storage/storageAccounts/blobServices/containers/write |
| [List Blobs](list-blobs) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read |
| [Find Blobs by Tags in Container](find-blobs-by-tags-container) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/filter/action |
| [Put Blob](put-blob) | For create or replace: Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write To create new blob: Microsoft.Storage/storageAccounts/blobServices/containers/blobs/add/action |
| [Put Blob from URL](put-blob-from-url) | For create or replace: Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write To create new blob: Microsoft.Storage/storageAccounts/blobServices/containers/blobs/add/action |
| [Get Blob](get-blob) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read |
| [Get Blob Properties](get-blob-properties) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read |
| [Set Blob Properties](set-blob-properties) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write |
| [Get Blob Metadata](get-blob-metadata) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read |
| [Set Blob Metadata](set-blob-metadata) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write |
| [Get Blob Tags](get-blob-tags) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/tags/read |
| [Set Blob Tags](set-blob-tags) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/tags/write |
| [Find Blob by Tags](find-blobs-by-tags) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/filter/action |
| [Lease Blob](lease-blob) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write |
| [Snapshot Blob](snapshot-blob) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write or Microsoft.Storage/storageAccounts/blobServices/containers/blobs/add/action |
| [Copy Blob](copy-blob) | For destination blob: Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write or Microsoft.Storage/storageAccounts/blobServices/containers/blobs/add/action (when writing a new blob to the destination)For source blob in the same storage account: Microsoft.Storage/storageAccounts/blobServices/containers/blobs/readFor source blob in a different storage account: Available as anonymous, or include valid SAS token |
| [Copy Blob from URL](copy-blob-from-url) | For destination blob: Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write or Microsoft.Storage/storageAccounts/blobServices/containers/blobs/add/action (when writing a new blob to the destination)For source blob in the same storage account: Microsoft.Storage/storageAccounts/blobServices/containers/blobs/readFor source blob in a different storage account: Available as anonymous, or include valid SAS token |
| [Abort Copy Blob](abort-copy-blob) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write |
| [Delete Blob](delete-blob) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/delete |
| [Undelete Blob](delete-blob) | Microsoft.Storage/storageAccounts/blobServices/containers/write |
| [Set Blob Tier](set-blob-tier) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write |
| [Blob Batch](blob-batch) | Parent request: Microsoft.Storage/storageAccounts/blobServices/containers/write Sub-requests: See permissions for that request type. |
| [Set Immutability Policy](set-blob-immutability-policy) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/immutableStorage/runAsSuperUser/action |
| [Delete Immutability Policy](delete-blob-immutability-policy) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/immutableStorage/runAsSuperUser/action |
| [Set Blob Legal Hold](set-blob-legal-hold) | Microsoft.Storage/storageAccounts/blobServices/containers/write |
| [Put Block](put-block) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write |
| [Put Block from URL](put-block-from-url) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write |
| [Put Block List](put-block-list) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write |
| [Get Block List](get-block-list) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read |
| [Query Blob Contents](query-blob-contents) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read |
| [Put Page](put-page) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write |
| [Put Page from URL](put-page-from-url) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write |
| [Get Page Ranges](get-page-ranges) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read |
| [Incremental Copy Blob](incremental-copy-blob) | For destination blob: Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write For source blob: Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read For new blob: Microsoft.Storage/storageAccounts/blobServices/containers/blobs/add/action |
| [Append Block](append-block) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write or Microsoft.Storage/storageAccounts/blobServices/containers/blobs/add/action |
| [Append Block from URL](append-block-from-url) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write or Microsoft.Storage/storageAccounts/blobServices/containers/blobs/add/action |
| [Set Blob Expiry](set-blob-expiry) | Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write |

### Permissions for Queue service operations

| Queue service operation | RBAC action |
| --- | --- |
| [List Queues](list-queues1) | Microsoft.Storage/storageAccounts/queueServices/queues/read (scoped to the storage account or above) |
| [Set Queue Service Properties](set-queue-service-properties) | Microsoft.Storage/storageAccounts/queueServices/read |
| [Get Queue Service Properties](get-queue-service-properties) | Microsoft.Storage/storageAccounts/queueServices/read |
| [Preflight Queue Request](preflight-queue-request) | Anonymous |
| [Get Queue Service Stats](get-queue-service-stats) | Microsoft.Storage/storageAccounts/queueServices/read |
| [Create Queue](create-queue4) | Microsoft.Storage/storageAccounts/queueServices/queues/write |
| [Delete Queue](delete-queue3) | Microsoft.Storage/storageAccounts/queueServices/queues/delete |
| [Get Queue Metadata](get-queue-metadata) | Microsoft.Storage/storageAccounts/queueServices/queues/read |
| [Set Queue Metadata](set-queue-metadata) | Microsoft.Storage/storageAccounts/queueServices/queues/write |
| [Get Queue ACL](get-queue-acl) | Microsoft.Storage/storageAccounts/queueServices/queues/getAcl/action |
| [Set Queue ACL](set-queue-acl) | Microsoft.Storage/storageAccounts/queueServices/queues/setAcl/action |
| [Put Message](put-message) | Microsoft.Storage/storageAccounts/queueServices/queues/messages/add/action or Microsoft.Storage/storageAccounts/queueServices/queues/messages/write |
| [Get Messages](get-messages) | Microsoft.Storage/storageAccounts/queueServices/queues/messages/process/action or (Microsoft.Storage/storageAccounts/queueServices/queues/messages/delete and Microsoft.Storage/storageAccounts/queueServices/queues/messages/read) |
| [Peek Messages](peek-messages) | Microsoft.Storage/storageAccounts/queueServices/queues/messages/read |
| [Delete Message](delete-message2) | Microsoft.Storage/storageAccounts/queueServices/queues/messages/process/action or Microsoft.Storage/storageAccounts/queueServices/queues/messages/delete |
| [Clear Messages](clear-messages) | Microsoft.Storage/storageAccounts/queueServices/queues/messages/delete |
| [Update Message](update-message) | Microsoft.Storage/storageAccounts/queueServices/queues/messages/write |

### Permissions for Table service operations

| Table service operation | RBAC action |
| --- | --- |
| [Set Table Service Properties](set-table-service-properties) | Microsoft.Storage/storageAccounts/tableServices/write |
| [Get Table Service Properties](get-table-service-properties) | Microsoft.Storage/storageAccounts/tableServices/read |
| [Preflight Table Request](preflight-table-request) | Anonymous |
| [Get Table Service Stats](get-table-service-stats) | Microsoft.Storage/storageAccounts/tableServices/read |
| [Performing Entity Group Transactions](performing-entity-group-transactions) | Sub-operation authorizes separately |
| [Query Tables](query-tables) | Microsoft.Storage/storageAccounts/tableServices/tables/read (scoped to the storage account or above) |
| [Create Table](create-table) | Microsoft.Storage/storageAccounts/tableServices/tables/write |
| [Delete Table](delete-table) | Microsoft.Storage/storageAccounts/tableServices/tables/delete |
| [Get Table ACL](get-table-acl) | Microsoft.Storage/storageAccounts/tableServices/tables/getAcl/action |
| [Set Table ACL](set-table-acl) | Microsoft.Storage/storageAccounts/tableServices/tables/setAcl/action |
| [Query Entities](query-entities) | Microsoft.Storage/storageAccounts/tableServices/tables/entities/read |
| [Insert Entity](insert-entity) | Microsoft.Storage/storageAccounts/tableServices/tables/entities/write or Microsoft.Storage/storageAccounts/tableServices/tables/entities/add/action |
| [Insert Or Merge Entity](insert-or-merge-entity) | Microsoft.Storage/storageAccounts/tableServices/tables/entities/write or (Microsoft.Storage/storageAccounts/tableServices/tables/entities/add/action and Microsoft.Storage/storageAccounts/tableServices/tables/entities/update/action) |
| [Insert Or Replace Entity](insert-or-replace-entity) | Microsoft.Storage/storageAccounts/tableServices/tables/entities/write or (Microsoft.Storage/storageAccounts/tableServices/tables/entities/add/action and Microsoft.Storage/storageAccounts/tableServices/tables/entities/update/action) |
| [Update Entity](update-entity2) | Microsoft.Storage/storageAccounts/tableServices/tables/entities/write or Microsoft.Storage/storageAccounts/tableServices/tables/entities/update/action |
| [Merge Entity](merge-entity) | Microsoft.Storage/storageAccounts/tableServices/tables/entities/write or Microsoft.Storage/storageAccounts/tableServices/tables/entities/update/action |
| [Delete Entity](delete-entity1) | Microsoft.Storage/storageAccounts/tableServices/tables/entities/delete |

### Permissions for File service operations

| File service operation | RBAC action |
| --- | --- |
| [Get File Service Properties](get-file-service-properties) | Microsoft.Storage/storageAccounts/fileServices/read |
| [Set File Service Properties](set-file-service-properties) | Microsoft.Storage/storageAccounts/fileServices/write |
| [Preflight File Request](preflight-file-request) | Anonymous |
| [List Shares](list-shares) | Microsoft.Storage/storageAccounts/fileServices/shares/read |
| [Create Share](create-share) | Microsoft.Storage/storageAccounts/fileServices/shares/write |
| [Snapshot Share](snapshot-share) | Microsoft.Storage/storageAccounts/fileServices/shares/write |
| [Get Share Properties](get-share-properties) | Microsoft.Storage/storageAccounts/fileServices/shares/read |
| [Set Share Properties](set-share-properties) | Microsoft.Storage/storageAccounts/fileServices/shares/write |
| [Get Share Metadata](get-share-metadata) | Microsoft.Storage/storageAccounts/fileServices/shares/read |
| [Set Share Metadata](set-share-metadata) | Microsoft.Storage/storageAccounts/fileServices/shares/write |
| [Delete Share](delete-share) | Microsoft.Storage/storageAccounts/fileServices/shares/delete |
| [Restore Share](restore-share) | Microsoft.Storage/storageAccounts/fileServices/shares/restore/action |
| [Get Share ACL](get-share-acl) | Microsoft.Storage/storageAccounts/fileServices/shares/read |
| [Set Share ACL](set-share-acl) | Microsoft.Storage/storageAccounts/fileServices/shares/write |
| [Get Share Stats](get-share-stats) | Microsoft.Storage/storageAccounts/fileServices/shares/read |
| [Lease Share](lease-share) | Microsoft.Storage/storageAccounts/fileServices/shares/lease/action |
| [Create Permission](create-permission) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/modifypermissions/action and Microsoft.Storage/storageAccounts/fileServices/writeFileBackupSemantics/action |
| [Get Permission](get-permission) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/read and Microsoft.Storage/storageAccounts/fileServices/readFileBackupSemantics/action |
| [List Directories and Files](list-directories-and-files) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/read and Microsoft.Storage/storageAccounts/fileServices/readFileBackupSemantics/action |
| [Create Directory](create-directory) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/write and Microsoft.Storage/storageAccounts/fileServices/writeFileBackupSemantics/action |
| [Get Directory Properties](get-directory-properties) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/read and Microsoft.Storage/storageAccounts/fileServices/readFileBackupSemantics/action |
| [Set Directory Properties](set-directory-properties) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/write and Microsoft.Storage/storageAccounts/fileServices/writeFileBackupSemantics/action, and Microsoft.Storage/storageAccounts/fileServices/fileShares/files/modifypermissions/action if x-ms-file-permission or x-ms-file-permission-key is included in HTTP request header. |
| [Delete Directory](delete-directory) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/write and Microsoft.Storage/storageAccounts/fileServices/writeFileBackupSemantics/action |
| [Get Directory Metadata](get-directory-metadata) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/read and Microsoft.Storage/storageAccounts/fileServices/readFileBackupSemantics/action |
| [Set Directory Metadata](set-directory-metadata) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/write and Microsoft.Storage/storageAccounts/fileServices/writeFileBackupSemantics/action |
| [Rename Directory](rename-directory) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/write and Microsoft.Storage/storageAccounts/fileServices/writeFileBackupSemantics/action |
| [Create File](create-file) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/write and Microsoft.Storage/storageAccounts/fileServices/writeFileBackupSemantics/action |
| [Get File](get-file) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/read and Microsoft.Storage/storageAccounts/fileServices/readFileBackupSemantics/action |
| [Get File Properties](get-file-properties) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/read and Microsoft.Storage/storageAccounts/fileServices/readFileBackupSemantics/action |
| [Set File Properties](set-file-properties) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/write and Microsoft.Storage/storageAccounts/fileServices/writeFileBackupSemantics/action, and Microsoft.Storage/storageAccounts/fileServices/fileShares/files/modifypermissions/action if x-ms-file-permission or x-ms-file-permission-key is included in HTTP request header. |
| [Put Range](put-range) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/write and Microsoft.Storage/storageAccounts/fileServices/writeFileBackupSemantics/action |
| [Put Range from URL](put-range-from-url) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/write and Microsoft.Storage/storageAccounts/fileServices/writeFileBackupSemantics/action |
| [List Ranges](list-ranges) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/read and Microsoft.Storage/storageAccounts/fileServices/readFileBackupSemantics/action |
| [Get File Metadata](get-file-metadata) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/read and Microsoft.Storage/storageAccounts/fileServices/readFileBackupSemantics/action |
| [Set File Metadata](set-file-metadata) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/write and Microsoft.Storage/storageAccounts/fileServices/writeFileBackupSemantics/action |
| [Delete File](delete-file2) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/write and Microsoft.Storage/storageAccounts/fileServices/writeFileBackupSemantics/action |
| [Copy File](copy-file) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/write and Microsoft.Storage/storageAccounts/fileServices/writeFileBackupSemantics/action, and Microsoft.Storage/storageAccounts/fileServices/fileShares/files/modifypermissions/action if x-ms-file-permission or x-ms-file-permission-key is included in HTTP request header. |
| [Abort Copy File](abort-copy-file) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/write and Microsoft.Storage/storageAccounts/fileServices/writeFileBackupSemantics/action |
| [List Handles](list-handles) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/read and Microsoft.Storage/storageAccounts/fileServices/readFileBackupSemantics/action |
| [Force Close Handles](force-close-handles) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/write and Microsoft.Storage/storageAccounts/fileServices/writeFileBackupSemantics/action |
| [Lease File](lease-file) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/write and Microsoft.Storage/storageAccounts/fileServices/writeFileBackupSemantics/action |
| [Rename File](rename-file) | Microsoft.Storage/storageAccounts/fileServices/fileShares/files/write and Microsoft.Storage/storageAccounts/fileServices/writeFileBackupSemantics/action |