---
layout: Conceptual
title: Audit log activities | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/audit-log-activities
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Discover how to monitor and investigate activities in Microsoft 365 with the unified audit log. Search for specific events and export results.
f1.keywords:
- NOCSH
ms.author: v-lilkafka
author: kafkadesign
manager: laurawi
ms.date: 2026-10-15T00:00:00.0000000Z
audience: Admin
ms.topic: reference
ms.service: purview
ms.subservice: purview-audit
ms.collection:
- purview-compliance
- audit
- m365copilot
search.appverid:
- MOE150
- MET150
ai-usage: ai-assisted
ms.custom: sfi-ga-nochange, msecd-doc-authoring-1018
locale: en-us
document_id: 7405f5ff-bcb6-7799-db12-f2c730686c19
document_version_independent_id: 7405f5ff-bcb6-7799-db12-f2c730686c19
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/audit-log-activities.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-log-activities
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/audit-log-activities.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: d429f232-553e-51b1-bfef-e34a4f45b360
---

# Audit log activities | Microsoft Learn

The tables in this article describe the activities recorded in the Microsoft 365 audit log. You can search for these activities by searching the audit log in the [Microsoft Purview portal](https://purview.microsoft.com).

Tip

Select one of the links in the **In this article** list at the top of this article to go directly to a specific product table.

Audit logging is turned on by default for Microsoft 365 organizations. If auditing isn't turned on for your organization, a banner appears that prompts you to start recording user and admin activity. For instructions, see [Turn on auditing](audit-log-enable-disable#turn-on-auditing).

These tables group related activities or the activities from a specific service. The tables include the friendly name that's displayed in the **Activities** drop-down list (or that are available in PowerShell) and the name of the corresponding operation that appears in the detailed information of an audit record and in the CSV file when you export the search results. For descriptions of the detailed information, see [Audit log detailed properties](audit-log-detailed-properties).

Important

Some operation names listed in the **Operation** column in the following tables contain a period ( `.` ). You must include the period in the operation name if you specify the operation in a PowerShell command when searching the audit log, creating audit retention policies, creating alert policies, or creating activity alerts. Also be sure to use double quotation marks (`" "`) to contain the operation name.

## Agent 365 activities

The following table lists Agent 365 activities that are logged when an agent is invoked or performs any actions or tool calls.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Executed AI tool | AIExecuteTool | Agent executed a tool call. |
| Invoked AI agent | AIInvokeAgent | AI agent is invoked by a user, agent, or event. |
| Made AI inference call | AIInferenceCall | AI agent leveraged an AI model to produce an answer or determine next steps. |
| Applied AI guardrail | AIGuardrail | A guardrail was applied to an AI agent's request or response to enforce safety or compliance policies. |

## Application administration activities

The following table lists application admin activities that Microsoft 365 audit logs when an admin adds or changes an application registered in Microsoft Entra ID. You must register any application that relies on Microsoft Entra ID for authentication in the directory.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Added credentials to a service principal | Add service principal credentials. | Credentials were added to a service principal in Microsoft Entra ID. A service principal represents an application in the directory. |
| Added delegation entry | Add delegation entry. | An authentication permission was created or granted to an application in Microsoft Entra ID. |
| Added service principal | Add service principal. | An application was registered in Microsoft Entra ID. A service principal represents an application in the directory. |
| Removed a service principal from the directory | Remove service principal. | An application was deleted or unregistered from Microsoft Entra ID. A service principal represents an application in the directory. |
| Removed credentials from a service principal | Remove service principal credentials. | Credentials were removed from a service principal in Microsoft Entra ID. A service principal represents an application in the directory. |
| Removed delegation entry | Remove delegation entry. | An authentication permission was removed from an application in Microsoft Entra ID. |
| Set delegation entry | Set delegation entry. | An authentication permission was updated for an application in Microsoft Entra ID. |

## Briefing email activities

The following table lists the activities in Briefing email that the Microsoft 365 audit log records. For more information about Briefing email, see:

- [Overview of Briefing email](/en-us/Briefing/be-overview)
- [Configure Briefing email](/en-us/Briefing/be-admin)

| Friendly name | Operation | Description |
| --- | --- | --- |
| Updated organization privacy settings | UpdatedOrganizationBriefingSettings | Admin updates the organization privacy settings for Briefing email. |
| Updated user privacy settings | UpdatedUserBriefingSettings | Admin updates the user privacy settings for Briefing email. |

## Communication compliance activities

The following table lists communication compliance activities that the Microsoft 365 audit log records. For more information, see [Learn about Microsoft Purview Communication Compliance](communication-compliance).

Note

You can see these activities when you use the [Search-UnifiedAuditLog](/en-us/powershell/module/exchange/search-unifiedauditlog) PowerShell cmdlet. You can't see these activities in the **Activities** drop-down list.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Policy match | SupervisionRuleMatch | A user sent a message that matches a policy's condition. |
| Policy update | SupervisionPolicyCreated, SupervisionPolicyUpdated, SupervisionPolicyDeleted | A communication compliance administrator performed a policy update. |
| Tag applied to messages | SupervisoryReviewTag | Tags are applied to messages or messages are resolved. |

## Compliance Manager activities

The following table lists the operations and activities that the audit log records when an admin manages settings in Compliance Manager. For more information, see [Learn about Compliance Manager](compliance-manager).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Roles change | ComplianceManagerRolesChange | An admin changed the roles for users. |
| Tenant automation level change | ComplianceManagerAutomationLevelChange | An admin changed the automation level for the organization across all actions. |
| Testing source automation change | ComplianceManagerAutomationChange | An admin changed the testing source automation settings. |

## Content explorer activities

The following table lists the activities in Content explorer recorded in the Microsoft 365 audit log. You access content explorer on the Data classifications tool in the Microsoft Purview portal. For more information, see [Using data classification content explorer](data-classification-content-explorer).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Accessed item | LabelContentExplorerAccessedItem | An admin (or a user who's a member of the Content Explorer Content Viewer role group) used content explorer to view an email message or SharePoint and OneDrive document. |
| AccessedAggregates | AccessedAggregates | An admin used content explorer to navigate between different aggregates. |
| AccessedContentList | AccessedContentList | When admin Clicked on any site/user in Content Explorer to get list of items. |
| AccessedItemDownload | AccessedItemDownload | An admin used content explorer to download an item. |
| AccessedItemPreview | AccessedItemPreview | An admin used content explorer to preview an item. |
| AccessedSiteList | AccessedSiteList | An admin used content explorer to navigate to SharePoint and OneDrive to get the site list. |
| AccessedUserList | AccessedUserList | An admin used content explorer to navigate to Exchange/Teams workload to get the user list. |
| SearchedContentList | SearchedContentList | When admin Searched for a file in Content Explorer. |
| SearchedSiteList | SearchedSiteList | An admin used content explorer to search for a site. |
| SearchedUserList | SearchedUserList | An admin used content explorer to search for a user. |

## Data Security Investigations activities

Data Security Investigations provides powerful investigation tools that might require the ability to audit activities to ensure secure and approved use of the solution. To meet these requirements, the unified audit log records Data Security Investigations activities.

The following table lists Data Security Investigations activities that the Microsoft 365 audit log records. For more information, see [Learn about Microsoft Purview Data Security Investigations](data-security-investigations).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Canceled DSI sample view | DSISampleViewCancelled | A user canceled a samples view. |
| Canceled DSI statistics view | DSIStatisticsViewCancelled | A user canceled a statistics job. |
| Created DSI Investigation | CreatedDSIInvestigation | A user created an investigation. |
| Deleted Data Security Investigations capacity | DSICapacityDeleted | A user deleted the Data Security Investigation capacity. |
| Deleted DSI Investigation | DeletedDSIInvestigation | A user deleted an investigation. |
| DSI AI feedback provided | DSIAIFeedbackProvided | A user provided AI feedback. |
| DSI investigation list viewed | DSIInvestigationListViewed | A user viewed the list of investigations. |
| DSI search added | DSIPurviewSearchAdded | A user added a search. |
| DSI search updated | DSIPurviewSearchUpdated | A user updated a search. |
| DSIProbeJobResultsViewed | DSIProbeJobResultsViewed | A user viewed the results of examination. |
| Get DSI Investigation | GetDSIInvestigation | A user viewed an investigation. |
| Get DSI search | GetSearchDSIInvestigation | A user viewed a search. |
| Investigation created from Defender XDR | DSIInvestigationCreatedFromXDR | A user created an investigation from Defender XDR. |
| Investigation created from Purview IRM | DSIInvestigationCreatedFromIRM | A user created an investigation from Microsoft Purview Insider Risk Management. |
| Item added to mitigation | DSIItemAddedToMitigation | A user added an item to an investigation's mitigation plan. |
| Item removed from mitigation | DSIItemRemovedFromMitigation | A user removed an item from an investigation's mitigation plan. |
| Mitigation plan list viewed | DSIMitigationPlanListViewed | A user viewed the mitigation plan list. |
| Started categorization job | DSIInvestigationCategorizationJobSubmitted | A user started a categorization job. |
| Started probing job | DSIProbeJobSubmitted | A user started an examination job. |
| Started purge job | DSIPurgeStarted | A user started a purge job. |
| Started vectorization job | DSIInvestigationVectorizationJobSubmitted | A user stated a vectorization job. |
| Submitted DSI search add to evidence set job | DSIPurviewSearchAddToEvidenceSetJobSubmitted | A user added searched data to an investigation scope. |
| Submitted DSI search sample job | DSIPurviewSearchSampleJobSubmitted | A user started a samples job. |
| Submitted DSI search statistics job | DSIPurviewSearchStatisticsJobSubmitted | A user started a statistics job. |
| Updated Data Security Investigations capacity | DSICapacityUpdated | A user updated the Data Security Investigation capacity. |
| Updated DSI Investigation | UpdatedDSIInvestigation | A user updated an investigation. |
| Updated DSI Investigation members | DSIInvestigationMembersUpdated | A user updated an investigation's members. |
| Updated status on item from mitigation plan | DSIMitigationItemStatusUpdated | A user updated the status of an item on an investigation's mitigation plan. |
| Uploaded file for DSI search | DSIPurviewSearchUploadFile | A user uploaded a file to search. |
| Vector search started | DSIVectorSearchStarted | A user ran a vector search. |
| Viewed data processing errors for a DSI evidence set | DSIInvestigationSettingsUpdated | A user updated investigation settings. |
| Viewed Data Security Investigations capacity | DSICapacityViewed | A user viewed the Data Security Investigation capacity. |
| Viewed default DSI investigation settings | DSIInvestigationSettingsDefaultViewed | A user viewed investigation settings. |
| Viewed DSI evidence set document | DSIEvidenceSetDocumentViewed | A user viewed a document in an investigation. |
| Viewed DSI investigation settings | DSIInvestigationSettingsViewed | A user viewed investigation settings. |
| Viewed DSI sample results | DSISampleResultsViewed | A user viewed sample results. |
| Viewed DSI sample status | DSISampleStatusViewed | A user viewed the status of a samples job. |
| Viewed DSI statistics results | DSIStatisticsResultsViewed | A user viewed search statistics. |
| Viewed individual activity | DSISingleActivityViewed | A user viewed an activity in an investigation. |
| Viewed investigation activities list | DSIActivitiesViewed | A user viewed the investigation activities. |
| Viewed investigation evidence set | DSIEvidenceSetViewed | A user viewed the list of items in the investigation. |
| Viewed item from mitigation plan | DSIItemViewedFromMitigation | A user viewed an item from an investigation's mitigation plan. |

## Data Security Posture Agent activities

The following table lists the activities for the [Data Security Posture Agent](copilot-in-purview-posture-agent-get-started) in the Microsoft 365 audit log.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Agent Ran | AgentRan | User ran the Data Security Posture Agent. |
| Agent re-ran | Agent Reran | User reran the Data Security Posture Agent. |
| Agent result viewed | AgentResultViewed | User viewed the results of a Data Security Posture Agent run. |
| Agent run cancelled | AgentRunCancelled | User canceled a run for Data Security Posture Agent. |
| Agent run deleted | AgentRunDeleted | User deleted a run for Data Security Posture Agent. |

## Directory administration activities

The following table lists Microsoft Entra directory and domain-related activities that are logged when an administrator manages their organization in the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339) or in the Azure management portal.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Added a partner to the directory | Add partner to company. | Added a partner (delegated administrator) to your organization. |
| Added domain to company | Add domain to company. | Added a domain to your organization. |
| Removed a partner from the directory | Remove partner from company. | Removed a partner (delegated administrator) from your organization. |
| Removed domain from company | Remove domain from company. | Removed a domain from your organization. |
| Set company information | Set company information. | Updated the company information for your organization. Includes email addresses for subscription-related email that Microsoft 365 sends, and technical notifications about Microsoft 365 services. |
| Set domain authentication | Set domain authentication. | Changed the domain authentication setting for your organization. |
| Set password policy | Set password policy. | Changed the length and character constraints for user passwords in your organization. |
| Turned on Microsoft Entra ID Sync | Set DirSyncEnabled flag. | Set the property that enables a directory for Microsoft Entra ID Sync. |
| Updated domain | Update domain. | Updated the settings of a domain in your organization. |
| Updated the federation settings for a domain | Set federation settings on domain. | Changed the federation (external sharing) settings for your organization. |
| Verified domain | Verify domain. | Verified that your organization was the owner of a domain. |
| Verified email verified domain | Verify email verified domain. | Used email verification to verify that your organization is the owner of a domain. |

## Disposition review activities

The following table lists the [activities a disposition reviewer took](disposition#viewing-and-disposing-of-content) when an item reached the end of its configured retention period, or when an item automatically moved to the next disposition stage or was permanently deleted as a result of [autoapproval](disposition#auto-approval-for-disposition).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Added reviewers | AddReviewer | A disposition reviewer added one or more other users to the current disposition review stage. |
| Approved disposal | ApproveDisposal | For manual approval: A disposition reviewer approved the disposition of the item to move it to the next disposition stage. If the item was in the only or final stage of disposition review, the disposition approval marked the item as eligible for permanent deletion.  For autoapproval: No manual action was taken within the configured autoapproval time period so the item automatically moved to the next disposition stage. If the item was in the only or final stage of disposition review, the item automatically became eligible for permanent deletion. |
| Extended retention period | ExtendRetention | A disposition reviewer extended the retention period of the item. |
| Relabeled item | RelabelItem | A disposition reviewer relabeled the retention label. |

## Dragon Copilot admin activities

The following table lists administrative activities for Dragon Copilot recorded in the Microsoft 365 audit log. These events are logged when an administrator changes Dragon Copilot configuration. These events include changes in environments, products, Electronic Health Record (EHR) connectors, billing plans, groups, role assignments, settings, and extensions. If your organization uses Dragon Copilot, you can [search the audit log](audit-search) for these activities by using the **Activities** picker list. For more information about Dragon Copilot, see the [Dragon Copilot documentation](/en-us/industry/healthcare/dragon-copilot/).

You can also search for Dragon Copilot admin activities by running the `Search-UnifiedAuditLog -RecordType DragonCopilotAdmin` command in [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Accepted terms | AcceptedTerms | Terms of service were accepted. |
| Activated subscription | ActivatedSubscription | A subscription was activated. |
| Added group member | AddedGroupMember | A user was added to a group. |
| Canceled deprovision | CanceledDeprovision | A previously queued deprovision was cancelled. |
| Created billing plan | CreatedBillingPlan | A billing plan was created. |
| Created child organization | CreatedChildOrganization | A child organization was created. |
| Created data export configuration | CreatedDataExportConfig | A data export configuration was created. |
| Created EHR connector | CreatedEhrConnector | An EHR connector was created. |
| Created EHR instance | CreatedEhrInstance | An EHR integration instance was created. |
| Created EHR user | CreatedEhrUser | An EHR user mapping was created. |
| Created environment | CreatedEnvironment | A new Dragon Copilot environment was created. |
| Created extension | CreatedExtension | An extension was installed. |
| Created group | CreatedGroup | A user group was created. |
| Created organization role assignment | CreatedOrganizationRoleAssignment | An organization role assignment was created. |
| Created role assignment | CreatedRoleAssignment | A role was assigned to a user. |
| Deleted billing plan | DeletedBillingPlan | A billing plan was deleted. |
| Deleted data export configuration | DeletedDataExportConfig | A data export configuration was deleted. |
| Deleted device connector | DeletedDeviceConnector | A device connector under an EHR connector was deleted. |
| Deleted EHR instance | DeletedEhrInstance | An EHR integration instance was removed. |
| Deleted EHR user | DeletedEhrUser | An EHR user mapping was deleted. |
| Deleted environment | DeletedEnvironment | An environment was deleted. |
| Deleted group | DeletedGroup | A user group was deleted. |
| Deleted organization | DeletedOrganization | An organization was deleted from the hierarchy. |
| Deleted organization role assignment | DeletedOrganizationRoleAssignment | An organization role assignment was deleted. |
| Deleted role assignment | DeletedRoleAssignment | A role assignment was removed. |
| Deleted setting | DeletedSetting | A configuration setting was deleted. |
| Deprovisioned product | DeprovisionedProduct | A product was deprovisioned from an environment. |
| Installed device connector | InstalledDeviceConnector | A device connector was installed or upgraded under an EHR connector from a published package. |
| Installed device connector from package | InstalledDeviceConnectorFromPackage | A device connector was installed or upgraded under an EHR connector from a sideloaded device package. |
| Listed billing plans | ListedBillingPlans | Billing plans were listed. |
| Listed bulk user imports | ListedBulkUserImports | Bulk user imports were listed. |
| Listed device connectors | ListedDeviceConnectors | Device connectors installed under an EHR connector were listed. |
| Listed EHR instances | ListedEhrInstances | EHR instances were listed. |
| Listed environments | ListedEnvironments | All environments were listed. |
| Listed extensions | ListedExtensions | Extensions were listed. |
| Listed groups | ListedGroups | User groups were listed. |
| Listed organizations | ListedOrganizations | Organizations were listed. |
| Listed role assignments | ListedRoleAssignments | Role assignments were listed. |
| Listed role definitions | ListedRoleDefinitions | An administrator listed the available role definitions. |
| Listed settings | ListedSettings | Configuration settings were listed. |
| Provisioned product | ProvisionedProduct | A product was provisioned for an environment. |
| Queued deprovision | QueuedDeprovision | An environment was queued for deprovisioning. |
| Removed group member | RemovedGroupMember | A user was removed from a group. |
| Set device connector state | SetDeviceConnectorState | A device connector under an EHR connector was enabled or disabled. |
| Started bulk user import | StartedBulkUserImport | A bulk user import was started. |
| Updated billing plan | UpdatedBillingPlan | Billing plan properties were modified. |
| Updated data export configuration | UpdatedDataExportConfig | A data export configuration was modified. |
| Updated device connector configuration | UpdatedDeviceConnectorConfiguration | The configuration of a device connector under an EHR connector was updated. |
| Updated EHR connector | UpdatedEhrConnector | An EHR connector was modified. |
| Updated EHR instance | UpdatedEhrInstance | An EHR integration instance was modified. |
| Updated environment | UpdatedEnvironment | Environment properties were modified. |
| Updated extension | UpdatedExtension | An extension was updated. |
| Updated group | UpdatedGroup | Group properties were modified. |
| Updated organization | UpdatedOrganization | Organization properties were modified. |
| Updated setting | UpdatedSetting | A configuration setting was changed. |
| Verified device connector package | VerifiedDeviceConnectorPackage | A sideloaded device package was verified against an EHR connector without being installed. |
| Viewed billing plan | ViewedBillingPlan | Billing plan details were viewed. |
| Viewed bulk user import | ViewedBulkUserImport | A bulk user import was viewed. |
| Viewed data export configuration | ViewedDataExportConfig | A data export configuration was viewed. |
| Viewed device connector | ViewedDeviceConnector | An installed device connector under an EHR connector was viewed. |
| Viewed EHR connector | ViewedEhrConnector | An EHR connector was viewed. |
| Viewed EHR instance | ViewedEhrInstance | An EHR instance was viewed. |
| Viewed environment | ViewedEnvironment | Environment details were viewed. |
| Viewed extension | ViewedExtension | Extension details were viewed. |
| Viewed group | ViewedGroup | Group details were viewed. |
| Viewed organization | ViewedOrganization | Organization details were viewed. |
| Viewed role assignment | ViewedRoleAssignment | A role assignment was viewed. |
| Viewed role definition | ViewedRoleDefinition | An administrator viewed a role definition. |
| Viewed setting | ViewedSetting | A setting value was viewed. |

## Dragon Copilot Web activities

The following table lists user and application activities for Dragon Copilot Web recorded in the Microsoft 365 audit log. These events capture user access, clinical workflow actions, AI-assisted operations, and session lifecycle events performed within Dragon Copilot Web. Dragon Copilot Web supports clinical documentation workflows including ambient recording, transcript review, AI-assisted note generation, clinical chat, and EHR-integrated experiences.

If your organization uses Dragon Copilot Web, you can search for these activities in Microsoft Purview Audit by selecting the appropriate activity name or by filtering on the Dragon Copilot record types. Audit records are emitted under the following record types:

- DragonCopilotAccess
- DragonCopilotClinicalData
- DragonCopilotSession

You can also search for Dragon Copilot Web audit events by using `Search-UnifiedAuditLog` and filtering on the corresponding record type.

### Dragon Copilot access activities

The following table lists user access and interaction activities for Dragon Copilot recorded in the Microsoft 365 audit log. These events are logged when users access Dragon Copilot or interact with its features and underlying services. These activities include launching Dragon Copilot from an EHR system, accessing Dragon Copilot, and updating patient session data. Events also capture failures related to these operations. If your organization uses Dragon Copilot, you can [search the audit log](audit-search) for these activities by using the **Activities** picker list. For more information about Dragon Copilot, see the [Dragon Copilot documentation](/en-us/industry/healthcare/dragon-copilot/).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Application accessed | AppAccessed | A user opened the Dragon Copilot web application. |
| EHR launch completed | EhrLaunchCompleted | Dragon Copilot launch from EHR completed. |
| EHR launch failed | EhrLaunchFailed | Dragon Copilot launch from EHR failed. |
| Encounter accessed | EncounterAccessed | A user opened a patient encounter in Dragon Copilot. |
| License check failed | LicenseCheckFailed | User doesn't have Dragon Copilot license. |
| Session data updated | SessionDataUpdated | Session data updated. |
| Session data update failed | SessionDataUpdateFailed | Session data update failed. |

### Dragon Copilot clinical data activities

| Friendly name | Operation | Description |
| --- | --- | --- |
| Transcript viewed | TranscriptViewed | A user viewed the transcript of an ambient or dictation session. |
| Clinical chat opened | ClinicalChatOpened | A user opened the clinical chat interface in Dragon Copilot. |
| Clinical chat episode viewed | ClinicalChatEpisodeViewed | A user viewed a previous clinical chat conversation episode. |
| Clinical chat prompt sent | ClinicalChatPromptSent | A user sent a message or prompt in the clinical chat interface. |
| Copilot prompt executed | CopilotPromptExecuted | A user triggered an AI action such as note summarization, generation, or rewrite. |
| Note generated | NoteGenerated | A clinical note was generated by the AI assistant and presented to the user. |
| Note updated | NoteUpdated | An AI-generated clinical note was updated with new or revised content and presented to the user. |
| AI suggested edit presented | AiSuggestedEditPresented | An AI-suggested edit to a clinical note was presented to the user for review. |
| AI suggested edit accepted | AiSuggestedEditAccepted | A user accepted an AI-suggested edit to a clinical note. |
| AI suggested edit rejected | AiSuggestedEditRejected | A user rejected an AI-suggested edit to a clinical note. |
| Clinical chat feedback submitted | ClinicalChatFeedbackSubmitted | A user submitted feedback on a clinical chat response. |

### Dragon Copilot session activities

| Friendly name | Operation | Description |
| --- | --- | --- |
| Session started | SessionStarted | A user started a new clinical documentation session in Dragon Copilot. |
| Session ended | SessionEnded | A user ended a clinical documentation session in Dragon Copilot. |
| Recording started | RecordingStarted | A user started audio recording during a clinical session. |
| Recording ended | RecordingEnded | A user stopped audio recording during a clinical session. |

## eDiscovery activities

The audit log records eDiscovery activities that you perform in the Microsoft Purview portal. It logs events when administrators or eDiscovery managers (or any user assigned eDiscovery permissions) perform the following tasks in the Microsoft Purview portal:

- Creating and managing eDiscovery cases.
- Creating and editing searches for eDiscovery cases.
- Performing search actions, such as generating statistics, creating a sample, and exporting from search.
- Creating, editing, and removing holds for eDiscovery cases.
- Creating review sets and performing review activities in eDiscovery cases.

For more information about searching the audit log, the permissions that are required, and exporting search results, see [Search the audit log](audit-search).

### How to search for and view eDiscovery activities

The audit log records eDiscovery activities that you perform in the Microsoft Purview portal or in PowerShell. To search for eDiscovery activities, see [Search for eDiscovery activities in the audit log](edisc-ref-audit-log).

### eDiscovery activity reference

The following table lists the eDiscovery activities that are logged when an administrator or eDiscovery manager performs an eDiscovery-related activity by using the Microsoft Purview portal. Some activities performed in the classic eDiscovery user experience might be returned when you search for activities in this list.

Note

The client IP field is included for all activities performed in the new eDiscovery experience. To distinguish activities performed in the new experience from those in the classic experience, check for the presence of the client IP field in the audit entry. (In the following image, the first entry is eDiscovery case deleted in new modern ux and the other two entries without IP addresses are classic ux).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Added favorite | FavoriteSet | User set a case to favorite. |
| Added Purview search | PurviewSearchAdded | A new search was created. This audit activity includes the case name, case ID, and search name that was created. |
| Added review set | ReviewSetAdded | User created a review set. |
| Added saved search for a review set | ReviewSetSavedSearchAdded | User created saved filters in a review set. The audit activity includes the review set name, saved filters name, and the query used. |
| Added tag template | TagTemplateAdded | User created tag template in eDiscovery settings. |
| Cancelled sample view | SampleViewCancelled | User canceled sample view. The audit activity includes the canceled search’s name, ID, query, and associated settings. |
| Cancelled statistics view | StatisticsViewCancelled | User canceled statistics view. The audit activity includes the canceled search’s name, ID, query, and associated settings. |
| Changed eDiscovery case | CaseUpdated | Updated an eDiscovery case. |
| Changed hold in eDiscovery case | HoldUpdated | Hold was modified or edited. This audit activity includes the hold name, ID, and the specific data sources and query values that were modified. |
| Closed eDiscovery case | CaseClosed | An eDiscovery case was closed. |
| Copied review set | ReviewSetCopied | User triggers the “Add to another review set” process. |
| Created eDiscovery case | CaseAdded | Added a new eDiscovery case. |
| Created hold in eDiscovery case | HoldCreated | A new hold was created. This audit activity includes the case name, case ID, and hold name that was created. |
| Deleted eDiscovery case | CaseRemoved | An eDiscovery case was deleted. You must remove any hold associated with the case before you can delete the case. |
| Deleted file for Purview search | PurviewSearchDeleteFile | User deleted a file from a search. This audit activity includes the case name, case ID, search name, search ID, and the ID of the file the user deleted. |
| Deleted hold in eDiscovery case | HoldRemoved | A hold that is associated with an eDiscovery case was deleted. Deleting a hold releases all of the content locations from the hold. |
| Deleted Purview search | PurviewSearchDeleted | A search was deleted. This activity includes the deleted case name, case ID, and search name. |
| Deleted Purview Search export job | PurviewSearchExportJobDeleted | An export from search was deleted. This activity includes the deleted export name, the case information in which the export is included, the user, and the deletion timestamp. |
| Removed favorite | FavoriteRemoved | User removed a case from favorites. |
| Removed saved search for a review set | ReviewSetSavedSearchRemoved | User deleted saved filters in a review set. |
| Removed tag template | TagTemplateRemoved | User removed a tag template in eDiscovery settings. The audit activity includes the name and object ID of the tag template removed. |
| Reopened eDiscovery case | CaseReopened | An eDiscovery case was reopened. |
| Retried distribution sync for hold | HoldRetryDistributionSync | User triggered “retry policy” in a hold. |
| Retrieved actions for all review sets | GetActionsForAllReviewSets | User viewed a list of actions associated with all review sets in a case. |
| Retrieved all action for hold | GetActionsForAllHolds | User viewed a list of actions associated with all holds in a case. The audit activity includes case name, ID, hold name, ID, and the name of the list of actions. |
| Retrieved all action for search | GetActionsForSearch | User viewed a list of actions (such as exports) associated with a search. The audit activity includes case name, ID, search name, ID, and the name of the list of actions. |
| Retrieved all actions for all exports | GetActionsForAllExports | User viewed a list of exports in a case. The audit activity includes case name, ID, case settings, and the list of export names viewed. |
| Retrieved all actions for case | GetActionsForCase | User viewed a list of actions (such as exports) associated with an eDiscovery case. |
| Retrieved all actions for hold | GetActionsForHold | User viewed a list of actions associated with a hold. |
| Retrieved all actions for review set | GetActionsForReviewSet | User viewed a list of actions (such as exports) associated with a review set. The audit activity includes case name, ID, review set name, ID, and the name of the list of actions. |
| Retrieved single action for case | GetSingleActionForCase | User viewed a single action associated with an eDiscovery case. For example, the user viewed the export process in process manager. The audit activity includes case name, ID, and settings and ID associated with the process. |
| Retrieved single action for hold | GetSingleActionForHold | User viewed a single action associated with a hold. |
| Retrieved single action for review set | GetSingleActionForReviewSet | User viewed a single action associated with a review set. |
| Retrieved single action for search | GetSingleActionForSearch | User viewed a single action associated with a search. For example, the user viewed the export process in the search’s process manager. The audit activity includes case name, ID, and settings and ID associated with the process. |
| Submitted new algo job | AlgoJobSubmitted | User ran analytics on the documents in a review set. |
| Submitted new burn job | BurnJobSubmitted | User converted all the redacted documents in a review set to PDF files. |
| Submitted purview search add to review set job | PurviewSearchAddToReviewSetJobSubmitted | User triggered an “add to review set” process from a search. This audit activity includes the search name, ID, and the specific data sources and query values that were associated to the search. It also includes relevant add to review set process settings used. |
| Submitted purview search export job | PurviewSearchExportJobSubmitted | User triggered an “export” process from a search. This audit activity includes the search name, ID, and the specific data sources and query values that were associated to the search. It also includes relevant export process settings used and the export name. |
| Submitted purview search sample job | PurviewSearchSampleJobSubmitted | User triggered a “generate sample” process from a search. This audit activity includes the search name, ID, and the specific data sources and query values that were associated to the search. It also includes relevant sample process settings used. |
| Submitted purview search statistics job | PurviewSearchStatisticsJobSubmitted | User triggered a “generate statistics” process from a search. This audit activity includes the search name, ID, and the specific data sources and query values that were associated to the search. It also includes relevant statistics process settings used. |
| Submitted review set export job | ReviewSetExportJobSubmitted | Exported documents from review set. This audit activity includes the review set name, list of documents IDs being exported and relevant export process settings. |
| Tagged documents by ID for a review set | ReviewSetDocumentsTaggedById | User applied tags to specific documents in a review set. The audit activity includes the case name, review set name, and the list of items being tagged. |
| Tagged documents by query for a review set | ReviewSetDocumentsTaggedByQuery | User applied tags to specific documents in a review set after filtering by query. The audit activity includes the case name, review set name, and the list of items being tagged. |
| Updated case members | CaseMembersUpdated | Case membership was updated. As a member of a case, a user can perform various case-related tasks depending on whether they're assigned the necessary permissions. |
| Updated case settings | CaseSettingsUpdated | User modified the settings for a case. Case settings include case information, premium feature access, case permissions, and settings that control search and analytics behavior. |
| Updated notes for a review set | ReviewSetNotesUpdated | User updated note for a review set document. |
| Updated Purview search | PurviewSearchUpdated | Search was modified or edited. This audit activity includes the search name, ID, and the specific data sources and query values that were modified. |
| Updated review set | ReviewSetUpdated | User updated the review set such as review set name and description. |
| Updated review set annotation | ReviewSetAnnotationsUpdated | User annotated a document in a review set. This audit activity includes the review set name and other information such as the annotated document ID. |
| Updated saved search for a review set | ReviewSetSavedSearchUpdated | User modified saved filters in a review set. The audit activity includes the review set name, saved filters name, and the query used. |
| Updated tag template | TagTemplateUpdated | User updated a tag template in eDiscovery settings. The audit activity includes the name and object ID of the tag template updated. |
| Updated tags | TagsUpdated | User updated review set tags in a case. |
| Updated tags for a tag template | TagTemplateTagsUpdated | User updated tags for a tag template. The audit activity includes the name and ID of the tag template tags updated. |
| Updated tenant settings | TenantSettingsUpdated | User updated eDiscovery’s organization settings. |
| Viewed analytics review set attachments report | AlgoGetReviewSetAttachmentsReport | User viewed analytics attachment report. This audit activity includes case and review set name and ID. |
| Viewed analytics review set documents report | AlgoGetReviewSetDocumentsReport | User viewed analytics document report. |
| Viewed analytics review set email report | AlgoGetReviewSetEmailsReport | User viewed analytics email report. |
| Viewed analytics review set report | AlgoGetReviewSetReport | User viewed analytics report in a review set. This audit activity includes case and review set name and ID, as well as the report type. |
| Viewed analytics review set report by file type | AlgoGetReviewSetReportByFileType | User viewed analytics report graph by file type. |
| Viewed analytics review set report by source | AlgoGetReviewSetReportBySource | User viewed analytics document by source. This audit activity includes case and review set name and ID. |
| Viewed case metadata | CaseMetadataViewed | Metadata about an eDiscovery case was viewed. |
| Viewed case settings | CaseSettingsViewed | User viewed the settings for a case. Case settings include case information, premium feature access, case permissions, and settings that control search and analytics behavior. |
| Viewed data processing errors for a review set | ReviewSetDataProcessingErrorViewed | User viewed processing errors in a review set. |
| Viewed default case settings | CaseSettingsDefaultViewed | Default case setting viewed. |
| Viewed eDiscovery case | CaseViewed | A user viewed an eDiscovery case in the Microsoft Purview portal. The audit record for this event includes the name, case settings, and case ID of the case that was viewed. |
| Viewed eDiscovery case list | CaseListViewed | This activity is logged when a user viewed a list of eDiscovery cases. The audit record includes the name and ID of the cases that was viewed in the cases list. |
| Viewed favorite list | FavoriteListViewed | User viewed a list of favorite cases. |
| Viewed hold | HoldViewed | User viewed a hold inside a case. This audit activity includes the hold name and ID the user viewed. It also includes the specific data sources and query values inside the hold that was viewed by the user. |
| Viewed hold list | HoldListViewed | User viewed the holds list inside a case. This audit activity includes the case name, case ID, and the list of holds name and ID the user viewed. |
| Viewed hold results | HoldResultsViewed | User viewed hold’s results. The audit activity includes case name, case ID, hold name, and hold ID. |
| Viewed hold status | HoldStatusViewed | User viewed hold’s status. The audit activity includes case name, case ID, hold name, and hold ID. |
| Viewed if analytics settings are changed | AlgoIsSettingChanged | This audit activity includes case and review set name and ID. |
| Viewed load count in case | LoadCountInCaseViewed | User viewed the count of load sets in a case. |
| Viewed load list | LoadListViewed | User viewed a list of load sets in review set. |
| Viewed Purview search | PurviewSearchViewed | User viewed a specific search. This audit activity includes the search name, ID, and the specific data sources and query values inside the search that was viewed by the user. |
| Viewed Purview search list | PurviewSearchListViewed | User viewed the searches list inside a case. This audit activity includes the case name, case ID, and the list of searches name and ID the user viewed. |
| Viewed query report for a review set | ReviewSetQueryReportViewed | User viewed query report inside a review set. |
| Viewed review set document | ReviewSetDocumentViewed | User viewed a document inside a review set. This audit activity includes the case name, case ID, review set name, review set ID and other information such as the ID of the document viewed. |
| Viewed review set list | ReviewSetListViewed | User viewed the list of review sets in a case. |
| Viewed review set summary | ReviewSetSummaryViewed | User viewed the Overview of a Review set. |
| Viewed sample results | SampleResultsViewed | User viewed search sample results view. |
| Viewed sample status | SampleStatusViewed | User viewed search sample view’s status. The audit activity includes search’s name, ID, query, and associated settings. |
| Viewed saved search list for a review set | ReviewSetSavedSearchListViewed | User viewed a list of saved filters in a review set. The audit activity includes the review set name and the name of the list of saved filters viewed. |
| Viewed search count for a review set | ReviewSetSearchCountViewed | User ran a search within a review set and viewed the count returned. The audit activity includes the case name, review set name and the count of items returned in the search results. |
| Viewed search options for a review set | ReviewSetSearchOptionsViewed | User viewed the settings of a review set. The audit activity includes the case name and review set name. |
| Viewed search results for a review set | ReviewSetSearchRun | User ran a search within a review set. The audit activity includes the case name, review set name and the list of items returned in the search results. |
| Viewed statistics results | StatisticsResultsViewed | User viewed search statistics results. |
| Viewed statistics status | StatisticsStatusViewed | User viewed search statistics view’s status. The audit activity includes search’s name, ID, query, and associated settings. |
| Viewed tag template list | TagTemplateListViewed | User viewed the list of tag template in eDiscovery settings. The audit activity includes the list of tag templates viewed. |
| Viewed tags | TagsViewed | User viewed review set tags in a case. |
| Viewed tags for a tag template | TagTemplateTagsViewed | User viewed tags for a tag template. The audit activity includes the name and ID of the tag template tags viewed. |
| Viewed tenant settings | TenantSettingsViewed | User viewed eDiscovery’s organization settings. The audit activity contains information on the setting values. |

### Detailed properties for eDiscovery activities

The following table lists the properties that the portal shows on the details page for an eDiscovery activity listed in the search results. These properties are also included in the CSV file when you export the audit log search results. An audit log record for an eDiscovery activity doesn't include every detailed property listed in the following table.

Tip

When you export the search results, the CSV file contains a column named **AuditData**, which contains the detailed properties described in the following table in a multivalue property. You can use the Power Query feature in Excel to split this column into multiple columns so that each property has its own column. This setup lets you sort and filter on one or more of these properties. For more information, see [Search the audit log](audit-search).

| Property | Description |
| --- | --- |
| CaseId | The identity (GUID) of the eDiscovery case created, changed, or deleted. |
| CaseName | The name of the eDiscovery case created, changed, or deleted. |
| ClientApplication | eDiscovery cmdlet activities have a value of **EMC** for this property. This value indicates the activity was performed by using the Microsoft Purview portal GUI or running the cmdlet in PowerShell. |
| ClientIP | The IP address of the device that was used when the activity was logged. The IP address is displayed in either an IPv4 or IPv6 address format. |
| ClientRequestId | For eDiscovery activities, this property is typically blank. |
| CmdletVersion | The build number for the version of the Microsoft Purview portal running in your organization. |
| CreationTime | The creation date and time in Coordinated Universal Time (UTC) for the activity. |
| DataSources | A list of source ID, source name, and location details associated to the activity. |
| EffectiveOrganization | The name of the Microsoft 365 organization. |
| ExportName | Name of the eDiscovery export. |
| ExtendedProperties | Additional properties related to the eDiscovery activity. For example, when case members are updated, this field contains the updated case member information; or when the review set description is updated, this field contains the updated review set description updated by the user. |
| ID | The ID of the report entry. The ID uniquely identifies the audit log entry. |
| Item | The name of the item associated with the activity. For example, this field contains the name of the document viewed when a user views a review set document. |
| JobId | The GUID of the eDiscovery process. |
| ObjectId | The GUID of the object (for example, a search, hold, or review set) created, accessed, or changed, by the activity listed in the *Operation* property. |
| ObjectName | The name of the object (for example, a search, hold or review set) created, accessed, or changed, by the activity listed in the Operation property. |
| ObjectType | The type of eDiscovery object created, deleted, or modified. For example, a search action (generate sample results or trigger an export from search) are listed as *Search* in this field. |
| Operation | The name of the operation that corresponds to the eDiscovery activity that was performed. |
| OrganizationId | The GUID for your Microsoft 365 organization. |
| QueryId | The GUID of the query associated with the activity. |
| QueryText | The query text associated with the activity, such as a search statistic process or add to review process. |
| RecordType | The type of operation indicated by the record. |
| ResultStatus | If the action (specified in the Operation property) was successful or not. |
| Settings | Settings applied to the eDiscovery activity. |
| StartTime | The date and time in Coordinated Universal Time (UTC) when the eDiscovery activity was started. |
| UserCancelled | Whether the specific activity was canceled by the user. |
| UserId | The user who performed the activity (specified in the Operation property) that resulted in the record being logged. |
| UserKey | An alternative ID for the user identified in the UserId property. For eDiscovery activities, the value for this property is typically the same as the UserId property. |
| UserServicePlan | The subscription used by your organization. For eDiscovery activities, this property is typically blank. |
| UserType | The type of user that performed the operation. The following values indicate the user type.  0 A regular user. 2 An administrator in your organization. 3 A Microsoft datacenter administrator or datacenter system account. 4 A system account. 5 An application. 6 A service principal. |
| Version | The version number of the activity (identified by the Operation property) that's logged. |
| Workload | The service where the activity occurred. |

## Encrypted message portal activities

Your organization can access logs for encrypted messages through the encrypted message portal. These logs help you determine when your external recipients read and forward messages. For more information about enabling and using encrypted message portal activity logs, see [Encrypted message portal activity log](audit-log-encrypted-messages).

Each audit entry for a tracked message contains the following fields:

- **MessageID**: Contains the ID of the message being tracked. Use this key identifier to follow a message through the system.
- **Recipient**: List of all recipient email addresses.
- **Sender**: The originating email address.
- **AuthenticationMethod**: Describes the authenticating method for accessing the message, such as OTP, Yahoo, Gmail, or Microsoft.
- **AuthenticationStatus**: Contains a value indicating that the authentication succeeded or failed.
- **OperationStatus**: Whether the indicated operation succeeded or failed.
- **AttachmentName**: Name of the attachment.
- **OperationProperties**: A list of optional properties. For example, the number of OTP passcodes sent, or the email subject.

## eSignature activities

The following table lists the eSignature activities that the Microsoft 365 audit log records. For more information, see [eSignature for Microsoft 365](/en-us/microsoft-365/documentprocessing/esignature-overview).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Cancelled by the requestor | ESignatureRequestCanceled | The signing request was cancelled by the requestor. |
| Declined by a signer | ESignatureRequestDeclined | A signer declined the request. |
| Document was downloaded | ESignatureRequestDownloaded | The document was downloaded by a member of the workflow. |
| Document was viewed | ESignatureDocumentViewed | The document was viewed by a member of the workflow. |
| Link to the signed document expired | ESignatureRequestExpired | The link to the signed document expired. |
| Request was completed | ESignatureRequestCompleted | An electronic signature request was completed. |
| Request was created | ESignatureRequestCreated | An electronic signature request was created by a member of the organization. |
| Request was sent | ESignatureRequestSent | An electronic signature request was sent to recipients. |
| Request was signed by a user | ESignatureDocumentSigned | An electronic signature request was signed by a recipient. |

## Exchange admin activities

Exchange administrator audit logging (which Microsoft 365 enables by default) logs an event in the audit log when an administrator (or a user assigned administrative permissions) makes a change in your Exchange Online organization. The Exchange admin audit log records changes made by using the Exchange admin center or by running a cmdlet in Exchange Online PowerShell. The audit log doesn't record cmdlets that begin with the verbs **Get-**, **Search-**, or **Test-**. For more detailed information about admin audit logging in Exchange, see [Administrator audit logging](/en-us/exchange/administrator-audit-logging-exchange-2013-help).

Important

Some Exchange Online cmdlets aren't logged in the Exchange admin audit log or in the audit log. Many of these cmdlets relate to maintaining the Exchange Online service and Microsoft datacenter personnel or service accounts run them. These cmdlets aren't logged because they would result in a large number of "noisy" auditing events. If there's an Exchange Online cmdlet that isn't being audited, submit a design change request (DCR) to Microsoft Support.

Use these tips to search for Exchange admin activities when searching the audit log:

- Use the date range boxes and the **Users** list to narrow the search results for cmdlets run by a specific Exchange administrator within a specific date range.
- Select the **Activity** column to sort the cmdlet names in alphabetical order and display events from the Exchange admin audit log.
- Select the **Download all results** option to export the search results and get information about what cmdlet was run, which parameters and parameter values were used, and what objects were affected. For more information, see [Export, configure, and view audit log records](audit-log-export-records).
- Use the `Search-UnifiedAuditLog -RecordType ExchangeAdmin` command in Exchange Online PowerShell to return only audit records from the Exchange admin audit log. It might take up to 30 minutes after an Exchange cmdlet is run for the corresponding audit log entry to be returned in the search results. For more information, see [Search-UnifiedAuditLog](/en-us/powershell/module/exchange/search-unifiedauditlog). For information about exporting the search results returned by the **Search-UnifiedAuditLog** cmdlet to a CSV file, see the "Tips for exporting and viewing the audit log" section in [Export, configure, and view audit log records](audit-log-export-records#tips-for-exporting-and-viewing-the-audit-log).

## Exchange mailbox activities

The following table lists the activities recorded in the Microsoft 365 audit log. Mailbox audit logging automatically logs mailbox activities performed by the mailbox owner, a delegated user, or an administrator in the audit log for up to 180 days. An admin can turn off mailbox audit logging for all users in your organization. In this case, no mailbox actions for any user are logged. For more information, see [Manage mailbox auditing](audit-mailboxes).

Important

The default retention period for Audit (Standard) changed from 90 days to 180 days. Audit (Standard) logs generated before October 17, 2023, are retained for 90 days. Audit (Standard) logs generated on or after October 17, 2023, follow the new default retention of 180 days.

You can also search for mailbox activities by using the **Search-UnifiedAuditLog** cmdlet in [Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Accessed mailbox attachments | AttachmentAccess | A message attachment was accessed. |
| Accessed Mailbox folder | FolderBind | A mailbox folder was accessed. This action is also logged when the admin or delegate opens the mailbox. Audit records for folder bind actions performed by delegates are consolidated. One audit record is generated for individual folder access within a 24-hour period. |
| Accessed mailbox items | MailItemsAccessed | Messages were read or accessed in mailbox. Audit records for this activity are triggered in one of two ways: when a mail client (such as Outlook) performs a bind operation on messages or when mail protocols (such as Exchange ActiveSync or IMAP) sync items in a mail folder. Analyzing audit records for this activity is useful when investigating compromised email account. |
| Accessed message | MessageBind | A message was viewed in the preview pane or opened by an admin. This value is available only for users without E5/A5/G5 licenses. |
| Added delegate mailbox permissions | Add-MailboxPermission | An administrator assigned the FullAccess mailbox permission to a user (known as a delegate) to another person's mailbox. The FullAccess permission allows the delegate to open the other person's mailbox, and read and manage the contents of the mailbox. The audit record for this activity is also generated when a system account in the Microsoft 365 service periodically performs maintenance tasks in behalf of your organization. A common task performed by a system account is updating the permissions for system mailboxes. For more information, see System accounts in Exchange mailbox audit records. |
| Added or removed user with delegate access to calendar folder | UpdateCalendarDelegation | A user was added or removed as a delegate to the calendar of another user's mailbox. Calendar delegation gives someone else in the same organization permissions to manage the mailbox owner's calendar. |
| Added permissions to folder | AddFolderPermissions | A folder permission was added. Folder permissions control which users in your organization can access folders in a mailbox and the messages located in those folders. |
| Copied messages to another folder | Copy | A message was copied to another folder. |
| Created mailbox item | Create | An item is created in the Calendar, Contacts, Notes, or Tasks folder in the mailbox. For example, a new meeting request is created. Creating, sending, or receiving a message isn't audited. Also, creating a mailbox folder isn't audited. |
| Created new inbox rule in Outlook web app | New-InboxRule | A mailbox owner or other user with access to the mailbox created an inbox rule in the Outlook web app. |
| Delete priority cleanup label item | PriorityCleanupDelete | The item with a label of Priority Cleanup type is getting deleted. |
| Deleted messages from Deleted Items folder | SoftDelete | A message was permanently deleted or deleted from the Deleted Items folder. These items are moved to the Recoverable Items folder. Messages are also moved to the Recoverable Items folder when a user selects it and presses **Shift+Delete**. |
| Label message as a record |  | A user applied a retention label to an email message and that label is configured to mark the item as a record. |
| Labeled item as a record | ApplyRecord | An item is labeled as a record. |
| Labeled message as a record | ApplyRecordLabel | A message was classified as a record. Occurs when a retention label that classifies content as a record is manually or automatically applied to a message. |
| Modified folder permission | ModifyFolderPermissions | A folder permission was changed. Folder permissions control which users in your organization can access mailbox folders and the messages in the folder. |
| Modified inbox rule from Outlook web app | Set-InboxRule | A mailbox owner or other user with access to the mailbox modified an inbox rule using the Outlook web app. |
| Moved messages to another folder | Move | A message was moved to another folder. |
| Moved messages to Deleted Items folder | MoveToDeletedItems | A message was deleted and moved to the Deleted Items folder. |
| Perform search query | SharepointSearchQueryInitiated | The user performs a search on SharePoint. |
| Preserve Mailbox item | PreservedMailItemProactively | The mail item is proactively preserved. Proactive preservation is a Microsoft Purview Data Lifecycle Management (DLM) feature, where mails deleted by risky users in the tenant are preserved in dumpster. |
| Priority cleanup label applied | ApplyPriorityCleanup | The Priority Cleanup label is applied to an item. |
| Priority cleanup label applied on Exchange item | ApplyPriorityCleanup | A retention label for priority cleanup is applied to an item on Exchange. |
| Purged messages from the mailbox | HardDelete | A message was purged from the Recoverable Items folder (permanently deleted from the mailbox). |
| Removed delegate mailbox permissions | Remove-MailboxPermission | An administrator removed the FullAccess permission (that was assigned to a delegate) from a person's mailbox. After the FullAccess permission is removed, the delegate can't open the other person's mailbox or access any content in it. |
| Removed permissions from folder | RemoveFolderPermissions | A folder permission was removed. Folder permissions control which users in your organization can access folders in a mailbox and the messages located in those folders. |
| Search items in a mailbox | SearchQueryInitiated | A person uses Outlook (Windows, Mac, iOS, Android, or Outlook on the web) or the Mail app for Windows 10 to search for items in a mailbox. |
| Sent message | Send | A message was sent, replied to, or forwarded. |
| Sent message using Send As permissions | SendAs | A message was sent using the SendAs permission. This means that another user sent the message as though it came from the mailbox owner. |
| Sent message using Send On Behalf permissions | SendOnBehalf | A message was sent using the SendOnBehalf permission. This means that another user sent the message on behalf of the mailbox owner. The message the recipient to whom the message was sent on behalf of and who actually sent the message. |
| Update item label | UpdateComplianceTag | When the label is applied to an item. |
| Updated inbox rules from Outlook client | UpdateInboxRules | A mailbox owner or other user with access to the mailbox created, modified, or removed an inbox rule by using the Outlook client. |
| Updated message | Update | A message or its properties was changed. |
| User signed in to mailbox | MailboxLogin | The user signed in to their mailbox. |

### System accounts in Exchange mailbox audit records

In audit records for some mailbox activities, especially **Add-MailboxPermissions**, you might see the user who performed the activity identified as NT AUTHORITY\SYSTEM or NT SERVICE\MSExchangeAdminApiNetCore(Microsoft.Exchange.AdminApi.NetCore). This system account in the Exchange service in the Microsoft cloud performs scheduled maintenance tasks on behalf of your organization. For example, a common audited activity performed by the NT SERVICE\MSExchangeAdminApiNetCore(Microsoft.Exchange.AdminApi.NetCore) account is updating the permissions on the DiscoverySearchMailbox, which is a system mailbox. This update verifies that the FullAccess permission (which is the default) is assigned to the Discovery Management role group for the DiscoverySearchMailbox. This update ensures that eDiscovery administrators can perform necessary tasks in their organization.

Another system user account that might appear in an audit record for **Add-MailboxPermission** is Administrator@apcprd03.prod.outlook.com. This service account also appears in mailbox audit records related to verifying and updating the FullAccess permission assigned to the Discovery Management role group for the DiscoverySearchMailbox system mailbox. Specifically, audit records that identify the Administrator@apcprd03.prod.outlook.com account typically trigger when Microsoft support personnel run a role-based access control diagnostic tool on behalf of your organization.

## Fabric activities

The following table lists the Microsoft Fabric activities in Power BI that the Microsoft 365 audit log records. You can search the audit log for these activities in Power BI. For information about audit settings, see [Audit and usage tenant settings](/en-us/fabric/admin/service-admin-portal-audit-usage).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Applied a PostgreSQL database schema | ApplyPostgreSQLDatabaseSchema | Generated when a user applies (plans and executes) a PostgreSQL database schema through the custom PG schema service (pgschema-based ALM flow). The audit log records caller identity, operation result, and the affected PostgreSQL database artifact. |
| Assign Warehouse Server Alias | AssignWarehouseServerAlias | A workspace administrator assigned a server alias to a Fabric Warehouse workspace. |
| Automatically bound user credentials to Git | AutoBoundGitCredentials | Automatically bound user credentials to Git. |
| Branch workspace admin profile configured | GitBranchWorkspaceAdminProfileConfigured | Branch workspace admin profile configured. |
| Branch workspace configured | GitBranchWorkspaceConfigured | Branch workspace configured. |
| Branched out to a workspace in Git | GitBranchedOut | Branched out to a workspace in Git. |
| Browsed PostgreSQL database objects | PgSQLDbObjectExplorer | Generated when a user browses PostgreSQL database schema objects through Object Explorer. The audit log records caller identity, operation result, and the affected PostgreSQL database artifact. |
| Cancelled a Digital Operations Ontology Agent conversation | DigitalOperationsOntologyAgentConversationCancelled | A user canceled a Digital Operations Ontology Agent conversation. |
| Checked out Git branch | GitCheckedOutBranch | Checked out Git branch. |
| Compute Items Sizes | ComputeItemsSize | Calculated current size of all items for the OneLake item-size report. |
| Create the cross tenant auth mapping | CreateCrossTenantAuthMapping | Create a user mapping for the cross tenant auth feature. |
| Created Artifact Definition | CreatedArtifactDefinition | Created Artifact Definition is a Fabric External Sources activity which is generated when an External Sources artifact definition is created. Shared across item types: for MirroredStorage it carries SourceType and ConnectionId; for AWS Databricks Catalog it carries CatalogName, WorkspaceConnectionId, and MirroringMode. |
| Created AWS Databricks Catalog | CreatedAWSDatabricksCatalog | Created AWS Databricks Catalog is an AWSDatabricksCatalog activity which is generated when a Fabric AWS Databricks Catalog item is created, capturing the bound AWS Databricks workspace ConnectionId and the initial MirroredScope (catalogs/schemas/tables selected for mirroring). |
| Created a Digital Operations Ontology Agent conversation | DigitalOperationsOntologyAgentConversationCreated | A user created a Digital Operations Ontology Agent conversation. |
| Created a Fabric Copilot session | FabricCopilotSessionCreated | A user created a Fabric Copilot session. |
| Create a Microsoft Fabric free trial | CreatedFabricTrial | A new Microsoft Fabric free trial capacity was started. |
| Created MirroredStorage | CreatedMirroredStorage | Generated when a user or service principal creates a Fabric MirroredStorage item, linking an external storage source to a workspace as OneLake shortcuts. |
| Created workspace relation | CreatedWorkspaceRelation | Created workspace relation. |
| Deleted a Fabric Copilot session | FabricCopilotSessionDeleted | A user deleted a Fabric Copilot session. |
| Deleted a task flow | DeletedTaskFlow | Deleted a task flow. |
| Deleted connection by tenant admin | DeletedGatewayClusterDatasourceAsAdmin | A tenant admin deleted the connection. |
| Deleted connection role assignment by tenant admin | DeletedGatewayDatasourceByAdmin | A tenant admin deleted the connection role assignment. |
| Deleted workspace relation | DeletedWorkspaceRelation | Deleted workspace relation. |
| Downloaded dataflow refresh logs | DownloadedDataflowRefreshLogs | Downloaded dataflow refresh logs. |
| Edited Power BI semantic model options | EditedSemanticModelOptions | A user made a change to their semantic model options. This occurs when changes are made in the model options dialog. |
| Executed a tenant relocation | TenantRelocationExecuted | Executed tenant relocation. |
| Export item definitions | ExportItemDefinitions | Export multiple item definitions from a workspace. |
| Exported a PostgreSQL database schema | ExportPostgreSQLDatabaseSchema | Generated when a user dumps a PostgreSQL database schema through the custom PG schema service (pgschema-based ALM flow). The audit log records caller identity, operation result, and the affected PostgreSQL database artifact. |
| Get Items Sizes | GetItemsSize | Retrieved cached item sizes for the OneLake item-size report. |
| Get connection by tenant admin | GetGatewayClusterDatasourceAsAdmin | A tenant admin retrieved the connection details. |
| Get on-demand billing limits | GetOnDemandBillingLimits | Generated when a capacity admin opens the On-demand billing page and the current billing categories and their 24-hour compute limits are returned for a Fabric capacity. |
| Get on-demand billing quota | GetOnDemandBillingQuota | Generated when the On-demand billing experience loads and the subscription-level on-demand billing quota usage and limits are retrieved. |
| Get BackupVault's Immutability state. | GetBackupVaultImmutability | Get BackupVault's Immutability state. |
| Get Capacity Overage Config. This can happen via Public API or using UX. | GetCapacityOverageBillingConfiguration | Get Capacity Overage Config. This can happen via Public API or using UX. |
| Git connection settings updated | GitConnectionSettingsUpdated | Git connection settings updated. |
| Granted consent to tenant relocation | TenantRelocationConsentGranted | Tenant relocation consent granted. |
| Import item definitions | ImportItemDefinitions | Import multiple item definitions into a workspace. |
| Imported OneLake lifecycle policy | ImportedLifecyclePolicy | Imported OneLake Lifecycle policy. |
| Imported PostgreSQL sample data | ImportSampleDataToPostgreSQLDatabase | Generated when a user imports supported sample data into a Fabric Native PostgreSQL database. The audit log records caller identity, operation result, and the affected PostgreSQL database artifact. |
| Initialized connection to Git | GitConnectionInitialized | Initialized connection to Git. |
| Item definition exported | ItemDefinitionExported | A Fabric item definition has been exported. |
| List all of the cross tenant auth mappings | ListCrossTenantAuthMappings | List cross tenant auth mappings in a tenant. |
| Logged in to Git provider | ConfiguredGitProviderCredentials | Logged in to Git provider. |
| Logged out of Git provider | DeletedGitProviderCredentials | Logged out of Git provider. |
| Microsoft Fabric Audit activity to retrieve FMI bindings | GetFabricManagedIdentityBindings | Microsoft Fabric Audit activity to retrieve FMI bindings. |
| Migrate Gen1 dataflow | MigrateGen1Dataflow | A user upgraded a Power BI Gen1 dataflow to a Fabric Gen2.1 dataflow in place by using the Upgrade Wizard. |
| Modified OneLake default tier | ModifiedDefaultTier | Modified OneLake default tier. |
| Modified OneLake file soft-delete settings | ModifiedOneLakeFileSoftDeleteSettings | Generated when a workspace admin changes the OneLake file-level soft-delete retention settings (enable/disable, retention period). |
| Planning session upgraded | PlanningSessionUpgraded | Session type is upgraded in planning workload. |
| Recover an artifact | ArtifactRecovered | A user recovered a previously soft-deleted artifact, such as a gateway or gateway cluster member, restoring it to active state. |
| Refreshed AWS Databricks Catalog Shortcuts | RefreshedAWSDatabricksCatalogShortcuts | Refreshed AWS Databricks Catalog shortcuts is an AWSDatabricksCatalog activity which is generated when the refresh-catalog-metadata operation re-syncs the already-mirrored shortcuts against the underlying AWS Databricks Unity Catalog. |
| Retrieved artifact's Logical Id | ArtifactLogicalIdRetrieved | Retrieved artifact's Logical Id. |
| Retrieved PostgreSQL SQL audit policy | GetSqlAuditPolicyOnDatabase | Generated when a user retrieves the SQL audit policy settings for a PostgreSQL database artifact. The audit log records caller identity, operation result, and the affected PostgreSQL database artifact. |
| Revoked consent to tenant relocation | TenantRelocationConsentRevoked | Tenant relocation consent revoked. |
| Sent a Digital Operations Ontology Agent message | DigitalOperationsOntologyAgentMessageSent | A user sent a message in a Digital Operations Ontology Agent conversation. |
| Sent a Fabric Copilot message | FabricCopilotSessionMessageSent | A user sent a message in a Fabric Copilot session. |
| Set BackupVault's Immutability state. | SetBackupVaultImmutability | Set BackupVault's Immutability state. |
| Set PostgreSQL SQL audit policy | SetSqlAuditPolicyOnDatabase | Generated when a user updates SQL audit policy settings for a PostgreSQL database artifact. The audit log records caller identity, operation result, and the affected PostgreSQL database artifact. |
| Set Warehouse Connection Mode To Automatic | SetWarehouseConnectionModeToAutomatic | A workspace administrator set the Fabric Warehouse SQL connection mode to Automatic. |
| Set Warehouse Connection Mode To Proxy | SetWarehouseConnectionModeToProxy | A workspace administrator set the Fabric Warehouse SQL connection mode to Proxy. |
| Set Warehouse Connection Mode To Redirect | SetWarehouseConnectionModeToRedirect | A workspace administrator set the Fabric Warehouse SQL connection mode to Redirect. |
| Set Warehouse Hardware Acceleration | SetWarehouseHardwarePlatform | Changed the current hardware acceleration settings for warehouses in a workspace. |
| Soft delete an artifact | ArtifactSoftDeleted | A user soft deleted an artifact, such as a gateway or gateway cluster member, marking it for deletion while allowing recovery within a retention period. |
| Switched Git branch | GitSwitchedBranch | Switched Git branch for workspace. |
| Update on-demand billing limits | UpdateOnDemandBillingLimits | Generated when a capacity admin enables or disables a billing category, or changes its 24-hour compute limit, on a Fabric capacity. One audit event is emitted per billing category. |
| Update Capacity Overage Config. This can happen via Public API or using UX. | UpdateCapacityOverageBillingConfiguration | Update Capacity Overage Config. This can happen via Public API or using UX. |
| Updated a Fabric Copilot session | FabricCopilotSessionUpdated | A user updated a Fabric Copilot session. |
| Updated a Fabric Copilot session state | FabricCopilotSessionStateUpdated | A user updated the state of a Fabric Copilot session. |
| Updated artifact's Logical Id | ArtifactLogicalIdUpdated | Updated artifact's Logical Id. |
| Updated authorization setting in GraphQL | UpdatedAuthorizationSettingGraphQL | Updated authorization setting in GraphQL. |
| Updated Artifact Definition | UpdatedArtifactDefinition | Updated Artifact Definition is a Fabric External Sources activity which is generated when an External Sources artifact definition is updated via the update-item-definition API. Shared across item types (e.g. MirroredStorage, AWS Databricks Catalog); the properties carried depend on the item type. |
| Updated AWS Databricks Catalog Definition | UpdatedAWSDatabricksCatalogDefinition | Updated AWS Databricks Catalog definition is an AWSDatabricksCatalog activity which is generated when the item's Databricks workspace connection or mirrored scope (catalogs/schemas/tables) is updated via the update-item-definition API. |
| Updated connection role assignment by tenant admin | UpdatedGatewayDatasourceByAdmin | A tenant admin add or updates the connection role assignment. |
| validate connection access for a given identity. | ValidatedConnectionAccess | validate connection access for a given identity. |
| Updated git items selection | GitItemsSelectionUpdated | Updated git items selection. |
| Updated MirroredStorage definition | UpdatedMirroredStorageDefinition | Generated when a user or service principal modifies the mirroring scope of an existing MirroredStorage item, changing which external paths are exposed in OneLake. |
| Unassign Warehouse Server Alias | UnassignWarehouseServerAlias | A workspace administrator assigned a server alias to a Fabric Warehouse workspace. |
| Workspace relations retrieved | WorkspaceRelationsRetrieved | Workspace relations retrieved. |

## File and page activities

The following table lists the file and page activities in SharePoint and OneDrive that the Microsoft 365 audit log records.

| Friendly name | Operation | Description |
| --- | --- | --- |
| (none) | FileAccessedExtended | This activity is related to the "Accessed file" (FileAccessed) activity. A FileAccessedExtended event is logged when the same person continually accesses a file for an extended period (up to three hours).  The purpose of logging FileAccessedExtended events is to reduce the number of FileAccessed events that are logged when a file is continually accessed. This approach helps reduce the noise of multiple FileAccessed records for what is essentially the same user activity, and lets you focus on the initial (and more important) FileAccessed event. |
| (none) | FileModifiedExtended | This activity is related to the "Modified file" (FileModified) activity. A FileModifiedExtended event is logged when the same person continually modifies a file for an extended period (up to three hours).  The purpose of logging FileModifiedExtended events is to reduce the number of FileModified events that are logged when a file is continually modified. This approach helps reduce the noise of multiple FileModified records for what is essentially the same user activity, and lets you focus on the initial (and more important) FileModified event. |
| (none) | FilePreviewed | User previews files on a SharePoint or OneDrive site. These events typically occur in high volumes based on a single activity, such as viewing an image gallery. |
| (none) | PagePrefetched | A user's client (such as website or mobile app) requests the indicated page to help improve performance if the user browses to it. This event is logged to indicate that the page content is served to the user's client. This event isn't a definitive indication that the user navigated to the page.  When the client renders the page content (as per the user's request), it should generate a ClientViewSignaled event. Not all clients support indicating a prefetch, and therefore some prefetched activities might instead be logged as PageViewed events. |
| (none) | PageViewedExtended | This activity is related to the "Viewed page" (PageViewed) activity. A PageViewedExtended event is logged when the same person continually views a web page for an extended period (up to three hours).  The purpose of logging PageViewedExtended events is to reduce the number of PageViewed events that are logged when a page is continually viewed. This approach helps reduce the noise of multiple PageViewed records for what is essentially the same user activity, and lets you focus on the initial (and more important) PageViewed event. |
| Accessed file | FileAccessed | User or system account accesses a file. After a user accesses a file, the system doesn't log the FileAccessed event again for the same user and file for the next five minutes. |
| Archived file | FileArchived | A user or system account archived a file with Microsoft 365 Archive. When an automatic file archive policy archives the file, the event includes the policy ID, policy version, and the file's last access date. |
| Changed record status to locked | LockRecord | The record status of a retention label that classifies a document as a record is locked. This status means the document wasn't modified or deleted. Only users assigned at least the contributor permission for a site can change the record status of a document. |
| Changed record status to unlocked | UnlockRecord | The record status of a retention label that classifies a document as a record is unlocked. This status means that the document can be modified or deleted. Only users assigned at least the contributor permission for a site can change the record status of a document. |
| Changed retention label for a file | ComplianceSettingChanged | A retention label is applied to or removed from a document. This event is triggered when a retention label is manually or automatically applied to a message. |
| Checked in file | FileCheckedIn | User checks in a document that they checked out from a document library. |
| Checked out file | FileCheckedOut | User checks out a document located in a document library. Users can check out and make changes to documents that are shared with them. |
| Copied file | FileCopied | User copies a document from a site. The copied file can be saved to another folder on the site. |
| Deleted file | FileDeleted | User deletes a document from a site. |
| Deleted file from recycle bin | FileDeletedFirstStageRecycleBin | User deletes a file from the recycle bin of a site. |
| Deleted file from second-stage recycle bin | FileDeletedSecondStageRecycleBin | User deletes a file from the second-stage recycle bin of a site. |
| Deleted file marked as a record | RecordDelete | A document or email that was marked as a record is deleted. An item is considered as a record when a retention label that marks items as a record is applied to content. |
| Detected document sensitivity mismatch | DocumentSensitivityMismatchDetected | User uploads a document to a site that's protected with a sensitivity label and the document has a higher priority sensitivity label than the sensitivity label applied to the site. For example, a document labeled Confidential is uploaded to a site labeled General.  This event isn't triggered if the document has a lower priority sensitivity label than the sensitivity label applied to the site. For example, a document labeled General is uploaded to a site labeled Confidential. For more information about sensitivity label priority, see [Label priority (order matters)](sensitivity-labels#label-priority-order-matters). |
| Detected malware in file | FileMalwareDetected | SharePoint anti-virus engine detects malware in a file. |
| Discarded file checkout | FileCheckOutDiscarded | User discards (or undoes) a checked out file. That means any changes they made to the file when it was checked out are discarded, and not saved to the version of the document in the document library. |
| Downloaded file | FileDownloaded | User downloads a document from a site. |
| Modified file | FileModified | User or system account modifies the content or the properties of a document on a site. The system waits five minutes before it logs another FileModified event when the same user modifies the content or properties of the same document. |
| Moved file | FileMoved | User moves a document from its current location on a site to a new location. |
| Performed search query | SearchQueryPerformed | User or system account performs a search in SharePoint or OneDrive. Some common scenarios where a service account performs a search query include applying an eDiscovery holds and retention policy to sites and OneDrive accounts, and autoapplying retention or sensitivity labels to site content. To enable logging for this activity, see [Get started with auditing solutions](audit-get-started). |
| Priority cleanup move file to recycle bin | PriorityCleanupFileRecycled | An item is moved to Stage 2 recycle bin by a priority cleanup policy on OneDrive or SharePoint Online. |
| Priority cleanup permanent delete of file | PriorityCleanupFileDeleted | An item is permanently deleted by a priority cleanup policy on OneDrive or SharePoint Online. |
| Reactivated file | FileUnarchived | A file archived with Microsoft 365 Archive was reactivated and is available to access. |
| Recycled a file | FileRecycled | User moves a file into the SharePoint Recycle Bin. |
| Recycled a folder | FolderRecycled | User moves a folder into the SharePoint Recycle Bin. |
| Recycled all minor versions of file | FileVersionsAllMinorsRecycled | User deletes all minor versions from the version history of a file. The deleted versions are moved to the site's recycle bin. |
| Recycled all versions of file | FileVersionsAllRecycled | User deletes all versions from the version history of a file. The deleted versions are moved to the site's recycle bin. |
| Recycled version of file | FileVersionRecycled | User deletes a version from the version history of a file. The deleted version is moved to the site's recycle bin. |
| Renamed file | FileRenamed | User renames a document. |
| Requested file reactivation | FileUnarchiveRequested | A user requested to reactivate a file archived with Microsoft 365 Archive. |
| Restored file | FileRestored | User restores a document from the recycle bin of a site. |
| Started bulk deleting file versions | FileVersionBulkDeletionStarted | Admin started a bulk deletion of file versions across a SharePoint site or document library to reclaim storage space by permanently removing old versions that exceed the version policy. |
| Started bulk expiring file versions by using a schedule file | FileVersionBulkExpirationByScheduleStarted | Admin starts a bulk expiration of file versions using a schedule file on a SharePoint site, applying version expiration according to that schedule. |
| Started generating file version expiration report | FileVersionExpirationReportStarted | Admin started generating a file version expiration report for a SharePoint site or document library that includes certain version metadata and expiration information. |
| Started tenant apply file version policy | TenantApplyFileVersionPolicyStarted | Admin started applying the tenant-level file version policy across all sites in the organization, which sets version limits or trims existing versions for all document libraries tenant-wide. |
| Started updating version settings on all document libraries in the site | DocumentLibraryVersionPolicyBulkUpdateStarted | Admin started a bulk update of version policy settings across all document libraries in a SharePoint site. |
| Uploaded file | FileUploaded | User uploads a document to a folder on a site. |
| View signaled by client | ClientViewSignaled | A user's client (such as website or mobile app) signals that the indicated page is viewed by the user. This activity is often logged following a PagePrefetched event for a page. **NOTE**: Because ClientViewSignaled events are signaled by the client, rather than the server, it's possible the event might not be logged by the server and therefore might not appear in the audit log. It's also possible that information in the audit record might not be trustworthy. However, because the user's identity is validated by the token used to create the signal, the user's identity listed in the corresponding audit record is accurate. The system waits five minutes before it logs the same event when the same user's client signals that the page is viewed again by the user. |
| Viewed page | PageViewed | User views a page on a site. This activity doesn't include using a Web browser to view files located in a document library. After a user views a page, the system doesn't log the PageViewed event again for the same user and page for the next five minutes. |

### Frequently asked questions about FileAccessed and FilePreviewed events

**Can non-user activities trigger FilePreviewed audit records that include a user agent like "OneDriveMpc-Transform\_Thumbnail"?**

There are no known scenarios where non-user actions generate events like these. User actions like opening a user profile card (by selecting their name or email address in a message in Outlook on the web) generate similar events.

**Are calls to the OneDriveMpc-Transform\_Thumbnail always intentionally triggered by the user?**

No. But browser prefetch can result in similar events.

**If I see a FilePreviewed event coming from a Microsoft-registered IP address, does that mean the preview shows on the screen of the user's device?**

No. Browser prefetch might log the event.

**Are there scenarios where a user previewing a document generates FileAccessed events?**

Both the FilePreviewed and FileAccessed events indicate that a user's call led to a read of the file (or a read of a thumbnail rendering of the file). While these events are intended to align with preview versus access intention, the event distinction isn't a guarantee of the user's intent.

**What causes FileAccessed audit events in Insider Risk Management scenarios?**

Creating a case in Insider Risk Management and enabling Content Explorer generates and records a FileAccessed event in the audit log. In this scenario, the event is generated by the Insider Risk Management/Content Explorer workflow rather than by a direct user file-open action, and the same ApplicationId value, `00001111-aaaa-2222-bbbb-3333cccc4444`, is used for these events. This is important for administrators because it helps distinguish these system-generated FileAccessed events from other FileAccessed activity during an investigation. You can use the ApplicationId field as one of the properties to help identify or filter these specific events when reviewing audit log results.

### The app@sharepoint user in audit records

In audit records for some file activities (and other SharePoint-related activities), you might notice the user who performed the activity (identified in the User and UserId fields) is app@sharepoint. This user means that an application performed the activity. In this case, the application was granted permissions in SharePoint to perform organization-wide actions (such as searching a SharePoint site or OneDrive account) on behalf of a user, admin, or service. This process of giving permissions to an application is called *SharePoint App-Only* access. This user means that an application, instead of a user, presented the authentication to SharePoint to perform an action. This is why the app@sharepoint user is identified in certain audit records. For more information, see [Grant access using SharePoint App-Only](/en-us/sharepoint/dev/solution-guidance/security-apponly-azureacs).

For example, app@sharepoint is often identified as the user for "Performed search query" and "Accessed file" events. That's because an application with SharePoint App-Only access in your organization performs search queries and accesses files when applying retention policies to sites and OneDrive accounts.

Here are a few other scenarios where app@sharepoint might be identified in an audit record as the user who performed an activity:

- **Microsoft 365 Groups**. When a user or admin creates a new group, audit records are generated for creating a site collection, updating lists, and adding members to a SharePoint group. An application performs these tasks on behalf of the user who created the group.
- **Microsoft Teams**. Similar to Microsoft 365 Groups, audit records are generated for creating a site collection, updating lists, and adding members to a SharePoint group when a team is created.
- **Compliance features**. When an admin implements compliance features, such as retention policies, eDiscovery holds, and autoapplying sensitivity labels.

In these and other scenarios, you might also notice that multiple audit records with app@sharepoint as the specified user were created within a short time frame, often within a few seconds of each other. This pattern also means they were probably triggered by the same user-initiated task. Also, the ApplicationDisplayName and EventData fields in the audit record might help you identify the scenario or application that triggered the event.

## Microsoft 365 Archive file-level policy activities

The following table lists Microsoft 365 Archive file-level policy activities in SharePoint and OneDrive that are recorded in the Microsoft 365 audit log. For audit activity generated when an individual file is archived, see File and page activities.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Added site to file archive policy | FileArchivePolicySiteAdded | An admin added a site to an automatic file archive policy. |
| Changed file archive policy | FileArchivePolicyChanged | An admin changed an automatic file archive policy. |
| Completed file archive policy run | FileArchivePolicyRunCompleted | A run of an automatic file archive policy completed. The event includes the run outcome, number of files archived, amount of storage archived, number of sites processed, and whether the policy ran in what-if mode. |
| Created file archive policy | FileArchivePolicyCreated | An admin created an automatic file archive policy. |
| Deleted file archive policy | FileArchivePolicyDeleted | An admin deleted an automatic file archive policy. |
| Removed site from file archive policy | FileArchivePolicySiteRemoved | An admin removed a site from an automatic file archive policy. |
| Started file archive policy | FileArchivePolicyStarted | An admin started an automatic file archive policy. |

## Folder activities

The following table lists the folder activities in SharePoint and OneDrive recorded in the Microsoft 365 audit log. Audit records for some SharePoint activities indicate the app@sharepoint user performed the activity on behalf of the user or admin who initiated the action. For more information, see The app@sharepoint user in audit records.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Copied folder | FolderCopied | User copies a folder from a site to another location in SharePoint or OneDrive. |
| Created folder | FolderCreated | User creates a folder on a site. |
| Deleted folder | FolderDeleted | User deletes a folder from a site. |
| Deleted folder from recycle bin | FolderDeletedFirstStageRecycleBin | User deletes a folder from the recycle bin on a site. |
| Deleted folder from second-stage recycle bin | FolderDeletedSecondStageRecycleBin | User deletes a folder from the second-stage recycle bin on a site. |
| Modified folder | FolderModified | User modifies a folder on a site. This action includes changing the folder metadata, such as changing tags and properties. |
| Moved folder | FolderMoved | User moves a folder to a different location on a site. |
| Renamed folder | FolderRenamed | User renames a folder on a site. |
| Restored folder | FolderRestored | User restores a deleted folder from the recycle bin on a site. |

## Forms activities

The following table lists the user and admin activities in Microsoft Forms that the Microsoft 365 audit log records. Microsoft Forms is a forms, quiz, and survey tool you can use to collect data for analysis. Some operations include additional activity parameters, as noted in the descriptions.

If a coauthor or an anonymous responder performs a Forms activity, the audit log records it slightly differently. For more information, see the Forms activities performed by coauthors and anonymous responders section.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Added form coauthor | AddFormCoauthor | A user uses a collaboration link to help design the form or view responses. This event is logged when a user uses a collaboration URL (not when the collaboration URL is first generated). |
| Added specific responder | AddSpecificResponder | Form owner adds a new user or group to the specific responders list. |
| Allowed share form for copy | AllowShareFormForCopy | Form owner creates a template link to share the form with other users. This event is logged when the form owner selects to generate the template URL. |
| Connected to Excel workbook | ConnectToExcelWorkbook | Connected the form to an Excel workbook. Property ExcelWorkbookLink:string is the associated Excel workbook ID of the current form. |
| Created a collection | CollectionCreated | Form owner created a collection. |
| Created comment | CreateComment | Form owner adds comment or score to a quiz. |
| Created form | CreateForm | Form owner creates a new form. Property DataMode:string is the current form is set to sync with a new or existing Excel workbook if the property value equals DataSync. Property ExcelWorkbookLink:string is the associated Excel workbook ID of the current form. |
| Created response | CreateResponse | Similar to receiving a new response. A user submitted a response to a form. Property ResponseId:string and Property ResponderId:string is which result is being viewed. For an anonymous responder, the ResponderId property is null. |
| Created summary link | GetSummaryLink | Form owner creates summary results link to share results. |
| Deleted all responses | DeleteAllResponses | Form owner deletes all response data. |
| Deleted collection from the Recycle Bin | CollectionHardDeleted | Form owner hard-deleted a collection from the Recycle Bin. |
| Deleted form | DeleteForm | Form owner deletes a form. This action includes SoftDelete (delete option used and form moved to recycle bin) and HardDelete (Recycle bin is emptied). |
| Deleted Response | DeleteResponse | Form owner deletes one response. Property ResponseId:string is the response being deleted. |
| Deleted summary link | DeleteSummaryLink | Form owner deletes summary results link. |
| Disabled anyone can respond setting | DisallowAnonymousResponse | Form owner turns off the setting allowing anyone to respond to the form. |
| Disabled collaboration | DisableCollaboration | Form owner turns off the setting of collaboration on the form. |
| Disabled specific people can respond setting | DisableSpecificResponse | Form owner turns off the setting allowing only specific people or specific groups in the current organization to respond to the form. |
| Disallowed share form for copy | DisallowShareFormForCopy | Form owner deletes template link. |
| Edited form | EditForm | Form owner edits a form such as creating, removing, or editing a question. The property *EditOperation:string* is the edit operation name. The possible operations are:- CreateQuestion- CreateQuestionChoice - DeleteQuestion - DeleteQuestionChoice - DeleteFormImage - DeleteQuestionImage - UpdateQuestion - UpdateQuestionChoice - UploadFormImage/Bing/Onedrive - UploadQuestionImage - ChangeTheme FormImage includes any place within Forms where the user can upload an image, such as in a query or as a background theme. |
| Enabled anyone can respond setting | AllowAnonymousResponse | Form owner turns on the setting allowing anyone to respond to the form. |
| Enabled Office 365 work or school account collaboration | EnableWorkOrSchoolCollaboration | Form owner turns on the setting allowing users with a Microsoft 365 work or school account to view and edit the form. |
| Enabled people in my organization collaboration | EnableSameOrgCollaboration | Form owner turns on the setting allowing users in the current organization to view and edit the form. |
| Enabled specific people can respond setting | EnableSpecificResponse | Form owner turns on the setting allowing only specific people or specific groups in the current organization to respond to the form. |
| Enabled specific people collaboration | EnableSpecificCollaboaration | Form owner turns on the setting allowing only specific people or specific groups in the current organization to view and edit the form. |
| Exported form | ExportForm | Form owner exports results to Excel. Property ExportFormat:string is if the Excel file is Download or Online. |
| Listed forms | ListForms | Form owner is viewing a list of forms. Property ViewType:string is which view the form owner is looking at: All Forms, Shared with Me, or Group Forms. |
| Moved a form into collection | MovedFormIntoCollection | Form owner moved a form into a collection. |
| Moved a form out of collection | MovedFormOutofCollection | Form owner moved a form out of a collection. |
| Moved collection to the Recycle Bin | CollectionSoftDeleted | Form owner moved a collection to the Recycle Bin. |
| Moved form | MoveForm | Form owner moves a form. Property DestinationUserId:string is the user ID of the person who moved the form. Property NewFormId:string is the new ID for the newly copied form. Property IsDelegateAccess:boolean is the current form move action is performed through the admin delegate page. |
| Previewed form | PreviewForm | Form owner previews a form by using the Preview function. |
| Removed form coauthor | RemoveFormCoauthor | Form owner deletes a collaboration link. |
| Removed specific responder | RemoveSpecificResponder | Form owner removes a user or group from the specific responders list. |
| Renamed a collection | CollectionRenamed | Form owner changed the name of a collection. |
| Sent Forms Pro invitation | ProInvitation | User selects to activate a Pro trial. |
| Submitted response | SubmitResponse | A user submits a response to a form. Property IsInternalForm:boolean is if the responder is within the same organization as the form owner. |
| Updated a collection | CollectionUpdated | Form owner updated a collection property. |
| Updated form phishing status | UpdatePhishingStatus | This event is logged whenever the detailed value for the internal security status changes, regardless of whether this change affects the final security state (for example, form is now Closed or Opened). This change might result in duplicate events without a final security state change. The possible status values for this event are:- Take Down - Take Down by Admin - Admin Unblocked - Auto Blocked - Auto Unblocked - Customer Reported - Reset Customer Reported. |
| Updated form setting | UpdateFormSetting | Form owner updates one or multiple form settings. Property FormSettingName:string is updated sensitive settings' name. Property NewFormSettings:string is updated settings' name and new value. Property thankYouMessageContainsLink:boolean is updated thank-you message contains a URL link. |
| Updated response | UpdateResponse | Form owner updated a comment or score on a quiz. Property ResponseId:string and Property ResponderId:string is which result is being viewed. For an anonymous responder, the ResponderId property is null. |
| Updated user phishing status | UpdateUserPhishingStatus | This event is logged whenever the value for the user security status changes. The value of the user status in the audit record is **Confirmed as Phisher** when the user created a phishing form that the Microsoft Online safety team took down. If an admin unblocks the user, the value of the user's status is set to **Reset as Normal User**. |
| Updated user setting | UpdateUserSetting | Form owner updates a user setting. Property UserSettingName:string is the setting's name and new value. |
| Viewed form (design time) | ViewForm | Form owner opens an existing form for editing. Property AccessDenied:boolean is access of current form is denied due to permission check. Property FromSummaryLink:boolean is current request comes from the summary link page. |
| Viewed response | ViewResponse | Form owner views a particular response. Property ResponseId:string and Property ResponderId:string is which result is being viewed. For an anonymous responder, the ResponderId property is null. |
| Viewed response page | ViewRuntimeForm | User opened a response page to view. This event is logged regardless of whether the user submits a response or not. |
| Viewed responses | ViewResponses | Form owner views the aggregated list of responses. Property ViewType:string is whether form owner is viewing Detail or Aggregate. |

### Forms activities performed by coauthors and anonymous responders

Forms supports collaboration when designing forms and analyzing responses. A form collaborator is known as a *coauthor*. Coauthors can do everything a form owner can do, except delete or move a form. Forms also allows you to create a form that can be responded to anonymously. This means the responder doesn't have to sign in to your organization to respond to a form.

The following table lists the auditing activities and information recorded in the Microsoft 365 audit log for activities performed by coauthors and anonymous responders.

| Activity type | Internal or external user | User ID that's logged | Organization logged in to | Forms user type |
| --- | --- | --- | --- | --- |
| Coauthoring activities | External | `urn:forms:coauthor#a0b1c2d3@forms.office.com`(The second part of the ID is a hash, which differs for different users) | Form owner's org | Coauthor |
| Coauthoring activities | External | UPN | Coauthor's org | Coauthor |
| Coauthoring activities | Internal | UPN | Form owner's org | Coauthor |
| Response activities | Anonymous | `urn:forms:anonymous#a0b1c2d3@forms.office.com`(The second part of the User ID is a hash, which differs for different users) | Form owner's org | Responder |
| Response activities | External | `urn:forms:external#a0b1c2d3@forms.office.com`(The second part of the User ID is a hash, which differs for different users) | Form owner's org | Responder |
| Response activities | External | UPN | Responder's org | Responder |

## Information barriers activities

The following table lists the activities in Information Barriers that the Microsoft 365 audit log records. For more information about Information Barriers, see [Learn about Information Barriers in Microsoft 365](information-barriers).

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Applied information barrier mode to site | SiteIBModeSet | A SharePoint or global administrator applied a mode to the site. |
| Applied segments to site | SiteIBSegmentsSet | A SharePoint, global administrator, or site owner added one or more information barriers segments to a site. |
| Changed AppBypassInformationBarrier setting for the tenant | AppBypassInformationBarrier | A SharePoint or global administrator changed apps access for SharePoint sites. |
| Changed information barrier mode of site | SiteIBModeChanged | A SharePoint or global administrator updated the mode of the site. |
| Changed segments of site | SiteIBSegmentsChanged | A SharePoint or global administrator changed one or more information barriers segments for a site. |
| Disabled information barriers for SharePoint and OneDrive | SPOIBIsDisabled | A SharePoint or global administrator disabled information barriers for SharePoint and OneDrive in the organization. |
| Enabled information barriers for SharePoint and OneDrive | SPOIBIsEnabled | A SharePoint or global administrator disabled information barriers for SharePoint and OneDrive in the organization. |
| Information barriers insights report completed | InformationBarriersInsightsReportCompleted | System completes build of the information barriers insights report. |
| Information barriers insights report OneDrive section queried | InformationBarriersInsightsReportOneDriveSectionQueried | An administrator queries the information barriers insights report for OneDrive accounts. |
| Information barriers insights report scheduled | InformationBarriersInsightsReportSchedule | An administrator schedules the information barriers insights report. |
| Information barriers insights report SharePoint section queried | InformationBarriersInsightsReportSharePointSectionQueried | An administrator queries the information barriers insights report for SharePoint sites. |
| Removed segment from site | SiteIBSegmentsRemoved | A SharePoint or global administrator removes one or more information barriers segments from a site. |

## Microsoft 365 Admin Center Agent Management activities

The following table lists Agent Management activities that the Microsoft 365 audit log records. For more information, see [Manage Microsoft 365 Copilot agents in the Microsoft 365 admin center](/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Blocked Agent | BlockedAgent | An admin blocked an agent. Users in the organization can't use the agent. |
| Deleted Agent | DeletedAgent | An admin deleted a shared agent that deletes the underlying files and the agent. |
| Deployed Agent | DeployedAgent | An admin deployed an agent. The agent becomes active and usable for specific users, groups, or the entire organization. |
| Removed Agent | RemovedAgent | An admin removed a previously installed agent for the whole organization or for specific users and groups. |
| Unblocked Agent | UnblockedAgent | An admin unblocked a previously blocked agent. |
| Updated Agent | UpdatedAgent | An admin updated a custom agent by uploading the latest manifest file. |
| Updated Tenant-level Agent Settings | UpdatedTenantSettings | An admin updated tenant level settings that apply to agents. |

## Microsoft 365 Apps Admin Services cloud policy activities

The following table lists the activities for policy configuration changes in the [Cloud Policy service](/en-us/microsoft-365-apps/admin-center/overview-cloud-policy?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) that the Microsoft 365 audit log records.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Created policy configuration | CreatedPolicyConfig | A new policy configuration was created. |
| Deleted policy configuration | DeletedPolicyConfig | A policy configuration was deleted. |
| Updated policy configuration | UpdatedPolicyConfig | An existing policy configuration was updated, for example by adding, changing, or removing policy settings, or by changing the policy configuration's name, description, or scope. |
| Updated policy configuration priority | UpdatedPolicyConfigPriority | The priority of a policy configuration was changed. |

## Microsoft 365 Apps Admin Services cloud update activities

The following table lists the activities for configuration changes and triggered actions in the [Cloud Update service](/en-us/microsoft-365-apps/admin-center/cloud-update?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) that the Microsoft 365 audit log records.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Device configuration updated | updateddeviceconfiguration | An action for a device managed by Cloud Update was triggered. This action includes triggering a rollback, resuming a rolled back device, or changing the update channel. |
| Profile configuration updated | updatedprofileconfiguration | A Cloud Update profile's configuration changed. This change includes updates to the profile's state, set deadline, Update Validation enablement, and configured waves and wave delay. |
| Tenant configuration updated | updatedtenantconfiguration | The Cloud Update's organization-wide configuration changed. This change includes updates to exclusions, exclusion windows, and generating a new Tenant Association Key (TAK). |

## Microsoft 365 Backup activities

The following table lists the activities in Microsoft 365 Backup that the Microsoft 365 audit log records. Microsoft 365 Backup is designed to ensure your organization's data is always protected and easily recoverable. For more information about Microsoft 365 Backup, see [Overview of Microsoft 365 Backup](/en-us/microsoft-365/backup/backup-overview?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Activated a Backup Policy | BackupPolicyActivated | A Microsoft 365 Backup policy is activated from an inactive state. |
| Activated Draft Restore Task | RestoreTaskActivated | A draft restore task for Microsoft 365 Backup is activated. This is a long running operation. |
| Backup Item Created | BackupItemAdded | One or more backup items are added to a Microsoft 365 Backup policy. |
| Backup Item Removed | BackupItemRemoved | One or more backup items are removed from a Microsoft 365 Backup policy. |
| Browsed Site for Restore | SiteBrowsedForRestore | A site was browsed in Microsoft 365 Backup to identify and select items for granular restore. |
| Cancel Offboard Backup Item | CancelOffboardBackupItem | Offboarding canceled for a backup item. |
| Completed Granular Restore for Backup Item | BackupItemGranularRestoreCompleted | A granular restore for one or more backup items is completed in Microsoft 365 Backup. |
| Completed Granular Restore Session | GranularRestoreSessionCompleted | A granular restore session is completed in Microsoft 365 Backup. |
| Completed Restore Task | RestoreTaskCompleted | A restore task is completed in Microsoft 365 Backup. |
| Created Draft Restore Task | DraftRestoreTaskCreated | A restore task is created in Microsoft 365 Backup. By default, the restore task is created as draft. |
| Created Granular Browse Session | GranularBrowseSessionCreated | A granular browse session is created in Microsoft 365 Backup to enable browsing of backed-up content for item-level restore. |
| Created Granular Restore Session | GranularRestoreSessionCreated | A granular restore session is created in Microsoft 365 Backup. |
| Created new Backup policy | NewBackupPolicyCreated | A new Microsoft 365 Backup policy was created by a Global Admin. By default, a backup policy is created in an inactive state. |
| Deleted a Backup Policy | BackupPolicyDeleted | A Microsoft 365 Backup policy is deleted. |
| Deleted Draft Restore Task | DraftRestoreTaskDeleted | A draft restore task is deleted in Microsoft 365 Backup. |
| Edited a Backup Policy | BackupPolicyEdited | A Microsoft 365 Backup policy was updated. You can update a backup policy by performing any of the following actions: 1. Renaming the policy.2. Add one or more protection units.3. Removing one or more protection units. |
| Edited Draft Restore Task | DraftRestoreTaskEdited | A draft restore task is edited in Microsoft 365 Backup. |
| Offboard Backup Item | OffboardBackupItem | Backup item is offboarding. |
| Paused a Backup Policy | BackupPolicyPaused | A Microsoft 365 Backup policy is paused from active state. |
| Programmatically got Backup Item | GetBackupItem | User requests the protection unit backed up using Microsoft 365 Backup programmatically. |
| Programmatically got Details of Backup Policy | ViewBackupPolicyDetails | Details of a Microsoft 365 Backup policy are accessed programmatically. |
| Programmatically got Details of Restore Task | GetRestoreTaskDetails | A user requests details of restore task by its identifier in Microsoft 365 Backup. |
| Programmatically got list of all Backup Policies | ListAllBackupPolicies | A user programmatically gets the list of all backup policies backed up using Microsoft 365 Backup. |
| Programmatically got list of Backup Items in Backup Policies | ListAllBackupItemsInPolicies | A list of all protection units present in a backup policy in Microsoft 365 Backup is requested programmatically. |
| Programmatically got list of Backup Items in Tenant | ListAllBackupItemsInTenant | A user programmatically gets list of all protection units in the organization backed up using Microsoft 365 Backup. |
| Programmatically got list of Backup Items in Workload | ListAllBackupItemsInWorkload | A user programmatically gets list of all protection units in workload (SharePoint, OneDrive, or Exchange) backed up using Microsoft 365 Backup. |
| Programmatically got list of Restore Items in Restore Task | GetAllRestoreArtifactsInTask | A user programmatically gets all artifacts in a restore task in Microsoft 365 Backup. |
| Programmatically got list of Restore Points | ListAllRestorePoints | A user programmatically gets all restore points in Microsoft 365 Backup. Restore Points represent the timestamp when an artifact is protected (per Protection Policy). Only Global Admins have access. |
| Programmatically got list of Restore Tasks | ListAllRestoreTasks | A user programmatically gets the list of existing restore sessions in Microsoft 365 Backup. This list includes the restore session created for every service type enrolled in the organization. |
| Restore item restoration complete | BackupItemRestoreCompleted | The restoration of an item backed up by Microsoft 365 Backup is completed. |
| Restore item restoration triggered | BackupItemRestoreTriggered | Restore is triggered for an item backed up with Microsoft 365 Backup. |
| Triggered Granular Restore for Backup Item | BackupItemGranularRestoreTriggered | A granular restore is triggered for a backup item in a granular restore session in Microsoft 365 Backup. |
| Triggered Granular Restore Session | GranularRestoreSessionTriggered | A granular restore session is triggered in Microsoft 365 Backup. This is a long running operation. |

## Microsoft 365 Copilot admin activities

The following table lists admin activities related to Microsoft 365 Copilot and Microsoft 365 Copilot Chat that the Microsoft 365 audit log records. You can access Copilot across Microsoft services. The audit log records activities that show how and when users interact with Copilot. This information includes the Microsoft service where the activity took place and references to the files accessed during the interaction.

To access the text from the user's prompt during the interaction, see [Content Search](ediscovery-content-search-overview) or view the [**AI interaction**](dspm-for-ai-considerations#activity-explorer-events) event from the activity explorer in Data Security Posture Management for AI.

For more information about auditing and other compliance management options for Microsoft 365 Copilot, see [Use Microsoft Purview to manage data security & compliance for Microsoft 365 Copilot & Microsoft 365 Copilot Chat](ai-m365-copilot).

For more information about events related to user interactions with AI, see [Audit logs for Copilot and AI activities](audit-copilot).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Created a new Copilot plugin | CreatePlugin | A user (or admin or system on behalf of a user) created a new Copilot plugin. |
| Created a new Copilot promptbook | CreatePromptBook | A user (or admin or system on behalf of a user) created a new promptbook in Copilot. |
| Deleted a Copilot plugin | DeletePlugin | A user (or admin or system on behalf of a user) deleted a Copilot plugin. |
| Deleted a Copilot promptbook | DeletePromptBook | A user (or admin or system on behalf of a user) deleted a Copilot promptbook. |
| Disabled a Copilot plugin | DisableCopilotPlugin | A user (or admin or system on behalf of a user) disabled a Copilot plugin. |
| Disabled a Copilot promptbook | DisablePromptBook | A user (or admin or system on behalf of a user) disabled a Copilot promptbook. |
| Enabled a Copilot plugin | EnablePlugin | A user (or admin or system on behalf of a user) enabled a Copilot plugin. |
| Enabled a Copilot promptbook | EnablePromptBook | A user (or admin or system on behalf of a user) enabled a Copilot promptbook. |
| Exported AI Interactions | AIEnterpriseInteractionsExported | An admin exported interactions with Copilot. |
| Interacted with Copilot | CopilotInteraction | A user (or admin or system on behalf of a user) entered prompts in Copilot. |
| Sent change notification for AI interaction creation | AIInteractionCreatedNotification | A change notification was sent to notify a subscribed listener application of a new Copilot AI interaction. |
| Sent change notification for AI interaction deletion | AIInteractionDeletedNotification | A change notification was sent to notify a subscribed listener application of a deleted Copilot AI interaction. |
| Sent change notification for AI interaction update | AIInteractionUpdatedNotification | A change notification was sent to notify a subscribed listener application of an updated Copilot AI interaction. |
| Subscribed to AI interactions | SubscribedToAIInteractions | A subscription was created by a listener application to receive change notifications for Copilot AI interactions. |
| Updated a Copilot plugin setting | UpdatePlugin | A user (or admin or system on behalf of a user) updated a Copilot plugin setting. |
| Updated a Copilot promptbook setting | UpdatePromptBook | A user (or admin or system on behalf of a user) updated a Copilot promptbook setting. |
| Updated a Copilot setting | UpdateTenantSettings | An admin (or system on behalf of an admin) updated a Copilot setting. |

## Microsoft 365 Copilot scheduled prompts activities

By using Copilot Scheduled Prompts, users can automate Copilot prompts to run on a defined schedule in Microsoft 365 Copilot chat. The following table lists the activities recorded in the Microsoft 365 audit log. Admins can manage this feature in your organization. For more information, see [Manage scheduled prompts for Microsoft 365 Copilot](/en-us/microsoft-365-copilot/scheduled-prompts?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Created a scheduled prompt | ScheduledPromptCreated | A user scheduled a Copilot prompt from Microsoft 365 Copilot Chat (Office.com chat). |
| Deleted a scheduled prompt | ScheduledPromptDeleted | A user deletes a scheduled prompt from the management window. The prompt is removed from the list and no longer runs. |
| Executed a scheduled prompt | ScheduledPromptExecute | Logged at the start of each scheduled run. It doesn't confirm the prompt was completed. |

## Microsoft Defender for Cloud activities

The following table lists Microsoft Defender for Cloud activities that are logged in the Microsoft 365 audit log. For more information, see [What is Microsoft Defender for Cloud?](/en-us/azure/defender-for-cloud/defender-for-cloud-introduction).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Connector created | ConnectorCreated | A user created a cloud environment connector for AWS, Azure, Google Cloud Platform (GCP), GitHub, JFrog, or Azure DevOps. |
| Connector deleted | ConnectorDeleted | A user deleted a cloud environment connector. |
| Connector modified | ConnectorModified | A user updated the configuration of an existing cloud environment connector. |
| Enablement rule collection created | EnablementRuleCollectionCreated | A user created an enablement rule collection to configure Defender plans and extensions for an environment. |
| Enablement rule collection deleted | EnablementRuleCollectionDeleted | A user deleted an enablement rule collection. |
| Enablement rule collection modified | EnablementRuleCollectionModified | A user modified an enablement rule collection to change Defender plan or extension settings. |
| Global setting modified | GlobalSettingModified | A user modified a global setting. |
| Rule collection created | RuleCollectionCreated | A user created a rule collection. |
| Rule collection deleted | RuleCollectionDeleted | A user deleted a rule collection and its associated rules. |
| Rule collection disabled | RuleCollectionDisabled | A user disabled an active rule collection without deleting it. |
| Rule collection enabled | RuleCollectionEnabled | A user enabled a previously disabled rule collection. |
| Rule collection modified | RuleCollectionModified | A user modified a rule collection. |
| Rule created | RuleCreated | A user created a rule. |
| Rule deleted | RuleDeleted | A user deleted a rule. |

## Microsoft Defender for Endpoint general settings activities

The following table lists the activities for Microsoft Defender for Endpoint general settings recorded in the Microsoft 365 audit log. For more information about the settings Microsoft Defender for Endpoint, see [Configure general Defender for Endpoint settings](/en-us/defender-endpoint/preferences-setup).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Changed data retention | ChangeDataRetention | Edited the data retention settings for Defender for Endpoint. |
| Downloaded offboarding package | DownloadOffboardingPkg | Downloaded the package used to remove devices from Defender for Endpoint. |
| Downloaded onboarding package | DownloadOnboardingPkg | Downloaded the package used to onboard devices to Defender for Endpoint. |
| Set advanced features | SetAdvancedFeatures | Changed advanced features in Defender for Endpoint, enabling more precise controls during an incident. Only settings for advanced features that are generally available are logged in the Microsoft 365 audit log. |

## Microsoft Defender for Endpoint indicator settings activities

The following table lists the activities for Microsoft Defender for Endpoint indicator settings that the Microsoft 365 audit log records. For more information about Microsoft Defender for Endpoint indicators, see [Manage indicators](/en-us/defender-endpoint/manage-indicators).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Added indicator | AddIndicator | Created a new indicator of compromise used to track attacks and events. |
| Deleted indicator | DeleteIndicator | Removed an indicator of compromise. |
| Edited indicator | EditIndicator | Edited an indicator of compromise. |

## Microsoft Defender for Endpoint response actions activities

The following table lists the activities for Microsoft Defender for Endpoint response actions, including Live response, that the Microsoft 365 audit log records. For more information about Microsoft Defender for Endpoint response actions, see [Take response actions on a device](/en-us/defender-endpoint/respond-machine-alerts).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Collected investigation package | CollectInvestigationPackage | Collected information about a device that's used to understand attack tools and techniques. |
| Collected Logs | LogsCollection | Collected log information about Defender for Endpoint. |
| Downloaded file | DownloadFile | Downloaded a suspicious file for further investigation. |
| Isolated device | IsolateDevice | Isolated a device from the network, helping prevent attacks from spreading. |
| Offboarded device | DeviceOffBoarding | Removed a device from Defender for Endpoint. |
| Ran Antivirus scan | RunAntiVirusScan | Ran Microsoft Defender Antivirus scan on a device. |
| Ran get Live response file link | LiveResponseGetFile | Opened a Live response session, opening a remote shell into a device. |
| Ran Live response API | RunLiveResponseApi | Opened a Live response session via an API call, opening a remote shell into a device. |
| Ran Live response session | RunLiveResponseSession | Ran a Live response session, opening a remote shell into a device. |
| Released from isolation | ReleaseFromIsolation | Added an isolated device back onto the network. |
| Removed app restrictions | RemoveAppRestrictions | Allow an app to run. |
| Restricted app execution | RestrictAppExecution | Prevent a malicious app from running. |
| Stopped and quarantined file | StopAndQuarantineFile | Quarantined a suspicious file for further analysis. |

## Microsoft Defender for Endpoint roles settings activities

The following table lists the activities for Microsoft Defender for Endpoint role settings that the Microsoft 365 audit log records. For more information about roles in Microsoft Defender for Endpoint, see [Create and manage roles for role-based access control](/en-us/defender-endpoint/user-roles).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Added role | AddRole | Added new security role and permissions. |
| Deleted role | DeleteRole | Removed security roles and permissions. |
| Edited role | EditRole | Edited security roles and permissions. |

## Microsoft Defender for Experts activities

The following table lists the activities in Microsoft Defender Experts that the Microsoft 365 audit log records. For more information about Microsoft Defender Experts, see [Learn about Microsoft Defender Experts for XDR](/en-us/defender-xdr/dex-xdr-overview?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) and [Learn about Microsoft Defender Experts for Hunting](/en-us/microsoft-365/security/defender/defender-experts-for-hunting?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Defender Experts analyst permission created | DefenderExpertsAnalystPermissionCreated | An administrator granted one or more role permissions to Defender Experts analysts to investigate incidents or remediate threats. |
| Defender Experts analyst permission modified | DefenderExpertsAnalystPermissionModified | An administrator modified role permissions for Defender Experts analysts to investigate incidents or remediate threats. |

## Microsoft Defender for Identity activities

The following table lists the activities for Microsoft Defender for Identity that the Microsoft 365 audit log records.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Added alert notification recipient | AlertNotificationsRecipientAdded | A recipient was added to the security alerts notification configuration. |
| Added exclusions configuration | ExclusionConfigurationAdded | A global exclusion was added for an alert or for an entity. |
| Added health issues notification recipient | MonitoringAlertNotificationRecipientAdded | A recipient was added to the health issues notification configuration. |
| Added remediation action | RemediationActionAdded | A remediation action was added to the queue. |
| Added sensor | SensorCreated | A new sensor was added. |
| Created workspace | WorkspaceCreated | The workspace was created. |
| Deleted alert notification recipient | AlertNotificationsRecipientDeleted | A recipient was removed from the security alerts notification configuration. |
| Deleted exclusions configuration | ExclusionConfigurationDeleted | A global exclusion was deleted for an alert or for an entity. |
| Deleted health issues notification recipient | MonitoringAlertNotificationRecipientDeleted | A recipient was removed from the heath issues notification configuration. |
| Deleted workspace | WorkspaceDeleted | The workspace was deleted. |
| Downloaded Domain Controller coverage Excel | DomainControllerCoverageExcelDownloaded | The Domain Controller coverage Excel file was downloaded. |
| Downloaded report | ReportDownloaded | A report was downloaded. |
| Downloaded security alert Excel | AlertExcelDownloaded | The detailed Excel file of an alert was downloaded. |
| Regenerated sensor deployment key | SensorDeploymentAccessKeyUpdated | The sensors access key was regenerated. |
| Removed sensor | SensorDeleted | A sensor was deleted. |
| Retrieved sensor deployment key | SensorDeploymentAccessKeyReceived | The sensors access key was retrieved. |
| Updated alert threshold configuration | WorkspaceAlertThresholdLevelUpdated | The alerts thresholds configuration was updated. |
| Updated directory services account configuration | DirectoryServicesAccountConfigurationUpdated | The Directory services accounts set was modified. |
| Updated entity remediation configuration | EntityRemediatorConfigurationUpdated | The Manage action accounts mode was modified. |
| Updated entity tags | TaggingConfigurationUpdated | A tag was added or removed from an entity. |
| Updated exclusions configuration | ExclusionConfigurationUpdated | A global exclusion was updated for an alert or for an entity. |
| Updated health issue | MonitoringAlertUpdated | A health issue was modified. |
| Updated remediation action | RemediationActionUpdated | A remediation action was completed. |
| Updated remediation action configuration | RemediationActionConfigurationUpdated | The Manage action accounts set was modified. |
| Updated reporter configuration | ReporterConfigurationUpdated | A report's scheduling was modified. |
| Updated security notification configuration | NotificationConfigurationUpdated | The security alerts or health issues notifications configuration was modified. |
| Updated sensor configuration | SensorConfigurationUpdated | A sensor's configuration was updated. |
| Updated sensors activation mode | SensorActivationMethodConfigurationUpdated | The sensors activation mode was modified. |
| Updated syslog forwarding configuration | SyslogServiceConfigurationUpdated | The syslog forwarding configuration was modified. |
| Updated Unified RBAC configuration | URbacAuthorizationStatusChanged | The Unified Role Based Access Control configuration was modified. |
| Updated VPN configuration | VpnConfigurationUpdated | The VPN (radius accounting) configuration was modified. |

## Microsoft Defender for Office 365 activities

The following table lists the activities for Microsoft Defender for Office 365 logged in the Microsoft 365 audit log. For more information about Microsoft Defender for Office 365, see [Microsoft Defender for Office 365 overview](/en-us/defender-office-365/mdo-about?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

Note

These events aren't listed as friendly names in audit search. This table is a complementary resource for the [Office 365 Management Activity API schema](/en-us/office/office-365-management-api/office-365-management-activity-api-schema).

| Events | Operation | Description |
| --- | --- | --- |
| Alert events | SecurityComplianceAlerts | Security and compliance alert signals for alerts generated based on Alert policies in the Microsoft Purview compliance portal. |
| Attack Simulation admin events | AttackSimAdmin | Events related to admin activities in Attack Simulation & Training in Microsoft Defender for Office 365. |
| Attack Simulation training events | UserTraining | Events related to user training in Attack Simulation & Training in Microsoft Defender for Office 365. |
| Attack Simulation user events | AttackSim | Events related to user activities in Attack Simulation & Training in Microsoft Defender for Office 365. |
| Automated incident response (AIR) events | AirInvestigation | Automated incident response (AIR) events and data. |
| Campaign events | Campaign | Email campaign events from Microsoft Defender for Office 365. |
| Content detection events | ThreatIntelligenceAtpContent | Phishing and malware events for files in SharePoint, OneDrive for Business, and Microsoft Teams from Microsoft Defender for Office 365. |
| Outbound spam events | HygieneEvent | Events related to outbound spam protection. |
| Phishing and malware events | ThreatIntelligence | Phishing and malware events from the built-in security add-on for on-premises mailboxes (formerly Exchange Online Protection) and Microsoft Defender for Office 365. |
| Quarantine events | Quarantine | Quarantine events from Microsoft Defender for Office 365. |
| Submission events | MailSubmission | Admin and user submission events from the built-in security add-on for on-premises mailboxes (formerly Exchange Online Protection) and Microsoft Defender for Office 365. |
| URL Click Events | ThreatIntelligenceUrl | Safe links time-of-block and block override events from Microsoft Defender for Office 365. |

## Microsoft Defender XDR automation activities

The following table lists automation activities for Microsoft Defender XDR recorded in the Microsoft 365 audit log. For more information, see [Search the audit log for events in Microsoft Defender XDR](/en-us/defender-xdr/microsoft-xdr-auditing).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Created a generated playbook | GeneratedPlaybookCreated | A user created a generated playbook. |
| Created an automation rule | AutomationRuleCreated | A user created an automation rule. |
| Deactivated a generated playbook | GeneratedPlaybookInactive | A user deactivated a generated playbook. |
| Deactivated an automation rule | AutomationRuleInactive | A user deactivated an automation rule. |
| Edited a generated playbook | GeneratedPlaybookEdited | A user edited a generated playbook. |
| Edited an automation rule | AutomationRuleEdited | A user edited an automation rule. |
| Activated a generated playbook | GeneratedPlaybookActivated | A user activated a generated playbook. |
| Activated an automation rule | AutomationRuleActivated | A user activated an automation rule. |
| Removed a generated playbook | GeneratedPlaybookRemoved | A user removed a generated playbook. |
| Removed an automation rule | AutomationRuleRemoved | A user removed an automation rule. |
| Triggered a generated playbook | TriggerGeneratedPlaybook | A user manually triggered a generated playbook. |

## Microsoft Defender XDR case management activities

The following table lists the case management activities that are logged in the Microsoft 365 audit log when users create and manage cases in the Microsoft Defender portal. For more information, see [Microsoft Defender XDR](/en-us/defender-xdr/?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

| Friendly name | Operation | Description |
| --- | --- | --- |
| A case was assigned to a different user or team member | ChangedCaseAssignment | Generated when a case is assigned or reassigned to a different user. |
| A comment in a case was edited | UpdatedCommentInCase | Generated when an existing comment on a case is edited. |
| A comment was added to a case | AddedCommentToCase | Generated when a comment is added to a case. |
| A comment was deleted from a case | DeletedCommentFromCase | Generated when a comment is deleted from a case. |
| A new case was created in the system | CreatedCase | Generated when a user creates a new case. Not logged for cases created by application or service accounts. |
| An existing case was deleted from the system | DeletedCase | Generated when a case is deleted. |
| An object was linked to a case | LinkedObject | Generated when an object, such as an alert or entity, is linked to a case. |
| An object was unlinked from a case | UnlinkedObject | Generated when an object is unlinked from a case. |
| Case content was changed | UpdatedCase | Generated when a case is updated with changes, such as custom fields, that aren't captured by a more specific operation. |
| One or more tags were added to a case | AddedTagsToCase | Generated when one or more tags are added to a case. |
| One or more tags were removed from a case | RemovedTagsFromCase | Generated when one or more tags are removed from a case. |
| The classification of a case was changed | ChangedCaseClassification | Generated when the classification of a case is changed. |
| The closing notes of a case were modified or updated | ChangedCaseClosingNotes | Generated when the closing notes of a case are changed. |
| The description of a case was modified or updated | ChangedCaseDescription | Generated when the description of a case is changed. |
| The name or title of a case was changed | ChangedCaseName | Generated when the name (title) of a case is changed. |
| The priority level of a case was modified | ChangedCasePriority | Generated when the priority of a case is changed. |
| The severity of a case was changed | ChangedCaseSeverity | Generated when the severity of a case is changed. |
| The status of a case was updated | ChangedCaseStatus | Generated when the status of a case is changed. |

## Microsoft Defender XDR custom detection activities

The following table lists the custom detection activities for Microsoft Defender XDR recorded in the Microsoft 365 audit log. For more information about Microsoft Defender XDR custom detections, see [Create and manage custom detections rules](/en-us/microsoft-365/security/defender/custom-detection-rules?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Changed custom detection rule status | ChangeCustomDetectionRuleStatus | A custom detection rule was turned off or on. |
| Created custom detection rule | CreateCustomDetection | A new custom detection rule was created. |
| Deleted custom detection rule | DeleteCustomDetection | A custom detection rule was removed. |
| Edited custom detection rule | EditCustomDetection | A custom detection rule was modified. |
| Ran custom detection rule | RunCustomDetection | A custom detection rule was manually run. |

## Microsoft Defender XDR incident activities

The following table lists the incident activities for Microsoft Defender XDR recorded in the Microsoft 365 audit log. For more information about incidents in Microsoft Defender XDR, see [Incidents overview](/en-us/defender-xdr/incidents-overview?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Added comment to incident | AddCommentToIncident. | Added comment to incident. |
| Added tags to incident | AddTagsToIncident | Added tags to incident. |
| Assigned user to incident | AssignUserToIncident | Assigned user to incident. |
| Edit incident classification | EditIncidentClassification | Edit incident classification. |
| Removed tags from incident | RemoveTagsFromIncident | Removed tags from the incident. |
| Unassigned user to incident | UnAssignUserFromIncident | Unassigned user to incident. |
| Updated incidents status | UpdateIncidentStatus | Updated incidents status. |

## Microsoft Defender XDR suppression rule activities

The following table lists the activities for suppression rules for Microsoft Defender XDR recorded in the Microsoft 365 audit log. For more information about suppression rules in Microsoft Defender XDR, see [Manage suppression rules](/en-us/defender-endpoint/manage-suppression-rules).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Created suppression rule | CreateSuppressionRule | Created alert suppression rule. |
| Deleted suppression rule | DeleteSuppressionRule | Deleted alert suppression rule. |
| Disabled suppression rule | DisableSuppressionRule | Disabled alert suppression rule. |
| Edited suppression rule | EditSuppressionRule | Deleted alert suppression rule. |
| Enabled suppression rule | EnableSuppressionRule | Enabled alert suppression rule. |

## Microsoft Edge WebContentFiltering activities

The following table lists the browsing activities in Microsoft Edge recorded in the Microsoft 365 audit log for the WebContentFiltering feature. The table includes the friendly name that displays in the **Activities** column and the name of the corresponding operation that appears in the detailed information of an audit record and in the .csv file when you export the search results.

[Search the audit log](audit-search) describes how you can search the audit logs from the Microsoft Purview portal. Users need to be a global admin or have audit read permissions to access audit logs. Use the **Activities** filter to search for specific activities. To list all WebContentFiltering activities, select *WebContentFiltering* in the **Record type** filter. Use the date range boxes and the **Users** list to scope the search results further if needed.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Allowed URL Navigation in Microsoft Edge | URLNavigationAllowed | User browsed a URL. |
| Blocked URL Navigation in Microsoft Edge | URLNavigationBlocked | Browsed URL is blocked by WebContentFiltering policy. |

## Microsoft Entra group administration activities

The following table lists group administration activities that the Microsoft 365 audit log records when an admin or a user creates or changes a Microsoft 365 group or when an admin creates a security group by using the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339) or the Azure management portal. For more information about groups in Microsoft 365, see [View, create, and delete Groups in the Microsoft 365 admin center](/en-us/microsoft-365/admin/create-groups/create-groups?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Added group | AddGroup | A group was created. |
| Added member to group | AddMemberToGroup. | A member was added to a group. |
| Deleted group | Delete group. | A group was deleted. |
| Removed member from group | RemoveMemberFromGroup. | A member was removed from a group. |
| Updated group | UpdateGroup. | A property of a group was changed. |

## Microsoft Entra risk detection activities

The following table lists risk detection activities recorded in the Microsoft 365 audit log when using Microsoft Entra ID Protection. For more information about risk detection, see [Learn about risk detections.](/en-us/entra/id-protection/concept-identity-protection-risks).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Compromised sign-in detection | CompromisedSignIn | Sign-in risk detections represent the probability that a given authentication request isn't the authorized owner of the account. |
| Compromised user detection | CompromisedUser | User risk detections might flag a legitimate user account as at risk, when a potential threat actor gains access to an account by compromising their credentials or when they detect some type of anomalous user activity. |

## Microsoft Graph Data Connect

The following table lists the user and admin activities in [Microsoft Graph Data Connect](/en-us/graph/data-connect-concept-overview) recorded in the Microsoft 365 audit log. The table includes the friendly name that displays in the **Activities** column and the name of the corresponding operation that appears in the detailed information of an audit record and in the CSV file when you export the search results.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Approved or denied an app | ConsentModificationRequest | A user performed a consent modification request. |
| Extraction ran | DataAccessRequestOperation | A user performed an extraction. Partner datasets and ISV runs are excluded. |

## Microsoft Places Directory activities

The following table lists the admin activities in [Microsoft Places Directory](/en-us/microsoft-365/places/places-overview?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json) that the Microsoft 365 audit log records. The table includes the friendly name that displays in the **Activities** column and the name of the corresponding operation that appears in the detailed information of an audit record and in the CSV file when you export the search results.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Created a place | CreatedPlace | An admin performed an operation for creating places. |
| Deleted a place | DeletedPlace | An admin performed an operation for deleting places. |
| Updated a place | UpdatedPlace | An admin performed an operation for updating places. |

## Microsoft Purview Audit solution activities

The following table lists activities associated with audit solutions in the Microsoft Purview portal and the [Audit Search Graph API](/en-us/graph/api/resources/security-auditlogquery). The *SecurityComplianceCenter* workload audits these activities. For more information, see [Search the audit log](audit-search).

Audit search and export activities that use [Search-UnifiedAuditLog](/en-us/powershell/module/exchange/search-unifiedauditlog) aren't audited.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Audit search canceled | AuditSearchCancelled | An audit search job was canceled. |
| Audit search completed | AuditSearchCompleted | An audit search job was completed. |
| Audit search created | AuditSearchCreated | A new audit search request was submitted. |
| Audit search deleted | AuditSearchDeleted | An audit search job was deleted. |
| Audit search export job completed | AuditSearchExportJobCompleted | The export job to export the search results of an audit search query was completed. |
| Audit search export job created | AuditSearchExportJobCreated | An export job was created to export the search results of an audit search query. |
| Audit search export results downloaded | AuditSearchExportResultsDownloaded | The search results from an audit search query were downloaded. |

## Microsoft Purview governance activities

The following table lists Microsoft Purview governance activities recorded in the Microsoft 365 audit log. For more information, see [Microsoft Purview governance solutions](data-governance-overview).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Asset or entity created | EntityCreated | A new asset or entity was created or added to an existing asset. |
| Classification added | ClassificationAdded | Added classifications to asset entity. |
| Classification definition created | ClassificationDefinitionCreated | Created a classification type. |
| Classification definition deleted | ClassificationDefinitionDeleted | Deleted a classification type. |
| Classification definition updated | ClassificationDefinitionUpdated | Updated a classification type. |
| Classification deleted | ClassificationDeleted | Deleted classifications from asset entity. |
| Classification updated | ClassificationUpdated | Updated classifications on asset entity. |
| Entity deleted | EntityDeleted | An asset or entity was deleted from an existing asset. |
| Entity updated | EntityUpdated | **Includes**: attribute update, business attribute update, collection info (only include collection ID), contacts update, customAttributes, hierarchy, homeId, labels, sourceDetails. |
| Glossary term assigned | GlossaryTermAssigned | Assigned terms to asset entity. |
| Glossary term created | GlossaryTermCreated | Created a term. |
| Glossary term deleted | GlossaryTermDeleted | Deleted a term. |
| Glossary term disassociated | GlossaryTermDisassociated | Disassociated terms from asset entity. |
| Glossary term updated | GlossaryTermUpdated | Updated a term. |
| Sensitivity label changed | SensitivityLabelChanged | Sensitivity label was added, updated, or deleted. |

## Microsoft Purview on-demand classification activities

The following table lists the activities from Microsoft Purview on-demand classification that the Microsoft 365 audit log records. For more information about on-demand classification, see [Learn about on-demand classification in Microsoft Purview](on-demand-classification).

Note

These audit activities are only available in Audit (Premium). You must be assigned the appropriate license before these activities are logged in the audit log. For more information, see [Audit (Premium)](audit-solutions-overview#audit-premium). For Audit (Premium) licensing requirements, see [Auditing solutions in Microsoft 365](audit-solutions-overview#licensing-requirements).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Classified file as part of an on-demand classification scan | DataScanClassification | File was evaluated for sensitive content as part of an on-demand classification scan for SharePoint or OneDrive. |
| Classified file on device as part of an on-demand classification scan | SensitiveInfoDiscovered | File was evaluated for sensitive content as part of an on-demand classification scan for Endpoint devices. |
| Declassified file as part of an on-demand classification scan | DataScanDeClassification | File no longer matches the sensitive information types defined in the corresponding On-demand classification scan triggered for SharePoint or OneDrive locations. |

## Microsoft Purview permission activities

The following table lists Microsoft Purview administration activities that the Microsoft 365 audit log records when an administrator manages role-based access control (RBAC) role groups and user assignments. For more information, see [Permissions in the Microsoft Purview portal](purview-permissions). See [Office 365 Management Activity API schema](/en-us/office/office-365-management-api/office-365-management-activity-api-schema#security-and-compliance-rbac-schema) for the audit log schema.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Create RBAC role group definition | CreateRBACRoleGroupDefinition | An RBAC role group definition is created. |
| Delete RBAC role group definition | DeleteRBACRoleGroupDefinition | An RBAC role group definition is deleted. |
| Update RBAC role group definition | UpdateRBACRoleGroupDefinition | An RBAC role group definition is updated. |
| Add user assignments to role group | GrantPermissionsAsync | User assignments to an RBAC role group are added. |
| Remove user assignments to role group | DeletePermissionAsync | User assignments to an RBAC role group are removed. |
| Updated user role assignments expiration in role group | UpdatePermission | A user assignment expiration date is updated in an RBAC role group. |

## Microsoft Security Copilot agent management

The following table lists the Agent management operations in Security Copilot that the Microsoft 365 audit log records. These activities characterize activities for agents and the components necessary for them to function such as triggers. For more information about Security Copilot agent management, see [Microsoft Security Copilot agents overview](/en-us/copilot/security/agents-overview).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Created a new Security Copilot agent | CreateCopilotAgent | A user (or admin or system on behalf of a user) created a new Security Copilot agent. |
| Created a new Security Copilot agent trigger | CreateCopilotforSecurityAgentTrigger | A user (or admin or system on behalf of a user) created a new promptbook in Copilot. |
| Deleted a Security Copilot agent | DeleteCopilotAgent | A user (or admin or system on behalf of a user) deleted a Security Copilot agent. |
| Deleted a Security Copilot agent trigger | DeleteCopilotForSecurityAgentTrigger | A user (or admin or system on behalf of a user) deleted a Security Copilot trigger. |
| Updated a Security Copilot agent setting | UpdateCopilotAgent | A user (or admin or system on behalf of a user) updated a Security Copilot agent setting. |
| Updated a Security Copilot agent trigger | UpdateCopilotforSecurityAgentTrigger | A user (or admin or system on behalf of a user) updated a Security Copilot agent trigger setting. |

## Microsoft Security Copilot interactions

The following table lists the types of user interactions with AI components in Security Copilot that the Microsoft 365 audit log records. These operations represent individual prompting, embedded experiences, or agentic workflows. For more information about Security Copilot interactions, see [Prompting in Security Copilot](/en-us/copilot/security/prompting-security-copilot) and [Microsoft Security Copilot agents overview](/en-us/copilot/security/agents-overview).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Interacted with Copilot | CopilotInteraction | A user (or admin or system on behalf of a user) entered prompts in Copilot or an agent. |

## Microsoft Security Copilot platform management

The following table lists management operations of a Security Copilot and its components that the Microsoft 365 audit log records. These operations represent tenant or workspace settings or AI components such as plugins and promptbooks. For more information about the management elements of Security Copilot, see [What is Microsoft Security Copilot](/en-us/copilot/security/microsoft-security-copilot).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Created a new Copilot plugin | CreatePlugin | A user (or admin or system on behalf of a user) created a new Copilot plugin. |
| Created a new Copilot promptbook | CreatePromptBook | A user (or admin or system on behalf of a user) created a new promptbook in Copilot. |
| Deleted a Copilot plugin | DeletePlugin | A user (or admin or system on behalf of a user) deleted a Copilot plugin. |
| Deleted a Copilot promptbook | DeletePromptBook | A user (or admin or system on behalf of a user) deleted a Copilot promptbook. |
| Disabled a Copilot plugin | DisableCopilotPlugin | A user (or admin or system on behalf of a user) disabled a Copilot plugin. |
| Disabled a Copilot promptbook | DisablePromptBook | A user (or admin or system on behalf of a user) disabled a Copilot promptbook. |
| Enabled a Copilot plugin | EnablePlugin | A user (or admin or system on behalf of a user) enabled a Copilot plugin. |
| Enabled a Copilot promptbook | EnablePromptBook | A user (or admin or system on behalf of a user) enabled a Copilot promptbook. |
| Updated a Copilot plugin setting | UpdatePlugin | A user (or admin or system on behalf of a user) updated a Copilot plugin setting. |
| Updated a Copilot promptbook setting | UpdatePromptBook | A user (or admin or system on behalf of a user) updated a Copilot promptbook setting. |
| Updated a Copilot setting | UpdateTenantSettings | An admin (or system on behalf of an admin) updated a Copilot setting. |

## Microsoft Sentinel AI tool activities

The following table lists the AI tool related activities in Microsoft Sentinel data lake recorded in the Microsoft 365 audit log. For more information about MCP tools in Microsoft Sentinel data lake, see [Tool collection in Microsoft Sentinel MCP server](/en-us/azure/sentinel/datalake/sentinel-mcp-tools-overview).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Completed AI tool run | SentinelAIToolRunCompleted | Microsoft Sentinel AI tool run completed. |
| Created AI tool | SentinelAIToolCreated | User creates a Microsoft Sentinel AI tool. |
| Started AI tool run | SentinelAIToolRunStarted | Microsoft Sentinel AI tool run started. |

## Microsoft Sentinel data lake job activities

The following table lists the job activities in Microsoft Sentinel data lake that the Microsoft 365 audit log records. For more information about jobs in Microsoft Sentinel data lake, see [Create and manage Jupyter notebook jobs (preview)](/en-us/azure/sentinel/datalake/notebook-jobs) and [Create KQL jobs in the Microsoft Sentinel data lake (preview)](/en-us/azure/sentinel/datalake/kql-jobs).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Completed a job run adhoc | JobRunAdhocCompleted | Ad hoc Job execution completed. |
| Completed a job run scheduled | JobRunScheduledCompleted | Scheduled Job execution completed. |
| Created job | JobCreated | A job is created. |
| Deleted a custom table | CustomTableDelete | As part of a job run, the custom table was deleted. |
| Deleted job | JobDeleted | A job is deleted. |
| Disabled job | JobDisabled | The job is disabled. |
| Enabled job | JobEnabled | A disabled job is reenabled. |
| Ran a job adhoc | JobRunAdhoc | Job is triggered manually and run started. |
| Ran a job on schedule | JobRunScheduled | Job run is triggered due to schedule. |
| Read from table | TableRead | As part of the job run, a table is read. |
| Stopped a job run | JobRunStopped | User manually cancels or stops an ongoing job run. |
| Updated job | JobUpdated | The job definition and/or configuration and schedule details of the job if updated. |
| Wrote to a custom table | CustomTableWrite | As part of the job run, data was written to a custom table. |

## Microsoft Sentinel data lake KQL activities

The following table lists the KQL activities in Microsoft Sentinel data lake that the Microsoft 365 audit log records. For more information about KQL in Microsoft Sentinel data lake, see [KQL and the Microsoft Sentinel data lake (preview)](/en-us/azure/sentinel/datalake/kql-overview).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Completed KQL query | KQLQueryCompleted | User runs interactive queries via KQL on data in their Microsoft Sentinel data lake. |

## Microsoft Sentinel data lake notebook activities

The following table lists the notebook activities in Microsoft Sentinel Data lake recorded in the Microsoft 365 audit log. For more information about notebooks in Microsoft Sentinel data lake, see [Use notebooks in Microsoft Sentinel data lake](/en-us/azure/sentinel/datalake/notebooks-overview).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Deleted a custom table | CustomTableDelete | User deleted a table as part of their notebook execution. |
| Read from table | TableRead | User read a table as part of their notebook execution. |
| Started session | SessionStarted | User started a notebook session. |
| Stopped session | SessionStopped | User stopped a notebook session. |
| Wrote to a custom table | CustomTableWrite | User wrote to a table as part of their notebook execution. |

## Microsoft Sentinel data lake onboarding activities

The following table lists the Microsoft Sentinel data lake onboarding activities recorded in the Microsoft 365 audit log. For more information about onboarding to Microsoft Sentinel data lake, see [Onboarding to Microsoft Sentinel data lake (preview)](/en-us/azure/sentinel/datalake/sentinel-lake-onboarding).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Changed subscription of Sentinel lake | SentinelLakeSubscriptionChanged | User modified the billing subscription ID or resource group associated with the data lake. |
| Onboarded data for Sentinel lake | SentinelLakeDefaultDataOnboarded | During onboarding, default data onboard is logged. |
| Set up Sentinel lake | SentinelLakeSetup | At the time of onboarding, Microsoft Sentinel data lake is set up and the details are logged. |

## Microsoft Sentinel graph activities

The following table lists the graph activities in Microsoft Sentinel recorded in the Microsoft 365 audit log. For more information about Microsoft Sentinel graph, see [What is Microsoft Sentinel Graph? (preview)](/en-us/azure/sentinel/datalake/sentinel-graph-overview).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Created a graph scenario | GraphScenarioCreated | User created a graph instance for a predefined graph scenario. |
| Deleted a graph scenario | GraphScenarioDeleted | User deleted or disable a graph instance for a predefined graph scenario. |
| Ran a graph query | GraphQueryRun | User ran a graph query. |

## Microsoft Sentinel data lake customer managed keys activities

The following table lists the customer-managed key (CMK) activities in Microsoft Sentinel data lake that the Microsoft 365 audit log records. For more information about CMK in Microsoft Sentinel data lake, see [Set up Microsoft Sentinel customer-managed key](/en-us/azure/sentinel/customer-managed-keys).

| Friendly name | Operation | Description |
| --- | --- | --- |
| **Disabled CMK encryption** | CMKDisabled | The customer-managed key was removed and encryption reverted to Microsoft-managed keys for the data lake. |
| **Enabled CMK encryption** | CMKEnabled | A customer-managed key was configured for the data lake successfully. |
| **Received CMK encryption request** | CMKRequestReceived | A request to enable customer-managed key encryption was received for the data lake, including the required key details. |
| **Accepted CMK encryption request** | CMKRequestAccepted | The request to enable customer-managed key encryption was accepted for the data lake. |
| **Rejected CMK encryption request** | CMKRequestRejected | A key wrap, unwrap, or validation operation failed. |
| **Rolled back CMK operation** | CMKRollbackExecuted | The customer-managed key configuration could not be completed, so the operation was rolled back for the data lake and reverted to Microsoft-managed keys. |
| **Updated CMK encryption** | CMKUpdated | The encryption key was rotated or changed for the data lake. |

## Microsoft To Do activities

The following table lists the activities in Microsoft To Do that the Microsoft 365 audit log records. For more information about Microsoft To Do, see [Support for Microsoft To Do](https://support.microsoft.com/todo).

Note

To audit events for Microsoft To Do activities, you need a paid Project Plan 1 license (or higher) in addition to the relevant Microsoft 365 license that includes entitlements to Audit (Standard).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Accepted sharing link on folder | AcceptedSharingLinkOnFolder | Accepted sharing link for a folder. |
| Attachment created | AttachmentCreated | An attachment was created for a task. |
| Attachment deleted | AttachmentDeleted | An attachment was deleted. |
| Attachment updated | AttachmentUpdated | An attachment was updated. |
| Folder sharing link shared | FolderSharingLinkShared | Created a sharing link for a folder. |
| Linked entity created | LinkedEntityCreated | A linked entity of task was created. |
| Linked entity deleted | LinkedEntityDeleted | A linked entity was deleted. |
| Linked entity updated | LinkedEntityUpdated | A linked entity was updated. |
| SubTask created | SubTaskCreated | A subtask was created. |
| SubTask deleted | SubTaskDeleted | A subtask was deleted. |
| SubTask updated | SubTaskUpdated | A subtask was updated. |
| Task created | TaskCreated | A task was created. |
| Task deleted | TaskDeleted | A task was deleted. |
| Task read | TaskRead | A task was read. |
| Task updated | TaskUpdated | A task was updated. |
| TaskList created | TaskListCreated | A task list was created. |
| TaskList read | TaskListRead | A task list was read. |
| TaskList updated | TaskListUpdated | A task list was updated. |
| User invited | UserInvited | Invited user to a folder. |

## Microsoft 365 Organizational Data Service activities

The following table lists the activities in Microsoft 365 Organizational Data Service that the Microsoft 365 audit log records. For more information about Microsoft 365 Organizational Data Service, see [Microsoft 365 Organizational Data Service](/en-us/viva/organizational-data).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Updated data sharing settings | DataSharingSettingsUpdated | Logged when a customer updates the list of apps allowed to share data, including which attributes each app can access. |
| Updated access policies | AccessPoliciesUpdated | Logged when a customer updates access policies that control access to organizational data. |
| Updated access policy associations | AccessPolicyAssociationsUpdated | Logged when a customer updates attribute or app associations to access policies that control access to organizational data. |

## People Skills activities

The following table lists the activities in People Skills (Viva) that are logged in the Microsoft 365 audit log. For more information about this feature, see **[People Skills documentation](/en-us/microsoft-365/copilot/people-skills-overview)**.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Added custom skills | CustomSkillsAdded | Generated when a tenant administrator adds custom skills to the tenant skills library. |
| Added graph skills | GraphSkillsAdded | Generated when a tenant administrator adds graph-based skills to the tenant library. |
| Added skill from inference | SkillAddedFromInference | Generated when the system adds an inferred skill to a user profile via TBA-triggered inference. |
| Added skill from learning | SkillAddedFromLearning | Generated when the system adds a skill inferred from learning activity. |
| Added user skill | UserSkillAdded | Generated when a user adds a skill to their own profile. |
| Applied external bulk tag | ExternalBulkTagApplied | Generated when a third-party application applies bulk content tags via the service-to-service (S2S) API. |
| Changed inferencing setting | InferencingToggleChanged | Generated when the E3/E5 inferencing toggle status changes. |
| Completed tenant offboarding | TenantOffboardCompleted | Generated when tenant offboarding completes and all tenant data has been deleted. |
| Deactivated tenant auto-on | TenantAutoOnDeactivated | Generated when the auto-on tenant setting is deactivated by the system. |
| Deleted custom skills | CustomSkillsDeleted | Generated when a tenant administrator deletes custom skills from the tenant library. |
| Deleted external skills | ExternalSkillsDeleted | Generated when a third-party application deletes previously ingested skills data. |
| Deleted graph skills | GraphSkillsDeleted | Generated when a tenant administrator removes graph-based skills from the tenant library. |
| Deleted tenant skills library | TenantSkillsLibraryDeleted | Generated when the tenant skills library is removed as part of offboarding. |
| Deleted user data | UserDataDeleted | Generated when user data is deleted during tenant offboarding. |
| Deleted user skill | UserSkillDeleted | Generated when a user removes a skill from their profile. |
| Exported skills | SkillsExported | Generated when a tenant administrator exports skills data from the service. |
| Ingested external skills | ExternalSkillsIngested | Generated when a third-party application ingests skills data into People Skills via the service-to-service (S2S) API. |
| Provisioned skills library | SkillsLibraryProvisioned | Generated when the skills library is auto-provisioned for a tenant. |
| Provisioned tenant | TenantProvisioned | Generated when a tenant administrator provisions the People Skills skills library for their tenant. |
| Started tenant offboarding | TenantOffboardKickoff | Generated when tenant offboarding (data deletion) is initiated by the system. |
| Updated tenant settings | TenantSettingsUpdated | Generated when a tenant administrator modifies People Skills tenant-level configuration settings. |
| Updated user skill | UserSkillUpdated | Generated when a user updates metadata on an existing skill in their profile. |
| Validated custom skills | CustomSkillsValidated | Generated when a tenant administrator validates custom skills data (marks skills as validated). |

## Personal insights activities

The following table lists the activities in personal insights recorded in the Microsoft 365 audit log. For more information about personal insights, see [Admin guide for personal insights](/en-us/viva/insights/personal/Overview/mya-for-admins).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Updated organization MyAnalytics settings | UpdatedOrganizationMyAnalyticsSettings | Admin updates organization-level settings for personal insights. |
| Updated user MyAnalytics settings | UpdatedUserMyAnalyticsSettings | Admin updates user settings for personal insights. |

## Planner activities

The following table lists the user and admin activities in Microsoft Planner that the Microsoft 365 audit log records. The table includes the friendly name that displays in the **Activities** column and the name of the corresponding operation that appears in the detailed information of an audit record and in the CSV file when you export the search results.

Note

Portfolio activity in Planner is logged with Microsoft Project for web roadmap activity. For details, see the Project for the web activities section.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Added a member to a roster | RosterMemberAdded | A member was added to a roster. If the add operation was a *ResultStatus.Failure* or *ResultStatus.AuthorizationFailure*, the *MemberIds* is a list of member IDs attempted. |
| Added a reaction to a chat message | ChatMessageReactionAdded | A reaction was added to a chat message by a user or an app. |
| Assigned a task | TaskAssigned | A task's assignee was modified by a user or an app. This might be an unassigned task getting assigned or an assigned task with a new assignee. |
| Completed a task | TaskCompleted | A task was marked completed by a user or an app. |
| Copied a plan | PlanCopied | A plan was copied by a user or an app. If the copy operation was a *ResultStatus.Failure* or *ResultStatus.Failure*, the *newPlanId* is null, the *newContainerType* is *ContainerType.Invalid*, and *newContainerId* is null. |
| Created a chat message | ChatMessageCreated | A chat message was created by a user or an app. |
| Created a goal | GoalCreated | A goal was created by a user or an app. If the create operation was a *ResultStatus.Failure* or *ResultStatus.AuthorizationFailure*, the *ObjectId* is null and *PlanId* is null. |
| Created a plan | PlanCreated | A plan was created by a user or an app. If the create operation was a *ResultStatus.Failure* or *ResultStatus.AuthorizationFailure*, the *ObjectId* is null, *ContainerType* is *ContainerType.Invalid* and *ContainerId* is null. |
| Created a roster | RosterCreated | A roster was created by a user or an app. If the create operation was a *ResultStatus.Failure* or *ResultStatus.AuthorizationFailure*, the *ObjectId* is null, *MemberIds* is an empty string. |
| Created a task | TaskCreated | A task was created by a user or an app. If the create operation was a *ResultStatus.Failure* or *ResultStatus.AuthorizationFailure*, the *ObjectId* is null and *PlanId* is null. |
| Deleted a chat message | ChatMessageDeleted | A chat message was deleted from a task chat by a user or an app. |
| Deleted a goal | GoalDeleted | A goal was deleted by a user or an app. |
| Deleted a plan | PlanDeleted | A plan was deleted by a user or an app. |
| Deleted a roster | RosterDeleted | A roster was deleted by a user or an app. |
| Deleted a task | TaskDeleted | A task was deleted by a user or an app. |
| Modified a chat message | ChatMessageModified | A chat message was modified by a user or an app. |
| Modified a goal | GoalModified | A goal was modified by a user or an app. |
| Modified a plan | PlanModified | A plan was modified by a user or an app. |
| Modified a task | TaskModified | A task was modified by a user or an app. |
| Read a goal | GoalRead | A goal was read by a user or an app. If the read operation was a *ResultStatus.Failure* or *ResultStatus.AuthorizationFailure*, the *PlanId* is null. |
| Read a list of chat messages | ChatMessageListRead | A list of chat messages was queried by a user or an app. -if the query operation was a *ResultStatus.Failure* or *ResultStatus.AuthorizationFailure*, *MessageList* is an empty string. |
| Read a list of goals | GoalListRead | A list of goals was queried by a user or an app. If the query operation was a *ResultStatus.Failure* or *ResultStatus.AuthorizationFailure*, *GoalList* is an empty string. |
| Read a list of plans | PlanListRead | A list of plans was queried by a user or an app. If the query operation was a *ResultStatus.Failure* or *ResultStatus.AuthorizationFailure*, *PlanList* is an empty string. |
| Read a list of tasks | TaskListRead | A list of tasks was queried by a user or an app. If the query operation was a *ResultStatus.Failure* or *ResultStatus.AuthorizationFailure*, *TaskList* is an empty string. |
| Read a plan | PlanRead | A plan was read by a user or an app. If the read operation was a *ResultStatus.Failure* or *ResultStatus.AuthorizationFailure*, *ContainerType* is *ContainerType.Invalid* and ContainerId is null. |
| Read a task | TaskRead | A task was read by a user or an app. If the read operation was a *ResultStatus.Failure* or *ResultStatus.AuthorizationFailure*, *PlanId* is null. |
| Removed a member to a roster | RosterMemberDeleted | A member was removed from a roster. If the remove operation was a *ResultStatus.Failure* or *ResultStatus.AuthorizationFailure*, *MemberIds* is the list of member IDs attempted. |
| Removed a reaction to a chat message | ChatMessageReactionRemoved | A reaction was removed from a chat message by a user or an app |
| Updated a roster's sensitivity label | RosterSensitivityLabelUpdated | A user or an app updates a roster's sensitivity label. |
| Updated tenant settings | TenantSettingsUpdated | Organization settings are updated by an organization admin. If the update operation was a *ResultStatus.Failure* or *ResultStatus.AuthorizationFailure*, the *ObjectId* is original settings, and *TenantSettings* is the attempted organization settings. |

## Power Apps activities

You can search the audit log for app-related activities in Power Apps. These activities include creating, launching, and publishing an app. Assigning permissions to apps is also audited. For a description of all Power Apps activities, see [Activity logging for Power Apps](/en-us/power-platform/admin/logging-powerapps#what-events-are-audited).

Note

[Alert Policies (Protection Alert)](/en-us/powershell/module/exchange/new-protectionalert) audit events (RecordType:45) aren't currently supported for PowerApps.

## Power Automate activities

You can search the audit log for activities in Power Automate (formerly called Microsoft Flow). These activities include creating, editing, and deleting flows, and changing flow permissions.

## Project for the web activities

You can search the audit log for activities in Microsoft Project for the web. Microsoft Project for the web is built on the [Microsoft Dataverse](https://powerplatform.microsoft.com/dataverse/) and has an associated Project Power App. To enable auditing for scenarios where the user is using the Microsoft Dataverse or the Project Power App, see the [System Settings Auditing tab](/en-us/power-platform/admin/system-settings-dialog-box-auditing-tab) guidance. For a list of entities related to Project for the web, see the [Export user data from Project for the web](/en-us/project-for-the-web/export-user-data-from-project-for-the-web#find-user-data-in-dataverse-with-the-advanced-find-search-feature) guidance.

For information about Microsoft Project for the web, see [Microsoft Project for the web](https://support.microsoft.com/office/get-started-with-project-for-the-web-50bf3e29-0f0d-4b7a-9d2c-7c78389b67ad).

Note

Auditing events for Microsoft Project for the web activities requires a paid Project Plan 1 license (or higher).

The following table lists the Microsoft Project for web activities recorded in the Microsoft 365 audit log:

| Friendly name | Operation | Description |
| --- | --- | --- |
| Created project | ProjectCreated | A project was created by a user or app. |
| Created roadmap | RoadmapCreated | A roadmap or portfolio was created by a user or app. |
| Created roadmap item | RoadmapItemCreated | A roadmap or portfolio item was created by a user or app. |
| Created task | TaskCreated | A task was created by a user or app. |
| Deleted project | ProjectDeleted | A project was deleted by a user or app. |
| Deleted roadmap | RoadmapDeleted | A roadmap or portfolio was deleted by a user or app. |
| Deleted roadmap item | RoadmapItemDeleted | A roadmap or portfolio item was deleted by a user or app. |
| Deleted task | TaskDeleted | A task was deleted by a user or app. |
| Project accessed | ProjectAccessed | A project was read by a user or app. |
| Project home accessed | ProjectListAccessed | A user queried a list of projects and/or roadmaps. |
| Roadmap accessed | RoadmapAccessed | A roadmap or portfolio was read by a user or app. |
| Roadmap item accessed | RoadmapItemAccessed | A roadmap or portfolio item was read by a user or app. |
| Task accessed | TaskAccessed | A task was read by a user or app. |
| Updated project | ProjectUpdated | A project was modified by a user or app. |
| Updated project settings | ProjectForTheWebProjectSettings | An admin updated project settings. |
| Updated roadmap | RoadmapUpdated | A roadmap or portfolio was modified by a user or app. |
| Updated roadmap item | RoadmapItemUpdated | A roadmap or portfolio item was modified by a user or app. |
| Updated roadmap settings | ProjectForTheWebRoadmaptSettings | An admin updated roadmap or portfolio settings. |
| Updated task | TaskUpdated | A task was modified by a user or app. |

## Quarantine activities

The following table lists the quarantine activities recorded in the Microsoft 365 audit log. For more information about quarantine, see [Quarantine email messages](/en-us/microsoft-365/security/office-365-security/quarantine-about?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Deleted quarantine message | QuarantineDeleteMessage | An admin or user deleted an email message that was harmful. |
| Denied quarantine message release request | QuarantineReleaseRequestDeny | An admin denial for a release request from a user for an email message that was harmful. |
| Exported quarantine message | QuarantineExport | An admin or user exported an email message that was harmful. |
| Previewed quarantine message | QuarantinePreview | An admin or user previewed an email message that was harmful. |
| Release request quarantine message | QuarantineReleaseRequest | A user requested the release of an email message that was harmful. |
| Released quarantine message | QuarantineRelease | An admin or user released an email message from quarantine that was harmful. |
| Viewed quarantine message's header | QuarantineViewHeader | An admin or user viewed the header of an email message that was harmful. |

## Report activities

The following table lists the activities for usage reports recorded in the Microsoft 365 audit log.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Updated usage report privacy settings | UpdateUsageReportsPrivacySetting | Admin updated privacy settings for usage reports. |

## Retention policy and retention label activities

The following table lists the configuration activities recorded in the Microsoft 365 audit log for [retention policies and retention labels](retention) when you create, reconfigure, or delete them.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Changed adaptive scope membership | ApplicableAdaptiveScopeChange | Users, sites, or groups were added to or removed from the adaptive scope. These changes result from running the scope's query. Because the changes are system-initiated, the reported user displays as a GUID rather than a user account. |
| Configured settings for a retention policy | NewRetentionComplianceRule | Administrator configured the retention settings for a new retention policy. Retention settings include how long items are retained, and what happens to items when the retention period expires (such as deleting items, retaining items, or retaining and then deleting them). This activity also corresponds to running the [New-RetentionComplianceRule](/en-us/powershell/module/exchange/new-retentioncompliancerule) cmdlet. |
| Created adaptive scope | NewAdaptiveScope | Administrator created an adaptive scope. |
| Created retention label | NewComplianceTag | Administrator created a new retention label. |
| Created retention policy | NewRetentionCompliancePolicy | Administrator created a new retention policy. |
| Deleted adaptive scope | RemoveAdaptiveScope | Administrator deleted an adaptive scope. |
| Deleted retention label | RemoveComplianceTag | Administrator deleted a retention label. |
| Deleted retention policy | RemoveRetentionCompliancePolicy | Administrator deleted a retention policy. |
| Deleted settings from a retention policy | RemoveRetentionComplianceRule | Administrator deleted the configuration settings of a retention policy. Most likely, this activity is logged when an administrator deletes a retention policy or runs the [Remove-RetentionComplianceRule](/en-us/powershell/module/exchange/Remove-RetentionComplianceRule) cmdlet. |
| Enabled regulatory record option for retention labels | SetRestrictiveRetentionUI | Administrator ran the [Set-RegulatoryComplianceUI](/en-us/powershell/module/exchange/set-regulatorycomplianceui) cmdlet so that an administrator can then select the UI configuration option for a retention label to mark content as a regulatory record. |
| Priority cleanup label applied on file | PriorityCleanupTagApplied | A retention label for priority cleanup is applied to an item on OneDrive or SharePoint (includes label replacement). |
| Retained email item proactively | ExchangeDataProactivelyPreserved | Adaptive protection automatically applied a retention label to retain an item in Exchange. |
| Retained file proactively | SharePointDataProactivelyPreserved | Adaptive protection automatically applied a retention label to retain an item in SharePoint or OneDrive. |
| Updated adaptive scope | SetAdaptiveScope | Administrator changed the description or query for an existing adaptive scope. |
| Updated retention label | SetComplianceTag | Administrator updated an existing retention label. |
| Updated retention policy | SetRetentionCompliancePolicy | Administrator updated an existing a retention policy. Updates that trigger this event include adding or excluding content locations that the retention policy is applied to. |
| Updated settings for a retention policy | SetRetentionComplianceRule | Administrator changed the retention settings for an existing retention policy. Retention settings include how long items are retained, and what happens to items when the retention period expires (such as deleting items, retaining items, or retaining and then deleting them). This activity also corresponds to running the [Set-RetentionComplianceRule](/en-us/powershell/module/exchange/set-retentioncompliancerule) cmdlet. |

## Role administration activities

The following table lists Microsoft Entra role administration activities recorded in the Microsoft 365 audit log when an admin manages admin roles in the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339) or in the Azure management portal.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Add member to Role | Add member to role. | Added a user to an admin role in Microsoft 365. |
| Removed a user from a directory role | Remove member from role. | Removed a user to from an admin role in Microsoft 365. |
| Set company contact information | Set company contact information. | Updated the company-level contact preferences for your organization. This includes email addresses for subscription-related email sent by Microsoft 365, and technical notifications about services. |

## Sensitive information types activities

The following table lists the audit events for activities recorded in the Microsoft 365 audit log involving creation and updating of [sensitive information types](sit-create-a-custom-sensitive-information-type).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Created new sensitive information type | CreateRulePackage / EditRulePackage\* | A new sensitive information type was [created](sit-create-a-custom-sensitive-information-type). This information includes any SITs created by copying an [out of the box SIT](sit-create-a-custom-sensitive-information-type). **Note**: This activity surfaces under the audit activities 'Created rule package' or 'Edited rule package'. |
| Deleted a sensitive information type | EditRulePackage / RemoveRulePackage | An existing sensitive information type was deleted. This activity surfaces under the audit activity "Edited rule package" or "Removed rule package." |
| Edited a sensitive information type | EditRulePackage | An existing sensitive information type was edited. This information can include operations like adding or removing a pattern and editing the regex or keyword associated with the sensitive information type. This activity surfaces under the audit activity "Edited rule package." |

## Sensitivity label activities

The following table lists events recorded in the Microsoft 365 audit log that result from using [sensitivity labels](sensitivity-labels) with containers and items managed by Microsoft Purview. Containers include SharePoint sites, Teams sites, and Loop workspaces. Items include documents, emails, calendar events, Loop components and pages, and Copilot pages. For auto-labeling policies, items also include files and data assets in Microsoft Purview Data Map.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Applied sensitivity label to file | FileSensitivityLabelApplied  SensitivityLabelApplied | A sensitivity label was applied to an item by using Microsoft 365 apps, Office for the web, the details pane in a SharePoint document library or from the Files tab in Teams, or an auto-labeling policy. The operations for this activity are different depending on how the label was applied: - Office for the web, details pane in a SharePoint document library or the Files tab in Teams, or an auto-labeling policy (FileSensitivityLabelApplied)  - Microsoft 365 apps (SensitivityLabelApplied). |
| Applied sensitivity label to site | SiteSensitivityLabelApplied | A sensitivity label was applied to a SharePoint site, Teams site that isn't group-connected, or a Loop workspace. |
| Changed sensitivity label applied to file | FileSensitivityLabelChangedSensitivityLabelUpdated | A different sensitivity label was applied to an item. The operations for this activity are different depending on how the label was changed: - Office for the web, details pane in a SharePoint document library or the Files tab in Teams, or an auto-labeling policy (FileSensitivityLabelChanged)  - Microsoft 365 apps (SensitivityLabelUpdated). |
| Changed sensitivity label on a site | SiteSensitivityLabelChanged | A different sensitivity label was applied to a SharePoint site, Teams site that isn't group-connected, or a Loop workspace. |
| Failed to apply file sensitivity label | FileSensitivityLabelAppliedFailed | A sensitivity label failed to be applied to an item by using Office for the web, the details pane in a SharePoint document library or from the Files tab in Teams, or an auto-labeling policy. |
| Failed to change file sensitivity label | FileSensitivityLabelChangedFailed | A different sensitivity label failed to be applied to an item using Office for the web, the details pane in a SharePoint document library or from the Files tab in Teams, or an auto-labeling policy. |
| Failed to remove file sensitivity label | FileSensitivityLabelRemovedFailed | A sensitivity label failed to be removed from an item by using Office for the web, the details pane in a SharePoint document library or from the Files tab in Teams, or an auto-labeling policy. |
| Removed sensitivity label from file | FileSensitivityLabelRemoved  SensitivityLabelRemoved | A sensitivity label was removed from an item by using Microsoft 365 apps, Office for the web, the details pane in a SharePoint document library or the Files tab in Teams, an auto-labeling policy, or the [Unlock-SPOSensitivityLabelEncryptedFile](/en-us/powershell/module/microsoft.online.sharepoint.powershell/unlock-sposensitivitylabelencryptedfile) cmdlet. The operations for this activity are different depending on how the label was removed: - Office for the web, details pane in a SharePoint document library or the Files tab in Teams, or an auto-labeling policy (FileSensitivityLabelRemoved)  - Microsoft 365 apps (SensitivityLabelRemoved). |
| Removed sensitivity label from site | SiteSensitivityLabelRemoved | A sensitivity label was removed from a SharePoint site, Teams site that isn't group-connected, or a Loop workspace. |

The following table lists descriptions for values recorded in the Microsoft 365 audit log included in the *FailureReason* property for audit activities that log failures to apply, change, or remove sensitivity labels. These properties aren't available for other sensitivity label activities:

| FailureReason property | Property description |
| --- | --- |
| CannotOverrideCurrentLabel | A sensitivity label wasn't assigned to the file because the currently applied sensitivity label has a higher priority. |
| DowngradeJustificationTextMissing | Sensitivity label wasn't assigned to the file because justification text is required for this operation. |
| FileEncrypted | A sensitivity label wasn't assigned to the file because it's encrypted. |
| FileExtensionNotSupported | A sensitivity label wasn't assigned to the file because the file type isn't supported for this operation. |
| FileLockedOrCheckedOut | A sensitivity label wasn't assigned to the file because it's locked or checked out. |
| FileNotFound | A sensitivity label wasn't assigned to the file because it isn't available. |
| FileNotSupported | A sensitivity label wasn't assigned to the file because it doesn't support this operation. |
| FileTooLarge | A sensitivity label wasn't assigned to the file because it's too large to support this operation. |
| InvalidArgument | A sensitivity label wasn't assigned to the file because some parameters provided to perform this operation aren't valid. |
| LabelIdNotFound | A sensitivity label wasn't assigned to the file because the sensitivity label provided is unavailable or isn't valid. |
| LabelNotSupported | A sensitivity label wasn't assigned to the file because the sensitivity label provided isn't supported. |
| LabelOperationsDisabled | A sensitivity label wasn't assigned to the file because the sensitivity label operation is disabled on the file. |
| MinorVersionLimitExceeded | A sensitivity label wasn't assigned to the file because the version limit is exceeded. |
| UnauthorizedAccessException | A sensitivity label wasn't assigned to the file because the current user isn't authorized to perform this operation. |
| Unknown | A sensitivity label wasn't assigned to the file because of an internal error. |
| ZeroByteFileError | A sensitivity label wasn't assigned to the file because the operation can't be performed on a zero-byte file. |

Additional auditing information for sensitivity labels:

- When you use sensitivity labels for Microsoft 365 Groups, and therefore Teams sites that are group-connected, the labels are audited with group management in Microsoft Entra ID. For more information, see [Audit logs in Microsoft Entra ID](/en-us/azure/active-directory/reports-monitoring/concept-audit-logs).
- When you use sensitivity labels for Teams meeting invites, and Teams meeting options and chat, see [Search the audit log for events in Microsoft Teams](/en-us/microsoftteams/audit-log-events).
- When you use sensitivity labels with Power BI, see [Audit schema for sensitivity labels in Power BI](/en-us/power-bi/enterprise/service-security-sensitivity-label-audit-schema).
- When you use sensitivity labels with Microsoft Defender for cloud apps, see [Governing connected apps](/en-us/defender-cloud-apps/governance-actions) and the labeling information for file governance actions.

## SharePoint list activities

The following table lists the activities recorded in the Microsoft 365 audit log related to when users interact with lists and list items in SharePoint. Audit records for some SharePoint activities show that the app@sharepoint user performed the activity on behalf of the user or admin who initiated the action. For more information, see The app@sharepoint user in audit records.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Created list | ListCreated | A user created a SharePoint list. |
| Created list column | ListColumnCreated | A user created a SharePoint list column. A list column is a column that's attached to one or more SharePoint lists. |
| Created list content type | ListContentTypeCreated | A user created a list content type. A list content type is a content type that's attached to one or more SharePoint lists. |
| Created list item | ListItemCreated | A user created an item in an existing SharePoint list. |
| Created site column | SiteColumnCreated | A user created a SharePoint site column. A site column is a column that isn't attached to a list. A site column is also a metadata structure that can be used by any list in a given web. |
| Created site content type | Site ContentType Created | A user created a site content type. A site content type is a content type that's attached to the parent site. |
| Deleted list | ListDeleted | A user deleted a SharePoint list. |
| Deleted list column | List Column Deleted | A user deleted a SharePoint list column. |
| Deleted list content type | ListContentTypeDeleted | A user deleted a list content type. |
| Deleted list item | List Item Deleted | A user deleted a SharePoint list item. |
| Deleted site column | SiteColumnDeleted | A user deleted a SharePoint site column. |
| Deleted site content type | SiteContentTypeDeleted | A user deleted a site content type. |
| Recycled list item | ListItemRecycled | A user moved a SharePoint list item to the Recycle Bin. |
| Restored list | ListRestored | A user restored a SharePoint list from the Recycle Bin. |
| Restored list item | ListItemRestored | A user restored a SharePoint list item from the Recycle Bin. |
| Updated list | ListUpdated | A user updated a SharePoint list by modifying one or more properties. |
| Updated list column | ListColumnUpdated | A user updated a SharePoint list column by modifying one or more properties. |
| Updated list content type | ListContentTypeUpdated | A user updated a list content type by modifying one or more properties. |
| Updated list item | ListItemUpdated | A user updated a SharePoint list item by modifying one or more properties. |
| Updated list view | ListViewUpdated | A user updated a SharePoint list view by modifying one or more properties. |
| Updated site column | SiteColumnUpdated | A user updated a SharePoint site column by modifying one or more properties. |
| Updated site content type | SiteContentTypeUpdated | A user updated a site content type by modifying one or more properties. |

## SharePoint Embedded container type activities

The following table lists SharePoint Embedded container type activities that the Microsoft 365 audit log records. For more information about SharePoint Embedded, see [SharePoint Embedded overview](/en-us/sharepoint/dev/embedded/overview).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Created container type | ContainerTypeCreated | A SharePoint Embedded container type was created. |
| Deleted container type | ContainerTypeDeleted | A SharePoint Embedded container type was deleted. |
| Updated container type | ContainerTypeUpdated | A SharePoint Embedded container type was updated. |
| Updated container type owners | ContainerTypeOwnersUpdated | The owners of a SharePoint Embedded container type were updated. |

## Sharing and access request activities

The following table lists the user sharing and access request activities in SharePoint and OneDrive recorded in the Microsoft 365 audit log. For sharing events, the **Detail** column under **Results** identifies the name of the user or group the item was shared with and whether that user or group is a member or guest in your organization. For more information, see [Use sharing auditing in the audit log](audit-log-sharing).

Note

Users can be either *members* or *guests* based on the UserType property of the user object. A member is usually a user within the organization, and a guest is usually a collaborator outside of your organization. When a user accepts a sharing invitation (and isn't already part of your organization), a guest account is created for them in your organization's directory. After the guest user has an account in your directory, you might share resources directly with them (without requiring an invitation).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Accepted access request | AccessRequestAccepted | An access request to a site, folder, or document was accepted and the requesting user was granted access. |
| Accepted sharing invitation | SharingInvitationAccepted | User (member or guest) accepted a sharing invitation and was granted access to a resource. This event includes information about the user who was invited and the email address that was used to accept the invitation (they could be different). This activity is often accompanied by a second event that describes how the user was granted access to the resource, for example, adding the user to a group that has access to the resource. |
| Added permission level to site collection | PermissionLevelAdded | A permission level was added to a site collection. |
| Blocked sharing invitation | SharingInvitationBlocked | A sharing invitation sent by a user in your organization is blocked because of an external sharing policy that either allows or denies external sharing based on the domain of the target user. In this case, the sharing invitation was blocked because:  The target user's domain isn't included in the list of allowed domains.  Or  The target user's domain is included in the list of blocked domains.  For more information about allowing or blocking external sharing based on domains, see [Restricted domains sharing in SharePoint and OneDrive](/en-us/sharepoint/restricted-domains-sharing). |
| Created a company shareable link | CompanyLinkCreated | User created a company-wide link to a resource. Company-wide links can only be used by members in your organization. They can't be used by guests. |
| Created access request | AccessRequestCreated | User requests access to a site, folder, or document they don't have permissions to access. |
| Created an anonymous link | AnonymousLinkCreated | User created an anonymous link to a resource. Anyone with this link can access the resource without having to be authenticated. |
| Created secure link | SecureLinkCreated | A secure sharing link was created to this item. |
| Created sharing invitation | SharingInvitationCreated | User shared a resource in SharePoint or OneDrive with a user who isn't in your organization's directory. |
| Deleted secure link | SecureLinkDeleted | A secure sharing link was deleted. |
| Denied access request | AccessRequestDenied | An access request to a site, folder, or document was denied. |
| Removed a company shareable link | CompanyLinkRemoved | User removed a company-wide link to a resource. The link can no longer be used to access the resource. |
| Removed an anonymous link | AnonymousLinkRemoved | User removed an anonymous link to a resource. The link can no longer be used to access the resource. |
| Shared file, folder, or site | SharingSet | User (member or guest) shared a file, folder, or site in SharePoint or OneDrive with a user in your organization's directory. The value in the **Detail** column for this activity identifies the name of the user the resource was shared with and whether this user is a member or a guest.  This activity is often accompanied by a second event that describes how the user was granted access to the resource. For example, adding the user to a group that has access to the resource. |
| Unshared file, folder, or site | SharingRevoked | User (member or guest) unshared a file, folder, or site that was previously shared with another user. |
| Updated access request | AccessRequestUpdated | An access request to an item was updated. |
| Updated an anonymous link | AnonymousLinkUpdated | User updated an anonymous link to a resource. The updated field is included in the EventData property when you export the search results. |
| Updated sharing invitation | SharingInvitationUpdated | An external sharing invitation was updated. |
| Used a company shareable link | CompanyLinkUsed | User accessed a resource by using a company-wide link. |
| Used an anonymous link | AnonymousLinkUsed | An anonymous user accessed a resource by using an anonymous link. The user's identity might be unknown, but you can get other details such as the user's IP address. |
| Used secure link | SecureLinkUsed | A user used a secure link. |
| User added to secure link | AddedToSecureLink | A user was added to the list of entities who can use a secure sharing link. |
| User removed from secure link | RemovedFromSecureLink | A user was removed from the list of entities who can use a secure sharing link. |
| Withdrew sharing invitation | SharingInvitationRevoked | User withdrew a sharing invitation to a resource. |

## Site administration activities

The following table lists events that result from site administration tasks in SharePoint and are recorded in the Microsoft 365 audit log. Audit records for some SharePoint activities indicate the app@sharepoint user performed the activity on behalf of the user or admin who initiated the action. For more information, see The app@sharepoint user in audit records.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Added allowed data location | AllowedDataLocationAdded | A SharePoint or global administrator added an allowed data location in a multigeo environment. |
| Added exempt user agent | ExemptUserAgentSet | A SharePoint or global administrator added a user agent to the list of exempt user agents in the SharePoint admin center. |
| Added geo location admin | GeoAdminAdded | A SharePoint or global administrator added a user as a geo admin of a location. |
| Allowed user to create groups | AllowGroupCreationSet | Site administrator or owner adds a permission level to a site that allows a user assigned that permission to create a group for that site. |
| Apply theme to a web | WebThemeApplied | A SharePoint, global administrator, or a site owner applied a web theme. |
| Canceled site geo move | SiteGeoMoveCancelled | A SharePoint or global administrator canceled a SharePoint or OneDrive site geo move. The multigeo capability lets an organization span multiple Microsoft datacenter geographies, which are called geos. For more information, see [Multi-Geo Capabilities in OneDrive and SharePoint](/en-us/microsoft-365/enterprise/multi-geo-capabilities-in-onedrive-and-sharepoint-online-in-microsoft-365?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json). |
| Changed a sharing policy | SharingPolicyChanged | A SharePoint or global administrator changed a SharePoint sharing policy by using the Microsoft 365 admin center, SharePoint admin center, or SharePoint Management Shell. Any change to the settings in the sharing policy in your organization are logged. The policy that was changed is identified in the **ModifiedProperties** field in the detailed properties of the event record. |
| Changed device access policy | DeviceAccessPolicyChanged | A SharePoint or global administrator changed the unmanaged devices policy for your organization. This policy controls access to SharePoint, OneDrive, and Microsoft 365 from devices that aren't joined to your organization. Configuring this policy requires an Enterprise Mobility + Security subscription. For more information, see [Control access from unmanaged devices](/en-us/sharepoint/control-access-from-unmanaged-devices). |
| Changed exempt user agents | CustomizeExemptUsers | A SharePoint or global administrator customized the list of exempt user agents in the SharePoint admin center. You can specify which user agents to exempt from receiving an entire web page to index. This means when a user agent you specified as exempt encounters an InfoPath form, the form is returned as an XML file, instead of an entire web page. This makes indexing InfoPath forms faster. |
| Changed network access policy | NetworkAccessPolicyChanged | A SharePoint or global administrator changed the location-based access policy (also called a trusted network boundary) in the SharePoint admin center or by using SharePoint PowerShell. This type of policy controls who can access SharePoint and OneDrive resources in your organization based on authorized IP address ranges that you specify. For more information, see [Control access to SharePoint and OneDrive data based on network location](/en-us/sharepoint/control-access-based-on-network-location). |
| Completed migration job | MigrationJobCompleted | A migration job completed. |
| Completed site geo move | SiteGeoMoveCompleted | A site geo move that a global administrator in your organization scheduled completed. The multigeo capability lets an organization span multiple Microsoft datacenter geographies, which are called geos. For more information, see [Multi-Geo Capabilities in OneDrive and SharePoint](/en-us/microsoft-365/enterprise/multi-geo-capabilities-in-onedrive-and-sharepoint-online-in-microsoft-365?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json). |
| Create tenant-wide theme | TenantWideThemeCreated | A SharePoint administrator, global administrator, or brand manager created a custom theme applied across all SharePoint sites in your organization. |
| Created Sent To connection | SendToConnectionAdded | A SharePoint or global administrator creates a new Send To connection on the Records management page in the SharePoint admin center. A Send To connection specifies settings for a document repository or a records center. When you create a Send To connection, a Content Organizer can submit documents to the specified location. |
| Created site collection | SiteCollectionCreated | A SharePoint or global administrator creates a site collection in your SharePoint organization or a user provisions their OneDrive site. |
| Delete tenant-wide theme | TenantWideThemeDeleted | A SharePoint administrator, global administrator, or brand manager deleted a custom theme applied across all SharePoint sites in your organization. |
| Deleted orphaned hub site | HubSiteOrphanHubDeleted | A SharePoint or global administrator deleted an orphan hub site, which is a hub site that doesn't have any sites associated with it. An orphaned hub is likely caused by the deletion of the original hub site. |
| Deleted Sent To connection | SendToConnectionRemoved | A SharePoint or global administrator deletes a Send To connection on the Records management page in the SharePoint admin center. |
| Deleted site | SiteDeleted | Site administrator deletes a site. |
| Enabled document preview | PreviewModeEnabledSet | Site administrator enables document preview for a site. |
| Enabled legacy workflow | LegacyWorkflowEnabledSet | Site administrator or owner adds the SharePoint 2013 Workflow Task content type to the site. Global administrators can also enable workflows for the entire organization in the SharePoint admin center. |
| Enabled Office on Demand | OfficeOnDemandSet | Site administrator enables Office on Demand, which lets users access the latest version of Office desktop applications. Office on Demand is enabled in the SharePoint admin center and requires a Microsoft 365 subscription that includes full, installed Office applications. |
| Enabled result source for People Searches | PeopleResultsScopeSet | Site administrator creates the result source for People Searches for a site. |
| Enabled RSS feeds | NewsFeedEnabledSet | Site administrator or owner enables RSS feeds for a site. Global administrators can enable RSS feeds for the entire organization in the SharePoint admin center. |
| Joined site to hub site | HubSiteJoined | A site owner associates their site with a hub site. |
| Modified site collection quota | SiteCollectionQuotaModified | Site administrator modifies the quota for a site collection. |
| Permanently delete site | SitePermanentlyDeleted | A SharePoint or global administrator permanently deletes a site from SharePoint Admin Center Deleted Sites. |
| Registered hub site | HubSiteRegistered | A SharePoint or global administrator creates a hub site. The results are that the site is registered to be a hub site. |
| Removed allowed data location | AllowedDataLocationDeleted | A SharePoint or global administrator removed an allowed data location in a multigeo environment. |
| Removed geo location admin | GeoAdminDeleted | A SharePoint or global administrator removed a user as a geo admin of a location. |
| Renamed site | SiteRenamed | Site administrator or owner renames a site. |
| Restore Site | SiteRestored | A SharePoint or global administrator restores a site from SharePoint Admin Center Deleted Sites. |
| Scheduled site geo move | SiteGeoMoveScheduled | A SharePoint or global administrator scheduled a SharePoint or OneDrive site geo move. The multigeo capability lets an organization span multiple Microsoft datacenter geographies, which are called geos. For more information, see [Multi-Geo Capabilities in OneDrive and SharePoint](/en-us/microsoft-365/enterprise/multi-geo-capabilities-in-onedrive-and-sharepoint-online-in-microsoft-365?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json). |
| Set host site | HostSiteSet | A SharePoint or global administrator changes the designated site to host personal or OneDrive sites. |
| Set storage quota for geo location | GeoQuotaAllocated | A SharePoint or global administrator configured the storage quota for a geo location in a multigeo environment. |
| Unjoined site from hub site | HubSiteUnjoined | A site owner disassociates their site from a hub site. |
| Unregistered hub site | HubSiteUnregistered | A SharePoint or global administrator unregisters a site as a hub site. When a hub site is unregistered, it no longer functions as a hub site. |
| Update DisableSiteBranding config | UpdateDisableSiteBranding | A SharePoint or global administrator enables or disables site branding. |
| Update tenant-wide theme | TenantWideThemeUpdated | A SharePoint administrator, global administrator, or brand manager updated a custom theme applied across all SharePoint sites in your organization. |

## Site permissions activities

The following table lists events related to assigning permissions in SharePoint and using groups to give (and revoke) access to sites recorded in the Microsoft 365 audit log. Audit records for some SharePoint activities indicate the app@sharepoint user performed the activity on behalf of the user or admin who initiated the action. For more information, see The app@sharepoint user in audit records.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Added site collection admin | SiteCollectionAdminAdded | Site collection administrator or owner adds a person as a site collection administrator for a site. Site collection administrators have full control permissions for the site collection and all subsites. This activity is also logged when an admin gives themselves access to a user's OneDrive account (by editing the user profile in the SharePoint admin center or by [using the Microsoft 365 admin center](/en-us/office365/admin/add-users/get-access-to-and-back-up-a-former-user-s-data?toc=%2Fpurview%2Ftoc.json&amp;bc=%2Fpurview%2Fbreadcrumb%2Ftoc.json)). |
| Added user or group to SharePoint group | AddedToGroup | User added a member or guest to a SharePoint group. This action might be intentional or the result of another activity, such as a sharing event. |
| Broke permission level inheritance | PermissionLevelsInheritanceBroken | An item was changed so that it no longer inherits permission levels from its parent. |
| Broke sharing inheritance | SharingInheritanceBroken | An item was changed so that it no longer inherits sharing permissions from its parent. |
| Created group | GroupAdded | Site administrator or owner creates a group for a site, or performs a task that results in a group being created. For example, the first time a user creates a link to share a file, a system group is added to the user's OneDrive site. This event can also be a result of a user creating a link with edit permissions to a shared file. |
| Deleted group | GroupRemoved | User deletes a group from a site. |
| Modified 'Members Can Share' setting | WebMembersCanShareModified | The **Members Can Share** setting was modified on a site. |
| Modified access request setting | WebRequestAccessModified | The access request settings were modified on a site. |
| Modified permission level on a site collection | PermissionLevelModified | A permission level was changed on a site collection. |
| Modified site permissions | SitePermissionsModified | Site administrator or owner (or system account) changes the permission level that is assigned to a group on a site. This activity is also logged if all permissions are removed from a group. **NOTE**: This operation is deprecated in SharePoint. To find related events, you can search for other permission-related activities such as **Added site collection admin**, **Added user or group to SharePoint group**, **Allowed user to create groups**, **Created group**, and **Deleted group.** |
| Removed permission level from site collection | PermissionLevelRemoved | A permission level was removed from a site collection. |
| Removed site collection admin | SiteCollectionAdminRemoved | Site collection administrator or owner removes a person as a site collection administrator for a site. This activity is also logged when an admin removes themselves from the list of site collection administrators for a user's OneDrive account (by editing the user profile in the SharePoint admin center). To return this activity in the audit log search results, you have to search for all activities. |
| Removed user or group from SharePoint group | RemovedFromGroup | User removed a member or guest from a SharePoint group. This action might be intentional or the result of another activity, such as an unsharing event. |
| Requested site admin permissions | SiteAdminChangeRequest | User requests to be added as a site collection administrator for a site collection. Site collection administrators have full control permissions for the site collection and all subsites. |
| Restored sharing inheritance | SharingInheritanceReset | A change was made so that an item inherits sharing permissions from its parent. |
| Updated group | GroupUpdated | Site administrator or owner changes the settings of a group for a site. This change can include the group's name, who can view or edit the group membership, and how membership requests are handled. |

## Stream activities

You can search the audit log for activities in Microsoft Stream. These activities include video activities performed by users, group channel activities, and admin activities such as managing users, managing organization settings, and exporting reports. For a description of these activities, see the "Actions logged in Stream" section in [Audit Logs in Microsoft Stream](/en-us/stream/audit-logs#actions-logged-in-stream).

## Synchronization activities

The following table lists file synchronization activities recorded in the Microsoft 365 audit log for SharePoint and OneDrive.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Allowed computer to sync files | ManagedSyncClientAllowed | User established a sync relationship with a site. The sync relationship is successful because the user's computer is a member of a domain that's been added to the list of domains (called the *safe recipients list*) that can access document libraries in your organization.  For more information about this feature, see [Use PowerShell cmdlets to enable OneDrive sync for domains that are on the safe recipients list](/en-us/powershell/module/microsoft.online.sharepoint.powershell/). |
| Blocked computer from syncing files | UnmanagedSyncClientBlocked | User tries to establish a sync relationship with a site from a computer that isn't a member of your organization's domain or is a member of a domain that hasn't been added to the list of domains (called the *safe recipients list)* that can access document libraries in your organization. The sync relationship isn't allowed, and the user's computer is blocked from syncing, downloading, or uploading files on a document library.  For information about this feature, see [Use PowerShell cmdlets to enable OneDrive sync for domains that are on the safe recipients list](/en-us/powershell/module/microsoft.online.sharepoint.powershell/). |
| Downloaded file changes to computer | FileSyncDownloadedPartial | This event is deprecated along with the old OneDrive sync app (Groove.exe). |
| Downloaded files to computer | FileSyncDownloadedFull | User downloaded a file to their computer from a SharePoint document library or OneDrive using OneDrive sync app (OneDrive.exe). |
| Uploaded file changes to document library | FileSyncUploadedPartial | This event is deprecated along with the old OneDrive sync app (Groove.exe). |
| Uploaded files to document library | FileSyncUploadedFull | User uploaded a new file or changes to a file in SharePoint document library or OneDrive by using OneDrive sync app (OneDrive.exe). |

## SystemSync activities

The following table lists the activities for SystemSync recorded in the Microsoft 365 audit log.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Data Share Created | DataShareCreated | When the user created the data export. |
| Data Share Deleted | DataShareDeleted | When the user deleted the data export. |
| Download Copy Of Lake Data | DownloadCopyOfLakeData | When the copy of Lake Data is downloaded. |
| Generate Copy Of Lake Data | GenerateCopyOfLakeData | When the copy of Lake Data is generated. |

## Teams activities

The following table lists Microsoft Teams activities recorded in the Microsoft 365 audit log. You can search the audit log for user and admin activities in Microsoft Teams. Teams is a chat-centered workspace in Microsoft 365. It brings a team's conversations, meetings, files, and notes together into a single place. For more detailed search guidance, see [Search the audit log for events in Microsoft Teams](audit-teams-audit-log-events).

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Accept message | UserAccepted | Accept a new message from a person who never established contact with. |
| Added bot to team | BotAddedToTeam | A user adds a bot to a team. |
| Added channel | ChannelAdded | A user adds a channel to a team. |
| Added connector | ConnectorAdded | A user adds a connector to a channel. |
| Added details about Teams meeting ^9^ | MeetingDetail | Teams added information about a meeting, including the start time, the end time, the URL to join the meeting, and the recording start/stop time for the meeting. |
| Added information about call participants ^10, 11, 12^ | CallParticipantDetail | Teams added information about the participants of a call, including the user ID of each participant, the time each participant joined and left the call, and participant connection information. |
| Added information about meeting participants ^9, 12, 14^ | MeetingParticipantDetail | Teams added information about the participants of a meeting, including the user ID of each participant, the time a participant joined the meeting, the time a participant left the meeting, and the start/stop time of a meeting recording by the user. You can also see logs with timestamps and information about: - Who joined a meeting - Where screensharing occurred - Who started the screenshare - When screensharing occurred- When screensharing stopped - When take, give, or request control was activated - If these control requests were accepted - Who accepted these control requests - Who the content was shared with. |
| Added members ^6, 8^ | MemberAdded | A team owner adds members to a team, channel, or group chat. |
| Added tab | TabAdded | A user adds a tab to a channel. |
| Applied sensitivity label | SensitivityLabelApplied | A user or meeting organizer applied a sensitivity label to a Teams meeting. |
| Approved request | ApprovedRequest | After the user views the details of the approval request, they approved it. |
| Block user | UserBlocked | Block a user from sending messages to you. |
| Canceled approval request | CanceledApprovalRequest | User canceled an approval request they made. |
| Cancelled approval asynchronously | CancelledApprovalAsync | User cancels an approval request asynchronously. |
| Changed channel setting | ChannelSettingChanged | The ChannelSettingChanged operation is logged when the following activities are performed by a team member. For each of these activities, a description of the setting that was changed (shown in parentheses) is displayed in the **Item** column in the audit log search results. <br>- Changes name of a team channel (**Channel name**)<br>- Changes description of a team channel (**Channel description**). |
| Changed organization setting | TeamsTenantSettingChanged | The TeamsTenantSettingChanged operation is logged when the following activities are performed by a global admin in the Microsoft 365 admin center. These activities affect org-wide Teams settings. For more information, see [Manage Teams settings for your organization](/en-us/microsoftteams/enable-features-office-365). For each of these activities, a description of the setting that was changed (shown in parentheses) is displayed in the **Item** column in the audit log search results.<br>- Enables or disables Teams for the organization (**Microsoft Teams**).<br>- Enables or disables interoperability between Microsoft Teams and Skype for Business for the organization (**Skype for Business interoperability**).<br>- Enables or disables the organizational chart view in Microsoft Teams clients (**Org chart view**).<br>- Enables or disables the ability for team members to schedule private meetings (**Private meeting scheduling**).<br>- Enables or disables the ability for team members to schedule channel meetings (**Channel meeting scheduling**).<br>- Enables or disables video calling in Teams meetings (**Video for Skype meetings**).<br>- Enables or disables screen sharing in Microsoft Teams meetups for the organization (**Screen sharing for Skype meetings**).<br>- Enables or disables that ability to add animated images (called Giphys) to Teams conversations (**Animated images**).<br>- Changes the content rating setting for the organization (**Content rating**). The content rating restricts the type of animated image that can be displayed in conversations.<br>- Enables or disables the ability for team members to add customizable images (called custom memes) from the internet to team conversations (**Customizable images from the Internet**).<br>- Enables or disables the ability for team members to add editable images (called stickers) to team conversations (**Editable images**).<br>- Enables or disables that ability for team members to use bots in Microsoft Teams chats and channels (**Org-wide bots)**.<br>- Enables specific bots for Microsoft Teams. This doesn't include the T-Bot, which is Teams help bot that's available when bots are enabled for the organization (**Individual bots**).<br>- Enables or disables the ability for team members to add extensions or tabs (**Extensions or tabs**).<br>- Enables or disables the side-loading of proprietary bots for Microsoft Teams (**Side loading of Bots**).<br>- Enables or disables the ability for users to send email messages to a Microsoft Teams channel (**Channel email**). |
| Changed role of members in team | MemberRoleChanged | A team owner changes the role of members in a team. The following values indicate the role type assigned to the user. **1** - The Member role.**2** - The Owner role.**3** - The Guest role.The Members property also includes the name of your organization and the member's email address. |
| Changed sensitivity label | SensitivityLabelChanged | A user changed a sensitivity label on a Teams meeting. |
| Changed team setting | TeamSettingChanged | The TeamSettingChanged operation is logged when the following activities are performed by a team owner. For each of these activities, a description of the setting that was changed (shown in parentheses) is displayed in the **Item** column in the audit log search results.<br>- Changes the access type for a team. Teams can be set as private or public (**Team access type**). When a team is private (the default setting), users can access the team only by invitation. When a team is public, it's discoverable by anyone.<br>- Changes the information classification of a team (**Team classification**). For example, team data can be classified as high business impact, medium business impact, or low business impact.<br>- Changes the name of a team (**Team name**).<br>- Changes the team description (**Team description**).<br>- Changes made to team settings. To access these settings, a team owner can right-click a team, select **Manage team**, and then select the **Settings** tab. For these activities, the name of the setting that was changed is displayed in the **Item** column in the audit log search results. |
| Create org scoped template instance | CreateOrgScopedTemplateInstance | User created an organization scoped template instance. |
| Create team scoped template instance | CreateTeamScopedTemplateInstance | User created a team scoped template instance. |
| Create update request | CreateUpdateRequest | User created a new update template. |
| Created a chat ^1, 6^ | ChatCreated | A Teams chat was created. |
| Created approval | CreatedApproval | User created a new approval request. |
| Created approval asynchronously | CreatedApprovalAsync | User creates a new approval request asynchronously. |
| Created export job | CreatedExportJob | User created an export job. |
| Created provisioning | CreatedProvisioning | User created provisioning of CDS (Common Data Service) instance. |
| Created team | TeamCreated | A user creates a team. |
| Delete update request | DeleteUpdateRequest | User deletes an update template. |
| Deleted a message ^2^ | MessageDeleted | A message in a chat or channel was deleted. |
| Deleted all organization apps | DeletedAllOrganizationApps | Deleted all organization apps from the catalog. |
| Deleted app | AppDeletedFromCatalog | An app was deleted from the catalog. |
| Deleted channel | ChannelDeleted | A user deletes a channel from a team. |
| Deleted team | TeamDeleted | A team owner deletes a team. |
| Detected impersonation attempt | TeamsImpersonationDetected | An external message sender is detected to have potential impersonation activity. |
| Detected security risk in meeting | SecurityRiskInMeetingDetected | A security risk was detected in a Microsoft Teams meeting, such as brand, domain, or user impersonation by a meeting organizer or participant. |
| Detected security risk in call | SecurityRiskInCallDetected | A security risk was detected during an incoming call in Microsoft Teams, such as brand, domain, or user impersonation. |
| Downloaded file | DownloadedFile | User downloaded file attached to an approval request. |
| Edit org scoped template instance | EditOrgScopedTemplateInstance | User edited an organization scoped template instance. |
| Edit team scoped template instance | EditTeamScopedTemplateInstance | User edited a team scoped template instance. |
| Edit update request | EditUpdateRequest | User opens template edit wizard and selects the save button to confirm any update or enable/disable templates. |
| Edited a message | GraphMessageUpdated | A user updates a chat or channel message. |
| Edited a message with a URL link in Teams | MessageEditedHasLink | A user edits a message and adds a URL link to it in Teams. |
| Edited approval request | EditedApprovalRequest | User took an edit action on an approval request. |
| Exported messages ^1,^^2^ | MessagesExported | Chat or channel messages were exported. |
| Exported recordings ^1^ | RecordingsExported | Chat recordings were exported. |
| Exported transcripts ^1^ | TranscriptsExported | Chat transcripts were exported. |
| Failed to validate invitation to shared channel ^3^ | FailedValidation | A user responds to an invitation to a shared channel but the invitation failed validation. |
| Fetched all hosted content of a message^1^ | MessageHostedContentsListed | All hosted content in a message, such as images or code snippets, was retrieved. |
| Fetched chat ^1^ | ChatRetrieved | A Microsoft Teams chat was retrieved. |
| Get org scoped template instance | GetOrgScopedTemplateInstance | User fetched an organization scoped template instance. |
| Get team scoped template instance | GetTeamScopedTemplateInstance | User fetched a team scoped template instance. |
| Got async operation | GotAsyncOperation | User got async operation entity. |
| Installed app | AppInstalled | An app was installed. |
| Obtain list of meeting recordings ^13^ | GraphMeetingRecordingsListed | List recording details for an online meeting. |
| Obtain list of meeting transcripts ^13^ | GraphMeetingTranscriptsListed | List transcript details for an online meeting. |
| Obtain meeting transcript content ^13^ | GraphMeetingTranscriptContentRead | Get the transcript content for an online meeting or an ad hoc call. |
| Obtain meeting transcript instance ^13^ | GraphMeetingTranscriptRead | Get the transcript details for an online meeting or ad hoc call. |
| Obtained meeting recording content ^13^ | GraphMeetingRecordingContentRead | Get the recording content for an online meeting or an ad hoc call. |
| Obtained meeting recording instance ^13^ | GraphMeetingRecordingRead | Get the recording details for an online meeting or an ad hoc call. |
| Performed action on card | PerformedCardAction | A user took action on an adaptive card within a chat. Adaptive cards are typically used by bots to allow the rich display of information and interaction in chats. Only inline input actions on an adaptive card inside a chat are available in the audit log. For example, when a user submits a poll response in a channel conversation on an adaptive card generated by a Poll bot. User actions such as "View result", which opens a dialog, or user actions inside dialogs aren't available in the audit log. |
| Populate AI-generated notes in chat | AINotesUpdate | AI-generated notes were populated for a group chat. |
| Populate AI-generated notes in live meetings | LiveNotesUpdate | AI-generated notes were populated for a live meeting. |
| Posted new message ^3,^^4,^^6, 8^ | MessageSent | A new message was posted to a chat or a channel. |
| Published app | AppPublishedToCatalog | An app was added to the catalog. |
| Read a message ^1^ | MessageRead | A message of a chat or channel was retrieved. |
| Read hosted content of a message ^1^ | MessageHostedContentRead | Hosted content in a message, such as an image or a code snippet, was retrieved. |
| Reassigned approval request | ReassignedApprovalRequest | User reassigned an approval request to another user. |
| Received Read Receipt on a message | MessageReadReceiptReceived | A read receipt was received indicating that a user has read one or more messages in a chat. The audit record includes the chat thread and the point up to which messages were read. |
| Rejected approval request | RejectedApprovalRequest | After the user views the details of the approval request, they rejected it. |
| Removed bot from team | BotRemovedFromTeam | A user removes a bot from a team. |
| Removed connector | ConnectorRemoved | A user removes a connector from a channel. |
| Removed members ^6, 8^ | MemberRemoved | A team owner removes members from a team, channel, or group chat. |
| Removed sensitivity label | SensitivityLabelRemoved | A user removed a sensitivity label from a Teams meeting. |
| Removed sharing of team channel ^3^ | TerminatedSharing | A team or channel owner disabled sharing for a shared channel. |
| Removed tab | TabRemoved | A user removes a tab from a channel. |
| Responded to approval | RespondedToApproval | User took action on an approval request. |
| Responded to invitation for shared channel ^3^ | InviteeResponded | A user responded to a shared channel invitation. |
| Responded to invitee response to shared channel ^3^ | ChannelOwnerResponded | A channel owner responded to a response from a user who responded to a shared channel invitation. |
| Responded with custom response | RespondedWithCustomResponse | User responded with a custom response text to an approval request. |
| Restored sharing of team channel ^3^ | SharingRestored | A team or channel owner re-enabled sharing for a shared channel. |
| Retrieved messages ^1^ | MessagesListed | Messages from a chat or channel were retrieved. |
| Sensitive content shared | SensitiveContentShared | Logged when **Detect sensitive content during screen sharing** meeting option is enabled for a Teams meeting and within that meeting there's sensitive content (for example, credit card numbers, bank account numbers, social security numbers and similar identification numbers) displayed on screen during a screen sharing session. For more information, see [Manage whether meetings in your organization can detect sensitive content during screen sharing](/en-us/microsoftteams/detect-sensitive-content). |
| Sent a message with a URL link in Teams | MessageCreatedHasLink | A user sends a message containing a URL link in Teams. |
| Sent change notification for message creation ^1^ | MessageCreatedNotification | A change notification was sent to notify a subscribed listener application of a new message. |
| Sent change notification for message deletion ^1^ | MessageDeletedNotification | A change notification was sent to notify a subscribed listener application of a deleted message. |
| Sent change notification for message update ^1^ | MessageUpdatedNotification | A change notification was sent to notify a subscribed listener application of an updated message. |
| Sent invitation for shared channel ^3^ | InviteSent | A channel owner or member sends an invitation to a shared channel. Invitations to shared channels can be sent to people outside of your organization if the channel policy is configured to share the channel with external users. |
| Submit update | SubmitUpdate | User submitted a new update. |
| Subscribed to message change notifications ^1^ | SubscribedToMessages | A subscription was created by a listener application to receive change notifications for messages. |
| Security Risk detected in a Teams call | SecurityRiskInCallDetected | An external Teams call is detected to have potential security concern such as impersonation |
| Teams Admin Action | TeamsAdminAction | Logged when a Teams admin performs actions like updating, adding, or deleting Teams related settings or configurations using admin tools like PowerShell, Admin Center, API, etc. |
| Thread creation probed | CreateThreadProbe | A user probed whether they can create a chat with users in your organization. The following properties are populated for each of these activities:**Activity**: The name of this activity, CreateThreadProbe.**CorrelationId**: Unique request identifier for the audit log.**CreationTime**: The time at which the audit log was created.ExtraProperties\*\*: Contains a single key-value pair that describes the environment where the probe request initiated.**ID**: The ID of the report entry. The ID uniquely identifies the audit log entry.**OrganizationId**: The GUID for your Microsoft 365 organization.**ParticipantInfo**: Contains a list of objectId and tenantId pairs describing the set of target users against which the initiating user (UserKey user) initiated the probe. In other words, these are the set of users with which the initiating user wants to create a thread. Only contains users from your organization.**RecordType**: The type of operation indicated by the record.**UserID**: The user principal name of the user that initiated the probe.**UserKey**: GUID of the user that initiated the probe.**UserSIPDomain**: The SIP domain of the user that initiated the probe.**UserTenantId**:The tenant of the user that initiated the probe.**UserType**: The type of the user that initiated the probe. Only takes on the value 0, which represents a regular AAD user.**Version**: The version number of the activity (identified by the Operation property) that's logged.**Workload**: The service where the activity occurred. |
| Unblock User | UserUnblocked | Unblock a user that was previously blocked. |
| Undeleted a message | GraphMessageUndeleted | A message in a chat or channel was deleted. |
| Uninstalled app | AppUninstalled | An app was uninstalled. |
| Update Teams Message | GraphMessageUpdated | Occurs when a user edits an existing chat message. |
| Updated a chat ^1^ | ChatUpdated | A Teams chat was updated. |
| Updated a message ^1^ | MessageUpdated | A message of a chat or channel was updated. |
| Updated app | AppUpdatedInCatalog | An app was updated in the catalog. |
| Updated approval request asynchronously | UpdatedApprovalRequestAsync | User took action on an approval request asynchronously. |
| Updated connector | ConnectorUpdated | A user modified a connector in a channel. |
| Updated tab | TabUpdated | A user modified a tab in a channel. |
| Upgraded app | AppUpgraded | An app was upgraded to its latest version in the catalog. |
| User signed in to Teams | TeamsSessionStarted | A user signs in to a Microsoft Teams client. This event doesn't capture token refresh activities. |
| View approval request | ViewApprovalRequest | User makes a request to view an approval request. |
| View update | ViewUpdate | User views the details of the update. |
| Viewed approval request | ViewedApprovalRequest | User views the details of the approval request from either the adaptive card or within the app. |
| Viewed approval with additional field | ViewedApprovalWithAdditionalField | User views the details of the approval request that contains at least one editable text field. |
| Viewed approval with group request | ViewedApprovalWithGroupRequest | User views the details of the approval request with a group included. |

Note

^1^ An audit record for this event is only logged when the operation is performed by calling a Microsoft Graph API. If the operation is performed in the Teams client, an audit record isn't logged.^2^ This event is only available in Audit (Premium). That means users must be assigned the appropriate license before these events are logged in the audit log. For more information about activities only available in Audit (Premium), see [Audit (Premium) in Microsoft Purview](audit-solutions-overview#audit-premium). For Audit (Premium) licensing requirements, see [Auditing solutions in Microsoft 365](audit-solutions-overview#licensing-requirements). ^3^ This event is in public preview. ^4^This event is generated for chat only if there are guests, federated and/or anonymous users.^5^ This event is currently unavailable in Government Community Cloud (GCC), Government Community Cloud High (GCC-High), and Department of Defense (DoD) organizations. ^6^ This event is included in all participating tenants for federated chats. ^7^ This event has participating domain info for 1:1 federated chats. ^8^ This event is included in all chat conversations between external Teams users managed by an organization and external Teams users not managed by an organization. ^9^ This event is currently available in Government Community Cloud (GCC), Government Community Cloud High (GCC-High), Department of Defense (DoD) organizations and air-gapped environments. ^10^ This event is included in all participating tenants. ^11^ An audit record isn't logged for activities with Agents or Bots. This capability is currently in development. ^12^ Calls that are recorded or transcribed are included in MeetingParticipantDetail. ^13^ This event is logged by Graph API access and not by Teams client. ^14^ This event is now shared with all participating tenants, not just the organizer tenant. Participating tenants will receive Meeting Participant Detail audit records for their own users who attended a Teams meeting organized by another tenant. 

## Teams Evaluation Data Hub activities

The following table lists activities for Teams Evaluation Data Hub recorded in the Microsoft 365 audit log. Teams Evaluation Data Hub provides storage and data-access capabilities for conversational data sets (for example, meetings, chats, and Q&A logs) used to evaluate Microsoft Teams experiences. The audit log records when users or services read or write data sets in the hub and when access permissions on a data set are granted or revoked.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Granted access permission | PermissionGranted | A user or service was granted access permission to a Teams Evaluation Data Hub data set or data asset. |
| Read data from storage | DataRead | A user or service read, browsed, or downloaded data from Teams Evaluation Data Hub storage. |
| Revoked access permission | PermissionRevoked | A user or service had access permission revoked for a Teams Evaluation Data Hub data set or data asset. |
| Wrote data to storage | DataWrite | Data in Teams Evaluation Data Hub storage was created, updated, overwritten, or deleted by a user or service. |

## Teams Healthcare activities

If your organization uses the [Patients application](/en-us/MicrosoftTeams/expand-teams-across-your-org/healthcare/patients-app-overview) in Microsoft Teams, you can search the audit log for activities related to the Patients app. If your environment is configured to support the Patients app, an additional activity group for these activities is available in the **Activities** picker list.

![Microsoft Teams Healthcare activities in Activities picker list.](media/teamshealthcareauditactivities.png)

For a description of the Patients app activities, see [Audit logs for Patients app](/en-us/MicrosoftTeams/expand-teams-across-your-org/healthcare/patients-audit).

## Teams Shifts activities

The following table lists Shift app in Microsoft Teams activities recorded in the Microsoft 365 audit log. If your organization uses the Shifts app in Microsoft Teams, you can search the audit log for activities related to the Shifts app. If your environment is configured to support Shifts apps, the **Activities** picker list includes an additional activity group for these activities.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Accepted off shift message | OffShiftDialogAccepted | A user acknowledged the off-shift message to access Teams after shift hours. |
| Added open shift | OpenShiftAdded | A user added an open shift to a scheduling group. |
| Added scheduling group | ScheduleGroupAdded | A user added a new scheduling group to the schedule. |
| Added shift | ShiftAdded | A user added a shift. |
| Added shift request | RequestAdded | A user added a shift request. |
| Added Time clock entry | TimeClockEntryAdded | A user added a new manual Time clock entry on Time Sheet. |
| Added time off | TimeOffAdded | A user added time off on the schedule. |
| Added workforce integration | WorkforceIntegrationAdded | The Shifts app is integrated with a third-party system. |
| Canceled shift request | RequestCancelled | A user canceled a shift request. |
| Changed schedule setting | ScheduleSettingChanged | A user changed a setting in Shifts settings. |
| Clocked in using Time clock | ClockedIn | A user clocked in using Time clock. |
| Clocked out using Time clock | ClockedOut | A user clocked out using Time clock. |
| Deleted open shift | OpenShiftDeleted | A user deleted an open shift from a scheduling group. |
| Deleted scheduling group | ScheduleGroupDeleted | A user deleted a scheduling group from the schedule. |
| Deleted shift | ShiftDeleted | A user deleted a shift. |
| Deleted Time clock entry | TimeClockEntryDeleted | A user deleted a Time clock entry on Time Sheet. |
| Deleted time off | TimeOffDeleted | A user deleted time off. |
| Edited open shift | OpenShiftEdited | A user edited an open shift in a scheduling group. |
| Edited scheduling group | ScheduleGroupEdited | A user edited a scheduling group. |
| Edited shift | ShiftEdited | A user edited a shift. |
| Edited Time clock entry | TimeClockEntryEdited | A user edited a Time clock entry on Time Sheet. |
| Edited time off | TimeOffEdited | A user edited time off. |
| Ended break using Time clock | BreakEnded | A user ended a break during an active Time clock session. |
| Responded to shift request | RequestRespondedTo | A user responded to a shift request. |
| Shared schedule | ScheduleShared | A user shared a team schedule for a date range. |
| Started break using Time clock | BreakStarted | A user started a break during an active Time clock session. |
| Withdrew schedule | ScheduleWithdrawn | A user withdrew a published schedule. |

## Teams Updates activities

The following table lists activities for the Updates app in Microsoft Teams recorded in the Microsoft 365 audit log. If your organization uses the Updates app in Microsoft Teams, you can search the audit log for activities related to the Updates app. If your environment is configured to support Updates apps, the **Activities** picker list includes an additional activity group for these activities.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Create an update request | CreateUpdateRequest | A user created an update request. |
| Edit an update request | EditUpdateRequest | A user opens the request editing workflow and selects **Save** to confirm and save any changes, or enables or disables the update request directly. |
| Submit an update | SubmitUpdate | A user submitted an update. |
| View the details of one update | ViewUpdate | A user views the details of the update. |

## Teams User Concern activities

The following table lists user concern activities in Microsoft Teams recorded in the Microsoft 365 audit log. These events are generated when a user reports a concern about a message, call, or another user in Microsoft Teams. For more information, see [End user reporting for Security](/en-us/microsoftteams/end-user-reporting-security).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Reported call in Teams | CallReported | A user reported a call as a concern in Microsoft Teams. |
| Reported message in Teams | MessageReported | A user reported a message as a concern in Microsoft Teams. |
| Reported user in Teams | UserReported | A user reported another user as a concern in Microsoft Teams. |

## Trainable Classifier activities

The following table lists the activities for [trainable classifiers](trainable-classifiers-learn-about) recorded in the Microsoft 365 audit log.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Created Purview Data Classification model | ModelCreate | A user (or admin or system on behalf of a user) created a new trainable model in Purview Data Classification. |
| Deleted Purview Data Classification model | ModelUpdate | A user (or admin or system on behalf of a user) updated a new trainable model in Purview Data Classification. |
| Published Purview Data Classification model | ModelPublish | A user (or admin or system on behalf of a user) published a new trainable model in Purview Data Classification. |
| Updated Purview Data Classification model | ModelDelete | A user (or admin or system on behalf of a user) deleted a new trainable model in Purview Data Classification. |

## Universal Print management activities

The following table lists the activities recorded in the Microsoft 365 audit log when actions are performed on printers, connectors, printer shares, and tenant-level settings using the [Universal Print](/en-us/universal-print/discover-universal-print) service.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Added group access to printer share | ShareAccessControlGroupAdded | A group is granted access to a printer share. |
| Added member to pull-print printer | PullPrintPrinterMemberAdded | A member is added to a pull-print printer group for access control. |
| Added user access to printer share | ShareAccessControlUserAdded | A user is granted access to a printer share. |
| Created printer share | ShareCreated | A printer share is created, allowing multiple users to access the printer. |
| Created pull-print printer | PullPrintPrinterCreated | A pull-print virtual printer is created for secure print release. |
| Deleted printer share | ShareDeleted | A printer share is deleted, removing shared access. |
| Deleted pull-print printer | PullPrintPrinterDeleted | A pull-print virtual printer is deleted from Universal Print. |
| Disabled allow-all access for printer share | ShareAccessControlAllowAllDisabled | Universal access to the printer share is disabled. |
| Disabled include-all-printers | PullPrintPrinterIncludeAllPrintersDisabled | All printers are excluded from the pull-print configuration. |
| Downloaded report | ReportDownloaded | A report is downloaded from Universal Print for analysis or auditing. |
| Enabled allow-all access for printer share | ShareAccessControlAllowAllEnabled | All users are allowed access to the printer share. |
| Enabled include-all-printers | PullPrintPrinterIncludeAllPrintersEnabled | All printers are included in the pull-print configuration. |
| Modified printer settings | PrinterSettingsModified | Printer configuration settings are updated in Universal Print. |
| Modified printer share settings | ShareSettingsModified | Settings for a printer share are updated in Universal Print. |
| Modified pull-print printer settings | PullPrintPrinterSettingsModified | Settings for a pull-print printer are updated in Universal Print. |
| Modified tenant print settings | TenantPrintSettingsModified | Tenant-level print settings are updated in Universal Print. |
| Registered connector | ConnectorRegistered | The connector is registered with Universal Print, enabling communication between printers and the cloud service. |
| Registered printer | PrinterRegistered | A printer is registered with Universal Print, making it available for cloud-based printing. |
| Removed group access from printer share | ShareAccessControlGroupRemoved | A group’s access to a printer share is removed. |
| Removed member from pull-print printer | PullPrintPrinterMemberRemoved | A member is removed from a pull-print printer group. |
| Removed user access from printer share | ShareAccessControlUserRemoved | A user’s access to a printer share is removed. |
| Swapped printer | PrinterSwapped | A printer is replaced or swapped with another device in Universal Print. |
| Unregistered connector | ConnectorUnregistered | The connector is unregistered from Universal Print, removing its ability to manage printers. |
| Unregistered printer | PrinterUnregistered | A printer is removed from Universal Print, making it unavailable for cloud-based printing. |

## Universal Print print job activities

The following table lists the activities recorded in the Microsoft 365 audit log when actions are performed on print jobs using the [Universal Print](/en-us/universal-print/discover-universal-print) service.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Aborted print job | PrintJobAborted | The print job is terminated unexpectedly due to an error or interruption. |
| Acknowledged print job | PrintJobAcknowledged | The print job is acknowledged by the printer, indicating that the printer has received and is ready to process the print job. |
| Canceled print job | PrintJobCanceled | The print job is canceled by the user or system before completion. |
| Completed print job | PrintJobCompleted | The print job finishes successfully, and all pages are printed. |
| Fetched print job document | PrintJobDocumentFetched | A print job document is retrieved by the printer or the Universal Print connector. |
| Submitted print job | PrintJobCreated | The print job is submitted to the print queue, indicating the start of the printing process. |
| Uploaded print job document | PrintJobDocumentUploaded | A print job document is successfully uploaded to Universal Print. |

## User administration activities

The following table lists user administration activities recorded in the Microsoft 365 audit log when an admin adds or changes a user account by using the [Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=2024339) or the Azure management portal.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Added user | Add user. | A user account is created. |
| Changed user license | Change user license. | The license assigned to a user changed. To see what licenses were changed, see the corresponding **Updated user** activity. |
| Changed user password | Change user password. | A user changes their password. Self-service password reset has to be enabled (for all or selected users) in your organization to allow users to reset their password. You can also track self-service password reset activity in Microsoft Entra ID. For more information, see [Reporting options for Microsoft Entra password management](/en-us/azure/active-directory/authentication/howto-sspr-reporting). |
| Deleted user | Delete user. | A user account was deleted. |
| Reset user password | Reset user password. | Administrator resets the password for a user. |
| Set license properties | Set license properties. | Administrator modified the properties of a license assigned to a user. |
| Set property that forces user to change password | Set force change user password. | Administrator set the property that forces a user to change their password the next time the user signs in to Microsoft 365. |
| Updated user | Update user. | Administrator changes one or more properties of a user account. For a list of the user properties that can be updated, see the "Update user attributes" section in [Microsoft Entra audit Report Events](/en-us/azure/active-directory/reports-monitoring/concept-audit-logs). |

## Viva Engage activities

The following table lists the user and admin activities in Viva Engage recorded in the Microsoft 365 audit log. To return Viva Engage-related activities from the audit log, select **Show results for all activities** in the **Activities** list. Use the date range boxes and the **Users** list to narrow the search results.

Note

Some Viva Engage audit activities are only available in Audit (Premium). That means users must be assigned the appropriate license before these activities are logged in the audit log. For more information, see [Audit (Premium)](audit-solutions-overview#audit-premium). For Audit (Premium) licensing requirements, see [Auditing solutions in Microsoft 365](audit-solutions-overview#licensing-requirements). In the following table, Audit (Premium) activities are highlighted with an asterisk (\*).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Added corporate communicator | AddUserRole | A user is assigned as a corporate communicator. |
| Changed custom usage policy | UsagePolicyUpdated | A tenant admin updates a custom usage policy. |
| Changed data retention policy | SoftDeleteSettingsUpdated | Verified admin updates the setting for the network data retention policy to either Hard Delete or Soft Delete. Only verified admins can perform this operation. |
| Changed network configuration | NetworkConfigurationUpdated | Network or verified admin changes the Viva Engage network's configuration. This change includes setting the interval for exporting data and enabling chat. |
| Changed network profile settings | ProcessProfileFields | Network or verified admin changes the information that appears on member profiles for network users network. |
| Changed private content mode | SupervisorAdminToggled | Verified admin turns *Private Content Mode* on or off. This mode lets an admin view the posts in private groups and view private messages between individual users (or groups of users). Only verified admins only can perform this operation. |
| Changed security configuration | NetworkSecurityConfigurationUpdated | Verified admin updates the Viva Engage network's security configuration. This update includes setting password expiration policies and restrictions on IP addresses. Only verified admins can perform this operation. |
| Conversation closed | CloseConversation | The Viva Engage thread was closed, preventing users from replying to it. This action is available to an admin, corporate communicator, or a user delegate. |
| Conversation opened | OpenConversation | The Viva Engage thread conversation was opened which allows users to reply to the thread. This action is available to an admin, corporate communications, or a user delegate. |
| Create a segment | SegmentCreated | Admin creates a segmentation. |
| Created file | FileCreated | User uploads a file. |
| Created group | GroupCreation | User creates a group. |
| Created message | MessageCreation | User creates a message. |
| Delete a segment | SegmentDeleted | Admin deletes a segmentation. |
| Deleted group | GroupDeletion | A group is deleted from Viva Engage. |
| Deleted message | MessageDeleted | User deletes a message. |
| Download segmentation admin reports | SegmentationReportDownloaded | Admin reports are downloaded. |
| Downloaded file | FileDownloaded | User downloads a file. |
| Event content exported | EventContentExported | Event organizer exports event questions, replies, reaction, and upvote count to a CSV. This action is available to event organizer, co-organizers only. Network admin can toggle this feature off for the entire network in the Engage admin settings. |
| Event moderation enabled | EventModerationEnabled | Event organizer enabled moderation for an event. This action is available to event organizers only. |
| Exported data | DataExport | Verified admin exports Viva Engage network data. Only verified admins can perform this operation. |
| Failed to access file | FileAccessFailure | User failed to access a file. |
| Failed to access group | GroupAccessFailure | User failed to access a group. |
| Failed to access thread | ThreadAccessFailure | User failed to access a message thread. |
| Generate segmentation admin reports | SegmentationReportGenerated | Admin user triggers a report generation. |
| Reacted to message | MarkedMessageChanged | User reacted to a message. |
| Remove curated topic\* | RemoveCuratedTopic | User removes a curated topic. |
| Removed Corporate Communicator | RemoveUserRole | A user is removed from the Corporate Communicator role. |
| Shared file | FileShared | User shares a file with another user. |
| Suspended network user | NetworkUserSuspended | Network or verified admin suspends (deactivates) a user from Viva Engage. |
| Suspended user | UserSuspension | User account is suspended (deactivated). |
| Tenant Usage Policy Acceptance | UsagePolicyAcceptance | A user accepts an organization-specific usage policy. |
| Thread Muted | AdminThreadMuted | A thread was muted by admin or watch alert (system user). A watch alert occurs when a thread is flagged for a certain theme (set by the admin) and is automuted by the system. |
| Thread Unmuted | AdminThreadUnmuted | Admin unmuted a thread. |
| Updated file description | FileUpdateDescription | User changes the description of a file. |
| Updated file name | FileUpdateName | User changes the name of a file. |
| Updated message | MessageUpdated | User updates a message. |
| Updated role assignment for Network Admin | NetworkAdminUpdated | A user is either promoted or demoted to the Network Admin role. |
| Updated role assignment for Verified Admin | NetworkVerifiedAdminUpdated | A user is either promoted or demoted to the Verified Admin role. |
| Viewed file | FileVisited | User views a file. |
| Viewed thread | ThreadViewed | User views a message thread. |
| Added Community Agent to a community | AgentAddedToCommunity | A community admin adds Community Agent to a community. |
| Updated Community Agent settings | AgentSettingsUpdated | A community admin updates Community Agent settings. |
| Removed Community Agent from a community | AgentRemovedFromCommunity | A community admin removes Community Agent from a community. |
| Added Community Agent grounding source | AgentGroundingSourceAdded | A community admin adds a SharePoint or web grounding source to Community Agent. |
| Granted Community Agent access to a grounding source | AgentGroundingSourceAccessGranted | A community admin grants Community Agent access to a SharePoint grounding source. |
| Removed Community Agent grounding source | AgentGroundingSourceRemoved | A community admin removes a SharePoint or web grounding source from Community Agent. |
| Approved Community Agent suggested answer | SuggestedAnswerApproved | A community admin or community expert approves an answer suggested by Community Agent without editing it. |
| Edited and approved Community Agent suggested answer | SuggestedAnswerEditedAndApproved | A community admin or community expert edits an answer suggested by Community Agent and then approves it. |
| Dismissed Community Agent suggested answer | SuggestedAnswerDismissed | A community admin or community expert dismisses an answer suggested by Community Agent. |

## Viva Glint activities

The following table lists the user and admin activities in Viva Glint that the Microsoft 365 audit log records. The table includes the friendly name that's displayed in the **Activities** column and the name of the corresponding operation that appears in the detailed information of an audit record and in the .csv file when you export the search results.

[Search the audit log](audit-search) explains how you can search for audit logs from the Microsoft Purview portal. To access audit logs, you need to be a global admin or have audit read permissions. Use the *Activities* filter to search for specific activities and to list all Viva Glint activities by choosing *VivaGlint* in the *Record type* filter. Use the date range boxes and the *Users* list to narrow the search results further.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Added agentic policy | PolicyAdded | An agentic policy was added. |
| Added Company Admin | AddCompanyAdmin | A user was added to the Company Admin role. |
| Added Support User | AddSupportUser | A user was added to the Support User role. |
| Assigned User Role | AssignRole | A user is assigned to a new role. |
| Changed Client Details | ClientDetailsChanged | Change activity in Viva Glint General Settings or Advanced Configuration: Details. |
| Company Admin Logged In | AdminLogin | A Company Admin user logged into Viva Glint. |
| Company Admin Logged Out | AdminLogout | A Company Admin user logged out of Viva Glint. |
| Completed agentic campaign | CampaignCompleted | An agentic campaign was completed. |
| Created agentic campaign | CampaignCreated | An agentic campaign was created. |
| Created User Role | RoleCreated | Glint User Role creation activity. |
| Deleted agentic campaign | CampaignDeleted | An agentic campaign was deleted. |
| Deleted agentic policy | PolicyDeleted | An agentic policy was deleted. |
| Deleted retained agentic campaign data | CampaignRetentionDeleted | Retained agentic campaign data was deleted. |
| Deleted Support Access | GlintSupportAccessDeleted | A user was removed from the Support User role. |
| Deleted System | GlintSystemDeleted | The Viva Glint system was deleted. |
| Deleted tenant data for a DSR request | DsrTenantDeleted | Tenant data was deleted for a data subject rights (DSR) request. |
| Deleted User | GlintUserDeleted | Viva Glint user deletion activity. |
| Deleted user data for a DSR request | DsrUserDeleted | User data was deleted for a data subject rights (DSR) request. |
| Disabled Advanced Configuration Access | UserAdvConfigDisabled | A Company Admin user disabled Advanced Configuration access in Viva Glint. |
| Disabled Glint to Insights integration | GlintToInsightsIntegrationDisabled | A user disabled importing Viva Insights data in Viva Glint |
| Enabled Advanced Configuration Access | UserAdvConfigEnabled | A Company Admin user enabled Advanced Configuration access in Viva Glint. |
| Enabled Glint to Insights integration | GlintToInsightsIntegrationEnabled | A user enabled importing Viva Insights data in Viva Glint |
| Executed Data Apps Job | GlintDataAppsJobRun | Viva Glint Advanced Configuration Data app and Upload activity. |
| Exported agentic campaign policy violations | VivaGlintAgenticPolicyViolationsExported | Agentic campaign policy violations export activity. |
| Exported agentic campaign topic analysis | VivaGlintAgenticTopicAnalysisExported | Agentic campaign topic analysis export activity. |
| Exported all agentic campaign data | VivaGlintAgenticAllDataExported | Agentic campaign raw data export activity. |
| Exported Glint 360 Feedback | GlintFeedbackProgramExport | Viva Glint 360 feedback program data export activity. |
| Exported Glint Distribution Lists | GlintUserGroupExport | Distribution List export activity. |
| Exported Glint People | GlintUserExport | Glint People data export activity. |
| Exported Glint Pulse Program Response Rate | GlintPulseProgramRespondentRateExport | Glint pulse program response rate export activity. |
| Exported Glint Question Library | GlintQuestionExport | Glint question library export activity. |
| Exported Glint Survey Program | GlintPulseProgramExport | Glint survey program content export activity. |
| Exported Glint User Role | GlintRoleExport | Glint User Role data export activity. |
| Exported Raw Survey Data | RawSurveyReponseExport | Raw survey response data export activity. |
| Exported User Data | UserDataExport | Employee data export activity. |
| Generated agentic campaign report | ReportGenerated | An agentic campaign report was generated. |
| Imported Glint 360 Feedback | GlintFeedbackProgramImport | 360 Feedback program data import activity. |
| Imported Glint SFTP | GlintRubiconImport | Employee data SFTP import activity. |
| Imported Glint User Data | GlintUserImport | Employee data import activity. |
| Imported Glint User Role | GlintRoleImport | User Role employee data activity. |
| Launched agentic campaign | CampaignLaunched | An agentic campaign was launched. |
| Removed Company Admin | RemoveCompanyAdmin | A user was removed from the Company Admin role. |
| Reopened Survey | SurveyReopen | A closed Viva Glint survey was reopened. |
| Reordered agentic policy priorities | PolicyPrioritiesReordered | Agentic policy priorities were reordered. |
| Set Data DSR Control | DataDsrControlSet | User Data controls for survey data deletion in General Settings update activity. |
| Set Discarding Employee IDs | DiscardingEmployeeIdsSet | User Data controls for Employee ID reuse in General Settings update activity. |
| Shared agentic campaign report | ReportShared | An agentic campaign report was shared. |
| Unassigned User Role | UnassignRole | A user is removed from a role. |
| Updated agentic campaign | CampaignUpdated | An agentic campaign was updated. |
| Updated agentic policy | PolicyUpdated | An agentic policy was updated. |
| Updated agentic settings | AgenticSettingsUpdated | Agentic settings were updated. |
| Updated Glint to Insights integration | GlintToInsightsIntegrationUpdated | A user updated the configuration for importing Viva Insights data in Viva Glint |
| Viewed As | ViewAs | Admins' "View As" another user activity. |

## Viva Goals activities

The following table lists the user and admin activities in Viva Goals that the Microsoft 365 audit log records. The table includes the friendly name that displays in the **Activities** column and the name of the corresponding operation that appears in the detailed information of an audit record and in the CSV file when you export the search results.

[Search the audit log](audit-search) explains how you can search for audit logs from the Microsoft Purview portal. To access audit logs, you need to be a global admin or have audit read permissions. You can use the **Activities** filter to search for specific activities. To list all Viva Goals activities, select **VivaGoals** in the **Record type** filter. You can also use the date range boxes and the **Users** list to narrow the search results further.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Dashboard created | Dashboard created | User created a new dashboard on Viva Goals. |
| Dashboard deleted | Dashboard deleted | User deleted a dashboard on Viva Goals. |
| Dashboard updated | Dashboard updated | User updated a dashboard on Viva Goals. |
| Data exported | Data exported | A user exported list of OKRs or list of users in an organization on Viva Goals. |
| Goals policy updated | Goals policy updated | The global admin modified the policy or settings at organization level on Viva Goals. For example, the global admin configured who can create organizations on Viva Goals. |
| OKR or Project created | OKR or Project created | User created an OKR or Project on Viva Goals. |
| OKR or Project deleted | OKR or Project deleted | User deleted an OKR or Project. |
| OKR or Project updated | OKR or Project updated | An OKR/Project was modified or a check-in was made by the user or an integration on Viva Goals. |
| Organization created | Organization created | Admin or the user created a new organization on Viva Goals. |
| Organization integrations updated | Organization integrations updated | The user (typically Organization owners or admins) configured a third party integration or updated an existing third party integration for an organization on Viva Goals. |
| Organization settings updated | Organization settings updated | The user (typically Organization owners or admins) updated organization specific settings on Viva Goals. |
| Team added | Team added | A new team was created within an organization on Viva Goals. |
| Team deleted | Team deleted | A team within an organization on Viva Goals was deleted by the user. |
| Team updated | Team updated | A team within an organization on Viva Goals was modified or updated. |
| User added | User added | A new user was added to an organization on Viva Goals. |
| User deactivated | User deactivated | A user was deactivated in an organization. |
| User deleted | User deleted | A user was deleted from an organization on Viva Goals. |
| User logged in | User logged in | User signed in to Viva Goals. |

## Viva Insights activities

Viva Insights provides insight into how groups collaborate across your organization. The following table lists activities recorded in the Microsoft 365 audit log that users assigned the Administrator or Analyst roles in Viva Insights perform. Users assigned the Analyst role have full access to all service features and use the product to do analysis. Users assigned the Administrator role can configure privacy settings and system defaults, and can prepare, upload, and verify organizational data in Viva Insights. For more information, see [Introducing Microsoft Viva Insights](/en-us/viva/insights/introduction).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Accessed OData link | AccessedOdataLink | Analyst accessed the OData link for a query. |
| Added delegate access | AddDelegates | A user added delegate access for organization insights or Copilot dashboard. |
| Canceled query | CanceledQuery | Analyst canceled a running query. |
| Created meeting exclusion | MeetingExclusionCreated | Analyst created a meeting exclusion rule. |
| Deleted result | DeletedResult | Analyst deleted a query result. |
| Downloaded report | DownloadedReport | Analyst downloaded a query result file. |
| Executed query | ExecutedQuery | Analyst ran a query. |
| Modified CXO Settings | ModifiedCXOSettings | This event logs the assignment or removal of users/groups to access the Microsoft 365 Copilot Dashboard. |
| Modified Exclusion List Using Entra Group | ModifiedExclusionListUsingEntraGroup | This event logs changes to the exclusion list using the Entra group in the Copilot Dashboard. |
| Modified Minimum Group Size | ModifiedMinimumGroupSize | This event logs modifications to the organization's minimum group size for generating insights in the Copilot Dashboard and Viva Insights advanced analysis. |
| Removed delegate access | RemoveDelegates | A user removed delegate access for organization insights or Copilot dashboard. |
| Updated data access setting | UpdatedDataAccessSetting | Admin updated data access settings. |
| Uploaded organization data | UploadedOrgData | Admin uploaded organizational data file. |
| User logged in^\*^ | UserLoggedIn | A user signed in to their Microsoft 365 user account. |
| Viewed Explore | ViewedExplore | Analyst viewed visualizations in one or more Explore page tabs. |

Note

^\*^A Microsoft Entra sign-in activity event is created when a user signs in. This activity is logged even if you don't turn on Viva Insights in your organization. For more information about user sign in activities, see [Sign-in logs in Microsoft Entra ID](/en-us/azure/active-directory/reports-monitoring/concept-sign-ins).

## Viva Pulse activities

The following table lists the user and admin activities in Viva Pulse recorded in the Microsoft 365 audit log. The table includes the friendly name that's displayed in the **Activities** column and the name of the corresponding operation that appears in the detailed information of an audit record and in the CSV file when you export the search results.

[Search the audit log](audit-search) explains how you can search for audit logs from the Microsoft Purview portal. To access audit logs, you need to be a global admin or have audit read permissions. You can use the **Activities** filter to search for specific activities. To list all Viva Pulse activities, select *VivaPulse* in the **Record type** filter. You can also use the date range boxes and the **Users** list to narrow the search results further.

Important

Microsoft recommends that you use roles with the fewest permissions. Minimizing the number of users with the Global Administrator role helps improve security for your organization. Learn more about Microsoft Purview [roles and permissions](purview-permissions).

| Friendly name | Operation | Description |
| --- | --- | --- |
| Admin deleted a user's data | PulseDeleteUserData | Admin deleted a user's data. |
| Admin updated tenant's settings | PulseTenantSettingsUpdate | Admin updated an organization setting for Viva Pulse. |
| Confidential conversation started | PulseConfidentialConversationStarted | Author started a confidential conversation. |
| Conversation message deleted | PulseConfidentialConversationMessageDeleted | User deleted a conversation message. |
| Conversation response added | PulseConfidentialConversationResponded | Author or recipient responded on a conversation. |
| User canceled a Pulse survey | PulseCancel | User canceled a Pulse survey. |
| User created a Pulse draft | PulseCreateDraft | User created a Pulse draft. |
| User created a Pulse survey | PulseCreate | New Viva Pulse feedback request is created. |
| User deleted a Pulse draft | PulseDeleteDraft | User deleted a Pulse draft. |
| User deleted a question for Library | PulseQuestionDeleted | User removed a question for pulse question library. |
| User extended their pulse survey deadline | PulseExtendDeadline | User extended the deadline for the existing Viva Pulse feedback request. |
| User invited additional users to Pulse survey | PulseInvite | User invited additional users to an existing Viva Pulse feedback request. |
| User request a pulse data export | PulseDataExport | Admin or Author request a pulse export operation. |
| User shared a pulse report | PulseShareResults | User shared Viva Pulse feedback results with other users. |
| User submitted response to a pulse survey | PulseSubmit | Admin or user provided feedback for a Viva Pulse feedback request. |

## Windows 365 Customer Lockbox activities

The following table lists the user and admin activities in Windows 365 Customer Lockbox that the Microsoft 365 audit log records. To return Windows 365 Customer Lockbox-related activities from the audit log, select **Windows365CustomerLockbox** under **Record types**. Use the date range boxes and the **Users** list to narrow the search results.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Backfill CMD Agent | AddDevicesToBackfill Operation | Backfill CMD Agent on Cloud PC. |
| Bulk reinstall CMD Agent | TriggerClientAgentCheckBulkAction Operation | Bulk reinstall CMD agent on demand. |
| Check PowerShell Execution Policy | Check PowerShell Execution Policy | Check PowerShell execution policy. |
| Create LogCollection Request | Create LogCollection Request | Create log collection request to Cloud PC. |
| Create new work items (Scheduler) | Create new work items (Scheduler) | Create new work items, such as Provision, Deprovision, Reprovision, and others. |
| Create Remote Action Operation in ActionModeratorService | Create Remote Action Operation in ActionModeratorService | Create remote action by tenantID, workspaceID, actionType, actionParameters. |
| Create VmExtension Request | Create VmExtention Request | Creates VM extension requests to execute VM extension to run custom scripts on the customer device. |
| Execute AppHealthPlugin | Execute AppHealthPlugin | Execute AppHealthPlugin. |
| Install RD agent | Install RD agent | Install RD agent on the device of the user. |
| OCE Run Commands on VM | OCE Run Commands on VM | Run commands by tenantID, deviceID list, and script. |
| Post Remote Action Operation | Post Remote Action Operation | Post Remote Action, plus polling the result by GetActions operation. |
| Reinstall CMD Agent | AddDevicesToReinstall Operation | Reinstall CMD Agent on demand. |
| Run hybrid AADJ extension | Run hybrid AADJ extension | Run hybrid AADJ extension on the device of the user. |
| Trigger CMD Agent Canary check. | Trigger CMD Agent Canary check. | Trigger CMD Agent Canary check on specific device. |
| Trigger device remediation | Trigger device remediation | Trigger device remediation. |
| Trigger generic action | Trigger generic action | Trigger device action for user. |
| Trigger generic action by SaaF | Trigger generic action by SaaF | Trigger device action (Retargeting, EnableRdpAccessForCitrix, DisableRdpAccessFprCitrix) for user. |
| Trigger generic action with options | Trigger generic action with options | Trigger device action with option parameters, more powerful than that of trigger generic action. |
| Trigger orchestrator | Trigger orchestrator | Trigger orchestrator for the user. |
| Upload folder to blob | Upload folder to blob | Compress and upload customer device's folder to blob. |

## Fabric Workspace Inbound External Data Share setting

The following table lists the Fabric admin activities for enabling and disabling the Workspace Inbound External Data Share setting.

| Friendly name | Operation | Description |
| --- | --- | --- |
| Enabled external data shares bypass on the workspace | ExternalDataSharesBypassForWorkspaceEnabled | Admin allowed External Data Shares to access data in workspaces where inbound public network access is restricted. |
| Disabled external data shares bypass on the workspace | ExternalDataSharesBypassForWorkspaceDisabled | Admin blocked External Data Shares from accessing data in workspaces where inbound public network access is restricted. |