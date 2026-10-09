---
layout: Conceptual
title: Change notifications for Outlook resources in Microsoft Graph - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/outlook-change-notifications-overview
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: SuryaLashmiS
ms.author: MSGraphDocsVteam
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: outlook
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: how-to
description: Subscribe to changes to Outlook resources (create, update, and delete) and changed resource data in Microsoft Graph APIs and receive notifications via webhooks.
ms.localizationpriority: high
ms.custom: scenarios:getting-started
ms.date: 2024-11-07T00:00:00.0000000Z
locale: en-us
document_id: 7750c9fb-f1f2-be55-fc31-b168b36c5a67
document_version_independent_id: 7750c9fb-f1f2-be55-fc31-b168b36c5a67
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/outlook-change-notifications-overview.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: outlook-change-notifications-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/outlook-change-notifications-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 007bec5f-1fd2-3153-d096-9f59b999485a
---

# Change notifications for Outlook resources in Microsoft Graph - Microsoft Graph | Microsoft Learn

The Microsoft Graph API lets you subscribe to changes to a resource—including creation, update, or deletion of the resource—and receive notifications via webhooks. A [subscription](/en-us/graph/api/resources/change-notifications-api-overview) specifies the desired types of changes to monitor for a specific resource, and includes a URL for an endpoint to receive notifications of those changes.

Setting up a subscription reduces the overhead of otherwise having to query and compare resources to deduce any changes. You can optionally specify in the subscription request to encrypt and include as part of a notification the resource data that has changed, saving a separate subsequent API call to get the resource payload.

There is a maximum limit of 1000 active subscriptions for Outlook resources per mailbox for all applications. You can subscribe to changes in contacts, events, or messages in the mailbox.

## Subscribe to changes in contacts, calendar, or mail

To subscribe to change notifications of Outlook resources, first create a [subscription](/en-us/graph/api/resources/subscription).

The following Outlook resources support subscriptions with or without resource data in the [change notification](/en-us/graph/api/resources/changenotification) payload.

- [contact](/en-us/graph/api/resources/contact)
- [event](/en-us/graph/api/resources/event)
- [message](/en-us/graph/api/resources/message)

## Create a subscription

To create a subscription, specify the Outlook resource and the type of changes (creation, update, or deletion) for which you want to receive notifications. See an example.

### Request permissions

Creating and managing (getting, updating, and deleting) a subscription requires a read scope to the resource. For example, to get change notifications on messages, your app needs the Mail.Read permission. Outlook change notifications support delegated and application permission scopes. Note the following limitations:

- Delegated permission supports subscribing to items in folders in only the signed-in user's mailbox. For example, you can't use the delegated permission Calendars.Read to subscribe to events in another user’s mailbox.
- To subscribe to change notifications of Outlook contacts, events, or messages in *shared or delegated* folders:

    - Use the corresponding application permission to subscribe to changes of items in a folder or mailbox of *any* user in the tenant.
    - Don't use the Outlook sharing permissions (Contacts.Read.Shared, Calendars.Read.Shared, Mail.Read.Shared, and their read/write counterparts), as they do **not** support subscribing to change notifications on items in shared or delegated folders.

Depending on the resource, use the least privileged permission specified in the following table to call this API.

| Resource | Supported Resource Paths | Delegated (work or school account) | Delegated (personal Microsoft account) | Application |
| --- | --- | --- | --- | --- |
| [contact](/en-us/graph/api/resources/contact) | Changes to all personal contacts in a user's mailbox: `/me/contacts``/users/{id}/contacts`Changes to contacts in a user's contactFolder:`/users/{id}/contactFolders/{id}/contacts` | Contacts.Read | Contacts.Read | Contacts.Read |
| [event](/en-us/graph/api/resources/event) | Changes to all events in a user's mailbox: `/me/events``/users/{id}/events` | Calendars.Read | Calendars.Read | Calendars.Read |
| [message](/en-us/graph/api/resources/message) | Changes to all messages in a user's mailbox: `/me/messages``/users/{id}/messages`Changes to messages in a user's mailFolder:`/users/{id}/mailFolders/{id}/messages` | Mail.ReadBasic, Mail.Read | Mail.ReadBasic, Mail.Read | Mail.ReadBasic, Mail.Read |

### Resource path

The **resource** value identifies the mailbox to subscribe to, for example `users/{id}/messages`. Provide a user identifier that resolves to a single, unambiguous mailbox; otherwise, subscription creation might fail intermittently with a `503 ServiceUnavailable` error, such as "Mailbox info is stale."

Important

We recommend that you identify the user by object ID (OID) rather than by user principal name (UPN), because the OID always maps to a single user.

If you prefer to use a UPN and the UPN begins with a GUID, such as `3f8c2a71-6d45-4e9b-a237-81c5f0d762ae@contoso.com`, the portion before the `@` symbol can be misinterpreted as a mailbox GUID rather than a UPN. To prevent this, prefix the value with `AAD-UPN:` so that it's always treated as a UPN. Use the `AAD-UPN:` prefix only when the value is the UPN of a work or school account.

For an example that uses the `AAD-UPN:` prefix, see Example 2.

### Include resource data in notification payload

To have resource data included in a change notification, you **must** specify the following properties, in addition to those you normally include when creating a subscription:

- **includeResourceData**: Set this property to `true` to explicitly request resource data.
- **resource**: This property specifies the resource URL. Make sure to use the `$select` query parameter to explicitly specify the Outlook resource properties to include in the notification payload.

    Note

    Do not include in the URL `$top`, `$skip`, `$orderby`, `$select=Body,UniqueBody`, and `$expand` other than **singleValueExtendedProperties** or **multiValueExtendedProperties**.
- **encryptionCertificate**: This property contains only the public key that Microsoft Graph uses to encrypt resource data. Keep the corresponding private key to [decrypt the content](change-notifications-with-resource-data#decrypting-resource-data-from-change-notifications).
- **encryptionCertificateId**: This property is your own identifier for the certificate. Use this ID to match in each change notification which certificate to use for decryption.

See an example for subscribing to change notifications with resource data for the **message** resource.

### Refine the conditions for a notification

You can further refine the conditions for a notification by using the `$filter` query parameter. See an example.

One common application of `$filter` is to get notified upon a change in a specific resource property. For example, you can use `$filter` to subscribe to unread messages in a folder (the **isRead** property is `false`), and include all the change types:

- A message added to or marked unread in the folder would trigger a `Created` notification.
- Reading a message or marking it as read in the folder would trigger a `Deleted` notification.
- A change to any property, other than **isRead**, of a **message** resource in the folder would trigger an `Updated` notification.

If you don't use a `$filter` when creating the subscription:

- Adding a message to the folder would result in a `Created` notification.
- Reading a message in the folder, marking the message as read, or changing any other property of a message in that folder would result in an `Updated` notification.
- Deleting the message would result in a `Delete` notification.

### Subscribe to lifecycle notifications

The Outlook **contact**, **event**, and **message** resources also support subscribing to lifecycle notifications. Lifecycle notifications are needed in case your app gets their subscriptions removed or misses some change notifications. Apps should implement logic to detect and recover from the loss, and resume a continuous change notification flow. To learn more, see [subscribing to lifecycle notifications](change-notifications-lifecycle-events).

### Keep track of subscription lifetime

Make sure to [extend](/en-us/graph/api/subscription-update) a subscription before it expires. The maximum lifetime for a subscription without Outlook resource data can be found in the [subscription lifetime table](change-notifications-overview#subscription-lifetime).

If you lose the permission granted earlier for a subscription and the subscription expires meanwhile, request permission again to [create](/en-us/graph/api/subscription-post-subscriptions) a new subscription.

## Receive notification payloads

Depending on your subscription, notifications include resource data. Subscriptions with resource data allow you to get the resource payload along with the notification, avoiding the overhead for a separate API call to get the changed resource data.

### Receive notifications with resource data

The following is an example of the payload of a notification with resource data of a **message** resource. The **resource** and **resourceData** properties correspond to the **message** instance that triggered the notification. Use the **encryptedContent** property to decrypt the resource data.

```json
{
    "value": [
      {
        "subscriptionId": "dfd11b2f-8222-4189-9545-4205c95d6235",
        "subscriptionExpirationDateTime": "2021-12-31T16:16:44.9907405+05:30",
        "changeType": "created",
        "resource": "Users('722effaf-0433-4272-9ac4-d5ec11c3cd77')/messages('AAMkAGUwNjQ4ZjIxLTQ3Y2Y8AAA=')",
        "clientState": "<<--SpecifiedClientState-->>",
        "tenantId": "<<--TenantForWhichNotificationWasSent-->>",
        "encryptedContent": {
          "data": "<<--EncryptedContent-->>",
          "dataKey": "<<--EnryptedDataKeyUsedForEncryptingContent-->>",
          "dataSignature": "Qw/9ubWeUYJPWWXvNiGgct2FkNG2MXTRm/BLUpJM66k=",
          "encryptionCertificateId": "<<--IdOfTheCertificateUsedForEncryptingDataKey-->>",
          "encryptionCertificateThumbprint": "<<--ThumbprintOfTheCertificateUsedForEncryptingDataKey-->>"
        },
        "resourceData": {
          "@odata.type": "#microsoft.graph.message",
          "@odata.id": "Users('722effaf-0433-4272-9ac4-d5ec11c3cd77')/messages('AAMkAGUwNjQ4ZjIxLTQ3Y2Y8AAA=')",
          "@odata.etag": "W/\"CQAAABYAAACQ2fKdhq8oSKEDSVrdi3lRAAGDUR8n\"",
          "id": "AAMkAGUwNjQ4ZjIxLTQ3Y2Y8AAA="
        }
      }
    ]
    "validationTokens": ["<<--ValidationTokens-->>"]
}
```

For details about how to validate tokens and decrypt the payload, see [Set up change notifications that include resource data](change-notifications-with-resource-data).

The following is an example of a decrypted notification payload. The decrypted payload conforms to the Outlook [message](/en-us/graph/api/resources/message) schema. The payload is similar to that returned by a [GET message](/en-us/graph/api/message-get) operation. However, the notification payload contains only those properties specified with a `$select` parameter in the **resource** property of the subscription. Notification payloads for other Outlook resources like [contact](/en-us/graph/api/resources/contact) and [event](/en-us/graph/api/resources/event) follow their respective schemas.

```json
{
    "receivedDateTime@odata.type":"#DateTimeOffset",
    "receivedDateTime":"2021-12-30T10:53:35Z",
    "subject":"TEST MESSAGE FOR RICH NOTIFICATIONS",
    "bodyPreview":"Hello,\r\n\r\nWhat\u2019s up?\r\n\r\nThanks\r\nMegan",
    "importance@odata.type":"#microsoft.graph.importance",
    "importance":"normal",
    "from": {
        "@odata.type":"#microsoft.graph.recipient",
        "emailAddress": {
            "@odata.type":"#microsoft.graph.emailAddress",
            "name":"Megan Brown",
            "address":"Megan.Brown@microsoft.com"
        }
    }
}
```

### Receive notifications without resource data

Notifications without resource data give you enough information to make GET calls to get the resource. Subscriptions for notifications without resource data don't require an encryption certificate, because the actual resource data is not sent over.

The next example shows the payload of a notification that corresponds to an Outlook **message** resource. It includes the **resource** and **resourceData** properties, which represent the resource that triggered the notification. Use the **resource** and **@odata.id** properties to make calls to Microsoft Graph to get the payload of the resource.

Note

GET calls always return the current state of the resource. If the resource is changed between the time the notification is sent and the time the resource is retrieved, the operation returns the state of the resource on retrieval.

```json
"value": [
 {
   "subscriptionId": "c6126aa3-0ed8-412f-a988-71e6cee627c4",
   "subscriptionExpirationDateTime": "2022-01-02T03:12:18.2257768+05:30",
   "changeType": "created",
   "resource": "Users/622eaaff-0683-4862-9de4-f2ec83c2bd98/Messages/AAMkAGUwNjQ4ZjIxAAA=",
   "resourceData": {
     "@odata.type": "#Microsoft.Graph.Message",
     "@odata.id": "Users/622eaaff-0683-4862-9de4-f2ec83c2bd98/Messages/AAMkAGUwNjQ4ZjIAAA=",
     "@odata.etag": "W/\"CQAAABYAAACQ2fKdhq8oSKEDSVrdi3lRAAGDUUXn\"",
     "id": "AAMkAGUwNjQ4ZjIxAAA="
   },
   "clientState": "<<--SpecifiedClientState-->>",
   "tenantId": "<<--TenantForWhichNotificationWasSent-->>"
 }
]
```

## Examples

### Example 1: Create a subscription to get change notifications without resource data when the user receives a new message

The following example requests a notification for a message being created in the user's mailbox.

#### Request

```http
POST https://graph.microsoft.com/v1.0/subscriptions
Content-type: application/json
{
    "changeType": "created",
    "notificationUrl": "https://webhook.azurewebsites.net/api/send/myNotifyClient",
    "resource": "users/622eaaff-0683-4862-9de4-f2ec83c2bd98/messages",
    "expirationDateTime": "2021-07-07T21:42:18.2257768+00:00",
    "clientState": "secretClientState"
}
```

#### Response

The following example shows the response.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 201 Created
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#subscriptions/$entity",
    "id": "5522bd62-7c96-4530-85b0-00b916f6151a",
    "resource": "users/622eaaff-0683-4862-9de4-f2ec83c2bd98/messages",
    "applicationId": "507c3b9a-67b8-463d-88a2-15a8cefb2111",
    "changeType": "created",
    "clientState": "secretClientState",
    "notificationUrl": "https://webhook.azurewebsites.net/api/send/myNotifyClient",
    "notificationQueryOptions": null,
    "notificationContentType": null,
    "lifecycleNotificationUrl": null,
    "expirationDateTime": "2022-01-01T21:42:18.2257768Z",
    "creatorId": "a4c7bd34-4f3b-46b7-a25d-b63c1e2a2842",
    "includeResourceData": null,
    "latestSupportedTlsVersion": "v1_2",
    "encryptionCertificate": null,
    "encryptionCertificateId": null,
    "notificationUrlAppId": null
}
```

### Example 2: Create a subscription using a UPN that begins with a GUID

The following example subscribes to notifications for a message being created in the mailbox of a user whose UPN begins with a GUID. The `resource` value uses the `AAD-UPN:` prefix so that Exchange treats the value as a UPN. For more information, see Resource path.

#### Request

```http
POST https://graph.microsoft.com/v1.0/subscriptions
Content-type: application/json
{
    "changeType": "created",
    "notificationUrl": "https://webhook.azurewebsites.net/api/send/myNotifyClient",
    "resource": "users/AAD-UPN:3f8c2a71-6d45-4e9b-a237-81c5f0d762ae@contoso.com/messages",
    "expirationDateTime": "2021-07-07T21:42:18.2257768+00:00",
    "clientState": "secretClientState"
}
```

#### Response

The following example shows the response.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 201 Created
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#subscriptions/$entity",
    "id": "5522bd62-7c96-4530-85b0-00b916f6151a",
    "resource": "users/AAD-UPN:3f8c2a71-6d45-4e9b-a237-81c5f0d762ae@contoso.com/messages",
    "applicationId": "507c3b9a-67b8-463d-88a2-15a8cefb2111",
    "changeType": "created",
    "clientState": "secretClientState",
    "notificationUrl": "https://webhook.azurewebsites.net/api/send/myNotifyClient",
    "notificationQueryOptions": null,
    "notificationContentType": null,
    "lifecycleNotificationUrl": null,
    "expirationDateTime": "2022-01-01T21:42:18.2257768Z",
    "creatorId": "a4c7bd34-4f3b-46b7-a25d-b63c1e2a2842",
    "includeResourceData": null,
    "latestSupportedTlsVersion": "v1_2",
    "encryptionCertificate": null,
    "encryptionCertificateId": null,
    "notificationUrlAppId": null
}
```

### Example 3: Create a subscription to get change notifications with resource data when the user receives a new message

The following example subscribes to notifications with resource data for a message being created in the user's mailbox. The properties of the **message** resource to be included in the notification payload are specified using the `$select` query parameter.

#### Request

```http
POST https://graph.microsoft.com/v1.0/subscriptions
Content-type: application/json
{
    "changeType": "created",
    "notificationUrl": "https://webhook.azurewebsites.net/api/send/myNotifyClient",
    "resource": "users/622eaaff-0683-4862-9de4-f2ec83c2bd98/messages?$select=Subject,bodyPreview,importance,receivedDateTime,from",
    "expirationDateTime": "2022-01-01T21:42:18.2257768+00:00",
    "clientState": "secretClientValue",
    "includeResourceData": true,
    "encryptionCertificate": "MIIDMzCCAhugAwIBAgIQE7D+++Dk1hKQBqWA==",
    "encryptionCertificateId": "testCertificateId"
}
```

#### Response

The following example shows the response.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 201 Created
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#subscriptions/$entity",
    "id": "178eec5f-cf3c-4e7e-8a9c-8640deb5b5c5",
    "resource": "users/622eaaff-0683-4862-9de4-f2ec83c2bd98/messages?$select=Subject,bodyPreview,importance,receivedDateTime,from",
    "applicationId": "507c3b9a-67b8-463d-88a2-15a8cefb2111",
    "changeType": "created",
    "clientState": "secretClientValue",
    "notificationUrl": "https://webhook.azurewebsites.net/api/send/myNotifyClient",
    "notificationQueryOptions": null,
    "notificationContentType": null,
    "lifecycleNotificationUrl": null,
    "expirationDateTime": "2022-01-01T12:32:35.1582696Z",
    "creatorId": "a4c7bd34-4f3b-46b7-a25d-b63c1e2a2842",
    "includeResourceData": true,
    "latestSupportedTlsVersion": "v1_2",
    "encryptionCertificate": "MIIDMzCCAhugAwIBAgIQE7D+++Dk1hKQBqWA==",
    "encryptionCertificateId": "testCertificateId",
    "notificationUrlAppId": null
}
```

### Example 4: Create a subscription to get change notifications with resource data for a message based on a condition

The following example subscribes to notifications with resource data for a message being created in the Drafts folder, containing one or more attachments, and of high importance.

#### Request

```http
POST https://graph.microsoft.com/v1.0/subscriptions
Content-type: application/json
{
    "changeType": "created",
    "notificationUrl": "https://webhook.azurewebsites.net/api/send/myNotifyClient",
    "resource": "me/mailfolders('Drafts')/messages?$select=Subject,bodyPreview&$filter=hasAttachments eq true AND importance eq 'High'",
    "expirationDateTime": "2022-01-01T21:42:18.2257768+00:00",
    "clientState": "secretClientValue",
    "includeResourceData": true,
    "encryptionCertificate": "MIIDMzCCAhugAwIBAgIQE7D+++Dk1hKQBqWA==",
    "encryptionCertificateId": "testCertificateId"
}
```

#### Response

The following example shows the response.

> 
> **Note:** The response object shown here might be shortened for readability.

```http
HTTP/1.1 201 Created
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#subscriptions/$entity",
    "id": "239dbc5f-cf3c-4e7e-8c9c-3340abc5b5c5",
    "resource": "me/mailfolders('Drafts')/messages?$select=Subject,bodyPreview&$filter=hasAttachments eq true AND importance eq 'High'",
    "applicationId": "507c3b9a-67b8-463d-88a2-15a8cefb2111",
    "changeType": "created",
    "clientState": "secretClientValue",
    "notificationUrl": "https://webhook.azurewebsites.net/api/send/myNotifyClient",
    "notificationQueryOptions": null,
    "notificationContentType": null,
    "lifecycleNotificationUrl": null,
    "expirationDateTime": "2022-01-20T12:32:35.1582696Z",
    "creatorId": "a4c7bd34-4f3b-46b7-a25d-b63c1e2a2842",
    "includeResourceData": true,
    "latestSupportedTlsVersion": "v1_2",
    "encryptionCertificate": "MIIDMzCCAhugAwIBAgIQE7D+++Dk1hKQBqWA==",
    "encryptionCertificateId": "testCertificateId",
    "notificationUrlAppId": null
}
```