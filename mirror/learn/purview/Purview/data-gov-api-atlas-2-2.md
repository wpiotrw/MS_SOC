---
layout: Conceptual
title: Use APIs available with Atlas 2.2. with Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-api-atlas-2-2
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2025-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: This tutorial describes the APIs available with the Atlas 2.2 upgrade for use with Microsoft Purview Data Map.
ms.custom: sfi-image-nochange
locale: en-us
document_id: 91ac044d-e34c-23d5-9b03-ff99472c0a61
document_version_independent_id: 91ac044d-e34c-23d5-9b03-ff99472c0a61
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-api-atlas-2-2.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-api-atlas-2-2
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-api-atlas-2-2.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 5a194af6-adde-3aab-2ece-63f65fedb674
---

# Use APIs available with Atlas 2.2. with Data Map | Microsoft Learn

In this tutorial, learn to programmatically interact with new Atlas 2.2 APIs with Microsoft Purview Data Map.

## Prerequisites

- If you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.
- You must have an existing Microsoft Purview account. If you don't have a catalog, see the [quickstart for creating a Microsoft Purview account](create-microsoft-purview-portal).
- To establish a bearer token and to call any APIs, see [the documentation about how to authenticate APIs for Microsoft Purview](data-gov-api-rest-data-plane).

## Business metadata APIs

Business metadata is a template that contains custom attributes (key values). You can create these attributes globally and then apply them across multiple typedefs.

### Atlas endpoint

For all the requests, you'll need the Atlas endpoint for your Microsoft Purview account.

1. Find your Microsoft Purview account in the [Azure portal](https://portal.azure.com)
2. Select the **Properties** page on the left side menu
3. Copy the **Atlas endpoint** value

![Screenshot of the properties page for Microsoft Purview with the Atlas endpoint box highlighted.](media/tutorial-atlas-2-2-apis/endpoint.png)

### Create business metadata with attributes

You can send a `POST` request to the following endpoint:

```
POST {{endpoint}}/api/atlas/v2/types/typedefs
```

Tip

The **applicableEntityTypes** property tells which data types the metadata will be applied to.

Sample JSON:

```json
   {
  "businessMetadataDefs": [
    {
      "category": "BUSINESS_METADATA",
      "createdBy": "admin",
      "updatedBy": "admin",
      "version": 1,
      "typeVersion": "1.1",
      "name": "<Name of Business Metadata>",
      "description": "",
      "attributeDefs": [
        {
          "name": "<Attribute Name>",
          "typeName": "string",
          "isOptional": true,
          "cardinality": "SINGLE",
          "isUnique": false,
          "isIndexable": true,
          "options": {
            "maxStrLength": "50",
            "applicableEntityTypes": "[\"Referenceable\"]"
          }          
        }
      ]
    }
  ]
}
```

### Add or update an attribute to existing business metadata

You can send a `PUT` request to the following endpoint:

```
PUT {{endpoint}}/api/atlas/v2/types/typedefs
```

Sample JSON:

```json
   {
  "businessMetadataDefs": [
    {
      "category": "BUSINESS_METADATA",
      "createdBy": "admin",
      "updatedBy": "admin",
      "version": 1,
      "typeVersion": "1.1",
      "name": "<Name of Business Metadata>",
      "description": "",
      "attributeDefs": [
        {
          "name": "<Attribute Name>",
          "typeName": "string",
          "isOptional": true,
          "cardinality": "SINGLE",
          "isUnique": false,
          "isIndexable": true,
          "options": {
            "maxStrLength": "500",
            "applicableEntityTypes": "[\"Referenceable\"]"
          }          
        },
        {
          "name": "<Attribute Name 2>",
          "typeName": "int",
          "isOptional": true,
          "cardinality": "SINGLE",
          "isUnique": false,
          "isIndexable": true,
          "options": {
            "applicableEntityTypes": "[\"Referenceable\"]"
          }          
        }
      ]
    }
  ]
}
```

### Get a business metadata definition

You can send a `GET` request to the following endpoint:

```
GET {endpoint}}/api/atlas/v2/types/typedef/name/{{Business Metadata Name}}
```

### Set a business metadata attribute to an entity

You can send a `POST` request to the following endpoint:

```
POST {{endpoint}}/api/atlas/v2/entity/guid/{{GUID}}/businessmetadata?isOverwrite=true
```

Sample JSON:

```json
{
  "myBizMetaData1": {
        "bizAttr1": "I am myBizMetaData1.bizAttr1",
        "bizAttr2": 123,
  }
 }
```

### Delete a business metadata attribute from an entity

You can send a `DELETE` request to the following endpoint:

```
'DELETE' {{endpoint}}/api/atlas/v2/entity/guid/{{GUID}}/businessmetadata?isOverwrite=true
```

Sample JSON:

```json
{
  "myBizMetaData1": {
    "bizAttr1": ""    
  }
}
```

### Delete a business metadata type definition

Note

You can only delete business metadata type definition if it has no references, i.e., if it has not been assigned to any assets in the catalog.

You can send a `DELETE` request to the following endpoint:

```
DELETE {{endpoint}}/api/atlas/v2/types/typedef/name/{{Business Metadata Name}}
```

## Custom attribute APIs

Custom attributes are key/value pairs that can be directly added to an Atlas entity.

### Set a custom attribute to an entity

You can send a `POST` request to the following endpoint:

```
POST {{endpoint}}/api/atlas/v2/entity
```

Sample JSON:

```json
{
    "entity": {
        "typeName": "azure_datalake_gen2_path",
        "attributes": {
           
            "qualifiedName": "<FQN of the asset>",
            "name": "data6.csv"
        },
        "guid": "3ffb28ff-138f-419e-84ba-348b0165e9e0",
        "customAttributes": {
            "custAttr1": "attr1",
            "custAttr2": "attr2"
        }
    }
}
```

## Label APIs

Labels are free text tags that can be applied to any Atlas entity.

### Set labels to an entity

You can send a `POST` request to the following endpoint:

```
POST {{endpoint}}/api/atlas/v2/entity/guid/{{GUID}}/labels
```

Sample JSON:

```json
[
  "label1",
  "label2"
]
```

### Delete labels to an entity

You can send a `DELETE` request to the following endpoint:

```
DELETE {{endpoint}}/api/atlas/v2/entity/guid/{{GUID}}/labels
```

Sample JSON:

```json
[
  "label2"
]
```