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
ms.date: 2026-10-01T00:00:00.0000000Z
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
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/aebdc4a3-c54b-4eea-94e3-663d5e166f57
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/1baec8e6-ab38-4b56-bb59-f6282d94f311
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 6e6097c9-5516-d241-0299-2adc10e56ea2
---

# What's new in Microsoft Graph - Microsoft Graph | Microsoft Learn

Microsoft Graph provides a unified programmability model that you can use to access data in Microsoft 365, Windows, and Enterprise Mobility + Security. This article provides information about what's new in Microsoft Graph APIs, documentation, SDKs, and more.

For more detailed API-level updates, see the [Microsoft Graph API changelog](https://developer.microsoft.com/graph/changelog/).

For details about previous updates to Microsoft Graph, see [Microsoft Graph what's new history](whats-new-earlier).

Important

Features in *preview* status are subject to change without notice, and might not be promoted to generally available (GA) status. Don't use preview features in production apps.

## October 2026: New and generally available

### Mail | Message trace

- Added support for identifying recalled messages in message trace. Use the [exchangeMessageTrace](/en-us/graph/api/resources/exchangemessagetrace) resource's **status** property, which can now return `recalled`.

## October 2026: New in preview only

### Backup and recovery | Microsoft 365 backup and storage

- Track admin activities on backup and restore resources, including policy changes, dynamic rule executions, offboarding, and restore task completions, by using the [activityLogBase](/en-us/graph/api/resources/activitylogbase?view=graph-rest-beta&amp;preserve-view=true) resource and its derived types.

### Mailbox import and export

- Added the **isHidden** property to the [mailboxFolder](/en-us/graph/api/resources/mailboxfolder?view=graph-rest-beta&amp;preserve-view=true) resource to identify hidden mailbox folders.
- Use the existing **includeHiddenFolders** query parameter for [listing folders](/en-us/graph/api/mailbox-list-folders?view=graph-rest-beta&amp;preserve-view=true) and [listing child folders](/en-us/graph/api/mailboxfolder-list-childfolders?view=graph-rest-beta&amp;preserve-view=true). Set it to `true` to include both hidden and nonhidden folders.

## September 2026: New and generally available

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

- Added the [provision](/en-us/graph/api/device-provision) action to the [device](/en-us/graph/api/resources/device) resource in v1.0 to enable approved Virtual Desktop Infrastructure (VDI) providers to provision devices in a customer's directory.

### Identity and access | Governance

- Promoted the **access reviews customer-provided data**APIs from beta to v1.0. Use them to review entitlement data that you upload for resources that Microsoft Entra doesn't discover itself, such as third-party applications. The promoted surface includes:
    - the **description** property on [accessReviewInstanceDecisionItemResource](/en-us/graph/api/resources/accessreviewinstancedecisionitemresource) to describe the resource under review.
    - [accessReviewInstanceDecisionItemPermission](/en-us/graph/api/resources/accessreviewinstancedecisionitempermission) complex type and the **permission** property on [accessReviewInstanceDecisionItem](/en-us/graph/api/resources/accessreviewinstancedecisionitem), which describe the permission that grants the principal access to the resource under review.
    - [accessReviewInstanceDecisionItemCustomDataProvidedResource](/en-us/graph/api/resources/accessreviewinstancedecisionitemcustomdataprovidedresource) complex type, which represents a decision item resource whose entitlement data is supplied by the customer rather than discovered by Microsoft Entra.
    - [batchApplyCustomDataProvidedResourceDecisions](/en-us/graph/api/accessreviewinstance-batchapplycustomdataprovidedresourcedecisions) method on [accessReviewInstance](/en-us/graph/api/resources/accessreviewinstance) to set the apply result on all decision items that match a customer-provided resource in one call.
    - [accessReviewInstanceDecisionItemApplyResult](/en-us/graph/api/resources/enums#accessreviewinstancedecisionitemapplyresult-values) enumeration type to represent the result of applying a recorded decision to the target resource.
- Clarified that the [List resources](/en-us/graph/api/accesspackagecatalog-list-resources) method returns SharePoint Online resources only when it's called with delegated permissions. To retrieve SharePoint site information with application permissions, use the [sites: getAllSites](/en-us/graph/api/site-getallsites) method.

### Identity and access | Identity and sign-in

Added the [anonymousCalendarSharingFreeBusyDetail](/en-us/graph/api/resources/anonymouscalendarsharingfreebusydetail), [anonymousCalendarSharingFreeBusyReviewer](/en-us/graph/api/resources/anonymouscalendarsharingfreebusyreviewer), and [anonymousCalendarSharingFreeBusySimple](/en-us/graph/api/resources/anonymouscalendarsharingfreebusysimple) resource types. Use these cross-tenant access policy capabilities to authorize anonymous external users to view calendar free/busy information at different levels of detail.

### Security | Audit log query

- Added the **isRecordCountLimitExceeded**, **recordCountLimit**, and **approximateReturnedRecordCount** properties to the [auditLogQuery](/en-us/graph/api/resources/security-auditlogquery) resource. Use these properties to determine whether a completed query exceeded the per-search record-count limit and to inspect the applicable limit and approximate returned record count.

### Teamwork and communications | Messaging

Updated the [getAllRetainedMessages](/en-us/graph/api/channel-getallretainedmessages) method to support exporting retained versions of private-channel messages that were edited or deleted after the tenant completed private-channel storage migration.

## September 2026: New in preview only

### Agents

Added the **isDisabled** property to the [agentIdentityBlueprint](/en-us/graph/api/resources/agentidentityblueprint?view=graph-rest-beta&amp;preserve-view=true) resource. Use it to deactivate an agent identity blueprint without deleting it.

### Application

Added the **isDeviceAccessEnabled** property to the [onPremisesPublishing](/en-us/graph/api/resources/onpremisespublishing?view=graph-rest-beta&amp;preserve-view=true) resource to configure device access for Microsoft Entra Private Access.

### Backup and recovery | Microsoft 365 backup and storage

- Added the **policyId** property to the [restoreSessionBase](/en-us/graph/api/resources/restoresessionbase?view=graph-rest-beta&amp;preserve-view=true) resource type to scope restore sessions to a protection policy.
- Added the optional **policyId** parameter to the [restorePoint: search](/en-us/graph/api/restorepoint-search?view=graph-rest-beta&amp;preserve-view=true) method to validate protection-unit membership and improve policy-scoped routing. You can also filter the restore points collection by `protectionUnit/policyId`.

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

- Added the [directoryRoleManagementDeletedItemContainer](/en-us/graph/api/resources/directoryrolemanagementdeleteditemcontainer?view=graph-rest-beta&amp;preserve-view=true) resource type and related methods for recovering custom role definitions that have been deleted. Use these APIs to list and inspect soft-deleted custom roles, restore them to the active role definitions collection, or permanently delete them.
- Added the [provision](/en-us/graph/api/device-provision?view=graph-rest-beta&amp;preserve-view=true) action to the [device](/en-us/graph/api/resources/device?view=graph-rest-beta&amp;preserve-view=true) resource to enable approved Virtual Desktop Infrastructure (VDI) providers to provision devices in a customer's directory.

### Groups

- Added the **disableNesting** property to the [group](/en-us/graph/api/resources/group?view=graph-rest-beta&amp;preserve-view=true) resource. Use it to prevent other groups from being added as members of a security group.

### Identity and access | Directory management

- Added the [provision](/en-us/graph/api/device-provision?view=graph-rest-beta&amp;preserve-view=true) action to the [device](/en-us/graph/api/resources/device?view=graph-rest-beta&amp;preserve-view=true) resource to enable approved Virtual Desktop Infrastructure (VDI) providers to provision devices in a customer's directory.

### Identity and access | Governance

Clarified that the [Get accessPackageResourceEnvironment](/en-us/graph/api/accesspackageresourceenvironment-get?view=graph-rest-beta&amp;preserve-view=true) method returns SharePoint Online resource environments only when it's called with delegated permissions. A SharePoint Online resource environment corresponds to a SharePoint root site, so to retrieve root site information with application permissions, use the [List sites](/en-us/graph/api/site-list?view=graph-rest-beta&amp;preserve-view=true) method with the `$filter=siteCollection/root ne null` query option.

- Added public preview support for lifecycle policies that govern agent identities and guest users. Use [lifecyclePolicy](/en-us/graph/api/resources/identitygovernance-lifecyclepolicy?view=graph-rest-beta&amp;preserve-view=true) and its derived policy types to configure scope, rules, workflow enforcement, impact evaluation, and processing reports.
- Added guest-user lifecycle actions to [attest](/en-us/graph/api/user-attest?view=graph-rest-beta&amp;preserve-view=true), [add the signed-in user as a sponsor](/en-us/graph/api/user-addselfassponsor?view=graph-rest-beta&amp;preserve-view=true), and [remove the signed-in user as a sponsor](/en-us/graph/api/user-removeselfassponsor?view=graph-rest-beta&amp;preserve-view=true).

### Identity and access | Identity and sign-in

Added the **requireCertificateSidAlignment** property to the [x509CertificateAuthenticationMethodConfiguration](/en-us/graph/api/resources/x509certificateauthenticationmethodconfiguration?view=graph-rest-beta&amp;preserve-view=true) resource. Use it to require certificate SID alignment for hybrid and cloud-only users during certificate-based authentication.

### People and workplace intelligence | Analytics

Added the **sensitivityLabel** property to the [searchHit](/en-us/graph/api/resources/searchhit?view=graph-rest-beta&amp;preserve-view=true) resource type to provide sensitivity-label information for the search result resource.

### Reports | Partner billing reports

Added the [billedAggregatedUsage](/en-us/graph/api/resources/partners-billing-billedaggregatedusage?view=graph-rest-beta&amp;preserve-view=true) resource type and related export method for CSP partners to generate billed aggregated Azure usage reports for a specific invoice.

### Security | Data security and compliance

Added the `contentFiltering` member to the [userActivityTypes](/en-us/graph/api/resources/enums-security?view=graph-rest-beta&amp;preserve-view=true#useractivitytypes-values) enumeration used by the [compute protection scopes for a user](/en-us/graph/api/userprotectionscopecontainer-compute?view=graph-rest-beta&amp;preserve-view=true) and [compute protection scopes for a tenant](/en-us/graph/api/tenantprotectionscopecontainer-compute?view=graph-rest-beta&amp;preserve-view=true) APIs, enabling applications to determine whether data loss prevention policies govern content filtering before evaluating content.

Updated the [contentActivity](/en-us/graph/api/resources/contentactivity?view=graph-rest-beta&amp;preserve-view=true) resource to support reporting Secure by Default policy evaluations that couldn't be completed. Enforcement planes can submit structured incomplete-inspection reasons through the existing content activity ingestion API.

### Security | Audit log query

- Added the **isRecordCountLimitExceeded**, **recordCountLimit**, and **approximateReturnedRecordCount** properties to the [auditLogQuery](/en-us/graph/api/resources/security-auditlogquery?view=graph-rest-beta&amp;preserve-view=true) resource. Use these properties to determine whether a completed query exceeded the per-search record-count limit and to inspect the applicable limit and approximate returned record count.

### Teamwork and communications | Messaging

Updated the [getAllRetainedMessages](/en-us/graph/api/channel-getallretainedmessages?view=graph-rest-beta&amp;preserve-view=true) method to document support for retained private-channel message versions captured after the tenant's private-channel storage migration completed.

## August 2026: New and generally available

### Applications

- Added the [authenticationBehaviors](/en-us/graph/api/resources/authenticationbehaviors) resource type and the **coopEnforcement** property to the v1.0 endpoint. Application owners can use the property to explicitly test Cross-Origin-Opener-Policy enforcement, temporarily suppress enforcement while remediating an incompatible browser authentication flow, or return to the service default. The property is available in the global service only and isn't available in national cloud deployments.
- Added the **authenticationBehaviors** property to the [application](/en-us/graph/api/resources/application) resource type in v1.0. Returned only on `$select`.

### Change notifications | Subscription

- Added support for delivering change notifications to Web Push endpoints (RFC 8291) for the [subscription](/en-us/graph/api/resources/subscription) resource type.
- Added the [getVapidPublicKey](/en-us/graph/api/subscription-getvapidpublickey) method to obtain the VAPID public key (RFC 8292) used when creating Web Push subscriptions.

### Files

- Added the [Upsert columns](/en-us/graph/api/filestoragecontainer-patch-columns) method to the [fileStorageContainer](/en-us/graph/api/resources/filestoragecontainer) resource type to create or update up to 20 columnDefinition objects in a single request.
- Added the **appliedByUser** parameter to the [assignSensitivityLabel](/en-us/graph/api/driveitem-assignsensitivitylabel) action on the [driveItem](/en-us/graph/api/resources/driveitem) resource. This parameter allows app-only callers to specify the user identity on whose behalf the sensitivity label is applied.

### Identity and access | Directory management

- Added the **managerApplications** property to the [agentIdentity](/en-us/graph/api/resources/agentidentity) and [agentIdentityBlueprintPrincipal](/en-us/graph/api/resources/agentidentityblueprintprincipal) resources to identify the applications that manage the backing agent identity blueprint.

Added the [recovery](/en-us/graph/api/resources/entrarecoveryservices-recovery) resource type and related methods to programmatically recover critical Microsoft Entra directory objects from automatically created point-in-time snapshots. Use these APIs to inspect available snapshots, preview and scope changes before restoration, run recovery jobs, monitor progress, and review failed changes.

### Identity and access | Governance

- Added the [externalSapAcConnectionInfo](/en-us/graph/api/resources/externalsapacconnectioninfo) complex type, along with the supporting [authenticationInfo](/en-us/graph/api/resources/authenticationinfo) and [clientCredentialAuthenticationInfo](/en-us/graph/api/resources/clientcredentialauthenticationinfo) types, to configure connections from Microsoft Entra entitlement management to SAP Access Control (AC) systems. Set these on the **connectionInfo** property of an [externalOriginResourceConnector](/en-us/graph/api/resources/externaloriginresourceconnector) when its **connectorType** is `sapAc`.
- Promoted the **Lifecycle Workflows provisioning and workflow subject**APIs from beta to v1.0, introducing a broader, extensible subject model for workflows and surfacing per-subject processing results. The promoted surface includes:
    - [workflowSubject](/en-us/graph/api/resources/identitygovernance-workflowsubject) base type and its [provisioningObjectWorkflowSubject](/en-us/graph/api/resources/identitygovernance-provisioningobjectworkflowsubject) and [directoryObjectWorkflowSubject](/en-us/graph/api/resources/identitygovernance-directoryobjectworkflowsubject) derived types
    - [subjectProcessingResult](/en-us/graph/api/resources/identitygovernance-subjectprocessingresult) resource with the **subjectProcessingResults** navigation property on the [run](/en-us/graph/api/resources/identitygovernance-run) and [workflow](/en-us/graph/api/resources/identitygovernance-workflow) resources
    - [subjectSummary](/en-us/graph/api/resources/identitygovernance-subjectsummary) resource and the [summary](/en-us/graph/api/identitygovernance-subjectprocessingresult-summary) method on the [subjectProcessingResult](/en-us/graph/api/resources/identitygovernance-subjectprocessingresult) resource
    - [activateAndWait](/en-us/graph/api/identitygovernance-workflow-activateandwait) action on the [workflow](/en-us/graph/api/resources/identitygovernance-workflow) resource, returning the [awaitedWorkflowProcessingResult](/en-us/graph/api/resources/identitygovernance-awaitedworkflowprocessingresult) resource
    - [provisioningAttributeMapping](/en-us/graph/api/resources/identitygovernance-provisioningattributemapping) and [attributeSetEntry](/en-us/graph/api/resources/identitygovernance-attributesetentry) resources
    - [customTaskExtensionResponseData](/en-us/graph/api/resources/identitygovernance-customtaskextensionresponsedata) resource, the **replyMode** property on [customTaskExtension](/en-us/graph/api/resources/identitygovernance-customtaskextension), and the **targetSubject** property on [customTaskExtensionCalloutData](/en-us/graph/api/resources/identitygovernance-customtaskextensioncalloutdata)
    - **targetSubjectType** property on [workflowBase](/en-us/graph/api/resources/identitygovernance-workflowbase) and **workflowSubject** property on [taskProcessingResult](/en-us/graph/api/resources/identitygovernance-taskprocessingresult)
    - [subjectType](/en-us/graph/api/resources/enums-identitygovernance#subjecttype-values) and [customTaskExtensionReplyMode](/en-us/graph/api/resources/enums-identitygovernance#customtaskextensionreplymode-values) enumerations, along with the `extensibility` and `extensibilityOnDemand` enumeration members
- Added the [externalOriginResourceConnector](/en-us/graph/api/resources/externaloriginresourceconnector) resource type and methods to [create](/en-us/graph/api/entitlementmanagement-post-externaloriginresourceconnectors), [list](/en-us/graph/api/entitlementmanagement-list-externaloriginresourceconnectors), [get](/en-us/graph/api/externaloriginresourceconnector-get), [update](/en-us/graph/api/externaloriginresourceconnector-update), and [delete](/en-us/graph/api/externaloriginresourceconnector-delete) connections from Microsoft Entra entitlement management to SAP Identity Access Governance (SAP IAG). For an SAP IAG connector, specify the SAP IAG endpoint, OAuth token endpoint, and client ID, along with the Azure subscription, resource group, key vault, and secret that identify where its client secret is stored. The connector is associated with an access package resource so that entitlement management can provision access to resources in SAP IAG through access packages.
- Added the **reviewerId** and **scopeType** properties to [accessReviewReviewerScope](/en-us/graph/api/resources/accessreviewreviewerscope) to specify a reviewer directly or as a well-known scope instead of through a query.
- Added the **applyDescription** property to [accessReviewInstanceDecisionItem](/en-us/graph/api/resources/accessreviewinstancedecisionitem) to describe the result of applying a decision.
- Added the **appRoleId** and **appRoleDisplayName** properties to [accessReviewInstanceDecisionItemServicePrincipalResource](/en-us/graph/api/resources/accessreviewinstancedecisionitemserviceprincipalresource) to identify the app role under review.
- Added the **errors** property to [accessReviewInstance](/en-us/graph/api/resources/accessreviewinstance) and the [accessReviewError](/en-us/graph/api/resources/accessreviewerror) resource type to report errors that occur during the review instance lifecycle.
- Added the [accessReviewPrincipalScope](/en-us/graph/api/resources/accessreviewprincipalscope), [accessReviewResourceScope](/en-us/graph/api/resources/accessreviewresourcescope), and [accessReviewAccessPackageAssignmentPolicyScope](/en-us/graph/api/resources/accessreviewaccesspackageassignmentpolicyscope) resource types. Use them in the **principalScopes** and **resourceScopes** properties of [principalResourceMembershipsScope](/en-us/graph/api/resources/principalresourcemembershipsscope) to state which principals have their access to which resources reviewed without writing a query expression.
- Added the **accessReviewPrincipalScopeType**, **accessReviewResourceScopeType**, and **accessReviewReviewerScopeType** enumeration types to identify well-known principal, resource, and reviewer scopes.

### Identity and access | Identity and sign-in

Added support for managing Microsoft 365 cross-tenant capabilities in cross-tenant access policies. Use the [m365CapabilityBase](/en-us/graph/api/resources/m365capabilitybase) resource and the **m365Capabilities** relationship to manage which Microsoft 365 experiences—such as calendar sharing, MailTips, places booking, and cross-tenant migration—are enabled between tenants. For the default policy, you can [list](/en-us/graph/api/crosstenantaccesspolicyconfigurationdefault-list-m365capabilities), [create](/en-us/graph/api/crosstenantaccesspolicyconfigurationdefault-post-m365capabilities), and [update](/en-us/graph/api/crosstenantaccesspolicyconfigurationdefault-update-m365capabilities) capabilities. For partner policies, you can [list](/en-us/graph/api/crosstenantaccesspolicyconfigurationpartner-list-m365capabilities), [create](/en-us/graph/api/crosstenantaccesspolicyconfigurationpartner-post-m365capabilities), [update](/en-us/graph/api/crosstenantaccesspolicyconfigurationpartner-update-m365capabilities), and [delete](/en-us/graph/api/crosstenantaccesspolicyconfigurationpartner-delete-m365capabilities) capabilities.

### Mail

- Added the [note](/en-us/graph/api/resources/note) resource type and methods to [list](/en-us/graph/api/user-list-notes), [create](/en-us/graph/api/user-post-notes), [get](/en-us/graph/api/note-get), [update](/en-us/graph/api/note-update), and [delete](/en-us/graph/api/note-delete) quick-capture notes in a user's *Notes* folder. Use [delta query](/en-us/graph/api/note-delta) to synchronize notes that were added, updated, or deleted since the previous request. You can also [list](/en-us/graph/api/note-list-attachments), [add](/en-us/graph/api/note-post-attachments), and [delete](/en-us/graph/api/attachment-delete) inline image attachments, and use open or legacy extended properties to store custom data on a note.

### Security | Alerts and incidents

- Added the **tenantId** property to the [userAccount](/en-us/graph/api/resources/security-useraccount) resource to provide the Entra home tenant ID for the compromised user account indicated in a [security alert](/en-us/graph/api/resources/security-alert) where the alert evidence is related to a [processEvidence](/en-us/graph/api/resources/security-processevidence), [userEvidence](/en-us/graph/api/resources/security-userevidence), or [mailboxEvidence](/en-us/graph/api/resources/security-mailboxevidence).
- Added the [alert: moveAlerts](/en-us/graph/api/security-alert-movealerts) and [incident: mergeIncidents](/en-us/graph/api/security-incident-mergeincidents) actions to support moving alerts and merging incidents in Microsoft Defender.
- Added the [correlationReason](/en-us/graph/api/resources/security-correlationreason) enumeration and [mergeResponse](/en-us/graph/api/resources/security-mergeresponse) resource type.

### Security | eDiscovery

Added the `cloudNativeHtmlConversion` member to the [additionalDataOptions](/en-us/graph/api/resources/security-ediscoveryaddtoreviewsetoperation#additionaldataoptions-values) enumeration.

### Mailbox import and export

- Added the **wellKnownName** property to the [mailboxFolder](/en-us/graph/api/resources/mailboxfolder) resource type in v1.0. Use this property to identify folders created by Outlook by using a locale-independent name.
- Added the [Delete mailboxItem](/en-us/graph/api/mailboxfolder-delete-items) method to the [mailboxItem](/en-us/graph/api/resources/mailboxitem) resource type in v1.0. Use this method to delete an individual mailbox item from a mailbox folder with Exchange soft-delete or hard-delete semantics.

### Security

Updated the retirement date for the legacy Microsoft Graph [security alerts API](/en-us/graph/api/resources/alert) from August 31, 2026 to October 15, 2026.

### Identity and access | Monitoring & health

- Added support for tagging Microsoft Entra recommendations and their impacted resources. Use the [recommendation: addTag](/en-us/graph/api/recommendation-addtag?view=graph-rest-beta&amp;preserve-view=true), [recommendation: removeTag](/en-us/graph/api/recommendation-removetag?view=graph-rest-beta&amp;preserve-view=true), [impactedResource: addTag](/en-us/graph/api/impactedresource-addtag?view=graph-rest-beta&amp;preserve-view=true), and [impactedResource: removeTag](/en-us/graph/api/impactedresource-removetag?view=graph-rest-beta&amp;preserve-view=true) methods to manage the **tags** relationship, backed by the new [recommendationTag](/en-us/graph/api/resources/recommendationtag?view=graph-rest-beta&amp;preserve-view=true) resource. You can also add or remove a tag on up to 50 impacted resources in a single request by using the [impactedResource: addTag](/en-us/graph/api/impactedresource-addtag-collection?view=graph-rest-beta&amp;preserve-view=true) and [impactedResource: removeTag](/en-us/graph/api/impactedresource-removetag-collection?view=graph-rest-beta&amp;preserve-view=true) methods.
- Added alternate remediation states for recommendations and impacted resources. Use the [markPlanned](/en-us/graph/api/recommendation-markplanned?view=graph-rest-beta&amp;preserve-view=true), [acceptRisk](/en-us/graph/api/recommendation-acceptrisk?view=graph-rest-beta&amp;preserve-view=true), and [applyAlternateMitigation](/en-us/graph/api/recommendation-applyalternatemitigation?view=graph-rest-beta&amp;preserve-view=true) methods on the [recommendation](/en-us/graph/api/resources/recommendation?view=graph-rest-beta&amp;preserve-view=true) resource, and the corresponding methods on the [impactedResource](/en-us/graph/api/resources/impactedresource?view=graph-rest-beta&amp;preserve-view=true) resource.
- Added the `needsMoreAction` member to the **recommendationStatus** enumeration, and the `critical` member to the **recommendationPriority** enumeration.
- Added the [nistClassification](/en-us/graph/api/resources/nistclassification?view=graph-rest-beta&amp;preserve-view=true) resource and the **nistClassifications** property to the [recommendationBase](/en-us/graph/api/resources/recommendationbase?view=graph-rest-beta&amp;preserve-view=true) resource to map recommendations to NIST Cybersecurity Framework 2.0 functions and categories.
- Added the **categoryGroup** property (and the new **recommendationCategoryGroup** enumeration), **completedBySystemDateTime**, **completedByUserDateTime**, **failedReviewDateTime**, **needsMoreActionResourceCount**, **remediatedDateTime**, and **statusModifiedDateTime** properties to the [recommendationBase](/en-us/graph/api/resources/recommendationbase?view=graph-rest-beta&amp;preserve-view=true) resource. Added the `microsoftEntraSuite` member to the **requiredLicenses** enumeration and the **lastRefreshedDateTime** property to the [recommendationConfiguration](/en-us/graph/api/resources/recommendationconfiguration?view=graph-rest-beta&amp;preserve-view=true) resource.

### People and workplace intelligence | Analytics

Added the **sensitivityLabel** property to the [searchHit](/en-us/graph/api/resources/searchhit?view=graph-rest-beta&amp;preserve-view=true) resource type to provide sensitivity-label information for the search result resource.

### Security

Added the **incidentConfiguration** property to the [detectionAction](/en-us/graph/api/resources/security-detectionaction?view=graph-rest-beta&amp;preserve-view=true) resource and the [incidentConfiguration](/en-us/graph/api/resources/security-incidentconfiguration?view=graph-rest-beta&amp;preserve-view=true) complex type. Use this setting to exclude alerts generated by a custom detection rule from automatic incident correlation and create standalone, single-alert incidents.

### Security | Audit log query

- Added the **isRecordCountLimitExceeded**, **recordCountLimit**, and **approximateReturnedRecordCount** properties to the [auditLogQuery](/en-us/graph/api/resources/security-auditlogquery?view=graph-rest-beta&amp;preserve-view=true) resource. Use these properties to determine whether a completed query exceeded the per-search record-count limit and to inspect the applicable limit and approximate returned record count.

### Security | Data security and compliance

Added the `contentFiltering` member to the [userActivityTypes](/en-us/graph/api/resources/enums-security?view=graph-rest-beta&amp;preserve-view=true#useractivitytypes-values) enumeration used by the [compute protection scopes for a user](/en-us/graph/api/userprotectionscopecontainer-compute?view=graph-rest-beta&amp;preserve-view=true) and [compute protection scopes for a tenant](/en-us/graph/api/tenantprotectionscopecontainer-compute?view=graph-rest-beta&amp;preserve-view=true) APIs, enabling applications to determine whether data loss prevention policies govern content filtering before evaluating content.

Added the **policyConfiguration** property to the [policyScopeBase](/en-us/graph/api/resources/policyscopebase?view=graph-rest-beta&amp;preserve-view=true) resource type. Enforcement planes can use the effective Secure by Default configuration returned by the protection scope APIs to determine whether to audit or block content when policy evaluation can't be completed.

Updated the [contentActivity](/en-us/graph/api/resources/contentactivity?view=graph-rest-beta&amp;preserve-view=true) resource to support reporting Secure by Default policy evaluations that couldn't be completed. Enforcement planes can submit structured incomplete-inspection reasons through the existing content activity ingestion API

### Teamwork and communications | Messaging

Updated the [getAllRetainedMessages](/en-us/graph/api/channel-getallretainedmessages?view=graph-rest-beta&amp;preserve-view=true) method to document support for retained private-channel message versions captured after the tenant's private-channel storage migration completed.

## Contribute to Microsoft Graph

Are there scenarios you'd like Microsoft Graph to support?

- Suggest and vote for new features by using the [Microsoft Graph Feedback Portal](https://aka.ms/graphfeedback). Some new features originate as popular requests from the developer community. The Microsoft Graph team regularly evaluates customer needs and releases new features to the beta (`https://graph.microsoft.com/beta`) and v1.0 (`https://graph.microsoft.com/v1.0`) endpoints.
- [Join](https://aka.ms/m365-dev-call) the weekly Microsoft 365 platform community call and become an active member of the Microsoft Graph community. To discover the full calendar of developer calls, visit the [Microsoft 365 and Power Platform community page](https://aka.ms/community/calls).
- [Join](https://ux.microsoft.com/Panel/M365Devs?utm_source=graphDocs) our research panel to provide your input on our developer experiences.