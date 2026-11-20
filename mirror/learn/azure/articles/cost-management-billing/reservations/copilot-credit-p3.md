---
layout: Conceptual
title: Copilot Credit P3 - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/copilot-credit-p3
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/118/azure-cost-management/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/f54500da-fd24-ec11-b6e6-000d3a4f07b8
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
description: Learn about Copilot Credit P3 in Azure reservations.
author: pri-mittal
ms.reviewer: primittal
ms.service: cost-management-billing
ms.subservice: reservations
ms.topic: how-to
ms.date: 2026-11-19T00:00:00.0000000Z
ms.author: primittal
locale: en-us
document_id: 9bf324e1-99de-01d1-b45f-51f920d720ad
document_version_independent_id: 7a0f4c3d-b11b-bc23-ba37-6b21ce1e9134
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/reservations/copilot-credit-p3.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/reservations/copilot-credit-p3
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/reservations/copilot-credit-p3.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 4f506637-ba18-41e5-1324-596b840d82c3
---

# Copilot Credit P3 - Microsoft Cost Management | Microsoft Learn

Important

**Changes to Copilot Credit pre-purchase plan availability starting January 1, 2027**

Starting January 1, 2027, you can buy or renew the Copilot Credit pre-purchase plan only through an Enterprise Agreement (EA) or a Cloud Solution Provider (CSP) partner. Buy online channels and built-in tiered volume discounts will no longer apply.

If you have a Microsoft Customer Agreement for enterprise (MCA-E), you can't buy or renew Copilot Credit pre-purchase plans starting January 1, 2027. Consider AI Flex Plan for your Microsoft AI portfolio instead. To learn more, see the [Flex Plan overview](../benefits/flex-plan/flex-plan-overview).

Save on your Copilot Credit costs when you buy a pre-purchase plan. Pre-purchase plans are commit units (CUs) bought at discounted tiers in your purchasing currency for a specific product. The more you buy, the greater the discount. Purchased CUs pay down qualifying costs in US dollars (USD). So, if Microsoft Copilot Studio generates a retail cost of $100 based on Copilot Credit usage, then 100 Copilot Credit CUs (CCCUs) are consumed.

Your Copilot Credit pre-purchase plan automatically uses your CCCUs to pay for eligible Copilot Credit usage during its one-year term or until Copilot Credit CUs run out. Your pre-purchase plan Copilot Credit CUs start paying for your Copilot usage without having to redeploy or reassign the plan. By default, plans are configured to renew at the end of the one-year term.

## Prerequisites

To buy a pre-purchase plan, you must have one of the following Azure subscriptions and roles:

- For an Azure subscription, the owner role or reservation purchaser role is required.
- For an Enterprise Agreement (EA) subscription, the [**Reserved Instances** policy option](../manage/direct-ea-administration#view-and-manage-enrollment-policies) must be enabled. To enable that policy option, you must be an EA administrator of the subscription.
- For a Cloud Solution Provider (CSP) subscription, follow one of these articles:
    - [Buy Azure reservations on behalf of a customer](/en-us/partner-center/customers/azure-reservations-buying)
    - [Allow the customer to buy their own reservations](/en-us/partner-center/customers/give-customers-permission)

## Determine the right size to buy

To get started, estimate your expected Copilot Credit usage. This helps you determine the appropriate size for your pre-purchase plan. Each pre-purchase plan has a one-year term.

For example, suppose you expect to consume 1,500,000 Copilot Credit with custom agents created in Microsoft Copilot Studio. Assuming the pay-as-you-go rate for Copilot Credit to be $0.01, then at the pay-as-you-go rate, this will cost $15,000. By purchasing Tier 2 (15,000 CU) pre-purchase plan, let's say the cost of that tier is $14,100, it will give a 6% saving compared to the pay-as-you-go rate for the same usage.

Note

Pre-purchase plan discounts don't combine with other discounts you might have. If you have additional discounts, the pre-purchase plan discount is applied independently, which may result in a lower effective discount rate than the listed tier percentage. Factor in your existing discounts when estimating savings.

## Purchase Copilot Credit commit units

Purchase Copilot Credit pre-purchase plans in the [Azure portal reservations](https://portal.azure.com/#view/Microsoft_Azure_Reservations/ReservationsBrowseBlade/productType/Reservations).

1. Go to the [Azure portal](https://portal.azure.com)
2. Navigate to the **Reservations** service.
3. On the **Purchase reservations page**, select **Copilot Credit Pre-Purchase Plan**.[![Screenshot showing Copilot Credit pre-purchase plan.](media/copilot-credit/copilot-credit.png)](media/copilot-credit/copilot-credit.png#lightbox)
4. On the **Select the product you want to purchase** page, select a subscription. Use the **Subscription** list to select the subscription used to pay for the reserved capacity. The payment method of the subscription is charged the upfront costs for the reserved capacity. Charges **not** are deducted from the enrollment's Azure Prepayment (previously called monetary commitment) balance or charged as overage. The Copilot Credit prepurchase plan is billed as a separate charge and appears as its own line item on your invoice.
5. Select a scope.

    - **Single resource group scope** - Applies the reservation discount to the matching resources in the selected resource group only.
    - **Single subscription scope** - Applies the reservation discount to the matching resources in the selected subscription.
    - **Shared scope** - Applies the reservation discount to matching resources in eligible subscriptions that are in the billing context. For Enterprise Agreement customers, the billing context is the enrollment.
    - **Management group** - Applies the reservation discount to the matching resource in the list of subscriptions that are a part of both the management group and billing scope.
6. Select how many Copilot Credit commit units you want to purchase.

    [![Screenshot showing Copilot Credit pre-purchase plan discount tiers and their term lengths.](media/copilot-credit/copilot-credit-discount.png)](media/copilot-credit/copilot-credit-discount.png#lightbox)
7. Choose to automatically renew the pre-purchase reservation. *The setting is configured to renew automatically by default*. For more information, see [Renew a reservation](reservation-renew).

## Change scope and ownership

You can make the following types of changes to a reservation after purchase:

- Update reservation scope
- Update who can view or manage the reservation. For more information, see [Who can manage a reservation by default](manage-reserved-vm-instance#who-can-manage-a-reservation-by-default).

You can't split or merge a **Copilot Credit Pre-Purchase Plan**. For more information about managing reservations, see [Manage reservations after purchase](manage-reserved-vm-instance).

## Cancellations and exchanges

Cancel and exchange operations aren't supported for **Copilot Credit Pre-Purchase Plans**. All purchases are final.