---
layout: Conceptual
title: Savings plan scopes - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/scope-savings-plan
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
description: Learn about savings plan scopes and how they're processed.
author: nwokolo
ms.author: onwokolo
ms.reviewer: onwokolo
ms.service: cost-management-billing
ms.subservice: savings-plan
ms.topic: concept-article
ms.date: 2026-10-29T00:00:00.0000000Z
locale: en-us
document_id: 7ae5e4b1-b93f-7757-c1e0-544263a38c35
document_version_independent_id: 403817a9-3486-0360-9f3e-c15abc595587
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/savings-plan/scope-savings-plan.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/savings-plan/scope-savings-plan
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/savings-plan/scope-savings-plan.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
platformId: 51cc4259-191f-9dea-b11e-1f62be077625
---

# Savings plan scopes - Microsoft Cost Management | Microsoft Learn

The scope of a savings plan determines where its benefits apply.

You have the following options to scope a savings plan, depending on your needs:

## Scope options

- **Resource group scope** - Applies benefits to eligible resources in the selected resource group.
- **Subscription scope** - Applies benefits to eligible resources in the selected subscription.
- **Management group**- Applies benefits to eligible resources from all subscriptions that are in both:
    - The management group.
    - The same enrollment or billing profile as the subscription used to purchase the benefit.
- **Shared scope** - Applies benefits to eligible resources within subscriptions in the EA enrollment or MCA billing profile. Shared scope benefits apply across all Microsoft Entra tenants in the enrollment or billing profile.

## Scope processing order

While applying savings plan benefits to your usage, Azure processes savings plans in the following order:

1. Savings plans with resource group scope.
2. Savings plans with subscription scope.
3. Savings plans with management group scope.
4. Savings plans with shared scope.

You can update the scope after you buy a savings plan. To do so, go to the savings plan, select **Configuration**, and rescope the savings plan. Rescoping a savings plan isn't a commercial transaction, so it doesn't change your savings plan term. For more information, see [Update the scope](manage-savings-plan#change-the-savings-plan-scope).