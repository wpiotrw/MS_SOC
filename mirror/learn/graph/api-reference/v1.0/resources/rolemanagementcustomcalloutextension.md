---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: roleManagementCustomCalloutExtension resource type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/rolemanagementcustomcalloutextension?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: amanswaika
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-id-governance
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a custom workflow extension for Privileged Identity Management role management operations.
ms.localizationpriority: medium
doc_type: resourcePageType
ms.date: 2026-10-19T00:00:00.0000000Z
locale: en-us
document_id: cccd3d30-bfbc-a403-2e4b-3202cc87551a
document_version_independent_id: 2978ea52-dd3d-155e-2b70-5bc2acd07675
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/rolemanagementcustomcalloutextension.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/rolemanagementcustomcalloutextension
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/rolemanagementcustomcalloutextension.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: e34ed17e-bbef-a899-c7cd-04d470c6c921
---

# roleManagementCustomCalloutExtension resource type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents a custom workflow extension for Privileged Identity Management (PIM) role management operations. Use this resource to integrate external approval, ticketing, compliance, audit, or notification systems into role assignment lifecycle events for Microsoft Entra roles, Azure resources, and groups.

Inherits from [customCalloutExtension](customcalloutextension).

## Methods

| Method | Return type | Description |
| --- | --- | --- |
| [List](../privilegedaccessroot-list-customextensions) | [roleManagementCustomCalloutExtension](rolemanagementcustomcalloutextension) collection | Get a list of PIM custom extensions. |
| [Create](../privilegedaccessroot-post-customextensions) | [roleManagementCustomCalloutExtension](rolemanagementcustomcalloutextension) | Create a PIM custom extension. |
| [Get](../rolemanagementcustomcalloutextension-get) | [roleManagementCustomCalloutExtension](rolemanagementcustomcalloutextension) | Retrieve a PIM custom extension. |
| [Update](../rolemanagementcustomcalloutextension-update) | [roleManagementCustomCalloutExtension](rolemanagementcustomcalloutextension) | Update a PIM custom extension. |
| [Delete](../rolemanagementcustomcalloutextension-delete) | None | Delete a PIM custom extension. |

## Properties

| Property | Type | Description |
| --- | --- | --- |
| authenticationConfiguration | [customExtensionAuthenticationConfiguration](customextensionauthenticationconfiguration) | The authentication configuration used to secure calls to the external app. Inherited from [customCalloutExtension](customcalloutextension). |
| clientConfiguration | [customExtensionClientConfiguration](customextensionclientconfiguration) | The HTTP connection settings for calls to the external app. Inherited from [customCalloutExtension](customcalloutextension). |
| customAttributes | String collection | The custom attribute names to include in the callout payload. |
| description | String | The description of the custom extension. Inherited from [customCalloutExtension](customcalloutextension). |
| displayName | String | The display name of the custom extension. Inherited from [customCalloutExtension](customcalloutextension). |
| endpointConfiguration | [customExtensionEndpointConfiguration](customextensionendpointconfiguration) | The configuration for the external endpoint that PIM calls. Inherited from [customCalloutExtension](customcalloutextension). |
| id | String | The unique identifier for the custom extension. Inherited from [entity](entity). |
| isEnabled | Boolean | When `true`, enables the custom extension. When `false`, disables it. Nullable. |
| resourceType | [customExtensionResourceType](enums#customextensionresourcetype-values) | The PIM provider to which the extension applies. The possible values are: `entraRoles`, `azureResources`, `entraGroups`, `unknownFutureValue`, `applicationAuthorization`, `appRoles`. Use the `Prefer: include-unknown-enum-members` request header to get the following values in this [evolvable enumeration](/en-us/graph/best-practices-concept#handling-future-members-in-evolvable-enumerations): `applicationAuthorization`, `appRoles`. Supports `$filter` (`eq`). |
| type | [customCalloutExtensionType](enums#customcalloutextensiontype-values) | The role assignment lifecycle stage at which PIM invokes the extension. The possible values are: `preApproval`, `postApproval`, `grant`, `revoke`, `unknownFutureValue`. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.roleManagementCustomCalloutExtension",
  "id": "String (identifier)",
  "authenticationConfiguration": {
    "@odata.type": "microsoft.graph.customExtensionAuthenticationConfiguration"
  },
  "clientConfiguration": {
    "@odata.type": "microsoft.graph.customExtensionClientConfiguration"
  },
  "customAttributes": ["String"],
  "description": "String",
  "displayName": "String",
  "endpointConfiguration": {
    "@odata.type": "microsoft.graph.customExtensionEndpointConfiguration"
  },
  "isEnabled": "Boolean",
  "resourceType": "String",
  "type": "String"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/rolemanagementcustomcalloutextension?view=graph-rest-beta&accept=text/markdown)
