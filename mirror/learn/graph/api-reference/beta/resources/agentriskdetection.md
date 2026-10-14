---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: agentRiskDetection resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/agentriskdetection?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: jiayle27
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-sign-in
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents the agentic risk detections as evaluated by Microsoft Entra ID Protection based on various signals and machine learning.
ms.date: 2025-11-27T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 9bd5247b-6044-9742-23b7-18201982c02b
document_version_independent_id: 9c649c1f-c269-5c94-3678-5f4c32eea2e1
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/agentriskdetection.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/agentriskdetection
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/agentriskdetection.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/079cf7bf-da09-4bd3-ab74-bd5a5da031d1
- https://authoring-docs-microsoft.poolparty.biz/devrel/d6f38669-3d05-40f2-afd8-e49f7dd20884
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b606cead-f1a2-4925-9a71-5fbd7a0d9b81
- https://authoring-docs-microsoft.poolparty.biz/devrel/55265cca-de9b-48dc-a77a-9047cc39a575
platformId: 699abab6-bc39-8eb1-b58a-8b26443993c9
---

# agentRiskDetection resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents the agentic risk detections as evaluated by Microsoft Entra ID Protection based on various signals and machine learning.

Inherits from [entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../identityprotectionroot-list-agentriskdetections) | [agentRiskDetection](agentriskdetection) collection | Get a list of the agentRiskDetection objects and their properties. |
| [Get](../agentriskdetection-get) | [agentRiskDetection](agentriskdetection) | Read the properties and relationships of [agentRiskDetection](agentriskdetection) object. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| activityDateTime | DateTimeOffset | Date and time that the risky activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  Supports `$filter` (`eq`, `le`, and `ge`). |
| additionalInfo | String | Additional information associated with the risk detection. |
| blueprintId | String | The identifier of the [blueprint](agentidentityblueprint) associated with the agent. Nullable. |
| detectedDateTime | DateTimeOffset | Date and time that the risk was detected. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  Supports `$filter` (`eq`, `le`, and `ge`). |
| detectionTimingType | riskDetectionTimingType | Timing of the detected risk (real-time/offline). The possible values are: `notDefined`, `realtime`, `nearRealtime`, `offline`, `unknownFutureValue`. |
| displayName | String | Human-readable name of the identity associated with this risk detection.  Supports `$filter` (`eq`, `startsWith`). |
| id | String | Unique ID of the risk detection. Inherited from [entity](entity). |
| identityId | String | Unique identifier of the identity associated with this risk detection.  Supports `$filter` (`eq`, `startsWith`). |
| identityType | [agentIdentityType](agentidentitytype) | The type of agent identity associated with this risk detection. The possible values are: `agentIdentity`, `agentIdentityBlueprintPrincipal`, `agentUser`, `user`, `unknownFutureValue`. You must use the `Prefer: include-unknown-enum-members` request header to get the following value in this evolvable enum: `agentIdentityBlueprintPrincipal`. Required.  Supports `$filter` (`eq`). |
| lastModifiedDateTime | DateTimeOffset | Date and time that the risk detection was last updated.  Supports `$filter` (`eq`, `le`, and `ge`). |
| riskDetail | [riskDetail](riskdetail) | Details of the detected risk.  Supports `$filter` (`eq`). |
| riskEventType | String | The type of risk event detected.  Supports `$filter` (`eq`). |
| riskEvidence | String | Evidence on the risky activity occurred.  Supports `$filter` (`eq`). |
| riskLevel | riskLevel | Level of the detected risk. The possible values are: `low`, `medium`, `high`, `hidden`, `none`, `unknownFutureValue`.  Supports `$filter` (`eq`). |
| riskState | riskState | The state of a detected agentic risk. The possible values are: `none`, `confirmedSafe`, `dismissed`, `atRisk`, `confirmedCompromised`, `unknownFutureValue`.  Supports `$filter` (`eq`). |
| source | String | The source system that generated the risk detection. Nullable. |
| agentDisplayName (deprecated) | String | Name of the agent. **Deprecated. Use `displayName` instead. This property will be removed after 2027-04-28.** Supports `$filter` (`eq`, `startsWith`). |
| agentId (deprecated) | String | The unique identifier for the agent. **Deprecated. Use `identityId` instead. This property will be removed after 2027-04-28.** See [riskyAgentIdentity](riskyagentidentity), [riskyAgentIdentityBlueprintPrincipal](riskyagentidentityblueprintprincipal), and [riskyAgentUser](riskyagentuser).  Supports `$filter` (`eq`, `startsWith`). |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.agentRiskDetection",
  "id": "String (identifier)",
  "activityDateTime": "String (timestamp)",
  "additionalInfo": "String",
  "agentDisplayName": "String",
  "agentId": "String",
  "blueprintId": "String",
  "detectedDateTime": "String (timestamp)",
  "detectionTimingType": "String",
  "displayName": "String",
  "identityId": "String",
  "identityType": "String",
  "lastModifiedDateTime": "String (timestamp)",
  "riskDetail": "String",
  "riskEventType": "String",
  "riskEvidence": "String",
  "riskLevel": "String",
  "riskState": "String",
  "source": "String"
}
```