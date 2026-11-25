---
layout: Conceptual
title: No subscriptions found error - Azure portal sign in - Microsoft Cost Management | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/cost-management-billing/troubleshoot-subscription/no-subscriptions-found
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
description: Provides the solution for a problem in which No subscriptions found error occurs during Azure portal sign in.
author: mjeffer
ms.author: diberry
ms.reviewer: mjeffer
ms.service: cost-management-billing
ms.subservice: billing
ms.topic: troubleshooting
ms.date: 2026-06-15T00:00:00.0000000Z
ms.custom: sfi-image-nochange
service.tree.id: b69a7832-2929-4f60-bf9d-c6784a865ed8
locale: en-us
document_id: 27983d8d-b2af-4b0d-72e5-4aaeebd28c97
document_version_independent_id: 4c7b01dc-5bf6-1de6-bcd3-ce5603549609
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/cost-management-billing/troubleshoot-subscription/no-subscriptions-found.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: cost-management-billing/troubleshoot-subscription/no-subscriptions-found
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/cost-management-billing/troubleshoot-subscription/no-subscriptions-found.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
- https://authoring-docs-microsoft.poolparty.biz/devrel/1d9b4802-f23d-41f1-9e27-65deeceacb8d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
- https://authoring-docs-microsoft.poolparty.biz/devrel/820483fb-3aa1-4b86-bc99-9a906a24f579
platformId: c6a87cb1-cf70-cc43-14af-5451a90bf228
---

# No subscriptions found error - Azure portal sign in - Microsoft Cost Management | Microsoft Learn

You might receive a "No subscriptions found" error message when you try to sign in to the [Azure portal](https://portal.azure.com/). This article provides a solution for this problem.

## Symptom

When you try to sign in to the [Azure portal](https://portal.azure.com/), you receive the following error message: `No subscriptions found`.

## Cause

This problem occurs if you selected at the wrong directory, or if your account doesn’t have sufficient permissions.

## Solution

### Scenario: Error message is received in the [Azure portal](https://portal.azure.com)

To fix this issue:

- Make sure that the correct Azure directory is selected by selecting your account at the top right. Then, either select **Switch directory**, or select the correct directory from the list.

    ![Screenshot showing select the directory at the top right of the Azure portal.](media/no-subscriptions-found/directory-switch.png)
- If the right Azure directory is selected but you still receive the error message, [assign the Owner role to your account](/en-us/azure/role-based-access-control/role-assignments-portal).

## Need help? Contact us.

If you have questions or need help, [create a support request](https://go.microsoft.com/fwlink/?linkid=2083458).