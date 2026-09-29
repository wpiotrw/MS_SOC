---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: anonymousCalendarSharingFreeBusyDetail resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/anonymouscalendarsharingfreebusydetail?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: lasharma
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-sign-in
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a capability for anonymous detailed free/busy calendar sharing.
ms.date: 2026-09-16T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: fc5b461e-545a-50d6-5e5a-1cba29596da3
document_version_independent_id: 5c2a5a02-3e87-d19b-65b0-80853e40e46c
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/anonymouscalendarsharingfreebusydetail.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/anonymouscalendarsharingfreebusydetail
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/anonymouscalendarsharingfreebusydetail.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: fd5cbd03-6a7c-c0f1-f863-c4487bc940fa
---

# anonymousCalendarSharingFreeBusyDetail resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents authorization for anonymous external users to view detailed calendar free/busy information, including meeting subject and location.

Inherits from [m365CapabilityBase](m365capabilitybase).

## Methods

This resource is part of a polymorphic collection managed by the [m365CapabilityBase](m365capabilitybase) base type. Operations are performed through the base type endpoints on the [crossTenantAccessPolicyConfigurationDefault](crosstenantaccesspolicyconfigurationdefault) or [crossTenantAccessPolicyConfigurationPartner](crosstenantaccesspolicyconfigurationpartner) resources.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| inboundAccess | [m365CapabilityInboundAccess](m365capabilityinboundaccess) | The inbound access settings for the capability. Inherited from [m365CapabilityBase](m365capabilitybase). |
| lastModifiedDateTime | DateTimeOffset | The automatically updated last modified timestamp for the capability. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024, is `2024-01-01T00:00:00Z`. Inherited from [m365CapabilityBase](m365capabilitybase). |
| name | String | The name or identifier of the capability. Inherited from [m365CapabilityBase](m365capabilitybase). |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.anonymousCalendarSharingFreeBusyDetail",
  "name": "String (identifier)",
  "lastModifiedDateTime": "String (timestamp)",
  "inboundAccess": {"@odata.type": "microsoft.graph.m365CapabilityInboundAccess"}
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/anonymouscalendarsharingfreebusydetail?view=graph-rest-beta&accept=text/markdown)
