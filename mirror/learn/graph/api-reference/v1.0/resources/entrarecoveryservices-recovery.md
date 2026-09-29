---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: recovery resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/entrarecoveryservices-recovery?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: yuhko-msft
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents the entry point for the Microsoft Entra Backup and Recovery service for a tenant.
ms.date: 2026-06-05T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 0cc1ea21-842d-55b4-8db4-b63d0239d57f
document_version_independent_id: 2c4c2c5a-be22-c043-ef18-5a564e961de9
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/entrarecoveryservices-recovery.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/entrarecoveryservices-recovery
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/entrarecoveryservices-recovery.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aebdc4a3-c54b-4eea-94e3-663d5e166f57
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1baec8e6-ab38-4b56-bb59-f6282d94f311
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: ad105e02-f004-12d6-ee0c-19edd98c6b7f
---

# recovery resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.entraRecoveryServices

Represents the entry point for the Microsoft Entra Backup and Recovery service. Provides access to snapshots and recovery jobs for a tenant, enabling administrators to restore directory objects to a previous state.

## Methods

None.

## Properties

None.

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| jobs | [microsoft.graph.entraRecoveryServices.recoveryJobBase](entrarecoveryservices-recoveryjobbase) collection | Collection of all recovery jobs (both preview and recovery) for the tenant. |
| snapshots | [microsoft.graph.entraRecoveryServices.snapshot](entrarecoveryservices-snapshot) collection | Collection of backup snapshots available for the tenant. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.entraRecoveryServices.recovery"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/entrarecoveryservices-recovery?view=graph-rest-beta&accept=text/markdown)
