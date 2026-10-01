---
layout: Conceptual
title: Manage a Conditional Azure Credit Offer (CACO) Resource - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/benefits/caco/manage-conditional-credit-offer
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
description: Learn how to manage your Conditional Azure Credit Offer (CACO) resource, including moving it across resource groups or subscriptions.
author: pri-mittal
ms.reviewer: primittal
ms.service: cost-management-billing
ms.subservice: billing
ms.topic: how-to
ms.date: 2026-09-30T00:00:00.0000000Z
ms.author: primittal
service.tree.id: b69a7832-2929-4f60-bf9d-c6784a865ed8
locale: en-us
document_id: 68c90f42-f97d-939e-f735-9b56a5a20ea1
document_version_independent_id: bb503949-4a9d-1b89-421c-c0dcbad14efa
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/benefits/caco/manage-conditional-credit-offer.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/benefits/caco/manage-conditional-credit-offer
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/benefits/caco/manage-conditional-credit-offer.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: f5367bc4-1b89-6465-8a83-086ca987d12f
---

# Manage a Conditional Azure Credit Offer (CACO) Resource - Microsoft Cost Management | Microsoft Learn

When you accept a Conditional Azure Credit Offer (CACO) in a Microsoft Customer Agreement, Microsoft creates a CACO commitment and one or more provisional (not spendable) credit resources. The commitment and provisional credit resources are placed in a subscription and a resource group. They follow the same setup as other credit resources, as described in [Manage an Azure credit resource under a subscription](../credits/manage-azure-credits). The provisional credit resources turn into awarded credits if you meet the spending target and other conditions in the CACO.

In the Azure portal, you can view metadata for a CACO. The metadata includes the status of the offer, start and end dates, spending target, currency, target end date, award credit, award start date, award end date, and system ID. You can view the metadata under the CACO resource.

[![Screenshot that shows the Conditional Azure Credit Offer overview pane.](../../manage/media/conditional-credit-offer/view-conditional-credit-offer.png)](../../manage/media/conditional-credit-offer/view-conditional-credit-offer.png#lightbox)

## Move a CACO resource across resource groups or subscriptions

You can move a CACO resource to another resource group or subscription, just like other Azure resources. This move only changes metadata and doesn't affect the credit or commitment.

The new resource group or subscription must remain within the same billing profile as the original billing profile that contains the CACO resource.

Moving a CACO resource doesn't move any provisional or awarded credits. You have to move those credit resources separately as needed.

### Move a CACO resource

Here are the high-level steps to move a CACO resource. For more information about moving an Azure resource, see [Move Azure resources to a new resource group or subscription](../../../azure-resource-manager/management/move-resource-group-and-subscription).

1. In the [Azure portal](https://portal.azure.com), go to **Resource groups**.
2. Select the resource group that contains the CACO resource.
3. Select the resource.
4. At the top of the pane, select **Move**, and then select **Move to another subscription** or **Move to another resource group**.
5. Follow the instructions to move the resource.
6. After the move is complete, verify that the resource is in the new resource group or subscription.

Moving a CACO resource changes its URI.

### View the CACO resource URI

1. In the [Azure portal](https://portal.azure.com), enter **conditional credit** in the search box.
2. Under **Services**, select **Conditional Credits**.
3. Select the CACO resource.
4. On the left pane, expand **Settings**, and then select **Properties**.
5. The CACO resource URI is the **Id** value.

[![Screenshot that shows an example Conditional Azure Credit Offer resource URI on the Properties pane.](../../manage/media/conditional-credit-offer/conditional-credit-offer-uri.png)](../../manage/media/conditional-credit-offer/conditional-credit-offer-uri.png#lightbox)

## Rename a CACO resource

The name of a CACO resource is a part of its URI and can't be changed. However, you can use [tags](../../../azure-resource-manager/management/tag-resources) to help identify the CACO resource based on a nomenclature that's relevant to your organization.

## Delete a CACO resource

You can delete a CACO resource only if its status is **Failed**, **Canceled**, or **Expired**. Deletion of a CACO resource is a permanent action and can't be undone.

## Cancel a CACO

If you have questions about canceling your CACO, contact your Microsoft account team.