---
layout: Conceptual
title: Use reports in Insider Risk Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-reports
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Use Microsoft Purview Insider Risk Management reports to review trends and insights for alerts, analytics, cases, and user activity across your insider risk program.
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
ms.custom: admindeeplinkCOMPLIANCE, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 77470f72-fdc1-48e8-3d0d-e39adfb45e93
document_version_independent_id: 77470f72-fdc1-48e8-3d0d-e39adfb45e93
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-reports.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-reports
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-reports.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: 54dc0084-43df-5ae8-1fb0-c3ca8f1980ac
---

# Use reports in Insider Risk Management | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Use reports in Microsoft Purview Insider Risk Management to understand the landscape of your insider risk program. Reports provide deeper insights and summary information for all areas relating to insider risk, including alerts, cases, user activity, and analytics generated from qualifying risk activities across Microsoft services to help identify insights into potential areas of risk.

The following reports are available by navigating to **Insider Risk Management** &gt; **Reports** in the [Microsoft Purview portal](purview-portal):

- **Alerts (preview)**: View alert report trends for generated alerts, actions taken on alerts over time, and alerts by policy.
- **Analytics**: View an analytics reports summary of anonymized user activities detected in your organization.
- **Cases (preview)**: View case report trends for created cases, actions taken on cases over time, and case status by policy and region.
- **User activity**: Review recent user activity reports, regardless if the user is included in a policy or alert.
- **Pay-as-you-go**: Review pay-as-you-go usage reports to identify cost-saving opportunities and fine-tune your policy configurations.

## Work with reports

To get started and view Insider Risk Management reports, you must be a member of the applicable role or role group. Permission requirements differ for viewing reports for alerts and cases and the permissions required to view reports for analytics. If your organization uses administrative units, access might vary for these reports. For more information, see:

- [Permissions for Insider Risk Management](insider-risk-management-permissions)
- [Permissions for Insider Risk Management and administrative units](insider-risk-management-permissions#consider-administrative-units-if-you-want-to-scope-user-permissions-to-a-region-or-department)

### Customize charts

For each report area, predefined report filter controls and a date selector help you quickly scope insights to specific criteria or date ranges. Select a filter at the top of the page for each area to quickly scope all the reports in the area to a filter setting. For reporting dates, select a specific month or select *Last 3 months* to view all data for the report area.

You might also want to pick and choose which reports to display by default in each report area. To customize the reports shown in each area, select **Customize view**. On the **Customize view** flyout pane, you can choose which reports to display and which reports to hide in each area.

### Chart details

To explore the results in a report, select **View details** for the report. In the details view, you can filter the information and change your view by dates or policies. To export data in a report, select **Export** to download either an image of the report chart or a .csv file with the report values.

## Alert reports (preview)

Investigating potentially risky user activities is an important step in minimizing insider risks for your organization. These risks might be activities that generate alerts from Insider Risk Management policies. Alert reports provide insights into alert volumes, progress of managing alerts, common alert sources, and time spent triaging. You can quickly filter all alert reports by *All alerts*, *Confirmed alerts*, and *Dismissed alerts*.

| Report type | Report | Description |
| --- | --- | --- |
| **Summary** | Alerts generated | Shows the number of low, medium, and high severity alerts generated during the specified date range.​ |
|  | Alerts acted on​ | Shows the number of alerts confirmed to a case or dismissed during the specified date range. |
|  | Dismissal reasons | Shows... |
| **Demographics** | Top countries/regions with alerts​ | Shows the number of alerts generated for users based on what country or region they’re in. *Not specified* means their country or region isn’t specified in Microsoft Entra ID. |
|  | Alerts generated by department | Shows the number of alerts generated for users based on what department they’re in. *Not specified* means their department isn’t specified in Microsoft Entra ID.​ |
| **Insights** | Alerts by top triggering event | Shows the number of alerts based on top triggering events detected during the specified date range.​ |
|  | Alerts by top activity that generated the alert | Shows the number of alerts based on top activities detected during the specified date range.​ |
| **Productivity** | Alert status by assignment | Shows the number of alerts assigned to specific admins, broken down by alert status.​ |
|  | Average days alerts are in *Needs Review* | Shows the average number of days that alerts remained in a *Needs review* status during the specified date range.​ |

## Analytics reports

After the first analytics scan completes for your organization, members of the *Insider Risk Management Admins* role group automatically receive an email notification. They can view the initial insights and recommendations for potentially risky activities by your users. Daily scans continue unless you turn off analytics for your organization. Admins receive email notifications for each of the three in-scope categories for analytics (data leaks, theft, and exfiltration) after the first instance of potentially risky activity in your organization. Admins don't receive email notifications for follow-up risk management activity detection resulting from the daily scans.

Note

If you disable and then re-enable the **Analytics** setting, you reset automatic email notifications. Members of the *Insider Risk Management Admins* role group receive email notifications for new scanning insights.

To view potential risks for your organization, go to **Insider Risk Management** &gt; **Reports** &gt; **Analytics**.

Note

If the scan for your organization isn't complete, you see a message that the scan is still active.

For completed analyses, you see the potential risks discovered in your organization and insights and recommendations to address these risks. Reports include identified risks and specific insights grouped by area, the total number of users (all types of Microsoft Entra accounts, including user, guest, system, and so on) with identified risks, the percentage of these users with potentially risky activities, and a recommended insider risk policy to help mitigate these risks. The reports include:

- **Data leaks insights**: For all users that might include accidental oversharing of information outside your organization or data leaks by users with malicious intent.
- **Data theft insights**: For departing users or users with deleted Microsoft Entra accounts that might include risky sharing of information outside your organization or data theft by users with malicious intent.
- **Top exfiltration insights**: For all users that might include sharing data outside of your organization.

![Screenshot of the Insider Risk Management analytics overview report showing data leaks, data theft, and exfiltration insights with user counts and recommended policies.](media/insider-risk-analytics-overview.png)

To display more information for an insight, select **View details** to display the details pane for the insight. The details pane includes the complete insight results, an insider risk policy recommendation, and **Create policy** to quickly help you create the recommended policy. Selecting **Create policy** takes you to the policy workflow and automatically selects the recommended policy template related to the insight. For example, if the analytics insight is for *Data Theft* activity, the *Data Theft* policy template is pre-selected in the policy workflow for you.

![Screenshot of the Insider Risk Management analytics details pane showing insight results, a policy recommendation, and the Create policy button.](media/insider-risk-analytics-details.png)

## Case reports (preview)

[Cases](insider-risk-management) help you investigate and act on issues generated by risk indicators defined in your policies. You manually create cases from alerts when you need to take further action to address a compliance-related issue for a user. Case reports provide trend information to help you track the type of cases, the current status of cases, cases by region or assignment, and more. You can quickly filter all case reports by *All cases*, *Confirmed cases*, and *Benign cases*.

| Report type | Report | Description |
| --- | --- | --- |
| **Summary** | Cases created | Shows the number of cases created during the specified date range. |
|  | Actioned cases | Shows the number of cases with activity during the specified date range. |
| **Demographics** | Top countries/regions with cases​ | Shows the number of cases created for users based on their country or region. *Not specified* means their country or region isn't specified in Microsoft Entra ID. |
|  | Top departments with cases​ | Shows the number of cases created for users based on their department. *Not specified* means their country or region isn't specified in Microsoft Entra ID. |
| **Productivity** | Case status by assignment | Shows the number of cases assigned to specific admins, broken down by alert status. |
|  | Average days with active status | Shows the average number of days that cases stayed in an *Active* status during the specified date range. |

## Pay-as-you-go usage reports

[Pay-as-you-go](purview-billing-models#pay-as-you-go-billing-model) usage reports provide transparency and enable more accurate budget planning and policy tuning. The reports let you explore granular breakdowns of billed processing usage across different data source categories and activity indicators over time. View your usage and trends, and understand activity patterns. This information empowers you to identify cost-saving opportunities and fine-tune your policy configurations.

This report is available in the **Reports** page by default. For prerequisites and billing details, see [Pay-as-you-go billing model](purview-billing-models#pay-as-you-go-billing-model).

## User activity reports

User activity reports let you examine potentially risky activities for specific users during a defined time period without assigning these activities, temporarily or explicitly, to an Insider Risk Management policy. In most Insider Risk Management scenarios, you explicitly define users in policies. These users might have policy alerts (depending on triggering events) and risk scores associated with the activities. But in some scenarios, you might want to examine the activities for users that you don't explicitly define in a policy. These activities might be for users that you receive a tip about the user and potentially risky activities, or users that typically don't need to be assigned to an Insider Risk Management policy.

After you configure indicators on the Insider Risk Management **Settings** page, the solution detects user activity for potentially risky activity associated with the selected indicators. This configuration makes all detected activity for users available for review, regardless if it has a triggering event or if it creates an alert. Reports are created on a per-user basis and can include all activities for a custom 90-day period. The solution doesn't support multiple reports for the same user.

After examining potentially risky activities, investigators can dismiss individual user's activities as benign. They can also share or email a link to the report with other investigators, or choose to assign users (temporarily or explicitly) to an Insider Risk Management policy. To view the **User activity reports** page, you must assign users to the *Insider Risk Management Investigators* role group.

![Screenshot of the Insider Risk Management user activity report overview page showing a list of user reports with status and date information.](media/insider-risk-user-activity-report-overview.png)

### Create a user activity report

To create a user activity report, complete the following steps:

1. Go to **Insider Risk Management** &gt; **Reports** &gt; **User activity**.
2. Select **Create user activity report**.
3. Select a date for the **Start date**.
4. Select a date for the **End date**.
5. In the **Users** field, search for one or more users by name or user principal name.
6. Select **Create report**.

User activity data becomes available for reporting about 48 hours after the activity occurs. For example, to review user activity data for December 1, you need to wait at least 48 hours before creating the report (you can create a report on December 3 at the earliest).

New reports typically take up to 10 hours before they're ready for review. When the report is ready, *Report ready* appears in the **Status** column on the User activity report page.

### View a user activity report

Select the user to view the detailed report:

![Screenshot of the Insider Risk Management user activity report showing activity details for the selected user.](media/insider-risk-user-activity-report.png)

The **User activity report** for the selected user contains the **User activity**, **Activity explorer**, and **Forensic evidence** tabs:

- **User activity**: Use this chart view to investigate potentially risky activities and view potentially related activities that occur in sequences. This tab is structured to enable quick review of a case, including a historical timeline of all activities, activity details, the current risk score for the user in the case, the sequence of risk events, and filtering controls to help with investigative efforts. For more information, see [User activity](insider-risk-management-activities#review-the-user-activity-tab).
- **Activity explorer**: This tab provides risk investigators with a comprehensive analytics tool that provides detailed information about activities. With the Activity explorer, reviewers can quickly review a timeline of detected risky activity and identify and filter all potentially risky activities associated with alerts. For more information, see [Activity explorer](insider-risk-management-activities#activity-explorer-tab).
- **Forensic evidence**: This tab allows risk investigators to review visual captures associated with risk activities included in cases from [forensic evidence detection](insider-risk-management-forensic-evidence).