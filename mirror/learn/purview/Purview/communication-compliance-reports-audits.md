---
layout: Conceptual
title: Use Communication Compliance reports and audits | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/communication-compliance-reports-audits
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Review Communication Compliance reports and audit data to monitor policy activity, investigate events, and support compliance reporting.
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
ms.custom: msecd-doc-authoring-1014, sfi-ga-nochange, sfi-image-nochange
ai-usage: ai-assisted
locale: en-us
document_id: 6da613f3-96ac-dde0-230b-4044155a4ead
document_version_independent_id: 6da613f3-96ac-dde0-230b-4044155a4ead
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/communication-compliance-reports-audits.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: communication-compliance-reports-audits
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/communication-compliance-reports-audits.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 37eb8d85-dcf6-66bf-48ae-cf11028d3bf9
---

# Use Communication Compliance reports and audits | Microsoft Learn

Important

[Microsoft Purview Communication Compliance](communication-compliance) provides the tools to help organizations detect regulatory compliance (for example, SEC or FINRA) and business conduct violations such as sensitive or confidential information, harassing or threatening language, and sharing of adult content. Communication Compliance is built with privacy by design. Usernames are pseudonymized by default, role-based access controls are built in, investigators are opted in by an admin, and audit logs are in place to help ensure user-level privacy.

## Use Communication Compliance reports

Note

Currently, if your role is scoped by one or more [admin units in Microsoft Purview](purview-admin-units), the admin units don't apply to reports. You can see all reports in the organization.

The **Reports** dashboard is the central location for viewing all Communication Compliance reports. To view and manage reports, assign users to the *Communication Compliance Viewers* role group.

Report widgets provide a quick view of insights most commonly needed for an overall assessment of the status of Communication Compliance activities. You can't export the information contained in the report widgets. Detailed reports provide in-depth information related to specific Communication Compliance areas and offer the ability to filter, group, sort, and export information while reviewing.

For the date range filter, the date and time for events are listed in Coordinated Universal Time (UTC). When filtering messages, all filters for the report apply at the 00:00:00 UTC start date to the 23:59:59 UTC end date.

![Screenshot of the Communication Compliance reports dashboard showing report categories: Items matched, Items pending review, Resolved items, Tagged as compliant, Tagged as noncompliant, and Tagged as questionable.](media/communication-compliance-reports-dashboard.png)

The **Reports dashboard** contains the following report widgets and detailed reports links:

### Report widgets

The Reports dashboard includes the following widgets that provide at-a-glance summaries of policy activity:

- **Recent policy matches**: displays the number of matches by active policies over time.
- **Resolved items by policy**: displays the number of policy match alerts resolved by policies over time.
- **Policy with most matches**: displays the policies and the number of matches for a given period, ranked highest to lowest for matches.
- **Users with most policy match**: displays the users (or anonymized usernames) and number of policy matches for a given period.
- **Escalations by policy**: displays the number of escalations per policy over a given time.

### Detailed reports

Use the *Export report* option to create a .CSV file containing the report details for any detailed report. The *Export report* option supports file size downloads up to 3 MB.

- **Policy settings and status**: provides a detailed look at policy configuration and settings, as well as the general status for each of the policy (matches and actions) on messages. Includes policy information and how policies are associated with users and groups, locations, review percentages, reviewers, status, and when the policy was last modified. Use the *Export* option to create a .CSV file containing the report details.
- **Items and actions per policy**: Review and export matching items and remediation actions per policy. Includes policy information and how policies are associated with:

    - Case created
    - Escalated items
    - Items matched
    - Items pending review
    - Resolved items
    - Tagged as compliant
    - Tagged as noncompliant
    - Tagged as questionable
    - User notified
- **Item and actions per location**: Review and export matching items and remediation actions per Microsoft 365 location. Includes information about how workload platforms are associated with:

    - Case created
    - Escalated items
    - Items matched
    - Items pending review
    - Resolved items
    - Tagged as compliant
    - Tagged as noncompliant
    - Tagged as questionable
    - User notified
- **Activity by user**: Review and export matching items and remediation actions per user. Includes information about how users are associated with:

    - Case created
    - Escalated items
    - Items matched
    - Items pending review
    - Resolved items
    - Tagged as compliant
    - Tagged as noncompliant
    - Tagged as questionable
    - User notified

Note

The items and actions displayed are only for the items and actions *matched* within the report's selected date range filter.

- **Sensitive information type per location** (preview): Review and export information about the detection of sensitive information types and the associated sources in Communication Compliance policies. Includes the overall total and the specific breakdown of sensitive information type instances in the sources configured in your organization. The values for each third-party source are displayed in separate columns in the .CSV file. Examples are:

    - **Email**: Sensitive information types detected in Exchange email messages.
    - **Teams**: Sensitive information types detected in Microsoft Teams channels and chat messages.
    - **Microsoft 365 Copilot and Microsoft 365 Copilot Chat**: Sensitive information types detected in Copilot interactions.
    - **Viva Engage**: Sensitive information types detected in Viva Engage inboxes, posts, chats, and replies.
    - **Third-party sources**: Sensitive information types detected for activities associated with third-party connectors configured in your organization. To view the breakdown of third-party sources for a specific sensitive information type in the report, hover your mouse over the value for the sensitive information type in the Third-party source column.
    - **Other**: Sensitive information types used for internal system processing. Selecting or deselecting this source for the report won't affect any values.
- **Email blast senders**: Review and export the list of senders of email blast messages that were filtered out from your Communication Compliance policies to reduce "noise." [**Filter email blasts** is a Communication Compliance policy setting](communication-compliance-policies#filter-email-blasts). The Email blast senders report includes the following fields:

    - Policy name
    - Policy last modified date
    - Sender
    - Number of mails filtered

### Export a message details report

You can create custom reports and review details for messages brought into the scope of specific policies. Use these reports for all-up reviews of messages and for creating a report snapshot for a customizable time period. You can create a one-time report, or if you often need to create the same report, schedule report creation on a daily, weekly, or monthly basis. You can create up to five schedules per policy.

When you create a report, reviewers for the policy receive an email notification with a link to the **Exports** tab, where they can download the report as a CSV file.

![Screenshot of a Communication Compliance message details report showing export options including user selection, frequency, date range, and the fields included for each policy message item such as Match ID, Sender, Date, Location, and Item Status.](media/communication-compliance-message-detail-report.png)

#### Create the report

To create a message details report, complete the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) using credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Communication Compliance** solution.
3. Select **Policies** in the left navigation.
4. Select a policy, then select **Export report** in the upper-right corner of the page.
5. On the **Export options** pane, under **Include items from these users**, select one of the following options:

    - **All users**. Select this option to create a report with message information for all users in the policy.
    - **Select users**. Select this option, then select specific users from the list, to create a report with messages sent by those specific users. Only the users who sent a message that the system flagged are available in the list.
6. In the **Select frequency** list, select how often you want to create the report.
7. If it's a one-time report, enter a start date and end date for the report. If it's a recurring report, enter a date to start sending reports and a date to stop sending reports.

    Note

    If you select **Daily**, **Weekly**, or **Monthly** for a recurring report, the report starts collecting messages from the previous day, week, or month, depending on which option you select. For example, if you choose **Daily** as the frequency and choose **June 4, 2024** as the start date for the report, the report starts collecting messages on June 3.
8. In the **Send report to these reviewers** list, add or delete reviewers as needed. By default, all reviewers for the policy (added during policy creation) are listed.
9. In the **Report name** field, accept the suggested name for the report or change it as needed.
10. Select **Create report** (for one-time reports) or **Start scheduled export** (for recurring reports).

    The **Preparing scheduled report** dialog box appears.
11. Select **Manage scheduled exports** to view the schedule of reports.

    Tip

    To edit a report schedule, select **Manage scheduled reports** from the **Exports** tab.
12. To make changes to a scheduled report:

    1. Select the checkbox for the report, then select **Edit**.
    2. In the **Export options** dialog box, make the changes that you want.

    Note

    To change the frequency or start date of the report, delete the report from the **Manage scheduled exports** page, then create the report again.

Note

You can create up to five scheduled reports per policy. If you already have five scheduled reports for a policy and want to create a new one, delete one of the existing report schedules before you can create a new one.

**Download a report when it's ready**

The time it takes to create a report depends on the number of scheduled reports and the size of the reports. Reviewers on the policy receive an email notification with a link to the **Exports** tab when a report is ready. To download a report from the **Exports** tab, select a report in the *Ready to download* state, then select **Download export(s)**.

Note

If your selected time period doesn't return any message results in the report, it means there were no messages for the selected time period. The report is blank.

#### What's included in a Message details report

Message details reports contain the following information for each message item in the policy:

- **Match ID**: Unique ID for a copy of the message in Communication Compliance.
- **Internet Message ID**: Unique ID for the message across platforms.
- **Conversation Family ID**: Thread ID for the message.
- **Sender column**: Sender of the message. If the policy match is a response from Microsoft 365 Copilot and Microsoft 365 Copilot Chat, the value is "Copilot".
- **Recipient column**: Recipients included in the message. If the policy match is a prompt to Copilot, the value is "Copilot".
- **Date**: The date when the message was sent.
- **Location**: Channel where the message was sent. This channel can be Exchange Online, Teams, Viva Engage, or any third-party channel that Communication Compliance supports.
- **Subject**: Subject of the message. If it's a Copilot interaction, the subject of the message is "Copilot" and the name of the Microsoft 365 app. For example: "Copilot in Excel".
- **Contains Attachments**: Status of any attachments for the message. Values are either *Yes* or *No*.
- **Policy Name**: Name of the policy associated with the message. This value is the same for all messages in the report.
- **Item Status**: Status of the message item in the policy. Values are *Pending* or *Resolved*.
- **Tags**: Tags assigned to the message. Values are *Questionable, Compliant*, or *Noncompliant*.
- **Keyword Matches**: Keyword matches for the message.
- **Trainable Classifier ID**: ID of the trainable classifier that was matched.
- **Trainable Classifier Name and Matched Keywords**: The name of the trainable classifier and the keywords that triggered the classifier match.
- **Reviewers**: Reviewers assigned to message.
- **Pending for (days)**: Number of days the message has been in a pending state. For resolved messages, the value is 0.
- **Comment for Resolved**: Comments for the message entered when resolved.
- **Resolved Date**: Date and Coordinated Universal Time (UTC) the message was resolved.
- **Last Updated By**: User name of the last updater.
- **Last Updated On**: Date and Coordinated Universal Time (UTC) the message was last updated.
- **History of Comments**: List of all comments for the message alert, including comment author and date and Coordinated Universal Time (UTC) of the comment.

Tip

You can also [archive message details outside of Communication Compliance](communication-compliance-investigate-remediate#archive-message-details-outside-of-communication-compliance-optional).

## Review Communication Compliance audit data

In some instances, you must provide information to regulatory or compliance auditors to prove that user activities and communications are scoped. This information might be a summary of all activities associated with a defined organizational policy or anytime a Communication Compliance policy changes. Communication Compliance policies have built-in audit trails for complete readiness for internal or external audits. Your communication policies capture detailed audit histories of every create, edit, and delete action to provide proof of scoped procedures.

Important

You must enable auditing for your organization before Communication Compliance events are recorded. To enable auditing, see [Step 2: Enable the audit log in Communication Compliance configuration](communication-compliance-configure#step-2-required-enable-the-audit-log). When activities trigger events that the Microsoft 365 Audit log captures, it can take up to 48 hours before you can view these events in Communication Compliance policies.

To view Communication Compliance policy update activities, select the **Export policy updates** control on the main page for any policy. You must be assigned the *Global Admin* or *Communication Compliance Admins* roles to export update activities. This action generates an audit file in the .CSV format that contains the following information:

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

| Field | Details |
| --- | --- |
| **AuditData** | Main data source for all policy update activities. All update activities are recorded and separated by comma delimiters. |
| **CreationDate** | Date the update activity was performed in a policy. |
| **Operations** | Update operations performed on the policy. |
| **UserIds** | User that performed the update activity in a policy. |

To view Communication Compliance review activities for a policy, select the **Export review activities** control on the **Overview** page for a specific policy. You must be assigned the *Global Admin* or *Communication Compliance Admins* roles to export review activities. This action generates an audit file in the .CSV format that contains the following information:

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

| Field | Details |
| --- | --- |
| **AuditData** | Main data source for all policy review activities. All review activities are recorded and separated by comma delimiters. |
| **CreationDate** | Date the review activity was performed in a policy. |
| **Operations** | Review operations performed on the policy. |
| **UserIds** | User that performed the review activity in a policy. |

You can also view audit activities in the unified audit log or with the [Search-UnifiedAuditLog](/en-us/powershell/module/exchange/search-unifiedauditlog) PowerShell cmdlet. To learn more about audit log retention policies, see [Manage audit log retention policies](audit-log-retention-policies).

For example, the following command searches the unified audit log for all scoped review activities (policies and rules):

```PowerShell
Search-UnifiedAuditLog -StartDate $startDate -EndDate $endDate -RecordType AeD -Operations SupervisoryReviewTag
```

To audit when Communication Compliance policies are created, updated, or deleted, run the following command:

```PowerShell
Search-UnifiedAuditLog -StartDate $startDate -EndDate $endDate -RecordType Discovery -Operations SupervisionPolicyCreated,SupervisionPolicyUpdated,SupervisionPolicyDeleted
```

To review events where content matched your current Communication Compliance policy rules, search the audit log with the following command:

```PowerShell
Search-UnifiedAuditLog -StartDate $startDate -EndDate $endDate -Operations SupervisionRuleMatch
```

Communication Compliance policy matches are stored in a scoped mailbox for each policy. In some cases, you might need to check the size of your scoped mailbox for a policy to make sure you aren't approaching the current 100-GB storage size or 1 million message limit. If you reach the mailbox limit, the system doesn't capture policy matches and you need to create a new policy (with the same settings) to continue to capture matches for the same activities.

To check the size of a scoped mailbox for a policy, complete the following steps:

1. [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).
2. Run the following command:

    ```PowerShell
    ForEach ($p in Get-SupervisoryReviewPolicyV2 | Sort-Object Name)
    {
       "<Name of your Communication Compliance policy>: " + $p.Name
       Get-MailboxStatistics $p.ReviewMailbox | ft ItemCount,TotalItemSize
    }
    ```