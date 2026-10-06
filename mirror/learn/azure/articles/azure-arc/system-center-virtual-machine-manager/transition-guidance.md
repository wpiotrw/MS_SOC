---
layout: Conceptual
title: Retirement of the Azure Arc-enabled System Center Virtual Machine Manager - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/system-center-virtual-machine-manager/transition-guidance
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
author: Jeronika-MS
learn_banner_products:
- azure
ms.author: krkarthik
ms.service: azure-arc
description: This article provides transition guidance following the retirement of Azure Arc-enabled System Center Virtual Machine Manager.
ms.date: 2026-10-06T00:00:00.0000000Z
ms.topic: how-to
ms.services: azure-arc
ms.subservice: azure-arc-scvmm
keywords: VMM, Arc, Azure, System Center
locale: en-us
document_id: 4143711b-962d-602c-f563-357666dc7068
document_version_independent_id: 75879322-2c3c-c7a0-eccd-8512d170bb0b
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/system-center-virtual-machine-manager/transition-guidance.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/system-center-virtual-machine-manager/transition-guidance
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/system-center-virtual-machine-manager/transition-guidance.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://authoring-docs-microsoft.poolparty.biz/devrel/c89972e1-0a93-4ce3-b588-9c24d08ca424
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://authoring-docs-microsoft.poolparty.biz/devrel/b2144970-2aee-47fb-9df2-af491ca710ec
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: ae3a9395-3d96-a625-6b5b-55f5c0e2999a
---

# Retirement of the Azure Arc-enabled System Center Virtual Machine Manager - Azure Arc | Microsoft Learn

Azure Arc-enabled System Center Virtual Machine Manager (SCVMM) enables organizations to extend Azure management capabilities to virtual machines (VMs) managed through System Center Virtual Machine Manager. The service provided inventory visibility in Azure, VM lifecycle operations, self-service VM management through Azure role-based access control, at-scale Arc agent installation, and access to Azure security, governance, monitoring, update management, and automation services for virtual machines.

As part of Azure Arc product portfolio evolution, Azure Arc-enabled SCVMM is retiring. Transition to services that align with your long-term management and modernization requirements.

Important

Azure Arc-enabled System Center Virtual Machine Manager (SCVMM) retires in September 2029. Begin planning your transition to the preferred alternatives based on how you use the service today. All new onboardings stop by October 2026. For the existing customers i.e., Azure subscriptions with active Azure Arc-enabled SCVMM deployments, Azure Arc-enabled SCVMM will be available for use with all the current capabilities until September 2029. Customers should plan and complete the transition as early as possible to have sufficient lead time before retirement. Customers can share their feedback or any concerns that they may have during this transition through email to arc-vmm-feedback@microsoft.com.

### Which migration path should I choose?

| **Current usage** | **Recommended path** |
| --- | --- |
| You **ONLY** use Azure management services such as Update Manager, Defender for Cloud, Azure Monitor, Azure Policy, Guest Configuration, or licensing Extended Security Updates, Pay-as-you-go SQL and Windows Server and **DON'T** require Azure-based VM lifecycle management. | Azure Arc-enabled Servers |
| You **ONLY** use Azure to perform VM lifecycle operations such as create, start, stop, restart, resize, delete, or self-service VM provisioning. | Contact arc-vmm-feedback@microsoft.com |
| You use **BOTH** VM lifecycle operations and Azure management services. | Contact arc-vmm-feedback@microsoft.com |

## Transition to Azure Arc-enabled Servers (Option 1)

Azure Arc-enabled Servers provides guest operating system management regardless of the underlying virtualization platform. Azure Arc-enabled Servers doesn't provide virtualization-layer VM lifecycle operations. It's intended for Azure management services usage and license procurement on the VMs.

### High-level transition process

1. Identify the VMs currently onboarded to Azure services for patching, monitoring, security, etc. and enrolled for Azure-based licensing like Extended Security Updates (ESUs), Pay-as-you-go licensing through Azure Arc-enabled SCVMM.
2. Execute the Azure CLI command by scoping it to the machines individually or at a resource group or a subscription level. **The Azure CLI command will be updated here by November 2026**.
3. Validate connectivity between the machines and Azure Arc.
4. Verify policies, monitoring, updates, security, license billing, and compliance functionality.
5. Establish plans to Arc-onboard additional machines at-scale in the future, if any.
6. Remove your Azure Arc-enabled SCVMM resources gracefully from Azure. To deboard your SCVMM managed environment from Azure Arc-enabled SCVMM, follow [these steps](remove-scvmm-from-azure-arc).

## Contact arc-vmm-feedback@microsoft.com (Option 2)

If your organization uses Azure Arc-enabled SCVMM to perform VM lifecycle operations from Azure, Microsoft will work with you to identify an appropriate transition path. Because infrastructure, connectivity, and VM management requirements vary across organizations, there isn't a single replacement solution recommended for every Azure Arc-enabled SCVMM environment. Microsoft has transition options for both connected and disconnected scenarios.

Contact us at arc-vmm-feedback@microsoft.com to start your transition assessment. The Azure Arc-enabled SCVMM product team will review your current environment and requirements with you and provide guidance on the Microsoft option that best fits your scenario. We encourage you to start this assessment early to allow sufficient time to plan and complete your transition.

## Frequently asked questions

### What happens in September 2026?

In September **2026**, Microsoft announced that Azure Arc-enabled SCVMM retires in September **2029**. However, customers should transition to the recommended alternatives and avoid planning new deployments.

### Will I lose any of the existing functionalities of Azure Arc-enabled SCVMM?

No. The existing capabilities will be supported till September 2029 and if you are an existing customer, you can continue to use the service with no impact. However, Microsoft will not add new capabilities to Azure Arc-enabled SCVMM in the interim period. Customers are recommended to plan and switch to the recommended alternatives as early as possible.

### I'm planning to deploy Azure Arc-enabled SCVMM. Can I use the service until September 2029?

Microsoft won't add new capabilities to Azure Arc-enabled SCVMM. While the onboarding experience will be available for the existing customers, newer customers won't be able to deploy Azure Arc-enabled SCVMM starting from October 2026. Instead, evaluate Azure Arc-enabled Servers and Azure Local for your cloud-native VM management needs.

### Can I continue using System Center Virtual Machine Manager?

Yes. The retirement applies only to Azure Arc-enabled SCVMM. Customers can continue using their on-premises SCVMM product subject to the applicable System Center lifecycle and support policies for the versions.

### Will the Azure Arc agents on my VMs continue to work?

While the Azure Arc agents installed on the VMs continue to work, you need to use Azure CLI command to switch your Azure Arc-enabled SCVMM machines to Azure Arc-enabled Server machines. When done, remove the rest of the Azure Arc-enabled SCVMM resources by following the steps in [this article](remove-scvmm-from-azure-arc).