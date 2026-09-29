---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: auditLogQuery resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/security-auditlogquery?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: imsandhya7-spec
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a query against the Microsoft 365 unified audit log.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-06-17T00:00:00.0000000Z
toc.title: Audit log query
locale: en-us
document_id: adaedd12-d801-a47a-ee35-15e7e0c3dcc3
document_version_independent_id: affa0267-44d0-4a42-0e34-2ebdafe69614
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/security-auditlogquery.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/security-auditlogquery
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/security-auditlogquery.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
platformId: dde4ef62-baf9-9882-907c-84e8d226dccb
---

# auditLogQuery resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.security

Represents a query against the Microsoft 365 unified audit log. Use this resource to define search parameters and retrieve audit log records.

Inherits from [microsoft.graph.entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [Get audit log query](../security-auditlogquery-get) | [auditLogQuery](security-auditlogquery) | Read the properties and relationships of an [auditLogQuery](security-auditlogquery) object. |
| [List records](../security-auditlogquery-list-records) | [auditLogRecord](security-auditlogrecord) collection | Get the auditLogRecord resources from the records navigation property. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| administrativeUnitIdFilters | String collection | The collection of administrative unit IDs to filter on. |
| displayName | String | The display name of the audit log query. |
| filterEndDateTime | DateTimeOffset | The end date and time of the audit log query filter. |
| filterStartDateTime | DateTimeOffset | The start date and time of the audit log query filter. |
| id | String | The unique identifier for the audit log query. Inherited from [entity](entity). |
| ipAddressFilters | String collection | The collection of IP addresses to filter on. |
| keywordFilter | String | The keyword to filter on. |
| objectIdFilters | String collection | The collection of object IDs to filter on. |
| operationFilters | String collection | The collection of operations to filter on. |
| recordTypeFilters | [microsoft.graph.security.auditLogRecordType](security-auditlogrecordtype) collection | The collection of record types to filter on. |
| serviceFilters | String collection | The collection of services to filter on. |
| status | microsoft.graph.security.auditLogQueryStatus | The status of the audit log query. Possible values are: `notStarted`, `running`, `succeeded`, `failed`, `cancelled`, `unknownFutureValue`. |
| userPrincipalNameFilters | String collection | The collection of user principal names to filter on. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| records | [microsoft.graph.security.auditLogRecord](security-auditlogrecord) collection | The collection of audit log records retrieved by the query. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.security.auditLogQuery",
  "id": "String (identifier)",
  "displayName": "String",
  "filterStartDateTime": "String (timestamp)",
  "filterEndDateTime": "String (timestamp)",
  "recordTypeFilters": ["String"],
  "keywordFilter": "String",
  "serviceFilters": ["String"],
  "operationFilters": ["String"],
  "userPrincipalNameFilters": ["String"],
  "ipAddressFilters": ["String"],
  "objectIdFilters": ["String"],
  "administrativeUnitIdFilters": ["String"],
  "status": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/security-auditlogquery?view=graph-rest-beta&accept=text/markdown)
