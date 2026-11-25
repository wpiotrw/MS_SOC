---
layout: Conceptual
title: Review Flex Plan prices in your price sheet - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/benefits/flex-plan/review-flex-plan-prices
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/118/azure-cost-management/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/748a4eaa-0e25-ec11-b6e6-000d3a4f07b8
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
adobe-target: true
learn_banner_products:
- azure
description: Learn how to find Flex Plan prices in your price sheet, compare them with on-demand prices, and identify the Flex Plan offer for each price.
author: Britt-Henderson
ms.author: britth
ms.reviewer: vikdesai
ms.service: cost-management-billing
ms.subservice: cost-management
ms.topic: how-to
ms.date: 2026-11-19T00:00:00.0000000Z
locale: en-us
document_id: c3ba560e-649c-0ff1-cbca-9a16b4313ae4
document_version_independent_id: 4b5f462d-5bbb-1ef0-02d1-6c71fbb8d292
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/benefits/flex-plan/review-flex-plan-prices.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/benefits/flex-plan/review-flex-plan-prices
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/benefits/flex-plan/review-flex-plan-prices.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
platformId: fe074468-86a4-e2be-087f-7606b74586af
---

# Review Flex Plan prices in your price sheet - Microsoft Cost Management | Microsoft Learn

Your price sheet lists a Flex Plan price for each meter that a Flex Plan offer covers. Use it to confirm that the prices you were quoted are the prices you're charged, and to compare Flex Plan prices with on-demand prices for the same meter.

## Prerequisites

- A Microsoft Customer Agreement billing account.
- The billing profile owner, contributor, reader, or invoice manager role.

## Get your price sheet

You can export or download your price sheet. Both include Flex Plan prices and the `priceFactors` column.

### Export your price sheet

1. In the Azure portal, go to **Cost Management** and select your billing profile scope.
2. Select **Exports**, and then select **Create**.
3. Select **Price sheet**.
4. For the dataset version, select **2026-10-01**.
5. Select a storage account and a schedule, and then create the export.

Dataset version 2026-10-01 includes the `priceFactors` column, which you need to identify Flex Plan prices. For more information, see [Create and manage exports](../../costs/tutorial-improved-exports).

### Download your price sheet

You can also download the price sheet from the Azure portal. A downloaded price sheet doesn't use dataset version 2026-10-01, but it includes the `priceFactors` column at the end of the file. For more information, see [View and download your organization's Azure pricing](../../manage/ea-pricing#download-pricing-for-an-mca-or-mpa-account) and [Compare downloads and exports](../../understand/compare-downloads-exports).

## Find Flex Plan prices

In the price sheet, a Flex Plan price is a row with these values:

| Column | Value |
| --- | --- |
| `priceType` | `FlexPlan` |
| `term` | The term of the Flex Plan offer, such as `P1M` (one month) or `P1Y` (one year) |
| `priceFactors` | A factor with `Type` set to `FlexPlan` and the `ProductCode` of the Flex Plan offer |

The `priceFactors` column is a JSON array that was added with the 2026-10-01 Cost Management exports dataset version. In the price sheet, the column describes the benefits that are associated with a price. In the case of Flex Plan, for example, `priceFactors` might look like this:

```json
[{"Factors":[{"Type":"FlexPlan","Extensions":{"ProductCode":"<product-code>"}}]}]
```

For more information, see [Understand price factors and supplemental charge details](../../automate/understand-price-factors-supplemental-charge-details#identify-flex-plan-charges).

## Compare Flex Plan and on-demand prices

1. Filter the price sheet to one meter by its `meterId`.
2. Find the row where `priceType` is `Consumption`. That row is the on-demand price.
3. Find the rows where `priceType` is `FlexPlan`. There's one row for each Flex Plan offer that covers the meter.
4. Compare `unitPrice` across the rows.

If more than one Flex Plan offer covers the meter, the rows can have the same price and term and differ only in the product code. To find out which offer each row belongs to, look up its product code.

## Identify the Flex Plan offer

To find out which offer a Flex Plan price belongs to, take the product code from the row's `priceFactors` column and look it up. For instructions, see [Discover available offers and prices](automate-flex-plan#discover-available-offers-and-prices).

Compare the offer details with your quote, such as:

- The offer and SKU names
- The term, such as one month or one year
- How often the commitment is billed, such as monthly or up front
- The minimum and maximum commitment amounts
- Whether the offer is a standard, trial, or promotional offer

Looking up a product code applies only to the price sheet. To identify the Flex Plan that covered usage in your cost and usage details, use the `benefitId` column instead. For more information, see [Understand price factors and supplemental charge details](../../automate/understand-price-factors-supplemental-charge-details#identify-flex-plan-charges).