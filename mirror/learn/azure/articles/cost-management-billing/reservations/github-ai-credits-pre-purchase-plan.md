---
layout: Conceptual
title: GitHub AI Credits Pre-Purchase Plan - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/github-ai-credits-pre-purchase-plan
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
description: Learn about GitHub AI Credits Pre-Purchase Plan in Azure reservations.
author: pri-mittal
ms.reviewer: primittal
ms.service: cost-management-billing
ms.subservice: reservations
ms.topic: how-to
ms.date: 2026-11-04T00:00:00.0000000Z
ms.author: primittal
locale: en-us
document_id: c9f20db3-28ed-a1c6-5342-45f0dbef8eab
document_version_independent_id: 5663a92b-5367-916e-44f1-8bb7d2f73b6d
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/reservations/github-ai-credits-pre-purchase-plan.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/reservations/github-ai-credits-pre-purchase-plan
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/reservations/github-ai-credits-pre-purchase-plan.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9bdc1705-9b40-49d6-8377-caa0b71fda66
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/686ed158-d915-41e9-9760-efa46ba88f6d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 8a4a697b-443c-bd03-11b2-f6727965dbba
---

# GitHub AI Credits Pre-Purchase Plan - Microsoft Cost Management | Microsoft Learn

Save on your GitHub AI Credits costs when you buy a pre-purchase plan. Pre-purchase plans are commit units (CUs) bought at discounted tiers in your purchasing currency for a specific product. The more you buy, the greater the discount. Purchased CUs pay down qualifying costs in US dollars (USD). So, if GitHub AI generates a retail cost of $100 based on GitHub AI Credits usage, then 100 GitHub AI Credits CUs (GHAICCUs) are consumed.

Your GitHub AI Credits pre-purchase plan automatically uses your GHAICCUs to pay for eligible GitHub AI Credits usage during its one-year term or until GitHub AI Credits CUs run out. Your pre-purchase plan GitHub AI Credits CUs start paying for your GitHub AI usage without having to redeploy or reassign the plan. By default, plans are configured to renew at the end of the one-year term.

## How GitHub AI Credits usage maps to your Azure subscription

GitHub AI Credits usage is billed through the Azure subscription linked to your GitHub organization. Understanding this mapping is important for ensuring your pre-purchase plan covers your usage:

- **GitHub organization → Azure subscription**: Each GitHub organization is linked to a specific Azure subscription for billing purposes. All GitHub AI Credits usage from that organization flows to that subscription.
- **Scope alignment**: The scope you select for your pre-purchase plan must include the Azure subscription linked to your GitHub organization. If you have multiple GitHub organizations linked to different Azure subscriptions, consider using **Shared scope** or **Management group** scope to cover all of them.
- **Verifying your linked subscription**: To check which Azure subscription is linked to your GitHub organization, go to your GitHub organization's billing settings and review the Azure subscription ID.

Tip

If you're unsure which subscription your GitHub usage is billed to, use **Shared scope** to apply the pre-purchase plan across all eligible subscriptions in your billing context. This ensures no usage is missed.

## Prerequisites

To buy a pre-purchase plan, you must have one of the following Azure subscriptions and roles:

- For an Azure subscription, the owner role or reservation purchaser role is required.
- For an Enterprise Agreement (EA) subscription, the [**Reserved Instances** policy option](../manage/direct-ea-administration#view-and-manage-enrollment-policies) must be enabled. To enable that policy option, you must be an EA administrator of the subscription.
- For a Cloud Solution Provider (CSP) subscription, follow one of these articles:
    - [Buy Azure reservations on behalf of a customer](/en-us/partner-center/customers/azure-reservations-buying)
    - [Allow the customer to buy their own reservations](/en-us/partner-center/customers/give-customers-permission)

## Determine the right size to buy

To get started, estimate your expected GitHub AI Credits usage. This helps you determine the appropriate size for your pre-purchase plan. Each pre-purchase plan has a one-year term.

Note

The following example uses hypothetical prices and quantities for illustration purposes only. Actual prices, discounts, and tier thresholds may vary. Refer to the Azure portal for current pricing.

For example, suppose you expect to consume 2,000,000 GitHub AI Credits. Assuming a hypothetical pay-as-you-go rate of $0.01 per credit, this would cost $20,000. By purchasing a Tier 1 (20,000 CU) pre-purchase plan at a hypothetical cost of $19,000, you would realize a 5% saving compared to the hypothetical pay-as-you-go rate for the same usage.

Note

Pre-purchase plan discounts don't combine with other discounts you might have. If you have additional discounts, the pre-purchase plan discount is applied independently, which may result in a lower effective discount rate than the listed tier percentage. Factor in your existing discounts when estimating savings.

## Purchase GitHub AI Credits commit units

You can pay for GitHub AI Credits pre-purchase plans with Azure Prepayment. These plans count toward your Microsoft Azure Consumption Commitment (MACC).

Purchase GitHub AI Credits pre-purchase plans in the [Azure portal reservations](https://portal.azure.com/#view/Microsoft_Azure_Reservations/ReservationsBrowseBlade/productType/Reservations).

1. Go to the [Azure portal](https://portal.azure.com)
2. Navigate to the **Reservations** service.
3. On the **Purchase reservations page**, select **GitHub AI Credits Pre-Purchase Plan**.
4. On the **Select the product you want to purchase** page, select a subscription. Use the **Subscription** list to select the subscription used to pay for the reserved capacity. The payment method of the subscription is charged the upfront costs for the reserved capacity.
5. Select a scope. The scope determines which Azure subscriptions' GitHub AI Credits usage is covered by this pre-purchase plan. Make sure the scope includes the subscription where your GitHub usage is billed.
6. Select the discount tier you want to purchase. [![Screenshot showing the Select the product you want to purchase page with GitHub AI Credits Pre-Purchase Plan tiers.](media/github-ai-credits/select-github-ai-credits-plan.png)](media/github-ai-credits/select-github-ai-credits-plan.png#lightbox)

    - **Single resource group scope** - Applies the reservation discount to the matching resources in the selected resource group only.
    - **Single subscription scope** - Applies the reservation discount to the matching resources in the selected subscription.
    - **Shared scope** - Applies the reservation discount to matching resources in eligible subscriptions that are in the billing context. For Enterprise Agreement customers, the billing context is the enrollment.
    - **Management group** - Applies the reservation discount to the matching resource in the list of subscriptions that are a part of both the management group and billing scope.

    Note

    GitHub usage is billed through the Azure subscription that is linked to your GitHub organization. To ensure your pre-purchase plan covers your GitHub AI Credits usage, verify that the subscription linked to your GitHub organization falls within the scope you select. If the linked subscription is outside the scope, the pre-purchase plan won't apply to that usage.
7. Select how many GitHub AI Credits commit units you want to purchase.
8. Choose to automatically renew the pre-purchase reservation. *The setting is configured to renew automatically by default*. For more information, see [Renew a reservation](reservation-renew).

## Change scope and ownership

You can make the following types of changes to a reservation after purchase:

- Update reservation scope
- Update who can view or manage the reservation. For more information, see [Who can manage a reservation by default](manage-reserved-vm-instance#who-can-manage-a-reservation-by-default).

You can't split or merge a **GitHub AI Credits Pre-Purchase Plan**. For more information about managing reservations, see [Manage reservations after purchase](manage-reserved-vm-instance).

## How does benefit application work?

When you have multiple purchasing options, understanding how benefits are applied helps you maximize your cost savings. You might have several types of purchases for your AI workloads:

- GitHub AI Credits pre-purchase plan - Covers GitHub AI Credits-specific usage
- [GitHub Pre-Purchase plan](/en-us/azure/cost-management-billing/reservations/github-pre-purchase) - Covers broader GitHub usage
- [Microsoft Agent prepurchase plan](agent-pre-purchase) - Covers broader AI workloads including Copilot Credit, Microsoft Foundry, and GitHub

### Understanding benefit overlap

**What is overlap?** Overlap occurs when multiple benefits can cover the same usage. For example:

- GitHub AI Credits usage is eligible for the GitHub AI Credits pre-purchase plan, the GitHub prepurchase plan, and the Microsoft Agent prepurchase plan

### Benefit application order (precedence)

When overlap occurs, Microsoft applies benefits in this specific order to maximize your savings:

1. **GitHub AI Credits Pre-Purchase Plan**

    - Applied first to GitHub AI Credits-specific usage
    - Most granular benefit preserved for specialized use
2. **GitHub Prepurchase Plan**

    - Applied next to remaining GitHub usage
    - Broader GitHub coverage
3. **Microsoft Agent Prepurchase Plan**

    - Applied last to remaining eligible usage across platforms
    - Broadest coverage for heterogeneous AI workloads

Important

GitHub AI Credits pre-purchase plan does not cover the purchase cost of other reservations or prepurchase plans - only actual usage costs.

## Cancellations and exchanges

Cancel and exchange operations aren't supported for **GitHub AI Credits Pre-Purchase Plans**. All purchases are final.