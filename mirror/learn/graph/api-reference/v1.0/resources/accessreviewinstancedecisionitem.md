---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: accessReviewInstanceDecisionItem resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/accessreviewinstancedecisionitem?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: jyothig123
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a decision on an accessReviewInstance.
ms.localizationpriority: medium
doc_type: resourcePageType
toc.keywords:
- access review decisions
ms.date: 2026-08-10T00:00:00.0000000Z
locale: en-us
document_id: d3b326ec-39ac-4724-8dff-b87f966b7b6e
document_version_independent_id: 5996d4a0-bb6b-ce00-8677-14bc9dc6bf79
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/accessreviewinstancedecisionitem.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/accessreviewinstancedecisionitem
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/accessreviewinstancedecisionitem.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: d875950f-2bdc-5e27-c911-4dd7e856abf1
---

# accessReviewInstanceDecisionItem resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents a Microsoft Entra [access review](accessreviewsv2-overview) decision on an instance of a review. This decision is the determination of an identity's access to a resource for a given [accessReviewInstance](accessreviewinstance). accessReviewInstanceDecisionItem is an open type and allows other properties to be passed in.

Each decision item is system-generated based off of the parent [accessReviewInstance](accessreviewinstance).

Inherits from [entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List instance decisions](../accessreviewinstance-list-decisions) (from an access review instance) | [accessReviewInstanceDecisionItem](accessreviewinstancedecisionitem) collection | Get a list of the [accessReviewInstanceDecisionItem](accessreviewinstancedecisionitem) objects and their properties. |
| [List stage decisions](../accessreviewstage-list-decisions) (from a stage of an access review instance) | [accessReviewInstanceDecisionItem](accessreviewinstancedecisionitem) collection | Get a list of the [accessReviewInstanceDecisionItem](accessreviewinstancedecisionitem) objects for a stage of an acecss review instance. |
| [Get](../accessreviewinstancedecisionitem-get) | [accessReviewInstanceDecisionItem](accessreviewinstancedecisionitem) | Read the properties and relationships of an [accessReviewInstanceDecisionItem](accessreviewinstancedecisionitem) object. |
| [Update](../accessreviewinstancedecisionitem-update) | [accessReviewInstanceDecisionItem](accessreviewinstancedecisionitem) | Update the properties of an [accessReviewInstanceDecisionItem](accessreviewinstancedecisionitem) object. |
| [Filter by current user](../accessreviewinstancedecisionitem-filterbycurrentuser) | [accessReviewInstanceDecisionItem](accessreviewinstancedecisionitem) collection | Returns the decision items for which the calling user is the reviewer. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| accessReviewId | String | The identifier of the accessReviewInstance parent. Supports `$select`. Read-only. |
| appliedBy | [userIdentity](useridentity) | The identifier of the user who applied the decision. Read-only. |
| appliedDateTime | DateTimeOffset | The timestamp when the approval decision was applied.`00000000-0000-0000-0000-000000000000` if the assigned reviewer hasn't applied the decision or it was automatically applied. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is `2014-01-01T00:00:00Z`. Supports `$select`. Read-only. |
| applyDescription | String | The description of the apply result. Read-only. |
| applyResult | String | The result of applying the decision. Possible values: `New`, `AppliedSuccessfully`, `AppliedWithUnknownFailure`, `AppliedSuccessfullyButObjectNotFound` and `ApplyNotSupported`. Supports `$select`, `$orderby`, and `$filter` (`eq` only). Read-only. |
| decision | String | Result of the review. Possible values: `Approve`, `Deny`, `NotReviewed`, or `DontKnow`. Supports `$select`, `$orderby`, and `$filter` (`eq` only). |
| id | String | The identifier of the decision. Inherited from [entity](entity). Supports `$select`. Read-only. |
| justification | String | Justification left by the reviewer when they made the decision. |
| permission | [accessReviewInstanceDecisionItemPermission](accessreviewinstancedecisionitempermission) | The permission that grants the principal access to a resource. Read-only. |
| principal | [identity](identity) | Every decision item in an access review represents a principal's access to a resource. This property represents details of the principal. For example, if a decision item represents access of User "Bob" to Group "Sales" - The principal is "Bob" and the resource is "Sales". Principals can be of two types - userIdentity and servicePrincipalIdentity. Supports `$select`. Read-only. |
| principalLink | String | A link to the principal object. For example, `https://graph.microsoft.com/v1.0/users/a6c7aecb-cbfd-4763-87ef-e91b4bd509d9`. Read-only. |
| recommendation | String | A system-generated recommendation for the approval decision based off last interactive sign-in to tenant. The value is `Approve` if the sign-in is fewer than 30 days after the start of review, `Deny` if the sign-in is greater than 30 days after, or `NoInfoAvailable`. Possible values: `Approve`, `Deny`, or `NoInfoAvailable`. Supports `$select`, `$orderby`, and `$filter` (`eq` only). Read-only. |
| resource | [accessReviewInstanceDecisionItemResource](accessreviewinstancedecisionitemresource) | Every decision item in an access review represents a principal's access to a resource. This property represents details of the resource. For example, if a decision item represents access of User "Bob" to Group "Sales" - The principal is Bob and the resource is "Sales". Resources can be of multiple types. See [accessReviewInstanceDecisionItemResource](accessreviewinstancedecisionitemresource). Read-only. |
| resourceLink | String | A link to the resource. For example, `https://graph.microsoft.com/v1.0/servicePrincipals/c86300f3-8695-4320-9f6e-32a2555f5ff8`. Supports `$select`. Read-only. |
| reviewedBy | [userIdentity](useridentity) | The identifier of the reviewer.`00000000-0000-0000-0000-000000000000` if the assigned reviewer hasn't reviewed. Supports `$select`. Read-only. |
| reviewedDateTime | DateTimeOffset | The timestamp when the review decision occurred. Supports `$select`. Read-only. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| insights | [governanceInsight](governanceinsight) collection | Insights are recommendations to reviewers on whether to approve or deny a decision. There can be multiple insights associated with an **accessReviewInstanceDecisionItem**. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.accessReviewInstanceDecisionItem",
  "accessReviewId": "String",
  "appliedBy": {
    "@odata.type": "microsoft.graph.userIdentity"
  },
  "appliedDateTime": "String (timestamp)",
  "applyDescription": "String",
  "applyResult": "String",
  "decision": "String",
  "id": "String (identifier)",
  "justification": "String",
  "permission": {
    "@odata.type": "microsoft.graph.accessReviewInstanceDecisionItemPermission"
  },
  "principal": {
    "@odata.type": "microsoft.graph.identity"
  },
  "principalLink": "String",
  "reviewedBy": {
    "@odata.type": "microsoft.graph.userIdentity"
  },
  "reviewedDateTime": "String (timestamp)",
  "recommendation": "String",
  "resource": {
    "@odata.type": "microsoft.graph.accessReviewInstanceDecisionItemResource"
  },
  "resourceLink": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/accessreviewinstancedecisionitem?view=graph-rest-beta&accept=text/markdown)
