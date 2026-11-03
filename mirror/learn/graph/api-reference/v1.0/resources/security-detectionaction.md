---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: detectionAction resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/security-detectionaction?view=graph-rest-1.0
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
description: Describes the actions that will be taken after a detection is made by the custom detection rule.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-08-25T00:00:00.0000000Z
locale: en-us
document_id: a63ff487-05f7-3a2c-10ae-a537f3b508bb
document_version_independent_id: d2e68e5e-cdf5-62b4-95e8-190fb0e087b5
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/security-detectionaction.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/security-detectionaction
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/security-detectionaction.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 32817113-9db6-a3e7-7b90-960773e0f627
---

# detectionAction resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.security

Describes the actions that are taken after a detection is made by a [custom detection rule](security-detectionrule), including the alert that is created and any automated actions that run against impacted entities.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| alertTemplate | [microsoft.graph.security.alertTemplate](security-alerttemplate) | The template that defines the alert that is generated when this rule detects a match, including alert metadata (severity, title, description), entity mappings, custom details, and MITRE tactics. |
| automatedActions | [microsoft.graph.security.automatedActionSet](security-automatedactionset) | The set of automated actions to run against entities that match the detection. |
| organizationalScope | [microsoft.graph.security.organizationalScope](security-organizationalscope) | The set of groups (for example, device groups) to which the parent custom detection rule applies. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.security.detectionAction",
  "alertTemplate": {
    "@odata.type": "microsoft.graph.security.alertTemplate"
  },
  "automatedActions": {
    "@odata.type": "microsoft.graph.security.automatedActionSet"
  },
  "organizationalScope": {
    "@odata.type": "microsoft.graph.security.organizationalScope"
  }
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/security-detectionaction?view=graph-rest-beta&accept=text/markdown)
