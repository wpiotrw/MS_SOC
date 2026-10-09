---
layout: Landing
title: Azure Blueprints documentation | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/blueprints/
summary: Simplify deployments by packaging artifacts, such as Azure Resource Manager templates, Azure role-based access control (Azure RBAC), and policies, in a single blueprint definition.
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/133/azure
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
adobe-target: true
description: Simplify deployments by packaging artifacts, such as Azure Resource Manager templates, Azure role-based access control (Azure RBAC), and policies, in a single blueprint definition.
ms.service: azure-blueprints
ms.topic: landing-page
author: kgremban
ms.author: kgremban
ms.date: 2020-08-27T00:00:00.0000000Z
locale: en-us
document_id: 6a648536-5a9b-ca8a-1074-552403d88e1b
document_version_independent_id: cd382efd-a17e-4b26-2475-16ef55c55c29
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/blueprints/index.yml
site_name: Docs
depot_name: Azure.azure-documents
page_type: landing
toc_rel: toc.json
asset_id: governance/blueprints/index
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/blueprints/index.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/40ba597f-f235-4787-be4d-fde8258e1045
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/4e834929-0ce1-4c1d-9c81-fcb14721edfb
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c4bc7fc-8fc8-4dea-bc53-680da859ef46
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/75670257-a3f0-4627-9981-8046f99219e6
platformId: fe8f4834-3fb1-d933-7581-20e0254f584b
---

# Azure Blueprints documentation

Simplify deployments by packaging artifacts, such as Azure Resource Manager templates, Azure role-based access control (Azure RBAC), and policies, in a single blueprint definition.

## About Azure Blueprints

### Overview

- [What is Azure Blueprints?](overview)
- [Stages of deployment](concepts/deployment-stages)
- [Lifecycle of a blueprint](concepts/lifecycle)

### video

- [Azure Friday - Azure Blueprints Overview](/en-us/Shows/Azure-Friday/An-overview-of-Azure-Blueprints)

## Get started

### Quickstart

- [Create a new blueprint (Portal)](create-blueprint-portal)
- [Create a new blueprint (Azure CLI)](create-blueprint-azurecli)
- [Create a new blueprint (Azure PowerShell)](create-blueprint-powershell)
- [Create a new blueprint (REST)](create-blueprint-rest-api)

### Tutorial

- [Use a blueprint sample](tutorials/create-from-sample)

### Deploy

- [Index of blueprint samples](samples/)

## Customize blueprints

### Concept

- [Dynamic parameters](concepts/parameters)
- [Sequence artifacts](concepts/sequencing-order)
- [Lock deployed resources](concepts/resource-locking)

### Tutorial

- [Protect new resources with locks](tutorials/protect-new-resources)

## Evolve to 'at scale'

### How-To Guide

- [Update existing blueprints](how-to/update-existing-assignments)
- [Manage assignments with PowerShell](how-to/manage-assignments-ps)
- [Import and export with PowerShell](how-to/import-export-ps)
- [Implement Blueprint Operators](how-to/configure-for-blueprint-operator)
- [Manage Blueprints as Code](https://github.com/Azure/azure-blueprints/blob/master/README.md)

## Get involved

### Get started

- [Microsoft Q&A for Azure Blueprints](/en-us/answers/topics/azure-blueprints.html)
- [Azure Governance YouTube channel](https://www.youtube.com/channel/UCZZ3-oMrVI5ssheMzaWC4uQ)
- [Request product feature](https://feedback.azure.com/d365community/forum/675ae472-f324-ec11-b6e6-000d3a4f0da0?c=775ae472-f324-ec11-b6e6-000d3a4f0da0)
- [Tech Community for Azure Governance](https://techcommunity.microsoft.com/category/azure/discussions/azuregovernance)

## Reference

### Reference

- [Blueprint specific functions](reference/blueprint-functions)
- [PowerShell module (PSGallery)](https://www.powershellgallery.com/packages/Az.Blueprint)
- [Azure CLI](/en-us/cli/azure/blueprint)
- [Azure PowerShell](/en-us/powershell/module/az.blueprint/#blueprint)
- [Azure SDK for .NET](/en-us/dotnet/api/microsoft.azure.management.blueprint)
- [REST](/en-us/rest/api/blueprints/)