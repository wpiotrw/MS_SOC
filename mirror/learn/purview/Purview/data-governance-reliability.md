---
layout: Conceptual
title: Reliability in Microsoft Purview for Data Governance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-reliability
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: sidontha
ms.date: 2024-01-24T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
search.appverid:
- MET150
- MOE150
description: Learn how Microsoft Purview ensures reliability with zone redundancy, disaster recovery, and business continuity for resilient data governance.
locale: en-us
document_id: d4b19ef9-4c44-6945-cdbe-7d7ccb0fa22c
document_version_independent_id: d4b19ef9-4c44-6945-cdbe-7d7ccb0fa22c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-reliability.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-reliability
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-reliability.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 511936e8-c59b-e08f-ec43-6831307220f3
---

# Reliability in Microsoft Purview for Data Governance | Microsoft Learn

This article describes reliability support in Purview for governance experiences. It covers both regional resiliency with availability zones and disaster recovery and business continuity. For a more detailed overview of reliability principles in Microsoft Azure, see [Azure reliability](/en-us/azure/well-architected/reliability/).

## Availability zone support

[Availability zones](/en-us/azure/reliability/availability-zones-overview) are physically separate groups of datacenters within an Azure region. When one zone fails, services can fail over to one of the remaining zones.

Microsoft Purview makes commercially reasonable efforts to support zone-redundant availability zones, where resources automatically replicate across zones, without any need for you to set up or configure.

### Prerequisites

- Microsoft Purview governance experience currently provides partial availability zone support in a limited number of regions. This partial availability zone support covers experiences and certain functionalities within an experience.
- Zone availability might or might not be available for Microsoft Purview governance experiences or features and functionalities that are in preview.

### Supported regions

The table below lists availability zone support:

| Region | Microsoft Purview Data Map | Scan | Policy | Insights |
| --- | --- | --- | --- | --- |
| Southeast Asia |  | ✅ | ✅ | ✅ |
| East US |  | ✅ | ✅ | ✅ |
| Australia East | ✅ | ✅ | ✅ | ✅ |
| West US 2 |  | ✅ | ✅ | ✅ |
| Canada Central | ✅ | ✅ | ✅ | ✅ |
| Central India |  | ✅ |  | ✅ |
| East US 2 |  | ✅ | ✅ | ✅ |
| France Central |  | ✅ | ✅ | ✅ |
| Germany West Central |  | ✅ | ✅ | ✅ |
| Japan East |  | ✅ | ✅ | ✅ |
| Korea Central |  | ✅ | ✅ | ✅ |
| West US 3 |  | ✅ | ✅ | ✅ |
| North Europe |  | ✅ | ✅ | ✅ |
| South Africa North |  | ✅ | ✅ | ✅ |
| Sweden Central |  | ✅ | ✅ | ✅ |
| Switzerland North |  | ✅ |  |  |
| USGov Virginia | ✅ | ✅ | ✅ | ✅ |
| South Central US |  | ✅ | ✅ | ✅ |
| Brazil South |  | ✅ | ✅ | ✅ |
| UK South | ✅ | ✅ | ✅ | ✅ |
| Qatar Central |  | ✅ | ✅ | ✅ |
| China North 3 | ✅ | ✅ | ✅ | ✅ |
| West Europe |  | ✅ | ✅ | ✅ |

## Disaster recovery and business continuity

Disaster recovery refers to practices that organizations use to recover from events such as natural disasters or failed deployments that result in downtime and data loss. Regardless of the cause, the best remedy for a disaster is a well-defined and tested disaster recovery plan and an application design that actively supports disaster recovery. Before you start creating your disaster recovery plan, see [Recommendations for designing a disaster recovery strategy](/en-us/azure/well-architected/reliability/disaster-recovery).

For disaster recovery, Microsoft uses the [shared responsibility model](/en-us/azure/reliability/concept-shared-responsibility). In this model, Microsoft ensures that the baseline infrastructure and platform services are available. However, many Azure services don't automatically replicate data or fall back from a failed region to cross-replicate to another enabled region. For those services, you're responsible for setting up a disaster recovery plan that works for your workload. Most services that run on Azure platform as a service (PaaS) offerings provide features and guidance to support disaster recovery. Use [service-specific features to support fast recovery](/en-us/azure/reliability/reliability-guidance-overview) to help develop your disaster recovery plan.

Important

Classic Microsoft Purview doesn't support automated disaster recovery. You're responsible for backup and restore activities. You can manually create a secondary Purview account as a warm standby instance in another region. This standby instance in another region doesn't support Microsoft Purview data governance.

To implement disaster recovery for Microsoft Purview classic data governance, see [disaster recovery and migration best practices](data-gov-best-practices-disaster-recovery-migration).