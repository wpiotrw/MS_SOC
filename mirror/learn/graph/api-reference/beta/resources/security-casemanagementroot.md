---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: caseManagementRoot resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/security-casemanagementroot?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: alfeldsh
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents the entry point for Microsoft Graph security case management APIs.
ms.date: 2026-05-29T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 81cdad3f-bd8c-5a06-9f7a-c8f5ee78a2e7
document_version_independent_id: 8ef36954-349d-bbb0-8316-a68ca1adec04
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/security-casemanagementroot.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/security-casemanagementroot
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/security-casemanagementroot.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 93fd8c26-efcb-786b-1b8e-b0ba91e738b7
---

# caseManagementRoot resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph.security

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents the entry point for Microsoft Graph security case management APIs. Use this resource to access cases that organize security investigations, related work, activities, and evidence.

| Context | Example |
| --- | --- |
| URL cast segment | `.../cases/microsoft.graph.security.caseManagement.incidentCase` |
| JSON body discriminator | `"@odata.type": "#microsoft.graph.security.caseManagement.incidentCase"` |

## Methods

None.

## Properties

None.

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| caseTypeConfigurations | [microsoft.graph.security.caseManagement.caseTypeConfiguration](security-casemanagement-casetypeconfiguration) collection | The collection of case type configurations that define the statuses and custom fields available for each case type. Read-only. Supports `$select`, `$count`, and `$expand` of the `statuses` and `customFields` relationships. |
| cases | [microsoft.graph.security.caseManagement.case](security-casemanagement-case) collection | The collection of security cases managed through the case management entry point. Supports `$filter`, `$orderby`, `$select`, `$top`, and `$skip`. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.security.caseManagementRoot"
}
```