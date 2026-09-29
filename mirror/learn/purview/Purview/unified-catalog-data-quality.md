---
layout: Conceptual
title: Data Quality in Microsoft Purview Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-09-08T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Get an overview of data quality in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 3667a59e-82d2-58e4-391e-1cbd09bd9096
document_version_independent_id: 3667a59e-82d2-58e4-391e-1cbd09bd9096
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: 20fde5cd-26d2-fc13-fa56-9b904f885e16
---

# Data Quality in Microsoft Purview Unified Catalog | Microsoft Learn

Data quality in Microsoft Purview Unified Catalog empowers governance domain and data owners to assess and oversee the quality of their data ecosystem, facilitating targeted actions for improvement. In today's AI-driven landscape, the reliability of data directly impacts the accuracy of AI-driven insights and recommendations. Without trustworthy data, there's a risk of eroding trust in AI systems and hindering their adoption.

Poor data quality or incompatible data structures can hamper business processes and decision-making capabilities. Data quality in Unified Catalog addresses these challenges by offering users the ability to evaluate data quality using no-code or low-code rules, including out-of-the-box (OOB) rules and AI-generated rules. These rules are applied at the column level and aggregated to provide scores at the levels of data assets, data products, and governance domains, ensuring end-to-end visibility of data quality within each domain.

Data quality in Microsoft Purview also incorporates AI-powered data profiling capabilities, recommending columns for profiling while allowing human intervention to refine these recommendations. This iterative process not only enhances the accuracy of data profiling but also contributes to the continuous improvement of the underlying AI models.

By applying data quality, organizations can effectively measure, monitor, and enhance the quality of their data assets, bolstering the reliability of AI-driven insights and fostering confidence in AI-based decision-making processes.

## Data quality life cycle

1. [Assign users(s) data quality steward permissions in Unified Catalog](data-governance-roles-permissions#how-to-assign-catalog-level-roles) to use all data quality features.
2. [Register](data-map-data-sources-register-manage#register-a-new-source) and [scan](data-map-scan-data-sources) a data source in Microsoft Purview Data Map.
3. [Add your data asset to a data product](unified-catalog-data-products-create-manage#add-and-remove-data-assets)
4. [Set up a data source connection to prepare your source for data quality assessment](unified-catalog-data-quality-supported-sources-connection).
5. [Configure and run data profiling for an asset in your data source.](unified-catalog-data-quality-profiling)
    1. When profiling is complete, browse the results for each column in the data asset to understand your data's current structure and state.
6. [Set up data quality rules](unified-catalog-data-quality-rules) based on the profiling results, and apply them to your data asset.
7. [Configure and run a data quality scan](unified-catalog-data-quality-scan) on a data product to assess the quality of all supported assets in the data product.
8. [Review your scan results](unified-catalog-data-quality-scores) to evaluate your data product's current data quality.
9. Repeat steps 5-8 periodically over your data asset's life cycle to ensure it's maintaining quality.
10. Continually monitor your data quality
    1. [Review data quality actions](unified-catalog-data-quality-actions) to identify and resolve problems.
    2. [Set data quality notifications](unified-catalog-data-quality-alerts) to alert you to quality issues.

## Supported data quality regions

Data quality is currently [supported in the following regions](data-catalog-regions).

Important

Data Quality capability is supported only when the accounts and the data sources are in the Purview supported regions. Data sources and purview account need to be in the same azure region. Concurrent DQ job execution limits are:

- **Manual scans**: Max 10 concurrent jobs.
- **Scheduled scans**: Max 25 concurrent jobs.
- **Manual profile**: Max 10 concurrent profiling jobs.
- **DQ Rule suggestion**: Max 10 concurrent jobs.

## Supported multicloud data sources

View the list of [supported data sources](unified-catalog-data-quality-supported-sources-file-formats).

Important

Data quality for Parquet files is designed to support:

1. A directory with Parquet Part File. For example: **./Sales/{Parquet Part Files}**. The fully qualified name must follow `https://(storage account).dfs.core.windows.net/(container)/path/path2/{SparkPartitions}`. Make sure the directory and subdirectory structure doesn't include {n} patterns. Instead, use a direct FQN leading to {SparkPartitions}.
2. A directory with partitioned Parquet files, partitioned by columns within the dataset like sales data partitioned by year and month. For example: **./Sales/{Year=2018}/{Month=Dec}/{Parquet Part Files}.**

Both of these essential scenarios, which present a consistent Parquet dataset schema, are supported. **Limitation:** Data quality isn't designed to support arbitrary hierarchies of directories with Parquet files. **We recommend presenting data in the (1) or (2) constructed structure.**

Currently, Microsoft Purview can only run data quality scans by using [Managed Identity](data-map-data-scan-credentials#use-microsoft-purview-system-assigned-managed-identity-to-set-up-scans) as an authentication option. Data quality services run on **Apache Spark 3.5** and **Delta Lake 3.2.1**.

## Data quality features

- [**Data source connection configuration**](unified-catalog-data-quality-supported-sources-connection)
    - Configure connection to allow Microsoft Purview data quality SaaS application to have read access to data for quality scanning and profiling.
    - Microsoft Purview uses Managed Identity as an authentication option.
- [**Data profiling**](unified-catalog-data-quality-profiling)
    - AI-enabled data profiling experience.
    - Industry standard statistical snapshot (distribution, min, max, standard deviation, uniqueness, completeness, duplicate, and more).
    - Drill down column level profiling measures.
- [**Data quality rules**](unified-catalog-data-quality-rules)
    - Out of box rules to measure six industry standards data quality dimensions (completeness, consistency, conformity, accuracy, freshness, and uniqueness).
    - Custom rules creation features include number of out of the box functions and expression values.
    - Auto generated rules with AI integrated experience.
- [**Data quality scanning**](unified-catalog-data-quality-scan)
    - Select and assign rules to columns for data quality scan.
    - Apply data freshness rule in the entity or table level to measure the data freshness SLA.
    - Scheduling data quality scanning job for time period (hourly, daily, weekly, monthly, and more).
- [**Data quality job monitoring**](unified-catalog-data-quality-job-monitor)
    - Enable monitoring data quality job status (active, completed, failed, and more).
    - Enable browsing the data quality scanning history.
- [**Data quality scoring**](unified-catalog-data-quality-scores)
    - Data quality score in rule level (what is the quality score for a rule that applied to a column).
    - Data quality score for data assets, data products, and governance domains (one governance domain can have many data products, one data product can have many data assets, one data asset can have many data columns).
- [**Data quality alerts**](unified-catalog-data-quality-alerts)
    - Configure alerts to notify data owners and data stewards if data quality threshold missed the expectation.
    - Configure email alias or distribution group to send the notification about data quality issues.
- [**Data quality actions**](unified-catalog-data-quality-actions)
    - Actions center for data quality with actions to address data quality anomaly states, including diagnostic queries for data quality steward to zero in on the specific data to fix for each anomaly state.
- [**Data quality managed virtual network**](unified-catalog-data-quality-managed-virtual-networks)
    - A virtual network managed by data quality that connects with private endpoints to your Microsoft Azure data sources.

## Data residency and encryption

Microsoft Managed Storage account stores data quality metadata and profiling summary. It stores them in the same region as the data source, so data residency remains intact. All data is encrypted. The Purview Resource Provider regional user data store is used for metadata. It handles all the encryption and is common across all Purview services. If you want more control over your data encryption with a customer-managed encryption key (CMK), use a separate process. Learn more about [Microsoft Purview Customer Key](customer-key-overview).

## Data quality compute pricing

Data quality usage is billed based on the Data Governance Processing Unit (DGPU) pay-as-you-go meters. Find details on [how pricing is computed for data quality](data-governance-billing#data-quality-pricing).

## Limitations

- Virtual network isn't supported for Google Big Query yet.
- You can apply a maximum of 200 data quality rules per data asset for a data quality scan. Get [details about this limit and workarounds](unified-catalog-data-quality-rules#limitation).