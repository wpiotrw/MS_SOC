---
layout: Conceptual
title: View Flex Plan costs and usage in Cost Management - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/benefits/flex-plan/view-flex-plan-costs
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
description: Learn how to see Flex Plan purchases, the usage a Flex Plan covers, and the products and resources that use it in cost analysis, budgets, exports, and downloads.
author: Britt-Henderson
ms.author: britth
ms.reviewer: vikdesai
ms.service: cost-management-billing
ms.subservice: cost-management
ms.topic: how-to
ms.date: 2026-11-19T00:00:00.0000000Z
locale: en-us
document_id: 9541a511-280b-713a-18b8-0489a47adde4
document_version_independent_id: 20b20366-c0ce-eb23-b43b-96d5f57a9631
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/benefits/flex-plan/view-flex-plan-costs.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/benefits/flex-plan/view-flex-plan-costs
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/benefits/flex-plan/view-flex-plan-costs.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
platformId: 2259d026-54e5-4b73-7586-a0a4fe8e5a6f
---

# View Flex Plan costs and usage in Cost Management - Microsoft Cost Management | Microsoft Learn

After you buy a Flex Plan, use Cost Management to see the purchase, the usage that the plan covers, and the usage that's billed at on-demand rates instead. This article shows you how to do that in cost analysis, how to get alerts with budgets, and how to get the detailed data with exports and downloads.

To see how much of a Flex Plan's commitment is used and how much is left, use the Flex Plans page in the Azure portal. For more information, see [Manage a Flex Plan](manage-flex-plan).

## Prerequisites

- A Microsoft Customer Agreement (MCA) or Microsoft Partner Agreement (MPA) billing account with a Flex Plan. Flex Plan isn't available for Enterprise Agreement (EA) or Cloud Solution Provider (CSP) subscriptions.
- Access to cost data at the billing account or billing profile scope, such as the billing account reader or billing profile reader role. For more information, see [Understand and work with scopes](../../costs/understand-work-scopes).

## How Flex Plan costs appear

Cost Management shows Flex Plan costs in two views:

| Charge | Actual cost | Amortized cost |
| --- | --- | --- |
| Flex Plan purchase (`Purchase` charge type) | The amount billed for the commitment | Not included. |
| Usage that the Flex Plan covers (`Usage` charge type) | Zero | The usage cost at the Flex Plan price |

Use actual cost to reconcile your invoice. Use amortized cost to see and allocate the cost of the usage that each plan covers.

In both views, the pricing model is **FlexPlan** for the purchase and for the usage that a Flex Plan covers. Usage that no Flex Plan covers keeps its usual pricing model, such as **OnDemand**.

## View your Flex Plan purchases

1. In the Azure portal, go to **Cost Management** and select your billing account or billing profile scope.
2. Select **Cost analysis**, and then select **Actual cost**.
3. Add a filter for **Pricing model** set to **FlexPlan** and a filter for **Charge type** set to **Purchase**.
4. Group by **Benefit** to see each Flex Plan purchase and its amount.

To see the commitment, term, and status behind a purchase, open the Flex Plan with the same name or ID on the Flex Plans page. For more information, see [Manage a Flex Plan](manage-flex-plan).

## See how much usage your Flex Plans cover

1. In **Cost analysis**, select **Amortized cost**.
2. Add a filter for **Charge type** set to **Usage**.
3. Group by **Pricing model**.

Usage with the **FlexPlan** pricing model is covered by a Flex Plan. Usage with other pricing models, such as **OnDemand**, isn't covered and is billed at its usual rate.

## See which products, meters, and resources use your Flex Plans

1. In **Cost analysis**, select **Amortized cost**.
2. Add a filter for **Charge type** set to **Usage** and a filter for **Pricing model** set to **FlexPlan**.
3. Group by **Product**, **Meter category**, **Meter**, or **Resource**.

If you have more than one Flex Plan, group by **Benefit** to see the usage that each plan covers.

## Get alerts about Flex Plan spending

Flex Plans send built-in notifications as you use the commitment and before the plan expires. For more information, see [Manage a Flex Plan](manage-flex-plan).

To get alerts at thresholds that you choose, create a budget in Cost Management for the scope that the Flex Plan covers, and set alert conditions, such as 50%, 80%, and 100% of the budget amount. Budgets track cost, not the commitment that's left on a specific Flex Plan. For more information, see [Create and manage budgets](../../costs/tutorial-acm-create-budgets).

## Export Flex Plan cost and usage data

To analyze Flex Plan data in your own tools, export cost and usage details.

1. In **Cost Management**, select **Exports**, and then select **Create**.
2. Select **Cost and usage details (actual)** or **Cost and usage details (amortized)**.
3. For the dataset version, select **2026-10-01**.
4. Select a storage account and a schedule, and then create the export.

For more information, see [Create and manage exports](../../costs/tutorial-improved-exports).

Every dataset version shows `FlexPlan` in the `pricingModel` column. Version 2026-10-01 adds the `priceFactors` column, which shows the Flex Plan offer that set each price.

You can also download a usage file from the Azure portal. A downloaded usage file doesn't use dataset version 2026-10-01, but it includes the `priceFactors` and `supplementalChargeDetails` columns at the end of the file. For more information, see [View and download your Azure usage and charges](../../understand/download-azure-daily-usage) and [Compare downloads and exports](../../understand/compare-downloads-exports).

These columns identify Flex Plan data in the export or download:

| Column | What it tells you |
| --- | --- |
| `chargeType` | `Purchase` for a Flex Plan purchase. `Usage` for usage that a Flex Plan covered. |
| `pricingModel` | `FlexPlan` for a Flex Plan purchase and for usage that a Flex Plan covered. |
| `benefitId`, `benefitName` | The Flex Plan that covered the usage. To see the plan's commitment, term, and remaining balance, open the plan in the Azure portal. |
| `priceFactors` | The price adjustments that applied, including a `FlexPlan` factor for usage that a Flex Plan covered. |

For more information, see [Understand price factors and supplemental charge details](../../automate/understand-price-factors-supplemental-charge-details#identify-flex-plan-charges) and [Microsoft Customer Agreement cost and usage details file schema](../../dataset-schema/cost-usage-details-mca).