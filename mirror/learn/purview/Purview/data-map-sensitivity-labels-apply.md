---
layout: Conceptual
title: Apply sensitivity labels to your data in Microsoft Purview Data Map (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-sensitivity-labels-apply
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2025-07-09T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to create sensitivity labels and automatically apply them to your data during a scan in Microsoft Purview Data Map.
ms.custom: sfi-image-nochange
locale: en-us
document_id: b8f2c29a-9437-82dd-6789-56787c3160d7
document_version_independent_id: b8f2c29a-9437-82dd-6789-56787c3160d7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-sensitivity-labels-apply.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-sensitivity-labels-apply
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-sensitivity-labels-apply.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: 5b02e8ca-ab25-dd8d-61b1-33066a5a8254
---

# Apply sensitivity labels to your data in Microsoft Purview Data Map (preview) | Microsoft Learn

Important

Labeling in the Microsoft Purview Data Map is currently in preview and involves [pay-as-you-go billing model](purview-billing-models#pay-as-you-go-billing-model). The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, preview, or otherwise not yet released into general availability.

## Create new or apply existing sensitivity labels in Data Map

If you don't already have sensitivity labels, you need to create them and make them scoped for **Files & other data assets**. Existing sensitivity labels from Microsoft Purview Information Protection can also be modified with this scope to make them available to Data Map.

### Step 1: Licensing requirements

Sensitivity labels are created and managed in the Microsoft Purview Information Protection. To create sensitivity labels for use through Microsoft Purview, you must have an active Microsoft 365 license that offers the benefit of automatically applying sensitivity labels and set up of pay as you go billing model.

To understand pay as you go billing by assets protected, see this [pay-as-you-go billing model](purview-billing-models#pay-as-you-go-billing-model). For information about the specific licenses required, see this [information on sensitivity labels](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-information-protection-sensitivity-labeling). Microsoft 365 E5 trial licenses can be attained for your tenant by navigating [here](https://signup.microsoft.com/signup?ShowInternalOffers=true&amp;OfferId=f6f20264-e785-4749-bd8e-884bab076de4) from your environment. For the full list of licenses, see the [Sensitivity labels in Microsoft Purview FAQ](data-map-sensitivity-labels-faq). If you don't already have the required license, you can sign up for a trial of [Microsoft 365 E5](https://www.microsoft.com/microsoft-365/business/compliance-solutions#midpagectaregion).

### Step 2: Create or modify existing label to be scoped to "Files & other data assets" so they're available for Data Map

To create new sensitivity labels or modify existing labels, follow these instructions:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Information Protection** card &gt; **Sensitivity labels**. If the **Information Protection** solution card isn't displayed, select **View all solutions** and then select **Information Protection** from the **Data Security** section.
2. Select **+ Create a label**.
3. Name the label. Then, under **Define the scope for this label**, select **Files & other data assets**.
4. Follow the rest of the prompts to configure the label settings. For more information about configuration options, see [What sensitivity labels can do](sensitivity-labels#what-sensitivity-labels-can-do) in the Microsoft 365 documentation.
5. To modify existing labels, browse to **Information Protection** &gt; **Labels**, and select your label. Then select **Edit label** to open the **Edit sensitivity label** configuration, with all of the settings you defined when you created the label.
6. When you're done creating all of your labels, make sure to view your label order, and reorder them as needed.

    To change the order of a label, select **...** **&gt; More actions** &gt; **Move up** or **Move down.**

    For more information, see the documentation for [label priority (order matters)](sensitivity-labels#label-priority-order-matters).

### Step 3: Create auto-labeling policies scoped to non-Microsoft 365 workloads

To create an auto-labeling policy for non-Microsoft 365 workloads, follow these instructions:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com/). Go to **Information Protection** &gt; **Policies** &gt; **Auto-labeling policies**.
2. Select **+ Create auto-labeling policy**.
3. At **Choose info you want this label applied to**, you can select any **non-enhanced** templated or Custom.
4. Name your auto-labeling policy and give it an optional description.
5. Select a sensitivity label with the **Files & other data assets** scope.
6. Keep the admin units set as **Full directory**, then select **Next**.
7. Select the non-Microsoft 365 locations you want to label. Select to label all assets within a location or specify which assets in each location you want to label. If you don't see a supported data source show up in the auto-labeling policy for selection, verify that the data source was correctly registered and shows up in Data Map. The locations displayed for auto-labeling policy scoping depend on what assets have already been registered. Check the list of [supported data sources for auto-labeling](data-map-data-sources).
8. Define **Common rules** to specify the same auto-labeling conditions/rules across multiple selected non-Microsoft locations. Select **Advanced rules** to define different specific rules for each location.
9. Create a new rule and select Microsoft's prebuilt, out of the box classifiers as conditions for auto-labeling. Custom sensitive info types and advanced classifiers like named entities (All Full Names, All Physical Addresses), trainable classifiers, credentials, and Exact Data Match are **not** supported.
10. Select **Run policy in simulation mode**, and select the checkbox if you want to automatically turn on the policy after seven days.

    Note

    Microsoft Purview Data Map locations don't support simulation.
11. Review your selected configurations and select **Create policy**.

### Step 4: Scan your data to apply sensitivity labels automatically

Wait 15 minutes after auto-labeling policy creation for policy to saturate. Scan your data in Data Map to automatically apply the labels you've created, based on the auto-labeling policy you've defined.

For more information on how to set up scans on various assets in Data Map, find [links to each data source that connect to Data Map](data-map-data-sources).

## View labels on assets in the catalog

Once you've configured auto-labeling policies for the non-Microsoft 365 workloads in Microsoft Purview Information Protection and scanned your data in Data Map, labels are automatically applied to your assets in Data Map.

**To view the labels applied to your assets in the Microsoft Purview catalog:**

In Microsoft Purview Unified Catalog, use the **Label** filtering options to show assets with specific labels only. For example:

[![Search for assets by label](media/how-to-automatically-label-your-content/filter-search-results-small.png)](media/how-to-automatically-label-your-content/filter-search-results.png#lightbox)

To view details of an asset including classifications found and label applied, select the asset in the results.

For example:

[![View a sensitivity label on a file in your Azure Blob Storage](media/how-to-automatically-label-your-content/view-labeled-files-blob-storage-small.png)](media/how-to-automatically-label-your-content/view-labeled-files-blob-storage.png#lightbox)

## View Insight reports for the classifications and sensitivity labels

Find insights on your classified and labeled data in Data Map use the **Classification** and **Sensitivity labeling** reports.