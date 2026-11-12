---
layout: Conceptual
title: Connect to and manage Azure Machine Learning in Microsoft Purview (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-azure-machine-learning
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: chigupta
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn how to connect to Azure Machine Learning in Microsoft Purview.
locale: en-us
document_id: 78f189bc-169f-0a7d-c6c6-3fe44b63f29f
document_version_independent_id: 78f189bc-169f-0a7d-c6c6-3fe44b63f29f
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-azure-machine-learning.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-azure-machine-learning
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-azure-machine-learning.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/d6f38669-3d05-40f2-afd8-e49f7dd20884
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/55265cca-de9b-48dc-a77a-9047cc39a575
platformId: af14a16b-a649-819f-c58b-fb24f333b269
---

# Connect to and manage Azure Machine Learning in Microsoft Purview (preview) | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

This article outlines how to register Azure Machine Learning and how to authenticate and interact with Azure Machine Learning in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

This integration between Azure Machine Learning and Microsoft Purview applies an auto push model that, once the Azure Machine Learning workspace has been registered in Microsoft Purview, the metadata from workspace is pushed to Microsoft Purview automatically on a daily basis. It isn't necessary to manually scan to bring metadata from the workspace into Microsoft Purview.

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | Yes | No |

When scanning the Azure Machine Learning source, Microsoft Purview supports:

- Extracting technical metadata from Azure Machine Learning, including:
    - Workspace
    - Models
    - Datasets
    - Jobs

Note

1. AML workspaces don't currently support pushing metadata through a private endpoint to Microsoft Purview.
2. You must register assets in your AML workspace for them to appear in Microsoft Purview.

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

## Prerequisites

- You must have an Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- You must have an active [Microsoft Purview account](create-microsoft-purview-portal).
- You need Data Source Administrator and Data Reader permissions to register a source and manage it in the Microsoft Purview governance portal. For more information about permissions, see [Access control in Microsoft Purview](data-gov-classic-permissions).
- An active Azure Machine Learning workspace
- A user needs the Contributor role in the Azure Machine Learning workspace to enable auto push from Azure Machine Learning workspace.

## Register

This section describes how to register an Azure Machine Learning workspace in Microsoft Purview by using [the Microsoft Purview governance portal](https://web.purview.azure.com/).

1. Go to your Microsoft Purview account.
2. Select **Data Map** on the left pane.
3. Select **Register**.
4. In **Register sources**, select **Azure Machine Learning (Preview)** &gt; **Continue**.

    ![Screenshot of the Azure Machine Learning source entry.](media/register-scan-azure-machine-learning/register-source.png)
5. On the **Register sources (Azure Machine Learning)** screen, do the following:

    1. For **Name**, enter a friendly name that Microsoft Purview lists as the data source for the workspace.
    2. For **Azure subscription** and **Workspace name**, select the subscription and workspace that you want to push from the dropdown. The Azure Machine Learning workspace URL is automatically populated.
    3. Select a collection from the list.
6. Select **Register** to register the source.

## Scan

After you register your Azure Machine Learning workspace, the metadata will be automatically pushed to Microsoft Purview on a daily basis.

## Browse and discover

To access the browse experience for data assets from your Azure Machine Learning workspace, select **Browse Assets**.

[![Screenshot of the browse assets selection.](media/register-scan-azure-machine-learning/browse-assets.png)](media/register-scan-azure-machine-learning/browse-assets.png#lightbox)

### Browse by collection

Browse by collection allows you to explore the different collections you're a data reader or curator for.

[![Screenshot of browsing by collection.](media/register-scan-azure-machine-learning/browse-by-collection.png)](media/register-scan-azure-machine-learning/browse-by-collection.png#lightbox)

### Browse by source type

1. On the browse by source types page, select **Azure Machine Learning**.

    [![Screenshot of the Azure Machine Learning source type.](media/register-scan-azure-machine-learning/browse-by-type.png)](media/register-scan-azure-machine-learning/browse-by-type.png#lightbox)
2. The top-level assets under your selected data type are listed. Pick one of the assets to further explore its contents. For example, after selecting Azure Machine Learning, you'll see a list of workspaces with assets in Unified Catalog.

    [![Screenshot of the top level assets.](media/register-scan-azure-machine-learning/top-level-assets.png)](media/register-scan-azure-machine-learning/top-level-assets.png#lightbox)
3. Selecting one of the workspaces displays the child assets.

    [![Screenshot of child assets.](media/register-scan-azure-machine-learning/child-assets.png)](media/register-scan-azure-machine-learning/child-assets.png#lightbox)
4. From the list, you can select on any of the asset items to view details. For example, selecting one of the Azure Machine Learning job assets displays the details of the job.

    [![Screenshot of asset details.](media/register-scan-azure-machine-learning/asset-details.png)](media/register-scan-azure-machine-learning/asset-details.png#lightbox)

## Lineage

To view lineage information, select an asset and then select the **Lineage** tab. From the lineage tab, you can see the asset's relationships when applicable. You can see what source data was used (if registered in Purview), the data asset created in Azure Machine Learning, any jobs, and finally the resulting machine learning model. In more advanced scenarios, you can see:

- If multiple data sources were used
- Multiple stages of training on multiple data assets
- If multiple models were created from the same data sources

[![Screenshot of the asset lineage.](media/register-scan-azure-machine-learning/asset-lineage.png)](media/register-scan-azure-machine-learning/asset-lineage.png#lightbox)

For more information on lineage in general, see [data lineage](data-gov-classic-lineage) and [lineage users guide](data-gov-classic-lineage-user-guide).