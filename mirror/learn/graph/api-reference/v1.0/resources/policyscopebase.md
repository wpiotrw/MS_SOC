---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: policyScopeBase resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/policyscopebase?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: kylemar
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Abstract base type defining the scope of applicability for a data governance policy, including locations, activities, and execution mode.
ms.date: 2025-04-08T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 86f72c0e-2bfa-460f-c551-2de3e7c6fabc
document_version_independent_id: 912a4b56-7552-6e56-af86-7ffd493e06b9
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/policyscopebase.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/policyscopebase
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/policyscopebase.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: c8048b75-be6b-a190-add0-0f2734db9eb2
---

# policyScopeBase resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Abstract base type defining the scope of applicability for a data governance policy, including locations, activities, and execution mode.

Used as a base type for more specific policy scopes like [policyTenantScope](policytenantscope) and [policyUserScope](policyuserscope).

## Properties

| Property | Type | Description |
| --- | --- | --- |
| activities | microsoft.graph.security.userActivityTypes | Flags specifying the user activities the calling application supports or is interested. Possible values are `none`, `uploadText`, `uploadFile`, `downloadText`, `downloadFile`, `unknownFutureValue`. Required. This object is a multi-valued enumeration. |
| executionMode | microsoft.graph.security.executionMode | Specifies how the policy should be executed. Possible values are `evaluateInline`, `evaluateOffline`, `unknownFutureValue`. Required. |
| locations | Collection([microsoft.graph.policyLocation](policylocation)) | The locations (like domains or URLs) to be protected. Required. |
| policyActions | Collection([microsoft.graph.dlpActionInfo](dlpactioninfo)) | The enforcement actions to take if the policy conditions are met within this scope. Required. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.policyScopeBase",
  "activities": "String",
  "executionMode": "String",
  "locations": [
    {
      "@odata.type": "microsoft.graph.policyLocation"
    }
  ],
  "policyActions": [
    {
      "@odata.type": "microsoft.graph.dlpActionInfo"
    }
  ]
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/policyscopebase?view=graph-rest-beta&accept=text/markdown)
