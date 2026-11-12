---
layout: Conceptual
title: Workflows in Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/concept-workflow
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This article describes workflows in Microsoft Purview, the roles they play, and who can create and manage them.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: nayenama
ms.service: purview
ms.subservice: purview-data-map-classic
ms.topic: article
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: template-concept, msecd-doc-authoring-1030
locale: en-us
document_id: e7dd1fed-e67f-80b2-2348-cdac31743285
document_version_independent_id: e7dd1fed-e67f-80b2-2348-cdac31743285
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/concept-workflow.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/concept-workflow
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/concept-workflow.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: d59887ba-9b52-261b-1704-da1ce5371cef
---

# Workflows in Microsoft Purview | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

Important

This feature is currently in preview. The [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) include additional legal terms that apply to Azure features that are in beta, in preview, or otherwise not yet released into general availability.

Workflows are automated, repeatable business processes that users can create within Microsoft Purview to validate and orchestrate CUD (create, update, delete) operations on their data entities. Enabling these processes allows organizations to track changes, enforce policy compliance, and ensure quality data across their data landscape.

Workflows automate the approval process for updates your data assets, so you can ensure quality updates.

## What are workflows?

Workflows are automated processes that are made up of connectors that contain a common set of pre-established actions and are run when specified operations occur in your data catalog.

[![Screenshot of an example data access workflow.](../media/concept-workflows/data-access-workflow-inline.png)](../media/concept-workflows/data-access-workflow.png#lightbox)

For example: A user attempts to delete a business glossary term that is bound to a workflow. When the user submits this operation, the workflow runs through its actions instead of, or before, the original delete operation.

Workflow actions include things like generating approval requests or sending a notification, that allow users to automate validation and notification systems across their organization.

Currently, there are two kinds of workflows:

- **Data governance** - for data policy, access governance, and loss prevention. Scoped at the collection level.
- **Data catalog** - to manage approvals for CUD (create, update, delete) operations for glossary terms. Scoped at the glossary level.

These workflows can be built from pre-established workflow templates provided in the Microsoft Purview governance portal, but are fully customizable using the available workflow connectors.

## Workflow templates

For all the different types of user defined workflows enabled and available for your use, Microsoft Purview provides templates to help workflow administrators create workflows without needing to build them from scratch. The templates are built into the authoring experience and automatically populate based on the workflow being created, so there's no need to search for them.

Templates are available to launch the workflow authoring experience. However, a workflow admin can customize the template to meet the requirements in their organization.

![Screenshot of data catalog workflow templates, as an example of available templates.](../media/concept-workflows/template-example.png)

## Workflow connectors

Workflow connectors are a common set of actions applicable across some workflows. They can be used in any workflow in Microsoft Purview to create processes customized to your organization. To view the list of existing workflow connectors in Microsoft Purview, see [the workflow connectors documentation.](../how-to-use-workflow-connectors).

## Workflow scope

Once a workflow is created and enabled, it can be bound to a particular scope. This gives you the flexibility to run different workflows for different areas/departments in your organization.

![Screenshot of data catalog scope application, showing a single collection and its subcollections selected.](../media/concept-workflows/scope-example.png)

Data governance workflows are scoped to collections, and can be bound to the root collection to govern the whole Microsoft Purview catalog, or any subcollection.

Data catalog workflows are scoped to the glossary and can be bound to the entire glossary, any single term, or any parent term to manage child-terms.

If there's no workflow directly associated with a scope, the workflow engine will traverse upward in the scope hierarchy to determine closest workflow, and run that workflow for the operation.

For example, the AdatumCorp Purview account has the following collection hierarchy:

Root Collection &gt; Sales | Finance | Marketing

- **Root collection** has the workflow *Self-Service data access default* defined and bound.
- **Sales** has *Self-Service data access for sales* defined and bound.
- **Finance** has *Self-Service data access for finance* defined and bound.
- **Marketing** has no workflows directly bound.

[![Chart of how workflows apply through collections, showing a root collection workflow applying to all other collections.](../media/concept-workflows/workflow-scope-application.png)](../media/concept-workflows/workflow-scope-application.png#lightbox)

When an access request is made for a data asset in Finance collection, the *Self-Service data access for finance collection* workflow is run.

However, when a request access is made for a data asset in Marketing collection, *Self-Service data access default workflow* is triggered. Because there are no workflows bound at the Marketing scope, the workflow engine traverses to the next level in the scope hierarchy, which is Marketing's parent: the root collection. The workflow at the parent scope, the root collection scope, is run.

## Who can manage workflows?

A new role, **Workflow Admin** is being introduced with workflow functionality.

A Workflow admin defined for a collection can create self-service workflows and bind these workflows to the collections they have access to.

A Workflow admin defined for any collection can create approval workflows for the business glossary. In order to bind the glossary workflows to a term you need to have at least [Data reader permissions](../data-gov-classic-permissions).