---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: anonymousCalendarSharingFreeBusySimple resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/anonymouscalendarsharingfreebusysimple?view=graph-rest-1.0
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
description: Represents a capability for anonymous simple free/busy calendar sharing.
ms.date: 2026-09-16T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: db71d4ca-c58c-4dc5-140e-c9ba87d4956d
document_version_independent_id: 8b0b551b-1f6d-07b5-2d06-43b6afdeacb0
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/anonymouscalendarsharingfreebusysimple.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/anonymouscalendarsharingfreebusysimple
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/anonymouscalendarsharingfreebusysimple.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 85cdb187-b553-2ac8-852f-3f54f3cae441
---

# anonymousCalendarSharingFreeBusySimple resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents authorization for anonymous external users to view simple calendar free/busy status, shown as busy or free.

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
  "@odata.type": "#microsoft.graph.anonymousCalendarSharingFreeBusySimple",
  "name": "String (identifier)",
  "lastModifiedDateTime": "String (timestamp)",
  "inboundAccess": {"@odata.type": "microsoft.graph.m365CapabilityInboundAccess"}
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/anonymouscalendarsharingfreebusysimple?view=graph-rest-beta&accept=text/markdown)
