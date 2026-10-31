---
layout: Conceptual
title: Buy a savings plan - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/buy-savings-plan
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
description: This article provides you with information to help you buy a savings plan.
author: nwokolo
ms.reviewer: onwokolo
ms.service: cost-management-billing
ms.subservice: savings-plan
ms.topic: how-to
ms.date: 2026-10-29T00:00:00.0000000Z
ms.author: onwokolo
locale: en-us
document_id: a1154b0a-2b9a-6339-8d4f-628e55f9249c
document_version_independent_id: 594084da-7337-1d3a-6da5-004ff4d1a503
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/savings-plan/buy-savings-plan.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/savings-plan/buy-savings-plan
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/savings-plan/buy-savings-plan.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c0439c36-80e3-415f-8e4c-6951e3f1b136
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/2812d699-d85f-4a7f-839d-44e218b35d24
platformId: bc04ec91-6256-c9cc-c876-18ca0df4f3e0
---

# Buy a savings plan - Microsoft Cost Management | Microsoft Learn

Savings plans help you save money by committing to a fixed hourly spend on eligible Microsoft Cloud resources for a one-year or three-year term.

You can pay for savings plans with monthly payments. Unlike an upfront purchase, where you pay the full amount, the monthly payment option divides the total cost of the savings plan into 12 or 36 equal payments. The total cost of upfront and monthly savings plans is the same.

If you purchase a savings plan through a Microsoft Customer Agreement, your monthly payment amount might vary depending on the current month's market exchange rate for your local currency.

Before you enter a commitment to buy a savings plan, review the following sections to prepare for your purchase.

## Prerequisites

The person who buys a savings plan must have the necessary permissions. For more information, see [Permissions to buy a savings plan](permission-buy-savings-plan).

## Purchase a savings plan

You can purchase a savings plan by using the [Azure portal](https://portal.azure.com/). You can also use the [Savings Plan Order Alias - Create](/en-us/rest/api/billingbenefits/savings-plan-order-alias/create) REST API.

After you buy a savings plan, you can [change the savings plan scope](manage-savings-plan#change-the-savings-plan-scope) to a different subscription.

### Buy a savings plan in the Azure portal

1. Sign in to the Azure portal.
2. In the **Search** area, enter **Savings plans**. Then select **Savings plans**.
3. Select **Add** to purchase a new savings plan.
4. Complete all the required fields:
    - **Name**: Friendly name for the new savings plan.
    - **Billing subscription**: Subscription used to pay for the savings plan. For more information about permissions and roles required to purchase a savings plan, see [Permissions to buy a savings plan](permission-buy-savings-plan).
    - **Savings plan**: Compute or database.
    - **Apply to any eligible resource**: Scope of resources that are eligible for savings plan benefits. For more information, see [Savings plan scopes](scope-savings-plan).
    - **Term length**: One year or three years.
    - **Hourly commitment in USD**: Select a recommended value from the dropdown list or enter a custom commitment amount. Each recommendation includes:
        - The hourly commitment.
        - The potential savings percentage compared to on-demand costs for the commitment.
        - The percentage of the selected scope's resource usage that is covered by the new savings plan. It includes the commitment amount plus any other previously purchased savings plan or reservation.
    - **Billing frequency**: **All upfront** or **Monthly**. The total cost of the savings plan is the same regardless of the selected frequency.
    - **Auto-renew**: **On** or **Off**. The savings plan will automatically renew at the end of its term if it is **On**. By default, this option is set to **Off**.

### Purchase with the Savings Plan Order Alias - Create API

You can buy savings plans by using Azure role-based access control (RBAC) permissions or with permissions on your billing scope. When you use the [Savings Plan Order Alias - Create](/en-us/rest/api/billingbenefits/savings-plan-order-alias/create) REST API, the format of the `billingScopeId` property in the request body is used to control the permissions that are checked.

#### Purchase by using Azure RBAC permissions

- You must have the savings plan purchaser role within, or be an owner of, the subscription that you plan to use, which is specified as `billingScopeId`.
- The `billingScopeId` property in the request body must use the `/subscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e` format.

#### Purchase by using billing permissions

The permissions needed to purchase a savings plan vary by account type:

- **Enterprise Agreement**: You must be an Enterprise Agreement admin with write permissions.
- **Microsoft Customer Agreement**: You must be a billing profile contributor or higher.
- **Microsoft Partner Agreement**: Only Azure RBAC permissions are currently supported.

The `billingScopeId` property in the request body must use the `/providers/Microsoft.Billing/billingAccounts/{accountId}/billingSubscriptions/aaaa0a0a-bb1b-cc2c-dd3d-eeeeee4e4e4e` format.

## View savings plan purchases and payments

To learn more about viewing savings plan purchases and payments, see [View savings plan purchases](view-transactions#view-savings-plan-purchases-in-the-azure-portal) and [View payments made](view-transactions#view-payments-made), respectively.

## Cancellations, exchanges, and trade-ins

Unlike reservations, you can't cancel or exchange savings plans. You can trade in select reservations for a savings plan. To learn more, visit [Reservation trade-in](reservation-trade-in).

## Need help?

If you have savings plan questions, contact your account team or [create a support request](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest). Currently, Microsoft provides expert support for savings plans only in English.