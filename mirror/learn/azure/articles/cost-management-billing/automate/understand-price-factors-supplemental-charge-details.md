---
layout: Conceptual
title: Understand price factors and supplemental charge details - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/automate/understand-price-factors-supplemental-charge-details
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
description: Learn how to read the priceFactors and supplementalChargeDetails columns in cost and usage details and price sheet data, including Flex Plan prices and Flex Plan and Spot Plus charges.
author: Britt-Henderson
ms.author: britth
ms.reviewer: vikdesai
ms.service: cost-management-billing
ms.subservice: cost-management
ms.topic: concept-article
ms.date: 2026-11-23T00:00:00.0000000Z
locale: en-us
document_id: b2a5a88a-0d55-f96f-5ece-e20e051ddd3d
document_version_independent_id: 964e2695-8c0f-167c-2108-6bef7705368c
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/automate/understand-price-factors-supplemental-charge-details.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../costs/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/automate/understand-price-factors-supplemental-charge-details
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/automate/understand-price-factors-supplemental-charge-details.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c0439c36-80e3-415f-8e4c-6951e3f1b136
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/2812d699-d85f-4a7f-839d-44e218b35d24
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
platformId: 1971dba2-1134-add3-03fe-39787a1770fd
---

# Understand price factors and supplemental charge details - Microsoft Cost Management | Microsoft Learn

Cost and usage details and price sheet data include a `priceFactors` column. Cost and usage details also include a `supplementalChargeDetails` column. Use these columns to see how a charge or price was set, for example, whether a contracted price, a savings plan, a Flex Plan, or a Spot Plus discount applied.

## Where the columns appear

| Dataset | Agreement types | Columns added in version 2026-10-01 |
| --- | --- | --- |
| Cost and usage details | EA, MCA, MPA, CSP | `priceFactors`, `supplementalChargeDetails` |
| Price sheet | EA, MCA | `priceFactors` |

How you get the columns depends on how you get your data:

- **Exports**: The columns are available in dataset version 2026-10-01. Older dataset versions don't include them. To get the columns, create or update an export and select dataset version 2026-10-01. For more information, see [Create and manage exports](../costs/tutorial-improved-exports).
- **Downloads**: Usage files and price sheets that you download from the Azure portal, or by using the download APIs, don't use dataset version 2026-10-01. Their version doesn't change. Instead, the new columns are added at the end of the file.

Flex Plan is available for Microsoft Customer Agreement (MCA) and Microsoft Partner Agreement (MPA) billing accounts. Enterprise Agreement (EA) data doesn't include Flex Plan prices, charges, or factors.

## Understand `priceFactors`

The `priceFactors` column is a JSON array that describes how the price you were charged or quoted was set, such as the best price available to you or a benefit that applied. In the price sheet, the column describes the benefits that are associated with a price, such as a savings plan or a Flex Plan. It's empty when none apply. In cost and usage details, a usage charge can have one or more factors. The column can be empty, for example, when the market price applies with no adjustment.

Each item in the array is a group that contains a `Factors` array. Each factor has these properties:

| Property | Description |
| --- | --- |
| `Type` | The kind of adjustment, such as `SavingsPlan`, `FlexPlan`, or `DynamicPrice`. Compare values without regard to case. |
| `Extensions` | Details for that type of adjustment, such as the `ProductCode` of the benefit or offer. The properties depend on the type. |

A factor can appear as a JSON object or as a JSON string that contains the object. Before you read a factor's properties, check whether it's a string, and if it is, parse it as JSON.

The following example shows a Flex Plan price in the price sheet, where the factor is a JSON object:

```json
[
  {
    "Factors": [
      {
        "Type": "FlexPlan",
        "Extensions": {
          "ProductCode": "<product-code>"
        }
      }
    ]
  }
]
```

The following example shows usage that a Flex Plan covered in cost and usage details, where the factor is a JSON string:

```json
[
  {
    "Factors": [
      "{\"Type\":\"FlexPlan\",\"Extensions\":{\"ProductCode\":\"<product-code>\",\"BenefitId\":\"<benefit-id>\",\"BenefitOrderId\":\"<benefit-order-id>\"}}"
    ]
  }
]
```

### How factors combine

In cost and usage details, groups and factors show how adjustments were applied to the market price:

- Factors in the same group apply together. Their discounts add together.
- Groups apply in order. Each group applies to the price that results from the previous group.

In the price sheet, all factors for a price are in the first group. The grouping and order of factors don't show how the factors combine or the order in which they apply. Use each factor's `Type` and `Extensions` to understand it.

### Factor types

| Type | Meaning | Appears in | Extensions |
| --- | --- | --- | --- |
| `BestOfPrice` | Your contracted price, or the best of the prices available to you that don't come from a benefit, was used. `PriceType` names the price that was used, such as `EffectivePrice` or `MarketPrice`. | Cost and usage details | `PriceType` |
| `SavingsPlan` | A savings plan commitment applies. | Cost and usage details, price sheet | Cost and usage details: `ProductCode`, `BenefitId`, `BenefitOrderId`. Price sheet: `ProductCode`. |
| `FlexPlan` | A Flex Plan commitment applies. Appears only for MCA and MPA. | Cost and usage details, price sheet | Cost and usage details: `ProductCode`, `BenefitId`, `BenefitOrderId`. Price sheet: `ProductCode`. |
| `AzurePromotion` | A consumption promotion applies. | Price sheet | `ProductCode` |
| `Credit` | A sponsorship credit applies. | Cost and usage details | `ProductCode`, `BenefitId`, `BenefitOrderId`, `PriceType` |
| `DynamicPrice` | A price adjustment applies to the usage, such as a Spot Plus discount. | Cost and usage details | `SubType`, `ValueType`, `Value` |

In cost and usage details, `BenefitId` and `BenefitOrderId` identify the savings plan, Flex Plan, promotion, or credit that applied to the usage. In the price sheet, `SavingsPlan`, `FlexPlan`, and `AzurePromotion` factors include only `ProductCode`, because a price isn't tied to a specific purchase. The `Extensions` properties that appear depend on the factor type, and a property can be missing or `null`. Check for a property before you use it.

For a `DynamicPrice` factor, `SubType` identifies the program, such as `SpotPlus`. `ValueType` describes how to read `Value`. For example, when `ValueType` is `DiscountPercentage`, a `Value` of `0.15` means a 15% discount. To see which price the discount applies to, check `priceTarget` in the matching price modifier in `supplementalChargeDetails`.

Other factor types and subtypes can appear. Design reports and scripts to handle values they don't recognize.

## Understand `supplementalChargeDetails`

The `supplementalChargeDetails` column contains a JSON object, stored as text, with supplemental pricing details for a charge. It's empty when no supplemental details apply, such as for a typical on-demand charge. This column appears only in cost and usage details, not in the price sheet. When the column has a value, it contains one of the following:

| When | What the column contains |
| --- | --- |
| A price modifier applies to the charge, such as a Spot Plus discount | An `ExternalizedPrice` object with a `priceModifiers` array. Each modifier has an `id`, `value`, `modifier`, and `priceTarget`. The `id` matches the `SubType` of the `DynamicPrice` factor in `priceFactors`. `modifier` describes the kind of adjustment, such as `discount`. Compare it without regard to case. `priceTarget` names the price that the modifier applies to, such as `RetailPrice`. |
| A cost or quantity cap was applied to the charge | `{"CapApplied": true}` |

The following example shows a Spot Plus discount of 15% that applies to the retail price:

```json
{
  "ExternalizedPrice": {
    "priceModifiers": [
      {
        "id": "SpotPlus",
        "value": 0.15,
        "modifier": "discount",
        "priceTarget": "RetailPrice"
      }
    ]
  }
}
```

## Uses for `priceFactors` and `supplementalChargeDetails`

The `priceFactors` and `supplementalChargeDetails` fields are useful for identifying prices and charges that are associated with benefits such as Flex Plan and Spot Plus.

## Identify Flex Plan charges

| To find | Look for |
| --- | --- |
| A Flex Plan purchase | `chargeType` is `Purchase` and `pricingModel` is `FlexPlan`. |
| Usage that a Flex Plan covered | `chargeType` is `Usage` and `pricingModel` is `FlexPlan`. `priceFactors` has a `FlexPlan` factor. |
| The Flex Plan that covered the usage | `benefitId`. To see the plan's commitment, term, and remaining balance, open the plan in the Azure portal. For more information, see [Manage a Flex Plan](../benefits/flex-plan/manage-flex-plan#open-a-flex-plan). |

To identify the Flex Plan that covered usage, use `benefitId`. The `ProductCode` in a `FlexPlan` factor identifies the Flex Plan offer, not the plan that you bought. Looking up a product code, as described in Identify Flex Plan prices in the price sheet, applies only to the price sheet.

In actual cost, a Flex Plan purchase shows its cost, and usage that the plan covers shows zero cost. Amortized cost doesn't include the purchase. Instead, usage that the plan covers shows the amount drawn from the plan, so you can allocate it to the subscriptions, resource groups, and resources that used the plan.

`pricingModel` isn't limited to dataset version 2026-10-01, so you can identify Flex Plan charges in earlier dataset versions too. In exports, you need version 2026-10-01 only for `priceFactors` and `supplementalChargeDetails`.

## Identify Flex Plan prices in the price sheet

Flex Plan prices appear as separate rows for each meter that a Flex Plan offer covers. Compared with the consumption row for the same meter, a Flex Plan row has:

- `priceType` set to `FlexPlan`.
- `term` set to the term of the Flex Plan offer, such as `P1M` or `P1Y`.
- `priceFactors` with the product code of the Flex Plan offer.

If more than one Flex Plan offer covers a meter, the price sheet has a row for each offer. The rows can have the same price and term and differ only in the product code.

To see details about an offer in the price sheet, such as its terms and its minimum and maximum commitment amounts, look up its product code. For more information, see [Discover available offers and prices](../benefits/flex-plan/automate-flex-plan#discover-available-offers-and-prices).

## Identify Spot Plus charges

[Spot Plus](/en-us/azure/virtual-machines/spot-plus-public-preview-azure-compute-technical) is a tier of Azure Spot Virtual Machines. In cost and usage details, look for these values:

| To find | Look for |
| --- | --- |
| Spot Plus usage and its discount | A `priceFactors` factor with `Type` set to `DynamicPrice` and `Extensions.SubType` set to `SpotPlus`. When `Extensions.ValueType` is `DiscountPercentage`, `Extensions.Value` is the discount. |
| The Spot Plus price modifier | A `supplementalChargeDetails` price modifier with `id` set to `SpotPlus`. |

The following example shows a Spot Plus discount of 15% in `priceFactors`:

```json
[
  {
    "Factors": [
      "{\"Type\":\"DynamicPrice\",\"Extensions\":{\"SubType\":\"SpotPlus\",\"ValueType\":\"DiscountPercentage\",\"Value\":0.15}}"
    ]
  }
]
```