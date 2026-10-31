---
layout: Conceptual
title: Monitor Data Map population in Microsoft Purview Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-scan-run-monitor-population
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
description: This guide describes how to monitor Microsoft Purview Data Map population, including the scan runs and links.
locale: en-us
document_id: cdb030f4-95fd-42f4-1869-0d866a59696a
document_version_independent_id: cdb030f4-95fd-42f4-1869-0d866a59696a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-scan-run-monitor-population.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-scan-run-monitor-population
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-scan-run-monitor-population.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 5a84315a-9122-dd34-c621-a59de9e777bc
---

# Monitor Data Map population in Microsoft Purview Data Map | Microsoft Learn

In Microsoft Purview, you can scan various types of data sources and view the scan status over time. You can also connect other services with Microsoft Purview and view the trends of the ingested assets and relationships. This article outlines how to monitor and get a bird's eye view of the Purview Data Map population.

## Monitor scan runs

1. Open your Microsoft Purview account and select **Data Map** -&gt; **Monitoring**. You need to have the **Data source admin** role on any collection to access this page. You can see the scan runs that belong to the collections on which you have data source admin privilege.
2. The high-level KPIs show total scan runs within a period. The default time period is the last 30 days. You can also choose to select the last seven days. Based on the time filter you select, you can see the distribution of succeeded, completed with exceptions, failed, canceled, and in progress scan runs by week or by the day in the graph. It's the scan run end-to-end status including the discovery and ingestion phases. For more information about the status details, see the scan run details section.

    [![View scan runs over time](media/how-to-monitor-scan-runs/monitor-scan-runs.png)](media/how-to-monitor-scan-runs/monitor-scan-runs.png#lightbox)
3. At the bottom of the graph, there's a **View more** link for you to explore further. The link opens the **Scan status** page. Here you can see a scan name and the number of times it has status of succeeded, completed with exceptions, failed, or canceled in the time period. You can also filter the list by source types.

    [![View scan status in details](media/how-to-monitor-scan-runs/view-scan-status.png)](media/how-to-monitor-scan-runs/view-scan-status.png#lightbox)
4. You can explore a specific scan further by selecting the **scan name**. It connects you to the scan history page, where you can find the list of scan runs with more execution details.

    [![View scan history for a given scan](media/how-to-monitor-scan-runs/view-scan-history.png)](media/how-to-monitor-scan-runs/view-scan-history.png#lightbox)
5. Select **run ID** to check more about the scan run details.

### Known limitations

Currently, this monitoring experience doesn't include the following information. You can check the corresponding scan run details.

- Lineage extraction scan runs for Azure SQL Database aren't covered.
- For scans of Azure Synapse Analytics workspace, Azure subscription/resource group, and Amazon Web Services (AWS) account, it only captures the parent scan run's status/count but not child scan runs' per resource.

## Scan run details

You can view the scan run history for a given scan from different places:

- Go to **Data Map** -&gt; **Monitoring** as described in the Monitor scan runs section.
- Go to **Data Map** -&gt; **Sources** -&gt; select the desired data source -&gt; see **Scans**, **Recent scans**, or **Recent failed scans**.
- Go to **Data Map** -&gt; **Collections** -&gt; select the desired collection -&gt; **Scans** -&gt; select the scan name that you want to view.

The retention of the scan run history is 90 days.

Select **run ID** to check more about the scan run details:

[![Screenshot of view scan run execution details.](media/how-to-monitor-scan-runs/monitor-scan-run-details.png)](media/how-to-monitor-scan-runs/monitor-scan-run-details.png#lightbox)

- The section on top provides an overview of the scan run, including the following information:

    - **Run ID**: A GUID used to identify this particular scan run.
    - **Scan type**: Manual or scheduled scan.
    - **Run type**: Full or incremental scan.
    - **Scan rule set**: The scan rule set used in the run, if applicable.
    - **Scan run status**: Overall scan status. It combines the metadata discovery and ingestion phases' status.
    - **Scan run duration**: The end-to-end execution duration and the start/end time.
- **Metadata discovery** section summarizes the metrics for discovery phase that Purview connects to the source, extracts the metadata/lineage and classifies the data.

    - **Discovery status**:

        | Status | Description |
        | --- | --- |
        | Completed | The metadata discovery succeeds. |
        | Completed with exceptions | The metadata discovery completes, while some underlying operation fails that might cause asset, metadata, or classification missing in the scan result. You can view details in the exception logs. |
        | Failed | The metadata discovery fails. You can check the error details by selecting the "More info" link next to it. |
        | Canceled | The scan run is canceled by user. |
        | In Progress | The metadata discovery is running in progress. |
        | Queued | The metadata discovery is waiting for available integration runtime resource.If you use self-hosted integration runtime, note each node can run many concurrent scans at the same time depending on your machine specification (CPU and memory). More scans are in Queued status. |
        | Throttled | The metadata discovery is being throttled. It means this Microsoft Purview account at the moment has more ongoing scan runs than the allowed max concurrent count. Learn more about the limit [here](classic-how-to-manage-quotas). This particular scan run is waiting and will start once your other ongoing scans finish. |

        The scan run isn't charged during "Throttled" or "Queued" status.

        - **Assets discovered**: The number of assets enumerated from the source. For both full and incremental scans, it includes all assets in the configured scope, regardless of whether they're existing assets or newly created or updated assets since the last scan run. For incremental scan, Microsoft Purview extracts detailed metadata only for newly created or updated assets.
    - **Assets classified**: The number of assets sampled to classify the data, regardless of whether the assets have any matching classification or not. It's a subset of the discovered assets based on the [sampling mechanism](data-map-data-sources#sampling-data-for-classification). For incremental scan, only newly created or updated assets might be selected for classification.
    - **Duration**: The discovery phase duration and the start/end time.
- **Metadata ingestion** section summarizes the metrics for ingestion phase that populates Data Map with the identified metadata and relationship.

    - **Ingestion status**:

        | Status | Description |
        | --- | --- |
        | Completed | All of the assets and relationships are ingested into Data Map successfully. |
        | Completed with exceptions (previous "Partially completed") | Partial of the assets and relationships are ingested into Data Map successfully, while some fail. You can view details in the exception logs. |
        | Failed | The ingestion phase fails. |
        | Canceled | The scan run is canceled by user, thus the ingestion is canceled along. |
        | In Progress | The ingestion is running in progress. |
        | Queued | The ingestion is waiting for available service resource or waiting for scan to discover metadata. |
    - **Assets ingested**: The number of assets ingested into Data Map. For incremental scan, it only includes the newly created or updated assets, in which case might be less than the "assets discovered" count. When scanning file-based source, it's the raw assets count before resource set aggregation.
    - **Relationships ingested**: The number of relationships ingested into Data Map. It includes lineage and other relationships like foreign key relationships.
    - **Duration**: The ingestion duration, and the start and end times.

## View the exception log (preview)

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

When some assets or relationships fail to be discovered from the source or fail to ingest into Data Map during a scan run, the scan status shows **completed with exceptions**. You can view the exception log by following these steps:

1. Select the scan.
2. Select the run ID of a scan with failures or exceptions.
3. Select **Download log** in the scan run details panel. It provides you with the exception log files that capture the details of the failures.

### Discovery phase log

The following table shows the schema of a discovery phase log file.

| Column | Description |
| --- | --- |
| TimeStamp | The UTC timestamp when the discovery operation happens. |
| ErrorCode | Error code of the exception. |
| OperationName | It contains the following values:- **Enumerate**: Indicates the operation of enumerating the child objects under a given scope; for example, list the folders/files under a container, list the tables under a database. When there's a failure, the operation item's child objects aren't included in the scan result.- **GetMetadata**: Indicates the operation of extracting the metadata for an object, such as a table or file. When there's a failure, the asset of the operation item might not contain full metadata. - **SampleResourceSet**: Indicates the operation of sampling the latest file matching the resource set pattern when you scan file-based data sources. When there's a failure, the resource set that the operation item belongs to might miss classification or schema.- **ReadData**: Indicates the operation of retrieving sample data from the source. When there's a failure, the operation item isn't classified. If it's a file-based source, it might also miss schema.- **Classify**: Indicates the operation of applying the classifications. When there's a failure, the operation item might miss classification.- **GenerateAsset**: Indicates the operation of converting the discovered metadata into Purview asset. When there's a failure, usually due to system error, the asset of the operation item doesn't show up in Data Map at last. |
| OperationItem | Identifier for the failed asset or relationship, usually uses the fully qualified name. |
| Message | More information on which asset or relationship failed to discover and the reason for the failure. |

Known limitations:

- The discovery phase log is supported when you use Azure integration runtime or Managed Virtual Network integration runtime for scan.
- The discovery phase log is supported when you scan Azure or Power BI data sources.
- Currently, it might not capture all the exceptions that happen during a scan run.

### Ingestion phase log

The following table shows the schema of an ingestion phase log file.

| Column | Description |
| --- | --- |
| TimeStamp | The UTC timestamp when the ingestion operation happens. |
| ErrorCode | Error code of the exception. |
| OperationItem | Identifier for the failed asset or relationship, usually uses the fully qualified name. |
| Message | More information on which asset or relationship failed to ingest and the reason for the failure. If there's an ingestion failure for a resource set, it might apply to multiple assets that match the same naming pattern, and the message includes the impacted count. |

## Monitor links

You can connect other services with Microsoft Purview to establish a "link", which makes the metadata and lineage of that service's assets available to Microsoft Purview. Currently, link is supported for [Azure Data Factory](data-map-lineage-azure-data-factory) and [Azure Synapse Analytics](data-map-lineage-azure-synapse-analytics).

To monitor the assets and relationship ingested over the links:

1. Go to your Microsoft Purview account -&gt; open **Microsoft Purview governance portal** -&gt; **Data Map** -&gt; **Monitoring** -&gt; **Links**. You need to have **Data source admin** role on any collection to access the Monitoring tab. And you can see the results that belong to the collections on which you have data source admin privilege. Permission on root collection is needed to monitor Azure Data Factory and Azure Synapse Analytics links.
2. You can see the high-level KPIs including total number of sources, number of ingested assets and relationship (lineage), followed by trending charts over time. You can apply more filters on the following to narrow down the results:

    - Source type
    - Source name
    - Date range: Default is 30 days. You can also choose last seven days or a custom date range. The retention is 45 days.

    The metrics are reported till the date time shown at the top right corner. And the aggregation happens hourly.

    [![Screenshot of view link results.](media/how-to-monitor-scan-runs/monitor-links.png)](media/how-to-monitor-scan-runs/monitor-links.png#lightbox)
3. At the bottom of the graph, there's a **View more** link for you to explore further. In the **Link status** page, you can see a list of source names along with the source type, assets ingested, relationship ingested and the last run date time. The filters in the previous page are carried over, and you can further filter the list by source type, source name, and date range.

    [![Screenshot of view link results by source.](media/how-to-monitor-scan-runs/monitor-links-drilldown.png)](media/how-to-monitor-scan-runs/monitor-links-drilldown.png#lightbox)
4. You can drill down to each source to see the next level details by clicking the source name. For example, for Azure Data Factory, it shows how each pipeline activity reports the assets and relationship to Microsoft Purview, with the name in the format of `<pipeline_name>/<activity_name>`.

    [![Screenshot of view link results by source's sub-artifacts.](media/how-to-monitor-scan-runs/monitor-links-drilldown-second-layer.png)](media/how-to-monitor-scan-runs/monitor-links-drilldown-second-layer.png#lightbox)

### Known limitations

- For Azure Data Factory and Azure Synapse Analytics, currently this link monitoring captures the assets and relationship generated from copy activity, but not data flow and SSIS activities.
- The aggregation and date filter are in UTC time.

## Scans no longer run

If your Microsoft Purview scan used to run successfully but now fails, check these things:

1. Check the error message for failure details.
2. Did you change or rotate credentials to your resource? If so, update your scan with the correct credentials.
3. Is an [Azure Policy](/en-us/azure/governance/policy/overview) preventing **updates to Storage accounts**? If so, follow the [Microsoft Purview exception tag guide](data-gov-azure-policy-exclusion) to create an exception for Purview accounts.
4. Are you using a self-hosted integration runtime? Check that it's up to date with the latest software and that it's connected to your network.