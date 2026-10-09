---
layout: Conceptual
title: Azure Blueprints retirement FAQ - Azure Blueprints | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/blueprints/blueprint-retirement-faq
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/133/azure
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/675ae472-f324-ec11-b6e6-000d3a4f0da0
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
adobe-target: true
author: kgremban
learn_banner_products:
- azure
ms.author: kgremban
ms.service: azure-blueprints
description: Frequently asked questions about the Azure Blueprints retirement, including what changes at retirement, data retention, deny-assignment impact, and migration to Azure Deployment Stacks and template specs.
ms.topic: concept-article
ms.date: 2026-06-26T00:00:00.0000000Z
locale: en-us
document_id: 5856f0dc-99a1-0c89-46b5-7659b3659074
document_version_independent_id: 322df1cd-0a5c-8f70-6e99-6f2551aa24d5
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/blueprints/blueprint-retirement-faq.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/blueprints/blueprint-retirement-faq
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/blueprints/blueprint-retirement-faq.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/40ba597f-f235-4787-be4d-fde8258e1045
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c4bc7fc-8fc8-4dea-bc53-680da859ef46
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 82600b9e-416f-7cd5-a14e-090059a6f132
---

# Azure Blueprints retirement FAQ - Azure Blueprints | Microsoft Learn

Azure Blueprints (Preview) is retired on **January 31, 2027**, with a phased retirement beginning July 31, 2026. For the phased timeline and migration recommendation, see [Azure Blueprints retirement](blueprint-retirement). This article answers common questions about the retirement.

## Frequently asked questions

### What happens if I don't migrate?

After January 31, 2027, Blueprints can no longer be modified, all Blueprint Locks (Deny Assignments) are removed, and Blueprint Definitions and Assignments are removed from the portal. Resources previously deployed by Blueprints remain in place and inherit parent RBAC, but any policy/permission enforcement that depended on Deny Assignments is gone. Customers without a migration plan effectively lose the management and lock-enforcement layer Blueprints provided.

#### Will existing Blueprint definitions and assignments remain readable or manageable for some time?

They shouldn't be relied on past the retirement date. Definitions and Assignments are **removed at retirement**. Before retirement, the service phases down to **read + delete only** (30 days before retirement).

### Will resources previously deployed through Blueprints remain in place?

Yes. Resources deployed by Blueprints **remain in place** unless you delete them. The main impact is on the **management surface** (Blueprint Definitions, Assignments, and Locks). The one exception is **Blueprint Locks (Deny Assignments)**, which are removed at retirement — this can have a real impact on the deployed resources' effective permissions.

### Does Microsoft still recommend a full migration for a tenant planned for retirement?

Yes. Microsoft recommends migration to **Deployment Stacks** (preferred) or template specs. Starting January 31, 2027, Blueprint updates are no longer possible (effectively delete-only), Locks (Deny Assignments) are removed, and Blueprints is retired. Any definitions, versions, and assignments you haven't exported are permanently deleted at retirement and can't be recovered, so export anything you want to keep before January 31, 2027.

### Which management options remain available in each phase?

| Phase | Portal | PowerShell / REST API | Read | Create | Update | Delete |
| --- | --- | --- | --- | --- | --- | --- |
| Phase 1 (on announce) | Yes | Yes | Yes | Definitions: No (net-new disabled). Assignments: Yes | Yes | Yes |
| Phase 2 (~T+90) | Yes | Yes | Yes | Assignments: No. Definitions: No | Definitions: No. Assignments: Yes | Yes |
| Phase 3 (~T-30) | Yes | Yes | Yes | No | No (PUT fully disabled) | Yes |
| Phase 4 (retired, Jan 31, 2027) | Removed | CLI/PS commands postponed (Apr/May 2027). REST: read/delete only until removed | Read goes away as the service is removed | No | No | Delete-only window until full service removal |

### Once retired, are Blueprint Locks / Deny Assignments removed automatically, even if I take no action?

Yes. At retirement, Microsoft removes all remaining Blueprint Locks (Deny Assignments) automatically.

### Apart from the locks, do later phases affect my ability to view, export, or delete existing definitions and assignments?

Through Phase 3, **read and delete remain available**. At Phase 4 (retirement), Definitions and Assignments are removed from the portal and ultimately deleted. Export anything you want to preserve before the retirement date.

### For a tenant already planned for decommissioning, can I take a limited approach instead of full migration?

The recommended path is to start migration as soon as possible and complete it before the retirement date. A limited "export + standard Azure resource locks" approach is acceptable when the tenant itself is on a near-term decommissioning timeline, but Microsoft recommends Deployment Stacks for any workload that outlives the retirement.

### Removing Deny Assignments effectively widens RBAC in my org. How do I retain that protection?

Manage the workload under a Deployment Stack. Deployment Stacks provide the equivalent management-plane protection, including deny settings, in a supported, forward-going service.

### How can I identify where Azure Blueprints is being used in my environment?

You can identify Azure Blueprints usage in two ways:

- **Azure Advisor** surfaces a recommendation highlighting subscriptions and management groups where Blueprints is in use.
- You can review the **Azure Blueprints blade in the Azure portal** to see your existing blueprint definitions and assignments directly.

### What's the recommended replacement for Azure Blueprints?

**Azure Deployment Stacks** is the recommended replacement. It provides the core capabilities you rely on in Blueprints, including:

- Grouping and managing a collection of resources as a single unit.
- Lifecycle management across create, update, and delete operations.
- Enforcing protection on managed resources through **deny assignments**.

Depending on your needs, you can also publish your definitions as **template specs** or store them in a **Git repository** to take advantage of versioning.

### Will I lose the resource-lock (deny assignment) protection that Blueprints provides?

Before retirement, migrate your managed resources to a **Deployment Stack** and configure **deny assignments** on the stack to preserve the same lock behavior you have today. Plan this migration early — it's an important step to avoid any gap in protection.