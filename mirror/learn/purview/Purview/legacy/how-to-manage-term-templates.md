---
layout: Conceptual
title: How to manage term templates for business glossary | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/how-to-manage-term-templates
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to manage term templates for business glossary in a Microsoft Purview Data Catalog.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: nayenama
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: how-to
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
locale: en-us
document_id: be3391ab-4e29-b640-32e9-b99b62377c37
document_version_independent_id: be3391ab-4e29-b640-32e9-b99b62377c37
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/how-to-manage-term-templates.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/how-to-manage-term-templates
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/how-to-manage-term-templates.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/3f837592-9b7c-422c-82fa-3523042264d7
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/f37b967c-efb8-47e1-9b0d-0ab7670e3db4
platformId: 246ffc59-4015-6fa4-85bf-be0f4b72725b
---

# How to manage term templates for business glossary | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Microsoft Purview allows you to create a glossary of terms that are important for enriching your data. Each new term added to your Microsoft Purview Data Catalog Glossary is based on a term template that determines the fields for the term. This article describes how to create a term template and custom attributes that can be associated to glossary terms.

## Manage term templates and custom attributes

Using term templates, you can create custom attributes, group them together and apply a template while creating terms.

Note

Once a term is created, the template associated with the term can't be changed.

1. Open the Microsoft Purview Data Catalog.
2. If you're using the [classic Microsoft Purview portal](../use-microsoft-purview-governance-portal), select **Glossary**. If you're using the [new Microsoft Purview portal](../purview-portal) under **Business glossary**, select **Glossaries**.
3. Select **Manage term templates**.

    ![Screenshot of Glossary terms &gt; Manage term templates button.](../media/how-to-manage-glossary-term-templates/manage-term-templates.png)
4. The page shows both system and custom attributes. Select the **Custom** tab to create or edit term templates.

    ![Screenshot of Glossary terms &gt; Manage term templates page.](../media/how-to-manage-glossary-term-templates/manage-term-custom.png)
5. Select **+ New term template** and enter a template name and description.

    ![Screenshot of Glossary terms &gt; Manage term templates &gt; New term templates](../media/how-to-manage-glossary-term-templates/new-term-template.png)
6. Select **+ New attribute** to create a new custom attribute for the term template. Enter an attribute name, description. The custom attribute name must be unique within a term template but can be same name can be reused across templates.

    Choose the field type from the list of options **Text**, **Single choice**, **Multi choice**, or **Date**. You can also provide a default value string for Text field types. The attribute can also be marked as **required**.

    ![Screenshot of Glossary terms &gt; New attribute page.](../media/how-to-manage-glossary-term-templates/new-attribute.png)
7. Once all the custom attributes are created, select **Preview** to arrange the sequence of custom attributes. You can drag and drop custom attributes in the desired sequence.

    ![Screenshot of Glossary terms &gt; Preview term template.](../media/how-to-manage-glossary-term-templates/preview-term-template.png)
8. Once all the custom attributes are defined, select **Create** to create a term template with custom attributes.

    ![Screenshot of Glossary terms &gt; New term template - Create button.](../media/how-to-manage-glossary-term-templates/create-term-template.png)
9. Existing custom attributes can be marked as expired by checking **Mark as Expired**. Once expired, the attribute can't be reactivated. The expired attribute is greyed out for existing terms. Future new terms created with this term template will no longer show the attribute that has been marked expired.

    ![Screenshot of Glossary terms &gt; Edit attribute to mark it as expired.](../media/how-to-manage-glossary-term-templates/expired-attribute.png)
10. To delete a term template, open the template and select **Delete**. Note, if the term template is in use, you can't delete it until you remove the glossary terms to which it's assigned.