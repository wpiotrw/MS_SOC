---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: deletedItemContainer resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/deleteditemcontainer?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: AlexFilipin
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: A container for deleted lifecycle workflow objects during the period before they're permanently deleted.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2024-05-23T00:00:00.0000000Z
locale: en-us
document_id: b2535a5b-e0b3-4b64-d0c8-cca0946a21f9
document_version_independent_id: 139f2a30-1d7b-eceb-ba8b-18f4f39ff168
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/deleteditemcontainer.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/deleteditemcontainer
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/deleteditemcontainer.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: b8ee6199-3629-a799-963f-c178a23e3def
---

# deletedItemContainer resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

A container for deleted lifecycle workflow objects during the period before they're permanently deleted. Microsoft Entra ID Governance may permanently delete the workflows after 30 days, or you may [permanently delete the workflows](../identitygovernance-deleteditemcontainer-delete), or you may [restore the deleted workflow and its associated objects](../identitygovernance-workflow-restore).

Inherits from [entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List deleted workflows](../identitygovernance-lifecycleworkflowscontainer-list-deleteditems) | [deletedItemContainer](deleteditemcontainer) collection | Get a list of the [deletedItemContainer](deleteditemcontainer) objects and their properties. |
| [Get a deleted workflow](../identitygovernance-deleteditemcontainer-get) | [deletedItemContainer](deleteditemcontainer) | Read the properties and relationships of a [deletedItemContainer](deleteditemcontainer) object. |
| [Restore](../identitygovernance-workflow-restore) | [workflow](identitygovernance-workflow) | Restore a deleted [lifecycle workflow](identitygovernance-workflow) from the [deletedItemContainer](deleteditemcontainer) object. |
| [Permanently delete a workflow](../identitygovernance-deleteditemcontainer-delete) | None | Permanently delete a deleted [lifecycle workflow](identitygovernance-workflow) from the [lifecycleWorkflowsContainer](identitygovernance-lifecycleworkflowscontainer) object. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| id | String | The unique identifier of the [workflow](identitygovernance-workflow) that was deleted. Inherited from [entity](entity). |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| workflows | [microsoft.graph.identityGovernance.workflow](identitygovernance-workflow) collection | Deleted workflows that end up in the deletedItemsContainer. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.deletedItemContainer",
  "id": "String (identifier)"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/deleteditemcontainer?view=graph-rest-beta&accept=text/markdown)
