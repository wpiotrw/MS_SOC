---
layout: Conceptual
monikers:
- graph-rest-beta
defaultMoniker: graph-rest-beta
versioningType: Ranged
title: externalSapAcConnectionInfo resource type - Microsoft Graph beta | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/externalsapacconnectioninfo?view=graph-rest-beta
config_moniker_range: graph-rest-beta
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
description: Represents connection information for connecting to SAP Access Control (AC) systems from Microsoft Entra Entitlement Management.
ms.date: 2026-07-13T00:00:00.0000000Z
ms.localizationpriority: medium
doc_type: resourcePageType
locale: en-us
document_id: b7223ca8-a3cc-2f1f-5c2e-019373bf4032
document_version_independent_id: 6a06a558-b508-e8f2-533b-44e4b200f037
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/beta/resources/externalsapacconnectioninfo.md
default_moniker: graph-rest-beta
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/externalsapacconnectioninfo
moniker_range_name: e91460ef4e2d3d4ee85e2756c1c65925
monikers:
- graph-rest-beta
item_type: Content
source_path: api-reference/beta/resources/externalsapacconnectioninfo.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://authoring-docs-microsoft.poolparty.biz/devrel/f488294d-f483-456e-94e3-755f933b811b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://authoring-docs-microsoft.poolparty.biz/devrel/02662057-0b9b-40f4-a3c7-537125b6d283
platformId: 7be89a22-a69f-d53f-7ab9-c7ca29cc10d0
---

# externalSapAcConnectionInfo resource type - Microsoft Graph beta | Microsoft Learn

Namespace: microsoft.graph

Important

APIs under the `/beta` version in Microsoft Graph are subject to change. Use of these APIs in production applications is not supported. To determine whether an API is available in v1.0, use the **Version** selector.

Represents connection information for connecting to SAP Access Control (AC) systems from Microsoft Entra Entitlement Management. This resource contains the configuration details required to establish a secure connection between an Entitlement Management [accessPackageResource](accesspackageresource)'s **externalOriginResourceConnector** and an SAP AC system, including the target system identity and Azure Key Vault references for credential storage. Used when connectorType in [externalOriginResourceConnector](externaloriginresourceconnector) is `sapAc`.

Inherits from [connectionInfo](connectioninfo).

## Properties

| Property | Type | Description |
| --- | --- | --- |
| authenticationInfo | [authenticationInfo](authenticationinfo) | The authentication configuration used to connect to the SAP AC system. |
| keyVaultName | String | The name of the Azure Key Vault that stores the credentials used for authentication. |
| resourceGroup | String | The Azure resource group that contains the Key Vault. |
| subscriptionId | String | The Azure subscription ID that contains the Key Vault. |
| systemId | String | The identifier of the target SAP AC system. |
| url | String | The endpoint that is used by Entitlement Management to communicate with the SAP AC system. Inherited from [connectionInfo](connectioninfo). |
| userIdentifier | String | The user identifier used to connect to the SAP AC system. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.externalSapAcConnectionInfo",
  "url": "String",
  "subscriptionId": "String",
  "resourceGroup": "String",
  "keyVaultName": "String",
  "systemId": "String",
  "userIdentifier": "String",
  "authenticationInfo": {
    "@odata.type": "microsoft.graph.authenticationInfo"
  }
}
```