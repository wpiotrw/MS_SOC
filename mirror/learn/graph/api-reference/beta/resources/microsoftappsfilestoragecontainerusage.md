---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: microsoftAppsFileStorageContainerUsage resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/microsoftappsfilestoragecontainerusage?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: anjkumari
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: reports
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents tenant-level storage usage data for SharePoint Embedded file storage containers.
ms.date: 2026-06-25T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 703887ac-3778-9779-e1a8-1b4bb7d0d894
document_version_independent_id: 02cd7eed-ae48-dbf4-a51b-fec753ff977f
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/microsoftappsfilestoragecontainerusage.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/microsoftappsfilestoragecontainerusage
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/microsoftappsfilestoragecontainerusage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 9d924947-80a6-fdcf-724b-8d13ba4627a2
---

# microsoftAppsFileStorageContainerUsage resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents tenant-level storage usage data for SharePoint Embedded file storage containers.

This resource provides aggregated metrics including total storage used and container count across the tenant, with the ability to expand to geo-level and app-level details.

Inherits from [entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [Get SharePoint Embedded file storage container usage summary](../reportroot-getmicrosoftappsfilestoragecontainerusagesummary) | [microsoftAppsFileStorageContainerUsage](microsoftappsfilestoragecontainerusage) | Get storage usage data for SharePoint Embedded file storage containers in a tenant. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| id | String | The unique identifier for the usage summary. The value is always `microsoftAppsFileStorageContainerUsageSummary`. Inherits from [entity](entity). |
| totalActiveContainerCount | Int64 | The total number of active file storage containers across the tenant. |
| totalActiveStorageUsedInBytes | Int64 | The total storage used in bytes across all active file storage containers in the tenant. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| usageByDataLocation | [microsoftAppsFileStorageContainerGeoUsage](microsoftappsfilestoragecontainergeousage) collection | Storage usage data broken down by geographic location. Expandable using `$expand=usageByDataLocation`. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.microsoftAppsFileStorageContainerUsage",
  "id": "String (identifier)",
  "totalActiveStorageUsedInBytes": "Int64",
  "totalActiveContainerCount": "Int64",
  "usageByDataLocation": [{"@odata.type": "#microsoft.graph.microsoftAppsFileStorageContainerGeoUsage"}]
}
```