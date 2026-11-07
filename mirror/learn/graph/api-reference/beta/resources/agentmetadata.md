---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: agentMetadata resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/agentmetadata?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: psanyal
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents metadata used to identify and evaluate an agent for data loss prevention policies.
ms.date: 2026-09-02T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 56488398-73df-2a5b-b988-1300cc071b59
document_version_independent_id: 8f3805e1-d68d-d5f8-06a3-90c180510ed5
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/agentmetadata.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/agentmetadata
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/agentmetadata.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: f0df5b51-cf78-0e2f-219f-5c662b50a675
---

# agentMetadata resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents metadata used to identify and evaluate an agent for data loss prevention (DLP) policies.

Configured in the **agentMetadata** property of [policyLocationAgent](policylocationagent).

## Properties

| Property | Type | Description |
| --- | --- | --- |
| agentAdministrativeUnitId | String | The identifier of the administrative unit associated with the agent. Optional. |
| agentBlueprintId | String | The identifier of the blueprint from which the agent was created. Optional. |
| agentCategory | String | The category of the agent, for example, `Agents.Foundry.MicrosoftAzure`, `Agents.Copilot.Studio`, or `Agents.Local`. Optional. |
| agentOwner | String | The owner associated with the agent. Optional. |
| agentPublisher | String | The publisher associated with the agent. Optional. |
| altAgentIds | String collection | Alternate identifiers that can identify the agent. Required when **agentMetadata** is provided. Use an empty collection (`[]`) when the agent has no alternate identifiers. |
| isEntraAgentId | Boolean | Indicates whether the **value** property of the associated [policyLocationAgent](policylocationagent) is a Microsoft Entra agent ID. Required when **agentMetadata** is provided. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.agentMetadata",
  "agentAdministrativeUnitId": "String",
  "agentBlueprintId": "String",
  "agentCategory": "String",
  "agentOwner": "String",
  "agentPublisher": "String",
  "altAgentIds": [
    "String"
  ],
  "isEntraAgentId": "Boolean"
}
```