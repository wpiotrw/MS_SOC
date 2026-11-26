---
layout: Conceptual
title: Monitor and track Azure free service usage - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/check-free-service-usage
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/118/azure-cost-management/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/ebeaa30a-2425-ec11-b6e6-000d3a4f0f84
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
description: Learn how to check free service usage in the Azure portal. There's no charge for services included in a free account unless you go over the service limits.
author: diberry
ms.author: diberry
ms.reviewer: mjeffer
ms.service: cost-management-billing
ms.subservice: billing
ms.topic: how-to
ms.date: 2026-06-15T00:00:00.0000000Z
ms.custom:
- sfi-image-nochange
- build-2025
service.tree.id: b69a7832-2929-4f60-bf9d-c6784a865ed8
locale: en-us
document_id: cc1b9f94-0697-7726-d678-1439a30005a0
document_version_independent_id: 13c3c83f-6033-d428-2b81-d2558cc71a13
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/manage/check-free-service-usage.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/manage/check-free-service-usage
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/manage/check-free-service-usage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
platformId: 03ff27d3-45ff-895c-04ed-fc3df6fad27a
---

# Monitor and track Azure free service usage - Microsoft Cost Management | Microsoft Learn

You're not charged for services included for free with your Azure free account, unless you exceed the limits of the services. To remain in the limits, you can use the Azure portal to track the free service usage.

Usage only appears in the Azure portal after you start using free resources so if you haven't used any resources, usage isn't shown. Note that usage and status doesn't immediately appear. It's delayed for one to two days after you use a resource.

## Check usage in the Azure portal

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Search for **Subscriptions**.![Screenshot that shows search in the Azure portal for subscriptions.](media/check-free-service-usage/billing-search-subscriptions.png)
3. Select the subscription that was created when you signed up for your Azure free account.
4. The page shows your free service usage.[![Screenshot showing the free account subscription page where you see your Azure usage.](media/check-free-service-usage/free-account-subscription-page.png)](media/check-free-service-usage/free-account-subscription-page.png#lightbox)

The page has the following usage areas:

- **Spending rate and forecast** - Shows the cost of resources that you've used over time. Select **View details** to get a more detailed view of your spending in Cost analysis.
- **Cost by resource** - Shows the costs for individual resources that you've used. Select **View details** to get a more detailed view of your spending in Cost analysis.
- **Top free services by usage** - The area only appears for Free accounts, so if you don't have a Free account, the area isn't shown. The area shows the free services that you've used. Select the **View all free services** to view the **Free services for 12 months**table that shows the following columns:
    - **Meter** - Identifies the unit of measure for the service being consumed.
    - **Usage/Limit** - Current month's usage and limit for the meter.
    - **Status**- Usage status of the service. Based on your usage, you can have one of the following statutes:
        - **Not in use** - You haven't used the meter or the usage for the meter hasn't reached the billing system.
        - **Exceeded on &lt;Date&gt;** - You've exceeded the limit for the meter on &lt;Date&gt;.
        - **Unlikely to Exceed** - You're unlikely to exceed the limit for the meter.
        - **Exceeds on &lt;Date&gt;** - You're likely to exceed the limit for the meter on &lt;Date&gt;.[![Screenshot showing the Free services for 12 months table.](media/check-free-service-usage/free-services-table.png)](media/check-free-service-usage/free-services-table.png#lightbox)
- **Top products by number of resources** - Shows the highest number of product resources that you've used.
- **Azure Defender coverage** - Shows your Azure Defender usage. Select **Upgrade coverage** to enable Microsoft Defender by starting a 30-day free trial.

Important

Free services are only available for the subscription that was created when you signed up for your Azure free account. If you can't see the free services table in the subscription overview page, they are not available for the subscription.

## Need help? Contact us.

If you have questions or need help, [create a support request](https://go.microsoft.com/fwlink/?linkid=2083458).