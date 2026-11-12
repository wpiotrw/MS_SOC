---
layout: Conceptual
title: Discover and govern multiple Azure sources in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/register-scan-azure-multiple-sources
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
description: Learn how to connect to multiple Azure sources in Microsoft Purview at once, and use Microsoft Purview features to scan and manage your sources.
locale: en-us
document_id: d02ebbf6-b33a-09ee-44f4-0308398a0359
document_version_independent_id: d02ebbf6-b33a-09ee-44f4-0308398a0359
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/register-scan-azure-multiple-sources.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: register-scan-azure-multiple-sources
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/register-scan-azure-multiple-sources.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 54ff96e8-24ca-4a69-7ae8-403ac3093a96
---

# Discover and govern multiple Azure sources in Microsoft Purview | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

This article outlines how to register multiple Azure sources and how to authenticate and interact with them in Microsoft Purview. For more information about Microsoft Purview, read the [introductory article](purview).

## Supported capabilities

#### Scanning capabilities

| Metadata Extraction | Full Scan | Incremental Scan | Scoped Scan |
| --- | --- | --- | --- |
| Yes | Yes | Yes | Yes |

#### Other capabilities

For **classifications**, **sensitivity labels**, **policies**, **data lineage**, and **live view**, see the [list of supported capabilities](data-map-data-sources#azure).

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- An active [Microsoft Purview account](create-microsoft-purview-portal).
- You'll need to be a Data Source Administrator and Data Reader to register a source and manage it in the Microsoft Purview governance portal. See our [Microsoft Purview Permissions page](data-gov-classic-permissions) for details.

## Register

This section describes how to register multiple Azure sources in Microsoft Purview using the [Microsoft Purview governance portal](https://web.purview.azure.com/).

### Prerequisites for registration

Microsoft Purview needs permissions to be able to list resources under a subscription or resource group.

1. Go to the subscription or the resource group in the Azure portal.
2. Select **Access Control (IAM)** from the left menu.
3. Select **+Add**.
4. In the **Select input** box, select the **Reader** role and enter your Microsoft Purview account name (which represents its MSI file name).
5. Select **Save** to finish the role assignment. This will allow Microsoft Purview to list resources under a subscription or resource group.

### Authentication for registration

There are two ways to set up authentication for multiple sources in Azure:

- Managed identity
- Service principal

You must set up authentication on each resource within your subscription or resource group that you want to register and scan. Azure Storage resource types (Azure Blob Storage and Azure Data Lake Storage Gen2) make it easy by allowing you to add the MSI file or service principal at the subscription or resource group level as a storage blob data reader. The permissions then trickle down to each storage account within that subscription or resource group. For all other resource types, you must apply the MSI file or service principal on each resource, or create a script to do so.

To learn how to add permissions on each resource type within a subscription or resource group, see the following resources:

- [Azure Blob Storage](register-scan-azure-blob-storage-source)
- [Azure Data Explorer](register-scan-azure-data-explorer)
- [Azure Data Lake Storage Gen1](register-scan-adls-gen1)
- [Azure Data Lake Storage Gen2](register-scan-adls-gen2)
- [Azure Dedicated SQL pool (formerly SQL DW)](register-scan-azure-synapse-analytics)
- [Azure SQL Database](register-scan-azure-sql-database)
- [Azure SQL Managed Instance](register-scan-azure-sql-managed-instance)
- [Azure Synapse Analytics](register-scan-synapse-workspace)

### Steps to register

1. Open the Microsoft Purview governance portal by:

    - Browsing directly to https://web.purview.azure.com and selecting your Microsoft Purview account.
    - Opening the [Azure portal](https://portal.azure.com), searching for and selecting the Microsoft Purview account. Selecting the [**the Microsoft Purview governance portal**](https://web.purview.azure.com/) button.
2. Select **Data Map** on the left menu.
3. Select **Register**.
4. On **Register sources**, select **Azure (multiple)**.

    ![Screenshot that shows the tile for Azure Multiple on the screen for registering multiple sources.](media/register-scan-azure-multiple-sources/register-azure-multiple.png)
5. Select **Continue**.
6. On the **Register sources (Azure)** screen, do the following:

    1. In the **Name** box, enter a name that the data source will be listed with in the catalog.
    2. In the **Management group** box, optionally choose a management group to filter down to.
    3. In the **Subscription** and **Resource group** dropdown list boxes, select a subscription or a specific resource group, respectively. The registration scope will be set to the selected subscription or resource group.

        ![Screenshot that shows the boxes for selecting a subscription and resource group.](media/register-scan-azure-multiple-sources/azure-multiple-source-setup.png)
    4. Select a collection from the list.
    5. Select **Register** to register the data sources.

## Scan

Important

Currently, scanning multiple Azure sources is only supported using Azure integration runtime, therefore, only Microsoft Purview accounts that allow public access on the firewall can use this option.

Follow the steps below to scan multiple Azure sources to automatically identify assets and classify your data. For more information about scanning in general, see our [introduction to scans and ingestion](data-map-scan-ingestion).

### Create and run scan

To create and run a new scan, do the following:

1. Select the **Data Map** tab on the left pane in the Microsoft Purview governance portal.
2. Select the data source that you registered.
3. Select **View details** &gt; **+ New scan**, or use the **Scan** quick-action icon on the source tile.
4. For **Name**, fill in the name.
5. For **Type**, select the types of resources that you want to scan within this source. Choose one of these options:

    - Leave it as **All**. This selection includes future resource types that might not currently exist within that subscription or resource group.
    - Use the boxes to specifically select resource types that you want to scan. If you choose this option, future resource types that might be created within this subscription or resource group won't be included for scans, unless the scan is explicitly edited in the future.

    ![Screenshot that shows options for scanning multiple sources.](media/register-scan-azure-multiple-sources/multiple-source-scan.png)
6. Select the credential to connect to the resources within your data source:

    - You can select a credential at the parent level as an MSI file, or you can select a credential for a particular service principal type. You can then use that credential for all the resource types under the subscription or resource group.
    - You can specifically select the resource type and apply a different credential for that resource type.

    Each credential will be considered as the method of authentication for all the resources under a particular type. You must set the chosen credential on the resources in order to successfully scan them, as described earlier in this article.
7. Within each type, you can select to either scan all the resources or scan a subset of them by name:

    - If you leave the option as **All**, then future resources of that type will also be scanned in future scan runs.
    - If you select specific storage accounts or SQL databases, then future resources of that type created within this subscription or resource group won't be included for scans, unless the scan is explicitly edited in the future.
8. Select **Test connection**. This will first test access to check if you've applied the Microsoft Purview MSI file as a reader on the subscription or resource group. If you get an error message, follow these instructions to resolve it. Then it will test your authentication and connection to each of your selected sources and generate a report. The number of sources selected will impact the time it takes to generate this report. If failed on some resources, hovering over the **X** icon will display the detailed error message.

    ![Screenshot showing the scan setup slider, with the Test Connection button highlighted.](media/register-scan-azure-multiple-sources/test-connection.png)![Screenshot showing an example test connection report, with some connections passing and some failing. Hovering over one of the failed connections shows a detailed error report.](media/register-scan-azure-multiple-sources/test-connection-report.png)
9. After your test connection has passed, select **Continue** to proceed.
10. Select scan rule sets for each resource type that you chose in the previous step. You can also create scan rule sets inline.

    ![Screenshot that shows scan rules for each resource type.](media/register-scan-azure-multiple-sources/multiple-scan-rule-set.png)
11. Choose your scan trigger. You can set up a schedule or run the scan once.
12. Review your scan and select **Save** to complete setup.

## View your scans and scan runs

1. View source details by selecting **View details** on the tile under the **Data Map** section.

    ![Screenshot that shows source details.](media/register-scan-azure-multiple-sources/multiple-source-detail.png)
2. View scan run details by going to the **Scan details** page.

    The *status bar* is a brief summary of the running status of the child resources. It's displayed on the subscription level or resource group level. The colors have the following meanings:

    - Green: The scan was successful.
    - Red: The scan failed.
    - Gray: The scan is still in progress.

    You can select each scan to view finer details.

    ![Screenshot that shows scan details.](media/register-scan-azure-multiple-sources/multiple-scan-full-details.png)
3. View a summary of recent failed scan runs at the bottom of the source details. You can also view more granular details about these runs.

## Manage your scans: edit, delete, or cancel

To manage a scan, do the following:

1. Go to the management center.
2. Select **Data sources** under the **Sources and scanning** section, and then select the desired data source.
3. Select the scan that you want to manage. Then:

    - You can edit the scan by selecting **Edit**.
    - You can delete the scan by selecting **Delete**.
    - If the scan is running, you can cancel it by selecting **Cancel**.

## Policies

The following types of policies are supported on this data resource from Microsoft Purview:

- [DevOps policies](concept-policies-devops)
- [Data owner policies](concept-policies-data-owner)

### Access policy pre-requisites on Azure Storage accounts

To be able to enforce policies from Microsoft Purview, data sources under a resource group or subscription need to be configured first. Instructions vary based on the data source type. Please review whether they support Microsoft Purview policies, and if so, the specific instructions to enable them, under the Access Policy link in the [Microsoft Purview connector document](data-map-data-sources).

### Configure the Microsoft Purview account for policies

#### Register the data source in Microsoft Purview

Before a policy can be created in Microsoft Purview for a data resource, you must register that data resource in Microsoft Purview Studio. You will find the instructions related to registering the data resource later in this guide.

Note

Microsoft Purview policies rely on the data resource ARM path. If a data resource is moved to a new resource group or subscription it will need to be de-registered and then registered again in Microsoft Purview.

#### Configure permissions to enable Data policy enforcement on the data source

Once a resource is registered, but before a policy can be created in Microsoft Purview for that resource, you must configure permissions. A set of permissions are needed to enable the **Data policy enforcement**. This applies to data sources, resource groups, or subscriptions. To enable *Data policy enforcement*, you must have *both* specific Identity and Access Management (IAM) privileges on the resource as well as specific Microsoft Purview privileges:

- You must have *either one* of the following IAM role combinations on the resource's Azure Resource Manager path or any parent of it (that is, using IAM permission inheritance):

    - IAM Owner
    - Both IAM Contributor and IAM User Access Administrator

    To configure Azure role-based access control (RBAC) permissions, follow [this guide](/en-us/azure/role-based-access-control/check-access). The following screenshot shows how to access the **Access Control** section in the Azure portal for the data resource to add a role assignment.

    [![Screenshot that shows the section in the Azure portal for adding a role assignment.](media/how-to-policies-data-owner-authoring-generic/assign-iam-permissions.png)](media/how-to-policies-data-owner-authoring-generic/assign-iam-permissions.png#lightbox)

    Note

    The *IAM Owner* role for a data resource can be inherited from a parent resource group, a subscription, or a subscription management group. Check which Microsoft Entra users, groups, and service principals hold or are inheriting the *IAM Owner* role for the resource.
- You also need to have the Microsoft Purview *Data source admin* role for the collection or a parent collection (if inheritance is enabled). For more information, see the [guide on managing Microsoft Purview role assignments](data-gov-classic-permissions#assign-permissions-to-your-users).

    The following screenshot shows how to assign the *Data source admin* role at the root collection level.

    [![Screenshot that shows selections for assigning the Data source admin role at the root collection level.](media/how-to-policies-data-owner-authoring-generic/assign-purview-permissions.png)](media/how-to-policies-data-owner-authoring-generic/assign-purview-permissions.png#lightbox)

#### Configure Microsoft Purview permissions to create, update, or delete access policies

To create, update or delete policies, you need to get the *Policy author* role in Microsoft Purview at *root collection level*:

- The *Policy author* role can create, update, and delete DevOps and Data Owner policies.
- The *Policy author* role can delete self-service access policies.

For more information about managing Microsoft Purview role assignments, see [Create and manage collections in the Microsoft Purview Data Map](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).

Note

Policy author role must be configured at the root collection level.

In addition, to easily search Microsoft Entra users or groups when creating or updating the subject of a policy, you can greatly benefit from getting the [Directory Readers](/en-us/azure/active-directory/roles/permissions-reference#directory-readers) permission in Microsoft Entra ID. This is a common permission for users in an Azure tenant. Without the Directory Reader permission, the Policy Author will have to type the complete username or email for all the principals included in the subject of a data policy.

#### Configure Microsoft Purview permissions for publishing Data Owner policies

Data Owner policies allow for checks and balances if you assign the Microsoft Purview *Policy author* and *Data source admin* roles to different people in the organization. Before a Data owner policy takes effect, a second person (*Data source admin*) must review it and explicitly approve it by publishing it. This does not apply to DevOps or Self-service access policies as publishing is automatic for them when those policies are created or updated.

To publish a Data owner policy you need to get the *Data source admin* role in Microsoft Purview at *root collection level*.

For more information about managing Microsoft Purview role assignments, see [Create and manage collections in the Microsoft Purview Data Map](data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).

Note

To publish Data owner policies, the Data source admin role must be configured at the root collection level.

#### Delegate access provisioning responsibility to roles in Microsoft Purview

After a resource has been enabled for **Data policy enforcement**, any Microsoft Purview user with the *Policy author* role at the root collection level can provision access to that data source from Microsoft Purview.

Note

Any Microsoft Purview root *Collection admin* can assign new users to root *Policy author* roles. Any *Collection admin* can assign new users to a *Data source admin* role under the collection. Minimize and carefully vet the users who hold Microsoft Purview *Collection admin*, *Data source admin*, or *Policy author* roles.

If a Microsoft Purview account with published policies is deleted, such policies will stop being enforced within an amount of time that depends on the specific data source. This change can have implications on both security and data access availability. The Contributor and Owner roles in IAM can delete Microsoft Purview accounts. You can check these permissions by going to the **Access control (IAM)** section for your Microsoft Purview account and selecting **Role Assignments**. You can also use a lock to prevent the Microsoft Purview account from being deleted through [Resource Manager locks](/en-us/azure/azure-resource-manager/management/lock-resources).

### Register the data source in Microsoft Purview for Data Policy Enforcement

The Azure subscription or resource group needs to be registered first with Microsoft Purview before you can create access policies. To register your resource, follow the **Prerequisites** and **Register** sections of this guide:

- [Register multiple sources in Microsoft Purview](register-scan-azure-multiple-sources#prerequisites)

After you've registered the data resource, you'll need to enable Data Policy Enforcement. This is a pre-requisite before you can create policies on the data resource. Data Policy Enforcement can impact the security of your data, as it delegates to certain Microsoft Purview roles managing access to the data sources. **Go through the secure practices related to Data Policy Enforcement in this guide**: [How to enable Data Policy Enforcement](how-to-enable-data-policy-enforcement)

Once your data source has the **Data Policy Enforcement** option set to **Enabled**, it will look like this screenshot: ![Screenshot shows how to register a data source for policy with the option Data policy enforcement set to enable.](media/how-to-policies-data-owner-resource-group/enable-policy-enforcement-resource-group.png)

### Create a policy

To create an access policy on an entire Azure subscription or resource group, follow these guides:

- [DevOps policy covering all sources in a subscription or resource group](how-to-policies-devops-resource-group#create-a-new-devops-policy)
- [Provision read/modify access to all sources in a subscription or resource group](how-to-policies-data-owner-resource-group#create-and-publish-a-data-owner-policy)