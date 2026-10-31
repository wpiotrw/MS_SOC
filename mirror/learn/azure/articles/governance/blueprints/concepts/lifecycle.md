---
layout: Conceptual
title: Understand the lifecycle of a blueprint - Azure Blueprints | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/blueprints/concepts/lifecycle
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
description: Learn about the lifecycle that a blueprint definition goes through and details about each stage, including updating and removing blueprint assignments.
ms.date: 2023-09-07T00:00:00.0000000Z
ms.topic: concept-article
locale: en-us
document_id: 49c280c4-169c-a375-9242-87d5418f578b
document_version_independent_id: 904b3b7a-9c8a-97d8-a2c1-acdf8b84cca2
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/blueprints/concepts/lifecycle.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/blueprints/concepts/lifecycle
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/blueprints/concepts/lifecycle.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/40ba597f-f235-4787-be4d-fde8258e1045
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/4e834929-0ce1-4c1d-9c81-fcb14721edfb
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c4bc7fc-8fc8-4dea-bc53-680da859ef46
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/75670257-a3f0-4627-9981-8046f99219e6
platformId: 3ebd8fae-fce3-d759-757e-adb60cc66ca6
---

# Understand the lifecycle of a blueprint - Azure Blueprints | Microsoft Learn

Important

Azure Blueprints (Preview) will be **retired on January 31, 2027**, with a phased retirement that began July 31, 2026. Migrate your existing blueprint definitions and assignments to [Deployment Stacks](../../../azure-resource-manager/bicep/deployment-stacks) (recommended) and [Template Specs](../../../azure-resource-manager/bicep/template-specs). Blueprint artifacts are converted to ARM JSON templates or Bicep files used to define deployment stacks. For the full phased timeline, impact, and FAQ, see [Azure Blueprints retirement](../blueprint-retirement) or https://aka.ms/AzureBlueprintsRetirement. To learn how to author an artifact as an ARM resource, see:

- [Policy](/en-us/azure/templates/microsoft.authorization/policyassignments?pivots=deployment-language-bicep)
- [RBAC](/en-us/azure/templates/microsoft.authorization/roleassignments?pivots=deployment-language-bicep)
- [Deployments](/en-us/azure/templates/microsoft.resources/deployments?pivots=deployment-language-bicep)

Like many resources within Azure, a blueprint in Azure Blueprints has a typical and natural lifecycle. They're created, deployed, and finally deleted when no longer needed or relevant. Azure Blueprints supports standard lifecycle operations. It then builds upon them to provide additional levels of status that support common continuous integration and continuous deployment pipelines for organizations that manage their Infrastructure as Code - a key element in DevOps.

To fully understand a blueprint and the stages, we'll cover a standard lifecycle:

- Creating and editing a blueprint
- Publishing the blueprint
- Creating and editing a new version of the blueprint
- Publishing a new version of the blueprint
- Deleting a specific version of the blueprint
- Deleting the blueprint

## Creating and editing a blueprint

To create a blueprint, add artifacts to it, save the definition to the management group or subscription scope, and provide a unique name version. The blueprint is now in a **Draft** mode and can't yet be assigned. While in the **Draft** mode, it can continue to be updated and changed.

A never published blueprint in **Draft** mode displays a different icon on the **Blueprint Definitions** page than ones that have been **Published**. The **Latest Version** is displayed as **Draft** for these never published blueprints.

Create and edit a blueprint with the [Azure portal](../create-blueprint-portal#create-a-blueprint) or [REST API](../create-blueprint-rest-api#create-a-blueprint).

## Publishing a blueprint

Once all planned changes have been made to a blueprint in **Draft** mode, it can be **Published** and made available for assignment. The **Published** version of the blueprint can't be altered. Once **Published**, the blueprint displays with a different icon than **Draft** blueprints and displays the provided version number in the **Latest Version** column.

Publish a blueprint with the [Azure portal](../create-blueprint-portal#publish-a-blueprint) or [REST API](../create-blueprint-rest-api#publish-a-blueprint).

## Creating and editing a new version of the blueprint

A **Published** version of a blueprint can't be altered. However, a new version of the blueprint can be added to the existing blueprint and modified as needed. Make changes to an existing blueprint by editing it. When the new changes are saved, the blueprint now has **Unpublished Changes**. These changes are a new **Draft** version of the blueprint.

Edit a blueprint with the [Azure portal](../create-blueprint-portal#edit-a-blueprint).

## Publishing a new version of the blueprint

Each edited version of a blueprint must be **Published** before it can be assigned. When **Unpublished Changes** have been made to a blueprint but not **Published**, the **Publish Blueprint** button is available on the edit blueprint page. If the button isn't visible, the blueprint has already been **Published** and has no **Unpublished Changes**.

Note

A single blueprint can have multiple **Published** versions that can each be assigned to subscriptions.

To publish a blueprint with **Unpublished Changes**, use the same steps for publishing a new blueprint.

## Deleting a specific version of the blueprint

Each version of a blueprint is a unique object and can be individually **Published**. As such, each version of a blueprint can also be deleted. Deleting a version of a blueprint doesn't have any impact on other versions of that blueprint.

Note

It's not possible to delete a blueprint that has active assignments. Delete the assignments first and then delete the version you wish to remove.

1. Select **All services** in the left pane. Search for and select **Blueprints**.
2. Select **Blueprint definitions** from the page on the left and use the filter options to locate the blueprint you want to delete a version of. Select it to open the edit page.
3. Select the **Published versions** tab and locate the version you wish to delete.
4. Right-click on the version to delete and select **Delete this version**.

## Deleting the blueprint

The core blueprint can also be deleted. Deleting the core blueprint also deletes any blueprint versions of that blueprint, including both **Draft** and **Published** blueprints. As with deleting a version of a blueprint, deleting the core blueprint doesn't remove the existing assignments of any of the blueprint versions.

Note

It's not possible to delete a blueprint that has active assignments. Delete the assignments first and then delete the version you wish to remove.

Delete a blueprint with the [Azure portal](../create-blueprint-portal#delete-a-blueprint) or [REST API](../create-blueprint-rest-api#delete-a-blueprint).

## Assignments

There's several points during the lifecycle a blueprint can be assigned to a subscription. When the mode of a version of the blueprint is **Published**, then that version can be assigned to a subscription. This lifecycle enables versions of a blueprint to be used and actively assigned while a newer version is being developed.

As versions of blueprints are assigned, it's important to understand where they're assigned and with what parameters they've been assigned with. The parameters can either be static or dynamic. To learn more, see [static and dynamic parameters](parameters).

### Updating assignments

When a blueprint is assigned, the assignment can be updated. There are several reasons for updating an existing assignment, including:

- Add or remove [resource locking](resource-locking)
- Change the value of [dynamic parameters](parameters#dynamic-parameters)
- Upgrade the assignment to a newer **Published** version of the blueprint

To learn how, see [update existing assignments](../how-to/update-existing-assignments).

### Unassigning assignments

If the blueprint is no longer needed, it can be unassigned from the management group or subscription. During blueprint unassignment, the following occurs:

- Removal of [blueprint resource locking](resource-locking)
- Deletion of the blueprint assignment object
- (Conditional) If a **system-assigned managed identity** was used, it's also deleted

Note

All resources deployed by the blueprint assignment remain in place, but are no longer protected by Azure Blueprints.