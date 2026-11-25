---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: identityVerificationStatus resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/identityverificationstatus?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: tilarso
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-sign-in
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a user's overall identity verification state and recent verification events.
ms.date: 2026-10-15T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 273c8d59-a1ab-1af1-d20b-65c3b37fc3c1
document_version_independent_id: 6c8916b2-0878-c4eb-4936-4633e90e9d3c
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/identityverificationstatus.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/identityverificationstatus
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/identityverificationstatus.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 1aecb3ef-f9d3-12d2-f44f-3263a726c63c
---

# identityVerificationStatus resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents a user's overall identity verification state and recent verification events. Each user has one **identityVerificationStatus** object. The service computes its properties from the user's verification events.

Inherits from [entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [Get](../identityverificationstatus-get) | [identityVerificationStatus](identityverificationstatus) | Read a user's identity verification status and recent verification events. |
| [Create verification event](../identityverificationstatus-post-verificationevents) | [identityVerificationEvent](identityverificationevent) | Record a verification event for a user. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| expiryDateTime | DateTimeOffset | The effective expiry of the user's overall verified state, computed as the latest **expiresDateTime** across active verification events. `null` when no active event has an expiry. Read-only. |
| id | String | The unique identifier of this singleton resource. Equals the owning user's object ID. Read-only. Inherited from [entity](entity). |
| lastVerifiedDateTime | DateTimeOffset | The date and time of the most recent successful identity verification. `null` when **state** is `unverified`. Read-only. |
| state | [verificationState](enums#verificationstate-values) | The overall verification state, computed from the most recent active verification event. The possible values are: `unverified`, `verified`, `revoked`, `suspended`, `issued`, `blocked`, `unknownFutureValue`. The service doesn't return an `expired` state; compare **expiryDateTime** with the current time to determine expiry. Read-only. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| verificationEvents | [identityVerificationEvent](identityverificationevent) collection | The user's recent verification events, automatically included when the status is retrieved. Contains up to 10 events, ordered by recency. Older events are removed when the limit is reached. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.identityVerificationStatus",
  "id": "String (identifier)",
  "state": "String",
  "lastVerifiedDateTime": "String (timestamp)",
  "expiryDateTime": "String (timestamp)"
}
```