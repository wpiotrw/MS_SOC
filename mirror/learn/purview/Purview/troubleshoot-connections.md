---
layout: Conceptual
title: Troubleshoot scans and connections in the Microsoft Purview Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/troubleshoot-connections
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article explains the steps to troubleshoot your scans and source connections in the Microsoft Purview Data Map.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: jingwang
ms.service: purview
ms.subservice: purview-data-map
ms.topic: how-to
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: ignite-fall-2021, msecd-doc-authoring-1030
locale: en-us
document_id: ef839de6-1cc3-7570-7592-ad9e4d32728e
document_version_independent_id: ef839de6-1cc3-7570-7592-ad9e4d32728e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/troubleshoot-connections.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: troubleshoot-connections
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/troubleshoot-connections.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: be016662-0317-b538-b7c6-ff9e12009315
---

# Troubleshoot scans and connections in the Microsoft Purview Data Map | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

This article describes how to troubleshoot connection errors while setting up scans on data sources in Microsoft Purview, or errors that could occur with your scans.

## Permission the credential on the data source

If you're using a managed identity or service principal as a method of authentication for scans, you'll have to allow these identities to have access to your data source.

There are specific instructions for each [source type](data-map-data-sources).

Important

Verify that you have followed all prerequisite and authentication steps for the source you are connecting to. You can find all available sources listed in the [Microsoft Purview supported sources article](data-map-data-sources).

## Verifying Azure Role-based Access Control to enumerate Azure resources in the Microsoft Purview governance portal

### Registering single Azure data source

To register a single data source in Microsoft Purview, such as an Azure Blob Storage or an Azure SQL Database, you must be granted at least **Reader** role on the resource or inherited from higher scope such as resource group or subscription. Some Azure RBAC roles, such as Security Admin, don't have read access to view Azure resources in control plane.

Verify this by following the steps below:

1. From the [Azure portal](https://portal.azure.com), navigate to the resource that you're trying to register in Microsoft Purview. If you can view the resource, it's likely, that you already have at least reader role on the resource.
2. Select **Access control (IAM)** &gt; **Role Assignments**.
3. Search by name or email address of the user who is trying to register data sources in Microsoft Purview.
4. Verify if any role assignments, such as Reader, exist in the list or add a new role assignment if needed.

### Scanning multiple Azure data sources

1. From the [Azure portal](https://portal.azure.com), navigate to the subscription or the resource group.
2. Select **Access Control (IAM)** from the left menu.
3. Select **+Add**.
4. In the **Select input** box, select the **Reader** role and enter your Microsoft Purview account name (which represents its MSI name).
5. Select **Save** to finish the role assignment.
6. Repeat the steps above to add the identity of the user who is trying to create a new scan for multiple data sources in Microsoft Purview.

## Scanning data sources using Private Link

If public endpoint is restricted on your data sources, to scan Azure data sources using Private Link, you need to set up a Self-hosted integration runtime and create a credential.

Important

Scanning multiple data sources which contain databases as Azure SQL database with *Deny public network access*, would fail. To scan these data sources using private Endpoint, instead use registering single data source option.

For more information about setting up a self-hosted integration runtime, see [the article about ingestion private endpoints and scanning sources.](data-gov-classic-private-link-end-to-end#deploy-self-hosted-integration-runtime-ir-and-scan-your-data-sources)

For more information how to create a new credential in Microsoft Purview, see [the article about credentials for source authentication in Microsoft Purview.](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account)

## Storing your credential in your key vault and using the right secret name and version

You must also store your credential in your Azure Key Vault instance and use the right secret name and version.

Verify this by following the steps below:

1. Navigate to your Key Vault.
2. Select **Settings** &gt; **Secrets**.
3. Select the secret you're using to authenticate against your data source for scans.
4. Select the version that you intend to use and verify that the password or account key is correct by selecting **Show Secret Value**.

## Verify permissions for the Microsoft Purview managed identity on your Azure Key Vault

Verify that the correct permissions have been configured for the Microsoft Purview managed identity to access your Azure Key Vault.

To verify this, do the following steps:

1. Navigate to your key vault and to the **Access policies** section
2. Verify that your Microsoft Purview managed identity shows under the *Current access policies* section with at least **Get** and **List** permissions on Secrets

    ![Image showing dropdown selection of both Get and List permission options](media/troubleshoot-connections/verify-minimum-permissions.png)

If you don't see your Microsoft Purview managed identity listed, then follow the steps in [Create and manage credentials for scans](data-map-data-scan-credentials) to add it.

## Scans no longer run

If your Microsoft Purview scan used to successfully run, but are now failing, check these things:

1. Have credentials to your resource changed or been rotated? If so, you'll need to update your scan to have the correct credentials.
2. Is an [Azure Policy](/en-us/azure/governance/policy/overview) preventing **updates to Storage accounts**? If so follow the [Microsoft Purview exception tag guide](data-gov-azure-policy-exclusion) to create an exception for Microsoft Purview accounts.
3. Are you using a self-hosted integration runtime? Check that it's up to date with the latest software and that it's connected to your network.

## Test connection passes but scan fails with connection error

Are you using private endpoints or virtual networks? Confirm your [network settings](data-gov-classic-security-best-practices#network-security), paying attention to your Network Security Group (NSG) rules.

## Receive JDK error when using a self-hosted integration runtime

Many sources that require a self-hosted integration runtime also require a certain version of Java to be installed on the machine where the self-hosted integration runtime is hosted. If you receive a JDK error, check the prerequisites on your specific [data source's page](data-map-data-sources) and install the recommended JDK version.