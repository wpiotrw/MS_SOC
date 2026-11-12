---
layout: Conceptual
title: Set Up Data Quality for Fabric Shortcut Databases in Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-fabric-shortcut-databases
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: mannan
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Get step-by-step guidance on how to configure a data quality scan for a Microsoft Fabric shortcut data asset in Microsoft Purview Unified Catalog.
ms.custom: sfi-image-nochange, msecd-doc-authoring-1030
locale: en-us
document_id: f5f8f8e7-3e57-0358-09b9-5769b09d9d26
document_version_independent_id: f5f8f8e7-3e57-0358-09b9-5769b09d9d26
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-data-quality-fabric-shortcut-databases.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-data-quality-fabric-shortcut-databases
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-data-quality-fabric-shortcut-databases.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/e7cd09c2-9e9a-4f0d-b160-c15783f45b1f
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1d337399-0ca4-4b4c-acef-8df37820e018
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: d2e909f2-fc12-1235-04c0-1de696cc4132
---

# Set Up Data Quality for Fabric Shortcut Databases in Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Shortcuts are objects in Microsoft OneLake that point to other storage locations. The location can be internal or external to OneLake. The shortcut target path is the location the shortcut points to. The shortcut path is where the shortcut appears. Shortcuts appear as folders in OneLake, and any workload or service with access to OneLake can use them.

This article explains how to create Fabric shortcuts for external data sources and configure data quality scans for the shortcut-based assets in Microsoft Purview Unified Catalog.

With OneLake shortcuts, you can unify your data across domains, clouds, and accounts in a single virtual data lake. All Microsoft Fabric analytical engines connect directly to data sources like Azure, Amazon Web Services (AWS), and OneLake through a unified namespace. OneLake manages permissions and credentials, so you don't need to configure each Fabric workload separately.

For more information about Fabric shortcuts, see the [OneLake shortcuts documentation](/en-us/fabric/onelake/onelake-shortcuts).

## Prerequisites

Before you can run data quality scans on shortcut databases, create a shortcut for your external data source. After you create the shortcut, run a Data Map scan to register the asset in Unified Catalog, then run a data quality scan.

Important

- Use a service principal or managed identity for Data Map scans, and managed identity for data quality scans.
- Any data sourced through a shortcut is processed in the same region as the Fabric workspace.
- The Fabric team needs to differentiate shortcut items from native items in the Microsoft OneLake SDK for Lakehouse subartifacts. For now, all shortcut items (tables and files) are considered as native items during Data Map scanning.

Sign in to your [Microsoft Fabric workspace](/en-us/fabric/get-started/workspaces). Select the ellipsis button under **Tables**, and select **New Shortcut**. On the **New shortcut** page, you can create shortcuts for several external sources. This article covers the following:

- Azure Data Lake Gen2 shortcuts
- Amazon S3 shortcuts
- Google Cloud Storage shortcuts

[![Screenshot of the Fabric workspace, with the new shortcut button highlighted.](media/data-quality-self-help/shortcut-create-new.png)](media/data-quality-self-help/shortcut-create-new.png#lightbox)

## Set up an Azure Data Lake Gen2 shortcut

To create an Azure Data Lake Gen2 shortcut and scan it for data quality, complete the following steps:

1. Select **Azure Data Lake Storage Gen2** on the Fabric workspace **New shortcut** page.

    [![Screenshot of the Fabric  new shortcut page with ADLS Gen2 highlighted.](media/data-quality-self-help/shortcut-new-shortcut-page.png)](media/data-quality-self-help/shortcut-new-shortcut-page.png#lightbox)
2. Select ADLS Gen2 SAS authentication.

    [![Screenshot of  the new shortcut window with the SAS token authentication selected.](media/data-quality-self-help/shortcut-sas-token.png)](media/data-quality-self-help/shortcut-sas-token.png#lightbox)
3. In the Azure portal, [generate a shared access signature (SAS)](/en-us/azure/storage/common/storage-sas-overview) and connection string for your ADLS Gen2 resource.
4. **Copy** the endpoint of the data lake.

    ![Screenshot of copying the data lake end point in the Azure portal.](media/data-quality-self-help/shortcut-copy-end-point.png)
5. Add storage details for the shortcut storage.

    [![Screenshot to add storage details to the Fabric shortcut in the new shortcut window.](media/data-quality-self-help/shortcut-add-storage-detail.png)](media/data-quality-self-help/shortcut-add-storage-detail.png#lightbox)
6. Navigate to and choose the correct delta folder.

    [![Screenshot to choose correct delta folder in the new shortcut window.](media/data-quality-self-help/shortcut-choose-correct-delta-folder.png)](media/data-quality-self-help/shortcut-choose-correct-delta-folder.png#lightbox)
7. Preview the shortcut delta table in your Fabric workspace.

    [![Screenshot of the OneLake delta table preview.](media/data-quality-self-help/shortcut-preview-delta-table.png)](media/data-quality-self-help/shortcut-preview-delta-table.png#lightbox)
8. [Start a Data Map scan](data-map-scan-data-sources) of your Azure Data Lake Gen2 resource. Use service principal or managed identity authentication.

    ![Screenshot of the data map scan for ADLS Gen2.](media/data-quality-self-help/datamap-servicepriciple.png)
9. When the Data Map scan finishes, your asset appears in Unified Catalog as a Fabric Lakehouse table.
10. [Associate the asset with a data product](unified-catalog-data-products-create-manage#add-and-remove-data-assets) for curation and data quality assessment.
11. In Unified Catalog, [configure and run a data quality scan](unified-catalog-data-quality-scan) or [run data profiling](unified-catalog-data-quality-profiling) as usual.

## Set up an Amazon S3 shortcut

To create an Amazon S3 shortcut and scan it for data quality, you need the S3 bucket URL, access key ID, and secret access key. Complete the following steps:

1. Select **New shortcut** in the Microsoft Fabric workspace.
2. Select **Amazon S3** and add the URL, access key ID, and secret access key.

    [![Screenshot of the Amazon S3 new shortcut page with added details.](media/data-quality-self-help/shortcut-amazon-s3-access-key.png)](media/data-quality-self-help/shortcut-amazon-s3-access-key.png#lightbox)
3. Add the connection URL and storage details.

    [![Screenshot of the Amazon S3 new shortcut page with added connection URL and storage details.](media/data-quality-self-help/shortcut-amazon-s3-connection-url.png)](media/data-quality-self-help/shortcut-amazon-s3-connection-url.png#lightbox)
4. Preview the shortcut in your Fabric workspace.
5. [Start a Data Map scan](data-map-scan-data-sources) of your Amazon S3 resource. Use service principal or managed identity authentication.
6. When the Data Map scan finishes, your data asset appears in Unified Catalog.
7. [Associate the asset with a data product](unified-catalog-data-products-create-manage#add-and-remove-data-assets) for curation and data quality assessment.
8. In Unified Catalog, [configure and run a data quality scan](unified-catalog-data-quality-scan) or [run data profiling](unified-catalog-data-quality-profiling) as usual.

## Set up a Google Cloud Storage (GCS) shortcut

To create a Google Cloud Storage shortcut and scan it for data quality, you need the storage URL and HMAC access key credentials. Complete the following steps:

1. Select **New shortcut** in the Fabric workspace.
2. Select **Google Cloud Storage** and add the URL, access key ID, and access key shortcut.

    [![Screenshot of GCS shortcut HMAC key.](media/data-quality-self-help/shortcut-gcs-connection-settings.png)](media/data-quality-self-help/shortcut-gcs-connection-settings.png#lightbox)
3. Add the connection URL and storage details.

    [![Screenshot of GCS connection url.](media/data-quality-self-help/shortcut-gcs-connection-url.png)](media/data-quality-self-help/shortcut-gcs-connection-url.png#lightbox)
4. Preview the shortcut in your Fabric workspace.
5. [Start a Data Map scan](data-map-scan-data-sources) of your Google Cloud Storage resource. Use service principal or managed identity authentication.
6. When the Data Map scan finishes, your data asset appears in Unified Catalog.
7. [Associate the asset with a data product](unified-catalog-data-products-create-manage#add-and-remove-data-assets) for curation and data quality assessment.
8. In Unified Catalog, [configure and run a data quality scan](unified-catalog-data-quality-scan) or [run data profiling](unified-catalog-data-quality-profiling) as usual.