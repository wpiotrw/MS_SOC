---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: directory resource type (deleted items) - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/directory?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: vimranga
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-directory-management
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a deleted item in the directory.
ms.localizationpriority: medium
doc_type: resourcePageType
toc.title: Deleted item
ms.date: 2026-08-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1028
locale: en-us
document_id: 8a884201-4e6d-133c-d205-1714e7900962
document_version_independent_id: 684d97da-56b9-8dda-1abc-409cebcba6c9
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/directory.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/directory
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/directory.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: e89d73c6-f1a7-c1c8-4255-e9e670a1ddaf
---

# directory resource type (deleted items) - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents a deleted item in the directory. When an item is deleted, it moves to the deleted items container. Deleted items remain available to restore for up to 30 days. After 30 days, the items are permanently deleted.

Currently, deleted items functionality is supported for the the following resources:

- [application](application)
- [agentIdentityBlueprint](agentidentityblueprint)
- [agentIdentity](agentidentity)
- [agentIdentityBlueprintPrincipal](agentidentityblueprintprincipal)
- [group](group)
- [servicePrincipal](serviceprincipal)
- [user](user)

Inherits from [entity](entity).

## Methods

| Method | Return Type | Description |
| --- | --- | --- |
| [List](../directory-deleteditems-list) | [directoryObject](directoryobject) collection | Gets a list of recently deleted items. |
| [List remote tenant groups](../directory-list-remotetenantgroups) | [remoteTenantGroup](remotetenantgroup) collection | Gets a list of the remote tenant groups in the directory. |
| [Get](../directory-deleteditems-get) | [directoryObject](directoryobject) | Gets the properties of a deleted item. |
| [Restore](../directory-deleteditems-restore) | [directoryObject](directoryobject) | Restores a recently deleted item. |
| [Permanently delete](../directory-deleteditems-delete) | None | Permanently deletes an item. |
| [List deleted items owned by user](../directory-deleteditems-getuserownedobjects) | [directoryObject](directoryobject) collection | Lists directory items owned by a user. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| id | String | A unique identifier for the object; for example, `12345678-9abc-def0-1234-56789abcde`. Key. Not nullable. Read-only. Inherited from [entity](entity). |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| administrativeUnits | [administrativeUnit](administrativeunit) collection | Conceptual container for user and group directory objects. |
| attributeSets | [attributeSet](attributeset) collection | Group of related custom security attribute definitions. |
| customSecurityAttributeDefinitions | [customSecurityAttributeDefinition](customsecurityattributedefinition) collection | Schema of a custom security attributes (key-value pairs). |
| deletedItems | [directoryObject](directoryobject) collection | Recently deleted items. Read-only. Nullable. |
| deviceLocalCredentials | [deviceLocalCredential](devicelocalcredential) collection | The credentials of the device's local administrator account backed up to Microsoft Entra ID. |
| federationConfigurations | [identityProviderBase](identityproviderbase) collection | Configure domain federation with organizations whose identity provider (IdP) supports either the SAML or WS-Fed protocol. |
| onPremisesSynchronization | [onPremisesDirectorySynchronization](onpremisesdirectorysynchronization) | A container for on-premises directory synchronization functionalities that are available for the organization. |
| publicKeyInfrastructure | [publicKeyInfrastructureRoot](publickeyinfrastructureroot) | The collection of public key infrastructure instances for the certificate-based authentication feature for users in a Microsoft Entra tenant. |
| remoteTenantGroups | [remoteTenantGroup](remotetenantgroup) collection | Collection of groups in remote Microsoft Entra tenants that are available in the directory. |
| subscriptions | [companySubscription](companysubscription) collection | List of commercial subscriptions that an organization acquired. |
| tenantGovernance | [microsoft.graph.tenantGovernance](tenantgovernanceservices-tenantgovernance) | Container for Microsoft Entra Tenant Governance capabilities. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.directory"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/directory?view=graph-rest-beta&accept=text/markdown)
