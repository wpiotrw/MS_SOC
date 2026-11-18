---
layout: Conceptual
title: What is a Flex Plan? - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/benefits/flex-plan/flex-plan-overview
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
description: Learn how a Flex Plan commitment, benefit balance, scope, and billing work.
author: pri-mittal
ms.service: cost-management-billing
ms.subservice: billing
ms.topic: overview
ms.date: 2026-11-10T00:00:00.0000000Z
ms.author: primittal
locale: en-us
document_id: f9725f2f-992d-5c30-3408-e572e3a4d054
document_version_independent_id: f2269214-d89a-bff9-5277-52ade001290a
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/benefits/flex-plan/flex-plan-overview.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/benefits/flex-plan/flex-plan-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/benefits/flex-plan/flex-plan-overview.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
platformId: bfb1216c-9949-8d68-3ba9-d2c131aa02f6
---

# What is a Flex Plan? - Microsoft Cost Management | Microsoft Learn

A Flex Plan helps you save on covered products by committing to a monetary amount for a selected term. Each offer defines the available terms, billing frequencies, commitment limits, covered products, and benefit prices. You choose an amount within the permitted range and where the benefit applies.

The commitment is flexible because covered usage draws from the same monetary balance throughout the term. Consumption can increase or decrease over time. The plan ends when the balance is exhausted or the term expires, whichever happens first.

Note

Flex Plan availability, terms, billing frequencies, commitment limits, currencies, products, SKUs, and pricing vary by offer.

## How a Flex Plan works

When you purchase a Flex Plan, you:

1. Select an available Flex Plan offer.
2. Select a supported term and billing frequency.
3. Enter a commitment amount within the displayed minimum and maximum.
4. Select where the benefit applies.
5. Review and submit the purchase.

The commitment amount becomes the plan's available balance. The plan becomes active on its effective date, and the benefit automatically applies to covered usage within its scope. You don't need to modify or restart the resources receiving the benefit.

For example, if a plan has a $50,000 balance and $850 of covered usage is billed at the applicable benefit price, Microsoft deducts $850 and the remaining balance is $49,150.

The balance isn't divided into hourly or monthly usage buckets. Any unused balance is forfeited when the term expires.

## Benefit application

Microsoft calculates covered usage at the applicable benefit price and deducts the result from the Flex Plan balance.

When usage is eligible for more than one commitment benefit, Microsoft applies the applicable benefits according to their terms. More specific commitment benefits apply before a Flex Plan.

When multiple Flex Plans might cover the same usage, Microsoft evaluates them in the following order:

1. **Scope eligibility**: The plan must be active, cover the product or SKU, and include the usage within its benefit scope.
2. **Offer type**: Free usage offers apply before paid plans.
3. **Product coverage**: More granular Flex Plans apply before broader Flex Plans.
4. **Scope specificity**: Among plans with the same offer type and product coverage, the plan with the more specific benefit scope applies first.
5. **Expiry**: Among eligible plans with the same offer type, product coverage, and scope, the plan with the earliest expiry applies first.

One unit of usage can draw from only one Flex Plan.

If the first applicable Flex Plan doesn't have enough balance for all covered usage, it applies until its balance is exhausted. Microsoft evaluates the remaining usage against the next applicable Flex Plan or benefit. If no other benefit applies, the remaining usage is billed at the applicable pay-as-you-go price.

### Benefit application examples

#### Scope eligibility is evaluated first

Plan A expires earlier but is scoped to Subscription A. Plan B is scoped to Subscription B. Usage from Subscription B draws from Plan B because Plan A's scope doesn't include the usage, even though Plan A expires first.

#### Free usage offers apply before paid plans

A workload is eligible for both a free usage offer and a paid Flex Plan. Microsoft applies the free usage offer first. Any remaining usage is evaluated for the paid plan.

#### More granular Flex Plans apply before broader Flex Plans

A workload is eligible for both a product-specific paid Flex Plan and a broader paid Flex Plan. Microsoft applies the product-specific plan first. Any remaining usage is evaluated for the broader plan.

## Benefit scope

The benefit applies only to covered usage within the selected scope. Depending on the offer, available scope options can include:

- **Single resource group**: Applies the benefit to covered usage from resources in the selected resource group.
- **Single subscription**: Applies the benefit to covered usage in the selected subscription.
- **Shared**: Applies the benefit to covered usage in eligible subscriptions within the billing context.
- **Management group**: Applies the benefit to covered usage in subscriptions that are both in the selected management group hierarchy and within the billing scope.

The subscription containing the Flex Plan resource and the scope where its benefit applies are separate settings. Moving the resource doesn't automatically change the benefit scope.

Changing the benefit scope affects future usage. It doesn't:

- Move the Flex Plan resource.
- Restart the plan term.
- Restore consumed balance.
- Reprocess finalized usage.

If a plan no longer has a valid subscription in its configured scope, Microsoft can change the plan to a shared scope and notify the Flex Plan owners.

## Commitment recommendations

Microsoft can provide a recommended commitment amount based on historical covered usage. A recommendation can include:

- Recommended commitment amount
- Term and billing frequency
- Minimum and maximum commitment amount
- Estimated savings and coverage
- Historical usage and cost details

Recommendations are estimates, not guarantees. Future usage, benefit prices, product coverage, and scope changes can affect actual savings.

## Promotions and free usage offers

If your billing account is eligible for a promotion or free usage offer, the offer appears in the Flex Plan purchase experience. Review the displayed offer details and terms before selecting it.

If no promotion or free usage offer appears, none is currently available for your billing account.

## Seller-purchased Flex Plans

If a seller purchases a Flex Plan on your behalf, it appears under the account used for the purchase. You don't need to purchase it again.

By using the appropriate permissions, you can view the plan, monitor utilization and remaining balance, and change its benefit scope. For more information, see [Manage a seller-purchased Flex Plan](manage-flex-plan#manage-a-seller-purchased-flex-plan).

## Billing

A Flex Plan supports upfront billing, monthly billing, or both.

- **Upfront**: Microsoft collects the full commitment at purchase.
- **Monthly**: Microsoft collects the commitment over the term. Each billing period has a minimum charge, but the charge can be higher when cumulative covered usage exceeds the amount collected so far.

Billing determines when Microsoft collects the committed amount. Benefit consumption determines how covered usage reduces the balance. For detailed calculations and invoice behavior, see [Understand Flex Plan billing and charges](flex-plan-billing).

## Price changes

Benefit prices can vary by offer, agreement, purchasing channel, and customer-specific terms. When a new benefit price becomes effective, Microsoft applies it to usage from the effective date forward. Earlier finalized usage isn't rerated solely because a new price becomes effective.

## Cancellations, exchanges, and transfers

Self-service cancellation isn't supported. You can't exchange a Flex Plan for a reservation, savings plan, another Flex Plan, or another commitment benefit.

You can't transfer a Flex Plan across billing entities. Moving the resource within its permitted billing boundary doesn't change where the benefit applies.

For Cloud Solution Provider (CSP) subscriptions, the associated Flex Plan is automatically canceled when you initiate subscription cancellation or transfer, not when the operation completes.