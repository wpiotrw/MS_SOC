---
layout: Conceptual
title: GitHub Pre-Purchase Plan - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/github-pre-purchase
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
description: Learn about GitHub Pre-Purchase Plan in Azure reservations.
author: pri-mittal
ms.reviewer: primittal
ms.service: cost-management-billing
ms.subservice: reservations
ms.topic: how-to
ms.date: 2026-11-04T00:00:00.0000000Z
ms.author: primittal
locale: en-us
document_id: d479f479-42f7-c818-e9df-d16bad8940e8
document_version_independent_id: 36e08a76-4ad0-1b7c-7582-363c679f303b
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/reservations/github-pre-purchase.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/reservations/github-pre-purchase
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/reservations/github-pre-purchase.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9bdc1705-9b40-49d6-8377-caa0b71fda66
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/686ed158-d915-41e9-9760-efa46ba88f6d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 4c606118-40e6-c830-1e1d-37d662775b4b
---

# GitHub Pre-Purchase Plan - Microsoft Cost Management | Microsoft Learn

Save on your GitHub costs when you buy a Pre-Purchase plan. Pre-Purchase plans are commit units (CUs) bought at discounted tiers in your purchasing currency for a specific product. The more you buy, the greater the discount. Purchased CUs pay down qualifying costs in US dollars (USD). So, if GitHub generates a retail cost of $100 based on GitHub usage, then 100 GitHub CUs (GCUs) are consumed.

Your GitHub Pre-Purchase plan automatically uses your GCUs to pay for eligible GitHub usage during its one-year term or until GitHub CUs run out. Your Pre-Purchase plan GitHub CUs start paying for your GitHub usage without having to redeploy or reassign the plan. By default, plans are configured to renew at the end of the one-year term.

## Services covered by GitHub Pre-Purchase plan

The GitHub Pre-Purchase plan covers usage across all products under the GitHub services umbrella, including GitHub Enterprise, GitHub Copilot, GitHub Advanced Security, and GitHub Actions, Codespaces, Packages, Large File Storage and any GitHub AI Overage Units among others.

## How GitHub usage maps to your Azure subscription

GitHub usage is billed through the Azure subscription linked to your GitHub organization. Understanding this mapping is important for ensuring your Pre-Purchase plan covers your usage:

- **GitHub organization → Azure subscription**: Each GitHub organization is linked to a specific Azure subscription for billing purposes. All GitHub usage from that organization — including GitHub Copilot and GitHub Actions — flows to that subscription.
- **Scope alignment**: The scope you select for your Pre-Purchase plan must include the Azure subscription linked to your GitHub organization. If you have multiple GitHub organizations linked to different Azure subscriptions, consider using **Shared scope** or **Management group** scope to cover all of them.
- **Verifying your linked subscription**: To check which Azure subscription is linked to your GitHub organization, go to your GitHub organization's billing settings and review the Azure subscription ID.

Tip

If you're unsure which subscription your GitHub usage is billed to, use **Shared scope** to apply the Pre-Purchase plan across all eligible subscriptions in your billing context. This ensures no usage is missed.

## Prerequisites

To buy a Pre-Purchase plan, you must have one of the following Azure subscriptions and roles:

- For an Azure subscription, the owner role or reservation purchaser role is required.
- For an Enterprise Agreement (EA) subscription, the [**Reserved Instances** policy option](../manage/direct-ea-administration#view-and-manage-enrollment-policies) must be enabled. To enable that policy option, you must be an EA administrator of the subscription.
- For a Cloud Solution Provider (CSP) subscription, follow one of these articles:
    - [Buy Azure reservations on behalf of a customer](/en-us/partner-center/customers/azure-reservations-buying)
    - [Allow the customer to buy their own reservations](/en-us/partner-center/customers/give-customers-permission)

## Determine the right size to buy

To get started, estimate your expected GitHub usage for the term. This helps you determine the appropriate size for your Pre-Purchase plan. Each Pre-Purchase plan has a one-year term.

**Example calculation:**

Note

The following examples use hypothetical prices and quantities for illustration purposes only. Actual prices, discounts, and tier thresholds may vary. Refer to the Azure portal for current pricing.

Suppose a customer expects to consume:

| Item | Quantity | Hypothetical Annual Total |
| --- | --- | --- |
| GHCP Business | 970 licenses | $221,160 |
| GitHub Enterprise | 560 licenses | $141,120 |
| Code Security | 380 licenses | $136,800 |
| AI Credits | 92,000 credits | $920 |
| **Total** |  | **$500,000** |

By purchasing Tier 3 (500,000 GitHub Commit Units) GitHub P3 at a hypothetical cost of $425,000, the customer realizes a 15% savings compared to the hypothetical pay-as-you-go rate for the same level of usage.

Consider a hypothetical scenario where your organization plans to use:

- **GitHub Copilot**: 500 licenses of GitHub Copilot Business
- **GitHub Actions**: 50,000 minutes of compute usage

**Assumed pay-as-you-go rates (for illustration purposes):**

- GitHub Copilot Business at hypothetical $19 per license/month = $114,000/year
- GitHub Actions at assumed rates = $6,000/year
- **Total estimated pay-as-you-go cost: $120,000**

**Assuming Tier 2 Pre-Purchase plan (120,000 CUs):**

- Estimated plan cost: $112,800
- **Potential savings: $7,200 (approximately 6% discount)**

This example demonstrates how the Pre-Purchase plan can provide cost savings for organizations with predictable GitHub usage patterns.

Note

Pre-purchase plan discounts don't combine with other discounts you might have. If you have additional discounts, the pre-purchase plan discount is applied independently, which may result in a lower effective discount rate than the listed tier percentage. Factor in your existing discounts when estimating savings.

## Purchase GitHub Pre-Purchase Plan commit units

You can pay for GitHub pre-purchase plan purchases with Azure prepayment. These purchases count toward your Microsoft Azure Consumption Commitment (MACC).

Purchase GitHub Pre-Purchase Plans in the [Azure portal reservations](https://portal.azure.com/#view/Microsoft_Azure_Reservations/ReservationsBrowseBlade/productType/Reservations).

1. Go to the [Azure portal](https://portal.azure.com)
2. Navigate to the **Reservations** service.
3. On the **Purchase reservations page**, select **GitHub Pre-Purchase Plan**.
4. On the **Select the product you want to purchase** page, select a subscription. Use the **Subscription** list to select the subscription used to pay for the purchase. The payment method of the subscription is charged the upfront cost for the reservation.
5. Select a scope. The scope determines which Azure subscriptions' GitHub usage is covered by this Pre-Purchase plan. Make sure the scope includes the subscription where your GitHub usage is billed.
6. Select the discount tier you want to purchase. [![Screenshot showing the Select the product you want to purchase page with GitHub Pre-Purchase Plan tiers.](media/github-pre-purchase/select-github-pre-purchase-plan.png)](media/github-pre-purchase/select-github-pre-purchase-plan.png#lightbox)
    - **Single resource group scope** - Applies the reservation discount to the matching resources in the selected resource group only.
    - **Single subscription scope** - Applies the reservation discount to the matching resources in the selected subscription.
    - **Shared scope** - Applies the reservation discount to matching resources in eligible subscriptions that are in the billing context. For Enterprise Agreement customers, the billing context is the enrollment.
    - **Management group** - Applies the reservation discount to the matching resource in the list of subscriptions that are a part of both the management group and billing scope.

Note

GitHub usage is billed through the Azure subscription that is linked to your GitHub organization. To ensure your Pre-Purchase plan covers your GitHub usage, verify that the subscription linked to your GitHub organization falls within the scope you select. If the linked subscription is outside the scope, the Pre-Purchase plan won't apply to that usage.

1. Select how many GitHub commit units you want to purchase.
2. Choose to automatically renew the Pre-Purchase reservation. *The setting is configured to renew automatically by default*. For more information, see [Renew a reservation](reservation-renew).

## Change scope and ownership

You can make the following types of changes to a reservation after purchase:

- Update reservation scope
- Update who can view or manage the reservation. For more information, see [Who can manage a reservation by default](manage-reserved-vm-instance#who-can-manage-a-reservation-by-default).

You can't split or merge a **GitHub Pre-Purchase Plan**. For more information about managing reservations, see [Manage reservations after purchase](manage-reserved-vm-instance).

## How does benefit application work?

When you have multiple AI-related purchasing options, understanding how benefits are applied helps you maximize your cost savings. You might have several types of purchases for your AI workloads:

- [GitHub AI Credits Pre-Purchase plan](github-ai-credits-pre-purchase-plan) - Covers GitHub AI Credits-specific usage
- GitHub Pre-Purchase plan - Covers broader GitHub usage
- [Microsoft Agent Pre-Purchase plan](agent-pre-purchase) - Covers broader AI workloads including Copilot Credit, Microsoft Foundry, and GitHub

### Understanding benefit overlap

**What is overlap?** Overlap occurs when multiple benefits can cover the same usage. For example:

- GitHub AI Credits usage is eligible for the GitHub AI Credits Pre-Purchase plan, the GitHub Pre-Purchase plan, and the Microsoft Agent Pre-Purchase plan

### Benefit application order (precedence)

When overlap occurs, Microsoft applies benefits in this specific order to maximize your savings:

1. **GitHub AI Credits Pre-Purchase Plan**

    - Applied first to GitHub AI Credits-specific usage
    - Most granular benefit preserved for specialized use
2. **GitHub Pre-Purchase Plan**

    - Applied next to remaining GitHub usage (including any AI Credits usage not fully covered above)
    - Broader GitHub coverage
3. **Microsoft Agent Pre-Purchase Plan**

    - Applied last to remaining eligible usage across platforms
    - Broadest coverage for heterogeneous AI workloads

Important

GitHub Pre-Purchase plan does not cover the purchase cost of other reservations or Pre-Purchase plans - only actual usage costs.

## Cancellations and exchanges

Cancel and exchange operations aren't supported for **GitHub Pre-Purchase Plans**. All purchases are final.