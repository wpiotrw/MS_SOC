---
layout: Conceptual
title: Availability and recovery of Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/copilot-security-availability-recovery
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Find out about the availability and recovery of the Security Copilot service
ms.date: 2026-02-25T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: concept-article
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: 
ms.reviewer: 
locale: en-us
document_id: abaae7d5-b03f-f46c-361a-c37803430ec7
document_version_independent_id: abaae7d5-b03f-f46c-361a-c37803430ec7
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/copilot-security-availability-recovery.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: copilot-security-availability-recovery
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/copilot-security-availability-recovery.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 65138636-336a-12df-cfc1-f87bd84f346e
---

# Availability and recovery of Security Copilot | Microsoft Learn

This article describes the availability and recovery support in Microsoft Security Copilot experiences.

## Availability zone support

Azure availability zones are at least three physically separate groups of datacenters within each Azure region. Datacenters within each zone are equipped with independent power, cooling, and networking infrastructure. When a local zone fails, availability zones are designed so that if one zone is affected, regional services, capacity, and high availability are supported through the remaining two zones.

Failures can range from software and hardware failures to events such as earthquakes, floods, and fires. Tolerance for failures is achieved with redundancy and logical isolation of Azure services. For more detailed information on availability zones in Azure, see [Regions and availability zones](/en-us/azure/reliability/availability-zones-overview).

Security Copilot makes commercially reasonable efforts to use zone-redundant availability resources; underlying resources automatically replicate across zones, without any need for you to set up or configure.

Note

Availability zones protect service uptime; they don’t determine where prompts are processed.

### Availability zones

Availability zones are supported in various Geos as listed in the table:

| Geo | Copilot Sessions |
| --- | --- |
| ANZ | ![](media/yes-icon.svg) |
| Asia | ![](media/yes-icon.svg) |
| Brazil | ![](media/yes-icon.svg) |
| Canada | ![](media/yes-icon.svg) |
| Europe | ![](media/yes-icon.svg) |
| India | Not supported due to capacity constraints |
| Japan | ![](media/yes-icon.svg) |
| Qatar | ![](media/yes-icon.svg) |
| South Africa | ![](media/yes-icon.svg) |
| Switzerland | ![](media/yes-icon.svg) |
| UAE | Not supported due to capacity constraints |
| UK | ![](media/yes-icon.svg) |
| US | ![](media/yes-icon.svg) |

Note

Processing location is unrelated to high availability location. It is determined dynamically per-user traffic.

### Zonal outage recovery

During a zone-wide outage, no action is required during zone recovery. Copilots for Security capabilities in supported Geos self-heal and rebalance automatically to take advantage of the healthy zone. For more information, see [What are Azure availability zones?](/en-us/azure/reliability/availability-zones-overview?tabs=azure-cli).

## Disaster recovery and business continuity

Disaster recovery (DR) is about recovering from high-impact events, such as natural disasters or failed deployments that result in downtime and data loss. Regardless of the cause, the best remedy for a disaster is a well-defined and tested DR plan and an application design that actively supports DR. Before you begin to think about creating your disaster recovery plan, see [Recommendations for designing a disaster recovery strategy](/en-us/azure/well-architected/reliability/disaster-recovery).

When it comes to DR, Microsoft uses the [shared responsibility model](/en-us/azure/reliability/business-continuity-management-program#shared-responsibility-model). In a shared responsibility model, Microsoft ensures that the baseline infrastructure and platform services are available. At the same time, many Azure services don't automatically replicate data or fall back from a failed region to cross-replicate to another enabled region. There may be scenarios where a specific Geo does not support replication or services have system errors.

For Security Copilot, best effort is made to back up and restore your data if there is an outage. However, it's important to note that you should have a plan ready to deal with outages, even if it involves manual intervention. This means that you should have a disaster recovery plan in place that suits your workload.

Most services that run on Azure platform as a service (PaaS) offerings also provide features and guidance to support DR and you can use [service-specific features to support fast recovery](/en-us/azure/reliability/reliability-guidance-overview) to help develop your DR plan.

### Recovery time objective and Recovery point objective

The following table lists the supported geographies for Security Copilot. There is 72-hour Recovery Time Objective (RTO) and 15-minute Recovery Point Objective (RPO) commitment for regional outages within a geography. If a particular region experiences an outage, the RTO and RPO commitments are applied for that Geo.

| Geo | Copilot Sessions |
| --- | --- |
| ANZ | ![](media/yes-icon.svg) |
| Asia | Not replicated due to capacity constraints |
| Brazil | Not replicated due to capacity constraints |
| Canada | ![](media/yes-icon.svg) |
| Europe | ![](media/yes-icon.svg) |
| India | Not replicated due to capacity constraints |
| Japan | ![](media/yes-icon.svg) |
| Qatar | ![](media/yes-icon.svg) |
| South Africa | Not replicated due to capacity constraints |
| UAE | ![](media/yes-icon.svg) |
| UK | ![](media/yes-icon.svg) |
| US | ![](media/yes-icon.svg) |