---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: onPasswordUpdateCustomExtension resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/onpasswordupdatecustomextension?view=graph-rest-beta
config_moniker_range: graph-rest-beta
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: junrlin
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-sign-in
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents a custom authentication extension for the onPasswordUpdate event, used to synchronize password updates to external systems.
ms.date: 2026-10-07T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 1687681a-fc3e-cdaa-b4fc-44683a518545
document_version_independent_id: 3ba5817d-066b-8426-3e2e-0800f0919ab2
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/onpasswordupdatecustomextension.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/onpasswordupdatecustomextension
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/onpasswordupdatecustomextension.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 69913d3e-fc1f-68ea-1017-04969112f760
---

# onPasswordUpdateCustomExtension resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents a [custom authentication extension](customauthenticationextension) for the **onPasswordUpdate** event. This extension allows organizations to notify an external system after a user completes a self-service password reset (SSPR), enabling the external system to synchronize the updated credential.

When a user completes SSPR, this extension calls a customer-provided API endpoint with an encrypted reference to the new password. The external system decrypts the reference and propagates the credential without changing the user-visible SSPR result.

The [onPasswordUpdateCustomExtensionHandler](onpasswordupdatecustomextensionhandler) references this resource through its **customExtension** relationship.

Inherits from [customAuthenticationExtension](customauthenticationextension).

## Methods

None.

For the list of API operations for managing this resource type, see the [customAuthenticationExtension](customauthenticationextension) resource type.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| authenticationConfiguration | [customExtensionAuthenticationConfiguration](customextensionauthenticationconfiguration) | Configuration for securing the API call to the external system. Inherited from [customCalloutExtension](customcalloutextension). |
| behaviorOnError | [customExtensionBehaviorOnError](customextensionbehavioronerror) | Error handling behavior when the external API fails or is unreachable. Inherited from [customAuthenticationExtension](customauthenticationextension). |
| clientConfiguration | [customExtensionClientConfiguration](customextensionclientconfiguration) | HTTP client configuration, including timeout and retry settings. Inherited from [customCalloutExtension](customcalloutextension). |
| description | String | Description of the custom authentication extension. Inherited from [customCalloutExtension](customcalloutextension). |
| displayName | String | Display name for the custom authentication extension. Inherited from [customCalloutExtension](customcalloutextension). |
| endpointConfiguration | [customExtensionEndpointConfiguration](customextensionendpointconfiguration) | HTTP endpoint configuration for the external API. Inherited from [customCalloutExtension](customcalloutextension). |
| id | String | Unique identifier for the custom authentication extension. Inherited from [entity](entity). |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.onPasswordUpdateCustomExtension",
  "id": "String (identifier)",
  "displayName": "String",
  "description": "String",
  "authenticationConfiguration": {
    "@odata.type": "microsoft.graph.customExtensionAuthenticationConfiguration"
  },
  "endpointConfiguration": {
    "@odata.type": "microsoft.graph.customExtensionEndpointConfiguration"
  },
  "clientConfiguration": {
    "@odata.type": "microsoft.graph.customExtensionClientConfiguration"
  },
  "behaviorOnError": {
    "@odata.type": "microsoft.graph.customExtensionBehaviorOnError"
  }
}
```