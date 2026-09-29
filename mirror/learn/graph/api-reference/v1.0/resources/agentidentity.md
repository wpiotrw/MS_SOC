---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: agentIdentity resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/agentidentity?view=graph-rest-1.0
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
description: Represents an agent identity in a directory. An agent identity is a specialized type of service principal that represents automated agents or services that can perform actions on behalf of Agent Identity Blueprint or users within the Microsoft Entra ID ecosystem.
ms.date: 2026-08-26T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 3295154b-f0ae-3d1f-0412-93d2a793184a
document_version_independent_id: 38e4e4ff-f9c0-05b3-bb8c-ab4c801f8d47
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/agentidentity.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/agentidentity
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/agentidentity.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 714259de-1c28-767d-5265-ddda499b7638
---

# agentIdentity resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents an agent identity in Microsoft Entra ID. An agent identity is an account used by AI agents to authenticate within the Microsoft Entra ID ecosystem.

Inherits from [servicePrincipal](serviceprincipal).

This resource is an open type that allows additional properties beyond those documented here.

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../agentidentity-list) | [agentidentity](agentidentity) collection | Get a list of the agentidentity objects and their properties. |
| [Create](../agentidentity-post) | [agentidentity](agentidentity) | Create a new agentidentity object. |
| [Get](../agentidentity-get) | [agentIdentity](agentidentity) | Read the properties and relationships of [agentIdentity](agentidentity) object. |
| [Update](../agentidentity-update) | [agentIdentity](agentidentity) | Update the properties of an agentIdentity object. |
| [Delete](../agentidentity-delete) | None | Delete an agentIdentity object. |
| **App role assignments** |  |  |
| [List appRoleAssignedTo](../serviceprincipal-list-approleassignedto) | [appRoleAssignment](approleassignment) collection | Get the users, groups, and agent identities assigned app roles for this agent identity. |
| [List appRoleAssignments](../serviceprincipal-list-approleassignments) | [appRoleAssignment](approleassignment) collection | Get the app roles that this agent identity is assigned. |
| [Create appRoleAssignment](../serviceprincipal-post-approleassignments) | [appRoleAssignment](approleassignment) | Create a new appRoleAssignment object. |
| [Delete appRoleAssignment](../serviceprincipal-delete-approleassignments) | [appRoleAssignment](approleassignment) | Delete an existing appRoleAssignment object. |
| **Delegated permission grants** |  |  |
| [List oauth2PermissionGrants](../serviceprincipal-list-oauth2permissiongrants) | [oAuth2PermissionGrant](oauth2permissiongrant) collection | Get the delegated permission grants authorizing this agent identity to access an API on behalf of a signed-in user. |
| **Deleted items** |  |  |
| [List](../directory-deleteditems-list) | [directoryObject](directoryobject) collection | Retrieve a list of recently deleted agent identities. |
| [Get](../directory-deleteditems-get) | [directoryObject](directoryobject) | Retrieve the properties of a recently deleted agent identity. |
| [Restore](../directory-deleteditems-restore) | [directoryObject](directoryobject) | Restore a recently deleted agent identity. |
| [Permanently delete](../directory-deleteditems-delete) | None | Permanently delete an agent identity. |
| **Directory objects** |  |  |
| [List ownedObjects](../agentidentity-list-ownedobjects) | [directoryObject](directoryobject) collection | Get directory objects owned by this agent identity. |
| **Memberships** |  |  |
| [List direct memberships](../agentidentity-list-memberof) | [directoryObject](directoryobject) collection | Get the groups that this agent identity is a direct member of. |
| [List transitive memberships](../agentidentity-list-transitivememberof) | [directoryObject](directoryobject) collection | Get the groups that this agent identity is a member of. This operation is transitive and includes the groups that this agent identity is a nested member of. |
| **Owners** |  |  |
| [List owners](../agentidentity-list-owners) | [directoryObject](directoryobject) collection | Get the owners of this agent identity. |
| [Add owners](../agentidentity-post-owners) | [directoryObject](directoryobject) | Add owners by posting to the owners collection. |
| [Remove owners](../agentidentity-delete-owners) | None | Remove a [directoryObject](directoryobject) object. |
| **Sponsors** |  |  |
| [List sponsors](../agentidentity-list-sponsors) | [directoryObject](directoryobject) collection | Get the sponsors for this agent identity. |
| [Add sponsors](../agentidentity-post-sponsors) | [directoryObject](directoryobject) | Add sponsors by posting to the sponsors collection. |
| [Remove sponsors](../agentidentity-delete-sponsors) | None | Remove a [directoryObject](directoryobject) object. |

## Properties

Important

While this resource inherits from **servicePrincipal**, some properties are not applicable.

| Property | Type | Description |
| --- | --- | --- |
| odata.type | String | `#microsoft.graph.agentIdentity`. Distinguishes this object as an agent identity. Can be used to identify this object as an agent identity, instead of another kind of service principal. |
| accountEnabled | Boolean | `true` if the agent identity account is enabled; otherwise, `false`. If set to `false`, then no users are able to sign in to this app, even if they're assigned to it. Inherited from [servicePrincipal](serviceprincipal). |
| agentIdentityBlueprintId | String | The **appId** of the agent identity blueprint that defines the configuration for this agent identity. |
| customSecurityAttributes | [customSecurityAttributeValue](customsecurityattributevalue) | An open complex type that holds the value of a custom security attribute that is assigned to a directory object. Nullable. Requires `$select` to retrieve. Inherited from [servicePrincipal](serviceprincipal). |
| createdByAppId | String | The **appId** of the application that created this agent identity. Set internally by Microsoft Entra ID. Read-only. Inherited from [servicePrincipal](serviceprincipal). |
| createdDateTime | DateTimeOffset | The date and time the agent identity was created. Read-only. Inherited from [servicePrincipal](serviceprincipal). |
| disabledByMicrosoftStatus | String | Specifies whether Microsoft has disabled the registered Agent Identity Blueprint. The possible values are: `null` (default value), `NotDisabled`, and `DisabledDueToViolationOfServicesAgreement` (reasons may include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement). Inherited from [servicePrincipal](serviceprincipal). |
| displayName | String | The display name for the agent identity. Inherited from [servicePrincipal](serviceprincipal). |
| id | String | The unique identifier for the agent identity. Inherited from [directoryObject](directoryobject). Key. Not nullable. Read-only. Inherited from [entity](entity). |
| managerApplications | Guid collection | The collection of application IDs designated as managers of this agent identity's backing [agentIdentityBlueprint](agentidentityblueprint). Read-only; the value is server-managed and reflects the **managerApplications** of the backing agentIdentityBlueprint. To change the managers, an owner or administrator must update the **managerApplications** property on the backing agentIdentityBlueprint **in the tenant where it's registered**. For multitenant agent identity blueprints, admins in a tenant where the blueprint is only consumed can't make this change — they must ask an owner or administrator in the blueprint's home tenant. Not nullable. Returned only on `$select`. |
| servicePrincipalType | String | Set to **ServiceIdentity** for all agent identities. Inherited from [servicePrincipal](serviceprincipal). |
| tags | String collection | Custom strings that can be used to categorize and identify the agent identity. Not nullable. The value is the union of strings set here and on the associated Agent Identity Blueprint entity's **tags** property. Inherited from [servicePrincipal](serviceprincipal). |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| appRoleAssignedTo | [appRoleAssignment](approleassignment) collection | App role assignments for this app or service, granted to users, groups, and other agent identities. Supports `$expand`. Inherited from [microsoft.graph.servicePrincipal](serviceprincipal) |
| appRoleAssignments | [appRoleAssignment](approleassignment) collection | App role assignment for another app or service, granted to this agent identity. Supports `$expand`. Inherited from [microsoft.graph.servicePrincipal](serviceprincipal) |
| createdObjects | [directoryObject](directoryobject) collection | Directory objects created by this agent identity. Read-only. Nullable. Inherited from [microsoft.graph.servicePrincipal](serviceprincipal) |
| memberOf | [directoryObject](directoryobject) collection | Roles that this agent identity is a member of. HTTP Methods: GET Read-only. Nullable. Supports `$expand`. Inherited from [microsoft.graph.servicePrincipal](serviceprincipal) |
| oauth2PermissionGrants | [oAuth2PermissionGrant](oauth2permissiongrant) collection | Delegated permission grants authorizing this agent identity to access an API on behalf of a signed-in user. Read-only. Nullable. Inherited from [microsoft.graph.servicePrincipal](serviceprincipal) |
| ownedObjects | [directoryObject](directoryobject) collection | Directory objects that are owned by this agent identity. Read-only. Nullable. Supports `$expand` and `$filter` (`/$count eq 0`, `/$count ne 0`, `/$count eq 1`, `/$count ne 1`). Inherited from [microsoft.graph.servicePrincipal](serviceprincipal) |
| owners | [directoryObject](directoryobject) collection | Directory objects that are owners of this agent identity. The owners are a set of nonadmin users or agent identities who are allowed to modify this object. Supports `$expand` and `$filter` (`/$count eq 0`, `/$count ne 0`, `/$count eq 1`, `/$count ne 1`). Inherited from [microsoft.graph.servicePrincipal](serviceprincipal) |
| sponsors | [directoryObject](directoryobject) collection | The sponsors for this agent identity. |

## JSON representation

The following JSON representation shows the resource type. Only a subset of all properties are returned by default. All other properties can only be retrieved using $select.

```json
{
  "@odata.type": "#microsoft.graph.agentIdentity",
  "id": "String (identifier)",
  "accountEnabled": "Boolean",
  "agentIdentityBlueprintId": "String",
  "createdByAppId": "String",
  "createdDateTime": "String (timestamp)",
  "disabledByMicrosoftStatus": "String",
  "displayName": "String",
  "managerApplications": [
    "Guid"
  ],
  "servicePrincipalType": "String",
  "tags": [
    "String"
  ]
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/agentidentity?view=graph-rest-beta&accept=text/markdown)
