---
layout: Conceptual
title: Detailed activity properties in the audit log | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/audit-log-detailed-properties
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Discover how to export audit log results and understand the additional activity properties included for Microsoft 365 services.
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-02-18T00:00:00.0000000Z
audience: Admin
ms.topic: reference
ms.service: purview
ms.subservice: purview-audit
ms.collection:
- purview-compliance
- audit
search.appverid:
- MOE150
- BCS160
- MET150
ms.custom: seo-marvel-apr2020
ai-usage: ai-assisted
locale: en-us
document_id: 2c860b55-8bb8-033e-e979-5dde64cae143
document_version_independent_id: 2c860b55-8bb8-033e-e979-5dde64cae143
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/audit-log-detailed-properties.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-log-detailed-properties
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/audit-log-detailed-properties.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: 63b0a056-81b2-29e5-6215-1fdeacc6e404
---

# Detailed activity properties in the audit log | Microsoft Learn

When you export the results of an audit log search from the Microsoft Purview portal, you can download all the results that meet your search criteria. You can export this information by selecting **Export results** &gt; **Download all results** on the **Audit log search** page. For more information, see [Search the audit log](audit-search).

When you export all results for an audit log search, the raw data from the unified audit log is copied to a comma-separated value (CSV) file that you download to your local computer. This file contains extra property information from each audit activity record in a column named **AuditData**. This column contains a multi-value property for multiple properties from the audit log record. Each of the **property: value** pairs in this multi-value property are separated by a comma.

The following table describes the activity properties that are included (depending on the service in which an activity occurs) in the multi-property **AuditData** column. The **Microsoft service that has this property** column indicates the service and type of activity (user or admin) that includes the property. For more detailed information about these properties or about properties that might not be listed in this article, see [Management Activity API Schema](/en-us/office/office-365-management-api/office-365-management-activity-api-schema).

Tip

You can use the JSON transform feature in Power Query in Excel to split the **AuditData** column into multiple columns so that each property has its own column. This feature lets you sort and filter on one or more of these properties. For step-by-step guidance, see [Export, configure, and view audit log records](audit-log-export-records).

| Property | Description | Microsoft service that has this property |
| --- | --- | --- |
| Actor | The user or service account that performed the action. | Microsoft Entra ID |
| AddOnName | The name of an add-on that was added, removed, or updated in a team. The type of add-ons in Microsoft Teams is a bot, a connector, or a tab. | Microsoft Teams |
| AddOnType | The type of an add-on that was added, removed, or updated in a team. The following values indicate the type of add-on. **1** - Indicates a bot.**2** - Indicates a connector.**3** - Indicates a tab. | Microsoft Teams |
| AppAccessContext | The application context for the user or service principal that performed the action. | Microsoft Teams |
| ArtifactShared | Files or content shared by the user. | Microsoft Teams |
| AzureActiveDirectoryEventType | The type of Microsoft Entra ID activity. The following values indicate the type of activity. **0** - Indicates an account sign-in activity.**1** - Indicates an Azure application security activity. | Microsoft Entra ID |
| ChannelGuid | The ID of a Microsoft Teams channel. The team that the channel is located in is identified by the **TeamName** and **TeamGuid** properties. | Microsoft Teams |
| ChannelName | The name of a Microsoft Teams channel. The team that the channel is located in is identified by the **TeamName** and **TeamGuid** properties. | Microsoft Teams |
| Client | The client device, the device OS, and the device browser used for the sign-in activity (for example, Nokia Lumia 920; Windows Phone 8; IE Mobile 11). | Microsoft Entra ID |
| ClientInfoString | Information about the email client that was used to perform the operation, such as a browser version, Outlook version, and mobile device information | Exchange (mailbox activity) |
| ClientIP | The IP address of the device that was used when the activity was logged. The IP address is displayed in either an IPv4 or IPv6 address format. For some services, the value displayed in this property might be the IP address for a trusted application (for example, Office on the web apps) calling into the service on behalf of a user and not the IP address of the device used by person who performed the activity. Also, for admin activity (or activity performed by a system account) for Microsoft Entra ID-related activities, the IP address isn't logged and the value for the ClientIP property is `null`. | Microsoft Entra ID, Exchange, SharePoint |
| CreationTime | The date and time in Coordinated Universal Time (UTC) when the audit log record is generated. | All |
| CurrentProtectionType | A complex property type containing fields to describe the current protection status of a document. Includes the following: **ProtectionType**: Enumerates the type of protection applied to the document. These values and their meanings apply: *0* (no protection), *1* (template-based protection), *2* (don't forward, for email), *3* (encrypt only), and *4* (custom, user configured protection) **Owner**: The email address of the user that configured protection. **TemplateId**: When the *ProtectionType* is set to *1* (template), this field contains the GUID of the template applied to the document. When the value of *ProtectionType* doesn't equal *1*, this field is blank. **DocumentEncrypted**: Boolean flag indicating if any type of encryption is applied to the document. Values are *True* or *False*. | All |
| DestinationFileExtension | The file extension of a file that is copied or moved. This property is displayed only for the FileCopied and FileMoved user activities. | SharePoint |
| DestinationFileName | The name of the file is copied or moved. This property is displayed only for the FileCopied and FileMoved actions. | SharePoint |
| DestinationRelativeUrl | The URL of the destination folder where a file is copied or moved. The combination of the values for the **SiteURL**, the **DestinationRelativeURL**, and the **DestinationFileName** property is the same as the value for the **ObjectID** property, which is the full path name for the file that was copied. This property is displayed only for the FileCopied and FileMoved user activities. | SharePoint |
| EventSource | Identifies that an activity occurred in SharePoint. Possible values are **SharePoint** and **ObjectModel**. | SharePoint |
| ExtendedProperties | The extended properties for Microsoft Purview and Microsoft Entra ID activities. | Microsoft Entra ID  Microsoft Purview |
| ExternalAccess | For Exchange admin activity, specifies whether the cmdlet was run by a user in your organization, by Microsoft datacenter personnel or a datacenter service account, or by a delegated administrator. The value **False** indicates that the cmdlet was run by someone in your organization. The value **True** indicates that the cmdlet was run by datacenter personnel, a datacenter service account, or a delegated administrator.  For Exchange mailbox activity, specifies whether a mailbox was accessed by a user outside your organization. | Exchange |
| ID | The ID of the report entry. The ID uniquely identifies the report entry. | All |
| InternalLogonType | Reserved for internal use. | Exchange (mailbox activity) |
| IsJoinedFromLobby | Whether or not the user joined a Teams session from the lobby. | Microsoft Teams |
| ItemType | The type of object that was accessed or modified. Possible values include **File**, **Folder**, **Web**, **Site**, **Tenant**, and **DocumentLibrary**. | SharePoint |
| LoginStatus | Identifies sign-in failures that might have occurred. | Microsoft Entra ID |
| LogonType | The type of mailbox access. The following values indicate the type of user who accessed the mailbox. **0** - Indicates a mailbox owner.**1** - Indicates an administrator.**2** - Indicates a delegate. **3** - Indicates the transport service in the Microsoft datacenter.**4** - Indicates a service account in the Microsoft datacenter. **6** - Indicates a delegated administrator. | Exchange (mailbox activity) |
| MailboxGuid | The Exchange GUID of the mailbox that was accessed. | Exchange (mailbox activity) |
| MailboxOwnerUPN | The email address of the person who owns the mailbox that was accessed. | Exchange (mailbox activity) |
| Members | Lists the users that have been added or removed from a team. The following values indicate the Role type assigned to the user. **1** - Indicates the Member role.**2** - Indicates the Owner role.**3** - Indicates the Guest role. The Members property also includes the name of your organization, and the member's email address. | Microsoft Teams |
| ModifiedProperties (Name, NewValue, OldValue) | The property is included for admin activities, such as adding a user as a member of a site or a site collection admin group. The property includes the name of the property that was modified (for example, the Site Admin group) the new value of the modified property (such the user who was added as a site admin, and the previous value of the modified object). | All (admin activity) |
| NewValue | The value after a change, includes all properties updated or deleted. | Microsoft Purview (governance) |
| ObjectFullyQualifiedName | The fully qualified name for an entity. | Microsoft Purview (governance) |
| ObjectId | For Exchange admin audit logging, the name of the object that was modified by the cmdlet.  For SharePoint activity, the full URL path name of the file or folder accessed by a user.  For Microsoft Entra ID activity, the name of the user account that was modified. | All |
| ObjectName | The main entity name. | Microsoft Purview (governance) |
| ObjectType | The entity type. | Microsoft Purview (governance) |
| OldValue | The value before a change, includes all properties updated or deleted. | Microsoft Purview (governance) |
| Operation | The name of the user or admin activity. The value of this property corresponds to the value that was selected in the **Activities** drop down list. If **Show results for all activities** was selected, the report includes entries for all user and admin activities for all services. For a description of the operations/activities that are logged in the audit log, see the **Audited activities** tab in [Search the audit log](audit-search).  For Exchange admin activity, this property identifies the name of the cmdlet that was run. | All |
| OrganizationId | The GUID for your organization. | All |
| Parameters | For Exchange admin activity, the name and value for all parameters that were used with the cmdlet that is identified in the Operation property. | Exchange (admin activity) |
| ParticipantInfo | Additional properties about the participant identity. | Microsoft Teams |
| ParticipatingDomainInformation | Domain information about the participant. | Microsoft Teams |
| Path | The name of the mailbox folder where the message that was accessed is located. This property also identifies the folder a where a message is created in or copied/moved to. | Exchange (mailbox activity) |
| PreviousProtectionType | A complex property type containing fields to describe the previous protection status of a document. Includes the following: **ProtectionType**: Enumerates the type of protection applied to the document. These values and their meanings apply: *0* (no protection), *1* (template-based protection), *2* (don't forward, for email), *3* (encrypt only), *4* (custom, user configured protection) **Owner**: The email address of the user that configured protection. **TemplateId**: When the *ProtectionType* is set to *1* (template), this field contains the GUID of the template applied to the document. When the value of *ProtectionType* doesn't equal *1*, this field is blank. **DocumentEncrypted**: Boolean flag indicating if any type of encryption is applied to the document. Values are *True* or *False*. | All |
| ProtectionEventType | Enumerates how the protection was changed by the operation being audited. The following values and meanings apply: **0** - Indicates unchanged. **1** - Indicates added. **2** - Indicates changed. **3** - Indicates removed. | All |
| RecordType | The type of operation indicated by the record. This property indicates the service or feature that the operation was triggered in. For a list of record types and their corresponding ENUM value (which is the value displayed in the **RecordType** property in an audit record), see [Audit log record type](/en-us/office/office-365-management-api/office-365-management-activity-api-schema#auditlogrecordtype). |  |
| ResultStatus | Indicates whether the action (specified in the **Operation** property) was successful or not.  For Exchange admin activity, the value is either **True** (successful) or **False** (failed). | All |
| SecurityComplianceCenterEventType | Indicates that the activity was a Microsoft Purview portal activity. All Microsoft Purview portal activities have a value of **0** for this property. | Microsoft Purview portal |
| SensitivityLabel | The sensitivity label assigned to a specific mail item. | Exchange |
| SharingType | The type of sharing permissions that you assigned to the user that you shared the resource with. This user is identified in the **UserSharedWith** property. | SharePoint |
| Site | The GUID of the site where the file or folder accessed by the user is located. | SharePoint |
| SiteUrl | The URL of the site where the file or folder accessed by the user is located. | SharePoint |
| SourceFileExtension | The file extension of the file that the user accessed. This property is blank if the object that was accessed is a folder. | SharePoint |
| SourceFileName | The name of the file or folder accessed by the user. | SharePoint |
| SourceRelativeUrl | The URL of the folder that contains the file the user accessed. The combination of the values for the **SiteURL**, the **SourceRelativeURL**, and the **SourceFileName** property is the same as the value for the **ObjectID** property, which is the full path name for the file the user accessed. | SharePoint |
| Subject | The subject line of the message that was accessed. | Exchange (mailbox activity) |
| TabType | The type of tab added, removed, or updated in a team. The possible values for this property are: **Excel pin** - An Excel tab. **Extension** - All first-party and third-party apps; such as Class Schedule, VSTS, and Forms. **Notes** - OneNote tab. **Pdfpin** - A PDF tab. **Powerbi** - A Power BI tab. **Powerpointpin** - A PowerPoint tab. **Sharepointfiles** - A SharePoint tab. **Webpage** - A pinned website tab. **Wiki-tab** - A wiki tab. **Wordpin** - A Word tab. | Microsoft Teams |
| Target | The user that the action (identified in the **Operation** property) was performed on. For example, if a guest is added to SharePoint or a Microsoft Team, that user is listed in this property. | Microsoft Entra ID |
| TeamGuid | The ID of a team in Microsoft Teams. | Microsoft Teams |
| TeamName | The name of a team in Microsoft Teams. | Microsoft Teams |
| UserAgent | Information about the user's browser. The browser provides this information. | SharePoint |
| UserDomain | Identity information about the tenant organization of the user (actor) who performed the action. | Microsoft Entra ID |
| UserId | The user who performed the action (specified in the **Operation** property) that resulted in the record being logged. Audit records for activity performed by system accounts (such as SHAREPOINT\system or NT AUTHORITY\SYSTEM) are also included in the audit log. Another common value for the UserId property is app@sharepoint. This value indicates that the "user" who performed the activity was an application that has the necessary permissions in SharePoint to perform organization-wide actions (such as search a SharePoint site or OneDrive account) on behalf of a user, admin, or service. For more information, see:[The app@sharepoint user in audit records](audit-log-activities#the-appsharepoint-user-in-audit-records) or [System accounts in Exchange mailbox audit records](audit-log-activities#system-accounts-in-exchange-mailbox-audit-records). | All |
| UserKey | Contains a valid Microsoft Entra ID Object ID in GUID format or hex format. For scenarios where the primary actor isn't a user, the *UserKey* is an empty string. See UserType and UserKey scenarios for details on various *UserKey* scenarios. | All |
| UserType | The type of user that performed the operation. See the UserType and UserKey scenarios for details on various *UserType* scenarios. | All |
| Version | Indicates the version number of the activity (identified by the **Operation** property) that's logged. | All |
| Workload | The Microsoft 365 service where the activity occurred. | All |

## UserType and UserKey scenarios

The following table provides details for *UserType* and *UserKey* scenarios:

| Value | UserType member name | Description | UserKey |
| --- | --- | --- | --- |
| 0 | Regular | A regular user without admin permissions. | Microsoft Entra Object ID in GUID format |
| 2 | Admin | An administrator in your Microsoft 365 organization.^1^ | Microsoft Entra Object ID in GUID format |
| 3 | DCAdmin | A Microsoft datacenter administrator or datacenter system account. | Microsoft Entra Object ID in GUID format |
| 4 | System | An audit event triggered by server-side logic. For example, Windows services or background processes. | Guid.Empty.ToString() (or the value '00000000-0000-0000-0000-000000000000'). |
| 5 | Application | An audit event triggered by a Microsoft Entra application. | Microsoft Entra Application Name or Application ID (when available). Otherwise, an empty string. |
| 6 | ServicePrincipal | A service principal. | Guid.Empty.ToString() (or the value '00000000-0000-0000-0000-000000000000'). |
| 7 | CustomPolicy | A customer created or managed policy. | Guid.Empty.ToString() (or the value '00000000-0000-0000-0000-000000000000'). |
| 8 | SystemPolicy | A Microsoft-managed or system policy. | Guid.Empty.ToString() (or the value '00000000-0000-0000-0000-000000000000'). |
| 9 | PartnerTechnician | A partner tenant's user working on behalf of the customer tenant (in [GDAP](/en-us/partner-center/gdap-introduction) scenarios). | Guid.Empty.ToString() (or the value '00000000-0000-0000-0000-000000000000'). |
| 10 | Guest | A guest or anonymous user. | Guid.Empty.ToString() (or the value '00000000-0000-0000-0000-000000000000'). |
| 11 | Agent | An AI agent | Microsoft Entra Object ID of the primary agent in GUID format. |

Note

^1^ For Microsoft Entra related events, the value for an administrator isn't used in an audit record. Audit records for activities performed by administrators indicate that a regular user (for example, **UserType: 0**) performed the activity. The **UserID** property identifies the person (regular user or administrator) who performed the activity.