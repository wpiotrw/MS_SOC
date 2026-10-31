---
layout: Conceptual
title: Billing service for Windows Server pay-as-you-go - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/billing-windows-server-pay-go
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
description: Learn about billing services for Windows Server pay-as-you-go enabled by Azure Arc.
ms.date: 2026-10-30T00:00:00.0000000Z
ms.topic: concept-article
locale: en-us
document_id: f0298b84-9230-1226-1a7c-595dc5bd122d
document_version_independent_id: 91e3ccdf-e1cd-2c78-3ba4-9907520047c2
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/billing-windows-server-pay-go.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/billing-windows-server-pay-go
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/billing-windows-server-pay-go.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/fc3f72c2-fb6f-4cea-95ee-b444e52254ee
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f12cf087-582d-48ac-a085-0c19adf1e391
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: e20b992b-c4d4-ffb6-be59-239f9baac6f0
---

# Billing service for Windows Server pay-as-you-go - Azure Arc | Microsoft Learn

Machines must be onboarded to Azure Arc through the deployment of the [Azure Connected Machine agent](agent-overview). Azure Arc-enabled servers need to be in a connected state. Azure Arc-enabled servers don't support disconnected machines.

Windows Server pay-as-you-go enabled by Azure Arc supports both Windows Server 2025 Standard and Datacenter editions. Windows Server Datacenter and Standard editions are billed at the same rate for pay-as-you-go enabled by Azure Arc. There's no difference between virtual and physical machines from a billing perspective. Also, there's no minimum CPU core count per machine or per subscription, nor a fixed increment in which CPU cores are counted.

## Benefits

[Enrolling in Windows Server pay-as-you-go](/en-us/windows-server/get-started/windows-server-pay-as-you-go?tabs=gui%2Cazureportal) provides key server management capabilities. Customers benefit from the following management services at no extra cost:

- Azure Update Manager
- Azure Change Tracking and Inventory
- Azure Machine Configuration

Customers also benefit from access to the following management services:

- Windows Admin Center
- Windows Server Best Practices Assessment\*
- Windows Server Remote Support
- Windows Server Accelerated Networking
- Windows Server Disaster Recovery\*

For these services, extra costs may be incurred for compute, storage, and log ingestion.

## Trial period

When you install Windows Server 2025 Standard or Datacenter, onboard your machine to Azure Arc, and enable Windows Server pay-as-you-go, you receive a seven day trial period for the enrolled Azure Arc-enabled server. During this period, invoicing reflects a trial entity for the Azure Arc-enabled servers. At the end of the seven day trial window, billing automatically commences for the Azure Arc-enabled server.

## Changes in core counts

If you change the number of cores for your Azure Arc-enabled server enrolled in Windows Server pay-as-you-go, the billing service adjusts the costs within 24 hours.

For example, if you increase the number of cores from 16 to 32, then within 24 hours the charges will be for 32 cores instead of 16 cores. Alternatively, if you decrease the number of cores from 16 to 8, then within 24 hours the charges will be for 8 cores instead of 16 cores.

## Disenrollment and deletion

When you disenroll an Azure Arc-enabled server from Windows Server pay-as-you-go or if the Arc agent status is no longer `Connected`, billing stops within 24 hours. When you delete the Azure Arc-enabled server resource, billing stops within 48 hours.

## Resource moves

If you move the Azure Arc-enabled server between resource groups, subscriptions, or regions, billing continues. Resource moves across tenants aren't supported for Windows Server pay-as-you-go enabled by Azure Arc.