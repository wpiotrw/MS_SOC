---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: agentCommunicationConfiguration resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/agentcommunicationconfiguration?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: sthapliyal
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: teams
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents the communication configuration for an agent, including the endpoint binding and Teams message notification settings that agents use to receive messages.
ms.date: 2026-07-28T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 6cdf3b56-6d43-1d14-f786-d58450949e56
document_version_independent_id: 23c2a475-00cc-b24d-3df1-79ca87bee946
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/agentcommunicationconfiguration.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/agentcommunicationconfiguration
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/agentcommunicationconfiguration.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 7113eb05-fc9f-e143-58e7-7c444a9afcc4
---

# agentCommunicationConfiguration resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents the communication configuration for an agent, including the endpoint binding (bot ID or callback URI) and the Teams message notification settings that agents use to receive messages.

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| **Agent identity blueprint** |  |  |
| [Get](../agentidentityblueprint-get-communicationconfiguration) | [agentCommunicationConfiguration](agentcommunicationconfiguration) | Read the communication configuration of an [agentIdentityBlueprint](agentidentityblueprint). |
| [Update](../agentidentityblueprint-update-communicationconfiguration) | [agentCommunicationConfiguration](agentcommunicationconfiguration) | Replace the communication configuration of an [agentIdentityBlueprint](agentidentityblueprint). |
| **Agent identity** |  |  |
| [Get](../agentidentity-get-communicationconfiguration) | [agentCommunicationConfiguration](agentcommunicationconfiguration) | Read the communication configuration of an [agentIdentity](agentidentity). |
| [Update](../agentidentity-update-communicationconfiguration) | [agentCommunicationConfiguration](agentcommunicationconfiguration) | Replace the communication configuration of an [agentIdentity](agentidentity). |
| [reset](../agentcommunicationconfiguration-reset) | [agentCommunicationConfiguration](agentcommunicationconfiguration) | Reset the communication configuration override for an agent identity, which restores effective configuration resolution to the agent blueprint level, and returns the blueprint's communication configuration as the new effective configuration. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| endpointConfiguration | [agentEndpointConfiguration](agentendpointconfiguration) | The endpoint binding (bot ID or callback URI) that the agent uses to receive messages. |
| isOverridableAtAgentIdLevel | Boolean | Indicates whether individual agent instances created from this blueprint can override the `endpointConfiguration`. When `true`, each instance can override it; when `false`, every instance inherits it. Not nullable. |
| teamworkConfiguration | [agentTeamworkConfiguration](agentteamworkconfiguration) | The per-conversation-context message notification settings (group chat, channel, one-on-one chat, and meeting chat) that agents use. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.agentCommunicationConfiguration",
  "isOverridableAtAgentIdLevel": "Boolean",
  "endpointConfiguration": {"@odata.type": "microsoft.graph.agentEndpointConfiguration"},
  "teamworkConfiguration": {"@odata.type": "microsoft.graph.agentTeamworkConfiguration"}
}
```