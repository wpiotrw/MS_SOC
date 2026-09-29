---
layout: Conceptual
title: Pipeline Overview - Microsoft Fabric | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/fabric/data-factory/pipeline-overview
breadcrumb_path: /fabric/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Fabric
show_latex: false
feedback_system: Standard
feedback_help_link_url: https://community.fabric.microsoft.com/datafactory
feedback_help_link_type: ask-the-community
feedback_product_url: https://ideas.fabric.microsoft.com/?forum=ea587140-44f9-ed11-8849-000d3a4ef41d
ms.service: fabric
author: whhender
ms.author: whhender
ms.subservice: data-factory
search.app:
- fabric-datafactory-docs
description: Learn about pipelines in Microsoft Fabric Data Factory, including activities, triggers, control flow, and how to use them for data processing workflows.
ms.reviewer: makromer
ms.topic: concept-article
ms.custom: fabric-data-factory
ms.date: 2025-08-01T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: 309549d3-addf-1829-3080-1f99f98e454a
document_version_independent_id: 309549d3-addf-1829-3080-1f99f98e454a
original_content_git_url: https://github.com/MicrosoftDocs/fabric-docs-pr/blob/live/docs/data-factory/pipeline-overview.md
site_name: Docs
depot_name: MSDN.fabric-docs
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.fabric-docs/{branchName}{pdfName}
asset_id: data-factory/pipeline-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/data-factory/pipeline-overview.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e7cd09c2-9e9a-4f0d-b160-c15783f45b1f
- https://authoring-docs-microsoft.poolparty.biz/devrel/655f39c4-21c5-49d3-8367-a1f9c1a0b930
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1d337399-0ca4-4b4c-acef-8df37820e018
- https://authoring-docs-microsoft.poolparty.biz/devrel/d30b39f7-a405-488d-84ef-d6d5296ad372
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
platformId: 296c133c-3f3e-8daf-278b-d66d5a4bb930
---

# Pipeline Overview - Microsoft Fabric | Microsoft Learn

Pipelines in Microsoft Fabric Data Factory help you orchestrate and automate your data workflows. A pipeline is a logical grouping of activities that together perform a task. For example, a pipeline could contain a set of activities that ingest and clean log data, and then kick off a data flow to analyze the log data.

The pipeline allows you to manage the activities as a set instead of each one individually. You deploy and schedule the pipeline instead of the activities independently.

## When to use pipelines

Pipelines solve common data challenges by automating repetitive tasks and ensuring consistent data processing.

Let's say you're a retail company that needs to process daily sales data from multiple stores. Each day, you need to:

1. **Collect data** from point-of-sale systems, online orders, and inventory databases
2. **Validate and clean** the data to ensure accuracy
3. **Transform** the data by calculating daily totals, applying business rules, and enriching with customer information
4. **Load** the processed data into your data warehouse for reporting
5. **Notify** your business intelligence team when the data is ready

A pipeline automates this entire workflow. It runs on schedule, handles errors gracefully, and provides visibility into each step. You get consistent and timely data processing without manual intervention.

## Key pipeline components

Pipelines consist of several key components that work together to create powerful data workflows. The main components include activities that perform the work and add logic to your pipeline, schedules or triggers that determine when pipelines run, and parameters that make your pipelines flexible and reusable.

### Activities

Activities are the building blocks of your pipeline. Each activity performs a specific task, and there are three main types of activities:

- [**Data movement activities**](activity-overview#data-movement-activities): Copy data between different sources and destinations
- [**Data transformation activities**](activity-overview#data-transformation-activities): Clean, aggregate, and reshape your data
- [**Control flow activities**](activity-overview#control-flow-activities): Add logic like conditions, loops, and error handling

You can chain activities together to create complex workflows. When one activity completes, it can trigger the next activity based on success, failure, or completion status.

For a full list of available activities and more information, see [the activity overview](activity-overview).

### Pipeline runs and scheduling

A pipeline run happens when a pipeline executes. During a run, all the activities in your pipeline are processed and completed. Each pipeline run gets its own unique run ID that you can use for tracking and monitoring.

You can start pipeline runs in three ways:

- **On-demand runs**: Select **Run** in the pipeline editor to trigger an immediate run. You'll need to save any changes before the pipeline starts.

    ![Screenshot showing where to select Run on the Home tab.](media/pipeline-runs/trigger-pipeline-run.png)
- **Scheduled runs**: Set up automatic runs based on time and frequency. When you create a schedule, you specify start and end dates, frequency, and time zone.

    ![Screenshot showing where to select Schedule on the Home tab.](media/pipeline-runs/schedule-pipeline-run.png)
- **Event-based runs**: Use event triggers to start your pipeline when specific events occur, such as new files arriving in a data lake or changes in a database.

    ![Screenshot showing where to select Trigger to add event-based run triggers on the home tab.](media/pipeline-runs/event-based-run.png)

For more information, see [Run, schedule, or trigger a pipeline](pipeline-runs).

### Parameters and variables

Parameters make your pipelines flexible. You can pass different values when you run the pipeline, allowing the same pipeline to process different datasets or use different configurations.

Variables store temporary values during pipeline execution. You can use them to pass data between activities or make decisions based on runtime conditions.

For more information, see [How to use parameters, expressions, and functions in pipelines](parameters).

## Pipeline monitoring and management

Fabric provides comprehensive monitoring for your pipelines:

- **Real-time monitoring**: Watch your pipeline progress as it runs, with visual indicators for each activity's status
- **Run history**: Review past executions to identify patterns and troubleshoot issues
- **Performance metrics**: Analyze execution times and resource usage to optimize your pipelines
- **Audit trail**: Track who ran which pipelines when, with detailed logs of start times, end times, activity duration, error messages, and data lineage

For more information, see [Monitor pipeline runs](monitor-pipeline-runs).

## Best practices

When designing pipelines, consider these recommendations:

- **Start simple**: Begin with basic data movement and gradually add complexity
- **Use parameters**: Make your pipelines reusable by parameterizing connections and file paths
- **Handle errors**: Plan for failures with retry logic and alternative processing paths
- **Monitor performance**: Regularly review execution times and optimize slow-running activities
- **Test thoroughly**: Validate your pipelines with sample data before processing production workloads