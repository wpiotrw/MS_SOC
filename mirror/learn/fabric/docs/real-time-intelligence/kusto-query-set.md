---
layout: Conceptual
title: Query data in a KQL queryset - Microsoft Fabric | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/fabric/real-time-intelligence/kusto-query-set
breadcrumb_path: /fabric/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Fabric
show_latex: false
feedback_system: Standard
feedback_help_link_url: https://community.fabric.microsoft.com/t5/Real-Time-Intelligence-forums/ct-p/dataactivator
feedback_help_link_type: ask-the-community
feedback_product_url: https://ideas.fabric.microsoft.com/?forum=f2a1a698-503e-ed11-bba2-000d3a8b12b6&category=f4e6a6b3-6748-ed11-bba3-000d3a8b12b6
ms.service: fabric
author: spelluru
ms.author: spelluru
ms.subservice: rti-kql-query
search.app:
- fabric-realtimeanalytics-docs
description: Learn how to use the KQL queryset to query the data in your KQL database in Real-Time Intelligence.
ms.reviewer: tzgitlin
ms.topic: how-to
ai-usage: ai-assisted
ms.date: 2026-06-09T00:00:00.0000000Z
ms.search.form: KQL Queryset
locale: en-us
document_id: efe128ac-f84f-3cbb-b77f-e3d6d8d47057
document_version_independent_id: efe128ac-f84f-3cbb-b77f-e3d6d8d47057
original_content_git_url: https://github.com/MicrosoftDocs/fabric-docs-pr/blob/live/docs/real-time-intelligence/kusto-query-set.md
site_name: Docs
depot_name: MSDN.fabric-docs
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.fabric-docs/{branchName}{pdfName}
asset_id: real-time-intelligence/kusto-query-set
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/real-time-intelligence/kusto-query-set.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/26e1a60c-4ce1-41de-b2d1-e5f3b7e68e6e
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad3bd485-5ca9-4865-afde-baec02586899
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
platformId: 5137f092-b04f-9c4e-7a95-71b58f9d1440
---

# Query data in a KQL queryset - Microsoft Fabric | Microsoft Learn

In this article, you learn how to use a KQL queryset. A KQL queryset lets you run queries, view results, and customize query results for data from different sources, such as an eventhouse or a KQL database.

You can also use a KQL queryset to run cross-service queries against an Azure Monitor [Log Analytics workspace](/en-us/azure/azure-monitor/logs/data-platform-logs) or an [Application Insights resource](/en-us/azure/azure-monitor/app/app-insights-overview).

KQL queryset uses Kusto Query Language (KQL) to create queries and also supports many SQL functions. For more information about the query language, see [Kusto Query Language overview](/en-us/azure/data-explorer/kusto/query/index?context=/fabric/context/context).

## Prerequisites

- A [workspace](../fundamentals/create-workspaces) with a Microsoft Fabric-enabled [capacity](../enterprise/licenses#capacity).
- A [KQL database](create-database) with editing permissions and data, or an Azure Data Explorer [cluster and database](/en-us/azure/data-explorer/create-cluster-and-database) with [AllDatabaseAdmin](/en-us/azure/data-explorer/manage-cluster-permissions#cluster-level-permissions) permissions.

## Select a data source

Queries run in the context of a data source. You can change the associated data source at any time and keep the queries saved in the query editor. You can associate your KQL queryset with multiple data source types, including a KQL database, an Azure Data Explorer cluster, or Azure Monitor.

Select the tab for your data source type.

# [Eventhouse / KQL Database](#tab/kql-database)
1. [Open your KQL queryset](create-query-set#open-an-existing-kql-queryset).
2. In the **Explorer** pane, under the search bar, open the database switcher ![](media/kusto-query-set/database-switcher.png) and select **Add data source** &gt; **Eventhouse / KQL Database**.

    ![Screenshot of the data source menu showing a list of connected data sources.](media/kusto-query-set/expand-database-menu-kql.png)
3. In the **OneLake catalog** window, select a KQL database to connect to your KQL queryset, and then select **Connect**.

    Alternatively, close the **OneLake catalog** window and use the **+ Add data source** menu to connect to a different data source.

# [Azure Data Explorer](#tab/azure-data-explorer-cluster)
1. [Open your KQL queryset](create-query-set#open-an-existing-kql-queryset).
2. In the **Explorer** pane, under the search bar, open the database switcher ![](media/kusto-query-set/database-switcher.png) and select **Add data source** &gt; **Azure Data Explorer**.

    ![Screenshot of the data source menu showing a list of connected databases.](media/kusto-query-set/expand-database-menu-adx.png)
3. Under **Connection URI**, enter the cluster URI.

    To find the connection URI, go to your cluster resource in the [Azure portal](https://portal.azure.com/#home). The connection URI is listed on the **Overview** page.

    ![Screenshot of the connection window showing an Azure Data Explorer cluster URI. The Connect button is highlighted.](media/kusto-query-set/connect-to-cluster.png)

    To add a free sample cluster, specify "help" as the **Connection URI**.

    ![Screenshot of the connection window showing help as the connection URI. The Connect button is highlighted.](media/kusto-query-set/connect-to-help.png)
4. Under **Database**, expand the list and select a data source.
5. Select **Connect**.

# [Azure Monitor](#tab/azure-monitor)
1. [Open your KQL queryset](create-query-set#open-an-existing-kql-queryset).
2. In the **Explorer** pane, under the search bar, open the database switcher ![](media/kusto-query-set/database-switcher.png) and select **Add data source** &gt; **Azure Monitor** &gt; **Application Insights** or **Log Analytics**.

    ![Screenshot of the data source menu showing a list of connected data sources.](media/kusto-query-set/expand-database-menu-azure-monitor.png)
3. Enter your connection parameters or a full connection URI:

    ![Screenshot of the connection window showing an Azure Monitor URI. The Connect cluster button is highlighted.](media/kusto-query-set/connect-to-monitor.png)

    **To enter your connection parameters**:

    1. Enter your **Subscription ID**. Find it in the Azure portal by selecting **Subscriptions** &gt; your subscription name, and then copy the subscription ID from the resource **Overview** page.
    2. Select the **Resource Group** from the drop-down list. Select the resource group that contains your Application Insights or Log Analytics resource.
    3. Enter the Log Analytics **Workspace Name** or the **Application Insights resource name**. Find the name in the Azure portal by opening the resource.
    4. Select the **Application Insights** or **Log Analytics** resource from the drop-down list. This list is populated with the resources in the selected resource group.

    **To enter a full connection URI**:

    1. Select **Connection URI** and enter your connection URI in one of these formats:

    Note

    Replace `<subscription-id>`, `<resource-group-name>`, and `<ai-app-name>` with your own values.

    For Log Analytics: `https://ade.loganalytics.io/subscriptions/<subscription-id>/resourcegroups/<resource-group-name>/providers/microsoft.operationalinsights/workspaces/<workspace-name>`

    For Application Insights: `https://ade.applicationinsights.io/subscriptions/<subscription-id>/resourcegroups/<resource-group-name>/providers/microsoft.insights/components/<ai-app-name>`
4. Select a **Database**. Expand the list and select a database.
5. Select **Connect**.

---

A list of tables associated with this data source appears below the data source name.

## Write a query

Now that you're connected to a data source, you can run queries against it. KQL queryset uses Kusto Query Language (KQL) to query data from any connected data source that you can access. To learn more about KQL, see [Kusto Query Language overview](/en-us/azure/data-explorer/kusto/query/index?context=/fabric/context/context).

The following examples use the public [StormEvents.csv sample file](https://kustosamples.blob.core.windows.net/samplefiles/StormEvents.csv).

1. Write or copy a query in the top pane of the KQL queryset.
2. Select the **Run** button, or press Shift+Enter to run the query.

    The query results appear in the results grid below the query pane. Notice the green check indicating that the query completed successfully, and the time used to compute the query results.

    [![Screenshot of the KQL queryset showing the results of a query. Both the query and the results pane are highlighted.](media/kusto-query-set/query-window.png)](media/kusto-query-set/query-window.png#lightbox)

Note

You can also use Copilot to help you write queries. For more information, see [Copilot for writing queries in KQL queryset](copilot-writing-queries).

## Interact with data sources

The data source explorer lets you switch between the data sources connected to the current queryset tab.

At the top of the data source explorer pane, under **Explorer**, you can use the search bar to search for a specific data source. You can also use the database switcher below the search bar to expand the data source connections menu. Select the data source that you want to use. If you didn't rename the tab earlier, it's automatically named after the data source.

[![Screenshot showing how to switch between data sources using the search bar and Database switcher in the Explorer pane.](media/kusto-query-set/explorer-pane-switch-db.png)](media/kusto-query-set/explorer-pane-switch-db.png#lightbox)

The data source explorer pane has two sections. The upper section lists all items in the data source, and the lower section shows all available data sources in the queryset.

### View items in the data source

The upper section of the data source explorer shows all items in the data source that you're using.

- Tables
- Materialized Views
- Shortcuts
- Functions

Select the arrow **&gt;** to the left of the item that you want to expand. You can drill down to show more details by selecting the arrow **&gt;** to the left of items in subsequent list levels. For example, under **Tables**, select the arrow **&gt;** to the left of a table to show the list of columns in that table.

To open the action menu, hover over an item in the expanded list and select the **More menu** [**...**]. The menu includes the following options:

- Refresh database
- View data profile
- Explore data
- Insert: to create and copy a script
- Get data: to add a new data source
- Create a dashboard
- Delete table

Different actions are available for different item types.

[![Screenshot showing the explorer pane, how to expand the list of items in your data source and where to find the More actions menu.](media/kusto-query-set/explorer-pane-more-actions.png)](media/kusto-query-set/explorer-pane-more-actions.png#lightbox)

### Browse available data sources

The lower section of the data source explorer shows all the available data sources that you add to the queryset.

To open the action menu, hover over the data source name and select the **More menu** [**...**]. The menu includes the following options:

- Refresh database
- Use this database: switch to use this data source in the current tab
- Query in a new tab: open this data source in a new tab in the queryset
- Remove source: removes all the databases in that data source
- Remove database: removes the selected database only
- Open in KQL database: opens this data source in a KQL database.

[![Screenshot showing the lower section of the Explorer pane where all data sources that were added to your queryset are listed.](media/kusto-query-set/explorer-pane-lower-section.png)](media/kusto-query-set/explorer-pane-lower-section.png#lightbox)

## Manage queryset tabs

Within a KQL queryset, you can create multiple tabs. Each tab can be associated with a different KQL database. This setup lets you save queries for later use or share them with others to collaborate on data exploration. You can also change the KQL database associated with any tab, which lets you run the same query on data in different databases.

You can manage your tabs in the following ways:

- **Change the existing data source connection**: Under **Explorer** and the search bar, use the database switcher to expand the data source connections menu.
- **Rename a tab**: Next to the tab name, select the **pencil icon**.
- **Add a new tab**: On the right of the existing tabs in the command bar, select the plus **+**. Different tabs can be connected to different data sources.
- **More actions**: On the right side of the command bar, use the tab menu to manage multiple tabs in your queryset.
- **Change tab positions**: Use drag and drop gestures.

[![Screenshot of the multiple tabs menu for managing multiple tabs in the KQL queryset.](media/kusto-query-set/multiple-tabs-menu-1.png)](media/kusto-query-set/multiple-tabs-menu-1.png#lightbox)

## Delete a KQL queryset

To delete your KQL queryset:

1. Select the workspace that contains your KQL queryset.
2. Hover over the KQL queryset that you want to delete. Select **More** [**...**], and then select **Delete**.

    [![Screenshot of Microsoft Fabric workspace showing how to delete a KQL queryset.](media/kusto-query-set/clean-up-query-set.png)](media/kusto-query-set/clean-up-query-set.png#lightbox)