---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: lifecyclePolicyRule resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-lifecyclepolicyrule?view=graph-rest-1.0
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
description: Represents an abstract base compliance rule evaluated as part of a lifecycle policy.
ms.date: 2026-11-02T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 13ef3981-abdb-c74e-44e6-8e62758c26a1
document_version_independent_id: 9149f4fc-f1ce-69e2-7db4-736e66a80021
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/identitygovernance-lifecyclepolicyrule.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/identitygovernance-lifecyclepolicyrule
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/identitygovernance-lifecyclepolicyrule.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: bd1dea1f-39f7-7717-bfac-ec7d123255d0
---

# lifecyclePolicyRule resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.identityGovernance

Represents an abstract base compliance rule that's evaluated as part of a [lifecyclePolicy](identitygovernance-lifecyclepolicy). Each enabled rule is evaluated independently, and any violation makes the policy noncompliant. A maximum of 10 rules are allowed per policy.

Updating individual rules directly isn't supported.

You can't create instances of this abstract type directly. Instead, use one of the following derived types:

- [periodicAttestationRule](identitygovernance-periodicattestationrule)
- [sponsorPresenceRule](identitygovernance-sponsorpresencerule)
- [inactivityRule](identitygovernance-inactivityrule)
- [accessPackageAssignmentRequiredRule](identitygovernance-accesspackageassignmentrequiredrule)
- [invitationRedemptionRule](identitygovernance-invitationredemptionrule)

Instances are differentiated by the **@odata.type** property. This is an abstract type.

Inherits from [entity](entity).

## Methods

None.

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

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/identitygovernance-lifecyclepolicyrule?view=graph-rest-beta&accept=text/markdown)
