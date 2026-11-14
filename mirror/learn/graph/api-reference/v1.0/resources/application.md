---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: application resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/application?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: Jackson-Woods
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-applications
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents an application.
ms.localizationpriority: high
doc_type: resourcePageType
ms.date: 2024-08-16T00:00:00.0000000Z
ms.custom: sfi-ropc-nochange
locale: en-us
document_id: f54172c8-c149-8002-b172-5d1d286177f0
document_version_independent_id: c23c0d2f-5f70-e67d-9068-99e660126fd0
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/application.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/application
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/application.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 57bc4f50-4444-2642-3b3b-c9cc3b40b783
---

# application resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents an application. Any application that outsources authentication to Microsoft Entra ID must be registered in the Microsoft identity platform. Application registration involves telling Microsoft Entra ID about your application, including the URL where it's located, the URL to send replies after authentication, the URI to identify your application, and more.

Inherits from [directoryObject](directoryobject).

This resource is an open type that allows additional properties beyond those documented here.

The [agentIdentityBlueprint](agentidentityblueprint) resource inherits from this object.

This resource supports:

- Adding your own data to custom properties as [extensions](/en-us/graph/extensibility-overview).
- Using [delta query](/en-us/graph/delta-query-overview) to track incremental additions, deletions, and updates, by providing a [delta](../user-delta) function.
- Alternate key syntax. The `appId` property is a supported alternate key. For more information, see [Get application](../application-get).

## Methods

| Method | Return Type | Description |
| --- | --- | --- |
| [List](../application-list) | [application](application) collection | Retrieve the list of applications in the organization. |
| [Create](../application-post-applications) | [application](application) | Creates (registers) a new application. |
| [Get](../application-get) | [application](application) | Read properties and relationships of application object. |
| [Update](../application-update) | None | Update application object. |
| [Upsert](../application-upsert) | [application](application) | Create a new application if it doesn't exist, or update the properties of an existing application. |
| [Delete](../application-delete) | None | Delete application object. |
| [Get delta](../application-delta) | [application](application) | Get newly created, updated, or deleted applications without performing a full read of the entire resource collection. |
| **Deleted items** |  |  |
| [List](../directory-deleteditems-list) | [directoryObject](directoryobject) collection | Retrieve a list of recently deleted applications. |
| [Get](../directory-deleteditems-get) | [directoryObject](directoryobject) | Retrieve the properties of a recently deleted application. |
| [Restore](../directory-deleteditems-restore) | [directoryObject](directoryobject) | Restore a recently deleted application. |
| [Permanently delete](../directory-deleteditems-delete) | None | Permanently delete an application. |
| [List deleted items owned by user](../directory-deleteditems-getuserownedobjects) | [directoryObject](directoryobject) collection | Retrieve the applications deleted in the tenant in the last 30 days and that are owned by a user. |
| **Certificates and secrets** |  |  |
| [Add password](../application-addpassword) | [passwordCredential](passwordcredential) | Add a strong password to an application. |
| [Remove password](../application-removepassword) | [passwordCredential](passwordcredential) | Remove a password from an application. |
| [Add key](../application-addkey) | [keyCredential](keycredential) | Add a key credential to an application. |
| [Remove key](../application-removekey) | None | Remove a key credential from an application. |
| **Owners** |  |  |
| [List](../application-list-owners) | [directoryObject](directoryobject) collection | Get the owners of an application. |
| [Add](../application-post-owners) | [directoryObject](directoryobject) | Assign an owner to an application. Application owners can be users or service principals. |
| [Remove](../application-delete-owners) | None | Remove an owner from an application. As a recommended best practice, apps should have at least two owners. |
| **Verified publisher** |  |  |
| [Set](../application-setverifiedpublisher) | None | Set the verified publisher of an application. |
| [Unset](../application-unsetverifiedpublisher) | None | Unset the verified publisher of an application. |

## Properties

Important

Specific usage of `$filter` and the `$search` query parameter is supported only when you use the **ConsistencyLevel** header set to `eventual` and `$count`. For more information, see [Advanced query capabilities on directory objects](/en-us/graph/aad-advanced-queries#application-properties).

| Property | Type | Description |
| --- | --- | --- |
| addIns | [addIn](addin) collection | Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams [can set the addIns property](/en-us/onedrive/developer/file-handlers) for its "FileHandler" functionality. This lets services like Microsoft 365 call the application in the context of a document the user is working on. |
| api | [apiApplication](apiapplication) | Specifies settings for an application that implements a web API. |
| appId | String | The unique identifier for the application that is assigned to an application by Microsoft Entra ID. Not nullable. Read-only. Alternate key. Supports `$filter` (`eq`). |
| applicationTemplateId | String | Unique identifier of the [applicationTemplate](applicationtemplate). Supports `$filter` (`eq`, `not`, `ne`). Read-only. `null` if the app wasn't created from an application template. |
| appRoles | [appRole](approle) collection | The collection of roles defined for the application. With [app role assignments](approleassignment), these roles can be assigned to users, groups, or service principals associated with other applications. Not nullable. App roles and exposed delegated permission scopes (**api.oauth2PermissionScopes**) share a default limit of 700 permission definitions per application. Enabled and disabled definitions both count. This limit is separate from the aggregate 1,200-entry application manifest limit and from app role assignment limits. For counting rules, behavior for existing objects above the limit, and design guidance, see [App role limits](/en-us/entra/identity-platform/howto-add-app-roles-in-apps#app-role-limits). |
| authenticationBehaviors | [authenticationBehaviors](authenticationbehaviors) | The set of breaking change behaviors related to token issuance that are configured for the application. Authentication behaviors are unset by default (`null`) and must be explicitly enabled or disabled. Nullable. Returned only on `$select`. Requires `$select` to retrieve.  For more information about authentication behaviors, see [Manage application authenticationBehaviors](/en-us/graph/applications-authenticationbehaviors). |
| certification | [certification](certification) | Specifies the certification status of the application. |
| createdByAppId | String | The **appId** of the application that created this application. Set internally by Microsoft Entra ID. Read-only. |
| createdDateTime | DateTimeOffset | The date and time the application was registered. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z`. Read-only.  Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `in`, and `eq` on `null` values) and `$orderby`. |
| deletedDateTime | DateTimeOffset | The date and time the application was deleted. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z`. Read-only. |
| description | String | Free text field to provide a description of the application object to end users. The maximum allowed size is 1,024 characters. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `startsWith`) and `$search`. |
| disabledByMicrosoftStatus | String | Specifies whether Microsoft has disabled the registered application. The possible values are: `null` (default value), `NotDisabled`, and `DisabledDueToViolationOfServicesAgreement` (reasons include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports `$filter` (`eq`, `ne`, `not`). |
| displayName | String | The display name for the application. Maximum length is 256 characters. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `in`, `startsWith`, and `eq` on `null` values), `$search`, and `$orderby`. |
| groupMembershipClaims | String | Configures the `groups` claim issued in a user or OAuth 2.0 access token that the application expects. To set this attribute, use one of the following valid string values: `None`, `SecurityGroup` (for security groups and Microsoft Entra roles), `All` (this gets all of the security groups, distribution groups, and Microsoft Entra directory roles that the signed-in user is a member of). |
| id | String | Unique identifier for the application object. This property is referred to as **Object ID** in the Microsoft Entra admin center. Inherited from [directoryObject](directoryobject). Key. Not nullable. Read-only. Supports `$filter` (`eq`, `ne`, `not`, `in`). |
| identifierUris | String collection | Also known as App ID URI, this value is set when an application is used as a resource app. The identifierUris acts as the prefix for the scopes you reference in your API's code, and it must be globally unique across Microsoft Entra ID. For more information on valid identifierUris patterns and best practices, see [Microsoft Entra application registration security best practices](/en-us/entra/identity-platform/security-best-practices-for-app-registration#application-id-uri-also-known-as-identifier-uri). Not nullable. Supports `$filter` (`eq`, `ne`, `ge`, `le`, `startsWith`). |
| info | [informationalUrl](informationalurl) | Basic profile information of the application such as app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more info, see How to: [Add Terms of service and privacy statement for registered Microsoft Entra apps](/en-us/azure/active-directory/develop/howto-add-terms-of-service-privacy-statement). Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, and `eq` on `null` values). |
| isDeviceOnlyAuthSupported | Boolean | Specifies whether this application supports device authentication without a user. The default is `false`. |
| isFallbackPublicClient | Boolean | Specifies the fallback application type as public client, such as an installed application running on a mobile device. The default value is `false`, which means the fallback application type is confidential client such as a web app. There are certain scenarios where Microsoft Entra ID can't determine the client application type. For example, the [ROPC](https://tools.ietf.org/html/rfc6749#section-4.3) flow where it's configured without specifying a redirect URI. In those cases, Microsoft Entra ID interprets the application type based on the value of this property. |
| keyCredentials | [keyCredential](keycredential) collection | The collection of key credentials associated with the application. Not nullable. Supports `$filter` (`eq`, `not`, `ge`, `le`). |
| logo | Stream | The main logo for the application. Not nullable. |
| managerApplications | Guid collection | A collection of application IDs for Microsoft first-party applications designated as managers. Manager applications can create service principals, agent identities, and agent users for managed agent blueprints. Limited to a maximum of 10 entries. Not nullable. Only supported on [agentIdentityBlueprint](agentidentityblueprint) objects; attempts to set this property on non-agent-blueprint applications return an error. Not returned by default; must be explicitly requested via `$select`. |
| nativeAuthenticationApisEnabled | nativeAuthenticationApisEnabled | Specifies whether the Native Authentication APIs are enabled for the application. The possible values are: `none` and `all`. Default is `none`. For more information, see [Native Authentication](/en-us/entra/external-id/customers/concept-native-authentication). |
| notes | String | Notes relevant for the management of the application. |
| oauth2RequiredPostResponse | Boolean | Specifies whether, as part of OAuth 2.0 token requests, Microsoft Entra ID allows POST requests, as opposed to GET requests. The default is `false`, which specifies that only GET requests are allowed. |
| optionalClaims | [optionalClaims](optionalclaims) | Application developers can configure optional claims in their Microsoft Entra applications to specify the claims that are sent to their application by the Microsoft security token service. For more information, see [How to: Provide optional claims to your app](/en-us/azure/active-directory/develop/active-directory-optional-claims). |
| parentalControlSettings | [parentalControlSettings](parentalcontrolsettings) | Specifies parental control settings for an application. |
| passwordCredentials | [passwordCredential](passwordcredential) collection | The collection of password credentials associated with the application. Not nullable. |
| publicClient | [publicClientApplication](publicclientapplication) | Specifies settings for installed clients such as desktop or mobile devices. |
| publisherDomain | String | The verified publisher domain for the application. Read-only. For more information, see [How to: Configure an application's publisher domain](/en-us/azure/active-directory/develop/howto-configure-publisher-domain). Supports `$filter` (`eq`, `ne`, `ge`, `le`, `startsWith`). |
| requestSignatureVerification | [requestSignatureVerification](requestsignatureverification) | Specifies whether this application requires Microsoft Entra ID to verify the signed authentication requests. |
| requiredResourceAccess | [requiredResourceAccess](requiredresourceaccess) collection | Specifies the resources that the application needs to access. This property also specifies the set of delegated permissions and application roles that it needs for each of those resources. This configuration of access to the required resources drives the consent experience. No more than 50 resource services (APIs) can be configured. Beginning mid-October 2021, the total number of required permissions must not exceed 400. For more information, see Limits on requested permissions per app. Not nullable. Supports `$filter` (`eq`, `not`, `ge`, `le`). |
| samlMetadataUrl | String | The URL where the service exposes SAML metadata for federation. This property is valid only for single-tenant applications. Nullable. |
| serviceManagementReference | String | References application or service contact information from a Service or Asset Management database. Nullable. |
| servicePrincipalLockConfiguration | [servicePrincipalLockConfiguration](serviceprincipallockconfiguration) | Specifies whether sensitive properties of a multitenant application should be locked for editing after the application is provisioned in a tenant. Nullable. `null` by default. |
| signInAudience | String | Specifies the Microsoft accounts that are supported for the current application. The possible values are: `AzureADMyOrg` (default), `AzureADMultipleOrgs`, `AzureADandPersonalMicrosoftAccount`, and `PersonalMicrosoftAccount`. See more in the table. The value of this object also limits the number of permissions an app can request. For more information, see Limits on requested permissions per app. The value for this property has implications on other app object properties. As a result, if you change this property, you might need to change other properties first. For more information, see [Validation differences for signInAudience](/en-us/azure/active-directory/develop/supported-accounts-validation?context=graph/context).Supports `$filter` (`eq`, `ne`, `not`). |
| spa | [spaApplication](spaapplication) | Specifies settings for a single-page application, including sign out URLs and redirect URIs for authorization codes and access tokens. |
| tags | String collection | Custom strings that can be used to categorize and identify the application. Not nullable. Strings added here will also appear in the **tags** property of any associated [service principals](serviceprincipal).Supports `$filter` (`eq`, `not`, `ge`, `le`, `startsWith`) and `$search`. |
| tokenEncryptionKeyId | String | Specifies the keyId of a public key from the keyCredentials collection. When configured, Microsoft Entra ID encrypts all the tokens it emits by using the key this property points to. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user. |
| uniqueName | String | The unique identifier that can be assigned to an application and used as an alternate key. Immutable. Read-only. |
| verifiedPublisher | [verifiedPublisher](verifiedpublisher) | Specifies the verified publisher of the application. For more information about how publisher verification helps support application security, trustworthiness, and compliance, see [Publisher verification](/en-us/azure/active-directory/develop/publisher-verification-overview). |
| web | [webApplication](webapplication) | Specifies settings for a web application. |

### signInAudience values

Important

Using the **signInAudience** property to limit where an application can be used **isn't** a replacement for proper tenant validation and authorization enforcement in your application code. If your application expects access only in specific tenants, you *must* enforce that validation in your application code. To learn more, see [Secure applications and APIs by validating claims](/en-us/entra/identity-platform/claims-validation).

| Value | Description |
| --- | --- |
| AzureADMyOrg | Users with a Microsoft work or school account in my organization's Microsoft Entra tenant (single tenant). This is the default value for the **signInAudience** property. |
| AzureADMultipleOrgs | Users with a Microsoft work or school account in any organization's Microsoft Entra tenant (multitenant). |
| AzureADandPersonalMicrosoftAccount | Users with a personal Microsoft account, or a work or school account in any organization's Microsoft Entra tenant. For authenticating users with Azure AD B2C user flows, use `AzureADandPersonalMicrosoftAccount`. This value allows for the widest set of user identities including local accounts and user identities from Microsoft, Facebook, Google, Twitter, or any OpenID Connect provider. |
| PersonalMicrosoftAccount | Users with a personal Microsoft account only. |

### Limits on requested permissions per app

Microsoft Entra ID limits the number of permissions that can be requested and consented by a client app. These limits depend on the `signInAudience` value for an app, shown in the [app's manifest](/en-us/graph/api/resources/application).

| signInAudience | Allowed users | Maximum permissions the app can request | Maximum Microsoft Graph permissions the app can request | Maximum permissions that can be consented in a single request |
| --- | --- | --- | --- | --- |
| AzureADMyOrg | Users from the organization where the app is registered | 400 | 400 | About 155 delegated permissions and about 300 application permissions |
| AzureADMultipleOrgs | Users from any Microsoft Entra organization | 400 | 400 | About 155 delegated permissions and about 300 application permissions |
| PersonalMicrosoftAccount | Consumer users (such as Outlook.com or Live.com accounts) | 30 | 30 | 30 |
| AzureADandPersonalMicrosoftAccount | Consumer users and users from any Microsoft Entra organization | 30 | 30 | 30 |

Note

For Microsoft Entra Agent ID, some high-risk Microsoft Graph permissions are globally blocked for agents and can't be granted to agent identities.

If you include a blocked Microsoft Graph delegated permission scope or app role in the `resourceAccess` collection of a `requiredResourceAccess` entry, the request is rejected with an HTTP `400 Bad Request` response and an error indicating that the permission is blocked and can't be granted to agent identities.

For the list of blocked Microsoft Graph permissions for agents, see [Microsoft Graph permissions blocked for agents](/en-us/graph/api/resources/agentid-platform-overview?view=graph-rest-beta#microsoft-graph-permissions-blocked-for-agents).

## Relationships

Important

Specific usage of the `$filter` query parameter is supported only when you use the **ConsistencyLevel** header set to `eventual` and `$count`. For more information, see [Advanced query capabilities on directory objects](/en-us/graph/aad-advanced-queries#user-properties).

| Relationship | Type | Description |
| --- | --- | --- |
| appManagementPolicies | [appManagementPolicy](appmanagementpolicy) collection | The appManagementPolicy applied to this application. |
| createdOnBehalfOf | [directoryObject](directoryobject) | Supports `$filter` (`/$count eq 0`, `/$count ne 0`). Read-only. |
| extensionProperties | [extensionProperty](extensionproperty) collection | Read-only. Nullable. Supports `$expand` and `$filter` (`/$count eq 0`, `/$count ne 0`). |
| federatedIdentityCredentials | [federatedIdentityCredential](federatedidentitycredential) collection | Federated identities for applications. Supports `$expand` and `$filter` (`startsWith`, `/$count eq 0`, `/$count ne 0`). |
| owners | [directoryObject](directoryobject) collection | Directory objects that are owners of this application. The owners are a set of nonadmin users or service principals who are allowed to modify this object. Supports `$expand`, `$filter` (`/$count eq 0`, `/$count ne 0`, `/$count eq 1`, `/$count ne 1`), and `$select` nested in `$expand`. |
| synchronization | [synchronization](synchronization-synchronization) | Represents the capability for Microsoft Entra identity synchronization through the Microsoft Graph API. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "addIns": [{"@odata.type": "microsoft.graph.addIn"}],
  "api": {"@odata.type": "microsoft.graph.apiApplication"},
  "appId": "String",
  "applicationTemplateId": "String",
  "appRoles": [{"@odata.type": "microsoft.graph.appRole"}],
  "authenticationBehaviors": {"@odata.type": "microsoft.graph.authenticationBehaviors"},
  "certification": {"@odata.type": "microsoft.graph.certification"},
  "createdByAppId": "String",
  "createdDateTime": "String (timestamp)",
  "deletedDateTime": "String (timestamp)",
  "disabledByMicrosoftStatus": "String",
  "displayName": "String",
  "groupMembershipClaims": "String",
  "id": "String (identifier)",
  "identifierUris": ["String"],
  "info": {"@odata.type": "microsoft.graph.informationalUrl"},
  "isDeviceOnlyAuthSupported": false,
  "isFallbackPublicClient": false,
  "keyCredentials": [{"@odata.type": "microsoft.graph.keyCredential"}],
  "logo": "Stream",
  "managerApplications": ["Guid"],
  "nativeAuthenticationApisEnabled": "String",
  "notes": "String",
  "oauth2RequiredPostResponse": false,
  "optionalClaims": {"@odata.type": "microsoft.graph.optionalClaims"},
  "parentalControlSettings": {"@odata.type": "microsoft.graph.parentalControlSettings"},
  "passwordCredentials": [{"@odata.type": "microsoft.graph.passwordCredential"}],
  "publicClient": {"@odata.type": "microsoft.graph.publicClientApplication"},
  "publisherDomain": "String",
  "requestSignatureVerification": {"@odata.type": "microsoft.graph.requestSignatureVerification"},
  "requiredResourceAccess": [{"@odata.type": "microsoft.graph.requiredResourceAccess"}],
  "servicePrincipalLockConfiguration": {"@odata.type": "microsoft.graph.servicePrincipalLockConfiguration"},
  "serviceManagementReference": "String",
  "signInAudience": "String",
  "spa": {"@odata.type": "microsoft.graph.spaApplication"},
  "tags": ["String"],
  "tokenEncryptionKeyId": "String",
  "uniqueName": "String",
  "verifiedPublisher": {"@odata.type": "microsoft.graph.verifiedPublisher"},
  "web": {"@odata.type": "microsoft.graph.webApplication"}
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/application?view=graph-rest-beta&accept=text/markdown)
