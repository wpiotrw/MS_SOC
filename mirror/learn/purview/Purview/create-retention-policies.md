---
layout: Conceptual
title: Automatically retain or delete content by using retention policies | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/create-retention-policies
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-06-09T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-lifecycle-management
ms.collection:
- purview-compliance
- m365copilot
- SPO_Content
ms.custom: admindeeplinkCOMPLIANCE
search.appverid:
- MOE150
- MET150
description: Use a retention policy to efficiently keep control of the content that users generate with email, documents, conversations, and call logs. Keep what you want and get rid of what you don't.
locale: en-us
document_id: 6fa39581-99b9-edb4-54e3-169016724c1a
document_version_independent_id: 6fa39581-99b9-edb4-54e3-169016724c1a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/create-retention-policies.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: create-retention-policies
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/create-retention-policies.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: bd8b4da3-9d50-5f62-1cde-b6a2069e2623
---

# Automatically retain or delete content by using retention policies | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use a retention policy to manage the data for your organization by deciding proactively whether to retain content, delete content, or retain and then delete the content.

A retention policy lets you do this very efficiently by assigning the same retention settings at the container level to be automatically inherited by content in that container. For example, all items in SharePoint sites, all email messages in users' Exchange mailboxes, all channel messages for teams that are used with Microsoft Teams. If you're not sure whether to use a retention policy at the container level or a retention label at the item level, see [Retention policies and retention labels](retention#retention-policies-and-retention-labels).

For more information about retention policies and how retention works in Microsoft 365, see [Learn about retention policies and retention labels](retention).

Note

The information on this page is for compliance administrators. If you are not an administrator and want to understand how retention policies have been configured for the apps that you use, contact your help desk, IT department, or administrator. If you're seeing messages about retention policies in Teams chats and channel messages, you might find it helpful to review [Teams messages about retention policies](https://support.microsoft.com/office/teams-messages-about-retention-policies-c151fa2f-1558-4cf9-8e51-854e925b483b).

## Before you begin

To make sure you have permissions to create and edit retention policies, see the [permissions information for data lifecycle management](get-started-with-data-lifecycle-management#permissions-for-retention-policies-and-retention-labels).

Decide before you create your retention policy whether it will be **adaptive** or **static**. For more information, see [Adaptive or static policy scopes for retention](retention#adaptive-or-static-policy-scopes-for-retention). If you decide to use an adaptive policy, you must create one or more adaptive scopes before you create your retention policy, and then select them during the create retention policy process. For instructions, see [Configuration information for adaptive scopes](purview-adaptive-scopes#configure-adaptive-scopes).

To retain prompts and responses for AI apps other than Microsoft 365 Copilot and Copilot Studio, you must first have a collection policy for these AI apps, and that policy includes the setting to capture content. For more information, see [Collection Policies solution overview](collection-policies-solution-overview).

If you're creating a retention policy for Teams and use [private channels](/en-us/microsoftteams/private-channels), make sure you're aware of the [migration of private channel messages in 2025](retention-policies-teams#migration-of-private-channel-messages-in-2025) so you know whether to select **Teams private channel messages** or **Teams channel messages** as the location.

## Create and configure a retention policy

Although a retention policy can support multiple services that are identified as "locations" in the retention policy, you can't create a single retention policy that includes all the supported locations:

- **Exchange mailboxes**
- **SharePoint sites** or **SharePoint classic and communication sites**
- **OneDrive accounts**
- **Microsoft 365 Group mailboxes & sites**
- **Skype for Business**
- **Exchange public folders**
- **Teams channel messages**
- **Teams chats**
- **Teams private channel messages** (applicable [pre-migration](retention-policies-teams#migration-of-private-channel-messages-in-2025) only)
- **Teams call logs**
- **Microsoft Copilot experiences**
- **Enterprise AI apps**
- **Other AI apps**
- **Viva Engage community messages**
- **Viva Engage user messages**

If you select the Teams or Viva Engage locations when you create a retention policy, the other locations are automatically excluded. This means that the instructions to follow depend on whether you need to include the Teams or Viva Engage locations.

Note

When you use adaptive policies instead of static policies, you can configure a single retention policy to include both Teams and Viva Engage locations. This isn't the case for static policies where Teams and Viva Engage locations require their own retention policy.

When you've more than one retention policy, and when you also use retention labels, see [The principles of retention, or what takes precedence?](retention#the-principles-of-retention-or-what-takes-precedence) to understand the outcome when multiple retention settings apply to the same content.

Select the tab for instructions to create a retention policy for Teams, Copilots, AI apps, Viva Engage, or the other supported services (Exchange, SharePoint, OneDrive, Microsoft 365 Groups, Skype for Business):

# [Retention policy for Teams &amp; AI apps](#tab/teams-retention)
Note

For AI apps other than Microsoft 365 Copilot and Copilot Studio, see Before you begin about the prerequisite of collection policies.

Retention policies for Teams support [shared channels](/en-us/MicrosoftTeams/shared-channels). When you configure retention settings for the **Teams channel message** location, if a team has any shared channels, they inherit retention settings from their parent team.

From late April 2026, retention policies also support newly created Teams call logs when you create the retention policies with PowerShell. For more information, see Retention policy for Teams call logs.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Data Lifecycle Management** &gt; **Policies** &gt; **Retention policies**.
2. Select **New retention policy** to start the **Create retention policy** configuration, and name your new retention policy.
3. For the **Assign admin units** page, keep the default of **Full directory**. Currently, admin units aren't supported for this policy.

1. For the **Choose the type of retention policy to create** page, select **Adaptive** or **Static**, depending on the choice you made from the Before you begin instructions. If you haven't already created adaptive scopes, you can select **Adaptive** but because there won't be any adaptive scopes to select, you won't be able to finish the configuration with this option.
2. Depending on your selected scope:

    - If you chose **Adaptive**: On the **Choose adaptive policy scopes and locations** page, select **Add scopes** and select one or more adaptive scopes that have been created. Then, select one or more locations. The locations that you can select depend on the [scope types](purview-adaptive-scopes#configure-adaptive-scopes) added. For example, if you only added a scope type of **User**, you'll be able to select **Teams chats** but not **Teams channel messages**.
    - If you chose **Static**: On the **Choose locations to apply the policy** page, select one or more locations:

        - **Teams channel message**: Messages from standard and shared channel chats, and standard and shared channel meetings. Includes messages from private channel chats and private channel meetings [post-migration](retention-policies-teams#migration-of-private-channel-messages-in-2025) only.
        - **Teams chats**: For Teams, messages from private 1:1 chats, group chats, meeting chats, and chat with yourself.
        - **Teams private channel messages**: Applicable [pre-migration](retention-policies-teams#migration-of-private-channel-messages-in-2025) only. Messages from private channel chats and private channel meetings. If you select this option, you can't select the other Teams locations in the same retention policy.
        - **Microsoft Copilot experiences**: For built-in and custom Copilot experiences, all user prompts responses. Includes Microsoft 365 Copilot, Security Copilot, Copilot in Fabric, Copilot Studio.
        - **Enterprise AI apps**: For non-Copilot Enterprise AI apps onboarded or connected to your org using methods like Entra registration or data connectors, all user prompts and responses. Includes Entra-registered AI apps, ChatGPT Enterprise, Microsoft Foundry.
        - **Other AI Apps**: For other supported AI apps, all user prompts and responses. includes ChatGPT, Google Gemini, Microsoft Bing, DeepSeek.

        By default, [all teams and all users are selected](retention-settings#a-policy-that-applies-to-entire-locations), but you can refine this by selecting the [**Choose** and **Exclude** options](retention-settings#a-policy-with-specific-inclusions-or-exclusions).
3. For **Decide if you want to retain content, delete it, or both** page, specify the configuration options for retaining and deleting content.

    You can create a retention policy that just retains content without deleting, retains and then deletes after a specified period of time, or just deletes content after a specified period of time. For more information, see [Settings for retaining and deleting content](retention-settings#settings-for-retaining-and-deleting-content).
4. Complete the configuration and save your settings.

For guidance when to use retention policies for Teams and understand the end user experience, see [Manage retention policies for Microsoft Teams](/en-us/microsoftteams/retention-policies) from the Teams documentation.

For technical details about how retention works for Teams and Copilot data, including what elements of messages are supported for retention and timing information with example walkthroughs, see [Learn about retention for Microsoft Teams](retention-policies-teams) and [Learn about retention for Copilot](retention-policies-copilot).

#### Known configuration issues for Teams retention policies

- Although you can select the option to start the retention period when items were last modified, the value of **When items were created** is always used. For messages that are edited, a copy of the original message is saved with its original timestamp to identify when this pre-edited message was created, and the post-edited message has a newer timestamp.
- When you select **Edit** for the Teams chats location, you might see guests and non-mailbox users. Retention policies aren't designed for these users, so don't select them.
- Before late April 2026: Teams call data records (CDRs) for Teams chat and channel messages were included in Teams chat retention policies. Now, CDRs are included only in a retention policy for Teams call logs, as documented in the next section.

#### Retention policy for Teams call logs

Teams call logs represent the collection of call-related data generated by Teams, including call data records (CDRs) and other call metadata. CDRs are also sometimes referred to as call detail records, or just call records.

Prior to supporting the retention of Teams call logs in late April 2026, CDRs for Teams chat and Teams channels were included in retention policies for the Teams chat location. Going forward, new CDRs are supported only when you create a retention policy for Teams call logs. CDRs included in previous Teams chat retention policies continue to be managed by those same policies.

This separate retention policy for call logs can be created and modified only by using PowerShell. It has the following considerations:

- The policy includes call logs for both Teams chat and Teams channels.
- The policy applies only to new call logs that are created after the policy is configured and active.

After you create the retention policy for Teams call logs, it's displayed in **Data Lifecycle Management** &gt; **Policies** in the Microsoft Purview portal, where it's visible but read-only.

To create a retention policy for Teams call logs, first use the [New-AppRetentionCompliancePolicy](/en-us/powershell/module/exchangepowershell/new-appretentioncompliancepolicy) cmdlet. As an example, the following command creates a Teams call log retention policy for all mailboxes:

```powershell
New-AppRetentionCompliancePolicy -Name "<PolicyName>" -Applications "User:MicrosoftTeamsCallLog" -ExchangeLocation "All"
```

Then use the [New-AppRetentionComplianceRule](/en-us/powershell/module/exchangepowershell/new-appretentioncompliancerule) cmdlet to create a retention rule that specifies the retention duration and action. For example, the following command creates a delete-only rule that permanently deletes Teams call log data after one year:

```powershell
New-AppRetentionComplianceRule -Name "<RuleName>" -Policy "<PolicyName>" -RetentionDuration 365 -RetentionDurationDisplayHint Days -RetentionComplianceAction Delete
```

For more information about using PowerShell cmdlets to create and manage retention policies, see [PowerShell cmdlets for retention policies and retention labels](retention-cmdlets).

#### Additional retention policies needed to support Teams

Teams is more than just messages and call logs from chats and channels. If you have teams that were created from a Microsoft 365 group (formerly Office 365 group), you should additionally configure a retention policy that includes that Microsoft 365 group by using the **Microsoft 365 Group mailboxes & sites** location. This retention policy applies to content in the group's mailbox, site, and files. Files include [Teams meeting recordings](/en-us/microsoftteams/meeting-recording?tabs=meeting-policy) and [transcripts](/en-us/microsoftteams/meeting-transcription-captions#transcription) from channel meetings.

To retain or delete Teams meeting recordings with their transcripts from user chats, you'll need a retention policy that includes the organizer's OneDrive account as the location.

If you have team sites that aren't connected to a Microsoft 365 group, which includes sites for Teams shared channels and Teams private channels, you need a retention policy that includes the **SharePoint classic and communication sites** or **OneDrive accounts** locations to retain and delete files in Teams:

- Files that are shared in chat are stored in the OneDrive account of the user who shared the file.
- Files that are uploaded to channels are stored in the SharePoint site for the team.

Tip

You can apply a retention policy to the files of just a specific team when it's not connected to a Microsoft 365 group by selecting the SharePoint site for the team, and the OneDrive accounts of users in the Team.

It's possible that a retention policy that's applied to Microsoft 365 groups, SharePoint sites, or OneDrive accounts could delete a file that's referenced in a Teams chat or channel message before those messages get deleted. In this scenario, the file still displays in the Teams message, but when users select the file, they get a "File not found" error. This behavior isn't specific to retention policies and could also happen if a user manually deletes a file from SharePoint or OneDrive.

# [Retention policy for Viva Engage](#tab/viva-engage-retention)
Note

Retention policies for Viva Engage do not inform users when messages are deleted as a result of a retention policy.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Data Lifecycle Management** &gt; **Policies** &gt; **Retention policies**.
2. Select **New retention policy** to create a new retention policy.
3. For the **Assign admin units** page, keep the default of **Full directory**. Currently, admin units aren't supported for this policy.

1. For the **Choose the type of retention policy to create** page, select **Adaptive** or **Static**, depending on the choice you made from the Before you begin instructions. If you haven't already created adaptive scopes, you can select **Adaptive** but because there won't be any adaptive scopes to select, you won't be able to finish the configuration with this option.
2. Depending on your selected scope:

    - If you chose **Adaptive**: On the **Choose adaptive policy scopes and locations** page, select **Add scopes** and select one or more adaptive scopes that have been created. Then, select one or more locations. The locations that you can select depend on the [scope types](purview-adaptive-scopes#configure-adaptive-scopes) added. For example, if you only added a scope type of **User**, you'll be able to select **Viva Engage user messages** but not **Viva Engage community messages**.
    - If you chose **Static**: On the **Choose locations to apply the policy** page, toggle on one or both of the locations for Viva Engage: **Viva Engage community message** and **Viva Engage user messages**.

        By default, all communities and users are selected, but you can refine this by specifying communities and users to be included or excluded.

        For Viva Engage user messages:

        - If you leave the default at **All users**, Azure B2B guest users are not included.
        - If you select **Edit** for **All users**, you can apply a retention policy to external users if you know their account.
3. For **Decide if you want to retain content, delete it, or both** page, specify the configuration options for retaining and deleting content.

    You can create a retention policy that just retains content without deleting, retains and then deletes after a specified period of time, or just deletes content after a specified period of time. For more information, see [Settings for retaining and deleting content](retention-settings#settings-for-retaining-and-deleting-content).
4. Complete the configuration and save your settings.

For technical details about how retention works for Viva Engage, including what elements of messages are supported for retention and timing information with example walkthroughs, see [Learn about retention for Viva Engage](retention-policies-viva-engage).

#### Known configuration issues for Viva Engage retention policies

- Although you can select the option to start the retention period when items were last modified, the value of **When items were created** is always used. For messages that are edited, a copy of the original message is saved with its original timestamp to identify when this pre-edited message was created, and the post-edited message has a newer timestamp.
- When you select **Edit** for the Viva Engage user messages location, you might see guests and non-mailbox users. Retention policies aren't designed for these users, so don't select them.

#### Additional retention policies needed to support Viva Engage

Viva Engage is more than just community messages and private messages. To retain and delete email messages for your Viva Engage network, configure an additional retention policy that includes any Microsoft 365 groups that are used for Viva Engage, by using the **Microsoft 365 Group mailboxes & sites** location.

This location will also include files that are uploaded to Viva Engage communities. These files are stored in the group-connected SharePoint site for the Viva Engage community.

It's possible that a retention policy that's applied to SharePoint sites could delete a file that's referenced in a Viva Engage message before those messages get deleted. In this scenario, the file still displays in the Viva Engage message, but when users select the file, they get a "File not found" error. This behavior isn't specific to retention policies and could also happen if a user manually deletes a file from SharePoint.

# [Retention policy for all other services](#tab/other-retention)
Use the following instructions for retention policies that apply to any of these services:

- Exchange: Email and public folders
- SharePoint: Sites and SharePoint Embedded containers
- OneDrive: Accounts
- Microsoft 365 groups
- Skype for Business

Note

If your organization is using [administrative units](purview-admin-units#permissions-for-administrative-units) and you're a restricted administrator assigned one or more adminsitrative units, you won't be able to configure a retention policy that includes SharePoint sites or Exchange public folders. For these locations, you must be an unrestricted administrator.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Solutions** &gt; **Data Lifecycle Management** &gt; **Policies** &gt; **Retention policies**.
2. Select **New retention policy** to start the **Create retention policy** configuration, and name your new retention policy.
3. For the **Assign admin units** page, keep the default of **Full directory**. Currently, admin units aren't supported for this policy.

1. For the **Choose the type of retention policy to create** page, select **Adaptive** or **Static**, depending on the choice you made from the Before you begin instructions. If you haven't already created adaptive scopes, you can select **Adaptive** but because there won't be any adaptive scopes to select, you won't be able to finish the configuration with this option. Adaptive policies don't support the locations for Exchange public folders or Skype for Business.
2. Depending on your selected scope:

    - If you chose **Adaptive**: On the **Choose adaptive policy scopes and locations** page, select **Add scopes** and select one or more adaptive scopes that have been created. Then, select one or more locations. The locations that you can select depend on the [scope types](purview-adaptive-scopes#configure-adaptive-scopes) added. For example, if you only added a scope type of **User**, you'll be able to select **Exchange mailboxes** but not **SharePoint sites**.
    - If you chose **Static**: On the **Choose locations** page, toggle on or off any of the locations except the locations for Teams and Viva Engage. For each location, you can leave it at the default to [apply the policy to the entire location](retention-settings#a-policy-that-applies-to-entire-locations), or [specify includes and excludes](retention-settings#a-policy-with-specific-inclusions-or-exclusions).

    Information specific to locations:

    - [Exchange mailboxes and Exchange public folders](retention-settings#configuration-information-for-exchange-mailboxes-and-exchange-public-folders)
    - [SharePoint sites and OneDrive accounts](retention-settings#configuration-information-for-sharepoint-sites-and-onedrive-accounts)
    - [Microsoft 365 Group mailboxes & sites](retention-settings#configuration-information-for-microsoft-365-group-mailboxes--sites)
    - [Skype for Business](retention-settings#configuration-information-for-skype-for-business)
3. For **Decide if you want to retain content, delete it, or both** page, specify the configuration options for retaining and deleting content.

    You can create a retention policy that just retains content without deleting, retains and then deletes after a specified period of time, or just deletes content after a specified period of time. For more information, see [Settings for retaining and deleting content](retention-settings#settings-for-retaining-and-deleting-content) on this page.
4. Complete the configuration and save your settings.

---

## Separate an existing 'Teams chats and Copilot interactions' policy

Previously, retention policies used the location **Teams chats and Copilot interactions** that combined Teams chat and Copilot interactions. There are now separate retention locations for Teams chat and Copilot interactions.

- You can separate Teams chats from Copilot interactions from an existing retention policy.
- You can create new retention policies for just Teams chats, or for just Copilot interactions.

Use the following PowerShell commands to separate an existing retention policy for **Teams chats and Copilot interactions**:

- To make your existing retention policy for the [older locations](retention-cmdlets#retention-cmdlets-for-older-locations) a Teams chat only policy:

    ```PowerShell
    Set-RetentionCompliancePolicy -Identity "<policy name>" -Applications "User:TeamsChatUserInteractions"
    ```

    Or, if you have an existing retention policy for [newer locations](retention-cmdlets#retention-cmdlets-for-newer-locations), such as Teams private channel messages and Viva Engage, you can add Teams chat to it:

    ```PowerShell
    Set-AppRetentionCompliancePolicy -Identity "<policy name>" -Applications "User:TeamsChatUserInteractions"
    ```
- To add Microsoft 365 Copilot interactions to an existing retention policy for [newer locations](retention-cmdlets#retention-cmdlets-for-newer-locations), such as Teams private channel messages and Viva Engage:

    ```PowerShell
    Set-AppRetentionCompliancePolicy -Identity “<policy name>” -Applications "User:M365Copilot"
    ```

For new retention policies, select the new locations, such as **Teams chat** or **Microsoft Copilot Experiences**.

Note

If you have existing retention policies for **Teams chats and Copilot interactions**, they continue to be supported, although they can't be edited when your tenant supports the separate locations. At this point, any new retention policies must use the new locations.

## How long it takes for retention policies to take effect

When you create and submit a retention policy, it can take up to seven days for the retention policy to be applied:

![Diagram of when retention policy take effect.](media/retention-policy-timings.png)

First, the retention policy needs to be distributed to the locations that you selected, and then applied to content. You can always check the distribution status of the retention policy by selecting it from the **Retention policies** page in the Microsoft Purview portal. From the flyout pane, if you see **(Error)** included in the status, and in the details for the locations see a message that it's taking longer than expected to deploy the policy or to try redeploying the policy, try running the [Set-AppRetentionCompliancePolicy](/en-us/powershell/module/exchange/set-appretentioncompliancepolicy) or [Set-RetentionCompliancePolicy](/en-us/powershell/module/exchange/set-retentioncompliancepolicy) PowerShell command to retry the policy distribution:

1. [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).
2. Run one of the following commands:

    - For the policy locations **Teams private channel messages**, **Viva Engage user messages** and **Viva Engage community messages**:

        ```PowerShell
        Set-AppRetentionCompliancePolicy -Identity <policy name> -RetryDistribution
        ```
    - For all other policy locations, such as **Exchange mailboxes**, **SharePoint classic and communication sites**, and **Teams channel messages**:

        ```PowerShell
        Set-RetentionCompliancePolicy -Identity <policy name> -RetryDistribution
        ```

## Updating retention policies

When settings from the retention policy are already applied to content, a change in configuration to the policy will be automatically applied to this content in addition to content that's newly identified.

Some settings can't be changed after the policy is created and saved, which include the name of the retention policy, the scope type (adaptive or static), and the retention settings except the retention period.

If you no longer need the retention settings that you've configured, see [Releasing a policy for retention](retention#releasing-a-policy-for-retention).

## Troubleshooting retention policies

If your retention policies aren't working as expected or you see errors related to your retention policies, use the following troubleshooting resources:

- [Identify errors in Microsoft 365 retention and retention label policies](/en-us/microsoft-365/troubleshoot/retention/identify-errors-in-retention-and-retention-label-policies)
- [Resolve errors in Microsoft 365 retention and retention label policies](/en-us/microsoft-365/troubleshoot/retention/resolve-errors-in-retention-and-retention-label-policies)