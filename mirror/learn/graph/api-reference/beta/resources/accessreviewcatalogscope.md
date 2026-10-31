---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: accessReviewCatalogScope resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/accessreviewcatalogscope?view=graph-rest-beta
config_moniker_range: graph-rest-beta
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
description: Represent an entitlement management catalog as the resource scope of an access review.
ms.date: 2026-09-03T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 9615328d-3cf6-a591-25a8-d357de7da9b5
document_version_independent_id: fe13b7f7-d7a2-ecfa-c1ff-8dcb0711f2e7
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/accessreviewcatalogscope.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/accessreviewcatalogscope
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/accessreviewcatalogscope.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 3b2b0fbb-51c5-24d9-2cbb-c2c098c30831
---

# accessReviewCatalogScope resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Note

This is the recommended API for access reviews. The previous version of the [access reviews API](/en-us/graph/api/resources/accessreviews-root?view=graph-rest-beta&amp;preserve-view=true) is deprecated.

Represents an entitlement management catalog as the resource scope of an [access review](accessreviewsv2-overview). Use this type in the **resourceScopes** collection of a [principalResourceMembershipsScope](principalresourcemembershipsscope) object configured in the **scope** property of an [accessReviewScheduleDefinition](accessreviewscheduledefinition).

Groups, applications, and custom data provided resources in the catalog are always reviewed. Use the **additionalCatalogResourceTypes** property to review other resource types in the same catalog, in addition to the resource types that are always reviewed.

Inherits from [accessReviewResourceScope](accessreviewresourcescope).

## Methods

None.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| additionalCatalogResourceTypes | [accessReviewCatalogResourceType](enums#accessreviewcatalogresourcetype-values) | The resource types in the catalog to review, in addition to the resource types that are always reviewed. The possible values are: `none`, `accessPackage`, `unknownFutureValue`.The **additionalCatalogResourceTypes** property is a multi-valued enumeration and the property can contain multiple values in a comma-separated list. If you omit this property, only the resource types that are always reviewed are included in the review. |
| displayName | String | The display name of the catalog. Inherited from [accessReviewResourceScope](accessreviewresourcescope). |
| resourceId | String | The identifier of the catalog. Inherited from [accessReviewResourceScope](accessreviewresourcescope). |
| scopeType | [accessReviewResourceScopeType](enums#accessreviewresourcescopetype-values) | The scope type. Inherited from [accessReviewResourceScope](accessreviewresourcescope). The value is `catalog`. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.accessReviewCatalogScope",
  "resourceId": "String",
  "scopeType": "String",
  "displayName": "String",
  "additionalCatalogResourceTypes": "String"
}
```