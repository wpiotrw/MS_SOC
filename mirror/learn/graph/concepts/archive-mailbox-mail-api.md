---
layout: Conceptual
title: Use mail APIs with Exchange archive mailboxes (preview) - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/archive-mailbox-mail-api
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: Mekaus
ms.author: Mekaus
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: outlook
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: how-to
description: Learn how to access Exchange archive folders and messages, follow redirects, create folders, and synchronize changes with Microsoft Graph beta mail APIs.
ms.localizationpriority: medium
ms.date: 2026-11-18T00:00:00.0000000Z
ms.custom: msecd-doc-authoring-1032
ai-usage: ai-generated
locale: en-us
document_id: 69e120a4-30e0-5073-d3f5-5ffbc49c4b5a
document_version_independent_id: 69e120a4-30e0-5073-d3f5-5ffbc49c4b5a
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/archive-mailbox-mail-api.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: archive-mailbox-mail-api
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/archive-mailbox-mail-api.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/a3955c7b-f5ee-420d-aff5-d7119738f38b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31948f4-2f38-404b-ac93-c3c8c5b3ae33
platformId: 7e7157da-ad04-eda3-5430-adff6ba8e197
---

# Use mail APIs with Exchange archive mailboxes (preview) - Microsoft Graph | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Use Microsoft Graph beta mail APIs to list messages, create folders, and synchronize message changes in an Exchange archive mailbox.

This guide explains how to follow redirects when reading archive folders and messages, where to create archive folders, and how to keep track of message changes.

The folder and message examples in this guide use `/users/.../mailFolders` endpoints. Use the folder IDs returned by the mail API operation you're calling.

## Prerequisites

Before you begin, make sure you have:

- A work or school account with an archive mailbox. Personal Microsoft accounts aren't supported.
- An access token with the permissions required for your operation.
- An HTTP client that can handle redirects without automatically forwarding credentials to an untrusted host.

For the Exchange settings request used to discover the archive mailbox, use the following permissions:

| Operation | Delegated | Application |
| --- | --- | --- |
| Discover the archive mailbox | User.Read.All | User.Read.All |

For the mail API operations, use the permissions documented for [List messages](/en-us/graph/api/user-list-messages?view=graph-rest-beta&amp;preserve-view=true), [Create mailFolder](/en-us/graph/api/user-post-mailfolders?view=graph-rest-beta&amp;preserve-view=true), and [Create childFolder](/en-us/graph/api/mailfolder-post-childfolders?view=graph-rest-beta&amp;preserve-view=true).

## How archive mailboxes work

The *main archive* maintains the complete folder hierarchy. As the archive grows, *auxiliary archives* store additional content. A folder can appear in the main archive, and its messages can be stored in an auxiliary archive.

When you read a folder or message, or synchronize message changes, a supported API can return `308 Permanent Redirect`. The `Location` header in the response contains the URL to use for the content.

## Discover the archive mailbox

First, get the user's [Exchange settings](/en-us/graph/api/resources/exchangesettings?view=graph-rest-beta&amp;preserve-view=true). The response provides the mailbox ID you need for archive requests.

The following example shows how to request the Exchange settings for a user.

```http
GET https://graph.microsoft.com/beta/users/alex.wilber@contoso.com/settings/exchange
Authorization: Bearer {token}
```

The following example shows a response with separate IDs for the primary mailbox and the in-place archive mailbox.

```json
{
  "primaryMailboxId": "MBX:e0643f21@a7809c93",
  "inPlaceArchiveMailboxId": "MBX:f10964a6@a7809c93"
}
```

Save **inPlaceArchiveMailboxId**. In these examples, its value is `MBX:f10964a6@a7809c93`.

Use that returned value to address the main archive mailbox. Don't construct an archive mailbox ID from the user's email address or primary mailbox ID.

## Always target the main archive mailbox

Use the main archive mailbox ID when you start archive folder operations. You don't need to discover auxiliary archive mailboxes before you make a request.

| Operation | What your application should do |
| --- | --- |
| Supported folder and message reads | Start with the main archive. If Microsoft Graph returns a redirect, follow the supplied URL. |
| Create, update, or delete folders | Send the request to the main archive, even when the content in the folder resides in an auxiliary archive. These operations don't return a redirect. |

Create folders through the main archive. Folders created directly in an auxiliary archive don't synchronize back to the main archive and don't appear in Outlook.

## Follow a redirect

For supported folder reads, message reads, and message delta requests, follow these steps:

1. Make your request using the main archive mailbox ID.
2. If the response is `308 Permanent Redirect`, read the URL in the `Location` header.
3. Make the same request to that URL. The response returns the requested data.

The following flow shows a read request that is redirected.

```text
App                 Microsoft Graph
 |  Read archive content   |
 |------------------------>|
 |  308 + Location URL     |
 |<------------------------|
 |  GET the Location URL   |
 |------------------------>|
 |  Requested data         |
 |<------------------------|
```

If no redirect is needed, the original request returns the data directly.

## List messages in an archive folder using the mail API

Start the read request with the main archive mailbox ID and the target folder ID.

In the following example, the main archive is `MBX:f10964a6@a7809c93`. If its content resides in an auxiliary archive, the service supplies the URL for the follow-up request.

### Request

The following request shows how to list the message IDs and subjects in the archive folder.

```http
GET https://graph.microsoft.com/beta/users/MBX:f10964a6@a7809c93/mailFolders/AAMkAGVmMDEzMDAAAIBDAAAAA==/messages?$select=id,subject
```

### Redirect response

If the content is in an auxiliary archive, the service might return the following response.

```http
HTTP/1.1 308 Permanent Redirect
Location: https://graph.microsoft.com/beta/users/MBX:767fh867@a7809c93/mailFolders/AAMkAGVmMDEzMDAAAIBDAAAAA==/messages?$select=id,subject
Content-Length: 0
```

### Follow-up request

Make a GET request to the complete `Location` URL. Don't construct the URL yourself or replace its IDs.

```http
GET https://graph.microsoft.com/beta/users/MBX:767fh867@a7809c93/mailFolders/AAMkAGVmMDEzMDAAAIBDAAAAA==/messages?$select=id,subject
```

A successful request returns `200 OK` with the messages. The same redirect-handling approach applies to supported folder reads, message reads, and message delta requests.

Use the required mail API authentication and permissions. Before you send credentials to a redirect URL, verify HTTPS and a trusted Microsoft Graph endpoint. Check whether your SDK handles `308 Permanent Redirect` automatically; otherwise, handle it in your application and limit redirects.

## Create folders in the main archive using the mail API

Create archive folders through the main archive, including folders whose content resides in an auxiliary archive.

When a folder expands to an auxiliary archive, the service automatically creates the corresponding folder in the auxiliary archive. You don't need to create it yourself.

Don't create folders directly in an auxiliary archive. They don't synchronize back to the main archive or appear in Outlook. Don't reuse a URL from a content-read redirect to create folders.

### Create a folder

The following request shows how to create a folder.

```http
POST https://graph.microsoft.com/beta/users/MBX:f10964a6@a7809c93/mailFolders
Content-Type: application/json

{
  "displayName": "Project archive"
}
```

### Create a child folder

The following request shows how to create a child folder. Use the main archive mailbox ID and the parent folder ID from the main archive hierarchy in the request URL.

```http
POST https://graph.microsoft.com/beta/users/MBX:f10964a6@a7809c93/mailFolders/AAMkAGVmMDEzMDAAAIBDAAAAA==/childFolders
Content-Type: application/json

{
  "displayName": "Project documents"
}
```

## Read multiple pages and synchronize changes

If a response contains **@odata.nextLink**, request that complete URL to get the next page.

To track message changes in a folder, use a message delta request. The following example uses the same main archive mailbox and mail API folder IDs from the previous list messages example.

```http
GET https://graph.microsoft.com/beta/users/MBX:f10964a6@a7809c93/mailFolders/AAMkAGVmMDEzMDAAAIBDAAAAA==/messages/delta
```

To process the synchronization response:

1. If the request returns `308 Permanent Redirect`, follow the URL in the `Location` header.
2. Follow each **@odata.nextLink** until the response contains **@odata.deltaLink**.
3. Save the complete delta link for the next synchronization.

Keep a separate delta link for each folder. Use returned links exactly as provided; don't edit their mailbox IDs or tokens. If the API reports that synchronization state is no longer valid, follow its recovery instructions.

For the complete synchronization procedure, see [Synchronize message changes](/en-us/graph/delta-query-messages).

## Attachment upload sessions

The [attachment: createUploadSession](/en-us/graph/api/attachment-createuploadsession?view=graph-rest-beta&amp;preserve-view=true) method allows you to add large attachments to messages in primary mailboxes. It isn't supported for archive mailboxes; an archive request might return a `404 Not Found` response code.

To place an item directly into an archive mailbox, use the import API instead. For that separate workflow, see [Import an Exchange mailbox item using the mailbox import and export APIs](/en-us/graph/import-exchange-mailbox-item).

## Common questions

### Do I need to discover all auxiliary archive mailboxes?

No. Start folder requests with the main archive mailbox and follow the URL returned when a supported request is redirected.

### Do folder create, update, and delete operations require redirection?

No. Send these operations to the main archive mailbox, even when the content of the folder resides in an auxiliary archive.

### Why is a folder I created in an auxiliary archive missing from Outlook?

Folders created directly in an auxiliary archive don't synchronize back to the main archive. Create folders through the main archive instead.

### Can I use /me/mailFolders/archive to access the archive mailbox?

No. That URL identifies the *One-Click Archive* folder in the primary mailbox, not the Exchange archive mailbox.

For Exchange archive access, use the archive mailbox identifier and folder IDs. Well-known folder names aren't supported in archive request paths.

### Is non-IPM access blocked?

No. Existing API permissions and operation-specific restrictions still apply.