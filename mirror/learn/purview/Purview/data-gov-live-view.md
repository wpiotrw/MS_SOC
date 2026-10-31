---
layout: Conceptual
title: Live view (preview) for data governance in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-live-view
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2024-05-22T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn about live view (preview) in Microsoft Purview and how it can help users quickly access and govern their data estate.
locale: en-us
document_id: 865b585c-9abc-3ff0-a312-0ed1862d2432
document_version_independent_id: 865b585c-9abc-3ff0-a312-0ed1862d2432
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-live-view.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-live-view
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-live-view.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/ea957f26-244e-4bd1-9b19-105f0a0a73d6
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/85dd85bb-c2e5-412e-96b2-f2765a3fe51c
platformId: 59e45c43-e226-2eb4-3866-a460941698b0
---

# Live view (preview) for data governance in Microsoft Purview | Microsoft Learn

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

Some Azure resources are available to be seen in live view. Live view means that users with data access permissions can find these resources and their data assets in the catalog without setup or scanning. These resources and their metadata are immediately available when you access the [free or enterprise versions of Microsoft Purview](data-governance-free-version), so you can start your governance journey quickly.

[![Diagram showing live assets as a subset of data map assets.](media/live-view/assets-concept-diagram-inline.png)](media/live-view/assets-concept-diagram-inline.png#lightbox)

In this article we'll cover:

- What resources have live view available
- What metadata is available in live view
- Who has permissions to live view resources
- Next steps to govern live view resources

## Limitations

- Live view for Microsoft Fabric limitations:
    - Personal workspaces aren't supported yet in live view.
    - Only Microsoft Fabric item level metadata are available in live view.
    - Power BI Datasets don’t support showing schema in live view if the item hasn’t been scanned.
    - Dataflow Gen2 (Preview) items are displayed as Dataflow items.

## What resources have live view available?

Live view resources in the same tenant as your Microsoft Purview account are automatically accessible for users in your catalog. These resources have live view available:

| Resource | Level of view available |
| --- | --- |
| Azure Blob Storage | Storage account, Azure Blob Service, Container |
| Azure Data Lake Storage Gen 2 | Storage account, Azure Data Lake Storage Gen2 Service, File system |
| Azure SQL Database | Server, Database, Schema, Tables, Columns |
| Azure Subscriptions | Live view assets in the subscription |
| Microsoft Fabric | Workspace, [Item](register-scan-fabric-tenant#supported-capabilities) |

Users with permissions can browse and search for these assets in the catalog without needing to set up a scan.

## Metadata available in live view

Resources in live view in the catalog automatically have this metadata available:

- Name
- Properties
- Schema
- Lineage

Note

Live view resources won't automatically have classifications applied. To [automatically apply classifications](data-map-classification-apply-auto) to these resources, you need to [upgrade to the enterprise version of Microsoft Purview](data-governance-free-version-upgrade-to-enterprise), register and scan the resource.

[Data owners can also update the metadata on live view resources](data-gov-classic-metadata-curation) to add more information. Including manually adding description, contacts, etc.

## Live view permissions

Users that have permissions on the available resources are automatically able to access these resources in the catalog as either data readers or data owners. No other permissions in Microsoft Purview are required.

### Data readers

These are the permissions needed on the resources for a user to be able to see it as a reader in live view in Microsoft Purview.

| Data source | Reader permission |
| --- | --- |
| Azure SQL Database | [Reader role in Azure](/en-us/azure/role-based-access-control/built-in-roles#general) |
| Azure Blob Storage | [Reader role in Azure](/en-us/azure/role-based-access-control/built-in-roles#general) |
| Azure Data Lake Storage Gen2 | [Reader role in Azure](/en-us/azure/role-based-access-control/built-in-roles#general) |
| Azure Subscription | Read permission on subscription |

### Data owners

These are the permissions needed on the resources for a user to be able to see it as an owner and [curate its metadata](data-gov-classic-metadata-curation) in live view in Microsoft Purview.

| Data source | Owner permission |
| --- | --- |
| Azure SQL Database | "Microsoft.Sql/servers/write", "Microsoft.Sql/servers/databases/write", "Microsoft.Authorization/roleAssignments/write" |
| Azure Blob Storage | "Microsoft.Storage/storageAccounts/write", "Microsoft.Authorization/roleAssignments/write" |
| Azure Data Lake Storage Gen2 | "Microsoft.Storage/storageAccounts/write", "Microsoft.Authorization/roleAssignments/write" |

## Extend live view permissions

You can expand discoverability of these resources to users that don't have permissions already by enabling live view for all users. This can only be enabled with an [enterprise version of Microsoft Purview](data-governance-free-version-upgrade-to-enterprise). Extending live view also deepens the level of information available.

| Resource | Level of view available |
| --- | --- |
| Azure Blob Storage | Storage account, Azure Blob Service, Container, Folders, Files |
| Azure Data Lake Storage Gen 2 | Storage account, Azure Data Lake Storage Gen2 Service, File system, Folders, Files |
| Azure SQL Database | Server, Database, Schema, Tables, Columns, Views, Stored procedures |

Note

- For Azure Blob storage and Azure Data Lake Storage Gen 2, file schema is provided for parquet files.
- You can't extend live view permissions for Microsoft Fabric sources.

To enable these permissions, the user must be a [Data Source Administrator and Reader](data-gov-classic-permissions#roles) on the collection where they're going to host the resource.

To enable:

1. Browse the catalog for the source where you want to expand live view to users who don't already have data access permissions.
2. Select the data source.
3. Switch the **Live view** toggle under **Source management** to enable it.

    [![Screenshot of the live view toggle in the source management settings.](media/live-view/live-view-toggle-inline.png)](media/live-view/live-view-toggle-large.png#lightbox)
4. Add a credential for your resource. Select an existing credential or [add a new one](data-map-data-scan-credentials#create-a-new-credential). Your available options depend on which resources you're using. For more information about each credential, follow these links:

    - [Azure Blob Storage credential](register-scan-azure-blob-storage-source#authentication-for-a-scan)
    - [Azure Data Lake Gen 2 credential](register-scan-adls-gen2#authentication-for-a-scan)
    - [Azure SQL Database credential](register-scan-azure-sql-database#configure-authentication-for-a-scan)
5. Select **Test connection** to test your credential. You can only extend live view with a successful connection. [Follow this guide to troubleshoot connections.](troubleshoot-connections)
6. Choose a collection for your resource.

    Tip

    [Follow this link for more information about permissions in collections.](/en-us/purview/how-to-create-and-manage-collections#add-role-assignments)
7. Select **Apply** to register your source and extend your permissions.

    ![Screenshot of the enable live view menu, with a credential and collection selected, and save and run highlighted.](media/live-view/select-credential-and-collection.png)

## Preset scan

Note

Microsoft Fabric resources don't currently support a preset scan.

Assets with a live view allow data source administrators to perform preset scans. A live view asset has only some of it's metadata automatically available to users. A preset scan gathers the rest of that metadata and makes it available in Microsoft Purview.

A preset scan can only be run in the [enterprise version of Microsoft Purview](data-governance-free-version-upgrade-to-enterprise), and runs a scan with these default options:

- Full scan - all data assets are scanned and updated
- Default classifications - Microsoft Purview will check for default classifications for the source
- Scheduled - the scan is scheduled to run weekly by default, but the schedule can be updated.

Tip

To run a scan with any other options available to your source and organization, like custom classifications, perform [a regular scan](data-map-scan-data-sources).

To run a preset scan, a user must be a [Data Source Administrator](data-gov-classic-permissions#roles) on the collection where they're going to host the resource.

1. Browse the catalog for the source where you want to run a preset scan to enhance the metadata.
2. Select the data source.
3. Select the **Preset scan** toggle under **Source management** to scan.

    [![Screenshot of the source management pane, with the scan now button highlighted.](media/live-view/preset-scan-button-inline.png)](media/live-view/preset-scan-button-large.png#lightbox)
4. If live view permissions have already been extended, the scan starts. If live view hasn't been enabled, you need to submit a credential and select a collection to house the metadata:

    - [Azure Blob Storage credential](register-scan-azure-blob-storage-source#authentication-for-a-scan)
    - [Azure Data Lake Gen 2 credential](register-scan-adls-gen2#authentication-for-a-scan)
    - [Azure SQL Database credential](register-scan-azure-sql-database#configure-authentication-for-a-scan)
5. Select **Test connection** to test your credential. You can only scan with a successful connection. [Follow this guide to troubleshoot connections.](troubleshoot-connections)
6. Select **Apply** to run your scan.

    ![Screenshot of the scan menu, with a credential and collection selected, and the apply button highlighted.](media/live-view/preset-scan-enter-credentials.png)
7. To monitor the scan, select **Manage scans** in the **Source management** window.

    ![Screenshot of the source management pane, with the manage scans button highlighted. It's in the same location as the scan button was before.](media/live-view/manage-scans-inline.png)

### Update schedule

To update the schedule of a preset scan either:

- Select **Customize schedule** before selecting the toggle. You'll set your scan schedule and then the preset scan will be automatically enabled.

    ![Screenshot of the preset scan menu, with the customize schedule button highlighted.](media/live-view/customize-schedule-inline.png)
- Select the **Edit pencil** next to the schedule label after enabling the preset scan

    ![Screenshot of the preset scan menu, with the scan enabled and the pencil icon highlighted next to the schedule label.](media/live-view/edit-schedule-button-inline.png)

Then you can set your schedule to run monthly or weekly on specified days. Select **Apply** to apply the schedule to the scan.

![Screenshot of the scan schedule menu, showing a calendar and a dropdown to select times to run either monthly or weekly.](media/live-view/edit-scan-schedule-inline.png)

## Manage live view credentials

If you have extended live view permissions or run a preset scan your live view resource will have credentials that allow Microsoft Purview to access it.

If you need to update or remove those credentials, you can use the **Source management** window.

1. Browse the catalog for the source where you want to run a preset scan to enhance the metadata.
2. Select the data source.
3. Under source management, you can see your credential and collection listed, and the buttons to edit or delete the credentials.

    [![Screenshot of the source management window, showing the credentials with the edit and delete buttons highlighted.](media/live-view/edit-credentials-inline.png)](media/live-view/edit-credentials-large.png#lightbox)
4. Select the **Edit** pencil icon to update the credentials.

    Note

    You can't change the collection the source is mapped to.
5. Select **Delete** to remove the credentials.

    Note

    Deleting credentials will also disable extended live view permissions or preset scans.

## Enterprise governance of your data estate

In free version of governance solutions, users can only view live resources and manually update some metadata.

For access to all Microsoft Purview's applications, sources, automation, and to fully govern data assets in Microsoft Purview, [upgrade to the enterprise version of Microsoft Purview](data-governance-free-version-upgrade-to-enterprise).