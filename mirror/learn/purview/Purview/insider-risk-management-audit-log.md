---
layout: Conceptual
title: Review activities with the Insider Risk Management audit log | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-audit-log
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about the Insider Risk Management audit log in Microsoft Purview
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: article
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-02-18T00:00:00.0000000Z
audience: itpro
ms.collection:
- purview-compliance
ms.custom: sfi-image-nochange
locale: en-us
document_id: 9374b65d-927f-64ee-2600-a8551f333895
document_version_independent_id: 9374b65d-927f-64ee-2600-a8551f333895
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-audit-log.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-audit-log
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-audit-log.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: c0b8556d-6bf1-4f46-a540-4e7ac5fb5d2d
---

# Review activities with the Insider Risk Management audit log | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

The Insider Risk Management audit log helps you stay informed about actions taken on Insider Risk Management features. By using this audit log, you can independently review the actions of users assigned to one or more Insider Risk Management role groups. Your organization automatically enables the Insider Risk Management audit log and you can't disable it.

Note

When you turn content download on within a case, during or after case creation, a system-generated audit log for 'accessing files stored in SharePoint' may appear.

![Insider Risk Management audit log.](media/insider-risk-audit-log.png)

The audit log automatically and immediately updates whenever it detects identified risk activities. The audit log keeps information for 180 days (about six months). After 180 days, the log permanently deletes data.

Areas in identified risk activity detection include:

- Policies
- Cases
- Alerts
- Settings
- Users
- Notice templates

To view and export data from the audit log, assign users to the *Insider Risk Management* or *Insider Risk Management Auditors* role groups. For more information about Insider Risk Management role groups, see [Assign Insider Risk Management permissions](insider-risk-management-permissions).

Note

The Insider Risk Management audit log isn't associated with the Microsoft 365 audit log. They're independent auditing systems that capture information on separate areas. Disabling Microsoft 365 auditing doesn't impact activity auditing within Insider Risk Management.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## View activity in the insider risk audit log

To view feature activity detected for Insider Risk Management, go to the **Insider risk audit log** link in the top-right area of any Insider Risk Management tab. By default, you see the following information displayed for Insider Risk Management activities:

- **Activity:** A description of the identified risk activity taken within the Insider Risk Management solution by a user.
- **Category:** The area or item where the identified risk activity was performed. For example, you see *Policies* as the category when policy change activities were performed.
- **Activity performed by:** The user name of the user that performed the identified risk activity.
- **Date:** The date and time the identified risk activity was performed. The date and time are the local date and time for your organization.

For more information about a logged activity, select the activity to display the activity details pane. This pane includes additional information about the identified risk activity.

## Columns and filtering

To make it easier for auditors to review audit logs, the **Insider risk audit log** supports filtering. For basic filtering, queue columns are available to add to the view to provide different pivots on the files and messages. You can filter identified risk activities by the **Category, Date range,** and **Activity performed by** fields.

To add or remove column headings for the queue, use the **Customize columns** control and select from the column options. These columns map to common conditions supported in the **Insider risk audit log** and are listed later in this article.

## Audit log export

Users assigned to the *Insider Risk Management* or *Insider Risk Management Auditors* role groups can export audit log activity to a .csv (comma-separated values) file by selecting **Export** on the **Insider risk audit log** page. Depending on the audit log activity, some fields might not be included in the filtered queue, and those fields appear as blank in the exported file.

The file contains audit log activity information for the following fields:

- **Activity performed by:** Name of the user modifying an item value. Users listed here are assigned to one or more of the following [Insider Risk Management role groups](insider-risk-management-permissions): *Insider Risk Management*, *Insider Risk Management Admins*, *Insider Risk Management Analysts*, *Insider Risk Management Investigators*. Each role group has different permission levels for managing insider risk features.
- **Activity:** Type of activity taken on an item. Values are *Viewed, Deleted, Added, Edited policy, Case, User, Alert,* and *Settings.*
- **Added**: Objects you add during the identified risk activity, such as users, file types, or domains.
- **Alert volume**: Level of alert volume defined in Insider Risk Management settings.
- **Amount**: Currently selected custom indicator amounts for a policy.
- **Asset ID**: Asset ID of the priority physical asset the activity was performed on.
- **Category:** Category of the item modified. Values are *Policies, Cases, Users, Alerts, Settings,* and *Notice templates.*
- **Date:** Date and time, listed in your organization's local date and time.
- **Description**: Description input by the user for the object being acted on (such as a policy or a priority user group).
- **DLP policy**: The Microsoft Purview Data Loss Prevention (DLP) policy selected to trigger inclusion in an Insider Risk Management policy.
- **Indicator**: Indicator in the within insider risk settings that the activity was performed on (such as adding or removing an indicator).
- **Notice template**: Notice template that the identified risk activity was performed on.
- **Number of days**: Policy activation window defined in insider risk settings.
- **Number of files**: File volume limit defined in Insider Risk Management settings.
- **Policy template**: Policy template that the indicators acted on belongs to.
- **Previous amount**: Previously selected custom indicator amounts for a policy.
- **Priority user group**: Priority user group the identified risk activity was performed on.
- **Removed**: Objects you remove during the identified risk activity, such as users, file types, or domains.
- **Sender**: Sender field of the notice template the identified risk activity was performed on.
- **Target policy**: The policy the identified risk activity was performed on (such as adding a user to or removing a user from).
- **Template message body**: The message body of the notice template the identified risk activity was performed on.
- **Template subject**: The subject field of the notice template the identified risk activity was performed on.
- **User:** User the identified risk activity was performed on.