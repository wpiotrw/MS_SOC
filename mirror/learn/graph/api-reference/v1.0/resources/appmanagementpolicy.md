---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: appManagementPolicy resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/appmanagementpolicy?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: aricrowe57
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-sign-in
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents an application auth method policy for enforcing app management restrictions on specific applications or service principals.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2024-09-13T00:00:00.0000000Z
locale: en-us
document_id: f6842767-27ea-77b8-ccea-459bb46de304
document_version_independent_id: 02a40f56-2edd-c1af-9dca-e31ae78e9928
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/appmanagementpolicy.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/appmanagementpolicy
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/appmanagementpolicy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: fa535a43-937e-28bc-7168-813fe7fb9bc1
---

# appManagementPolicy resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Restrictions on app management operations for specific applications and service principals. If this resource is not configured for an application or service principal, the restrictions default to the settings in the [tenantAppManagementPolicy](tenantappmanagementpolicy) object.

To learn more about how to use app management policy, see [Microsoft Entra application authentication methods API overview](applicationauthenticationmethodpolicy).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../appmanagementpolicy-list) | [appManagementPolicy](appmanagementpolicy) | Return a list of app management policies created for applications and service principals along with their properties. |
| [Create](../appmanagementpolicy-post) | [appManagementPolicy](appmanagementpolicy) | Create an app management policy that can be assigned to an application or service principal object. |
| [Get](../appmanagementpolicy-get) | [appManagementPolicy](appmanagementpolicy) | Get a single app management policy object. |
| [Update](../appmanagementpolicy-update) | None | Update an app management policy. |
| [Delete](../appmanagementpolicy-delete) | None | Delete an app management policy from the collection of policies in appManagementPolicies. |
| [List applies to](../appmanagementpolicy-list-appliesto) | [appManagementPolicy](appmanagementpolicy) | Return a list of applications and service principals to which the policy is applied. |
| [Create applies to](../appmanagementpolicy-post-appliesto) | None | Assign an appManagementPolicy policy object to an application or service principal object. |
| [Delete applies to](../appmanagementpolicy-delete-appliesto) | None | Remove an appManagementPolicy policy object from an application or service principal object. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| displayName | String | The display name of the policy. Inherited from [policyBase](policybase). |
| description | String | The description of the policy. Inherited from [policyBase](policybase). |
| id | String | The unique identifier for the policy. |
| isEnabled | Boolean | Denotes whether the policy is enabled. |
| restrictions | [appManagementConfiguration](appmanagementconfiguration) | Restrictions that apply to an application or service principal object. |

## Relationships

| Relationship | Type | Description |
| --- | --- | --- |
| appliesTo | [directoryObject](directoryobject) | Collection of applications and service principals to which the policy is applied. |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#policies/appManagementPolicies",
  "description": "String",
  "displayName": "String",
  "id": "String (identifier)",
  "isEnabled": "Boolean",
  "restrictions": {"@odata.type": "microsoft.graph.appManagementConfiguration"}
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/appmanagementpolicy?view=graph-rest-beta&accept=text/markdown)
