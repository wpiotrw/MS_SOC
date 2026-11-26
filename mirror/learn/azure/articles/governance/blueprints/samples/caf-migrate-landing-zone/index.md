---
layout: Conceptual
title: CAF Migration landing zone blueprint sample overview - Azure Blueprints | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/governance/blueprints/samples/caf-migrate-landing-zone/
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
description: Overview and architecture of the CAF Migration landing zone blueprint sample, provided by the Microsoft Cloud Adoption Framework for Azure.
ms.date: 2023-09-07T00:00:00.0000000Z
ms.topic: sample
locale: en-us
document_id: 2067294d-9cd9-afff-57f0-f0c2c1fda6e7
document_version_independent_id: 1766fe6e-88a1-fa87-fa57-a24707c93e3b
original_content_git_url: https://github.com/MicrosoftDocs/azure-docs-pr/blob/live/articles/governance/blueprints/samples/caf-migrate-landing-zone/index.md
site_name: Docs
depot_name: Azure.azure-documents
page_type: conceptual
toc_rel: ../../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/Azure.azure-documents/{branchName}{pdfName}
asset_id: governance/blueprints/samples/caf-migrate-landing-zone/index
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/governance/blueprints/samples/caf-migrate-landing-zone/index.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/40ba597f-f235-4787-be4d-fde8258e1045
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/0c4bc7fc-8fc8-4dea-bc53-680da859ef46
platformId: 074111e5-e008-c05f-24fb-dbfe199f0ed6
---

# CAF Migration landing zone blueprint sample overview - Azure Blueprints | Microsoft Learn

Important

Azure Blueprints (Preview) will be **retired on January 31, 2027**, with a phased retirement that began July 31, 2026. Migrate your existing blueprint definitions and assignments to [Deployment Stacks](../../../../azure-resource-manager/bicep/deployment-stacks) (recommended) and [Template Specs](../../../../azure-resource-manager/bicep/template-specs). Blueprint artifacts are converted to ARM JSON templates or Bicep files used to define deployment stacks. For the full phased timeline, impact, and FAQ, see [Azure Blueprints retirement](../../blueprint-retirement) or https://aka.ms/AzureBlueprintsRetirement. To learn how to author an artifact as an ARM resource, see:

- [Policy](/en-us/azure/templates/microsoft.authorization/policyassignments?pivots=deployment-language-bicep)
- [RBAC](/en-us/azure/templates/microsoft.authorization/roleassignments?pivots=deployment-language-bicep)
- [Deployments](/en-us/azure/templates/microsoft.resources/deployments?pivots=deployment-language-bicep)

The CAF Migration landing zone blueprint (provided by the Microsoft Cloud Adoption Framework for Azure) is a set of infrastructure to help you set up for migrating your first workload and manage your cloud estate in alignment with the Cloud Adoption Framework.

The [CAF Foundation](../caf-foundation/) blueprint sample extends this sample.

## Architecture

The CAF Migration landing zone blueprint sample deploys foundation infrastructure resources in Azure that can be used by organizations to prepare their subscription for migrating virtual machines in to. It also helps put in place the governance controls necessary to manage their cloud estate. This sample will deploy and enforce resources, policies, and templates that will allow an organization to confidently get started with Azure.

![C A F Migration landing zone, image describes what gets installed as part of C A F guidance for initial landing zone.](../../media/caf-blueprints/caf-migration-landing-zone-architecture.png)

 Describes an Azure architecture which is achieved by deploying the C A F migration blueprint. It's applicable to a subscription with resource groups which consists of an Azure virtual network, storage account for storing logs, Log Analytics configured to store in the storage account. It also depicts Azure Key Vault configured and Azure Catalyst initial setup created. All these core infrastructures are accessed using Azure Active Directory.

This environment is composed of several Azure services used to provide a secure, fully monitored, enterprise-ready governance. This environment is composed of:

- An [Azure Key Vault](/en-us/azure/key-vault/general/overview) instance used to host secrets used for the Certificates, Keys, and Secrets deployed in the shared services environment
- Deploy [Log Analytics](/en-us/azure/azure-monitor/overview) is deployed to ensure all actions and services log to a central location from the moment you start your migration
- Deploy [Azure Virtual Network](../../../../virtual-network/virtual-networks-overview) providing an isolated network and subnets for your virtual machine.
- Deploy [Azure Catalyst Project](../../../../migrate/migrate-services-overview) for discovery and assessment. We're adding the tools for Server assessment, Server migration, Database assessment, and Database migration.

All these elements abide to the proven practices published in the [Azure Architecture Center - Reference Architectures](/en-us/azure/architecture/reference-architectures/).

Note

The CAF Migration blueprint lays out a landing zone for your workloads. You still need to perform the assessment and migration of your Virtual Machines / Databases on top of this foundational architecture.

For more information, see the [Microsoft Cloud Adoption Framework for Azure - Migrate](/en-us/azure/architecture/cloud-adoption/migrate/).