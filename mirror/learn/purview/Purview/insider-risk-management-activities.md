---
layout: Conceptual
title: Investigate Microsoft Purview Insider Risk Management activities | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-activities
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to investigate and triage Insider Risk Management alerts in Microsoft Purview. Review risk factors, explore activities, and create cases.
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: how-to
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-08-27T00:00:00.0000000Z
audience: itpro
ms.collection:
- purview-compliance
ms.custom: msecd-doc-authoring-1024, admindeeplinkCOMPLIANCE, sfi-image-nochange
ai-usage: ai-assisted
locale: en-us
document_id: dadd3508-a993-e99a-0a41-0d2c669d3f4b
document_version_independent_id: dadd3508-a993-e99a-0a41-0d2c669d3f4b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-activities.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-activities
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-activities.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 58b5d91f-4ed7-0714-5e55-6a33a8dfed73
---

# Investigate Microsoft Purview Insider Risk Management activities | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

To minimize insider risks in your organization, investigate potentially risky user activities. These risks might be activities that generate alerts from Insider Risk Management policies. They can also be risks from compliance-related activities that the policies detect but don't immediately create Insider Risk Management alerts for users.

![Diagram that shows how Insider Risk Management alerts are generated.](media/insider-risk-management-alert-generation-chart.png)

You can investigate these types of activities by using [User activity reports](insider-risk-management-reports) or with the **Triage Agent in Insider Risk Management** and **Standard alert** dashboards.

## Triaging alerts

Investigate and act on alerts in Insider Risk Management by following these steps:

1. **Review the dashboards for alerts**. On the Standard dashboard, [filter alerts](insider-risk-management-activities#filter-alerts-save-a-view-of-a-filter-set-customize-columns-or-search-for-alerts) by alert *Status* to locate *Needs review* alerts. You can also use spotlighted alerts on the dashboard to quickly see prioritized alerts. On the Alert Triage Agent dashboard, select the **Needs attention** filter to view alerts with the highest prioritization.
2. **Start with the alerts with the highest severity**. [Filter alerts](insider-risk-management-activities#filter-alerts-save-a-view-of-a-filter-set-customize-columns-or-search-for-alerts) by alert *Severity* if needed to help locate these types of alerts.
3. **Select an alert to discover more information and to review the alert details**. Review details and connections associated with the alert:

    1. View the agent summary tab to review intelligently distilled user activity and risk pattern narratives.
    2. Use the [Activity explorer tab](insider-risk-management-activities#activity-explorer-tab) to review a timeline of the associated potentially risky behavior, and to identify all risk activities for the alert.
    3. Use the [Data risk graph](insider-risk-management-data-risk-graph) to review connections and details about users and files for the alert.

    Tip

    If **Content preview (preview)** is available for the content within the alert, you can review relevant files from SharePoint, Exchange, and OneDrive for Business in Activity explorer to identify false positives, confirm that sensitive data is present, and quickly decide whether the alert warrants escalation.
4. **Act on the alert**. You can either confirm and [create a case for an alert](insider-risk-management-activities#create-a-case-for-an-alert) or dismiss and resolve the alert.

You can triage alerts by going to the **Alert details** page for an alert in either dashboard. On the **Alert details** page, you can review information about the alert. You can confirm the alert and create a new case, confirm the alert and add to an existing case, or dismiss the alert.

The **Alert details** page also includes the current status for the alert and the alert risk severity level, listed as *High*, *Medium*, or *Low*. The severity level might increase or decrease over time if you don't triage the alert. For false positives, you can select multiple alerts and dismiss them in bulk by selecting **Dismiss alerts**.

## Use Copilot to summarize an alert

Select **Summarize with Copilot** or the Copilot icon to quickly summarize an alert and prioritize the alerts that need further investigation. You can summarize selected alerts without opening the alert or after viewing the details of the alert. When you summarize an alert with Microsoft Copilot in Microsoft Purview, a **Copilot** pane appears on the right side of the screen with an alert summary.

The alert summary includes all the essential details about the alert, such as the policy that triggered the alert, the activity that generated the alert, the triggering event, the user involved, their last working date (if applicable), any key user attributes, and the user's top risk factors. Copilot in Microsoft Purview consolidates information about the user from all their alerts and in-scope policies and emphasizes the user's top risk factors.

Suggested prompts automatically show to help further refine your summary and provide additional insights to the activities associated with the alert. Choose from the following suggested prompts:

- *List all the data exfiltration activities involving this user*.
- *List all the sequential activities involving this user*.
- *Did the user engage in any unusual behavior?*
- *Show key actions performed by the user in the last 10 days*.
- *Summarize user's last 30 days of activity*.

Tip

You can also use the [standalone version of Microsoft Security Copilot to investigate Insider Risk Management, Microsoft Purview Data Loss Prevention (DLP), and Microsoft Defender XDR alerts](copilot-in-purview-promptbooks).

## Alerts (preview)

The new unified alert experience combines the Triage Agent and classic alert dashboards into a single alerts list page. This unified view lets you manage both classic and agent-triaged alerts from one location, making it easier to investigate and act on alerts without toggling between dashboards.

The unified alert experience includes the following capabilities:

- **Preview agent summaries, alert, and user details directly on the alerts list page** without opening the full alert details.
- **Filter by all classic and agent attributes on one page**, including a filter for agent-triaged alerts that need attention.
- **Manage the Triage Agent directly from the alerts list page**, including viewing agent categorization details.
- **New Agent Categorization column** added to the alerts list to quickly identify how the agent has categorized each alert.

Important

The following changes apply to the unified alert experience:

- Alert **Spotlight** is no longer available in the unified experience. To prioritize agent-triaged alerts, use the **Needs Attention** filter instead.
- The ability to toggle between the Triage Agent and classic alert dashboards is no longer available. Both alert types appear in a single unified view.
- The classic and new alert experiences will both be available for at least 60 days. After August 31, only the unified experience will be supported.

To access the unified alert experience, select the **Alerts (preview)** tab in the left navigation of the Insider Risk Management solution.

### System-generated notes for alerts (preview)

In the unified alert experience, system-generated notes are automatically added to alerts when there's a change in alert status, a change in the assigned user, or closure of an alert. These notes appear in the **Notes** tab within the alert details panel, helping analysts and investigators stay up to date with all activity on an alert without needing to manually track changes. Some system-generated notes might not appear for activity prior to July 1. For information about system-generated notes for cases, see [Case notes](insider-risk-management-cases#manage-case-notes).

### Alert notes (preview)

Analysts and investigators can add and view notes directly on alerts within the Purview portal.

Important

- You can add up to 50 manual notes per alert or case (not including system-generated notes).
- Notes can't be edited or deleted at this time.
- There's no sync between alert notes in Insider Risk Management and Microsoft Defender.

### User profile details (preview)

In the unified alert experience, you can view expanded user profile details directly from an alert. The expanded user profile aggregates all Insider Risk Management user signals into a unified view, making it easier to understand complete user risk at a glance.

To access expanded user profile details:

1. Select **Alerts (preview)** in the left navigation.
2. Select an alert.
3. Scroll down to **User details**.
4. Select **View user details**.

The expanded user profile includes the following additional signals from the user's Microsoft Entra profile:

- **Office location**
- **Employee type**
- **Department**
- **Last working date**
- **Entra account deletion date**

The profile also aggregates the following Insider Risk Management signals:

- **Past alert and case history**
- **Priority user group status**
- **Policy inclusion**
- **HR Connector last working date**

Note

When pseudo-anonymization is enabled, the expanded user profile details aren't visible.

For more information about user profile details, see [View user details](insider-risk-management-users#view-user-details).

## Use Spotlight to prioritize alerts (preview)

Note

Alert Spotlight will be removed in the unified alert experience (preview) on August 31, 2026. To prioritize alerts in the new experience, use the **Needs Attention** filter for agent-triaged alerts instead.

The alert **Spotlight** on the **Alerts** dashboard helps you prioritize alerts to triage. Every generated alert has a risk score, a list of activities performed, tags, and triggers. Alert spotlighting uses this information to determine if an alert is spotlighted.

An alert is automatically spotlighted if it has a risk score of 85 or higher and if at least three of the following conditions are met:

- One insight from the following table matches the highest insight of the alert.
- The alert contains priority content or the user is detected as a [potential high impact user](insider-risk-management-settings-policy-indicators#risk-score-boosters).
- The user is [manually brought into scope](insider-risk-management-policies#immediately-start-scoring-user-activity).
- Alert activity contains two or more high-confidence insights from the following table.

| Category | Indicator (high confidence insights) |
| --- | --- |
| [Device indicator](insider-risk-management-settings-policy-indicators#device-indicators) | - Creating or transferring files to a network share  - Creating or copying files to USB  - Using a browser to upload files to the web |
| [Office indicator](insider-risk-management-settings-policy-indicators#office-indicators) | - Sharing SharePoint files with people outside the organization  - Sharing SharePoint folders with people outside the organization  - Sharing file links with people outside organization in a Teams chat |
| [Policy](insider-risk-management-settings-policy-indicators#configure-policy-indicators-in-insider-risk-management) | - Content to prioritize  - Start scoring activity for users |
| [Risk score booster](insider-risk-management-settings-policy-indicators#risk-score-boosters) | - User is detected as a potential high impact user |
| [Sequence detection](insider-risk-management-policies#sequence-detection) | - Download from Microsoft 365 location then exfiltrate  - Download from Microsoft 365 location, exfiltrate, then delete  - Download from Microsoft 365 location, obfuscate, then exfiltrate |

## Triage Agent in Insider Risk Management dashboard

When you enable the [Triage Agent in Insider Risk Management](copilot-in-purview-triage-irm-agent-get-started) in your organization, the agent reviews alerts and displays them on the Triage Agent dashboard. This dashboard automatically includes prioritized alerts and filters to help Insider Risk Management analysts quickly investigate and resolve issues.

You can customize the dashboard columns and filter alerts triaged by the agent by priority, date, alert status, or alert scope. To view the Triage Agent dashboard, select **Triage Agent** at the top of the dashboard page.

Select an alert to display the Agent summary and overview details for the alert. Select **View details** to view details for the alert and for access to the details sections like the risk factors, risk pattern narratives (preview), the Activity explorer, and more.

If you disagree with the **Agent categorization**, select **Is this incorrect?** (preview) to provide feedback on why the categorization is incorrect.

Important

The file risk section of the Triage Agent is deprecated.

For an overview of how alerts provide details, context, and related content for risky activity and how to make your investigation process more effective, see the [Insider Risk Management Alerts Triage Experience video](https://www.youtube.com/watch?v=KgmpxBLJLPI).

### Understand the Agent summary tab

The **Agent summary** section in the **Alert details** page is only available when selecting an alert from the [Triage Agent in Insider Risk Management](copilot-in-purview-triage-irm-agent-get-started) dashboard. Agent summary information includes details on the categorization for the alert and details about the associated risks used in the triage process. This view provides you with the following information:

- **Agent categorization**: Alerts are categorized as **Needs attention** or **Less urgent**.
- **User info**: Provides the **Alert history**, **Title**, **Organization** and **Last working date** for the user. Select the tile to view additional details (preview).
- **Risk patterns**: Provides a narrative summary of each risk associated with the alert (preview).

Select the narrative summary (preview) for each listed risk to review the following details:

- **Summary**: Each risk pattern includes a narrative summary detailing the risky activity, the sensitive data involved, and the affected files.
- **Actors**: The device involved in the alert and the client IP address, if available.
- **Timeframe**: Provides the start and end dates and times in UTC.
- **Sensitive data involved**: Lists the sensitive information types, classifiers, and file sensitivity labels involved in the alert.
- **Activity names**: The types of actions taken by the user.
- **Activity details**: Explains key aspects of the observed activity, such as the scope of events, sensitive data and files involved, and other contextual signals that contribute to the risk assessment.

Select **Filter activity** for a filtered view of the relevant information in the Activity explorer that contributed to the selected narrative.

Note

The Triage Agent does the following:

- Performs an in-depth analysis of the most recent 30,000 activity events associated with the user referenced in the alert.
- Evaluates all recorded user activities to assess risk, rather than limiting the analysis to only the activities defined in the policy that triggered the alert.
- Relies on underlying activity log details to determine risk, and when specific information isn't available, it clearly indicates this by marking the detail as "Not found by agent".

## Standard alert dashboard

Insider Risk Management policies automatically generate alerts based on risk indicators you define, and display them on the Standard alert dashboard. These alerts give compliance analysts and investigators an all-up view of the current risk status and allow your organization to triage and take actions for discovered potential risks. By default, policies generate a certain number of low, medium, and high severity alerts, but you can [increase or decrease the alert volume](insider-risk-management-settings-intelligent-detections#configure-alert-volume-levels) to suit your needs. Additionally, you can configure the [alert threshold for policy indicators](insider-risk-management-settings-policy-indicators#indicator-level-settings) when creating a new policy with the policy creation tool. To view the Standard dashboard, select **Standard** at the top of the dashboard page.

Note

For any generated alerts, Insider Risk Management generates a single aggregated alert per user. The system adds any new insights for that user to the same alert.

Important

If you [scope your policies by one or more administrative units](purview-admin-units), you can only see alerts for the users you're scoped for. For example, if an administrative scope applies to just users in Germany, you can only see alerts for users in Germany. Unrestricted administrators can see all alerts for all users in the organization.

Restricted administrators can't access alerts for the users assigned to them through security groups or distribution groups added in administrative units. Such user alerts are visible only to unrestricted administrators. Microsoft recommends adding users directly to administrative units to ensure their alerts are also visible to restricted administrators with administrative units assigned.

### Filter alerts, save a view of a filter set, customize columns, or search for alerts

Depending on the number and type of active Insider Risk Management policies in your organization, reviewing a large queue of alerts can be challenging. To help you keep track of alerts, you can:

- Filter alerts by various attributes.
- Save a view of a filter set to reuse later.
- Display or hide columns.
- Search for an alert.
- View alert reports.

#### Filter alerts

To narrow the alerts shown on the dashboard, follow these steps:

1. Select **Add filter**.
2. Select one or more of the following attributes:

    | Attribute | Description |
    | --- | --- |
    | **Activity that generated the alert** | Displays the top potentially risky activity and policy match during the activity evaluation period that leads to the alert. This value can update over time. |
    | **Alert dismissal reason** | The reason for dismissing the alert. |
    | **Assigned to** | The admin that the alert is assigned to for triaging (if assigned). |
    | **Policy** | The name of the policy. |
    | **Risk factors** | The risk factors that help determine how risky a user's activity might be. The possible values are *Cumulative exfiltration activities*, *Activities include priority content*, *Sequence activities*, *Activities include unallowed domains*, *Member of a priority user group*, and *Potential high impact user*. |
    | **Severity** | The user's risk severity level. The options are *High*, *Medium*, and *Low*. |
    | **Status** | Status of the alert. The options are *Confirmed*, *Dismissed*, *Needs review*, and *Resolved*. |
    | **Time detected (UTC)** | The start and end dates for when the alert was created. The filter searches for alerts between UTC 00:00 on the start date and UTC 00:00 on the end date. |
    | **Triggering event** | The event that brought the user into scope of the policy. The triggering event can change over time. |

    The attributes that you select are added to the filter bar.
3. Select an attribute in the filter bar, and then select a value to filter by. For example, select the **Time detected (UTC)** attribute, enter or select the dates in the **Start date** and **End date** fields, and then select **Apply**.

    Tip

    To start over at any point, select **Reset all** on the filter bar.

#### Save a view of a filter set to reuse later

To save the current filter set for later reuse, follow these steps:

1. After applying the filters as described in the preceding procedure, select **Save**, enter a name for the filter set, and then select **Save**.

    The filter set is added as a card. It includes a number that shows the count of alerts that meet the criteria in the filter set.

    Note

    You can save up to five filter sets. To delete a filter set, select the ellipsis (three dots) in the upper-right corner of the card, and then select **Delete**.
2. To reapply a saved filter set, select the card for the filter set.

#### Display or hide columns

To customize which columns appear in the alerts view, follow these steps:

1. On the right side of the page, select **Customize columns**.
2. Select or clear the checkboxes for the columns you want to display or hide.

The column settings are saved across sessions and across browsers.

### Search for alerts

Use the **Search** control to search for a user principal name (UPN), an assigned admin name, or an Alert ID.

### View alert reports

Go to **Insider Risk Management** &gt; **Reports** &gt; **Alerts** to view [Insider Risk Management alert reports](insider-risk-management-reports) for generated alerts, alerts by region, alerts by triggering event, and more.

### Header/summary section of the Alert details page

The **Header/summary** section in the **Alert details** page is only available when selecting an alert from the Standard dashboard. It contains general information about the user and alert. Use this information for context while reviewing detailed information about the detected risk management activity included in the alert for the user:

- **Activity that generated this alert**: Displays the top potentially risky activity and policy match during the activity evaluation period that led to the alert being generated.
- **Triggering event**: Displays the most recent triggering event that prompted the policy to start assigning risk scores to the user's activity. If you configure [integration with Communication Compliance](communication-compliance-policies#integrate-communication-compliance-with-microsoft-purview-insider-risk-management) for *Data leaks by risky users* or *Security policy violations by risky users* policies, the triggering event for these alerts is scoped to Communication Compliance activity.
- **User details**: Displays general information about the user assigned to the alert. If anonymization is enabled, the username, email address, alias, and organization fields are anonymized.
- **User alert history**: Displays a list of alerts for the user for the last 30 days. Includes a link to view the complete alert history for the user.

Note

When a user is detected as a potential high impact user, this information is highlighted in the alert header in the **User details** page. The user details also include a summary with the reasons the user is detected as such. To learn more about setting policy indicators for potential high impact users, see [Insider Risk Management settings](insider-risk-management-settings-policy-indicators).

Alerts generated from policies scoped to only activities that include [priority content](insider-risk-management-policies#prioritize-content-in-policies) include the *Only activity with priority content was scored for this alert* notification in the **Header/summary** section.

Tip

To get a quick overview of an alert, select **Summarize** on the alert details page. When you select **Summarize**, a **Copilot** pane appears on the right side of the page with an alert summary. The alert summary includes all the essential details about the alert, such as the policy that was triggered, the activity that generated the alert, the triggering event, the user involved, their last working date (if applicable), any key user attributes, and the user's top risk factors. Copilot in Microsoft Purview consolidates information about the user from all their alerts and in-scope policies and emphasizes the user's top risk factors. You can also summarize the alert from the Alerts queue without having to open the alert by using **Copilot**. Or use the [standalone version of Microsoft Security Copilot to investigate Insider Risk Management, Microsoft Purview Data Loss Prevention (DLP), and Microsoft Defender XDR alerts](copilot-in-purview-promptbooks).

### All risk factors tab

You can access this tab in **Alert details** for alerts in both dashboard views. It opens the summary of risk factors for the user's alert activity. Risk factors help you determine how risky the user's risk management activity is during your review. The risk factors include summaries for:

- **Cumulative exfiltration activities**: Events associated with cumulative exfiltration activities.
- **Health record access**: Potentially risky activities for events associated with accessing health records.
- **Priority content**: Potentially risky activities associated with priority content.
- **Risky browser usage**: Potentially risky activities for events associated with browsing to potentially inappropriate websites.
- **Sequences of activities**: Detected potentially risky activities associated with risk sequences.
- **Top exfiltration activities**: Exfiltration activities with the highest number of events for the alert.
- **Unallowed domains**: Potentially risky activities for events associated with unallowed domains.
- **Unusual activity for this user**: Specific activities for the user that are considered potentially risky, as they're unusual and a departure from their typical activities.

With these filters, you see only alerts with these risk factors, but the activity that generated an alert might not fall into any of these categories. For example, an alert containing sequence activities might be generated simply because the user copied a file to a USB device.

#### Content detected

The **Content detected** section on the **All risk factors** tab includes content associated with the risk activities for the alert and summarizes activity events by key areas. When you select an activity link, you open the Activity explorer and see more details about the activity.

### Activity explorer tab

Note

Users can access Activity explorer in the alert management area when their organization enables the feature and after the users trigger events.

The **Activity explorer** tab is available for alerts in both dashboard views. It provides risk investigators and analysts with a comprehensive analytics tool that provides detailed information about alerts. With the Activity explorer, reviewers can quickly review a timeline of detected potentially risky activity and identify and filter all risk activities associated with alerts.

#### Content preview (preview)

For supported activities, investigators can preview related content directly within Activity explorer to quickly validate risk without creating a case. Content preview (preview) enables early triage by helping investigators determine whether an activity contains sensitive data, represents a false positive, or requires escalation to a full investigation. Content preview is supported for activities that involve accessing or transmitting content.

##### Supported Content preview (preview) activities

Content preview is supported for activities that involve accessing or transmitting content, including:

- **SharePoint**: File accessed, file download, full file sync download
- **Exchange**: Email sent (hygiene events), Data loss prevention rule matches
- **OneDrive for Business**: File accessed, file download, full file sync download

##### Limitations of Content preview (preview)

Content preview isn't supported for activities that represent state changes, permission changes, deletions, or signal-only events. Examples include:

- File or folder deletion and recycle bin events
- Endpoint activities (such as file deletion, copying, printing, or USB transfers)
- Browser or removable media events
- Metadata-only events (user or group changes, Power BI export or deletion events)
- Files that have been renamed

#### Use the Activity explorer

When reviewing activities in the Activity explorer, investigators and analysts can select a specific activity and open the activity details pane. The pane displays detailed information about the activity that investigators and analysts can use during the alert triage process. Detailed information might provide context for the alert and assist with identifying the full scope of the risk activity that triggered the alert.

When selecting an activity's events from the activity timeline, the number of activities displayed in the explorer might not match the number of activity events listed in the timeline. Examples of why this difference might occur include:

- **Cumulative exfiltration detection**: Cumulative exfiltration detection analyzes event logs but applies a model that includes deduplicating similar activities to compute cumulative exfiltration risk. Additionally, you might see a difference in the number of potentially risky activities displayed in the Activity explorer if you make changes to your existing policy or settings. For example, if you modify allowed/unallowed domains or add new file type exclusions after a policy is created and potentially risky activity matches occur, the cumulative exfiltration detection activities differ from the results before the policy or settings changes. Cumulative exfiltration detection activity totals are based on the policy and settings configuration at the time of computation and don't include activities prior to the policy and settings changes.
- **Emails to external recipients**: Potentially risky activity for emails sent to external recipients is assigned a risk score based on the number of emails sent, which might not match the activity event logs.

![Screenshot of the Insider Risk Management Activity explorer details pane.](media/insider-risk-activity-explorer-details.png)

##### Sequences that contain events excluded from risk scoring

A [sequence detection](insider-risk-management-policies#sequence-detection) might contain one or more events that are excluded from risk scoring based on your settings configuration. For example, your organization might use the [**Global exclusions** setting](insider-risk-management-settings-global-exclusions) to exclude .png files from risk scoring since .png files aren't normally risky. But a .png file could be used to obfuscate a malicious activity. For this reason, if an event that's excluded from risk scoring is part of a sequence due to an obfuscation activity, the event is included in the sequence since it might be interesting in the context of the sequence.

The Activity explorer displays the following information for excluded events in sequences:

- If a sequence contains a step where *all* events are excluded, the insight includes just the activity name and date. Select the **View the excluded events** link to filter for the excluded events in the Activity explorer. The User activity scatter plot icon has a risk score of 0 if all events are excluded.
- If a sequence has an insight where *some* events are excluded, the event information for the nonexcluded events is displayed, but the event count doesn't include the excluded events. Select the **View the excluded events** link to filter for the excluded events in the Activity explorer.
- If you select a *sequence link* for an insight, you can drill down into the sequence of events in the activity details pane, including any events that were excluded from scoring. An event excluded from scoring is marked as **Excluded**.

#### Filter alerts in the Activity explorer

To filter alerts in the Activity explorer for column information, select **Filters**. You can filter alerts by one or more attributes listed in the details pane for the alert. Activity explorer also supports customizable columns to help investigators and analysts focus the dashboard on the information most important to them.

Use the *Activity scope*, *Risk factor*, and *Review status* filters to display and sort activities and insights for the following areas.

- **Activity scope**: Filters all scored activities for the user.

    - All scored activity for this user
    - Only scored activity in this alert
- **Risk factor**: Filters for risk factor activity applicable for all policies assigning risk scores. This filter includes all activity for all policies for included users.

    - Unusual activity
    - Includes events with priority content
    - Includes events with unallowed domain
    - Sequence activities
    - Cumulative exfiltration activities
    - Health record access activities
    - Risky browser usage
- **Review status**: Filters activity review status.

    - All
    - Not yet reviewed (filters out any activity that was part of a dismissed or resolved alert)

![Screenshot of the Insider Risk Management Activity explorer overview.](media/insider-risk-activity-explorer.png)

### Review the User activity tab

Both dashboard views provide the **User activity** tab for alerts. It's one of the most powerful tools for internal risk analysis and investigation for alerts and cases in the Insider Risk Management solution. You can quickly review all activities for a user, including a historical timeline of all alerts, alert details, the current risk score for the user, and the sequence of risk events.

![Screenshot of the Insider Risk Management User activity tab showing the risk activity timeline.](media/insider-risk-user-activities.png)

1. **Case actions**: The case action toolbar provides options for resolving the case. When viewing a case, you can resolve the case, send an email notice to the user, or escalate the case for a data or user investigation.
2. **Risk activity chronology**: The full chronology of all risk alerts associated with the case, including all the details available in the corresponding alert bubble.
3. **Filters and sorting (preview)**:

    - **Risk category**: Filter activities by the following risk categories: *Activities with risk scores &gt; 15 (unless in a sequence)* and *Sequence activities*.
    - **Activity Type**: Filter activities by the following types: *Access*, *Deletion*, *Collection*, *Exfiltration*, *Infiltration*, *Obfuscation*, *Security*, *Custom Indicator*, *Defense Evasion*, *Privilege Escalation*, *Communication Risk*, *User Compromise Risk*, and *AI Usage*.
    - **Sort by**: List the timeline of potentially risky activities by *Date occurred* or *Risk score*.
4. **Time filters**: By default, the User activity chart displays the last three months of potentially risky activities. You can easily filter the chart view by selecting the *6 Months*, *3 Months*, or *1 Month* tabs on the bubble chart.
5. **Risk sequence**: The chronological order of potentially risky activities is an important aspect of risk investigation. Identifying these related activities is an important part of evaluating overall risk for your organization. Alert activities that are related are displayed with connecting lines to highlight that these activities are associated with a larger risk area. An icon positioned over the sequence activities identifies sequences in this view relative to the risk score for the sequence. Hover over the icon to see the date and time of the risky activity associated with this sequence. This view of activities can help investigators 'connect the dots' for risk activities that could have been viewed as isolated or one-off events. Select the icon or any bubble in the sequence to display details for all the associated risk activities. Details include:

    - **Name** of the sequence.
    - **Date** or **Date range** of the sequence.
    - **Risk score** for the sequence. This score is the numerical score for the sequence of the combined alert risk severity levels for each related activity in the sequence.
    - **Number of events associated with each alert in the sequence**. Links to each file or email associated with each potentially risky activity are also available.
    - **Show activities in sequence**. Displays the sequence as a highlight line on the bubble chart and expands the alert details to display all related alerts in the sequence.
6. **Risk alert activity and details**: The User activity chart visually displays potentially risky activities as colored bubbles. The chart creates bubbles for different categories of risk. Select a bubble to display the details for each potentially risky activity. Details include:

    - **Date** of the risk activity.
    - The **risk activity category**. For example, *Email(s) with attachments sent outside the organization* or *File(s) downloaded from SharePoint Online*.
    - **Risk score** for the alert. This score is the numerical score for the alert risk severity level.
    - Number of events associated with the alert. Links to each file or email associated with the risk activity are also available.
7. **Cumulative exfiltration activities**: Select to view a visual chart of how activity is building over time for the user.
8. **Risk activity legend**: Across the bottom of the user activity chart, a color-coded legend helps you quickly determine risk category for each alert.

### Use the Data risk graph tab

Important

**Data risk graph is being deprecated.** The data risk graph in Microsoft Purview Insider Risk Management will be retired on **November 24, 2026**. After that date, the data risk graph experience will no longer be available.

You can't use this feature with the [anonymized usernames privacy setting](insider-risk-management-settings-privacy) enabled.

Both dashboard views provide access to the **Data risk graph** tab for alerts. By integrating with [Microsoft Sentinel](purview-sentinel), the data risk graph helps you view connections between impacted assets, users, and their activities in an interactive graph experience.

For more information about data risk graphs, see [Data risk graph in Insider Risk Management](insider-risk-management-data-risk-graph).

### Save a view of a filter to reuse later

If you create a filter and customize columns for the filter, you can save a view of your changes so that you or others can quickly filter for the same changes again later. When you save a view, you save both the filters and columns. When you load the view, it loads both saved filters and columns.

1. Create a filter and customize columns. 
    Tip

    To start over at any point, select **Reset**. To change columns that you customized, select **Reset columns**.
2. When you have the filter the way you want it, select **Save this view**, enter a name for the view, and then select **Save**. 
    Note

    The maximum length for a view name is 40 characters and you can't use any special characters.
3. To reuse the view of the filter later, select **Views**, and then select the view you want to open from the **Recommended views** tab (shows the most-used views) or the **Custom views** tab (displays the most frequently used filters).

When you select a view this way, it resets all the existing filters and replaces them with the view that you selected.

### Alert status and severity

Note

Insider Risk Management throttles trigger processing to help protect and optimize your risk investigation and review experience. This throttling guards against issues that might result in an overload of policy alerts, such as misconfigured data connectors or data loss prevention policies. Insider Risk Management doesn't process signals received beyond the throttling limits. [Learn more about limits in Insider Risk Management](insider-risk-management-limits).

You can triage alerts into one of the following statuses:

- **Confirmed**: An alert you confirm and assign to a new or existing case.
- **Dismissed**: An alert you dismiss as benign in the triage process. You can provide a reason for the alert dismissal and include notes that are available in the user's alert history to provide additional context for future reference or for other reviewers. Reasons could range from expected activities, nonimpactful events, simply reducing the number of alert activities for the user, or a reason related to the alert notes. Reason classification choices include *Activity is expected for this user*, *Activity is impactful enough for me to investigate further*, and *Alerts for this user contain too much activity*.
- **Needs review**: A new alert where triage actions haven't yet been taken.
- **Resolved**: An alert that's part of a closed and resolved case.

The system automatically calculates alert risk scores from several risk activity indicators. These indicators include the type of risk activity, the number and frequency of the activity occurrence, the history of users' risk activity, and the addition of activity risks that might boost the seriousness of the potentially risky activity. The alert risk score drives the programmatic assignment of a risk severity level for each alert and can't be customized. If you don't triage alerts and risk activities continue to accrue to the alert, the risk severity level can increase. Risk analysts and investigators can use alert risk severity to help triage alerts in accordance with your organization's risk policies and standards.

Alert risk severity levels are:

- **High severity**: The potentially risky activities and indicators for the alert pose significant risk. The associated risk activities are serious, repetitive, and correlate strongly to other significant risk factors.
- **Medium severity**: The potentially risky activities and indicators for the alert pose a moderate risk. The associated risk activities are moderate, frequent, and have some correlation to other risk factors.
- **Low severity**: The potentially risky activities and indicators for the alert pose a minor risk. The associated risk activities are minor, more infrequent, and don't correlate to other significant risk factors.

### Dismiss multiple alerts (preview)

To save triage time, analysts and investigators can dismiss multiple alerts at once. With the **Dismiss alerts** command bar option, you can select one or more alerts with a *Needs review* status on the dashboard and quickly dismiss these alerts as benign. You can select up to 400 alerts to dismiss at one time.

#### Dismiss an insider risk alert

To dismiss alerts, you must be a member of the *Insider Risk Management*, *Insider Risk Management Analysts*, or *Insider Risk Management Investigators* role group.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Alerts** in the left navigation.
4. On the **Alerts dashboard**, select the alerts that have a *Needs review* status.
5. On the Alerts command bar, select **Dismiss alerts**.
6. On the **Dismiss alerts** detail pane, review the user and policy details associated with the selected alerts.
7. Select **Dismiss alerts** to resolve the alerts as benign.

### Reports for alerts

To see reports for alerts, go to the **Reports** page. Each report widget on the **Reports** page displays information for the last 30 days:

- **Total alerts that need review**: The total number of alerts needing review and triage, including a breakdown by alert severity.
- **Open alerts over past 30 days**: The total number of alerts created by policy matches over the last 30 days, sorted by high, medium, and low alert severity levels.
- **Average time to resolve alerts**: A summary of useful alert statistics:
    - Average time to resolve high severity alerts, listed in hours, days, or months.
    - Average time to resolve medium severity alerts, listed in hours, days, or months.
    - Average time to resolve low severity alerts, listed in hours, days, or months.

### Assign an alert

If you're an administrator and a member of the *Insider Risk Management*, *Insider Risk Management Analysts*, or *Insider Risk Management Investigators* role group, you can assign ownership of an alert to yourself or to an Insider Risk Management user with one of the same roles. After you assign an alert, you can reassign it to a user with any of the same roles. You can only assign an alert to one admin at a time.

Note

If you [scope your policies by one or more administrative units](purview-admin-units), you can only give ownership of an alert to Insider Risk Management users with the appropriate role group permissions. The user highlighted in the alert must be in scope of the admin unit. For example, if an administrative scope applies to just users in Germany, the Insider Risk Management user can only see alerts for users in Germany. Unrestricted administrators can see all alerts for all users in the organization.

After you assign an admin, you can search by admin.

Note

Admins contained within a Microsoft Entra security group aren't supported for alert assignment. Admins must be directly assigned to one of the required roles.

If you're using a custom group, make sure that the custom group contains the [*Case management* role](purview-permissions#relationship-of-members-roles-and-role-groups). The *Insider Risk Management Analysts* and the *Insider Risk Management Investigators* role groups both contain the *Case management* role. If you're using a custom group, you must explicitly add the *Case management* role to the group.

#### Assign an alert from the Alerts dashboard

To assign an alert from the Alerts dashboard, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Alerts** in the left navigation.
4. On the **Alerts dashboard**, select the alerts that you want to assign.
5. In the command bar over the alerts queue, select **Assign**.
6. In the **Assign owner** pane on the right side of the screen, search for an admin with the appropriate permissions, and then select the checkbox for that admin.
7. Select **Assign**.

#### Assign an alert from the Alerts detail page

To assign an alert from the alert details page, follow these steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Alerts** in the left navigation.
4. Select an alert.
5. In the detail pane for the alert, in the upper-right corner of the page, select **Assign**.
6. In the **Suggested contacts** list, select the appropriate admin.

### Create a case for an alert

Create a case for an alert to investigate potentially risky activity. You must be a member of the *Insider Risk Management* or *Insider Risk Management Investigators* role group to create a case.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Alerts** in the left navigation.
4. On the **Alerts dashboard**, select the alert you want to confirm and create a new case for.
5. On the **Alerts details pane**, select **Actions** &gt; **Confirm alerts & create case**.
6. In the **Confirm alert and create insider risk case** dialog box, enter a name for the case, select users to add as contributors, and add comments as applicable. Comments automatically add to the case as a case note.
7. To download the content for the case, select **Create case with content download on** (preview). After you reach the content download limit, you can still create cases, but you must leave the box unchecked. If you don't enable content download when you create the case, you can enable downloads when the case is active.
8. Select **Create case** to create a new case.

After you create the case, investigators and analysts can manage and act on the case. For more information, see the [Insider Risk Management case](insider-risk-management-cases) article.

## Retention and item limits

As Insider Risk Management alerts age, their value to minimize potentially risky activity diminishes for most organizations. Conversely, active cases and associated artifacts (alerts, insights, activities) always provide value and don't have an automatic expiration date. This retention policy includes all future alerts and artifacts in an active status for any user associated with an active case.

To minimize the number of older items that provide limited current value, the following retention and limits apply for Insider Risk Management alerts, cases, and user reports:

| Item | Retention/Limit |
| --- | --- |
| Active cases (and associated artifacts) | 2,000 active cases, retained indefinitely and never expire |
| Alerts with Needs review status | 120 days from alert creation, then automatically deleted |
| Maximum number of active cases | 100 |
| Resolved cases (and associated artifacts) | 120 days from case resolution, then automatically deleted |
| User activities reports | 120 days from report creation, then automatically deleted |

## Best practices for managing your alert volume

To minimize insider risks in your organization, regularly review, investigate, and act on potentially risky insider alerts. Quickly taking action to reduce these risks can potentially save your organization time, money, and potential regulatory or legal consequences. [Learn about best practices for managing your Insider Risk Management alert queue](insider-risk-management-best-practices-alert-tuning).