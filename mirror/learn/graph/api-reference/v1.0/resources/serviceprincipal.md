---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: servicePrincipal resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/serviceprincipal?view=graph-rest-1.0
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
description: Represents an instance of an application in a directory. Inherits from directoryObject.
ms.localizationpriority: high
doc_type: resourcePageType
ms.date: 2026-11-02T00:00:00.0000000Z
locale: en-us
document_id: 2fcef076-0419-d0c9-1d49-c7c9a95317ce
document_version_independent_id: 0cd73e6b-f547-c257-4ffc-faeb4cfd1abf
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/serviceprincipal.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/serviceprincipal
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/serviceprincipal.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/b1cfdec6-b0c3-4209-818c-736879856e0e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/2d0723c1-cf38-4c30-ab3d-5df787b33270
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: 5d09c88c-e02d-3008-29c7-a525640154d2
---

# servicePrincipal resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents an instance of an application in a directory. Inherits from [directoryObject](directoryobject).

The [agentIdentityBlueprintPrincipal](agentidentityblueprintprincipal) resource inherits from this object.

This resource supports using [delta query](/en-us/graph/delta-query-overview) to track incremental additions, deletions, and updates, by providing a [delta](../serviceprincipal-delta) function. This resource is an open type that allows additional properties beyond those documented here.

## Methods

| Method | Return Type | Description |
| --- | --- | --- |
| [List](../serviceprincipal-list) | [servicePrincipal](serviceprincipal) collection | Retrieve a list of servicePrincipal objects. |
| [Create](../serviceprincipal-post-serviceprincipals) | [servicePrincipal](serviceprincipal) | Creates a new servicePrincipal object. |
| [Get](../serviceprincipal-get) | [servicePrincipal](serviceprincipal) | Read properties and relationships of servicePrincipal object. |
| [Update](../serviceprincipal-update) | [servicePrincipal](serviceprincipal) | Update servicePrincipal object. |
| [Upsert](../serviceprincipal-upsert) | [servicePrincipal](serviceprincipal) | Create a new servicePrincipal if it doesn't exist, or update the properties of an existing servicePrincipal. |
| [Delete](../serviceprincipal-delete) | None | Delete servicePrincipal object. |
| [Get delta](../serviceprincipal-delta) | servicePrincipal collection | Get incremental changes for service principals. |
| [servicePrincipal: attest](../serviceprincipal-attest) | None | Attest continued usage and compliance of an agent identity through its service principal. |
| [List created objects](../serviceprincipal-list-createdobjects) | [directoryObject](directoryobject) collection | Get a createdObject object collection. |
| [List owned objects](../serviceprincipal-list-ownedobjects) | [directoryObject](directoryobject) collection | Get an ownedObject object collection. |
| **Deleted items** |  |  |
| [List](../directory-deleteditems-list) | [directoryObject](directoryobject) collection | Retrieve a list of recently deleted servicePrincipal objects. |
| [Get](../directory-deleteditems-get) | [directoryObject](directoryobject) | Retrieve the properties of a recently deleted servicePrincipal object. |
| [Restore](../directory-deleteditems-restore) | [directoryObject](directoryobject) | Restore a recently deleted servicePrincipal object. |
| [Permanently delete](../directory-deleteditems-delete) | None | Permanently delete a servicePrincipal object. |
| **App role assignments** |  |  |
| [List appRoleAssignments](../serviceprincipal-list-approleassignments) | [appRoleAssignment](approleassignment) collection | Get the app roles that this service principal is assigned. |
| [Add appRoleAssignment](../serviceprincipal-post-approleassignments) | [appRoleAssignment](approleassignment) | Assign an app role to this service principal. |
| [Remove appRoleAssignment](../serviceprincipal-delete-approleassignments) | None | Remove an app role assignment from this service principal. |
| [List appRoleAssignedTo](../serviceprincipal-list-approleassignedto) | [appRoleAssignment](approleassignment) collection | Get the users, groups, and service principals assigned app roles for this service principal. |
| [Add appRoleAssignedTo](../serviceprincipal-post-approleassignedto) | [appRoleAssignment](approleassignment) | Assign an app role for this service principal to a user, group, or service principal. |
| [Remove appRoleAssignedTo](../serviceprincipal-delete-approleassignedto) | None | Remove an app role assignment for this service principal from a user, group, or service principal. |
| **Certificates and secrets** |  |  |
| [Add password](../serviceprincipal-addpassword) | [passwordCredential](passwordcredential) | Add a strong password or secret to a servicePrincipal. |
| [Remove password](../serviceprincipal-removepassword) | [passwordCredential](passwordcredential) | Remove a password or secret from a servicePrincipal. |
| [Add key](../serviceprincipal-addkey) | [keyCredential](keycredential) | Add a key credential to a servicePrincipal. |
| [Remove key](../serviceprincipal-removekey) | None | Remove a key credential from a servicePrincipal. |
| [Add token signing certificate](../serviceprincipal-addtokensigningcertificate) | [selfSignedCertificate](selfsignedcertificate) | Add a self-signed certificate to the service principal. Mostly used to configure SAML-based SSO applications from the [Microsoft Entra gallery](/en-us/azure/active-directory/saas-apps/tutorial-list). |
| **Delegated permission classifications** |  |  |
| [List](../serviceprincipal-list-delegatedpermissionclassifications) | [delegatedPermissionClassification](delegatedpermissionclassification) collection | Get the permission classifications for delegated permissions exposed by this service principal. |
| [Add](../serviceprincipal-post-delegatedpermissionclassifications) | [delegatedPermissionClassification](delegatedpermissionclassification) | Add a permission classification for a delegated permission exposed by this service principal. |
| [Remove](../serviceprincipal-delete-delegatedpermissionclassifications) | None | Remove a permission classification for a delegated permission exposed by this service principal. |
| **Delegated (OAuth2) permission grants** |  |  |
| [List](../serviceprincipal-list-oauth2permissiongrants) | [oAuth2PermissionGrant](oauth2permissiongrant) collection | Get the delegated permission grants authorizing this service principal to access an API on behalf of a signed-in user. |
| **Membership** |  |  |
| [List memberOf](../serviceprincipal-list-memberof) | [directoryObject](directoryobject) collection | Get the groups that this service principal is a direct member of from the memberOf navigation property. |
| [List transitive member of](../serviceprincipal-list-transitivememberof) | [directoryObject](directoryobject) collection | List the groups that this service principal is a member of. This operation is transitive and includes the groups that this service principal is a nested member of. |
| [Check member groups](../directoryobject-checkmembergroups) | String collection | Check for membership in a specified list of groups. |
| [Check member objects](../directoryobject-checkmemberobjects) | String collection | Check for membership in a specified list of group, directory role, or administrative unit objects. |
| [Get member groups](../directoryobject-getmembergroups) | String collection | Get the list of groups that this service principal is a member of. |
| [Get member objects](../directoryobject-getmemberobjects) | String collection | Get the list of groups, administrative units, and directory roles that this service principal is a member of. |
| **Owners** |  |  |
| [List](../serviceprincipal-list-owners) | [directoryObject](directoryobject) collection | Get the owners of a service principal. |
| [Add](../serviceprincipal-post-owners) | [directoryObject](directoryobject) | Assign an owner to a service principal. Service principal owners can be users or other service principals. |
| [Remove](../serviceprincipal-delete-owners) | None | Remove an owner from a service principal. As a recommended best practice, service principals should have at least two owners. |

## Properties

Important

Specific usage of `$filter` and the `$search` query parameter is supported only when you use the **ConsistencyLevel** header set to `eventual` and `$count`. For more information, see [Advanced query capabilities on directory objects](/en-us/graph/aad-advanced-queries#service-principal-properties).

| Property | Type | Description |
| --- | --- | --- |
| accountEnabled | Boolean | `true` if the service principal account is enabled; otherwise, `false`. If set to `false`, then no users are able to sign in to this app, even if they're assigned to it. Supports `$filter` (`eq`, `ne`, `not`, `in`). |
| addIns | [addIn](addin) collection | Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams [may set the addIns property](/en-us/onedrive/developer/file-handlers/?view=odsp-graph-online&amp;preserve-view=true) for its "FileHandler" functionality. This lets services like Microsoft 365 call the application in the context of a document the user is working on. |
| alternativeNames | String collection | Used to retrieve service principals by subscription, identify resource group and full resource IDs for [managed identities](/en-us/azure/active-directory/managed-identities-azure-resources/overview). Supports `$filter` (`eq`, `not`, `ge`, `le`, `startsWith`). |
| appDescription | String | The description exposed by the associated application. |
| appDisplayName | String | The display name exposed by the associated application. Maximum length is 256 characters. |
| appId | String | The unique identifier for the associated application (its **appId** property). Alternate key. Supports `$filter` (`eq`, `ne`, `not`, `in`, `startsWith`). |
| applicationTemplateId | String | Unique identifier of the [applicationTemplate](applicationtemplate). Supports `$filter` (`eq`, `not`, `ne`). Read-only. `null` if the service principal wasn't created from an application template. |
| appOwnerOrganizationId | Guid | Contains the tenant ID where the application is registered. This is applicable only to service principals backed by applications. Supports `$filter` (`eq`, `ne`, `NOT`, `ge`, `le`). |
| appRoleAssignmentRequired | Boolean | Specifies whether users or other service principals need to be granted an app role assignment for this service principal before users can sign in or apps can get tokens. The default value is `false`. Not nullable. Supports `$filter` (`eq`, `ne`, `NOT`). |
| appRoles | [appRole](approle) collection | The roles exposed by the application that's linked to this service principal. For more information, see the **appRoles** property definition on the [application](application) entity. Not nullable. App roles and exposed delegated permission scopes (**oauth2PermissionScopes**) share a default limit of 700 permission definitions per service principal, including definitions inherited from the application and definitions added directly to the service principal. Enabled and disabled definitions both count. This limit counts definitions, not app role assignments. For counting rules, behavior for existing objects above the limit, and design guidance, see [App role limits](/en-us/entra/identity-platform/howto-add-app-roles-in-apps#app-role-limits). |
| createdByAppId | String | The **appId** of the application that created this service principal. Set internally by Microsoft Entra ID. Read-only. |
| customSecurityAttributes | [customSecurityAttributeValue](customsecurityattributevalue) | An open complex type that holds the value of a custom security attribute that is assigned to a directory object. Nullable. Requires `$select` to retrieve. Supports `$filter` (`eq`, `ne`, `not`, `startsWith`). Filter value is case sensitive. - To read this property, the calling app must be assigned the *CustomSecAttributeAssignment.Read.All* permission. To write this property, the calling app must be assigned the *CustomSecAttributeAssignment.ReadWrite.All* permissions.<br>- To read or write this property in delegated scenarios, the admin must be assigned the *Attribute Assignment Administrator* role. |
| deletedDateTime | DateTimeOffset | The date and time the service principal was deleted. Read-only. |
| description | String | Free text field to provide an internal end-user facing description of the service principal. End-user portals such [MyApps](/en-us/azure/active-directory/user-help/my-apps-portal-end-user-access) displays the application description in this field. The maximum allowed size is 1,024 characters. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `startsWith`) and `$search`. |
| disabledByMicrosoftStatus | String | Specifies whether Microsoft has disabled the registered application. The possible values are: `null` (default value), `NotDisabled`, and `DisabledDueToViolationOfServicesAgreement` (reasons include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports `$filter` (`eq`, `ne`, `not`). |
| displayName | String | The display name for the service principal. Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, `in`, `startsWith`, and `eq` on `null` values), `$search`, and `$orderby`. |
| homepage | String | Home page or landing page of the application. |
| id | String | The unique identifier for the service principal. Inherited from [directoryObject](directoryobject). Key. Not nullable. Read-only. Supports `$filter` (`eq`, `ne`, `not`, `in`). |
| info | [informationalUrl](informationalurl) | Basic profile information of the acquired application such as app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more info, see How to: [Add Terms of service and privacy statement for registered Microsoft Entra apps](/en-us/azure/active-directory/develop/howto-add-terms-of-service-privacy-statement). Supports `$filter` (`eq`, `ne`, `not`, `ge`, `le`, and `eq` on `null` values). |
| keyCredentials | [keyCredential](keycredential) collection | The collection of key credentials associated with the service principal. Not nullable. Supports `$filter` (`eq`, `not`, `ge`, `le`). |
| loginUrl | String | Specifies the URL where the service provider redirects the user to Microsoft Entra ID to authenticate. Microsoft Entra ID uses the URL to launch the application from Microsoft 365 or the Microsoft Entra My Apps. When blank, Microsoft Entra ID performs IdP-initiated sign-on for applications configured with [SAML-based single sign-on](/en-us/azure/active-directory/manage-apps/what-is-single-sign-on#saml-sso). The user launches the application from Microsoft 365, the Microsoft Entra My Apps, or the Microsoft Entra SSO URL. |
| logoutUrl | String | Specifies the URL that the Microsoft's authorization service uses to sign out a user using OpenID Connect [front-channel](https://openid.net/specs/openid-connect-frontchannel-1_0.html), [back-channel](https://openid.net/specs/openid-connect-backchannel-1_0.html), or SAML sign out protocols. |
| notes | String | Free text field to capture information about the service principal, typically used for operational purposes. Maximum allowed size is 1,024 characters. |
| notificationEmailAddresses | String collection | Specifies the list of email addresses where Microsoft Entra ID sends a notification when the active certificate is near the expiration date. This is only for the certificates used to sign the SAML token issued for Microsoft Entra Gallery applications. |
| oauth2PermissionScopes | [permissionScope](permissionscope) collection | The delegated permissions exposed by the application. For more information, see the **oauth2PermissionScopes** property on the [application](application) entity's **api** property. Not nullable. These scopes and **appRoles** share a default limit of 700 permission definitions per service principal. Enabled and disabled definitions both count. For counting rules, behavior for existing objects above the limit, and design guidance, see [App role limits](/en-us/entra/identity-platform/howto-add-app-roles-in-apps#app-role-limits). |
| passwordCredentials | [passwordCredential](passwordcredential) collection | The collection of password credentials associated with the application. Not nullable. |
| preferredSingleSignOnMode | string | Specifies the single sign-on mode configured for this application. Microsoft Entra ID uses the preferred single sign-on mode to launch the application from Microsoft 365 or the My Apps portal. The supported values are `password`, `saml`, `notSupported`, and `oidc`. **Note:** This field might be `null` for older SAML apps and for OIDC applications where it isn't set automatically. |
| preferredTokenSigningKeyThumbprint | String | This property can be used on SAML applications (apps that have **preferredSingleSignOnMode** set to `saml`) to control which certificate is used to sign the SAML responses. For applications that aren't SAML, don't write or otherwise rely on this property. |
| replyUrls | String collection | The URLs that user tokens are sent to for sign in with the associated application, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to for the associated application. Not nullable. |
| resourceSpecificApplicationPermissions | [resourceSpecificPermission](resourcespecificpermission) collection | The resource-specific application permissions exposed by this application. Currently, resource-specific permissions are only supported for [Teams apps accessing to specific chats and teams](/en-us/microsoftteams/platform/graph-api/rsc/resource-specific-consent) using Microsoft Graph. Read-only. |
| samlSingleSignOnSettings | [samlSingleSignOnSettings](samlsinglesignonsettings) | The collection for settings related to saml single sign-on. |
| servicePrincipalNames | String collection | Contains the list of **identifiersUris**, copied over from the associated [application](application). Additional values can be added to hybrid applications. These values can be used to identify the permissions exposed by this app within Microsoft Entra ID. For example,<br>- Client apps can specify a resource URI that is based on the values of this property to acquire an access token, which is the URI returned in the "aud" claim.<br><br>The any operator is required for filter expressions on multi-valued properties. Not nullable.  Supports `$filter` (`eq`, `not`, `ge`, `le`, `startsWith`). |
| servicePrincipalType | String | Identifies whether the service principal represents an application, a managed identity, or a legacy application. This property is set by Microsoft Entra ID internally. The **servicePrincipalType** property can be set to three different values: <br>- `Application` - A service principal that represents an application or service. The **appId** property identifies the associated app registration, and matches the **appId** of an [application](application), possibly from a different tenant. If the associated app registration is missing, tokens aren't issued for the service principal.<br>- `ManagedIdentity` - A service principal that represents a [managed identity](/en-us/azure/active-directory/managed-identities-azure-resources/overview). Service principals representing managed identities can be granted access and permissions, but can't be updated or modified directly.<br>- `Legacy` - A service principal that represents an app created before app registrations, or through legacy experiences. A legacy service principal can have credentials, service principal names, reply URLs, and other properties that are editable by an authorized user, but doesn't have an associated app registration. The **appId** value doesn't associate the service principal with an app registration. The service principal can only be used in the tenant where it was created.<br>- `ServiceIdentity` - A service principal that represents an [agent identity](/en-us/graph/api/resources/agentidentity).<br><br>- `SocialIdp` - For internal use. |
| signInAudience | String | Specifies the Microsoft accounts that are supported for the current application. Read-only. Supported values are:<br>- `AzureADMyOrg`: Users with a Microsoft work or school account in my organization's Microsoft Entra tenant (single-tenant).<br>- `AzureADMultipleOrgs`: Users with a Microsoft work or school account in any organization's Microsoft Entra tenant (multitenant).<br>- `AzureADandPersonalMicrosoftAccount`: Users with a personal Microsoft account, or a work or school account in any organization's Microsoft Entra tenant.<br>- `PersonalMicrosoftAccount`: Users with a personal Microsoft account only. |
| tags | String collection | Custom strings that can be used to categorize and identify the service principal. Not nullable. The value is the union of strings set here and on the associated [application](application) entity's **tags** property.Supports `$filter` (`eq`, `not`, `ge`, `le`, `startsWith`). |
| tokenEncryptionKeyId | String | Specifies the keyId of a public key from the keyCredentials collection. When configured, Microsoft Entra ID issues tokens for this application encrypted using the key specified by this property. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user. |
| verifiedPublisher | [verifiedPublisher](verifiedpublisher) | Specifies the verified publisher of the application that's linked to this service principal. |

## Relationships

Important

Specific usage of the `$filter` query parameter is supported only when you use the **ConsistencyLevel** header set to `eventual` and `$count`. For more information, see [Advanced query capabilities on directory objects](/en-us/graph/aad-advanced-queries#user-properties).

| Relationship | Type | Description |
| --- | --- | --- |
| appManagementPolicies | [appManagementPolicy](appmanagementpolicy) collection | The appManagementPolicy applied to this application. |
| appRoleAssignedTo | [appRoleAssignment](approleassignment) | App role assignments for this app or service, granted to users, groups, and other service principals. Supports `$expand`. |
| appRoleAssignments | [appRoleAssignment](approleassignment) collection | App role assignment for another app or service, granted to this service principal. Supports `$expand`. |
| claimsMappingPolicies | [claimsMappingPolicy](claimsmappingpolicy) collection | The claimsMappingPolicies assigned to this service principal. Supports `$expand`. |
| createdObjects | [directoryObject](directoryobject) collection | Directory objects created by this service principal. Read-only. Nullable. |
| federatedIdentityCredentials | [federatedIdentityCredential](federatedidentitycredential) collection | Federated identities for a specific type of service principal - managed identity. Supports `$expand` and `$filter` (`/$count eq 0`, `/$count ne 0`). |
| homeRealmDiscoveryPolicies | [homeRealmDiscoveryPolicy](homerealmdiscoverypolicy) collection | The homeRealmDiscoveryPolicies assigned to this service principal. Supports `$expand`. |
| lifecycle | [microsoft.graph.identityGovernance.identityLifecycle](identitygovernance-identitylifecycle) | The lifecycle policy state of the service principal. Read-only. |
| memberOf | [directoryObject](directoryobject) collection | Roles that this service principal is a member of. HTTP Methods: GET Read-only. Nullable. Supports `$expand`. |
| oauth2PermissionGrants | [oAuth2PermissionGrant](oauth2permissiongrant) collection | Delegated permission grants authorizing this service principal to access an API on behalf of a signed-in user. Read-only. Nullable. |
| ownedObjects | [directoryObject](directoryobject) collection | Directory objects that this service principal owns. Read-only. Nullable. Supports `$expand`, `$select` nested in `$expand`, and `$filter` (`/$count eq 0`, `/$count ne 0`, `/$count eq 1`, `/$count ne 1`). |
| owners | [directoryObject](directoryobject) collection | Directory objects that are owners of this servicePrincipal. The owners are a set of nonadmin users or servicePrincipals who are allowed to modify this object. Supports `$expand`, `$filter` (`/$count eq 0`, `/$count ne 0`, `/$count eq 1`, `/$count ne 1`), and `$select` nested in `$expand`. |
| remoteDesktopSecurityConfiguration | [remoteDesktopSecurityConfiguration](remotedesktopsecurityconfiguration) | The remoteDesktopSecurityConfiguration object applied to this service principal. Supports `$filter` (`eq`) for **isRemoteDesktopProtocolEnabled** property. |
| synchronization | [synchronization](synchronization-synchronization) | Represents the capability for Microsoft Entra identity synchronization through the Microsoft Graph API. |
| tokenIssuancePolicies | [tokenIssuancePolicy](tokenissuancepolicy) collection | The tokenIssuancePolicies assigned to this service principal. |
| tokenLifetimePolicies | [tokenLifetimePolicy](tokenlifetimepolicy) collection | The tokenLifetimePolicies assigned to this service principal. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "accountEnabled": true,
  "addIns": [{"@odata.type": "microsoft.graph.addIn"}],
  "alternativeNames": ["String"] ,
  "appDisplayName": "String",
  "appId": "String",
  "appOwnerOrganizationId": "Guid",
  "appRoleAssignmentRequired": true,
  "appRoles": [{"@odata.type": "microsoft.graph.appRole"}],
  "createdByAppId": "String",
  "customSecurityAttributes": {
    "@odata.type": "microsoft.graph.customSecurityAttributeValue"
  },
  "disabledByMicrosoftStatus": "String",
  "displayName": "String",
  "homepage": "String",
  "id": "String (identifier)",
  "info": {"@odata.type": "microsoft.graph.informationalUrl"},
  "keyCredentials": [{"@odata.type": "microsoft.graph.keyCredential"}],
  "logoutUrl": "String",
  "notes": "String",
  "oauth2PermissionScopes": [{"@odata.type": "microsoft.graph.permissionScope"}],
  "passwordCredentials": [{"@odata.type": "microsoft.graph.passwordCredential"}],
  "preferredTokenSigningKeyThumbprint": "String",
  "replyUrls": ["String"],
  "resourceSpecificApplicationPermissions": [{"@odata.type": "microsoft.graph.resourceSpecificPermission"}],
  "servicePrincipalNames": ["String"],
  "servicePrincipalType": "String",
  "tags": ["String"],
  "tokenEncryptionKeyId": "String",
  "verifiedPublisher": {"@odata.type": "microsoft.graph.verifiedPublisher"}
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/serviceprincipal?view=graph-rest-beta&accept=text/markdown)
