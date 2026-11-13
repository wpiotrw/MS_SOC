---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: unifiedRoleDefinition resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/unifiedroledefinition?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: DougKirschner
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-directory-management
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: A role definition is a collection of permissions in Microsoft Entra.
ms.localizationpriority: medium
ms.reviewer: msodsrbac
doc_type: resourcePageType
toc.title: Role definition
ms.date: 2026-10-08T00:00:00.0000000Z
locale: en-us
document_id: aa367574-a801-486d-8790-aee27158548b
document_version_independent_id: 82200805-4d04-4c29-fbc5-3e8b88a23f33
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/unifiedroledefinition.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/unifiedroledefinition
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/unifiedroledefinition.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 998d0fc2-0d4e-110b-e908-8b41f9a4ae52
---

# unifiedRoleDefinition resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

A role definition is a collection of permissions in Microsoft Entra listing the operations that can be performed and the resources against which they can performed.

## Methods

| Method | Return Type | Description |
| --- | --- | --- |
| [List](../rbacapplication-list-roledefinitions) | [unifiedRoleDefinition](unifiedroledefinition) collection | Read a list of unifiedRoleDefinition objects, and their properties. |
| [Get](../unifiedroledefinition-get) | [unifiedRoleDefinition](unifiedroledefinition) | Read the properties of an active or soft-deleted unifiedRoleDefinition object. |
| [Create](../rbacapplication-post-roledefinitions) | [unifiedRoleDefinition](unifiedroledefinition) | Create a unifiedRoleDefinition object. |
| [Update](../unifiedroledefinition-update) | [unifiedRoleDefinition](unifiedroledefinition) | Update a unifiedRoleDefinition object. |
| [Delete](../unifiedroledefinition-delete) | None | Delete an active unifiedRoleDefinition object or permanently delete a soft-deleted custom role definition. |
| [unifiedRoleDefinition: restore](../unifiedroledefinition-restore) | [unifiedRoleDefinition](unifiedroledefinition) | Restore a soft-deleted custom role definition. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| deletedDateTime | DateTimeOffset | The date and time when the custom role definition was deleted. The value is `null` for active and restored role definitions. Read-only. |
| description | String | The description for the unifiedRoleDefinition. Read-only when **isBuiltIn** is `true`. |
| displayName | String | The display name for the unifiedRoleDefinition. Read-only when **isBuiltIn** is `true`. Required. Supports $filter (`eq`, `in`). |
| id | String | The unique identifier for the role definition. Key, not nullable, Read-only. Inherited from [entity](entity). Supports $filter (`eq`, `in`). |
| isBuiltIn | Boolean | Flag indicating whether the role definition is part of the default set included in Microsoft Entra or a custom definition. Read-only. Supports $filter (`eq`, `in`). |
| isEnabled | Boolean | Flag indicating whether the role is enabled for assignment. If `false` the role is not available for assignment. Read-only when **isBuiltIn** is true. |
| isPrivileged | Boolean | Flag indicating whether the role is privileged. Microsoft Entra ID defines a role as privileged if it contains at least one sensitive resource action in the **allowedResourceActions** collection of **rolePermissions**. Applies only to actions in the `microsoft.directory` resource namespace. Nullable. A value of `null` indicates that the privileged classification is unavailable, not that the role is nonprivileged. Read-only. Supports `$filter` (`eq`). |
| resourceScopes | String collection | List of the scopes or permissions the role definition applies to. Currently only `/` is supported. Read-only when **isBuiltIn** is true. **DO NOT USE. This will be deprecated soon. Attach scope to role assignment.** |
| rolePermissions | [unifiedRolePermission](unifiedrolepermission) collection | List of permissions included in the role. Read-only when **isBuiltIn** is `true`. Required. |
| templateId | String | Custom template identifier that can be set when **isBuiltIn** is `false` but is read-only when **isBuiltIn** is `true`. This identifier is typically used if one needs an identifier to be the same across different directories. |
| version | String | Indicates version of the role definition. Read-only when **isBuiltIn** is `true`. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| inheritsPermissionsFrom | [unifiedRoleDefinition](unifiedroledefinition) collection | Read-only collection of role definitions that the given role definition inherits from. Only Microsoft Entra built-in roles (**isBuiltIn** is `true`) support this attribute. Supports `$expand`. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.unifiedRoleDefinition",
  "deletedDateTime": "String (timestamp)",
  "description": "String",
  "displayName": "String",
  "id": "String (identifier)",
  "isBuiltIn": "Boolean",
  "isEnabled": "Boolean",
  "isPrivileged": "Boolean",
  "resourceScopes": [
    "String"
  ],
  "rolePermissions": [
    {
      "@odata.type": "microsoft.graph.unifiedRolePermission"
    }
  ],
  "templateId": "String",
  "version": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/unifiedroledefinition?view=graph-rest-beta&accept=text/markdown)
