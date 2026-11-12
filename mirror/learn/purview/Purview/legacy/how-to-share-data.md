---
layout: Conceptual
title: How to share data | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-share-data
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to share data with Microsoft Purview Data Sharing.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: how-to
ms.custom:
- references_regions
- devx-track-azurepowershell
- sfi-image-nochange
- msecd-doc-authoring-1030
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: a36f53d2-34f9-ded1-0ae6-ddbb2d5ecf05
document_version_independent_id: a36f53d2-34f9-ded1-0ae6-ddbb2d5ecf05
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-share-data.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-share-data
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-share-data.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/7cf8f81d-2989-4e5d-aa91-5191d10a3323
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/1cb9c90f-9a3f-4389-8367-0a20c542621f
platformId: d374f716-5225-0a3c-f071-ab6872abaac2
---

# How to share data | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently being retired, with support provided until September 2025 to allow for migration to [Microsoft Fabric external data sharing](/en-us/fabric/governance/external-data-sharing-overview).

Microsoft Purview Data Sharing supports in-place data sharing from Azure Data Lake Storage (ADLS Gen2) to ADLS Gen2, and Blob storage account to Blob storage account. This article explains how to share data using Microsoft Purview.

## Prerequisites to share data

### Microsoft Purview prerequisites

- [A Microsoft Purview account](../create-microsoft-purview-portal).
- A minimum of Data Reader role is needed on a Microsoft Purview collection to use data sharing in the governance portal. Refer to [Microsoft Purview permissions](../data-gov-classic-permissions) to learn more about the Microsoft Purview collection and roles.
- To use the SDK, no Microsoft Purview permissions are needed.
- Your data recipient's Azure sign-in email address, or the object ID and tenant ID of the recipient application, that you'll use to send the invitation to receive a share. The recipient's email alias won't work.

### Azure Storage account prerequisites

- Your Azure subscription must be registered for the **AllowDataSharing** preview feature. (If you haven't already registered this preview feature, consider using [Microsoft Fabric external data sharing](/en-us/fabric/governance/external-data-sharing-overview) instead, since Microsoft Purview Data Sharing will be retired in September 2025.) Or, [contact support](../concept-data-share#support).
- A source storage account **created after the registration step is completed**. Source storage account can be in a different Azure region from your Microsoft Purview account, but needs to follow the available configurations.
- You need the **Owner** or **Storage Blob Data Owner** role on the source storage account to be able to share data. You can find more details on the [ADLS Gen2](../register-scan-adls-gen2#data-sharing) or [Blob storage](../register-scan-azure-blob-storage-source#data-sharing) data source page.
- If the source storage account is in a different Azure subscription than the one for Microsoft Purview account, the Microsoft. Purview resource provider needs to be registered in the Azure subscription where the Storage account is located. It's automatically registered at the time of share provider adding an asset if the user has permission to do the `/register/action` operation and therefore, Contributor or Owner roles to the subscription where the Storage account is located. This registration is only needed the first time when sharing or receiving data into a storage account in the Azure subscription.
- A storage account needs to be registered in the collection to create a share using the Microsoft Purview portal experience. For instructions to register, see the [ADLS Gen2](../register-scan-adls-gen2) or [Blob storage](../register-scan-azure-blob-storage-source) data source pages. This step isn't required to use the SDK.

## Create a share

There are two ways you can create a data share:

- Directly from the data asset
- Use the data sharing application

### Create share from asset

1. You can create a share by starting from **Data Catalog**

    Within the [classic Microsoft Purview governance portal](https://web.purview.azure.com/) or the new [Microsoft Purview portal](https://purview.microsoft.com/), find the Azure Storage or Azure Data Lake Storage (ADLS) Gen 2 data asset you would like to share data from using either the [data catalog search](../unified-catalog-data-assets-search) or [browse](../unified-catalog-data-assets-search#browse-the-unified-catalog).

    ![Screenshot that shows the Microsoft Purview governance portal homepage with the search and browse options highlighted.](../media/how-to-share-data/search-or-browse.png)
2. Once you have found your data asset, select the **Data Share** button.

    [![Screenshot of a data asset in the Microsoft Purview governance portal with the Data Share button highlighted.](../media/how-to-share-data/select-data-share-inline.png)](../media/how-to-share-data/select-data-share-large.png#lightbox)
3. Select **+New Share**.

    [![Screenshot of the Data Share management window with the New Share button highlighted.](../media/how-to-share-data/select-new-share-inline.png)](../media/how-to-share-data/select-new-share-large.png#lightbox)
4. Follow the rest of the steps to create your data share.

### Create share from application

1. If you're using the [new Microsoft Purview experience](../purview-portal) You can create a share by starting from the **Data Catalog**.

    Open the [Microsoft Purview portal](https://purview.microsoft.com/). Navigate to the **Data Catalog** application. Then select **Shares**. Select **+New Share**.
2. If you're using the [classic Microsoft Purview experience](../use-microsoft-purview-governance-portal) You can create a share by starting from the **Data Map**.

    Open the [Microsoft Purview governance portal](https://web.purview.azure.com/). Select the **Data Map** icon from the left navigation. Then select **Shares**. Select **+New Share**.

    ![Screenshot that shows the Microsoft Purview governance portal Data Map with Data Map, Shares, and New Share highlighted.](../media/how-to-share-data/create-share-datamap-new-share.png)
3. From either location, select the Storage account type and the Storage account you want to share data from. Then select **Continue**.

    ![Screenshot that shows the New Share creation step with Type and Storage account options highlighted.](../media/how-to-share-data/create-share-datamap-select-type-account.png)
4. Follow the rest of the steps to create your data share.

### Create share

1. Specify a name and a description of share contents (optional). Then select **Continue**.

    [![Screenshot showing create share and enter details window, with the Continue button highlighted.](../media/how-to-share-data/create-share-details-inline.png)](../media/how-to-share-data/create-share-details-large.png#lightbox)
2. Search for and add all the assets you'd like to share out at the container, folder, and file level, and then select **Continue**.

    Important

    Only containers, files, and folders that belong to the current Blob or ADLSGen2 Storage account can be added to the share.

    ![Screenshot showing the add assets window, with a file and a folder selected to share.](../media/how-to-share-data/add-asset.png)
3. You can edit the display names the shared data will have, if you like. Then select **Continue**.

    ![Screenshot showing the second add assets window with the display names unchanged.](../media/how-to-share-data/provide-display-names.png)
4. Select **Add Recipient** and select **User** or **App**.

    To share data to a user, select **User**, then enter the Azure sign-in email address of who you want to share data with. By default, the option to enter email address of user is shown.

    [![Screenshot showing the add recipients page, with the add recipient button highlighted, default user email option shown.](../media/how-to-share-data/create-share-add-user-recipient-inline.png)](../media/how-to-share-data/create-share-add-user-recipient-large.png#lightbox)

    To to share data with a service principal, select **App**. Enter the object ID and tenant ID of the recipient you want to share data with.

    [![Screenshot showing the add app recipients page, with the add app option and required fields highlighted.](../media/how-to-share-data/create-share-add-app-recipient-inline.png)](../media/how-to-share-data/create-share-add-app-recipient-large.png#lightbox)
5. Select **Create and Share**. Optionally, you can specify an **Expiration date** for when to terminate the share. You can share the same data with multiple recipients by selecting **Add Recipient** multiple times.

You've now created your share. The recipients of your share will receive an invitation and they can view the share invitation in their Microsoft Purview account.

When a share is created, a new asset of type sent share is ingested into the Microsoft Purview catalog, in the same collection as the storage account from which you created the share. You can search for it like any other asset in the data catalog.

You can also track lineage for data shared using Microsoft Purview. See, [Microsoft Purview Data Sharing lineage](../how-to-lineage-purview-data-sharing) to learn more about share assets and data sharing lineage.

Note

Shares created using the SDK without registering the storage account with Microsoft Purview will not be ingested into the catalog. User can register their storage account if desired. If a storage account is un-registered or re-registered to a different collection, share assets of that storage account continue to be in the initial collection.

## Update a sent share

Once a share is created, you can update description, assets, and recipients.

Note

If you only have the **Reader** role on the source storage account, you will be able to view list of sent shares and received shares but not edit. You can find more details on the [ADLS Gen2](../register-scan-adls-gen2#data-sharing) or [Blob storage](../register-scan-azure-blob-storage-source#data-sharing) data source page.

You can find your sent shares one of two ways:

- Access the blob storage or ADLS Gen2 asset where the data was shared from in the data catalog. Open it, then select **Data Share**. There you're able to see all the shares for that asset. Select a share, and then select the **Edit** option.

    [![Screenshot of a data asset in the Microsoft Purview governance portal with the data share button highlighted.](../media/how-to-share-data/select-data-share-inline.png)](../media/how-to-share-data/select-data-share-large.png#lightbox)

    ![Screenshot of the Manage data shares page with a share selected and the edit button highlighted.](../media/how-to-share-data/select-share-to-edit.png)
- For shares that you sent, in the [classic Microsoft Purview governance portal](https://web.purview.azure.com/) you can find them in the **Shares** menu in the Microsoft Purview Data Map. In the new [Microsoft Purview portal](https://purview.microsoft.com/) you can find them in the **Data Catalog** application in the **Shares** menu. There you're able to see all the shares you have sent. Select a share, and then select the **Edit** option.

    [![Screenshot of the Data Shares menu in the Microsoft Purview Data Map.](../media/how-to-share-data/select-shares-in-data-map-inline.png)](../media/how-to-share-data/select-shares-in-data-map.png#lightbox)

From any of these places you can:

- Edit share details
- Edit shared assets
- Edit share recipients
- Delete your share

### Edit details

On the **Details** tab of the edit share page, you can update the share name and description. Save any changes by selecting **Save**.

[![Screenshot of the Details tab of the edit page, with the save button highlighted.](../media/how-to-share-data/edit-details-inline.png)](../media/how-to-share-data/edit-details-large.png#lightbox)

### Edit assets

On the **Asset** tab of the edit share page you can see all the shared files and folders.

You can **remove** any containers, files, or folders from the share by selecting the delete button in the asset's row however you can't remove all the assets of a sent share.

![Screenshot of the Asset tab of the edit page, with the delete button highlighted next to an asset.](../media/how-to-share-data/remove-asset.png)

You can **add new assets** by selecting the **Edit** button and then searching for and selecting any other containers, files, and folders in the asset that you would like to add.

![Screenshot of the Asset tab of the edit page, with the edit button highlighted.](../media/how-to-share-data/edit-assets.png)

Once you've selected your assets, select **Add**, and you'll see your new asset in the Asset tab.

Save all your changes by selecting the **Save** button.

### Edit recipients

On the **Recipients** tab of the edit share page you can see all the users and groups that are receiving your shares, their status, and the expiration date for their share.

Here are what each of the recipient statuses mean:

| Status | Meaning |
| --- | --- |
| Attached | The share has been accepted and the recipient has access to the shared data. |
| Detached | The recipient hasn't accepted the invitation or is no longer active. They aren't receiving the share. |

You can **remove or delete recipients** by either selecting the delete button on the recipient's row, or selecting multiple recipients and then selecting the **Delete recipients** button at the top of the page.

![Screenshot of the Recipients tab of the edit page, with a recipient selected, and both delete options highlighted.](../media/how-to-share-data/delete-recipients.png)

You can **add recipients** by selecting the **Add recipients** button.

![Screenshot of the Recipients tab of the edit page showing the Add recipients button highlighted.](../media/how-to-share-data/add-recipients.png)

Select **Add Recipient** again and select **User** or **App**.

To share data to a user, select **User**, then enter the Azure sign-in email address of who you want to share data with. By default, the option to enter email address of user is shown.

[![Screenshot showing the edit recipients page  with the add recipient button highlighted, default user email option shown.](../media/how-to-share-data/create-share-add-user-recipient-inline.png)](../media/how-to-share-data/create-share-add-user-recipient-large.png#lightbox)

To to share data with a service principal, select **App**. Enter the object ID and tenant ID of the recipient you want to share data with.

[![Screenshot showing the edit app recipients page, with the add app option and required fields highlighted.](../media/how-to-share-data/create-share-add-app-recipient-inline.png)](../media/how-to-share-data/create-share-add-app-recipient-large.png#lightbox)

Optionally, you can specify an **Expiration date** for when to terminate the share. You can share the same data with multiple recipients by clicking on **Add Recipient** multiple times.

When you're finished, select the **Add recipients** confirmation button at the bottom of the page.

Save all your changes by selecting the **Save** button.

### Delete share

To delete your share, on any tab in the edit share page, select the **Delete share** button.

![Screenshot showing the edit share page, with the delete share button highlighted.](../media/how-to-share-data/delete-share.png)

Confirm that you would like to delete in the pop-up window and the share will be removed.

## Troubleshoot

Here are some common issues for sharing data and how to troubleshoot.

### Can't create Microsoft Purview account

If you're getting an error related to *quota* when creating a Microsoft Purview account, it means your organization has exceeded [Microsoft Purview service limit](../classic-how-to-manage-quotas). If you require an increase in limit, contact support.

### Can't find my Storage account asset in the Catalog

There are a couple possible reasons:

- The data source isn't registered in Microsoft Purview. Refer to the registration steps for [Blob Storage](../register-scan-azure-blob-storage-source) and [ADLSGen2](../register-scan-adls-gen2) respectively. Performing a scan isn't necessary.
- Data source is registered to a Microsoft Purview collection that you don't have a minimum of Data Reader permission to. Refer to [Microsoft Purview catalog permissions](../data-gov-classic-permissions) and reach out to your collection admin for access.

### Can't create shares or edit shares

- You don't have permission to the data store where you want to share data from. Check the prerequisites for required data store permissions.

### Can't view list of shares in the storage account asset

- You don't have enough permissions the data store that you want to see shares of. You need a minimum of **Reader** role on the source storage account to see a read-only view of sent shares and received shares. You can find more details on the [ADLS Gen2](../register-scan-adls-gen2#data-sharing) or [Blob storage](../register-scan-azure-blob-storage-source#data-sharing) data source page.
- Review storage account prerequisites and make sure your storage account region, performance, and redundancy options are all supported.