---
layout: Conceptual
title: Choose a savings plan commitment amount - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/choose-commitment-amount
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
description: This article helps you determine how to choose a savings plan commitment amount.
author: nwokolo
ms.reviewer: onwokolo
ms.service: cost-management-billing
ms.subservice: savings-plan
ms.topic: how-to
ms.date: 2026-10-29T00:00:00.0000000Z
ms.author: onwokolo
locale: en-us
document_id: 6539ac57-43e3-6a25-6db7-a1f04dee75bc
document_version_independent_id: 377e8bdf-98ec-f841-a680-83e9acd43089
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/savings-plan/choose-commitment-amount.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/savings-plan/choose-commitment-amount
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/savings-plan/choose-commitment-amount.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d9dfd2a0-aa13-46ef-a37d-ed697b490607
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/06404839-4766-4799-8cab-c0e1c3b55e48
platformId: 35bdf847-d115-c30b-939f-d0d65e93e972
---

# Choose a savings plan commitment amount - Microsoft Cost Management | Microsoft Learn

To calculate savings plan purchase recommendations, Azure analyzes your hourly pay-as-you-go usage and cost data. It generates recommendations for the selected savings plan term (one year or three years), [benefit scope](scope-savings-plan) (shared, management group, subscription, or resource group), and lookback period (7, 30, or 60 days). Azure calculates your potential savings by simulating the total costs you would have under a savings plan. It examines each combination of term, benefit scope, and lookback period. It then compares these simulated costs with the actual pay-as-you-go costs you incurred. The commitment amount that returns the greatest savings for each term, benefit scope, and lookback period combination is highlighted. To learn more about how recommendations are generated, see [How savings plan recommendations are generated](purchase-recommendations#how-savings-plan-recommendations-are-generated).

Some products can benefit from both savings plans and reservations. If you buy either a savings plan or a reservation, wait at least seven days for recommendation systems to update and reflect your purchase before considering the other option. Avoid purchasing both products at the same time to ensure recommendations are accurate and to maximize your savings.

Savings plan recommendations are available in [Azure Advisor](https://portal.azure.com/#view/Microsoft_Azure_Expert/AdvisorMenuBlade/%7E/Cost), the [Azure portal](https://portal.azure.com/), and the [Savings plan benefit recommendations API](/en-us/rest/api/cost-management/benefit-recommendations/list).

## Recommendations in Azure Advisor

Recommendations for one-year and three-year savings plans in [Azure Advisor](https://portal.azure.com/#view/Microsoft_Azure_Expert/AdvisorMenuBlade/%7E/Cost) are currently available only for subscription scopes. These recommendations use a 30-day lookback period.

## Recommendations in the Azure portal

Recommendations for one-year and three-year savings plans in the [Azure portal](https://portal.azure.com/) are available for shared, management group, subscription, and resource group scopes. These recommendations use a 30-day lookback period.

## Savings plan recommendations API

One-year and three-year savings plan recommendations from the [Savings plan benefit recommendations API](/en-us/rest/api/cost-management/benefit-recommendations/list) are available for shared, management group, subscription, and resource group scopes. These recommendations are available for 7-day, 30-day, and 60-day lookback periods.

## Need help? Contact us

If you have savings plan questions, contact your account team or [create a support request](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest). Currently, Microsoft provides expert support for savings plans only in English.