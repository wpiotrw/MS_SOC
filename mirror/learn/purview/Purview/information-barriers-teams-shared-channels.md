---
layout: Conceptual
title: Information Barriers and shared channels | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/information-barriers-teams-shared-channels
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article explains how Information Barriers support in Microsoft Teams with Shared Channels.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.date: 2026-03-30T00:00:00.0000000Z
ms.topic: article
ms.service: purview
ms.subservice: purview-information-barriers
audience: Admin
ms.collection:
- purview-compliance
- M365-collaboration
search.appverid: MET150
f1.keywords:
- NOCSH
ms.custom: information-barriers
ai-usage: ai-assisted
locale: en-us
document_id: 4bbb6ed9-a6d7-9ee9-5294-8a72aa029aef
document_version_independent_id: 4bbb6ed9-a6d7-9ee9-5294-8a72aa029aef
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/information-barriers-teams-shared-channels.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: information-barriers-teams-shared-channels
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/information-barriers-teams-shared-channels.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: b4c6584d-6dbe-8c8b-9571-e21a4694a60d
---

# Information Barriers and shared channels | Microsoft Learn

[Shared channels](/en-us/microsoftteams/shared-channels?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) in Microsoft Teams create collaboration spaces where you can invite people who aren't in the team. You implement [Microsoft Purview Information Barriers](information-barriers) policies to restrict and prevent users and groups from communicating with each other within and outside of your organization.

Shared channels are enabled by default in Teams. You can decide if people can create shared channels, share them with people outside your organization, and participate in external shared channels by creating a channel policy. When you create Information Barriers policies in your organization, Teams performs checks when configuring shared channels to verify that none of the existing channel members and any new users added to the shared channel violate Information Barriers policy conditions.

Use the following table to understand how Information Barriers policies affect communications and result in specific behaviors when configuring shared channels:

| Scenario | Information Barriers behavior |
| --- | --- |
| **Share a channel with a user in your organization** | If an Information Barriers policy prevents the user from communicating with shared channel members, the user doesn't appear in the user search and the channel isn't shared with the team.  If an Information Barriers policy prevents adding the user, you see the following message: *We didn't find any matches. Talk to your IT admin about expanding the scope of your search.* |
| **Share a channel in your organization with another team that you own** | If an Information Barriers policy prevents users in the other team from communicating with shared channel members, the channel isn't shared with the team.  If an Information Barriers policy prevents communications, you see the following message: *The channel can't be shared with this team. Pick another team or contact your admin for more info.* |
| **Share a channel in your organization with another team that you don't own** | If an Information Barriers policy prevents the team owner or any users of the other team from communicating with shared channel members, the channel can't be shared with the team.  If an Information Barriers policy prevents communications, you see the following message: *The channel can't be shared with this team. Pick another team or contact your admin for more info.* |
| **Add a new user to the team when the team has shared channels with other teams** | If an Information Barriers policy prevents the new user from communicating with members of the shared channel team, the user can't be added to the team. When you add a user to a team with six or more shared channels, you immediately add the user to the channel and support sharing. Sharing for the team and the previously shared channels stops if an Information Barriers policy finds the new user to be non-compliant. If an Information Barriers policy prevents adding the user, you see the following message: *Unable to add user due to an Information Barriers policy.* |
| **Share a channel with an external team** | Information Barriers policies on internal and external organizations don't restrict communications between users from the different organizations. You can share shared channels with external guests. |