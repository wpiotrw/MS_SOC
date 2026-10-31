---
layout: Conceptual
title: Create and get data lineage relationships for custom assets using the Microsoft Purview REST API | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-api-create-lineage-relationships
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
description: This article describes how to create and get data lineage relationships for custom assets in the Microsoft Purview Data Map using the REST API.
locale: en-us
document_id: c0442053-e90b-6bc6-53d8-09afbd3707e1
document_version_independent_id: c0442053-e90b-6bc6-53d8-09afbd3707e1
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-api-create-lineage-relationships.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-api-create-lineage-relationships
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-api-create-lineage-relationships.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: db19720a-38da-07b0-a0f0-d29429ebf811
---

# Create and get data lineage relationships for custom assets using the Microsoft Purview REST API | Microsoft Learn

In this tutorial, you learn how to use Microsoft Purview REST APIs to:

1. Create assets and lineage relationships between the data assets.
2. Query lineage relationships/paths.

APIs referenced in this article:

- [Create Entity](/en-us/rest/api/purview/datamapdataplane/entity/bulk-create-or-update)
- [Create Relationship](/en-us/rest/api/purview/datamapdataplane/relationship/create)
- [Get Lineage by GUID](/en-us/rest/api/purview/datamapdataplane/lineage/get)

## Prerequisites

The use of these APIs requires [Data Curator and Data Reader roles](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections). Check [this tutorial](data-gov-api-rest-data-plane) for details on how to obtain the access token.

## Concepts

### Asset

In Microsoft Purview, there are two types of base assets: DataSet and Process.

- DataSet Assets that contain data such as Azure SQL Table, Oracle Table etc. should be inherited from DataSet.
- Process Assets that process data, such as a data pipeline, query, function etc. should be inherited from Process.

Refer to [assets and types](data-gov-api-custom-types#what-are-asset-and-type-in-microsoft-purview) to understand type definitions of DataSets and Processes.

### Relationships and lineage

In Microsoft Purview, there are three types of relationships for lineage:

- *dataset\_process\_inputs*: connects DataSet to Process, which means the DataSet is the input of the Process
- *process\_dataset\_outputs*: connects Process to DataSet, which means the Process produces the DataSet
- *direct\_lineage\_dataset\_dataset*: connects DataSet1 to DataSet2, which means DataSet1 is the upstream of DataSet2, although we wouldn’t know exactly which Process is between them

**Example 1:***Here’s an example of lineage with 2 DataSets, one Process and two lineage relationships*:

Dataset ---&gt; dataset\_process\_inputs ---&gt; Process ---&gt; process\_dataset\_outputs ---&gt; DataSet

[![Screenshot showing DataSet to Process to DataSet lineage.](media/lineage-rest-apis/dataset-process.jpg)](media/lineage-rest-apis/dataset-process.jpg#lightbox)

**Example 2:***Another example of lineage with 2 DataSets and one lineage relationship:*

Dataset ---&gt; direct\_lineage\_dataset\_dataset ---&gt; DataSet

[![Screenshot showing DataSet to DataSet lineage.](media/lineage-rest-apis/dataset-dataset.jpg)](media/lineage-rest-apis/dataset-dataset.jpg#lightbox)

## Create assets and lineage relationships between the data assets

In the following sections, let’s take hive\_table as an example type for DataSet, and hive\_query\_process as an example type for Process. We'll create assets with those two types and create lineages between them. You can use any other type, which inherits from DataSet or Process to create lineages.

### Example 1

#### Create assets via API

If the assets you want to create lineage for aren't created in Microsoft Purview yet, you can call the following API to create them.

**API**: [Bulk Create Assets](/en-us/rest/api/purview/datamapdataplane/entity/bulk-create-or-update)

**Task**: Create two hive\_tables as datasets - table1 and table2, each with 2 hive\_columns - column1 and column2.

```http
POST {endpoint}/datamap/api/atlas/v2/entity/bulk
```

With the body:

```json
{
  "entities": [
    {
      "typeName": "hive_table",
      "attributes": {
        "qualifiedName": "test_lineage.table1",
        "name": "table1"
      },
      "relationshipAttributes": {
        "columns": [
          {
            "guid": "-11",
            "typeName": "hive_column"
          },{
            "guid": "-12",
            "typeName": "hive_column"
          }
        ]
      },
      "guid": "-1"
    },
    {
      "typeName": "hive_column",
      "attributes": {
        "qualifiedName": "test_lineage.table1#column1",
        "name": "column1",
        "type": "int"
      },
      "guid": "-11",
      "relationshipAttributes": {
        "table": {
          "guid": "-1",
          "typeName": "hive_table"
        }
      }
    },
    {
      "typeName": "hive_column",
      "attributes": {
        "qualifiedName": "test_lineage.table1#column2",
        "name": "column2",
        "type": "int"
      },
      "guid": "-12",
      "relationshipAttributes": {
        "table": {
          "guid": "-1",
          "typeName": "hive_table"
        }
      }
    },
    {
      "typeName": "hive_table",
      "attributes": {
        "qualifiedName": "test_lineage.table2",
        "name": "table2"
      },
      "relationshipAttributes": {
        "columns": [
          {
            "guid": "-21",
            "typeName": "hive_column"
          },{
            "guid": "-22",
            "typeName": "hive_column"
          }
        ]
      },
      "guid": "-2"
    },
    {
      "typeName": "hive_column",
      "attributes": {
        "qualifiedName": "test_lineage.table2#column1",
        "name": "column1",
        "type": "int"
      },
      "guid": "-21",
      "relationshipAttributes": {
        "table": {
          "guid": "-2",
          "typeName": "hive_table"
        }
      }
    },
    {
      "typeName": "hive_column",
      "attributes": {
        "qualifiedName": "test_lineage.table2#column2",
        "name": "column2",
        "type": "int"
      },
      "guid": "-22",
      "relationshipAttributes": {
        "table": {
          "guid": "-2",
          "typeName": "hive_table"
        }
      }
    }    
  ]
}
```

**Task**: Create the process asset 'hive\_view\_query'

```http
POST {endpoint}/datamap/api/atlas/v2/entity/bulk
```

With the body:

```json
{
  "entities": [
    {
      "typeName": "hive_view_query",
      "attributes": {
        "qualifiedName": "test_lineage.HiveQuery1",
        "name": "HiveQuery1",
        "columnMapping": "[{\"DatasetMapping\":{\"Source\":\"test_lineage.table1\",\"Sink\":\"test_lineage.table2\"},\"ColumnMapping\":[{\"Source\":\"column1\",\"Sink\":\"column1\"},{\"Source\":\"column2\",\"Sink\":\"column2\"}]}]"
      },
      "guid": "-1"
    }
  ]
}
```

The above API calls result in creation of two hive\_tables(Datasets) and one hive\_view\_query(Process).

#### Create lineage relationships between Datasets and the Process

**API**: [Create Relationship](/en-us/rest/api/purview/datamapdataplane/relationship/create)

**Task**: Create lineage from table1 -&gt; HiveQuery1 (that is, Dataset -&gt; Process)

```http
POST {endpoint}/datamap/api/atlas/v2/relationship
```

With the body:

```json
{
        "typeName": "dataset_process_inputs",
        "guid": "-1",
        "end1": {
            "typeName": "hive_table",
            "uniqueAttributes": {
                "qualifiedName": "test_lineage.table1"
            }
        },
        "end2": {
            "typeName": "Process",
            "uniqueAttributes": {
                "qualifiedName": "test_lineage.HiveQuery1"
            }
        }
}
```

**Task**: Create lineage from HiveQuery1 -&gt; table2 (that is, Process -&gt; Dataset)

```http
POST {endpoint}/datamap/api/atlas/v2/relationship
```

With the body:

```json
{
        "typeName": "process_dataset_outputs",
        "guid": "-2",
        "end1": {
            "typeName": "Process",
            "uniqueAttributes": {
                "qualifiedName": "test_lineage.HiveQuery1"
            }
        },
        "end2": {
            "typeName": "hive_table",
            "uniqueAttributes": {
                "qualifiedName": "test_lineage.table2"
            }
        }
}
```

#### View lineage

Once the assets and lineage relationships are created, you can check the lineage graph in Microsoft Purview:

[![DataSet-Process-DataSet lineage.](media/lineage-rest-apis/view-lineage-1.jpg)](media/lineage-rest-apis/view-lineage-1.jpg#lightbox)

### Example 2

#### Create a hive table, table3, with two columns

**API**: [Bulk Create Assets](/en-us/rest/api/purview/datamapdataplane/entity/bulk-create-or-update)

**Task**: Create table3, with 2 hive\_columns, column1 and column2

```http
POST {endpoint}/datamap/api/atlas/v2/entity/bulk
```

With the body:

```json
{
"entities": [
    {
      "typeName": "hive_table",
      "attributes": {
        "qualifiedName": "test_lineage.table3",
        "name": "table3"
      },
      "relationshipAttributes": {
        "columns": [
          {
            "guid": "-31",
            "typeName": "hive_column"
          },{
            "guid": "-32",
            "typeName": "hive_column"
          }
        ]
      },
      "guid": "-3"
    },
    {
      "typeName": "hive_column",
      "attributes": {
        "qualifiedName": "test_lineage.table3#column1",
        "name": "column1",
        "type": "int"
      },
      "guid": "-31",
      "relationshipAttributes": {
        "table": {
          "guid": "-3",
          "typeName": "hive_table"
        }
      }
    },
    {
      "typeName": "hive_column",
      "attributes": {
        "qualifiedName": "test_lineage.table3#column2",
        "name": "column2",
        "type": "int"
      },
      "guid": "-32",
      "relationshipAttributes": {
        "table": {
          "guid": "-3",
          "typeName": "hive_table"
        }
      }
    }
   ]
}
```

#### Create direct lineage between table 2 and table 3, with column mapping

**API**: [Create Relationship](/en-us/rest/api/purview/datamapdataplane/relationship/create)

**Task**: Create lineage from table2 -&gt; table3 (that is, Dataset -&gt; Dataset) with column mapping

```http
POST {endpoint}/datamap/api/atlas/v2/relationship
```

With the body:

```json
{
    "typeName": "direct_lineage_dataset_dataset",
    "guid": "-1",
    "end1": {
        "typeName": "hive_table",
        "uniqueAttributes": {
            "qualifiedName": "test_lineage.table2"
        }
    },
    "end2": {
        "typeName": " hive_table ",
        "uniqueAttributes": {
            "qualifiedName": "test_lineage.table3"
        }
    },
    "attributes": {
      "columnMapping": "[{\"Source\":\"column1\",\"Sink\":\"column1\"},{\"Source\":\"column2\",\"Sink\":\"column2\"}]"
    }
}
```

#### View lineage

Now the lineage graph (together from Example 1 & Example 2 above) becomes:

[![DataSet to DataSet lineage.](media/lineage-rest-apis/view-lineage-2.jpg)](media/lineage-rest-apis/view-lineage-2.jpg#lightbox)

Notice that table2 is directly linked to table3, without a HiveQuery between them.

## Query lineage relationships/paths

**API**: [Get Lineage by GUID](/en-us/rest/api/purview/datamapdataplane/lineage/get)

**Task**: Get lineage of table2 via REST API

```http
GET {{endpoint}}/api/atlas/v2/lineage/{{guid_of_table2}}?direction=BOTH
```

Below you can JSON response payload:

```json
{
    "baseEntityGuid": "2a12b3ff-5816-4222-833a-035bf82e06e0",
    "lineageDirection": "BOTH",
    "lineageDepth": 3,
    "lineageWidth": -1,
    "childrenCount": -1,
    "guidEntityMap": {
        "16b93b78-8683-4f88-9651-24c4a9d797b0": {
            "typeName": "hive_table",
            "attributes": {
                "temporary": false,
                "lastAccessTime": 0,
                "createTime": 0,
                "qualifiedName": "test_lineage.table3",
                "name": "table3",
                "retention": 0
            },
            "lastModifiedTS": "1",
            "guid": "16b93b78-8683-4f88-9651-24c4a9d797b0",
            "status": "ACTIVE",
            "displayText": "table3",
            "classificationNames": [],
            "meaningNames": [],
            "meanings": [],
            "isIncomplete": false,
            "labels": [],
            "isIndexed": true
        },
        "cb22ba23-47a2-4149-ade6-e3d9642fe592": {
            "typeName": "hive_table",
            "attributes": {
                "temporary": false,
                "lastAccessTime": 0,
                "createTime": 0,
                "qualifiedName": "test_lineage.table1",
                "name": "table1",
                "retention": 0
            },
            "lastModifiedTS": "1",
            "guid": "cb22ba23-47a2-4149-ade6-e3d9642fe592",
            "status": "ACTIVE",
            "displayText": "table1",
            "classificationNames": [],
            "meaningNames": [],
            "meanings": [],
            "isIncomplete": false,
            "labels": [],
            "isIndexed": true
        },
        "bbeacce6-5bde-46f7-8fe4-689cbb36ba51": {
            "typeName": "hive_view_query",
            "attributes": {
                "qualifiedName": "test_lineage.HiveQuery1",
                "name": "HiveQuery1",
                "columnMapping": "[{\"DatasetMapping\":{\"Source\":\"test_lineage.table1\",\"Sink\":\"test_lineage.table2\"},\"ColumnMapping\":[{\"Source\":\"column1\",\"Sink\":\"column1\"},{\"Source\":\"column2\",\"Sink\":\"column2\"}]}]"
            },
            "lastModifiedTS": "1",
            "guid": "bbeacce6-5bde-46f7-8fe4-689cbb36ba51",
            "status": "ACTIVE",
            "displayText": "HiveQuery1",
            "classificationNames": [],
            "meaningNames": [],
            "meanings": [],
            "isIncomplete": false,
            "labels": [],
            "isIndexed": true
        },
        "2a12b3ff-5816-4222-833a-035bf82e06e0": {
            "typeName": "hive_table",
            "attributes": {
                "temporary": false,
                "lastAccessTime": 0,
                "createTime": 0,
                "qualifiedName": "test_lineage.table2",
                "name": "table2",
                "retention": 0
            },
            "lastModifiedTS": "1",
            "guid": "2a12b3ff-5816-4222-833a-035bf82e06e0",
            "status": "ACTIVE",
            "displayText": "table2",
            "classificationNames": [],
            "meaningNames": [],
            "meanings": [],
            "isIncomplete": false,
            "labels": [],
            "isIndexed": true
        }
    },
    "includeParent": false,
    "relations": [
        {
            "fromEntityId": "2a12b3ff-5816-4222-833a-035bf82e06e0",
            "toEntityId": "16b93b78-8683-4f88-9651-24c4a9d797b0",
            "relationshipId": "23df8e3e-b066-40b2-be29-9fd90693c51b",
            "columnMapping": "[{\"Source\":\"column1\",\"Sink\":\"column1\"},{\"Source\":\"column2\",\"Sink\":\"column2\"}]"
        },
        {
            "fromEntityId": "bbeacce6-5bde-46f7-8fe4-689cbb36ba51",
            "toEntityId": "2a12b3ff-5816-4222-833a-035bf82e06e0",
            "relationshipId": "5fe8d378-39cd-4c6b-8ced-91b0152d3014"
        },
        {
            "fromEntityId": "cb22ba23-47a2-4149-ade6-e3d9642fe592",
            "toEntityId": "bbeacce6-5bde-46f7-8fe4-689cbb36ba51",
            "relationshipId": "73e084bf-98a3-45fb-a1e4-c56cc40661b8"
        }
    ],
    "parentRelations": [],
    "widthCounts": {
        "INPUT": {
            "cb22ba23-47a2-4149-ade6-e3d9642fe592": 0,
            "bbeacce6-5bde-46f7-8fe4-689cbb36ba51": 1,
            "2a12b3ff-5816-4222-833a-035bf82e06e0": 1
        },
        "OUTPUT": {
            "16b93b78-8683-4f88-9651-24c4a9d797b0": 0,
            "2a12b3ff-5816-4222-833a-035bf82e06e0": 1
        }
    }
}
```

## Other Resources

### Type Definitions

All Assets/Entities and Relationships are defined in the type system.

Call [list all type definitions](/en-us/rest/api/purview/datamapdataplane/type/list) API to get current type definitions in your Microsoft Purview instance. If you’re not sure which typeName to use in the API calls described, you can check the type definitions API to find the appropriate Asset/Entity type.

Following is a sample response of this API:

[![TypeDef API response 1.](media/lineage-rest-apis/type-definition-1.jpg)](media/lineage-rest-apis/type-definition-1.jpg#lightbox)

You can see that in the entityDefs in the above response, asset types (such as oracle\_table, oracle\_view etc.) are defined. A further look at the definition of the asset (in this example, oracle\_view) shows that the asset is inherited DataSet type.

[![TypeDef API response 2.](media/lineage-rest-apis/type-definition-2.jpg)](media/lineage-rest-apis/type-definition-2.jpg#lightbox)

Similarly, you can find that a process (for example, Oracle\_function) is inherited from “Process” type as shown:

[![TypeDef API response 3.](media/lineage-rest-apis/type-definition-3.jpg)](media/lineage-rest-apis/type-definition-3.jpg#lightbox)

### Create New Custom Types

If you want to create custom assets or processes, you can use the following APIs.

**API**: [Create Typedef API](/en-us/rest/api/purview/datamapdataplane/type/bulk-create)

**Task**: Create a Custom Process Type

```http
POST {endpoint}/datamap/api/atlas/v2/types/typedefs
```

With the body:

```json
{
  "enumDefs": [],
  "structDefs": [],
  "classificationDefs": [],
  "entityDefs": [
    {
      "name": "MyCustomServiceProcess",
      "superTypes": [
        "Process"
      ],
      "typeVersion": "1.0",
      "attributeDefs": []
    }
  ],
  "relationshipDefs": []
}
```

**Task**: Create a Custom DataSet Type

```http
POST {endpoint}/datamap/api/atlas/v2/types/typedefs
```

With the body:

```json
{
  "enumDefs": [],
  "structDefs": [],
  "classificationDefs": [],
  "entityDefs": [
    {
      "name": "MyCustomDataSet",
      "superTypes": [
        "DataSet"
      ],
      "typeVersion": "1.0",
      "attributeDefs": []
    }
  ],
  "relationshipDefs": []
}
```