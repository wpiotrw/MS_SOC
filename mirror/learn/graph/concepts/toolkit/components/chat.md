---
layout: Conceptual
title: Chat component in Microsoft Graph Toolkit - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/toolkit/components/chat
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: sebastienlevert
ms.author: MSGraphDocsVteam
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: non-product-specific
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: article
description: The Chat component enables the user to have 1:1 or group conversations.
ms.localizationpriority: medium
ms.date: 2024-11-07T00:00:00.0000000Z
locale: en-us
document_id: 66ba2425-6c32-2d15-ab9f-34bc16c296da
document_version_independent_id: 66ba2425-6c32-2d15-ab9f-34bc16c296da
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/toolkit/components/chat.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: ../../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: toolkit/components/chat
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/toolkit/components/chat.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 94e9c822-2a0f-fa62-f582-845babbe40ba
---

# Chat component in Microsoft Graph Toolkit - Microsoft Graph | Microsoft Learn

Caution

The Microsoft Graph Toolkit is deprecated. The retirement period begins September 1, 2025, with full retirement planned for August 28, 2026. Developers should migrate to using the Microsoft Graph SDKs or other supported Microsoft Graph tools for building web experiences. For more information, see the [deprecation announcement](https://devblogs.microsoft.com/microsoft365dev/microsoft-graph-toolkit-retirement/).

Note

This component is in preview and is subject to change. The use of these components in production applications is not supported. This component is currently only available as a React component and doesn't have a web component equivalent.

The chat component enables the user to have 1:1 or group conversations. This component doesn't support channel conversations. The component allows for rendering conversations and authoring new messages. All data is stored in Microsoft Teams.

## Example

The following example displays a conversation using the `mgt-chat` component.

![A screenshot of a chat component](images/mgt-chat.png)

## Properties

| Attribute | Property | Description |
| --- | --- | --- |
| chat-id | chatId | A string ID to set the 1:1 or group [conversation](/en-us/graph/api/resources/chat) to render. Required. |

## CSS custom properties

The `mgt-chat` component doesn't define CSS custom properties.

## Events

The `mgt-chat` component doesn't offer any events.

## Templates

The `mgt-chat` component doesn't offer templates to override.

## Microsoft Graph permissions

This control uses the following Microsoft Graph APIs and permissions.

| Configuration | Permission | API |
| --- | --- | --- |
| `chatId` is set | Chat.ReadBasic, Chat.Read, ChatMessage.Read, Chat.ReadWrite, ChatMember.ReadWrite | [/chats/{id}/messages](/en-us/graph/api/chat-list-messages), [/chats/{id}/messages](/en-us/graph/api/chat-post-messages), [/chats/{id}/messages/{messageId}](/en-us/graph/api/chatmessage-update), [/me/chats/{id}/messages/{messageId}/softDelete](/en-us/graph/api/chatmessage-softdelete), [/chats/{id}/members/{membershipId}](/en-us/graph/api/chat-delete-members), [/chats/{id}/members](/en-us/graph/api/chat-post-members), [/chats/{id}/messages/{messageId}/hostedContents/{hostedContentId}](/en-us/graph/api/chatmessagehostedcontent-get), [/chats/{id}](/en-us/graph/api/chat-patch) |

### Subcomponents

The `mgt-chat` component consists of one or more subcomponents that might require other permissions than the ones listed previously. For more information, see the documentation for each subcomponent:

- [mgt-person](person)
- [mgt-people-picker](people-picker)

## Authentication

The `mgt-chat` component uses the global authentication provider described in the [authentication documentation](../providers/providers).

## Cache

The `mgt-chat` component caches chat messages and related metadata.

## Localization

The `mgt-chat` component doesn't expose any localization variables.

## Known issues

- The `mgt-chat` component doesn't support the same `chatId` being used in multiple instances of the component or across multiple tabs.
- The `mgt-chat` component doesn't support theming and won't respect browsers preferences.