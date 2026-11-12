---
layout: Conceptual
title: Microsoft Purview Self-service access concepts | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/concept-self-service-data-access-policy
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Understand what self-service access and data discovery are in Microsoft Purview, and explore how users can take advantage of it.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.topic: concept-article
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1030
locale: en-us
document_id: 6b11e1cb-2d9a-91ac-4d09-56e6dfa43f0a
document_version_independent_id: 6b11e1cb-2d9a-91ac-4d09-56e6dfa43f0a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/concept-self-service-data-access-policy.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/concept-self-service-data-access-policy
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/concept-self-service-data-access-policy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: db46b7a8-faa5-89d7-524e-5f607b7b5822
---

# Microsoft Purview Self-service access concepts | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

This article helps you understand Microsoft Purview Self-service data access policy.

Important

Microsoft Purview Self-service data access policy is currently in PREVIEW. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, preview, or otherwise not yet released into general availability.

## Important limitations

The self-service data access policy is only supported when the prerequisites mentioned in [Data Policy Enforcement](../how-to-enable-data-policy-enforcement#prerequisites) are satisfied.

## Overview

Microsoft Purview Self-service data access workflow allows data consumer to request access to data when browsing or searching for data. Once the data access request is approved, a policy gets auto-generated to grant access to the requestor provided the data source is enabled for Data Policy Enforcement. Currently, self-service data access policy is supported for storage accounts, containers, folders, and files.

A **workflow admin** needs to map a self-service data access workflow to a collection. Collection is logical grouping of data sources that are registered within Microsoft Purview. **Only data source(s) that are registered** for Data Policy Enforcement has self-service policies auto-generated.

## Terminology

- **Data consumer** is anyone who uses the data. Example, a data analyst accessing marketing data for customer segmentation. Data consumer and data requestor will be used interchangeably within this document.
- **Collection** is logical grouping of data sources that are registered within Microsoft Purview.
- **Self-service data access workflow** is the workflow that is initiated when a data consumer requests access to data.
- **Approver** is either a security group, a Microsoft Entra user, or a Microsoft Entra group that can approve self-service access requests.

## How to use Microsoft Purview self-service data access policy

Microsoft Purview allows organizations to catalog metadata about all registered data assets. It allows data consumers to search for or browse to the required data asset.

With self-service data access workflow, data consumers can not only find data assets but also request access to the data assets. When the data consumer requests access to a data asset, the associated self-service data access workflow is triggered.

A default self-service data access workflow template is provided with every Microsoft Purview account. The default template can be amended to add more approvers and/or set the approver's email address. For more details, refer [Create and enable self-service data access workflow](../how-to-workflow-self-service-data-access-hybrid).

Whenever a data consumer requests access to a dataset, the notification is sent to the workflow approver(s). The approver(s) can view the request and approve it either from Microsoft Purview governance portal or from within the email notification. When the request is approved, a policy is auto-generated and applied against the respective data source. Self-service data access policy gets auto-generated only if the data source is registered for **Data Policy Enforcement**. The prerequisites mentioned within the [Data Policy Enforcement](../how-to-enable-data-policy-enforcement#prerequisites) have to be satisfied.

Data consumer can access the requested dataset using tools such as Power BI or Azure Synapse Analytics workspace.

Note

Users won't be able to browse to the asset using the Azure portal or Storage explorer if the only permission granted is read/modify access at the file or folder level of the storage account.

Caution

Folder level permission is required to access data in ADLS Gen 2 using Power BI. Additionally, resource sets aren't supported by self-service policies. Hence, folder level permission needs to be granted to access resource set files such as CSV or parquet.