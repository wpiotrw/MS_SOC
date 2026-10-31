---
layout: Conceptual
title: Manage Communication Compliance policies | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/communication-compliance-policies
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Create and manage Communication Compliance policies in Microsoft Purview to detect inappropriate content, regulatory violations, and risky communications.
keywords: Microsoft 365, Microsoft Purview, compliance, Communication Compliance
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-22T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-communication-compliance
ms.collection:
- purview-compliance
- microsoft-365-copilot
search.appverid:
- MET150
- MOE150
ms.custom: sfi-ga-nochange, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 17b76c97-5ec1-6dee-1a00-6798f0220bfc
document_version_independent_id: 17b76c97-5ec1-6dee-1a00-6798f0220bfc
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/communication-compliance-policies.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: communication-compliance-policies
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/communication-compliance-policies.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e4f48d48-dfb7-4973-a019-e504674667cb
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/495840e0-c52f-49d2-a584-185aefeb98c7
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 2f5e7e34-0e92-cb58-1187-697c09b185d7
---

# Manage Communication Compliance policies | Microsoft Learn

Important

[Microsoft Purview Communication Compliance](communication-compliance) provides the tools to help organizations detect regulatory compliance (for example, SEC or FINRA) and business conduct violations such as sensitive or confidential information, harassing or threatening language, and sharing of adult content. Communication Compliance is built with privacy by design. Usernames are pseudonymized by default, role-based access controls are built in, investigators are opted in by an admin, and audit logs are in place to help ensure user-level privacy.

## Create and manage policies

Create Communication Compliance policies for Microsoft 365 organizations in the Microsoft Purview portal. Communication Compliance policies define which communications and users are subject to review in your organization, set custom conditions the communications must meet, and specify who should do reviews.

- Users assigned the *Communication Compliance Admins* role can set up policies and access the **Communication Compliance** page and global settings in Microsoft Purview.
- You can export the modification history to a .csv file that includes the status of alerts pending review, escalated items, and resolved items.
- You can't rename policies, but you can delete them when no longer needed.

Important

PowerShell isn't supported for creating and managing Communication Compliance policies. To create and manage these policies, use the policy management controls in the Communication Compliance solution.

## Choose a policy template

Policy templates are predefined policy settings that you can use to quickly create policies to address common compliance scenarios. Each of these templates has differences in conditions and scope. All templates use the same types of detection signals. You can choose from the following policy templates:

| Area | Policy Template | Details |
| --- | --- | --- |
| **Conflict of interest** | Detect conflict of interest | - Locations: Exchange Online, Microsoft Teams, Viva Engage  - Direction: Internal  - Review Percentage: 100%  - Conditions: None |
| **Copilot interactions** | Detect Microsoft 365 Copilot and Microsoft 365 Copilot Chat interactions | - Location: Microsoft 365 Copilot and Microsoft 365 Copilot Chat  - Direction: Inbound, Outbound, Internal  - Review Percentage: 100%  - Conditions: Prompt Shields, Protected material classifiers |
| **Inappropriate content** | Detect inappropriate content | - Location: Microsoft Teams, Viva Engage  - Direction: Inbound, Outbound, Internal  - Review Percentage: 100%  - Conditions: Hate, Violence, Sexual, Self-harm classifiers |
| **Inappropriate images** | Detect inappropriate images | - Locations: Exchange Online, Microsoft Teams - Direction: Inbound, Outbound, Internal  - Review Percentage: 100%  - Conditions: Adult and Racy image classifiers |
| **Inappropriate text** | Detect inappropriate text | - Locations: Exchange Online, Microsoft Teams, Viva Engage  - Direction: Inbound, Outbound, Internal  - Review Percentage: 100%  - Conditions: Threat, Discrimination, and Targeted harassment classifiers |
| **Regulatory compliance** | Detect financial regulatory compliance | - Locations: Exchange Online, Microsoft Teams, Viva Engage  - Direction: Inbound, Outbound  - Review Percentage: 10%  - Conditions: Customer complaints, Gifts & entertainment, Money laundering, Regulatory collusion, Stock manipulation, and Unauthorized disclosure classifiers |
| **Sensitive information** | Detect sensitive info types | - Locations: Exchange Online, Microsoft Teams, Viva Engage  - Direction: Inbound, Outbound, Internal  - Review Percentage: 10%  - Conditions: Sensitive information, out-of-the-box content patterns, and types, custom dictionary option, attachments larger than 1 MB |

## User-reported messages policy

The *User-reported messages* policy is implemented for your organization when you purchase a license that includes Microsoft Purview Communication Compliance. However, this feature can take up to 30 days to become available after license purchase.

As part of a layered defense to detect and remediate inappropriate messages in your organization, you can supplement Communication Compliance policies with user-reported messages in Microsoft Teams and Viva Engage (preview). To support a safe and compliant work environment, this feature empowers users in your organization to self-report inappropriate internal Teams chat messages and Viva Engage conversations, such as harassing or threatening language, sharing of adult content, and sharing of sensitive or confidential information.

### User-reported messages in Microsoft Teams

Enabled by default in the [Teams admin center](/en-us/microsoftteams/manage-teams-in-modern-portal), the *Report inappropriate content* option in Teams messages lets users in your organization submit inappropriate internal personal and group chat messages for review by Communication Compliance reviewers for the User-reported messages policy. A default system policy supports these messages and supports reporting messages in Teams group and private chats.

Azure AI Content Safety's hate, self-harm, sexual, and violence classifiers evaluate user-reported messages. This evaluation helps investigators quickly assess potential risk in user-reported content and take action.

![Screenshot of the Report this message option in a Teams chat message.](media/communication-compliance-report-message.png)

When a user submits a Teams chat message for review, the message is copied to the User-reported message policy. Reported messages initially remain visible to all chat members and there's no notification to chat members or the submitter that a message has been reported in channel, private, or group chats. A user can't report the same message more than once and the message remains visible to all users included in the chat session during the policy review process.

During the review process, Communication Compliance reviewers can perform all the standard [remediation actions](communication-compliance-investigate-remediate#decide-on-a-remediation-action) on the message, including removing the message from the Teams chat. Depending on how the messages are remediated, the message sender and recipients see different notification messages in Teams chats after the review. Any user-reported content that triggers the Content Safety classifiers shows the classifier name that flagged the message and a corresponding severity value is visible in the **Severity** column.

Important

If a user reports a message that was sent before they were added to a chat, Teams message remediation isn't supported; the Teams message can't be removed from the chat.

![Screenshot of the User-reported messages policy in the Communication Compliance solution.](media/communication-compliance-user-reported-messages-policy.png)

User-reported messages from Teams chats are the only messages processed by the User-reported message policy and you can only modify the assigned reviewers for the policy. You can't edit all other policy properties. When you create the policy, all members of the *Communication Compliance Admins* role group (if populated with at least one user) or all members of your organization's *Global Admin* role group are assigned as initial reviewers. A randomly selected user from the *Communication Compliance Admins* role group (if populated with at least one user) or a randomly selected user from your organization's *Global Admin* role group is the policy creator.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

Admins should immediately assign custom reviewers to this policy as appropriate for your organization. This assignment might include reviewers such as your Compliance Officer, Risk Officer, or members of your Human Resources department.

#### Customize the reviewers for chat messages submitted as user-reported messages

To customize the reviewers assigned to the User-reported messages policy, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) using credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Communication Compliance** solution.
3. Select **Policies** in the left navigation.
4. Select the *User-reported messages* policy, then select **Edit**.
5. On the **Detect user-reported messages** pane, assign reviewers for the policy. Reviewers must have mailboxes hosted on Exchange Online. When you add reviewers to a policy, they automatically receive an email message that notifies them of the assignment to the policy and provides links to information about the review process.
6. Select **Save**.

The *Report inappropriate content* option is enabled by default and you can control it via Teams messaging policies in the [Teams Admin Center](/en-us/microsoftteams/manage-teams-in-modern-portal). Users in your organization automatically receive the global policy, unless you create and assign a custom policy. Edit the settings in the global policy or create and assign one or more custom policies to turn on or turn off the *Report inappropriate content* option. For more information, see [Manage messaging policies in Teams](/en-us/microsoftteams/messaging-policies-in-teams).

Important

If you use PowerShell to turn on or turn off the **End user reporting** option in the Teams Admin Center, use [Microsoft Teams cmdlets module version 4.2.0](/en-us/MicrosoftTeams/teams-powershell-release-notes) or later.

### User-reported messages in Viva Engage

The **Report Conversations** option is off by default in the Viva Engage admin center. When you turn on this option, you see different options depending on whether you have a license that includes Communication Compliance:

- **Licenses that don't include Communication Compliance**. If you don't have a license that includes Communication Compliance, when you turn on the option, the Viva Engage admin can specify an email address to receive reported conversations. The admin can also enter pre-submission instructions and post-submission confirmations for the user. [Learn more about enabling the **Report Conversations** option if you don't have a license that includes Communication Compliance](/en-us/viva/engage/report-conversation-overview)
- **Licenses that do include Communication Compliance**. If you have a license that includes Communication Compliance, when you turn on the option, any reported conversations automatically route through Communication Compliance for investigation.

#### How upgrades and downgrades in licensing affect the reported conversations workflow

The following behaviors apply when your organization upgrades or downgrades between licenses that do and don't include Communication Compliance:

- If you upgrade from a license that doesn't include Communication Compliance to a license that includes Communication Compliance and turn on the **Report Conversations** option, reported conversations automatically route to Communication Compliance. The Viva Engage admin can continue to access earlier reported conversations and can view new reported conversations [if they're added as an investigator in Communication Compliance](communication-compliance-permissions).
- If you downgrade from a license that includes Communication Compliance to a license that doesn't include Communication Compliance and turn on the **Report Conversations** option, the workflow reverts to the process described in this article for customers that don't have a Communication Compliance license. To continue to use the feature, an admin must turn on the **Report Conversations** option in the Viva Engage admin center again and specify an email address to send reported conversations to.

#### User experience for customers that have a license that includes Communication Compliance

If you choose to route user-reported conversations through Communication Compliance, you can create pre-submission instructions for the user.

To report a conversation in Viva Engage, the user selects the ellipsis (three dots), then selects **Report conversation**.

The command name changes to **Report comment**, **Report question**, or **Report answer** depending on whether the user is viewing a comment, question, or answer in Viva Engage or Answers in Viva.

If the user submits the report successfully, they see a confirmation message.

When a conversation is reported, the conversation is copied to the Communication Compliance User-reported message policy. The Communication Compliance investigator can review reported conversations in the User Reported policy inbox and can do all the standard [remediation actions](communication-compliance-investigate-remediate#decide-on-a-remediation-action) for the conversation.

#### Turn on the Report Conversation feature in the Viva Engage admin center

To turn on the Report Conversation feature in the Viva Engage admin center, complete the following steps:

1. Go to the Viva Engage admin center.
2. On the **Settings** page, select **Report Conversations**.
3. Turn on the setting.
4. Under **Report recipient**, add an email address to route reports to. This email address is used to notify the admin in case there's any problem with the configuration.
5. In the **Pre-submission details or instructions for users** box, enter any instructions you want to display for the user.
6. In the **Post-submission instructions to user** box, enter any instructions (optional) that the user will see after reporting a conversation.

## Integrate Communication Compliance with Microsoft Purview Insider Risk Management

When users experience employment stressors, they might engage in risky activities. Workplace stress can lead to uncharacteristic or malicious behavior by some users that surfaces as potentially inappropriate behavior on your organization's messaging systems. Counterproductive work behavior can be a precursor to more serious violations, such as sabotaging company assets or leaking sensitive information. By integrating Communication Compliance with [Microsoft Purview Insider Risk Management](insider-risk-management), you can detect stressors that indicate an unhealthy workplace environment.

You can integrate Communication Compliance with Insider Risk Management by automatically creating a Communication Compliance policy from Insider Risk Management. You can create this type of policy in two different ways:

- By creating an Insider Risk Management trigger for policy templates
- By selecting Insider Risk Management policy indicators for data-based policy templates
- By selecting generative AI policy indicators for policy templates

### Create an Insider Risk Management trigger for policy templates

Communication Compliance can provide risk signals detected in applicable messages to Insider Risk Management risky user policies by using a dedicated Detect inappropriate text policy. This policy is automatically created if you select it as an option when creating a policy by using the [Data leaks by risky users template](insider-risk-management-policy-templates#data-leaks-by-risky-users) or the [Security policy violations by risky users template](insider-risk-management-policy-templates#security-policy-violations-by-risky-users) in Insider Risk Management. For example, the following screenshot shows the option selected in the *Data leaks by risky users* template.

![Screenshot of the Communication Compliance option selected in the Data leaks by risky users template in Insider Risk Management.](media/communication-compliance-option-insider-risk-management-template.png)

When configured for an Insider Risk Management policy, Communication Compliance creates a dedicated policy named *Insider risk trigger - (date created)* and automatically includes all organization users in the policy. This policy starts detecting risky behavior in messages by using the Microsoft provided Threat, Harassment, and Discrimination trainable classifiers and automatically sends these signals to Insider Risk Management. If needed, you can edit this policy to update the scope of included users and the policy conditions and classifiers.

Users who send five or more messages classified as potentially risky within 24 hours are automatically brought in-scope for Insider Risk Management policies that include this option. Once in-scope, the Insider Risk Management policy detects potentially risky activities configured in the policy. The policy generates alerts as applicable. It can take up to 48 hours from the time risky messages are sent until the time a user is brought in-scope in an Insider Risk Management policy. If an alert is generated for a potentially risky activity detected by the Insider Risk Management policy, the triggering event for the alert is identified as being sourced from the Communication Compliance risky activity.

All users assigned to the [Insider Risk Management Investigators](insider-risk-management-plan#plan-permissions-to-support-the-review-and-investigation-workflow) role group are automatically assigned as reviewers in the dedicated Communication Compliance policy. Insider Risk Management investigators might need to review the associated risky user alert directly on the Communication Compliance alerts page (linked from the Insider Risk Management alert details). To enable this access, manually add them to the *Communication Compliance Investigators* role group.

Before integrating Communication Compliance with Insider Risk Management, consider the following guidance when detecting messages containing potentially inappropriate text:

- **For organizations without an existing *Detect inappropriate text* policy**. The Insider Risk Management policy workflow automatically creates the new *Risky user in messages - (date created)* policy. In most cases, you don't need to take any further action.
- **For organizations with an existing *Detect inappropriate text* policy**. The Insider Risk Management policy workflow automatically creates the new *Risky user in messages - (date created)* policy. Although you have two Communication Compliance policies for potentially inappropriate text in messages, investigators don't see duplicate alerts for the same activity. Insider Risk Management investigators only see alerts for the dedicated integration policy and Communication Compliance investigators only see the alerts for the existing policy. If needed, you can edit the dedicated policy to change the included users or individual policy conditions as applicable.

### Select Insider Risk Management policy indicators for data-based policy templates

The **Policy indicators** setting in Insider Risk Management provides Communication Compliance indicators to choose from when using the *Data theft*, *Data leaks*, *Data leaks by risky users*, and *Data leaks by priority users* templates:

- Sending financial regulatory text that might be risky
- Sending inappropriate images
- Sending inappropriate content
- Sending messages that contain specific sensitive info types

For more information on creating a Communication Compliance policy this way, see [Insider Risk Management policy indicators settings](insider-risk-management-settings-policy-indicators#communication-compliance-indicators).

### Select generative AI policy indicators for policy templates

The **Policy indicators** setting in Insider Risk Management provides generative AI app indicators to choose from when using the *Data leaks*, *Data leaks by risky users*, *Data leaks by priority users*, or *Risky AI usage* policy templates. These Azure AI Content Safety indicators help detect when prompts and responses in AI apps match the following classifiers:

- [Prompt Shields](/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Protected material detection](/en-us/azure/ai-services/content-safety/concepts/protected-material)

For more information on creating a Communication Compliance policy this way, see [Insider Risk Management policy indicators settings](insider-risk-management-settings-policy-indicators#generative-ai-apps-indicators). For more information on Azure AI Content Safety, see [Azure AI Content Safety](/en-us/azure/ai-services/content-safety/overview).

## Policy health (preview)

The policy health status gives you insights into potential issues or optimizations for your Communication Compliance policies. At the top of the **Policies** page, you see a summary that lists the total number of policy warnings and recommendations, and the total number of healthy policies. If a specific policy has a warning or recommendations, the **Policy health** column lists a link to the warning or recommendations. When you select the link, a details pane opens on the right side of the screen with the **Policy Health** tab selected, which makes it easy to quickly review the warning or recommendation and take action on it.

![Screenshot of the Communication Compliance Policies page showing policy warnings, recommendations, and healthy policies.](media/communication-compliance-home.png)

The **Policy Health** tab has two parts. The upper part of the tab shows general information about the policy, including whether the policy is active, whether it's updated, and general tips. The lower part of the tab shows the specific warning or recommendations. If you're a member of the *Communication Compliance* or *Communication Compliance Admins* group, you can take action directly from the warning or recommendation. If you're a member of the *Communication Compliance Analysts* or *Communication Compliance Investigators* group, you can see the warning or recommendation so you can prompt your admin to take action.

- **Warnings**: If you don't take action on a warning, the policy stops working. For the policy health preview, there's one warning, related to a policy's storage limit size.
- **Recommendations**: Recommendations provide suggestions for optimizing policies. If you ignore a policy recommendation, the policy continues to work. If you're a member of the *Communication Compliance* or *Communication Compliance Admins* group, you can act on a recommendation as long as the policy is active and if it's not updating. If you're a member of the *Communication Compliance Analysts* or *Communication Compliance Investigators*group, you can see the recommendation and prompt your admin to take action. For the preview, there are two recommendations:
    - **Potentially reduce false positives by filtering out bulk emails**: This recommendation prompts you to turn on the Filter email blasts setting in Communication Compliance to exclude bulk emails from policy evaluation. This setting helps reduce false positives by excluding bulk emails, such as newsletters, and spam, phishing, and malware, from getting flagged by Communication Compliance policies if the policy conditions are matched.
    - **Reduce user scoping blind spots**: This recommendation prompts you to reduce blind spots by turning on the **Show insights and recommendations for users who match this policy's conditions but weren't included in the policy** checkbox (used with the **Selected users** policy option).
- **Healthy policies**: If there are no warnings or recommendations for a specific policy, the policy is considered healthy.

### Reduce user scoping blind spots

You can reduce user-scoping related blind spots by turning on the **Show insights and recommendations for users who match this policy's conditions but weren't included in the policy** checkbox. When you turn on this checkbox, you see insights and recommendations for users who are sending messages that match the policy condition but aren't included in the scope of the policy. In this case, Communication Compliance recommends that you include those users in the scope of the policy so that you can review the messages sent by those users and take actions. You can select the specific users that you want to add or you can extend the policy to all users.

Insights for these users are aggregated; you can't see the messages sent by them until you add them to the scope of the policy.

If an admin doesn't act on a recommendation, the recommendation continues to recur. To turn off recommendations for users outside the scope of the policy, turn off the checkbox.

## Pause a policy

After you create a Communication Compliance policy, you can temporarily pause the policy. Use pausing for testing or troubleshooting policy matches, or for optimizing policy conditions. Instead of deleting a policy in these circumstances, pausing a policy also preserves existing policy alerts and messages for ongoing investigations and reviews. Pausing a policy prevents inspection and alert generation for all user message conditions defined in the policy for the time the policy is paused. To pause or restart a policy, you must be a member of the *Communication Compliance Admins* role group.

To pause a policy, go to the **Policy** page, select a policy, then select **Pause policy** from the actions toolbar. On the **Pause policy** pane, confirm you'd like to pause the policy by selecting **Pause**. In some cases, it can take up to 24 hours for a policy to be paused. Once the policy is paused, alerts aren't generated for messages matching the policy. However, messages associated with alerts that you created before pausing the policy remain available for investigation, review, and remediation.

The policy status for paused policies can show several states:

- **Active**: The policy is active.
- **Paused**: The policy is fully paused.
- **Pausing**: The policy is in the process of being paused.
- **Resuming**: The policy in the process of being resumed.
- **Error in resuming**: An error was encountered when resuming the policy. For the error stack trace, hover your mouse over the *Error in resuming* status in the Status column on the Policy page.
- **Error in pausing**: An error was encountered when pausing the policy. For the error stack trace, hover your mouse over the *Error in pausing* status in the Status column on the Policy page.

To resume a policy, go to the **Policy** page, select a policy, then select **Resume policy** from the actions toolbar. On the **Resume policy** pane, confirm you'd like to resume the policy by selecting **Resume**. In some cases, it can take up to 24 hours for a policy to be resumed. Once the policy is resumed, alerts are generated for messages matching the policy and made available for investigation, review, and remediation.

## Copy a policy

If your organization has existing Communication Compliance policies, you might find it helpful to create a new policy from an existing policy. When you copy a policy, you create an exact duplicate of an existing policy, including all included users, all assigned reviewers, and all policy conditions. Some scenarios where copying a policy is helpful include:

- **Policy storage limit reached**: Active Communication Compliance policies have message storage limits. When the storage limit for a policy is reached, the policy is automatically deactivated. If your organization needs to continue detecting, capturing, and acting on inappropriate messages covered by the deactivated policy, you can quickly create a new policy with an identical configuration.
- **Detect and review inappropriate messages for different groups of users**: Some organizations prefer to create multiple policies with the same configuration but include different groups of users and different reviewers for each policy.
- **Similar policies with small changes**: For policies with complex configurations or conditions, it might save time to create a new policy from a similar policy.

To copy a policy, you must be a member of the *Communication Compliance* or *Communication Compliance Admins* role groups. After you create a new policy from an existing policy, it can take up to 24 hours to view messages that match the new policy configuration.

To copy a policy and create a new policy, complete the following steps:

1. Select the policy you want to copy.
2. Select **Copy policy** on the command bar or select **Copy policy** from the action menu for the policy.
3. In the **Copy policy** pane, accept the default name for the policy in the **Policy name** field or rename the policy. The policy name for the new policy can't be the same as an existing active or deactivated policy. Complete the **Description** field as needed.
4. If you don't need further customization of the policy, select **Copy policy** to complete the process. If you need to update the configuration of the new policy, select **Customize policy**. This selection starts the policy workflow to help you update and customize the new policy.

## Mark a policy as a favorite

After you create a Communication Compliance policy, you can mark the policy as a favorite. When you mark a policy as a favorite, you can filter favorite policies to appear at the top of the policies list. By marking a policy as a favorite, you can also easily sort policies by favorites.

To mark a policy as a favorite, you have the following options:

- **Mark as favorite**: Enables you to mark selected policies as favorites, so you can easily find the policies that you're most interested in rather than having to search for them.
- **Sort favorites**: Sorts the policies by favorites, so your favorite policies appear at the top of the list.
- **Customize columns**: Choose to list the favorites that you want to see. You can also choose to sort favorite policies in ascending or descending order.

To sort policies by groups:

- **All policies**: This is the default view, displaying all the policies in the list.
- **Only favorites**: Groups policies by favorites at the top of the list.

![Screenshot of the Communication Compliance Policies page showing sort by group options.](media/communication-compliance-group-favorites.png)

## Policy activity detection

Communications are scanned every hour from the time you create a policy. For example, if you create an inappropriate content policy at 11:00 AM, the policy gathers Communication Compliance signals every hour starting from when you created the policy. Editing a policy doesn't change this time. To view the last scan date and Coordinated Universal Time (UTC) for a policy, go to the *Last policy scan* column on the **Policy** page. After creating a new policy, you might need to wait up to an hour to view the first policy scan date and time.

The following table outlines the time to detection for supported content types:

| Content type | Time to detection |
| --- | --- |
| Email attachment | 24 hours |
| Email body content | 1 hour |
| Email metadata | 1 hour |
| Email OCR | 24 hours |
| Microsoft 365 Copilot and Microsoft 365 Copilot Chat body content (prompts and responses) | 1 hour |
| Team attachment | 24 hours |
| Teams body content | 1 hour |
| Teams metadata | 1 hour |
| Teams modern attachment | 24 hours |
| Teams OCR | 24 hours |
| Teams shared channels | 24 hours |
| Teams transcripts | 1 hour |
| Viva Engage attachment | Up to 24 hours |
| Viva Engage body content | 1 hour |

For existing policies created before July 31, 2022, it might take up to 24 hours to detect messages and review alerts that match these policies. To reduce the latency for these policies, [copy the existing policy](communication-compliance-policies#copy-a-policy) and create a new policy from the copy. If you don't need to retain any data from the older policy, you can pause or delete it.

To identify an older policy, review *Last policy scan* column on the **Policy** page. Older policies display a full date for the scan while policies created after July 31, 2022 display *1 hour ago* for the scan. To reduce latency, you can also wait until February 28, 2023 for your existing policies to be automatically migrated to the new detection criteria.

## Storage limit notification

Each Communication Compliance policy has a storage limit size of 100 GB or 1 million messages, whichever limit you reach first. As the policy approaches these limits, Communication Compliance automatically sends notification emails to users assigned to the *Communication Compliance* or *Communication Compliance Admins* role groups. Notification messages are sent when the storage size or message count reaches 80, 90, and 95 percent of the limit. When the policy limit is reached, the policy is automatically deactivated and stops processing messages for alerts.

Important

If a policy is deactivated because it reached the storage and message limits, evaluate how to manage the deactivated policy. If you delete the policy, you permanently delete all messages, associated attachments, and message alerts. If you need to maintain these items for future use, don't delete the deactivated policy.

To manage policies that approach the storage and message limits, consider making a copy of the policy to maintain coverage continuity or take the following actions to help minimize current policy storage size and message counts:

- Reduce the number of users assigned to the policy. Removing users from the policy or creating different policies for different groups of users can help slow the growth of policy size and total messages.
- Examine the policy for excessive false positive alerts. Add exceptions or make changes to the policy conditions to ignore common false positive alerts.
- Make a copy of the policy if a policy reaches the storage or message limits and deactivates it to continue detecting and taking action for the same conditions and users.

## Policy settings

The following settings control how Communication Compliance policies are scoped, evaluated, and reviewed.

### Choose which users to include

You can select **All users**, define specific users in a Communication Compliance policy, or select an adaptive scope.

- **All users**: When you select **All users**, you apply the policy to all users and all groups that any user is included in as a member.
- **Select users**: When you define specific users, you apply the policy to the defined users and any groups the defined users are included in as a member. If you choose the **Selected users** option, the **Show insights and recommendations for users who match this policy's conditions but weren't included in the policy** checkbox automatically appears. Leave this checkbox selected if you want to [receive recommendations when users outside of the selected users match the policy conditions](communication-compliance-policies#reduce-user-scoping-blind-spots). This setting isn't available if you choose the **All users** option or the **Select adaptive scopes** option.
- **Select adaptive scope**: An adaptive scope uses a query that you specify to define the membership of users or groups. If you decide to create an adaptive policy, you must [create one or more adaptive scopes](purview-adaptive-scopes#configure-adaptive-scopes) before you create your policy, and then select them when you choose this option. The scopes that you can select depend on the scope types that you add. For example, if you only added a scope type of **User**, you can select **Groups**. To learn more, see [Advantages of using an adaptive scope](purview-adaptive-scopes).

### Choose the communication direction to monitor

By default, the **Direction is** condition appears and you can't remove it. Choose communication direction settings in a policy individually or together:

- **Inbound**: Detects communications sent **to** scoped users from external and internal senders, including other scoped users in the policy.
- **Outbound**: Detects communications sent **from** scoped users to external and internal recipients, including other scoped users in the policy.
- **Internal**: Detects communications **between** the scoped users or groups in the policy.

### Choose sensitive information types

You can include sensitive information types as part of your Communication Compliance policy. Sensitive information types are either predefined or custom data types that help identify and protect credit card numbers, bank account numbers, passport numbers, and more. As part of [Learn about Microsoft Purview Data Loss Prevention](dlp-learn-about-dlp), the sensitive information configuration can use patterns, character proximity, confidence levels, and even custom data types to help identify and flag content that might be sensitive. The default sensitive information types are:

- Financial
- Medical and health
- Privacy
- Custom information type

Important

Sensitive info types have two different ways of defining the max unique instance count parameters. To learn more, see [Create custom sensitive information types](sit-create-a-custom-sensitive-information-type).

The Communication Compliance solution supports default sensitive information types and bundled named-entity sensitive information types, which are collections of sensitive information types. For more information about sensitive information details and the patterns included in the default types, see [Sensitive information type entity definitions](sit-sensitive-information-type-entity-definitions#sensitive-information-type-entity-definitions). For information on supported bundled named-entity sensitive information types, see the following articles:

- [All credentials](sit-defn-all-creds)
- [All full names](sit-defn-all-full-names)
- [All medical terms and conditions](sit-defn-all-medical-terms-conditions)
- [All Physical Addresses](sit-defn-all-physical-addresses)

For more information about sensitive information details and the patterns included in the default types, see [Sensitive information type entity definitions](sit-sensitive-information-type-entity-definitions#sensitive-information-type-entity-definitions).

### Configure custom keyword dictionaries

Configure custom keyword dictionaries (or lexicons) to easily manage keywords specific to your organization or industry. Keyword dictionaries support up to 100 KB of terms (post-compression) in the dictionary and support any language. The tenant limit is also 100 KB after compression. If needed, you can apply multiple custom keyword dictionaries to a single policy or have a single keyword dictionary per policy. You can source these dictionaries from a file, such as a .CSV or .TXT list, or from [an imported keyword list](sit-create-a-keyword-dictionary). Use custom dictionaries when you need to support terms or languages specific to your organization and policies.

### Use Microsoft-provided trainable classifiers

Communication Compliance policies that use Microsoft provided trainable classifiers inspect and evaluate messages that meet a [minimum word count requirement](classifier-tc-definitions#word-count-requirements), depending on the language of the content. Custom trainable classifiers aren't supported. For a complete list of supported languages, word count requirements, and file types for Microsoft provided trainable classifiers, see [Trainable classifier definitions](classifier-tc-definitions).

To identify and take action on messages containing inappropriate language content that doesn't meet the word count requirement, create a sensitive information type or custom keyword dictionary for Communication Compliance policies detecting this type of content.

| Microsoft provided trainable classifier | Description |
| --- | --- |
| [Corporate sabotage](trainable-classifiers-definitions#corporate-sabotage) | Detects messages that might mention acts to damage or destroy corporate assets or property. This classifier can help you manage regulatory compliance obligations such as NERC Critical Infrastructure Protection standards or state by state regulations like Chapter 9.05 RCW in Washington state. |
| [Customer complaints](trainable-classifiers-definitions#customer-complaints) | Detects messages that might suggest customer complaints made on your organization's products or services, as required by law for regulated industries. This classifier can help you manage regulatory compliance obligations such as FINRA Rule 4530, FINRA 4513, FINRA 2111, Consumer Financial Protection Bureau, Code of Federal Regulations Title 21: Food and Drugs, and the Federal Trade Commission Act. |
| [Discrimination](trainable-classifiers-definitions#discrimination) | Detects potentially explicit discriminatory language and is particularly sensitive to discriminatory language against the African American/Black communities when compared to other communities. |
| [Gifts & entertainment](trainable-classifiers-definitions#gifts--entertainment) | Detects messages that might suggest exchanging gifts or entertainment in return for service, which violates regulations related to bribery. This classifier can help you manage regulatory compliance obligations such as Foreign Corrupt Practices Act (FCPA), UK Bribery Act, and FINRA Rule 2320. |
| [Harassment](trainable-classifiers-definitions#harassment) | Detects potentially offensive content in multiple languages that targets people regarding race, color, religion, national origin. |
| [Money laundering](trainable-classifiers-definitions#money-laundering) | Detects signs that might suggest money laundering or engagement in acts to conceal or disguise the origin or destination of proceeds. This classifier can help you manage regulatory compliance obligations such as the Bank Secrecy Act, the USA Patriot Act, FINRA Rule 3310, and the Anti-Money Laundering Act of 2020. |
| [Profanity](trainable-classifiers-definitions#profanity) | Detects potentially profane content in multiple languages that would likely offend most people. |
| [Regulatory collusion](trainable-classifiers-definitions#regulatory-collusion) | Detects messages that might violate regulatory anti-collusion requirements such as an attempted concealment of sensitive information. This classifier can help you manage regulatory compliance obligations such as the Sherman Antitrust Act, Securities Exchange Act 1933, Securities Exchange Act of 1934, Investment Advisers Act of 1940, Federal Commission Act, and the Robinson-Patman Act. |
| [Stock manipulation](trainable-classifiers-definitions#stock-manipulation) | Detects signs of possible stock manipulation, such as recommendations to buy, sell, or hold stocks that might suggest an attempt to manipulate the stock price. This classifier can help you manage regulatory compliance obligations such as the Securities Exchange Act of 1934, FINRA Rule 2372, and FINRA Rule 5270. |
| [Threat](trainable-classifiers-definitions#threat) | Detects potential threatening content in multiple languages aimed at committing violence or physical harm to a person or property. |
| [Unauthorized disclosure](trainable-classifiers-definitions#unauthorized-disclosure) | Detects sharing of information containing content that is explicitly designated as confidential or internal to unauthorized individuals. This classifier can help you manage regulatory compliance obligations such as FINRA Rule 2010 and SEC Rule 10b-5. |

Important

Microsoft provided trainable classifiers might detect a large volume of bulk sender/newsletter content due to a known issue. You can mitigate the detection of large volumes of bulk sender/newsletter content by selecting the [**Filter email blasts** check box](communication-compliance-configure#step-5-required-create-a-communication-compliance-policy) when you create the policy. You can also edit an existing policy to turn on this feature.

### Content safety classifiers based on large language models

Communication Compliance includes a set of Azure AI classifiers for Microsoft 365 Copilot, Teams, and Viva Engage communications. These classifiers run on large language models and are highly accurate. They evaluate messages containing three or more words. If the evaluated severity is 4 or higher, the solution displays the message as an alert and adds a **Severity** column to the **Alerts** dashboard to make it easier to prioritize alerts. Investigators can sort and filter on the **Severity** column.

The **Severity** column only appears if the policy match comes from one of the classifiers listed in the following table. For all other classifiers, the column is empty.

The following table describes the classifiers:

| Classifier | Description |
| --- | --- |
| Hate | *Hate* refers to any content that attacks or uses pejorative or discriminatory language with reference to a person or identity group based on certain differentiating attributes of these groups, including but not limited to race, ethnicity, nationality, gender identity and expression, sexual orientation, religion, immigration status, ability status, personal appearance, and body size. |
| Sexual | *Sexual* describes language related to anatomical organs and genitals, romantic relationships, acts portrayed in erotic or affectionate terms, pregnancy, physical sexual acts, including those portrayed as an assault or a forced sexual violent act against one’s will, prostitution, pornography, and abuse. |
| Violence | *Violence* describes language related to physical actions intended to hurt, injure, damage, or kill someone or something; describes weapons, guns and related entities, such as manufactures, associations, legislation, and so on. |
| Self-harm | *Self-harm* describes language related to physical actions intended to purposely hurt, injure, damage one’s body, or kill oneself. |

[Learn more about Azure AI Content Safety](https://azure.microsoft.com/products/ai-services/ai-content-safety/)

#### Considerations when using classifiers

Keep the following limitations and considerations in mind when using content safety classifiers:

- Only Microsoft 365 Copilot, Teams, and Viva Engage workloads are supported.
- The solution evaluates only messages containing five or more words. It doesn't evaluate attachments and OCR images.
- The solution doesn't evaluate Teams meeting transcripts.
- Feedback loop isn't yet supported to submit misclassified items to Microsoft.
- The solution supports up to 10,000 characters per message.
- [Learn about supported languages](/en-us/azure/ai-services/content-safety/language-support)

### Detect risky generative AI interactions

Communication Compliance detects harmful user-generated and AI-generated content in applications and services. This detection includes evaluation of user prompts submitted to generative AI services and the inclusion of known text content that might be sensitive to your organization.

The following table describes the classifiers.

| Classifier | Description |
| --- | --- |
| [Prompt Shield](/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection) | Detects adversarial user input attacks such as user prompt injection attacks (jailbreak). User prompt injection attacks deliberately exploit system vulnerabilities to elicit unauthorized behavior from the large language model. |
| [Protected material](/en-us/azure/ai-services/content-safety/concepts/protected-material) | Detects known text content that might be protected under copyright or branding laws. Detecting the display of protected material in generative AI responses ensures compliance with intellectual property laws and maintains content originality. |

For more information, see [Learn more about Azure AI Content Safety](/en-us/azure/ai-services/content-safety/overview).

### Configure optical character recognition (OCR) scanning

Note

Microsoft Purview includes [OCR (preview) settings](ocr-learn-about) for Microsoft Purview Insider Risk Management, Microsoft Purview Data Loss Prevention, Microsoft Purview Data Loss Management, and auto-labeling. Use the OCR (preview) settings to provide image-scanning capabilities for those solutions and technologies. Communication Compliance has its own built-in OCR scanning functionality as described in this section and doesn't support the OCR (preview) settings at this time.

You can configure built-in or custom Communication Compliance policies to scan and identify printed or handwritten text from images that might be inappropriate in your organization. Integrated [Azure AI services and optical scanning support](/en-us/azure/ai-services/computer-vision/overview-ocr) for identifying text in images help analysts and investigators detect and act on instances where inappropriate conduct might be missed in communications that is primarily nontextual.

You can enable optical character recognition (OCR) in new policies from templates, custom policies, or update existing policies to expand support for processing embedded images and attachments. When you enable OCR in a policy created from a policy template, the solution automatically scans embedded or attached images in email and Microsoft Teams chat messages. For images embedded in document files, OCR scanning isn't supported. For custom policies, configure one or more conditional settings associated with keywords, Microsoft provided trainable classifiers, or sensitive info types in the policy to enable the selection of OCR scanning.

The solution scans and processes images from 100 KB to 4 MB in the following image formats:

- .jpg/.jpeg (joint photographic experts group)
- .png (portable network graphics)
- .bmp (bitmap)
- .tiff (tag image file format)

When you review pending policy matches for policies with OCR enabled, you see images identified and matched to policy conditions as child items for associated alerts. You can view the original image to evaluate the identified text in context with the original message. It might take up to 48 hours for detected images to be available with alerts.

### Choose conditions for your policies

The conditions you choose for a policy apply to communications from both email and third-party sources in your organization (Instant Bloomberg, for example).

At this time, the condition names that you choose depend on whether you're creating a new policy or an existing policy:

- For *new policies*, we recommend using the condition builder. The condition builder supports the *OR* operator, which enables you to combine multiple conditions in the same policy to create compound conditions with AND, OR, and NOT operators. This support helps you address complex scenarios for your unique compliance requirements. If you create a new policy with a template, Communication Compliance automatically uses the condition builder. Learn more about the condition builder.

    All exceptions in the condition builder are replaced with a NOT condition. You must include the NOT condition within a nested group.
- For *existing policies*, use the condition names listed in the first column in the following table.

Tip

To save time, you can [test certain conditions before creating your policy](communication-compliance-configure#test-conditions-preview-when-you-create-or-edit-a-policy).

#### Condition names for existing and new policies

The following table lists condition names to use for existing policies vs. new policies (using the condition builder). It also lists how to use each condition.

| Condition name for existing policies | Condition name for new policies | How to use this condition |
| --- | --- | --- |
| **Attachment contains any of these words** **Attachment contains none of these words** | **Attachment contains words or phrases** | To apply the policy when certain words or phrases are included or excluded in a message attachment (such as a Word document).Make sure to use the following syntax when entering conditional text: - Remove all leading and trailing spaces.- Add quotation marks before and after each keyword or key phrase.- Separate each keyword or key phrase with a comma.- Don't include spaces between items separated by a comma. **Example:** "banker","insider trading","confidential 123"Each word or phrase you enter is applied separately (only one word must apply for the policy to apply to the attachment). For more information about entering words or phrases, see the next section Matching words and phrases to emails or attachments. |
| **Attachment is any of these file types** **Attachment is none of these file types** | **Attachment file extension is** | To bring communications into scope that include or exclude specific types of attachments, enter the file extensions (such as .exe or .pdf). If you want to include or exclude multiple file extensions, enter file types separated by a comma (example *.exe,.pdf,.zip*). Don't include spaces between items separated by a comma. Only one attachment extension must match for the policy to apply. |
| **Attachment is larger than** **Attachment is not larger than** | **Attachment size equals or is larger than** | To review messages based on the size of their attachments, specify the maximum or minimum size an attachment can be before the message and its attachments are subject to review. For example, for an existing policy, if you specify **Attachment is larger than** &gt; **2.0 MB**, all messages with attachments 2.01 MB and over are subject to review. You can choose bytes, kilobytes, megabytes, or gigabytes for this condition. |
| **Content contains any of these sensitive info types** | **Content contains sensitive info types** | Apply to the policy when any sensitive information types are included or excluded in a message. Each sensitive information type you choose is applied separately and only one of these sensitive information types must apply for the policy to apply to the message. For more information about custom sensitive information types, see [Learn about sensitive information types](sensitive-information-type-learn-about). |
| **Content matches any of these classifiers** | **Content matches trainable classifiers** | Apply to the policy when any trainable classifiers are included or excluded in a message. Some classifiers are predefined in your organization, and custom classifiers must be configured separately before they're available for this condition. For existing policies, only one trainable classifier can be defined as a condition in a policy. If you're using the condition builder for a new policy, you're not limited to a single trainable classifier. For more information about configuring trainable classifiers, see [Learn about trainable classifiers](classifier-learn-about). |
| **Message contains any of these words** **Message contains none of these words** | **Message contains words or phrases** | To apply the policy when certain words or phrases are included or excluded in a message. Make sure to use the following syntax when entering conditional text: - Remove all leading and trailing spaces.- Add quotation marks before and after each keyword or key phrase.- Separate each keyword or key phrase with a comma.- Don't include spaces between items separated by a comma. **Example:** "banker","insider trading","confidential 123"Each word or phrase you enter is applied separately (only one word must apply for the policy to apply to the message). For more information about entering words and phrases, see the next section Matching words and phrases to emails or attachments. |
| **Message is classified with any of these labels** **Message is not classified with any of these labels** | **Message has retention labels applied** | To apply the policy when certain retention labels are included or excluded in a message. Retention labels must be configured separately and configured labels are chosen as part of this condition. Each label you choose is applied separately (only one of these labels must apply for the policy to apply to the message). For more information about retention labels, see [Learn about retention policies and retention labels](retention). |
| **Message is received from any of these domains** **Message is not received from any of these domains** | **Sender domain is** | Apply the policy to include or exclude specific domains in received messages. Make sure to use the following syntax when entering conditional text: -Enter each domain and separate multiple domains with a comma. -Don't include spaces between items separated by a comma.-Remove all leading and trailing spaces. Each domain entered is applied separately, only one domain must apply for the policy to apply to the message. If you want to use **Message is received from any of these domains** to look for messages from specific domains, you need to combine this with another condition like **Message contains any of these words**, or **Content matches any of these classifiers**, or you might get unexpected results.  For existing policies, if you want to scan all emails but want to exclude messages from a specific domain that don't need review (newsletters, announcements, and so on), you must configure a **Message is not received from any of these domains** condition that excludes the domain (example 'contoso.com,wingtiptoys.com'). |
| **Message is received from any of these external email addresses** **Message is not received from any of these external email addresses** | **Sender is** | Apply the policy to include or exclude messages received or not received from specific external email addresses (example someone@outlook.com).Use this condition to detect only messages that come from outside the organization (messages that cross the firewall).Make sure to use the following syntax when entering email addresses:- Enter each email address and separate multiple email addresses with a comma.- Don't include spaces between email addresses separated by a comma.- Remove all leading and trailing spaces.- Remove any single quote or double quotes |
| **Message is sent to any of these domains** **Message is not sent to any of these domains** | **Recipient domain is** | Apply the policy to include or exclude specific domains in sent messages. Make sure to use the following syntax when entering conditional text: -Enter each domain and separate multiple domains with a comma. -Don't include spaces between items separated by a comma. -Remove all leading and trailing spaces.Each domain is applied separately; only one domain must apply for the policy to apply to the message.  For existing policies, if you want to exclude all emails sent to two specific domains, configure the **Message is not sent to any of these domains** condition with the two domains (example 'contoso.com,wingtiptoys.com'). |
| **Message is sent to any of these external email addresses** **Message is not sent to any of these external email addresses** | **Recipient is** | Apply the policy to include or exclude messages sent or not sent to specific external email addresses (example someone@outlook.com).Use this condition to detect only messages that are sent outside the organization (messages that cross the firewall).Make sure to use the following syntax when entering email addresses:- Enter each email address and separate multiple email addresses with a comma.- Don't include spaces between email addresses separated by a comma.- Remove all leading and trailing spaces.- Remove any single quote or double quotes |
| **Message size is larger than** **Message size is not larger than** | **Message size equals or is larger than** | To review messages based on a certain size, use these conditions to specify the maximum or minimum size a message can be before it's subject to review. For example, for an existing policy, if you specify **Message size is larger than** &gt; **1.0 MB**, all messages that are 1.01 MB and larger are subject to review. You can choose bytes, kilobytes, megabytes, or gigabytes for this condition. |

Important

If a condition includes a list, don't include spaces between list items. For example, enter "bias,harassment" instead of "bias, harassment".

#### Matching words and phrases to emails or attachments

Each word you enter and separate with a comma is applied separately (only one word must apply for the policy condition to apply to the email or attachment). For example, let's use the condition **Message contains any of these words** with the keywords "banker", "confidential", and "insider trading" separated by a comma (banker,confidential,"insider trading"). The policy applies to any messages that includes the word "banker", "confidential", or the phrase "insider trading". Only one of these words or phrases must occur for this policy condition to apply. Words in the message or attachment must exactly match what you enter.

Important

When importing a custom dictionary file, each word or phrase must be separated with a carriage return and on a separate line. For example:

*banker* *confidential* *insider trading*

To scan both email messages and attachments for the same keywords, create a [custom keyword dictionary](sit-create-a-keyword-dictionary) for the terms you want to scan. This policy configuration identifies defined keywords that appear in either the email message **OR** in the email attachment. Using the standard conditional policy settings (**Message contains any of these words** and **Attachment contains any of these words**) to identify terms in messages and in attachments requires the terms to be present in **BOTH** the message and the attachment.

#### Use the condition builder to create complex conditions (new policies)

If you want to create nested conditions or use the **OR** operator in addition to the **AND** operator in new policies, use the condition builder. To use multiple operators (both **AND** and **OR**) in the same condition, you must create a separate group for each operator. Select **Add group** to create a group.

To use the condition builder, you must first opt in. To do this, in the **Conditions** section, above the existing condition builder, turn the **Condition builder** option on. If you create a new policy by using a template, you don't have to opt in to the condition builder. Communication Compliance automatically uses the condition builder for new policies based on templates.

All exceptions in the condition builder are replaced with a NOT condition. For example, the existing condition builder includes the **Message is not received from any of these domains** condition. This condition is renamed to **Sender domain is** in the condition builder, so to build the **Message is not received from any of these domains** condition in the condition builder, use the **Sender domain is** condition together with the **NOT** condition. You must include the **NOT** condition within a nested group.

You can use conditions with trainable classifiers and sensitive info types as an exception by using the **NOT** condition in a nested group, but keyword highlighting isn't available in this case.

To make it easier to see a summary of a complex condition that includes multiple **AND** and **OR** operators or groups, the condition builder includes a simplified summary view of the condition. To see the summary for a condition you built, turn on the **Quick Summary** option.

For scenarios that show how to use conditions in policies, see [Scenarios for using conditions in Communication Compliance policies](communication-compliance-conditions-scenarios).

### Set the review percentage for policy matches

To reduce the amount of content to review, specify a percentage of all communications governed by a Communication Compliance policy. Communication Compliance selects a real-time, random sample of content from the total percentage of content that matches chosen policy conditions. If you want reviewers to review all items, configure **100%** in a Communication Compliance policy.

### Filter email blasts

Use the **Filter email blasts** setting to exclude messages sent from email blast services. Messages that match the conditions you specify don't generate alerts. This exclusion includes bulk email, such as newsletters, and spam, phishing, and malware. When you select this option, you can view a [report](communication-compliance-reports-audits#detailed-reports) that lists the bulk email senders that were filtered out. Reports are retained for 60 days. The list of senders is filtered before the content is analyzed, so there might be senders that don't match the content conditions.

This setting is on by default for new policies. If the **Filter email blasts setting** is off for existing policies, a recommendation is generated to turn on the setting.

## Manage alert policies

After you configure a policy, Communication Compliance automatically creates a corresponding alert policy and generates alerts for messages that match conditions defined in the policy. It can take up to 24 hours after creating a policy to start receiving alerts from activity indicators. By default, all policy matches alert triggers are assigned a severity level of medium in the associated alert policy. Communication Compliance generates alerts for a policy once the aggregation trigger threshold level is met in the associated alert policy. A single email notification is sent once every 24 hours for any alerts, regardless of the number of individual messages that match policy conditions. For example, Contoso has an inappropriate content policy enabled and for January 1, there were 100 policy matches that generated six alerts. A single email notification for the six alerts is sent at end of January 1.

For Communication Compliance policies, the system configures the following alert policy values by default:

| Alert policy trigger | Default value |
| --- | --- |
| Aggregation | Simple aggregation |
| Threshold | Default: 4 activities  Minimum: 3 activities  Maximum: 2,147,483,647 activities |
| Window | Default: 60 minutes  Minimum: 60 minutes  Maximum: 10,000 minutes |

Note

The alert policy threshold trigger settings for activities support a minimum value of 3 or higher for Communication Compliance policies.

You can change the default settings for triggers on number of activities, period for the activities, and for specific users in alert policies on the **Alert policies** page in Microsoft Purview.

### Change the severity level for an alert policy

To change the severity level for an alert policy, see [Alert policies in the Microsoft Defender portal](/en-us/defender-xdr/alert-policies#manage-alerts).