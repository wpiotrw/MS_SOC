---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: lifecyclePolicyRule resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-lifecyclepolicyrule?view=graph-rest-beta
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
description: Represents an abstract base compliance rule evaluated as part of a lifecycle policy.
ms.date: 2026-07-31T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 5dd616c2-f9ec-608d-575c-3579f348a2c5
document_version_independent_id: 9149f4fc-f1ce-69e2-7db4-736e66a80021
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/identitygovernance-lifecyclepolicyrule.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/identitygovernance-lifecyclepolicyrule
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/identitygovernance-lifecyclepolicyrule.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: bd1dea1f-39f7-7717-bfac-ec7d123255d0
---

# lifecyclePolicyRule resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph.identityGovernance

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents an abstract base compliance rule that's evaluated as part of a [lifecyclePolicy](identitygovernance-lifecyclepolicy). Each enabled rule is evaluated independently, and any violation makes the policy noncompliant. A maximum of 10 rules are allowed per policy.

You can't create instances of this abstract type directly. Instead, use one of the following derived types:

- [periodicAttestationRule](identitygovernance-periodicattestationrule)
- [sponsorPresenceRule](identitygovernance-sponsorpresencerule)
- [inactivityRule](identitygovernance-inactivityrule)

Instances are differentiated by the **@odata.type** property. This is an abstract type.

Inherits from [entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List rules](../identitygovernance-lifecyclepolicy-list-rules) | [microsoft.graph.identityGovernance.lifecyclePolicyRule](identitygovernance-lifecyclepolicyrule) collection | Get a list of the lifecyclePolicyRule objects and their properties. |
| [Get lifecyclePolicyRule](../identitygovernance-lifecyclepolicyrule-get) | [microsoft.graph.identityGovernance.lifecyclePolicyRule](identitygovernance-lifecyclepolicyrule) | Read the properties and relationships of [lifecyclePolicyRule](identitygovernance-lifecyclepolicyrule) object. |
| [Update lifecyclePolicyRule](../identitygovernance-lifecyclepolicyrule-update) | [microsoft.graph.identityGovernance.lifecyclePolicyRule](identitygovernance-lifecyclepolicyrule) | Update the properties of a lifecyclePolicyRule object. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| gracePeriodInDays | Int32 | The optional grace period, in days, that starts when the rule violation is first detected. The allowed range is 0 through 30. If omitted or set to `null`, the **gracePeriodInDays** value of the containing lifecycle policy applies. A value of `0` means no additional grace period. If multiple rules remain violated, the earliest rule grace-period expiry starts the policy action sequence; the policy-level grace period isn't added again. |
| id | String | The unique identifier for the rule. Inherited from [entity](entity). |
| isEnabled | Boolean | Indicates whether the rule is enabled and evaluated as part of its policy. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.identityGovernance.lifecyclePolicyRule",
  "gracePeriodInDays": "Int32",
  "id": "String (identifier)",
  "isEnabled": "Boolean"
}
```