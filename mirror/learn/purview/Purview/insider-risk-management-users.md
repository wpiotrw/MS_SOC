---
layout: Conceptual
title: Manage the workflow with the Insider Risk Management users dashboard | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-users
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to use the Insider Risk Management Users dashboard to review users with triggering indicators, risk scores, and active alerts as part of the investigation workflow.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: how-to
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: itpro
ms.collection:
- purview-compliance
ms.custom: msecd-doc-authoring-1014, admindeeplinkCOMPLIANCE, sfi-image-nochange
ai-usage: ai-assisted
locale: en-us
document_id: fafa165a-2720-7d2e-ca0c-95f97ad9c6a9
document_version_independent_id: fafa165a-2720-7d2e-ca0c-95f97ad9c6a9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-users.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-users
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-users.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 468a4ba1-b34c-b679-e7d1-4ddf14a06ab8
---

# Manage the workflow with the Insider Risk Management users dashboard | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

The **Users dashboard** is an important tool in the Insider Risk Management workflow. It helps investigators and analysts have a more complete understanding of risk activities. This dashboard offers views and management features to meet administrative needs between creating Insider Risk Management policies and managing Insider Risk Management cases.

After users are added to Insider Risk Management policies, background processes automatically evaluate user activities for [triggering indicators](insider-risk-management-settings-policy-indicators). After the process identifies triggering indicators, it assigns risk scores to user activities. Some of these activities result in an insider risk alert, but some activities don't meet a minimum risk score level and an insider risk alert isn't created. The **Users dashboard** allows you to view users with these types of indicators and risk scores, as well as users that have active insider risk alerts.

Learn more about how the Users dashboard displays users in the following scenarios:

- Users with active insider risk policy alerts
- Users with triggering events
- Users identified as potential high impact users or in priority user groups
- Users added temporarily to policies

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Users with active insider risk policy alerts

The **Users dashboard** automatically displays all users with active insider risk policy alerts. These users with alerts have both a triggering indicator and an activity risk score that meets the requirements for creating an insider risk alert. You can view activities for these users by selecting the user in the **Users dashboard** and navigating to the **User activity** tab.

## Users with triggering events

The **Users dashboard** automatically displays all users with triggering events, but that don't have an activity risk score that would create an insider risk alert. For example, a user with a reported resignation date is displayed because this activity is a triggering event but isn't an activity that has a risk score. You can view activities for these users by selecting the user in the **Users dashboard** and navigating to the **User activity** tab.

## Users added temporarily to policies

The **Users dashboard** shows users you add to Insider Risk Management policies after an unusual event outside of the Insider Risk Management workflow. Temporarily adding users (from the Policies dashboard) is also a way to start scoring user activity for an Insider Risk Management policy for testing the policy, even if you don't configure a required connector.

When you manually add a user to a policy, the solution scores user activities for the previous 90 days and adds them to the **User activity** timeline. For example, you have a user not currently being assigned risk scores for an insider risk policy and the user has data leak activities reported to the legal department in your organization. The legal department recommends that you configure new short-term detection requirements for the user. You can temporarily assign the user to your *Data leaks* policy for a designated length of time (activation window). All users added temporarily are displayed in the **Users dashboard** because triggering event requirements are waived.

Note

It might take several hours for new manually added users to appear in the **Users dashboard**. Activities for the previous 90 days for these users might take up to 24 hours to display. To view activities for manually added users, select the user on the **Users dashboard** and open the **User activity** tab on the details pane.

The user is automatically removed from the **Users dashboard** and scoring stops when the time defined in the **Activation window** expires if:

- the user doesn't have any additional triggering events or insider risk policy alerts, and
- the manually defined **Activation window** duration is longer than the global policy **Activation window** duration.

The **Activation window** setting with the longest duration always overrides the **Activation window** setting with a shorter duration. For example, you configure the **Activation window** on the global **Policy timeframes** tab in the Insider Risk Management global settings for 15 days, which automatically applies to all your insider risk policies.

You temporarily add a user to your *Data leaks* insider risk policy and define 30 days as the **Activation window** for this user. The global **Activation window** setting of 15 days is overridden by defining the **Activation window** setting of 30 days for the temporarily added user. The temporarily added user remains in the **Users dashboard** and is in-scope for the policy for 30 days.

In the opposite scenario where the global **Activation window** setting is longer than the **Activation window** setting defined for a temporarily added user, the global **Activation window** setting overrides the **Activation window** setting for the temporarily added user. The temporarily added user remains in the **Users dashboard** and is in-scope for the policy for the number of days defined in the global **Activation window** settings.

## View user information on the Users dashboard

Each user displayed in the **Users dashboard** shows the following information:

- **Users**: Username for a user. This field is anonymized if the global anonymization setting for Insider Risk Management is enabled.
- **Alert severity level**: Current calculated risk level of the user. The system calculates this score every 24 hours and uses the alert risk scores from all active alerts associated with the user. For users with only triggering indicators, the alert severity level is zero.
- **Active alerts**: Number of active alerts for all policies.
- **Confirmed violations**: Number of cases resolved as *confirmed policy violation* for the user.
- **Case**: Current active case for the user.

To quickly locate a specific user, use **Search** at the top right of the Users dashboard. When searching for users, you must use the user principal name (UPN). For example, when searching for a user named 'Tiara Hidayah' that has a UPN of 'thidayah' in your organization, enter 'thidayah' or some part of the UPN in **Search**.

![Screenshot of the Insider Risk Management Users dashboard showing user details, alert severity levels, and active alerts.](media/insider-risk-users-dashboard.png)

Note

The number of users displayed on the **Users dashboard** might be limited in some instances, depending on the volume of active alerts and matching policies. The **Users dashboard** displays users with active alerts as the system generates the alerts. In rare cases, the maximum number of displayed users is reached. If the maximum number of displayed users is reached, the **Users dashboard** adds users with active alerts who aren't displayed as existing user alerts are triaged.

## View user details

To view more details about risk activity for a user, open the user details pane by double-clicking a user in the **Users dashboard**. On the details pane, you can view the following information:

- **User profile** tab

    - **Name and title**: Name and position title for the user from Microsoft Entra ID. These user fields are anonymized or empty if you enable the global anonymization setting for Insider Risk Management.
    - **User details**: Shows whether the user is a potential high impact user or if the user is in priority user groups.
    - **Alert and activity summary**: Shows active user alerts and open cases.
    - **User email**: Email address for the user.
    - **Alias**: Network alias for the user.
    - **Organization or department**: Organization or department for the user.
    - **In scope**: Shows in-scope assignment of the user to policies.

    The following additional user profile signals are available in the unified alert experience (preview). To access, select an alert on the **Alerts (preview)** tab, scroll down to **User details**, and select **View user details**:

    - **Office location**: The user's office location from their Entra profile.
    - **Employee type**: The user's employee type from their Entra profile.
    - **Department**: The user's department from their Entra profile.
    - **Last working date**: The user's last scheduled date of work, if available.
    - **Past alert and case history**: A summary of the user's previous alerts and cases across Insider Risk Management.
    - **Priority user group status**: Shows whether the user belongs to any priority user groups.
    - **Policy inclusion**: Lists the policies in which the user is currently in scope.

    Note

    When pseudo-anonymization is enabled, the expanded user profile details aren't visible.
- **User activity** tab

    - **History of recent user activity**: Shows both triggering indicators and insider risk indicators for risk activities up to the last 90 days. All risk activities pertinent to insider risk indicators are also scored, though the activities might or might not have generated an insider risk alert. Triggering indicator examples might be a resignation date or the last scheduled date of work for the user. Insider risk indicators are activities determined to have an element of risk, which might potentially lead to a security incident, and are defined in policies that the user is included in. Event and risk activities are listed with the most recent item listed first.

## Use Copilot to summarize user activities (preview)

Select **Summarize with Copilot** on the user details pane to quickly summarize the activities for users that might need further investigation. When you summarize user risk activities with Microsoft Copilot in Microsoft Purview, a **Copilot** pane appears on the right side of the screen with a user summary.

![Screenshot of the Insider Risk Management user details pane with the Summarize with Copilot button available for investigating a selected user.](media/insider-risk-management-copilot-users.png)

The user summary includes essential details such as the user’s name, title, user principal name, alert and case history, and top risk factors. The top risk factors provide crucial insights into the user roles, permissions, involvement in exfiltration activities, sequential patterns, or any unusual behavior. This view helps you identify users who might pose the highest insider risk to your organization.

Suggested prompts are automatically listed to help further refine your summary and to help provide additional insights to the activities associated with the user. Choose from the following suggested prompts:

- *List all the data exfiltration activities involving this user*.
- *List all the sequential activities involving this user*.
- *Did the user engage in any unusual behavior?*
- *Show key actions performed by the user in the last 10 days*.
- *Summarize user's last 30 days of activity*.

Tip

You can also use the [standalone version of Microsoft Security Copilot to investigate Insider Risk Management, Microsoft Purview data loss prevention (DLP), and Microsoft Defender XDR alerts](copilot-in-purview-promptbooks).

## Remove users from in-scope assignment to policies

You might need to stop assigning risk scores to a user in Insider Risk Management policies. Use **Stop scoring activity for users** on the **Users dashboard** to stop assigning risk scores for a user from all Insider Risk Management policies that they're currently in scope for. Stopping scoring activity doesn't remove the user from the overall policy assignment (when you add users or groups to a policy configuration), but simply removes the user from active processing by policies after current triggering events. If the user has another triggering event in the future, risk scores from policies automatically begin to be assigned to the user again. Any existing alerts or cases for this user don't remove.

### Remove a user from in-scope status in all Insider Risk Management policies

To remove a user from in-scope status in all Insider Risk Management policies, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Users** in the left navigation.
4. On the **Users dashboard**, select the users you want to stop scoring activity for.
5. Select **Stop scoring activity for users**.

Note

Removing a user from in-scope status might take several minutes. When the process completes, the user doesn't appear on the **Users dashboard**. If the removed user has active alerts or cases, the user remains on the **Users dashboard** and the user details show that they are no longer in-scope for a policy.

## Run automated tasks with Power Automate flows for a user

Using recommended Power Automate flows, risk investigators and analysts can quickly take action to notify users when they're added to an insider risk policy.

To run, manage, and create Power Automate flows for Insider Risk Management users:

1. Select **Automate** on the user action toolbar.
2. Choose the Power Automate flow to run, then select **Run flow**.
3. After the flow completes, select **Done**.

For more information about Power Automate flows for Insider Risk Management, see [Getting started with Insider Risk Management settings](insider-risk-management-settings-power-automate).