---
layout: Conceptual
title: Search the audit log for events in Microsoft Teams | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/audit-teams-audit-log-events
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to retrieve and analyze Microsoft Teams activity data using the audit log in the Microsoft Purview portal. Follow step-by-step instructions to get started.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.topic: article
audience: Admin
ms.service: purview
ms.subservice: purview-audit
ms.collection:
- purview-compliance
- M365-collaboration
- audit
f1.keywords:
- NOCSH
ms.reviewer: anwara
ms.date: 2026-03-30T00:00:00.0000000Z
search.appverid: MET150
ai-usage: ai-assisted
locale: en-us
document_id: b867485c-019b-b051-1103-708a5b1c261b
document_version_independent_id: b867485c-019b-b051-1103-708a5b1c261b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/audit-teams-audit-log-events.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-teams-audit-log-events
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/audit-teams-audit-log-events.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: 93e0d86b-e93a-694c-b77e-003725ee44b8
---

# Search the audit log for events in Microsoft Teams | Microsoft Learn

Important

The Microsoft Teams admin center is gradually replacing the Skype for Business admin center, and Microsoft is migrating Teams settings to it from the Microsoft 365 admin center. If a setting has been migrated, you'll see a notification and then be directed to the setting's location in the Teams admin center. For more information, see [Manage Teams during the transition to the Teams admin center](/en-us/microsoftteams/manage-teams-skypeforbusiness-admin-center).

The audit log helps you investigate specific activities across Microsoft services. For Microsoft Teams, the audit log tracks activities such as:

- Team creation
- Team deletion
- Added channel
- Deleted channel
- Changed channel setting

For a complete list of Teams activities that are audited, see [Teams activities in the audit log](audit-log-activities).

Note

Audit events from private channels are also logged as they are for teams and standard channels.

## Turn on auditing in Teams

Before you can view audit data, you need to turn on auditing in the Microsoft Purview portal. For more information, see [Turn auditing on or off](audit-log-enable-disable).

Important

Audit data is only available from the point at which you turn on auditing.

## Retrieve Teams data from the audit log

To retrieve audit logs for Teams activities, use the Microsoft Purview portal. For step-by-step instructions, see [Search the audit log](audit-search).

Important

Audit data is only visible in the audit log if auditing is turned on.

The length of time that an audit record is retained and searchable in the audit log depends on your Microsoft 365 or Office 365 subscription, and specifically the type of license assigned to users. For more information, see the [Security & Compliance Center service description](/en-us/office365/servicedescriptions/office-365-platform-service-description/office-365-securitycompliance-center?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

## Search the audit log effectively

Use the following tips when searching for Teams activities in the audit log.

- Select specific activities to search for by selecting the checkbox next to one or more activities. To cancel the selection, select the activity. Use the search box to display the activities that contain the keyword that you type.
- Select **Show results for all activities** in the **Activities** list to display events for activities run using cmdlets. If you know the name of the operation for these activities, type it in the search box to display the activity, then select it.
- Select **Clear all** to clear the current search criteria. The date range returns to the default of the last seven days.
- If 5,000 results are found, you can probably assume that there are more than 5,000 events that met the search criteria. Refine the search criteria and rerun the search to return fewer results, or export all the search results by selecting **Export** &gt; **Download all results**. For step-by-step instructions to export audit logs, see [Search the audit log](audit-search).

For more information about using audit log search, see [How to do an audit log search for Teams](https://www.youtube.com/embed/UBxaRySAxyE).

## Teams activities

For a list of all events that are logged for user and admin activities in Teams in the Microsoft 365 audit log, see:

- [Teams activities in the audit log](audit-log-activities#teams-activities)
- [Shifts app in Teams activities in the audit log](audit-log-activities#teams-shifts-activities)
- [Updates app in Teams activities in the audit log](audit-log-activities#teams-updates-activities)

## Office 365 Management Activity API

You can use the Office 365 Management Activity API to get information about Teams events. For more information about the Management Activity API schema for Teams, see [Teams schema](/en-us/office/office-365-management-api/office-365-management-activity-api-schema#microsoft-teams-schema).

## Attribution in Teams audit logs

When you change membership in Teams (such as adding or deleting users) through Microsoft Entra ID, Microsoft 365 admin portal, or Microsoft 365 Groups Graph API, Teams audit messages and the General channel show an existing owner of the team as the initiator, not the actual initiator of the action. In these scenarios, check Microsoft Entra ID or [Microsoft 365 Group audit logs](audit-search) to see the relevant information.

## Use Defender for Cloud Apps to set activity policies

By using [Microsoft Defender for Cloud Apps](/en-us/cloud-app-security/what-is-cloud-app-security) integration, you can set [activity policies](/en-us/cloud-app-security/user-activity-policies) to enforce a wide range of automated processes by using the app provider's APIs. With these policies, you can monitor specific activities carried out by various users or follow unexpectedly high rates of one certain type of activity.

After you set an activity detection policy, it starts to generate alerts. Alerts only happen for activities that occur after you create the policy. Here are some example scenarios for how you can use activity policies in Defender for Cloud Apps to monitor Teams activities.

### External user scenario

From a business perspective, you might want to keep an eye on the addition of external users to your Teams environment. If you enable external users, monitoring their presence is a good idea. You can use [Defender for Cloud Apps](/en-us/cloud-app-security/what-is-cloud-app-security) to identify potential threats.

![Policy to monitor adding external users](media/teamsexternaluseraddpolicy.png)

The screenshot of this policy to monitor adding external users shows you how to name the policy, set the severity according to your business needs, set it as (in this case) a single activity, and then establish the parameters that specifically monitor only the addition of noninternal users and limit this activity to Teams.

You can view the results from this policy in the activity log:

![Events triggered by external users policy](media/teamsexternaluserlist.png)

Here you can review matches to the policy you set, make any adjustments as needed, or export the results to use elsewhere.

### Mass delete scenario

As mentioned earlier, you can monitor deletion scenarios. You can create a policy that monitors mass deletion of Teams sites. In this example, you set up an alert-based policy to detect mass deletion of teams within 30 minutes.

![Policy showing the setting up of a policy for mass team deletion detection](media/teamsmassdeletepolicy.png)

As the screenshot shows, you can set many different parameters for this policy to monitor Teams deletions, including severity, single or repeated action, and parameters limiting this to Teams and site deletion. You can set these parameters independently of a template, or you can use a template, depending on your organizational needs.

After you create a policy that works for your business, you can review the results in the activity log as events are triggered:

![Screenshot of events triggered by mass deletions](media/teamsmassdeletelist.png)

You can filter down to the policy you set to see the results. If the results you get in the activity log aren't satisfactory (maybe you see lots of results, or nothing at all), you can fine-tune the query to make it more relevant to what you need.

### Alert and governance scenario

You can set alerts and send emails to admins and other users when an activity policy is triggered. You can set automated governance actions such as suspending a user or requiring a user to sign in again. This example shows how a user account can be suspended when an activity policy is triggered and determines a user deleted two or more teams in 30 minutes.

![Screenshot of alerts and governance actions for an activity policy.](media/audit-log-governance.png)

## Use Defender for Cloud Apps to set anomaly detection policies

[Anomaly detection policies](/en-us/cloud-app-security/anomaly-detection-policy) in Defender for Cloud Apps provide out-of-the-box user and entity behavioral analytics (UEBA) and machine learning (ML) so that you can immediately run advanced threat detection across your cloud environment. Because they're automatically enabled, the new anomaly detection policies provide immediate results by providing immediate detections, targeting numerous behavioral anomalies across your users and the machines and devices connected to your network. Additionally, the new policies expose more data from the Defender for Cloud Apps detection engine, to help you speed up the investigation process and contain ongoing threats.

Teams events integration into anomaly detection policies is currently in development. You can set up anomaly detection policies for other Microsoft 365 products and take action on users who match those policies.