---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: mailboxFolder resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/mailboxfolder?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: cparker-msft
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: outlook
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a folder in a user's mailbox, such as inbox, drafts, or other user created folders.
ms.date: 2026-08-06T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: f0442cac-550d-7ccd-2142-e04a1ed2056a
document_version_independent_id: 47644eac-9f27-83ae-af46-060371ef6829
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/mailboxfolder.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/mailboxfolder
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/mailboxfolder.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: cb511528-7fec-57ac-2de1-fbb39f57ef7e
---

# mailboxFolder resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents a folder in a user's mailbox, such as inbox, drafts, or other user created folders. Folders can contain various mailbox items like messages, events, contacts, other Outlook items, and child folders.

This resource supports [delta query](/en-us/graph/delta-query-overview) to track incremental additions, deletions, and updates, by providing a [delta](../mailboxfolder-delta) function. It also supports [single-value and multi-value extended properties](extended-properties-overview) for storing and accessing custom data that isn't already exposed in the Microsoft Graph API metadata.

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../mailbox-list-folders) | [mailboxFolder](mailboxfolder) collection | Get all the [mailboxFolder](mailboxfolder) objects in the specified mailbox, including any search folders. |
| [Create](../mailbox-post-folders) | [mailboxFolder](mailboxfolder) | Create a new [mailboxFolder](mailboxfolder) or child **mailboxFolder** in a user's mailbox. |
| [Get](../mailboxfolder-get) | [mailboxFolder](mailboxfolder) | Read the properties and relationships of a [mailboxFolder](mailboxfolder) object. |
| [Update](../mailboxfolder-update) | [mailboxFolder](mailboxfolder) | Update [mailboxFolder](mailboxfolder) properties such as the **displayName** within a mailbox. |
| [Delete](../mailbox-delete-folders) | None | Delete a [mailboxFolder](mailboxfolder) or a child **mailboxFolder** within a mailbox. |
| [Get delta](../mailboxfolder-delta) | [mailboxFolder](mailboxfolder) collection | Get a set of [mailboxFolder](mailboxfolder) objects that were added, deleted, or removed from the user's mailbox. |
| [List child mailbox folders](../mailboxfolder-list-childfolders) | [mailboxFolder](mailboxfolder) collection | Get the [mailboxFolder](mailboxfolder) collection under the specified **mailboxFolder** in a mailbox. |
| [List items in folder](../mailboxfolder-list-items) | [mailboxItem](mailboxitem) collection | Get the [mailboxItem](mailboxitem) collection within a specified [mailboxFolder](mailboxfolder) in a mailbox. |
| [Delete item in folder](../mailboxfolder-delete-items) | None | Delete a [mailboxItem](mailboxitem) from a [mailboxFolder](mailboxfolder) in a mailbox. |
| **Extended properties** |  |  |
| [Create single-value property](../singlevaluelegacyextendedproperty-post-singlevalueextendedproperties) | [mailboxFolder](mailboxfolder) | Create one or more single-value extended properties in a new or existing mailbox folder. |
| [Get single-value property](../singlevaluelegacyextendedproperty-get) | [mailboxFolder](mailboxfolder) | Get mailbox folders that contain a single-value extended property by using `$expand` or `$filter`. |
| [Create multi-value property](../multivaluelegacyextendedproperty-post-multivalueextendedproperties) | [mailboxFolder](mailboxfolder) | Create one or more multi-value extended properties in a new or existing mailbox folder. |
| [Get multi-value property](../multivaluelegacyextendedproperty-get) | [mailboxFolder](mailboxfolder) | Get a mailbox folder that contains a multi-value extended property by using `$expand`. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| childFolderCount | Int32 | The number of immediate child folders in the current folder. |
| displayName | String | The display name of the folder. |
| id | String | The unique identifier for the folder. |
| parentFolderId | String | The unique identifier for the parent folder of this folder. |
| totalItemCount | Int32 | The number of items in the folder. |
| type | String | Describes the folder class type. |
| wellKnownName | String | The locale-independent well-known name of the folder for folders created by Outlook, such as `inbox`, `sentitems`, `drafts`, `deleteditems`, or `archive`. For user-created folders, the value is `null`. Read-only. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| childFolders | [mailboxFolder](mailboxfolder) collection | The collection of child folders in this folder. |
| items | [mailboxItem](mailboxitem) collection | The collection of items in this folder. |
| multiValueExtendedProperties | [multiValueLegacyExtendedProperty](multivaluelegacyextendedproperty) collection | The collection of multi-value extended properties defined for the **mailboxFolder**. |
| singleValueExtendedProperties | [singleValueLegacyExtendedProperty](singlevaluelegacyextendedproperty) collection | The collection of single-value extended properties defined for the **mailboxFolder**. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.mailboxFolder",
  "displayName": "String",
  "childFolderCount": "Int32",
  "id": "String (identifier)",
  "parentFolderId": "String",
  "totalItemCount": "Int32",
  "wellKnownName": "String",
  "type": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/mailboxfolder?view=graph-rest-beta&accept=text/markdown)
