---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: contentPackage resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/security-contentmanagement-contentpackage?view=graph-rest-beta
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
description: Represents a content package published in the security content catalog at its latest published version.
ms.date: 2026-11-02T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: f72a148b-56e2-e7b4-1307-48b17d0325fd
document_version_independent_id: 6772c542-d635-4f20-d0d2-937ce7dfda12
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/security-contentmanagement-contentpackage.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/security-contentmanagement-contentpackage
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/security-contentmanagement-contentpackage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d56bfe0c-ecd5-4d90-854f-35482bbb1314
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/02e99b71-5808-477b-9387-4c6efa24e46b
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 2eb69f05-b912-dc3d-bfc9-8021d495f073
---

# contentPackage resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph.security.contentManagement

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents a content package published in the security content catalog at its latest published version. Catalog packages are read-only publisher state; tenants manage installations through [installedPackage](security-contentmanagement-installedpackage).

Inherits from [contentPackageBase](security-contentmanagement-contentpackagebase). Catalog and installed packages share publisher metadata through this base type, but retain separate endpoints and lifecycle behavior.

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List packages](../contentmanagementroot-list-packages) | [microsoft.graph.security.contentManagement.contentPackage](security-contentmanagement-contentpackage) collection | List content packages published in the catalog. |
| [Get contentPackage](../security-contentmanagement-contentpackage-get) | [microsoft.graph.security.contentManagement.contentPackage](security-contentmanagement-contentpackage) | Read the properties and relationships of a contentPackage object. |
| [List contents](../security-contentmanagement-contentpackage-list-contents) | [microsoft.graph.security.contentManagement.contentItem](security-contentmanagement-contentitem) collection | List the content items shipped by a published contentPackage. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| author | [microsoft.graph.security.contentManagement.contentAuthor](security-contentmanagement-contentauthor) | The package author. Inherited from [contentPackageBase](security-contentmanagement-contentpackagebase). Read-only. Supports `$filter` (`eq`, `ne`) on `author/displayName`. |
| categories | [microsoft.graph.security.contentManagement.contentCategories](security-contentmanagement-contentcategories) | Publisher taxonomy for the package. Inherited from [contentPackageBase](security-contentmanagement-contentpackagebase). Read-only. Supports `$filter` (`any`) on `categories/domains` and `categories/verticals`. |
| contentProductId | String | ARM-facing product identifier of the package in Azure Marketplace and Azure Resource Manager, distinct from the version-stable **id**. Inherited from [contentPackageBase](security-contentmanagement-contentpackagebase). Read-only. Supports `$filter` (`eq`, `ne`). |
| dependencies | [Json](json) | Publisher-defined package prerequisites and bill-of-materials criteria as JSON. Returned on by-key reads; unavailable on collection reads even with `$select`. Read-only. |
| description | String | Plain-text description of the latest version, when supplied by the publisher. Inherited from [contentPackageBase](security-contentmanagement-contentpackagebase). Read-only. |
| descriptionHtml | String | Publisher-authored description of the latest version, including HTML markup. Callers that render this field must sanitize it as untrusted markup. Inherited from [contentPackageBase](security-contentmanagement-contentpackagebase). Read-only. |
| displayName | String | Display name of the latest version of the package. Read-only. Supports `$filter` (`eq`, `ne`) and `$orderby`. |
| firstPublishDateTime | DateTimeOffset | Date and time when the package was first published, in UTC. Null when unknown. Read-only. Supports `$filter` (`eq`, `ne`, `gt`, `ge`, `lt`, `le`) and `$orderby`. |
| icon | String | Publisher-authored icon reference for the package, when declared. Inherited from [contentPackageBase](security-contentmanagement-contentpackagebase). Read-only. |
| id | String | Stable identifier of the package across versions. Inherited from [entity](entity). Read-only. Supports `$filter` (`eq`, `ne`). |
| isDeprecated | Boolean | Indicates whether the package is deprecated in this catalog generation. Read-only. Supports `$filter` (`eq`, `ne`). |
| isFeatured | Boolean | Indicates whether the package is editorially promoted by the publisher. Read-only. Supports `$filter` (`eq`, `ne`). |
| isNew | Boolean | Indicates whether the package is marked as new by the publisher. Read-only. Supports `$filter` (`eq`, `ne`). |
| isPreview | Boolean | Indicates whether the latest version is a prerelease, as declared by the publisher. Read-only. Supports `$filter` (`eq`, `ne`). |
| kind | String | Package kind, such as `Solution` or `Standalone`. Open string defined by the publisher; null when no kind is declared. Read-only. Supports `$filter` (`eq`, `ne`). |
| lastPublishDateTime | DateTimeOffset | Date and time when the package was last published, in UTC. Null when unknown. Read-only. Supports `$filter` (`eq`, `ne`, `gt`, `ge`, `lt`, `le`) and `$orderby`. |
| mainTemplate | [Json](json) | Publisher-defined deployment template as a direct JSON object. Included by default on by-key reads; unavailable on collection reads even with `$select`. Read-only. |
| migratedToPackageId | String | Publisher-supplied identifier of the package that this package migrated to, when applicable. Read-only. |
| providers | String collection | Security providers for which the package delivers content. Inherited from [contentPackageBase](security-contentmanagement-contentpackagebase). Read-only. Supports `$filter` (`any`). |
| publisherDisplayName | String | Display name of the publishing organization. Inherited from [contentPackageBase](security-contentmanagement-contentpackagebase). Read-only. Supports `$filter` (`eq`, `ne`). |
| source | [microsoft.graph.security.contentManagement.contentPackageSource](security-contentmanagement-contentpackagesource) | Publisher source information. Returned on by-key reads; unavailable on collection reads even with `$select`. Read-only. |
| support | [microsoft.graph.security.contentManagement.contentSupport](security-contentmanagement-contentsupport) | Support contact and tier information for the package. Inherited from [contentPackageBase](security-contentmanagement-contentpackagebase). Read-only. Supports `$filter` (`eq`, `ne`) on `support/tier` and `support/displayName`. |
| version | String | Latest version of the package in the committed catalog generation. Read-only. Supports `$filter` (`eq`, `ne`) and `$orderby`. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| contents | [microsoft.graph.security.contentManagement.contentItem](security-contentmanagement-contentitem) collection | Content items shipped by the latest version of the package. Read-only. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.security.contentManagement.contentPackage",
  "id": "String (identifier)",
  "contentProductId": "String",
  "kind": "String",
  "version": "String",
  "displayName": "String",
  "description": "String",
  "descriptionHtml": "String",
  "icon": "String",
  "publisherDisplayName": "String",
  "source": {
    "@odata.type": "microsoft.graph.security.contentManagement.contentPackageSource"
  },
  "author": {
    "@odata.type": "microsoft.graph.security.contentManagement.contentAuthor"
  },
  "support": {
    "@odata.type": "microsoft.graph.security.contentManagement.contentSupport"
  },
  "providers": [
    "String"
  ],
  "categories": {
    "@odata.type": "microsoft.graph.security.contentManagement.contentCategories"
  },
  "firstPublishDateTime": "String (timestamp)",
  "lastPublishDateTime": "String (timestamp)",
  "isDeprecated": "Boolean",
  "dependencies": {
    "@odata.type": "microsoft.graph.Json"
  },
  "migratedToPackageId": "String",
  "isFeatured": "Boolean",
  "isPreview": "Boolean",
  "isNew": "Boolean",
  "mainTemplate": {
    "@odata.type": "microsoft.graph.Json"
  }
}
```