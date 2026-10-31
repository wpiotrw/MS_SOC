---
layout: Conceptual
title: Create an Azure policy exclusion for Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-azure-policy-exclusion
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
description: Learn how to create an exception to deploy Microsoft Purview while leaving existing Azure policies in place to maintain security.
locale: en-us
document_id: 44f7dccf-d80e-ee38-e290-1e5069794468
document_version_independent_id: 44f7dccf-d80e-ee38-e290-1e5069794468
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-azure-policy-exclusion.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-azure-policy-exclusion
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-azure-policy-exclusion.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/eea02214-631d-404a-92d1-5a3357c32a26
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/f42c31d7-eed9-43b7-9757-54caffb53cdc
platformId: 6f691529-3453-1fcf-4528-3be08fc8c32b
---

# Create an Azure policy exclusion for Microsoft Purview | Microsoft Learn

Many subscriptions have [Azure Policies](/en-us/azure/governance/policy/overview) in place that restrict the creation or update of some resources. This is to maintain subscription security and cleanliness. However, Microsoft Purview accounts created before December 15, 2023 (or deployed using API version previous to 2023-05-01-preview) deployed an Azure Storage account when it was created. It's managed by Azure, so you don't need to maintain it, but it's necessary for Microsoft Purview to run correctly. Existing policies could block Microsoft Purview from updating this Azure Storage account, which can cause errors during scanning.

Overall, your approach to resolving this error is going to be dependent on your organizations needs and policies, but here are a few ways you could update your policies to resolve this issue.

To maintain your policies in your subscription, but still allow the creation and updates to these managed resources, you can create an exclusion. For example, adding an exclusion for the resource group where your Microsoft Purview account is being deployed.

For steps to create an exclusion for your policies, see [these steps to add an exclusion to your policy](/en-us/azure/governance/policy/tutorials/create-and-manage#update-assignment-with-exclusion).

## Use resource selectors on a created policy

Depending on other policies deployed in your subscription, or depending on your region, you could need to add **Resource selectors** under the **Advanced** tab when assigning a policy. For example, you might need to add a resource selector for **resourceLocation** set to the region where you'll deploy your Microsoft Purview account. For more information about these conditions, see [our documentation on location conditions](/en-us/azure/active-directory/conditional-access/location-condition).

## Create an exemption

Exemptions are recommended for time-bound or specific scenarios where a resource or resource hierarchy should still be tracked and would otherwise be evaluated, but there's a specific reason it shouldn't be assessed for compliance. It would allow a temporary exception to your policy for a resource to exist for a finite amount of time.

For more information, see [the documentation for policy exemptions](/en-us/azure/governance/policy/concepts/exemption-structure#exemption-creation-and-management).