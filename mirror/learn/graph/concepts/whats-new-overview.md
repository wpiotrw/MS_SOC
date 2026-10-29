---
layout: Conceptual
title: What's new in Microsoft Graph - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/whats-new-overview
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: Lauragra
ms.author: MSGraphDocsVteam
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: non-product-specific
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: whats-new
description: Find out what's new in Microsoft Graph APIs, SDKs, documentation, and other resources.
ms.localizationpriority: high
ms.date: 2026-10-06T00:00:00.0000000Z
locale: en-us
document_id: 62dfb7e7-bb91-b6de-735b-97e63c2620df
document_version_independent_id: 7ac1c0c8-1433-e6c6-84a8-cbe00071fdd7
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/whats-new-overview.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: whats-new-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/whats-new-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/aebdc4a3-c54b-4eea-94e3-663d5e166f57
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/1baec8e6-ab38-4b56-bb59-f6282d94f311
platformId: 6e6097c9-5516-d241-0299-2adc10e56ea2
---

# What's new in Microsoft Graph - Microsoft Graph | Microsoft Learn

Microsoft Graph provides a unified programmability model that you can use to access data in Microsoft 365, Windows, and Enterprise Mobility + Security. This article provides information about what's new in Microsoft Graph APIs, documentation, SDKs, and more.

For more detailed API-level updates, see the [Microsoft Graph API changelog](https://developer.microsoft.com/graph/changelog/).

For details about previous updates to Microsoft Graph, see [Microsoft Graph what's new history](whats-new-earlier).

Important

Features in *preview* status are subject to change without notice, and might not be promoted to generally available (GA) status. Don't use preview features in production apps.

## October 2026: New and generally available

### Backup and recovery | Microsoft 365 backup and storage

- Use the **policyId** property on the [restoreSessionBase](/en-us/graph/api/resources/restoresessionbase) resource to scope restore sessions to a protection policy.
- Use the optional **policyId** parameter on the [restorePoint: search](/en-us/graph/api/restorepoint-search) method to validate protection-unit membership and improve policy-scoped routing. You can also filter the restore points collection by **protectionUnit/policyId**.
- Added the [getStatisticsByPolicy](/en-us/graph/api/backupreport-getstatisticsbypolicy) method to the [backupReport](/en-us/graph/api/resources/backupreport) resource type in v1.0. Use it to retrieve policy-level protection statistics for Microsoft 365 Backup Storage.

### Calendars

- Promoted the **isSharedWithMe** property of [calendar](/en-us/graph/api/resources/calendar) resource from beta to v1.0. The property is used to identify the shared calendars.
- Added the [delta](/en-us/graph/api/calendar-delta) method to the [calendar](/en-us/graph/api/resources/calendar) resource type. Use it to track calendars added, deleted, or updated in a user's mailbox.

### Calendars | Places

- Use the **lastUpdatedTime** and **customProperties** properties on the [place](/en-us/graph/api/resources/place) resource to read when a place was last updated and manage custom string key-value metadata.
- The [Place update](/en-us/graph/api/place-update) API doesn't honor administrative roles assigned to groups in Microsoft Entra ID. Instead, assign the required role directly to the user in Microsoft Entra ID, or assign it to a user or group through the Microsoft 365 admin center.

### Identity and access | Governance

- Added the [groupResource](/en-us/graph/api/resources/groupresource) resource type and the **resources** relationship to the [privilegedAccessGroup](/en-us/graph/api/resources/privilegedaccessgroup) resource. Use them to list and get groups managed through Privileged Identity Management (PIM) for groups.

### Mail | Message trace

Added support to identify recalled messages in message trace. Use `recalled` as a supported value of the **status** property of the [exchangeMessageTrace](/en-us/graph/api/resources/exchangemessagetrace) resource.

### Security | Audit log query

Added 35 members, from `PlannerCustomFieldDefinition` through `MESRawEmailContentMetadata`, to the [auditLogRecordType](/en-us/graph/api/resources/security-auditlogrecordtype) enumeration and added the matching [auditData derived types](/en-us/graph/api/resources/security-auditdata-derived-types) to represent workload-specific audit event payloads.

### Tasks and plans

Added support for single-value extended properties on [todoTask](/en-us/graph/api/resources/todotask) and [todoTaskList](/en-us/graph/api/resources/todotasklist) resources, enabling apps to store and retrieve custom data for Microsoft To Do tasks and task lists.

### Tenants | Tenant governance

Added the [refreshStatus](/en-us/graph/api/tenantgovernanceservices-relatedtenant-refreshstatus) method to get the status of the most recent related tenants refresh operation.

## October 2026: New in preview only

### Applications

Added the `audit` member to the **appManagementRestrictionState** enumeration type used by the [appManagementPolicy](/en-us/graph/api/resources/appmanagementpolicy?view=graph-rest-beta&amp;preserve-view=true) resource. Use this value to evaluate application management policy restrictions without enforcing them.

### Backup and recovery | Microsoft 365 backup and storage

- Track admin activities on backup and restore resources, including policy changes, dynamic rule executions, offboarding, and restore task completions, by using the [activityLogBase](/en-us/graph/api/resources/activitylogbase?view=graph-rest-beta&amp;preserve-view=true) resource and its derived types.
- Removed the **tags** property on the [restoreTaskActivityLog](/en-us/graph/api/resources/restoretaskactivitylog?view=graph-rest-beta&amp;preserve-view=true) in favor of the **restoreJobType** property. Use the **restoreJobType** property with values from the [restoreJobType](/en-us/graph/api/resources/enums?view=graph-rest-beta&amp;preserve-view=true#restorejobtype-values) enumeration type.
- Added the **backupPolicyDeleted** member as a new supported value for the **activityType** property on the [activityLogBase](/en-us/graph/api/resources/activitylogbase?view=graph-rest-beta&amp;preserve-view=true) resource and its derived types.

### Calendars | Places

The [Place update](/en-us/graph/api/place-update?view=graph-rest-beta&amp;preserve-view=true) API doesn't honor administrative roles assigned to groups in Microsoft Entra ID. Instead, assign the required role directly to the user in Microsoft Entra ID, or assign it to a user or group through the Microsoft 365 admin center.

### Device and app management | Cloud PC

- Updated the date when deprecated image properties on [cloudPcDeviceImage](/en-us/graph/api/resources/cloudpcdeviceimage?view=graph-rest-beta&amp;preserve-view=true), [cloudPcSourceDeviceImage](/en-us/graph/api/resources/cloudpcsourcedeviceimage?view=graph-rest-beta&amp;preserve-view=true), and [cloudPcGalleryImage](/en-us/graph/api/resources/cloudpcgalleryimage?view=graph-rest-beta&amp;preserve-view=true) will stop returning data from January 31, 2024 to December 7, 2026. No replacement is planned for **recommendedSku**. Review the replacement property guidance in these resource topics and update affected integrations before the deadline.
- Added support for extending Windows 365 Reserve access for multiple users through the [submitManagedLicenseOperation](/en-us/graph/api/cloudpcmanagedlicense-submitmanagedlicenseoperation?view=graph-rest-beta&amp;preserve-view=true) action on the [cloudPcManagedLicense](/en-us/graph/api/resources/cloudpcmanagedlicense?view=graph-rest-beta&amp;preserve-view=true) collection. Poll the submitted operation to check completion and inspect per-user results.
- Use the [retrieveManagedLicenseOperation](/en-us/graph/api/cloudpcmanagedlicense-retrievemanagedlicenseoperation?view=graph-rest-beta&amp;preserve-view=true) operation to retrieve the status and per-user results of a submitted operation.

### Device and app management | Device updates

- Added the [driverUpdatePolicy](/en-us/graph/api/resources/windowsupdates-driverupdatepolicy?view=graph-rest-beta&amp;preserve-view=true), [driverUpdateRing](/en-us/graph/api/resources/windowsupdates-driverupdatering?view=graph-rest-beta&amp;preserve-view=true), and [driverUpdateApprovalRule](/en-us/graph/api/resources/windowsupdates-driverupdateapprovalrule?view=graph-rest-beta&amp;preserve-view=true) resource types to manage driver and firmware update approvals and deployments with Windows Autopatch.
- Added the [featureUpdatePolicy](/en-us/graph/api/resources/windowsupdates-featureupdatepolicy?view=graph-rest-beta&amp;preserve-view=true) and [featureUpdateRing](/en-us/graph/api/resources/windowsupdates-featureupdatering?view=graph-rest-beta&amp;preserve-view=true) resource types to manage feature update deployments and gradual rollout settings with Windows Autopatch.
- Added the [tenantSetting](/en-us/graph/api/resources/windowsupdates-tenantsetting?view=graph-rest-beta&amp;preserve-view=true) and [mdmAppSetting](/en-us/graph/api/resources/windowsupdates-mdmappsetting?view=graph-rest-beta&amp;preserve-view=true) resource types to manage tenant-level and MDM application settings for Windows Autopatch.
- Added the [applicableCatalog](/en-us/graph/api/resources/windowsupdates-applicablecatalog?view=graph-rest-beta&amp;preserve-view=true) and [applicableDevice](/en-us/graph/api/resources/windowsupdates-applicabledevice?view=graph-rest-beta&amp;preserve-view=true) resource types to identify updates that apply to devices targeted by a Windows Autopatch policy.
- Added the [updateData](/en-us/graph/api/resources/windowsupdates-updatedata?view=graph-rest-beta&amp;preserve-view=true) resource type and related device profile, policy assignment, catalog applicability, and driver reporting resources to retrieve Windows Autopatch deployment data.

### Files

Updated the [getSharePointApiUsage](/en-us/graph/api/reportroot-getsharepointapiusage?view=graph-rest-beta&amp;preserve-view=true) method to support SharePoint service prioritization reports. Use this report to retrieve total, standard, heavy, billed standard, and billed heavy API request counts by application and date.

### Identity and access | Directory management

- Added the [objectConnection](/en-us/graph/api/resources/synchronization-objectconnection?view=graph-rest-beta&amp;preserve-view=true) resource type and related methods to inspect or clear cached connector data store linkage records.
- Added the **objectConnections** relationship to the [synchronizationJob](/en-us/graph/api/resources/synchronization-synchronizationjob?view=graph-rest-beta&amp;preserve-view=true) resource to access linkage records for known object identifiers.

### Identity and access | Governance

- Added the [accessDriftSummary](/en-us/graph/api/resources/accessdriftsummary?view=graph-rest-beta&amp;preserve-view=true) resource type and related methods for identifying governed resources whose actual access differs from access-package intent. Use it to list and inspect drift summaries, retrieve drift details, and download bulk reconciliation reports. Access drift details identify whether each affected identity is a user or group through the **identityType** property of [entraDriftIdentityInfo](/en-us/graph/api/resources/entradriftidentityinfo?view=graph-rest-beta&amp;preserve-view=true).
- Added methods to read and configure a user's [approverDelegate](/en-us/graph/api/resources/approverdelegate?view=graph-rest-beta&amp;preserve-view=true). Use them to delegate approval of Microsoft Entra entitlement management access package assignment requests and access reviews to another user or group for a specified period of time. Users can manage their own delegate, and Identity Governance Administrators can manage the delegate of any user.
- Added the **gracePeriodInDays** property to the [lifecyclePolicyRule](/en-us/graph/api/resources/identitygovernance-lifecyclepolicyrule?view=graph-rest-beta&amp;preserve-view=true) resource. Use it to configure an optional grace period for each lifecycle policy rule before the policy action sequence starts.
- Added the [roleManagementCustomCalloutExtension](/en-us/graph/api/resources/rolemanagementcustomcalloutextension?view=graph-rest-beta&amp;preserve-view=true) resource type and related methods for integrating external approval, ticketing, compliance, and audit workflows into Privileged Identity Management role assignment lifecycle events. Use these capabilities to associate custom extensions with role management policies, submit approval or denial results for Microsoft Entra role and group assignment requests, and optionally update assignment schedules.

### Identity and access | Identity and sign-in

- Added public preview support for OnPasswordUpdate custom authentication extensions. Use the [onPasswordUpdateCustomExtension](/en-us/graph/api/resources/onpasswordupdatecustomextension?view=graph-rest-beta&amp;preserve-view=true) resource to notify external systems after a self-service password reset and the [onPasswordUpdateListener](/en-us/graph/api/resources/onpasswordupdatelistener?view=graph-rest-beta&amp;preserve-view=true) resource to configure when the notification occurs.
- Added the [conditionalAccessPolicyPlan](/en-us/graph/api/resources/conditionalaccesspolicyplan?view=graph-rest-beta&amp;preserve-view=true) resource type and related methods for grouping shared Conditional Access conditions with scenario-specific rules. Use policy plans to consolidate common targeting conditions and manage rule-specific enforcement controls.

### Groups

Added the **mailboxId** property to the [group](/en-us/graph/api/resources/group?view=graph-rest-beta&amp;preserve-view=true) resource type to identify the Exchange mailbox associated with a Microsoft 365 group. The property is returned only when specified in `$select`.

### Mail | Message trace

Added support to identify recalled messages in message trace. Use `recalled` as a supported value of the **status** property of the [exchangeMessageTrace](/en-us/graph/api/resources/exchangemessagetrace?view=graph-rest-beta&amp;preserve-view=true) resource.

### Mailbox import and export

- Added the **isHidden** property to the [mailboxFolder](/en-us/graph/api/resources/mailboxfolder?view=graph-rest-beta&amp;preserve-view=true) resource to identify hidden mailbox folders.
- Use the existing **includeHiddenFolders** query parameter for [listing folders](/en-us/graph/api/mailbox-list-folders?view=graph-rest-beta&amp;preserve-view=true) and [listing child folders](/en-us/graph/api/mailboxfolder-list-childfolders?view=graph-rest-beta&amp;preserve-view=true). Set it to `true` to include both hidden and nonhidden folders.

### Reports | Identity and access reports

- Added the [appManagementAudit](/en-us/graph/api/resources/appmanagementaudit?view=graph-rest-beta&amp;preserve-view=true) resource type and related methods to retrieve Microsoft Entra application management audit logs. Use these APIs to understand how app management policy restrictions affected application and service principal changes.
- Added the `passwordUpdate` member to the **eventType** property of the [appliedAuthenticationEventListener](/en-us/graph/api/resources/appliedauthenticationeventlistener?view=graph-rest-beta&amp;preserve-view=true) resource to identify OnPasswordUpdate custom extension listeners triggered during sign-ins.

### Security

Added the **incidentConfiguration** property to the [detectionAction](/en-us/graph/api/resources/security-detectionaction?view=graph-rest-beta&amp;preserve-view=true) resource and the [incidentConfiguration](/en-us/graph/api/resources/security-incidentconfiguration?view=graph-rest-beta&amp;preserve-view=true) complex type. Use this setting to exclude alerts generated by a custom detection rule from automatic incident correlation and create standalone, single-alert incidents.

### Security | Audit log query

Added 35 members, from `PlannerCustomFieldDefinition` through `MESRawEmailContentMetadata`, to the [auditLogRecordType](/en-us/graph/api/resources/security-auditlogrecordtype?view=graph-rest-beta&amp;preserve-view=true) enumeration and added the matching [auditData derived types](/en-us/graph/api/resources/security-auditdata-derived-types?view=graph-rest-beta&amp;preserve-view=true) to represent workload-specific audit event payloads.

### Security | Case management

Clarified the existing maximum length of the **message** property on the [comment](/en-us/graph/api/resources/security-casemanagement-comment?view=graph-rest-beta&amp;preserve-view=true) resource: 1,000 characters for incident cases and 5,000 characters for generic cases. These limits apply when you [create a comment activity](/en-us/graph/api/security-casemanagement-case-post-activities?view=graph-rest-beta&amp;preserve-view=true). The 5,000-character limit also applies when you [update a comment activity](/en-us/graph/api/security-casemanagement-activity-update?view=graph-rest-beta&amp;preserve-view=true) in a generic case; the update of comment activities in incident cases remains unsupported.

### Security | Data security and compliance

Applications can now supply one or more sensitivity labels with file content submitted to the [processContent](/en-us/graph/api/userdatasecurityandgovernance-processcontent?view=graph-rest-beta&amp;preserve-view=true) API by using the **sensitivityLabels** property of [processContentMetadataBase](/en-us/graph/api/resources/processcontentmetadatabase?view=graph-rest-beta&amp;preserve-view=true).

Added the `unknownFutureValue` member to the [applicationMode](/en-us/graph/api/resources/enums?view=graph-rest-beta&amp;preserve-view=true#applicationmode-values) enumeration as a sentinel for future application modes.

Updated the **evaluationErrorType** enumeration to use customer-facing reasons for incomplete policy evaluations, and removed the **errorMessage** property from the [evaluationErrorDetail](/en-us/graph/api/resources/evaluationerrordetail?view=graph-rest-beta&amp;preserve-view=true) complex type. Use **errorType** to identify why an evaluation couldn't be completed.

### Security | Workbooks

- Added the [workbook](/en-us/graph/api/resources/security-workbook?view=graph-rest-beta&amp;preserve-view=true) resource type and related methods to manage tenant-scoped Microsoft Security workbook documents. Use stable IDs for repeatable deployments and replace a workbook's JSON content as a complete document.

### Teamwork and communications | Messaging

Added support for setting and unsetting custom emoji reactions on chat messages by specifying a display name (**displayName**), service-issued identifier (**reactionId**), or both. For more information, see [chatMessageReaction](/en-us/graph/api/resources/chatmessagereaction?view=graph-rest-beta&amp;preserve-view=true).

## September 2026: New and generally available

### Applications

- Updated the availability of the **coopEnforcement** property on the [authenticationBehaviors](/en-us/graph/api/resources/authenticationbehaviors) resource to include the supported national cloud deployments: US Government L4, US Government L5 (DoD), and China operated by 21Vianet.

### Calendars | Work hours and locations

Added app-only support to the [workHoursAndLocationsSetting](/en-us/graph/api/resources/workhoursandlocationssetting), [workPlanOccurrence](/en-us/graph/api/resources/workplanoccurrence), and [workPlanRecurrence](/en-us/graph/api/resources/workplanrecurrence) resources and related methods. Apps can use the `Calendars.Read.All` application permission to read a user's setting, recurrences, and occurrences, and `Calendars.ReadWrite.All` to create, update, and delete them.

### Change notifications

Promoted the `unknownFutureValue` member of the **changeType** enumeration from beta to v1.0. The enumeration is used by the [changeNotification](/en-us/graph/api/resources/changenotification) and [commsNotification](/en-us/graph/api/resources/commsnotification) resources to identify notification change types.

### Files

- Added the **isPatternToken** property to the [fileStorageContainerCustomPropertyValue](/en-us/graph/api/resources/filestoragecontainercustompropertyvalue) resource to indicate whether a custom property value is a `urlTemplate` pattern that consumers must resolve before use, rather than a literal value.
- Added the **isOfficeRestricted** property to the [fileStorageContainerTypeSettings](/en-us/graph/api/resources/filestoragecontainertypesettings) and [fileStorageContainerTypeRegistrationSettings](/en-us/graph/api/resources/filestoragecontainertyperegistrationsettings) resources, and the **fileStorageContainerTypeSettingsOverride** enumeration.
- Use the [revokeGrants](/en-us/graph/api/permission-revokegrants) method of the [permission](/en-us/graph/api/resources/permission) resource to revoke access to a sharing link for specified recipients.

### Groups

Added the **onPremisesExtensionAttributes** property to the [group](/en-us/graph/api/resources/group) resource. Use it to access extension attributes 1-15 synchronized from on-premises Active Directory.

### Identity and access | Directory management

- Added the [directoryRoleManagementDeletedItemContainer](/en-us/graph/api/resources/directoryrolemanagementdeleteditemcontainer) resource type and related methods to v1.0. Use these APIs to list and inspect soft-deleted custom roles, restore them to the active role definitions collection, or permanently delete them.
- Added the [provision](/en-us/graph/api/device-provision) action to the [device](/en-us/graph/api/resources/device) resource in v1.0 to enable approved Virtual Desktop Infrastructure (VDI) providers to provision devices in a customer's directory. Added the [provision](/en-us/graph/api/device-provision) action to the [device](/en-us/graph/api/resources/device) resource in v1.0 to enable approved Virtual Desktop Infrastructure (VDI) providers to provision devices in a customer's directory.

### Identity and access | Governance

- Added the [roleManagementCustomCalloutExtension](/en-us/graph/api/resources/rolemanagementcustomcalloutextension) resource type and related methods for integrating external approval, ticketing, compliance, and audit workflows into Privileged Identity Management role assignment lifecycle events.
- Promoted the **access reviews customer-provided data**APIs from beta to v1.0. Use them to review entitlement data that you upload for resources that Microsoft Entra doesn't discover itself, such as third-party applications. The promoted surface includes:
    - the **description** property on [accessReviewInstanceDecisionItemResource](/en-us/graph/api/resources/accessreviewinstancedecisionitemresource) to describe the resource under review.
    - [accessReviewInstanceDecisionItemPermission](/en-us/graph/api/resources/accessreviewinstancedecisionitempermission) complex type and the **permission** property on [accessReviewInstanceDecisionItem](/en-us/graph/api/resources/accessreviewinstancedecisionitem), which describe the permission that grants the principal access to the resource under review.
    - [accessReviewInstanceDecisionItemCustomDataProvidedResource](/en-us/graph/api/resources/accessreviewinstancedecisionitemcustomdataprovidedresource) complex type, which represents a decision item resource whose entitlement data is supplied by the customer rather than discovered by Microsoft Entra.
    - [batchApplyCustomDataProvidedResourceDecisions](/en-us/graph/api/accessreviewinstance-batchapplycustomdataprovidedresourcedecisions) method on [accessReviewInstance](/en-us/graph/api/resources/accessreviewinstance) to set the apply result on all decision items that match a customer-provided resource in one call.
    - [accessReviewInstanceDecisionItemApplyResult](/en-us/graph/api/resources/enums#accessreviewinstancedecisionitemapplyresult-values) enumeration type to represent the result of applying a recorded decision to the target resource.
- Clarified that the [List resources](/en-us/graph/api/accesspackagecatalog-list-resources) method returns SharePoint Online resources only when it's called with delegated permissions. To retrieve SharePoint site information with application permissions, use the [sites: getAllSites](/en-us/graph/api/site-getallsites) method.

### Identity and access | Identity and sign-in

- Added the [resourceAccountKeyAuthenticationMethod](/en-us/graph/api/resources/resourceaccountkeyauthenticationmethod) resource type and related methods for managing resource account key credentials on shared devices. Use the APIs to list, get, and delete credentials that enable devices such as Teams Rooms and Teams phones to sign in without user interaction.
- Added the [anonymousCalendarSharingFreeBusyDetail](/en-us/graph/api/resources/anonymouscalendarsharingfreebusydetail), [anonymousCalendarSharingFreeBusyReviewer](/en-us/graph/api/resources/anonymouscalendarsharingfreebusyreviewer), and [anonymousCalendarSharingFreeBusySimple](/en-us/graph/api/resources/anonymouscalendarsharingfreebusysimple) resource types. Use these cross-tenant access policy capabilities to authorize anonymous external users to view calendar free/busy information at different levels of detail.

### Security | Audit log query

Added the **isRecordCountLimitExceeded**, **recordCountLimit**, and **approximateReturnedRecordCount** properties to the [auditLogQuery](/en-us/graph/api/resources/security-auditlogquery) resource. Use these properties to determine whether a completed query exceeded the per-search record-count limit and to inspect the applicable limit and approximate returned record count.

### Teamwork and communications | Messaging

Updated the [getAllRetainedMessages](/en-us/graph/api/channel-getallretainedmessages) method to support exporting retained versions of private-channel messages that were edited or deleted after the tenant completed private-channel storage migration.

## September 2026: New in preview only

### Agents

Added the **isDisabled** property to the [agentIdentityBlueprint](/en-us/graph/api/resources/agentidentityblueprint?view=graph-rest-beta&amp;preserve-view=true) resource. Use it to deactivate an agent identity blueprint without deleting it.

### Applications

- Updated the availability of the **coopEnforcement** property on the [authenticationBehaviors](/en-us/graph/api/resources/authenticationbehaviors?view=graph-rest-beta&amp;preserve-view=true) resource to include the supported national cloud deployments: US Government L4, US Government L5 (DoD), and China operated by 21Vianet.
- Added the **isDeviceAccessEnabled** property to the [onPremisesPublishing](/en-us/graph/api/resources/onpremisespublishing?view=graph-rest-beta&amp;preserve-view=true) resource to configure device access for Microsoft Entra Private Access.

### Backup and recovery | Microsoft 365 backup and storage

- Added the **policyId** property to the [restoreSessionBase](/en-us/graph/api/resources/restoresessionbase?view=graph-rest-beta&amp;preserve-view=true) resource to scope restore sessions to a protection policy.
- Added the optional **policyId** parameter to the [restorePoint: search](/en-us/graph/api/restorepoint-search?view=graph-rest-beta&amp;preserve-view=true) method to validate protection-unit membership and improve policy-scoped routing. You can also filter the restore points collection by **protectionUnit/policyId**.

### Backup storage

- Added the [getStatisticsByPolicy](/en-us/graph/api/backupreport-getstatisticsbypolicy?view=graph-rest-beta&amp;preserve-view=true) method to retrieve policy-level protection statistics for Microsoft 365 Backup Storage. Use the report to monitor protected and unprotected artifacts across completed, in-progress, and failed states, review offboarding activity, and determine when the metrics were last calculated.

### Calendar | Places

- Added the [stringDictionary](/en-us/graph/api/resources/stringdictionary?view=graph-rest-beta&amp;preserve-view=true) resource type to represent custom string key-value pairs.
- Added the **customProperties** property to the [place](/en-us/graph/api/resources/place?view=graph-rest-beta&amp;preserve-view=true) resource type to store customer-defined string key-value pairs.
- Added the read-only **lastUpdatedTime** property to the [place](/en-us/graph/api/resources/place?view=graph-rest-beta&amp;preserve-view=true) resource type to indicate when the place was last updated.

### Calendars | Work hours and locations

Added app-only support to the [workHoursAndLocationsSetting](/en-us/graph/api/resources/workhoursandlocationssetting?view=graph-rest-beta&amp;preserve-view=true), [workPlanOccurrence](/en-us/graph/api/resources/workplanoccurrence?view=graph-rest-beta&amp;preserve-view=true), and [workPlanRecurrence](/en-us/graph/api/resources/workplanrecurrence?view=graph-rest-beta&amp;preserve-view=true) resources and related methods. Apps can use the `Calendars.Read.All` application permission to read a user's setting, recurrences, and occurrences, and `Calendars.ReadWrite.All` to create, update, and delete them.

### Change notifications

Added the `unknownFutureValue` member to the **changeType** enumeration used by the [changeNotification](/en-us/graph/api/resources/changenotification?view=graph-rest-beta&amp;preserve-view=true) resource to support forward-compatible notification change types.

### Device and app management | Cloud PC

- Added the **isDisasterRecoveryActive** property to the [cloudPC](/en-us/graph/api/resources/cloudpc?view=graph-rest-beta&amp;preserve-view=true) resource to indicate whether the Cloud PC currently runs in its disaster recovery region after a failover event.
- Use `failoverInProgress` and `failbackInProgress` as supported values for the **status** property on the [cloudPC](/en-us/graph/api/resources/cloudpc?view=graph-rest-beta&amp;preserve-view=true) and [cloudPcStatusSummary](/en-us/graph/api/resources/cloudpcstatussummary?view=graph-rest-beta&amp;preserve-view=true) resources.

### Files

- Added the **userObjectId** parameter to the [getByUser](/en-us/graph/api/filestoragecontainer-getbyuser?view=graph-rest-beta&amp;preserve-view=true) method on the [fileStorageContainer](/en-us/graph/api/resources/filestoragecontainer?view=graph-rest-beta&amp;preserve-view=true) resource to retrieve a list of file storage containers owned by a user by passing the user's Microsoft Entra ID object ID.
- Added the **isPatternToken** property to the [fileStorageContainerCustomPropertyValue](/en-us/graph/api/resources/filestoragecontainercustompropertyvalue?view=graph-rest-beta&amp;preserve-view=true) resource to indicate whether a custom property value is a `urlTemplate` pattern that consumers must resolve before use, rather than a literal value.

### Identity and access | Directory management

- Added the [directoryRoleManagementDeletedItemContainer](/en-us/graph/api/resources/directoryrolemanagementdeleteditemcontainer?view=graph-rest-beta&amp;preserve-view=true) resource type and related methods for recovering custom role definitions that have been deleted. Use these APIs to list and inspect soft-deleted custom roles, including when they were deleted through the **deletedDateTime** property, restore them to the active role definitions collection, or permanently delete them.
- Added the [provision](/en-us/graph/api/device-provision?view=graph-rest-beta&amp;preserve-view=true) action to the [device](/en-us/graph/api/resources/device?view=graph-rest-beta&amp;preserve-view=true) resource to enable approved Virtual Desktop Infrastructure (VDI) providers to provision devices in a customer's directory.

### Groups

- Added the **disableNesting** property to the [group](/en-us/graph/api/resources/group?view=graph-rest-beta&amp;preserve-view=true) resource. Use it to prevent other groups from being added as members of a security group.

### Identity and access | Directory management

Added the [provision](/en-us/graph/api/device-provision?view=graph-rest-beta&amp;preserve-view=true) action to the [device](/en-us/graph/api/resources/device?view=graph-rest-beta&amp;preserve-view=true) resource to enable approved Virtual Desktop Infrastructure (VDI) providers to provision devices in a customer's directory.

### Identity and access | Governance

- Added the [accessReviewCatalogScope](/en-us/graph/api/resources/accessreviewcatalogscope?view=graph-rest-beta&amp;preserve-view=true) resource to scope an access review to an entitlement management catalog. Use the **additionalCatalogResourceTypes** property to review access packages in the catalog, in addition to the groups, applications, and custom data provided resources that are always reviewed.
- Clarified that the [Get accessPackageResourceEnvironment](/en-us/graph/api/accesspackageresourceenvironment-get?view=graph-rest-beta&amp;preserve-view=true) method returns SharePoint Online resource environments only when it's called with delegated permissions. A SharePoint Online resource environment corresponds to a SharePoint root site, so to retrieve root site information with application permissions, use the [List sites](/en-us/graph/api/site-list?view=graph-rest-beta&amp;preserve-view=true) method with the `$filter=siteCollection/root ne null` query option.
- Added public preview support for lifecycle policies that govern agent identities and guest users. Use [lifecyclePolicy](/en-us/graph/api/resources/identitygovernance-lifecyclepolicy?view=graph-rest-beta&amp;preserve-view=true) and its derived policy types to configure scope, rules, workflow enforcement, impact evaluation, and processing reports.
- Added the [selectedAgentBuilderPlatformsSubjectSet](/en-us/graph/api/resources/identitygovernance-selectedagentbuilderplatformssubjectset?view=graph-rest-beta&amp;preserve-view=true) resource type to include only agent identities created by selected builder platforms in an agent identity lifecycle policy scope.
- Added guest-user lifecycle actions to [attest](/en-us/graph/api/user-attest?view=graph-rest-beta&amp;preserve-view=true), [add the signed-in user as a sponsor](/en-us/graph/api/user-addselfassponsor?view=graph-rest-beta&amp;preserve-view=true), and [remove the signed-in user as a sponsor](/en-us/graph/api/user-removeselfassponsor?view=graph-rest-beta&amp;preserve-view=true).

### Identity and access | Identity and sign-in

Added the **requireCertificateSidAlignment** property to the [x509CertificateAuthenticationMethodConfiguration](/en-us/graph/api/resources/x509certificateauthenticationmethodconfiguration?view=graph-rest-beta&amp;preserve-view=true) resource. Use it to require certificate SID alignment for hybrid and cloud-only users during certificate-based authentication.

### Identity and access | Monitoring & health

- Added support for tagging Microsoft Entra recommendations and their impacted resources. Use the [recommendation: addTag](/en-us/graph/api/recommendation-addtag?view=graph-rest-beta&amp;preserve-view=true), [recommendation: removeTag](/en-us/graph/api/recommendation-removetag?view=graph-rest-beta&amp;preserve-view=true), [impactedResource: addTag](/en-us/graph/api/impactedresource-addtag?view=graph-rest-beta&amp;preserve-view=true), and [impactedResource: removeTag](/en-us/graph/api/impactedresource-removetag?view=graph-rest-beta&amp;preserve-view=true) methods to manage the **tags** relationship, backed by the new [recommendationTag](/en-us/graph/api/resources/recommendationtag?view=graph-rest-beta&amp;preserve-view=true) resource. You can also add or remove a tag on up to 50 impacted resources in a single request by using the [impactedResource: addTag](/en-us/graph/api/impactedresource-addtag-collection?view=graph-rest-beta&amp;preserve-view=true) and [impactedResource: removeTag](/en-us/graph/api/impactedresource-removetag-collection?view=graph-rest-beta&amp;preserve-view=true) methods.
- Added alternate remediation states for recommendations and impacted resources. Use the [markPlanned](/en-us/graph/api/recommendation-markplanned?view=graph-rest-beta&amp;preserve-view=true), [acceptRisk](/en-us/graph/api/recommendation-acceptrisk?view=graph-rest-beta&amp;preserve-view=true), and [applyAlternateMitigation](/en-us/graph/api/recommendation-applyalternatemitigation?view=graph-rest-beta&amp;preserve-view=true) methods on the [recommendation](/en-us/graph/api/resources/recommendation?view=graph-rest-beta&amp;preserve-view=true) resource, and the corresponding methods on the [impactedResource](/en-us/graph/api/resources/impactedresource?view=graph-rest-beta&amp;preserve-view=true) resource.
- Added the `needsMoreAction` member to the **recommendationStatus** enumeration, and the `critical` member to the **recommendationPriority** enumeration.
- Added the [nistClassification](/en-us/graph/api/resources/nistclassification?view=graph-rest-beta&amp;preserve-view=true) resource and the **nistClassifications** property to the [recommendationBase](/en-us/graph/api/resources/recommendationbase?view=graph-rest-beta&amp;preserve-view=true) resource to map recommendations to NIST Cybersecurity Framework 2.0 functions and categories.
- Added the **categoryGroup** property (and the new **recommendationCategoryGroup** enumeration), **completedBySystemDateTime**, **completedByUserDateTime**, **failedReviewDateTime**, **needsMoreActionResourceCount**, **remediatedDateTime**, and **statusModifiedDateTime** properties to the [recommendationBase](/en-us/graph/api/resources/recommendationbase?view=graph-rest-beta&amp;preserve-view=true) resource. Added the `microsoftEntraSuite` member to the **requiredLicenses** enumeration and the **lastRefreshedDateTime** property to the [recommendationConfiguration](/en-us/graph/api/resources/recommendationconfiguration?view=graph-rest-beta&amp;preserve-view=true) resource.

### People and workplace intelligence | Analytics

Added the **sensitivityLabel** property to the [searchHit](/en-us/graph/api/resources/searchhit?view=graph-rest-beta&amp;preserve-view=true) resource type to provide sensitivity-label information for the search result resource.

### Reports | Partner billing reports

Added the [billedAggregatedUsage](/en-us/graph/api/resources/partners-billing-billedaggregatedusage?view=graph-rest-beta&amp;preserve-view=true) resource type and related export method for CSP partners to generate billed aggregated Azure usage reports for a specific invoice.

### Security | Audit log query

Added the **isRecordCountLimitExceeded**, **recordCountLimit**, and **approximateReturnedRecordCount** properties to the [auditLogQuery](/en-us/graph/api/resources/security-auditlogquery?view=graph-rest-beta&amp;preserve-view=true) resource. Use these properties to determine whether a completed query exceeded the per-search record-count limit and to inspect the applicable limit and approximate returned record count.

### Security | Case management

Added the [slaPolicyDefinition](/en-us/graph/api/resources/security-casemanagement-slapolicydefinition?view=graph-rest-beta&amp;preserve-view=true) resource type and related methods for managing SLA policies for each security case type. Use these APIs to configure scope, pause, and exit criteria and warning and breach timers.

### Security | Data security and compliance

- Added the `contentFiltering` member to the [userActivityTypes](/en-us/graph/api/resources/enums-security?view=graph-rest-beta&amp;preserve-view=true#useractivitytypes-values) enumeration used by the [compute protection scopes for a user](/en-us/graph/api/userprotectionscopecontainer-compute?view=graph-rest-beta&amp;preserve-view=true) and [compute protection scopes for a tenant](/en-us/graph/api/tenantprotectionscopecontainer-compute?view=graph-rest-beta&amp;preserve-view=true) APIs, enabling applications to determine whether data loss prevention policies govern content filtering before evaluating content.
- Updated the [contentActivity](/en-us/graph/api/resources/contentactivity?view=graph-rest-beta&amp;preserve-view=true) resource to support reporting Secure by Default policy evaluations that couldn't be completed. Enforcement planes can submit structured incomplete-inspection reasons through the existing content activity ingestion API.
- Added the **policyConfiguration** property to the [policyScopeBase](/en-us/graph/api/resources/policyscopebase?view=graph-rest-beta&amp;preserve-view=true) resource type. Enforcement planes can use the effective Secure by Default configuration returned by the protection scope APIs to determine whether to audit or block content when policy evaluation can't be completed.
- Added support for applying Microsoft Purview data loss prevention policies to agent interactions. Use [tenantProtectionScopeContainer: compute](/en-us/graph/api/tenantprotectionscopecontainer-compute?view=graph-rest-beta&amp;preserve-view=true) to retrieve agent policy scopes, and use the tenant-scoped [processContent](/en-us/graph/api/tenantdatasecurityandgovernance-processcontent?view=graph-rest-beta&amp;preserve-view=true) method to evaluate content exchanged between protected agents and users, other agents, or tools.

### Tasks and plans

Added the [plan](/en-us/graph/api/resources/plan?view=graph-rest-beta&amp;preserve-view=true) resource type for Planner Graph V4. Use these APIs to create and manage plans and tasks with richer scheduling, dependency, custom field, and chat capabilities than the existing Planner API surface.

### Teamwork and communications | Messaging

Updated the [getAllRetainedMessages](/en-us/graph/api/channel-getallretainedmessages?view=graph-rest-beta&amp;preserve-view=true) method to document support for retained private-channel message versions captured after the tenant's private-channel storage migration completed.

## Contribute to Microsoft Graph

Are there scenarios you'd like Microsoft Graph to support?

- Suggest and vote for new features by using the [Microsoft Graph Feedback Portal](https://aka.ms/graphfeedback). Some new features originate as popular requests from the developer community. The Microsoft Graph team regularly evaluates customer needs and releases new features to the beta (`https://graph.microsoft.com/beta`) and v1.0 (`https://graph.microsoft.com/v1.0`) endpoints.
- [Join](https://aka.ms/m365-dev-call) the weekly Microsoft 365 platform community call and become an active member of the Microsoft Graph community. To discover the full calendar of developer calls, visit the [Microsoft 365 and Power Platform community page](https://aka.ms/community/calls).
- [Join](https://ux.microsoft.com/Panel/M365Devs?utm_source=graphDocs) our research panel to provide your input on our developer experiences.