---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: agentIdentityBlueprintPrincipal resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/agentidentityblueprintprincipal?view=graph-rest-1.0
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
description: Represents an agent identity blueprint principal in a directory. An Agent Identity Blueprint principal is a specialized service principal that serves as the parent blueprint for creating agent identity instances within the Microsoft Entra ID ecosystem.
ms.date: 2026-08-26T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 824b6c14-6f27-76ba-4f3a-b9d370305767
document_version_independent_id: c58c5230-6154-71f8-4de3-c609f9d542f2
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/agentidentityblueprintprincipal.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/agentidentityblueprintprincipal
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/agentidentityblueprintprincipal.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 26995eac-1cdf-7348-1c84-91bb3dca9fa1
---

# agentIdentityBlueprintPrincipal resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents an agent identity blueprint principal in a tenant. An agent identity blueprint principal is instantiated from an [agentIdentityBlueprint](agentidentityblueprint) object and is used to create [agent identities](agentidentity) within a Microsoft Entra ID tenant, and perform various identity management operations that affect all agent identities created.

Inherits from [servicePrincipal](serviceprincipal).

This resource is an open type that allows additional properties beyond those documented here.

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../agentidentityblueprintprincipal-list) | [agentIdentityBlueprintPrincipal](agentidentityblueprintprincipal) collection | Get a list of the agentIdentityBlueprintPrincipal objects and their properties. |
| [Create](../agentidentityblueprintprincipal-post) | [agentIdentityBlueprintPrincipal](agentidentityblueprintprincipal) | Create a new agentIdentityBlueprintPrincipal object. |
| [Get](../agentidentityblueprintprincipal-get) | [agentIdentityBlueprintPrincipal](agentidentityblueprintprincipal) | Read the properties and relationships of [agentIdentityBlueprintPrincipal](agentidentityblueprintprincipal) object. |
| [Update](../agentidentityblueprintprincipal-update) | [agentIdentityBlueprintPrincipal](agentidentityblueprintprincipal) | Update the properties of an agentIdentityBlueprintPrincipal object. |
| [Delete](../agentidentityblueprintprincipal-delete) | None | Delete an agentIdentityBlueprintPrincipal object. |
| **App role assignments** |  |  |
| [List app role assigned to](../serviceprincipal-list-approleassignedto) | [appRoleAssignment](approleassignment) collection | Get the users, groups, and agent identities assigned app roles for this agent identity blueprint principal. |
| [Add app role assigned to](../serviceprincipal-post-approleassignedto) | [appRoleAssignment](approleassignment) | Assign an app role for this agent identity blueprint principal to a user, group, or service principal. |
| [Remove app role assigned to](../serviceprincipal-delete-approleassignedto) | None | Remove an app role assignment for this agent identity blueprint principal from a user, group, or service principal. |
| [List app role assignments](../serviceprincipal-list-approleassignments) | [appRoleAssignment](approleassignment) collection | Get the app roles that this agent identity blueprint principal is assigned. |
| [Add app role assignment](../serviceprincipal-post-approleassignments) | [appRoleAssignment](approleassignment) | Assign an app role to this agent identity blueprint principal. |
| [Remove app role assignment](../serviceprincipal-delete-approleassignments) | None | Remove an app role assignment from this agent identity blueprint principal. |
| **Delegated permission grants** |  |  |
| [List OAuth 2.0 permission grants](../serviceprincipal-list-oauth2permissiongrants) | [oAuth2PermissionGrant](oauth2permissiongrant) collection | Get the delegated permission grants authorizing this agent identity blueprint principal to access an API on behalf of a signed-in user. |
| **Deleted items** |  |  |
| [List](../directory-deleteditems-list) | [directoryObject](directoryobject) collection | Retrieve a list of recently deleted agent identities. |
| [Get](../directory-deleteditems-get) | [directoryObject](directoryobject) | Retrieve the properties of a recently deleted agent identity. |
| [Restore](../directory-deleteditems-restore) | [directoryObject](directoryobject) | Restore a recently deleted agent identity. |
| [Permanently delete](../directory-deleteditems-delete) | None | Permanently delete an agent identity. |
| **Directory objects** |  |  |
| [List owned objects](../agentidentityblueprintprincipal-list-ownedobjects) | [directoryObject](directoryobject) collection | Get directory objects owned by this agent identity blueprint principal. |
| [List created objects](../agentidentityblueprintprincipal-list-createdobjects) | [directoryObject](directoryobject) collection | Get directory objects created by this agent identity blueprint principal. |
| **Memberships** |  |  |
| [List member of](../agentidentityblueprintprincipal-list-memberof) | [directoryObject](directoryobject) collection | Get the groups that this agent identity blueprint principal is a direct member of. |
| **Owners** |  |  |
| [List owners](../agentidentityblueprintprincipal-list-owners) | [directoryObject](directoryobject) collection | Get the owners of this agent identity blueprint principal. |
| [Add owners](../agentidentityblueprintprincipal-post-owners) | None | Assign an owner to this agent identity blueprint principal. |
| [Remove owners](../agentidentityblueprintprincipal-delete-owners) | None | Remove an owner from this agent identity blueprint principal. |
| **Sponsors** |  |  |
| [List sponsors](../agentidentityblueprintprincipal-list-sponsors) | [directoryObject](directoryobject) collection | Get the sponsors for this agent identity blueprint principal. |
| [Add sponsors](../agentidentityblueprintprincipal-post-sponsors) | [directoryObject](directoryobject) | Add sponsors by posting to the sponsors collection. |
| [Remove sponsors](../agentidentityblueprintprincipal-delete-sponsors) | None | Remove a [directoryObject](directoryobject) object. |

## Properties

Important

While this resource inherits from **servicePrincipal**, some properties are not applicable and return `null` or default values. These properties are excluded from the table below.

| Property | Type | Description |
| --- | --- | --- |
| accountEnabled | Boolean | `true` if the agent identity blueprint principal account is enabled; otherwise, `false`. If set to `false`, then no users are able to sign in to this app, even if they're assigned to it. Inherited from [servicePrincipal](serviceprincipal). |
| appDescription | String | The description exposed by the associated agent identity blueprint. Inherited from [servicePrincipal](serviceprincipal). |
| appDisplayName | String | The display name exposed by the associated agent identity blueprint. Maximum length is 256 characters. Inherited from [servicePrincipal](serviceprincipal). |
| appId | String | The **appId** of the associated agent identity blueprint. Alternate key. Inherited from [servicePrincipal](serviceprincipal). |
| appOwnerOrganizationId | Guid | Contains the tenant ID where the agent identity blueprint is registered. This is applicable only to agent identity blueprint principals backed by applications. Inherited from [servicePrincipal](serviceprincipal). |
| appRoleAssignmentRequired | Boolean | Specifies whether users or other service principals need to be granted an app role assignment for this agent identity blueprint principal before users can sign in or apps can get tokens. The default value is `false`. Not nullable. Inherited from [servicePrincipal](serviceprincipal). |
| appRoles | [appRole](approle) collection | The roles exposed by the agent identity blueprint, which this agent identity blueprint principal represents. For more information, see the **appRoles** property definition on the application entity. Not nullable. Inherited from [servicePrincipal](serviceprincipal). |
| createdByAppId | String | The **appId** of the application that created this agent identity blueprint principal. Set internally by Microsoft Entra ID. Read-only. Inherited from [servicePrincipal](serviceprincipal). |
| disabledByMicrosoftStatus | String | Specifies whether Microsoft has disabled the registered agent identity blueprint. The possible values are: `null` (default value), `NotDisabled`, and `DisabledDueToViolationOfServicesAgreement` (reasons may include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement). Inherited from [servicePrincipal](serviceprincipal). |
| displayName | String | The display name for the agent identity blueprint principal. Inherited from [servicePrincipal](serviceprincipal). |
| id | String | The unique identifier for the agent identity blueprint principal. Inherited from [entity](entity). Key. Not nullable. Read-only. |
| info | [informationalUrl](informationalurl) | Basic profile information of the acquired application such as app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. Inherited from [servicePrincipal](serviceprincipal). |
| managerApplications | Guid collection | The collection of application IDs designated as managers of this agent identity blueprint principal's backing [agentIdentityBlueprint](agentidentityblueprint). Read-only; the value is server-managed and reflects the **managerApplications** of the backing agentIdentityBlueprint. To change the managers, an owner or administrator must update the **managerApplications** property on the backing agentIdentityBlueprint **in the tenant where it's registered**. For multitenant agent identity blueprints, admins in a tenant where the blueprint is only consumed can't make this change — they must ask an owner or administrator in the blueprint's home tenant. Not nullable. Returned only on `$select`. |
| publishedPermissionScopes | [permissionScope](permissionscope) collection | The delegated permissions exposed by the application. For more information, see the **oauth2PermissionScopes** property on the agent identity blueprint entity's **api** property. Not nullable. Inherited from [servicePrincipal](serviceprincipal). |
| publisherName | String | The name of the Microsoft Entra tenant that published the application. Inherited from [servicePrincipal](serviceprincipal). |
| servicePrincipalNames | String collection | Contains the list of **identifiersUris**, copied over from the associated agent identity blueprint. More values can be added to hybrid agent identity blueprint. These values can be used to identify the permissions exposed by this app within Microsoft Entra ID. Not nullable. **Property blocked on Agent Identity Blueprint Principal.** Inherited from [servicePrincipal](serviceprincipal). |
| servicePrincipalType | String | Identifies if the agent identity blueprint principal represents an application. This is set by Microsoft Entra ID internally. For an agent identity blueprint principal that represents an application this is set as **Application**. Inherited from [servicePrincipal](serviceprincipal). |
| signInAudience | String | Specifies the Microsoft accounts that are supported for the current agent identity blueprint. Read-only. Supported values are: `AzureADMyOrg`, `AzureADMultipleOrgs`, `AzureADandPersonalMicrosoftAccount`, and `PersonalMicrosoftAccount`. Inherited from [servicePrincipal](serviceprincipal). |
| tags | String collection | Custom strings that can be used to categorize and identify the agent identity blueprint principal. Not nullable. The value is the union of strings set here and on the associated agent identity blueprint entity's **tags** property. Inherited from [servicePrincipal](serviceprincipal). |
| verifiedPublisher | [verifiedPublisher](verifiedpublisher) | Specifies the verified publisher of the application that's linked to this agent identity blueprint principal. Inherited from [servicePrincipal](serviceprincipal). |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| appManagementPolicies | [appManagementPolicy](appmanagementpolicy) collection | The appManagementPolicy applied to this agent identity blueprint principal. Inherited from [microsoft.graph.servicePrincipal](serviceprincipal) |
| appRoleAssignedTo | [appRoleAssignment](approleassignment) collection | App role assignments for this agent identity blueprint principal, granted to users, groups, and other service principals. Supports `$expand`. Inherited from [microsoft.graph.servicePrincipal](serviceprincipal) |
| appRoleAssignments | [appRoleAssignment](approleassignment) collection | App role assignment for another app or service, granted to this agent identity blueprint principal. Supports `$expand`. Inherited from [microsoft.graph.servicePrincipal](serviceprincipal) |
| createdObjects | [directoryObject](directoryobject) collection | Directory objects created by this agent identity blueprint principal. Read-only. Nullable. Inherited from [microsoft.graph.servicePrincipal](serviceprincipal) |
| memberOf | [directoryObject](directoryobject) collection | Roles that this agent identity blueprint principal is a member of. HTTP Methods: GET Read-only. Nullable. Supports `$expand`. Inherited from [microsoft.graph.servicePrincipal](serviceprincipal) |
| oauth2PermissionGrants | [oAuth2PermissionGrant](oauth2permissiongrant) collection | Delegated permission grants authorizing this agent identity blueprint principal to access an API on behalf of a signed-in user. Read-only. Nullable. Inherited from [microsoft.graph.servicePrincipal](serviceprincipal) |
| ownedObjects | [directoryObject](directoryobject) collection | Directory objects that are owned by this agent identity blueprint principal. Read-only. Nullable. Supports `$expand` and `$filter` (`/$count eq 0`, `/$count ne 0`, `/$count eq 1`, `/$count ne 1`). Inherited from [microsoft.graph.servicePrincipal](serviceprincipal) |
| owners | [directoryObject](directoryobject) collection | Directory objects that are owners of this agent identity blueprint principal. The owners are a set of nonadmin users or servicePrincipals who are allowed to modify this object. Supports `$expand` and `$filter` (`/$count eq 0`, `/$count ne 0`, `/$count eq 1`, `/$count ne 1`). Inherited from [microsoft.graph.servicePrincipal](serviceprincipal) |
| sponsors | [directoryObject](directoryobject) collection | The sponsors for this agent identity blueprint principal. Sponsors are users or service principals who can authorize and manage the lifecycle of agent identity instances. |

## JSON representation

The following JSON representation shows the resource type. Only a subset of all properties are returned by default. All other properties can only be retrieved using `$select`.

```json
{
  "@odata.type": "#microsoft.graph.agentIdentityBlueprintPrincipal",
  "id": "String (identifier)",
  "accountEnabled": "Boolean",
  "createdByAppId": "String",
  "appDescription": "String",
  "appDisplayName": "String",
  "appId": "String",
  "appOwnerOrganizationId": "Guid",
  "appRoleAssignmentRequired": "Boolean",
  "disabledByMicrosoftStatus": "String",
  "displayName": "String",
  "publisherName": "String",
  "servicePrincipalNames": [
    "String"
  ],
  "servicePrincipalType": "String",
  "signInAudience": "String",
  "tags": [
    "String"
  ],
  "appRoles": [
    {
      "@odata.type": "microsoft.graph.appRole"
    }
  ],
  "info": {
    "@odata.type": "microsoft.graph.informationalUrl"
  },
  "managerApplications": [
    "Guid"
  ],
  "publishedPermissionScopes": [
    {
      "@odata.type": "microsoft.graph.permissionScope"
    }
  ],
  "verifiedPublisher": {
    "@odata.type": "microsoft.graph.verifiedPublisher"
  }
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/agentidentityblueprintprincipal?view=graph-rest-beta&accept=text/markdown)
