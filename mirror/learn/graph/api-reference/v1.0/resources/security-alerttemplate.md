---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: alertTemplate resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/security-alerttemplate?view=graph-rest-1.0
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
description: Describes the alert that is generated in response to a detection by a custom detection rule.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-08-25T00:00:00.0000000Z
locale: en-us
document_id: 58c21c0c-8eff-5a9d-9371-7f7c1f1545d3
document_version_independent_id: 33e4aa06-bc03-955f-4689-c1395336a144
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/security-alerttemplate.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/security-alerttemplate
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/security-alerttemplate.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: eb32efb5-5c30-3ed3-e82b-f06c9496a108
---

# alertTemplate resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph.security

Describes the alert that is generated in response to a detection by a [custom detection rule](security-detectionrule), including the alert metadata, recommended actions, custom details, MITRE tactics, and entity mappings.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| customDetails | [microsoft.graph.security.alertCustomDetails](security-alertcustomdetails) | Custom key-value detail pairs to include in the alert. Each value identifies the detection query column that supplies the corresponding custom detail. |
| description | String | Description of the alert triggered by the custom detection rule. |
| entityMappings | [microsoft.graph.security.entityMappingConfiguration](security-entitymappingconfiguration) | Defines how detection query columns map to the entities that are attached to the resulting alert. |
| recommendedActions | String | Recommended actions to mitigate the threat related to the alert triggered by the custom detection rule. |
| severity | [microsoft.graph.security.alertSeverity](security-alert#alertseverity-values) | Severity assigned to the alert triggered by the custom detection rule. The possible values are: `informational`, `low`, `medium`, `high`. |
| tactics | [microsoft.graph.security.mitreTactic](security-mitretactic) collection | The MITRE ATT&CK tactics framing for this alert. |
| title | String | Name of the alert triggered by the custom detection rule. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.security.alertTemplate",
  "customDetails": {
    "@odata.type": "microsoft.graph.security.alertCustomDetails"
  },
  "description": "String",
  "entityMappings": {
    "@odata.type": "microsoft.graph.security.entityMappingConfiguration"
  },
  "recommendedActions": "String",
  "severity": "String",
  "tactics": [
    {
      "@odata.type": "microsoft.graph.security.mitreTactic"
    }
  ],
  "title": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/security-alerttemplate?view=graph-rest-beta&accept=text/markdown)
