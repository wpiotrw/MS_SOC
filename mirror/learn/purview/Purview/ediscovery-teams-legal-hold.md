---
layout: Conceptual
title: Place a Microsoft Teams user or team on legal hold | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-teams-legal-hold
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn to place a Microsoft Teams user or team on legal hold using the Microsoft Purview portal and learn what needs a legal hold based on data requirements.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.topic: article
ms.service: purview
ms.subservice: purview-ediscovery
audience: admin
ms.collection:
- purview-compliance
- M365-collaboration
- ediscovery
ms.reviewer: anwara
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
search.appverid: MET150
f1.keywords:
- NOCSH
locale: en-us
document_id: affefcd9-9dab-6f96-92be-310aefaff342
document_version_independent_id: affefcd9-9dab-6f96-92be-310aefaff342
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-teams-legal-hold.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-teams-legal-hold
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-teams-legal-hold.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 0828ef55-5207-5e58-91dd-350cf92781a5
---

# Place a Microsoft Teams user or team on legal hold | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

When a reasonable expectation of litigation exists, organizations are required to preserve electronically stored information (ESI), including Teams chat messages that are relevant to the case. Organizations may need to preserve all messages related to a specific investigation or for a specific person. This article will discuss using a legal hold to preserve content in Microsoft Teams. To preserve content in other services in Microsoft 365, see [Create an eDiscovery hold](ediscovery-create-holds).

Note

Private channel chats are stored in user mailboxes, while standard channel chats are stored in the mailbox associated with the parent team. If there is already a legal hold in place for a user mailbox, the hold policy will now automatically apply to private channel messages stored in that mailbox. There is no further action needed for an admin to turn this on. Legal hold of files shared in private channels is also supported.

Within Microsoft Teams, an entire team or select users can be put on legal hold. Doing that will make sure that all messages that were exchanged in those teams (including private and shared channels) or messages exchanged by those individuals are discoverable by the organization's compliance managers or Teams Admins.

Note

Placing a user on hold does not automatically place a group on hold or vice-versa. Notifications sent in activity feeds can't be placed on hold.

To put a user or a team on legal hold, use the following guidance:

- [Create a hold in eDiscovery (Standard)](ediscovery-create-holds#how-to-create-an-ediscovery-hold)
- [Create and manage a hold in eDiscover (Premium)](ediscovery-managing-holds)

Important

When a user or group is placed on hold, all compliance copies of messages are preserved. For example, if a user posts a message in a channel and then modifies the message, both copies of the message are preserved. Without the hold, only the latest message is preserved.

## Content locations to place on hold to preserve Teams content

As a helpful guide, use the following table to understand what content locations (such as a mailbox or a site) to place on hold to preserve different types of Teams content.

| **Scenario** | **Content location** |
| --- | --- |
| Chat messages for a user (for example, 1:1 chats, 1:N group chats, and private channel conversations) | User mailbox |
| Chat messages in standard and shared channels | Mailbox associated with the parent team |
| Files in standard channels (for example, Wiki content and files) | SharePoint site associated with the parent team |
| Files in private and shared channels | Dedicated SharePoint site associated with the channel |
| User's private content | The user's OneDrive for Business account |
| Card content in chats | User mailbox for 1:1 chats, 1:N group chats, and private channel conversations; the parent team mailbox for card content in standard and shared channel messages. For more information, see the "Preserve card content" section in [Create an eDiscovery hold](ediscovery-create-holds#preserve-card-content). |
|  |  |

Note

To retain message content in private channels, you need to put the user mailboxes (of the members of a private channel) on hold. and when using eDiscovery tool to search private channel messages, you have to search the user's mailbox. As was stated earlier, private channel chats are stored in user mailboxes, not in the group mailbox associated with the parent team.