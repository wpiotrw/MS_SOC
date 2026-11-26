---
layout: Conceptual
title: Understand your detailed usage and charges - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/understand/understand-usage
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
description: Learn how to read and understand your detailed usage and charges file. View a list of terms and descriptions used in the file.
author: diberry
ms.reviewer: jkinma
ms.service: cost-management-billing
ms.subservice: billing
ms.topic: concept-article
ms.date: 2026-11-19T00:00:00.0000000Z
ms.author: jkinma
service.tree.id: 95459a4b-434c-4f83-879b-aa5f509fc7fa
locale: en-us
document_id: 96771ba5-ef91-ed15-33a3-ff5e5b9e753f
document_version_independent_id: de9baa15-55e1-4cb8-32d0-6583a8b5d689
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/understand/understand-usage.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/understand/understand-usage
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/understand/understand-usage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 28d8db88-0feb-d308-e8ab-eb923cfc7dad
---

# Understand your detailed usage and charges - Microsoft Cost Management | Microsoft Learn

The detailed usage and charges file contains daily rated usage based on negotiated rates, purchases (for example, reservations, Marketplace fees), and refunds for the specified period. Fees don't include credits, taxes, or other charges or discounts. You manually download the usage and charges file.

## Charges for account types

The information in the usage and charges file is the same information that's [exported from Cost Management](../costs/tutorial-improved-exports). And, it's the same information that gets retrieved from the Cost Details API. A downloaded file keeps its schema version, and new columns, such as `priceFactors` and `supplementalChargeDetails`, are added at the end of the file. To select a dataset version, such as 2026-10-01, use exports. For more information, see [Compare downloads and exports](compare-downloads-exports). For more information about choosing a method to get cost details, see [Choose a cost details solution](../automate/usage-details-best-practices).

The following table covers which charges are included for each account type.

| Account type | Azure usage | Marketplace usage | Purchases | Refunds |
| --- | --- | --- | --- | --- |
| Enterprise Agreement (EA) | Yes | Yes | Yes | No |
| Microsoft Customer Agreement (MCA) | Yes | Yes | Yes | Yes |
| Pay-as-you-go | Yes | Yes | No | No |

To learn more about Marketplace orders (also known as external services), see [Understand your Azure external service charges](understand-azure-marketplace-charges).

For download instructions, see [How to get your Azure billing invoice and daily usage data](../manage/download-azure-invoice-daily-usage-date). You can open your usage and charges CSV file in Microsoft Excel or another spreadsheet application.

## List of terms and descriptions

If you want to see a list of all available terms in the usage and charges file, see [Understand cost details data fields](../automate/understand-usage-details-fields).

## Ensure charges are correct

To learn more about detailed usage and charges, read about how to understand your [pay-as-you-go](review-individual-bill) or [Microsoft Customer Agreement](review-customer-agreement-bill) invoice.

## Unexpected usage or charges

If you have usage or charges that you don't recognize, there are several things you can do to help understand why:

- Review the invoice that has charges for the resource
- Review your invoiced charges in Cost analysis
- Find people responsible for the resource and engage with them
- Analyze the audit logs
- Analyze user permissions to the resource's parent scope
- To help identify the charges Create an [Azure support request](https://go.microsoft.com/fwlink/?linkid=2083458)

For more information, see [Analyze unexpected charges](analyze-unexpected-charges).

Azure doesn't log most user actions. Instead, Microsoft logs resource usage for billing. If you notice a usage spike in the past and you didn't have logging enabled, Microsoft can't pinpoint the cause. Enable logging for the service that you want to view the increased usage for so that the appropriate technical team can assist you with the issue.

## Need help? Contact us.

If you have questions or need help, [create a support request](https://go.microsoft.com/fwlink/?linkid=2083458).