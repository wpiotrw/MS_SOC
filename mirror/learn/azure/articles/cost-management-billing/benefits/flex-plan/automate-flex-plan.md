---
layout: Conceptual
title: Automate Flex Plan operations - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/benefits/flex-plan/automate-flex-plan
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
description: Learn how to automate Flex Plan discovery, purchasing, management, monitoring, and cost-data retrieval.
author: pri-mittal
ms.service: cost-management-billing
ms.subservice: billing
ms.topic: how-to
ms.date: 2026-11-10T00:00:00.0000000Z
ms.author: primittal
locale: en-us
document_id: c267fd61-b670-4eea-5651-e1230a628efa
document_version_independent_id: d29d91a3-2afc-879b-0620-4860985aef52
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/benefits/flex-plan/automate-flex-plan.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/benefits/flex-plan/automate-flex-plan
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/benefits/flex-plan/automate-flex-plan.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 0891061f-c534-cacf-f207-500ca55f8394
---

# Automate Flex Plan operations - Microsoft Cost Management | Microsoft Learn

Use Azure Billing Benefits and Cost Management interfaces to integrate Flex Plan tasks into FinOps and purchasing workflows.

Note

Tool and API availability can differ by operation and purchasing channel. Use the [Azure Billing Benefits REST API](/en-us/rest/api/billingbenefits/operation-groups) to identify the Flex Plan operations available for your account and API version.

## Before you begin

Your application or identity needs permission on the relevant:

- Billing account or billing profile
- Billing subscription
- Flex Plan order and resource
- Benefit scope

Use Microsoft Entra authentication and least-privilege role assignments.

## Discover available offers and prices

Automate offer discovery to retrieve Flex Plans available to the customer. The response can include:

- Offer and SKU identifiers
- Terms and billing frequencies
- Minimum and maximum commitment amounts
- Currency and region
- Covered products and SKUs
- Benefit prices
- Whether the offer is available to the account

Don't hard-code offer configuration. Availability and pricing can change. Retrieve the current offer before validating a request or presenting purchase options.

## Retrieve recommendations

Use the [Benefit Recommendations API](/en-us/rest/api/cost-management/benefit-recommendations/list) to retrieve available purchase recommendations. A recommendation can include:

- Recommended commitment amount
- Term and billing frequency
- Lookback period
- Estimated savings
- Covered usage
- Cost details

Validate that a recommendation is still within the offer's current minimum and maximum before purchasing.

## Validate a purchase

Before submitting a purchase through an available Flex Plan purchase operation, retrieve the current offer and validate:

- Commitment purchase amount
- Payment schedule
- Currency
- Applicable purchase price
- Benefit scope
- Start date

Repeat validation after changing the term, billing frequency, commitment amount, or offer. Don't submit a request that uses cached limits or expired offer data.

## Purchase a Flex Plan

When an automated purchase operation is available for the customer's channel, the request typically supplies:

- Billing scope
- Subscription or resource placement
- Offer identifier
- Commitment amount
- Term
- Billing frequency
- Benefit scope
- Start date

Use the idempotency or alias mechanism documented for the operation. Record the returned order and plan identifiers, and read the created resource before reporting success.

Seller-assisted and Cloud Solution Provider purchases can use different transaction interfaces while creating the same type of Flex Plan benefit.

## View and manage plans

Automate retrieval of:

- Status and dates
- Original and remaining commitment
- Benefit scope
- Covered usage and utilization

Use the Flex Plan operations listed in the [Billing Benefits REST API reference](/en-us/rest/api/billingbenefits/operation-groups) to change supported settings. Re-read the resource after an update to confirm the effective configuration.

You can manage plans that a seller purchases on your behalf through supported operations with the appropriate permissions. See [Manage a seller-purchased Flex Plan](manage-flex-plan#manage-a-seller-purchased-flex-plan).

## Export usage and cost data

Create a [Cost Management export](../../costs/tutorial-improved-exports) or use the [Cost Management query API](/en-us/rest/api/cost-management/query) to retrieve available cost and usage data, including:

- Flex Plan benefit identifier
- Amount of benefit consumed
- Covered product and resource
- Retail and effective costs
- Amortized cost
- Uncovered usage

Join cost data to the Flex Plan order and plan identifiers for reporting.

## Handle errors

Automation should explicitly handle:

- Insufficient permissions
- Commitment outside the permitted range
- Unsupported term or billing frequency
- Offer no longer available
- Expired offer availability period
- Invalid benefit scope
- Conflicting or concurrent updates

Don't treat an empty or partial response as a successful purchase.