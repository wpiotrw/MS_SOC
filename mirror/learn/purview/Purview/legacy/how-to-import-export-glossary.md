---
layout: Conceptual
title: Import and export glossary terms | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-import-export-glossary
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how import and export business glossary terms in Microsoft Purview.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: evwhite
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: how-to
ms.date: 2024-04-30T00:00:00.0000000Z
locale: en-us
document_id: cfe8be05-e022-fa29-0b58-689956afea52
document_version_independent_id: cfe8be05-e022-fa29-0b58-689956afea52
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-import-export-glossary.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-import-export-glossary
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-import-export-glossary.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/3f837592-9b7c-422c-82fa-3523042264d7
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/f37b967c-efb8-47e1-9b0d-0ab7670e3db4
platformId: 7fc13758-5509-51b8-80d6-2c9b2f3ba0de
---

# Import and export glossary terms | Microsoft Learn

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

This article describes how to work with the business glossary in Microsoft Purview. It provides steps to create a business glossary term in the Microsoft Purview Data Catalog. It also shows you how to import and export glossary terms by using .CSV files.

Note

To edit the glossary, and import or export terms, you need to have [data curator permissions.](../data-gov-classic-permissions)

## Import terms into the glossary

The Microsoft Purview Data Catalog provides a template .CSV file for you to import terms from the catalog into your glossary. Duplicate terms include both spelling and capitalization, because term names are case-sensitive.

1. Open the Microsoft Purview Data Catalog.
2. If you're using the [classic Microsoft Purview portal](../use-microsoft-purview-governance-portal), select **Glossary**. If you're using the [new Microsoft Purview portal](../purview-portal) under **Business glossary**, select **Glossaries**.
3. Select the glossary where you want to import terms.

    1. [In the Microsoft Purview portal](../purview-portal), select **View terms** and then select **Import terms**.
    2. [In the classic governance portal](../use-microsoft-purview-governance-portal), select **Import terms**.
4. Select the template, or templates, for the terms you want to import, and then select **Continue**.

    You can select multiple templates and import terms for different templates from a single .csv file.

    ![Screenshot of the template list for importing a term, with the system default template highlighted.](../media/how-to-create-import-export-glossary/select-term-template-for-import.png)
5. Download the .csv template and use it to enter the terms that you want to add.

    Give your template file a name that starts with a letter and includes only letters, numbers, spaces, an underscore (\_), or other non-ASCII Unicode characters. Special characters in the file name will create an error.

    Important

    The system supports only importing columns that are available in the template. The **System default** template will have all the default attributes.

    Custom term templates define out-of-the box attributes and additional custom attributes. Therefore, the .CSV file differs in the total number of columns and the column names, depending on the term template that you select. You can also review the file for problems after upload.

    If you want to upload a file with a rich text definition, be sure to enter the definition with markup tags and populate the column `IsDefinitionRichText` to `true` in the .CSV file.

    ![Screenshot of the button for downloading a sample template file.](../media/how-to-create-import-export-glossary/select-file-for-import.png)
6. After you finish filling out your .CSV file, select your file to import, and then select **OK**.

The system will upload the file and add all the terms to your selected glossary.

Important

The email address for an expert or steward should be the primary address of the user from the Microsoft Entra group. Alternate emails, user principal names, and non-Microsoft Entra ID emails are not yet supported.

## Export terms from the glossary

When you're in any of your glossaries, the **Export terms** button is disabled by default. After you select the terms that you want to export, the **Export terms** button is enabled.

Note

Selected terms **don't** need to be from the same term template to be able to export them.

Select **Export terms** to download the selected terms.

[![Screenshot of the button to export terms on the glossary terms page.](../media/how-to-create-import-export-glossary/select-term-template-for-export.png)](../media/how-to-create-import-export-glossary/select-term-template-for-export.png#lightbox)

Important

The import process currently doesn't support updating the parent of a term.

## Business terms with approval workflow enabled

If [workflows](../concept-workflow) are enabled on a term, then any import actions for the term will go through an approval before they're saved in the data catalog.

When an import approval workflow is enabled for the Microsoft Purview glossary, you'll see **Submit for approval** instead of **OK** in the **Import** window when you're importing terms via .CSV file. Selecting **Submit for approval** triggers the workflow. However, the terms in the file won't be updated in the catalog until all the approvals are met.