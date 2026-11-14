---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: agentIdentityBlueprint resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/agentidentityblueprint?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: zallison22
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-agent-id
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: An agent identity blueprint is a specialized application type that serves as the template for creating agent identity instances within the Microsoft Entra ID ecosystem.
ms.date: 2026-03-31T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 9d7eb421-a871-57a0-96de-562261852926
document_version_independent_id: 0227a1f6-cffc-9f2f-ed12-545c3ac5b215
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/agentidentityblueprint.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/agentidentityblueprint
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/agentidentityblueprint.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 9e5c4507-6502-8976-7ce7-c2e5dc58efdb
---

# agentIdentityBlueprint resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

An agent identity blueprint serves as a template for creating agent identities within the Microsoft Entra ID ecosystem.

Inherits from [application](application).

This resource is an open type that allows additional properties beyond those documented here.

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../agentidentityblueprint-list) | [agentIdentityBlueprint](agentidentityblueprint) collection | Get a list of the agentIdentityBlueprint objects and their properties. |
| [Create](../agentidentityblueprint-post) | [agentIdentityBlueprint](agentidentityblueprint) | Create (register) a new agentIdentityBlueprint. |
| [Get](../agentidentityblueprint-get) | [agentIdentityBlueprint](agentidentityblueprint) | Read the properties and relationships of [agentIdentityBlueprint](agentidentityblueprint) object. |
| [Update](../agentidentityblueprint-update) | [agentIdentityBlueprint](agentidentityblueprint) | Update the properties of an agentIdentityBlueprint object. |
| [Upsert](../agentidentityblueprint-upsert) | [agentIdentityBlueprint](agentidentityblueprint) | Create a new agent identity blueprint if it doesn't exist, or update the properties of an existing blueprint. |
| [Delete](../agentidentityblueprint-delete) | None | Delete an agentIdentityBlueprint object. |
| **Credentials** |  |  |
| [Add password](../agentidentityblueprint-addpassword) | [passwordCredential](passwordcredential) | Add a strong password or secret to an agent identity blueprint. |
| [Remove password](../agentidentityblueprint-removepassword) | [passwordCredential](passwordcredential) | Remove a password or secret from an agent identity blueprint. |
| [Add key](../agentidentityblueprint-addkey) | [keyCredential](keycredential) | Add a key credential to an agent identity blueprint. |
| [Remove key](../agentidentityblueprint-removekey) | None | Remove a key credential from an agent identity blueprint. |
| [List federated identity credential](../federatedidentitycredential-list) | [federatedIdentityCredential](federatedidentitycredential) collection | Get a list of the [federatedIdentityCredential](federatedidentitycredential) objects and their properties. |
| [Create federated identity credential](../federatedidentitycredential-post) | [federatedIdentityCredential](federatedidentitycredential) | Create a new [federatedIdentityCredential](federatedidentitycredential) object. |
| [Get federated identity credential](../federatedidentitycredential-get) | [federatedIdentityCredential](federatedidentitycredential) | Read the properties and relationships of a [federatedIdentityCredential](federatedidentitycredential) object. |
| [Update federated identity credential](../federatedidentitycredential-update) | None | Update the properties of a [federatedIdentityCredential](federatedidentitycredential) object. |
| [Upsert federated identity credential](../federatedidentitycredential-upsert) | [federatedIdentityCredential](federatedidentitycredential) | Create a new [federatedIdentityCredential](federatedidentitycredential) if it doesn't exist, or update the properties of an existing [federatedIdentityCredential](federatedidentitycredential) object. |
| [Delete federated identity credential](../federatedidentitycredential-delete) | None | Delete a [federatedIdentityCredential](federatedidentitycredential) object. |
| **Deleted items** |  |  |
| [List](../directory-deleteditems-list) | [directoryObject](directoryobject) collection | Retrieve a list of recently deleted agent identities. |
| [Get](../directory-deleteditems-get) | [directoryObject](directoryobject) | Retrieve the properties of a recently deleted agent identity. |
| [Restore](../directory-deleteditems-restore) | [directoryObject](directoryobject) | Restore a recently deleted agent identity. |
| [Permanently delete](../directory-deleteditems-delete) | None | Permanently delete an agent identity. |
| **Owners** |  |  |
| [List owners](../agentidentityblueprint-list-owners) | [directoryObject](directoryobject) collection | Get the owners of this agent identity blueprint principal. |
| [Add owners](../agentidentityblueprint-post-owners) | [directoryObject](directoryobject) | Assign an owner to this agent identity blueprint principal. |
| [Remove owners](../agentidentityblueprint-delete-owners) | None | Remove an owner from this agent identity blueprint principal. |
| **Sponsors** |  |  |
| [List sponsors](../agentidentityblueprint-list-sponsors) | [directoryObject](directoryobject) collection | Get the sponsors for this agent identity blueprint. Sponsors are users or service principals who can authorize and manage the lifecycle of agent identity instances. |
| [Add sponsors](../agentidentityblueprint-post-sponsors) | [directoryObject](directoryobject) | Add sponsors by posting to the sponsors collection. |
| [Remove sponsors](../agentidentityblueprint-delete-sponsors) | None | Remove a [directoryObject](directoryobject) object. |
| **Verified publisher** |  |  |
| [Set](../agentidentityblueprint-setverifiedpublisher) | None | Set the verified publisher of an application. |
| [Unset](../agentidentityblueprint-unsetverifiedpublisher) | None | Unset the verified publisher of an application. |

## Properties

Important

While this resource inherits from **application**, some properties are not applicable and return `null` or default values. These properties are excluded from the table below.

| Property | Type | Description |
| --- | --- | --- |
| api | [apiApplication](apiapplication) | Specifies settings for an agent identity blueprint that implements a web API. Inherited from [application](application). |
| appId | String | The unique identifier for the agent identity blueprint that is assigned by Microsoft Entra ID. Not nullable. Read-only. Inherited from [application](application). |
| appRoles | [appRole](approle) collection | The collection of roles defined for the agent identity blueprint. With app role assignments, these roles can be assigned to users, groups, or service principals associated with other applications. Not nullable. Inherited from [application](application). |
| certification | [certification](certification) | Specifies the certification status of the agent identity blueprint. Inherited from [application](application). |
| createdByAppId | String | The **appId** of the application that created this agent identity blueprint. Set internally by Microsoft Entra ID. Read-only. Inherited from [application](application). |
| createdDateTime | DateTimeOffset | The date and time the agent identity blueprint was registered. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. Read-only. Inherited from [application](application). |
| description | String | Free text field to provide a description of the agent identity blueprint to end users. The maximum allowed size is 1,024 characters. The least privileged permission to update this property is *AgentIdentityBlueprint.UpdateBranding.All*. Inherited from [application](application). |
| disabledByMicrosoftStatus | String | Specifies whether Microsoft has disabled the registered agent identity blueprint. The possible values are: `null` (default value), `NotDisabled`, and `DisabledDueToViolationOfServicesAgreement` (reasons may include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement). Inherited from [application](application). |
| displayName | String | The display name for the agent identity blueprint. Maximum length is 256 characters. The least privileged permission to update this property is *AgentIdentityBlueprint.UpdateBranding.All*. Inherited from [application](application). |
| groupMembershipClaims | String | Configures the `groups` claim issued in a user or OAuth 2.0 access token that the agent identity blueprint expects. To set this attribute, use one of the following string values: `None`, `SecurityGroup` (for security groups and Microsoft Entra roles), `All` (this gets all security groups, distribution groups, and Microsoft Entra directory roles that the signed-in user is a member of). Inherited from [application](application). |
| id | String | Unique identifier for the agent identity blueprint object. This property is referred to as **Object ID** in the Microsoft Entra admin center. Key. Not nullable. Read-only. Inherited from [directoryObject](directoryobject). |
| identifierUris | String collection | Also known as App ID URI, this value is set when an agent identity blueprint is used as a resource app. The identifierUris acts as the prefix for the scopes you reference in your API's code, and it must be globally unique across Microsoft Entra ID. Not nullable. Inherited from [application](application). |
| info | [informationalUrl](informationalurl) | Basic profile information of the agent identity blueprint, such as it's marketing, support, terms of service, and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. Inherited from [application](application). |
| keyCredentials | [keyCredential](keycredential) collection | The collection of key credentials associated with the agent identity blueprint. Not nullable. The least privileged permission to update this property is *AgentIdentityBlueprint.AddRemoveCreds.All*. Inherited from [application](application). |
| managerApplications | Guid collection | A collection of application IDs for Microsoft first-party applications designated as managers of this agent blueprint. Manager applications can create agent blueprint principals, agent identities, and agent users for managed agent blueprints without requiring highly privileged permissions such as `AgentIdentityBlueprintPrincipal.ReadWrite.All`. Limited to a maximum of 10 entries. Not nullable. Only Microsoft first-party applications can be designated as managers. Not returned by default. Supports `$select`. |
| optionalClaims | [optionalClaims](optionalclaims) | Application developers can configure optional claims in their Microsoft Entra agent identity blueprints to specify the claims that are sent to their application by the Microsoft security token service. Inherited from [application](application). |
| passwordCredentials | [passwordCredential](passwordcredential) collection | The collection of password credentials associated with the agent identity blueprint. Not nullable. The least privileged permission to update this property is *AgentIdentityBlueprint.AddRemoveCreds.All*. Inherited from [application](application).You can also add passwords after creating the agent identity blueprint by calling the [Add password](../agentidentityblueprint-addpassword) API. |
| publisherDomain | String | The verified publisher domain for the agent identity blueprint. Read-only. Inherited from [application](application). |
| requiredResourceAccess | [requiredResourceAccess](requiredresourceaccess) collection | Specifies the resources that the agentIdentityBlueprint needs to access. This property also specifies the set of delegated permissions and application roles that it needs for each of those resources. This configuration of access to the required resources drives the consent experience. No more than 50 resource services (APIs) can be configured. The total number of required permissions must not exceed 400. For more information, see Limits on requested permissions per app. Not nullable. Inherited from [application](application).Supports `$filter` (`eq`, `not`, `ge`, `le`). |
| serviceManagementReference | String | References application or service contact information from a Service or Asset Management database. Nullable. Inherited from [application](application). |
| signInAudience | String | Specifies the Microsoft accounts that are supported for the current agent identity blueprint. The possible values are: `AzureADMyOrg` (default), `AzureADMultipleOrgs`, `AzureADandPersonalMicrosoftAccount`, and `PersonalMicrosoftAccount`. Inherited from [application](application). |
| tags | String collection | Custom strings that can be used to categorize and identify the agent identity blueprint. Not nullable. Inherited from [application](application). |
| tokenEncryptionKeyId | Guid | Specifies the keyId of a public key from the keyCredentials collection. When configured, Microsoft Entra ID encrypts all the tokens it emits by using the key this property points to. Inherited from [application](application). |
| uniqueName | String | The unique identifier that can be assigned to an agent identity blueprint and used as an alternate key. Immutable. Read-only. Inherited from [application](application). |
| verifiedPublisher | [verifiedPublisher](verifiedpublisher) | Specifies the verified publisher of the agent identity blueprint. Inherited from [application](application). |
| web | [webApplication](webapplication) | Specifies settings for a web application. Inherited from [application](application). |

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

| Relationship | Type | Description |
| --- | --- | --- |
| appManagementPolicies | [appManagementPolicy](appmanagementpolicy) collection | The appManagementPolicy applied to this agent identity blueprint. Inherited from [microsoft.graph.application](application) |
| federatedIdentityCredentials | [federatedIdentityCredential](federatedidentitycredential) collection | Federated identities for agent identity blueprints. Inherited from [microsoft.graph.application](application) |
| inheritablePermissions | [inheritablePermission](inheritablepermission) collection | Defines scopes of a resource application that may be automatically granted to agent identities without additional consent. |
| owners | [directoryObject](directoryobject) collection | Directory objects that are owners of this agent identity blueprint. The owners are a set of nonadmin users or service principals allowed to modify this object. Read-only. Nullable. Inherited from [microsoft.graph.application](application) |
| sponsors | [directoryObject](directoryobject) collection | The sponsors for this agent identity blueprint. Sponsors are users or groups who can authorize and manage the lifecycle of agent identity instances. Required during the create operation. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.agentIdentityBlueprint",
  "id": "String (identifier)",
  "appId": "String",
  "identifierUris": ["String"],
  "createdByAppId": "String",
  "createdDateTime": "String (timestamp)",
  "description": "String",
  "disabledByMicrosoftStatus": "String",
  "displayName": "String",
  "groupMembershipClaims": "String",
  "publisherDomain": "String",
  "requiredResourceAccess": [{"@odata.type": "microsoft.graph.requiredResourceAccess"}],
  "signInAudience": "String",
  "tags": ["String"],
  "tokenEncryptionKeyId": "Guid",
  "uniqueName": "String",
  "serviceManagementReference": "String",
  "certification": {
    "@odata.type": "microsoft.graph.certification"
  },
  "optionalClaims": {
    "@odata.type": "microsoft.graph.optionalClaims"
  },
  "api": {
    "@odata.type": "microsoft.graph.apiApplication"
  },
  "appRoles": [
    {
      "@odata.type": "microsoft.graph.appRole"
    }
  ],
  "info": {
    "@odata.type": "microsoft.graph.informationalUrl"
  },
  "keyCredentials": [
    {
      "@odata.type": "microsoft.graph.keyCredential"
    }
  ],
  "managerApplications": ["Guid"],
  "passwordCredentials": [
    {
      "@odata.type": "microsoft.graph.passwordCredential"
    }
  ],
  "verifiedPublisher": {
    "@odata.type": "microsoft.graph.verifiedPublisher"
  },
  "web": {
    "@odata.type": "microsoft.graph.webApplication"
  }
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/agentidentityblueprint?view=graph-rest-beta&accept=text/markdown)
