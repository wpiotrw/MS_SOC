---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: caseSlaPolicyEntry resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/security-casemanagement-caseslapolicyentry?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: msklotz
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a single SLA policy's denormalized status for a case.
ms.date: 2026-08-26T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 9984f244-1562-17a6-5c3e-435bd6abfa05
document_version_independent_id: b34764ac-2d49-416f-a9c1-ba84241b01ce
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/security-casemanagement-caseslapolicyentry.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/security-casemanagement-caseslapolicyentry
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/security-casemanagement-caseslapolicyentry.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 49e4be02-0310-8722-3673-f85755ee8fab
---

# caseSlaPolicyEntry resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph.security.caseManagement

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents a single SLA (service level agreement) policy's denormalized status for a [case](security-casemanagement-case). Returned as an entry in the **slaPolicies** collection on a case. This resource is entirely server-computed; the SLA policy engine assigns and maintains SLA policies independently of the case management API.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| breachTargetDateTime | DateTimeOffset | The date and time the SLA policy is targeted to breach, if applicable. `null` when the policy is paused or completed. Computed by the service. |
| policyDisplayName | String | The display name of the SLA policy. Computed by the service. |
| policyId | String | The unique identifier of the SLA policy, assigned by the SLA policy engine. Computed by the service. |
| status | microsoft.graph.security.caseManagement.caseSlaPolicyStatus | The current SLA status for this policy on this case. Computed by the service. |

### caseSlaPolicyStatus values

| Member | Description |
| --- | --- |
| active | The SLA policy is actively tracked and within its target. |
| atRisk | The SLA policy is at risk of breaching its target. |
| breached | The SLA policy has breached its target. |
| paused | Tracking for the SLA policy is paused. |
| completedMet | The SLA policy completed within its target. |
| completedBreached | The SLA policy completed after breaching its target. |
| unknownFutureValue | Evolvable enumeration sentinel value. Don't use. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.security.caseManagement.caseSlaPolicyEntry",
  "policyId": "String",
  "policyDisplayName": "String",
  "status": "String",
  "breachTargetDateTime": "DateTimeOffset"
}
```