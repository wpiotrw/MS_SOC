---
layout: Conceptual
title: View savings plan utilization - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/view-utilization
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
description: Learn how to view savings plan utilization in the Azure portal.
author: nwokolo
ms.reviewer: onwokolo
ms.service: cost-management-billing
ms.subservice: savings-plan
ms.topic: how-to
ms.date: 2026-10-29T00:00:00.0000000Z
ms.author: onwokolo
locale: en-us
document_id: b310f189-3173-b6e6-1aa0-5fb9500d1bd8
document_version_independent_id: e5d94a11-5c05-a7bf-aca9-604725c4976e
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/savings-plan/view-utilization.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/savings-plan/view-utilization
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/savings-plan/view-utilization.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: e037a752-f842-5b5c-ddd3-b8122f6f075f
---

# View savings plan utilization - Microsoft Cost Management | Microsoft Learn

You can view savings plan utilization percentage in the Azure portal.

Note

It can take up to 48 hours after a savings plan purchase for initial utilization data to appear in utilization reports and cost analysis. Afterward, you can expect usage data to appear within 2 to 24 hours.

## View utilization in the Azure portal with Azure RBAC access

To view savings plan utilization, you must have Azure RBAC access to the savings plan or you must have elevated access to manage all Azure subscriptions and management groups.

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Search for **Savings plans** and then select it.
3. The list shows all savings plans for which you have the Owner or Reader role. Each savings plan shows the last known utilization percentages for the last day and the last seven days.
4. Select the utilization percentage to see the utilization history.

## View utilization as billing administrator

An Enterprise Agreement (EA) administrator or a Microsoft Customer Agreement (MCA) billing administrator can view the utilization from **Cost Management + Billing**.

1. Sign in to the [Azure portal](https://portal.azure.com).
2. Go to **Cost Management + Billing** &gt; **Savings plans**.
3. Select the utilization percentage to see the utilization history.

## Get Savings plan utilization with the API

You can get [savings plan utilization data](https://go.microsoft.com/fwlink/?linkid=2209373) by using the Benefit Utilization Summary API.