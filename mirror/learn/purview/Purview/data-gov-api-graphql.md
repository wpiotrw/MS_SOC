---
layout: Conceptual
title: GraphQL API with Microsoft Purview (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-api-graphql
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
description: This tutorial describes the working with the GraphQL API to interact with Microsoft Purview resources.
locale: en-us
document_id: 2c808eb7-44f3-6179-9d4a-5c703aebae74
document_version_independent_id: 2c808eb7-44f3-6179-9d4a-5c703aebae74
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-api-graphql.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-api-graphql
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-api-graphql.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 62143542-c96a-a179-2369-874dbc382de8
---

# GraphQL API with Microsoft Purview (preview) | Microsoft Learn

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

In this tutorial, learn to programmatically interact with Microsoft Purview using the GraphQL API. For more information about GraphQL in general, see [this introduction to GraphQL](https://graphql.org/learn/).

Using GraphQL is similar to using the REST APIs, in that you send a JSON payload to a service endpoint. However, GraphQL allows us to return complete information in a single fetch, eliminating the need for multiple API calls.

GraphQL also uses declarative data fetching. Declarative data fetching is useful for selective fetch on fields like classification/term/related entity linked to the original entity. By using GraphQL with these query patterns, we can optimize backend database fetching and data transmission. A good example is “Get Entity with filtered related entities, separated by aliases."

With its introspection feature, the GraphQL API becomes self-descriptive, enabling clients to retrieve schema details such as available queries, types, and query parameters. See more about [introspection](https://graphql.org/learn/introspection/).

## Prerequisites

- If you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) before you begin.
- You must have an existing Microsoft Purview account. If you don't, see the [quickstart for creating a Microsoft Purview account](create-microsoft-purview-portal).
- To establish a bearer token and to call any APIs, see [the documentation about how to authenticate APIs for Microsoft Purview](data-gov-api-rest-data-plane).

## GraphQL Endpoint

For all the requests, you can send a `POST` request to the following endpoint:

```dotnetcli
POST https://{{endpoint}}/datamap/api/graphql
```

- If you're using [the new Microsoft Purview portal](purview-portal), the {{endpoint}} value is: `api.purview-service.microsoft.com`.
- If you're using [the classic Microsoft Purview governance portal](use-microsoft-purview-governance-portal), the {{endpoint}} value is: `{your_purview_account_name}.purview.azure.com`.

## Basic query

### Entity - List By Guids

```JSON
query {
    entities(where: { guid: ["<guid1>", "<guid2>"] }) { #Values in the array are combined as a logical-OR.
        guid
        createTime
        updateTime
        typeName
        attributes
        name
        qualifiedName
        description
    }
}
```

Sample Response:

```JSON
{
    "data": {
        "entities": [
            {
                "guid": "9fb74c11-ac48-4650-95bc-760665c5bd92",
                "createTime": 1553072455110,
                "updateTime": 1553072455110,
                "typeName": "azure_storage_account",
                "attributes": {
                    "qualifiedName": "https://exampleaccount.core.windows.net",
                    "name": "ExampleStorageAccount",
                },
                "name": "ExampleStorageAccount",
                "qualifiedName": "https://exampleaccount.core.windows.net",
                "description": "Example Storage Account"
            }
        ]
    }
}
```

### Query entities by type and qualified name

```JSON
query {
    entities(
        where: {
            type: { typeName: ["<entityType1>", "<entityType2>"] }
            qualifiedName: { in: ["<qualifiedName1>", "<qualifiedName2>"] }
        }
    ) {
        guid
        typeName
        qualifiedName
        attributes
    }
}
```

The operator `in` is used to query multiple qualified names.

Possible Operators could be `exists|eq|ne|in|nin|gt|ge|lt|le`. You can find more server schema details with [introspection](https://graphql.org/learn/introspection/).

## Declarative data fetching

### Get entity with selected fields

```JSON
query {
    entities(where: { guid: "<guid>" }) {
        guid
        typeName
        attributes
        businessAttributes
        qualifiedName
    }
}
```

### Get entity with all fields

```JSON
query {
    entities(where: { guid: "<guid>" }) {
        guid
        createTime
        createdBy
        updateTime
        updatedBy
        lastModifiedTS
        typeName
        attributes
        businessAttributes
        collectionId
        customAttributes
        hierarchyInfo {
            ...hierarchyInfoFields
        }
        labels
        sensitivityLabel {
            ...sensitivityLabelFields
        }
        source
        sourceDetails
        qualifiedName
        name
        description
        displayName
        userDescription
        classifications {
            ...classificationFields
        }
        relatedEntities {
            ...relatedEntitiesFields
        }
        assignedTerms {
            ...assignedTermsFields
        }
    }
}
```

### Get entity with classifications

#### - with all classifications

```JSON
query {
    entities(where: { guid: "<guid>" }) {
        guid
        typeName
        attributes
        classifications {
            typeName
            attributes
        }
    }
}
```

#### - with filtered classifications

```JSON
query {
    entities(where: { guid: "<guid>" }) {
        guid
        typeName
        attributes
        classifications(where: { type: { typeName: "<classificationType>" } }) {
            typeName
            attributes
        }
    }
}
```

### Get entity with related entities

#### - with all related entities

```JSON
query {
    entities(where: { guid: "<guid>" }) {
        guid
        typeName
        attributes
        relatedEntities {
            relationshipAttributeName
            relationship {
                guid
                typeName
                attributes
            }
            entity {
                guid
                typeName
                qualifiedName
                attributes
            }
        }
    }
}
```

#### - with filtered related entities

```JSON
query {
    entities(where: { guid: "<guid>" }) {
        guid
        typeName
        attributes
        relatedEntities(where: { relationshipAttributeName: "<relAttrName1>" }) {
            entity {
                guid
                typeName
                qualifiedName
                attributes
            }
        }
    }
}
```

#### - with filtered related entities, separated by aliases

```JSON
query {
    entities(where: { guid: "<guid>" }) {
        guid
        typeName
        attributes
        alias1: relatedEntities(where: { relationshipAttributeName: "<relAttrName1>" }) {
            entity {
                guid
                typeName
                attributes
            }
        }
        alias2: relatedEntities(where: { relationshipAttributeName: "<relAttrName2>" }) {
            entity {
                guid
                typeName
                attributes
            }
        }
    }
}
```

### Get entity with glossary terms

#### - with all glossary terms

```JSON
query {
    entities(where: { guid: "<guid>" }) {
        guid
        typeName
        attributes
        assignedTerms {
            confidence
            createdBy
            description
            expression
            steward
            source
            status
            term {
                qualifiedName
                name
                shortDescription
                longDescription
            }
        }
    }
}
```

#### - with filtered glossary terms

```JSON
query {
    entities(where: { guid: "<guid>" }) {
        guid
        typeName
        attributes
        assignedTerms {
            confidence
            createdBy
            description
            expression
            steward
            source
            status
            term {
                qualifiedName
                name
                shortDescription
                longDescription
            }
        }
    }
}
```

## Filtering (preview)

The performance of exact matching for ‘GUID’ and ‘Qualified-Name’ is guaranteed in the examples provided in the 'basic queries' section. However, there are some limitations for other filtering patterns:

- **Filtering on Non-indexed Fields**: Fields other than GUID & qualified name are currently not indexed (as examples in the “Simple filter” section). Filtering over nonindexed fields without criteria on GUID/Qualified-name will result in a table scan and might cause performance issues on large datasets.
- **Nested Filtering**: Similar to nonindexed fields, nested filtering can cause table scans, which might cause performance issues on large datasets. For example, finding an entity with a linked classification/term/related entity.

Despite these limitations, this call pattern is superior to client-side filtering and is currently used by our internal client.

### Simple filter

#### Query entities by type and system attributes

```JSON
query {
    entities(
        where: {
            type: { typeName: "<entityType>" }
            name: { eq: "<value>" }
            createTime: { timerange: LAST_7D }
            updateTime: { gt: "<timestamp>" }
        }
    ) {
        guid
        typeName
        qualifiedName
        attributes
    }
}
```

#### Query entities by type and attributes

```JSON
query {
    entities(
        where: {
            type: { typeName: "<entityType>" }
            attribute: { field: "<attrName>",operator: eq, value: "<attrValue>" }
        }
    ) {
        guid
        typeName
        qualifiedName
        attributes
    }
}
```

#### Query entities by type and business attributes

```JSON
query {
    entities(
        where: {
            type: { typeName: "<entityType>" }
            businessAttribute: { field: "<BusinessMetadataName>.<BusinessAttributeName>", operator: eq, value: "<BizAttrValue>" }
        }
    ) {
        guid
        typeName
        qualifiedName
        attributes
    }
}
```

#### Query entities by collection

Currently, this query pattern isn't supported for subassets.

```JSON
query {
    entities(
        where: {
            type: { typeName: "<entityType>" }
            collectionID: "<collectionId>"
        }
    ) {
        guid
        typeName
        qualifiedName
        attributes
    }
}
```

#### Filter combination

Keys in an object(map) are combined as a logical AND.

```JSON
query {
    entities(
        where: {
            type: { typeName: "<entityType>" }
            or: [
                {
                    and: [
                        { attribute: { field: "<attrName1>", value: "<attrValue1>" } }
                        { attribute: { field: "<attrName2>", value: "<attrValue2>" } }
                    ]
                }
                {
                    not: {
                        businessAttribute: {
                            field: "<BusinessMetadataName>.<BusinessAttributeName>", value: "<BizAttrValue>"
                        }
                    }
                }
            ]
        }
    ) {
        guid
        typeName
        qualifiedName
        attributes
    }
}
```

### Nested filter

Currently, this query pattern isn't supported for subassets.

#### Query entity by classification

```JSON
query {
    entities(
        where: {
            classification: { type: { typeName: "<classificationType>", includeSubTypes: true } }
        }
    ) {
        guid
        typeName
        qualifiedName
        attributes
    }
}
```

#### Query entity by related entity

```JSON
query {
    entities(
        where: {
            relatedEntity: {
                relationshipAttributeName: "<relAttrName>"
                entity: {
                    type: { typeName: "<entityType>" }
                }
            }
        }
    ) {
        guid
        typeName
        qualifiedName
        attributes
    }
}
```

#### Query entity by glossary terms

```JSON
query {
    entities(
        where: {
            assignedTerm: {
                term: {
                    qualifiedName: { eq: "<termName>" }
                }
            }
        }
    ) {
        guid
        typeName
        qualifiedName
        attributes
    }
}
```

## Other queries

### Get relationship

```JSON
query {
    relationships(where: { guid: "<guid>" }) {
        guid
        typeName
        attributes
        end1 {
            guid
            typeName
            qualifiedName
            attributes
        }
        end2 {
            guid
            typeName
            qualifiedName
            attributes
        }
    }
}
```

Sample Response:

```JSON
{
    "data": {
        "relationships": [
            {
                "guid": "...",
                "typeName": "ExampleRelationship",
                "attributes": {},
                "end1": {
                    "guid": "...",
                    "typeName": "column",
                    "qualifiedName": "...",
                    "attributes": {}
                },
                "end2": {
                    "guid": "...",
                    "typeName": "column",
                    "qualifiedName": "...",
                    "attributes": {}
                }
            }
        ]
    }
}
```

### Lineage

#### Get dataset with downstream datasets

This query returns downstream datasets to 2 degrees.

```JSON
query {
    entities(where: { guid: "<guid>" }) {#dataset
        guid
        typeName
        qualifiedName
        relatedEntities(where: { relationshipAttributeName: "inputToProcesses" }) {
            entity {#process
                guid
                typeName
                relatedEntities(where: { relationshipAttributeName: "outputs" }) {
                    entity {#dataset
                        guid
                        typeName
                        qualifiedName
                        relatedEntities(where: { relationshipAttributeName: "inputToProcesses" }) {
                            entity {#process
                                guid
                                typeName
                                qualifiedName
                                relatedEntities(where: { relationshipAttributeName: "outputs" }) {
                                    entity {#dataset
                                        guid
                                        typeName
                                        qualifiedName
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
```

Sample Response:

```JSON
{
    "data": {
        "entities": [
            {
                "guid": "...",
                "typeName": "Dataset",
                "qualifiedName": "...",
                "relatedEntities": [
                    {
                        "entity": {
                            "guid": "...",
                            "typeName": "Process",
                            "relatedEntities": [
                                {
                                    "entity": {
                                        "guid": "...",
                                        "typeName": "Dataset",
                                        "qualifiedName": "...",
                                        "relatedEntities": [
                                            {
                                                "entity": {
                                                    "guid": "...",
                                                    "typeName": "Process",
                                                    "relatedEntities": [
                                                        {
                                                            "entity": {
                                                                "guid": "...",
                                                                "typeName": "Dataset",
                                                                "qualifiedName": "..."
                                                            }
                                                        }
                                                    ]
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        ]
    }
}
```

## Limitations

### Query fetch-depth limitation:

Queries are limited by query depth. The maximum depth is 5. For example, the following query will fail:

```JSON
query {
    entities { #depth 1
        relatedEntities { #depth 2
            entity {
                relatedEntities { #depth 3
                    entity {
                        assignedTerms{ #depth 4
                            term {
                                classifications { #depth 5
                                    ...
                                }
                            }
                        }
                        relatedEntities { #depth 4
                            entity {
                                assignedTerms{ #depth 5
                                    term {
                                        classifications { #depth 6
                                            ...
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
```

### Execution-time fetch-cost limitation:

Queries are constrained by the cost of query execution. The maximum allowable cost is set at 100 units.

The execution fetch cost is computed each time we aim to retrieve related entities, assigned terms, or classifications for a given entity or term.

#### Example

Consider a scenario where we query 3 entities, each with two related entities. The cost calculation would be as follows:

- One unit for the root query
- Three units for each level-1 entity

Hence, the total cost for this query would be `1 (root query) + 3 (level-1 entities) = 4`.

### Filtering performance

Filtering is currently preview and has some limitations. See filtering for more information.

GraphQL queries begin with a root query that retrieves the top-level nodes. It then recursively fetches the related nodes.

The performance of a nested query is primarily determined by the root query because the related nodes are fetched from a known starting point, similar to a foreign key in SQL.

To optimize performance, it’s crucial to avoid wildcard root queries that could trigger a table scan on the top-level nodes.

For instance, the following query could cause performance issues on large datasets because the `name` field isn't indexed:

```JSON
query {
    entities(where: { name: { eq: "<value>" } }) {
        guid
        typeName
        attributes
        relatedEntities {
            entity {
                guid
                typeName
                attributes
            }
        }
    }
}
```

To prevent such performance issues, ensure that you apply a filter on `guid` or `qualifiedName`.