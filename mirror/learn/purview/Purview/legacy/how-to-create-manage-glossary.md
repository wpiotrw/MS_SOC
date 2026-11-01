---
layout: Conceptual
title: Create and manage classic glossaries in the Microsoft Purview Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-create-manage-glossary
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to create and manage business glossaries in Microsoft Purview.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: evwhite
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: how-to
ms.date: 2024-06-05T00:00:00.0000000Z
locale: en-us
document_id: 19a75154-53df-70f3-4475-c741e5ed9699
document_version_independent_id: 19a75154-53df-70f3-4475-c741e5ed9699
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-create-manage-glossary.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-create-manage-glossary
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-create-manage-glossary.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/3f837592-9b7c-422c-82fa-3523042264d7
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/f37b967c-efb8-47e1-9b0d-0ab7670e3db4
platformId: 520179d9-815d-51eb-c9b5-cd45a896d887
---

# Create and manage classic glossaries in the Microsoft Purview Data Map | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Tip

The [new Microsoft Purview Data Catalog](../unified-catalog) has a new glossary experience. For more information, see [the glossary terms in the data catalog article.](../unified-catalog-glossary-terms-create-manage)

In the classic Microsoft Purview data governance experience, you can create multiple business glossaries to support separate glossaries for any context in your business. This article provides the steps to create and manage business glossaries in the classic Microsoft Purview Data Catalog.

## Create a new glossary

To create a classic business glossary, follow these steps:

1. Open the **Data catalog**
2. In the [classic Microsoft Purview portal](../use-microsoft-purview-governance-portal), select **Glossary**.
3. On the **Business glossary** page, select **+ New glossary**.

    ![Screenshot of the button and pane for creating a new glossary.](../media/how-to-create-manage-glossary/select-new-glossary.png)
4. Give your glossary a **Name** and a **Description**.
5. You need to select at least one **Steward**, a Microsoft Entra user or group who will manage the glossary.
6. You'll also need to select at least one **Expert**, a Microsoft Entra user or group who can be contacted for more information about the glossary.
7. You can give additional information about the stewards or experts here, and when you're finished, select **Create**.

    ![Screenshot that shows the new glossary template with all sections filled out.](../media/how-to-create-manage-glossary/create-new-glossary.png)
8. Once your new glossary is created, you'll be able to see it in the list of glossaries. You can switch between glossaries by selecting their names.

    ![Screenshot showing the business glossary page, with the new glossary highlighted and selected.](../media/how-to-create-manage-glossary/glossary-created.png)

## Manage or delete a glossary

1. To edit or delete a glossary, hover over the glossary and select the ellipsis button next to the glossary's name.

    ![Screenshot of the business glossary page, with a glossary highlighted, and the ellipsis button selected.](../media/how-to-create-manage-glossary/edit-or-delete-glossary.png)
2. If you select **Edit glossary**, you can edit the description and the steward or the expert, but at this time you can't change the glossary name. Select **Save** to save the changes.

    ![Screenshot of edit glossary page, with all values filled and the save button highlighted.](../media/how-to-create-manage-glossary/edit-glossary.png)
3. If you select **Delete glossary**, you'll be asked to confirm the deletion. All terms associated with the glossary will be deleted if you delete the glossary. Select **Delete** again to delete the glossary.

    ![Screenshot of the delete glossary window.](../media/how-to-create-manage-glossary/delete-glossary.png)