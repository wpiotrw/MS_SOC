---
layout: Conceptual
title: Quickstart - Share data | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/quickstart-data-share
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to securely share data from your environment using Microsoft Purview Data Sharing.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: sidnotha
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: quickstart
ms.custom: references_regions, devx-track-azurepowershell, msecd-doc-authoring-1030
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: c0df742e-104f-a11a-5b1f-4216347cc175
document_version_independent_id: c0df742e-104f-a11a-5b1f-4216347cc175
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/quickstart-data-share.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/quickstart-data-share
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/quickstart-data-share.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/7cf8f81d-2989-4e5d-aa91-5191d10a3323
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/1cb9c90f-9a3f-4389-8367-0a20c542621f
platformId: 24d6dbd8-9e89-f370-bef1-c94a137ed0ce
---

# Quickstart - Share data | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently being retired, with support provided until September 2025 to allow for migration to [Microsoft Fabric external data sharing](/en-us/fabric/governance/external-data-sharing-overview).

This article provides a quick guide on how to share data and receive shares from Azure Data Lake Storage (ADLS Gen2) or Blob storage accounts.

Important

Data sharing is accessed through the [classic Microsoft Purview governance portal](../use-microsoft-purview-governance-portal): https://web.purview.azure.com

## Prerequisites

### Microsoft Purview prerequisites

- [A Microsoft Purview account](../create-microsoft-purview-portal). You can also use two Microsoft Purview accounts, one for data provider and one for data consumer to test both scenarios.
- Your recipient's Azure sign-in email address that you can use to send the invitation to. The recipient's email alias won't work.

### Azure Storage account prerequisites

- Your Azure subscription must be registered for the **AllowDataSharing** preview feature. (If you haven't already registered this preview feature, consider using [Microsoft Fabric external data sharing](/en-us/fabric/governance/external-data-sharing-overview) instead, since Microsoft Purview Data Sharing will be retired in September 2025.) Or, [contact support](../concept-data-share#support).
- Source and target storage accounts **created after** the registration step is completed. **Both storage accounts must be in the same Azure region as each other**. Both storage accounts need to be ADLS Gen2 or Blob Storage accounts. Your storage accounts can be in a different Azure region from your Microsoft Purview account.
- Latest version of the storage SDK, PowerShell, CLI, and Azure Storage Explorer. Storage REST API version must be February 2020 or later.
- The storage accounts need to be registered in the collections where you'll send or receive the share. If you're using one Microsoft Purview account, this can be two different collections, or the same collection. For instructions to register, see the [ADLS Gen2](../register-scan-adls-gen2) or [Blob storage](../register-scan-azure-blob-storage-source) data source pages.
- If the source or target storage accounts are in a different Azure subscription than the one for Microsoft Purview account, the Microsoft. Purview resource provider is automatically registered in the Azure subscription where the data store is located at the time of share provider adding an asset or share consumer mapping an asset and **ONLY** if the user has permission to do the /register/action operation for the resource provider. The permission is included in the Contributor and Owner roles. 
    Note

    This registration is only needed the first time when sharing or receiving data into a storage account in the Azure subscription.

### Required roles

Here are required roles for sharing data and receiving shares.

| - | Azure Storage account roles | Microsoft Purview collection roles |
| --- | --- | --- |
| **Data provider** | One of the following roles: <br>- Owner<br>- Storage Blob Data Owner | Data Reader |
| **Data consumer** | One of the following roles: <br>- Contributor<br>- Owner<br>- Storage Blob Data Contributor<br>- Storage Blob Data Owner | Data Reader |

Note

If you created the Microsoft Purview account, you're automatically assigned all the roles to the root collection. Refer to [Microsoft Purview permissions](../data-gov-classic-permissions) to learn more about the Microsoft Purview collection and roles.

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

    Open the [Microsoft Purview portal](https://purview.microsoft.com/). Navigate to the **Data Catalog** application. Then select **Shares** from the left navigation. Select **+New Share**.
2. If you're using the [classing Microsoft Purview experience](../use-microsoft-purview-governance-portal) You can create a share by starting from the **Data Map**.

    Open the [Microsoft Purview governance portal](https://web.purview.azure.com/). Select the **Data Map** icon from the left navigation. Then select **Shares**. Select **+New Share**.

    ![Screenshot that shows the Microsoft Purview governance portal Data Map with Data Map, Shares and New Share highlighted.](../media/how-to-share-data/create-share-datamap-new-share.png)
3. From either location, select the Storage account type and the Storage account you want to share data from. Then select **Continue**.

    ![Screenshot that shows the New Share creation step with Type and Storage account options highlighted.](../media/how-to-share-data/create-share-datamap-select-type-account.png)
4. Follow the rest of the steps to create your data share.

### Create share

1. Specify a name and a description of share contents (optional). Then select **Continue**.

    [![Screenshot showing create share and enter details window, with the Continue button highlighted.](../media/how-to-share-data/create-share-details-inline.png)](../media/how-to-share-data/create-share-details-large.png#lightbox)
2. Search for and add all the assets you'd like to share out at the container, folder, or file level, and then select **Continue**.

    ![Screenshot showing the add assets window, with a file and a folder selected to share.](../media/how-to-share-data/add-asset.png)
3. You can edit the display names the shared data will have, if you like. Then select **Continue**.

    ![Screenshot showing the second add assets window with the display names unchanged.](../media/how-to-share-data/provide-display-names.png)
4. Select **Add Recipient** and select **User** or **App**.

    To share data to a user, select **User**, then enter the Azure sign-in email address of who you want to share data with. By default, the option to enter email address of user is shown.

    [![Screenshot showing the add recipients page, with the add recipient button highlighted, default user email option shown.](../media/how-to-share-data/create-share-add-user-recipient-inline.png)](../media/how-to-share-data/create-share-add-user-recipient-large.png#lightbox)

    To to share data with a service principal, select **App**. Enter the object ID and tenant ID of the recipient you want to share data with.

    [![Screenshot showing the add app recipients page, with the add app option and required fields highlighted.](../media/how-to-share-data/create-share-add-app-recipient-inline.png)](../media/how-to-share-data/create-share-add-app-recipient-large.png#lightbox)
5. Select **Create and Share**. Optionally, you can specify an **Expiration date** for when to terminate the share. You can share the same data with multiple recipients by selecting **Add Recipient** multiple times.

You've now created your share. The recipients of your share will receive an invitation and they can view the pending share in their Microsoft Purview account.

## Receive share

1. You can view your share invitations in any Microsoft Purview account. Open the Microsoft Purview governance portal by browsing directly to [the classic portal](https://web.purview.azure.com) or the [new Microsoft Purview portal](https://purview.microsoft.com) and selecting your Microsoft Purview account.
2. In the classic portal, select the **Data Map** icon from the left navigation. In the new portal, navigate to the **Data Catalog** application.
3. Select **Share invites**. If you received an email invitation, you can also select the **View share invite** link in the email to select a Microsoft Purview account.

    If you're a guest user of a tenant, you'll be asked to verify your email address for the tenant before viewing share invitation for the first time. [You can see our guide for steps.](../how-to-receive-share#guest-user-verification) Once verified, it's valid for 12 months.

    ![Screenshot showing the Share invites page in the Microsoft Purview governance portal.](../media/how-to-receive-share/view-invites.png)
4. Alternately, within the Microsoft Purview portal, find the Azure Storage or Azure Data Lake Storage (ADLS) Gen 2 data asset you would like to receive the share into using either the [data catalog search](../unified-catalog-data-assets-search) or [browse](../unified-catalog-data-assets-search#browse-the-unified-catalog). Select the **Data Share** button. You can see all the invitations in the **Share invites** tab.
5. Select name of the share to view or configure.
6. If you don't want to accept the invitation, select **Delete**.

    [![Screenshot showing the share attachment page with the delete button highlighted.](../media/how-to-receive-share/select-delete-invitation-inline.png)](../media/how-to-receive-share/select-delete-invitation-large.png#lightbox)

    Note

    If you delete an invitation, if you want to accept the share in future it will need to be resent. To deselect the share without deleting select the **Cancel** button instead.
7. You can edit the **Received share name** if you like. Then select a **Storage account name** for a target storage account in the same region as the source. You can choose to **Register a new storage account to attach the share** in the drop-down as well.

    Important

    The target storage account needs to be in the same Azure region as the source storage account.
8. Configure the **Path** (either a new container name, or the name of an existing share container) and, **New folder** (a new folder name for the share within in your container).
9. Select **Attach to target**.

    [![Screenshot showing share invitation configuration page, with a share name added, a collection selected, and the accept and configure button highlighted.](../media/how-to-receive-share/attach-shared-data-inline.png)](../media/how-to-receive-share/attach-shared-data-large.png#lightbox)
10. On the Manage data shares page, you'll see the new share with the status of **Attaching** until it has completed and is attached.

    ![Screenshot showing the attach share window, with the Attach button highlighted after you specify a target data store to receive or access shared data.](../media/how-to-receive-share/manage-data-shares-window-creating.png)
11. You can access shared data from the target storage account through Azure portal, Azure Storage Explorer, Azure Storage SDK, PowerShell or CLI. You can also analyze the shared data by connecting your storage account to Azure Synapse Analytics Spark or Databricks.

## Clean up resources

To clean up the resources created for the quick start, follow the steps below:

1. Within Microsoft Purview portal, [delete the sent share](../how-to-share-data#delete-share).
2. Also [delete your received share](../how-to-receive-share#delete-received-share).
3. Once the shares are successfully deleted, delete the target container and folder Microsoft Purview created in your target storage account when you received shared data.

## Troubleshoot

To troubleshoot issues with sharing data, refer to the [troubleshooting section of the how to share data article](../how-to-share-data#troubleshoot). To troubleshoot issues with receiving share, refer to the [troubleshooting section of the how to receive shared data article](../how-to-receive-share#troubleshoot).