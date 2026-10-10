---
layout: Conceptual
title: Change notifications for Microsoft Teams resources - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/teams-change-notification-in-microsoft-teams-overview
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: anandab-msft
ms.author: MSGraphDocsVteam
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: teams
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: how-to
description: Subscribe to resource and resource data changes in Microsoft Teams using the Microsoft Graph API. Learn about change notification types and payloads.
ms.localizationpriority: high
ms.custom: scenarios:getting-started
ms.date: 2026-03-16T00:00:00.0000000Z
locale: en-us
document_id: 21ab1d41-2c00-5ae0-de45-0cae5e34467e
document_version_independent_id: 0869760b-8852-d5af-b219-2523ea9f5618
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/teams-change-notification-in-microsoft-teams-overview.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: teams-change-notification-in-microsoft-teams-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/teams-change-notification-in-microsoft-teams-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: d4683f03-53e1-21c6-13ed-81fea3ab895a
---

# Change notifications for Microsoft Teams resources - Microsoft Graph | Microsoft Learn

Change notifications for Microsoft Teams resources using Microsoft Graph enable you to subscribe to a resource's changes (create, update, and delete). Change notifications provide a low latency model, allowing you to maintain a [subscription](/en-us/graph/api/resources/change-notifications-api-overview). You can also get the resource data in the notifications and avoid calling the API to get the payload.

Note

The maximum time a subscription can last is 60 minutes; however, subscriptions can be renewed until the caller has permission to access the resource.

## Change notification types

Microsoft Teams supports two types of change notifications:

- **Change notification to track all changes related to a resource across the tenant:** For example, you can subscribe to changes in messages in any channel across the tenant and get notified whenever a message is created, updated, or deleted in any channel in the tenant.
- **Change notification to track all changes for a specific resource:** For example, you can subscribe to changes in messages in a particular channel and get notified whenever a message is created, updated, or deleted.

For details about which resources support which types of change notifications, see [Microsoft Graph change notifications](change-notifications-overview).

## Supported resources

The following table lists the Microsoft Teams resources that support change notifications and their corresponding resource paths. Apply the resource path for your scenario as specified when [creating a subscription](/en-us/graph/api/subscription-post-subscriptions). The type of the resource path payload is the type under the "Resource" column or a collection of that type.

| **Resource** | **Supported resource paths** | **Resource data can be included in notifications** |
| --- | --- | --- |
| Teams [callRecording] | **Online meetings:**All recordings in an organization: `communications/onlineMeetings/getAllRecordings`All recordings for a specific meeting: `communications/onlineMeetings/{onlineMeetingId}/recordings`A call recording that becomes available in a meeting organized by a specific user: `users/{userId}/onlineMeetings/getAllRecordings`A call recording that becomes available in a meeting where a particular Teams app is installed: `appCatalogs/teamsApps/{id}/installedToOnlineMeetings/getAllRecordings`**Ad hoc calls, including PSTN, 1:1, and group calls:**All recordings in an organization: `communications/adhocCalls/getAllRecordings`All recordings for a specific ad hoc call: `communications/adhocCalls/{adhocCallId}/recordings`A call recording that becomes available to a specific user that initiated call recording: `users/{userId}/adhocCalls/getAllRecordings` | Yes |
| Teams [callTranscript](/en-us/graph/api/resources/calltranscript) | **Online meetings:**All transcripts in an organization: `communications/onlineMeetings/getAllTranscripts` All transcripts for a specific meeting: `communications/onlineMeetings/{onlineMeetingId}/transcripts`A call transcript that becomes available in a meeting organized by a specific user: `users/{userId}/onlineMeetings/getAllTranscripts` A call transcript that becomes available in a meeting where a particular Teams app is installed: `appCatalogs/teamsApps/{id}/installedToOnlineMeetings/getAllTrancripts`**Ad hoc calls, including PSTN, 1:1, and group calls:**All transcripts in an organization: `communications/adhocCalls/getAllTranscripts` All transcripts for a specific ad hoc call: `communications/adhocCalls/{adhocCallId}/transcripts`A call transcript that becomes available to a specific user that initiated call transcription: `users/{userId}/adhocCalls/getAllTranscripts` | Yes |
| Teams [channel](/en-us/graph/api/resources/channel) | Changes to channels in all teams:`/teams/getAllChannels`Changes to channel in a specific team:`/teams/{id}/channels` | Yes |
| Teams [chat](/en-us/graph/api/resources/chat) | Changes to any chat in the tenant:`/chats`Changes to a specific chat:`/chats/{id}`Changes to any chat in the tenant where a particular Teams app is installed:`/appCatalogs/teamsApps/{id}/installedToChats` | Yes |
| Teams [chatMessage](/en-us/graph/api/resources/chatMessage) | Changes to chat messages in all channels in all teams:`/teams/getAllMessages`Changes to chat messages in a specific channel:`/teams/{id}/channels/{id}/messages`Changes to chat messages in all chats:`/chats/getAllMessages`Changes to chat messages in a specific chat:`/chats/{id}/messages`Changes to chat messages in all chats a particular user is part of:`/users/{id}/chats/getAllMessages`Changes to chat messages in all the chats in the tenant where a particular Teams app is installed:`/appCatalogs/teamsApps/{id}/installedToChats/getAllMessages` | Yes |
| Teams [conversationMember](/en-us/graph/api/resources/conversationMember) | Changes to membership in a specific team:`/teams/{id}/members` Changes to membership in a specific chat:`/chats/{id}/members` Changes to membership in all chats:`/chats/getAllMembers` Changes to membership in all channels under a specific team:`teams/{id}/channels/getAllMembers`Changes to membership in all the chats in the tenant where a particular Teams app is installed:`/appCatalogs/teamsApps/{id}/installedToChats/getAllMembers` Changes to membership in all channels across the tenant:`teams/getAllChannels/getAllMembers` | Yes |
| Teams [team](/en-us/graph/api/resources/team) | Changes to any team in the tenant:`/teams`Changes to a specific team:`/teams/{id}` | Yes |
| Teams [teamsAppInstallation](/en-us/graph/api/resources/teamsappinstallation) | Changes when a particular Teams app is installed, upgraded, or deleted:`/appCatalogs/teamsApps/{teams-app-id}/installations` | Yes |

## Notification payloads

You can get the notification with or without resource data, depending on your subscription. Subscribing with resource data lets you get the message payload and the notification, removing the need to call back and get the content.

### Notifications with resource data

For notifications with resource data, the payload looks like the following. This payload is for a notification corresponding to the chat message resource. The actual notification includes the **resource** and **resourceData** properties, which represent the resource that has triggered the notification.

```json
{
    "value": [{
        "subscriptionId": "10493aa0-4d29-4df5-bc0c-ef742cc6cd7f",
        "changeType": "created",
        "clientState": "<<--SpecifiedClientState-->>",
        "subscriptionExpirationDateTime": "2021-02-02T10:30:34.9097561-08:00",
        "resource": "chats('19:8ea0e38b-efb3-4757-924a-5f94061cf8c2_97f62344-57dc-409c-88ad-c4af14158ff5@unq.gbl.spaces')/messages('1612289765949')",
        "resourceData": {
            "id": "1612289765949",
            "@odata.type": "#Microsoft.Graph.chatMessage",
            "@odata.id": "chats('19:8ea0e38b-efb3-4757-924a-5f94061cf8c2_97f62344-57dc-409c-88ad-c4af14158ff5@unq.gbl.spaces')/messages('1612289765949')"
        },
        "encryptedContent": {
            "data": "<<--EncryptedContent-->",
            "dataKey": "<<--EnryptedDataKeyUsedForEncryptingContent-->>",
            "encryptionCertificateId": "<<--IdOfTheCertificateUsedForEncryptingDataKey-->>",
            "encryptionCertificateThumbprint": "<<--ThumbprintOfTheCertificateUsedForEncryptingDataKey-->>"
        },
        "tenantId": "<<--TenantForWhichNotificationWasSent-->>"
    }],
    "validationTokens": ["<<--ValidationTokens-->>"]
}
```

For details about validating tokens and decrypting the payload, see [Set up change notifications that include resource data](change-notifications-with-resource-data).

The decrypted notification payload looks like the following. The decrypted payload for the previous example conforms to the [chatMessage](/en-us/graph/api/resources/chatMessage) schema. The payload is similar to that returned by GET operations.

```json
{
  "id": "1612289992105",
  "replyToId": null,
  "etag": "1612289992105",
  "messageType": "message",
  "createdDateTime": "2021-02-02T18:19:52Z",
  "lastModifiedDateTime": "2021-02-02T18:19:52.105Z",
  "lastEditedDateTime": null,
  "deletedDateTime": null,
  "subject": null,
  "summary": null,
  "chatId": "19:8ea0e38b-efb3-4757-924a-5f94061cf8c2_97f62344-57dc-409c-88ad-c4af14158ff5@unq.gbl.spaces",
  "importance": "normal",
  "locale": "en-us",
  "webUrl": null,
  "from": {
    "application": null,
    "device": null,
    "user": {
      "id": "8ea0e38b-efb3-4757-924a-5f94061cf8c2",
      "displayName": "Ramjot Singh",
      "userIdentityType": "aadUser"
    },
    "conversation": null
  },
  "body": {
    "contentType": "text",
    "content": "test"
  },
  "channelIdentity": null,
  "attachments": [],
  "mentions": [],
  "policyViolation": null,
  "reactions": [],
  "replies": [],
  "hostedContents": []
}
```

### Notifications without resource data

Notifications without resource data give you enough information to make GET calls to get the resource. Subscriptions for notifications without resource data don't require an encryption certificate (because actual resource data isn't sent over).

The payload looks like the following. This payload is for a message sent in a channel.

```json
{
  "subscriptionId": "9f9d1ed0-c9cc-42e7-8d80-a7fc4b0cda3c",
  "changeType": "created",
  "tenantId": "<<--TenantForWhichNotificationWasSent-->>",  
  "clientState": "<<--SpecifiedClientState-->>",
  "subscriptionExpirationDateTime": "2021-02-02T11:26:41.0537895-08:00",
  "resource": "teams('fbe2bf47-16c8-47cf-b4a5-4b9b187c508b')/channels('19:4a95f7d8db4c4e7fae857bcebe0623e6@thread.tacv2')/messages('1612293113399')",
  "resourceData": {
    "id": "1612293113399",
    "@odata.type": "#Microsoft.Graph.chatMessage",
    "@odata.id": "teams('fbe2bf47-16c8-47cf-b4a5-4b9b187c508b')/channels('19:4a95f7d8db4c4e7fae857bcebe0623e6@thread.tacv2')/messages('1612293113399')"
  }
}
```

The previous example shows a notification corresponding to a chat message resource. The actual notification includes the **resource** and **resourceData** properties, which represent the resource that has triggered the notification. The **resource** and **@odata.id** properties can be used to make calls to Microsoft Graph to get the payload of the resource.

Note

GET calls always return the current state of the resource. If the resource is changed between when the notification is sent and when the resource is retrieved, the operation returns the updated resource.