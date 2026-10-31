---
layout: Conceptual
title: Service principal authentication for Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-service-principal
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
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: This article describes how you can create a service principal in Azure for use with Microsoft Purview.
ms.custom: sfi-image-nochange
locale: en-us
document_id: d6e5edcd-dbad-b070-32b9-620770554372
document_version_independent_id: d6e5edcd-dbad-b070-32b9-620770554372
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-service-principal.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-service-principal
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-service-principal.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/f488294d-f483-456e-94e3-755f933b811b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/02662057-0b9b-40f4-a3c7-537125b6d283
platformId: cd4a6ce7-a48c-c63e-c773-c48d91887bbd
---

# Service principal authentication for Microsoft Purview | Microsoft Learn

You can create a new or use an existing service principal in your Microsoft Entra tenant to authenticate Microsoft Purview with other services. This article explains how to prepare a service principal for Purview to use to authenticate with other services.

## App registration

1. Follow the steps in this linked article section to create a service principal: [Register an application with Microsoft Entra ID and create a service principal](/en-us/entra/identity-platform/howto-create-service-principal-portal#register-an-application-with-microsoft-entra-id-and-create-a-service-principal).

    Tip

    For the Redirect URL, if you have an authentication endpoint for your organization you want to use, add it. Otherwise, `https://contoso.com/auth` works.
2. Once you register the app, copy the **Application (client) ID** value. Use this value later to create a credential in Microsoft Purview.

    ![Screenshot that shows the newly created application.](media/create-service-principal-azure/create-service-principal-azure-new-app.png)

## Add a secret to the client credentials

1. Follow the steps in this linked article section to create a new client secret: [Create a new client secret](/en-us/entra/identity-platform/howto-create-service-principal-portal#option-3-create-a-new-client-secret).
2. Copy the **Secret value**. Use this value later to create a secret in Azure Key Vault (KV).

    ![Screenshot that shows the client secret.](media/create-service-principal-azure/create-service-principal-azure-client-secret.png)

## Add the secret to your Azure Key Vault

To allow Microsoft Purview to use this service principal to authenticate with other services, store this credential in Azure Key Vault.

- If you need an Azure Key vault, you can [follow these steps to create one.](/en-us/azure/key-vault/general/quick-create-portal)
- To grant your Microsoft Purview account access to the Azure Key Vault, you can [follow these steps](data-map-data-scan-credentials#microsoft-purview-permissions-on-the-azure-key-vault).

1. Go to your **Key Vault**.

    ![Screenshot that shows the Key vault.](media/create-service-principal-azure/create-service-principal-azure-key-vault.png)
2. Select **Settings** &gt; **Secrets** &gt; **+ Generate/Import**.

    ![Screenshot that options in the Key vault.](media/create-service-principal-azure/create-service-principal-azure-generate-secret.png)
3. Enter the **Name** of your choice, and save it to create a credential in Microsoft Purview.
4. Enter the **Value** as the **Secret value** from your Service Principal.

    ![Screenshot that shows the Key vault to create a secret.](media/create-service-principal-azure/create-service-principal-azure-sp-secret.png)
5. Select **Create** to complete.

## Create a credential for your secret in Microsoft Purview

To enable Microsoft Purview to use this service principal to authenticate with other services, follow these three steps:

1. [Connect your Azure Key Vault to Microsoft Purview](data-map-data-scan-credentials#create-azure-key-vaults-connections-in-your-microsoft-purview-account)
2. Grant your service principal authentication on your source. Every source is different, [so select your specific source page from the list of supported sources](data-map-data-sources) and follow instructions to assign permissions.
3. [Create a new credential in Microsoft Purview](data-map-data-scan-credentials#create-a-new-credential) - Use the service principal's application (client) ID and the name of the secret you created in your Azure Key Vault.