---
layout: Conceptual
monikers:
- microsoft-sentinel
- azure-monitor
- azure-data-explorer
- microsoft-fabric
defaultMoniker: microsoft-fabric
versioningType: Ranged
title: 'Tutorial: Create your first graphs in Kusto Query Language - Kusto | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/kusto/query/tutorials/your-first-graph?view=microsoft-fabric
config_moniker_range: 'microsoft-fabric || azure-data-explorer || azure-monitor || microsoft-sentinel '
breadcrumb_path: /kusto/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Kusto
feedback_system: Standard
recommendations: true
author: oronkaiser-MSFT-nonEMU
ms.author: oronkaiser
ms.service: azure-data-explorer
services: kusto
description: Learn how to model and query interconnected data using graph semantics in Kusto Query Language (KQL). Build transient and persistent graphs to analyze organizational hierarchies.
ms.topic: tutorial
ms.custom: mvc
ms.reviewer: royo
ms.date: 2026-07-29T00:00:00.0000000Z
locale: en-us
document_id: d8d5f130-f9cd-26d7-3096-21f901059e51
document_version_independent_id: d8d5f130-f9cd-26d7-3096-21f901059e51
original_content_git_url: https://github.com/MicrosoftDocs/dataexplorer-docs-pr/blob/live/data-explorer/kusto/query/tutorials/your-first-graph.md
default_moniker: microsoft-fabric
site_name: Docs
depot_name: Learn.kusto-docs
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Learn.kusto-docs/{branchName}{pdfName}
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: query/tutorials/your-first-graph
moniker_range_name: f0081dc5071f32aee7689305c3508dfe
monikers:
- microsoft-sentinel
- azure-monitor
- azure-data-explorer
- microsoft-fabric
item_type: Content
source_path: data-explorer/kusto/query/tutorials/your-first-graph.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/26e1a60c-4ce1-41de-b2d1-e5f3b7e68e6e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e7cd09c2-9e9a-4f0d-b160-c15783f45b1f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad3bd485-5ca9-4865-afde-baec02586899
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1d337399-0ca4-4b4c-acef-8df37820e018
platformId: a5cf7776-ca2b-538c-836c-b29ca46f5240
---

# Tutorial: Create your first graphs in Kusto Query Language - Kusto | Microsoft Learn

> 
> Switch services using the **Version** drop-down list. [Learn more about navigation](../../docs-navigation).  Applies to: ✅ Microsoft Fabric ✅ Azure Data Explorer ✅ Azure Monitor ✅ Microsoft Sentinel

Graph semantics in Kusto enables you to model and query data as interconnected networks, making it intuitive to analyze complex relationships like organizational hierarchies, social networks, and attack paths. Unlike traditional relational queries that rely on joins, graphs use direct relationships between entities to traverse connections efficiently.

In this tutorial, you:

::: moniker range="azure-data-explorer microsoft-fabric"

- Create a transient graph using the make-graph operator
- Query graphs to find relationships using graph-match
- Build persistent graph models for reusable analysis
- Compare transient versus persistent graph approaches

::: moniker-end

::: moniker range="azure-monitor microsoft-sentinel"

- Create a transient graph using the make-graph operator
- Query graphs to find relationships using graph-match
- Compare transient versus persistent graph approaches

::: moniker-end

If you don't have an Azure Data Explorer cluster, [create a free cluster](/en-us/azure/data-explorer/start-for-free-web-ui) before you begin.

## Prerequisites

- A Microsoft account or Microsoft Entra user identity to sign in to the [help cluster](https://dataexplorer.azure.com/clusters/help)

::: moniker range="microsoft-fabric"

- A [Fabric workspace](/en-us/fabric/get-started/create-workspaces) with a Microsoft Fabric-enabled [capacity](/en-us/fabric/enterprise/licenses#capacity)

::: moniker-end

## Access your query environment

::: moniker range="azure-data-explorer"

Open the [Azure Data Explorer Web UI](https://dataexplorer.azure.com/clusters/help) to access the help cluster for this tutorial.

::: moniker-end

::: moniker range="microsoft-fabric"

Navigate to your Microsoft Fabric workspace and open a KQL database to run the queries.

::: moniker-end

::: moniker range="microsoft-sentinel"

Navigate to the advanced hunting page to start querying Microsoft Sentinel data.

::: moniker-end

::: moniker range="azure-monitor"

Navigate to Logs or to a Log Analytics workspace in the Azure portal to start querying Azure Monitor data.

::: moniker-end

## Create a transient graph with organizational data

Create your first graph using sample organizational data. Transient graphs are created dynamically during query execution using the `make-graph` operator, which makes them ideal for ad-hoc analysis and exploration.

You'll work with a simple company structure where employees report to managers. This organizational hierarchy provides an intuitive example for understanding graph relationships:

![Diagram that shows the organizational hierarchy with Alice as CEO, Bob and Carol as managers, and Dave, Eve, and Frank as individual contributors.](../media/graphs/tutorial-first-graph.png)

Create the organizational graph structure using employee and reporting relationship data:

```kusto
// Create sample employee data
let employees = datatable(name:string, role:string, age:long) 
[ 
  "Alice", "CEO", 45,  
  "Bob", "Engineering Manager", 35,  
  "Carol", "Marketing Manager", 38,  
  "Dave", "Developer", 28,  
  "Eve", "Developer", 26,
  "Frank", "Marketing Specialist", 30
]; 
// Create reporting relationships
let reports = datatable(employee:string, manager:string) 
[ 
  "Bob", "Alice",  
  "Carol", "Alice",  
  "Dave", "Bob",
  "Eve", "Bob",
  "Frank", "Carol"
]; 
// Build the graph and explore it
reports 
| make-graph employee --> manager with employees on name 
| graph-to-table nodes 
```

### Output

| name | role | age |
| --- | --- | --- |
| Alice | CEO | 45 |
| Bob | Engineering Manager | 35 |
| Carol | Marketing Manager | 38 |
| Dave | Developer | 28 |
| Eve | Developer | 26 |
| Frank | Marketing Specialist | 30 |

## Query relationships with graph-match patterns

Use the `graph-match` operator to find specific patterns in your organizational graph. The `graph-match` operator searches for relationships and connections within the graph structure.

Find all employees who directly report to Alice by matching the immediate reporting relationship pattern:

```kusto
let employees = datatable(name:string, role:string, age:long) 
[ 
  "Alice", "CEO", 45,  
  "Bob", "Engineering Manager", 35,  
  "Carol", "Marketing Manager", 38,  
  "Dave", "Developer", 28,  
  "Eve", "Developer", 26,
  "Frank", "Marketing Specialist", 30
]; 
let reports = datatable(employee:string, manager:string) 
[ 
  "Bob", "Alice",  
  "Carol", "Alice",  
  "Dave", "Bob",
  "Eve", "Bob",
  "Frank", "Carol"
]; 
reports 
| make-graph employee --> manager with employees on name 
| graph-match (alice)<-[reports]-(employee)
  where alice.name == "Alice"  
  project employee = employee.name, role = employee.role, age = employee.age
```

### Direct reports output

| employee | role | age |
| --- | --- | --- |
| Bob | Engineering Manager | 35 |
| Carol | Marketing Manager | 38 |

Next, find all employees in Alice's entire organization, including indirect reports, using variable length edges with `*1..3` to traverse multiple levels of the hierarchy:

```kusto
let employees = datatable(name:string, role:string, age:long) 
[ 
  "Alice", "CEO", 45,  
  "Bob", "Engineering Manager", 35,  
  "Carol", "Marketing Manager", 38,  
  "Dave", "Developer", 28,  
  "Eve", "Developer", 26,
  "Frank", "Marketing Specialist", 30
]; 
let reports = datatable(employee:string, manager:string) 
[ 
  "Bob", "Alice",  
  "Carol", "Alice",  
  "Dave", "Bob",
  "Eve", "Bob",
  "Frank", "Carol"
]; 
reports 
| make-graph employee --> manager with employees on name 
| graph-match (alice)<-[reports*1..3]-(employee)
  where alice.name == "Alice"
  project employee = employee.name, role = employee.role, reportingLevels = array_length(reports)
```

### All organization members output

| employee | role | reportingLevels |
| --- | --- | --- |
| Bob | Engineering Manager | 1 |
| Carol | Marketing Manager | 1 |
| Dave | Developer | 2 |
| Eve | Developer | 2 |
| Frank | Marketing Specialist | 2 |

::: moniker range="azure-data-explorer microsoft-fabric"

## Create a persistent graph model

Persistent graphs are stored in the database and can be queried repeatedly without rebuilding the graph structure. Create the same organizational structure as a persistent graph for better performance and reusability.

Create functions that return your sample data, and then define a graph model structure:

```kusto
// Create a function that returns employee data
.create function Employees() {
    datatable(name: string, role: string, age: long)
    [
        "Alice", "CEO", 45,
        "Bob", "Engineering Manager", 35,
        "Carol", "Marketing Manager", 38,
        "Dave", "Developer", 28,
        "Eve", "Developer", 26,
        "Frank", "Marketing Specialist", 30
    ]
}

// Create a function that returns reporting relationships
.create function Reports() {
    datatable(employee: string, manager: string)
    [
        "Bob", "Alice",
        "Carol", "Alice",
        "Dave", "Bob",
        "Eve", "Bob",
        "Frank", "Carol"
    ]
}
```

Define the graph model with node and edge schemas:

```kusto
.create-or-alter graph_model OrganizationGraph ```
{
    "Schema": {
        "Nodes": {
            "Employee": {
                "name": "string",
                "role": "string",
                "age": "long"
            }
        },
        "Edges": {
            "ReportsTo": {
            }
        }
    },
    "Definition": {
        "Steps": [
            {
                "Kind": "AddNodes",
                "Query": "Employees()",
                "NodeIdColumn": "name",
                "Labels": ["Employee"]
            },
            {
                "Kind": "AddEdges",
                "Query": "Reports()",
                "SourceColumn": "employee",
                "TargetColumn": "manager",
                "Labels": ["ReportsTo"]
            }
        ]
    }
}
```
```

Create a graph snapshot to materialize the model into a queryable structure:

```kusto
.make graph_snapshot OrganizationGraph_v1 from OrganizationGraph
```

## Query your persistent graph

Query the persistent graph using the same patterns as transient graphs. Find all employees who report to Alice:

```kusto
graph("OrganizationGraph")
| graph-match (alice)<-[reports]-(employee)
  where alice.name == "Alice"
  project employee = employee.name, role = employee.role, age = employee.age
```

Find all employees in Alice's organization, including indirect reports:

```kusto
graph("OrganizationGraph")
| graph-match (alice)<-[reports*1..3]-(employee)
  where alice.name == "Alice"
  project employee = employee.name, role = employee.role, reportingLevels = array_length(reports)
```

Query a specific snapshot version if needed:

```kusto
graph("OrganizationGraph", "OrganizationGraph_v1")
| graph-match (alice)<-[reports*1..3]-(employee)
  where alice.name == "Alice"
  project employee = employee.name, role = employee.role
```

::: moniker-end

## Compare transient and persistent graphs

Understanding when to use each approach helps you choose the right method for your analysis needs:

| Aspect | Transient Graphs | Persistent Graphs |
| --- | --- | --- |
| **Creation** | `make-graph` operator during query | `.create-or-alter graph_model` + `.make graph_snapshot` |
| **Storage** | In-memory during query execution | Stored in database |
| **Reusability** | Must rebuild for each query | Query repeatedly without rebuilding |
| **Performance** | Good for smaller datasets | Optimized for large, complex graphs |
| **Use cases** | Ad-hoc analysis, exploration | Production analytics, repeated queries |
| **Memory limits** | Limited by node memory | Handles larger datasets |

## Clean up resources

::: moniker range="azure-data-explorer microsoft-fabric"

If you don't plan to continue using the persistent graph models, delete them with the following commands:

1. Drop the graph model:

    ```kusto
    .drop graph_model OrganizationGraph
    ```
2. Drop the helper functions:

    ```kusto
    .drop function Employees
    .drop function Reports
    ```

::: moniker-end

The transient graphs are automatically cleaned up when the query completes, so no additional cleanup is needed for those examples.