---
layout: Conceptual
title: Take action on Insider Risk Management cases | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-cases
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Investigate Insider Risk Management cases in Microsoft Purview and take actions such as notifying users, resolving cases, sharing details, or escalating to eDiscovery (Premium).
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
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
ms.custom: msecd-doc-authoring-1014, admindeeplinkCOMPLIANCE, sfi-image-nochange
ai-usage: ai-assisted
locale: en-us
document_id: 699d73b9-a740-675d-02ee-766041b7d0ec
document_version_independent_id: 699d73b9-a740-675d-02ee-766041b7d0ec
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-cases.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-cases
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-cases.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 825bac38-685e-3ed2-9ba7-9daf988124ae
---

# Take action on Insider Risk Management cases | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Cases are the core of Insider Risk Management. They let you investigate and act on issues that risk indicators in your policies generate. Create cases manually from alerts when you need to take extra steps to address a compliance-related issue for a user. Each case focuses on one user. You can add multiple alerts for that user to an existing case or start a new case.

After you investigate the details of a case, take action by:

- Sending the user a notice
- Resolving the case as benign
- Sharing the case with your ServiceNow instance or with an email recipient
- Escalating the case for an eDiscovery (Premium) investigation

For an overview of how you investigate and manage cases in Insider Risk Management, see the [Insider Risk Management Investigation and Escalation video](https://www.youtube.com/watch?v=UONUSmkRC8s).

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Use the Cases dashboard

Tip

To see reports for cases, go to the **Reports** page. Each report widget on the **Reports** page displays information for the last 30 days:

- **Active cases**: The total number of active cases under investigation.
- **Cases over past 30 days**: The total number of cases created, sorted by *Active* and *Closed* status.
- **Statistics**: Average time of active cases, listed in hours, days, or months.

The Insider Risk Management **Cases dashboard** enables you to view and act on cases. The case queue lists all active and closed cases for your organization, along with the current status of the following case attributes:

- **Case ID**: The ID of the case.
- **Case name**: The name of the case, defined when you confirm an alert and create the case.
- **Status**: The status of the case, either *Active* or *Closed*.
- **User**: The user for the case. If you enable anonymization for usernames, the portal displays anonymized information.
- **Content download**: This field shows whether content download is on or off for the case.
- **Time case opened**: The time that passes since the case is opened.
- **Total policy alerts**: The number of policy matches included in the case. This number might increase if you add new alerts to the case.
- **Last activity date**: The time that passes since you add a case note or change the case state.
- **Last updated by**: The name of the Insider Risk Management analyst or investigator that last updated the case.

Note

If you [scope your policies by one or more administrative units](purview-admin-units), you can only give ownership of a case to Insider Risk Management users with the appropriate role group permissions. The user highlighted in the alert must be in scope of the admin unit. For example, if an administrative scope applies to just users in Germany, the Insider Risk Management user can only see alerts for users in Germany. Unrestricted administrators can see all cases for all users in the organization.

Use the **Search** control to search for a Case ID or to search for specific text in case names. Use the case filter to sort cases by the following attributes:

- Status
- Time case opened, start date, and end date
- Last updated, start date, and end date

## Assign a case

If you're an administrator with the appropriate permissions, you can assign ownership of a case to yourself or to an Insider Risk Management user with the Insider Risk Management, Insider Risk Management Analyst, or Insider Risk Management Investigator role. After you assign a case, you can reassign it to a user with any of the same roles. You can only assign a case to one admin at a time.

If you assign an admin to a case, you can filter by admin.

### Assign a case from the Cases dashboard

To assign a case from the Cases dashboard, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Cases** in the left navigation.
4. On the **Cases dashboard**, select the cases that you want to assign.
5. In the command bar over the cases queue, select **Assign**.
6. On the **Assign owner** pane on the right side of the screen, search for an admin with the appropriate permissions, and then select the checkbox for that admin.
7. Select **Assign**.

### Assign a case from the Cases detail page

To assign a case from the case detail page, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Cases** in the left navigation.
4. Select a case.
5. In the detail pane for the case, select **Assign**.
6. In the **Suggested contacts** list, select the appropriate admin.

## Filter cases

Depending on the number and type of active Insider Risk Management policies in your organization, reviewing a large queue of cases can be challenging. By using case filters, analysts and investigators can sort cases by several attributes. To filter alerts on the **Cases dashboard**, select the **Filter** control. You can filter cases by one or more attributes:

- **Status**: Select one or more status values to filter the case list. The options are *Active* and *Closed*.
- **Time case opened**: Select the start and end dates for when the case was opened.
- **Last updated**: Select the start and end dates for when the case was updated.

## Filter cases, save views, customize columns, or search cases

Depending on the number and type of active Insider Risk Management policies in your organization, reviewing a large queue of cases can be challenging. To help you keep track of cases, you can:

- Filter cases by various attributes.
- Save a view of a filter set to reuse later.
- Display or hide columns.
- Search for an alert.

### Filter cases

To filter cases on the Cases dashboard, complete the following steps:

1. Select **Add filter**.
2. Select one or more of the following attributes:

    | Attribute | Description |
    | --- | --- |
    | **Assigned to** | The admin that the alert is assigned to for triaging (if assigned). |
    | **Last activity date** | The start and end dates for when the case was last updated. |
    | **Status** | Current status of the case. The options are *Active* and *Closed*. |
    | **Time case opened** | The start and end dates for when the case was opened. |

    The filter bar shows the attributes that you select.
3. Select an attribute in the filter bar, and then select a value to filter by. For example, select the **Last activity date** attribute, enter or select the dates in the **Start date** and **End date** fields, and then select **Apply**.

    Tip

    To start over at any point, select **Reset all** on the filter bar.

### Save a view of a filter set to reuse later

To save a filter set for reuse, complete the following steps:

1. After applying the case filters described in Filter cases, select **Save** over the filter bar, enter a name for the filter set, and then select **Save**.

    The filter set appears as a card over the filter bar. It includes a number that shows the count of cases that meet the criteria in the filter set.

    Note

    You can save up to five filter sets. To delete a filter set, select the ellipsis (three dots) in the upper-right corner of the card, and then select **Delete**.
2. To reapply a saved filter set, select the card for the filter set.

### Display or hide columns

To display or hide columns on the Cases dashboard, complete the following steps:

1. On the right side of the page, select **Customize columns**.
2. Select or clear the checkboxes for the columns you want to display or hide.

The portal saves the column settings across sessions and across browsers.

### Search for cases

Use the **Search** control to search for a user principal name (UPN), an assigned admin name, or an Alert ID.

## Investigate a case

Deeper investigation into Insider Risk Management alerts is critical to taking proper corrective actions. Insider Risk Management cases are the central management tool to dive deeper into user risk activity history, alert details, the sequence of risk events, and to explore the content and messages exposed to risks. Risk analysts and investigators also use cases to centralize review feedback and notes and to process case resolution.

Selecting a case opens the case management tools and allows analysts and investigators to dig into the details of cases.

### Review the case overview

The **Case overview** tab summarizes the case details for risk analysts and investigators. It includes the following information in the **About this case** area:

- **Case ID**: The ID of the case.
- **Status**: The current status of the case, either Active or Closed.
- **Case created on**: The date and time the case was created.
- **User's risk score**: The current calculated risk level of the user for the case. The system calculates this score every 24 hours and uses alert risk scores from all active alerts associated to the user. When *User is detected as a potential high impact user* or *User is a member of a priority user group* risk booster is enabled as **Risk score boosters** in the **Policy indicators** section of the **Insider Risk Management settings** page, the **User details** page includes detailed information about the user's calculated risk level.
- **Email**: The email alias of the user for the case.
- **Organization or department**: The organization or department that the user is assigned to.
- **Manager name**: The name of the user's manager.
- **Manager email**: The email alias of the user's manager.

![Screenshot of the Insider Risk Management case details page showing the About this case area with case ID, status, risk score, and manager information.](media/insider-risk-case-details.png)

The **Case overview** tab also includes an **Alerts** section that includes the following information about policy match alerts associated with the case:

- **Policy matches**: The name of the Insider Risk Management policy associated with the match alerts for potentially risky user activity that might lead to a security incident.
- **Status**: Status of the alert.
- **Severity**: Severity of the alert.
- **Time detected**: The time that has passed since the alert was generated.

### Review alerts in a case

The **Alerts** tab summarizes the current alerts included in the case. You can add new alerts to an existing case. When you assign new alerts, the **Alert** queue includes them. The queue lists the following alert attributes:

- Alert
- Alert ID
- Status
- Severity
- Time detected

Select an alert from the queue to display the **Alert detail** page.

Use the search control to search for an Alert ID or specific text in alert names. Use the alert filter to sort cases by the following attributes:

- Status
- Severity
- Time detected, start date, and end date

Use the filter control to filter alerts by several attributes, including:

- **Status**: Select one or more status values to filter the alert list. The options are *Confirmed*, *Dismissed*, *Needs review*, and *Resolved*.
- **Severity**: Select one or more alert risk severity levels to filter the alert list. The options are *High*, *Medium*, and *Low*.
- **Time detected**: Select the start and end dates for when the alert was created.
- **Policy**: Select one or more policies to filter the alerts generated by the selected policies.

### Review user activity in a case

Risk analysts and investigators use the **User activity** tab to review user activity details. It provides a visual representation of all the potentially risky activities associated with risk alerts and cases. Use this information to determine whether those risky activities might lead to a security incident. For example, as part of the alert triage process, analysts might need to review all the risk activities associated with the case for more details. In cases, risk investigators can review user activity details and the bubble chart to help understand the overall scope of the risk activities associated with the case. For more information about the User activity chart, see the [Insider Risk Management activities](insider-risk-management-activities#review-the-user-activity-tab) article.

### Activity explorer (preview)

The **Activity explorer** tab helps risk analysts and investigators review case activity details associated with risk alerts. For example, as part of the case management actions, investigators and analysts might need to review all the risk activities associated with the case for more details. By using the **Activity explorer**, reviewers can quickly examine a timeline of detected potentially risky activity and identify and filter all risk activities associated with alerts.

For more information about the Activity explorer, see the [Insider Risk Management activities](insider-risk-management-activities#activity-explorer-tab) article.

### Review forensic evidence

The **Forensic evidence** tab helps risk investigators review visual captures associated with risk activities included in cases. For example, as part of the case management actions, investigators might need to clarify the context of the user activity under review. Viewing the actual clips of the activity can help the investigator determine if the user activity is potentially risky and might lead to a security incident.

For more information about forensic evidence, see the [Learn about Insider Risk Management forensic evidence](insider-risk-management-forensic-evidence) article.

### Use Content explorer for case evidence

The **Content explorer** tab helps risk investigators review copies of all individual files and email messages associated with risk alerts. For example, if an alert is created when a user downloads hundreds of files from SharePoint Online and the activity triggers a policy alert, the case captures and copies all the downloaded files for the alert to the Insider Risk Management case from original storage sources.

If content download is off for the case, select **Add content** from the Content explorer tab. If you've reached the maximum number cases with content downloaded limit, you must resolve cases to download additional content.

The Content explorer is a powerful tool with basic and advanced search and filtering features. To learn more about using the Content explorer, see [Insider Risk Management Content explorer](insider-risk-management-content-explorer).

![Screenshot of the Content explorer tab in an Insider Risk Management case showing files and email messages associated with risk alerts.](media/insider-risk-content-explorer.png)

### Manage case notes

Risk analysts and investigators use the **Case notes** tab in a case to share comments, feedback, and insights about their work for the case. Notes are permanent additions to a case. After saving a note, you can't edit or delete it. When you create a case from an alert, the comments you enter in the **Confirm alert and create insider risk case** dialog box automatically become a case note.

The case notes dashboard shows notes by the user who created the note and the time that passes since the note is saved. To search the case note text field for a specific keyword, use **Search** on the case dashboard and enter a specific keyword.

#### System-generated notes (preview)

System-generated notes are automatically added to cases when there's a change in status or assignment. The following changes trigger a system-generated note:

- A change in case status
- A change in the assigned user
- Closure of a case
- A case escalation

System-generated notes appear alongside analyst-created notes in the **Notes** tab within the case details panel, helping you stay up to date with all activity on a case.

#### Add a case note

To add a note to a case, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Cases** in the left navigation.
4. Select a case, then select the **Case notes** tab.
5. Select **Add case note**.
6. In the **Add case note** dialog box, type the note.
7. Select **Save** to add the note to the case.

### Manage case contributors

Risk analysts and investigators can add other reviewers to the case through the **Contributors** tab. Users must be assigned the **Role Management** role to add contributors to the case. By default, all users assigned the **Insider Risk Management Investigators** and the **Insider Risk Management** roles appear as contributors for each active and closed case.

You can grant temporary access to a case by adding a user as a contributor, but with the following restrictions:

- Analysts and investigators can add contributors.
- You can't add analysts as contributors.
- Contributors can't add contributors.

Contributors have all case management control on the specific case except for:

- Permission to confirm or dismiss alerts.
- Permission to edit the contributors for cases.

#### Add a contributor to a case

To add a contributor to a case, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Cases** in the left navigation.
4. Select a case, and then select the **Contributors** tab.
5. Select **Add contributor**.
6. In the **Add contributor** dialog box, start typing the name of the user you want to add, and then select the user from the suggested user list. This list comes from the Microsoft Entra ID of your tenant subscription.
7. Select **Add** to add the user as a contributor.

## Case actions

Risk investigators can take action on a case in one of several methods. The method depends on the severity of the case, the history of risk of the user, and the risk guidelines of your organization. In some situations, you might need to escalate a case to a user or data investigation to collaborate with other areas of your organization and to dive deeper into risk activities. Insider Risk Management is tightly integrated with other Microsoft Purview solutions to help you with end-to-end resolution management.

### Send email notice

In most cases, user actions that create insider risk alerts are inadvertent or accidental. Sending a reminder notice to the user by email is an effective method for documenting case review and action. This method reminds users of corporate policies or points them to refresher training. You generate notices from [notice templates that you create](insider-risk-management-notices) for your Insider Risk Management infrastructure.

Remember that sending an email notice to a user ***does not*** resolve the case as *Closed*. In some cases, you might want to leave a case open after sending a notice to a user to look for more risk activities without opening a new case. If you want to resolve a case after sending a notice, select **Resolve case** as a follow-on step after sending a notice.

#### Send a notice to the user assigned to a case

To send a notice to the user assigned to a case, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Cases** in the left navigation.
4. Select a case, and then select **Send email notice** on the case action toolbar.
5. In the **Send e-mail notice** dialog box, select the **Choose a notice template** dropdown control to select the notice template for the notice. This selection pre-fills the other fields in the notice.
6. Review the notice fields and update as appropriate. The values you enter override the values in the template.
7. Select **Send** to send the notice to the user. All sent notices are added to the case notes queue on the **Case notes** dashboard.

### Escalate for investigation

Escalate the case for user investigation when you need extra legal review for the user's risk activity. This escalation opens a new Microsoft Purview eDiscovery (Premium) case in your Microsoft 365 organization. eDiscovery (Premium) provides an end-to-end workflow to preserve, collect, review, analyze, and export content that's responsive to your organization's internal and external legal investigations. It also lets your legal team manage the entire legal hold notification workflow to communicate with custodians involved in a case. Escalating to an eDiscovery (Premium) case from an Insider Risk Management case helps your legal team take appropriate action and manage content preservation. For more information about eDiscovery (Premium) cases, see [Overview of Microsoft Purview eDiscovery (Premium)](ediscovery-overview).

#### Escalate a case to a user investigation

To escalate a case to a user investigation, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Cases** in the left navigation.
4. Select a case, and then select **Escalate for investigation** on the case action toolbar.
5. In the **Escalate for investigation** dialog box, enter a name for the new user investigation. If needed, enter notes about the case, and then select **Escalate**.
6. Review the notice fields and update as appropriate. The values you enter override the values on the template.
7. Select **Confirm** to create the user investigation case.

After you escalate the Insider Risk Management case to a new user investigation case, you can review the new case in the **eDiscovery** &gt; **Advanced** area in the Microsoft Purview portal.

### Run automated tasks by using Power Automate flows for the case

By using recommended Power Automate flows, risk investigators and analysts can quickly take action to:

- Request information from HR or business about a user in an insider risk case.
- Notify manager when a user has an insider risk alert.
- Create a record for an Insider Risk Management case in ServiceNow.
- Notify users when they're added to an insider risk policy.

To run, manage, or create Power Automate flows for an Insider Risk Management case:

1. Select **Automate** on the case action toolbar.
2. Choose the Power Automate flow to run, and then select **Run flow**.
3. After the flow completes, select **Done**.

For more information about Power Automate flows for Insider Risk Management, see [Getting started with Insider Risk Management settings](insider-risk-management-settings-power-automate).

### View or create a Microsoft Teams team for the case

When you enable Microsoft Teams integration for Insider Risk Management in settings, the solution automatically creates a Microsoft Teams team every time you confirm an alert and create a case. Risk investigators and analysts can quickly open Microsoft Teams and navigate directly to the team for a case by selecting **View Microsoft Teams team** on the case action toolbar.

For cases you open before enabling Microsoft Team integration, risk investigators and analysts can create a new Microsoft Teams team for a case by selecting **Create Microsoft Teams team** on the case action toolbar.

When you resolve a case, the solution automatically archives the associated Microsoft Team (hides it and turns it to read-only).

For more information about Microsoft Teams for Insider Risk Management, see [Getting started with Insider Risk Management settings](insider-risk-management-settings-teams).

### Resolve the case

After risk analysts and investigators complete their review and investigation, resolve a case to act on all the alerts currently included in the case. Resolving a case adds a resolution classification, changes the case status to *Closed*, and automatically adds the resolution action reasons to the case notes queue on the **Case notes** dashboard. Resolve cases as either:

- **Benign**: The classification for cases where policy match alerts are evaluated as low risk, non-serious, or false positive.
- **Confirmed policy violation**: The classification for cases where policy match alerts are evaluated as risky, serious, or the result of malicious intent.

    Note

    If you select the option to delete the case and associated content immediately when resolving the case, you permanently remove all related content, alerts, and insights.

#### Resolve a case

To resolve a case, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Insider Risk Management** solution.
3. Select **Cases** in the left navigation.
4. Select a case, and then select **Resolve case** on the case action toolbar.
5. In the **Resolve case** dialog box, select the **Resolve as** dropdown control to select the resolution classification for the case. The options are **Benign** or **Confirmed policy violation**.
6. In the **Resolve case** dialog box, enter the reasons for the resolution classification in the **Action taken** text field.
7. Select **Resolve** to close the case.