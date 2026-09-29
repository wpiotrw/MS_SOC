---
layout: Conceptual
title: Changes to the Azure reservation exchange policy - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/reservations/reservation-exchange-policy-changes
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
description: Learn how changes to the Azure reservation exchange policy might affect you.
ms.author: primittal
ms.reviewer: primittal
ms.service: cost-management-billing
ms.subservice: reservations
ms.topic: concept-article
ms.date: 2026-08-27T00:00:00.0000000Z
author: onwokolo
locale: en-us
document_id: 8e527742-18e2-fbe9-eb24-592cd9f1e8b8
document_version_independent_id: 12b0641b-d1ce-cbf8-abf8-821ea767028b
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/reservations/reservation-exchange-policy-changes.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/reservations/reservation-exchange-policy-changes
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/reservations/reservation-exchange-policy-changes.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/68cb9039-df60-49b0-8ef8-89ad96497f63
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/725b6df3-93e8-472d-834e-e7e0d2953d35
platformId: 6e914bd7-f5db-1715-cc1e-95d77b77d878
---

# Changes to the Azure reservation exchange policy - Microsoft Cost Management | Microsoft Learn

Starting February 1, 2027, reservations purchased after this date aren't eligible for exchange if the corresponding service is supported by savings plans. This restriction applies to Azure Virtual Machines, Azure App Service, Azure SQL Database, and similar services. Reservations purchased before February 1, 2027, keep the right to one final exchange.

Any compute or database products that become eligible for savings plans after February 1, 2027, are also subject to the preceding change. This change means that the corresponding previously purchased reservations are exchangeable one final time. This change excludes the following reservations:

- Reservations for products or services that are deprecated and approaching end of life.
- Reservations for products and services that aren't covered by savings plans, such as Azure VMware Solution. If you have a reservation for Azure VMware Solution, this policy change doesn't affect it.
- Cloud environments that don't currently support savings plans.

If you need flexibility across services and regions, consider [savings plans](../savings-plan/) as a commitment-based option for dynamic workloads. Savings plans are based on a dollar-per-hour spend commitment and automatically apply discounts across eligible compute or database services and regions, making them a good option for evolving or dynamic workloads.

Alternatively, reservations remain the appropriate option for predictable, stable workloads, and you can continue to purchase them. [Instance size flexibility](instance-size-flexibility) for virtual machines isn't affected by the change in exchange policy.

The reservation [cancellation policy](exchange-and-refund-azure-reservations) isn't changing. The total canceled commitment can't exceed $50,000 USD in a 12-month rolling window for a billing profile or single enrollment.

You can [trade in](../savings-plan/reservation-trade-in) existing reservations that cover dynamic or evolving workloads for a savings plan. There's no change to the trade-in policy. To compare your options, see [decide between a savings plan and a reservation](../savings-plan/decide-between-savings-plan-reservation).

Learn more about [Azure savings plan for compute](../savings-plan/) and how it works with reservations.

## Example scenarios

The following examples describe scenarios that might represent your situation with this change. Use these scenarios to understand how the final exchange rule applies based on when the reservation was purchased and whether it was exchanged before or after February 1, 2027.

### Scenario 1

You purchase a one-year or three-year compute or database reservation **before** February 1, 2027. You can exchange it as many times as you like before February 1, 2027. If you exchange the reservation after February 1, 2027, the new reservation isn't exchangeable because exchanges are processed as a cancellation, refund, and new purchase (which are governed by the February 1, 2027, terms). You can always trade in the reservation for a savings plan at any time.

### Scenario 2

You purchase a one-year or three-year compute or database reservation **after** February 1, 2027. You can't exchange this reservation. However, you can always trade in the reservation for a savings plan.

### Scenario 3

You purchase a one-year or three-year compute or database reservation with 10 quantities **before** February 1, 2027. After February 1, 2027, you exchange 2 quantities of the compute reservation. You can still exchange each of the remaining 8 quantities on the original reservation one more time. You can always trade in the reservation for a savings plan.

### Scenario 4

You purchase a one-year or three-year compute or database reservation **before** February 1, 2027, and enable automatic renewal (or manually renew it). The renewal occurs after February 1, 2027. Because a renewal is processed as a cancellation of the original reservation and a new reservation purchase, the new reservation is governed by the February 1, 2027 terms and isn't exchangeable. You can always trade in the reservation for a savings plan.