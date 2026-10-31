---
layout: Conceptual
title: Create and manage Insider Risk Management policies | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-policies
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Create and manage Microsoft Purview Insider Risk Management policies to define users in scope, configure risk indicators and thresholds, and use templates, analytics, and anomaly detections to identify risky activity.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: how-to
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-25T00:00:00.0000000Z
audience: itpro
ms.collection:
- purview-compliance
ms.custom: admindeeplinkCOMPLIANCE, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: dd65324d-ae18-18c8-440c-c836a46107d3
document_version_independent_id: dd65324d-ae18-18c8-440c-c836a46107d3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-policies.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-policies
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-policies.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: b9a95489-e324-3574-9baa-63e41351de66
---

# Create and manage Insider Risk Management policies | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Insider Risk Management policies determine which users are in scope and which types of risk indicators are configured for alerts. You can quickly create a security policy that applies to all users in your organization or define individual users or groups for management in a policy. Policies support content priorities to focus policy conditions on multiple or specific Microsoft Teams, SharePoint sites, data sensitivity types, and data labels. By using templates, you can select specific risk indicators and customize event thresholds for policy indicators, effectively customizing risk scores, and level and frequency of alerts.

You can also configure quick data leak and data theft policies by departing user policies that automatically define policy conditions based on results from the latest analytics. Also, risk score boosters and anomaly detections help identify potentially risky user activity that is of higher importance or unusual. Policy windows allow you to define the time frame to apply the policy to alert activities and are used to determine the duration of the policy once activated.

For an overview of how policies created with built-in policy templates can help you quickly act on potential risks, see the [Insider Risk Management Policies Configuration video](https://www.youtube.com/watch?v=kudK5ajZTUo).

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Policy dashboard

The **Policy dashboard** lets you quickly see the user and agent policies in your organization, the health of each policy, manually add users to security policies, and view the status of alerts associated with each policy. Your policies are separated into two categories: **User policy** and **Agent policy**. Switch between the two to locate relevant policy details. **Agent policy** covers agents from Microsoft Copilot Studio and Microsoft Foundry.

- **Policy name**: Name assigned to the policy in the policy workflow.
- **Status**: Health status for each policy. Displays number of policy warnings and recommendations, or a status of *Healthy* for policies without issues. You can select the policy to see the health status details for any warnings or recommendations.
- **Active alerts**: Number of active alerts for each policy.
- **Confirmed alerts**: Total number of alerts that resulted in cases from the policy in the last 365 days.
- **Actions taken on alerts**: Total number of alerts that were confirmed or dismissed for the last 365 days.
- **Policy alert effectiveness**: Percentage determined by total confirmed alerts divided by total actions taken on alerts (which is the sum of alerts that were confirmed or dismissed over the past year).

![Screenshot of the Insider Risk Management policy dashboard showing policy names, health status, active alerts, confirmed alerts, and alert effectiveness metrics.](media/insider-risk-policy-dashboard.png)

## Policy recommendations from analytics

Insider risk analytics gives you an aggregate view of anonymized user activities related to security and compliance. With this view, you can evaluate potential insider risks in your organization without configuring any insider risk policies. This evaluation helps your organization identify potential areas of higher risk and helps determine the type and scope of Insider Risk Management policies you might consider configuring. If you decide to act on analytics scan results for [data leaks](insider-risk-management-policy-templates#data-leaks) or [data theft](insider-risk-management-policy-templates#data-theft-by-departing-users) by departing users policies, you can even configure a quick policy based on these results.

For more information about insider risk analytics and policy recommendations, see [Insider Risk Management settings: Analytics](insider-risk-management-settings-analytics).

Note

You must be an unrestricted administrator to access analytics insights. [Learn how administrative groups affect permissions](insider-risk-management-permissions#consider-administrative-units-if-you-want-to-scope-user-permissions-to-a-region-or-department).

## Quick policies

For many organizations, getting started with an initial policy can be a challenge. If you're new to Insider Risk Management or are using the recommended actions to get started, use a quick policy to create and configure a new policy. Quick policy settings automatically populate from recommended best practices or on results from the latest analytics scan in your organization. For example, if the analytics check detected potential data leak activities in your organization, the *Date leaks* quick policy automatically includes the indicators used to detect those activities.

You can choose from the following quick policies:

- **Critical assets protection**: Detects activities involving your organization's most valuable assets. Loss of these assets could result in legal liability, financial loss, or reputational damage.​
- **Data leaks**: Detect potential data leaks from all users in your organization, which can range from accidental oversharing of sensitive info to data theft with malicious intent. ​
- **Data theft from Microsoft 365 apps by users leaving your organization**: Detects potential data theft from Microsoft 365 cloud apps by users leaving your organization or whose account was deleted from Microsoft Entra ID.
- **Data theft from non-Microsoft 365 apps by users leaving your organization**: Detects potential data theft from non-Microsoft 365 cloud apps, including Microsoft Fabric, by users leaving your organization or whose account was deleted from Microsoft Entra ID.
- **Email exfiltration**: Detects when users email sensitive assets outside your organization. For example, users emailing sensitive assets to their personal email address.​

To get started, go to **Insider Risk Management** &gt; **Policies** and select **Create policy** &gt; **Quick policy**. If you're reviewing analytics reports, select **View details** &gt; **Get started** to get started with a quick policy for the applicable area.

When you start the quick policy workflow, review the policy settings and configure the policy with a single selection. If you need to customize a quick policy, change the conditions after the policy is created. Stay up to date with the detection results for a quick policy by configuring email notifications each time you have a policy warning or each time the policy generates a high severity alert.

Note

You must be an unrestricted administrator to create quick policies. [Learn how administrative groups affect permissions](insider-risk-management-permissions#consider-administrative-units-if-you-want-to-scope-user-permissions-to-a-region-or-department).

## Prioritize content in policies

Insider Risk Management policies support specifying a higher priority for content depending on where you store it, the type of content, or how you classify it. You can also choose whether to assign risk scores to all activities detected by a policy or only activities that include priority content. Specifying content as a priority increases the risk score for any associated activity, which in turn increases the chance of generating a high severity alert. However, some activities don't generate an alert at all unless the related content contains built-in or custom sensitive info types or you specify it as a priority in the policy.

For example, your organization has a dedicated SharePoint site for a highly confidential project. Data leaks for information in this SharePoint site could compromise the project and would have a significant impact on its success. By prioritizing this SharePoint site in a Data leaks policy, you automatically increase risk scores for qualifying activities. This prioritization increases the likelihood that these activities generate an insider risk alert and raises the severity level for the alert.

Additionally, you can choose to focus this policy for SharePoint site activity that only includes priority content for this project. Risk scores are assigned and alerts are generated only when specified activities include priority content. Activities without priority content aren't scored, but you can still review them if an alert is generated.

Important

Cumulative exfiltration activity always receives a risk score, regardless of whether or not it contains prioritized content.

The following policy templates support priority content selection:

- Data leaks
- Data leaks by priority users
- Data leaks by risky users
- Data theft by departing users
- Risky AI usage

Note

If you configure a policy to generate alerts only for activity that includes priority content, no changes are applied to risk score boosters.

When you create an Insider Risk Management policy in the policy workflow, you can choose from the following priorities:

- **SharePoint sites**: Assign a higher risk score to any activity associated with all file types in defined SharePoint sites. Users configuring the policy and selecting priority SharePoint sites can select SharePoint sites that they have permission to access. If SharePoint sites aren't available for selection in the policy by the current user, another user with the required permissions can select the sites for the policy later, or the current user should be given access to the required sites.
- **Sensitive information types**: Assign a higher risk score to any activity associated with content that contains [sensitive information types](sit-sensitive-information-type-entity-definitions).
- **Sensitivity labels**: Assign a higher risk score to any activity associated with content that has specific [sensitivity labels](sensitivity-labels) applied.
- **File extensions**: Assign a higher risk score to any activity associated with content that has specific file extensions. Users configuring a data theft/leak policy that selects **File extensions to prioritize** in the policy workflow can define up to 50 file extensions to prioritize in the policy. Entered extensions can include or omit a '.' as the first character of the prioritized extension.
- **Trainable classifiers**: Assign a higher risk score to any activity associated with content that is included in a [trainable classifier](classifier-learn-about). Users configuring a policy that selects Trainable classifiers in the policy workflow can select up to 5 trainable classifiers to apply to the policy. These classifiers can be existing classifiers that identify patterns of sensitive information like social security, credit card, or bank account numbers or custom classifiers created in your organization.

## Sequence detection

Risk management activities might not occur as isolated events. These risks are frequently part of a larger sequence of events. A sequence is a group of two or more potentially risky activities performed one after the other that might suggest an elevated risk. Identifying these related user activities is an important part of evaluating overall risk. When you select sequence detection for data theft or data leaks policies, you see insights from sequence information activities on the **User activity** tab within an Insider Risk Management case. The following policy templates support sequence detection:

- Data leaks
- Data leaks by priority users
- Data leaks by risky users
- Data theft by departing users
- Risky AI usage

These Insider Risk Management policies can use specific indicators and the order that they occur to detect each step in a sequence of risk. Selected sequence detections only detect sequences of risk in the order displayed in policy setup workflow. For policies created from the *Data leaks* and *Data leaks by priority user* templates, you can also select which sequences trigger the policy. File names are used when mapping activities across a sequence. These risks are organized into four main categories of activity:

- **Collection**: Detects download activities by in-scope policy users. Example risk management activities include downloading files from SharePoint sites, third-party cloud services, unallowed domains, or moving files into a compressed folder.
- **Exfiltration**: Detects sharing or extraction activities to internal and external sources by in-scope policy users. An example risk management activity includes sending emails with attachments from your organization to external recipients.
- **Obfuscation**: Detects the masking of potentially risky activities by in-scope policy users. An example risk management activity includes renaming files on a device.
- **Clean-up**: Detects deletion activities by in-scope policy users. An example risk management activity includes deleting files from a device.

Note

Sequence detection uses indicators that you enable in the global settings for Insider Risk Management. If you don't select appropriate indicators, you can turn on these indicators in the sequence detection step in the policy workflow.

You can customize individual threshold settings for each sequence detection type when you configure it in the policy. These threshold settings adjust alerts based on the volume of files associated with the sequence type.

Note

A [sequence](insider-risk-management-policies#sequence-detection) might contain one or more events that are excluded from risk scoring based on your settings configuration. For example, your organization might use the [**Global exclusions** setting](insider-risk-management-settings-global-exclusions) to exclude .png files from risk scoring since .png files aren't normally risky. But a .png file could be used to obfuscate a malicious activity. For this reason, if an event that's excluded from risk scoring is part of a sequence due to an obfuscation activity, the event is included in the sequence since it might be interesting in the context of the sequence. [Learn more about how exclusions that are part of a sequence are shown in the Activity explorer](insider-risk-management-activities#sequences-that-contain-events-excluded-from-risk-scoring).

To learn more about sequence detection management in the **User activity** view, see [Insider Risk Management cases: User activity](insider-risk-management-cases#review-user-activity-in-a-case).

## Cumulative exfiltration detection

With privacy on by default, insider risk indicators help identify unusual levels of risk activities when evaluated daily for users that are in-scope for insider risk policies. Cumulative exfiltration detection uses machine learning models to help you identify when exfiltration activities that a user performs over a certain time exceed the normal amount performed by users in your organization for the past 30 days over multiple exfiltration activity types. For example, if a user shared more files than most users over the past month, this activity is detected and classified as a cumulative exfiltration activity.

Insider Risk Management analysts and investigators might use cumulative exfiltration detection insights to help identify exfiltration activities that might not typically generate [alerts](insider-risk-management-activities#standard-alert-dashboard) but are more than what is typical for their organization. Some examples might be departing users slowly exfiltrate data across a range of days, or when users repeatedly share data across multiple channels more than usual for data sharing for your organization, or compared to their peer groups.

Note

By default, cumulative exfiltration detection generates risk scores based on a user's cumulative exfiltration activity compared to their organization norms. You can enable *Cumulative exfiltration detection* options in the **Policy indicators** section of the Insider Risk Management settings page.

Higher risk scores are assigned to cumulative exfiltration activities for SharePoint sites, sensitive information types, and content with [sensitivity labels](sensitivity-labels#label-priority-order-matters) configured as priority content in a policy or for activity involving labels configured as high priority in [Microsoft Purview Information Protection](information-protection).

Cumulative exfiltration detection is enabled by default when using the following policy templates:

- Data leaks
- Data leaks by priority users
- Data leaks by risky users
- Data theft by departing users

Important

The option to only score activities containing priority content doesn't apply to cumulative exfiltration activities. Cumulative exfiltration activity always receives a risk score, regardless of whether or not it contains prioritized content.

### Peer groups for cumulative exfiltration detection

Insider Risk Management identifies three types of peer groups for analyzing exfiltration activity performed by users. It defines peer groups for users based on the following criteria:

**SharePoint sites**: Insider Risk Management identifies peer groups based on users who access similar SharePoint sites. **Similar organization**: Users with reports and team members based on organization hierarchy. This option requires that your organization uses Microsoft Entra ID to maintain organization hierarchy. **Similar job title**: Users with a combination of organizational distance and similar job titles. For example, a user with a Senior Sales Manager title with a similar role designation as a Lead Sales Manager in the same organization is identified as similar job title. This option requires that your organization uses Microsoft Entra ID to maintain organization hierarchy, role designations, and job titles. If you don't have Microsoft Entra ID configured for organization structure and job titles, then Insider Risk Management identifies peer groups based on common SharePoint sites.

When you enable cumulative exfiltration detection, your organization agrees to share Microsoft Entra data with the Microsoft Purview portal, including organization hierarchy and job titles. If your organization doesn't use Microsoft Entra ID to maintain this information, detection might be less accurate.

Note

Cumulative exfiltration detection uses exfiltration indicators that you enable in the global settings for Insider Risk Management and exfiltration indicators that you select in a policy. As such, cumulative exfiltration detection only evaluates the necessary exfiltration indicators. Cumulative exfiltration activities for [sensitivity labels](sensitivity-labels) configured in priority content generate higher risk scores.

When you enable cumulative exfiltration detection for data theft or data leak policies, insights from cumulative exfiltration activities appear on the **User activity** tab within an Insider Risk Management case. For more information about user activity management, see [Insider Risk Management cases: User activities](insider-risk-management-cases#review-user-activity-in-a-case).

## Policy health

Note

If your policy is [scoped by one or more administrative units](purview-admin-units), you can only view policy health for the policies you're scoped for. If you're an unrestricted administrator, you can view policy health for all policies in the tenant.

The policy health status gives you insights into potential issues with your Insider Risk Management policies. The **Status** column on the **Policies** tab alerts you to policy issues that might prevent user activity from being reported or explain why the number of activity alerts is unusual. The policy health status also confirms that the policy is healthy and doesn't need attention or configuration changes.

Important

You must have the *Insider Risk Management* or the *Insider Risk Management Admins* role to access policy health.

If there are issues with a policy, the policy health status displays notification warnings and recommendations to help you take action to resolve policy issues. These notifications can help you resolve the following issues:

- **Policies with incomplete configuration**. These issues might include missing users or groups in the policy or other incomplete policy configuration steps.
- **Policies with indicator configuration issues**. Indicators are an important part of each policy. If you don't configure indicators, or if you select too few indicators, the policy might not evaluate risky activities as expected.
- **Policy triggers aren't working, or policy trigger requirements aren't properly configured**. Policy functionality might depend on other services or configuration requirements to effectively detect triggering events to activate risk score assignment to users in the policy. These dependencies might include issues with connector configuration, Microsoft Defender for Endpoint alert sharing, or data loss prevention policy configuration settings.
- **Volume limits are nearing or over limits**. Insider Risk Management policies use numerous Microsoft 365 services and endpoints to aggregate risk activity signals. Depending on the number of users in your policies, volume limits might delay identification and reporting of risk activities. Learn more about these limits in the [Policy template limits](insider-risk-management-policy-templates#policy-template-limits) section.

To quickly view the health status for a policy, go to the **Policy** tab and check the **Status** column. You see the following policy health status options for each policy:

- *Healthy*: No issues are identified with the policy.
- *Recommendations*: An issue with the policy that might prevent the policy from operating as expected.
- *Warnings*: An issue with the policy that might prevent it from identifying potentially risky activities.

For more details about any recommendations or warnings, select a policy on the **Policy** tab to open the policy details card. The **Notifications** section of the details card displays more information about the recommendations and warnings, including guidance on how to address these issues.

![Screenshot of the Insider Risk Management policy health details card showing warnings and recommendations for resolving policy configuration issues.](media/insider-risk-policy-health.png)

### Notification messages

Use the following table to learn more about recommendations and warning notifications and actions to take to resolve potential issues.

| Notification messages | Policy templates | Causes / Try this action to fix |
| --- | --- | --- |
| **DLP policy doesn't meet requirements** | - Data leaks  - Data leaks by priority users | DLP policies used as triggering events must be configured to generate high severity alerts.  1. Edit your DLP policy to assign applicable alerts as *High severity*.  OR  2. Edit this policy and select *User performs an exfiltration activity* as the triggering event. |
| **DLP policy isn't selected as the triggering event** | - Data leaks  - Data leaks by priority users | A DLP policy wasn't selected as a triggering event or the selected DLP policy was deleted.  Edit the policy and either select an active DLP policy or 'User performs an exfiltration activity' as the triggering event in the policy configuration. |
| **DLP policy used in this policy is turned off** | - Data leaks  - Data leaks by priority users | DLP policy used in this policy is turned off.  1. Turn the DLP policy assigned to this policy on.  OR  2. Edit this policy and either select a new DLP policy or 'User performs an exfiltration activity' as the triggering event in the policy configuration. |
| **HR connector hasn't uploaded data recently** | - Data theft by departing user  - Security policy violations by departing user  - Data leaks by risky users  - Security policy violations by risky users | HR connector didn't import data in more than 7 days.  Check that your HR connector is configured correctly and sending data. |
| **HR connector isn't configured or working as expected** | - Data theft by departing user  - Security policy violations by departing user  - Data leaks by risky users  - Security policy violations by risky users | There's an issue with the HR connector.  1. If you're using an HR connector, check that your HR connector is sending correct data  OR  2. Select the Microsoft Entra account deleted triggering event. |
| **Microsoft Defender for Endpoint alerts aren't being shared with the Microsoft Purview portal** | - Security policy violations  - Security policy violations by departing users  - Security policy violations by risky users  - Security policy violations by priority users | Microsoft Defender for Endpoint alerts aren't being shared with the Microsoft Purview portal.  Configure sharing of Microsoft Defender for Endpoint alerts. |
| **No devices are onboarded** | - Data theft by departing users  - Data leaks  - Data leaks by risky users  - Data Leaks by priority users | Device indicators are selected but there aren't any devices onboarded to the Microsoft Purview portal  Check whether devices are onboarded and meet requirements. |
| **No indicators have been selected for this policy** | All policy templates | Indicators weren't selected for the policy  Edit your policy and select appropriate policy indicators for the policy. |
| **No priority user groups are included in this policy** | - Data leaks by priority users  - Security policy violations by priority users | Priority user groups aren't assigned to the policy.  Configure priority user groups in Insider Risk Management settings and assign priority user groups to the policy. |
| **No triggering event has been selected for this policy** | All policy templates | A triggering event isn't configured for the policy  Risk scores won't be assigned to user activities until you edit the policy and select a triggering event. |
| **No users or groups are included in this policy** | All policy templates | Users or groups aren't assigned to the policy.  Edit your policy and select users or groups for the policy. |
| **Policy hasn't generated any alerts** | All policy templates | You might want to review your policy configuration so that you're analyzing the most relevant scoring activity.  1. Confirm that you selected indicators that you want to score. The more indicators selected, the more activities are assigned risk scores.  2. Review threshold customization for policy. If the thresholds selected don't align with your organization's risk tolerance, adjust the selections so that alerts are created based on your preferred thresholds.  3. Review the users and groups selected for the policy. Confirm you selected all of the applicable users and groups.  4. For security violation policies, confirm you selected the alert triage status that you want to score for Microsoft Defender for Endpoint alerts in Intelligent Detections in settings. |
| **Policy isn't assigning risk scores to activity** | All policy templates | You might want to review your policy scope and triggering event configuration so that the policy can assign risk scores to activities  1. Review the users that are selected for the policy. If you have few users selected, you might want to select additional users.  2. If you're using an HR connector, check that your HR connector is sending the correct data.  3. If you're using a DLP policy as your triggering event, check your DLP policy configuration to ensure it's configured to be used in this policy.  4. For security violation policies, review the Microsoft Defender for Endpoint alert triage status selected in Insider risk settings &gt; Intelligent detections. Confirm that the alert filter isn't too narrow. |
| **Triggering event is repeatedly occurring for over 15% of users in this policy** | All policy templates | Adjust the triggering event to help reduce how often users are brought into the policy scope. |
| **We're unable to check the status of your HR connector right now, please check again later** | - Data theft by departing user  - Security policy violations by departing user  - Data leaks by risky users  - Security policy violations by risky users | The Insider Risk Management solution is unable to check the status of your HR connector.  Check that your HR connector is configured correctly and sending data, or come back and check the policy status. |
| **You're approaching the maximum limit of users being actively scored for this policy template** | All policy templates | Each policy template has a maximum number of included users. See the [Policy template limits](insider-risk-management-policy-templates#policy-template-limits) section for details.  Review the users in the Users tab and remove any users who don't need to be scored anymore. |
| **Your organization doesn't have a Microsoft Defender for Endpoint subscription** | - Security policy violations  - Security policy violations by departing users  - Security policy violations by risky users  - Security policy violations by priority users | An active Microsoft Defender for Endpoint subscription wasn't detected for your organization.  Until a Microsoft Defender for Endpoint subscription is added, these policies won't assign risk scores to user activity. |

## Create a new policy

To create a new Insider Risk Management policy, generally use the policy workflow in the **Insider Risk Management** solution in the Microsoft Purview portal. You can also create quick policies for general data leaks and data theft by departing users from Analytics checks if applicable.

Complete [Create an Insider Risk Management policy](insider-risk-management-configure#step-6-required-create-an-insider-risk-management-policy) to configure new insider risk policies.

## Update a policy

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Policies** in the left navigation.
4. On the policy dashboard, select the policy you want to update.
5. On the policy details page, select **Edit policy**.
6. On the **Name and description** page, update the description for the policy if you want. 
    Note

    You can't edit the **Policy template** or **Name** field.
7. Select **Next** to continue.
8. Follow the remaining steps to [configure your Insider Risk Management policy](insider-risk-management-configure#step-6-required-create-an-insider-risk-management-policy).

## Copy a policy

You might need to create a new policy that's similar to an existing policy but needs just a few configuration changes. Instead of creating a new policy from scratch, you can copy an existing policy and then modify the areas that need to be updated in the new policy.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Policies** in the left navigation.
4. On the policy dashboard, select the policy you want to copy.
5. On the policy details page, select **Copy**.
6. In the policy workflow, name the new policy, and then update the policy configuration as needed.

## Immediately start scoring user activity

Some scenarios require assigning risk scores to users with insider risk policies outside of the Insider Risk Management triggering event workflow. Use **Start scoring activity for users** on the **Policies** tab to manually add one or more users to one or more insider risk policies for a specific amount of time. This action starts assigning risk scores to their activity and bypasses the requirement for a user to have a triggering indicator, like a DLP policy match or an Employment End Date from the HR Connector.

The value in the **Reason for scoring activity** field appears on the users' activity timeline. The **Users** dashboard displays users you manually add to policies, and alerts are created if the activity meets the policy alert thresholds. You can have up to 4,000 users in scope that you manually add by using the **Start scoring activity for users** feature.

Some scenarios where you might want to immediately start scoring user activities include:

- You identify users with risk concerns and want to immediately start assigning risk scores to their activity for one or more of your policies.
- There's an incident that might require you to immediately start assigning risk scores to involved users' activity for one or more of your policies.
- You haven't configured your HR connector yet, but you want to start assigning risk scores to user activities for HR events by uploading a .csv file.

Note

It might take several hours for manually added users to appear in the **Users** dashboard. Activities for the previous 90 days for these users might take up to 24 hours to display. To view activities for manually added users, go to the **Users** tab, select the user on the **Users** dashboard, and then open the **User activity** tab on the details pane.

### Manually start scoring activity for users in one or more Insider Risk Management policies

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Policies** in the left navigation.
4. On the policy dashboard, select the policies where you want to add users.
5. Select **Start scoring activity for users**.
6. In the **Add users to multiple policies** pane, enter a reason for adding the users in the **Reason** field.
7. Define the number of days to score the user's activity in the **This should last for (choose between 5 and 30 days)** field.
8. Enter the name of the user you want to add, or use the **Search user to add to policies** field to search for a user, then select the user name. Repeat this process to assign additional users. The list of users you select appears in the users section of the **Add users to multiple policies** pane.

    Note

    If the policy is scoped by [one or more administrative units](purview-admin-units), you can only see users that you're scoped for.

    Select **Import** to import a .csv (comma-separated values) file to import a list of users. The file must be in the following format and must list the user principal names:

    ```csv
    user principal name
    user1@domain.com
    user2@domain.com
    ```
9. Select **Add users to policies** to accept the changes.

## Stop scoring users in a policy

To stop scoring users in a policy, see the [Insider Risk Management users: Remove users from in-scope assignment to policies](insider-risk-management-users#remove-users-from-in-scope-assignment-to-policies) article.

## Delete a policy

Important

You can't undo a policy deletion.

When you delete a policy, you have two options. You can:

- Delete just the policy.
- Delete the policy and all associated alerts and users.

If you choose the second option:

- All alerts generated by that policy are deleted unless they're associated with a case. Associated cases are never deleted when you delete a policy.
- Any user associated with an alert from that policy is removed from the **Users** page.
- If a user is in scope of more than one policy, you remove the user only from the policy that you're deleting. You don't remove the user from other active policies.

For example, you might create a policy for test purposes before rolling it out to your organization. After you finish testing, you can quickly delete the policy and all associated test data so that you can start fresh when you're ready to push the policy live.

It can take up to 72 hours to complete a policy deletion.

Note

If you delete a policy associated with Insider Risk Management [Adaptive Protection](insider-risk-management-adaptive-protection), you see a warning that Adaptive Protection stops assigning insider risk levels to users until you choose a different policy in Adaptive Protection. This warning appears because Adaptive Protection must be associated with a policy to be in effect.

### To delete a policy

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Policies** in the left navigation.
4. On the policy dashboard, select the policy you want to delete.
5. Select **Delete** on the dashboard toolbar.
6. Choose one of the following options:

    - Select **Delete only the policy**.
    - Select **Delete the policy and all associated alerts and users**.

    Important

    You can't undo a policy deletion.
7. Select **Confirm**.

    You see a message in the upper part of the screen that tells you if the deletion was successful or whether it's pending.