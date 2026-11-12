---
layout: Landing
title: Azure Policy documentation | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/policy/
summary: Azure Policy helps you manage and prevent IT issues with policy definitions that enforce rules and effects for your resources.
breadcrumb_path: /azure/bread/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/228/azure-policy
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
description: Azure Policy helps you manage and prevent IT issues with policy definitions that enforce rules and effects for your resources.
ms.service: azure-policy
ms.topic: landing-page
author: kgremban
ms.author: kgremban
ms.date: 2025-03-24T00:00:00.0000000Z
locale: en-us
document_id: 5cf12886-1874-b415-6ad8-5120b2828efa
document_version_independent_id: 4e0837d5-1b6e-7bc4-45ab-ee1b97600686
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/policy/index.yml
site_name: Docs
depot_name: Azure.azure-documents
page_type: landing
toc_rel: toc.json
asset_id: governance/policy/index
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/policy/index.yml
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/eea02214-631d-404a-92d1-5a3357c32a26
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/f42c31d7-eed9-43b7-9757-54caffb53cdc
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 836e3127-c7c7-48a0-2e5d-11d82e0f017b
---

# Azure Policy documentation

Azure Policy helps you manage and prevent IT issues with policy definitions that enforce rules and effects for your resources.

## About Azure Policy

### Overview

- [What is Azure Policy?](overview)
- [Policy effect](concepts/effect-basics)
- [Definition structure](concepts/definition-structure-basics)
- [Scope](concepts/scope)
- [Assignment structure](concepts/assignment-structure)
- [Exemption structure](concepts/exemption-structure)

### Architecture

- [Cloud Adoption Framework (Govern)](/en-us/azure/cloud-adoption-framework/govern/)
- [Enterprise-scale landing zones](/en-us/azure/cloud-adoption-framework/ready/enterprise-scale/)

## Get started

### Quickstart

- [Assign a policy (Azure portal)](assign-policy-portal)
- [Assign a policy (Azure CLI)](assign-policy-azurecli)
- [Assign a policy (Azure PowerShell)](assign-policy-powershell)
- [Assign a policy (REST)](assign-policy-rest-api)
- [Assign a policy (ARM template)](assign-policy-template)
- [Assign a policy (Bicep)](assign-policy-bicep)
- [Assign a policy (Terraform)](assign-policy-terraform)

### Tutorial

- [Create and manage policies](tutorials/create-and-manage)
- [Use VS Code extension](how-to/extension-for-vscode)
- [Design Azure Policy as Code workflows](concepts/policy-as-code)

### Deploy

- [Index of policy samples](/en-us/azure/governance/policy/samples/index)

## Author policies

### Tutorial

- [Create a custom policy](tutorials/create-custom-policy-definition)
- [Manage tag governance](tutorials/govern-tags)

### How-To Guide

- [Create policy with SDK](how-to/programmatically-create)
- [Author policies for arrays](how-to/author-policies-for-arrays)
- [Export resources](how-to/export-resources)

### Concept

- [Regulatory Compliance](concepts/regulatory-compliance)
- [Azure Policy for Kubernetes](concepts/policy-for-kubernetes)
- [Azure Machine Configuration](../machine-configuration/overview)

## Review & Remediate resources

### How-To Guide

- [Get compliance data](how-to/get-compliance-data)
- [Determine causes of non-compliance](how-to/determine-non-compliance)
- [Exempt resources](concepts/exemption-structure)
- [Remediate non-compliant resources](how-to/remediate-resources)

## Get involved

### Get started

- [Microsoft Q&A for Azure Policy](/en-us/answers/topics/azure-policy.html)
- [Azure Governance YouTube channel](https://www.youtube.com/channel/UCZZ3-oMrVI5ssheMzaWC4uQ)
- [Request product feature](https://feedback.azure.com/d365community/forum/675ae472-f324-ec11-b6e6-000d3a4f0da0?c=5b220886-f324-ec11-b6e6-000d3a4f0da0)
- [Tech Community for Azure Governance](https://techcommunity.microsoft.com/t5/Azure-Governance/bd-p/AzureGovernance)

## Reference

### Reference

- [Azure CLI](/en-us/cli/azure/policy)
- [Azure PowerShell (Policy)](/en-us/powershell/module/az.resources/#policy)
- [Azure PowerShell (Policy Insights)](/en-us/powershell/module/az.policyinsights#policy-insights)
- [REST](/en-us/rest/api/policy/)
- [Resource Manager templates](/en-us/azure/templates/microsoft.authorization/allversions)

## Reference (more)

### Reference

- [Azure SDK for .NET (Assignments)](/en-us/dotnet/api/microsoft.azure.management.resourcemanager.models.policyassignment)
- [Azure SDK for .NET (Policy Definitions)](/en-us/dotnet/api/microsoft.azure.management.resourcemanager.models.policydefinition)
- [Azure SDK for JavaScript (Policy)](/en-us/javascript/api/@azure/arm-policy)
- [Azure SDK for JavaScript (Policy Insights)](/en-us/javascript/api/@azure/arm-policyinsights)
- [Azure SDK for Python (Policy)](/en-us/python/api/azure-mgmt-resource/azure.mgmt.resource.policy)
- [Azure SDK for Python (Policy client)](/en-us/python/api/azure-mgmt-resource/azure.mgmt.resource.policyclient)
- [Azure SDK for Python (Policy Insights)](/en-us/python/api/azure-mgmt-policyinsights/azure.mgmt.policyinsights)