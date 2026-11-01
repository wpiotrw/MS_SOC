---
layout: Conceptual
title: Request Access to Data Products in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-product-access-requests
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: nidought
ms.date: 2025-02-05T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to request access to a data product in Microsoft Purview Unified Catalog.
locale: en-us
document_id: 3f4c757a-14d6-820b-ba37-a76e0e4b11e1
document_version_independent_id: 3f4c757a-14d6-820b-ba37-a76e0e4b11e1
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-product-access-requests.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-product-access-requests
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-product-access-requests.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://authoring-docs-microsoft.poolparty.biz/devrel/97159432-14a9-4307-a469-d2f2c75f0e33
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/50565c62-5f6b-4687-be38-323113c72c2e
platformId: bddf9deb-f5c0-0f86-fff5-7b1630affc7f
---

# Request Access to Data Products in Unified Catalog | Microsoft Learn

Note

This article explains how to request access to a data product. To manage access to data products, see [Manage data products access policies](unified-catalog-data-product-access-policies).

Follow the steps in this article to request access to a data product and its assets in Microsoft Purview Unified Catalog.

## Considerations

In this experience, the approvers of the request must provide access to the individual data assets manually as part of the approval process or specify an access provider to do so and record the status of access provisioned.

When you receive confirmation that your request is approved or see the status change on the Unified Catalog **Data product search** page in the **My data access** tab, you can view the details on how to access and use the data. Learn how to [access and use data products](unified-catalog-data-products-search).

## How to request access to a data product

If you discover a data product in the catalog that you want to access, you can request access directly through Microsoft Purview. The request triggers a workflow that asks the owners of the data resource to grant you access to the data product.

This article outlines how to make an access request.

1. In Unified Catalog, select **Discovery**, then select **Data products**.
2. To find a data product, [search or browse for it](unified-catalog-data-products-search) by entering a keyword or natural language in the search bar.
3. Select the data product to open the data product details page.
4. Select **Request access**.
5. Fill in the form. The form is different depending on your organization and the data product, but provide all information.
6. When you're finished, select **Send**.

Approval requests are sent to all involved parties. When your request is approved or rejected, you get an email notification.

## How to view data product access requests

You can see all your requests in Unified Catalog by selecting **Discovery**, then **Data products**, and selecting the **My data access** tab.

Select a data product name to open the **Access Request** flyout pane. This detailed request view helps you understand the approvals or actions taken, and view the asset level access provisioning status and any instructions, if provided.

### Request statuses

- **Pending**: The approver receives the request for review.
- **Declined**: The approver denies the request.
- **Approved**: The approver grants the request but hasn't finished provisioning access for the requestor.
- **Completed**: The data asset is provisioned, and the request is fully complete.

## How to cancel an access request

You can cancel an access request if it isn't in the **Completed** status. To cancel an access request:

1. In Unified Catalog, select **Discovery**, then **Data products**, then the **My data access** tab.
2. On the **Access Request** flyout pane, select **Delete**.

If your request is approved and completed, only the data product owner can delete it. The data owner must manually deprovision access to individual assets before [deleting a request](unified-catalog-data-product-access-policies#delete-access-requests).