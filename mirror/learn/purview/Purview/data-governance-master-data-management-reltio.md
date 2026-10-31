---
layout: Conceptual
title: Microsoft Purview and Reltio Master Data Management (MDM) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-master-data-management-reltio
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2024-09-14T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to deploy the Microsoft Purview and Reltio integration as a master data management (MDM) solution for your data estate governance.
ms.custom: sfi-image-nochange
locale: en-us
document_id: bb3b8a8f-6649-89e8-1b8b-fc655e4a4db3
document_version_independent_id: bb3b8a8f-6649-89e8-1b8b-fc655e4a4db3
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-master-data-management-reltio.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-master-data-management-reltio
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-master-data-management-reltio.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 0b67fb0b-1787-cd23-b792-84d4ff524d3a
---

# Microsoft Purview and Reltio Master Data Management (MDM) | Microsoft Learn

Reltio Integration for Microsoft Purview is implemented through our Reltio Integration Hub (RIH). The integration consists of Reltio and Microsoft Purview connections and recipes to read the tenant business config from Reltio and create corresponding objects in Microsoft Purview.

The integration supports these objects:

- Entity types
- Entity attributes - Simple, Nested, Reference
- Relationship types
- Relationship attributes - Simple, Nested

The foundation of the integration is creating the EntityDefs in Microsoft Purview's Data Map for every Reltio’s object.

Microsoft Purview’s Data Map is like a central inventory which powers the Microsoft Purview Unified Catalog, the Microsoft Purview Data Estate Insights and the Microsoft Purview Data Policy as unified experiences within the Microsoft Purview governance portal.

EntityDef is like a class in object-oriented programming and provides the schema or blueprint for all the Reltio objects. It defines the structure of the entities, attributes, relationships, and their types. This schema ensures that all instances of the entity adhere to rules and constraints for the entities.

| Reltio | Microsoft Microsoft Purview |
| --- | --- |
| System | EntityDef “reltio\_system” |
| Tenant | EntityDef “reltio\_tenant” |
| Entity Type | EntityDef “reltio\_entity\_type” |
| Simple attribute (Entity Type, Relationship Type) | EntityDef “reltio\_attribute” |
| Nested attribute (Entity Type, Relationship Type) | EntityDef “reltio\_attribute” |
| Reference attribute (Entity Type) | EntityDef “reltio\_attribute” |
| Relationship Type | EntityDef “reltio\_relationship\_type” |

Later the integration creates a Reltio System as an Entity in Microsoft Purview's Data Map. The Reltio tenant is created also as an Entity under the Reltio System in Microsoft Purview using the implements relationship.

![Screenshot of reltio lineage.](media/reltio-mdm/reltio-lineage.png)

Reltio System contains the following properties: description, displayName (same as Reltio label), name (last part of Reltio URI), qualifiedName (unique identifier).

![Screenshot of reltio-datamap-asset.](media/reltio-mdm/reltio-datamap-asset.png)

Reltio Tenant contains the following properties: description, displayName, isActive (if entity isn't removed on Reltio), name, qualifiedName, updatedBy (autopopulated), updatedTime (autopopulated).

![Screenshot of reltio-datamap-asset 1.](media/reltio-mdm/reltio-datamap-asset-1.png)

Properties are descriptive attributes or metadata that provide context about the data asset, helping with discovery, management, and governance without affecting the actual structure or format of the data.

The Microsoft Purview Entity qualifiedName is derived using the

```
<collectionId>/<env>/<tenantId>/<URI>
```

Since the Entity qualifiedName uses the tenant ID and env, it's always unique for a tenant, so the same Microsoft Purview account can be used for multiple tenants.

The created Entities can be verified under DataMap-&gt;Domains-&gt;Collection (by default root)-&gt; Assets-&gt; search the name of your Asset/Entity. To ensure Entities appear in Unified Catalog add them manually to Microsoft Purview Data Product where they need to be published. Entities appear in Unified Catalog assigned to chosen Data Products as Data Assets, with their attributes (subnested and referenced attributes not included) in the Schema section. Schema section is available only for the Entities of specific Asset types: Reltio Entity Type, Reltio Relationship Type. Schema defines the structure of the data and dictates how the data is stored, queried, and maintained. It governs how data must be formatted and what relationships exist within the data

![Screenshot of reltio-datamap-asset 2.](media/reltio-mdm/reltio-datamap-asset-2.png)

![Screenshot of reltio-datamap-asset 3.](media/reltio-mdm/reltio-datamap-asset-3.png)

![Screenshot of reltio-datamap-asset 4.](media/reltio-mdm/reltio-datamap-asset-4.png)

![Screenshot of reltio-datamap-asset 5.](media/reltio-mdm/reltio-datamap-asset-5.png)

![Screenshot of reltio-datamap-asset 6.](media/reltio-mdm/reltio-datamap-asset-6.png)

### Schema

Schema is an important concept that reflects how data is stored and organized in the data store. It reflects the structure of the data and the data restrictions of the elements that construct the structure. Elements on the same schema can be classified differently (due to their content). Also, different transformation (lineage) can happen to only a subset of elements. Due to these aspects, Microsoft Purview can model schema and schema elements as entities, hence schema is usually a relationship attribute to the data asset entity. Examples of schema elements are: columns of a table, json properties of json schema, xml elements of xml schema etc.

[Type definitions and how to create custom types in Microsoft Purview](/en-us/purview/tutorial-custom-types#what-is-schema-in-microsoft-purview)

### Reltio objects mapping to Microsoft Purview entities

#### Entity Types

Entity Types within a tenant are created as Entities called Reltio MDM Entity in Microsoft Purview with a contains relationship with the tenant.

![Screenshot of reltio-lineage-1.](media/reltio-mdm/reltio-lineage-1.png)

![Screenshot of reltio-lineage-2.](media/reltio-mdm/reltio-lineage-2.png)

### Properties of Reltio MDM Entity

Reltio MDM entity contains these properties: description, displayName, isAbstract (if the entity is abstract on Reltio), isActive, name, qualifiedName.

![Screenshot of reltio-mdm-entity-property-1.](media/reltio-mdm/reltio-mdm-entity-property-1.png)

![Screenshot of reltio-mdm-entity-property-2.](media/reltio-mdm/reltio-mdm-entity-property-2.png)

### Relationship Types

Relationship Types within a tenant are created as Entities called Reltio Relationship Type in Microsoft Purview with a contains relationship with the tenant.

Also, Reltio Relationship Type Entity has relations with two Reltio MDM Entities: start\_relationship and end\_relationship. Relationship attributes are added as Entities called Reltio Attributes with a contains relation with the Reltio **Relationship Type Entity.**

This screenshot shows a Contact Reltio MDM Entity connected to have address Reltio Relationship Type Entity with start\_relationship Relationship. And later has address Reltio Relationship Type Entity is connected to Location Reltio Entity **Type Entity** with end\_relationship Relationship. The **has address** Reltio Relationship Type Entity has four simple data attributes with contains relation: Address Type, Address. Rank, Active, Status.

![Screenshot of reltio-relationship-type-1.](media/reltio-mdm/reltio-relationship-type-1.png)

Relationship attributes can further have a contains relation with the Reference attribute. In the example, the Address Type relationship data attributes references the Contact Reltio Entity Type Entity.

![Screenshot of reltio-relationship-type-2.](media/reltio-mdm/reltio-relationship-type-2.png)

Also, Reltio Relationship Type Entities contain the same properties as Reltio Entity Type Entities: description, displayName, isActive, name, qualifiedName.

![Screenshot of reltio-relationship-type-3.](media/reltio-mdm/reltio-relationship-type-3.png)

### Attributes

All Reltio Attribute Entities (Simple, Nested, Reference) may contain the following properties (depending on the availability on Reltio):

- dataType (Nested, Reference, or data type for Simple attributes),
- description, displayName, isActive, name, qualifiedName,
- faceted
- hidden
- important
- PII
- RDMAttributeName
- required
- searchable
- system

![Screenshot of reltio-attribute.](media/reltio-mdm/reltio-attribute.png)

### Simple Attributes

Simple attributes are created as Entities called Reltio Attribute in Microsoft Purview with a contains relationship with its entity.

![Screenshot of reltio-simple-attribute-1.](media/reltio-mdm/reltio-simple-attribute-1.png)

![Screenshot of reltio-simple-attribute-2.](media/reltio-mdm/reltio-simple-attribute-2.png)

![Screenshot of reltio-simple-attribute-3.](media/reltio-mdm/reltio-simple-attribute-3.png)

### Nested Attributes

Nested attributes are created as Entities called Reltio Attribute in Microsoft Purview with a relationship with its entity. Sub nested attributes are also created as Entities called Reltio Attribute with a relationship with the parent nested attribute. This screenshot shows a Contact Reltio Entity Type that contains the Email nested attribute, which further contains multiple sub nested attributes like username, domain type, etc.

![Screenshot of reltio-nested-attribute-1.](media/reltio-mdm/reltio-nested-attribute-1.png)

![Screenshot of reltio-nested-attribute-2.](media/reltio-mdm/reltio-nested-attribute-2.png)

### Reference Attributes

A Reference attribute in a Reltio Entity Type is also created as Entities called Reltio Attribute in Microsoft Purview with a contains relationship with its entity. Sub referenced attributes are also created as Entities called Reltio Attribute with a contains relationship with the parent reference attribute.

This screenshot shows a Contact Reltio Entity Type entity with a Reference attribute called Address, which contains multiple simple attributes like verification status, PO Box, state, country/region, etc., and some nested attributes like Zip and Geo Location.

![Screenshot of reltio-reference-attribute-1.](media/reltio-mdm/reltio-reference-attribute-1.png)

![Screenshot of reltio-reference-attribute-2.](media/reltio-mdm/reltio-reference-attribute-2.png)

### Lookup tables

- Microsoft Purview Created Assets
- Stores Microsoft Purview asset GUID. Will be used for soft delete of Microsoft Purview assets.
- Microsoft Purview Reference Attributes Table
- Stores ID of reference attributes and its array of referred URIs. This is created for avoiding going through the L3 configuration twice in order to create reference attributes.

### Microsoft Purview Recursion Table

Acts as a stack for storing function calls for implementing recursive calls for processing nested attributes. Stores attribute’s json, asset ID of parent, asset type of parent, relationship type. Contains a dummy field called processed which is not used but is required for getting a single entry from the table.

### Configure RIH recipes

You need to have the Microsoft Purview connector license in your contract. Reach out to your Reltio Account Manager for licensing needs.

Once you have the Microsoft Purview connector license in your Reltio contract, the Microsoft Purview connector recipes and connections are deployed to your tenant's Reltio Integration Hub (RIH) instance.

- Configure Connections
- Configure Environment properties.

**To configure the recipes:** Check the recipes

The recipes package contains two connections and seven recipe functions. The package is deployed in the Reltio Solution Templates project in your RIH account.

- Connect with your Reltio tenant
    - Enter the connection details
        - Connection Name: for example, Microsoft Purview
        - Environment URL: for example, 361, tst-01 etc
        - Tenant Id: for example, a0bcdEf1ghiJ2Kl
        - Set Client Authorization to No
        - Reltio User Name and Password
    - Select Connect
- The status changes to Connected and the button to Disconnect when the connection is established
- Connect with your Purview account

Before you’re able to connect you need to generate the client ID and client secret based on this documentation - [API authentication for Microsoft Purview Data Planes](/en-us/purview/tutorial-using-rest-apis)

1. Enter the connection details

- Connection Name - for example, Microsoft Purview Portal
- Connection Type - Cloud
- Authentication type - Azure OAuth 2
- Azure Tenant ID - for example, a0bcdEf1ghiJ2Kl
- Azure OAuth client ID & client secret
- Base URL 

    ```
    https://api.purview-service.microsoft.com
    ```
- OAuth scopes

1. Select Connect

- The status changes to Connected and the button to Disconnect when the connection is established.

Manually create a Microsoft Purview Domain in the Data Map domains and add it to the recipe parameters (name of parameter) & add Collection to the recipe parameters name to create the Reltio system in an existing Domain & Collection. Make sure the User ID of Collection creator matches the UserID of integration recipe, otherwise data won’t be populated there. If you don't create the Domain then the recipe fails. If you don’t provide a value for Collection then the integration uses this default value:

- Collection - purviewintegration

![Screenshot of reltio-purview-collection.](media/reltio-mdm/reltio-purview-collection.png)

### Use Reltio integration for Microsoft Purview

Let's cover the usage scenarios for Reltio Integration for Microsoft Purview. The following recipes and functions are deployed to the Recipes folder:

- Main
- Initial setup
- Create Entities
- Create Attributes
- Create Relationships
- Create reference attribute relationships
- Soft-delete Assets