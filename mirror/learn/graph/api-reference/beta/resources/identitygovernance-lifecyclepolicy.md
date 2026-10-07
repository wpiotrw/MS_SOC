---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: lifecyclePolicy resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-lifecyclepolicy?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: siaggarwal-ops
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents an abstract base policy that governs the lifecycle of identities through compliance rules and enforcement actions.
ms.date: 2026-07-31T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 011bb577-09dd-3401-4d40-dcc12e63d3ad
document_version_independent_id: fb614e1b-72af-0ca2-4d09-f1790aa045e0
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/identitygovernance-lifecyclepolicy.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/identitygovernance-lifecyclepolicy
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/identitygovernance-lifecyclepolicy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 4b50bc9d-58ee-5575-a674-8522472354ec
---

# lifecyclePolicy resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph.identityGovernance

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents the abstract base type for lifecycle policies that govern identities by evaluating compliance rules and applying enforcement actions when an identity becomes non-compliant. A maximum of 10 policies are allowed per subject type per tenant.

You can't create instances of this abstract type directly. Instead, use the following derived type:

- [agentIdentityLifecyclePolicy](identitygovernance-agentidentitylifecyclepolicy)

Instances are differentiated by the **@odata.type** property.

Inherits from [entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [Get lifecyclePolicy](../identitygovernance-lifecyclepolicy-get) | [microsoft.graph.identityGovernance.lifecyclePolicy](identitygovernance-lifecyclepolicy) | Read the properties and relationships of [lifecyclePolicy](identitygovernance-lifecyclepolicy) object. |
| [Update lifecyclePolicy](../identitygovernance-lifecyclepolicy-update) | [microsoft.graph.identityGovernance.lifecyclePolicy](identitygovernance-lifecyclepolicy) | Update the properties of a lifecyclePolicy object. |
| [Delete lifecyclePolicy](../identitygovernance-lifecyclepolicy-delete) | None | Delete a lifecyclePolicy object. |
| [lifecyclePolicy: restore](../identitygovernance-lifecyclepolicy-restore) | [microsoft.graph.identityGovernance.lifecyclePolicy](identitygovernance-lifecyclepolicy) | Restore a soft-deleted lifecyclePolicy object. |
| [List rules](../identitygovernance-lifecyclepolicy-list-rules) | [microsoft.graph.identityGovernance.lifecyclePolicyRule](identitygovernance-lifecyclepolicyrule) collection | Get the compliance rules defined on the policy. |
| [Evaluate impact](../identitygovernance-lifecyclepolicy-impact) | [lifecyclePolicyImpactSummary](identitygovernance-lifecyclepolicyimpactsummary) collection | Evaluate the impact of the policy during a specified period. |
| [Get report](../identitygovernance-lifecyclepolicy-list-report) | [lifecyclePolicyReport](identitygovernance-lifecyclepolicyreport) | Read the latest processing report for the policy. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| createdDateTime | DateTimeOffset | The date and time when the policy was created. |
| description | String | The description of the policy. |
| displayName | String | The display name of the policy. |
| enforcementAction | [microsoft.graph.identityGovernance.lifecyclePolicyEnforcementAction](identitygovernance-lifecyclepolicyenforcementaction) | The action taken when an identity governed by the policy becomes non-compliant. This is a polymorphic type; the possible types are [deleteOnlyEnforcementAction](identitygovernance-deleteonlyenforcementaction), [disableOnlyEnforcementAction](identitygovernance-disableonlyenforcementaction), and [disableThenDeleteEnforcementAction](identitygovernance-disablethendeleteenforcementaction). |
| gracePeriodInDays | Int32 | The number of days after an identity becomes non-compliant before the enforcement action is applied. |
| id | String | The unique identifier for the policy. Inherited from [entity](entity). |
| isEnabled | Boolean | Indicates whether the policy is enabled and actively evaluated. |
| lastModifiedDateTime | DateTimeOffset | The date and time when the policy was last modified. |
| notificationSchedule | [microsoft.graph.identityGovernance.lifecyclePolicyNotificationSettings](identitygovernance-lifecyclepolicynotificationsettings) | The notification settings for the policy, including the offsets, in days after non-compliance, at which notifications are sent. |
| policySource | [microsoft.graph.identityGovernance.lifecyclePolicySource](enums-identitygovernance#lifecyclepolicysource-values) | Indicates whether the policy is system-managed (a built-in default) or created by an administrator. The possible values are: `userCreated`, `systemDefault`, `unknownFutureValue`. |
| scope | [subjectSet](subjectset) | The set of subjects that the policy applies to. For example, use an [allExcludingGroupsSubjectSet](identitygovernance-allexcludinggroupssubjectset) to exclude specific groups from evaluation. |
| versionNumber | Int32 | The version number of the policy, which increments each time the policy is updated. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| createdBy | [directoryObject](directoryobject) | The user or service principal that created the policy. |
| lastModifiedBy | [directoryObject](directoryobject) | The user or service principal that last modified the policy. |
| report | [microsoft.graph.identityGovernance.lifecyclePolicyReport](identitygovernance-lifecyclepolicyreport) | The latest processing report for the policy. |
| rules | [microsoft.graph.identityGovernance.lifecyclePolicyRule](identitygovernance-lifecyclepolicyrule) collection | The collection of inline compliance rules evaluated for the policy. Rules are combined with AND logic. A maximum of 10 rules are allowed per policy. |
| versions | [microsoft.graph.identityGovernance.lifecyclePolicy](identitygovernance-lifecyclepolicy) collection | The collection of previous versions of the policy. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.identityGovernance.lifecyclePolicy",
  "id": "String (identifier)",
  "createdDateTime": "String (timestamp)",
  "description": "String",
  "displayName": "String",
  "isEnabled": "Boolean",
  "lastModifiedDateTime": "String (timestamp)",
  "scope": {
    "@odata.type": "microsoft.graph.subjectSet"
  },
  "versionNumber": "Integer",
  "policySource": "String",
  "gracePeriodInDays": "Integer",
  "enforcementAction": {
    "@odata.type": "microsoft.graph.identityGovernance.lifecyclePolicyEnforcementAction"
  },
  "notificationSchedule": {
    "@odata.type": "microsoft.graph.identityGovernance.lifecyclePolicyNotificationSettings"
  }
}
```