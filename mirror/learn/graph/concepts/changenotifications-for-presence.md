---
layout: Conceptual
title: Get change notifications for presence updates in Microsoft Teams - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/changenotifications-for-presence
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: awang119
ms.author: MSGraphDocsVteam
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: cloud-communications
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: how-to
description: Use change notifications in Microsoft Graph to subscribe to presence changes for Microsoft Teams users.
ms.localizationpriority: high
ms.custom: scenarios:getting-started
ms.date: 2024-11-07T00:00:00.0000000Z
locale: en-us
document_id: bd52cdd6-f925-89a3-6957-33a7818e9cee
document_version_independent_id: bd52cdd6-f925-89a3-6957-33a7818e9cee
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/changenotifications-for-presence.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: changenotifications-for-presence
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/changenotifications-for-presence.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 144864a2-a13f-7334-4258-794aa7a02024
---

# Get change notifications for presence updates in Microsoft Teams - Microsoft Graph | Microsoft Learn

Change notifications in Microsoft Graph enable you to subscribe to changes in [user presence](/en-us/microsoftteams/presence-admins) information in Microsoft Teams. Change notifications provide an alternative to polling for presence by using the [GET presence](/en-us/graph/api/presence-get) and [POST getPresencesByUserId](/en-us/graph/api/cloudcommunications-getpresencesbyuserid) APIs.

Use webhooks to subscribe to users' presence information and get notifications when changes occur. For general information on webhooks, see [Microsoft Graph API change notifications](/en-us/graph/api/resources/change-notifications-api-overview).

Note

Effective June 30 2024, to get changes that occurred to an active meeting call, we recommend that you subscribe to rich notifications.

This API is available in the following [national cloud deployments](/en-us/graph/deployments).

| Global service | US Government L4 | US Government L5 (DOD) | China operated by 21Vianet |
| --- | --- | --- | --- |
| ✅ | ❌ | ❌ | ❌ |

## Permissions

| Permission type | Permissions (from least to most privileged) | Supported versions |
| --- | --- | --- |
| Delegated (work or school account) | Presence.Read.All. | V1, beta. |
| Delegated (personal Microsoft account) | Not supported. | Not supported. |
| Application | Not supported. | Not supported. |

## Supported resources for presence

A single user can create one presence subscription per unique application with a maximum expiration time of an hour. A subscription can be renewed via the [Update subscription API](/en-us/graph/api/subscription-update) before it expires, or a new subscription can be created for the same resource after expiration. Presence subscriptions support notifications with resource data, allowing more detailed information to be delivered along with change notifications. For more information, see [Set up change notifications with resource data](change-notifications-with-resource-data).

The following table lists the types of presence changes you can subscribe to. For more information, see [Create subscription](/en-us/graph/api/subscription-post-subscriptions).

| Presence subscription type | Resource URL | Supported change types |
| --- | --- | --- |
| Single user presence changes | `communications/presences/{id}` | Updated |
| Bulk user presence changes (maximum 650 user IDs) | `communications/presences?$filter=id in ('{id}', '{id}', ...)` | Updated |

## Subscribe to presence changes

To subscribe to presence changes, you can set the resource in the subscription payload to `communications/presences/{id}` where the {id} field must be replaced with the user ID GUID of the user's presence. This subscription delivers change notifications when the user presence changes.

Set `includeResourceData` to `true` and provide appropriate values for `encryptionCertificate` and `encryptionCertificateId` to subscribe to rich notifications.

### Example: Single user presence subscription payloads

```json
{
    "changeType": "updated",
    "notificationUrl": "https://webhook.contoso.com/api",
    "lifecycleNotificationUrl": "https://webhook.contoso.com/api",
    "resource": "communications/presences/{id}",
    "expirationDateTime": "2023-09-14T10:00:00.0000000Z",
    "includeResourceData": true,
    "encryptionCertificate": "{encryption certificate}",
    "encryptionCertificateId": "{certificate id}",
    "clientState": "{secret client state}"
}
```

## Subscribe to multiple users' presence

Bulk subscriptions for user presence can be created by setting the subscription resource value to `/communications/presences?$filter=id in ('{id}', '{id}',...)`, where the {id} represents a user IDs GUID of users. A maximum of 650 users can be subscribed in a single subscription. Presence changes for user IDs generate a notification.

### Example: Multiple user presence subscription payloads

```json
{
    "changeType": "updated",
    "notificationUrl": "https://webhook.contoso.com/api",
    "lifecycleNotificationUrl": "https://webhook.contoso.com/api",
    "resource": "/communications/presences?$filter=id in ('{id}', '{id}',...)",
    "expirationDateTime": "2023-09-14T10:00:00.0000000Z",
    "includeResourceData": true,
    "encryptionCertificate": "{encryption certificate}",
    "encryptionCertificateId": "{certificate id}",
    "clientState": "{secret client state}"
}
```

## Receive presence event notifications

Change notifications for presence events are triggered when changes to a user's availability and activity are made.

### Basic presence notifications

Basic notifications notify subscribers about the identity of the resource that changed. When you receive this information, you should make a separate GET call to get the details of the data. For basic presence notifications, you receive information about which user's presence changed but no data about the details of user's presence. You can use the [GET presence APIs](/en-us/graph/api/presence-get) to discover the state of the user's availability and activity.

#### Payload example

```json
{
  "value": [{
    "subscriptionId": "{Subscription id}",
    "clientState": "{secret client state}",
    "changeType": "updated",
    "tenantId": "{Organization/Tenant id}",
    "resource": "communications/presences/{id}",
    "subscriptionExpirationDateTime": "2023-09-14T10:00:00.0000000Z",
    "resourceData": {
      "@odata.id": "users/{User Id}/presence",
      "@odata.type": "#microsoft.graph.presence",
      "id": "{User Id}"
    },
    "organizationId": "{Organization/Tenant id}",
  }]
}
```

### Rich presence notifications

Rich notifications notify subscribers about the changes that occurred to a resource. For rich presence notifications, subscribers are notified when the user's `Availability` and `Activity` changes in `encryptedContent.data`. For information about subscribing to rich notifications and decrypting data, see [Set up change notifications that include resource data](/en-us/graph/change-notifications-with-resource-data).

Note

The availability and activity can be the same value.

For more information about possible combinations of availability and activity, see [Presence properties](/en-us/graph/api/resources/presence).

#### Payload example

```json
{
  "value": [{
    "subscriptionId": "{Subscription id}",
    "clientState": "{secret client state}",
    "changeType": "updated",
    "tenantId": "{Organization/Tenant id}",
    "resource": "communications/presences/{id}",
    "subscriptionExpirationDateTime": "2023-09-14T10:00:00.0000000Z",
    "resourceData": {
      "@odata.id": "users/{User Id}/presence",
      "@odata.type": "#microsoft.graph.presence",
      "id": "{User Id}"
    },
    "organizationId": "{Organization/Tenant id}",
    "encryptedContent": {
      "data": "{Encrypted content}",
      "dataSignature": "{Encrypted data signature}",
      "dataKey": "{Encrypted data key for encrypting content}",
      "encryptionCertificateId": "{User specified id of encryption certificate}",
      "encryptionCertificateThumbprint": "{Encrpytion certification thumbprint}"
    }
  }],
  "validationTokens": ["{Validation Tokens}"]
}
```

### Example: Decrypted notifications with resource data

```json
{
    "@odata.id": "users/{User Id}/presence",
    "@odata.type": "#microsoft.graph.presence",
    "id": "{User Id}",
    "availability": "{Availability}",
    "activity": "{Activity}"
}
```