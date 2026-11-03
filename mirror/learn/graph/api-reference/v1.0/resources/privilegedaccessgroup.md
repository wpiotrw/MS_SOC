---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: privilegedAccessGroup resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/privilegedaccessgroup?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: ilyalushnikov
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: The entry point for all resources related to Privileged Identity Management (PIM) for groups.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2024-07-22T00:00:00.0000000Z
locale: en-us
document_id: f4195b11-2c34-ba2b-2e16-add69d9fcd66
document_version_independent_id: 08989cb7-1f1e-59b1-a07c-ee548f47dcae
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/privilegedaccessgroup.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/privilegedaccessgroup
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/privilegedaccessgroup.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: b74b5fab-3262-5764-846e-e93ad547d544
---

# privilegedAccessGroup resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

The entry point for all resources related to Privileged Identity Management (PIM) for groups.

Inherits from [entity](entity).

## Methods

None.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| id | String | The unique identifier of an object in PIM governance for a group. Inherited from [entity](entity). |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| assignmentScheduleInstances | [privilegedAccessGroupAssignmentScheduleInstance](privilegedaccessgroupassignmentscheduleinstance) collection | The instances of assignment schedules to activate a just-in-time access. |
| assignmentScheduleRequests | [privilegedAccessGroupAssignmentScheduleRequest](privilegedaccessgroupassignmentschedulerequest) collection | The schedule requests for operations to create, update, delete, extend, and renew an assignment. |
| assignmentSchedules | [privilegedAccessGroupAssignmentSchedule](privilegedaccessgroupassignmentschedule) collection | The assignment schedules to activate a just-in-time access. |
| eligibilityScheduleInstances | [privilegedAccessGroupEligibilityScheduleInstance](privilegedaccessgroupeligibilityscheduleinstance) collection | The instances of eligibility schedules to activate a just-in-time access. |
| eligibilityScheduleRequests | [privilegedAccessGroupEligibilityScheduleRequest](privilegedaccessgroupeligibilityschedulerequest) collection | The schedule requests for operations to create, update, delete, extend, and renew an eligibility. |
| eligibilitySchedules | [privilegedAccessGroupEligibilitySchedule](privilegedaccessgroupeligibilityschedule) collection | The eligibility schedules to activate a just-in-time access. |
| resources | [groupResource](groupresource) collection | The groups managed through PIM for groups. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.privilegedAccessGroup",
  "id": "String (identifier)"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/privilegedaccessgroup?view=graph-rest-beta&accept=text/markdown)
