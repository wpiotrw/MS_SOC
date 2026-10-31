---
layout: Conceptual
title: Microsoft Purview private endpoints best practices | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-best-practices-account-merge-private-endpoints
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2024-09-12T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-map
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Find best practices for Microsoft Purview private endpoints.
locale: en-us
document_id: 4555f0c5-da1e-e1ea-c431-66c04eac7bfc
document_version_independent_id: 4555f0c5-da1e-e1ea-c431-66c04eac7bfc
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-best-practices-account-merge-private-endpoints.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-best-practices-account-merge-private-endpoints
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-best-practices-account-merge-private-endpoints.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 0fe4fd82-be5b-52ba-7d5a-cea96f26d2ce
---

# Microsoft Purview private endpoints best practices | Microsoft Learn

## Background

The new Microsoft Purview experience is single, organization-wide instance of Microsoft Purview that's the next step towards unifying your organization's governance, policy, compliance, risk, and security. It's a prerequisite to a single platform used to manage and govern any data, both structured and unstructured, across your data estate. Including Azure, Microsoft 365, Azure, on-premises, or multicloud and SaaS applications in future. For organizations with multiple accounts, this upgrade process involves merging existing accounts.

When merging Microsoft Purview accounts, it's important to consider the private endpoints. Private endpoints provide a secure and private connection to the Purview governance portal and other resources, ensuring that only users within your network can access them. During the merge process, resources, configurations, and data governance policies from multiple accounts are consolidated into a single, unified account. If one or more of your classic accounts have private endpoint connections, this requires careful planning to ensure that private endpoints are correctly configured and that all necessary connections are maintained. Failure to properly manage private endpoints during the merge can result in issues and potential failure in merge process.

This article contains information to guide you resolve conflict when merging accounts with private endpoints.

## Private endpoints in Microsoft Purview accounts

Private endpoints in classic mode include the following capabilities:

- **Account private endpoints**: Allowed only client calls originating from within the private network to access the Microsoft Purview account.
- **Portal private endpoints**: Enabled secure access to the Microsoft Purview governance portal using private network connectivity.
- **Ingestion private endpoints**: Used to scan Azure IaaS and PaaS data sources inside Azure virtual networks and on-premises data sources through a private connection, to provide network isolation for metadata, flowing from data sources to the Microsoft Purview Data Map.

Private endpoints in unified experience include:

- **Platform private endpoints**: The Platform private endpoint is a new private endpoint concept in the unified portal that provides you organizational-level account private endpoint connection.
- **Ingestion private endpoints**: Used to scan Azure IaaS and PaaS data sources inside Azure virtual networks and on-premises data sources through a private connection.

## Private endpoints conflict resolution during account merge

After you [upgrade your primary account](data-governance-purview-portal#how-to-choose-a-primary-account) into unified experience, you may need to plan for account merge for the remaining classic accounts in your tenant. It's recommended to follow these guidelines to avoid conflicts during the merge process:

- Identify classic accounts that have any private endpoints, including accounts with Managed Vnet IRs. Remove unnecessary private endpoints, Managed VNet IR's or self-hosted integration runtimes from secondary accounts.
- If an account private endpoint is identified as a conflict and blocking the merge process, it's recommended to delete all private endpoints or filter them out during the merge process. The filtered configurations will not be merged into the unified experience.
- If there's a conflict in an ingestion private endpoint, the ingestion private endpoint in the secondary account can be abandoned. It's recommended to use the ingestion private endpoint in the primary account instead. If ingestion private endpoint is needed for a different VNet, you can create more ingestion private endpoints in the primary account. Create a new self-hosted integration runtime for full VNet isolation if needed.
- Portal private endpoint should be filtered out during the merge and be deleted in the secondary account after the merge, as portal private endpoint will be deprecated.

## Conflicts on integration runtime

- If you're using Managed VNet IR and self-hosted integration runtimes in both accounts, it's recommended to delete Managed VNet IR and self-hosted integration runtime in the secondary account before merge. Create new Managed VNet IR or self-hosted integration runtime in the primary account after the merge. Alternatively, filtering out Managed VNET IR and self-hosted integration runtime is recommended. Scans using these will be filtered out and will need to be recreated after the merge.
- If the plan is to use the same self-hosted integration runtime virtual machines, uninstall self-hosted integration runtime in the secondary account before merge and install self-hosted integration runtime in the primary account after merging the secondary account. It's possible to reuse the same VMs and machines or use new ones.

## Conflicts on managed private endpoint connections:

- Ensure Managed private endpoint connections to Platform private endpoint are properly set up in the primary account.
- Delete conflicting Managed VNet private endpoints from secondary accounts. After the merge, recreate or reuse existing Managed VNet IR in the primary account for connections to the sources that got merged.

## Conflicting Azure Data Factory or ADS Lineage Connections

- It's recommended to filter out Azure Data Factory and ADS lineage connections during the merge. Work with the primary account's domain source admins to reconnect it.