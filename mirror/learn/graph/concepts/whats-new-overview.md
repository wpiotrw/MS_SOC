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
ms.date: 2026-09-18T00:00:00.0000000Z
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
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 6e6097c9-5516-d241-0299-2adc10e56ea2
---

# What's new in Microsoft Graph - Microsoft Graph | Microsoft Learn

Microsoft Graph provides a unified programmability model that you can use to access data in Microsoft 365, Windows, and Enterprise Mobility + Security. This article provides information about what's new in Microsoft Graph APIs, documentation, SDKs, and more.

For more detailed API-level updates, see the [Microsoft Graph API changelog](https://developer.microsoft.com/graph/changelog/).

For details about previous updates to Microsoft Graph, see [Microsoft Graph what's new history](whats-new-earlier).

Important

Features in *preview* status are subject to change without notice, and might not be promoted to generally available (GA) status. Don't use preview features in production apps.

## September 2026: New and generally available

### Calendars | Work hours and locations

Added app-only support to the [workHoursAndLocationsSetting](/en-us/graph/api/resources/workhoursandlocationssetting), [workPlanOccurrence](/en-us/graph/api/resources/workplanoccurrence), and [workPlanRecurrence](/en-us/graph/api/resources/workplanrecurrence) resources and related methods. Apps can use the `Calendars.Read.All` application permission to read a user's setting, recurrences, and occurrences, and `Calendars.ReadWrite.All` to create, update, and delete them.

### Change notifications

Promoted the `unknownFutureValue` member of the **changeType** enumeration from beta to v1.0. The enumeration is used by the [changeNotification](/en-us/graph/api/resources/changenotification) and [commsNotification](/en-us/graph/api/resources/commsnotification) resources to identify notification change types.

### Files

- Added the **isPatternToken** property to the [fileStorageContainerCustomPropertyValue](/en-us/graph/api/resources/filestoragecontainercustompropertyvalue) resource to indicate whether a custom property value is a `urlTemplate` pattern that consumers must resolve before use, rather than a literal value.
- Added the **isOfficeRestricted** property to the [fileStorageContainerTypeSettings](/en-us/graph/api/resources/filestoragecontainertypesettings) and [fileStorageContainerTypeRegistrationSettings](/en-us/graph/api/resources/filestoragecontainertyperegistrationsettings) resources, and the **fileStorageContainerTypeSettingsOverride** enumeration.

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

### Groups

- Added the **disableNesting** property to the [group](/en-us/graph/api/resources/group?view=graph-rest-beta&amp;preserve-view=true) resource. Use it to prevent other groups from being added as members of a security group.

### Identity and access | Directory management

- Added the [provision](/en-us/graph/api/device-provision?view=graph-rest-beta&amp;preserve-view=true) action to the [device](/en-us/graph/api/resources/device?view=graph-rest-beta&amp;preserve-view=true) resource to enable approved Virtual Desktop Infrastructure (VDI) providers to provision devices in a customer's directory.

### Identity and access | Governance

Clarified that the [Get accessPackageResourceEnvironment](/en-us/graph/api/accesspackageresourceenvironment-get?view=graph-rest-beta&amp;preserve-view=true) method returns SharePoint Online resource environments only when it's called with delegated permissions. A SharePoint Online resource environment corresponds to a SharePoint root site, so to retrieve root site information with application permissions, use the [List sites](/en-us/graph/api/site-list?view=graph-rest-beta&amp;preserve-view=true) method with the `$filter=siteCollection/root ne null` query option.

### Identity and access | Monitoring & health

- Added support for tagging Microsoft Entra recommendations and their impacted resources. Use the [recommendation: addTag](/en-us/graph/api/recommendation-addtag?view=graph-rest-beta&amp;preserve-view=true), [recommendation: removeTag](/en-us/graph/api/recommendation-removetag?view=graph-rest-beta&amp;preserve-view=true), [impactedResource: addTag](/en-us/graph/api/impactedresource-addtag?view=graph-rest-beta&amp;preserve-view=true), and [impactedResource: removeTag](/en-us/graph/api/impactedresource-removetag?view=graph-rest-beta&amp;preserve-view=true) methods to manage the **tags** relationship, backed by the new [recommendationTag](/en-us/graph/api/resources/recommendationtag?view=graph-rest-beta&amp;preserve-view=true) resource. You can also add or remove a tag on up to 50 impacted resources in a single request by using the [impactedResource: addTag](/en-us/graph/api/impactedresource-addtag-collection?view=graph-rest-beta&amp;preserve-view=true) and [impactedResource: removeTag](/en-us/graph/api/impactedresource-removetag-collection?view=graph-rest-beta&amp;preserve-view=true) methods.
- Added alternate remediation states for recommendations and impacted resources. Use the [markPlanned](/en-us/graph/api/recommendation-markplanned?view=graph-rest-beta&amp;preserve-view=true), [acceptRisk](/en-us/graph/api/recommendation-acceptrisk?view=graph-rest-beta&amp;preserve-view=true), and [applyAlternateMitigation](/en-us/graph/api/recommendation-applyalternatemitigation?view=graph-rest-beta&amp;preserve-view=true) methods on the [recommendation](/en-us/graph/api/resources/recommendation?view=graph-rest-beta&amp;preserve-view=true) resource, and the corresponding methods on the [impactedResource](/en-us/graph/api/resources/impactedresource?view=graph-rest-beta&amp;preserve-view=true) resource.
- Added the `needsMoreAction` member to the **recommendationStatus** enumeration, and the `critical` member to the **recommendationPriority** enumeration.
- Added the [nistClassification](/en-us/graph/api/resources/nistclassification?view=graph-rest-beta&amp;preserve-view=true) resource and the **nistClassifications** property to the [recommendationBase](/en-us/graph/api/resources/recommendationbase?view=graph-rest-beta&amp;preserve-view=true) resource to map recommendations to NIST Cybersecurity Framework 2.0 functions and categories.
- Added the **categoryGroup** property (and the new **recommendationCategoryGroup** enumeration), **completedBySystemDateTime**, **completedByUserDateTime**, **failedReviewDateTime**, **needsMoreActionResourceCount**, **remediatedDateTime**, and **statusModifiedDateTime** properties to the [recommendationBase](/en-us/graph/api/resources/recommendationbase?view=graph-rest-beta&amp;preserve-view=true) resource. Added the `microsoftEntraSuite` member to the **requiredLicenses** enumeration and the **lastRefreshedDateTime** property to the [recommendationConfiguration](/en-us/graph/api/resources/recommendationconfiguration?view=graph-rest-beta&amp;preserve-view=true) resource.

### People and workplace intelligence | Analytics

Added the **sensitivityLabel** property to the [searchHit](/en-us/graph/api/resources/searchhit?view=graph-rest-beta&amp;preserve-view=true) resource type to provide sensitivity-label information for the search result resource.

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