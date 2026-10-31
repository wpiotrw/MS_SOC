---
layout: Conceptual
title: Help dynamically mitigate risks with Adaptive Protection | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-adaptive-protection
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to mitigate risks with Adaptive Protection and Microsoft Purview Data Loss Prevention (DLP),  Microsoft Purview Data Lifecycle Management, and Microsoft Entra Conditional Access policies.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance, Conditional Access, DLP, data lifecycle management
ms.service: purview
ms.subservice: purview-adaptive-protection
ms.topic: how-to
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: itpro
ms.collection:
- purview-compliance
ms.custom: msecd-doc-authoring-1014, admindeeplinkCOMPLIANCE, sfi-ga-nochange, sfi-image-nochange
ai-usage: ai-assisted
locale: en-us
document_id: 0659d3ac-b65c-2957-80be-8bf91a2e4449
document_version_independent_id: 0659d3ac-b65c-2957-80be-8bf91a2e4449
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-adaptive-protection.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-adaptive-protection
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-adaptive-protection.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: b8964f3b-d84d-5d68-bc60-0db4bf223a31
---

# Help dynamically mitigate risks with Adaptive Protection | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Adaptive protection in Microsoft Purview uses machine learning to identify the most critical risks and proactively and dynamically apply protection controls from:

- [Microsoft Purview Data Loss Prevention (DLP)](dlp-learn-about-dlp)
- [Microsoft Purview Data Lifecycle Management (preview)](data-lifecycle-management)
- [Microsoft Entra Conditional Access (preview)](/en-us/entra/identity/conditional-access/overview)

Integration with data loss prevention, data lifecycle management, and Conditional Access helps organizations automate their response to insider risks and reduces the time required to identify and remediate potential threats. By using the capabilities of all four solutions, organizations can create a more comprehensive security framework that addresses both internal and external threats.

Important

To learn about licensing requirements for using Adaptive Protection with data loss prevention, data lifecycle management, and Conditional Access, see [Microsoft 365, Office 365, Enterprise Mobility + Security, and Windows 11 Subscriptions](https://aka.ms/M365EnterprisePlans).

Adaptive protection helps mitigate potential risks by using:

- **Context-aware detection**. Helps identify the most critical risks with ML-driven analysis of both content and user activities.
- **Dynamic controls**. Helps enforce effective controls on high-risk users while others maintain productivity.
- **Automated mitigation**. Helps minimize the impact of potential data security incidents and reduce admin overhead.

Adaptive protection dynamically assigns appropriate data loss prevention, data lifecycle management, and Conditional Access policies to users based on the insider risk levels defined and analyzed by the machine learning models in Insider Risk Management. Policies become adaptive based on user context, ensuring that the most effective policy, such as blocking data sharing through data loss prevention or blocking application access through Conditional Access, is applied only to high-risk users while low-risk users maintain productivity. Data loss prevention and Conditional Access policy controls constantly adjust, so when a user's insider risk level changes, an appropriate policy dynamically applies to match the insider new risk level. In the case of data lifecycle management, Insider Risk Management detects *Elevated risk level* users and preserves their deleted data for 120 days by using an automatically created data lifecycle management retention label policy.

Important

Insider Risk Management is currently available in tenants hosted in geographical regions and countries supported by Azure service dependencies. To verify that the Insider Risk Management solution is supported for your organization, see [Azure dependency availability by country/region](/en-us/troubleshoot/azure/general/dependency-availability-by-country). Insider Risk Management is available for commercial clouds but isn't available for US Government cloud programs at this time.

Watch the following video for a summary of how Adaptive Protection can help identify and mitigate the most critical risks in your organization: 

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Insider risk levels and preventive controls

With Adaptive Protection, administrators can configure risk factors or activities for customizable insider risk levels based on your organization's needs. The insider risk levels for Adaptive Protection update continuously and automatically based on the users' risk factors and insights. When users' data security risks increase or decrease, their insider risk levels adjust accordingly. Based on the insider risk levels, data loss prevention policies and Conditional Access policies automatically apply the right level of preventative controls as configured by admins, such as *block*, *block with override*, or *warning*.

Tip

*Insider risk levels* in Adaptive Protection differ from *alert severity levels* that assign Insider Risk Management users based on activity detected in Insider Risk Management policies.

- Insider risk levels (Elevated, Moderate, or Minor), as described in this article, measure risk determined by admin-defined conditions such as the number of exfiltration activities users perform in a day or whether their activity generated a high-severity insider risk alert.
- Alert severity levels (Low, Medium, or High) assign to users based on activity detected in Insider Risk Management policies. These levels calculate based on alert risk scores assigned to all active alerts associated with the user. These levels help insider risk analysts and investigators prioritize and respond to user activity accordingly.

For data lifecycle management, the data lifecycle management policy monitors users that assign an *Elevated risk level* by Insider Risk Management Adaptive Protection. When a risky user deletes any content from SharePoint, OneDrive, or Exchange Online, the contents are automatically preserved for 120 days. Admins can contact Microsoft support to restore any preserved content.

Depending on the Insider Risk Management policy assigned in Adaptive Protection, different criteria (users, groups, indicators, thresholds, etc.) are used to determine applicable insider risk levels. Insider risk levels are based on user insights, not solely on the number of instances of specific user activities. Insights are a calculation of the aggregate number of activities and the severity level of these activities.

For example, insider risk levels for User A wouldn't be determined by User A performing a potentially risky activity more than three times. The insider risk levels for User A would be determined by an insight of the aggregate number of activities and risk scores would be assigned to the activity based on the thresholds configured in the selected policy.

### Insider risk levels

Insider risk levels in Adaptive Protection define how risky a user's activity is and can base on criteria such as how many exfiltration activities they performed or whether their activity generated a high severity insider risk alert. These insider risk levels have built-in insider risk level definitions, but you can customize these definitions as needed:

- **Elevated risk level**: This risk level includes built-in definitions for users with high severity alerts, users with at least three sequence insights that each have a high severity alert for specific risk activities, or one or more confirmed high severity alerts.
- **Moderate risk level**: This risk level includes built-in definitions for users with medium severity alerts or users with at least two data exfiltration activities with high severity scores.
- **Minor risk level**: This risk level includes built-in definitions for users with low severity alerts or users with at least one data exfiltration activity with a high severity score.

For an insider risk level to assign to a user, the number of insights and the severity assigned to the activity need to match the definition for the insider risk level. The number of activities for an insight might be a single activity or multiple activities accruing to the single insight. The number of insights evaluates for the insider risk level definition, not the number of activities contained in an insight.

For example, suppose the conditions in the Insider Risk Management policy assigned to Adaptive Protection scope for identifying downloads from SharePoint sites in your organization. If the policy detects that a user downloaded 10 files from a SharePoint site in a single day that are determined to be high severity, this counts as a single insight that consists of 10 activity events. To qualify for assigning an *Elevated risk level* to the user, two additional insights (with high severity) require for the user. The additional insights might or might not contain one or more activities.

![Screenshot of the Adaptive Protection insider risk levels settings page showing Elevated, Moderate, and Minor risk level definitions and their built-in conditions.](media/insider-risk-management-ap-risk-levels.png)

### Customizing insider risk levels

Custom insider risk levels enable you to create insider risk levels that fit your organization's needs. You can customize the criteria for the insider risk level and define conditions for when to assign the insider risk level to users.

Consider the following examples for using Adaptive Protection together with data loss prevention, data lifecycle management, and Conditional Access policies.

- **Data loss prevention policies**:
    - Allow users with the *Minor risk level* or *Medium risk level* to receive policy tips and education on best practices for handling sensitive data. With this approach, you can influence positive behavior changes over time and reduce organizational data risks.
    - Block users with the *Elevated risk level* from saving or sharing sensitive data to minimize the impact of potential data incidents.
- **Data lifecycle management policy**:
    - Preserve any SharePoint, OneDrive, or Exchange Online content deleted by a risky user for 120 days. A risky user in this case is a user that Adaptive Protection assigns the *Elevated risk level*.
- **Conditional Access policies**:
    - Require *Minor risk level* users to acknowledge Terms of Use before using an application.
    - Block *Medium risk level* users from accessing certain applications.
    - Completely block *Elevated risk level* users from using *any* applications. [Learn more about commonly applied Conditional Access policies](/en-us/entra/identity/conditional-access/overview#commonly-applied-policies)

#### Insider risk level criteria and conditions

You can customize insider risk level criteria and conditions based on the following areas:

- **Alerts generated or confirmed for a user**: Choose conditions based on the [severity level for alerts](insider-risk-management-activities#alert-status-and-severity) that the selected Insider Risk Management policy generates or confirms for a user. Conditions for alerts aren't additive. The insider risk level is assigned to a user if one of the conditions is met.
- **Specific user activity**: Choose conditions for activity to detect, its severity, and the number of daily occurrences during the past activity detection window (optional). Conditions for user activity are additive. The insider risk level is assigned to a user only if all the conditions are met.

#### Past activity detection

The **Past activity detection** setting determines how many days back Adaptive Protection examines to detect whether a user meets the conditions defined by any of the insider risk levels. The default setting is 7 days, but you can choose between 5 and 30 days of previous activity to apply insider risk level conditions. This setting only applies to insider risk levels that are based on a user's daily activity and excludes insider risk levels based on alerts.

The following example illustrates how past activity detection settings and insider risk levels interact to determine if a user's past activity is in-scope:

- **Elevated risk level** setting: User performs at least three sequences, each with a high severity risk score (67 to 100)
- **Past activity detection** setting: 3 days

| User activity | Activity in-scope for insider risk level |
| --- | --- |
| User has 1 high severity sequence each day on Day T-3, T-2, T-1 | Yes |
| User has 1 high severity sequence on Day T-4 and 2 high severity sequences on Day T-3 | No |
| User has 3 high severity sequences on Day T-3 | Yes |

#### Insider risk level timeframe

The **Insider risk level timeframe** setting determines how long an insider risk level remains assigned to a user before it's automatically reset. The default setting is 7 days, but you can choose between 5 and 30 days before resetting the insider risk level for a user.

Insider risk levels also reset for a user when:

- The associated alert for the user is dismissed.
- The associated case for the user is resolved.
- The insider risk level end date is manually expired.

Note

If a user is currently assigned an insider risk level and that user meets the criteria again for that insider risk level, the insider risk level timeframe extends for the defined number of days for the user.

#### Risk level expiration options

When you enable the automatic expiration option (enabled by default), Adaptive Protection risk levels for a user automatically expire when the associated alert for a user is dismissed or the associated case for the user is closed. If you want to keep the Adaptive Protection risk level for a user even if the alert is dismissed or the case is closed, disable the option.

## Permissions for Adaptive Protection

Important

To learn about licensing requirements for using Adaptive Protection with data loss prevention, data lifecycle management, and Conditional Access, see [Microsoft 365, Office 365, Enterprise Mobility + Security, and Windows 11 Subscriptions](https://aka.ms/M365EnterprisePlans).

Depending on how you use Insider Risk Management built-in role groups and role groups for data loss prevention or Conditional Access, you might need to update [Insider Risk Management permissions](insider-risk-management-permissions) for administrators, analysts, and investigators in your organization.

The following table describes the permissions required for specific Adaptive Protection tasks.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

| Task | Required role group |
| --- | --- |
| Configure Adaptive Protection and update settings | *Insider Risk Management* or *Insider Risk Management Admins* |
| Create and manage Conditional Access policies with the Adaptive Protection condition | One of the following: *Global administrator*, *Conditional Access Administrator*, *Security Administrator* |
| Create and manage data loss prevention policies with the Adaptive Protection condition | One of the following: *Compliance Administrator*, *Compliance Data Administrator*, *DLP Compliance Management*, *Global Administrator* |
| View details on users' or agents' assigned insider risk levels | *Insider Risk Management*, *Insider Risk Management Analysts*, or *Insider Risk Management Investigators* |

Important

The four categories of role groups correspond to the following tabs on the Adaptive Protection page: **Insider risk levels**, **Users assigned insider risk levels**, **Data Loss Prevention**, **Conditional Access**. If you're not assigned to the appropriate role group, the tab doesn't appear on the **Adaptive protection** page.

[Learn more about role groups in Microsoft Defender for Office 365 and Microsoft Purview compliance](/en-us/microsoft-365/security/office-365-security/scc-permissions)

## Configure Adaptive Protection

Depending on the needs of your organization or where you're currently configured with Insider Risk Management, data loss prevention, data lifecycle management, and Conditional Access, you have two options to get started with Adaptive Protection:

- Quick setup
- Custom setup

### Quick setup

The quick setup option is the fastest way to get started with Adaptive Protection. With this option, you don't need any preexisting Insider Risk Management, data loss prevention, data lifecycle management, or Conditional Access policies. You also don't need to preconfigure any settings or features. If your organization doesn't have a current subscription or license that supports Insider Risk Management, data loss prevention, or data lifecycle management, sign up for a [Microsoft Purview risk and compliance solutions trial](compliance-easy-trials) before starting the quick setup process. You can also [sign up for a Microsoft Entra trial for Conditional Access](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).

To get started, select **Turn on Adaptive Protection** from the Adaptive Protection cards on the Microsoft Purview portal home page or the data loss prevention Overview page. You can also start the quick setup process by going to **Insider Risk Management** &gt; **Adaptive protection** &gt; **Dashboard** &gt; **Quick setup**.

Note

If you're already a [scoped admin](purview-admin-units#permissions-for-administrative-units) for Microsoft Purview, you can't turn on quick setup.

Here's what the quick setup process configures for Adaptive Protection:

| Area | Configuration |
| --- | --- |
| A new insider risk policy | - Policy template: [Data leaks](insider-risk-management-policy-templates#data-leaks) - Policy name: Adaptive Protection policy for Insider Risk Management  - Policy scope for users and groups: All users and groups  - Priority content: None  - Triggering events: Selected exfiltration events (you can view in Insider Risk Management settings)  - Policy indicators: A subset of Office indicators (you can view in Insider Risk Management settings)  - Risk score boosters: Activity is over user's usual activity for that day |
| Adaptive protection insider risk levels | - *Elevated risk level*: Users must have at least three high severity exfiltration sequences  - *Moderate risk level*: Users must have at least two high severity activities (excluding some types of downloads)  - *Minor risk level*: Users must have at least one high severity activity (excluding some types of downloads) |
| Insider risk settings (if already configured) | - Policy indicators: Office indicators not already configured (you can view in Insider Risk Management settings) - All other settings previously configured aren't updated or changed.  - Analytics: On (thresholds for triggering events in policies are the default settings determined by [Analytics recommendations](insider-risk-management-settings-analytics)) |
| Insider risk settings (if not already configured) | - Privacy: Show anonymized versions of user names. **Note:** User names aren't anonymized in Conditional Access or data loss prevention.  - Policy timeframes: Defaults  - Policy indicators: A subset of Office indicators (you can view in Insider Risk Management settings)  - Risk score boosters: All  - Intelligent Detections: Alert Volume = Default volume  - Analytics: On  - Admin notifications: Send notification email when first alert is generated to all |
| New Conditional Access policy (created in Report-only mode so users won't be blocked) | **1-Block access for users with Insider Risk (Preview)** - Included users: All users  - Excluded guest or external users: B2bDirectConnect User; OtherExternalUser; ServiceProvider  - Cloud apps: Office 365 apps  - Insider risk levels: *Elevated* - Block access: Selected |
| New data lifecycle management policy | An organization-wide autoapply label policy that monitors users assigned the *Elevated risk level*. Any SharePoint, OneDrive, or Exchange Online content deleted by a risky user is preserved for 120 days. If you haven't already turned on Adaptive Protection, the policy is automatically created and applied when you turn on Adaptive Protection. If you have already turned on Adaptive Protection, [you need to explicitly opt in to the data lifecycle management policy](retention) that's created automatically. |
| Two new data loss prevention policies | [Adaptive Protection policy for Endpoint DLP](dlp-adaptive-protection-learn#policy-values-for-devices-dlp-policy) - *Elevated risk level* rule: Blocked  - *Moderate*/*Minor risk level* rule: Audit  - Policy starts in test mode (audit only) [Adaptive Protection policy for Teams and Exchange DLP](dlp-adaptive-protection-learn#policy-values-for-teams-and-exchange-online-dlp-policy) - *Elevated risk level* rule: Blocked  - *Moderate*/*Minor risk level* rules: Audit  - Policy starts in test mode (audit only) |

After you start the quick setup process, it can take up to 72 hours before the following items are completed:

- Analytics
- Associated Insider Risk Management, data loss prevention, data lifecycle management, and Conditional Access policies
- Adaptive Protection insider risk levels, data loss prevention, data lifecycle management, and Conditional Access actions applied to applicable user activities.

Note

Once you enable Adaptive Protection, don't disable it before the setup process completes. Disabling Adaptive Protection before the setup process completes might lead to policy errors.

Administrators receive a notification email when the quick setup process completes.

### Custom setup

The custom setup option lets you customize the Insider Risk Management policy, the insider risk levels, and the data loss prevention and Conditional Access policies configured for Adaptive Protection.

Note

For data lifecycle management, if you don't turn on Adaptive Protection, the policy isn't created and applied automatically. If you turn on Adaptive Protection for your organization, you need to [explicitly opt in to apply the data lifecycle management policy](retention).

The custom setup option also lets you configure these items before enabling the Adaptive Protection connections between Insider Risk Management and data loss prevention. In most cases, use this option if your organization already has Insider Risk Management and data loss prevention policies in place.

Complete the following steps to configure Adaptive Protection by using the custom setup.

#### Step 1: Create Insider Risk Management policy

Assign insider risk levels to users or agents when a policy assigned in Adaptive Protection either detects user or agent activity or generates alerts that match the insider risk level conditions you define in the next step. If you don't want to use an existing Insider Risk Management policy, create a new Insider Risk Management policy. Your Insider Risk Management policy for Adaptive Protection should include:

- **Users whose activity you want to detect**. This group can include all users and groups in your organization or just a subset for specific risk mitigation scenarios or testing purposes.
- **Activities you consider risky and custom thresholds that influence an activity's risk score**. Risky activities might include emailing people outside your organization or copying files to USB devices.

Select **Create insider risk policy** to start the new policy workflow. The [Data leaks](insider-risk-management-policy-templates#data-leaks) policy template is automatically selected in the workflow, but you can select any policy template.

Important

Depending on the policy template you select, you might need to configure [additional settings](insider-risk-management-configure#step-4-recommended-configure-prerequisites-for-policies) for the policy to properly detect potentially risky activities and to create applicable alerts.

#### Step 2: Configure insider risk level settings

Select the **Insider risk levels** tab. Start by selecting the Insider Risk Management policy you want to use for Adaptive Protection. This policy can be the new policy you created in Step 1 or an existing policy or policies that you already configured.

Next, accept the applicable built-in insider risk level conditions or create your own. Depending on the type of policy you select, the insider risk level conditions reflect the applicable conditions associated with indicators and activities you configure in the policy.

For example, if you choose a policy based on the [Data leaks](insider-risk-management-policy-templates#data-leaks) policy template, the built-in insider risk level condition choices apply to indicators and activities available in that policy. If you select a policy based on the [Security policy violations](insider-risk-management-policy-templates#security-policy-violations) policy template, the built-in insider risk level conditions automatically scope to indicators and activities available in that policy.

##### Customize an insider risk level for your policy

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) by using credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Adaptive protection** in the left navigation, then select **Insider risk levels**.
4. On the **Insider risk levels** page, select **Edit** for the insider risk level you want to customize (*Elevated*, *Moderate*, or *Minor*).
5. On the **Custom insider risk level** pane, select an option in the **Insider risk level based on** section:

    - **Alert generated or confirmed for a user**
    - **Specific user activity**
6. If you select the **Alert generated or confirmed for a user** option, choose the severity levels for alerts that are generated or confirmed for a user that should use this insider risk level. You can keep the *Severity for generated alerts* and the *Severity for confirmed alerts* conditions or remove one of these conditions if you only want to use one. If you need to add one of these conditions back, select **Add condition**, then select the condition. For each condition, choose the severity level that should be applied for the condition (*High*, *Medium*, or *Low*). If the **any** of the conditions are met, the insider risk level is assigned to a user.
7. If you select the **Specific user activity** option, choose the activity to detect, its severity, and number of daily occurrences during the past activity detection window. You must configure the *Activities*, *Activity severity*, and *Activity occurrences during detection window* conditions for this insider risk level.

    For the *Activities* condition, the options you can choose from automatically update for the types of activities you define with the indicators configured in the associated policy. If needed, select the **Assign this insider risk level to any user who has a future alert confirmed, even if conditions above aren't met** checkbox. If the **all** of the conditions are met, the insider risk level is assigned to a user.

    For the *Activity severity* condition, specify the severity level for the activities included in the daily activity insight. The options are *High*, *Medium*, and *Low*, and are based on risk score ranges.

    For the *Activity occurrences during detection window* condition, specify the number of times selected activities must be detected within the specified *Past activity detection* period. This number isn't related to the number of events that might occur for an activity. For example, if the policy detects that a user downloaded 20 files from SharePoint in one day, that count is one daily activity insight consisting of 20 events.
8. Select **Confirm** to apply the custom insider risk level conditions.

##### How insider risk level is assigned if a user is in scope for multiple policies

If a user is in scope for multiple policies and receives alerts of different severity levels, the user is assigned the highest severity level received. For example, consider a policy that assigns an *Elevated risk level* if users receive a high severity alert. If a user receives a low-severity alert from policy 1, a medium-severity alert from policy 2, and a high-severity alert from policy 3, the user is assigned an *Elevated risk level* - the level for the highest alert severity received.

Insider risk level conditions must be present in selected policies to be detected. For example, if you select the *Copy to USB* activity to assign a *Moderate risk level*, but the activity is selected in just one of three selected policies, then only activity from that one policy assigns a *Moderate risk level* for that activity.​

#### Step 3: Create or edit a data loss prevention policy

Next, create a new data loss prevention policy or edit an existing policy to restrict actions for users who match your insider risk level conditions in Adaptive Protection. Use the following guidelines for your data loss prevention policy configuration:

- You must include the *User's insider risk level for Adaptive Protection is* condition in your data loss prevention policy. This data loss prevention policy can include other conditions as needed.
- Although you can include other locations in the data loss prevention policy, Adaptive Protection currently supports only Exchange, Microsoft Teams, and devices.

Select **Create policy** to start the data loss prevention policy workflow and create a new data loss prevention policy. If you have an existing data loss prevention policy that you'd like to configure for Adaptive Protection, go to **Data loss prevention** &gt; **Policies** in the Microsoft Purview portal and select the data loss prevention policy you'd like to update for Adaptive Protection. For guidance on how to configure a new data loss prevention policy or update an existing data loss prevention policy for Adaptive Protection, see [Learn about Adaptive Protection in data loss prevention: Manual configuration](dlp-adaptive-protection-learn#policy-values-for-devices-dlp-policy).

Tip

We recommend testing the data loss prevention policy (with policy tips) so you can review data loss prevention alerts to verify that the policy is working as expected before enabling Adaptive Protection.

#### Step 4: Create or edit a Conditional Access policy

Next, create a new Conditional Access policy or edit an existing policy to restrict actions for users who match your insider risk level conditions in Adaptive Protection. Use the following guidelines for your Conditional Access policy configuration:

- On the Conditional Access page where you control access based on signals from conditions, set the *Insider risk* condition to *Yes*, and then select an insider risk level (*Elevated*, *Moderate*, or *Minor*). This is the insider risk level that users must have in order for the policy to be enforced.

Select **Create policy** to start the Conditional Access policy workflow and create a new Conditional Access policy. If you have an existing Conditional Access policy that you'd like to configure for Adaptive Protection, go to **Protection** &gt; **Conditional Access** in the [Microsoft Entra admin center](https://entra.microsoft.com) and select the Conditional Access policy you'd like to update for Adaptive Protection. For guidance on how to configure a new Conditional Access policy or update an existing Conditional Access policy for Adaptive Protection, see [Common Conditional Access policy: Insider risk based policy](/en-us/entra/identity/conditional-access/how-to-policy-insider-risk).

#### Step 5: Turn on Adaptive Protection

After you complete the Insider Risk Management policy, insider risk level, DLP policy, and Conditional Access policy configuration steps, you're ready to enable Adaptive Protection. When you turn on Adaptive Protection:

- The Insider Risk Management policy starts looking for user activity matching your insider risk level conditions. If detected, the insider risk levels are assigned to users.
- Users who are assigned insider risk levels appear on the **Users assigned insider risk levels** tab in Adaptive Protection.
- The data loss prevention policy applies protection actions for any user assigned to insider risk levels included in the data loss prevention policy. The data loss prevention policy is added to the **Data Loss Prevention** tab in **Adaptive protection**. You can view details about the data loss prevention policy and edit policy conditions from the dashboard.
- The data lifecycle management policy, which is automatically created, applies protection actions for any user assigned to the *Elevated risk level*. The following message appears with a green background on the **Adaptive Protection** tab to let users know that proactive data preservation is being applied: "Your organization is also being dynamically protected from users who might potentially delete critical data." The message also provides a link to the data lifecycle management setting where you can turn off the proactive data preservation feature, if desired.
- The Conditional Access policy applies protection actions for any user assigned to insider risk levels included in the Conditional Access policy. The Conditional Access policy is added to the **Conditional Access policies** tab in **Adaptive protection**. You can view details about the Conditional Access policy and edit policy conditions from the dashboard.

To enable Adaptive Protection, select the **Adaptive Protection settings** tab, and then turn **Adaptive Protection** to *On*. It might take up to 36 hours before you can expect to see Adaptive Protection insider risk levels and data loss prevention, data lifecycle management, and Conditional Access actions applied to applicable user activities.

Watch the following video on the Microsoft Mechanics channel to [see how Adaptive Protection can automatically adjust the strength of data protection based on calculated data security insider risk levels of users](https://youtu.be/9GLsxvtoLWE).

## Manage Adaptive Protection

When you enable Adaptive Protection and configure your Insider Risk Management, data loss prevention, and Conditional Access policies, you can access information about policy metrics, users currently included, and insider risk levels currently in scope.

Note

Data lifecycle management metrics don't currently appear on the dashboard. However, if proactive data preservation is turned on, you see the following message on the **Adaptive Protection** tab: "Your organization is also being dynamically protected from users who might potentially delete critical data."

### Use the Adaptive Protection dashboard

After you complete either the Quick setup or Custom setup process, the **Dashboard** tab in **Adaptive protection** displays widgets for summary information about user insider risk levels, Conditional Access policies, and data loss prevention policies.

- **Users assigned insider risk levels**: Shows the number of users for each insider risk level (*Elevated*, *Moderate*, and *Minor*).
- **Policies using insider risk levels**: Shows the status of policies (*Not started* or *Complete*), the type of policy (*Conditional Access* or *Data Loss Prevention*), and the number of configured policies for each type of policy. If a policy type isn't configured, select **Quick setup** to configure the policy.

![Screenshot of the Adaptive Protection dashboard showing widgets for users assigned insider risk levels and policies using insider risk levels.](media/insider-risk-management-ap-dashboard.png)

### View users assigned insider risk levels

The **Users assigned insider risk levels** tab shows users assigned an insider risk level in Adaptive Protection. You can review the following information for each user:

- **Users**: Lists the user name. For data loss prevention policies, if the [Show anonymized versions of usernames](insider-risk-management-settings-privacy) option is selected in Insider Risk Management settings, you see anonymized user names. For Conditional Access policies, user names aren't anonymized even if the **Show anonymized versions of usernames** setting is selected.

    Important

    To maintain referential integrity, anonymization of usernames (if turned on) isn't preserved for users from Adaptive Protection who have alerts or activity that appear outside Insider Risk Management. Actual usernames appear in related data loss prevention alerts and the activity explorer.
- **Insider risk level**: The current insider risk level assigned to the user.
- **Assigned to user**: The number of days or months that pass since assigning an insider risk level to the user.
- **Insider risk level resets**: The number of days until the insider risk level automatically resets for the user.

    To manually reset the insider risk level for a user, select the user, then select **Expire**. This user no longer has an assigned insider risk level. Existing alerts or cases for this user aren't removed. If this user is included in the selected Insider Risk Management policy, an insider risk level is assigned again if a triggering event is detected.
- **Active alerts**: The number of current Insider Risk Management alerts for the user.
- **Cases confirmed as violation**: The number of confirmed cases for the user.
- **Case**: The name of the case.

You can filter users by *Insider risk level*.

![Screenshot of the Adaptive Protection users page listing users with their assigned insider risk levels, active alerts, and risk level reset dates.](media/insider-risk-management-ap-users.png)

To view detailed insider risk and Adaptive Protection information for a specific user, select the user to open the user details pane. The details pane contains three tabs: **User profile**, **User activity**, and **Adaptive protection summary**. For information about the **User profile** and **User activity** tabs, see [View user details](insider-risk-management-users#view-user-details).

The **Adaptive protection summary** tab aggregates information in four sections:

- **Adaptive protection**: Displays information about the current *Risk level*, *Risk level assigned on*, and *Risk level reset on* for the user.
- **Data Loss Prevention policies in scope (dynamic)**: Displays all the data loss prevention policies currently in scope for the user and the start and end date for the policy. This information is based on the insider risk level for the user and data loss prevention policy configuration for insider risk levels. For example, if a user has activities that are defined as *Elevated risk level* for Insider Risk Management policies, and two data loss prevention policies are configured with the *Elevated risk level* condition, these two data loss prevention policies are displayed here for the user.
- **Conditional Access policies in scope (dynamic)**: Displays all the Conditional Access policies currently in scope for the user and the start and end date for the policy. This information is based on the insider risk level for the user and Conditional Access policy configuration for insider risk levels. For example, if a user has activities that are defined as *Elevated risk level* for Insider Risk Management policies, and a Conditional Access policy is configured with the *Elevated risk level* condition, the Conditional Access policy is displayed here for the user.
- **Insider risk policy for Adaptive protection**: Displays any Insider Risk Management policy where the user is currently in-scope.

![Screenshot of the Adaptive Protection user details pane showing the user's current insider risk level, in-scope DLP and Conditional Access policies, and risk level reset date.](media/insider-risk-management-ap-user-details.png)

### Manage Conditional Access policies for Adaptive Protection

The **Conditional Access policies** page shows all Conditional Access policies that use the **Insider risk** condition. You can review the following information for each policy:

- **Policy name**: The name of the Conditional Access policy.
- **Policy state**: The current state of the policy. Values are *Active* or *Inactive*.
- **Insider risk levels**: The insider risk levels included in the Conditional Access policy by using the **Insider Risk** condition. The options are *Elevated*, *Moderate*, or *Minor*.
- **Policy status**: The current status of the Conditional Access policy. The options are *On* or *Test with notifications*.
- **Created on**: The date you created the Conditional Access policy.
- **Last modified**: The date you last edited the Conditional policy.

![Screenshot of the Adaptive Protection Conditional Access policies page showing policies linked to insider risk levels, their state, and status.](media/insider-risk-management-ap-ca-policies.png)

### Manage Data Loss Prevention policies for Adaptive Protection

The **Data Loss Prevention policies** page shows all data loss prevention policies that use the **User's insider risk level for Adaptive Protection is** condition. You can review the following information for each policy:

- **Policy name**: The name of the data loss prevention policy.
- **Policy state**: The current state of the policy. Values are *Active* or *Inactive*.
- **Policy location**: The [DLP policy locations](dlp-policy-reference#locations) included in the data loss prevention policy. Currently, Adaptive Protection supports Exchange, Teams, and Devices.
- **Insider risk levels**: The insider risk levels included in the data loss prevention policy by using the **Insider risk level for Adaptive Protection is** condition. The options are *Elevated*, *Moderate*, or *Minor*.
- **Policy status**: The current status of the data loss prevention policy. The options are *On* or *Test with notifications*.
- **Created**: The date you created the data loss prevention policy.
- **Last modified**: The date you last edited the data loss prevention policy.

![Screenshot of the Adaptive Protection Data Loss Prevention policies page showing policies associated with insider risk level conditions, their state, and status.](media/insider-risk-management-ap-dlp-policies.png)

### Tune your insider risk level settings

After reviewing users with insider risk levels, you might find too many or too few users assigned an insider risk level. Use these two methods to tune your policy configurations and adjust the number of users assigned insider risk levels:

- Modify insider risk level settings. Adjust your thresholds to assign an insider risk level to a user:
    - Increase or decrease the severity of the activity required to assign an insider risk level. For example, reduce the activity or alert severity if you're seeing too few users with insider risk levels.
    - If the insider risk level is based on a specific user activity, increase or decrease the activity occurrences during the detection window. For example, reduce the activity occurrences if you're seeing too few users with insider risk levels.
    - Change what the insider risk level is based on. For example, assign an insider risk level only if the alert is confirmed to decrease the number of users if you're seeing too many users with insider risk levels.
- [Modify policy thresholds](insider-risk-management-settings-policy-indicators#indicator-level-settings). Since policy detections assign insider risk levels, modify your policy to change the requirements to assign an insider risk level. Modify a policy by increasing or decreasing the policy thresholds that lead to high, medium, or low severity activities and alerts.

## Disable Adaptive Protection

In certain scenarios, you might need to temporarily disable Adaptive Protection. To disable Adaptive Protection, select the **Adaptive Protection settings** tab and turn **Adaptive Protection***Off*.

If you turn off Adaptive Protection after it's been on and active, the system stops assigning insider risk levels to users and stops sharing them with data loss prevention, data lifecycle management, and Conditional Access. All existing insider risk levels for users are reset. After turning off Adaptive Protection, it might take up to six hours to stop assigning insider risk levels to user activity and reset them all. The Insider Risk Management, data loss prevention, data lifecycle management, and Conditional Access policies aren't automatically deleted.

![Screenshot of the Adaptive Protection settings page with the toggle to enable or disable Adaptive Protection.](media/insider-risk-management-ap-enable.png)

Note

You can opt out of data lifecycle management protection without disabling Insider Risk Management Adaptive Protection by turning off the **Adaptive protection in Data Lifecycle Management** setting in data lifecycle management. If you turn off this setting, the data lifecycle management policy is deleted. The setting isn't enabled again unless you turn it back on. [Learn more about the **Adaptive protection in Data Lifecycle Management** setting](retention#dynamically-mitigate-the-risk-of-accidental-or-malicious-deletes)