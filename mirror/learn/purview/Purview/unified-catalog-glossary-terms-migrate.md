---
layout: Conceptual
title: Migrate Classic Glossary Terms and Enable Asset Curation in Unified Catalog (Preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-glossary-terms-migrate
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2026-06-23T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.localizationpriority: medium
ms.collection:
- tier2
search.appverid:
- MET150
- MOE150
description: Learn how to migrate glossary terms (preview) created in the classic Microsoft Purview governance portal to Microsoft Purview Unified Catalog. This process allows you to curate data assets and columns in Unified Catalog.
locale: en-us
document_id: 10455f5a-dc0f-c855-6dda-398fec894080
document_version_independent_id: 10455f5a-dc0f-c855-6dda-398fec894080
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-glossary-terms-migrate.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-glossary-terms-migrate
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-glossary-terms-migrate.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: f540faf2-9d53-8621-43b3-0421b48e9c09
---

# Migrate Classic Glossary Terms and Enable Asset Curation in Unified Catalog (Preview) | Microsoft Learn

Microsoft Purview Unified Catalog provides a centralized place for creating and managing [glossary terms](unified-catalog-glossary-terms) for both business concepts and data assets. If you created [glossary terms for data assets and columns](how-to-create-manage-glossary-term) in the classic data governance glossary experience, you can start migrating them into the unified glossary experience in Unified Catalog.

This article explains the one-time migration process and the benefits of managing all your glossary terms for [business concepts](data-governance-get-started#business-concepts) and data assets in one centralized place.

Note

The process outlined in this article enables you to curate data assets with glossary terms. Therefore, even if you don't plan to migrate classic terms, you still need to complete the workflow described in the steps below to enable asset curation.

## Overview

You can bring classic glossary terms into the Unified Catalog for centralized creation and management of all glossary terms. This migration process is also what enables curation of data assets. After your terms are migrated to the **.StagingDomain** domain (a system domain automatically created for migration), you can move them into the governance domain that manages them going forward.

With the new unified glossary experience, any glossary term can apply to a business concept and data asset and column. The **Related** tab on each glossary term page shows its relationship to other glossary terms, data products, critical data elements, data assets, and columns.

When you migrate your glossary terms, you can:

- Use Unified Catalog as your single entry point for glossary terms within governance domains.
- Connect your terms to logical [business concepts](data-governance-get-started#business-concepts) and physical concepts, or [data assets](unified-catalog-data-assets-search) (tables and columns).
- Invoke Copilots to enhance your glossary term creation and management experience.

## Who needs to complete this process

This process is a required step in order to curate, or attach glossary terms to, data assets.

If your organization has glossary terms in the classic data governance experience, the migration process brings those terms into the updated experience, Unified Catalog.

If you're new to Unified Catalog in the Microsoft Purview portal, or never created glossary terms in the classic data governance experience, you still need to follow the steps of the enablement process by confirming use of current terms in Unified Catalog.

## Plan for the migration and enablement process

Important

**Review this section closely and plan early.** The migration and enablement process is a one-time action that you can't reverse. When the process finishes, terms in the classic governance experience become read-only, and term templates convert to custom attributes that you can't edit or delete. Use this information to help you develop a thorough migration plan that involves the right people and ensures the most efficient outcomes for your organization.

### What gets migrated and what doesn't

#### Glossaries and terms

The migration process moves glossaries and glossary terms that you created in the classic data governance experience. You can find these classic terms in the new Purview portal in **Unified Catalog**, under **Catalog management**, on the **Classic types** page.

When you migrate terms, this metadata is migrated into Unified Catalog:

- Glossaries and terms within, including all out-of-the-box metadata such as acronyms and parent information.
- All existing relationships to assets and columns in Microsoft Purview Data Map.

#### Term templates

The migration process moves all [term templates](how-to-manage-term-templates) when you migrate terms. During this process, term templates convert to [business concept attributes](unified-catalog-attributes-business-concept). The attributes have the **.StagingDomain** domain scope, which you can extend to more domains.

You [can't edit or delete business concept attributes](unified-catalog-attributes-business-concept#expire-an-attribute-or-attribute-group), so be sure to review term templates and delete unwanted ones before you migrate them.

#### Workflows

Any [workflows](concept-workflow) you have on classic terms are **not** migrated.

### Cleanup work to do before migration

- **Review and delete unwanted terms.** Delete any classic terms that you don't want to migrate *before* beginning the migration process, so that unwanted terms don't clutter the **.StagingDomain** domain. This step greatly facilitates and speeds up your process of relocating terms once they're brought over into Unified Catalog.
- **Review and delete unwanted term templates.** Term templates convert to business concept attributes after migration. These [attributes can't be edited or deleted](unified-catalog-attributes-business-concept#expire-an-attribute-or-attribute-group), so be sure not to migrate anything you don't want to appear or manage in Unified Catalog.

### What happens during migration

The migration process creates a system-generated **.StagingDomain** governance domain and adds the migrated terms to it. Depending on the number of terms, it can take up to 48 hours for all migrated terms to appear in the staging domain. All glossary terms are added to the staging domain as drafts.

Only users who have both the Governance Domain Creator and Data Curator roles can see the **.StagingDomain** domain. You can't edit or publish this domain.

### What happens after migration

When migration finishes, all terms are added to the **.StagingDomain** domain. The classic terms no longer appear on the **Classic types** page in Unified Catalog.

The **.StagingDomain** domain stays in your list of governance domains, even after you reassign the terms to the appropriate governance domains. You can't delete it.

The classic glossary experience becomes read-only, and you can't create any new terms there. Classic glossary terms don't appear when you search for them in data assets in Data Map.

Classic term APIs become read-only after migration finishes.

### Plan who moves and manages the migrated terms

Identify a user in your organization to conduct the migration. This user needs both the **Governance Domain Creator** and **Data Curator** roles. This user also needs access to the **.StagingDomain** domain.

Identify the Data Stewards in your organization who move the terms into the correct governance domains. Add each of those Data Stewards as owners of the **.StagingDomain** domain.

#### Required user roles

| Role | Necessary for | Description |
| --- | --- | --- |
| **Governance Domain Creator** and **Data Curator** (both are required) | Performing the migration and accessing the **.StagingDomain** domain. | Only users with this role can start the migration process. The user who starts the migration process becomes the owner of the **.StagingDomain** domain. Users with this role can access the **.StagingDomain** domain to view and move migrated terms. |
| **Data Steward** | Adding glossary terms to a governance domain. | Data Stewards must be assigned to the governance domain that they're moving migrated glossary terms into. Data Stewards must also be added to the **.StagingDomain** domain so they can move terms from that domain to the appropriate governance domain. |

Learn how to assign [data governance roles and permissions](data-governance-roles-permissions).

## Steps for migrating glossary terms and enabling asset curation

This process enables your organization to add glossary terms to data assets and columns. During this process, you choose whether to migrate your existing glossary terms in the classic experience into Unified Catalog, or to use the glossary terms you already have in the Unified Catalog without migrating classic terms.

### Step 1: Assign the necessary roles

See the required roles for the migration process.

### Step 2: Choose how to enable asset curation

1. In the [Microsoft Purview portal](https://purview.microsoft.com), go to **Unified Catalog** &gt; **Catalog management** &gt; **Classic types**.
2. Select **Enable asset curation**.
3. On the **Enable asset curation** flyout pane, select one of the following options, then select **Enable**:
    - **Migrate classic terms to Unified Catalog**: Select this option to migrate classic terms into Unified Catalog. After migration, classic terms are deactivated and placed in a read-only state for reference. When full migration is complete, you can curate data assets and columns with Unified Catalog terms.
    - **Switch directly to terms in Unified Catalog**: Select this option if you don't have any classic terms, or you intend to no longer use your classic terms and don't want to migrate them. If you have classic terms and select this option, your classic terms are deactivated and placed in a read-only state.

If you select **Migrate classic terms to Unified Catalog**, you see a summary of what will be migrated on the **Migrate glossary terms** flyout pane. Migration is a one-time process that can't be reversed, so you have an option of migrating a small sample of terms to see how the process goes, or to do the full migration all at once. At **Mode**, select how you want to proceed:

- **Sample migration**: This option migrates up to five glossaries so you can see how the migration works. Select this option, and then select **Start sample migration** to start the sample migration.
- **Full migration**: This option moves all glossaries and terms at once. Select this option, and then select **Start full migration** to start the migration process. This process can't be stopped or reversed after you start it.

    Note

    After you start the full migration process, access to terms in the classic governance experience is restricted to read-only. Any classic terms added by using APIs going forward are automatically added to the **.StagingDomain** domain.

### Step 3: View terms in the staging domain and add more users to roles

After you select **Start full migration**, the glossary terms gradually appear in the **.StagingDomain** domain on the governance domains page. Depending on the number of terms migrated, the migration process can take up to 48 hours.

To locate the **.StagingDomain** domain:

1. In Unified Catalog, go to **Catalog management** &gt; **Governance domains**.
2. At the top of the list, find the domain named **.StagingDomain**.

When you begin migration, assign the necessary **Data Stewards** to the **.StagingDomain** domain so they can move terms to governance domains. On the staging domain's page, go to the **Roles** tab. Select the icon next to the **Data Steward** header to add users to this role for the domain. You might also want to add more users as owners of the **.StagingDomain** domain to help manage the domain.

### Step 4: Move terms from the staging domain to owning domains

Important

A single term can only have 100 relationships in Unified Catalog. Review the relationships and clean up before migrating.

When migration is complete, reassign the glossary terms from the **.StagingDomain** domain to the appropriate governance domains for ongoing ownership. To assign migrated terms to a governance domain:

1. In **Unified Catalog**, under **Catalog management**, select **Governance domains**.
2. Select **.StagingDomain**, at the top of the list of governance domains.
3. On the **Details** tab, find the **Glossary terms** card and select **View all**.
4. Select **Move to**, and then select the box next to the terms you want to move. Selected terms are moved into one governance domain. To move terms into separate domains, select the terms going into one domain at a time.
5. After selecting the terms to move, select **Move item**.
6. In the **Move to** window, select the governance domain from the dropdown list that you want to move the terms into.
7. Select **Move**.

The terms are moved into their new governance domain. You can now add glossary terms to data assets and columns. Data Stewards see a notice at the top of the glossary terms list page that new terms were added to their governance domain.

Note

- Term hierarchies always move as a unit. If you select a parent term, all of its children move with the parent. If you don't want the hierarchy to be moved, remove the parent terms first.
- The migration process doesn't automatically move any terms with duplicate names in the destination governance domain.