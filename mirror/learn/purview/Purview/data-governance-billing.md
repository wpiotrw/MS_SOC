---
layout: Conceptual
title: Billing in Microsoft Purview Data Governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-billing
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: jife
ms.date: 2026-04-24T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how billing works for Microsoft Purview data governance solutions, including Unified Catalog.
locale: en-us
document_id: e14bfa35-5e2a-d4c7-a159-176610b35b56
document_version_independent_id: e14bfa35-5e2a-d4c7-a159-176610b35b56
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-billing.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-billing
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-billing.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: c92b8549-3c9d-a8df-c9ab-b06166516c89
---

# Billing in Microsoft Purview Data Governance | Microsoft Learn

Microsoft Purview data governance solutions include [Microsoft Purview Unified Catalog](unified-catalog) and [Microsoft Purview Data Map](data-map). For Unified Catalog, you pay for governed assets and data health management capabilities. The billing for these components operates on a pay-as-you-go model. There's no cost to scan assets into Microsoft Purview Data Map when certain billing conditions are met. This article explains how to prepare for billing and how data governance capabilities are charged.

For complete pricing information, with pricing calculators, see the [Microsoft Purview pricing](https://azure.microsoft.com/pricing/details/purview/) site.

To learn more about the pay-as-you-go billing model for Microsoft Purview, including the consent experience, see [Microsoft Purview billing models](purview-billing-models).

## Prerequisites

To use Microsoft Purview pay-as-you go, you need:

- An [Azure subscription](/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/initial-subscriptions) in the same tenant as Microsoft Purview.
- An [Azure resource group](/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal) in that subscription.

If you already have these resources for other purposes, you can also use them with Microsoft Purview.

## Billing setup

To use the data governance experience in the Microsoft Purview portal, you need to be set up for Microsoft Purview pay-as-you-go billing. Pay-as-you-go took effect for Microsoft Purview on January 6, 2025. For details about required roles and the setup experience, visit one of the resources below based on your situation:

- If you're a new data governance customer using Unified Catalog in the Microsoft Purview portal, see [Enable Microsoft Purview pay-as-you-go features for new customers](purview-payg-subscription-based-enablement).
- If you're an existing Azure Purview customer using the [classic data governance pricing model](data-gov-classic-pricing), see [Consent to use pay-as-you-go capabilities](purview-payg-consent-based-enablement).

If you don't consent to the pay-as-you-go pricing model, you can still use the classic Data Catalog in the [classic data Microsoft Purview portal](use-microsoft-purview-governance-portal).

Your Data Map assets remain intact regardless of whether you consent to the new billing experience for Unified Catalog.

## Pricing components

Two pricing components support data governance in Microsoft Purview. Unified Catalog has two meters that run based on:

1. Number of unique governed assets per day; see Unified Catalog billing.
2. Data governance processing units per run; see Data health management.

## Unified Catalog billing

A single meter starts for an organization when users begin to govern unique data assets. A unique data asset can be a table or a view linked to a governance concept, such as a [data product](unified-catalog-data-products) or a [critical data element](unified-catalog-critical-data-elements).

Assets that are collected in Data Map but aren't linked to a governance concept don't count as governed assets.

Tip

- To view specific pricing information and a calculator for your region, see the **Data Governance** tab on the [Microsoft Purview pricing](https://azure.microsoft.com/pricing/details/purview/) site.
- For an admin view into your organization's consumption across governance domains, see [Usage monitoring (preview)](data-governance-admin-experience#usage-monitoring-preview).

### What are governed assets and how are you billed

In Unified Catalog, when you actively manage and curate data assets, you turn them into **governed assets**. A governed asset is a data asset that you attach or associate to governance concepts, such as data products, critical data elements, glossary terms, and data quality. If you don't associate a technical asset to a governance concept, it isn't a governed asset.

For example, if you have a Microsoft SQL Server with 200 tables, and only 20 tables are in the gold tier of the medallion structure, you created 20 data products with each data product linked to a table. Every day, the Unified Catalog billing system counts the tables that are associated to the data product. Since only 20 tables link to data products, only 20 tables are governed assets, instead of the full 200 tables.

Over time, you might want to attach a [glossary term](unified-catalog-glossary-terms) and a policy to the data product, which then also apply to the governed assets. In each case, a governed asset is still a single governed asset regardless of how many concepts you attach to the asset.

- **Example 1:** A SQL table is referenced within a data product. You use the same SQL table in five other data products. The SQL table is counted one time only, once a day.
- **Example 2:** You create 50 governance domains and data products, but don't attach any tables, files, reports, or dashboards. In this case, you aren't charged for any governed assets.
- **Example 3:** You accidentally attach a server to the data product. Microsoft Purview counts just the server as a single asset, not all the children tables within the server.

View pricing information on the **Data Governance** tab on the [Microsoft Purview pricing](https://azure.microsoft.com/pricing/details/purview/) site.

## Data health management usage

The Microsoft Purview Data Governance Enterprise Data Management meter starts when you run [data quality and health management](unified-catalog-data-health-management) actions on your governed data estate. You pay for data management usage based on the data governance processing unit (DGPU) pay-as-you-go meters. A DGPU is the amount of service performance consumed for 60 minutes and comes in three different performance options: Basic, Standard, and Advanced. The Basic SKU option is the default performance option until you select a higher option.

View pricing information at each performance level on the **Data Governance** tab on the [Microsoft Purview pricing](https://azure.microsoft.com/pricing/details/purview/) site.

### Data governance processing units explained

A DGPU is a fully managed compute unit that runs compute-heavy capabilities such as data quality and data health management. Each DGPU provides 60 minutes of compute time, running across varying sets of nodes based on the workload need.

The number of DGPUs you consume depends on:

1. Data quality or health (metadata quality) rule type: Out of the box or custom.
2. The volume of data.
3. Source type: The same volume of data might generate different DGPUs across two different source types.

Some ranges of DGPU generation are as follows:

| Data Source | Row count | SKU type | Rule type | DGPU per rule per run |
| --- | --- | --- | --- | --- |
| Azure SQL DB | 1 Million | Basic | Empty/blank check | 0.02 |
| Azure SQL DB | 1 Million | Basic | StringFormat=Regex/Like check | 0.02 |
| Azure SQL DB | 1 Million | Basic | Table lookup (1 mill row reference table) | 0.03 |
| Azure SQL DB | 1 Million | Basic | Unique check | 0.02 |
| Azure SQL DB | 1 Million | Basic | Duplicate check = 3 column-combo | 0.02 |

### Data health controls pricing

Data health controls, self-serve analytics, and reports within **Health management** use the Basic SKU, as these capabilities don't require higher processing capacity.

The total DGPU consumption depends on the data volume, the calculation of control scores, and report generation. The control job is scheduled to run daily when you initially provision it and triggers only if at least one business domain exists. If you remove all business domains, the job doesn't run.

You can adjust the schedule as needed; the job always runs based on your configured schedule. If you don't want to refresh a specific control, you can edit the control and toggle it to deactivate.

This flexibility lets you fully manage schedules and selectively inactivate controls to optimize costs and manage DGPU consumption.

Tip

- Default control refreshes daily. Scheduled controls run based on the schedule you configure.
- To stop using data health controls, manually disable them from the schedule page. You can activate or deactivate individual controls separately, so you can focus on the most relevant controls.

### Data quality pricing

Data quality usage is billed based on DGPU pay-as-you-go meters. For example, if you run 100 data quality jobs in a single day, and each run produces 0.02 DGPU, then the total DGPU for that day is two DGPUs. Data quality for on-premises data sources uses the Basic SKU for DGPU consumption. To calculate the cost based on performance option and region, visit the [Microsoft Purview pricing](https://azure.microsoft.com/pricing/details/purview/) site.

You can also use a data quality and data health control pricing calculator on the [Microsoft Azure Pricing calculator page](https://azure.microsoft.com/pricing/calculator/?service=purview) to calculate pricing for governed assets, DGPU consumption price for data quality, and data health controls. Use the calculator to budget the investment for the data governance program of your organization. On the calculator page, search for Microsoft Purview to calculate price and budget the data governance investment.

Here's example of consumed processing units for basic to complex rules for different data volumes, based on the standard performance option.

| **Rule complexity** | **10,000 records** | - | **100,000 records** | - | **1,000,000 records** | - | **10,000,000 records** | - | **100,000,000 records** | - | **1,000,000,000 records** | - |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Duration | PU | Duration | PU | Duration | PU | Duration | PU | Duration | PU | Duration | PU |
| Simple | Elapsed time: 1m 1s | 0.02 | Elapsed time: 1m 1s | 0.02 | Elapsed time: 1m 1s | 0.02 | Elapsed time: 1m 16s | 0.02 | Elapsed time: 1m 16s | 0.02 | Elapsed time: 1m 31s | 0.03 |
| Medium | Elapsed time: 1m 1s | 0.02 | Elapsed time: 1m 1s | 0.02 | Elapsed time: 1m 1s | 0.02 | Elapsed time: 1m 16s | 0.02 | Elapsed time: 1m 31s | 0.03 | Elapsed time: 2m 1s | 0.03 |
| High | Elapsed time: 1m 1s | 0.02 | Elapsed time: 1m 1s | 0.02 | Elapsed time: 1m 31s | 0.03 | Elapsed time: 1m 32s | 0.03 | Elapsed time: 2m 1s | 0.03 | Elapsed time: 2m 51s | 0.04 |

Tip

- Increase data volume: For testing, you can use the same data asset by adding more data, or you can create multiple data assets with different data volumes; see the example above.
- Example of rule complexity
    - Simple rule: Blank or empty value check.
    - Medium complex rule: Uniqueness rule, data type, or format check rule.
    - High complex rule: Duplicate check with multiple selected columns; credit card, national ID, table lookup, and SSN validation are in the category of complex rule.

## Data Map and scanning charges

Unified Catalog currently runs on the existing Data Map. Data Map and scan charges don't apply to Unified Catalog customers once they either [consent to the Microsoft Purview billing model](purview-payg-consent-based-enablement) or [upgrade from free to enterprise tier](data-governance-free-version-upgrade-to-enterprise). The new Unified Catalog is rolling out in multiple regions; check the [supported regions for Unified Catalog](unified-catalog-regions).

Customers using the classic Data Catalog can check pricing on the **Data Map (Classic)** tab of the [Microsoft Purview pricing](https://azure.microsoft.com/pricing/details/purview/) site.

## Resources

- [Data governance billing FAQ](data-governance-billing-faq)
- [Learn about Microsoft Purview billing models](purview-billing-models)
- [Microsoft Purview pricing site](https://azure.microsoft.com/pricing/details/purview/)
- [Unified Catalog supported regions](unified-catalog-regions)