---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: agentIdentityLifecyclePolicy resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-agentidentitylifecyclepolicy?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
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
description: Represents a lifecycle policy that governs the lifecycle of agent identities through compliance rules and enforcement actions.
ms.date: 2026-11-02T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 7677fff1-7899-b06d-1e97-db534e01712e
document_version_independent_id: 287448a8-615a-bacc-2ea6-63198628690f
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/identitygovernance-agentidentitylifecyclepolicy.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/identitygovernance-agentidentitylifecyclepolicy
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/identitygovernance-agentidentitylifecyclepolicy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 1d02efc9-f1c0-34ca-f038-f5a115931984
---

# agentIdentityLifecyclePolicy resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.identityGovernance

Represents a lifecycle policy that governs the lifecycle of agent identities through compliance rules and enforcement actions.

Inherits from [lifecyclePolicy](identitygovernance-lifecyclepolicy).

## Methods

For the list of operations, see the methods of the [lifecyclePolicy](identitygovernance-lifecyclepolicy) base type.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| createdDateTime | DateTimeOffset | The date and time when the policy was created. Inherited from [lifecyclePolicy](identitygovernance-lifecyclepolicy). |
| description | String | The description of the policy. Inherited from [lifecyclePolicy](identitygovernance-lifecyclepolicy). |
| displayName | String | The display name of the policy. Inherited from [lifecyclePolicy](identitygovernance-lifecyclepolicy). |
| enforcementAction | [microsoft.graph.identityGovernance.lifecyclePolicyEnforcementAction](identitygovernance-lifecyclepolicyenforcementaction) | The action taken when an agent identity governed by the policy becomes non-compliant. Inherited from [lifecyclePolicy](identitygovernance-lifecyclepolicy). |
| gracePeriodInDays | Int32 | The number of days after an identity becomes non-compliant before the enforcement action is applied. Inherited from [lifecyclePolicy](identitygovernance-lifecyclepolicy). |
| id | String | The unique identifier for the policy. Inherited from [entity](entity). |
| isEnabled | Boolean | Indicates whether the policy is enabled and actively evaluated. Inherited from [lifecyclePolicy](identitygovernance-lifecyclepolicy). |
| lastModifiedDateTime | DateTimeOffset | The date and time when the policy was last modified. Inherited from [lifecyclePolicy](identitygovernance-lifecyclepolicy). |
| notificationSchedule | [microsoft.graph.identityGovernance.lifecyclePolicyNotificationSettings](identitygovernance-lifecyclepolicynotificationsettings) | The notification settings for the policy, including the offsets, in days after non-compliance, at which notifications are sent. Inherited from [lifecyclePolicy](identitygovernance-lifecyclepolicy). |
| policySource | microsoft.graph.identityGovernance.lifecyclePolicySource | Indicates whether the policy is system-managed (a built-in default) or created by an administrator. Inherited from [lifecyclePolicy](identitygovernance-lifecyclepolicy). The possible values are: `userCreated`, `systemDefault`, `unknownFutureValue`. |
| scope | [subjectSet](subjectset) | The set of agent identities that the policy applies to. Inherited from [lifecyclePolicy](identitygovernance-lifecyclepolicy). |
| versionNumber | Int32 | The version number of the policy, which increments each time the policy is updated. Inherited from [lifecyclePolicy](identitygovernance-lifecyclepolicy). |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| createdBy | [directoryObject](directoryobject) | The user or service principal that created the policy. Inherited from [lifecyclePolicy](identitygovernance-lifecyclepolicy). |
| lastModifiedBy | [directoryObject](directoryobject) | The user or service principal that last modified the policy. Inherited from [lifecyclePolicy](identitygovernance-lifecyclepolicy). |
| report | [microsoft.graph.identityGovernance.lifecyclePolicyReport](identitygovernance-lifecyclepolicyreport) | The latest processing report for the policy. Inherited from [lifecyclePolicy](identitygovernance-lifecyclepolicy). |
| rules | [microsoft.graph.identityGovernance.lifecyclePolicyRule](identitygovernance-lifecyclepolicyrule) collection | The collection of inline compliance rules evaluated for the policy. Rules are combined with AND logic. A maximum of 10 rules are allowed per policy. Inherited from [lifecyclePolicy](identitygovernance-lifecyclepolicy). |
| versions | [microsoft.graph.identityGovernance.lifecyclePolicy](identitygovernance-lifecyclepolicy) collection | The collection of previous versions of the policy. Inherited from [lifecyclePolicy](identitygovernance-lifecyclepolicy). |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.identityGovernance.agentIdentityLifecyclePolicy",
  "createdDateTime": "String (timestamp)",
  "description": "String",
  "displayName": "String",
  "enforcementAction": {
    "@odata.type": "microsoft.graph.identityGovernance.lifecyclePolicyEnforcementAction"
  },
  "gracePeriodInDays": "Int32",
  "id": "String (identifier)",
  "isEnabled": "Boolean",
  "lastModifiedDateTime": "String (timestamp)",
  "notificationSchedule": {
    "@odata.type": "microsoft.graph.identityGovernance.lifecyclePolicyNotificationSettings"
  },
  "policySource": "String",
  "scope": {
    "@odata.type": "microsoft.graph.subjectSet"
  },
  "versionNumber": "Int32"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-agentidentitylifecyclepolicy?view=graph-rest-beta&accept=text/markdown)
