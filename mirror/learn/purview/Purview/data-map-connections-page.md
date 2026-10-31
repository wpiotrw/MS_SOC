---
layout: Conceptual
title: Data map connections page | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-connections-page
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article explains the uses for the connections page in the Microsoft Purview Data Map.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.service: purview
ms.subservice: purview-data-map
ms.topic: concept-article
ms.date: 2024-09-10T00:00:00.0000000Z
locale: en-us
document_id: 5759620e-8d81-9787-0377-557a3682552a
document_version_independent_id: 5759620e-8d81-9787-0377-557a3682552a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-connections-page.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-connections-page
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-connections-page.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 9a0d9309-b321-19df-31b5-dfee49210748
---

# Data map connections page | Microsoft Learn

The **Connections** page in the Microsoft Purview Data Map is a page for creating unique connections to services to use more of Microsoft Purview Data Map's features.

This page is **not** for [registered data sources](data-map-data-sources-register-manage#register-a-new-source). Instead this page is for connections in [workflows](concept-workflow) and [protection policies](data-gov-protection-policy).

To view and manage connections, you can find the connections page by:

- In the [Microsoft Purview portal](https://purview.microsoft.com):
    1. Select the Data Map application.
    2. Select the **Source management** dropdown.
    3. Select the **Connections** page.
- In the [classic Microsoft Purview governance portal](https://web.purview.azure.com):
    1. Select the **Management** application.
    2. Under the **Security and access** list, select **Connections**.

## Use

You might use the connection page when creating connections for some [workflows](concept-workflow) or [protection policies](data-gov-protection-policy) that require you to make special connections to partner resources.

For example:

- [Connect to ServiceNow in workflows](how-to-use-servicenow-workflows#connect-to-servicenow)
- [Create a policy enforcement connection for Amazon S3](how-to-create-protection-policy-amazon-s3)

On this page, you can edit and delete your connections by hovering over a connection and either selecting the **Edit** pencil button, or the **Delete** trashcan button.