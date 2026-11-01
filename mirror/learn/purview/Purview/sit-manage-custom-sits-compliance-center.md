---
layout: Conceptual
title: Manage custom sensitive information types | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-manage-custom-sits-compliance-center
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-sensitive-information-types
ms.date: 2026-06-26T00:00:00.0000000Z
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
description: Learn how to modify, and remove custom sensitive information types.
ms.custom: seo-marvel-apr2020, msecd-doc-authoring-1014
ai-usage: ai-assisted
locale: en-us
document_id: db6f4713-f720-f363-4c3d-886f103454b2
document_version_independent_id: db6f4713-f720-f363-4c3d-886f103454b2
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-manage-custom-sits-compliance-center.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-manage-custom-sits-compliance-center
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-manage-custom-sits-compliance-center.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: d29d19f1-e26b-488d-8fd2-e728019ad945
---

# Manage custom sensitive information types | Microsoft Learn

This article walks you through the steps to modify and remove an existing custom sensitive information type.

## Modify custom sensitive information types

To modify a custom sensitive information type, perform the following steps:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Information Protection** &gt; **Classifiers** &gt; **Sensitive info types** and choose the sensitive information type from the list that you want to modify.
2. Choose **Edit**.
3. You can add other patterns, with unique primary and supporting elements, confidence levels, character proximity, and [**additional checks**](sit-regex-validators-additional-checks#sensitive-information-type-additional-checks) or edit/remove the existing ones.

## Delete custom sensitive information types

Note

You can only remove custom sensitive information types; you can't remove built-in sensitive information types.

Important

Before your remove a custom sensitive information type, verify that no DLP policies or Exchange mail flow rules (also known as *transport rules*) still reference the custom sensitive information type that you plan to remove.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) &gt; **Information Protection** &gt; **Classifiers** &gt; **Sensitive info types** and choose the sensitive information type that you want to delete.