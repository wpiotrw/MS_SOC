---
layout: Conceptual
title: Search for eDiscovery (classic) activities in the audit log | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/ediscovery-search-for-activities-in-the-audit-log
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn what events are logged when users assigned eDiscovery permissions perform Content search, eDiscovery (Standard), and eDiscovery (Premium) tasks in the Microsoft Purview portal.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-10-31T00:00:00.0000000Z
ROBOTS: NOINDEX, NOFOLLOW
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
ms.custom: seo-marvel-apr2020
locale: en-us
document_id: add92ffe-e0d2-d5e6-fab4-1841e9769d1c
document_version_independent_id: add92ffe-e0d2-d5e6-fab4-1841e9769d1c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/ediscovery-search-for-activities-in-the-audit-log.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: ediscovery-search-for-activities-in-the-audit-log
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/ediscovery-search-for-activities-in-the-audit-log.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: d4b73fc4-4288-a2ac-d3de-6b14b6829894
---

# Search for eDiscovery (classic) activities in the audit log | Microsoft Learn

Caution

Microsoft retired all classic eDiscovery experiences on August 31, 2025. This retirement includes classic [Content Search](ediscovery-content-search-overview), classic [eDiscovery (Standard)](ediscovery-standard-get-started), and classic [eDiscovery (Premium)](ediscovery-overview).

The guidance in this article only applies to organizations hosted in Microsoft 365 operated by 21Vianet (China). If your organization isn't hosted by 21Vianet, use the guidance for the [new eDiscovery experience](edisc) in the [Microsoft Purview portal](https://purview.microsoft.com).

Content Search and eDiscovery-related activities (for Microsoft Purview eDiscovery (Standard) and Microsoft Purview eDiscovery (Premium)) that are performed in Microsoft Purview portal or by running the corresponding PowerShell cmdlets are logged in the audit log. Events are logged when administrators or eDiscovery managers (or any user assigned eDiscovery permissions) perform the following Content Search and eDiscovery (Standard) tasks in the Microsoft Purview portal:

- Creating and managing eDiscovery (Standard) and eDiscovery (Premium) cases.
- Creating, starting, and editing Content searches.
- Performing search actions, such as previewing, exporting, and deleting search results.
- Managing custodians and review sets in eDiscovery (Premium).
- Configuring permissions filtering for Content search.
- Managing the eDiscovery Administrator role.

For more information about searching the audit log, the permissions that are required, and exporting search results, see [Search the audit log](audit-search).

## How to search for and view eDiscovery activities

Currently, you have to do a few specific things to view eDiscovery activities in the audit log. Here's how:

1. Go to the [Microsoft Purview portal](https://compliance.microsoft.com) and sign in using your work or school account.
2. In the left navigation pane of the Microsoft Purview portal, select **Audit**.
3. In the **Activities** drop-down list, under **eDiscovery activities** or **eDiscovery (Premium) activities**, select one or more activities to search for.

    Note

    The **Activities** drop-down list also includes a group of activities named **eDiscovery cmdlet activities** that will return records from the cmdlet audit log.
4. Select a date and time range to display eDiscovery events that occurred within that period.
5. In the **Users** box, select one or more users to display search results for. Leave this box blank to return entries for all users.
6. Select **Search** to run the search using your search criteria.
7. After the search results are displayed, you can select **Filter results** to filter or sort the resulting activity records. Unfortunately, you can't use filtering to explicitly exclude certain activities.
8. To view details about an activity, select the activity record in the list of search results.

    A **Details** fly out page is displayed that contains the detailed properties from the event record. To display additional details, select **More information**. For a description of these properties, see the Detailed properties for eDiscovery activities section.
9. If desired, you can export the audit log search results to a CSV file, and then use the Excel Power Query feature to format and filter these records. For more information, see [Export, configure, and view audit log records](audit-log-export-records).

## eDiscovery activities

The following table describes the Content Search and eDiscovery (Standard) activities that are logged when an administrator or eDiscovery manager performs an eDiscovery-related activity using the Microsoft Purview portal. Some activities performed in eDiscovery (Premium) may be returned when you search for activities in this list.

Note

The eDiscovery activities described in this section provide similar information to the eDiscovery cmdlet activities described in the next section. We recommend that you use the eDiscovery activities described in this section because they will appear in the audit log search results within 30 minutes. It may take up to 24 hours for eDiscovery cmdlet activities to appear in audit log search results.

| **Friendly name** | **Operation** | **Corresponding cmdlet** | **Description** |
| --- | --- | --- | --- |
| Added member to eDiscovery case | CaseMemberAdded | Add-ComplianceCaseMember | A user was added as a member of an eDiscovery case. As a member of a case, a user can perform various case-related tasks depending on whether they've been assigned the necessary permissions. |
| Changed content search | SearchUpdated | Set-ComplianceSearch | An existing content search was changed. Changes can include adding or removing content locations or editing the search query. |
| Changed eDiscovery administrator membership | CaseAdminUpdated | Update-eDiscoveryCaseAdmin | The list of eDiscovery Administrators in your organization was changed. This activity is logged when the list of eDiscovery Administrators is replaced with a group of new users. If a single user is added or removed, the CaseAdminAdded operation is logged. |
| Changed eDiscovery case | CaseUpdated | Set-ComplianceCase | An eDiscovery case was changed. Changes include closing an open case or reopening a closed case. |
| Changed eDiscovery case membership | CaseMemberUpdated | Update-ComplianceCaseMember | The membership list of an eDiscovery case was changed. This activity is logged when all members are replaced with a group of new users. If a single member is added or removed, CaseMemberAdded or CaseMemberRemoved operation is logged. |
| Changed search permissions filter | SearchPermissionUpdated | Set-ComplianceSecurityFilter | A search permissions filter was changed. |
| Changed search query for eDiscovery case hold | HoldUpdated | Set-CaseHoldRule | A query-based hold associated with an eDiscovery case was changed. Possible changes include editing the query or date range for a query-based hold. |
| Content search preview item downloaded | PreviewItemDownloaded | N/A | A user downloaded an item to their local computer (by selecting the **Download original item** link) when previewing search results. |
| Content search preview item listed | PreviewItemListed | N/A | A user selected **Preview search results** to display the preview search results page, which lists up to 1,000 items from the results of a search. |
| Created content search | SearchCreated | New-ComplianceSearch | A new content search was created. |
| Created eDiscovery administrator | CaseAdminAdded | Add-eDiscoveryCaseAdmin | A user was added as an eDiscovery Administrator in the organization. |
| Created eDiscovery case | CaseAdded | New-ComplianceCase | An eDiscovery case was created. When a case is created, you only have to give it a name. Other case-related tasks such as adding members, creating holds, and creating content searches associated with the case result in additional events being logged. |
| Created search permissions filter | SearchPermissionCreated | New-ComplianceSecurityFilter | A search permissions filter was created. |
| Created search query for eDiscovery case hold | HoldCreated | New-CaseHoldRule | A query-based hold associated with an eDiscovery case was created. |
| Deleted content search | SearchRemoved | Remove-ComplianceSearch | An existing content search was deleted. |
| Deleted eDiscovery administrator | CaseAdminRemoved | Remove-eDiscoveryCaseAdmin | An eDiscovery Administrator was deleted from your organization. |
| Deleted eDiscovery case | CaseRemoved | Remove-ComplianceCase | An eDiscovery case was deleted. Any hold associated with the case has to be removed before the case can be deleted. |
| Deleted search permissions filter | SearchPermissionRemoved | Remove-ComplianceSecurityFilter | A search permissions filter was deleted. |
| Deleted search query for eDiscovery case hold | HoldRemoved | Remove-CaseHoldRule | A query-based hold associated with an eDiscovery case was deleted. Removing the query from the hold is often the result of deleting a hold. When a hold or a hold query is deleted, the content locations that were on hold are released. |
| Downloaded export of content search | SearchExportDownloaded | N/A | A user downloaded the results of a content search to their local computer. A **Started export of content search** activity has to be initiated before search results can be downloaded. |
| Previewed results of content search | SearchPreviewed | N/A | A user previewed the results of a content search. |
| Purged results of content search | SearchResultsPurged | New-ComplianceSearchAction | A user purged the results of a Content search by running the **New-ComplianceSearchAction -Purge** command. |
| Removed analysis of content search | RemovedSearchResultsSentToZoom | Remove-ComplianceSearchAction | A content search prepare action (to prepare search results for eDiscovery (Premium)) was deleted. If the preparation action was less than two weeks old, the search results that were prepared for eDiscovery (Premium) were deleted from the Microsoft Azure storage area. If the preparation action was older than 2 weeks, then this event indicates that only the corresponding preparation action was deleted. |
| Removed export of content search | RemovedSearchExported | Remove-ComplianceSearchAction | A content search export action was deleted. If the export action was less than two weeks old, the search results that were uploaded to the Microsoft Azure storage area were deleted. If the export action was older than 2 weeks, then this event indicates that only the corresponding export action was deleted. |
| Removed member from eDiscovery case | CaseMemberRemoved | Remove-ComplianceCaseMember | A user was removed as a member of an eDiscovery case. |
| Removed preview results of content search | RemovedSearchPreviewed | Remove-ComplianceSearchAction | A content search preview action was deleted. |
| Removed purge action performed on content search | RemovedSearchResultsPurged | Remove-ComplianceSearchAction | A content search purge action was deleted. |
| Removed search report | SearchReportRemoved | Remove-ComplianceSearchAction | A content search export report action was deleted. |
| Started analysis of content search | SearchResultsSentToZoom | New-ComplianceSearchAction | The results of a content search were prepared for analysis in eDiscovery (Premium). |
| Started content search | SearchStarted | Start-ComplianceSearch | A content search was started. When you create or change a content search by using the Microsoft Purview portal, the search is automatically started. |
| Started export of content search | SearchExported | New-ComplianceSearchAction | A user exported the results of a content search. |
| Started export report | SearchReport | New-ComplianceSearchAction | A user exported a content search report. |
| Stopped content search | SearchStopped | Stop-ComplianceSearch | A user stopped a content search. |
| (none) | CaseViewed | Get-ComplianceCase | A user viewed an eDiscovery (Standard) case in the Microsoft Purview portal. The audit record for this event includes the name of the case that was viewed. |
| (none) | SearchViewed | Get-ComplianceSearch | A user viewed a Content search in the Microsoft Purview portal by accessing the search on the **Searches** tab in an eDiscovery (Standard) case or accessing it on the **Content search** page. The audit record for this event includes the identity of the search that was viewed. |
| (none) | ViewedSearchPreviewed | Get-ComplianceSearchAction -Preview | A user previewed the results of a Content search in the Microsoft Purview portal. This activity is also logged when a user previews the results of a search associated with an eDiscovery (Standard) case. |
|  |  |  |  |

## eDiscovery (Premium) activities

The following table describes the eDiscovery (Premium) activities logged in the audit log. These activities can be used to help you track the progression of activity in an eDiscovery (Premium) case.

| **Friendly name** | **Operation** | **Description** |
| --- | --- | --- |
| Added data to another review set | AddWorkingSetQueryToWorkingSet | User added documents from one review set to a different review set. |
| Added data to review set | AddQueryToWorkingSet | User added the search results from a content search associated with an eDiscovery (Premium) case to a review set. |
| Added non-Microsoft 365 data to review set | AddNonOffice365DataToWorkingSet | User added non-Microsoft 365 data to a review set. |
| Added remediated documents to review set | AddRemediatedData | User uploads documents that had indexing errors that were fixed to a review set. |
| Analyzed data in review set | RunAlgo | User ran analytics on the documents in a review set. |
| Annotated document in review set | AnnotateDocument | User annotated a document in a review set. Annotation includes redacting content in a document. |
| Compared load sets | LoadComparisonJob | User compared two different load sets in a review set. A load set is when data from a content search that associated with the case is added to a review set. |
| Converted redacted documents to PDF | BurnJob | User converted all the redacted documents in a review set to PDF files. |
| Created review set | CreateWorkingSet | User created a review set. |
| Created review set search | CreateWorkingSetSearch | User created a search query that searches the documents in a review set. |
| Created tag | CreateTag | User created a tag group in a review set. A tag group can contain one or more child tags. These tags are then used to tag documents in the review set. |
| Deleted review set search | DeleteWorkingSetSearch | User deleted a search query in a review set. |
| Deleted tag | DeleteTag | User deleted a tag or a tag group in a review set. |
| Downloaded document | DownloadDocument | User downloaded a document from a review set. |
| Edited tag | UpdateTag | User changed a tag in a review set. |
| Exported documents from review set | ExportJob | User exported documents from a review set. |
| Modified case setting | UpdateCaseSettings | User modified the settings for a case. Case settings include case information, access permissions, and settings that control search and analytics behavior. |
| Modified review set search | UpdateWorkingSetSearch | User edited a search query in a review set. |
| Previewed review set search | PreviewWorkingSetSearch | User previewed the results of a search query in a review set. |
| Remediated error documents | ErrorRemediationJob | User fixes files that contained indexing errors. |
| Tagged document | TagFiles | User tags a document in a review set. |
| Tagged results of a query | TagJob | User tags all of the documents that match the criteria of search query in a review set. |
| Viewed document in review set | ViewDocument | User viewed a document in a review set. |
|  |  |  |

## eDiscovery cmdlet activities

The following table lists the cmdlet audit log records that are logged when an administrator or user performs an eDiscovery-related activity by using the Microsoft Purview portal or by running the corresponding cmdlet in Security & Compliance PowerShell. The detailed information in the audit log record is different for the cmdlet activities listed in this table and the eDiscovery activities described in the previous section.

As previously stated, it may take up to 24 hours for eDiscovery cmdlet activities to appear in the audit log search results.

Tip

The cmdlets in the **Operation** column in the following table are linked to the corresponding cmdlet help topic on TechNet. Go to the cmdlet help topic for a description of the available parameters for each cmdlet. The parameter and the parameter value that were used with a cmdlet are included in the audit log entry for each eDiscovery cmdlet activity that's logged.

| **Friendly name** | **Operation (cmdlet)** | **Description** |
| --- | --- | --- |
| Created hold in eDiscovery case | [New-CaseHoldPolicy](/en-us/powershell/module/exchange/new-caseholdpolicy) | A hold was created for an eDiscovery case. A hold can be created with or without specifying a content source. If content sources are specified, they'll be identified in the audit log entry. |
| Deleted hold from eDiscovery case | [Remove-CaseHoldPolicy](/en-us/powershell/module/exchange/remove-caseholdpolicy) | A hold that is associated with an eDiscovery case was deleted. Deleting a hold releases all of the content locations from the hold. Deleting the hold also results in deleting the case hold rules associated with the hold (see **Remove-CaseHoldRule** below). |
| Changed hold in eDiscovery case | [Set-CaseHoldPolicy](/en-us/powershell/module/exchange/set-caseholdpolicy) | A hold that is associated with an eDiscovery was changed. Possible changes include adding or removing content locations or turning off (disabling) the hold. |
| Created search query for eDiscovery case hold | [New-CaseHoldRule](/en-us/powershell/module/exchange/new-caseholdrule) | A query-based hold associated with an eDiscovery case was created. |
| Deleted search query for eDiscovery case hold | [Remove-CaseHoldRule](/en-us/powershell/module/exchange/remove-caseholdrule) | A query-based hold associated with an eDiscovery case was deleted. Removing the query from the hold is often the result of deleting a hold. When a hold or a hold query is deleted, the content locations that were on hold are released. |
| Changed search query for eDiscovery case hold | [Set-CaseHoldRule](/en-us/powershell/module/exchange/set-caseholdrule) | A query-based hold associated with an eDiscovery case was changed. Possible changes include editing the query or date range for a query-based hold. |
| Created eDiscovery case | [New-ComplianceCase](/en-us/powershell/module/exchange/new-compliancecase) | An eDiscovery case was created. When a case is created, you only have to give it a name. Other case-related tasks such as adding members, creating holds, and creating content searches associated with the case result in additional events being logged. |
| Deleted eDiscovery case | [Remove-ComplianceCase](/en-us/powershell/module/exchange/remove-compliancecase) | An eDiscovery case was deleted. Any hold associated with the case has to be removed before the case can be deleted. |
| Changed eDiscovery case | [Set-ComplianceCase](/en-us/powershell/module/exchange/set-compliancecase) | An eDiscovery case was changed. Changes include closing an open case or reopening a closed case. |
| Added member to eDiscovery case | [Add-ComplianceCaseMember](/en-us/powershell/module/exchange/add-compliancecasemember) | A user was added as a member of an eDiscovery case. As a member of a case, a user can perform various case-related tasks depending on whether they've been assigned the necessary permissions. |
| Removed member from eDiscovery case | [Remove-ComplianceCaseMember](/en-us/powershell/module/exchange/remove-compliancecasemember) | A user was removed as a member of an eDiscovery case. |
| Changed eDiscovery case membership | [Update-ComplianceCaseMember](/en-us/powershell/module/exchange/update-compliancecasemember) | The membership list of an eDiscovery case was changed. This activity is logged when all members are replaced with a group of new users. If a single member is added or removed, the **Add-ComplianceCaseMember** or **Remove-ComplianceCaseMember** operation is logged. |
| Created content search | [New-ComplianceSearch](/en-us/powershell/module/exchange/new-compliancesearch) | A new content search was created. |
| Deleted content search | [Remove-ComplianceSearch](/en-us/powershell/module/exchange/remove-compliancesearch) | An existing content search was deleted. |
| Changed content search | [Set-ComplianceSearch](/en-us/powershell/module/exchange/set-compliancesearch) | An existing content search was changed. Changes can include adding or removing content locations that are searched and editing the search query. |
| Started content search | [Start-ComplianceSearch](/en-us/powershell/module/exchange/start-compliancesearch) | A content search was started. When you create or change a content search by using the Microsoft Purview portal GUI, the search is automatically started. If you create or change a search by using the **New-ComplianceSearch** or **Set-ComplianceSearch** cmdlet, you have to run the **Start-ComplianceSearch** cmdlet to start the search. |
| Stopped content search | [Stop-ComplianceSearch](/en-us/powershell/module/exchange/stop-compliancesearch) | A content search that was running was stopped. |
| Created content search action | [New-ComplianceSearchAction](/en-us/powershell/module/exchange/new-compliancesearchaction) | A content search action was created. Content search actions include previewing search results, exporting search results, preparing search results for analysis in eDiscovery (Premium), and permanently deleting items that match the search criteria of a content search. |
| Deleted content search action | [Remove-ComplianceSearchAction](/en-us/powershell/module/exchange/remove-compliancesearchaction) | A content search action was deleted. |
| Created search permissions filter | [New-ComplianceSecurityFilter](/en-us/powershell/module/exchange/new-compliancesecurityfilter) | A search permissions filter was created. |
| Deleted search permissions filter | [Remove-ComplianceSecurityFilter](/en-us/powershell/module/exchange/remove-compliancesecurityfilter) | A search permissions filter was deleted. |
| Changed search permissions filter | [Set-ComplianceSecurityFilter](/en-us/powershell/module/exchange/set-compliancesecurityfilter) | A search permissions filter was changed. |
| Created eDiscovery administrator | [Add-eDiscoveryCaseAdmin](/en-us/powershell/module/exchange/add-ediscoverycaseadmin) | A user was added as an eDiscovery Administrator in your organization. |
| Deleted eDiscovery administrator | [Remove-eDiscoveryCaseAdmin](/en-us/powershell/module/exchange/remove-ediscoverycaseadmin) | An eDiscovery Administrator was deleted from your organization. |
| Changed eDiscovery administrator membership | [Update-eDiscoveryCaseAdmin](/en-us/powershell/module/exchange/update-ediscoverycaseadmin) | The list of eDiscovery Administrators in your organization was changed. This activity is logged when the list of eDiscovery Administrators is replaced with a group of new users. If a single user is added or removed, the **Add-eDiscoveryCaseAdmin** or **Remove-eDiscoveryCaseAdmin** operation is logged. |
| (none) | [Get-ComplianceCase](/en-us/powershell/module/exchange/get-compliancecase) | This activity is logged when a user viewed a list of eDiscovery (Standard) or eDiscovery (Premium) cases. This activity is also logged when a user views a specific case in eDiscovery (Standard). When a user views a specific case, the audit record includes the identity of the case that was viewed. If the user only viewed a list of cases, the audit record doesn't contain a case identity. |
| (none) | [Get-ComplianceSearch](/en-us/powershell/module/exchange/get-compliancesearch) | This activity is logged when a user viewed a list of Content searches or searches associated with an eDiscovery (Standard) case. This activity is also logged when a user views a specific Content search or views a specific search associated with an eDiscovery (Standard) case. When a user views a specific search, the audit record includes the identity of the search that was viewed. If the user only viewed a list of searches, the audit record doesn't contain a search identity. |
| (none) | [Get-ComplianceSearchAction](/en-us/powershell/module/exchange/get-compliancesearchaction) | This activity is logged when a user viewed a list of compliance search actions (such as exports, previews, or purges) or actions associated with an eDiscovery (Standard) case. This activity is also logged when a user views a specific compliance search action (such as an export) or views a specific action associated with an eDiscovery (Standard) case. When a user views a search action, the audit record includes the identity of the search action that was viewed. If the user only viewed a list of actions, the audit record doesn't contain an action identity. |
|  |  |  |

## Detailed properties for eDiscovery activities

The following table describes the properties that are included on the flyout page for an eDiscovery activity listed in the search results. These properties are also included in the CSV file when you export the audit log search results. An audit log record for an eDiscovery activity won't include every detailed property listed below.

Tip

When you export the search results, the CSV file contains a column named **AudtiData**, which contains the detailed properties described in the following table in a multi-value property. You can use the Power Query feature in Excel to split this column into multiple columns so that each property will have its own column. This will let you sort and filter on one or more of these properties. For more information, see [Search the audit log](audit-search).

| **Property** | **Description** |
| --- | --- |
| Case | The identity (GUID) of the eDiscovery case that was created, changed, or deleted. |
| ClientApplication | eDiscovery cmdlet activities have a value of **EMC** for this property. This indicates the activity was performed by using the Microsoft Purview portal GUI or running the cmdlet in PowerShell. |
| ClientIP | The IP address of the device that was used when the activity was logged. The IP address is displayed in either an IPv4 or IPv6 address format. |
| ClientRequestId | For eDiscovery activities, this property is typically blank. |
| CmdletVersion | The build number for the version of the Microsoft Purview portal running in your organization. |
| CreationTime | The date and time in Coordinated Universal Time (UTC) when the eDiscovery activity was completed. |
| EffectiveOrganization | The name of the Microsoft 365 organization. |
| ExchangeLocations | The Exchange Online mailboxes that are included in a content search or placed on hold in an eDiscovery case. |
| Exclusions | Mailbox or site locations that are excluded from a content search or a hold in an eDiscovery case. |
| ExtendedProperties | Additional properties from a content search, a content search action, or hold in an eDiscovery case, such as the object GUID and the corresponding cmdlet and cmdlet parameters that were used when the activity was performed. |
| Id | The ID of the report entry. The ID uniquely identifies the audit log entry. |
| NonPIIParameters | A list of the parameters (without any values) that were used with the cmdlet identified in the Operation property. The parameters listed in this property are the same as those listed in the Parameters property. |
| ObjectId | The GUID or name of the object (for example, a Content search or an eDiscovery (Standard) case) that was created, accessed, changed, or deleted by the activity listed in the Operation property. This object is also identified in the Item column in the audit log search results. |
| ObjectType | The type of eDiscovery object that the user created, deleted, or modified; for example, a content search action (preview, export, or purge), an eDiscovery case, or a content search. |
| Operation | The name of the operation that corresponds to the eDiscovery activity that was performed. |
| OrganizationId | The GUID for your Microsoft 365 organization. |
| Parameters | The name and value for the parameters that were used with the corresponding cmdlet. |
| PublicFolderLocations | The public folder locations in Exchange Online that are included in a content search or placed on hold in an eDiscovery case. |
| Query | The search query associated with the activity, such as a content search or a query-based hold. |
| RecordType | The type of operation indicated by the record. The value of **18** indicates an event related to an activity listed in the eDiscovery cmdlet activities section. A value of **24** indicates an event related to an activity listed in the How to search for and view eDiscovery activities section. |
| ResultStatus | Indicates whether the action (specified in the Operation property) was successful or not. |
| SecurityComplianceCenterEventType | Indicates that the activity was a Microsoft Purview portal event. All eDiscovery activities will have a value of **0** for this property. |
| SharepointLocations | The SharePoint Online sites that are included in a content search or placed on hold in an eDiscovery case. |
| StartTime | The date and time in Coordinated Universal Time (UTC) when the eDiscovery activity was started. |
| UserId | The user who performed the activity (specified in the Operation property) that resulted in the record being logged. Records for eDiscovery activity performed by system accounts (such as NT AUTHORITY\SYSTEM) are also included in the audit log. |
| UserKey | An alternative ID for the user identified in the UserId property. For eDiscovery activities, the value for this property is typically the same as the UserId property. |
| UserServicePlan | The subscription used by your organization. For eDiscovery activities, this property is typically blank. |
| UserType | The type of user that performed the operation. The following values indicate the user type.  0 A regular user. 2 An administrator in your organization. 3 A Microsoft datacenter administrator or datacenter system account. 4 A system account. 5 An application. 6 A service principal. |
| Version | Indicates the version number of the activity (identified by the Operation property) that's logged. |
| Workload | The service where the activity occurred. For eDiscovery activities, the value is **SecurityComplianceCenter**. |