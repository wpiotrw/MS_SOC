---
layout: Conceptual
title: Error when creating a VM as an Azure Enterprise user - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/troubleshoot-billing/cannot-create-vm
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
description: Provides several solutions to an issue in which you can't create a VM as an Enterprise Agreement (EA) user in portal.
ms.topic: troubleshooting
author: diberry
ms.author: diberry
ms.reviewer: mjeffer
ms.service: cost-management-billing
ms.subservice: billing
ms.date: 2026-06-15T00:00:00.0000000Z
ms.custom:
- build-2025
service.tree.id: b69a7832-2929-4f60-bf9d-c6784a865ed8
locale: en-us
document_id: 1f00b87a-877c-5871-8d8f-31e55c12c5ab
document_version_independent_id: bce065f0-7c1a-629c-7030-25011b2327ed
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/troubleshoot-billing/cannot-create-vm.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/troubleshoot-billing/cannot-create-vm
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/troubleshoot-billing/cannot-create-vm.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
platformId: 2bbb580c-e6d2-a120-e3f3-aa2aded1865b
---

# Error when creating a VM as an Azure Enterprise user - Microsoft Cost Management | Microsoft Learn

This article provides several solutions to an issue in which you can't create a VM as an Azure Enterprise Agreement (EA) user in portal.

*Original product version:* Billing *Original KB number:* 4091792

## Symptoms

When you create a VM as an EA user in the [Azure portal](https://portal.azure.com/), you receive the following message:

`Retail prices displayed here. Contact your reseller for accurate pricing.`

![Screenshot of the price error message.](media/cannot-create-vm/price-error.png)

## Cause

This issue occurs in one of the following scenarios:

- You're a direct EA user, and **AO view charges** or **DA view charges** is disabled.
- You're an indirect EA user who has **release markup** enabled and **AO view charges** or **DA view charges** disabled.
- You're an indirect EA user who has **release markup** not enabled.
- You use an EA dev/test subscription under an account that isn't marked as dev/test in the Azure portal.

## Resolution

Follow these steps to resolve the issue based on your scenario.

### Scenario 1

When you're a direct or indirect EA user who has **release markup** enabled and **AO view charges** or **DA view charges** disabled, you can use the following workaround:

1. Sign in to the [Azure portal](https://portal.azure.com/#blade/Microsoft_Azure_GTM/ModernBillingMenuBlade/AllBillingScopes).
2. Navigate to **Cost Management + Billing**.
3. In the left menu, select **Billing scopes** and then select a billing account scope.
4. In the left navigation menu, select **Policies**.
5. Enable **Department Admins can view charges** and **Account Owners view charges**.

### Scenario 2

When you're an indirect EA user who has **release markup** disabled, you can contact the reseller for accurate pricing.

### Scenario 3

When you use an EA dev/test subscription under an account that isn't marked as dev/test in the Azure portal, you can use the following workaround:

1. Sign in to the [Azure portal](https://portal.azure.com/#blade/Microsoft_Azure_GTM/ModernBillingMenuBlade/AllBillingScopes).
2. Navigate to **Cost Management + Billing**.
3. In the left menu, select **Billing scopes** and then select a billing account scope.
4. In the left menu, select **Accounts**.
5. Find the account that has the issue and in the right side of the window, select the ellipsis symbol (**...**) and then select **Edit**.
6. In the Edit account window, select **Dev/Test** and then select **Save**.