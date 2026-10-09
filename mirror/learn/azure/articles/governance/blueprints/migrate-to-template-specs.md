---
layout: Conceptual
title: Migrate Azure Blueprints to template specs - Azure Blueprints | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/blueprints/migrate-to-template-specs
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
description: Step-by-step instructions to migrate Azure Blueprints definitions and artifacts to template specs, and deploy them with Azure Deployment Stacks before the Blueprints retirement.
ms.topic: how-to
ms.date: 2026-06-26T00:00:00.0000000Z
locale: en-us
document_id: 0b1b30cc-1a4c-56fd-f587-16f32d26115e
document_version_independent_id: 16b26657-cda7-ad69-b710-8b93cdba7c32
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/blueprints/migrate-to-template-specs.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/blueprints/migrate-to-template-specs
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/blueprints/migrate-to-template-specs.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/40ba597f-f235-4787-be4d-fde8258e1045
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/4e834929-0ce1-4c1d-9c81-fcb14721edfb
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c4bc7fc-8fc8-4dea-bc53-680da859ef46
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/75670257-a3f0-4627-9981-8046f99219e6
platformId: eba5ee2d-394d-4d4b-b9dc-649f2db14519
---

# Migrate Azure Blueprints to template specs - Azure Blueprints | Microsoft Learn

Azure Blueprints (Preview) is retired on **January 31, 2027**. This article shows how to migrate your blueprint definitions and artifacts into **template specs**, and how to deploy them with **Azure Deployment Stacks** so you keep versioning and deny-assignment protection. For the full phased timeline, see [Azure Blueprints retirement](blueprint-retirement).

A **template spec** is a resource type (`Microsoft.Resources/templateSpecs`) that stores an ARM template or Bicep file in your Azure environment so it can be versioned and shared across your organization. Template specs replace the *artifact storage and versioning* role that blueprint definitions provided. Deployment stacks replace the *assignment, lifecycle, and locking* role that blueprint assignments provided.

## Prerequisites

- Azure CLI or Azure PowerShell.
- Permission to read your existing blueprint definitions and to create template specs and deployment stacks at your target scope (subscription or management group).
- Owner or User Access Administrator on the target scope if you need to configure deny settings.

## Migration steps

1. **Export your blueprint definitions.** Export each blueprint definition (including its artifacts — Azure Policy assignments, role assignments, and ARM templates) to JSON. For more information, see [Export your blueprint definition](how-to/import-export-ps#export-your-blueprint-definition).

    Export everything you want to keep **before January 31, 2027**. After retirement, unexported definitions, versions, and assignments are deleted.
2. **Convert the exported artifacts into a single template.** Convert the exported JSON into a single ARM template or Bicep file. Map each blueprint artifact to its equivalent ARM resource:

    | Blueprint artifact | ARM/Bicep equivalent |
    | --- | --- |
    | Policy assignment | [`Microsoft.Authorization/policyAssignments`](/en-us/azure/templates/microsoft.authorization/policyassignments?pivots=deployment-language-bicep) |
    | Role assignment | [`Microsoft.Authorization/roleAssignments`](/en-us/azure/templates/microsoft.authorization/roleassignments?pivots=deployment-language-bicep) |
    | ARM template | A [module](../../azure-resource-manager/bicep/modules), nested template, or linked template |
    | Resource group | [`Microsoft.Resources/resourceGroups`](/en-us/azure/templates/microsoft.resources/resourcegroups?pivots=deployment-language-bicep) |

    Set the appropriate `targetScope` (for example, `subscription`) in your Bicep file to match the scope your blueprint assigned to.
3. **Publish the template as a template spec.** Create a template spec from your converted template. The template spec stores the template and a version in Azure. For more information, see [Azure Resource Manager template specs](../../azure-resource-manager/bicep/template-specs).

    Using Azure CLI:

    ```azurecli
    az ts create \
      --name blueprint-migration \
      --version 1.0.0 \
      --resource-group myResourceGroup \
      --location westus2 \
      --template-file ./main.bicep
    ```

    Using Azure PowerShell:

    ```azurepowershell
    New-AzTemplateSpec `
      -Name blueprint-migration `
      -Version 1.0.0 `
      -ResourceGroupName myResourceGroup `
      -Location westus2 `
      -TemplateFile ./main.bicep
    ```
4. **Deploy the template spec with a deployment stack.** Deploy the template spec through a deployment stack so you get lifecycle management and deny-assignment protection equivalent to blueprint locks. Reference the template spec by its resource ID. The `--deny-settings-mode` (`DenySettingsMode`) setting reproduces the **blueprint lock** behavior (`denyDelete` is similar to "Do Not Delete"; `denyWriteAndDelete` is similar to "Read Only"). For more information, see [Protect managed resources against deletion](../../azure-resource-manager/bicep/deployment-stacks#protect-managed-resources).

    Using Azure CLI:

    ```azurecli
    az stack sub create \
      --name blueprint-migration-stack \
      --location westus2 \
      --template-spec "/subscriptions/<subscriptionId>/resourceGroups/myResourceGroup/providers/Microsoft.Resources/templateSpecs/blueprint-migration/versions/1.0.0" \
      --deny-settings-mode denyDelete \
      --action-on-unmanage deleteResources
    ```

    Using Azure PowerShell:

    ```azurepowershell
    New-AzSubscriptionDeploymentStack `
      -Name blueprint-migration-stack `
      -Location westus2 `
      -TemplateSpecId "/subscriptions/<subscriptionId>/resourceGroups/myResourceGroup/providers/Microsoft.Resources/templateSpecs/blueprint-migration/versions/1.0.0" `
      -DenySettingsMode DenyDelete `
      -ActionOnUnmanage DeleteResources
    ```
5. **Verify and decommission the blueprint.**

    1. Confirm the deployment stack created the expected resources and that deny settings are applied.
    2. Confirm policy and role assignments are in place at the target scope.
    3. After you verify, remove the original blueprint assignment and definition (export first if you haven't already).

## When to use a Git repository instead

If your priority is source control and pull-request review rather than storing templates in Azure, you can keep your converted Bicep files in a **Git repository** and deploy them with deployment stacks directly from your pipeline. Template specs and Git repositories both provide versioning — choose template specs to share templates *within Azure* and Git to manage them *as code*.