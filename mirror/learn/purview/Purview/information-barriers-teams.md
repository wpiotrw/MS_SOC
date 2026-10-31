---
layout: Conceptual
title: Information Barriers in Microsoft Teams | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/information-barriers-teams
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article explains how Information Barriers are supported in Microsoft Teams.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.date: 2026-06-01T00:00:00.0000000Z
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
ms.custom:
- seo-marvel-apr2020
- sfi-image-nochange
ai-usage: ai-assisted
locale: en-us
document_id: 8b59a4cd-e139-6678-42eb-5b2ec76ea8ff
document_version_independent_id: 8b59a4cd-e139-6678-42eb-5b2ec76ea8ff
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/information-barriers-teams.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: information-barriers-teams
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/information-barriers-teams.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: d8903370-1aaa-9a21-704f-bbccc546df88
---

# Information Barriers in Microsoft Teams | Microsoft Learn

[Microsoft Purview Information Barriers](information-barriers) (IBs) are policies that prevent individuals or groups from communicating with each other. This article covers IB behavior in Microsoft Teams, including shared channels. For more information about shared channels and Information Barriers behavior, see [Information Barriers and shared channels](information-barriers-teams-shared-channels).

For Microsoft Teams, Information Barriers can determine and prevent the following kinds of unauthorized collaborations:

- Adding a user to a team or channel
- User access to team or channel content
- User access to 1:1 and group chats
- User access to meetings
- Prevents lookups and discovery, users aren't visible in the people picker.

Note

- You can't create IB groups across tenants.
- Version 1 doesn't support using bots, Microsoft Entra apps, or APIs to send activity feed notifications, and it doesn't support some APIs to add users.
- Private channels comply with Information Barriers policies that you configure.
- For information about support for barriers for SharePoint sites that are connected to Teams, see [Segments associated with Microsoft Teams sites](information-barriers-sharepoint#view-and-manage-segments-as-an-administrator).

## Background

The primary driver for Information Barriers is the financial services industry, where the Financial Industry Regulatory Authority ([FINRA](https://www.finra.org)) reviews IBs and conflicts of interest within member firms ([Debt Research Regulatory Notice 15-31](https://www.finra.org/sites/default/files/Regulatory-Notice-15-31_0.pdf)). However, IBs are useful across many industries including education, legal, government, and professional services. For more information about IB scenarios, see [Learn about Information Barriers](information-barriers).

## When to use Information Barriers

Use IBs in situations like these:

- You need to prevent a team from communicating or sharing data with a specific other team.
- You need to prevent a team from communicating or sharing data with anyone outside of the team.

The Information Barrier Policy Evaluation Service determines whether a communication complies with IB policies.

## Manage segments and policies

Manage IB segments and policies in the [Microsoft Purview portal](purview-portal) or by using PowerShell cmdlets. For full guidance, see [Get started with Information Barriers](information-barriers-policies) and [Manage Information Barriers policies](information-barriers-edit-segments-policies).

Important

Support for 5,000 segments and assigning users to multiple segments is only available when your organization isn't in *Legacy* mode. Assigning users to multiple segments requires extra steps to change the Information Barriers mode for your organization. For more information, see [Use multi-segment support in Information Barriers](information-barriers-multi-segment).

For organizations in *Legacy* mode, the maximum number of segments supported is 250, and users are restricted to being assigned to only one segment. Organizations in *Legacy* mode are eligible to upgrade to the newest version of Information Barriers in the future. For more information, see the [Information Barriers roadmap](https://www.microsoft.com/microsoft-365/roadmap?filters=&amp;searchterms=information%2Cbarriers).

Important

Before you set up or define policies, you must enable scoped directory search in Microsoft Teams. Wait at least a few hours after enabling scoped directory search before you set up or define policies for IB. For more information, see [Define IB policies](information-barriers-policies#required-subscriptions-and-permissions).

## Information Barriers administrator role

The IB Compliance Management role is responsible for managing IB policies. For more information about this role, see [Permissions in the Microsoft Purview portal](purview-permissions).

## Information barrier triggers

IB policies activate when the following Teams events take place:

- **Add members to a team**: Whenever you add a user to a team, the system evaluates the user's policy against the IB policies of other team members. After the user is successfully added, the user can perform all functions in the team without further checks. If the user's policy blocks them from being added to the team, the user doesn't show up in search.

    ![Screenshot of searching for a new member to add to a team and finding no matches.](media/information-barriers-add-members.png)
- **Request a new chat**: Each time that a user requests a new chat with one or more other users, the system evaluates the chat to make sure that it isn't violating any IB policies. If the conversation violates an IB policy, the conversation isn't started.

    Here's an example of a 1:1 chat.

    ![Screenshot showing blocked communication in 1:1 chat.](media/information-barriers-one-one-chat.png)

    Here's an example of a group chat.

    ![Screenshot showing group chat.](media/information-barriers-group-chat.png)
- **Invite a user to join a meeting**: When you invite a user to join a meeting, the system evaluates the IB policy that applies to the user against the IB policies that apply to the other team members. If there's a violation, the user isn't allowed to join the meeting.

    ![Screenshot showing user blocked from meeting.](media/information-barriers-meeting.png)
- **Share a screen between two or more users**: When a user shares a screen with other users, the system evaluates the sharing to make sure that it doesn't violate the IB policies of other users. If an IB policy is violated, the screen share isn't allowed.

    Here's an example of screen share before the policy is applied.

    ![Screenshot showing a user chat.](media/ib-before-screen-share-policy.png)

    Here's an example of screen share after the policy is applied. The screen share and call icons aren't visible.

    ![Screenshot showing user char with blocked settings.](media/ib-after-screen-share-policy.png)
- **Place a phone call in Teams**: Whenever a user initiates a voice call (via VOIP) to another user or group of users, the system evaluates the call to make sure that it doesn't violate the IB policies of other team members. If there's any violation, the voice call is blocked.
- **Guests in Teams**: IB policies apply to guests in Teams, too. If guests need to be discoverable in your organization's global address list, see [Manage guest access in Microsoft 365 Groups](/en-us/microsoft-365/admin/create-groups/manage-guest-access-in-groups?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json). After guests are discoverable, you can [define IB policies](information-barriers-policies).

## How policy changes impact existing chats

When the IB policy administrator changes a policy or activates a policy change because of a change to a user's profile (such as for a job change), the Information Barrier Policy Evaluation Service automatically searches the members to ensure that their membership in the team doesn't violate any policies.

If users have an existing chat or other communication, and you set a new policy or change an existing policy, the service evaluates existing communications to make sure that the communications are still allowed.

- **1:1 chat**: If communication between two users is no longer allowed (because of application to one or both users of a policy that blocks communication), the service blocks further communication. Their existing chat conversations become read-only.

    Here's an example that shows the chat is visible.

    ![Screenshot showing user chat is available.](media/ib-before-chat-contacts-policy.png)

    Here's an example that shows the chat is disabled.

    ![Screenshot showing user chat is disabled.](media/ib-after-1-1chat-policy.png)
- **Group chat**: If communication from one user to a group is no longer allowed (for example, because a user changed jobs), the service removes the user, along with the other users whose participation violates the policy, from group chat, and blocks further communication with the group. The user can still see old conversations, but can't see or participate in any new conversations with the group. If the new or changed policy that prevents communication is applied to more than one user, the service removes the users who are affected by the policy from group chat. They can still see old conversations.

    In this example, Enrico moves to a different department within the organization and is removed from the group chat.

    ![Screenshot of a group chat from which a user has been removed.](media/information-barriers-user-changes-job.png)

    Enrico can no longer send messages to the group chat.

    ![Screenshot of not being able to send messages to group chat because the user was removed from the group.](media/information-barriers-user-changes-job-2.png)
- **Team**: The service removes any users who are removed from the group from the team and they can't see or participate in existing or new conversations.

## Scenario: A user in an existing chat becomes blocked

Currently, users experience the following scenarios if an IB policy blocks another user:

- **People tab**: A user can't see blocked users on the **People** tab.
- **People Picker**: Blocked users aren't visible in the people picker.

    ![Screenshot of Teams alerting the user that policy prevents display of another user's information.](media/information-barriers-people-picker.png)
- **Activity tab**: If a user visits the **Activity** tab of a blocked user, no posts appear. (The **Activity** tab displays channel posts only, and there are no common channels between the two users.)

    Here's an example of the activity tab view that is blocked.

    ![Screenshot showing the activity tab that is blocked.](media/ib-after-activity-tab-policy.png)
- **Org charts**: If a user accesses an org chart on which a blocked user appears, the blocked user doesn't appear on the org chart. Instead, an error message appears.
- **People card**: If a user participates in a conversation and the user is later blocked, other users see an error message instead of the people card when they hover over the blocked user's name. Actions listed on the card (such as calling and chat) are unavailable.
- **Suggested contacts**: Blocked users don't appear on the suggested contacts list (the initial contact list that appears for new users).
- **Chat contacts**: A user can see blocked users on the chats contact list, but the blocked users are identified. The only action that the user can perform on the blocked users is to delete them. The user can also select them to view their past conversation.
- **Calls contacts**: A user can see blocked users on the calls contact list, but the blocked users are identified. The only action that the user can perform on the blocked users is to delete them.

    Here's an example of a blocked user in the calls contact list.

    ![Screenshot showing user chat.](media/ib-before-chat-contacts-policy.png)
- **Skype to Teams migration**: During a migration from Skype for Business to Teams, the migration process includes all users—even those users who are blocked by IB policies. The migration process handles those users as described previously.

    Here's an example of a blocked user in the calls contact list.

    ![Screenshot showing user chat.](media/ib-before-chat-contacts-policy.png)

    Here's an example of the chat being disabled for a user on the calls contact list.

    ![Screenshot showing user blocked from chat.](media/ib-after-1-1chat-policy.png)

## Teams policies and SharePoint sites

When you create a team, you also create and associate a SharePoint site with Microsoft Teams for the files experience. Information barrier policies don't apply to this SharePoint site and its files by default. To enable Information Barriers in SharePoint and OneDrive, follow the guidance and steps in the [Use Information Barriers with SharePoint](information-barriers-sharepoint#enable-sharepoint-and-onedrive-information-barriers-in-your-organization) article.

## Information barrier modes and Teams

Information barrier modes help control who you can add to or remove from a Team. When you use Information Barriers with Teams, the following IB modes are supported:

- **Open**: This configuration is the default IB mode for all existing groups that were provisioned before Information Barriers were enabled. In this mode, no IB policies apply.
- **Implicit**: This configuration is the default IB mode when you provision a Team after enabling Information Barriers. *Implicit* mode allows you to add all compatible users in the group.
- **Owner Moderated**: This mode is set on a team when you want to allow collaboration between incompatible segment users that the owner moderates. The team owner can add new members per their IB policy.

Teams created before activating an IB policy in your tenant are automatically set to *Open* mode by default. When you activate IB policies on your tenant, you must update mode of your existing teams to *Implicit* to ensure that existing teams are IB-compliant. For more information about updating modes, see [Change Information Barriers modes with a PowerShell script](information-barriers-teams-powershell-script).

Use the [Set-UnifiedGroup](/en-us/powershell/module/exchange/set-unifiedgroup?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) cmdlet with the *InformationBarrierMode* parameter that corresponds to the mode you want to use for your segments. The allowed values for the *InformationBarrierMode* parameter are *Open*, *Implicit*, and *Owner Moderated*.

For example, to configure *Implicit* mode for a Microsoft 365 Group, use the following PowerShell command:

```powershell
Set-UnifiedGroup -InformationBarrierMode Implicit
```

To update the mode from *Open* to *Implicit* for all existing teams, use this [PowerShell script](information-barriers-teams-powershell-script).

If you change the *Open* mode configuration on existing Teams-connected groups to meet compliance requirements for your organization, you need to [update the IB modes](information-barriers-sharepoint#view-and-manage-ib-modes-as-an-administrator-with-sharepoint-powershell) for associated SharePoint sites connected to the Teams team.

## IB policy application in Teams

The IB policy application is a background IB processor for Teams that gets a notification when there are changes to either users (policy or segment changes) or groups (mode changes). The following steps outline the processing flow:

- The policy application receives a group change notification when mode is updated and retrieves the message thread and Group IDs applicable to the update.
- If the message thread exists, the application schedules processing and fetches all members from the team. It sends the underlying group and members to downstream Teams components for IB evaluation.
- The application evaluates the mode on the group and the IB policies per user and sends the results to the policy application.
- The policy application removes the non-compliant users from the group and team.

## Required licenses and permissions

For more information about licenses and permissions, plans, and pricing, see the [subscription requirements](https://aka.ms/M365EnterprisePlans) for Information Barriers.

## Usage notes

- **Users can't join any scheduled meetings**: If you enable IB policies, users can't join meetings if the meeting chat roster reaches its current limit of 1,000 users. IB checks rely on whether a user can be added to the meeting chat roster - only users who can be added are allowed to join the meeting. Every meeting in an IB-enabled tenant performs IB checks at the point of entry, even if the meeting organizer isn't explicitly covered by IB policies.

    Teams also enforces a separate meeting limit of 1,000 users. If you enable overflow, additional participants can join as view-only attendees. View-only participants aren't subject to IB policy checks. If you invite a large audience (for example, more than 1,000 users), Teams pre-adds 750 users to the meeting chat before the meeting starts. This process reserves room for about 250 additional users who actually join the meeting. Because pre-added users count toward the chat roster limit even if they never join the meeting, the chat roster can reach capacity before the meeting attendance limit is met. For recurring meetings, the roster can fill quickly, as any user who joins once remains on the roster for future occurrences. After the 1,000-user chat roster limit is reached, you can't add more users to the meeting.

    A short-term solution is to remove inactive members from the meeting chat roster to make space for new users or keep the chat disabled until the meeting begins and enable it only when needed. This solution helps align the chat participant count more closely with the meeting participant count. Regular Teams meetings work best for audiences of fewer than 1,000 expected attendees. For larger audiences, use [Teams Town hall](/en-us/microsoftteams/plan-town-halls?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) for a smoother experience.
- **Users can't join channel meetings**: If you enable IB policies, users can't join channel meetings if they're not a member of the team. The root cause is that IB checks rely on whether users can be added to a meeting chat roster, and only when they can be added to the roster are they allowed to join the meeting. The chat thread in a channel meeting is available to Team/Channel members only, and non-members can't see or access the chat thread. If you enable IB for the organization and a non-team member attempts to join a channel meeting, that user isn't allowed to join the meeting. However, if you don't enable IB for the organization and a nonteam member attempts to join a channel meeting, the user is allowed to join the meeting but they don't see the chat option in the meeting.
- **IB policies are supported in federated communication**: If you allow federation with external organizations, the users of those organizations aren't restricted by IB policies. If users of your organization join a group chat, meeting chat, or a call organized by external federated users, IB policies continue to restrict communication between users of your organization.