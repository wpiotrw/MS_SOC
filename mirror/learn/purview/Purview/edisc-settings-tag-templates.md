---
layout: Conceptual
title: Configure tag templates in eDiscovery | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/edisc-settings-tag-templates
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about tag templates in eDiscovery in the Microsoft Purview portal.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-04-02T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-ediscovery
ms.collection:
- purview-compliance
- ediscovery
search.appverid:
- MOE150
- MET150
f1.keywords:
- NOCSH
ai-usage: ai-assisted
locale: en-us
document_id: d9e1921c-a6d3-031a-bf61-f238e2948b70
document_version_independent_id: d9e1921c-a6d3-031a-bf61-f238e2948b70
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/edisc-settings-tag-templates.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: edisc-settings-tag-templates
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/edisc-settings-tag-templates.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: 5bfd6581-cee7-b020-02a2-5c371d6f9905
---

# Configure tag templates in eDiscovery | Microsoft Learn

Use tag templates to define and standardize tags and the review workflow across all [cases](edisc-cases-manage) and [review sets](edisc-review-set-manage) in your organization. Each tag template contains tag groups where you can create a grouping structure for individual tags.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Create tag templates

To create a new tag template, complete the following steps:

1. In the [Microsoft Purview portal](https://purview.microsoft.com), select **Settings** &gt; **eDiscovery** and then select **Tag templates**.
2. Select **Create**.
3. On **New tag template**, enter a name and description for the tag template.
4. In the initial tag group, enter a tag group name and use the dropdown to define this group as a **Multi-select** or **Single-select** tag group.
5. Enter at least one tag name in the tag group. Select **Add tag** to add more tags to the tag group.
6. If needed, select **Add tag group** to add more tag groups and tags to the tag template.
7. Preview the tag template group and tag structure in the **Preview** pane on the right side of **New tag template**.
8. When complete, select **Save**.

The tag template is now available for use in all cases and review sets in your organization.

## Manage tag templates

After you create a tag template, you can edit or delete it. You can also view information about the tag template, including the dates when you created or last modified it.

1. In the [Microsoft Purview portal](https://purview.microsoft.com), select **Settings** &gt; **eDiscovery** and then select **Tag templates**.

    - To edit a tag template, select the tag template name on **Manage tag templates** and select **Edit**. On **Edit tag template**, you can edit the tag template name, description, and tag groups and tags. When done, select **Save**.
    - To delete a tag template, select the tag template name on **Manage tag templates** and select **Delete**. Select **Yes** to confirm the deletion or **No** to cancel the deletion.

## Apply tag templates to a case and review sets

After you create a tag template, you can apply it to a review set. You can apply a tag template when you create a new review set or when you edit an existing review set.

To apply a tag template to a new review set, complete the following steps:

1. In the [Microsoft Purview portal](https://purview.microsoft.com), select **eDiscovery** &gt; **Cases** and select a case.
2. In the case, select **Review sets**, select a review set, then select the **All items** tab.
3. On the review set command bar, select **Manage** &gt; **Tags**.
4. On **Manage tags**, delete the blank tag group, then select **Import tag templates**.
5. On **Import tag templates**, select the tag template that you want to apply to the review set, then select **Import**.
6. If needed, edit the tag template as it applies to the case and review set.
7. Select **Save** to apply the tag templates to the case and review set.

The applied tag template is now available for use in the case and all included review sets.