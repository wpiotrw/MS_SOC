---
layout: Conceptual
title: Business continuity and disaster recovery with Windows 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/business-continuity-disaster-recovery
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn about business continuity and disaster recovery with Windows 365
author: aradinger
ms.author: aradinger
manager: olivchen
ms.date: 2026-03-11T00:00:00.0000000Z
ms.topic: overview
ms.service: windows-365
ms.subservice: windows-365-business
ms.localizationpriority: high
ms.reviewer: cawerner
ms.suite: ems
search.appverid: MET150
ms.custom: intune-azure; get-started
ms.collection:
- M365-identity-device-management
- tier1
locale: en-us
document_id: 2da47378-11f5-89e1-2209-aa2f93ec5ffe
document_version_independent_id: 2da47378-11f5-89e1-2209-aa2f93ec5ffe
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/business-continuity-disaster-recovery.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: business-continuity-disaster-recovery
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/business-continuity-disaster-recovery.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: a4d76388-da57-36aa-f9e7-fd47bfaa5cf0
---

# Business continuity and disaster recovery with Windows 365 | Microsoft Learn

Windows 365 provides highly resilient user cloud pcs, including:

- 99.9% highly available Windows 365 Cloud PC user sessions as defined in the [Windows 365 SLA](https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services).
- Disk storage with data object resiliency of 11 9s.
- Automated in-zone disaster recovery for compute.
- Recovery Point Objective (RPO) of ~0.

Windows 365 is part of Microsoft 365 and seamlessly uses Windows and Microsoft 365 solutions, features, and tools. This integration helps to make sure that user data and user context are portable and resilient. Important optional Windows and Microsoft 365 solutions include:

- OneDrive
- OneDrive for Business
- OneDrive Known Folder Move
- Windows Sync Your Settings
- Enterprise State Roaming

Using these Windows and Microsoft 365 solutions preserves user context and user data in cases when an individual Cloud PC has a non-Azure failure. These failures, like a failed OS update or user configuration errors, can result in an inaccessible Cloud PC, even if the underlying system is healthy. When using Windows 365 with these solutions, you can enjoy highly resilient and portable user data and user context, even if a specific Cloud PC must be reprovisioned from a base image.

## Data Resilience

If there's a larger disruption, like a full zone or region outage, the disk storage provided makes sure that data objects on the Cloud PC OS disks are 99.999999999% resilient against data loss, over a given year.

## Automated in-zone Disaster Recovery for Compute

Although rare, in-zone failures may disrupt Cloud PC operations. Examples of such failures include:

- vNic failure
- compute failure
- storage plane failure
- compute power failure

Azure automatically identifies compute failures and automatically moves the user workload to another resource in the zone.

If a user is actively using a session, there may be a slight disruption to the user while the service is restored. After restoration, the user must restore the connection by signing into their Cloud PC session again. If an in-zone failure occurs while the user is signed in and actively using their Cloud PC session, the user loses access until the system is restored.

Storage systems are separate from compute functions, and use storage redundancy to help deliver Windows 365 disaster recovery with an RPO of ~0. Automated Windows 365 disaster recovery is based on an up-to-date copy of the OS disk, with an RPO of ~0. Therefore, the process of recovery starts automatically because there's no need to accept the data loss associated with a past point-in-time recovery.

## In‑region resiliency and recovery

Windows 365 provides built‑in resiliency within an Azure region, but it does not protect against a full regional outage unless Cross‑Region Disaster Recovery is enabled. If an entire Azure region becomes unavailable and Cross‑Region Disaster Recovery is not configured, users won’t be able to access their Cloud PCs until the region is restored and healthy again.

Within a region, Cloud PCs are protected by point‑in‑time snapshots, which are distributed across all availability zones in that region. If a single availability zone is unavailable while the region itself remains healthy, an admin can manually restore a Cloud PC from a snapshot into another availability zone within the same region to bring users back online. This restore action is manual, not automatic, and depends on available capacity at the time of restore.

Recovery time for an in‑region restore is up to 4 hours (RTO). The amount of data that may be lost depends on the snapshot schedule (RPO), which is configurable and ranges from a minimum of 4 hours to a maximum of 24 hours.

For protection against full regional outages and faster, more predictable recovery across regions, Cross‑Region Disaster Recovery or Disaster Recovery Plus should be used.

## OneDrive, OneDrive for Business and OneDrive with Known Folder Move

Using Windows 365 with OneDrive and OneDrive Known Folder Move organizations provides these benefits:

- [Portable user data access](/en-us/onedrive/plan-onedrive-enterprise) across all physical and Cloud PCs.
- [Active/Active cross region user data resilience](/en-us/compliance/assurance/assurance-sharepoint-onedrive-data-resiliency) shared between Cloud PCs and all other authenticated use workspaces.
- User context portability and cross-region resilience using [Known Folder Move](/en-us/onedrive/redirect-known-folders).
- User data and Known Folder Move based context resilience with an [Recovery Time Objective (RTO) and RPO of 0](/en-us/compliance/assurance/assurance-sharepoint-onedrive-data-resiliency#blob-storage-resilience).
- Data [Versioning, corruption and accidental delete protection, and Point in Time Restore](/en-us/compliance/assurance/assurance-sharepoint-onedrive-data-resiliency#versioning-and-files-restore).

For more information on deploying and managing OneDrive for Small business, Medium-sized business, and Enterprises, see [this article](/en-us/onedrive/plan-onedrive-enterprise#deployment-and-management-options).

## Windows Sync Your Settings and Enterprise State Roaming

Both Windows base [Sync your Settings](https://support.microsoft.com/windows/about-sync-settings-on-windows-10-devices-deebcba2-5bc0-4e63-279a-329926955708) and [Enterprise State Roaming](/en-us/azure/active-directory/devices/enterprise-state-roaming-windows-settings-reference) retain Windows client user settings for portability and/or resilience (back up). To understand the differences between Sync your Settings and Enterprise State Roaming, see [What is enterprise state roaming?](/en-us/azure/active-directory/devices/enterprise-state-roaming-overview)

For an overview of Windows Settings, see [Windows Settings overview](/en-us/azure/active-directory/devices/enterprise-state-roaming-windows-settings-reference#windows-settings-overview) section of the Enterprise State Roaming document. To understand setting details such as grouping and applicability, see [Windows Settings details](/en-us/azure/active-directory/devices/enterprise-state-roaming-windows-settings-reference#windows-settings-details) in the Enterprise State Roaming document.

## Cloud PC Management Service

The Cloud PC management service includes:

- [Microsoft Intune admin center](https://go.microsoft.com/fwlink/?linkid=2109431)
- [Cloud PC end user portal](https://Windows365.microsoft.com)

The Cloud PC Management Service has a regionally redundant architecture that is designed to be highly available, with a target uptime of 99.99%. If there's a Management Service outage, the service has the following target objectives:

- RTO of &lt; 6 hours.
- RPO of &lt;30 minutes for changes made in the management service.

If there's a Management Service outage, assuming no other impacting outages, users won’t be able to access their Cloud PC sessions through the end user portal. Users can still access their Cloud PC instances by using any of the following options:

- a native app.
- directly from a bookmark for their Cloud PC session.
- https://rdweb.wvd.microsoft.com/webclient/index.html

## Summary

Windows 365 offers organizations with user workspaces that are:

- Highly available and backed by a financially guaranteed SLA.
- Automatically recovered if there's an in-zone Azure compute failure, with an expected RTO of &lt;10 minutes and an RPO of ~0.
- Automatic recovery, after the underlying regional or zone failure, with an RPO of ~0.

When organizations use Windows 365 with specified Windows and Microsoft 365 solutions and features, they enjoy:

- An even higher level of user data and user context resilience.
- Portable user data and user context.
- Active/Active data resilience providing ongoing access to user data, through OneDrive, even during a Windows 365 outage.

## Additional Windows 365 Service Resilience Resources

To learn more about how Microsoft designs and operates Windows 365 for high availability and continuity, explore these resources:

- [Learn about Windows 365 Service Resilience](enterprise/resilience)
- [Learn about Azure Virtual Desktop service architecture and resilience](/en-us/azure/virtual-desktop/service-architecture-resilience)
- [Learn about Windows 365 Connectivity Overview](enterprise/connectivity-overview)