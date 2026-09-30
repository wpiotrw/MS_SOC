---
layout: Conceptual
title: Azure Monitor Logs reference - SigninLogs - Azure Monitor | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/signinlogs
breadcrumb_path: ../../../breadcrumb/azure-monitor/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/20/azure-monitor/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/3887dc70-2025-ec11-b6e6-000d3a4f09d0
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
author: austinmccollum
learn_banner_products:
- azure
manager: tedhudek
ms.author: austinmc
ms.service: azure-monitor
description: Reference for SigninLogs table in Azure Monitor Logs.
ms.topic: generated-reference
ms.subservice: logs
ms.date: 2026-08-27T00:00:00.0000000Z
locale: en-us
document_id: 8209cd4f-9247-5c6d-0bf7-4cb4b5c739c9
document_version_independent_id: 7a3239e3-2b86-a7d4-b346-a150633a8530
original_content_git_url: https://github.com/MicrosoftDocs/azure-monitor-docs-pr/blob/live/articles/azure-monitor/reference/tables/signinlogs.md
site_name: Docs
depot_name: Learn.azure-monitor
page_type: conceptual
toc_rel: ../toc.json
asset_id: azure-monitor/reference/tables/signinlogs
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-monitor/reference/tables/signinlogs.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: b71e321b-1a93-a5b8-6127-56bc53e5bb10
---

# Azure Monitor Logs reference - SigninLogs - Azure Monitor | Microsoft Learn

## Table attributes

| Attribute | Value |
| --- | --- |
| **Resource types** | microsoft.graph/tenants |
| **Categories** | Azure Resources, Security |
| **Solutions** | LogManagement |
| **Basic** table support | Yes |
| **Auxiliary / Lake** table support | Yes |
| **DCR workspace transformation** support | Yes |
| **Ingestion API** support | No |
| **Sample Queries** | [Yes](/en-us/azure/azure-monitor/reference/queries/signinlogs) |

## Columns

| Column | Type | Description |
| --- | --- | --- |
| AADTenantId | string |  |
| Agent | dynamic | The agentic property for sign in logs. Includes the agentType and the parentAppId when the type is AgenticInstance. |
| AlternateSignInName | string | The identification that the user provided to sign in. It may be the userPrincipalName but it's also populated when a user signs in using other identifiers. |
| AppDisplayName | string | The application name displayed in the Azure Portal. |
| AppId | string | The application identifier in Microsoft Entra ID. |
| AppliedConditionalAccessPolicies | string |  |
| AppliedEventListeners | dynamic | Detailed information about the listeners, such as Azure Logic Apps and Azure Functions, that were triggered by the corresponding events in the sign-in event. |
| AppOwnerTenantId | string | The tenant identifier of the owenr of the application in Microsoft Entra ID. |
| AuthenticationAppDeviceDetails | string | Details of the app and device state used during the most recent authentication step using an authentication app. |
| AuthenticationAppPolicyEvaluationDetails | string | The details of the policies applied and enforced related to the authentication app during the latest signIn step. |
| AuthenticationContextClassReferences | string | Contains a collection of values that represent the conditional access authentication contexts applied to the sign-in. |
| AuthenticationDetails | string | The result of the authentication attempt and additional details on the authentication method. |
| AuthenticationMethodsUsed | string | The authentication methods used. Possible values: SMS, Authenticator App, App Verification code, Password, FIDO, PTA, or PHS. |
| AuthenticationProcessingDetails | string | Additional authentication processing details, such as the agent name in case of PTA/PHS or Server/farm name in case of federated authentication. |
| AuthenticationProtocol | string | Lists the protocol type or grant type used in the authentication. The possible values are: none, oAuth2, ropc, wsFederation, saml20, deviceCode. For authentications that use protocols other than the possible values listed, the protocol type is listed as none. |
| AuthenticationRequirement | string | This holds the highest level of authentication needed through all the sign-in steps, for sign-in to succeed. |
| AuthenticationRequirementPolicies | string | Sources of authentication requirement, such as conditional access, per-user MFA, identity protection, and security defaults. |
| AuthenticatorAppLocation | string | The location of the authenticator app. |
| AutonomousSystemNumber | string | The Autonomous System Number (ASN) of the network used by the actor. |
| \_BilledSize | real | The record size in bytes |
| Category | string |  |
| ClientAppUsed | string | The legacy client used for sign-in activity. For example: Browser, Exchange ActiveSync, Modern clients, IMAP, MAPI, SMTP, or POP. |
| ClientCredentialType | string | The type of client credential used. Examples include client assertion, client secret, etc. |
| ClientSessionId | string | ID of the client session associated with the signIn. |
| ConditionalAccessAudiences | string | The audiences targeted by the conditional access policy. |
| ConditionalAccessPolicies | dynamic | A list of conditional access policies that are triggered by the corresponding sign-in activity. |
| ConditionalAccessStatus | string | The status of the conditional access policy triggered. Possible values: success, failure, or notApplied. |
| CorrelationId | string | The identifier that's sent from the client when sign-in is initiated. This is used for troubleshooting the corresponding sign-in activity when calling for support. |
| CreatedDateTime | datetime | The date and time the sign-in was initiated. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. |
| CrossTenantAccessType | string | Describes the type of cross-tenant access used by the actor to access the resource. |
| DeviceDetail | dynamic | The device information from where the sign-in occurred. Includes information such as deviceId, OS, and browser. |
| DurationMs | long |  |
| FederatedCredentialId | string | Federated Credential Id. |
| FlaggedForReview | bool | During a failed sign in, a user may click a button in the Azure portal to mark the failed event for tenant admins. If a user clicked the button to flag the failed sign in, this value is true. |
| GlobalSecureAccessIpAddress | string | Global secure IP address that user signed in from. |
| HomeTenantId | string | The tenant identifier of the user initiating the sign in. Not applicable in Managed Identity or service principal sign ins. |
| HomeTenantName | string | The tenant name of the external tenant who homes the entitity taking action in the customer's tenant. |
| Id | string | The identifier representing the sign-in activity. |
| Identity | string | The display name of the actor identified in the signin. |
| IncomingTokenType | string | The type of token utilized to signIn (examples: primary refresh token, saml assertion). |
| IPAddress | string | The IP address of the client from where the sign-in occurred. |
| IPAddressFromResourceProvider | string | The IP address a user used to reach a resource provider, used to determine Conditional Access compliance for some policies. For example, when a user interacts with Exchange Online, the IP address Exchange receives from the user may be recorded here. This value is often null. |
| \_IsBillable | string | Specifies whether ingesting the data is billable. When \_IsBillable is `false` ingestion isn't billed to your Azure account |
| IsInteractive | bool | Indicates whether a user sign in is interactive. In interactive sign in, the user provides an authentication factor to Azure AD. These factors include passwords, responses to MFA challenges, biometric factors, or QR codes that a user provides to Azure AD or an associated app. In non-interactive sign in, the user doesn't provide an authentication factor. Instead, the client app uses a token or code to authenticate or access a resource on behalf of a user. Non-interactive sign ins are commonly used for a client to sign in on a user's behalf in a process transparent to the user. |
| IsRisky | bool |  |
| IsTenantRestricted | bool | Indicates if a signIn is under a tenant restrictions policy or not. |
| IsThroughGlobalSecureAccess | bool | Displays whether or not a user came through Global Secure Access service or not. |
| Level | string |  |
| Location | string | The 2 letter country code from where the sign-in occurred. Depending on IP address provided, this value may not always resolve to a city or region level of detail. |
| LocationDetails | dynamic | Provides the city, state, country/region and latitude and longitude from where the sign-in happened. |
| MfaDetail | dynamic | This property is deprecated. |
| NetworkLocationDetails | string | The network location details including the type of network used and its names. |
| OperationName | string |  |
| OperationVersion | string |  |
| OriginalRequestId | string | The request identifier of the first request in the authentication sequence. |
| OriginalTransferMethod | string | Transfer method used to initiate a session throughout all subsequent requests. |
| ProcessingTimeInMilliseconds | string |  |
| Resource | string |  |
| ResourceDisplayName | string | The name of the resource that the user signed in to. |
| ResourceGroup | string |  |
| ResourceId | string | The identifier of the resource that the user signed in to. |
| ResourceIdentity | string | The resource that the user signed in to. |
| ResourceOwnerTenantId | string | The tenant identifier of the owner of the resource referenced in the sign in. |
| ResourceProvider | string |  |
| ResourceServicePrincipalId | string | The identifier of the service principal representing the target resource in the sign-in event. |
| ResourceTenantId | string | The tenant identifier of the resource referenced in the sign in. |
| ResultDescription | string | Provides the error message or the reason for failure for the corresponding sign-in activity. |
| ResultSignature | string |  |
| ResultType | string | Provides the 5-6 digit error code that's generated during a sign-in event. 0 indicates success; other values are failures. You can find more information using the Azure AD Error Codes documentation or `https://login.microsoftonline.com/error`. |
| RiskDetail | string | The reason behind a specific state of a risky user, sign-in, or a risk event. Possible values: none, adminGeneratedTemporaryPassword, userPerformedSecuredPasswordChange, userPerformedSecuredPasswordReset, adminConfirmedSigninSafe, aiConfirmedSigninSafe, userPassedMFADrivenByRiskBasedPolicy, adminDismissedAllRiskForUser, or adminConfirmedSigninCompromised. The value none means that no action has been performed on the user or sign-in so far. Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers are returned hidden. |
| RiskEventTypes | string | This property is deprecated. |
| RiskEventTypes\_V2 | string | The list of risk event types associated with the sign-in. Possible values: unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence, or generic. |
| RiskLevel | string |  |
| RiskLevelAggregated | string | The aggregated risk level. Possible values: none, low, medium, high, or hidden. The value hidden means the user or sign-in was not enabled for Azure AD Identity Protection. Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers are returned hidden. |
| RiskLevelDuringSignIn | string | The risk level during sign-in. Possible values: none, low, medium, high, or hidden. The value hidden means the user or sign-in was not enabled for Azure AD Identity Protection. Note: Details for this property are only available for Azure AD Premium P2 customers. All other customers are returned hidden. |
| RiskState | string | The risk state of a risky user, sign-in, or a risk event. Possible values: none, confirmedSafe, remediated, dismissed, atRisk, or confirmedCompromised. |
| RootActorID | string | The root actor virtual ID associated with the sign-in. |
| ServicePrincipalId | string | The application identifier used for sign-in. This field is populated when you are signing in using an application. |
| ServicePrincipalName | string | The application name used for sign-in. This field is populated when you are signing in using an application. |
| SessionId | string | Id of the session that was generated during the signIn. |
| SessionLifetimePolicies | string | Any conditional access session management policies that were applied during the sign-in event. |
| SignInIdentifier | string | The identification that the user provided to sign in. It may be the userPrincipalName but it's also populated when a user signs in using other identifiers. |
| SignInIdentifierType | string | The type of sign in identifier. Possible values are: userPrincipalName, phoneNumber, proxyAddress, qrCode, onPremisesUserPrincipalName. |
| SourceAppClientId | string | The Source App's Client ID for Target Identities. |
| SourceSystem | string | The type of agent the event was collected by. For example, `OpsManager` for Windows agent, either direct connect or Operations Manager, `Linux` for all Linux agents, or `Azure` for Azure Diagnostics |
| Status | dynamic | The sign-in status. Includes the error code and description of the error (in case of a sign-in failure). |
| TimeGenerated | datetime |  |
| TokenIssuerName | string | The name of the identity provider. For example, sts.microsoft.com. |
| TokenIssuerType | string | The type of identity provider. The possible values are: AzureAD, or ADFederationServices, AzureADBackupAuth, ADFederationServicesMFAAdapter, NPSExtension. |
| TokenProtectionStatusDetails | dynamic | Token protection creates a cryptographically secure tie between the token and the device it's issued to. This field indicates whether the signin token was bound to the device or not. |
| Type | string | The name of the table |
| UniqueTokenIdentifier | string | A unique base64 encoded request identifier used to track tokens issued by Azure AD as they are redeemed at resource providers. |
| UserAgent | string | The user agent information related to sign-in. |
| UserDisplayName | string | The display name of the user. |
| UserId | string | The identifier of the user. |
| UserPrincipalName | string | The UPN of the user. |
| UserType | string | Identifies whether the user is a member or guest in the tenant. Possible values are: member and guest. |