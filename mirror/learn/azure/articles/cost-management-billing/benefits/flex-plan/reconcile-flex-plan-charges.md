---
layout: Conceptual
title: Reconcile Flex Plan charges and calculate savings - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/benefits/flex-plan/reconcile-flex-plan-charges
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
description: Learn how to check that usage covered by a Flex Plan is charged at the price in your price sheet, and how to calculate what you saved compared with on-demand prices.
author: Britt-Henderson
ms.author: britth
ms.reviewer: vikdesai
ms.service: cost-management-billing
ms.subservice: cost-management
ms.topic: how-to
ms.date: 2026-11-23T00:00:00.0000000Z
locale: en-us
document_id: bbda208d-9ed9-f62f-b3cb-7588752d2a7c
document_version_independent_id: eb15b8fc-6e08-e14e-20a4-26b761ad46fc
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/benefits/flex-plan/reconcile-flex-plan-charges.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/benefits/flex-plan/reconcile-flex-plan-charges
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/benefits/flex-plan/reconcile-flex-plan-charges.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
platformId: 5c01804c-6ee3-89d4-90fb-0b1ec82355ee
---

# Reconcile Flex Plan charges and calculate savings - Microsoft Cost Management | Microsoft Learn

Use your cost and usage details and your price sheet to check that usage covered by a Flex Plan is charged at the right price, and to calculate how much you saved compared with on-demand prices.

## Prerequisites

- Amortized cost and usage details that include the `priceFactors` column. Export them with dataset version 2026-10-01, or download a usage file, which includes the column at the end of the file. For more information, see [View Flex Plan costs and usage in Cost Management](view-flex-plan-costs#export-flex-plan-cost-and-usage-data).
- A price sheet that includes the `priceFactors` column. Export it with dataset version 2026-10-01, or download it. For more information, see [Review Flex Plan prices in your price sheet](review-flex-plan-prices#get-your-price-sheet).

## Check that you're charged your Flex Plan price

1. In the cost and usage details, find a row where `pricingModel` is `FlexPlan` and `chargeType` is `Usage`. Note its `meterId`, `effectivePrice`, and the `ProductCode` of the `FlexPlan` factor in `priceFactors`.
2. In the price sheet, find the rows with the same `meterId` where `priceType` is `FlexPlan`.
3. Select the row whose `priceFactors` has the same `ProductCode`.
4. Compare the `effectivePrice` from the cost and usage details with the `unitPrice` from the price sheet.

To identify the Flex Plan that covered the usage, use `benefitId` in the cost and usage details, and then open the plan in the Azure portal. For more information, see [Manage a Flex Plan](manage-flex-plan).

## Calculate your savings

Savings depend on the currency of the cost columns that you use. Savings that you calculate in your billing currency can differ from savings that you calculate in another currency, such as your pricing currency. Use cost columns in the same currency for both parts of the calculation.

The following example calculates savings in your billing currency. Your amortized cost and usage details include the cost of each usage row at your Flex Plan price and at the market price, so you don't need to multiply prices by quantities. For each usage row that a Flex Plan covered:

*Savings in billing currency = `paygCostInBillingCurrency` − `costInBillingCurrency`*

1. In the amortized cost and usage details, keep the rows where `pricingModel` is `FlexPlan` and `chargeType` is `Usage`.
2. For each row, subtract `costInBillingCurrency`, the cost at your Flex Plan price, from `paygCostInBillingCurrency`, the cost at the market price.
3. Add up the results by month, product, or Flex Plan.

In this example, `paygCostInBillingCurrency` is based on the market price (`PayGPrice`), not your contracted price. To calculate savings in US dollars instead, use `paygCostInUsd` and `costInUsd`.

Cost Management doesn't show Flex Plan savings in cost analysis, so calculate them from your exported or downloaded data.

## Reconcile with your invoice

Your invoice shows the Flex Plan commitment that you pay for, not the usage that the plan covers. To reconcile the commitment with your invoice, use actual cost. For more information, see [Understand your Flex Plan bill](flex-plan-billing).