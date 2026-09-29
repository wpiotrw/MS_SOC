---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: accessReviewInstanceDecisionItemResource resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/accessreviewinstancedecisionitemresource?view=graph-rest-1.0
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
description: Represents the resource associated with the decision item.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-07-30T00:00:00.0000000Z
locale: en-us
document_id: 0b331dc8-485a-3517-1ad5-6e870626419a
document_version_independent_id: 75a649af-aa27-57d0-3158-e8c40692dfaa
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/accessreviewinstancedecisionitemresource.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/accessreviewinstancedecisionitemresource
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/accessreviewinstancedecisionitemresource.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: fcf8f10d-3ac5-8f8f-0d73-625fba0421bf
---

# accessReviewInstanceDecisionItemResource resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

In an [accessReviewInstanceDecisionItem](accessreviewinstancedecisionitem), the **resource** property identifies the resource associated with the decision item.

An [accessReviewInstanceDecisionItemResource](accessreviewinstancedecisionitemresource) object is an open type that allows other properties to be passed in and is the base type for the following resources:

- [accessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource](accessreviewinstancedecisionitemaccesspackageassignmentpolicyresource)
- [accessReviewInstanceDecisionItemAccessPackageResource](accessreviewinstancedecisionitemaccesspackageresource)
- [accessReviewInstanceDecisionItemAzureRoleResource](accessreviewinstancedecisionitemazureroleresource)
- [accessReviewInstanceDecisionItemCustomDataProvidedResource](accessreviewinstancedecisionitemcustomdataprovidedresource)
- [accessReviewInstanceDecisionItemServicePrincipalResource](accessreviewinstancedecisionitemserviceprincipalresource)

## Properties

| Property | Type | Description |
| --- | --- | --- |
| description | String | Description of the resource. |
| displayName | String | Display name of the resource |
| id | String | Identifier of the resource |
| type | String | Type of resource. Types include: `Group`, `ServicePrincipal`, `DirectoryRole`, `AzureRole`, `AccessPackage`, `AccessPackageAssignmentPolicy`, and `CustomDataProvidedResource`. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.accessReviewInstanceDecisionItemResource",
  "description": "String",
  "displayName": "String",
  "id": "String (identifier)",
  "type": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/accessreviewinstancedecisionitemresource?view=graph-rest-beta&accept=text/markdown)
