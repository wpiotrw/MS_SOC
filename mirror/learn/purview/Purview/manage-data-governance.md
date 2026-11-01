---
layout: Conceptual
title: Data lifecycle & records management overview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/manage-data-governance
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-02-26T00:00:00.0000000Z
audience: Admin
ms.topic: overview
ms.service: purview
ms.subservice: purview-data-lifecycle-management
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
recommendations: false
description: Implement data lifecycle & records management in Microsoft Purview to manage compliance or regulatory requirements foryour data & records across their lifecycle.
locale: en-us
document_id: 6d0a1651-c6c4-7e29-fccb-d6c165153617
document_version_independent_id: 6d0a1651-c6c4-7e29-fccb-d6c165153617
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/manage-data-governance.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: manage-data-governance
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/manage-data-governance.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: b8a3ae6f-3d13-1981-a913-5d6084b7a70b
---

# Data lifecycle & records management overview | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Use the **Data Lifecycle Management** and **Records Management** solutions in Microsoft Purview to manage your organization's compliance and regulatory requirements for data & records across their lifecycle.

Tip

Looking to map and manage your data across your entire data estate, including multi-cloud, and software-as-a-service (SaaS)? Use [Microsoft Purview Data Map and Microsoft Purview Unified Catalog](data-governance-get-started).

From a licensing perspective, there can be considerable overlap between data lifecycle management and records management. Both solutions support retention and deletion of data for Microsoft 365 apps and services.

Use the following graphic to help you identify the main configurable components for these solutions that each have their own configuration area in the [Microsoft Purview portal](purview-portal):

![Main components to configure and use to oversee your data with Microsoft Purview.](media/dlm_rm.png)

The following sections detail the main capabilities for each solution, with links to understand more. However, if you're looking for a guided deployment, see [Deploy a data governance solution with Microsoft Purview](data-governance-solution).

Looking for complementary capabilities to protect your data? See [Protect your data with Microsoft Purview](information-protection).

## Microsoft Purview Data Lifecycle Management

Keep what you need and delete what you don't:

| Capability | What problems does it solve? |
| --- | --- |
| [Retention policies for Microsoft 365 workloads, with retention labels for exceptions](retention) | Lets you retain or delete content with policy management for email, documents, Teams and Viva Engage messages. |
| [Inactive mailboxes](inactive-mailboxes-in-office-365) | Lets you retain mailbox content after employees leave the organization so that this content remains accessible to administrators, compliance officers, and records managers. |
| [Archive mailboxes](archive-mailboxes) | Provides additional mailbox storage space for users. |
| [Import service for PST files](pst-import-overview) | Supports bulk-importing PST files to Exchange Online mailboxes to retain and search email messages for compliance or regulatory requirements. |

Want to learn more? See [Learn about data lifecycle management](data-lifecycle-management).

Ready to start using some or all of these capabilities? See [Get started with data lifecycle management](get-started-with-data-lifecycle-management).

## Microsoft Purview Records Management

Manage high-value items for business, legal, or regulatory record-keeping requirements:

| Capability | What problems does it solve? |
| --- | --- |
| [File plan](file-plan-manager) | Lets you create retention labels interactively or import in bulk, and export for analysis. Labels support additional administrative information (optional) to help you identify and track business or regulatory requirements. |
| [Retention labels for individual items, retention policies if needed for baseline retention](retention) | Labels support flexible retention and deletion schedules that can be applied manually or automatically, with records declaration when needed. |
| [Disposition review and proof of disposition](disposition) | Manual review of content before it's permanently deleted, with proof of disposition of records. |

Want to learn more? See [Learn about records management](records-management).

Ready to start using some or all of these capabilities? See [Get started with records management](get-started-with-records-management).

## Licensing requirements

To understand your licensing requirements and options, see the information from the Microsoft Purview Service Description, [Microsoft Purview Data Lifecycle Management & Records Management](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-data-lifecycle--records-management) section for feature-level licensing requirements.