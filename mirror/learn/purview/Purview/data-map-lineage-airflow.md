---
layout: Conceptual
title: Lineage from Airflow into Microsoft Purview (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-lineage-airflow
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
description: This article describes how to get lineage from Airflow into Microsoft Purview.
ms.custom: sfi-ropc-nochange
locale: en-us
document_id: 3cf9d46c-e7aa-3740-06b6-88e65bfe649e
document_version_independent_id: 3cf9d46c-e7aa-3740-06b6-88e65bfe649e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-lineage-airflow.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-lineage-airflow
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-lineage-airflow.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/f0234678-3067-4edc-abf7-8142d54bb7d2
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/b0f4f6b9-28ed-4892-be4e-517310289c68
platformId: 7d9842e2-d3d7-5153-fdb7-97ee144ea6a2
---

# Lineage from Airflow into Microsoft Purview (preview) | Microsoft Learn

[Airflow](https://airflow.apache.org/) is an open-source workflow automation and scheduling platform that can be used to author and manage data pipelines. Microsoft Purview supports collecting Airflow lineage by integrating with [OpenLineage](https://openlineage.io/), an open framework for data lineage collection and analysis. Learn about how Airflow works with OpenLineage from [here](https://openlineage.io/docs/integrations/airflow/).

Enabling OpenLineage in Airflow automatically tracks metadata and lineage about jobs and datasets as DAGs execute. The information is sent to an Azure Event Hubs that you configure. Microsoft Purview subscribes to the events, parse them and ingest into the data map.

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

## Supported capabilities

The supported Airflow versions are 1.10+ and 2.0-2.7.

Microsoft Purview supports metadata and lineage collection when the following types of data sources are used in Airflow:

- Amazon RDS for PostgreSQL
- Azure Database for PostgreSQL
- Google BigQuery
- PostgreSQL
- Snowflake

The following Airflow metadata are captured along:

- Airflow workspace
- Airflow DAG
- Airflow task

Lineage is collected into Microsoft Purview upon successful DAG runs in an event-based manner.

### Known limitations

- Column level lineage is currently not supported. The schema of the data assets is captured.
- If database views are referenced in the tasks, they're currently captured as table assets.
- All the metadata are ingested into Microsoft Purview root collection. The assets already existed in the data map are preserved in the configured collection.

## How to bring Airflow lineage into Microsoft Purview

As a prerequisite, you need a running Airflow instance.

To get lineage from Airflow into Microsoft Purview, you need to:

1. Set up an Azure Event Hubs
2. Configure Event Hubs to publish messages to Microsoft Purview
3. Configure your Airflow with OpenLineage
4. Run Airflow jobs and view the assets/lineage

### Set up Azure Event Hubs

Set up an Azure Event Hubs as the receiver of the metadata and lineage tracked by OpenLineage in Airflow.

1. [Create an Azure Event Hubs namespace](/en-us/azure/event-hubs/event-hubs-create#create-an-event-hubs-namespace).
2. [Create an event hub](/en-us/azure/event-hubs/event-hubs-create#create-an-event-hub). Name your event hub as “**microsoft\_internal\_openlineage**”.

    [![Screenshot of create an new event hub in Azure Event Hubs](media/how-to-lineage-airflow/create-event-hub.png)](media/how-to-lineage-airflow/create-event-hub.png#lightbox)
3. Go to your “microsoft\_internal\_openlineage” event hubs -&gt; **Access control (IAM)** -&gt; **Add role assignment**, assign “**Azure Event Hubs Data Receiver**” role to your Microsoft Purview account’s managed identity. For detailed steps, see [Assign Azure roles using the Azure portal](/en-us/azure/role-based-access-control/role-assignments-portal).

### Configure Event Hubs to publish messages to Microsoft Purview

Microsoft Purview supports consuming and pushing events from/to your own Event Hubs. Follow this doc to configure Event Hubs for Microsoft Purview: [Configure Event Hubs with Microsoft Purview to send and receive Atlas Kafka topics messages](data-map-kafa-notifications).

In summary:

- Go to your Microsoft Purview account -&gt; Managed resources tab, disable the managed Event Hubs namespace.
- Go to Kafka configuration tab -&gt; **+ Add configuration** -&gt; **Hook configuration**, input a name, and select the Event Hubs namespace and Event Hubs you created in previous step.

    [![Screenshot of configure Event Hubs to publish messages to Microsoft Purview](media/how-to-lineage-airflow/kafka-config.png)](media/how-to-lineage-airflow/kafka-config.png#lightbox)

### Configure your Airflow with OpenLineage

**Installation:**

To download and install the latest ‘openlineage-airflow’ library, update the ‘requirements.txt’ file of your running Airflow instance with:

```
openlineage-airflow
```

Note

The Airflow version and the openlineage-airflow version need to match. For example, when you use Airflow 2.7.1, you can use openlineage-airflow version 1.1.0 or 1.2.0. You can view matching versions on [this website](https://pypi.org/project/openlineage-airflow/#history).

**Configuration:**

Next, configure your Azure Event Hubs instance as the target to which OpenLineage sends the events.

1. Create an ‘openlineage.yml’ file under your Airflow root path. The content of the file is as below:

    ```yml
    transport:
      type: "kafka"
      config:
        bootstrap.servers: "{EVENTHUB_SERVER}:9093"
        security.protocol: "SASL_SSL"
        sasl.mechanism: "PLAIN"
        sasl.username: "$ConnectionString"
        sasl.password: "{PASSWORD}"
        client.id: "airflow-client"
      topic: "microsoft_internal_openlineage"
      flash: True
    ```

    Replace the two place-holders with values:

    - Get the `{EVENTHUB_SERVER}` from your Event Hubs namespace -&gt; **Host name**:

        [![Screenshot of Get host name from Event Hubs namespace](media/how-to-lineage-airflow/get-event-hub-host-name.png)](media/how-to-lineage-airflow/get-event-hub-host-name.png#lightbox)
    - Get the `{PASSWORD}` from your Event Hubs namespace -&gt; **Shared access policies** -&gt; **Connection string - primary key** or **Connection string - secondary key**:

        [![Screenshot of Get event hub connection string key](media/how-to-lineage-airflow/get-event-hub-connection-string.png)](media/how-to-lineage-airflow/get-event-hub-connection-string.png#lightbox)
2. Restart your Airflow server.

### Run Airflow jobs and view the assets/lineage

You can now run your Airflow jobs, then go to Microsoft Purview Governance portal to browse/search/view assets. The assets should show up shortly after a successful DAG run.

Browse Airflow assets:

![Screenshot of Browse Unified Catalog by source type](media/how-to-lineage-airflow/browse-by-source-type.png)

![Screenshot of Browse Airflow source to see details](media/how-to-lineage-airflow/browse-airflow.png)

View Airflow task asset details with lineage:

[![Screenshot of View Airflow lineage details on Airflow task asset](media/how-to-lineage-airflow/view-airflow-lineage.png)](media/how-to-lineage-airflow/view-airflow-lineage.png#lightbox)

## Troubleshooting tips

If you run the Airflow job but don’t see the corresponding assets/lineage shown up in Microsoft Purview:

- Check if your Airflow use case is supported by Microsoft Purview. Refer to the supported capabilities section.
- Go to your Event Hubs instance to check if any incoming requests and messages. If no, double check your OpenLineage configuration in Airflow.