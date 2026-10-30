---
layout: Conceptual
title: Decide between a savings plan and a reservation - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/decide-between-savings-plan-reservation
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
description: Learn how to decide between a savings plan and a reservation.
author: nwokolo
ms.author: onwokolo
ms.reviewer: onwokolo
ms.service: cost-management-billing
ms.subservice: savings-plan
ms.topic: concept-article
ms.date: 2026-10-29T00:00:00.0000000Z
locale: en-us
document_id: eccdaa31-58e9-0c34-3de5-b371ab5adfbd
document_version_independent_id: 06e67cea-9508-ba34-33af-a707222a6b42
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/savings-plan/decide-between-savings-plan-reservation.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/savings-plan/decide-between-savings-plan-reservation
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/savings-plan/decide-between-savings-plan-reservation.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/2ed91286-6cf7-4b83-810d-75d0ee3b09dd
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/6735bd7e-4f7b-457d-b58c-29e6f0198677
platformId: 3234d369-89c5-ceed-5b00-66b142d1435d
---

# Decide between a savings plan and a reservation - Microsoft Cost Management | Microsoft Learn

Azure provides you with two ways to save on your usage by committing for one or three years. You have the freedom to choose the savings options that best align with your workload patterns.

## Compare reservations with savings plans

Reservations and savings plans can help you save on eligible compute and database usage. With a reservation, you commit to a specific resource product or configuration for a set period. The applicable resource attributes, such as instance family and region, depend on the reservation product. For a compute example, you might commit to using a D2v4 virtual machine in the Japan East region for one year.

With a savings plan, you commit to a fixed hourly spend on eligible services across Azure regions for a set period. For example, you might commit to spending $5.00 per hour for three years. Eligibility depends on the selected plan type: a compute savings plan applies to eligible compute usage, and a database savings plan applies to eligible database usage. Each plan's benefits apply to eligible usage within its benefit scope, up to its hourly commitment.

### Choose a reservation

Choose reservations for compute or database workloads that run continuously and are highly stable, with no anticipated changes to the resource attributes required by the reservation, such as instance type, instance family, or region. When fully utilized, reservations can provide greater savings than savings plans for these workloads.

### Choose a savings plan

Choose savings plans when your compute or database workloads are dynamic or evolving, particularly if they use multiple eligible services or run in different Azure regions. Select a compute savings plan for eligible compute usage or a database savings plan for eligible database usage. Each plan provides flexible benefit application across the eligible services and regions for that plan type, with automatic optimization.

## How to optimize cost savings using both reservations and savings plans

To improve savings and limit unused commitments, consider the following sequence:

1. Right‑size first – Remove unused or oversized resources before buying any discounts. Discounts reduce rates, not waste.
2. Exchange underutilized reservations – If workloads changed, reassign existing reservations to better‑fit configurations instead of letting value go unused.
3. Trade‑in underutilized reservations for savings plans – When usage is variable, convert rigid reservations into more flexible, spend‑based savings plans.
4. Purchase new reservations – Commit only for stable, well‑understood workloads where usage and configuration are unlikely to change.
5. Purchase new savings plans – Finally, add flexible, spend‑based commitments sized to a clean, optimized baseline.

This sequence removes waste first, optimizes existing commitments next, and only then adds new commitments. It helps you achieve actual savings, not just theoretical discounts.