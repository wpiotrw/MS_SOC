---
layout: Conceptual
title: Type definitions and how to create custom types in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-api-custom-types
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2024-06-06T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Understand what type definitions are, how to create custom type definitions, and how to initialize assets of those custom types in Microsoft Purview.
locale: en-us
document_id: ea757195-85f7-9380-c8b2-6d8dfea5afcb
document_version_independent_id: ea757195-85f7-9380-c8b2-6d8dfea5afcb
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-api-custom-types.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-api-custom-types
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-api-custom-types.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 6b3a77b8-5bb8-4bf8-3764-c940b1f4307a
---

# Type definitions and how to create custom types in Microsoft Purview | Microsoft Learn

This tutorial will explain what type definitions are, how to create custom types, and how to initialize assets of custom types in Microsoft Purview.

In this tutorial, you'll learn:

- How Microsoft Purview uses the *type system* from [*Apache Atlas*](https://atlas.apache.org/#/)
- How to create a new custom type
- How to create relationships between custom types
- How to initialize new entities of custom types

## Prerequisites

For this tutorial you'll need:

- An Azure account with an active subscription. If you don't have one, you can [create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active Microsoft Purview (formerly Azure Purview) account. If you don't have one, see the [guide for getting started with Microsoft Purview for free](data-governance-free-version).
- A bearer token to your Microsoft Purview account. To establish a bearer token and to call any APIs, see [the documentation about how to authenticate APIs for Microsoft Purview](data-gov-api-rest-data-plane).
- Your Apache Atlas endpoint of your Microsoft Purview account. It will be one of these two endpoints, depending on your environment:

    - If you're using the [classic Microsoft Purview governance portal](use-microsoft-purview-governance-portal): `https://{{ACCOUNTNAME}}.purview.azure.com/catalog`
    - If you're using the [new Microsoft Purview portal](/en-us/purview/portal): `https://api.purview-service.microsoft.com/catalog`

Note

Before moving to the hands-on part of the tutorial, the first four sections will explain what a System Type is and how it is used in Microsoft Purview. All the REST API calls described further will use the **bearer token** and the **endpoint** which are described in the prerequisites.

To skip directly to the steps, use these links:

- Create custom type definitions
- Initialize assets of custom types

## What are *asset* and *type* in Microsoft Purview?

An *asset* is a metadata element that describes a digital or physical resource. The digital or physical resources that are expected to be cataloged as assets include:

- Data sources such as databases, files, and data feed.
- Analytical models and processes.
- Business policies and terms.
- Infrastructure like the server.

Microsoft Purview provides users a flexible *type system* to expand the definition of the asset to include new kinds of resources as they become relevant. Microsoft Purview relies on the [Type System](https://atlas.apache.org/2.0.0/TypeSystem.html) from Apache Atlas. All metadata objects (assets) managed by Microsoft Purview are modeled using type definitions. Understanding the Type System is fundamental to create new custom types in Microsoft Purview.

Essentially, a *Type* can be seen as a *Class* from Object Oriented Programming (OOP):

- It defines the properties that represent that type.
- Each type is uniquely identified by its *name*.
- A *type* can inherit from a *supertType*. This is an equivalent concept as inheritance from OOP. A type that extends a superType will inherit the attributes of the superType.

You can see all type definitions in your Microsoft Purview account by sending a `GET` request to the [All Type Definitions](/en-us/rest/api/purview/catalogdataplane/types/get-all-type-definitions) endpoint:

```http
GET https://{{ENDPOINT}}/catalog/api/atlas/v2/types/typedefs
```

Apache Atlas has few predefined system types that are commonly used as supertypes.

For example:

- **Referenceable**: This type represents all entities that can be searched for using a unique attribute called *qualifiedName*.
- **Asset**: This type extends from Referenceable and has other attributes such as: *name*, *description* and *owner*.
- **DataSet**: This type extends Referenceable and Asset. Conceptually, it can be used to represent a type that stores data. Types that extend DataSet can be expected to have a Schema. For example, a SQL table.
- **Lineage**: Lineage information helps one understand the origin of data and the transformations it may have gone through before arriving in a file or table. Lineage is calculated through *DataSet* and *Process*: DataSets (input of process) impact some other DataSets (output of process) through Process.

[![Diagram showing the relationships between system types.](media/tutorial-custom-types/base-model-diagram.png)](media/tutorial-custom-types/base-model-diagram.png#lightbox)

## Example of a *Type* definition

To better understand the Type system, let's look at an example and see how an **Azure SQL Table** is defined.

You can get the complete type definition by sending a `GET` request to the Type Definition [endpoint](/en-us/rest/api/purview/catalogdataplane/types/get-type-definition-by-name):

```http
GET https://{{ENDPOINT}}/catalog/api/atlas/v2/types/typedef/name/{name}
```

Tip

The **{name}** property tells which definition you are interested in. In this case, you should use **azure\_sql\_table**.

Below you can see a simplified JSON result:

```json
{
  "category": "ENTITY",
  "guid": "7d92a449-f7e8-812f-5fc8-ca6127ba90bd",
  "name": "azure_sql_table",
  "description": "azure_sql_table",
  "typeVersion": "1.0",
  "serviceType": "Azure SQL Database",
  "options": {
    "schemaElementsAttribute": "columns",
  },
  "attributeDefs": [
    { "name": "principalId", ...},
    { "name": "objectType", ...},
    { "name": "createTime", ...},
    { "name": "modifiedTime", ... }
  ],
  "superTypes": [
    "DataSet",
    "Purview_Table",
    "Table"
  ],
  "subTypes": [],
  "relationshipAttributeDefs": [
    {
      "name": "dbSchema",
      "typeName": "azure_sql_schema",
      "isOptional": false,
      "cardinality": "SINGLE",
      "relationshipTypeName": "azure_sql_schema_tables",
    },
    {
      "name": "columns",
      "typeName": "array<azure_sql_column>",
      "isOptional": true,
      "cardinality": "SET",
      "relationshipTypeName": "azure_sql_table_columns",
    },
  ]
}
```

Based on the JSON type definition, let's look at some properties:

- **Category** field describes in what category your type is. The list of categories supported by Apache Atlas can be found [here](https://atlas.apache.org/api/v2/json_TypeCategory.html).
- **ServiceType** field is useful when browsing assets *by source type* in Microsoft Purview. The *service type* will be an entry point to find all assets that belong to the same *service type* - as defined on their type definition. In the below screenshot of Purview UI, the user limits the result to be the entities specified with *Azure SQL Database* in **serviceType**:

    ![Screenshot of the portal showing the path from Unified Catalog to Browse to By source type and the asset highlighted.](media/tutorial-custom-types/browse-assets.png)

    Note

    **Azure SQL Database** is defined with the same *serviceType* as **Azure SQL Table**.
- **SuperTypes** describes the *"parent"* types you want to "*inherit*" from.
- **schemaElementsAttributes** from **options** influences what appears in the **Schema** tab of your asset in Microsoft Purview.

    Below you can see an example of how the **Schema** tab looks like for an asset of type Azure SQL Table:

    [![Screenshot of the schema tab for an Azure SQL Table asset.](media/tutorial-custom-types/schema-tab.png)](media/tutorial-custom-types/schema-tab.png#lightbox)
- **relationshipAttributeDefs** are calculated through the relationship type definitions. In our JSON, we can see that **schemaElementsAttributes** points to the relationship attribute called **columns** - which is one of elements from **relationshipAttributeDefs** array, as shown below:

    ```json
    ...
    "relationshipAttributeDefs": [
         ...
         {
           "name": "columns",
           "typeName": "array<azure_sql_column>",
           "isOptional": true,
           "cardinality": "SET",
           "relationshipTypeName": "azure_sql_table_columns",
         },
       ]
    ```

    Each relationship has its own definition. The name of the definition is found in **relationshipTypeName** attribute. In this case, it's *azure\_sql\_table\_columns*.

    - The **cardinality** of this relationship attribute is set to \*SET, which suggests that it holds a list of related assets.
    - The related asset is of type *azure\_sql\_column*, as visible in the *typeName* attribute.

    In other words, the *columns* relationship attribute relates the Azure SQL Table to a list of Azure SQL Columns that show up in the Schema tab.

## Example of a *relationship Type definition*

Each relationship consists of two ends, called *endDef1* and *endDef2*.

In the previous example, *azure\_sql\_table\_columns* was the name of the relationship that characterizes a table (endDef1) and its columns (endDef2).

For the full definition, you can do make a `GET` request to the following [endpoint](/en-us/rest/api/purview/catalogdataplane/types/get-type-definition-by-name) using *azure\_sql\_table\_columns* as the name:

```http
GET https://{{ENDPOINT}}/catalog/api/atlas/v2/types/typedef/name/azure_sql_table_columns
```

Below you can see a simplified JSON result:

```json
{
  "category": "RELATIONSHIP",
  "guid": "c80d0027-8f29-6855-6395-d243b37d8a93",
  "name": "azure_sql_table_columns",
  "description": "azure_sql_table_columns",
  "serviceType": "Azure SQL Database",
  "relationshipCategory": "COMPOSITION",
  "endDef1": {
    "type": "azure_sql_table",
    "name": "columns",
    "isContainer": true,
    "cardinality": "SET",
  },
  "endDef2": {
    "type": "azure_sql_column",
    "name": "table",
    "isContainer": false,
    "cardinality": "SINGLE",
  }
}
```

- **name** is the name of the relationship definition. The value, in this case *azure\_sql\_table\_columns* is used in the *relationshipTypeName* attribute of the entity that has this relationship, as you can see it referenced in the json.
- **relationshipCategory** is the category of the relationship and it can be either COMPOSITION, AGGREGATION or ASSOCIATION as described [here](https://atlas.apache.org/api/v2/json_RelationshipCategory.html).
- **enDef1** is the first end of the definition and contains the attributes:

    - **type** is the type of the entity that this relationship expects as end1.
    - **name** is the attribute that will appear on this entity's relationship attribute.
    - **cardinality** is either SINGLE, SET or LIST.
    - **isContainer** is a boolean and applies to containment relationship category. When set to true in one end, it indicates that this end is the container of the other end. Therefore:

        - Only the *Composition* or *Aggregation* category relationships can and should have in one end *isContainer* set to true.
        - *Association* category relationship shouldn't have *isContainer* property set to true in any end.
- **endDef2** is the second end of the definition and describes, similarly to endDef1, the properties of the second part of the relationship.

## Schema tab

### What is *Schema* in Microsoft Purview?

Schema is an important concept that reflects how data is stored and organized in the data store. It reflects the structure of the data and the data restrictions of the elements that construct the structure.

Elements on the same schema can be classified differently (due to their content). Also, different transformation (lineage) can happen to only a subset of elements. Due to these aspects, Purview can model schema and schema elements **as entities**, hence schema is usually a relationship attribute to the data asset entity. Examples of schema elements are: **columns** of a table, **json properties** of json schema, **xml elements** of xml schema etc.

There are two types of schemas:

- **Intrinsic Schema** - Some systems are intrinsic to schema. For example, when you create a SQL Table, the system requires you to define the columns that construct the table; in this sense, schema of a table is reflected by its columns.

    For data store with predefined schema, Purview uses the corresponding relationship between the data asset and the schema elements to reflect the schema. This relationship attribute is specified by the keyword **schemaElementsAttribute** in **options** property of the entity type definition.
- **Non Intrinsic Schema** - Some systems don't enforce such schema restrictions, but users can use it to store structural data by applying some schema protocols to the data. For example, Azure Blobs store binary data and don't care about the data in the binary stream. Therefore, it's unaware of any schema, but the user can serialize their data with schema protocols like json before storing it in the blob. In this sense, schema is maintained by some extra protocols and corresponding validation enforced by the user.

    For data store without inherent schema, schema model is independent of this data store. For such cases, Purview defines an interface for schema and a relationship between DataSet and schema, called **dataset\_attached\_schemas** - this extends any entity type that inherits from DataSet to have an **attachedSchema** relationship attribute to link to their schema representation.

### Example of *Schema tab*

The Azure SQL Table example from above has an intrinsic schema. The information that shows up in the Schema tab of the Azure SQL Table comes from the Azure SQL Column themselves.

Selecting one column item, we would see the following:

[![Screenshot of the addressID column page with the properties tab open and the data type highlighted.](media/tutorial-custom-types/azure-sql-column.png)](media/tutorial-custom-types/azure-sql-column.png#lightbox)

The question is, how did Microsoft Purview select the *data\_tye* property from the column and showed it in the Schema tab of the table?

[![Screenshot of the Azure SQL Table page with the schema page open.](media/tutorial-custom-types/schema-tab-data-type.png)](media/tutorial-custom-types/schema-tab-data-type.png#lightbox)

You can get the type definition of an Azure SQL Column by making a `GET` request to the [endpoint](/en-us/rest/api/purview/catalogdataplane/types/get-type-definition-by-name):

```http
GET https://{{ENDPOINT}}/catalog/api/atlas/v2/types/typedef/name/{name}
```

Note

{name} in this case is: azure\_sql\_column

Here's a simplified JSON result:

```json
{
  "category": "ENTITY",
  "guid": "58034a18-fc2c-df30-e474-75803c3a8957",
  "name": "azure_sql_column",
  "description": "azure_sql_column",
  "serviceType": "Azure SQL Database",
  "options": {
    "schemaAttributes": "[\"data_type\"]"
  },
  "attributeDefs": 
  [
    {
      "name": "data_type",
      "typeName": "string",
      "isOptional": false,
      "cardinality": "SINGLE",
      "valuesMinCount": 1,
      "valuesMaxCount": 1,
      "isUnique": false,
      "isIndexable": false,
      "includeInNotification": false
    }, 
  ...
  ]
  ...
}
```

Note

serviceType is Azure SQL Database, the same as for the table

- *schemaAttributes* is set to **data\_type**, which is one of the attributes of this type.

Azure SQL Table used *schemaElementAttribute* to point to a relationship consisting of a list of Azure SQL Columns. The type definition of a column has *schemaAttributes* defined.

In this way, the Schema tab in the table displays the attribute(s) listed in the *schemaAttributes* of the related assets.

## Create custom type definitions

### Why?

First, why would someone like to create a custom type definition?

There can be cases where there's no built-in type that corresponds to the structure of the metadata you want to import in Microsoft Purview.

In such a case, a new type definition has to be defined.

Note

The usage of built-in types should be favored over the creation of custom types, whenever possible.

Now that we gained an understanding of type definitions in general, let us create custom type definitions.

### Scenario

In this tutorial, we would like to model a 1:n relationship between two types, called *custom\_type\_parent* and *custom\_type\_child*.

A *custom\_type\_child* should reference one parent, whereas a *custom\_type\_parent* can reference a list of children.

They should be linked together through a 1:n relationship.

Tip

[Here](https://github.com/wjohnson/purview-ingestor-scenarios) you can find few tips when creating a new custom type.

### Create definitions

1. Create the *custom\_type\_parent* type definition by making a `POST` request to one of the two following endpoints:

[Classic Microsoft Purview governance portal](use-microsoft-purview-governance-portal):

```http
POST https://{{ENDPOINT}}.purview.azure.com/catalog/api/atlas/v2/types/typedefs
```

New Microsoft Purview portal:

```http
POST https://api.purview-service.microsoft.com/catalog/api/atlas/v2/types/typedefs
```

With the body:

```json
 {
    "entityDefs": 
    [
        {
            "category": "ENTITY",
            "version": 1,
            "name": "custom_type_parent",
            "description": "Sample custom type of a parent object",
            "typeVersion": "1.0",
            "serviceType": "Sample-Custom-Types",
            "superTypes": [
                "DataSet"
            ],
            "subTypes": [],
            "options":{
                "schemaElementsAttribute": "columns"
            }
        }
    ]
 }
```

1. Create the *custom\_type\_child* type definition by making a `POST` request to one of the two following endpoints:

[Classic Microsoft Purview governance portal](use-microsoft-purview-governance-portal):

```http
POST https://{{ENDPOINT}}.purview.azure.com/catalog/api/atlas/v2/types/typedefs
```

New Microsoft Purview portal:

```http
POST https://api.purview-service.microsoft.com/catalog/api/atlas/v2/types/typedefs
```

With the body:

```json
 {
    "entityDefs": 
    [
        {
            "category": "ENTITY",
            "version": 1,
            "name": "custom_type_child",
            "description": "Sample custom type of a CHILD object",
            "typeVersion": "1.0",
            "serviceType": "Sample-Custom-Types",
            "superTypes": [
                "DataSet"
            ],
            "subTypes": [],
            "options":{
               "schemaAttributes": "data_type"
            }
        }
    ]
 }
```

1. Create a custom type relationship definition by making a `POST` request to one of the two following endpoints:

[Classic Microsoft Purview governance portal](use-microsoft-purview-governance-portal):

```http
POST https://{{ENDPOINT}}.purview.azure.com/catalog/api/atlas/v2/types/typedefs
```

New Microsoft Purview portal:

```http
POST https://api.purview-service.microsoft.com/catalog/api/atlas/v2/types/typedefs
```

With the body:

```json
{
    "relationshipDefs": [
        {
            "category": "RELATIONSHIP",
            "endDef1" : {
                "cardinality" : "SET",
                "isContainer" : true,
                "name" : "Children",
                "type" : "custom_type_parent"
            },
            "endDef2" : {
                "cardinality" : "SINGLE",
                "isContainer" : false,
                "name" : "Parent",
                "type" : "custom_type_child"
            },
            "relationshipCategory" : "COMPOSITION",
            "serviceType": "Sample-Custom-Types",
            "name": "custom_parent_child_relationship"
        }
    ]
}
```

## Initialize assets of custom types

1. Initialize a new asset of type *custom\_type\_parent* by making a `POST` request to one of the two following endpoints:

[Classic Microsoft Purview governance portal](use-microsoft-purview-governance-portal):

```http
POST https://{{ENDPOINT}}.purview.azure.com/catalog/api/atlas/v2/entity
```

New Microsoft Purview portal:

```http
POST https://api.purview-service.microsoft.com/catalog/api/atlas/v2/entity
```

With the body:

```json

{
    "entity": {
        "typeName":"custom_type_parent",
        "status": "ACTIVE",
        "version": 1,
         "attributes":{
            "name": "First_parent_object",
            "description": "This is the first asset of type custom_type_parent",
            "qualifiedName": "custom//custom_type_parent:First_parent_object"
         }

    }
}
```

Save the *guid* as you'll need it later.

1. Initialize a new asset of type *custom\_type\_child* by making a `POST` request to one of the two following endpoints:

[Classic Microsoft Purview governance portal](use-microsoft-purview-governance-portal):

```http
POST https://{{ENDPOINT}}.purview.azure.com/catalog/api/atlas/v2/entity
```

New Microsoft Purview portal:

```http
POST https://api.purview-service.microsoft.com/catalog/api/atlas/v2/entity
```

With the body:

```json
{
   "entity": {
       "typeName":"custom_type_child",
       "status": "ACTIVE",
       "version": 1,
       "attributes":{
           "name": "First_child_object",
           "description": "This is the first asset of type custom_type_child",
           "qualifiedName": "custom//custom_type_child:First_child_object"
        }
   }
}
```

Save the *guid* as you'll need it later.

1. Initialize a new relationship of type *custom\_parent\_child\_relationship* by making a `POST` request to one of the two following endpoints:

[Classic Microsoft Purview governance portal](use-microsoft-purview-governance-portal):

```http
POST https://{{ENDPOINT}}.purview.azure.com/catalog/api/atlas/v2/relationship/
```

New Microsoft Purview portal:

```http
POST https://api.purview-service.microsoft.com/catalog/api/atlas/v2/relationship/
```

With the following body:

Note

The *guid* in end1 must be replaced with the the guid of the object created at step 6.1 The *guid* in end2 must be replaced with the guid of the object created at step 6.2

```json
{
   "typeName": "custom_parent_child_relationship",
   "end1": {
         "guid": "...",
       "typeName": "custom_type_parent"
   },
   "end2": {
       "guid": "...",
       "typeName": "custom_type_child"
   }
}
```

## View the assets in Microsoft Purview

1. Go to *Unified Catalog* in Microsoft Purview.
2. Select *Browse*.
3. Select *By source type*.
4. Select *Sample-Custom-Types*.

    ![Screenshot showing the path from the Unified Catalog to Browse assets with the filter narrowed to Sample-Custom-Types.](media/tutorial-custom-types/custom-types-objects.png)
5. Select the *First\_parent\_object*:

    ![Screenshot of the First_parent_object page.](media/tutorial-custom-types/first-parent-object.png)
6. Select the *Properties* tab:

    ![Screenshot of the properties tab with the related assets highlighted, showing one child asset.](media/tutorial-custom-types/children.png)
7. You can see the *First\_child\_object* being linked there.
8. Select the *First\_child\_object*:

    ![Screenshot of the First_child_object page, showing the overview tab.](media/tutorial-custom-types/first-child-object.png)
9. Select the *Properties* tab:

    ![Screenshot of the properties page, showing the related assets with a single parent asset.](media/tutorial-custom-types/parent.png)
10. You can see the Parent object being linked there.
11. Similarly, you can select the *Related* tab and will see the relationship between the two objects:

    ![Screenshot of the Related tab, showing the relationship between the child and parent.](media/tutorial-custom-types/relationship.png)
12. You can create multiple children by initializing a new child asset and inititialzing a relationship

    Note

    The *qualifiedName* is unique per asset, therefore, the second child should be called differently, such as: *custom//custom\_type\_child:Second\_child\_object*

    ![Screenshot of the First_parent_object, showing the two child assets highlighted.](media/tutorial-custom-types/two_children.png)

    Tip

    If you delete the *First\_parent\_object* you will notice that the children will also be removed, due to the *COMPOSITION* relationship that we chose in the definition.

## Limitations

There are several known limitations when working with custom types that will be enhanced in future, such as:

- Relationship tab looks different compared to built-in types
- Custom types have no icons
- Hierarchy isn't supported