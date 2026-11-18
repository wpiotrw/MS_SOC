---
layout: Conceptual
title: Manage a Flex Plan - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/benefits/flex-plan/manage-flex-plan
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
description: View utilization, scope, and other settings for a Flex Plan.
author: pri-mittal
ms.service: cost-management-billing
ms.subservice: billing
ms.topic: how-to
ms.date: 2026-11-10T00:00:00.0000000Z
ms.author: primittal
locale: en-us
document_id: d04ac496-959f-0ca6-13fd-e8a6606959ae
document_version_independent_id: 0baf6836-4534-cbf0-6294-eb55ad4f1936
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/benefits/flex-plan/manage-flex-plan.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/benefits/flex-plan/manage-flex-plan
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/benefits/flex-plan/manage-flex-plan.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
platformId: 1db92dea-3715-bc17-5ba8-9cbed95b836c
---

# Manage a Flex Plan - Microsoft Cost Management | Microsoft Learn

After purchasing a Flex Plan, use the Azure portal to monitor utilization, change supported settings, and manage access.

## Open a Flex Plan

1. Sign in to the [Azure portal](https://portal.azure.com/).
2. Search for and select **Flex Plans**.
3. Select the plan you want to manage.

The overview shows plan information such as:

- Status
- Original and remaining commitment
- Amount used
- Term start and end dates
- Billing frequency
- Benefit scope
- Subscription and resource group

## Manage a seller-purchased Flex Plan

If a seller purchases a Flex Plan on your behalf, it appears under the account used for the purchase. You don't need to purchase it again.

Open the plan from **Flex Plans** in the Azure portal. With the appropriate permissions, you can:

- View the plan details, status, and term.
- Monitor utilization and remaining balance.
- Change its benefit scope.
- Manage access and tags.

Seller purchase doesn't automatically grant you management permissions. If the plan isn't visible or a management action isn't available, confirm the account used for the purchase and your role assignments.

## View utilization

Select **Utilization** to see how covered usage consumes the Flex Plan commitment over time.

The chart shows:

- **Used**: The eligible spend applied to the commitment as of each day.
- **Unused**: The portion of the commitment that remains.

Together, the used and unused values equal the full commitment. Use the **Unit** selector to view utilization as either:

- Percentage of the total commitment
- Amount in the plan's currency

Use the date controls to show the last seven days, month, three months, year, three years, or a custom period within the plan term. Hover over the chart to see the used and unused values for a specific day.

Utilization data can be delayed by up to 24 hours. Data displayed for the latest day might be incomplete.

Flex Plan owners receive email notifications when utilization reaches configured thresholds, including 50 percent and 80 percent. The notifications help owners review consumption pace before the balance is exhausted or the term expires.

## Change the benefit scope

The benefit scope controls which resources can draw from the Flex Plan. Available options can include single resource group, single subscription, shared, and management group scope.

To change scope:

1. Open the Flex Plan.
2. Select **Settings** &gt; **Configuration**.
3. Select an available benefit scope.
4. If required, select the subscription, resource group, or management group.
5. Save the change.

Changing the benefit scope doesn't move the Flex Plan resource or restart its term.

If the plan no longer has a valid subscription in its configured scope, Microsoft changes the scope to **Shared** and sends an email notification to the Flex Plan owners.

## View transactions and amortized costs

Use Cost Management and billing views to review:

- Purchase transactions
- Monthly charges
- Covered usage
- Benefit deductions
- Amortized costs
- Unused value at expiration

Amortized views help allocate the commitment across the resources and products that consumed the benefit.

## Manage access

Select **Access control (IAM)** to add or remove role assignments for the Flex Plan.

Users need separate permissions to:

- View the plan
- Change its scope
- Assign access
- Manage the subscriptions, resource groups, or management groups used as a scope

For purchase permissions, see [Buy a Flex Plan](buy-flex-plan).

## Move the Flex Plan resource

You can move the Flex Plan resource between supported resource groups or subscriptions only when the source and destination are within the same billing entity.

Moving the resource changes its Azure resource location. It doesn't automatically change the benefit scope.

Transfers across billing entities aren't supported.

## Cancellation and exchanges

Self-service cancellation isn't supported. You can't exchange a Flex Plan for a reservation, savings plan, another Flex Plan, or another commitment benefit.

For Cloud Solution Provider (CSP) subscriptions, the associated Flex Plan is automatically canceled when subscription cancellation or transfer is initiated, not when the operation completes. This automatic cancellation is separate from self-service cancellation of a Flex Plan.

Flex Plans aren't transferred across billing entities as part of a subscription transfer.

## Notifications

Flex Plan owners receive email notifications for the following events:

- Purchase completion or failure
- Scope changes
- 50-percent utilization
- 80-percent utilization
- Upcoming expiration
- Expiration

Keep Flex Plan owner assignments current so the appropriate people receive notifications.