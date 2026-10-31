---
layout: Conceptual
title: Data Governance Report in Unified Catalog (Preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-reports-data-governance
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2025-07-27T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn about the data governance health report (preview) in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 0311f12e-c61c-4742-8f05-c4c70c75d9ba
document_version_independent_id: 0311f12e-c61c-4742-8f05-c4c70c75d9ba
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-reports-data-governance.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-reports-data-governance
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-reports-data-governance.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: d7a20ccb-7451-f850-e395-e19c14326255
---

# Data Governance Report in Unified Catalog (Preview) | Microsoft Learn

The data governance health report allows your team to track your health progress at a glance, and identify areas that need more work. This article covers how you can access this report and what the provided information means for your data governance health.

Note

If you don't use data health controls, the data governance health report doesn't refresh. Ensure that you set up the schedule to [run data health controls](unified-catalog-controls) for refreshing the health controls scores and the data governance health report.

## Prerequisites

- You need [data health reader](data-governance-roles-permissions#unified-catalog-permissions) permissions to view Data Estate Health information.

## View data governance health report

1. Open the Microsoft Purview portal and select **Unified Catalog**.
2. At **Health management**, select **Reports**.
3. Select the **Data governance (preview)** report.

The overview page of the report covers the overall health of your governance domains, and provides details about your data products.

[![Screenshot of data governance health report overview page.](media/data-governance-health-report/overview-page.png)](media/data-governance-health-report/overview-page.png#lightbox)

Use the filters to see information for specific governance domains, data products, or data products in a certain status (for example: draft).

## Overview

The main overview covers the controls for your governance domains.

### Controls and actions

The top controls and actions help you understand your overall governance health at a glance. They cover both [controls](unified-catalog-controls) and [actions](unified-catalog-data-health-management-actions-page).

![Screenshot of the data governance controls and actions.](media/data-governance-health-report/controls-and-actions.png)

| Control or action | Description | Example |
| --- | --- | --- |
| Governance score | Average of the ownership, cataloging, and classification controls. |  |
| Access and use | Average of the self-service access enablement and compliant data use controls. | (Self-serv score is **100** + Compliaant score is **5.6**) / 2 = **52.8%** is the Access and use score control group score. |
| Discoverability | Average of these two checks: number of governance domains with Unified Catalogs and the number data products that have data assets mapped. |  |
| Estate curation | Percentage of data assets that have classifications applied. | Estate curation score is **32.5%** because only 32.5% of data assets are classified during scan. |
| MDQ management | Average of data product useability (products with long descriptions and attached glossary terms), and percentage of data products with linked assets. | (MDQ data product usability is **87.9** + MDQ Linked asset is **83.3**) /2 = **85.6%** is the MDQ management score. |
| Trusted data | Average of three controls: Percentage of data products with owners, percentage of data products that have data quality scoring enabled, percentage of data products that are certified. | (% of data products with owner is **97.6** + % data product with data quality score is **68.4** + % of data product certified is **46.2**) = **70.7%** is the Trusted data score. |

Tip

If you use the filters, these KPIs reflect scores for the governance domains or data products you select.

### Data health by governance domain

The data health by governance domain chart gives you individual control scores for your governance domains without needing to use the filters. At a glance, you can see which of your governance domains are healthy and which need more attention.

![Screenshot of the data health by governance domains table.](media/data-governance-health-report/health-by-governed-domain.png)

### Governance score by controls

This column chart highlights your governance strengths and weaknesses by showing overall score for each control in Unified Catalog. Prioritize low or flagging scores to increase your data governance coverage across your data estate.

![Screenshot of the governance score by controls column chart.](media/data-governance-health-report/scores-by-controls.png)

### Health score trend

This table shows your daily health progression for all of the main health controls.

Use this table to track how well your team manages your data estate over time and to track your progress toward healthy data governance.

![Screenshot of the health score trends line chart.](media/data-governance-health-report/health-score-trend.png)

## Data product details

Select the **Data product details** tab at the bottom of the page to see action and control information for your data products.

[![Screenshot of data product details tab, highlighted at the bottom of the overview page.](media/data-governance-health-report/data-product-details-inline.png)](media/data-governance-health-report/data-product-details.png#lightbox)

### Data product controls and actions

The top controls and actions help you understand your overall governance health at a glance. They cover both [controls](unified-catalog-controls) and [actions](unified-catalog-data-health-management-actions-page).

![Screenshot of the data product details controls and actions.](media/data-governance-health-report/data-product-controls-and-actions.png)

| Control or action | Description | Example in the image above |
| --- | --- | --- |
| Classification | Percentage of data products that have classified assets attached. | **32.5%** of data assets are classified by Data Map scans. |
| Ownership | Percentage of data products that have an active owner. | **97.6%** of data products have at least one owner. |
| Connection | Percentage of data products that have at least one asset attached. | **100%** of data products have at least one data asset attached. |
| DQ measurement | Aggregation of data quality scores across the data products. | **48.9%** of data assets have a data quality score. |
| Self serve | Percentage of data products with self-service access setup. | **100%** of data products have a self-serve access policy attached. |
| Compliant | Percentage of data products with the purpose of use policy added. | **5.6%** of data products have a compliant policy attached. |
| Catalog | Percentage of data products with a description, published glossary terms, and a use case. | **94.4%** of data products have descriptions, use cases, and at least one glossary term associated. |
| Certification | Percentage of data products that have been verified. | **38.9%** of data products are verified. |
| MDQ linked assets | Percentage of data products with at least one asset and at least one published glossary term. | **83.3%** of data products have at least one data asset and one glossary term linked. |
| MDQ usability | Percentage of data products that have a description over 100 characters long, the parent domain has a description 100 characters long, and the associated term has a description 100 characters long. | **87%** of data products have descriptions and use cases that are at least 100 characters long. |

Use the filters to narrow your view to only certain governance domains, data products, or data products with a certain status.

### Governance score by data product

This bar chart highlights your strongest and weakest data products by showing the overall governance score for each data product. Prioritize low-scoring but high-use data products to bring the most value to Unified Catalog.

![Screenshot of the governance scores listed by data product in a bar chart.](media/data-governance-health-report/governance-score-by-data-product.png)

### Individual control checks

This table shows the pass or fail status for each individual control check available to your data product. You can check controls for low-scoring data products to see which areas need improvement.

![Screenshot of the control checks table, showing the individual controls for each data product and their pass/fail status.](media/data-governance-health-report/control-checks.png)

### Data assets

This table shows the pass or fail status for individual assets in Unified Catalog. If multiple data products reference a single asset, resolving any outstanding governance issues for that asset raises your score overall.

![Screenshot of the data assets table, showing the classification status for each asset.](media/data-governance-health-report/data-assets.png)

### Glossary terms report (preview)

Glossary terms provide vocabulary for business users. These terms allow users to discover and work with data in the vocabulary that's familiar to them versus using abstract technical terminology inherited from physical data sources. Terms are created under governance domains to create context specific to each part of your organization. Both sales and marketing might use the same term to mean different things, and your governance domains help your team to differentiate between those meanings. Once created, terms map to data products, to provide context for those data products, and to provide specific data governance based on business context. Terms are an active part of Microsoft Purview that provide data governance by now containing policies. The glossary terms report (preview) helps data stewards to browse:

- Glossary terms trends.
- Glossary terms hierarchy.
- Data product associated with glossary terms.
- Governance domain association with glossary terms.

![Screenshot of the glossary terms report.](media/data-governance-health-report/glossary-term-report.png)