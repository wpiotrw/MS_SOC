---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: workflowTemplate resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-workflowtemplate?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: kristinasmith
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a pre-configured template for lifecycle workflows that you can use to create a workflow. Workflow templates are available for common scenarios such as new hires and users that are leaving the organization.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2024-07-22T00:00:00.0000000Z
locale: en-us
document_id: 27179b44-48f0-ac41-d928-75d416f7b9a8
document_version_independent_id: 513d978a-6405-190b-17bc-8de618b33ab0
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/identitygovernance-workflowtemplate.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/identitygovernance-workflowtemplate
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/identitygovernance-workflowtemplate.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: cc5d0539-b47f-a26c-0221-8e9d0cdde847
---

# workflowTemplate resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.identityGovernance

Represents the pre-configured templates of Lifecycle Workflows that are available in Microsoft Entra ID. Workflow templates are available for common scenarios such as new hires and users that are leaving the organization.

Workflow templates allow you to set up workflows based on common lifecycle management scenarios. You can also create custom workflows from the workflow templates to achieve specific situations.

Inherits from [entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../identitygovernance-lifecycleworkflowscontainer-list-workflowtemplates) | [microsoft.graph.identityGovernance.workflowTemplate](identitygovernance-workflowtemplate) collection | Get a list of the [workflowTemplate](identitygovernance-workflowtemplate) objects and their properties. |
| [Get](../identitygovernance-workflowtemplate-get) | [microsoft.graph.identityGovernance.workflowTemplate](identitygovernance-workflowtemplate) | Read the properties and relationships of a [workflowTemplate](identitygovernance-workflowtemplate) object. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| category | microsoft.graph.identityGovernance.lifecycleWorkflowCategory | The category of the workflow template. The possible values are: `joiner`, `leaver`, `unknownFutureValue`, `mover`, `extensibility`. Use the `Prefer: include-unknown-enum-members` request header to get the following members in this [evolvable enum](/en-us/graph/best-practices-concept#handling-future-members-in-evolvable-enumerations): `mover`, `extensibility`.Supports `$filter`(`eq`, `ne`) and `$orderby`. |
| description | String | The description of the `workflowTemplate`. |
| displayName | String | The display name of the `workflowTemplate`.Supports `$filter`(`eq`, `ne`) and `$orderby`. |
| executionConditions | [microsoft.graph.identityGovernance.workflowExecutionConditions](identitygovernance-workflowexecutionconditions) | Conditions describing when to execute the workflow and the criteria to identify in-scope subject set. |
| id | String | The unique identifier for the `workflowTemplate`.Inherited from [entity](entity).Supports `$filter`(`eq`, `ne`) and `$orderby`. |

### Supported workflow templates

Lifecycle Workflows currently provide the following predefined workflow templates:

| Workflow template type | Lifecycle category |
| --- | --- |
| Onboard pre-hire employee | Joiner |
| Onboard new hire employee | Joiner |
| Post-Onboarding new hire employee | Joiner |
| Real-time employee change | Mover |
| Employee group membership changes | Mover |
| Employee job profile change | Mover |
| Real-time employee termination | Leaver |
| Pre-Offboarding of an employee | Leaver |
| Offboard an employee | Leaver |
| Post-Offboarding of an employee | Leaver |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| tasks | [microsoft.graph.identityGovernance.task](identitygovernance-task) collection | Represents the configured tasks to execute and their execution sequence within a [workflow](identitygovernance-workflow). This relationship is expanded by default. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.identityGovernance.workflowTemplate",
  "id": "String (identifier)",
  "category": "String",
  "description": "String",
  "displayName": "String",
  "executionConditions": {
    "@odata.type": "microsoft.graph.identityGovernance.workflowExecutionConditions"
  }
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-workflowtemplate?view=graph-rest-beta&accept=text/markdown)
