---
layout: Conceptual
title: Manage savings plans - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/manage-savings-plan
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
description: Learn how to manage savings plans. See steps to change the plan's scope, split a plan, and optimize its use.
author: nwokolo
ms.reviewer: onwokolo
ms.service: cost-management-billing
ms.subservice: savings-plan
ms.topic: how-to
ms.date: 2026-10-29T00:00:00.0000000Z
ms.author: onwokolo
locale: en-us
document_id: e6f181fa-d509-caf1-0251-37377e364db9
document_version_independent_id: 735af54c-9b7a-a3fb-6abe-40342878b2b1
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/savings-plan/manage-savings-plan.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/savings-plan/manage-savings-plan
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/savings-plan/manage-savings-plan.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
platformId: 525fca95-f061-ae17-f9c3-4bea1cbee7c4
---

# Manage savings plans - Microsoft Cost Management | Microsoft Learn

After you buy a savings plan, you can make the following changes if you have sufficient permissions:

- Update a savings plan scope.
- Change autorenewal settings.
- View savings plan details and utilization.
- Delegate savings plan role-based access control (RBAC) roles.

Except for autorenewal, these changes don't create a new commercial transaction or change the savings plan's end date.

You can't make the following types of changes after purchase:

- Hourly commitment
- Term length
- Billing frequency

Note

A billing administrator can fully manage savings plans. However, after purchase, a savings plan's directory can't be changed.

To learn more, see [Savings plan permissions](permission-view-manage). *Permission needed to manage a savings plan is separate from subscription permission.*

## Change the savings plan scope

Your hourly savings plan benefit automatically applies to savings plan-eligible resources that run in the savings plan's benefit scope. To learn more, see [Savings plan scopes](scope-savings-plan). Changing a savings plan's benefit scope doesn't alter the savings plan's term.

To update a savings plan scope as a billing administrator:

1. Sign in to the Azure portal and go to **Cost Management + Billing**.
    - If you're an Enterprise Agreement admin, on the left menu, select **Billing scopes**. Then in the list of billing scopes, select one.
    - If you're a Microsoft Customer Agreement billing profile owner, on the left menu, select **Billing profiles**. In the list of billing profiles, select one.
2. On the left menu, select **Products + services** &gt; **Savings plans**. The list of savings plans for your Enterprise Agreement enrollment or billing profile appears.
3. Select the savings plan you want.
4. Select **Settings** &gt; **Configuration**.
5. Change the scope.

If you purchased a savings plan, were added to one, or were assigned savings plan RBAC roles, follow these steps to update its scope.

1. Sign in to the Azure portal.
2. Select **All Services** &gt; **Savings plans** to list savings plans to which you have access.
3. Select the savings plan you want.
4. Select **Settings** &gt; **Configuration**.
5. Change the scope.

Selectable scopes must be associated with Enterprise offers (MS-AZR-0017P or MS-AZR-0148P), Microsoft Customer Agreements, or Microsoft Partner Agreements.

If you aren't a billing administrator and you change from shared to single scope, you can only select a subscription where you're the owner. Only subscriptions within the same billing account/profile as the savings plan can be selected.

If all subscriptions are moved out of a management group, the scope of the savings plan is automatically changed to **Shared**.

## Change the auto-renewal setting

To learn more about modifying auto-renewal settings for a savings plan, see [Change auto-renewal settings](manage-savings-plan#change-the-auto-renewal-setting).

## View savings plan reporting details

- To learn more about viewing savings plan utilization, see [View savings plan utilization](view-utilization).
- To learn more about viewing savings plan cost and usage, see [View savings plan cost and usage exports](utilization-cost-reports).
- To learn more about viewing savings plan transactions, see [View savings plan transactions](view-transactions).
- To learn more about viewing savings plan amortized costs, see [View amortized costs](../reservations/view-amortized-costs).

## Delegate savings plan RBAC roles

Users and groups who gain the ability to purchase, manage, or view savings plans via RBAC roles must do so from **Home** &gt; **Savings plan**.

### Delegate the savings plan purchaser role to a specific subscription

After you elevate access, follow these steps to delegate the purchaser role to a specific subscription:

1. Go to **Home** &gt; **Savings plans** to see all savings plans that are in the tenant.
2. To make modifications to the savings plan, add yourself as an owner of the savings plan order by using **Access control (IAM)**.

### Delegate savings plan administrator, contributor, or reader roles to a specific savings plan

To delegate the administrator, contributor, or reader roles to a specific savings plan:

1. Go to **Home** &gt; **Savings plans**.
2. Select the savings plan you want.
3. Select **Access control (IAM)** on the leftmost pane.
4. Select **Add**, and then select **Add role assignment** from the top navigation bar.

### Delegate savings plan administrator, contributor, or reader roles to all savings plans

[User Access administrator](../../role-based-access-control/built-in-roles#user-access-administrator) rights are required to grant RBAC roles at the tenant level. To get User Access administrator rights, follow the steps in [Elevate access steps](../../role-based-access-control/elevate-access-global-admin).

### Delegate the administrator, contributor, or reader role to all savings plans in a tenant

1. Go to **Home** &gt; **Savings plans**.
2. Select **Role assignment** from the top navigation bar.

## Cancellations, exchanges, and trade-ins

Unlike reservations, you can't cancel or exchange savings plans. You can trade in eligible compute or database reservations for a savings plan. To learn more, see [reservation trade-in](reservation-trade-in).

## Change billing subscription

Currently, the billing subscription used for monthly payments of a savings plan can't be changed.

## Check billing subscription for a savings plan

To check the billing subscription for a savings plan:

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Select **All services** &gt; **Savings plans**.
3. Select the savings plan.
4. Select **Renewal**.
5. Select **Replace this savings plan with a new savings plan purchase**.

These steps show the billing subscription of the current savings plan and other details. You can update details such as scope, billing subscription, quantity, term, and billing frequency for the new savings plan, which is purchased automatically when the current savings plan expires.

## Transfer a savings plan

Although you can't cancel, exchange, or refund a savings plan, you can transfer it from one supported agreement to another. For more information about supported transfers, see [Azure product transfer hub](../manage/subscription-transfer#product-transfer-support).

## Savings plan notifications

Depending on how you pay for your Azure subscription, the users listed in the following sections receive savings plan-related email notifications. The system sends notifications for the following events:

- Purchase
- Scope change
- Upcoming expiration: 30 days before
- Expiration
- Renewal
- Cancellation

For customers with Enterprise Agreement subscriptions:

- Notifications are sent to Enterprise Agreement administrators and Enterprise Agreement notification contacts.
- The Azure RBAC owner of the savings plan receives all notifications.

For customers with Microsoft Customer Agreement subscriptions:

- The purchaser receives a purchase notification.
- The Azure RBAC owner of the savings plan receives all notifications.

For Microsoft Partner Agreement partners:

- Notifications are sent to the partner.

## Need help?

If you have savings plan questions, contact your account team or [create a support request](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest). Currently, Microsoft provides expert support for savings plans only in English.