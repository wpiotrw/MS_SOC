---
layout: Conceptual
title: How graph in Microsoft Fabric works - Microsoft Fabric | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/fabric/graph/how-graph-works
breadcrumb_path: /fabric/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Fabric
show_latex: false
feedback_system: Standard
feedback_help_link_url: https://community.fabric.microsoft.com/powerbi
feedback_help_link_type: ask-the-community
feedback_product_url: https://ideas.fabric.microsoft.com/
ms.service: fabric
author: baanders
ms.author: baanders
ms.subservice: graph
description: Learn how data flows through graph in Microsoft Fabric, from data ingestion and storage in OneLake to graph modeling, querying, and returning results.
ms.topic: concept-article
ms.date: 2026-05-20T00:00:00.0000000Z
ms.reviewer: wangwilliam
ai-usage: ai-assisted
locale: en-us
document_id: b4f10949-de49-044f-c5e2-dcfb3ee3984b
document_version_independent_id: b4f10949-de49-044f-c5e2-dcfb3ee3984b
original_content_git_url: https://github.com/MicrosoftDocs/fabric-docs-pr/blob/live/docs/graph/how-graph-works.md
site_name: Docs
depot_name: MSDN.fabric-docs
page_type: conceptual
toc_rel: ../iq/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.fabric-docs/{branchName}{pdfName}
asset_id: graph/how-graph-works
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/graph/how-graph-works.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e7cd09c2-9e9a-4f0d-b160-c15783f45b1f
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1d337399-0ca4-4b4c-acef-8df37820e018
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
platformId: 17034404-61d8-1e97-a719-c37049bd9a53
---

# How graph in Microsoft Fabric works - Microsoft Fabric | Microsoft Learn

Graph in Microsoft Fabric transforms structured data stored in OneLake into a modeled, queryable graph. Query the graph by using visual or GQL-based tools that run through a common engine to produce visual, tabular, or programmatic results.

This article describes the graph architecture and explains the end-to-end data flow from source to insights.

The following diagram illustrates the end-to-end data flow from source to insights:

[!\[Diagram that shows the graph data flow from data sources through storage, graph modeling, query authoring, execution, and results.\](media/tutorial/graph-data-flow.png)
 Data flows from external sources into OneLake storage as tabular source tables. In the graph modeling step, you define node types, edge types, and table mappings to create a labeled property graph. Saving the model produces a queryable graph optimized for traversal. You author queries by using the Query Builder or Code Editor, then execute them through GQL, NL2GQL, or REST. Results return as visual graph diagrams, tabular result sets, or programmatic JSON responses.](media/tutorial/graph-data-flow.png#lightbox)

## Data sources

Data originates from external systems such as Azure services, other cloud platforms, or on-premises sources. Graph in Microsoft Fabric works with data from these sources after you ingest it into OneLake, where graph can read it.

## Storage in OneLake

You store ingested data in [OneLake](../onelake/onelake-overview) as tabular source tables in a lakehouse. Graph ingests data from your lakehouse tables when you save the model, so you don't need to set up a separate ETL pipeline or move data to an external database.

## Graph modeling

In the graph modeling step, you define the graph schema by specifying:

- **Node types:** Entities in your data, such as customers, products, or orders.
- **Edge types:** Relationships between entities, such as "purchases," "contains," or "produces."
- **Table mappings:** How node and edge definitions map to the underlying source tables.

This step creates the [labeled property graph](graph-data-models) structure. Complete graph modeling before you query the graph. For guidance on making these modeling decisions, see [Design a graph schema](design-graph-schema).

Note

Graph doesn't apply structural changes incrementally. If you add properties or change node types, edge types, keys, or mappings, select **Save** in the graph model editor to reload all data and rebuild the queryable graph.

## Queryable graph

When you save the model, graph ingests data from the underlying lakehouse tables and constructs a read-optimized, queryable graph. This graph structure is optimized for traversal and pattern matching, which enables fast and efficient graph queries at scale.

## Query authoring

You author queries against the queryable graph by using one of two experiences:

- **Query Builder:** A visual, interactive interface for exploring nodes and relationships without writing code. For more information, see [Query the graph with the query builder](tutorial-query-builder).
- **Code Editor:** A text-based editor for writing [GQL (Graph Query Language)](gql-language-guide) queries. For more information, see [Query the graph with GQL](tutorial-query-code-editor).

Both options target the same underlying graph. Choose the authoring experience that fits your workflow.

## Query execution

You run queries through a common execution layer that supports:

- **GQL:** Queries the graph by using the [international standard for graph query language (ISO/IEC 39075)](gql-language-guide).
- **Natural Language to GQL (NL2GQL) (preview):** Translates natural language questions into GQL queries. Add graph in Microsoft Fabric as a data source in [Fabric Data Agent](../data-science/concept-data-agent) to enable graph-powered AI reasoning. For details on how NL2GQL works, see the [Graph-powered AI reasoning announcement](https://blog.fabric.microsoft.com/en-US/blog/graph-powered-ai-reasoning-preview/).
- **REST-based execution:** Runs queries programmatically by using the [GQL query API](gql-query-api).

Tip

**Choose your query path:** Use GQL or REST for direct, programmatic access to graph data with full control over query structure. Use NL2GQL (preview) through Fabric Data Agent when you need natural language access — ideal for conversational AI and knowledge assistant scenarios.

This layer runs the query logic against the queryable graph and returns results.

## Query results

Depending on how you query the graph, you receive results in one or more of the following formats:

- **Visual graph diagrams:** Interactive visualizations of nodes and relationships.
- **Tabular result sets:** Structured data in rows and columns.
- **Programmatic responses:** JSON output for REST or downstream consumption.

Explore results interactively, share them as read-only querysets, or use them in other tools and applications.