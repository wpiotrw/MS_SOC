---
layout: Conceptual
title: Data quality health report in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-reports-data-quality-health
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-01-12T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to access and interpret the data quality reports in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 04a0bf45-c041-586d-a132-27a021095b1c
document_version_independent_id: 04a0bf45-c041-586d-a132-27a021095b1c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-reports-data-quality-health.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-reports-data-quality-health
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-reports-data-quality-health.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: bdc48f50-bea8-aa8b-f6c4-94ed22ea75da
---

# Data quality health report in Unified Catalog | Microsoft Learn

The data quality health report evaluates and summarizes the quality of data within an organization or system. It includes assessments of various data quality dimensions and metrics to help stakeholders understand the accuracy, completeness, consistency, reliability, and timeliness of their data. This data quality report allows your team to track your health management progress at a glance and identify areas that need more work to improve the quality of data in your data estate.

This article covers how you can access this report and what the provided data quality measure means for your health management.

## Report purposes

- **Monitoring and governance**: To continuously monitor and manage the quality of data, ensuring it meets the organization’s standards and regulatory requirements.
- **Decision support**: To provide stakeholders with reliable data for making informed business decisions.
- **Identifying issues**: To detect and document data quality issues, enabling timely remediation.
- **Improving data management**: To enhance data management practices by identifying root causes of data quality issues and implementing corrective measures.
- **Performance measurement**: To measure the effectiveness of data quality initiatives and track improvements over time.
- **Stakeholder communication**: To communicate data quality status and progress to stakeholders, including management, data product owners, data stewards, and IT teams. By providing a clear and comprehensive view of the state of data quality, these reports play a crucial role in maintaining the integrity and usefulness of data within an organization.

## Prerequisites

You need the [Data Health Reader](data-catalog-permissions#data-catalog-roles) role to view data health information.

## View data quality health report

1. In the Microsoft Purview portal, open **Unified Catalog**.
2. Go to **Health management** &gt; **Reports**.
3. Select the **DQ health** report.

## Data quality dimension reporting

The overview page of the report shows data quality dimension scores, data quality rule hierarchy, data quality status by dimension, and data quality dimensions and rule types used for different data assets. The top controls help you understand your overall health management at a glance.

[![Screenshot of data quality report overview page.](media/data-governance-health-report/dq-report-overview-page.png)](media/data-governance-health-report/dq-report-overview-page.png#lightbox)

Use the filters to see information for specific governance domains, data products, or data products in a certain status (for example: draft).

| Data Quality Dimension | Description |
| --- | --- |
| Accuracy | Data should accurately represent real-world entities. Context matters. For example, if you’re storing customer addresses, ensure they match the actual locations. |
| Completeness | The objective of this rule is to identify the empty, null, or missing data. This rule validates that all values are present (though not necessarily correct). |
| Conformity | This rule ensures that the data follows data formatting standards such as representation of dates, addresses, and allowed values. |
| Consistency | This rule checks that different values of the same record conform with a given rule and that there are no contradictions. Data consistency ensures that the same information is represented uniformly across different records. For example, if you have a product catalog, consistent product names and descriptions are crucial. |
| Timeliness | This rule aims to ensure that the data is accessible in as short a time as possible. It ensures that the data is up to date. |
| Uniqueness | This rule checks that values aren't duplicated. For example, if there's supposed to be only one record per customer, then there aren't multiple records for the same customer. Each customer, product, or transaction should have a unique identifier. |

Data quality overall score and dimension scores help data practitioners and data estate owners understand how complete, accurate, consistent, and trustworthy their data is. These scores also indicate what improvement actions need to be taken to enhance the quality of their data estate.

### How the scores are calculated

[![Screenshot of the data quality dimension score.](media/data-governance-health-report/data-quality-dimensions-score.png)](media/data-governance-health-report/data-quality-dimensions-score.png#lightbox)

Tip

If you use the filters, these KPIs show scores for the governance domains or data products you select.

### Data quality status by dimensions

**Overall score** % = Percentage of data quality dimension score of all measured dimensions divided by total number of dimensions with score. **Exception**: If any dimension score is **Blank**, the calculation excludes the **Blank** score from the overall score; for example:

| Data Quality Dimension | Score % |
| --- | --- |
| Accuracy | 100 |
| Completeness | 80 |
| Consistency | 100 |
| Conformity | Blank |
| Uniqueness | 100 |
| Timeliness | 50 |

Overall score % = ((100+80+100+100+50)/5)\*100 = 86%

As conformity score is **Blank**, the calculation excludes it from the overall score. If the conformity score is zero (0) instead of **Blank**, the calculation includes the zero score. In this scenario, the overall score = ((100+80+100+0+100+50)/6)\*100 = 72% (71.66%).

The score for each dimension is calculated as follows:

Data quality score for a dimension (%) = (Total number of records that pass all applied rules for the selected dimension across all data assets of a data product) ÷ (Total number of records of all data assets of the selected data product measured against the selected dimension) × 100

**Example:**

Total number of assets associated with a data product is 4. Total passed records for asset one are 1,000, for asset two are 200, for asset three are 4,000, and for asset four are 100. Total number of records for all four assets is 6,000. Data quality score (%) for the selected dimension = ((1,000 + 200 + 4,000 + 100) / 6,000) \* 100 = 88%.

Data quality dimension scores are calculated for each governance domain. Dimensions are mapped with rules, and the score rolls up from data asset columns to data asset, and from data asset to data product and governance domain level for each industry standard dimension. You can filter dimension level scores per governance domain to investigate more details.

[![Screenshot of the data health by governance domains table.](media/data-governance-health-report/data-quality-dimenion-domain-score.png)](media/data-governance-health-report/data-quality-dimenion-domain-score.png#lightbox)

### Data quality rules pass and fail ratio

The pass and fail ratio of data quality rules is measured for each data quality dimension for data products. This measure helps data owners and data practitioners understand what percentage of data in a data product is inaccurate, inconsistent, incomplete, duplicate, or not fresh enough as expected. This measure also helps to investigate and understand whether the applied rules are incorrect or the data is incorrect.

[![Screenshot of the data quality rules pass and fail ratio per dimension.](media/data-governance-health-report/data-quality-ration-report.png)](media/data-governance-health-report/data-quality-ration-report.png#lightbox)

**Example scenario 1**

You create rules to measure accuracy and completeness of a data asset. After a data quality scan is completed and the data health report is refreshed, if the Accuracy score is 100% and Completeness score is 16.6%, the report displays one data product count.

- Accuracy as 100%, with a green bar.
- Completeness as 16.6%, which is below the threshold (100%), as Failed with a red bar.

**Example scenario 2**

You apply two accuracy dimension rules. After a data quality scan, you see one accuracy rule score is 100%, which is visible in the report as Passed, shown with a green bar. Another accuracy rule dimension for same data product has a score of 15.98%, which is visible in the report as Failed, shown with a red bar. The report shows 50% Passed and 50% Failed, because Accuracy has two rule dimensions.

| Accuracy rule | Score | Result |
| --- | --- | --- |
| Rule 1 | 100% | Passed |
| Rule 2 | 15.98% | Failed |

Calculation:

- Passed rule = 1
- Failed rule = 1
- Total rules = 2
- Accuracy score pass fail ratio = (1/2) x 100 = 50%, so you see 50% Pass, and 50% Fail.

## Data quality details report

In the data quality health report, select the **Details** tab to see how many rules apply to data products, data assets, and critical data elements. These rules help measure and monitor the quality of the entire data estate of your organization. You can drill down to see how many records of a data asset failed for a rule type, which rule type is performing better, and which governance domain and data products are publishing and maintaining trustworthy data. You can filter the measures by governance domain and data product to understand the current state and to plan improvement actions. Here's an example of the details view:

[![Screenshot of data quality detail report.](media/data-governance-health-report/data-quality-details-report.png)](media/data-governance-health-report/data-quality-details-report.png#lightbox)

### Historical trend

In the data quality health report, select the **Historical Trend** tab to help you understand the historical trend of the data quality of governed data assets. You can filter governance domain and data product level trends for the associated data assets. You can also use the selector to select the top or bottom 10 data assets to browse the data quality trends of each data quality dimension. Here's an example of the historical trend view:

[![Screenshot of 13 months data quality history trend.](media/data-governance-health-report/dq-13-month-history.png)](media/data-governance-health-report/dq-13-month-history.png#lightbox)

Note

- The data quality health report depends on data health controls and Microsoft Purview metadata self-serve analytics model. If you don't use the data health controls and don't subscribe Unified Catalog metadata, the data quality health report doesn't refresh. You need to use data health controls or subscribe Microsoft Purview metadata for self-serve analytics to refresh the data quality health report.
- If you don't use the data quality feature, the data quality health report appears blank because the report is created using data generated from the data quality scan feature.