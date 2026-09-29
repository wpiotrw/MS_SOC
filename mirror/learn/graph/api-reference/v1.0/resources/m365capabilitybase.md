---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: m365CapabilityBase resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/m365capabilitybase?view=graph-rest-1.0
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
description: Represents an abstract base type for cross-tenant Microsoft 365 capabilities.
ms.date: 2026-08-07T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
toc.title: Microsoft 365 capabilities
locale: en-us
document_id: 5c36493b-eb37-561c-0ade-d7d7ac2c725d
document_version_independent_id: f3a1060a-2615-6956-f82c-379e9409c20b
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/m365capabilitybase.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/m365capabilitybase
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/m365capabilitybase.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: c17ee3b3-c07b-0bc9-c021-8ef80d4415c4
---

# m365CapabilityBase resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents an abstract base type for cross-tenant Microsoft 365 capabilities. This type can't be instantiated directly. Instances are created using specific derived types. All capability instances in a collection are differentiated by the **@odata.type** property.

The following types derive from **m365CapabilityBase**:

- [anonymousCalendarSharingFreeBusyDetail](anonymouscalendarsharingfreebusydetail)
- [anonymousCalendarSharingFreeBusyReviewer](anonymouscalendarsharingfreebusyreviewer)
- [anonymousCalendarSharingFreeBusySimple](anonymouscalendarsharingfreebusysimple)
- [crossTenantCalendarAvailabilityBasic](crosstenantcalendaravailabilitybasic)
- [crossTenantCalendarAvailabilityLimitedDetails](crosstenantcalendaravailabilitylimiteddetails)
- [crossTenantCalendarSharingFreeBusyDetail](crosstenantcalendarsharingfreebusydetail)
- [crossTenantCalendarSharingFreeBusyReviewer](crosstenantcalendarsharingfreebusyreviewer)
- [crossTenantCalendarSharingFreeBusySimple](crosstenantcalendarsharingfreebusysimple)
- [crossTenantMailTipsAll](crosstenantmailtipsall)
- [crossTenantMailTipsLimited](crosstenantmailtipslimited)
- [crossTenantMigration](crosstenantmigration)
- [crossTenantOpenProfileCard](crosstenantopenprofilecard)
- [crossTenantPlacesDeskBooking](crosstenantplacesdeskbooking)
- [crossTenantPlacesRoomBooking](crosstenantplacesroombooking)

## Methods

None.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| inboundAccess | [m365CapabilityInboundAccess](m365capabilityinboundaccess) | The inbound access settings for the capability. |
| lastModifiedDateTime | DateTimeOffset | The automatically updated last modified timestamp for the capability. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024, is `2024-01-01T00:00:00Z`. |
| name | String | The name or identifier of the capability. Key. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.m365CapabilityBase",
  "name": "String (identifier)",
  "lastModifiedDateTime": "String (timestamp)",
  "inboundAccess": {"@odata.type": "microsoft.graph.m365CapabilityInboundAccess"}
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/m365capabilitybase?view=graph-rest-beta&accept=text/markdown)
