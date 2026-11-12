---
layout: Conceptual
title: Impact of deleting Microsoft Purview account on access policies | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/concept-policies-purview-account-delete
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This guide discusses the consequences of deleting a Microsoft Purview account on published access policies
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: vlrodrig
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: article
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
locale: en-us
document_id: 3353dc46-eddd-826c-bd1d-0075a4a56c6b
document_version_independent_id: 3353dc46-eddd-826c-bd1d-0075a4a56c6b
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/concept-policies-purview-account-delete.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/concept-policies-purview-account-delete
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/concept-policies-purview-account-delete.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: e0ebdb63-8c91-e4d1-d3a1-cb3ca1ddbc3c
---

# Impact of deleting Microsoft Purview account on access policies | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

## Important considerations

Deleting a Microsoft Purview account that has active (that is, published) policies removes those policies. Any access to a data source or a dataset that was previously provisioned from Microsoft Purview gets revoked. This can lead to outages, that is, users or groups in your organization not able to access critical data. Review the decision to delete the Microsoft Purview account with the people in Policy Author role at root collection level before proceeding. To find out who holds that role in the Microsoft Purview account, review the section on managing role assignments in this [guide](../data-map-collections-manage-classic#add-roles-and-restrict-access-through-collections).

Before deleting the Microsoft Purview account, it's advisable that you provision access to the users in your organization that need access to datasets using an alternate mechanism or a different Purview account. Then orderly delete or unpublish any active policies

- [Deleting DevOps policies](../how-to-policies-devops-authoring-generic#delete-a-devops-policy) - You need to delete DevOps policies for them to be unpublished.
- [Unpublishing Data Owner policies](../how-to-policies-data-owner-authoring-generic#unpublish-a-policy).
- [Deleting Self-service access policies](../how-to-delete-self-service-data-access-policy) - You need to delete Self-service access policies for them to be unpublished.