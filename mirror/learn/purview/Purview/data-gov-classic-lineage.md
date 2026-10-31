---
layout: Conceptual
title: Data lineage in classic Microsoft Purview Data Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-classic-lineage
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: nidought
ms.date: 2025-02-14T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn about the concepts for data lineage in Microsoft Purview using the classic Data Catalog.
locale: en-us
document_id: 08a5245a-41e3-2d7d-92c4-8c129eca64db
document_version_independent_id: 08a5245a-41e3-2d7d-92c4-8c129eca64db
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-classic-lineage.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-classic-lineage
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-classic-lineage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/3f837592-9b7c-422c-82fa-3523042264d7
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/f37b967c-efb8-47e1-9b0d-0ab7670e3db4
platformId: 81a63622-af25-0de4-100f-6169e5cf65a3
---

# Data lineage in classic Microsoft Purview Data Catalog | Microsoft Learn

This article provides an overview of data lineage in the classic Microsoft Purview Data Catalog. It also details how data systems can integrate with the catalog to capture lineage of data. Microsoft Purview can capture lineage for data in different parts of your organization's data estate, and at different levels of preparation including:

- Raw data staged from various platforms
- Transformed and prepared data
- Data used by visualization platforms

For data lineage in the Unified Catalog, see how to [view data asset details](unified-catalog-data-products-search#view-data-asset-details) and lineage information.

## Use cases

Data lineage is broadly understood as the lifecycle that spans the data’s origin, and where it moves over time across the data estate. It's used for different kinds of backwards-looking scenarios such as troubleshooting, tracing root cause in data pipelines and debugging. Lineage is also used for data quality analysis, compliance and “what if” scenarios often referred to as impact analysis. Lineage is represented visually to show data moving from source to destination including how the data was transformed. Given the complexity of most enterprise data environments, these views can be hard to understand without doing some consolidation or masking of peripheral data points.

## Lineage experience in the classic Data Catalog

The catalog connects with other data processing, storage, and analytics systems to extract lineage information. The information is combined to represent a generic, scenario-specific lineage experience in the catalog.

[![end-end lineage showing data copied from blob store all the way to Power BI dashboard](media/concept-lineage/lineage-end-end-inline.png)](media/concept-lineage/lineage-end-end.png#lightbox)

Your data estate might include systems doing data extraction, transformation (ETL/ELT systems), analytics, and visualization systems. Each of the systems captures rich static and operational metadata that describes the state and quality of the data within the systems boundary. The goal of lineage in a data catalog is to extract the movement, transformation, and operational metadata from each data system at the lowest grain possible.

The following example is a typical use case of data moving across multiple systems, where a catalog would connect to each of the systems for lineage.

- Data Factory copies data from on-prem/raw zone to a landing zone in the cloud.
- Data processing systems like Synapse, Databricks would process and transform data from landing zone to Curated zone using notebooks.
- Further processing of data into analytical models for optimal query performance and aggregation.
- Data visualization systems will consume the datasets and process through their meta model to create a BI Dashboard, ML experiments and so on.

## Lineage granularity

The following section covers the details about the granularity of which the lineage information is gathered by Microsoft Purview. This granularity can vary based on the data systems supported in Microsoft Purview.

### Entity level lineage: Sources &gt; Process &gt; Targets

- Lineage is represented as a graph, typically it contains source and target entities in Data storage systems that are connected by a process invoked by a compute system.
- Data systems connect to the catalog to generate and report a unique object referencing the physical object of the underlying data system for example: SQL Stored procedure, notebooks, and so on.
- High fidelity lineage with other metadata like ownership is captured to show the lineage in a human readable format for source & target entities. for example: lineage at a hive table level instead of partitions or file level.

### Column or attribute level lineage

Identify attributes of a source entity that is used to create or derive attributes in the target entity. The name of the source attribute could be retained or renamed in a target. Systems like Azure Data Factory (ADF) can do a one-one copy from on-premises environment to the cloud. For example: `Table1/ColumnA -> Table2/ColumnA`.

### Process execution status

To support root cause analysis and data quality scenarios, we capture the execution status of the jobs in data processing systems. This requirement has nothing to do with replacing the monitoring capabilities of other data processing systems, neither the goal is to replace them.

## Summary

Lineage is a critical feature to support quality, trust, and audit scenarios. The goal of a data catalog is to build a robust framework where all the data systems within your environment can naturally connect and report lineage. Once the metadata is available, the catalog can bring together the metadata provided by data systems to power data governance use cases.