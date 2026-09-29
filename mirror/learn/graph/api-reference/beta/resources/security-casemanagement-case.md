---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: case resource type (case management) - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/security-casemanagement-case?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: alfeldsh
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents an abstract security case that tracks an investigation and organizes related work.
ms.date: 2026-05-29T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 4da0235b-d4b6-d6d2-08be-7da264378754
document_version_independent_id: dac5f1a3-2933-ede9-9e1e-fcda80194c26
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/security-casemanagement-case.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/security-casemanagement-case
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/security-casemanagement-case.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 634e13d1-b95f-af7a-6dd8-a9d791e45d44
---

# case resource type (case management) - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph.security.caseManagement

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents an abstract security case that tracks an investigation and organizes related tasks, activities, relations, and attachments. Use the [genericCase](security-casemanagement-genericcase) derived type to create case instances. You can't create [incidentCase](security-casemanagement-incidentcase) instances with API requests; incident cases are created by the service. Instances are differentiated by `@odata.type`. This is an abstract type.

For cast segments in URLs, use the full type name, for example `microsoft.graph.security.caseManagement.genericCase` or `microsoft.graph.security.caseManagement.incidentCase`.

Inherits from [microsoft.graph.security.caseManagement.caseManagementEntity](security-casemanagement-casemanagemententity).

## Methods

Use the [Update](../security-casemanagement-case-update) method to update **displayName** and **status** for all case types. Other mutable properties depend on the concrete case type.

| Method | Return type | Description |
| --- | --- | --- |
| [List](../security-casemanagementroot-list-cases) | [microsoft.graph.security.caseManagement.case](security-casemanagement-case) collection | List security cases. |
| [Create](../security-casemanagementroot-post-cases) | [microsoft.graph.security.caseManagement.case](security-casemanagement-case) | Create a security case by specifying a supported derived type in `@odata.type`. The [incidentCase](security-casemanagement-incidentcase) derived type isn't supported for create requests. |
| [Get](../security-casemanagement-case-get) | [microsoft.graph.security.caseManagement.case](security-casemanagement-case) | Read the properties and relationships of a security case. |
| [Update](../security-casemanagement-case-update) | [microsoft.graph.security.caseManagement.case](security-casemanagement-case) | Update the supported mutable properties of a security case. |
| [Delete](../security-casemanagementroot-delete-cases) | None | Delete a security case. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| createdBy | String | The user or service that created the case. Inherited from [caseManagementEntity](security-casemanagement-casemanagemententity). Supports `$filter` and `$orderby`. |
| createdDateTime | DateTimeOffset | The date and time when the case was created. Inherited from [caseManagementEntity](security-casemanagement-casemanagemententity). Supports `$filter` and `$orderby`. |
| customFields | [microsoft.graph.security.caseManagement.customFieldValues](security-casemanagement-customfieldvalues) | Tenant-defined custom field values keyed by the exact **displayName** of each custom field definition. The property and its dynamic fields don't support `$filter`. |
| displayName | String | The display name of the case. Supports `$filter` and `$orderby`. |
| id | String | The unique identifier for the case. Inherited from [entity](entity). Supports `$filter` and `$orderby`. |
| lastModifiedBy | String | The user or service that last modified the case. Inherited from [caseManagementEntity](security-casemanagement-casemanagemententity). Supports `$filter` and `$orderby`. |
| lastModifiedDateTime | DateTimeOffset | The date and time when the case was last modified. Inherited from [caseManagementEntity](security-casemanagement-casemanagemententity). Supports `$filter` and `$orderby`. |
| slaPolicies | [microsoft.graph.security.caseManagement.caseSlaPolicyEntry](security-casemanagement-caseslapolicyentry) collection | A denormalized, read-only collection of SLA (service level agreement) policy status entries for the case. Each entry represents one SLA policy applied to the case, including its current status and breach target time. Computed by the service; any value supplied in a create or update request is silently ignored. Supports `$filter` using the `any()` lambda operator only, for example, `$filter=slaPolicies/any(p: p/status eq 'breached')`. The `all()` lambda operator and other collection functions aren't supported. Doesn't support `$orderby`. |
| status | String | The tenant-defined lifecycle status of the case. Use a **displayName** value returned in the status tree by [List statuses](../security-casemanagement-casetypeconfiguration-list-statuses) from `/security/caseManagement/caseTypeConfigurations/genericCase/statuses` or `/security/caseManagement/caseTypeConfigurations/incidentCase/statuses`, depending on the case type. Supports `$filter` (`eq`). |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| activities | [microsoft.graph.security.caseManagement.activity](security-casemanagement-activity) collection | The timeline of comments and audit events associated with the case. Supports `$expand`. |
| attachments | [microsoft.graph.security.caseManagement.attachment](security-casemanagement-attachment) collection | Evidence files and metadata associated with the case. Supports `$expand`. |
| relations | [microsoft.graph.security.caseManagement.relation](security-casemanagement-relation) collection | Links from the case to related security resources. Supports `$expand`. |
| tasks | [microsoft.graph.security.caseManagement.task](security-casemanagement-task) collection | Tasks used to track work required to resolve the case. Supports `$expand`. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.security.caseManagement.case",
  "id": "String (identifier)",
  "createdDateTime": "String (timestamp)",
  "createdBy": "String",
  "lastModifiedDateTime": "String (timestamp)",
  "lastModifiedBy": "String",
  "displayName": "String",
  "status": "String",
  "customFields": {"@odata.type": "#microsoft.graph.security.caseManagement.customFieldValues"},
  "slaPolicies": [
    {"@odata.type": "microsoft.graph.security.caseManagement.caseSlaPolicyEntry"}
  ]
}
```