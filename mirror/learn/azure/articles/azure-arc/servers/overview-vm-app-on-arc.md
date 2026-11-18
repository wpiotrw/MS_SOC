---
layout: Conceptual
title: VM Applications overview for Azure Arc-enabled servers (preview) - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/overview-vm-app-on-arc
breadcrumb_path: ../../breadcrumb/azure-management/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/146/azure-arc/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/5c778dec-0625-ec11-b6e6-000d3a4f0858
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
author: davidsmatlak
learn_banner_products:
- azure
ms.reviewer: davidsmatlak
ms.author: davidsmatlak
ms.service: azure-arc
ms.subservice: servers-azure-arc
description: Learn how to prepare, deploy, and manage VM Applications on Azure Arc-enabled servers.
ms.date: 2026-11-05T00:00:00.0000000Z
ms.topic: overview
ai-usage: ai-assisted
locale: en-us
document_id: f2108311-6c5a-10d4-3705-0e3a4532e0d5
document_version_independent_id: 11ff41d7-b09d-140e-4a16-ce9a1b0dd36e
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/overview-vm-app-on-arc.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/overview-vm-app-on-arc
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/overview-vm-app-on-arc.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: d0b61047-4820-6c6e-0774-db936eff56b5
---

# VM Applications overview for Azure Arc-enabled servers (preview) - Azure Arc | Microsoft Learn

VM Applications simplify application management for Azure Arc-enabled servers across on-premises, edge, and multicloud environments. You package applications once, publish them to Azure Compute Gallery, and deploy them to both Azure virtual machines (VMs) and Arc-enabled servers. For shared capabilities, gallery resource properties, limits, and costs, see [VM Applications overview](/en-us/azure/virtual-machines/vm-applications).

## How VM applications on Azure Arc-enabled servers work

VM Applications integrate with your existing development workflows and Azure infrastructure. Teams publish versioned application packages, scripts, and configurations to Azure Compute Gallery, then deploy or update them on Azure Arc-enabled servers. Use the Azure portal, command-line tools, APIs, or infrastructure as code, and automate publishing and rollout through your CI/CD pipelines.

After deployment, review application status and operation results for individual servers, or use Azure Resource Graph to track inventory across your fleet. Use Azure Policy to audit application requirements and deploy missing applications.

## Prepare and create a VM application

Follow the preparation and publishing instructions in [Create and deploy VM Application](/en-us/azure/virtual-machines/vm-applications-how-to). Ensure your package and commands are compatible with the target server's operating system and application dependencies.

1. **Set up Azure resources.** Create the storage account, blob container, and Azure Compute Gallery described in the [prerequisites](/en-us/azure/virtual-machines/vm-applications-how-to#prerequisites). For publishing without SAS tokens, see [Publish VM Applications using a managed identity](/en-us/azure/virtual-machines/vm-applications-publish-with-managed-identity).
2. **Prepare the package and commands.** Package your application, prepare an optional configuration file, and define installation and removal commands. See [Package the application](/en-us/azure/virtual-machines/vm-applications-how-to#package-the-application) for packaging requirements and script examples.
3. **Upload the application files.** Upload the package and optional configuration file, then obtain the blob URLs or read-only SAS URLs needed for publishing. See [Upload the application files to Azure storage account](/en-us/azure/virtual-machines/vm-applications-how-to#upload-the-application-files-to-azure-storage-account).
4. **Create the application definition and version.** Specify the supported operating system, package source, commands, and replication regions. Follow [Create the VM Application](/en-us/azure/virtual-machines/vm-applications-how-to#create-the-vm-application).

Replicate the application version to the Azure region associated with each target Arc-enabled server. After publishing and replication finish, follow [Deploy VM Applications on Arc-enabled servers](deploy-vm-app-on-arc).

## Deploy and manage applications on Arc-enabled servers

Arc-enabled servers require Azure Connected Machine agent version 1.69 or later and outbound access to the required Azure Storage endpoints. Arc-enabled Linux servers also require OpenSSL version 1.1.1 or later installed. Review the full [deployment prerequisites](deploy-vm-app-on-arc#prerequisites) before you deploy.

Use the Arc-specific guides for the rest of the application lifecycle:

- [Deploy VM Applications on Arc-enabled servers](deploy-vm-app-on-arc) for deployment commands and resource properties.
- [Manage VM Applications on Arc-enabled servers](manage-vm-app-on-arc) to review operation results, update a deployed application, or remove it.
- [Govern and monitor VM Applications on Arc-enabled servers](monitor-vm-app-on-arc) to inventory deployments with Azure Resource Graph and audit required applications with Azure Policy.