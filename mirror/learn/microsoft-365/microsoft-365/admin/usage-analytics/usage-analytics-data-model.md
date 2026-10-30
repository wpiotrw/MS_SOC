---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Microsoft 365 Usage Analytics Data Model - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/usage-analytics/usage-analytics-data-model?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: dansimp
author: Dansimp
manager: dansimp
ms.date: 2026-03-12T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: m365-core
ms.subservice: activity-reports
ms.localizationpriority: medium
ms.collection:
- Tier2
- scotvorg
- M365-subscription-management
- Adm_O365
- Adm_TOC
- SPO_Content
- operations-pod
ms.custom: AdminSurgePortfolio
search.appverid:
- BCS160
- MET150
- MOE150
ms.assetid: 08c5307c-4a6b-4761-8410-a6c96725760f
description: Learn how Microsoft 365 usage analytics connects to an API and provides monthly usage trends across services. Explore data tables to track adoption and activity.
locale: en-us
document_id: de44679b-998b-3de8-292b-d2993af9bad9
document_version_independent_id: 7fd9ecf7-0468-d01e-dcca-d18a19ebb7c2
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/usage-analytics/usage-analytics-data-model.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/usage-analytics/usage-analytics-data-model
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/usage-analytics/usage-analytics-data-model.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e4f48d48-dfb7-4973-a019-e504674667cb
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/495840e0-c52f-49d2-a584-185aefeb98c7
platformId: 82926e99-29da-194e-a0ba-14c9dc3a2167
---

# Microsoft 365 Usage Analytics Data Model - Microsoft 365 admin | Microsoft Learn

## Data for the Microsoft 365 usage analytics tables

The Microsoft 365 usage analytics data model connects to an API that exposes multidimensional data about service usage and adoption. The APIs that Microsoft 365 usage analytics uses to generate its data come from various generally available Graph APIs. The Microsoft 365 usage analytics API itself isn't generally available.

Note

For more information, see [Working with Microsoft 365 usage reports in Microsoft Graph](/en-us/graph/api/resources/report).

This API provides information about the monthly trend of usage of the various Microsoft 365 services. For the exact data returned by the API, see the table in the following section.

## Data tables returned by the Microsoft 365 reporting API

| **Table name** | **Information in the table** | **Date range** |
| --- | --- | --- |
| **Tenant Product Usage** | Monthly totals of:<br>- Enabled users.<br>- Active users.<br>- Month-over-month retained users.<br>- First-time users.<br>- Cumulative active users. | Monthly aggregated data for a rolling 12-month period, including the current partial month. |
| **Tenant Product Activity** | Monthly totals of activities and active user counts for product activities.For more information about the activities returned in this table, see [Active user in Microsoft 365 usage reports](active-user-in-usage-reports). | Monthly aggregated data for a rolling 12-month period, including the current partial month. |
| **Tenant Office Licenses** | Number of Microsoft Office subscriptions assigned to users. | End-of-month state data for a rolling 12-month period, including the current partial month. |
| **Tenant Mailbox Usage** | Mailbox data, including:<br>- Total mailbox count.<br>- Storage usage. | End-of-month state data for a rolling 12-month period, including the current partial month. |
| **Tenant Client Usage** | Number of users actively using specific clients or devices to connect to:<br>- Exchange Online.<br>- Teams.<br>- Viva Engage. | Monthly aggregated data for a rolling 12-month period, including the current partial month. |
| **Tenant SharePoint Usage** | SharePoint site data, including:<br>- Total sites (Teams or Groups sites).<br>- Number of documents.<br>- File count by activity type.<br>- Storage used. | End-of-month state data for a rolling 12-month period, including the current partial month. |
| **Tenant OneDrive Usage** | OneDrive account data, including:<br>- Number of accounts.<br>- Number of documents across OneDrives.<br>- Storage used.<br>- File count by activity type. | End-of-month state data for a rolling 12-month period, including the current partial month. |
| **Tenant Microsoft 365 Groups Usage** | Microsoft 365 Groups usage data, including:<br>- Mailbox.<br>- SharePoint.<br>- Viva Engage. | End-of-month state data for a rolling 12-month period, including the current partial month. |
| **Tenant Office Activation** | Office subscription activation data, including:<br>- Total activations.<br>- Activations per device (Android, iOS, Mac, PC).<br>- Activations by service plan (for example, Microsoft 365 Apps for enterprise, Visio, Project). | End-of-month state data for a rolling 12-month period, including the current partial month. |
| **User State** | User metadata, including:<br>- Display name.<br>- Assigned products.<br>- Location.<br>- Department.<br>- Title.<br>- Company.<br><br>Includes users who were assigned a license during the last complete month. Each user has a unique user ID. | Users who had a license assigned during the last complete month. |
| **User Activity** | Per-user activity data for licensed users.For more information about the activities returned in this table, see [Active user in Microsoft 365 usage reports](active-user-in-usage-reports). | Users who performed an activity in any service during the last complete month. |

To see the detailed information for each data table, see the following sections.

### Data table - User State

The **User State** table provides user-level details for all users who have a license assigned during the last complete month. It brings in data from Microsoft Entra ID.

| **Name** | **Description** |
| --- | --- |
| **UserId** | Unique user ID that represents a user and enables joining with other data tables within the data set. |
| **Timeframe** | Month value for which this table has data. |
| **UPN** | User principal name (UPN) that uniquely identifies the user to join with other external data sources. |
| **DisplayName** | User's display name. |
| **IDType** | Account user used to sign in. Values can be: <br>- 1 if the user is a Viva Engage user who connects using their Viva Engage ID.<br>- 0 if the user connects to Viva Engage using their Microsoft 365 ID. |
| **HasLicenseEXO** | Set to true if the user is assigned a license and enabled to use Exchange on the last day of the month. |
| **HasLicenseODB** | Set to true if the user is assigned a license and enabled to use OneDrive on the last day of the month. |
| **HasLicenseSPO** | Set to true if the user is assigned a license and enabled to use SharePoint on the last day of the month. |
| **HasLicenseYAM** | Set to true if the user is assigned a license and enabled to use Viva Engage on the last day of the month. |
| **HasLicenseSFB** | Set to true if the user is assigned a license and enabled to use Teams on the last day of the month. |
| **HasLicenseTeams** | Set to true if the user is assigned a license and enabled to use Microsoft Teams on the last day of the month. |
| **Company** | Company data represented in Microsoft Entra ID for this user. |
| **Department** | Department data represented in Microsoft Entra ID for this user. |
| **LocationCity** | City data represented in Microsoft Entra ID for this user. |
| **LocationCountry** | Country/region data represented in Microsoft Entra ID for this user. |
| **LocationState** | State data represented in Microsoft Entra ID for this user. |
| **LocationOffice** | User's office. |
| **Title** | Title data represented in Microsoft Entra ID for this user. |
| **Deleted** | True if the user was deleted from Microsoft 365 in the last complete month. |
| **DeletedDate** | Date when the user was deleted from Microsoft 365. |
| **YAM\_State** | State of the user in the Viva Engage system. Values can be: <br>- Active.<br>- Deleted.<br>- Suspended. |
| **YAM\_ActivationDate** | Date the user entered the state of being active in Viva Engage. |
| **YAM\_DeletionDate** | Date the user entered the state of being deleted in Viva Engage. |
| **YAM\_SuspensionDate** | Date the user entered the state of being suspended in Viva Engage. |

### Data table - User Activity

The **User Activity** table contains data about each user who had an activity in any of the services in the previous month.

| **Name** | **Description** |
| --- | --- |
| **UserID** | Unique user ID that represents a user and enables joining with other data tables within the data set. |
| **Timeframe** | Month value for which this table represents data. |
| **EXO\_EmailSent** | Number of emails sent. |
| **EXO\_EmailReceived** | Number of emails received. |
| **EXO\_EmailRead** | Number of email read activities performed by the user. Includes:<br>- Multiple reads of the same email.<br>- Emails received in previous periods. |
| **EXO\_AppointmentCreated** | Number of appointments created. |
| **EXO\_MeetingAccepted** | Number of meetings accepted. |
| **EXO\_MeetingCancelled** | Number of meetings canceled. |
| **EXO\_MeetingDeclined** | Number of meetings declined. |
| **EXO\_MeetingSent** | Number of meetings sent. |
| **ODB\_FileViewedModified** | Number of files the user interacted with on any OneDrive. Includes the following actions:<br>- Create.<br>- Update.<br>- Delete.<br>- View.<br>- Download. |
| **ODB\_FileSynched** | Number of files the user synchronized on any OneDrive. |
| **ODB\_FileSharedInternally** | Number of files shared internally from any OneDrive including sharing with users within groups. |
| **ODB\_FileSharedExternally** | Number of files the user shared externally from any OneDrive. |
| **ODB\_AccessedByOwner** | Number of OneDrive sites the user interacted with that they own. |
| **ODB\_AccessedByOthers** | Number of OneDrive sites owned by another user that the user interacted with. |
| **SPO\_GroupFileViewedModified** | Number of files the user interacted with on any group site. |
| **SPO\_GroupFileSynched** | Number of files the user synchronized on any group site. |
| **SPO\_GroupFileSharedInternally** | Number of files shared internally from any group site including sharing within groups. |
| **SPO\_GroupFileSharedExternally** | Number of files the user shared externally from any group site. |
| **SPO\_GroupAccessedByOwner** | Number of group sites the user interacted with that they own. |
| **SPO\_GroupAccessedByOthers** | Number of group sites owned by another user that the user interacted with. |
| **SPO\_OtherFileViewedModified** | Number of files the user interacted with on any other site. |
| **SPO\_OtherFileSynched** | Number of files the user synchronized from any other site. |
| **SPO\_OtherFileSharedInternally** | Number of files shared internally from any other site including sharing within groups. |
| **SPO\_OtherFileSharedExternally** | Number of files the user shared externally from any other site. |
| **SPO\_OtherAccessedByOwner** | Number of other sites the user interacted with that they own. |
| **SPO\_OtherAccessedByOthers** | Number of other sites owned by another user that the user interacted with. |
| **SPO\_TeamFileViewedModified** | Number of files the user interacted with on any team site. |
| **SPO\_TeamFileSynched** | Number of files the user synchronized from any team site. |
| **SPO\_TeamFileSharedInternally** | Number of files shared internally from any team site including sharing within groups. |
| **SPO\_TeamFileSharedExternally** | Number of files the user shared externally from any team site. |
| **SPO\_TeamAccessedByOwner** | Number of team sites the user interacted with that they own. |
| **SPO\_TeamAccessedByOthers** | Number of team sites owned by another user that the user interacted with. |
| **Teams\_ChatMessages** | Number of chat messages sent. |
| **Teams\_ChannelMessage** | Number of messages posted to channels. |
| **Teams\_CallParticipate** | Number of calls the user participated in. |
| **Teams\_MeetingParticipate** | Number of meetings the user joined. |
| **Teams\_HasOtherAction** | Boolean value indicating whether the user performed other actions in Microsoft Teams. The user is considered active but has a zero value for the following items: <br>- Chat Messages.<br>- 1:1 calls.<br>- Channel Messages.<br>- Total Meetings.<br>- Meetings organized. |
| **YAM\_MessagePost** | Number of Viva Engage messages the user posted. |
| **YAM\_MessageLiked** | Number of Viva Engage messages the user liked. |
| **YAM\_MessageRead** | Number of Viva Engage messages the user read. |
| **SFB\_P2PSummary** | Number of peer-to-peer sessions the user took part in. |
| **SFB\_ConfOrgSummary** | Number of conference sessions the user organized. |
| **SFB\_ConfPartSummary** | Number of conference sessions the user participated in. |

### Data table - Tenant Product Usage

The **Tenant Product Usage** table provides month-over-month adoption data in terms of the following types of user for each product within Microsoft 365:

- Enabled.
- Active.
- Returning
- First-time users.

The Microsoft 365 values represent active usage in any of the products.

| **Name** | **Description** |
| --- | --- |
| **Product** | Name of products for which the usage information is summarized.<br>- The Microsoft 365 value represents activity across any of the products. |
| **Timeframe** | Month value.<br>- One row per product per month.<br>- Includes the last 12 months, including the current partial month. |
| **EnabledUsers** | Number of users enabled to use the product for the timeframe value.<br>- Users enabled for any portion of the month are counted. |
| **ActiveUsers** | Number of users who performed an intentional activity in the product for the timeframe value.<br>- A user is counted as active if they performed one of the key product activities.<br>- Key activities are listed in the **Tenant Product Activity** table. |
| **CumulativeActiveUsers** | Number of users enabled to use the product.<br>- Includes users who used the product at least once since data collection started.<br>- Calculated up to and including the timeframe month. |
| **MoMReturningUsers** | Number of users active in the timeframe month.<br>- Users must also be active during the previous month. |
| **FirstTimeUsers** | Number of users who became active in the timeframe month for the first time.<br>- Activity is measured from the start of data collection in the new usage system.<br>- Once a user is counted as a first-time user, the user is never counted again. |
| **Content Date** | If the timeframe is:<br>- The current month, the latest date with available data.<br>- A previous month, the last date of that month. |

### Data table - Tenant Product Activity

The **Tenant Product Activity** table provides monthly totals of activity and active user count for various activities within the products.

| **Name** | **Description** |
| --- | --- |
| **Timeframe** | Month value.<br>- One row per product per month.<br>- Includes the last 12 months, including the current partial month. |
| **Product** | Name of the product within Microsoft 365 for which usage data is available. |
| **Activity** | Name of the activity in a product that is used to showcase active use of the product. |
| **ActivityCount** | Total number of actions counted for each activity across all active users.<br>- For SharePoint and OneDrive activities, this value represents the number of distinct documents users interacted with. |
| **ActiveUserCount** | Number of users who performed the activity within the product. |
| **TotalDurationInMinute** | Total duration, in minutes, across all active users.<br>- Applies to audio or video sessions in applicable Microsoft Teams activities. |
| **Content Date** | If the timeframe is:<br>- The current month, the latest date with available data.<br>- A previous month, the last date of that month. |

### Data table - Tenant Mailbox Usage

The **Tenant Mailbox Usage** table shows summary data for all licensed Exchange Online users with a user mailbox. It shows the end of month state for all user mailboxes. You can't add the data in this table across multiple months. The latest month's data in this table shows the most recent state.

| **Name** | **Description** |
| --- | --- |
| **TotalMailboxes** | Number of user mailboxes for the Microsoft 365 subscription. |
| **IssueWarningQuota** | Total quota for issuing warnings across all user mailboxes. |
| **ProhibitSendQuota** | Total quota for prohibiting send actions across all user mailboxes. |
| **ProhibitSendReceiveQuota** | Total quota for prohibiting send and receive actions across all user mailboxes. |
| **TotalItemBytes** | Amount of storage used across all user mailboxes, in bytes. |
| **MailboxesNoWarning** | Number of user mailboxes that are under the storage warning limit. |
| **MailboxesIssueWarning** | Number of user mailboxes that were issued a storage quota warning. |
| **MailboxesExceedSendQuota** | Number of user mailboxes that exceeded the send quota. |
| **MailboxesExceedSendReceiveQuota** | Number of user mailboxes that exceeded the send and receive quota. |
| **DeletedMailboxes** | Number of user mailboxes deleted in the timeframe. |
| **Timeframe** | Month value. |
| **Content Date** | If the timeframe is:<br>- The current month, the latest date with available data.<br>- A previous month, the last date of that month. |

### Data table - Tenant Client Usage

The **Tenant Client Usage** table provides month-over-month summary data about the clients that users use to connect to:

- Exchange Online.
- Microsoft Teams.
- Viva Engage.

This table doesn't yet have client use data for SharePoint and OneDrive.

| **Name** | **Description** |
| --- | --- |
| **Product** | Name of the product within Microsoft 365 for which client usage data is available. |
| **ClientId** | Name of each device used to connect to the product. |
| **UserCount** | Number of users who used each client for each product. |
| **Timeframe** | Month value. |
| **Content Date** | If the timeframe is:<br>- The current month, the latest date with available data.<br>- A previous month, the last date of that month. |

### Data table - Tenant SharePoint Usage

The **Tenant SharePoint Usage** table shows month-over-month summary data about the usage or activity of SharePoint sites. The data in this table only covers Team Sites and Group sites and represents the end-of-month state of SharePoint sites:

- The values reflect the final totals at the end of the month, not interim activity.
- During the month, users might create, delete, and add files.
- Only the state at the end of the month is recorded.

In the following example, the resulting values shown are seven documents and 5 MB, which represent the end-of-month state:

- A user creates five documents that use 10 MB of storage.
- The user then deletes some files and adds others.
- At the end of the month, the site contains seven documents that use 5 MB of storage.

To avoid duplicate counts of aggregations, this table is hidden. It's used as a source to create two reference tables.

| **Name** | **Description** |
| --- | --- |
| **SiteType** | Site type value. Possible values are:<br>- Any: Represents either team or group sites.<br>- Team.<br>- Group. |
| **TotalSites** | Number of sites that existed at the end of the timeframe. |
| **DocumentCount** | Total number of documents that existed on the site at the end of the timeframe. |
| **DiskUsed** | Total storage used, summed across all sites at the end of the timeframe. |
| **ActivityType** | Number of sites that recorded specific types of file activity. Represents any file activity that was performed. For example:<br>- Any activity.<br>- Active files.<br>- Files shared externally.<br>- Files shared internally.<br>- Files synchronized. |
| **SitesWithOwnerActivities** | Number of active sites where the site owner performed a file activity on their own site.<br>- The site owner is the person responsible for the site.<br>- The site owner can be identified using the PowerShell command `get-sposite`. |
| **SitesWithNonOwnerActivities** | Number of active sites summed up for the month where users other than the site owner performed a file activity.<br>- The site owner is the person responsible for the site.<br>- The site owner can be identified using the PowerShell command `get-sposite`. |
| **ActivityTotalSites** | Number of sites that recorded any activity during the timeframe.<br>- Sites deleted by the end of the timeframe are still counted if they had activity earlier in the timeframe. |
| **Timeframe** | Date value.<br>- Used as a many-to-one relationship with the Calendar table. |
| **Content Date** | If the timeframe is:<br>- The current month, the latest date with available data.<br>- A previous month, the last date of that month. |

### Data table - Tenant OneDrive Usage

The **Tenant OneDrive Usage** table provides data about the OneDrive accounts. For example:

- Number of accounts.
- Number of documents across OneDrive accounts.
- Storage used.
- File count by activity type.

The table also shows the end-of-month state of OneDrive accounts:

- The values reflect the final state at the end of the month, not changes made during the month.
- Users might create, delete, and add files throughout the month.
- Only the end-of-month totals are recorded in this table.

In the following example, the table records seven files and 5 MB, which represent the end-of-month state:

- A user creates five documents that use 10 MB of storage.
- During the month, the user deletes some files and adds others.
- By the end of the month, the account contains seven files that use 5 MB of storage.

| **Name** | **Description** |
| --- | --- |
| **SiteType** | Value is `OneDrive`. |
| **TotalSites** | Number of OneDrive accounts that exist at the end of the timeframe. |
| **DocumentCount** | Total number of documents that exist across all OneDrive accounts at the end of the timeframe. |
| **DiskUsed** | Total storage used, summed across all OneDrive accounts at the end of the timeframe. |
| **ActivityType** | Number of accounts that recorded specific types of file activity. For example:<br>- Any activity.<br>- Active files.<br>- Files shared externally.<br>- Files shared internally.<br>- Files synchronized. |
| **SitesWithOwnerActivities** | Number of active OneDrive accounts where the account owner performed a file activity on their own account. |
| **SitesWithNonOwnerActivities** | Number of OneDrive accounts with file activity by users other than the owner. |
| **ActivityTotalSites** | Number of OneDrive accounts that recorded any activity during the timeframe.<br>- Accounts deleted by the end of the timeframe are still counted if they had activity earlier in the timeframe. |
| **Timeframe** | Date value.<br>- Used as a many-to-one relationship with the Calendar table. |
| **Content Date** | If the timeframe is:<br>- The current month, the latest date with available data.<br>- A previous month, the last date of that month. |

### Data table - Tenant Microsoft 365 Groups Usage

The **Tenant Microsoft 365 Groups Usage** table provides data about how Microsoft 365 Groups is used across the organization.

| **Name** | **Description** |
| --- | --- |
| **TimeFrame** | Month value. There's one row per product per month for the last 12 months, including the current partial month. |
| **GroupType** | Type of group (private, public, or any). |
| **TotalGroups** | Number of groups in each group type. |
| **ActiveGroups** | Number of active groups. |
| **MBX\_TotalGroups** | Number of mailbox groups. |
| **MBX\_ActiveGroups** | Number of active mailbox groups. |
| **MBX\_TotalActivities** | Number of mailbox activities. |
| **MBX\_TotalItems** | Number of mailbox items. |
| **MBX\_StorageUsed** | Quantity of mailbox storage used. |
| **SPO\_TotalGroups** | Number of SharePoint groups. |
| **SPO\_ActiveGroups** | Number of active SharePoint groups. |
| **SPO\_FileAccessedActiveGroups** | Number of SharePoint groups that have file accessed activities. |
| **SPO\_FileSyncedActiveGroups** | Number of SharePoint groups that have file synchronized activities. |
| **SPO\_FileSharedInternallyActiveGroups** | Number of SharePoint groups that shared activities internally, or with groups that might include external users. |
| **SPO\_FileSharedExternallyActiveGroups** | Number of SharePoint groups that shared activities externally. |
| **SPO\_TotalActivities** | Number of SharePoint activities. |
| **SPO\_FileAccessedActivities** | Number of SharePoint file accessed activities. |
| **SPO\_FileSyncedActivities** | Number of SharePoint file synchronized activities. |
| **SPO\_FileSharedInternallyActivities** | Number of SharePoint file shared activities internally, or with groups that might include external members. |
| **SPO\_FileSharedExternallyActivities** | Number of SharePoint file shared activities externally. |
| **SPO\_TotalFiles** | Number of SharePoint files. |
| **SPO\_ActiveFiles** | Number of active SharePoint files. |
| **SPO\_StorageUsed** | Quantity of SharePoint storage used. |
| **YAM\_TotalGroups** | Number of Viva Engage groups. |
| **YAM\_ActiveGroups** | Number of active Viva Engage groups. |
| **YAM\_LikedActiveGroups** | Number of Viva Engage groups with like activity. |
| **YAM\_PostedActiveGroups** | Number of Viva Engage groups with post activity. |
| **YAM\_ReadActiveGroups** | Number of Viva Engage groups with read activity. |
| **YAM\_TotalActivities** | Number of Viva Engage activities. |
| **YAM\_LikedActivities** | Number of Viva Engage like activities. |
| **YAM\_PostedActivities** | Number of Viva Engage post activities. |
| **YAM\_ReadActivities** | Number of Viva Engage read activities. |

### Data table - Tenant Office Licenses

The **Tenant Office Licenses** table provides month-over-month summary data about the license assignment for users.

| **Name** | **Description** |
| --- | --- |
| **LicenseName** | Name of the license. |
| **AssignedCount** | Number of assigned licenses. |
| **Timeframe** | Month value. |

### Data table - Tenant Office Activation

The **Tenant Office Activation** table provides data about the number of Office subscription activations across the service plans. For example:

- Microsoft 365 Apps for enterprises.
- Visio.
- Project.

It also provides data about the number of activations per device (Android, iOS, Mac, or PC).

| **Name** | **Description** |
| --- | --- |
| **ServicePlanName** | Name of the service plan. |
| **TotalEnabled** | Number of users enabled for the service plan by the end of the timeframe. |
| **TotalActivatedUsers** | Number of users who activated the service plan by the end of the timeframe. |
| **AndroidCount** | Number of activations for the service plan on Android devices by the end of the timeframe. |
| **iOSCount** | Number of activations for the service plan on iOS devices by the end of the timeframe. |
| **MacCount** | Number of activations for the service plan on Mac devices by the end of the timeframe. |
| **PcCount** | Number of activations for the service plan on PC devices by the end of the timeframe. |
| **WinRtCount** | Number of activations for the service plan on Windows Mobile devices by the end of the timeframe. |
| **Timeframe** | - Date value.<br>- Used as a many-to-one relationship with the Calendar table. |
| **Content Date** | If the timeframe is:<br>- The current month, the latest date with available data.<br>- A previous month, the last date of that month. |