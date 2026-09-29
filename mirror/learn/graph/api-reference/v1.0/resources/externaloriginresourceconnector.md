---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: externalOriginResourceConnector resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/externaloriginresourceconnector?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: vikama-microsoft
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a connector used to communicate with external resource systems.
ms.date: 2026-07-22T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 08184976-1571-d962-eb48-c5aa173da471
document_version_independent_id: 713abcdd-976d-55db-a6fc-1831b7206ae3
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/externaloriginresourceconnector.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/externaloriginresourceconnector
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/externaloriginresourceconnector.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac4b7417-d4c2-43d4-94bf-f22fa1416b34
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/68876bab-7da4-4e70-b295-395b3a255a1f
platformId: 22863ead-32f2-95b1-15c6-aa610c93a9b4
---

# externalOriginResourceConnector resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents a connector used to communicate with an external resource system in Microsoft Entra ID Governance. The connector integrates with SAP Identity Access Governance (SAP IAG) to enable access management and governance for resources that originate in that system.

Inherits from [entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../entitlementmanagement-list-externaloriginresourceconnectors) | [externalOriginResourceConnector](externaloriginresourceconnector) collection | Get a list of the [externalOriginResourceConnector](externaloriginresourceconnector) objects and their properties. |
| [Create](../entitlementmanagement-post-externaloriginresourceconnectors) | [externalOriginResourceConnector](externaloriginresourceconnector) | Create a new [externalOriginResourceConnector](externaloriginresourceconnector) object. |
| [Get](../externaloriginresourceconnector-get) | [externalOriginResourceConnector](externaloriginresourceconnector) | Read the properties and relationships of an [externalOriginResourceConnector](externaloriginresourceconnector) object. |
| [Update](../externaloriginresourceconnector-update) | [externalOriginResourceConnector](externaloriginresourceconnector) | Update the properties of an [externalOriginResourceConnector](externaloriginresourceconnector) object. |
| [Delete](../externaloriginresourceconnector-delete) | None | Delete an [externalOriginResourceConnector](externaloriginresourceconnector) object. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| connectionInfo | [connectionInfo](connectioninfo) | The connection information used to communicate with the external resource system. When **connectorType** is `sapIag`, the type is [externalTokenBasedSapIagConnectionInfo](externaltokenbasedsapiagconnectioninfo). |
| connectorType | connectorType | The type of connector to SAP being used. The possible values are: `sapIag` (SAP Cloud Identity Access Governance), `unknownFutureValue`. |
| createdBy | String | The identifier of the user or application that created the connector. |
| createdDateTime | DateTimeOffset | The date and time when the connector was created. |
| description | String | A description of the connector. |
| displayName | String | The display name of the connector. |
| id | String | The unique identifier of the connector. Inherited from [entity](entity). |
| modifiedBy | String | The identifier of the user or application that last modified the connector. |
| modifiedDateTime | DateTimeOffset | The date and time when the connector was last modified. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.externalOriginResourceConnector",
  "id": "String (identifier)",
  "displayName": "String",
  "description": "String",
  "connectorType": "String",
  "connectionInfo": {
    "@odata.type": "microsoft.graph.connectionInfo"
  },
  "createdBy": "String",
  "createdDateTime": "String (timestamp)",
  "modifiedBy": "String",
  "modifiedDateTime": "String (timestamp)"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/externaloriginresourceconnector?view=graph-rest-beta&accept=text/markdown)
