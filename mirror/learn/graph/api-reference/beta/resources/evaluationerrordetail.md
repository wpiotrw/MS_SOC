---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: evaluationErrorDetail resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/evaluationerrordetail?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: zhengnlu
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents the reason why a policy evaluation couldn't be completed.
ms.date: 2026-09-10T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: ca6948e0-9017-d4cc-518d-d67ca513ea04
document_version_independent_id: 82f815df-20f5-fa58-8f6b-f784af160d42
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/evaluationerrordetail.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/evaluationerrordetail
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/evaluationerrordetail.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: ef61e78d-48e6-029b-7bcb-9de9e3c2a372
---

# evaluationErrorDetail resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents the structured reason for the **inspectionIncompleteReason** property of [evaluationIncompleteActivityMetadata](evaluationincompleteactivitymetadata) when a policy evaluation couldn't be completed.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| errorCategory | [evaluationErrorCategory](enums#evaluationerrorcategory-values) | The high-level category of the error. Required. The possible values are: `unknown`, `systemLimit`, `systemError`, `enforcementError`, `unknownFutureValue`. |
| errorType | [evaluationErrorType](enums#evaluationerrortype-values) | The specific reason the evaluation couldn't be completed. Required. The possible values are: `unsupportedFile`, `passwordProtectedFile`, `missingOrInvalidConfiguration`, `agentFailure`, `enforcementTimeout`, `osOverride`, `processNonExistent`, `other`, `serviceTimeout`, `serviceError`, `serviceUnavailable`, `contentTooLarge`, `partiallyScanned`, `unscannable`, `billingNotSetup`, `authenticationOrAuthorizationFailed`, `unknownFutureValue`. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.evaluationErrorDetail",
  "errorCategory": "String",
  "errorType": "String"
}
```