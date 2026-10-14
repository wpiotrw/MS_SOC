---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: unifiedRoot resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/unifiedroot?view=graph-rest-1.0
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
description: Container resource that groups the unified (vNext) access review collections under the accessReviews/unified path segment.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-06-30T00:00:00.0000000Z
locale: en-us
document_id: dc514421-0021-2eb7-d265-ed9de6b21b45
document_version_independent_id: e0b9384b-b0c2-7841-fbf5-4107e87e9718
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/unifiedroot.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/unifiedroot
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/unifiedroot.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 5202e9f9-348e-a93c-ce0b-bd2e7f845c6d
---

# unifiedRoot resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Container resource that groups the unified access review collections under the `identityGovernance/accessReviews/unified` path segment. The `unified` route is the entry point for **user-centric (catalog-scope) access reviews**, where an administrator reviews a user's access across all the resources contained in an [entitlement management catalog](accesspackagecatalog) in a single review, rather than reviewing one resource at a time.

A catalog is a container that groups multiple resource types—currently groups and applications. With a user-centric review, a reviewer (typically the user's manager) evaluates a principal's access to every group and application in the catalog from a single, consolidated view. The collections reuse the same [accessReviewScheduleDefinition](accessreviewscheduledefinition), [accessReviewInstance](accessreviewinstance), and [accessReviewInstanceDecisionItem](accessreviewinstancedecisionitem) resource shapes as the generally available access reviews API; the catalog scope is expressed through the [principalResourceMembershipsScope](principalresourcemembershipsscope) of the review definition.

This resource is reached through the **unified** relationship on the [accessReviewSet](accessreviewset) resource.

The following table summarizes how the unified route differs from the current access reviews API.

| Aspect | Current access reviews (`accessReviews`) | Unified access reviews (`accessReviews/unified`) |
| --- | --- | --- |
| Review focus | Reviews a single resource at a time (one group, application, directory role, or access package). | User-centric: reviews a principal's access across all groups and applications in a catalog in one review. |
| Scope model | Typically an [accessReviewQueryScope](accessreviewqueryscope) targeting one resource. | A [principalResourceMembershipsScope](principalresourcemembershipsscope) with a resource scope of `scopeType: catalog`. |
| Routing | Addressed under `identityGovernance/accessReviews`. | Addressed under `identityGovernance/accessReviews/unified`. The path segment is self-describing, discoverable in metadata, and works with the Microsoft Graph SDKs and Graph Explorer. |

Inherits from [entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List definitions](../unifiedroot-list-definitions) | [accessReviewScheduleDefinition](accessreviewscheduledefinition) collection | Retrieve the user-centric (catalog-scope) [accessReviewScheduleDefinition](accessreviewscheduledefinition) objects through the unified route. |
| [Create definition](../unifiedroot-post-definitions) | [accessReviewScheduleDefinition](accessreviewscheduledefinition) | Create a new user-centric (catalog-scope) [accessReviewScheduleDefinition](accessreviewscheduledefinition) object through the unified route. |

Only listing and creating definitions are documented as dedicated **unified** methods, because creating a catalog-scope review is the one operation that is specific to the unified route. After a definition is created, its instances, stages, and decisions are managed through the shared [accessReviewScheduleDefinition](accessreviewscheduledefinition), [accessReviewInstance](accessreviewinstance), and [accessReviewInstanceDecisionItem](accessreviewinstancedecisionitem) operations (for example, get, update, delete, list instances, stop, and apply decisions), addressed under the `identityGovernance/accessReviews/unified` path segment.

## Properties

None.

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| decisions | [accessReviewInstanceDecisionItem](accessreviewinstancedecisionitem) collection | Represents the unified (vNext) access review decisions on an instance of a review. |
| definitions | [accessReviewScheduleDefinition](accessreviewscheduledefinition) collection | Represents the unified (vNext) template and scheduling for an access review. |
| instances | [accessReviewInstance](accessreviewinstance) collection | Represents the unified (vNext) instance of a review. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.unifiedRoot"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/unifiedroot?view=graph-rest-beta&accept=text/markdown)
