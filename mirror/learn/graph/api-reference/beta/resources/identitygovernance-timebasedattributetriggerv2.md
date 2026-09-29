---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: timeBasedAttributeTriggerV2 resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-timebasedattributetriggerv2?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: jackschedel
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents an extensible time-based trigger that evaluates a user's date attribute to initiate a lifecycle workflow.
ms.date: 2026-08-10T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 6409b7f1-8b31-4c8e-1d07-1667bf104b63
document_version_independent_id: 544a27ba-7430-a57b-8e9e-1171de0ef77a
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/identitygovernance-timebasedattributetriggerv2.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/identitygovernance-timebasedattributetriggerv2
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/identitygovernance-timebasedattributetriggerv2.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: b399974a-ddfd-c2c6-b601-b8a7170df532
---

# timeBasedAttributeTriggerV2 resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph.identityGovernance

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents an extensible time-based trigger that evaluates a user's date attribute by using a configurable operator to initiate a [lifecycle workflow](identitygovernance-workflow).

Inherits from [workflowExecutionTrigger](identitygovernance-workflowexecutiontrigger).

## Properties

| Property | Type | Description |
| --- | --- | --- |
| attribute | String | The name of the date-type user attribute to evaluate, such as `employeeHireDate` or `employeeLeaveDateTime`. |
| operator | [microsoft.graph.identityGovernance.workflowExecutionTriggerOperator](identitygovernance-workflowexecutiontriggeroperator) | The operator that determines how to evaluate the date attribute. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.identityGovernance.timeBasedAttributeTriggerV2",
  "attribute": "String",
  "operator": {"@odata.type": "microsoft.graph.identityGovernance.workflowExecutionTriggerOperator"}
}
```