---
layout: Conceptual
title: Align cloud investments to your purchase orders for Microsoft Marketplace - Marketplace customer documentation | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/marketplace/purchase-orders
uhfHeaderId: MSDocsHeader-Partner-Center
breadcrumb_path: /marketplace/breadcrumb/toc.json
feedback_system: None
description: Learn how to set up purchase orders for Microsoft Marketplace spend in the Azure portal.
author: kylecallahan
ms.author: v-callahanky
ms.review: kagoel
ms.service: marketplace-customer
ms.topic: quickstart
ms.date: 2026-10-19T00:00:00.0000000Z
locale: en-us
document_id: 54e0068c-fecc-b9a0-85b4-53c75953a38a
document_version_independent_id: 54e0068c-fecc-b9a0-85b4-53c75953a38a
original_content_git_url: https://github.com/MicrosoftDocs/partner-center-pr/blob/live/marketplace/purchase-orders.md
site_name: Docs
depot_name: MSDN.marketplace
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.marketplace/{branchName}{pdfName}
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: purchase-orders
moniker_range_name: 
monikers: []
item_type: Content
source_path: marketplace/purchase-orders.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/970f20f1-2f12-4aa9-9c95-c00fe1f5e722
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/432c4950-b799-4ed5-93d5-b9b2934edf7d
platformId: de14f021-508b-995b-9149-41fb03881078
---

# Align cloud investments to your purchase orders for Microsoft Marketplace - Marketplace customer documentation | Microsoft Learn

Organizations often use purchase orders to track cloud spending for budgeting, procurement, and financial reporting. As Microsoft Cloud investments grow across Azure, Microsoft products, and third-party solutions from Microsoft Marketplace, organizations may need more flexibility in how those investments are allocated with purchase orders.

## What are purchase orders in the Azure portal?

Purchase orders in the Azure portal help you align cloud investments purchased through Microsoft Marketplace with your organization's internal purchase orders, simplifying cost tracking and budget management. Azure billing administrators can create and manage purchase orders, map and review allocated spending, and generate supplemental documents that align with how their organization tracks and reconciles costs. You can also modify allocations as business needs evolve.

### When to use purchase orders

You can use purchase orders in different ways, depending on how your organization manages cloud spending.

- **Single purchase order for all cloud purchases:** Use one purchase order to track all Azure and Microsoft Marketplace spending under a single procurement record.
- **Separate purchase orders for Azure and Marketplace purchases:** Allocate Azure charges to one purchase order and Microsoft Marketplace charges to another to align with separate budgets, procurement processes, or financial reporting requirements.
- **Purchase orders by software company:** Allocate charges from a specific software company selling through Microsoft Marketplace to a dedicated purchase order.
- **Purchase orders by product or solution:** Track spending for individual Azure services or Microsoft Marketplace solutions using separate purchase orders.

### Who can allocate cloud costs with purchase orders?

Permission to create new purchase order and allocation records in the Azure portal varies depending on your Microsoft customer agreement type.

- **Microsoft Customer Agreement (MCA-E):** Billing administrator
- **Enterprise Agreement (EA):** Enterprise administrator

**Before using purchase orders**

- Ensure that the appropriate billing permissions are assigned.
- Determine how your organization wants to structure purchase orders for Azure and Microsoft Marketplace spending.
- Establish internal ownership for managing purchase orders and reviewing allocations in the Azure portal.

### What you can do

| Capability | Customer outcome |
| --- | --- |
| Create new purchase orders | Maintain purchase order records and budgets in Azure portal. |
| Map cloud investments | Associate Marketplace charges for a product, a software company, or a broader purchase category to a purchase order. |
| Review charges | Compare allocated budgets with billed and unbilled charges. |
| Modify allocations | Reassign eligible charges after invoicing when an allocation needs to change. |
| Configure supplemental documents | Choose how supporting purchase-order information is generated and grouped. |

Important

Purchase order records and supplemental documents support your organization's internal accounting and reconciliation processes. They don't replace the Microsoft invoice, change the amount due, or extend the invoice payment due date.

## Create a purchase order in the Azure portal

Create a purchase order to allocate cloud investments against an approved budget. When you create the purchase order, define its active dates, allocated budget, and status. You can also add mapping to specify which purchases across Azure and Microsoft Marketplace are allocated to the purchase order.

1. Go to **Cost Management + Billing** in the Azure portal.
2. Select a billing scope. If you're a Global administrator, select the checkbox to view all scopes in the directory.
3. In the left-hand navigation, under billing, select *Billing profiles*.
4. Select the billing profile that you want.
5. In the left-hand navigation, find the invoice management section, and select **Purchase orders**.
6. There are two tabs. *All POs* and *All mappings* provide at-a-glance list views.
7. Select the **New purchase order**button at the top of the page.
    - Enter a unique name for the purchase order.
    - Select an effective date in UTC.
    - Select an expiration date in UTC.
    - Optionally, enter notes or a description.
    - Optionally, enter an allocated budget (in your billing account currency).

### Purchase order field reference

| Field | How to use this field |
| --- | --- |
| Purchase order name | Enter a recognizable identifier to help you align with your internal procurement system record. Alphanumeric characters and dashes are acceptable. |
| Effective date (UTC) | Select the date when you want the purchase order to be eligible for allocation. |
| Expiration date (UTC) | Select the last date you want charges allocated to this purchase order. |
| Description | Add any context to explain what this purchase order is for. This information is referenced only in the purchase order details and doesn't appear on invoices or supplemental documents. |
| Allocated budget | Enter an approved amount in the currency of your customer billing profile. |
| Status | Set the status to **Active** to make the purchase order available for allocations. Set it to **Inactive** to retain the purchase order but make it unavailable for allocations. |

### Add mapping during purchase order setup

You can allocate cloud investments to purchase orders through mapping. You can map allocations during the purchase order setup or after. To establish mapping in the flow of creating a new purchase order, select the **Add a mapping to this PO** checkbox.

1. Select an option from the **Map to** dropdown menu.
2. Select an effective date in UTC for this allocation. The default is the purchase order’s effective date, but you can select any date after the purchase order effective date.
3. Select an expiration date in UTC for this allocation. The date must not be later than the purchase order’s expiration date.
4. Set the status to **Active** to enable this allocation upon the effective date. Choosing **Inactive** simply saves this mapping to the purchase order for future use.
5. For mapping to a software company, also known as a publisher, enter the *publisher ID*.
6. For mapping to a Marketplace product, enter both the *publisher ID* and *offer ID*.
7. Optionally, select **Add additional mapping** if you want to map more than one allocation to this purchase order. You might do this to allocate two products from different vendors toward the same purchase order.
8. Select **Create**.

When you add more than one mapping, a **Mapping preview** appears showing previously entered allocations. Select **Edit preview** if you want to remove a mapping before creating the purchase order. You can't change mapping values from this preview. To make a change, remove the existing mapping, then add a new one.

Tip

You can find the publisher ID and offer ID separated by "." in the URL for a Marketplace product. Example: //marketplace.microsoft.com/product/**publisherID**.**offerID**

### View purchase order details

1. Open the **Purchase orders** page to find table views of all purchase orders and mappings.
2. There are two tabs: *All POs* and *All mappings*.
3. Select **All POs** to review purchase order details at a glance.
4. Compare *utilized budget* against *allocated budget* for each purchase order.
5. Sort the view by field columns and apply filters to find specific purchase orders quickly.
6. Select a purchase order name to view the complete description and a list of *Billed charges* and *Pending charges*.
7. Select **Edit** to modify eligible field values for this purchase order.
8. Select **View PO mapping** to view all mappings filtered for that purchase order.
9. Select **Return** to go back to the table view.

### Edit purchase orders

You can edit individual purchase orders one at a time from the *Purchase order details* page or edit multiple purchase orders all at once from the *All POs* table view.

- From the *Purchase order details* view, select **Edit** on the upper left.
- From the *All POs* view, select **Edit PO** in the top right corner.

Editable fields will show a pencil icon. From this table view, you can edit the following fields for any purchase order:

- Description
- Expiration date
- Status
- Allocated budget

Updated field values will change to **bold text** and append a blue *Undo* button.

- Select *Undo* to revert changes.
- Select *Review* in the top right of the table to simplify the view and show only purchase orders with edits.
- Select *Continue edits* to expand the view to all purchase orders again.
- Select *Submit* to save all changes. A green checkmark and bar confirms "Purchase order edit request completed."

Note

Effective dates in the past and purchase order names cannot be changed.

## Enable supplemental documents

After you create purchase orders and map cloud investments to them, enable supplemental documents to generate purchase order-specific views of your billed charges. These documents help finance, procurement, and accounts payable teams reconcile Microsoft Marketplace and Azure charges against their internal purchase orders. Supplemental documents group charges according to your allocations defined by purchase order mappings and provide supporting detail that aligns Microsoft billing data with your organization's accounting and reconciliation processes. They don't replace your Microsoft invoice or change billing terms, but they can simplify month-end review and audit activities.

**To enable supplemental documents**

1. Open your billing profile and navigate to Invoice management &gt; **Invoice preferences**.
2. Turn on **Enable supplemental documents**.
3. For MCA customers, choose whether you want to **Split supplements by***purchase order* or *invoice section*. This selection does not apply for EA customers.
4. Select **Save changes**.

Note

Invoice preferences are configured at the billing profile level and apply to all supplemental documents generated for that billing profile.

### Example purchase order supplement

The following example shows a purchase order supplement document for a customer with an **Enterprise Agreement**. The document includes multiple pages with the following sections:

1. A summary section that provides customer account details, billing period, and amount due.
2. A billing details by product section that provides itemized charges, including quantity and any applicable taxes.
3. A definition of terms section.

**Summary**

[![Screenshot of a sample purchase order supplemental document showing summary charges aligned to a purchase order and invoice.](media/purchase-orders/supplement-charge-summary.png)](media/purchase-orders/supplement-charge-summary.png#lightbox)

**Billing details by product**

[![Screenshot of a sample supplemental document showing billing details by product with itemized charges.](media/purchase-orders/supplement-charge-details.png)](media/purchase-orders/supplement-charge-details.png#lightbox)

**Definitions**

A final page in the purchase order supplement provides a definition of terms used in the document.

- **Charges**: Usage and purchases from Microsoft for the period
- **Usage Charges**: Product/SKU description
- **Unit Price**: price per unit
- **Qty**: quantity of consumption for the period
- **Commitment Usage**: Credits drained form the prepaid balance (also known as monetary commit)
- **Net Charge**: Price multiplied by quantity, less commitment usage
- **Net Amount**: Charges after utilizing credits from monetary commit
- **Tax Rate**: rate of taxation per local guidelines
- **Tax Amount**: Tax rate multiplied by net charge
- **Total**: The sum of net charge plus tax amount

The following example shows a purchase order supplement document for a customer with a **Microsoft Customer Agreement**.

**Summary**

[![Screenshot of a sample supplemental document showing a summary of invoiced charges aligned to a purchase order.](media/purchase-orders/purchase-order-supplement-summary.png)](media/purchase-orders/purchase-order-supplement-summary.png#lightbox)

**Details by section**

[![Screenshot of a sample supplemental document showing details of charges organized by invoice section.](media/purchase-orders/supplement-details-by-section.png)](media/purchase-orders/supplement-details-by-section.png#lightbox)

## Learn more

- [Map cloud investments to your purchase orders](purchase-order-mapping)