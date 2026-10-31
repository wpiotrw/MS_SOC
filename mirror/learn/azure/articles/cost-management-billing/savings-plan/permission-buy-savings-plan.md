---
layout: Conceptual
title: Permissions to buy a savings plan - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/permission-buy-savings-plan
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
description: This article provides you with information to understand who can buy a savings plan.
author: nwokolo
ms.reviewer: onwokolo
ms.service: cost-management-billing
ms.subservice: savings-plan
ms.topic: how-to
ms.date: 2026-10-29T00:00:00.0000000Z
ms.author: onwokolo
locale: en-us
document_id: c07a2539-c8e0-1ff9-1960-c781feb8e1a6
document_version_independent_id: 976ff739-8e6f-cd05-fc85-54073a72f47a
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/savings-plan/permission-buy-savings-plan.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/savings-plan/permission-buy-savings-plan
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/savings-plan/permission-buy-savings-plan.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
platformId: 13e71011-d7cc-aa10-182e-c78be719bc5b
---

# Permissions to buy a savings plan - Microsoft Cost Management | Microsoft Learn

Savings plan discounts apply only to resources associated with subscriptions purchased through an Enterprise Agreement, Microsoft Customer Agreement, or Microsoft Partner Agreement. You can buy a savings plan for an Azure subscription under an Enterprise Agreement (MS-AZR-0017P or MS-AZR-0148P), Microsoft Customer Agreement, or Microsoft Partner Agreement. To determine whether you're eligible to buy a plan, [check your billing type](../manage/view-all-accounts#check-the-type-of-your-account).

Note

The savings plan isn't supported for the China legacy Online Service Premium Agreement (OSPA) platform.

### Enterprise Agreement customers

Savings plan purchasing for Enterprise Agreement customers is limited to:

- Enterprise Agreement admins with write permissions can purchase savings plans from **Cost Management + Billing** &gt; **Savings plan**. No subscription-specific permissions are needed.
- Users with subscription owner or savings plan purchaser roles in at least one subscription in the enrollment account can purchase savings plans from **Home** &gt; **Savings plan**.

Enterprise Agreement (EA) customers can limit purchases to EA admins by disabling the **Add Savings Plan** policy option in the [Azure portal](https://portal.azure.com/#blade/Microsoft_Azure_GTM/ModernBillingMenuBlade/BillingAccounts). To change settings, navigate to the **Policies** menu.

### Microsoft Customer Agreement customers

Savings plan purchasing for Microsoft Customer Agreement customers is limited to:

- Users with billing profile contributor permissions or higher can purchase savings plans from **Cost Management + Billing** &gt; **Savings plan** experience. No subscription-specific permissions are needed.
- Users with subscription owner or savings plan purchaser roles in at least one subscription in the billing profile can purchase savings plans from **Home** &gt; **Savings plan**.

Microsoft Customer Agreement (MCA) billing profile owners can restrict savings plan purchases by disabling the **Add Savings Plan** policy option in the [Azure portal](https://portal.azure.com/#blade/Microsoft_Azure_GTM/ModernBillingMenuBlade/BillingAccounts). Since June 2025, MCA billing profile owners and billing account owners can purchase savings plans even if the **Add Savings Plan** policy option is disabled in the Azure portal. To change settings, go to the **Policies** menu under **Billing Profile**.

### Microsoft Partner Agreement partners

Partners can use **Home** &gt; **Savings plan** in the [Azure portal](https://portal.azure.com/) to purchase savings plans on behalf of their customers.

As of June 2023, partners can purchase a savings plan through the Partner Center. Previously, the savings plan was only supported for purchase through the Azure portal. Partners can now purchase a savings plan through the Partner Center portal or APIs. They can also continue to use the Azure portal.

To purchase a savings plan by using the Partner Center APIs, see [Purchase savings plans](/en-us/partner-center/developer/azure-purchase-savings-plan).

## Need help?

If you have savings plan questions, contact your account team or [create a support request](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest). Currently, Microsoft provides expert support for savings plans only in English.