---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: approverDelegate resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/approverdelegate?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: lnalepa
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents the delegation of approval responsibilities from one user to another user or group, for a specified period of time.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-03-03T00:00:00.0000000Z
locale: en-us
document_id: 0f67f77e-860b-a82e-07b6-1aaf8c56f636
document_version_independent_id: 11169484-c0e7-0e0b-1044-af7c34e2d491
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/approverdelegate.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/approverdelegate
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/approverdelegate.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: f3095d68-609a-c876-1dd2-02ab37c6cd5b
---

# approverDelegate resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents the delegation of approval responsibilities from one user to another user or group, for a specified period of time.

An approver delegate applies across all [Microsoft Entra entitlement management](entitlementmanagement-overview) access package assignment requests and all [access reviews](accessreviewsv2-overview) that are assigned to the user. While the delegation is in effect, the delegate can approve or deny on behalf of the user, and the user can still approve or deny their own pending items.

This resource is configured in the **approverDelegate** property of [identityGovernanceUserSettings](identitygovernanceusersettings), which is exposed through the **identityGovernance** property of the [user](user) resource. Users can manage their own approver delegate through the `/me/identityGovernance/approverDelegate` path, and administrators can manage the approver delegate of any user through the `/users/{user-id}/identityGovernance/approverDelegate` path.

## Methods

None.

To manage the approver delegate of a user, use the [Get approverDelegate](../approverdelegate-get) and [Update approverDelegate](../approverdelegate-update) methods on the [user](user) resource.

There's no delete operation. To stop a delegation, use the update operation to submit a schedule that has already expired.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| delegate | [userSet](userset) | The user or group that receives the approval delegation. Only the [singleUser](singleuser) and [groupMembers](groupmembers) subtypes are supported. |
| schedule | [requestSchedule](requestschedule) | The period during which the delegation is in effect, expressed as a start date and an expiration pattern. If you don't specify a schedule, the delegation starts immediately and doesn't expire. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.approverDelegate",
  "delegate": {
    "@odata.type": "microsoft.graph.userSet"
  },
  "schedule": {
    "@odata.type": "microsoft.graph.requestSchedule"
  }
}
```