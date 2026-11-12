---
layout: Conceptual
title: How to request access to a data source in Microsoft Purview. | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-request-access
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article describes how a user can request access to a data source from within Microsoft Purview.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: sidontha nayenama
ms.service: purview
ms.subservice: purview-data-map-classic
ms.topic: how-to
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: template-how-to, msecd-doc-authoring-1030
locale: en-us
document_id: 001449f2-75b7-4a89-74be-2f46672a606b
document_version_independent_id: 001449f2-75b7-4a89-74be-2f46672a606b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-request-access.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-request-access
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-request-access.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 000746c2-f644-10cc-ca97-57a36aa1aa75
---

# How to request access to a data source in Microsoft Purview. | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

If you discover a data asset in the catalog that you would like to access, you can request access directly through Microsoft Purview. The request will trigger a workflow that will request that the owners of the data resource grant you access to that data source.

This article outlines how to make an access request.

Note

For this option to be available for a resource, a [self-service access workflow](../how-to-workflow-self-service-data-access-hybrid) needs to be created and assigned to the collection where the resource is registered. Contact the collection administrator, data source administrator, or workflow administrator of your collection for more information. Or, for information on how to create a self-service access workflow, see our [self-service access workflow documentation](../how-to-workflow-self-service-data-access-hybrid).

## Request access

1. To find a data asset, use Microsoft Purview's [search](../unified-catalog-data-assets-search) or [browse](../unified-catalog-data-assets-search#browse-the-unified-catalog) functionality.

    ![Screenshot of the Microsoft Purview governance portal, with the search bar and browse buttons highlighted.](../media/how-to-self-service-request-access/search-or-browse.png)
2. Select the asset to go to asset details.
3. Select **Request access**.

    ![Screenshot of a data asset's overview page, with the Request button highlighted in the mid-page menu.](../media/how-to-self-service-request-access/request-access.png)

    Note

    If this option isn't available, a [self-service access workflow](../how-to-workflow-self-service-data-access-hybrid) either hasn't been created, or hasn't been assigned to the collection where the resource is registered. Contact the collection administrator, data source administrator, or workflow administrator of your collection for more information. Or, for information on how to create a self-service access workflow, see our [self-service access workflow documentation](../how-to-workflow-self-service-data-access-hybrid).
4. The **Request access** window will open. You can provide comments on why data access is requested.
5. Select **Send** to trigger the self-service data access workflow.

    Note

    If you want to request access on behalf of another user, select the checkbox **Request for someone else** and populate the email id of that user.

    ![Screenshot of a data asset's overview page, with the Request access window overlaid. The Send button is highlighted at the bottom of the Request access window.](../media/how-to-self-service-request-access/send.png)

    Note

    A request access to resource set will actually submit the data access request for the folder one level up which contains all these resource set files.
6. Data owners will be notified of your request and will either approve or reject the request.