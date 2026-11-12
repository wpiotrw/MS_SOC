---
layout: Conceptual
title: Microsoft Customer Agreement (MCA) price sheet schema - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/dataset-schema/price-sheet-mca
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
description: Learn about the data fields available in the Microsoft Customer Agreement price sheet.
author: vikramdesai01
ms.reviewer: vikdesai
ms.service: cost-management-billing
ms.subservice: common
ms.topic: reference
ms.date: 2026-11-10T00:00:00.0000000Z
ms.author: vikdesai
locale: en-us
document_id: 59b3bde7-ea03-5755-f2a7-e900298b24c4
document_version_independent_id: e0a9d1b8-43a1-288f-8495-a98e28c361ce
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/dataset-schema/price-sheet-mca.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../costs/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/dataset-schema/price-sheet-mca
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/dataset-schema/price-sheet-mca.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c0439c36-80e3-415f-8e4c-6951e3f1b136
- https://authoring-docs-microsoft.poolparty.biz/devrel/6ab7faaf-d791-4a26-96a2-3b11738538e7
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/2812d699-d85f-4a7f-839d-44e218b35d24
- https://authoring-docs-microsoft.poolparty.biz/devrel/302e28b0-1f09-4811-9a9b-2a72e0770581
platformId: cb3cffe9-16eb-cf7d-c474-97115853a51a
---

# Microsoft Customer Agreement (MCA) price sheet schema - Microsoft Cost Management | Microsoft Learn

This article lists the data fields in each version of the Microsoft Customer Agreement price sheet. The latest version is 2026-10-01.

## Version 2026-10-01

Here's the list of all of the data fields found in your price sheet.

| **Column** | **Field Name** | **Description** |
| --- | --- | --- |
| 1 | basePrice | The unit price at the time the customer signs the agreement. Or, the unit price at the time that the service meter becomes generally available (GA) if GA is after the agreement is signed. |
| 2 | billingAccountId | Unique identifier for the billing account. |
| 3 | billingAccountName | Name of the billing account. |
| 4 | billingCurrency | Currency in which charges are posted. |
| 5 | billingProfileId | Unique identifier of the EA enrollment, pay-as-you-go subscription or MCA billing profile. |
| 6 | billingProfileName | Name of the billing profile that is set up to receive invoices. The prices in the price sheet are associated with this billing profile. |
| 7 | currency | Currency in which all the prices are reflected. |
| 8 | effectiveEndDate | End date of the price sheet billing period. |
| 9 | effectiveStartDate | Start date of the price sheet billing period. |
| 10 | marketPrice | The current list price for a given product or service. The price is without any negotiations and is based on your Microsoft Agreement type. For PriceType *Consumption*, marketPrice is reflected as the pay-as-you-go price. For PriceType *Savings Plan*, market price reflects the Savings plan benefit on top of pay-as-you-go price for the corresponding commitment term. For PriceType *ReservedInstance*, marketPrice reflects the total price of the one or three-year commitment. |
| 11 | meterId | Unique identifier for the meter. |
| 12 | meterCategory | Name of the classification category for the meter. For example, *Cloud services*, and *Networking* |
| 13 | meterName | The name of the meter. Purchases and Marketplace usage might be shown as blank or unassigned. |
| 14 | meterSubCategory | Name of the meter subclassification category. Purchases and Marketplace usage might be shown as blank or unassigned. |
| 15 | meterType | Name of the meter type. |
| 16 | meterRegion | The name of the Azure region associated with the meter. It generally aligns with the resource location, except for certain global meters that are shared across regions. In such cases, the meter region indicates the primary region of the meter. The meter is used to track the usage of specific services or resources, mainly for billing purposes. Each Azure service, resource, and region have its own billing meter ID that precisely reflects how its consumption and price are calculated. |
| 17 | priceType | Price type for a product. For example, an Azure resource has its pay-as-you-go rate with priceType as *Consumption*. If the resource is eligible for a savings plan, it also has its savings plan rate with another priceType as *SavingsPlan*. Other priceTypes include *ReservedInstance*. |
| 18 | Product | Name of the product accruing the charges. For example, Basic SQL DB vs Standard SQL DB. |
| 19 | productId | Unique identifier for the product. |
| 20 | productOrderName | Name of the purchased product plan. Indicates if this pricing is standard Azure Plan pricing, Dev/Test pricing etc. |
| 21 | serviceFamily | Service family that the service belongs to. |
| 22 | SkuId | Unique identifier of the SKU. |
| 23 | Term | Duration associated with priceType. For example, SavingsPlan priceType has two commitment options: one year and three years. The Term is *P1Y* for a one-year commitment and *P3Y* for a three-year commitment. |
| 24 | tierMinimumUnits | Defines the lower bound of the tier range for which prices are defined. For example, if the range is 0 to 100, tierMinimumUnits would be 0. |
| 25 | unitOfMeasure | The unit of measure for billing for the service. For example, compute services are billed per hour. |
| 26 | unitPrice | The per-unit price at the time of billing for a given product or service. It includes any negotiated discounts on top of the market price. For PriceType *ReservedInstance*, unitPrice reflects the total cost of the one or three-year commitment including discounts. **Note**: The unit price isn't the same as the effective price in usage details downloads when services have differential prices across tiers. If services have multi-tiered pricing, the effective price is a blended rate across the tiers and doesn't show a tier-specific unit price. The blended price or effective price is the net price for the consumed quantity spanning across the multiple tiers, where each tier has a specific unit price. |
| 27 | priceFactors | JSON array listing the factors affecting the price, such as benefits applied. When multiple factors apply, factors in the same group are combined while factors in separate groups are applied in sequence. Each factor includes a product code, which can be joined to product data to identify the benefit. Empty when standard market price applies. |

## Version 2024-08-01

Heres the list of all of the data fields found in your price sheet.

| **Column** | **Field Name** | **Description** |
| --- | --- | --- |
| 1 | basePrice | The unit price at the time the customer signs the agreement. Or, the unit price at the time that the service meter becomes generally available (GA) if GA is after the agreement is signed. |
| 2 | billingAccountId | Unique identifier for the billing account. |
| 3 | billingAccountName | Name of the billing account. |
| 4 | billingCurrency | Currency in which charges are posted. |
| 5 | billingProfileId | Unique identifier of the EA enrollment, pay-as-you-go subscription or MCA billing profile. |
| 6 | billingProfileName | Name of the billing profile that is set up to receive invoices. The prices in the price sheet are associated with this billing profile. |
| 7 | currency | Currency in which all the prices are reflected. |
| 8 | effectiveEndDate | End date of the price sheet billing period. |
| 9 | effectiveStartDate | Start date of the price sheet billing period. |
| 10 | marketPrice | The current list price for a given product or service. The price is without any negotiations and is based on your Microsoft Agreement type. For PriceType *Consumption*, marketPrice is reflected as the pay-as-you-go price. For PriceType *Savings Plan*, market price reflects the Savings plan benefit on top of pay-as-you-go price for the corresponding commitment term. For PriceType *ReservedInstance*, marketPrice reflects the total price of the one or three-year commitment. |
| 11 | meterId | Unique identifier for the meter. |
| 12 | meterCategory | Name of the classification category for the meter. For example, *Cloud services*, and *Networking* |
| 13 | meterName | The name of the meter. Purchases and Marketplace usage might be shown as blank or unassigned. |
| 14 | meterSubCategory | Name of the meter subclassification category. Purchases and Marketplace usage might be shown as blank or unassigned. |
| 15 | meterType | Name of the meter type. |
| 16 | meterRegion | The name of the Azure region associated with the meter. It generally aligns with the resource location, except for certain global meters that are shared across regions. In such cases, the meter region indicates the primary region of the meter. The meter is used to track the usage of specific services or resources, mainly for billing purposes. Each Azure service, resource, and region have its own billing meter ID that precisely reflects how its consumption and price are calculated. |
| 17 | priceType | Price type for a product. For example, an Azure resource has its pay-as-you-go rate with priceType as *Consumption*. If the resource is eligible for a savings plan, it also has its savings plan rate with another priceType as *SavingsPlan*. Other priceTypes include *ReservedInstance*. |
| 18 | Product | Name of the product accruing the charges. For example, Basic SQL DB vs Standard SQL DB. |
| 19 | productId | Unique identifier for the product. |
| 20 | productOrderName | Name of the purchased product plan. Indicates if this pricing is standard Azure Plan pricing, Dev/Test pricing etc. |
| 21 | serviceFamily | Service family that the service belongs to. |
| 22 | SkuId | Unique identifier of the SKU. |
| 23 | Term | Duration associated with priceType. For example, SavingsPlan priceType has two commitment options: one year and three years. The Term is *P1Y* for a one-year commitment and *P3Y* for a three-year commitment. |
| 24 | tierMinimumUnits | Defines the lower bound of the tier range for which prices are defined. For example, if the range is 0 to 100, tierMinimumUnits would be 0. |
| 25 | unitOfMeasure | The unit of measure for billing for the service. For example, compute services are billed per hour. |
| 26 | unitPrice | The per-unit price at the time of billing for a given product or service. It includes any negotiated discounts on top of the market price. For PriceType *ReservedInstance*, unitPrice reflects the total cost of the one or three-year commitment including discounts. **Note**: The unit price isn't the same as the effective price in usage details downloads when services have differential prices across tiers. If services have multi-tiered pricing, the effective price is a blended rate across the tiers and doesn't show a tier-specific unit price. The blended price or effective price is the net price for the consumed quantity spanning across the multiple tiers, where each tier has a specific unit price. |

## Version 2023-05-01

Heres the list of all of the data fields found in your price sheet.

| **Column** | **Field Name** | **Description** |
| --- | --- | --- |
| 1 | basePrice | The unit price at the time the customer signs the agreement. Or, the unit price at the time that the service meter becomes generally available (GA) if GA is after the agreement is signed. |
| 2 | billingAccountId | Unique identifier for the billing account. |
| 3 | billingAccountName | Name of the billing account. |
| 4 | billingCurrency | Currency in which charges are posted. |
| 5 | billingProfileId | Unique identifier of the EA enrollment, pay-as-you-go subscription or MCA billing profile. |
| 6 | billingProfileName | Name of the billing profile that is set up to receive invoices. The prices in the price sheet are associated with this billing profile. |
| 7 | currency | Currency in which all the prices are reflected. |
| 8 | discount | The price discount offered for Graduation Tier, Free Tier, Included Quantity, or Negotiated discounts when applicable. Represented as a percentage. Not available in the updated version of the price sheet. |
| 9 | effectiveEndDate | End date of the price sheet billing period. |
| 10 | effectiveStartDate | Start date of the price sheet billing period. |
| 11 | includedQuantity | Quantities of a specific service to which a customer is entitled to consume without incremental charges. Not available in the updated version of the price sheet. |
| 12 | marketPrice | The current list price for a given product or service. The price is without any negotiations and is based on your Microsoft Agreement type. For PriceType *Consumption*, marketPrice is reflected as the pay-as-you-go price. For PriceType *Savings Plan*, market price reflects the Savings plan benefit on top of pay-as-you-go price for the corresponding commitment term. For PriceType *ReservedInstance*, marketPrice reflects the total price of the one or three-year commitment. |
| 13 | meterId | Unique identifier for the meter. |
| 14 | meterCategory | Name of the classification category for the meter. For example, *Cloud services*, and *Networking* |
| 15 | meterName | The name of the meter. Purchases and Marketplace usage might be shown as blank or unassigned. |
| 16 | meterSubCategory | Name of the meter subclassification category. Purchases and Marketplace usage might be shown as blank or unassigned. |
| 17 | meterType | Name of the meter type. |
| 18 | meterRegion | The name of the Azure region associated with the meter. It generally aligns with the resource location, except for certain global meters that are shared across regions. In such cases, the meter region indicates the primary region of the meter. The meter is used to track the usage of specific services or resources, mainly for billing purposes. Each Azure service, resource, and region have its own billing meter ID that precisely reflects how its consumption and price are calculated. |
| 19 | priceType | Price type for a product. For example, an Azure resource has its pay-as-you-go rate with priceType as *Consumption*. If the resource is eligible for a savings plan, it also has its savings plan rate with another priceType as *SavingsPlan*. Other priceTypes include *ReservedInstance*. |
| 20 | Product | Name of the product accruing the charges. For example, Basic SQL DB vs Standard SQL DB. |
| 21 | productId | Unique identifier for the product. |
| 22 | serviceFamily | Service family that the service belongs to. |
| 23 | SkuId | Unique identifier of the SKU. |
| 24 | Term | Duration associated with priceType. For example, SavingsPlan priceType has two commitment options: one year and three years. The Term is *P1Y* for a one-year commitment and *P3Y* for a three-year commitment. |
| 25 | tierMinimumUnits | Defines the lower bound of the tier range for which prices are defined. For example, if the range is 0 to 100, tierMinimumUnits would be 0. |
| 26 | unitOfMeasure | The unit of measure for billing for the service. For example, compute services are billed per hour. |
| 27 | unitPrice | The per-unit price at the time of billing for a given product or service. It includes any negotiated discounts on top of the market price. For PriceType *ReservedInstance*, unitPrice reflects the total cost of the one or three-year commitment including discounts. **Note**: The unit price isn't the same as the effective price in usage details downloads when services have differential prices across tiers. If services have multi-tiered pricing, the effective price is a blended rate across the tiers and doesn't show a tier-specific unit price. The blended price or effective price is the net price for the consumed quantity spanning across the multiple tiers, where each tier has a specific unit price. |