---
layout: Conceptual
title: Disaster Recovery for Microsoft Purview Data Map | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-map-disaster-recovery
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: pragyarathi
ms.date: 2026-07-20T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.custom: msecd-doc-authoring-1017
ms.localizationpriority: medium
ms.collection:
- tier2
search.appverid:
- MET150
- MOE150
description: Learn how to set up a manual disaster recovery (BCDR) environment for Microsoft Purview Data Map so you can keep governing data during a regional outage.
ai-usage: ai-assisted
locale: en-us
document_id: 2a3f6152-9e0a-8f53-c2ac-8fe493a19abf
document_version_independent_id: 2a3f6152-9e0a-8f53-c2ac-8fe493a19abf
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-map-disaster-recovery.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-map-disaster-recovery
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-map-disaster-recovery.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/f488294d-f483-456e-94e3-755f933b811b
- https://authoring-docs-microsoft.poolparty.biz/devrel/aebdc4a3-c54b-4eea-94e3-663d5e166f57
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/02662057-0b9b-40f4-a3c7-537125b6d283
- https://authoring-docs-microsoft.poolparty.biz/devrel/1baec8e6-ab38-4b56-bb59-f6282d94f311
platformId: ecce4c03-1189-f2c1-f1dd-7f1b68aa46b1
---

# Disaster Recovery for Microsoft Purview Data Map | Microsoft Learn

This article provides backup and recovery guidance for data governance admins who use [Microsoft Purview Data Map](data-map) in a production deployment. It covers manual business continuity and disaster recovery (BCDR) methods. Before you begin, review the prerequisites described first in this article. For detailed BCDR steps for Unified Catalog, see [Disaster recovery for Unified Catalog (manual)](unified-catalog-disaster-recovery).

## Prerequisites

### Step 1. Create an Enterprise tier account

Create a Purview Data Governance account at the **Enterprise** tier. This serves as the **primary account** with full governance capabilities.

### Step 2. Request Classic Purview provisioning in a secondary region

Create a support ticket through the Customer Support channel requesting enablement of Classic Purview account provisioning in a **secondary (paired) region** for BCDR purposes. This region shouldn't be the same as the primary region.

### Step 3. Create a Classic Purview account

After Classic provisioning is enabled in the secondary region, create a **Classic Purview account**. This account serves as the **secondary (backup) account** with limited capabilities.

Note

The first three steps are common to both Data Map and Unified Catalog BCDR.

### Step 4. Make note of MSI identities

Capture the primary account's managed identity object ID (Identity A) and the secondary account's managed identity object ID (Identity B).

### Step 5. Confirm Key Vault DR readiness

Make sure that either the secondary-region key vault holds the same secret names, or the key vault is geo-resilient with the paired secondary region.

### Step 6. Confirm data source DR readiness

Make sure that each data source that's registered and scanned in Microsoft Purview has source-side DR (geo-replication/RA-GRS, SQL failover group, and so on) that provides a reachable copy in or near the secondary region.

## Set up the secondary account and networking

Set up the secondary account to mirror the primary account, and then configure networking:

1. Recreate the collection hierarchy in the secondary account to match the primary account (same names).
2. Assign role-based access control (RBAC) roles on the secondary account collections (Collection Admin, Data Source Admin, Data Curator, Data Reader) to the same principals as the primary account.
3. Create the integration runtimes (IRs) in the secondary account (Managed virtual network (VNet) IR, Azure IR, or both) matching the primary account. Make sure the integration runtimes are present and **Running**.
4. If a self-hosted integration runtime (SHIR) is used, install a new SHIR node and register it against the secondary account by using the secondary account's authentication key.
5. Recreate the managed virtual network and managed private endpoints in the secondary region.
6. Approve each managed private endpoint on the target resource side.
7. Create private endpoints (account/portal/ingestion) and private DNS records for the secondary account.

## Configure identity and access on data sources

Grant the secondary account's identity the same access on each data source that the primary account's identity has:

1. For each data source, grant Identity B the same data-plane role that Identity A has (for example, Storage Blob Data Reader, SQL `db_datareader`, and so on).
2. Open the data source firewalls and network rules for the secondary account's integration runtime or account (IP ranges, service endpoints, private endpoints, **Allow trusted Microsoft services**). This access is required for the secondary account to reach the source over the network.
3. Register the key vault connection in the secondary account and grant Identity B get/list secret permission on the key vault. Use a DR-enabled or secondary-region key vault that holds the same secret names.

## Mirror scan configuration to the secondary account

Replicate the primary account's scan configuration in the secondary account:

1. Register the same data sources in the secondary account under the matching collections.
2. Create the same credentials in the secondary account (referencing the secondary account key vault connection and the same secret names).
3. Recreate custom classification rules in the secondary account (same names).
4. Recreate scan rulesets in the secondary account (system and custom) matching the primary account.
5. Create the same scans in the secondary account with matching scope selection, ruleset, and integration runtime binding.
6. Create the same triggers and schedules in the secondary account.

## Validate regularly

In the steady state, check the following for your primary and secondary accounts:

1. For manually triggered or scheduled scans in the secondary account, make sure each scan reaches the **Succeeded** state (not **Failed** or **Completed with error**).
2. Compare discovered asset counts between the primary and secondary accounts after both complete a scan of the same source. Counts and asset qualified names should match within one scan interval of each other.
3. Spot-check classifications applied by rulesets on the same assets in the primary and secondary accounts. The same classifications should be present in the secondary account.
4. Verify schema parity on a representative tabular asset. Column names and types should match.

## Fail over during a disaster recovery event

When a disaster recovery event occurs, create a support ticket requesting the following actions:

1. Promote the secondary (Classic) account to **Enterprise** tier.
2. Demote the primary (Enterprise) account to **Secondary**.

Share the tenant ID, account name, and region for both the primary and secondary accounts in the support ticket.

The failover completes, and the previously secondary account becomes the new primary with full Enterprise capabilities.

## Resolve common errors

| Symptom | Most likely cause | Fix |
| --- | --- | --- |
| Secondary account scan fails at authentication | Identity B isn't granted on the data source | Grant Identity B the data-plane role. |
| Secondary account scan fails with a network or timeout error | Data source firewall isn't opened for the secondary account, or the managed private endpoint isn't approved | Open the firewall or approve the managed private endpoint. |
| Credential **Test connection** fails in the secondary account | Key vault connection is missing, or Identity B lacks secret access | Register the key vault connection and grant secret get/list permission. |
| Assets present in the primary account but missing in the secondary account | Configuration drift — source or scan not mirrored | Mirror the configuration and run reconciliation. |
| Can't create the secondary account | Single instance per tenant, or Classic provisioning isn't enabled | Raise a support ticket. |