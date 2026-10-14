---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: investigationActionStep resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/tenantgovernanceservices-investigationactionstep?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: akhil-potturi
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-tenant-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents an ordered investigation step returned with related tenant metrics to help callers drill into the signals behind an aggregate metric.
ms.date: 2026-07-09T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1028
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 01f86e2d-a018-2fd5-d626-64cfef12cf18
document_version_independent_id: 938cec2b-5202-f7cd-71cd-d10138209bab
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/tenantgovernanceservices-investigationactionstep.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/tenantgovernanceservices-investigationactionstep
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/tenantgovernanceservices-investigationactionstep.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/4e834929-0ce1-4c1d-9c81-fcb14721edfb
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/75670257-a3f0-4627-9981-8046f99219e6
platformId: 1a04d856-2a61-6c2a-59a5-3b834e270a3d
---

# investigationActionStep resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents an ordered investigation step returned with [related tenant](tenantgovernanceservices-relatedtenant) metrics to help callers drill into the signals behind an aggregate metric. Each step reuses the Microsoft Graph recommendations pattern: it pairs human-readable guidance with an existing Microsoft Graph or Azure Resource Manager (ARM) API that, when called, reveals more information about the quality, quantity, or source of the connections behind the aggregate metric. Investigation steps are computed at read time and returned through the **investigationHints** relationship on metrics resources such as [b2bRegistrationMetrics](tenantgovernanceservices-b2bregistrationmetrics), [b2BSignInActivityMetrics](tenantgovernanceservices-b2bsigninactivitymetrics), [multiTenantApplicationMetrics](tenantgovernanceservices-multitenantapplicationmetrics), and [billingMetrics](tenantgovernanceservices-billingmetrics).

## Properties

| Property | Type | Description |
| --- | --- | --- |
| actionUrl | [microsoft.graph.investigationActionUrl](tenantgovernanceservices-investigationactionurl) | The follow-on API reference for the step, containing the URL template and a machine-readable execution directive that a client uses to retrieve the drill-in data. |
| stepNumber | String | The one-based order, as a string, in which the step should be evaluated by a client. Steps are intended to be run in ascending **stepNumber** order because later steps can depend on the output of earlier steps. This value is the key of the resource. |
| text | String | Human-readable guidance that explains what the step does and why it's useful for investigating the related metric. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.investigationActionStep",
  "stepNumber": "String (identifier)",
  "text": "String",
  "actionUrl": {
    "@odata.type": "microsoft.graph.investigationActionUrl"
  }
}
```