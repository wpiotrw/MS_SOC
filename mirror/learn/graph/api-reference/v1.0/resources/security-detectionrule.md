---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: detectionRule resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/security-detectionrule?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: mmekler
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a custom detection rule written in Advanced hunting to automatically recognize security events when they occur, and to trigger alerts and response actions.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-08-25T00:00:00.0000000Z
locale: en-us
document_id: 993d3660-0007-b78c-e40e-a108006ae809
document_version_independent_id: d70ae79c-7d68-fc97-7535-f56611bdc71a
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/security-detectionrule.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/security-detectionrule
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/security-detectionrule.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: 6e06bcfa-ebfb-c378-6857-737ceead7d07
---

# detectionRule resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.security

Represents a custom detection rule written in **Advanced hunting** to automatically recognize security events when they occur, and to trigger alerts and response actions.

Custom detection rules let you proactively monitor various events and system states by using [advanced hunting](../security-security-runhuntingquery) queries, including suspected breach activity and misconfigured endpoints. A custom detection rule automatically recognizes security events when they occur, and triggers alerts and response actions. You can set the rules to run at regular intervals, generating alerts and taking response actions whenever matches occur.

Inherits from [entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../security-rulesroot-list-detectionrules) | [microsoft.graph.security.detectionRule](security-detectionrule) collection | Get a list of the [detectionRule](security-detectionrule) objects and their properties. |
| [Create](../security-rulesroot-post-detectionrules) | [microsoft.graph.security.detectionRule](security-detectionrule) | Create a new [detectionRule](security-detectionrule) object. |
| [Get](../security-detectionrule-get) | [microsoft.graph.security.detectionRule](security-detectionrule) | Read the properties and relationships of a [detectionRule](security-detectionrule) object. |
| [Update](../security-detectionrule-update) | [microsoft.graph.security.detectionRule](security-detectionrule) | Update the properties of a [detectionRule](security-detectionrule) object. |
| [Delete](../security-rulesroot-delete-detectionrules) | None | Delete a [detectionRule](security-detectionrule) object. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| createdBy | String | Name of the user or application that created the rule. Read-only. Supports `$filter` (`eq`, `ne`, `not`, `in`, `startsWith`, `endsWith`, `contains`). |
| createdDateTime | DateTimeOffset | Timestamp of rule creation. Read-only. Supports `$filter` (`eq`, `ne`, `not`, `le`, `ge`, `lt`, `gt`) and `$orderby`. |
| description | String | A user-supplied description of the detection rule. Supports `$filter` (`eq`, `ne`, `not`, `in`, `startsWith`, `endsWith`, `contains`). |
| detectionAction | [microsoft.graph.security.detectionAction](security-detectionaction) | The actions taken when a detection is made by this rule, including the alert that is created and any automated response actions. Supports `$filter` on the following nested **alertTemplate** properties:- String: **detectionAction/alertTemplate/title**, **detectionAction/alertTemplate/description**, **detectionAction/alertTemplate/recommendedActions** — each supports `eq`, `ne`, `not`, `in`, `startsWith`, `endsWith`, `contains`.<br>- Enum: **detectionAction/alertTemplate/severity** — supports `eq`, `ne`, `not`, `in`. |
| displayName | String | The display name of the rule. Supports `$filter` (`eq`, `ne`, `not`, `in`, `startsWith`, `endsWith`, `contains`) and `$orderby`. |
| id | String | The client-provided unique identifier of the rule. Supports `$filter` (`eq`, `ne`, `not`, `in`) and `$orderby`. |
| lastModifiedBy | String | Name of the user or application that last updated the rule. Read-only. Supports `$filter` (`eq`, `ne`, `not`, `in`, `startsWith`, `endsWith`, `contains`). |
| lastModifiedDateTime | DateTimeOffset | Timestamp of when the rule was last updated. Read-only. Supports `$filter` (`eq`, `ne`, `not`, `le`, `ge`, `lt`, `gt`) and `$orderby`. |
| queryCondition | [microsoft.graph.security.queryCondition](security-querycondition) | The advanced hunting query that defines the detection logic of this rule. Supports `$filter` on **queryCondition/queryText** (String) with `eq`, `ne`, `not`, `in`, `startsWith`, `endsWith`, `contains`. |
| schedule | [microsoft.graph.security.ruleSchedule](security-ruleschedule) | The triggering schedule of this rule. Supports `$filter` on **schedule/frequency** (Duration) with `eq`, `ne`, `not`, `le`, `ge`, `lt`, `gt`. Supports `$orderby` on **schedule/frequency**. |
| status | microsoft.graph.security.detectionRuleStatus | The current run status of the rule. The possible values are: `enabled`, `disabled`, `autoDisabled`, `unknownFutureValue`. Supports `$filter` (`eq`, `ne`, `not`, `in`) and `$orderby`. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.security.detectionRule",
  "id": "String (identifier)",
  "displayName": "String",
  "description": "String",
  "status": "String",
  "createdBy": "String",
  "createdDateTime": "String (timestamp)",
  "lastModifiedBy": "String",
  "lastModifiedDateTime": "String (timestamp)",
  "queryCondition": {
    "@odata.type": "microsoft.graph.security.queryCondition"
  },
  "schedule": {
    "@odata.type": "microsoft.graph.security.ruleSchedule"
  },
  "detectionAction": {
    "@odata.type": "microsoft.graph.security.detectionAction"
  }
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/security-detectionrule?view=graph-rest-beta&accept=text/markdown)
