---
layout: Conceptual
title: Search the audit log | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/audit-search
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Discover how to effectively search audit logs in Microsoft Purview, manage search jobs, and analyze user activity for compliance and security.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-06-19T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-audit
ms.collection:
- purview-compliance
- audit
search.appverid:
- MOE150
- MET150
ms.custom: seo-marvel-apr2020, admindeeplinkEXCHANGE, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: 6408997d-c5c2-afec-5f48-1471024ffc86
document_version_independent_id: 6408997d-c5c2-afec-5f48-1471024ffc86
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/audit-search.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-search
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/audit-search.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: caba0dfb-c592-a02e-73ec-dec3ef60025b
---

# Search the audit log | Microsoft Learn

Search in Microsoft Purview Audit (Standard) and Audit (Premium) gives your organization access to critical audit log event data so you can gain insight and further investigate user activities.

- Search jobs that you start through the Microsoft Purview portal don't need the web browser window to stay open to finish. These jobs keep running even after you close the browser window.
- The system now keeps completed search jobs for 30 days, so you can look back at past audit searches.
- Each admin Audit account user can have up to 10 search jobs running at the same time, with a limit of one unfiltered search job.

## Before you search the audit log

Review the following items before you start searching the audit log.

- Audit log search is turned on by default for Microsoft 365 and Office 365 enterprise organizations. Verify the current unified audit log ingestion setting for your organization by running the following command in **Exchange Online PowerShell**:

    ```powershell
    Get-AdminAuditLogConfig | Format-List UnifiedAuditLogIngestionEnabled
    ```

    The value of `True` for the *UnifiedAuditLogIngestionEnabled* property indicates that audit log search is turned on. For more information, see [Turn audit log search on or off](audit-log-enable-disable).

    Important

    Be sure to run the previous command in Exchange Online PowerShell. Although the **Get-AdminAuditLogConfig** cmdlet is also available in Security & Compliance PowerShell, the *UnifiedAuditLogIngestionEnabled* property is always `False`, even when audit log search is turned on.
- You must be assigned the *Audit Logs* or *View-Only Audit Logs* roles in the Microsoft Purview portal to search the audit log. For more information, see [Get started with auditing solutions](audit-get-started). To access audit cmdlets, you must be assigned the *Audit Logs* or *View-Only Audit Logs* roles in the Exchange admin center. You can also create custom role groups with the ability to search the audit log by adding the *View-Only Audit Logs* or *Audit Logs* roles to a custom role group. For more information, see [Permissions in the Microsoft Purview portal](purview-permissions).
- When a user or admin performs an audited activity, the system generates an audit record and stores it in the audit log for your organization. The length of time that an audit record is retained (and searchable in the audit log) depends on your Office 365 or Microsoft 365 Enterprise subscription, and specifically the type of the license that is assigned to specific users.

    - For users assigned an Office 365 E5 or Microsoft 365 E5 license (or users with a Microsoft Purview Suite (formerly known as Microsoft 365 E5 Compliance) or Microsoft 365 E5 eDiscovery and Audit add-on license), the system retains audit records for Microsoft Entra ID, Exchange, and SharePoint activity for one year by default. Organizations can also create audit log retention policies to retain audit records for activities in other services for up to one year. For more information, see [Manage audit log retention policies](audit-log-retention-policies).

        Note

        If your organization participated in the private preview program for the one-year retention of audit records, the retention duration for audit records that were generated before the general availability rollout date won't be reset.
    - For users assigned any other (non-E5) Office 365 or Microsoft 365 license, the system retains audit records for 180 days. For a list of Office 365 and Microsoft 365 subscriptions that support unified audit logging, see the [subscription requirements](https://aka.ms/M365EnterprisePlans) for Audit (Standard) and Audit (Premium).

        Important

        The default retention period for Audit (Standard) changed from 90 days to 180 days. Audit (Standard) logs generated before October 17, 2023 are retained for 90 days. Audit (Standard) logs generated on or after October 17, 2023 follow the new default retention of 180 days.

        Note

        Even when mailbox auditing on by default is turned on, you might notice that mailbox audit events for some users aren't found in audit log searches in the Microsoft Purview portal or via the Office 365 Management Activity API. For more information, see [Mailbox audit logging](audit-mailboxes#next-steps).
- To turn off audit log search for your organization, use the following command to disable unified audit log ingestion in Exchange Online PowerShell:

    ```powershell
    Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $false
    ```

    To turn unified audit log ingestion back on for your organization, run the following command in Exchange Online PowerShell:

    ```powershell
    Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true
    ```

    For more information, see [Turn off audit log search](audit-log-enable-disable).
- The underlying cmdlet used to search the audit log is an Exchange Online cmdlet, which is **Search-UnifiedAuditLog**. That means you can use this cmdlet to search the audit log instead of using the search tool on the **Audit** page in the Microsoft Purview portal. You have to run this cmdlet in Exchange Online PowerShell. For more information, see [Search-UnifiedAuditLog](/en-us/powershell/module/exchange/search-unifiedauditlog).

    For information about exporting the search results returned by the **Search-UnifiedAuditLog** cmdlet to a CSV file, see [Tips for exporting and viewing the audit log](audit-log-export-records#tips-for-exporting-and-viewing-the-audit-log).
- To programmatically download data from the audit log, use the Office 365 Management Activity API instead of a PowerShell script. The Office 365 Management Activity API is a REST web service that you can use to develop operations, security, and compliance monitoring solutions for your organization. For more information, see [Office 365 Management Activity API reference](/en-us/office/office-365-management-api/office-365-management-activity-api-reference).
- Microsoft Entra ID is the directory service for Microsoft 365. The unified audit log contains user, group, application, domain, and directory activities performed in the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339) or in the Azure management portal. For a complete list of Microsoft Entra events, see [Microsoft Entra audit Report Events](/en-us/azure/active-directory/reports-monitoring/concept-audit-logs).
- Microsoft doesn't guarantee a specific time after an event occurs for the corresponding audit record to be returned in the results of an audit log search. For core services (such as Exchange, SharePoint, OneDrive, and Teams), audit record availability is typically 60 to 90 minutes after an event occurs. For other services, audit record availability might be longer. However, some issues that are unavoidable (such as a server outage) might occur outside of the audit service that delays the availability of audit records. For this reason, Microsoft doesn't commit to a specific time.
- To search for Power BI activities in the audit log, you have to enable auditing in the Power BI admin portal. For instructions, see the "Audit logs" section in [Power BI admin portal](/en-us/power-bi/service-admin-portal#audit-logs).

## Get started with search

Important

The execution time (search time) of a Search job depends on several factors, including the selected date range, the number of users included, the volume of activities, and overall tenant size. In large tenants with a high number of users, broadly-scoped Search jobs may take up to 48 hours to complete.

Complete the following steps to get started with search:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Select the **Audit** solution card. If the **Audit** solution card isn't displayed, select **View all solutions** and then select **Audit** from the **Core** section.
3. On the **Search** page, configure the following search criteria as applicable:

    1. **Date and time range (UTC)**: The last seven days are selected by default. Select a date and time range to display the events that occurred within that period. The date and time are presented in Coordinated Universal Time (UTC). The maximum date range that you can specify is 180 days. An error is displayed if the selected date range is greater than 180 days.

        Tip

        If you use the maximum date range of 180 days, select the current time for the **Start date**. Otherwise, you receive an error saying that the start date is earlier than the end date. If you turn on auditing within the last 180 days, the maximum date range can't start before the date that auditing was turned on.
    2. **Keyword Search**: Enter a keyword or phrase to search for in the audit log. The keyword or phrase is searched for in the audit log or in the file, folder, or sites (if specified) for the search. To search for text that contains special characters, replace the special characters with an asterisk(\*) in your keyword search. For example, to search for *test\_search\_document*, use *test\*search\*document*.

        Important

        Terms entered in the **Keyword Search** field are only searched within indexed content (content within the Audit *common schema*). Audit *data content* in the audit log isn't searched for these keywords.
    3. **Admin Units**: Select the drop-down list to display the [administrative units](purview-admin-units#permissions-for-administrative-units) you want the audited activities scoped to for your search. You can select one or more administrative units to scope your search to. Leave this box blank to return entries for all administrative units in your organization.
    4. **Activities - friendly names**: Select the drop-down list to display the friendly names for audited activities that you can search for. Friendly names for user and admin activities are organized into groups of related activities. Using friendly names, you can select specific audited activities or you can select the activity group name to select all activities in the group. You can also select a selected activity to clear the selection. To search for a friendly name in the **Activities - friendly names** drop-down list, use the search box above that list.
    5. **Activities - operations names**: Enter the exact operation names to search for audited activities to include in your search results. You can enter one or more operation names, separated by commas. The **Activities - operations names** search criterion is similar to previous searches only available in PowerShell and provides greater flexibility helping you find the data that you need.

        Important

        Operation names must be entered exactly as they are named. If operation names are entered incorrectly, no results are returned.

        For example, to search for all activities related to enabling and disabling information barriers for a SharePoint site in your organization, you would:

        - Review the [audit activities](audit-log-activities) article to find the exact operation name for the information barriers activities you want to search for. In this [information barriers activities example](audit-log-activities#information-barriers-activities), the operation names are *SPOIBIsEnabled* and *SPOIBIsDisabled*.
        - Enter *SPOIBIsEnabled,SPOIBIsDisabled* in the **Activities - operations names** field. Copy and paste the operation names directly from [audit activities](audit-log-activities) to the **Activities - operations names** field to ensure that they're entered correctly and without typos.
    6. **Record types**: Select the drop-down list to display the record types for audited activities that you can search for. You can select one or more record types to search for. To search for a record type in the list, use the search box over the list.

        Specific [record types](audit-supported-services) are associated with specific Microsoft services and applications. For example, if you want to scope your search for specific record types associated with sensitivity labels in Microsoft Purview Information Protection (MIP), you could select the *MIPLabel*, *MipAutoLabelExchangeItem*, *MipAutoLabelSharePointItem*, and *MipAutoLabelSharePointPolicyLocation* record types from the list.
    7. **Search name**: Enter in a custom name for your search job. This name is used to identify your search job in the search job history. If you don't enter a name, the search job is automatically named using a combination of the date and time defined for the search and other defined search criteria values.
    8. **Users**: Select this field and select the names one or more users to display search results for. The audit log entries for the selected activity performed by the users you select in this box are displayed in the list of results. Leave this box blank to return entries for all users (and service accounts) in your organization.
    9. **File, folder, or site**: Enter part or all of a file or folder name to find related activity. This returns results for matching files, folders, and sites. You can also enter a full URL or part of one, just avoid special characters or spaces. You can use \* as a wildcard at the end of the URL. For example, `https://<tenantname>.sharepoint.com/sites/site123*`. Leave the field blank to see activity for all files and folders in your organization.
    10. **Workloads**: Enter or search for workload services to search for activity related to the selected workloads. Enter the name of a workload to jump to the workload in the list or scroll to the workloads you'd like to select.
4. Select **Search** to start your search job. A maximum of 10 search jobs can be run in parallel for one user account. If a user requires more than 10 search jobs, they must wait for an *In progress* job to finish or delete a search job.

## Search job dashboard

The search job dashboard displays active and completed search jobs. For each search job, the dashboard shows the following information:

- **Search name**: The name of the search job. You can see the full search name for a job by hovering the cursor over the search job name.
- **Job status**: The status of the search job. The status can be *Queued*, *In Progress*, or *Completed*.
- **Progress (%)**: The percentage of the search job that the job completes.
- **Search time**: The total running time that elapses to complete the search job.
- **Total results**: The total number of results the search job returns. When a query returns more than 100,000 results, an approximate count is displayed.
- **Creation time**: The date and time the search job created in UTC.
- **Search performed by**: The user account that creates the search job.

![Screenshot of the audit search job dashboard showing search results and available columns in Microsoft Purview.](media/audit-search/audit-new-search-columns.png)

Deleting a search job removes only the search job definition and the associated search result, not the backend data associated with search. To delete a search job, select the search job in the dashboard and then select **Delete** on the command bar.

To copy the search criteria for an existing search job, select the search job you want to copy and then select **Copy this search** on the command bar. The search criteria are copied to the search page and you can modify the search criteria as needed for a new search.

## Search job details dashboard

To view details about a search job, select the search job in the dashboard. The dashboard shows the total number of items in the job at the top. The total result number removes duplicates, so it might be less than the number of items in the search job dashboard.

![Screenshot of the search job details dashboard showing audit activity results and column details in Microsoft Purview.](media/audit-search/audit-search-job-details-dashboard.png)

The search job details dashboard displays the following information about the individual items gathered in the search job results:

- **Date (UTC)**: The date and time the activity occurred.
- **IP Address**: The IP address of the device that was used to perform the activity.
- **User**: The user account that performed the activity.
- **Record type**: The record type associated with the activity.
- **Activity**: The friendly name of the activity that was performed.
- **Item**: The name of the file, folder, or site that the activity was acted on.
- **Admin Units**: The admin unit that the user account that performed the activity belongs to.
- **Details**: Additional details about the activity.

You can sort the search job items by using the column headers or create a custom filter by using the filter pane. Use the filter to filter the search job items for specific values for any of the dashboard column criteria. To export all search job items to a .csv file, select **Export** on the command bar. Export supports results up to 50,000 rows for Audit (Standard) and up to 1,000,000 rows for Audit (Premium).

Select a specific activity to see more details about the activity in a fly-out window. The fly-out window displays the additional information about the activity.

![Screenshot of the search job item details fly-out showing the selected audit record's properties and event information.](media/audit-search/audit-new-search-result-details.png)

## Scoping access to audit logs using administrative units

Access to search the audit log is based on the [administrative units](purview-admin-units) assigned to the user in the Microsoft Purview portal. A restricted admin can only search and export user-generated audit logs within the scope of their assigned administrative units. An unrestricted admin has access to all audit logs, including logs generated by non-user and system accounts. To access scoped activity logs from any Microsoft service, including Exchange mailbox activity logs, use the [Search-UnifiedAuditLog](/en-us/powershell/module/exchange/search-unifiedauditlog) cmdlet.

| Admin units assigned to admins | Admin units available to perform scoped search on | Access to search and export audit logs |
| --- | --- | --- |
| None (Default): Unrestricted admin | All administrative units are available | Access to all activity logs from any user, nonuser, or system account. |
| One or more administrative units: Restricted admin | Only those administrative units assigned to the admin are available | Access to activity logs from users with a matching administrative unit assignment. |

Only [unrestricted admins](/en-us/purview/microsoft-365-compliance-center-permissions#administrative-units-support-in-microsoft-purview) can access the following audit activities through search queries. These logs are not yet accessible when queried by a restricted admin. To view a complete list of audit logs for these activities, submit a search request by using an unrestricted admin account.

| Service | Operation |
| --- | --- |
| Azure Information Protection | Discover |
| Dynamics 365 | CrmDefaultActivity |
| Endpoint data loss prevention | FileCreated  FileCreatedOnNetworkShare  FileCreatedOnRemovableMedia  FileDeleted |
| Exchange | Set-Mailbox  Set-MailboxPlan  SupervisionBulkEmailExclusion |
| Microsoft Forms | ViewRuntimeForm |

For more information about administrative units, see [Permissions in the Microsoft Purview portal](purview-permissions).