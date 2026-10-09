---
layout: Conceptual
title: Enhance Microsoft Hosted Network (MHN) Cloud PC Resiliency with Multi-Region Selection | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/enhanced-resiliency-mhn
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Resiliency enhancements for MHN
author: swarnimsri
ms.author: srivastavasw
ms.service: windows-365
ms.topic: concept-article
ms.date: 2025-12-10T00:00:00.0000000Z
ms.subservice: windows-365-enterprise
locale: en-us
document_id: 218e5f6b-eb39-14d1-f8c3-ae3034161898
document_version_independent_id: 218e5f6b-eb39-14d1-f8c3-ae3034161898
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/enhanced-resiliency-mhn.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/enhanced-resiliency-mhn
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/enhanced-resiliency-mhn.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: a59ba523-4692-2940-9b72-0af840725b5e
---

# Enhance Microsoft Hosted Network (MHN) Cloud PC Resiliency with Multi-Region Selection | Microsoft Learn

## Overview

Microsoft Hosted Network with Automatic region selection is a core Windows 365 capability for intelligently managing Cloud PC network and region placement.

Starting December 2025, we are introducing a three-tier region selection experience and an enhanced deployment service that distributes your Cloud PCs across the maximum number of regions to improve resiliency while giving admins greater flexibility and control.

### The three tiers are:

#### Geography level [Recommended]

Selects all region groups and regions within a geography by default, offering the highest resiliency by enabling placement across the maximum number of regions.

> 
> *Example:* Choosing Europe allows new Cloud PCs to be distributed across all Azure region within Europe.

#### Region group level [new addition]

A region group typically maps to a specific geographical boundary (for example, US East, US West etc.). Selecting this level helps maintain data sovereignty when required, while also maximizing resiliency by distributing Cloud PCs across the regions within this Region group.

> 
> *Example:* To provision Cloud PCs in the Japan boundary, select the Japan region group.

#### Region level

Limits provisioning to one Azure region of your choice.

> 
> *Example:* To host Cloud PCs in Germany West Central only, select the Germany West Central region. You can also select multiple individual regions, i.e. France Central and Germany West Central. This model allows customers to balance compliance and resiliency needs—whether prioritizing sovereignty or maximizing availability.

Example of the three-tier provisioning experience:![Screenshot of Intune portal showing the region and region group options during the creation of a provision policy.](media/enhanced-resiliency-mhn/intune-portal-provisioning-select-region.png)

## Why is Microsoft Hosted Network with Geography the default recommendation?

- **Simplifies Cloud PC deployment:** As a true SaaS solution, Microsoft handles network and Cloud PC placement, so IT teams don’t need to manage their own network or pick individual regions.
- **Enhances resiliency:** By balancing Cloud PCs across the maximum number of Azure regions, it reduces the impact of regional outages as the Cloud PCs in the non-impacted regions are available.
- **Optimizes for success:** The service automatically selects the regions with the highest deployment success.
- **Consolidated region grouping:** More regions are included under each geography and categorized by region group, making it easier to select multiple regions and take full advantage of Microsoft Hosted Network. Region groupings are designed to ensure similar end-user latency, regardless of Cloud PC location. You can learn more about our new three-tier region grouping [here](requirements?tabs=enterprise,ent).

## Microsoft Hosted Network with multi-region selection makes your estate of Cloud PCs more resilient in three ways:

### Limiting impact of single-region outages through Cloud PC distribution

When your provisioning policy has multiple Azure regions selected, Windows 365 distributes Cloud PCs across all the selected regions. This means Cloud PCs aren’t concentrated in a single region. If one region experiences issues, only a fraction of users is affected, not your entire estate.

**Key details:**

- Starting December 2025, new Cloud PCs deployed under provisioning policies with multi-region selection distribute Cloud PCs across all selected regions, provided those regions are in optimal health at the time of provisioning. This distribution change applies only to provisioning policies using the Microsoft Hosted Network network type with multi-region selection. Customers who prefer a single region can continue to pin Cloud PCs to a specific Azure region by selecting it during provisioning policy configuration.
- Distribution of Cloud PCs across regions is achieved at the policy level; Cloud PCs region distribution in different policies is managed independently.
- Cloud PC distribution may vary across the selected regions. Distribution will evolve as more Cloud PCs are provisioned, new regions added, and region configuration updated.
- Our goal is to maximize distribution across all selected regions. However, some regions will not be considered during provisioning if the region is not in optimal health.

### Distributing snapshots for Cross-region disaster recovery (CRDR)

If customers opt for Microsoft Hosted Network with multi-region selection for CRDR configuration, their recovery snapshots are distributed across multiple regions instead of being concentrated in one region. So, if the disaster recovery region faces health issues during recovery, only Cloud PCs with snapshots in that region are affected. Remaining Cloud PCs can still recover from their respective regions.

- Snapshot distribution is configured separately in the User Settings, and the distribution happens at tenant level. You can learn more about CRDR [here](cross-region-disaster-recovery).
- Each Cloud PC has one backup snapshot that can be located in any of the eligible regions as chosen by customer in the CRDR configuration.

## Three Tiers of Region Selection: Benefits & Considerations

### Tier 1: Geography

*Example:* A multinational company selects the “Asia” geography for a provisioning policy that is assigned to all Cloud PC users across the continent. Cloud PCs are distributed across all Asian regions.

*Benefits:* Maximum resiliency and flexibility; largest number of regions covered for deployment; minimum Impact of single-region outage.

### Tier 2: Region Group

*Example:* A financial services firm located in Japan with strict data residency requirements selects the "Asia" geography and the "Japan" region group. Cloud PCs are distributed across all Azure regions in Japan.

*Benefits:* Ensures data remains within the selected boundary, while still gaining resiliency if multiple regions exist in the chosen region group. If only one region is available within the region group, resiliency is limited until more regions are supported.

### Tier 3: Specific Region

*Example:* A customer from Korea selects "Korea Central" only.

*Benefits:* Full control over where Cloud PCs are deployed.

*Tradeoff:* No cross-region distribution—if that region is affected, all Cloud PCs in that region are impacted.

## Nuances & Customer Controls

- **Data Residency:** Microsoft Hosted Network with multi-region selection always respects the customer’s selected geography, region group, or region for data residency.
- **Default selections during provisioning:** By default, all regions in the customer’s selected geography are opted-in when Microsoft Hosted Network is selected. Customers can uncheck region groups or regions to limit deployment.
- **Easy Rollback:** If you are not satisfied with your deployment approach, you can always revert by moving Cloud PCs with the Cloud PC Move feature. Learn more on how to move Cloud PCs [here](move-cloud-pc).
- **Future region expansion:** The *"Opt in for new region group and regions"* checkbox in the region selection blade adds flexibility to automatically add any future Azure regions that get supported by Windows365.
- **Layered resiliency approach:** These resiliency benefits with Microsoft Hosted Network are in addition to already existing Point-in-time recovery and our business continuity and disaster recovery solutions. Microsoft Hosted Network's resiliency benefits is designed to limit impact and is not a substitute for the Windows 365 Business Continuity and Disaster recovery solutions that provide a way to recover Cloud PCs. For mission-critical workloads, consider layering Microsoft Hosted Network's resiliency benefits with premium disaster recovery add-ons (like Cross-Region Disaster Recovery or Disaster Recovery Plus) for enterprise-grade continuity.
- **Updating grouping in existing provisioning policies:** Our updated three-tier grouping model does not require any changes to existing provisioning policies or Cloud PC migrations by administrators. Starting December 2025, existing policies automatically map to the same regions previously selected in the two-tier experience. The table below is provided to illustrate how legacy two-tier region selections map to the new three-tier grouping model:

Note

This table is not intended to be an authoritative list of supported regions or geographies. It is provided solely for configuration‑mapping guidance. Visit [requirements for Windows 365](requirements?tabs=enterprise,ent#supported-azure-regions-for-cloud-pc-provisioning) learn docs for the complete and up-to-date list of supported geographies, region groups, and regions.

| Old policy configuration (Geography with Region marked as Automatic) | Geography in new Policy Configuration | Region Group in new policy configuration |
| --- | --- | --- |
| Asia | Asia | Southeast Asia, East Asia |
| Australia | Australia & New Zealand (ANZ) | Australia, New Zealand |
| Canada | Canada | All |
| European Union | Europe | EU (North Europe, Sweden, West Europe, Poland, Italy, Spain, West Europe) |
| France | Europe | France |
| Germany | Europe | Germany |
| India | India | India |
| Norway | Europe | Norway |
| South Africa | Africa | South Africa |
| South Korea | Asia | South Korea |
| Switzerland | Europe | Switzerland |
| UAE | Middle East | UAE |
| United Kingdom | Europe | UK |
| US Central | US Central | US Central |
| US East | US East | US East |
| US West | US West | US West |
| South America | South America | Brazil |
| Qatar | Middle East | Qatar |
| Middle East | Middle East | Israel Central |
| Japan | Asia | Japan |
| Mexico | Mexico | Mexico |

## FAQs

### Is there a way to know which Cloud PC is provisioned exactly in which region?

Customers who want to identify the exact region where each Cloud PC is provisioned have a couple of options:

- **All Cloud PCs Blade:** The Region column (hidden by default) in the All Cloud PCs view displays the current deployment region of each Cloud PC. You can enable this column to surface the region information in the Intune portal.
- **Microsoft Graph API:** The *ListCloudPCs* API includes a *deviceRegionName* property in its response, which indicates the provisioning region for each Cloud PC.