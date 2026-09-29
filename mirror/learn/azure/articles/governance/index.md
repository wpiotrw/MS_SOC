---
layout: Hub
title: Azure governance documentation | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/
summary: Get the most advanced set of governance capabilities of any major cloud provider.
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
description: Get the most advanced set of governance capabilities of any major cloud provider.
ms.service: azure-policy
ms.topic: hub-page
author: lauradolan
ms.author: ladolan
ms.date: 2025-03-24T00:00:00.0000000Z
ms.custom: build-2025
locale: en-us
document_id: 4f62ded8-96aa-c928-1b8b-2d45853b8c23
document_version_independent_id: aaae6207-08a2-900b-8e1e-34f36237b14b
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/index.yml
site_name: Docs
depot_name: Azure.azure-documents
page_type: hub
asset_id: governance/index
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/index.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/fd7d5d12-dbbc-4585-98a0-c6a0a5324f97
- https://authoring-docs-microsoft.poolparty.biz/devrel/eea02214-631d-404a-92d1-5a3357c32a26
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/298ced0f-48c4-410b-86eb-c2214b75cbdd
- https://authoring-docs-microsoft.poolparty.biz/devrel/f42c31d7-eed9-43b7-9757-54caffb53cdc
platformId: 7cf24de0-2b6e-d96b-8722-805c66635b0a
---

# Azure governance documentation

Get the most advanced set of governance capabilities of any major cloud provider.

![](/en-us/media/hubs/shared/icon-overview.svg?branch=main)

Overview
[Governance overview](management-groups/azure-management)

![](/en-us/media/hubs/shared/icon-video.svg?branch=main)

video
[Governance YouTube channel](https://www.youtube.com/channel/UCZZ3-oMrVI5ssheMzaWC4uQ)

![](/en-us/media/hubs/shared/icon-architecture.svg?branch=main)

Architecture
[Governance in the Cloud Adoption Framework](/en-us/azure/architecture/cloud-adoption/governance)

![](/en-us/media/hubs/shared/icon-training.svg?branch=main)

Training
[Build a cloud governance strategy on Azure](/en-us/training/modules/build-cloud-governance-strategy-azure/)

## Components and Services

![](media/management-groups.svg)
### Azure Management Groups

- [Overview](management-groups/overview)
- [Protect your resource hierarchy](management-groups/how-to/protect-resource-hierarchy)
- [See more &gt;](management-groups/)

![](media/service-groups.png)
### Azure Service Groups

- [Overview](service-groups/overview)
- [Create a service group using the REST API](service-groups/create-service-group-rest-api)
- [Add service groups members](service-groups/create-service-group-member-rest-api)
- [Manage Service Groups](service-groups/manage-service-groups)

![](media/azure-policy.svg)
### Azure Policy

- [Overview](policy/overview)
- [Azure Policy glossary](policy/policy-glossary)
- [Policy definition structure](policy/concepts/definition-structure-basics)
- [Azure Policy effect](policy/concepts/effect-basics)
- [See more &gt;](policy/)

![](media/azure-blueprints.svg)
### Azure Blueprints

- [Overview](blueprints/overview)
- [Protect resources](blueprints/tutorials/protect-new-resources)
- [See more &gt;](blueprints/)

![](media/azure-resource-graph.svg)
### Azure Resource Graph

- [Overview](resource-graph/overview)
- [Explore your Azure resources](resource-graph/concepts/explore-resources)
- [Track changes](resource-graph/how-to/get-resource-changes)
- [See more &gt;](resource-graph/)

![](media/cost-management.svg)
### Cost Management

- [Overview](../cost-management-billing/cost-management-billing-overview)
- [Manage AWS cost and usage](../cost-management-billing/costs/aws-integration-manage)
- [See more &gt;](../cost-management-billing/)

## Samples

Policy definitions, compliance blueprints, resource queries and more

![](media/azure-policy.svg)

[Azure Policy](/en-us/azure/governance/policy/samples/index)

![](media/azure-blueprints.svg)

[Azure Blueprints](blueprints/samples/)

![](media/azure-resource-graph.svg)

[Azure Resource Graph](resource-graph/samples/starter)

## Developer Resources

### Management Groups

- [Azure CLI](/en-us/cli/azure/account/management-group)
- [Azure PowerShell](/en-us/powershell/module/az.resources/#resources)
- [Azure SDK for .NET](/en-us/dotnet/api/overview/azure/management-groups)
- [Azure SDK for Go](https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/services/preview/resources/mgmt/2018-03-01-preview/managementgroups)
- [Azure SDK for JavaScript](/en-us/javascript/api/overview/azure/arm-managementgroups-readme)
- [Azure SDK for Python](/en-us/python/api/azure-mgmt-managementgroups/azure.mgmt.managementgroups)
- [REST](/en-us/rest/api/managementgroups)
- [Resource Manager templates](/en-us/azure/templates/microsoft.management/managementgroups)

### Azure Policy

- [Azure CLI](/en-us/cli/azure/policy)
- [Azure PowerShell](/en-us/powershell/module/az.resources/#policy)(Policy)
- [Azure PowerShell](/en-us/powershell/module/az.policyinsights#policy-insights)(Policy Insights)
- [Azure PowerShell](https://www.powershellgallery.com/packages/Az.GuestConfiguration)(Guest Configuration)
- [REST](/en-us/rest/api/policy/)(Policy)
- [REST](/en-us/rest/api/guestconfiguration/)(Guest Configuration)
- [Resource Manager templates](/en-us/azure/templates/microsoft.authorization/allversions)

### Azure Policy (more)

- [Azure SDK for .NET](/en-us/dotnet/api/microsoft.azure.management.resourcemanager.models.policyassignment)(Assignments)
- [Azure SDK for .NET](/en-us/dotnet/api/microsoft.azure.management.resourcemanager.models.policydefinition)(Policy Definitions)
- [Azure SDK for JavaScript](/en-us/javascript/api/@azure/arm-policy)(Policy)
- [Azure SDK for JavaScript](/en-us/javascript/api/@azure/arm-policyinsights)(Policy Insights)
- [Azure SDK for Python](/en-us/python/api/azure-mgmt-policyinsights/azure.mgmt.policyinsights)

### Azure Blueprints

- [Blueprint functions](blueprints/reference/blueprint-functions)
- [Azure CLI](/en-us/cli/azure/blueprint)
- [Azure PowerShell](/en-us/powershell/module/az.blueprint/#blueprint)
- [Azure PowerShell](https://www.powershellgallery.com/packages/Az.Blueprint)(PowerShell Gallery Module)
- [Azure SDK for .NET](/en-us/dotnet/api/overview/azure/blueprint)
- [REST](/en-us/rest/api/blueprints/)

### Azure Resource Graph

- [Azure CLI](/en-us/cli/azure/graph)
- [Azure PowerShell](/en-us/powershell/module/az.resourcegraph/#resourcegraph)
- [Azure SDK for .NET](/en-us/dotnet/api/azure.resourcemanager.resourcegraph)
- [Azure SDK for .NET](https://www.nuget.org/packages/Azure.ResourceManager.ResourceGraph/)(NuGet)
- [Azure SDK for Go](https://godoc.org/github.com/Azure/azure-sdk-for-go/services/resourcegraph/mgmt/2021-03-01/resourcegraph)
- [Azure SDK for Java](/en-us/java/api/com.azure.resourcemanager.resourcegraph)
- [Azure SDK for Java](https://central.sonatype.com/artifact/com.azure.resourcemanager/azure-resourcemanager-resourcegraph/1.0.0)(Maven)
- [Azure SDK for JavaScript](/en-us/javascript/api/@azure/arm-resourcegraph)
- [Azure SDK for Python](/en-us/python/api/azure-mgmt-resourcegraph/azure.mgmt.resourcegraph)
- [Azure SDK for Ruby](https://rubygems.org/gems/azure_mgmt_resourcegraph)(Gem)
- [REST](/en-us/rest/api/azure-resourcegraph/)
- [Resource Manager templates](/en-us/azure/templates/microsoft.resourcegraph/allversions)

### Cost Management

- [REST](/en-us/rest/api/cost-management)(Cost Management)
- [REST](/en-us/rest/api/consumption)(Consumption)
- [Resource Manager templates](/en-us/azure/templates/microsoft.consumption/budgets)

[UserVoice](https://feedback.azure.com/d365community/forum/675ae472-f324-ec11-b6e6-000d3a4f0da0) | [Microsoft Tech Community - Azure Governance](https://techcommunity.microsoft.com/t5/Azure-Governance/bd-p/AzureGovernance) | [Azure Support](https://azure.microsoft.com/support/create-ticket/)