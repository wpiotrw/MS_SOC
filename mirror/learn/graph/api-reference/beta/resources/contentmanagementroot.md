---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: contentManagementRoot resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/contentmanagementroot?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: AlexBrohshtut
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: security
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Provides the entry point under `/security` for content repositories, the published security content catalog, and the tenant's installed content.
ms.date: 2026-11-02T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 1d1f297e-f3c4-9c3a-042b-812279b9c79b
document_version_independent_id: 9ae6d906-9b37-bf06-791e-9779d089ce99
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/contentmanagementroot.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/contentmanagementroot
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/contentmanagementroot.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 0f5358e4-2999-0550-8257-41b8ea08db10
---

# contentManagementRoot resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Provides the entry point under `/security` for content repositories, the published security content catalog, and the tenant's installed content.

Inherits from [entity](entity).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List installedPackageContents](../contentmanagementroot-list-installedpackagecontents) | [microsoft.graph.security.contentManagement.installedContentItem](security-contentmanagement-installedcontentitem) collection | List installed content items across all installed packages. |
| [List installedPackages](../contentmanagementroot-list-installedpackages) | [microsoft.graph.security.contentManagement.installedPackage](security-contentmanagement-installedpackage) collection | List the content packages installed in the tenant. |
| [List packageContents](../contentmanagementroot-list-packagecontents) | [microsoft.graph.security.contentManagement.contentItem](security-contentmanagement-contentitem) collection | List published content items across all catalog packages. |
| [List packages](../contentmanagementroot-list-packages) | [microsoft.graph.security.contentManagement.contentPackage](security-contentmanagement-contentpackage) collection | List content packages published in the catalog. |
| [List repositories](../contentmanagementroot-list-repositories) | [microsoft.graph.security.contentManagement.contentManagementRepository](security-contentmanagement-contentmanagementrepository) collection | Get the source-control repositories connected to the tenant. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| id | String | A unique identifier for this resource. Inherited from [entity](entity). |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| installedPackageContents | [microsoft.graph.security.contentManagement.installedContentItem](security-contentmanagement-installedcontentitem) collection | Installed content items listed across every installed package. |
| installedPackages | [microsoft.graph.security.contentManagement.installedPackage](security-contentmanagement-installedpackage) collection | Content packages the tenant has installed, keyed the same way as **packages** so the same identity addresses the catalog entry and the tenant's installation of it. |
| packageContents | [microsoft.graph.security.contentManagement.contentItem](security-contentmanagement-contentitem) collection | Read-only content items published across packages for cross-package discovery. |
| packages | [microsoft.graph.security.contentManagement.contentPackage](security-contentmanagement-contentpackage) collection | Content packages published in the catalog and available to install. Read-only. |
| repositories | [microsoft.graph.security.contentManagement.contentManagementRepository](security-contentmanagement-contentmanagementrepository) collection | Connected source-control repositories that deliver security content as code. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.contentManagementRoot",
  "id": "String (identifier)"
}
```