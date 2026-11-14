---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: authenticationInfo resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/authenticationinfo?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: vikama-microsoft
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents the authentication configuration used to connect to an external system.
ms.date: 2026-11-06T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 62a7dd54-945f-538f-fecd-8a057af2bb57
document_version_independent_id: a88abf59-4c43-5161-2263-49adc2acafa6
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/authenticationinfo.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/authenticationinfo
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/authenticationinfo.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: bb0d2d62-9a33-bb0d-2d8f-8c941c0c56de
---

# authenticationInfo resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents an abstract base type for the authentication configuration used by Microsoft Entra Entitlement Management to connect to an external system. This is an abstract type and can't be created directly. Use one of its derived types instead.

The **authenticationInfo** property of [externalSapAcConnectionInfo](externalsapacconnectioninfo) uses this type.

The following types are derived from authenticationInfo:

- [clientCredentialAuthenticationInfo](clientcredentialauthenticationinfo)

## Methods

None.

## Properties

None.

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.authenticationInfo"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/authenticationinfo?view=graph-rest-beta&accept=text/markdown)
