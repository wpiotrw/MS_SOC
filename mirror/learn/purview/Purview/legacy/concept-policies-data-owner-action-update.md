---
layout: Conceptual
title: Role definitions SQL Performance Monitor and SQL Security Auditor supported only from DevOps policies experience | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/concept-policies-data-owner-action-update
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This guide discusses actions that have been retired from Data owner policies experience and are now supported only from the DevOps policies experience.
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
document_id: 8b0b07b2-a3a0-2f33-4181-ae5f718a56ec
document_version_independent_id: 8b0b07b2-a3a0-2f33-4181-ae5f718a56ec
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/concept-policies-data-owner-action-update.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/concept-policies-data-owner-action-update
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/concept-policies-data-owner-action-update.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/cbe4ca68-43ac-4375-aba5-5945a6394c20
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/ced846cc-6a3c-4c8f-9dfb-3de0e90e2742
platformId: debf6e79-f614-39e9-7fe3-27ea6033cb1b
---

# Role definitions SQL Performance Monitor and SQL Security Auditor supported only from DevOps policies experience | Microsoft Learn

Important

**Retirement of Microsoft Purview data governance capabilities only**

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. **Microsoft Purview as a whole is not being retired. Microsoft Purview data security and compliance capabilities are not affected by this announcement, and Microsoft will continue investing in them.**

Microsoft is consolidating its **data governance** capabilities in Microsoft Fabric. New Microsoft Purview data governance accounts can no longer be created, and existing data governance capabilities will remain in maintenance mode through November 12, 2027.

For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

This guide discusses actions that have been retired from Data owner policies experience and are now supported only from the DevOps policies experience.

## Important considerations

The following two actions that were previously available in the Microsoft Purview Data owner policies experience are now supported only from the Microsoft Purview DevOps policies, which is a more focused experience.

- SQL Performance Monitor
- SQL Security Auditor

If you currently have Data owner policies with these actions we encourage you to give the DevOps policies experience a try. Creating new policies or editing existing policies that involve these two actions is now unsupported from the Data owner experience.