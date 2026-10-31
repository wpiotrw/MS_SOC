---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: onPasswordUpdateListener resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/onpasswordupdatelistener?view=graph-rest-beta
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
description: Represents an event listener for the onPasswordUpdate authentication event, used to notify external systems after password updates.
ms.date: 2026-10-07T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: 2ecb90c6-50af-ecf9-76e0-4ae5a7476e02
document_version_independent_id: 80574261-cb7f-3bcf-86ed-33e60384b619
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/onpasswordupdatelistener.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/onpasswordupdatelistener
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/onpasswordupdatelistener.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: a8af8800-d97c-13b8-a2b0-6307cd0b548d
---

# onPasswordUpdateListener resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents an [authentication event listener](authenticationeventlistener) that triggers after a user completes a self-service password reset (SSPR). This listener allows organizations to notify an external system of the password update for selected applications.

When a password update occurs, the listener evaluates its configured conditions to determine whether to invoke the associated handler.

Inherits from [authenticationEventListener](authenticationeventlistener).

## Methods

None.

For the list of API operations for managing this resource type, see the [authenticationEventListener](authenticationeventlistener) resource type.

## Properties

| Property | Type | Description |
| --- | --- | --- |
| authenticationEventsFlowId | String | Identifier of the authentication events flow. Inherited from [authenticationEventListener](authenticationeventlistener). |
| conditions | [authenticationConditions](authenticationconditions) | Conditions that determine when this listener is active, such as which applications trigger the event. Inherited from [authenticationEventListener](authenticationeventlistener). |
| displayName | String | Display name for the authentication event listener. Inherited from [authenticationEventListener](authenticationeventlistener). |
| handler | [onPasswordUpdateHandler](onpasswordupdatehandler) | Configuration for the handler to invoke when this listener is triggered. This is typically an [onPasswordUpdateCustomExtensionHandler](onpasswordupdatecustomextensionhandler). |
| id | String | Unique identifier for the authentication event listener. Inherited from [authenticationEventListener](authenticationeventlistener). |
| priority | Int32 | Priority of this listener relative to other listeners for the same event. Lower values indicate higher priority. Inherited from [authenticationEventListener](authenticationeventlistener). |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.onPasswordUpdateListener",
  "id": "String (identifier)",
  "displayName": "String",
  "priority": "Integer",
  "conditions": {
    "@odata.type": "microsoft.graph.authenticationConditions"
  },
  "authenticationEventsFlowId": "String",
  "handler": {
    "@odata.type": "microsoft.graph.onPasswordUpdateHandler"
  }
}
```