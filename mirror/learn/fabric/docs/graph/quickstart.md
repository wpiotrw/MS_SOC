---
layout: Conceptual
title: 'Quickstart: Create Your First Graph in Microsoft Fabric - Microsoft Fabric | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/fabric/graph/quickstart
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
description: Create a basic graph with two nodes and one edge in Microsoft Fabric in just a few minutes using the visual graph modeling experience.
ms.topic: quickstart
ms.date: 2026-06-23T00:00:00.0000000Z
ms.reviewer: wangwilliam
ms.search.form: Quickstart - Create your first graph in Microsoft Fabric
ai-usage: ai-assisted
locale: en-us
document_id: 1780830b-2915-3a39-8712-f2cd251c6146
document_version_independent_id: 1780830b-2915-3a39-8712-f2cd251c6146
original_content_git_url: https://github.com/MicrosoftDocs/fabric-docs-pr/blob/live/docs/graph/quickstart.md
site_name: Docs
depot_name: MSDN.fabric-docs
page_type: conceptual
toc_rel: ../iq/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.fabric-docs/{branchName}{pdfName}
asset_id: graph/quickstart
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/graph/quickstart.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e7cd09c2-9e9a-4f0d-b160-c15783f45b1f
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1d337399-0ca4-4b4c-acef-8df37820e018
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
platformId: 98a12372-9149-3c27-08d5-488a60a0065e
---

# Quickstart: Create Your First Graph in Microsoft Fabric - Microsoft Fabric | Microsoft Learn

In this quickstart, you use graph in Microsoft Fabric to create a basic graph with two nodes and one edge, and then run a query. This process takes about 15 minutes.

For a comprehensive tutorial that covers the full Adventure Works data model and more advanced scenarios, see the [graph tutorial](tutorial-introduction).

## Prerequisites

Before you start this quickstart, verify that:

1. You have access to a Microsoft Fabric capacity (F2 or higher) or a [Fabric trial](../fundamentals/fabric-trial).
2. [Graph is available in your region](overview#region-availability).
3. You're a member of a Fabric workspace or have permission to create items in the workspace. For more information, see [Workspaces in Microsoft Fabric](../admin/portal-workspaces).

    Important

    Access management of the graph is restricted to the workspace that hosts it. Users outside of the workspace can't access the graph. Users within the workspace who have access to the underlying data in the lakehouse can model and query the graph.

## Load sample data

To create your graph, first load sample data into a lakehouse in your Fabric workspace.

### Download the sample data

1. Go to the [graph in Microsoft Fabric GQL example datasets](https://github.com/microsoft/fabric-samples/tree/main/docs-samples/graph) on GitHub.
2. Select the *adventureworks\_docs\_sample.zip* file and download it to your local machine.

    Tip

    To download a file from GitHub, select the file, and then select the **Download raw file** icon.
3. Extract the downloaded *adventureworks\_docs\_sample.zip* file to a folder on your local machine.

    Tip

    In File Explorer, right-click the zip file and select **Extract All**, then choose a destination folder.

### Create a lakehouse

1. In [Microsoft Fabric](https://fabric.microsoft.com/), select the workspace where you want to create the lakehouse.
2. Select **+ New item**.
3. Select **Store data** &gt; **Lakehouse**.
4. Enter a name (for example, "AdventureWorksLakehouse"), clear the **Lakehouse schemas** option, and select **Create**.

### Load the data into tables

For this quickstart, you only need two tables: *adventureworks\_customers* and *adventureworks\_orders*. Upload the full sample data folder, and then load just these two tables.

Note

The full set of sample files is used in the [full graph tutorial](tutorial-introduction). You can also use them to explore additional data on your own.

1. In your lakehouse, hover over **Files**, select the ellipsis (...), and then select **Upload** &gt; **Upload folder**.
2. Browse to the extracted folder and upload it. This action uploads all the sample data files to your lakehouse.
3. Expand **Files** and the uploaded folder to see the subfolders. For this quickstart, you only need to load two of them as tables.
4. Hover over the *adventureworks\_customers* subfolder, select the ellipsis (...), and choose **Load to Tables** &gt; **New table**.
5. Set the file type to **parquet** and select **Load**.
6. Repeat steps 4-5 for the *adventureworks\_orders* subfolder.

When you finish, you see the two tables under **Tables** in the lakehouse Explorer panel.

[![Screenshot showing the adventureworks_customers and adventureworks_orders tables.](media/quickstart/tables.png)](media/quickstart/tables.png#lightbox)

## Create a graph model

1. In your [Microsoft Fabric workspace](https://fabric.microsoft.com/), select **+ New item**.
2. Enter *graph* in the search box, press **Enter** to search for graph items, and select **Graph model**. Alternatively, scroll down to **Analyze and train data** &gt; **Graph model**.

    [![Screenshot showing the new item menu with the option to select Graph model.](media/quickstart/new-item-graph-model.png)](media/quickstart/new-item-graph-model.png#lightbox)
3. Enter a name for your graph model, such as *AdventureWorksGraph*, and select **Create**.

After creating the graph model, you're taken to the graph view where you can see the default mode is set to **Model**. Across the top ribbons, you see buttons for **Save**, **Get data**, **Add node**, **Add edge**, and **Delete**.

[![Screenshot showing the default view of the graph model.](media/quickstart/default-view.png)](media/quickstart/default-view.png#lightbox)

## Add data to your graph

To add data to your graph, follow these steps in graph view:

1. In the top ribbon, select **Get data**.
2. From the **OneLake catalog**, select your lakehouse with the Adventure Works data.
3. Select **Add**.
4. Select the *adventureworks\_customers* and *adventureworks\_orders* tables, and then select **Load**.

    [![Screenshot showing the get data dialog with selected tables.](media/quickstart/get-data.png)](media/quickstart/get-data.png#lightbox)

## Define your graph's structure

Now that your data is loaded, define your graph's structure by adding nodes and edges. In this quickstart, you add two node types (`Customer` and `Order`) and one edge type (`purchases`) to model the relationship between customers and their orders.

### Add two nodes

1. In the top ribbon, select **Add node**.
2. Configure the first node:

    - **Node label**: `Customer`
    - **Source table**: adventureworks\_customers
    - **Key**: CustomerID\_K

    [![Screenshot showing the add node to graph dialog.](media/quickstart/node-add-customer.png)](media/quickstart/node-add-customer.png#lightbox)
3. Select **+ Add property**, **Add all columns**, and **Apply**. This step makes all columns in this source table available as properties for the node.

    [![Screenshot showing the add node to graph dialog with four properties.](media/quickstart/node-add-customer-properties.png)](media/quickstart/node-add-customer-properties.png#lightbox)
4. Select **Create**. You see a node for `Customer` appear on the graph canvas.
5. Select **Add node** again.
6. Configure the second node:

    - **Node label**: `Order`
    - **Source table**: adventureworks\_orders
    - **Key**: SalesOrderDetailID\_K
7. Select **+ Add property**, **Add all columns**, and **Apply**. This step makes all columns in this source table available as properties for the node.
8. Select **Create**.

You now have two nodes, `Customer` and `Order`, visible on the graph canvas.

![Screenshot showing two new nodes on the canvas.](media/quickstart/nodes.png)

### Add one edge

1. In the top ribbon, select **Add edge**.
2. Configure the edge:

    - **Edge label**: `purchases`
    - **Source table**: adventureworks\_orders
    - **Origin node**: `Customer`
    - **Origin key**: CustomerID\_FK
    - **Target node**: `Order`
    - **Target key**: SalesOrderDetailID\_K

    [![Screenshot showing the add edge dialog.](media/quickstart/edge-add-purchases.png)](media/quickstart/edge-add-purchases.png#lightbox)
3. Select **+ Add property**, **Add all columns**, and **Apply**. This step makes all columns in this source table available as properties for the edge.
4. Select **Create**.
5. In the top ribbon, select **Save**.

You see the node and edge labels in the graph view canvas.

![Screenshot showing the new edge between the two nodes on the canvas.](media/quickstart/nodes-edge.png)

The data might take a few minutes to finish loading. Wait for the *Data load is in progress* label to show *Data load completed...* before proceeding to the next section.

[![Screenshot showing the confirmation message that data load completed.](media/quickstart/data-load-completed.png)](media/quickstart/data-load-completed.png#lightbox)

## Query your graph

Run a GQL query to find the top five customers by order count.

1. In the **Modes** panel, select **Query** mode.
2. In the top ribbon, select **Query builder &gt; Code editor**.

    [![Screenshot showing how to select query mode and the code editor.](media/quickstart/query-mode-code-editor.png)](media/quickstart/query-mode-code-editor.png#lightbox)
3. Enter the following GQL query in the input box:

    ```gql
    MATCH (c:Customer)-[:purchases]->(o:`Order`)
    RETURN c.fullName AS customer_name, count(o) AS num_orders
    GROUP BY customer_name
    ORDER BY num_orders DESC
    LIMIT 5
    ```
4. In the top ribbon, select **Run query**. You see five rows listing customer names and their order counts, sorted from most to fewest orders.

    [![Screenshot showing the result of running a GQL query.](media/quickstart/code-editor-query-and-results.png)](media/quickstart/code-editor-query-and-results.png#lightbox)

Congratulations! You created your first graph in Microsoft Fabric and ran a query against it.