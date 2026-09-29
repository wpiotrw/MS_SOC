---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: security resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/security?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: preetikr
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: The security resource is the entry point for the Security object model. It returns a singleton security resource. It doesn't contain any usable properties.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2024-09-12T00:00:00.0000000Z
locale: en-us
document_id: 4de346b4-5111-8d75-4829-e2bcc39df413
document_version_independent_id: ac5e70f9-70bf-2465-b050-75b6da5e6a53
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/security.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/security
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/security.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1577a46d-8446-40bd-bfae-0578362f4d94
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f769bf00-f89e-4c24-8f5f-d0170c0a71cb
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/cdf3f22d-5420-4d59-a2bf-66d6b3d9c828
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/faddc47a-29dc-46f7-b30f-81d9d6c05fa0
platformId: b6733c8a-154a-2f89-559f-38160e5727f4
---

# security resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

The security resource is the entry point for the Security object model. It returns a singleton security resource. It doesn't contain any usable properties.

## Methods

| Method | Return Type | Description |
| --- | --- | --- |
| [Run hunting query](../security-security-runhuntingquery) | [microsoft.graph.security.huntingQueryResults](security-huntingqueryresults) | Queries a specified set of event, activity, or entity data supported by Microsoft 365 Defender to proactively look for specific threats in your environment. |

## Properties

None

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| alerts | [alert](alert) collection | Read-only. Nullable. |
| alerts\_v2 | [microsoft.graph.security.alert](security-alert) collection | A collection of alerts in Microsoft 365 Defender. |
| auditLog | [microsoft.graph.security.auditCoreRoot](security-auditcoreroot) | The entry point for the audit log query API. |
| data security and compliance | [microsoft.graph.tenantDataSecurityAndGovernance](tenantdatasecurityandgovernance) | A container for Microsoft Purview data security and compliance APIs. |
| identities | [microsoft.graph.security.identityContainer](security-identitycontainer) | A container for security identities APIs. |
| incidents | [microsoft.graph.security.incident](security-incident) collection | A collection of incidents in Microsoft 365 Defender, each of which is a set of correlated alerts and associated metadata that reflects the story of an attack. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
}
```

## Example

The **security** resource is available at the root of the graph.

```http
GET https://graph.microsoft.com/v1.0/security
```

```http
HTTP/1.1 200 OK
Content-type: application/json

{
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/security?view=graph-rest-beta&accept=text/markdown)
