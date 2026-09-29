---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: accessReviewReviewerScope resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/accessreviewreviewerscope?view=graph-rest-1.0
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
description: Represents reviewers of an access review or user consent requests.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-08-10T00:00:00.0000000Z
locale: en-us
document_id: 40a20fee-80d9-64dd-2e8f-c7bbb9a875cb
document_version_independent_id: 766d4862-6c8d-a0a7-3c22-1dbc4aaabf5c
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/accessreviewreviewerscope.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/accessreviewreviewerscope
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/accessreviewreviewerscope.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: dc62b610-cb01-d300-7fdc-c49be146e152
---

# accessReviewReviewerScope resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Use **accessReviewReviewerScope** to configure reviewers in the following properties:

- [accessReviewScheduleDefinition](accessreviewscheduledefinition): **reviewers**, **fallbackReviewers**, **backupReviewers**
- [accessReviewInstance](accessreviewinstance): **reviewers**, **fallbackReviewers**
- [accessReviewStage](accessreviewstage): **reviewers**, **fallbackReviewers**

This type is also used for [user consent requests](consentrequests-overview).

Reviewers can be specified as a static list of users (that is, specific users, group owners, and group members) or dynamically, in which every user is reviewed by their manager, group owners, or application owners. To create a self-review (where users review their own access) in Microsoft Entra access reviews, the **reviewers** property of the [accessReviewScheduleDefinition](accessreviewscheduledefinition) should be an empty collection.

Inherits from [accessReviewScope](accessreviewscope).

## Properties

| Property | Type | Description |
| --- | --- | --- |
| query | String | The query specifying who will be the reviewer. |
| queryRoot | String | In the scenario where reviewers need to be specified dynamically, this property is used to indicate the relative source of the query. This property is only required if a relative query, for example, `./manager`, is specified. Possible value: `decisions`. |
| queryType | String | The type of query. Examples include `MicrosoftGraph` and `ARM`. |
| reviewerId | String | The identifier of the reviewer. |
| scopeType | accessReviewReviewerScopeType | The type of the reviewer scope. The possible values are: `user`, `group`, `self`, `manager`, `sponsor`, `resourceOwner`, `managerOrSponsor`, `unknownFutureValue`. |

For more about configuration options for **reviewers**, see [Assign reviewers to your access review definition using the Microsoft Graph API](/en-us/graph/accessreviews-reviewers-concept).

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.accessReviewReviewerScope",
  "query": "String",
  "queryRoot": "String",
  "queryType": "String",
  "reviewerId": "String",
  "scopeType": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/accessreviewreviewerscope?view=graph-rest-beta&accept=text/markdown)
