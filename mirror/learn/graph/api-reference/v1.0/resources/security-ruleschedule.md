---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: ruleSchedule resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/security-ruleschedule?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: mmekler
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents how often the custom detection rule runs, and when it next runs.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-08-25T00:00:00.0000000Z
locale: en-us
document_id: 7cfe8543-31ac-7a73-0dbd-dccb677ba0ac
document_version_independent_id: 6d3f8fa5-562d-c0e1-8995-552fb73d5a3d
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/security-ruleschedule.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/security-ruleschedule
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/security-ruleschedule.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 4579d600-935f-5d60-ed04-9e664d531bbc
---

# ruleSchedule resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.security

Represents how often the [custom detection rule](security-detectionrule) runs, and when it next runs.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| frequency | Duration | The recurring time interval at which the rule runs (ISO 8601 duration, for example P1D for daily, PT1H for hourly). |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.security.ruleSchedule",
  "frequency": "String (duration)"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/security-ruleschedule?view=graph-rest-beta&accept=text/markdown)
