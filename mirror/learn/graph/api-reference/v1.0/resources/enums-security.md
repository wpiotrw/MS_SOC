---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: Security enum values - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/enums-security?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: BenAlfasi
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Microsoft Graph security subnamespace enumeration values
doc_type: enumPageType
ms.localizationpriority: medium
ms.date: 2026-01-08T00:00:00.0000000Z
locale: en-us
document_id: 6a2a4444-1c63-7730-e23f-6b2b019ac1ae
document_version_independent_id: 9e0bae80-7b72-ef99-e370-86cf2ccefe02
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/enums-security.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/enums-security
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/enums-security.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 339ade5f-2dd6-dae8-2ea1-2c616abd5e34
---

# Security enum values - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.security

### appInfoCsaStarLevel values

| Member |
| --- |
| selfAssessment |
| certification |
| attestation |
| cStarAssessment |
| continuousMonitoring |
| unknown |
| unknownFutureValue |

### appInfoDataAtRestEncryptionMethod values

| Member |
| --- |
| aes |
| bitLocker |
| blowfish |
| des3 |
| des |
| rc4 |
| rsA |
| notSupported |
| unknown |
| unknownFutureValue |

### appInfoDataRetentionPolicy values

| Member |
| --- |
| dataRetained |
| deletedImmediately |
| deletedWithinTwoWeeks |
| deletedWithinOneMonth |
| deletedWithinThreeMonths |
| deletedWithinMoreThanThreeMonths |
| unknown |
| unknownFutureValue |

### appInfoFedRampLevel values

| Member |
| --- |
| high |
| moderate |
| low |
| liSaaS |
| unknown |
| unknownFutureValue |
| notSupported |

### appInfoHolding values

| Member |
| --- |
| private |
| public |
| unknown |
| unknownFutureValue |

### appInfoPciDssVersion values

| Member |
| --- |
| v1 |
| v2 |
| v3 |
| v3\_1 |
| v3\_2 |
| v3\_2\_1 |
| notSupported |
| unknown |
| unknownFutureValue |
| v4 |

### appInfoEncryptionProtocol values

| Member |
| --- |
| tls1\_0 |
| tls1\_1 |
| tls1\_2 |
| tls1\_3 |
| notApplicable |
| notSupported |
| unknown |
| unknownFutureValue |
| ssl3 |

### appInfoUploadedDataTypes values

| Member |
| --- |
| documents |
| mediaFiles |
| codingFiles |
| creditCards |
| databaseFiles |
| none |
| unknown |
| unknownFutureValue |

### cloudAppInfoState values

| Member |
| --- |
| true |
| false |
| unknown |
| unknownFutureValue |

### entityType values

| Member |
| --- |
| userName |
| ipAddress |
| machineName |
| other |
| unknown |
| unknownFutureValue |

### mailboxConfigurationType values

| Member |
| --- |
| mailForwardingRule |
| owaSettings |
| ewsSettings |
| mailDelegation |
| userInboxRule |
| unknownFutureValue |

### logDataProvider values

| Member |
| --- |
| barracuda |
| bluecoat |
| checkpoint |
| ciscoAsa |
| ciscoIronportProxy |
| fortigate |
| paloAlto |
| squid |
| zscaler |
| mcafeeSwg |
| ciscoScanSafe |
| juniperSrx |
| sophosSg |
| websenseV75 |
| websenseSiemCef |
| machineZoneMeraki |
| squidNative |
| ciscoFwsm |
| microsoftIsaW3C |
| sonicwall |
| sophosCyberoam |
| clavister |
| customParser |
| juniperSsg |
| zscalerQradar |
| juniperSrxSd |
| juniperSrxWelf |
| microsoftConditionalAppAccess |
| ciscoAsaFirepower |
| genericCef |
| genericLeef |
| genericW3C |
| iFilter |
| checkpointXml |
| checkpointSmartViewTracker |
| barracudaNextGenFw |
| barracudaNextGenFwWeblog |
| microsoftDefenderForEndpoint |
| zscalerCef |
| sophosXg |
| iboss |
| forcepoint |
| fortios |
| ciscoIronportWsaIi |
| paloAltoLeef |
| forcepointLeef |
| stormshield |
| contentkeeper |
| ciscoIronportWsaIii |
| checkpointCef |
| corrata |
| ciscoFirepowerV6 |
| menloSecurityCef |
| watchguardXtm |
| openSystemsSecureWebGateway |
| wandera |
| unknownFutureValue |

### receiverProtocol values

| Member |
| --- |
| ftp |
| ftps |
| syslogUdp |
| syslogTcp |
| syslogTls |
| unknownFutureValue |

### trafficType values

| Member |
| --- |
| downloadedBytes |
| uploadedBytes |
| unknown |
| unknownFutureValue |

### auditLogQueryStatus values

| Member |
| --- |
| notStarted |
| running |
| succeeded |
| failed |
| cancelled |
| unknownFutureValue |

### auditLogUserType values

| Member |
| --- |
| regular |
| reserved |
| admin |
| dcAdmin |
| system |
| application |
| servicePrincipal |
| customPolicy |
| systemPolicy |
| partnerTechnician |
| guest |
| unknownFutureValue |

### actionAfterRetentionPeriod values

| Member |
| --- |
| none |
| delete |
| startDispositionReview |
| unknownFutureValue |

### behaviorDuringRetentionPeriod values

| Member |
| --- |
| doNotRetain |
| retain |
| retainAsRecord |
| retainAsRegulatoryRecord |
| unknownFutureValue |

### contentFormat values

| Member |
| --- |
| text |
| html |
| markdown |
| unknownFutureValue |

### defaultRecordBehavior values

| Member |
| --- |
| startLocked |
| startUnlocked |
| unknownFutureValue |

### detectionStatus values

| Member |
| --- |
| detected |
| blocked |
| prevented |
| unknownFutureValue |

### eventPropagationStatus values

| Member |
| --- |
| none |
| inProcessing |
| failed |
| success |
| unknownFutureValue |

### eventStatusType values

| Member |
| --- |
| pending |
| error |
| success |
| notAvaliable |
| unknownFutureValue |

### hostPortProtocol values

| Member |
| --- |
| tcp |
| udp |
| unknownFutureValue |

### hostPortStatus values

| Member |
| --- |
| open |
| filtered |
| closed |
| unknownFutureValue |

### hostReputationClassification values

| Member |
| --- |
| unknown |
| neutral |
| suspicious |
| malicious |
| unknownFutureValue |

### hostReputationRuleSeverity values

| Member |
| --- |
| unknown |
| low |
| medium |
| high |
| unknownFutureValue |

### indicatorSource values

| Member |
| --- |
| microsoft |
| osint |
| public |
| unknownFutureValue |

### intelligenceProfileKind values

| Member |
| --- |
| actor |
| tool |
| unknownFutureValue |

### queryType values

| Member |
| --- |
| files |
| messages |
| unknownFutureValue |

### retentionTrigger values

| Member |
| --- |
| dateLabeled |
| dateCreated |
| dateModified |
| dateOfEvent |
| unknownFutureValue |

### vulnerabilitySeverity values

| Member |
| --- |
| none |
| low |
| medium |
| high |
| critical |
| unknownFutureValue |

### deviceAssetIdentifier values

| Member |
| --- |
| deviceId |
| deviceName |
| remoteDeviceName |
| targetDeviceName |
| destinationDeviceName |
| unknownFutureValue |

### deviceIdEntityIdentifier values

| Member |
| --- |
| deviceId |
| unknownFutureValue |

### disableUserEntityIdentifier values

| Member |
| --- |
| accountSid |
| initiatingProcessAccountSid |
| requestAccountSid |
| onPremSid |
| unknownFutureValue |

### emailEntityIdentifier values

| Member |
| --- |
| networkMessageId |
| recipientEmailAddress |
| unknownFutureValue |

### fileEntityIdentifier values

| Member |
| --- |
| sha1 |
| initiatingProcessSHA1 |
| sha256 |
| initiatingProcessSHA256 |
| unknownFutureValue |

### forceUserPasswordResetEntityIdentifier values

| Member |
| --- |
| accountSid |
| initiatingProcessAccountSid |
| requestAccountSid |
| onPremSid |
| unknownFutureValue |

### huntingRuleErrorCode values

| Member |
| --- |
| queryExecutionFailed |
| queryExecutionThrottling |
| queryExceededResultSize |
| queryLimitsExceeded |
| queryTimeout |
| alertCreationFailed |
| alertReportNotFound |
| partialRowsFailed |
| unknownFutureValue |
| noImpactedEntity |

### huntingRuleRunStatus values

| Member |
| --- |
| running |
| completed |
| failed |
| partiallyFailed |
| unknownFutureValue |

### isolationType values

| Member |
| --- |
| full |
| selective |
| unknownFutureValue |

### mailboxAssetIdentifier values

| Member |
| --- |
| accountUpn |
| fileOwnerUpn |
| initiatingProcessAccountUpn |
| lastModifyingAccountUpn |
| targetAccountUpn |
| senderFromAddress |
| senderDisplayName |
| recipientEmailAddress |
| senderMailFromAddress |
| unknownFutureValue |

### markUserAsCompromisedEntityIdentifier values

| Member |
| --- |
| accountObjectId |
| initiatingProcessAccountObjectId |
| servicePrincipalId |
| recipientObjectId |
| unknownFutureValue |

### scopeType values

| Member |
| --- |
| deviceGroup |
| unknownFutureValue |

### stopAndQuarantineFileEntityIdentifier values

| Member |
| --- |
| deviceId |
| sha1 |
| initiatingProcessSHA1 |
| unknownFutureValue |

### userAssetIdentifier values

| Member |
| --- |
| accountObjectId |
| accountSid |
| accountUpn |
| accountName |
| accountDomain |
| accountId |
| requestAccountSid |
| requestAccountName |
| requestAccountDomain |
| recipientObjectId |
| processAccountObjectId |
| initiatingAccountSid |
| initiatingProcessAccountUpn |
| initiatingAccountName |
| initiatingAccountDomain |
| servicePrincipalId |
| servicePrincipalName |
| targetAccountUpn |
| unknownFutureValue |

### submissionResultCategory values

| Member |
| --- |
| notJunk |
| spam |
| phishing |
| malware |
| allowedByPolicy |
| blockedByPolicy |
| spoof |
| unknown |
| noResultAvailable |
| unknownFutureValue |
| beingAnalyzed |
| notSubmittedToMicrosoft |
| phishingSimulation |
| allowedDueToOrganizationOverride |
| blockedDueToOrganizationOverride |
| allowedDueToUserOverride |
| blockedDueToUserOverride |
| itemNotfound |
| threatsFound |
| noThreatsFound |
| domainImpersonation |
| userImpersonation |
| brandImpersonation |
| authenticationFailure |
| spoofedBlocked |
| spoofedAllowed |
| reasonLostInTransit |
| bulk |

### antispamTeamsDirection values

| Member |
| --- |
| unknown |
| inbound |
| outbound |
| intraorg |
| unknownFutureValue |

### teamsDeliveryLocation values

| Member |
| --- |
| unknown |
| teams |
| quarantine |
| failed |
| unknownFutureValue |

### recipientType values

| Member |
| --- |
| user |
| roleGroup |
| unknownFutureValue |

### teamsMessageDeliveryAction values

| Member |
| --- |
| unknown |
| deliveredAsSpam |
| delivered |
| blocked |
| replaced |
| unknownFutureValue |

### cloudAttachmentVersion values

| Member |
| --- |
| latest |
| recent10 |
| recent100 |
| all |
| unknownFutureValue |

### documentVersion values

| Member |
| --- |
| latest |
| recent10 |
| recent100 |
| all |
| unknownFutureValue |

### contentProcessingErrorType values

| Member |
| --- |
| transient |
| permanent |
| unknownFutureValue |

### dlpAction values

| Member |
| --- |
| notifyUser |
| blockAccess |
| deviceRestriction |
| browserRestriction |
| unknownFutureValue |
| restrictAccess |
| generateAlert |
| generateIncidentReportAction |
| sPBlockAnonymousAccess |
| sPRuntimeAccessControl |
| sPSharingNotifyUser |
| sPSharingGenerateIncidentReport |
| restrictWebGrounding |

### executionMode values

| Member |
| --- |
| evaluateInline |
| evaluateOffline |
| unknownFutureValue |

### policyPivotProperty values

| Member |
| --- |
| none |
| activity |
| location |
| unknownFutureValue |

### protectionScopeState values

| Member |
| --- |
| notModified |
| modified |
| unknownFutureValue |

### userActivityTypes values

| Member |
| --- |
| none |
| uploadText |
| uploadFile |
| downloadText |
| downloadFile |
| unknownFutureValue |

### userActivityType values

| Member |
| --- |
| uploadText |
| uploadFile |
| downloadText |
| downloadFile |
| unknownFutureValue |

### labelActionSource values

| Member |
| --- |
| manual |
| automatic |
| recommended |
| none |
| unknownFutureValue |

### sensitivityLabelTarget values

| Member |
| --- |
| email |
| site |
| unifiedGroup |
| teamwork |
| unknownFutureValue |

### applicationMode values

| Member |
| --- |
| manual |
| automatic |
| recommended |

### restrictionAction values

| Member |
| --- |
| warn |
| audit |
| block |

### sensorCandidateActivationMode values

| Member |
| --- |
| manual |
| automated |
| unknownFutureValue |

### action values

| Member |
| --- |
| disable |
| enable |
| forcePasswordReset |
| revokeAllSessions |
| requireUserToSignInAgain |
| markUserAsCompromised |
| unknownFutureValue |

### alertStatus values

| Member |
| --- |
| unknown |
| new |
| inProgress |
| resolved |
| unknownFutureValue |

### identityProvider values

| Member |
| --- |
| entraID |
| activeDirectory |
| okta |
| unknownFutureValue |

### serviceSource values

| Member |
| --- |
| unknown |
| microsoftDefenderForEndpoint |
| microsoftDefenderForIdentity |
| microsoftDefenderForCloudApps |
| microsoftDefenderForOffice365 |
| microsoft365Defender |
| azureAdIdentityProtection |
| microsoftAppGovernance |
| dataLossPrevention |
| unknownFutureValue |
| microsoftDefenderForCloud |
| microsoftSentinel |
| microsoftThreatIntelligence |
| microsoftSecurityForAI |

### serviceStatus values

| Member |
| --- |
| stopped |
| starting |
| running |
| disabled |
| onboarding |
| unknown |
| unknownFutureValue |

### antispamDirectionality values

| Member |
| --- |
| unknown |
| inbound |
| outbound |
| intraOrg |
| unknownFutureValue |

### deliveryAction values

| Member |
| --- |
| unknown |
| deliveredToJunk |
| delivered |
| blocked |
| replaced |
| unknownFutureValue |

### deliveryLocation values

| Member |
| --- |
| unknown |
| inbox\_folder |
| junkFolder |
| deletedFolder |
| quarantine |
| onprem\_external |
| failed |
| dropped |
| others |
| unknownFutureValue |

### eventSource values

| Member |
| --- |
| system |
| admin |
| user |
| unknownFutureValue |

### remediationAction values

| Member |
| --- |
| moveToJunk |
| moveToInbox |
| hardDelete |
| softDelete |
| moveToDeletedItems |
| unknownFutureValue |
| moveToQuarantine |

### remediationSeverity values

| Member |
| --- |
| low |
| medium |
| high |
| unknownFutureValue |

### threatType values

| Member |
| --- |
| unknown |
| spam |
| malware |
| phish |
| none |
| unknownFutureValue |

### timelineEventType values

| Member |
| --- |
| originalDelivery |
| systemTimeTravel |
| dynamicDelivery |
| userUrlClick |
| reprocessed |
| zap |
| quarantineRelease |
| air |
| unknown |
| unknownFutureValue |

### verdictCategory values

| Member |
| --- |
| none |
| malware |
| phish |
| siteUnavailable |
| spam |
| decryptionFailed |
| unsupportedUriScheme |
| unsupportedFileType |
| undefined |
| unknownFutureValue |

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/enums-security?view=graph-rest-beta&accept=text/markdown)
