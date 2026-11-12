---
layout: Conceptual
title: Data Quality Scores in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-scores
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Understand how to interpret the data quality scores after running a data quality scan in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 87448aaa-8723-026a-82cb-525974bb1a85
document_version_independent_id: 87448aaa-8723-026a-82cb-525974bb1a85
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-scores.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-scores
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-scores.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 1397e548-c4c3-fc89-05c6-e0f2683b67c6
---

# Data Quality Scores in Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

After you [create data quality rules](unified-catalog-data-quality-rules) and [run a data quality scan](unified-catalog-data-quality-scan), your data assets receive a data quality score based on results from your rules. This article explains how scores are calculated so you can better understand your data quality results and develop action items to improve your data's integrity.

## Understand data quality scores

Data quality rules describe the state of the data. They show how far the data is from the ideal state described by the rules. Each rule produces a score that describes how close the data is to its desired state. Most rules are straightforward; they divide the total number of rows that pass the assessment by the total number of rows to arrive at the score.

The formula used to calculate the data quality score for a rule against data in a column is:

`[(total number of passed records)/(passed records + failed records + miscast records + empty records)]`

- Numerator = total number of passed records
- Denominator = total number of records (number of passed records + number of failed records + number of miscast records + number of empty records)

Note

- **Passed**: Number of records that passed an applied rule.
- **Unevaluable**: The columns required to evaluate this rule aren't evaluable.
- **Failed**: Number of records that failed an applied rule.
- **Miscast**: The data type of the asset and the type that customer listed it as not matching. It can't be converted to the expressed type.
- **Empty**: Null or blank records.
- **Ignored**: Rows didn't participate in the rule evaluation. Users can express rows to ignore; for example, ignore all rows that have email="n/a", or ignore all rows where departmentCode='test' or 'internal'. Ignored records aren't used for score calculation.

Microsoft Purview Data Quality then gives a sense for the state of each column by generating a column score. This score is the average of all the scores of the rules on that column. Once the column scores are calculated, the formula used to calculate average percentage data quality score for data products and governance domains is:

`[(Percentage 1 + Percentage 2) / (Sample size 1 + Sample size 2)] x 100`

The score is multiplied by 100 to make the scores more readable.

## Example calculation

Let's imagine there's a column that doesn't have the [**Empty/blank fields** rule](unified-catalog-data-quality-rules#emptyblank-fields) defined on it. This implies that null values are allowed for this column. So certain rules, like the [**Unique values** rule](unified-catalog-data-quality-rules#unique-values), will filter out null values in that case.

For example: If the asset has 10,000 rows in a table but 3,000 were null and 500 weren't unique then the score would be: `((10000 - 3000 - 500)/(10000 - 3000) )* 100 = 93`

The null rows are ignored when evaluating the data and determining a score.

## Specific rule scores

For [**Custom** rules](unified-catalog-data-quality-rules#custom-rules), there's a capability similar to what you might see for the unique values rule. But in this case, the filter isn't on nulls, but rather the filter expression.

Some rules, like the [**Freshness** rule](unified-catalog-data-quality-rules#freshness), are either pass or fail, so their scores are either 0 or 100. The Freshness rule is applied at the data asset level, not at the column level.

## Rule details and history

You can view the details and history of rule scores by selecting a rule. Selecting a specific rule name and navigating to the rule **History** tab, you see the trend of the different scan runs for the particular rule.

- Rule **Details** provides information on the number of rows passed, failed, and ignored for the various runs for the particular rule. Rules that are in **draft state** (OFF state) won't have their scores contribute to the global score. Rules in a draft state won't be run at all during quality scans and so won't have scores.

    ![Screenshot that shows the Data Quality scores at a rule level.](media/how-to-view-data-quality-scan-results/dq-rule-level-score.png)
- Columns and rules have a many-to-many relationship, the same rule can be applied to many columns, and many rules can be applied to the same column. You can view the trend pattern of each rule by going to the **Schema** tab on the asset's data quality page and viewing the line in the **Trend** column.
- Asset level data quality score trends are available for the last 50 runs. This quality score trend helps data quality stewards to monitor data quality trend and fluctuations month over month. Data quality can also [trigger alerts](unified-catalog-data-quality-alerts) for every data quality scan if the quality score doesn't meet the threshold or business expectation.
- Global score is the average of the production rules defined on the asset. The asset level global score is also rolled up to the data product level and governance domain level. The global score is intended to be the official definition of the state of the data asset, data product, and governance domain in context of quality of data.
- A summary report is created for data quality dimension. This report contains data quality score for each data quality dimension. Global score for the governance domain is published also in this report. You can browse the quality score for each governance domain, data product, and data asset from this Power BI report.

    [![Data Quality dimension reports ](media/how-to-view-data-quality-scan-results/dq-dimensions-report.png)](media/how-to-view-data-quality-scan-results/dq-dimensions-report.png#lightbox)

Note

- Data quality dimensions are recognized terms used by data practitioners to describe a feature of data that can be measured or assessed against defined standards in order to quantify the quality level of data used to run a business.
- The data quality score for an asset is the arithmetic average of the scores of the rules applied to its columns.
- The data quality score for a data product is the arithmetic average of the data quality scores of the data assets associated with that data product.
- The data quality score for a governance domain is the arithmetic average of the data quality scores of the data products associated with that domain.