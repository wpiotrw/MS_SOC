---
layout: Conceptual
title: Terms in your Microsoft Customer Agreement price sheet - Azure - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/mca-understand-pricesheet
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/118/azure-cost-management/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/ebeaa30a-2425-ec11-b6e6-000d3a4f0f84
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
description: Learn how to read and understand your usage and bill for a Microsoft Customer Agreement.
author: diberry
ms.service: cost-management-billing
ms.subservice: billing
ms.topic: reference
ms.date: 2026-11-19T00:00:00.0000000Z
ms.author: jkinma
ms.reviewer: jkinma
ms.custom:
- build-2025
service.tree.id: 95459a4b-434c-4f83-879b-aa5f509fc7fa
locale: en-us
document_id: 4cfadc03-d120-5268-e709-fe0b582d111b
document_version_independent_id: fe521a00-2ef6-f560-1ebc-230450ddb26a
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/manage/mca-understand-pricesheet.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/manage/mca-understand-pricesheet
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/manage/mca-understand-pricesheet.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 41adadb6-4bda-fe2c-3e72-71d77ecdba3b
---

# Terms in your Microsoft Customer Agreement price sheet - Azure - Microsoft Cost Management | Microsoft Learn

This article applies to an Azure billing account for a Microsoft Customer Agreement. Check if you have access to a Microsoft Customer Agreement.

If you're a billing profile Owner, Contributor, Reader, or Invoice Manager you can download your organization's price sheet from the Azure portal. See [View and download your organization's pricing](ea-pricing).

You can't select a schema version for a downloaded price sheet. When new columns are added, such as `priceFactors`, they're added at the end of the file. To select a dataset version, such as 2026-10-01, use exports. For more information, see [Compare downloads and exports](../understand/compare-downloads-exports).

## Terms and descriptions in your price sheet

The following section describes the important terms shown in your Microsoft Customer Agreement price sheet.

| **Field Name** | **Description** |
| --- | --- |
| basePrice | The unit price at the time the customer signs the agreement. Or, the unit price at the time that the service meter becomes generally available (GA) if GA is after the agreement is signed. |
| billingAccountId | Unique identifier for the billing account. |
| billingAccountName | Name of the billing account. |
| billingCurrency | Currency in which charges are posted |
| billingProfileId | Unique identifier for the billing profile. |
| billingProfileName | Name of the billing profile that is set up to receive invoices. The prices in the price sheet are associated with this billing profile. |
| currency | Currency in which all the prices are reflected. |
| discount | The price discount offered for Graduation Tier, Free Tier, Included Quantity, or discounts when applicable. Represented as a percentage. Not available in the updated version of the price sheet. |
| effectiveEndDate | End date of the price sheet billing period. |
| effectiveStartDate | Start date of the price sheet billing period. |
| includedQuantity | Quantities of a specific service to which a customer is entitled to consume without incremental charges. Not available in the updated version of the price sheet. |
| marketPrice | The current list price for a given product or service. The price is without any discounts and is based on your Microsoft Agreement type. For `PriceType`*Consumption*, marketPrice is reflected as the pay-as-you-go price. For `PriceType`*Savings Plan*, market price reflects the Savings plan benefit on top of pay-as-you-go price for the corresponding commitment term. For `PriceType`*ReservedInstance*, marketPrice reflects the total price of the one or three-year commitment. |
| meterId | Unique identifier for the meter. |
| meterCategory | Name of the classification category for the meter. For example, *Cloud services*, and *Networking* |
| meterName | Name of the meter. The meter represents the deployable resource of an Azure service. |
| meterSubCategory | Name of the meter subclassification category. |
| meterType | Name of the meter type. |
| meterRegion | Name of the region where the meter for the service is available. Identifies the location of the datacenter for certain services that are priced based on datacenter location. |
| priceType | Price type for a product. For example, an Azure resource has its pay-as-you-go rate with `priceType` as *Consumption*. If the resource is eligible for a savings plan, it also has its savings plan rate with another `priceType` as *SavingsPlan*. If the product is covered by a Flex Plan offer, it also has a Flex Plan rate for each offer, with `priceType` as *FlexPlan*. Other `priceTypes` include *ReservedInstance*. |
| Product | Name of the product accruing the charges. For example, Basic SQL DB vs Standard SQL DB. |
| productId | Unique identifier for the product whose meter is consumed. |
| productOrderName | Name of the purchased product plan. Not applicable for price sheets dated December 2022 and later. |
| serviceFamily | Type of Azure service. For example, Compute, Analytics, and Security. |
| SkuID | Unique identifier of the SKU. |
| Term | Duration of the term for reservation, savings plan, and Flex Plan prices, in ISO 8601 format. Terms can be any length that the offer defines, such as *P1M* (one month), *P2M* (two months), *P1Y* (one year), or *P3Y* (three years). |
| tierMinimumUnits | Defines the lower bound of the tier range for which prices are defined. For example, if the range is 0 to 100, tierMinimumUnits would be 0. |
| unitOfMeasure | Identifies the units of measure for billing for the service. For example, compute services are billed per hour. |
| unitPrice | The per-unit price at the time of billing for a given product or service. It includes any discounts on top of the market price. For `PriceType`*ReservedInstance*, `unitPrice` reflects the total cost of the one or three-year commitment including discounts. **Note**: The unit price isn't the same as the effective price in usage details downloads when services have differential prices across tiers. If services have multi-tiered pricing, the effective price is a blended rate across the tiers and doesn't show a tier-specific unit price. The blended price or effective price is the net price for the consumed quantity spanning across the multiple tiers, where each tier has a specific unit price. |
| priceFactors | JSON array that lists the factors that set the price, such as a savings plan or Flex Plan. Empty for consumption prices. For a Flex Plan price, it includes the product code of the Flex Plan offer. This column appears at the end of the downloaded file. For more information, see [Understand price factors and supplemental charge details](../automate/understand-price-factors-supplemental-charge-details). |

## Check access to a Microsoft Customer Agreement

To determine whether you have access to a billing account for a Microsoft Customer Agreement, check the agreement type:

1. Go to the Azure portal. Search for and select **Cost Management + Billing**.

    [![Screenshot that shows a search for Cost Management + Billing.](../../includes/media/billing-check-mca/billing-search-cost-management-billing.png)](../../includes/media/billing-check-mca/billing-search-cost-management-billing.png#lightbox)
2. If you have access to just one billing scope, select **Settings** &gt; **Properties**. You have access to a billing account for a Microsoft Customer Agreement if the billing account type is **Microsoft Customer Agreement**.

    [![Screenshot of the Azure portal that shows a billing account type of Microsoft Customer Agreement for a single billing scope.](../../includes/media/billing-check-mca/billing-mca-property.png)](../../includes/media/billing-check-mca/billing-mca-property.png#lightbox)

    If you have access to multiple billing scopes, check the type in the **Billing account type** column. You have access to a billing account for a Microsoft Customer Agreement if the billing account type for any of the scopes is **Microsoft Customer Agreement**.

    [![Screenshot of the Azure portal that shows a billing account type of Microsoft Customer Agreement for multiple billing scopes.](../../includes/media/billing-check-mca/billing-mca-in-the-list.png)](../../includes/media/billing-check-mca/billing-mca-in-the-list.png#lightbox)

## Need help? Contact us.

If you have questions or need help, [create a support request](https://go.microsoft.com/fwlink/?linkid=2083458).