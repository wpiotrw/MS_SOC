---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: conditionalAccessPolicyPlan resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccesspolicyplan?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: ebasseri
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-sign-in
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a Conditional Access policy plan that combines shared conditions with scenario-specific rules and enforcement controls.
ms.reviewer: conditionalaccesspm
ms.date: 2026-10-02T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 1b91848b-7554-c917-e48b-98a7381b538c
document_version_independent_id: 0ffbfb01-a90e-6125-848f-a445c73d0ae0
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/conditionalaccesspolicyplan.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/conditionalaccesspolicyplan
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/conditionalaccesspolicyplan.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 939f3f2b-3b78-18b6-c96f-ce2d04987194
---

# conditionalAccessPolicyPlan resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents a Conditional Access policy plan that groups shared conditions and related rules into a single policy configuration. The shared conditions apply to every rule in the plan, while each rule defines scenario-specific conditions and enforcement controls.

Inherits from [entity](entity)

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../conditionalaccessroot-list-plans) | [conditionalAccessPolicyPlan](conditionalaccesspolicyplan) collection | Retrieve a list of Conditional Access policy plans. |
| [Create](../conditionalaccessroot-post-plans) | [conditionalAccessPolicyPlan](conditionalaccesspolicyplan) | Create a Conditional Access policy plan. |
| [Get](../conditionalaccesspolicyplan-get) | [conditionalAccessPolicyPlan](conditionalaccesspolicyplan) | Retrieve a Conditional Access policy plan. |
| [Update](../conditionalaccesspolicyplan-update) | [conditionalAccessPolicyPlan](conditionalaccesspolicyplan) | Update a Conditional Access policy plan. |
| [Delete](../conditionalaccessroot-delete-plans) | None | Delete a Conditional Access policy plan. |
| [List rules](../conditionalaccesspolicyplan-list-rules) | [conditionalAccessPolicyRule](conditionalaccesspolicyrule) collection | Retrieve the rules contained in the Conditional Access policy plan. |
| [Create rule](../conditionalaccesspolicyplan-post-rules) | [conditionalAccessPolicyRule](conditionalaccesspolicyrule) | Create a rule in the Conditional Access policy plan. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| createdDateTime | DateTimeOffset | The date and time the plan was created, in UTC. Read-only. |
| description | String | A free-text description of the plan's purpose and scope. |
| displayName | String | The administrator-defined display name for the plan. |
| id | String | The unique identifier for the plan. Read-only. Inherits from [entity](entity). |
| modifiedDateTime | DateTimeOffset | The date and time the plan was last modified, in UTC. Read-only. |
| owners | String collection | The IDs of users and groups recorded as metadata owners of the plan. Does not grant any role or permission to the plan. |
| sharedConditions | [conditionalAccessConditionSet](conditionalaccessconditionset) | The conditions that apply to every rule in the plan. During evaluation, these conditions are combined with each rule's **conditions** property; rules can add conditions but can't remove plan-level conditions. |
| tags | String collection | The administrator-defined tags used to categorize and organize the plan. |
| templateId | String | The identifier of the Microsoft-managed template from which the plan was created. The value is `null` for custom plans. |
| version | Int32 | The version number of the plan. The service increments this value each time the plan is updated. Read-only. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| rules | [conditionalAccessPolicyRule](conditionalaccesspolicyrule) collection | The unordered collection of rules contained in the plan. Each rule defines scenario-specific conditions and enforcement controls. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.conditionalAccessPolicyPlan",
  "id": "String (identifier)",
  "displayName": "String",
  "description": "String",
  "owners": [
    "String"
  ],
  "tags": [
    "String"
  ],
  "version": "Integer",
  "templateId": "String",
  "createdDateTime": "String (timestamp)",
  "modifiedDateTime": "String (timestamp)",
  "sharedConditions": {
    "@odata.type": "microsoft.graph.conditionalAccessConditionSet"
  },
  "rules": [
    {
      "@odata.type": "microsoft.graph.conditionalAccessPolicyRule"
    }
  ]
}
```