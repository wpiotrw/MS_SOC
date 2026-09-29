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
ms.date: 2026-09-14T00:00:00.0000000Z
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
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 6e6097c9-5516-d241-0299-2adc10e56ea2
---

# What's new in Microsoft Graph - Microsoft Graph | Microsoft Learn

Microsoft Graph provides a unified programmability model that you can use to access data in Microsoft 365, Windows, and Enterprise Mobility + Security. This article provides information about what's new in Microsoft Graph APIs, documentation, SDKs, and more.

For more detailed API-level updates, see the [Microsoft Graph API changelog](https://developer.microsoft.com/graph/changelog/).

For details about previous updates to Microsoft Graph, see [Microsoft Graph what's new history](whats-new-earlier).

Important

Features in *preview* status are subject to change without notice, and might not be promoted to generally available (GA) status. Don't use preview features in production apps.

## September 2026: New and generally available

### Files

Added the **isPatternToken** property to the [fileStorageContainerCustomPropertyValue](/en-us/graph/api/resources/filestoragecontainercustompropertyvalue) resource to indicate whether a custom property value is a `urlTemplate` pattern that consumers must resolve before use, rather than a literal value.

### Groups

Added the **onPremisesExtensionAttributes** property to the [group](/en-us/graph/api/resources/group) resource. Use it to access extension attributes 1-15 synchronized from on-premises Active Directory.

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

### Teamwork and communications | Messaging

Updated the [getAllRetainedMessages](/en-us/graph/api/channel-getallretainedmessages) method to support exporting retained versions of private-channel messages that were edited or deleted after the tenant completed private-channel storage migration.

## September 2026: New in preview only

### Agents

Added the **isDisabled** property to the [agentIdentityBlueprint](/en-us/graph/api/resources/agentidentityblueprint?view=graph-rest-beta&amp;preserve-view=true) resource. Use it to deactivate an agent identity blueprint without deleting it.

### Backup and recovery | Microsoft 365 backup and storage

- Added the **policyId** property to the [restoreSessionBase](/en-us/graph/api/resources/restoresessionbase?view=graph-rest-beta&amp;preserve-view=true) resource type to scope restore sessions to a protection policy.
- Added the optional **policyId** parameter to the [restorePoint: search](/en-us/graph/api/restorepoint-search?view=graph-rest-beta&amp;preserve-view=true) method to validate protection-unit membership and improve policy-scoped routing. You can also filter the restore points collection by `protectionUnit/policyId`.

### Backup storage

- Added the [getStatisticsByPolicy](/en-us/graph/api/backupreport-getstatisticsbypolicy?view=graph-rest-beta&amp;preserve-view=true) method to retrieve policy-level protection statistics for Microsoft 365 Backup Storage. Use the report to monitor protected and unprotected artifacts across completed, in-progress, and failed states, review offboarding activity, and determine when the metrics were last calculated.

### Calendar | Places

- Added the [stringDictionary](/en-us/graph/api/resources/stringdictionary?view=graph-rest-beta&amp;preserve-view=true) resource type to represent custom string key-value pairs.
- Added the **customProperties** property to the [place](/en-us/graph/api/resources/place?view=graph-rest-beta&amp;preserve-view=true) resource type to store customer-defined string key-value pairs.
- Added the read-only **lastUpdatedTime** property to the [place](/en-us/graph/api/resources/place?view=graph-rest-beta&amp;preserve-view=true) resource type to indicate when the place was last updated.

### Device and app management | Cloud PC

- Added the **isDisasterRecoveryActive** property to the [cloudPC](/en-us/graph/api/resources/cloudpc?view=graph-rest-beta&amp;preserve-view=true) resource to indicate whether the Cloud PC currently runs in its disaster recovery region after a failover event.
- Use `failoverInProgress` and `failbackInProgress` as supported values for the **status** property on the [cloudPC](/en-us/graph/api/resources/cloudpc?view=graph-rest-beta&amp;preserve-view=true) and [cloudPcStatusSummary](/en-us/graph/api/resources/cloudpcstatussummary?view=graph-rest-beta&amp;preserve-view=true) resources.

### Files

- Added the **userObjectId** parameter to the [getByUser](/en-us/graph/api/filestoragecontainer-getbyuser?view=graph-rest-beta&amp;preserve-view=true) method on the [fileStorageContainer](/en-us/graph/api/resources/filestoragecontainer?view=graph-rest-beta&amp;preserve-view=true) resource to retrieve a list of file storage containers owned by a user by passing the user's Microsoft Entra ID object ID.
- Added the **isPatternToken** property to the [fileStorageContainerCustomPropertyValue](/en-us/graph/api/resources/filestoragecontainercustompropertyvalue?view=graph-rest-beta&amp;preserve-view=true) resource to indicate whether a custom property value is a `urlTemplate` pattern that consumers must resolve before use, rather than a literal value.

### Identity and access | Directory management

- Added the [provision](/en-us/graph/api/device-provision?view=graph-rest-beta&amp;preserve-view=true) action to the [device](/en-us/graph/api/resources/device?view=graph-rest-beta&amp;preserve-view=true) resource to enable approved Virtual Desktop Infrastructure (VDI) providers to provision devices in a customer's directory.

### Groups

- Added the **disableNesting** property to the [group](/en-us/graph/api/resources/group?view=graph-rest-beta&amp;preserve-view=true) resource. Use it to prevent other groups from being added as members of a security group.

### Identity and access | Governance

Clarified that the [Get accessPackageResourceEnvironment](/en-us/graph/api/accesspackageresourceenvironment-get?view=graph-rest-beta&amp;preserve-view=true) method returns SharePoint Online resource environments only when it's called with delegated permissions. A SharePoint Online resource environment corresponds to a SharePoint root site, so to retrieve root site information with application permissions, use the [List sites](/en-us/graph/api/site-list?view=graph-rest-beta&amp;preserve-view=true) method with the `$filter=siteCollection/root ne null` query option.

### People and workplace intelligence | Analytics

Added the **sensitivityLabel** property to the [searchHit](/en-us/graph/api/resources/searchhit?view=graph-rest-beta&amp;preserve-view=true) resource type to provide sensitivity-label information for the search result resource.

### Security | Data security and compliance

Added the `contentFiltering` member to the [userActivityTypes](/en-us/graph/api/resources/enums-security?view=graph-rest-beta&amp;preserve-view=true#useractivitytypes-values) enumeration used by the [compute protection scopes for a user](/en-us/graph/api/userprotectionscopecontainer-compute?view=graph-rest-beta&amp;preserve-view=true) and [compute protection scopes for a tenant](/en-us/graph/api/tenantprotectionscopecontainer-compute?view=graph-rest-beta&amp;preserve-view=true) APIs, enabling applications to determine whether data loss prevention policies govern content filtering before evaluating content.

Added the **policyConfiguration** property to the [policyScopeBase](/en-us/graph/api/resources/policyscopebase?view=graph-rest-beta&amp;preserve-view=true) resource type. Enforcement planes can use the effective Secure by Default configuration returned by the protection scope APIs to determine whether to audit or block content when policy evaluation can't be completed.

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

### Teamwork and communications | Calls and online meetings

- Updated the [getAllRecordings](/en-us/graph/api/onlinemeeting-getallrecordings) and [getAllTranscripts](/en-us/graph/api/onlinemeeting-getalltranscripts) methods to document a service-update issue that can cause paginated requests to return an empty collection followed by duplicate items.
- Updated the [getAllRecordings](/en-us/graph/api/onlinemeeting-getallrecordings) method to return a Microsoft Graph URL that you can use to download recording content.

### Tenants | Tenant governance

- Promoted the [tenantGovernance](/en-us/graph/api/resources/tenantgovernanceservices-tenantgovernance) resource type and related methods from beta to v1.0 for discovering related tenants and managing governance invitations, requests, relationships, settings, and policy templates across Microsoft Entra tenants.

## August 2026: New in preview only

### Applications

- Added the **coopEnforcement** property to the [authenticationBehaviors](/en-us/graph/api/resources/authenticationbehaviors?view=graph-rest-beta&amp;preserve-view=true) resource. Application owners can use it to explicitly test Cross-Origin-Opener-Policy enforcement, temporarily suppress enforcement while remediating an incompatible browser authentication flow, or return to the service default.

### Device and app management | Cloud licensing

Added cloud licensing support for devices, enabling license assignment and usage tracking for device-based licensing scenarios. The new capabilities include:

- Added the [deviceCloudLicensing](/en-us/graph/api/resources/cloudlicensing-devicecloudlicensing?view=graph-rest-beta&amp;preserve-view=true) resource type and the **cloudLicensing** property to the [device](/en-us/graph/api/resources/device?view=graph-rest-beta&amp;preserve-view=true) resource.
- Use the [List usageRights for device](/en-us/graph/api/cloudlicensing-devicecloudlicensing-list-usagerights?view=graph-rest-beta&amp;preserve-view=true) method to retrieve usage rights granted to a device through direct assignments and transitive group-based assignments.
- Use the [Create assignment for device](/en-us/graph/api/cloudlicensing-devicecloudlicensing-post-assignments?view=graph-rest-beta&amp;preserve-view=true) method to assign licenses directly to devices.
- Use the [List waitingMembers for device](/en-us/graph/api/cloudlicensing-devicecloudlicensing-list-waitingmembers?view=graph-rest-beta&amp;preserve-view=true) method to retrieve devices in the waiting room due to license capacity limits.

### Device and app management | Cloud PC

- Added the [retrieveCloudPcPerformanceMetricsReport](/en-us/graph/api/cloudpcreports-retrievecloudpcperformancemetricsreport?view=graph-rest-beta&amp;preserve-view=true) method to the [cloudPcReports](/en-us/graph/api/resources/cloudpcreports?view=graph-rest-beta&amp;preserve-view=true) resource type. Use it to get VM-level utilization and performance metrics for a specific Cloud PC, including CPU, memory, and network metrics.

### Files

- Added the [Upsert columns](/en-us/graph/api/filestoragecontainer-patch-columns?view=graph-rest-beta&amp;preserve-view=true) method to the [fileStorageContainer](/en-us/graph/api/resources/filestoragecontainer?view=graph-rest-beta&amp;preserve-view=true) resource type to create or update up to 20 columnDefinition objects in a single request.
- Added the **appliedByUser** parameter to the [assignSensitivityLabel](/en-us/graph/api/driveitem-assignsensitivitylabel?view=graph-rest-beta&amp;preserve-view=true) action on the [driveItem](/en-us/graph/api/resources/driveitem?view=graph-rest-beta&amp;preserve-view=true) resource. This parameter allows app-only callers to specify the user identity on whose behalf the sensitivity label is applied, enabling label assignment for SharePoint Embedded containers.

### Identity and access | Governance

- Added support for configurable time-based lifecycle workflow triggers through the [timeBasedAttributeTriggerV2](/en-us/graph/api/resources/identitygovernance-timebasedattributetriggerv2?view=graph-rest-beta&amp;preserve-view=true) resource. Select a date-type user attribute and configure an operator to run workflows on an exact date, within a rolling window, or between two offsets before or after that date.

### Identity and access | Identity and sign-in

- Added the [anonymousCalendarSharingFreeBusySimple](/en-us/graph/api/resources/anonymouscalendarsharingfreebusysimple?view=graph-rest-beta&amp;preserve-view=true), [anonymousCalendarSharingFreeBusyDetail](/en-us/graph/api/resources/anonymouscalendarsharingfreebusydetail?view=graph-rest-beta&amp;preserve-view=true), and [anonymousCalendarSharingFreeBusyReviewer](/en-us/graph/api/resources/anonymouscalendarsharingfreebusyreviewer?view=graph-rest-beta&amp;preserve-view=true) capabilities that derive from [m365CapabilityBase](/en-us/graph/api/resources/m365capabilitybase?view=graph-rest-beta&amp;preserve-view=true). Use these capabilities in cross-tenant access policies to authorize anonymous external users to view calendar free/busy information at simple, detailed, or reviewer fidelity.

### Mail

- Changed the **members** property on the [distributionList](/en-us/graph/api/resources/distributionlist?view=graph-rest-beta&amp;preserve-view=true) resource to an expandable relationship. Use `$expand=members` with the [Get distribution list](/en-us/graph/api/distributionlist-get?view=graph-rest-beta&amp;preserve-view=true) method instead of the removed standalone methods for listing and getting members.

### People and workplace intelligence

- Updated [Manage profile source precedence in Microsoft 365](/en-us/graph/profilepriority-configure-profilepropertysetting) to clarify supported data sources for HR and work position data, explain how source precedence affects single-value versus multi-value properties, and add guidance on correctly configuring and removing tenant-level settings using the Microsoft Graph API or PowerShell.
- Added the [People data sources in Microsoft 365](/en-us/graph/people-data-sources) concept article that describes the data sources that build the Microsoft 365 user profile, including Microsoft Entra ID, Copilot connectors, Organizational data, SharePoint, People Skills, user edits, and the API user source. The article also provides a reference table of built-in source IDs (GUIDs) and explains how source metadata appears in the profile API output.

### Security | Advanced hunting

- Added the [getHuntingSchemaTables](/en-us/graph/api/security-security-gethuntingschematables?view=graph-rest-beta&amp;preserve-view=true) function to the [security](/en-us/graph/api/resources/security?view=graph-rest-beta&amp;preserve-view=true) resource. Use it to retrieve only the advanced hunting tables that the signed-in user can access, returned as a collection so that you can apply OData query parameters to request a targeted subset of tables and columns.

### Security | Alerts and incidents

- Added the [createAlert](/en-us/graph/api/security-alert-createalert?view=graph-rest-beta&amp;preserve-view=true) action to the [alert](/en-us/graph/api/resources/security-alert?view=graph-rest-beta&amp;preserve-view=true) resource for creating Microsoft 365 Defender alerts programmatically, including alert properties, incident-linking options, workspace routing, and inline entity definitions in a single request.

### Security | Case management

- Added the **slaPolicies** property to the [case](/en-us/graph/api/resources/security-casemanagement-case?view=graph-rest-beta&amp;preserve-view=true) resource type, a read-only collection of [caseSlaPolicyEntry](/en-us/graph/api/resources/security-casemanagement-caseslapolicyentry?view=graph-rest-beta&amp;preserve-view=true) objects that report the current status and breach target time of each SLA policy applied to a case.
- Added the [download attachment content](/en-us/graph/api/security-casemanagement-attachment-download-content?view=graph-rest-beta&amp;preserve-view=true) and [upload attachment content](/en-us/graph/api/security-casemanagement-attachment-upload-content?view=graph-rest-beta&amp;preserve-view=true) methods to the [attachment](/en-us/graph/api/resources/security-casemanagement-attachment?view=graph-rest-beta&amp;preserve-view=true) resource type to transfer case evidence in chunks and retrieve it after malware scanning.
- Added the [get relation](/en-us/graph/api/security-casemanagement-relation-get?view=graph-rest-beta&amp;preserve-view=true) and [delete relation](/en-us/graph/api/security-casemanagement-relation-delete?view=graph-rest-beta&amp;preserve-view=true) methods to the [relation](/en-us/graph/api/resources/security-casemanagement-relation?view=graph-rest-beta&amp;preserve-view=true) resource type to read and remove links between a case and related security resources.
- Added the [delete task](/en-us/graph/api/security-casemanagement-task-delete?view=graph-rest-beta&amp;preserve-view=true) method to the [task](/en-us/graph/api/resources/security-casemanagement-task?view=graph-rest-beta&amp;preserve-view=true) resource type to remove a task from a case.

### Security | Data security and compliance

- Added the `privacyDataMatch`, `aiPowered`, and `unknownFutureValue` members to the **classificationMethod** enumeration for the [sensitiveType](/en-us/graph/api/resources/sensitivetype?view=graph-rest-beta&amp;preserve-view=true) resource. These members support privacy data matching based on tenant data, AI-powered classification that can benefit from supported caller-supplied embeddings, and forward-compatible handling of future values.
- Replaced the **offsetChunks** property and **embeddingOffsetChunk** resource type with the **chunkOffsets** property and [chunkOffsets](/en-us/graph/api/resources/chunkoffsets?view=graph-rest-beta&amp;preserve-view=true) complex type in [embeddingInput](/en-us/graph/api/resources/embeddinginput?view=graph-rest-beta&amp;preserve-view=true). Use **chunkOffsets** to associate precomputed embedding vectors with their source text ranges by using base64-encoded start positions and lengths.

### Teamwork and communications | Calls and online meetings

- Updated the [getAllRecordings](/en-us/graph/api/onlinemeeting-getallrecordings?view=graph-rest-beta&amp;preserve-view=true) and [getAllTranscripts](/en-us/graph/api/onlinemeeting-getalltranscripts?view=graph-rest-beta&amp;preserve-view=true) methods to document a service-update issue that can cause paginated requests to return an empty collection followed by duplicate items.

### Teamwork and communications | Messaging

- Added the [agentCommunicationConfiguration](/en-us/graph/api/resources/agentcommunicationconfiguration?view=graph-rest-beta&amp;preserve-view=true) resource type and related methods to configure how agents send and receive messages in Microsoft Teams. Define default communication settings on an [agentIdentityBlueprint](/en-us/graph/api/resources/agentidentityblueprint?view=graph-rest-beta&amp;preserve-view=true) and override them for a specific agent on [agentIdentity](/en-us/graph/api/resources/agentidentity?view=graph-rest-beta&amp;preserve-view=true).
- Added the [reorder sections](/en-us/graph/api/teamworksection-reorder?view=graph-rest-beta&amp;preserve-view=true) and [reorder section items](/en-us/graph/api/teamworksectionitem-reorder?view=graph-rest-beta&amp;preserve-view=true) actions. Use these actions to apply a complete custom order to a user's sections or to the items in a user-defined section.

## Contribute to Microsoft Graph

Are there scenarios you'd like Microsoft Graph to support?

- Suggest and vote for new features by using the [Microsoft Graph Feedback Portal](https://aka.ms/graphfeedback). Some new features originate as popular requests from the developer community. The Microsoft Graph team regularly evaluates customer needs and releases new features to the beta (`https://graph.microsoft.com/beta`) and v1.0 (`https://graph.microsoft.com/v1.0`) endpoints.
- [Join](https://aka.ms/m365-dev-call) the weekly Microsoft 365 platform community call and become an active member of the Microsoft Graph community. To discover the full calendar of developer calls, visit the [Microsoft 365 and Power Platform community page](https://aka.ms/community/calls).
- [Join](https://ux.microsoft.com/Panel/M365Devs?utm_source=graphDocs) our research panel to provide your input on our developer experiences.