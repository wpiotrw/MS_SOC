---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: comment resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/security-casemanagement-comment?view=graph-rest-beta
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
description: Represents a human-authored comment in a case activity timeline.
ms.date: 2026-05-29T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 22b108c8-c510-fc62-dc00-ee55981b535b
document_version_independent_id: 804a363e-fc0d-51c7-4074-d3ef23d15baf
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/security-casemanagement-comment.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/security-casemanagement-comment
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/security-casemanagement-comment.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 929f6e07-6c51-869a-102c-6578cf4ad257
---

# comment resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph.security.caseManagement

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents a human-authored comment in a case activity timeline.

For cast segments in URLs, use the full type name, for example `microsoft.graph.security.caseManagement.comment`.

Inherited from [activity](security-casemanagement-activity).

## Methods

This resource is part of a polymorphic collection managed by the [activity](security-casemanagement-activity) base type. Use the activity endpoints to [create](../security-casemanagement-case-post-activities), [get](../security-casemanagement-activity-get), [update](../security-casemanagement-activity-update), and [delete](../security-casemanagement-activity-delete) comment activities.

Updating and deleting comment activities isn't supported for [incidentCase](security-casemanagement-incidentcase) objects.

To use a supported query option with a property declared only on **comment**, cast the base activities collection to `microsoft.graph.security.caseManagement.comment`.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| createdBy | String | The user or service that created the resource. Inherited from [caseManagementEntity](security-casemanagement-casemanagemententity). Supports `$filter`. |
| createdDateTime | DateTimeOffset | The date and time when the resource was created. Inherited from [caseManagementEntity](security-casemanagement-casemanagemententity). Supports `$filter`. |
| id | String | The unique identifier for the resource. Inherited from [entity](entity). Supports `$filter`. |
| lastModifiedBy | String | The user or service that last modified the resource. Inherited from [caseManagementEntity](security-casemanagement-casemanagemententity). Supports `$filter`. |
| lastModifiedDateTime | DateTimeOffset | The date and time when the resource was last modified. Inherited from [caseManagementEntity](security-casemanagement-casemanagemententity). Supports `$filter`. |
| message | String | The comment body. The maximum length is 1,000 characters for [incident cases](security-casemanagement-incidentcase) and 5,000 characters for [generic cases](security-casemanagement-genericcase). Supports `$filter`. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.security.caseManagement.comment",
  "id": "String (identifier)",
  "createdDateTime": "String (timestamp)",
  "createdBy": "String",
  "lastModifiedDateTime": "String (timestamp)",
  "lastModifiedBy": "String",
  "message": "String"
}
```