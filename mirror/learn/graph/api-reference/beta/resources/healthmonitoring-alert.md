---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: alert resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/healthmonitoring-alert?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: HuaTang92
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-monitoring-health
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a system-detected health monitoring alert associated with common Microsoft Entra authentication and access management scenarios.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-10-13T00:00:00.0000000Z
locale: en-us
document_id: f6d6b226-891e-8dc8-4137-bac18e9a3967
document_version_independent_id: 4b0293e7-b5c1-36ba-cb21-518b97ae0d23
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/healthmonitoring-alert.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/healthmonitoring-alert
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/healthmonitoring-alert.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 04e65d0a-6efe-9856-d9f5-4484e2864476
---

# alert resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph.healthMonitoring

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents a system-detected health monitoring alert associated with common Microsoft Entra authentication and access management scenarios. Anomaly detection catches unusual patterns in health metrics data streams, for example, unusually high MFA sign-in failures, and surfaces these patterns in the form of alerts in Microsoft Entra Health monitoring.

This resource supports subscribing to [change notifications](/en-us/graph/change-notifications-overview).

Inherits from [microsoft.graph.entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../healthmonitoring-healthmonitoringroot-list-alerts) | [microsoft.graph.healthMonitoring.alert](healthmonitoring-alert) collection | Get a list of the [microsoft.graph.healthMonitoring.alert](healthmonitoring-alert) objects and their properties. |
| [Get](../healthmonitoring-alert-get) | [microsoft.graph.healthMonitoring.alert](healthmonitoring-alert) | Read the properties and relationships of a [microsoft.graph.healthMonitoring.alert](healthmonitoring-alert) object. |
| [Update](../healthmonitoring-alert-update) | [microsoft.graph.healthMonitoring.alert](healthmonitoring-alert) | Update the properties of a [microsoft.graph.healthMonitoring.alert](healthmonitoring-alert) object. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| alertType | microsoft.graph.healthMonitoring.alertType | Indicates the type of alert. The possible values are: `unknown`, `mfaSignInFailure`, `managedDeviceSignInFailure`, `compliantDeviceSignInFailure`, `unknownFutureValue`, `conditionalAccessBlockedSignIn`, `samlSignInFailure`, `internetAppBlockedByPolicy`, `privateAppBlockedByConnector`, `remoteNetworkTunnelConnectivity`, `remoteNetworkBgpConnectivity`, `agentIdAutonomousSignInFailure`, `agentIdInteractiveSignInFailure`. Use the `Prefer: include-unknown-enum-members` request header to get the following value or values in this [evolvable enum](/en-us/graph/best-practices-concept#handling-future-members-in-evolvable-enumerations): `conditionalAccessBlockedSignIn`, `samlSignInFailure`, `internetAppBlockedByPolicy`, `privateAppBlockedByConnector`, `remoteNetworkTunnelConnectivity`, `remoteNetworkBgpConnectivity`, `agentIdAutonomousSignInFailure`, `agentIdInteractiveSignInFailure`. Supports `$filter` (`eq`). |
| category | microsoft.graph.healthMonitoring.category | The classification that groups the scenario. The possible values are: `unknown`, `authentication`, `unknownFutureValue`. |
| createdDateTime | DateTimeOffset | The time when Microsoft Entra Health monitoring generated the alert. Supports `$orderby`. |
| documentation | [microsoft.graph.healthMonitoring.documentation](healthmonitoring-documentation) | A key-value pair that contains the name of and link to the documentation to aid in investigation of the alert. |
| enrichment | [microsoft.graph.healthMonitoring.enrichment](healthmonitoring-enrichment) | Investigative information on the alert. This information typically includes counts of impacted objects, which include directory objects such as users, groups, and devices, and a pointer to supporting data. |
| id | String | The unique GUID identifier of this alert in the associated tenant. Inherited from [microsoft.graph.entity](entity). |
| scenario | microsoft.graph.healthMonitoring.scenario | The area being monitored on the system that is emitting the source signals. The possible values are: `unknown`, `mfa`, `devices`, `unknownFutureValue`, `conditionalAccess`, `saml`, `gsa`, `agentId`. Use the `Prefer: include-unknown-enum-members` request header to get the following value or values in this [evolvable enum](/en-us/graph/best-practices-concept#handling-future-members-in-evolvable-enumerations): `conditionalAccess`, `saml`, `gsa`, `agentId`. |
| signals | [microsoft.graph.healthMonitoring.signals](healthmonitoring-signals) | The collection of signals that were used in the generation of the alert. These signals are sourced from [serviceActivity APIs](serviceactivity) and are added to the alert as key-value pairs. |
| state | microsoft.graph.healthMonitoring.alertState | The current lifecycle state of the alert. The possible values are: `active`, `resolved`, `unknownFutureValue`. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.healthMonitoring.alert",
  "id": "String (identifier)",
  "alertType": "String",
  "scenario": "String",
  "category": "String",
  "createdDateTime": "String (timestamp)",
  "state": "String",
  "enrichment": {
    "@odata.type": "microsoft.graph.healthMonitoring.enrichment"
  },
  "signals": {
    "@odata.type": "microsoft.graph.healthMonitoring.signals"
  },
  "documentation": {
    "@odata.type": "microsoft.graph.healthMonitoring.documentation"
  }
}
```