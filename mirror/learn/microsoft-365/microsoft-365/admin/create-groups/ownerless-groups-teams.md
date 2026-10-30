---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Manage ownerless Microsoft 365 groups and teams - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/create-groups/ownerless-groups-teams?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
ms.reviewer: rahulnayak
ms.date: 2026-08-13T00:00:00.0000000Z
f1.keywords: NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
audience: Admin
ms.topic: how-to
ms.service: m365-core
ms.subservice: identity
ms.localizationpriority: medium
ms.collection:
- M365-subscription-management
- Adm_O365
- Adm_TOC
- trust-pod
ms.custom:
- AdminSurgePortfolio
- AdminTemplateSet
- admindeeplinkMAC
- m365-groups
- user-accounts
search.appverid:
- MET150
- MOE150
description: Learn how to automatically invite members to become owners in an ownerless Microsoft 365 group or a team in Microsoft Teams.
locale: en-us
document_id: 44c73a40-30f1-78f4-9130-37790d58fcda
document_version_independent_id: 44c73a40-30f1-78f4-9130-37790d58fcda
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/create-groups/ownerless-groups-teams.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/create-groups/ownerless-groups-teams
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/create-groups/ownerless-groups-teams.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: cc417a46-e1b3-f5b1-67c0-66a85659551c
---

# Manage ownerless Microsoft 365 groups and teams - Microsoft 365 admin | Microsoft Learn

A team in Microsoft Teams or a Microsoft 365 group can become ownerless if you delete an owner's account in Microsoft 365. Groups and teams need an owner to add or remove members and change group settings.

This article explains how to handle ownerless Microsoft 365 groups in the Microsoft 365 admin center.

## How the ownerless group policy works

An Exchange administrator or Groups administrator can create a policy that automatically asks the members who are the most active in the group if they accept ownership.

When a member accepts the invitation to become an owner, the action is logged in the Microsoft Purview portal audit log.

If there's no group activity, the policy asks random group members to accept ownership.

Note

The Ownerless Group feature is available only in public clouds.

## Requirements of the ownerless group policy

To set up and manage the Microsoft 365 ownerless group policy, you need to meet **one** of the following requirements:

- **An eligible Microsoft 365 subscription**

    - Eligible plans include Microsoft 365 Business Premium, Microsoft 365 Enterprise E3 and E5, Office 365 and Microsoft 365 Government G3 and G5, Microsoft 365 Education A3 and A5, and Frontline F1 and F3.
- **An Azure P1 or P2 premium plan**

    - All notification options in the ownerless groups policy require an Azure premium plan because a security group is used to specify which group members receive ownership notifications. Security groups are a feature of Azure premium plans.

## Limitations of the ownerless group policy

Managing ownerless groups by using this policy has a few limitations. The following list explains these limitations:

- **The ownerless group policy only applies to Microsoft 365 groups.**

    - Not all SharePoint, Stream, and other apps' groups are Microsoft 365 groups. Viva Engage groups are Microsoft 365 groups if the tenant is in Native mode.
- **You can't batch update the groups the policy targets.**

    - You can only search for and add one Microsoft 365 group at a time to this policy.

## Set up the ownerless group or team policy

1. In the [Microsoft 365 admin center](https://admin.microsoft.com), expand **Settings** and select **Org settings**.
2. On the [Services](https://go.microsoft.com/fwlink/p/?linkid=2053743) tab, select **Microsoft 365 Groups**.
3. Select the **When there's no owner, email and ask active group members to become an owner** checkbox.
4. If you want to keep the default configuration settings, select **Save**.

## Customize the ownerless group policy

1. On the **Microsoft 365 Groups** pane, select **Configure policy**.
2. On the **Weekly notification options** page, specify who can receive ownership notifications. If you choose to allow or block certain members, search for and add the security group that you want to use.

    1. To limit who can be invited to be an owner by using a security group, you need a Microsoft Azure P1 or P2 license for each Microsoft 365 group member in your organization, but you don't need to assign it.
    2. Type the number of active members that you want to notify, and select the number of weeks to send the notification. The notification list is created during the first notification and doesn't change.
    3. Select **Next**.
3. On the **Who is this email coming from** page, select a sender for the email, and then select **Next**.

    Shared mailboxes aren't supported. The sender must be either a user mailbox or a group mailbox.
4. On the **Subject and message** page, customize the email and optionally include a **policy guideline URL**, and then select **Next**.

    You can't have the notification's language change based on the recipient's country or region.
5. On the **Select which groups to target** page, select **Specific groups**, and choose the groups and teams that you want to include in this policy, or select **All groups**.

    You can select up to 50 groups.
6. Select **Next**.
7. On the **Review and finish** page, confirm your settings and select **Finish**, and then select **Done**.

## After you set up the ownerless group policy

Notifications are sent weekly starting within 24 hours of policy creation. The audit log tracks notifications and responses.

If a user is part of multiple ownerless groups, they can receive separate weekly notifications, one for each group they're an active member of.

### When someone accepts or declines group ownership

Up to two members per group can accept the invitation to become an owner. Once someone accepts ownership, the policy stops sending notifications to the group's members.

If a member declines ownership, they stop receiving the weekly notifications.

If a member doesn't accept or decline ownership, they keep receiving the weekly notifications for the number of weeks specified in the policy.

### When no one accepts group ownership

After the notification period specified in the policy ends, the policy stops sending notifications. In this scenario, the ownerless groups policy takes no further action. Tenant admins need to find and [assign an owner for each ownerless group](/en-us/admin/create-groups/add-or-remove-members-from-groups).

## See which groups are ownerless

Admins have multiple options to see which Microsoft 365 groups are ownerless.

### Use the Microsoft 365 admin center

1. Sign in as administrator to the Microsoft 365 admin center.
2. Expand Teams & Groups and select "Active teams & groups"
3. Click on Filter and select "Ownerless groups"

    [![Screenshot showing ownerless groups.](media/ownerless-groups-teams/list-ownerless-group-from-mac.jpg)](media/ownerless-groups-teams/list-ownerless-group-from-mac.jpg#lightbox)
4. You see a list of Microsoft 365 Groups that don't have any owners assigned.

    [![Screenshot showing a list of groups with no owners assigned.](media/ownerless-groups-teams/ownerless-groups-listed.jpg)](media/ownerless-groups-teams/ownerless-groups-listed.jpg#lightbox)
5. Select the group and assign an owner to the group.

    [![Screenshot showing how to assign owners.](media/ownerless-groups-teams/assign-owners.png)](media/ownerless-groups-teams/assign-owners.png#lightbox)

### Use the Exchange admin center

1. Sign in to [Exchange admin center](https://admin.cloud.microsoft/exchange) and select **Groups** under **Recipients**. Or, [click here](https://admin.cloud.microsoft/exchange#/groups) to sign in to **Groups** under **Exchange admin center**.
2. Select **Filter** and choose the **Ownerless groups** option.

    [![Screenshot showing how to filter on ownerless groups.](media/ownerless-groups-teams/filter-on-ownerless-groups.png)](media/ownerless-groups-teams/filter-on-ownerless-groups.png#lightbox)
3. From the list, select a group and choose **Add group owners** to assign an owner to the group.

    [![Screenshot showing how to add group owners.](media/ownerless-groups-teams/add-owners-group.png)](media/ownerless-groups-teams/add-owners-group.png#lightbox)
4. By searching the [audit log](/en-us/purview/audit-search#get-started-with-search) in the Microsoft Purview portal. To search for ownerless groups, follow these steps:

    1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com/).
    2. Select the **Audit** solution card.

        If the **Audit** solution card isn't displayed, select **View all solutions**, and then select **Audit** in the **Core** section.
    3. On the **Search** page, in the **Activities - friendly names** field, select **Unattended ownerless group** from the dropdown list.
    4. Select the **Search** button.

## Auditing changes to ownerless group policy

To find details about changes to the ownerless group policy, search for the **Updated the ownerless group policy** activity.

1. Sign in to the [Microsoft Purview portal](https://sip.purview.microsoft.com/audit/auditsearch) and start a new audit log search.

    Note

    For help with Microsoft Purview authentication, see [Microsoft Purview portal](/en-us/purview/purview-portal).
2. Under **Activities - friendly names**, type **ownerless group**, and select the **Updated the ownerless group policy** activity.
3. Specify the start and end dates for the audit log search.

    [![Screenshot of audit log.](../../media/audit-ownerless-group1.png)](../../media/audit-ownerless-group1.png#lightbox)

    When the search finishes, you see the following result.

    [![Screenshot of result of audit log search.](../../media/result-audit-ownerless-group1.png)](../../media/result-audit-ownerless-group1.png#lightbox)

    The following example shows an audit log entry for changes made:

    [![Screenshot of an audit log.](../../media/audit-log1.png)](../../media/audit-log1.png#lightbox)

## Common issues with the ownerless group policy

- **Exchange Online throttles policy notifications.**

    - Because this policy sends notifications from one mailbox, Exchange Online can throttle the policy's notification emails if there are too many ownerless groups in your organization. Exchange Online mailboxes are limited to 10,000 sent emails per day.
- **The action buttons *Yes* and *No* aren't available in a forwarded notification email.**

    - If a member forwards their notification email to a different member, the forward recipient can't accept or decline the invitation.
- **Member can't see *Yes* and *No* in the notification email.**

    - Members should open notification emails in a separate window, not a preview pane. If the member views the notification in an email preview pane, they can't see the **Yes** and **No** options.
    - Make sure that the user principal name (UPN) and primary email address of the sender are the same. For information about how to update the UPN or primary email address of a user, see [Change a user name and email address](/en-us/microsoft-365/admin/add-users/change-a-user-name-and-email-address). If they don't match, the recipient can't see the **Yes** and **No** options.
- **The policy for ownerless groups is configured, but group members don't receive notifications.**

    - This problem occurs if the specified sender in the policy doesn't have a user or group mailbox provisioned in Exchange Online. If the sender has a user or group mailbox, check the [audit log](/en-us/purview/audit-get-started#step-3-search-the-audit-log) in the [Microsoft Purview portal](https://go.microsoft.com/fwlink/p/?linkid=2077149) to trace whether email notifications were sent.
    - Members who don't have a user mailbox provisioned in Exchange Online don't receive notifications.