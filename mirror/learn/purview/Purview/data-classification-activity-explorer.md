---
layout: Conceptual
title: Get started with Activity explorer | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-07-22T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1017
audience: Admin
ms.topic: get-started
ms.service: purview
ms.collection:
- tier1
- purview-compliance
- m365solution-mip
- m365initiative-compliance
- highpri
search.appverid:
- MOE150
- MET150
description: Activity explorer lets you see and filter on the actions users are taking on your labeled content.
locale: en-us
document_id: 1f6fe4d9-148d-9cad-6929-02e456a35119
document_version_independent_id: 1f6fe4d9-148d-9cad-6929-02e456a35119
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-classification-activity-explorer.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-classification-activity-explorer
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-classification-activity-explorer.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: eb407a3f-714f-d16b-5db5-89c569bfb0ba
---

# Get started with Activity explorer | Microsoft Learn

[Activity explorer](https://purview.microsoft.com/informationprotection/dataclassification/activityexplorer) lets you monitor what's being done with your labeled content. Activity explorer provides a historical view of activities on your labeled content. The activity information comes from the Microsoft 365 unified audit logs. It's transformed and then made available in the activity explorer UI. Activity explorer reports on up to 30 days worth of data.

Activity explorer gives you multiple ways to sort and view the data.

## When activities appear

Activity explorer isn't a real-time view. Because its data comes from the Microsoft 365 unified audit log, activities appear on the same schedule as audit records — not the moment they occur.

- For core services (Exchange, SharePoint, OneDrive, and Teams), allow 60 to 90 minutes after an activity for it to appear in activity explorer. Other services can take longer, and Microsoft doesn't guarantee a specific time for an activity to become available. For more information, see [Search the audit log](audit-search#before-you-search-the-audit-log).
- After you enable or change a policy, allow time for the policy to reach the workload *and* for the resulting activities to flow in. An empty view right after you turn on a policy usually means the data pipeline hasn't caught up yet, not that the policy failed.
- Devices report endpoint activities only while they're online. An offline device backfills its activities after it reconnects.

Note

If a recent activity isn't showing yet, confirm that it falls within the 30 days of data that activity explorer reports on, and allow the audit-log availability time described earlier before you treat a missing activity as a defect. To confirm an activity independently, search for it in [Audit](audit-search).

## Filters

Filters are the building blocks of activity explorer. Each filter focuses on a different dimension of the collected data. You can use about 50 different individual filters, including:

- Date range
- Activity type
- Location
- Sensitivity label
- User
- Client IP
- Device name
- Is protected

To see all the filters, open the filter pane in activity explorer and look at the dropdown list.

Note

Filter options are generated based on the first 500 records to ensure optimal performance. This limitation might cause some values to not appear in the filter dropdown. For endpoint events, only the most restrictive DLP rule appears. Filters you apply in activity explorer also operate based on this most restrictive rule.

## Filter sets

Activity explorer comes with predefined sets of filters to help save time when you want to focus on a specific activity. Use filter sets to quickly provide you with a view of higher level activities than individual filters do. Some of the predefined filter sets are:

- Endpoint DLP activities
- Sensitivity labels applied, changed, or removed
- Egress activities
- DLP policies that detected activities
- Network DLP activities
- Protected Browser

You can also create and save your own filter sets by combining individual filters.

## Microsoft Security Copilot in activity explorer (preview)

In *preview*, [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview) is embedded in activity explorer. It can help efficiently drill down into Activity data and help you identify activities, files with sensitive info, users, and other details that are relevant to an investigation.

Important

Be sure to check the responses from Security Copilot for accuracy and completeness before taking any action based on the information provided. You can provide feedback to help improve the accuracy of the responses.

### Data hunting

Security Copilot skills use all the data available to Microsoft Purview, filters, and filter sets available in activity explorer and use machine learning to provide you with insights into the activity (sometimes referred to as *data hunting*) on your data that is most important to you.

- **Show me the top 5 activities from the past week**
- **Filter and investigate activities**
- **Find files used in specific activities**

Selecting a prompt automatically opens the Security Copilot side card and shows you the results of the query. You can then further refine the query.

### Natural language to filter set generation

Use the prompt box to enter complex natural language queries to generate filter sets. For example, you can enter:

`Filter and investigate files copied to cloud with sensitive info type credit card number for past 30 days.`

Security Copilot generates a filter set for your query. Review the filter to make sure it fits your needs, then apply it to the data.

## Prerequisites

### SKU/subscriptions licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

### Permissions

An account must be explicitly assigned membership in any one of these role groups, or must be explicitly granted the role.

### Roles and role groups

Use roles and role groups to fine-tune your access controls. For more information, see [Permissions in the Microsoft Purview portal](purview-permissions).

#### Microsoft Purview roles

- Information Protection Admin
- Information Protection Analyst
- Information Protection Investigator
- Information Protection Reader (along with Information Protection Admin)

#### Microsoft Purview role groups

- Information Protection
- Information Protection Investigators
- Information Protection Analysts
- Information Protection Admins & Information Protection Readers (both role groups needs to be assigned)

#### Microsoft 365 roles

- Compliance Admins
- Security Admins
- Compliance Data Admins

#### Microsoft 365 role groups

- Compliance Administrator
- Security Administrator
- Security Reader

## Activity types

Activity explorer gathers information from the audit logs of multiple sources of activities.

Some examples of the **Sensitivity label activities** and **Retention labeling activities** from applications native to Microsoft Office, the Microsoft Purview Information Protection client and scanner, SharePoint, Exchange (sensitivity labels only), and OneDrive include:

- Label applied
- Label changed (upgraded, downgraded, or removed)
- Auto-labeling simulation
- File read

For the current list of activities listed in Activity explorer, go into Activity explorer and open the activity filter. The list of activities is available in the dropdown list.

Labeling activity specific to the Microsoft Purview Information Protection client and scanner that comes into Activity explorer includes:

- Protection applied
- Protection changed
- Protection removed
- Files discovered

For more detailed information on what labeling activity makes it into Activity explorer, see [Labeling events available in Activity explorer](data-classification-activity-explorer-available-events).

Additionally, Activity Explorer gathers DLP policy match events from Microsoft 365 workloads such as Exchange, SharePoint, OneDrive, Teams chat and channels, and on-premises SharePoint folders, libraries, and file shares. When you enable Endpoint data loss prevention (DLP), Activity Explorer also includes device-level activities from onboarded Windows 10, Windows 11, and the three most recent major macOS versions.

### Enhanced matched conditions for Exchange DLP events (preview)

For Exchange Online DLP events, Activity Explorer surfaces enhanced matched condition details for non-sensitive information type (SIT) conditions in addition to SIT matches. Every non-SIT condition that contributed to a DLP policy match is displayed with three levels of detail:

- **Condition name**: The specific policy condition that was matched, for example, *Sender domain is* or *Attachment's file extension is*.
- **Matched value**: The actual value that triggered the condition match, for example, `contoso.com` or `.docx`.
- **Source**: The part of the message where the match was found, for example, the message header, envelope, or attachment.

Enhanced matched condition details appear on the event detail flyout for Exchange DLP events in Activity Explorer and the [DLP Alerts dashboard](dlp-alerts-dashboard-get-started#view-other-matched-conditions-in-dlp-events). The following condition categories are supported:

- **Sender conditions**: Sender is, Sender domain is, Sender address contains words, Sender address matches patterns, Sender is a member of, Sender IP address is, Sender AD attribute
- **Recipient conditions**: Recipient is, Recipient domain is, Recipient address contains words, Recipient address matches patterns, Recipient is a member of, Recipient AD attribute
- **Attachment conditions**: Attachment's file extension is, Document name contains words, Document name matches patterns, Document property is, Document size equals or is greater than, Document is password protected, Document could not be scanned, Document didn't complete scanning
- **Content conditions**: Content character set contains words, Content is shared from M365, Content is received from
- **Header conditions**: Header contains words, Header matches patterns
- **Message property conditions**: Message size over, Message type is, Message importance is, Subject contains words, Subject matches patterns, Subject or body contains words, Subject or body matches patterns, Has sender overridden the policy tip

For the full reference of Exchange DLP conditions, see [Data loss prevention Exchange conditions and actions reference](dlp-exchange-conditions-and-actions).

Some example events gathered from devices include the following actions taken on files:

- Deletion
- Creation
- Copy to clipboard
- Modify
- Read
- Print
- Rename
- Copy to network share
- Access by an unallowed app

Understanding the actions that are taken on content with sensitivity labels helps you determine whether the controls that you have in place, such as [Microsoft Purview Data Loss Prevention](dlp-learn-about-dlp) policies, are effective. If not, or if you discover something unexpected (such as a large number of items labeled `highly confidential` that are downgraded to `general`), you can manage your policies and take new actions to restrict the undesired behavior.

Note

- Activity explorer doesn't monitor retention activities for Exchange.
- Legacy Azure Information Protection (AIP) labels are not supported; as a result, they may appear as GUIDs in Activity Explorer.

Note

If a user reports the Teams DLP verdict as a false positive, the activity shows as **DLP info** in the list on Activity explorer. The entry doesn't have any rule and policy match details but shows synthetic values. There's also no incident report generated for false positive reporting.

### Activity type events and alerts

This table shows the events that Activity Explorer triggers for three sample policy configurations. The events depend on whether a policy match is detected.

| Policy configuration | Activity Explorer event triggered for this action type | Activity Explorer event triggered when a DLP rule is matched | Activity Explorer alert triggered |
| --- | --- | --- | --- |
| Policy contains a single rule allowing the activity without auditing it. | Yes | No | No |
| Policy contains two rules: Matches for Rule #1 are allowed; policy matches for Rule #2 are audited. | Yes  (Rule #2 only) | Yes  (Rule #2 only) | Yes  (Rule #2 only) |
| Policy contains two rules: Matches for both rules are allowed and not audited. | Yes | No | No |