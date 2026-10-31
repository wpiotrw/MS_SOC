---
layout: Conceptual
title: Lineage from SQL Server Integration Services into Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-lineage-sql-server-integration-services
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2025-05-01T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: This article describes the data lineage extraction from SQL Server Integration Services into Microsoft Purview.
locale: en-us
document_id: 758ba41a-194d-8fd1-fddd-cf419ad5724d
document_version_independent_id: 758ba41a-194d-8fd1-fddd-cf419ad5724d
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-lineage-sql-server-integration-services.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-lineage-sql-server-integration-services
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-lineage-sql-server-integration-services.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/863312f2-92a9-45bd-81bf-43238667a3ae
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a716028-8b9a-46e4-928f-203f70c0fcfe
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 8f1bffe3-706f-83b4-829d-3593f38100fc
---

# Lineage from SQL Server Integration Services into Microsoft Purview | Microsoft Learn

This article elaborates on the data lineage aspects of SQL Server Integration Services (SSIS) in Microsoft Purview.

## Prerequisites

- [Lift and shift SQL Server Integration Services workloads to the cloud](/en-us/sql/integration-services/lift-shift/ssis-azure-lift-shift-ssis-packages-overview)

## Supported scenarios

The current scope of support includes the lineage extraction from SSIS packages executed by Azure Data Factory SSIS integration runtime.

On premises SSIS lineage extraction is not supported yet.

Only source and destination are supported for Microsoft Purview SSIS lineage running from Data Factory’s SSIS Execute Package activity. Transformations under SSIS are not yet supported.

### Supported data stores

| Data store | Supported |
| --- | --- |
| Azure Blob Storage | Yes |
| Azure Data Lake Storage Gen1 | Yes |
| Azure Data Lake Storage Gen2 | Yes |
| Azure Files | Yes |
| Azure SQL Database \* | Yes |
| Azure SQL Managed Instance \* | Yes |
| Azure Synapse Analytics \* | Yes |
| SQL Server \* | Yes |

*\* Microsoft Purview currently doesn't support query or stored procedure for lineage or scanning. Lineage is limited to table and view sources only.*

## How to bring SSIS lineage into Microsoft Purview

### Step 1: [Connect a Data Factory to Microsoft Purview](data-map-lineage-azure-data-factory)

### Step 2: Trigger SSIS activity execution in Azure Data Factory

You can [run SSIS package with Execute SSIS Package activity](/en-us/azure/data-factory/how-to-invoke-ssis-package-ssis-activity) or [run SSIS package with Transact-SQL in ADF SSIS Integration Runtime](/en-us/azure/data-factory/how-to-invoke-ssis-package-stored-procedure-activity).

Once Execute SSIS Package activity finishes the execution, you can check lineage report status from the activity output in [Data Factory activity monitor](/en-us/azure/data-factory/monitor-visually#monitor-activity-runs). ![ssis-status](media/how-to-lineage-sql-server-integration-services/activity-report-lineage-status.png)

### Step 3: Browse lineage Information in your Microsoft Purview account

- You can browse Unified Catalog by choosing asset type “SQL Server Integration Services”.

[![Browser assets](media/how-to-lineage-sql-server-integration-services/browse-assets-1.png)](media/how-to-lineage-sql-server-integration-services/browse-assets-1.png#lightbox)![browser-assets-ssis](media/how-to-lineage-sql-server-integration-services/browse-assets-2.png)![browse-assets-ssis-package](media/how-to-lineage-sql-server-integration-services/browse-assets-3.png)

- You can also search Unified Catalog using keywords.

[![search-ssis](media/how-to-lineage-sql-server-integration-services/search-assets.png)](media/how-to-lineage-sql-server-integration-services/search-assets.png#lightbox)

- You can view lineage information for an SSIS Execute Package activity and open in Data Factory to view/edit the activity settings.

[![show-ssis-lineage](media/how-to-lineage-sql-server-integration-services/lineage.png)](media/how-to-lineage-sql-server-integration-services/lineage.png#lightbox)

- You can choose one data source to drill into how the columns in the source are mapped to the columns in the destination.

[![show-ssis-lineage-drill-in](media/how-to-lineage-sql-server-integration-services/lineage-drill-in.png)](media/how-to-lineage-sql-server-integration-services/lineage-drill-in.png#lightbox)