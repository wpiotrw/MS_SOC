---
layout: Conceptual
title: Data Quality Thresholds for data quality rules in Microsoft Purview Data Governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-threshold
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-05-10T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
ai-usage: ai-assisted
description: Learn about data quality thresholds for data quality rules and data assets in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 02f0189a-a448-343d-3230-f57f104703ba
document_version_independent_id: 02f0189a-a448-343d-3230-f57f104703ba
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-threshold.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-threshold
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-threshold.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: a2ed5839-dff3-c4c4-2bb8-06b2e7b992d1
---

# Data Quality Thresholds for data quality rules in Microsoft Purview Data Governance | Microsoft Learn

A data quality threshold is a predefined limit that determines whether data meets an acceptable level of quality. In simple terms, it answers the question: How good is good enough?

For example, if you run a completeness rule on a column:

- Total records: 1,000
- Records with values: 920
- Completeness score: 92%

If your threshold is 90%, the data meets the expectation.

If your threshold is 95%, the data doesn't meet the expectation.

The threshold is the cutoff point that defines whether the data meets the expectation for specific use cases.

## Why thresholds matter

Different types of data require different quality expectations. For example:

- Email address column: Might require 99–100% completeness.
- Description column: Perhaps 80–90% is acceptable.
- Financial transactions: Might require 100% accuracy.

Using one fixed threshold, such as 80% for everything, can be misleading, especially for critical or regulated data.

## Types of thresholds

- Rule-level threshold: Set for each rule (for example, completeness must be ≥ 95%).
- Data asset level threshold: Different expectations for different columns.
- Data product level threshold: Overall score requirement.

## Configurable data quality thresholds

You can configure Data Quality thresholds to set minimum acceptable quality scores at the rule and data asset levels. Define the threshold to align quality evaluation with business criticality.

### Configure or edit the default threshold for a data asset

1. In Microsoft Purview Unified Catalog, select **Health management**, and then select **Data quality**.
2. Select a governance domain, select a data product, and then select a data asset.
3. On the **Overview** page, select **Set score threshold**.
4. Change the default threshold.
5. Select **Save**.

    [![asset level threshold](media/how-to-view-data-quality-scan-results/setscorethreshold.png)](media/how-to-view-data-quality-scan-results/setscorethreshold.png#lightbox)

### Configure the threshold for a data quality rule

1. In Unified Catalog, select **Health management**, and then select **Data quality**.
2. Select a governance domain, select a data product, and then select a data asset.
3. On the **Rules** page, select **New rule**.
4. Select the out-of-the-box rule or the custom rule, and select **Next**.
5. Select **Score threshold** and change the default threshold value.
6. Select **Save**.

[![data quality rule level threshold](media/how-to-view-data-quality-scan-results/data-quality-rule-threshold.png)](media/how-to-view-data-quality-scan-results/data-quality-rule-threshold.png#lightbox)

### Edit a data quality rule threshold

1. On the **Rules** page of a data asset, select the edit icon for a rule.
2. From the overview, select **Score threshold**.
3. Edit the threshold value.
4. Select **Save**.

### Configure alerts

Set an alert to notify you when the data quality score of a data asset or rule falls below a defined threshold. When you set up or edit a rule threshold, follow these steps:

- Set the **Alert** toggle to on.
- At **Recipient**, add one or more users.
- Select **Save**.

[![set alert for threshold](media/how-to-view-data-quality-scan-results/set-alert.png)](media/how-to-view-data-quality-scan-results/set-alert.png#lightbox)

Note

If you don't configure a threshold, the default threshold values and colors are used. The default threshold score values are:

- **Low (red)**: 0-40
- **Medium (orange)**: 40-80
- **High (green)**: 80-100

Important

Threshold metadata doesn't publish to Azure Data Lake Storage Gen2 or Fabric Lakehouse for self-serve analytics.

**The benefits that an organization gets from the configurable data quality threshold feature are:**

- Enables the enterprise to align their organization with quality governance.
- Improves trust in the data quality scores produced by Microsoft Purview Data Quality, enabling teams across the enterprise to confidently determine whether data is fit for their specific use cases.
- Helps organizations move beyond generic quality checks and toward business-driven data quality management.
- Supports regulatory and decision-critical use cases.
- Reduces user or organizational confusion caused by uniform threshold evaluation.

Setting rule-level thresholds creates a clear standard for what "good" looks like. Alerts ensure you act the moment data drifts below that standard. This has several practical benefits:

- **Early detection of issues**: Catch things like missing, inconsistent, or incorrect data before they impact reports, pipelines, or models.
- **Reduced business risk**: Prevents bad data from driving incorrect decisions, financial errors, or compliance issues.
- **Faster remediation**: Alerts enable teams to respond immediately instead of discovering issues days or weeks later.
- **Accountability and governance**: Clear thresholds define ownership and expectations for data quality.
- **Operational efficiency**: Eliminates manual monitoring and reduces reliance on ad hoc checks.
- **Trust in data**: Consistent enforcement of quality standards increases confidence in analytics and AI outputs.

In short, **thresholds** define acceptable quality, and alerts make that standard actionable.